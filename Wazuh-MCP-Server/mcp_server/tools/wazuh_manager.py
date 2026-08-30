#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Wazuh Manager API tools - Manager API agents/rules/decoders/groups/cluster,
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
# Auto-extracted from wazuh_siem.py - Manager API surface (2026-08-11 - AUL Tunings)
class WazuhRulesInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    rule_id: Optional[str] = Field(default=None, max_length=16,
                                    description="Optional rule ID filter (comma-separated)")
    status: Optional[str] = Field(default=None,
                                   description="Filter by status: enabled, disabled, all")
    group: Optional[str] = Field(default=None, description="Filter by rule group")
    level: Optional[str] = Field(default=None,
                                  description="Filter by level range, e.g. '5-15'")
    pci_dss: Optional[str] = Field(default=None, description="PCI DSS requirement filter")
    gdpr: Optional[str] = Field(default=None, description="GDPR requirement filter")
    hipaa: Optional[str] = Field(default=None, description="HIPAA requirement filter")
    nist_800_53: Optional[str] = Field(default=None, description="NIST 800-53 requirement filter")
    mitre: Optional[str] = Field(default=None, description="MITRE technique ID filter")
    filename: Optional[str] = Field(default=None, description="Rule file name filter")
    search: Optional[str] = Field(default=None, max_length=128,
                                   description="Free-text search")
    select: Optional[str] = Field(default=None, max_length=256,
                                   description="Comma-separated field names to return")
    sort: Optional[str] = Field(default=None,
                                 description="Sort: +/-field, e.g. '-level'")
    q: Optional[str] = Field(default=None, max_length=256,
                              description="Lucene query string")
    distinct: bool = Field(default=False, description="Return distinct values only")
    limit: int = Field(default=50, ge=1, le=500)
    response_format: Literal["markdown", "json"] = Field(default="markdown")


@blueteam_tool(name="blueteam_wazuh_get_rules")
async def blueteam_wazuh_get_rules(params: WazuhRulesInput) -> str:
    api: dict[str, str] = {"limit": str(params.limit)}
    if params.rule_id:      api["rule_ids"] = params.rule_id.strip()
    if params.status:       api["status"] = params.status
    if params.group:        api["group"] = params.group
    if params.level:        api["level"] = params.level
    if params.pci_dss:      api["pci_dss"] = params.pci_dss
    if params.gdpr:         api["gdpr"] = params.gdpr
    if params.hipaa:        api["hipaa"] = params.hipaa
    if params.nist_800_53:  api["nist-800-53"] = params.nist_800_53
    if params.mitre:        api["mitre"] = params.mitre
    if params.filename:     api["filename"] = params.filename
    if params.search:       api["search"] = params.search
    if params.select:       api["select"] = params.select
    if params.sort:         api["sort"] = params.sort
    if params.q:            api["q"] = params.q
    if params.distinct:     api["distinct"] = "true"

    data = await _wazuh_api_get("/rules", api)
    items = data.get("data", {}).get("affected_items", [])
    if params.response_format == "json":
        return json.dumps({"count": len(items), "rules": items[:params.limit]}, indent=2)
    return "\n".join(
        [f"# Wazuh Rules ({len(items)})", ""]
        + [f"- `{r.get('id','?')}` (L{r.get('level','?')}): "
           f"{str(r.get('description',''))[:80]}"
           for r in items[:30]]
    )


# blueteam_wazuh_get_decoders
class WazuhDecodersInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    decoder_name: Optional[str] = Field(default=None, max_length=64)
    search: Optional[str] = Field(default=None, max_length=128)
    select: Optional[str] = Field(default=None, max_length=256)
    sort: Optional[str] = Field(default=None)
    q: Optional[str] = Field(default=None, max_length=256)
    distinct: bool = Field(default=False)
    limit: int = Field(default=50, ge=1, le=500)
    response_format: Literal["markdown", "json"] = Field(default="markdown")


@blueteam_tool(name="blueteam_wazuh_get_decoders")
async def blueteam_wazuh_get_decoders(params: WazuhDecodersInput) -> str:
    api: dict[str, str] = {"limit": str(params.limit)}
    if params.decoder_name: api["decoder_names"] = params.decoder_name.strip()
    if params.search:       api["search"] = params.search
    if params.select:       api["select"] = params.select
    if params.sort:         api["sort"] = params.sort
    if params.q:            api["q"] = params.q
    if params.distinct:     api["distinct"] = "true"

    data = await _wazuh_api_get("/decoders", api)
    items = data.get("data", {}).get("affected_items", [])
    if params.response_format == "json":
        return json.dumps({"count": len(items), "decoders": items[:params.limit]}, indent=2)
    return "\n".join(
        [f"# Wazuh Decoders ({len(items)})", ""]
        + [f"- `{d.get('name','?')}`: {str(d.get('details',''))[:60]}"
           for d in items[:30]]
    )


# blueteam_wazuh_get_groups
class WazuhGroupsInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    group_name: Optional[str] = Field(default=None, max_length=64)
    search: Optional[str] = Field(default=None, max_length=128)
    select: Optional[str] = Field(default=None, max_length=256)
    sort: Optional[str] = Field(default=None)
    q: Optional[str] = Field(default=None, max_length=256)
    distinct: bool = Field(default=False)
    response_format: Literal["markdown", "json"] = Field(default="markdown")


@blueteam_tool(name="blueteam_wazuh_get_groups")
async def blueteam_wazuh_get_groups(params: WazuhGroupsInput) -> str:
    api: dict[str, str] = {}
    if params.group_name: api["group_list"] = params.group_name.strip()
    if params.search:     api["search"] = params.search
    if params.select:     api["select"] = params.select
    if params.sort:       api["sort"] = params.sort
    if params.q:          api["q"] = params.q
    if params.distinct:   api["distinct"] = "true"

    data = await _wazuh_api_get("/groups", api)
    items = data.get("data", {}).get("affected_items", [])
    if params.response_format == "json":
        return json.dumps({"count": len(items), "groups": items}, indent=2)
    return "\n".join(
        [f"# Agent Groups ({len(items)})", ""]
        + [f"- `{g.get('name','?')}` ({g.get('count',0)} agents)"
           for g in items[:30]]
    )


# blueteam_wazuh_get_security_events
class WazuhSecurityEventsInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    search: Optional[str] = Field(default=None, max_length=128)
    select: Optional[str] = Field(default=None, max_length=256)
    sort: Optional[str] = Field(default="-timestamp")
    q: Optional[str] = Field(default=None, max_length=256)
    distinct: bool = Field(default=False)
    limit: int = Field(default=50, ge=1, le=500)
    response_format: Literal["markdown", "json"] = Field(default="markdown")


@blueteam_tool(name="blueteam_wazuh_get_security_events")
async def blueteam_wazuh_get_security_events(params: WazuhSecurityEventsInput) -> str:
    api: dict[str, str] = {"limit": str(min(params.limit, 500)),
                            "sort": params.sort or "-timestamp"}
    if params.search:   api["search"] = params.search
    if params.select:   api["select"] = params.select
    if params.q:        api["q"] = params.q
    if params.distinct: api["distinct"] = "true"

    data = await _wazuh_api_get("/security/events", api)
    items = data.get("data", {}).get("affected_items", [])
    if params.response_format == "json":
        return json.dumps({"count": len(items), "events": items[:params.limit]}, indent=2)
    return "\n".join(
        [f"# Security Events ({len(items)})", ""]
        + [f"- `[{str(e.get('timestamp','?'))[:19]}]` {e.get('user','?')}: "
           f"{str(e.get('action','?'))[:80]}"
           for e in items[:20]]
    )


# blueteam_wazuh_get_cluster_nodes
class WazuhClusterNodesInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    response_format: Literal["markdown", "json"] = Field(default="markdown")

@blueteam_tool(name="blueteam_wazuh_get_cluster_nodes")
async def blueteam_wazuh_get_cluster_nodes(params: WazuhClusterNodesInput) -> str:
    data = await _wazuh_api_get("/cluster/nodes")
    items = data.get("data", {}).get("affected_items", [])
    if params.response_format == "json":
        return json.dumps({"count": len(items), "nodes": items}, indent=2)
    return "\n".join(
        [f"# Cluster Nodes ({len(items)})", ""]
        + [f"- `{n.get('name','?')}` ({n.get('type','?')}) "
           f"v{n.get('version','?')} @ {n.get('ip','?')}"
           for n in items]
    )


# Resources
from mcp_server import mcp
from mcp_server.core.audit import _truncate_if_needed


@mcp.resource("wazuh://rules/taxonomy")
async def wazuh_rule_taxonomy() -> str:
    """Expose the current Wazuh rule taxonomy as an MCP resource."""
    if not WAZUH_API_URL or not WAZUH_API_PASSWORD:
        return json.dumps({"error": "WAZUH_API_URL and WAZUH_API_PASSWORD must be set."})
    from mcp_server.core.exceptions import BlueTeamMCPError
    try:
        data = await _wazuh_api_get("/rules", {"limit": "500", "sort": "-level"})
    except BlueTeamMCPError as e:
        return json.dumps({"error": str(e), "type": type(e).__name__})
    items = data.get("data", {}).get("affected_items", [])
    by_level: dict[int, int] = {}
    top_rules: list[dict] = []
    for r in items[:200]:
        lvl = r.get("level", 0)
        by_level[lvl] = by_level.get(lvl, 0) + 1
        top_rules.append({
            "id": r.get("id"), "level": lvl,
            "description": str(r.get("description", ""))[:80],
        })
    return json.dumps({
        "total_rules": len(items),
        "by_level": by_level,
        "top_rules": top_rules,
    }, indent=2)


@mcp.resource("wazuh://mitre/attack")
async def wazuh_mitre_attack() -> str:
    """Expose MITRE ATT&CK tactic-to-category mapping as an MCP resource."""
    return json.dumps({
        "description": "MITRE ATT&CK tactic → alert category mapping for Engine A/B correlation",
        "mapping": MITRE_TACTIC_TO_CATEGORY,
    }, indent=2)


# blueteam_wazuh_agents - filter parity with Wazuh Manager API
class WazuhAgentsInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    status: Optional[str] = Field(default=None,
                                   description="Filter: active, disconnected, never_connected, pending (comma-separated)")
    sort: Optional[str] = Field(default=None,
                                 description="Sort: +/-field, e.g. '-date_add'")
    search: Optional[str] = Field(default=None, max_length=128,
                                   description="Free-text search across agent name/ip")
    select: Optional[str] = Field(default=None, max_length=256,
                                   description="Comma-separated field names to return, e.g. 'id,name,ip,status'")
    q: Optional[str] = Field(default=None, max_length=256,
                              description="Lucene query string for advanced filtering")
    distinct: bool = Field(default=False,
                            description="Return distinct values only")
    limit: int = Field(default=100, ge=1, le=500)
    cursor: Optional[str] = Field(default=None,
                                   description="Opaque pagination cursor from previous response")


@blueteam_tool(name="blueteam_wazuh_agents")
async def blueteam_wazuh_agents(params: WazuhAgentsInput) -> str:
    """List Wazuh agents with full Manager API filter support and cursor pagination."""
    offset = 0
    if params.cursor:
        decoded = _decode_cursor(params.cursor)
        if decoded:
            offset = decoded.get("offset", 0)

    api: dict[str, str] = {
        "offset": str(offset),
        "limit": str(min(params.limit, 500)),
    }
    if params.status:   api["status"] = params.status
    if params.sort:     api["sort"] = params.sort
    if params.search:   api["search"] = params.search
    if params.select:   api["select"] = params.select
    if params.q:        api["q"] = params.q
    if params.distinct: api["distinct"] = "true"

    data = await _wazuh_api_get("/agents", api)
    agents = data.get("data", {}).get("affected_items", [])
    total = data.get("data", {}).get("total_affected_items", len(agents))
    next_cursor = _encode_cursor({"offset": offset + len(agents)}) if len(agents) >= params.limit else None
    return json.dumps({
        "total": total, "offset": offset, "limit": params.limit,
        "next_cursor": next_cursor, "agents": agents,
    }, indent=2)


# blueteam_wazuh_agents_summary
class WazuhAgentsSummaryInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    bypass_redaction: bool = Field(default=False, description="When true, skip PII/credential redaction")


@blueteam_tool(name="blueteam_wazuh_agents_summary")
async def blueteam_wazuh_agents_summary(params: WazuhAgentsSummaryInput) -> str:
    """Get Wazuh agent count by status.

    Args:
        params.bypass_redaction: When true, skip PII/credential redaction
    """
    data = await _wazuh_api_get("/agents/summary/status")
    return json.dumps(data.get("data", data), indent=2)


# blueteam_wazuh_manager_logs
class WazuhManagerLogsInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    log_type: str = Field(default="alerts", description="One of: alerts, ossec, cluster, auth, monitoring")
    search: Optional[str] = Field(default=None, max_length=128)
    sort: Optional[str] = Field(default=None)
    limit: int = Field(default=50, ge=1, le=500)
    cursor: Optional[str] = Field(default=None)


@blueteam_tool(name="blueteam_wazuh_manager_logs")
async def blueteam_wazuh_manager_logs(params: WazuhManagerLogsInput) -> str:
    """Fetch Wazuh manager logs with cursor pagination."""
    if params.log_type not in _WAZUH_LOG_TAG:
        return json.dumps({"error": f"log_type must be one of: {tuple(_WAZUH_LOG_TAG)}"})
    offset = 0
    if params.cursor:
        decoded = _decode_cursor(params.cursor)
        if decoded:
            offset = decoded.get("offset", 0)
    api: dict[str, str] = {
        "offset": str(offset),
        "limit": str(min(params.limit, 500)),
        "pretty": "true",
        "tag": _WAZUH_LOG_TAG[params.log_type],
    }
    if params.search: api["search"] = params.search
    if params.sort:   api["sort"] = params.sort

    data = await _wazuh_api_get("/manager/logs", api)
    items = data.get("data", {}).get("affected_items", data.get("data", []))
    if isinstance(items, dict):
        items = [items]
    total = data.get("data", {}).get("total_affected_items", len(items))
    next_cursor = _encode_cursor({"offset": offset + len(items)}) if len(items) >= params.limit else None
    return json.dumps({
        "total": total, "offset": offset, "limit": params.limit,
        "next_cursor": next_cursor, "logs": items,
    }, indent=2)


# Indexer tools + local alerts fallback (keep manual pattern for now
# these call _wazuh_indexer_post which still returns dicts, not exceptions)
