#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Wazuh Indexer query tools - Manager API agents/rules/decoders/groups/cluster,
Indexer alerts/search, MITRE resources, and local alerts fallback.

Manager API tools use @blueteam_tool for automatic audit logging, error handling (catching WazuhAuthError / WazuhAPIError),
and response truncation. Agent filtering now passes through Wazuh's native q/sort/select/search/status/distinct parameters.

NOTE: No ``from __future__ import annotations`` — deferred annotation
      evaluation (PEP 563) breaks the @blueteam_tool decorator's type
      resolution because the wrapper's __globals__ is tool_decorator.py.
"""

import json
from pathlib import Path
from typing import Optional, Literal
from pydantic import BaseModel, ConfigDict, Field
from mcp_server import (
    mcp,
    WAZUH_API_URL, WAZUH_API_PASSWORD,
    WAZUH_INDEXER_PASSWORD, WAZUH_INDEXER_URL,
)
from mcp_server.core.constants import (
    _WAZUH_ALERTS_MAX_LINES, MITRE_TACTIC_TO_CATEGORY,
    _WAZUH_LOG_TAG, _WAZUH_ALERTS_PATH,
)
from mcp_server.core.tool_decorator import blueteam_tool

from mcp_server.wazuh.auth import _wazuh_api_get
from mcp_server.wazuh.indexer import (
    _WAZUH_INDEX_PATTERNS, _encode_cursor, _decode_cursor,
)

# Manager API tools - all benefit from @blueteam_tool (audit + error + trunc)
# blueteam_wazuh_get_rules
# Indexer tools (remaining after Manager API split)
from mcp_server.core.audit import _audit_log, _truncate_if_needed
from mcp_server.core.redact import _redact_alert_data
from mcp_server.core.subprocess import _run_async


class WazuhAlertsInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    agent_name: Optional[str] = Field(default=None, max_length=256, description="Filter by agent name")
    srcip: Optional[str] = Field(default=None, max_length=45, description="Filter by source IP")
    since: Optional[str] = Field(default=None, max_length=24, description="Start time (ISO 8601 or relative like '24h')")
    until: Optional[str] = Field(default=None, max_length=24, description="End time (ISO 8601 or relative)")
    limit: int = Field(default=500, ge=1, le=2000, description="Max alerts to return")
    cursor: Optional[str] = Field(default=None, description="Pagination cursor from a previous response")
    bypass_redaction: bool = Field(default=False, description="When true, skip PII/credential redaction")
    redaction_policy: Optional[Literal["full", "protect_victim", "raw"]] = Field(default=None, description="Redaction policy")


@mcp.tool(
    name="blueteam_wazuh_alerts",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                  "idempotentHint": True, "openWorldHint": False}
)
async def blueteam_wazuh_alerts(params: WazuhAlertsInput) -> str:
    """Read Wazuh security alerts - local alerts.json first, auto-fallback to Indexer.

    Args:
        params.agent_name: Filter by agent name
        params.srcip: Filter by source IP
        params.since: Start time (ISO 8601 or relative like '24h')
        params.until: End time (ISO 8601 or relative)
        params.limit: Max alerts to return
        params.cursor: Pagination cursor
        params.bypass_redaction: When true, skip PII/credential redaction
        params.redaction_policy: 'full', 'protect_victim', or 'raw'
    """
    _audit_log("blueteam_wazuh_alerts", {})
    p = Path(_WAZUH_ALERTS_PATH)
    if not p.exists():
        from mcp_server.wazuh.indexer import _wazuh_indexer_post
        from mcp_server.wazuh.time_utils import _parse_time_window
        if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
            return json.dumps({
                "error": "WAZUH_INDEXER_URL and WAZUH_INDEXER_PASSWORD must be set. "
                         "Set these to enable automatic indexer fallback, "
                         "or use blueteam_wazuh_manager_logs."
            }, indent=2)
        search_after = None
        since_iso, until_iso = _parse_time_window(params.since or "24h", params.until)
        if params.cursor:
            decoded = _decode_cursor(params.cursor)
            if decoded:
                search_after = decoded.get("search_after")
        must = [{"range": {"@timestamp": {"gte": since_iso, "lt": until_iso,
                                           "format": "strict_date_optional_time"}}}]
        if params.agent_name:
            must.append({"match": {"agent.name": params.agent_name}})
        if params.srcip:
            must.append({"bool": {"should": [
                {"match": {"data.srcip": params.srcip}},
                {"match_phrase": {"full_log": params.srcip}},
            ], "minimum_should_match": 1}})
        body = {
            "size": min(params.limit, 2000),
            "sort": [{"@timestamp": {"order": "asc"}}],
            "query": {"bool": {"must": must}},
        }
        if search_after:
            body["search_after"] = search_after
        raw = await _wazuh_indexer_post(body)
        if "error" in raw:
            return json.dumps(raw, indent=2)
        hits = raw.get("hits", {})
        docs = [h.get("_source", h) for h in hits.get("hits", [])]
        next_cursor = None
        hit_list = hits.get("hits", [])
        if hit_list and len(docs) >= params.limit:
            last_sort = hit_list[-1].get("sort")
            if last_sort:
                next_cursor = _encode_cursor({"search_after": last_sort})
        return _truncate_if_needed(json.dumps({
            "source": "wazuh-indexer",
            "alerts": _redact_alert_data(docs, bypass=params.bypass_redaction,
                                          policy=params.redaction_policy),
            "count": len(docs),
            "next_cursor": next_cursor,
        }, indent=2))

    # Local alerts.json path
    skip = 0
    if params.cursor:
        decoded = _decode_cursor(params.cursor)
        if decoded:
            skip = decoded.get("scanned", 0)
    page = min((skip + params.limit) * 3, _WAZUH_ALERTS_MAX_LINES)
    r = await _run_async(["tail", "-n", str(page), _WAZUH_ALERTS_PATH])
    if r.get("returncode", 0) != 0:
        return json.dumps({"error": "Failed to read alerts",
                            "stderr": r.get("stderr", "")})
    alerts = []
    af = (params.agent_name or "").strip()
    ipf = (params.srcip or "").strip()
    scanned = 0
    for line in (r.get("stdout") or "").strip().splitlines():
        scanned += 1
        if scanned <= skip:
            continue
        if len(alerts) >= params.limit:
            break
        line = line.strip()
        if not line:
            continue
        try:
            a = json.loads(line)
            if af:
                ag = a.get("agent") or {}
                n = ag.get("name") or ag.get("id", "") if isinstance(ag, dict) else str(ag)
                if af.lower() not in (n or "").lower():
                    continue
            if ipf:
                ds = str(a.get("data", {}).get("srcip", ""))
                ds2 = str(a.get("data", {}).get("srcip2", ""))
                ts = str(a.get("srcip", ""))
                fl = str(a.get("full_log", ""))
                if ipf not in (ds, ds2, ts) and ipf not in fl:
                    continue
            alerts.append(a)
        except json.JSONDecodeError:
            continue
    next_cursor = _encode_cursor({"scanned": scanned}) if len(alerts) >= params.limit else None
    return _truncate_if_needed(json.dumps({
        "source": "local",
        "alerts": _redact_alert_data(alerts, bypass=params.bypass_redaction,
                                      policy=params.redaction_policy),
        "count": len(alerts),
        "next_cursor": next_cursor,
    }, indent=2))


class WazuhIndexerSearchInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    agent_name: Optional[str] = Field(default=None, max_length=256, description="Filter by agent name")
    srcip: Optional[str] = Field(default=None, max_length=45, description="Filter by source IP")
    since: Optional[str] = Field(default=None, max_length=24, description="Start time (ISO 8601 or relative like '24h')")
    until: Optional[str] = Field(default=None, max_length=24, description="End time (ISO 8601 or relative)")
    limit: int = Field(default=500, ge=1, le=10000, description="Max alerts per page")
    max_scanned: int = Field(default=0, ge=0, le=100000, description="When >0, auto-paginate up to this many documents")
    cursor: Optional[str] = Field(default=None, description="Pagination cursor from a previous response")
    keyword: Optional[str] = Field(default=None, max_length=256, description="Free-text keyword to narrow results")
    response_format: str = Field(default="json", description="'markdown' or 'json'")
    redaction_policy: Optional[Literal["full", "protect_victim", "raw"]] = Field(default=None, description="Redaction policy")
    reveal_owned: bool = Field(default=False, description="When true, unmask emails/subdomains at owned domains (BLUETEAM_OWNED_DOMAINS)")


@mcp.tool(
    name="blueteam_wazuh_indexer_search",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                  "idempotentHint": True, "openWorldHint": False}
)
async def blueteam_wazuh_indexer_search(params: WazuhIndexerSearchInput) -> str:
    """Query Wazuh Indexer (OpenSearch) for alerts/events with cursor pagination.

    Set ``params.max_scanned > 0`` for auto-pagination (server fetches up to N
    documents across multiple pages in a single call).

    Args:
        params.agent_name: Optional agent-name filter
        params.srcip: Optional source-IP filter
        params.since: ISO 8601 start in UTC (or relative like '24h')
        params.until: ISO 8601 end in UTC (or relative like 'now')
        params.limit: Max alerts per page (1-10000, default 500)
        params.max_scanned: When >0, auto-paginate across pages up to this many docs
        params.cursor: Pagination cursor from a previous response
        params.keyword: Free-text keyword to narrow results
        params.response_format: 'markdown' or 'json'
        params.redaction_policy: 'full', 'protect_victim', or 'raw'
        params.reveal_owned: When true, unmask emails/subdomains at owned domains (BLUETEAM_OWNED_DOMAINS)

    Returns:
        str: JSON with alerts, pagination cursor, and has_more flag.
    """
    _audit_log("blueteam_wazuh_indexer_search", {})
    from mcp_server.wazuh.indexer import (
        _wazuh_indexer_post, _KEYWORD_SEARCH_FIELDS,
    )
    from mcp_server.wazuh.time_utils import _parse_time_window

    if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
        return json.dumps({
            "error": "WAZUH_INDEXER_URL and WAZUH_INDEXER_PASSWORD must be set."
        }, indent=2)
    since_iso, until_iso = _parse_time_window(params.since, params.until)
    must: list[dict] = []
    if params.agent_name:
        must.append({"match": {"agent.name": params.agent_name}})
    if params.srcip:
        must.append({"bool": {"should": [
            {"match": {"data.srcip": params.srcip}},
            {"match": {"data.srcip2": params.srcip}},
            {"match": {"srcip": params.srcip}},
            {"match_phrase": {"full_log": params.srcip}},
        ], "minimum_should_match": 1}})
    must.append({"range": {"@timestamp": {
        "format": "strict_date_optional_time", "gte": since_iso, "lt": until_iso,
    }}})
    if params.keyword:
        parts = [
            f"{f}: ({params.keyword})^{b}" if b else f"{f}: ({params.keyword})"
            for f, b in _KEYWORD_SEARCH_FIELDS
        ]
        must.append({"query_string": {
            "query": " OR ".join(parts),
            "default_operator": "AND",
            "lenient": True,
        }})

    search_after = None
    if params.cursor:
        decoded = _decode_cursor(params.cursor)
        if decoded:
            search_after = decoded.get("search_after")

    all_docs: list[dict] = []
    total_scanned = 0
    total_val = 0
    total_relation = "eq"
    page_size = min(params.limit, 10000)
    _MAX_AUTO_SCAN = 100000
    effective_max = min(params.max_scanned, _MAX_AUTO_SCAN) if params.max_scanned > 0 else page_size

    while total_scanned < effective_max:
        body = {
            "size": min(page_size, effective_max - total_scanned),
            "sort": [{"@timestamp": {"order": "asc"}}, {"_id": "asc"}],
            "query": {"bool": {"must": must}} if must else {"match_all": {}},
        }
        if search_after:
            body["search_after"] = search_after
        raw = await _wazuh_indexer_post(body)
        if "error" in raw:
            if all_docs:
                break
            return json.dumps(raw, indent=2)
        hits = raw.get("hits", {})
        hit_list = hits.get("hits", [])
        docs = [h.get("_source", h) for h in hit_list]
        total = hits.get("total", {})
        total_val = total.get("value", 0) if isinstance(total, dict) else total
        total_relation = total.get("relation", "eq") if isinstance(total, dict) else "eq"
        if not docs:
            break
        all_docs.extend(docs)
        total_scanned += len(docs)
        last_sort = hit_list[-1].get("sort") if hit_list else None
        if len(docs) < page_size or last_sort is None:
            break
        search_after = last_sort

    next_cursor = (
        _encode_cursor({"search_after": search_after})
        if search_after and total_scanned < total_val
        else None
    )
    has_more = next_cursor is not None
    return _truncate_if_needed(json.dumps({
        "total": {"value": total_val, "relation": total_relation},
        "retrieved": total_scanned,
        "has_more": has_more,
        "next_cursor": next_cursor,
        "alerts": _redact_alert_data(all_docs, policy=params.redaction_policy, reveal_owned=params.reveal_owned),
    }, indent=2))


class MitreLookupInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    tactic_or_technique: str = Field(..., max_length=128, description="MITRE ATT&CK tactic or technique ID/name to look up")


# blueteam_mitre_lookup
@mcp.tool(
    name="blueteam_mitre_lookup",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                  "idempotentHint": True, "openWorldHint": False}
)
async def blueteam_mitre_lookup(params: MitreLookupInput) -> str:
    """Look up a MITRE ATT&CK tactic or technique in the local mapping.

    Args:
        params.tactic_or_technique: MITRE tactic or technique ID/name to look up
    """
    _audit_log("blueteam_mitre_lookup", {"query": params.tactic_or_technique})
    q = params.tactic_or_technique.strip().upper()
    results: dict[str, str] = {}
    for tactic, category in MITRE_TACTIC_TO_CATEGORY.items():
        if q in tactic.upper() or q in category.upper():
            results[tactic] = category
    if not results:
        return json.dumps({
            "query": params.tactic_or_technique,
            "result": "not_found",
            "available_tactics": list(MITRE_TACTIC_TO_CATEGORY.keys()),
        }, indent=2)
    return json.dumps({"query": params.tactic_or_technique, "matches": results}, indent=2)
