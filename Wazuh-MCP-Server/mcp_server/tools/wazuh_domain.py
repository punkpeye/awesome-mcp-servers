#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Wazuh domain lookup tool - search alerts by domain name
"""
from __future__ import annotations
import json, re
from typing import Optional, Literal
from collections import Counter
import httpx
from pydantic import BaseModel, ConfigDict, Field, field_validator
from mcp_server import (mcp, WAZUH_INDEXER_URL, WAZUH_INDEXER_PASSWORD,
                        _WAZUH_INDEXER_MAX_SIZE, _BYPASS_REDACTION_DESC, _REDACTION_POLICY_DESC, _REVEAL_OWNED_DESC, _FORENSIC_TOKEN_DESC,
                        _AGENT_NAME_DESC, _SINCE_DESC, _UNTIL_DESC,
                        RDAP_BASE_URL, CRTSH_BASE_URL)
from mcp_server.core.audit import _audit_log, _truncate_if_needed, _escape_md_table
from mcp_server.core.http_client import _api_call, _handle_api_error
from mcp_server.core.redact import _redact_alert_data
from mcp_server.wazuh.indexer import _wazuh_indexer_post, _WAZUH_INDEX_PATTERNS, _KEYWORD_SEARCH_FIELDS, _encode_cursor, _decode_cursor
from mcp_server.wazuh.time_utils import _parse_time_window
from mcp_server.core.validators import ValidAgentName, ValidKeyword

class WazuhDomainLookupInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    domain: str = Field(
        ...,
        max_length=253,
        description="Domain name to search for in Wazuh alerts "
                    "(e.g. 'tangerangkota.go.id', 'xxx.com').",
    )
    agent_name: ValidAgentName = Field(
        default=None,
        max_length=64,
        description=_AGENT_NAME_DESC,
    )
    since: Optional[str] = Field(
        default=None,
        max_length=30,
        description=_SINCE_DESC,
    )
    until: Optional[str] = Field(
        default=None,
        max_length=30,
        description=_UNTIL_DESC,
    )
    limit: int = Field(
        default=500,
        description="Max alerts per page.",
        ge=1,
        le=10000,
    )
    include_full_log: bool = Field(
        default=False,
        description="Include the full_log field in results. "
                    "The full_log field can be very large (100KB+ per alert). "
                    "Set to true only when you need the raw log line context.",
    )
    cursor: Optional[str] = Field(
        default=None,
        description="Pagination cursor from previous response (next_cursor).",
    )
    response_format: Literal["markdown", "json"] = Field(
        default="markdown",
        description="'markdown' for human readable summary, 'json' for structured data.",
    )
    keyword: ValidKeyword = Field(
        default=None,
        max_length=1024,
        description="Free-text keyword search to further narrow domain results. "
                    "Same syntax as blueteam_wazuh_indexer_search.",
    )
    max_scanned: Optional[int] = Field(
        default=None,
        ge=1000,
        le=500000,
        description="When set, auto-paginate through all matching alerts up to this limit. "
                    "Returns aggregated results (counts, top IPs, top rules) across ALL "
                    "scanned pages - no need to manually iterate with next_cursor."
                    "When None (default), returns a single page with next_cursor for"
                    "manual pagination. include_full_log is forced to False in this mode.",
    )
    bypass_redaction: bool = Field(
        default=False,
        description="Bypass PII redaction for audit investigations (Layer 1 credentials stay masked).",
    )
    redaction_policy: Optional[Literal["full", "protect_victim", "raw"]] = Field(
        default=None,
        description=_REDACTION_POLICY_DESC,
    )
    reveal_owned: bool = Field(default=False, description=_REVEAL_OWNED_DESC)
    forensic_token: Optional[str] = Field(default=None, max_length=128, description=_FORENSIC_TOKEN_DESC)

    @field_validator("domain")
    @classmethod
    def validate_domain(cls, v: str) -> str:
        if not v or len(v) > 253:
            raise ValueError("Invalid domain length (max 253)")
        if ".." in v:
            raise ValueError("Invalid domain format")
        v = v.strip().lower()
        if not re.match(
            r'^[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?'
            r'(\.[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*$',
            v,
        ):
            raise ValueError(
                "Invalid domain format - must be a valid domain name (e.g. example.com)"
            )
        return v


async def _wazuh_domain_lookup_full_scan(
    params: "WazuhDomainLookupInput",
    since_str: str,
    until_str: str,
    initial_search_after: Optional[list],
) -> str:
    """Auto-paginate through all matching alerts and return an aggregated summary.

    Uses the shared ``_full_scan_paginate`` loop internally.
    """
    async def _fetch_page(ps: int, sa):
        body = {
            "size": ps,
            "query": {"bool": {"filter": [
                {"range": {"@timestamp": {"gte": since_str, "lt": until_str,
                                               "format": "strict_date_optional_time"}}},
                {"query_string": {"query": f"data.domain: {params.domain}", "lenient": True}},
            ]}},
            "sort": [{"@timestamp": "asc"}, {"_id": "asc"}],
        }
        if params.agent_name:
            body["query"]["bool"]["filter"].append({"match": {"agent.name": params.agent_name}})
        if params.keyword:
            body["query"]["bool"]["filter"].append({"query_string": {"query": params.keyword, "lenient": True}})
        if sa:
            body["search_after"] = sa
        return await _wazuh_indexer_post(body)

    async def _full_scan_paginate(max_scanned, fetch_page, initial_sa, redact=True, bypass=False, reveal_owned=False):
        """Generic pagination loop. Returns {total_scanned, pages, exhausted, all_docs, ...}."""
        total_scanned = 0
        pages = []
        all_docs = []
        sa = initial_sa
        while total_scanned < max_scanned:
            page_size = min(1000, max_scanned - total_scanned)
            data = await fetch_page(page_size, sa)
            if "error" in data:
                return {"_error": data["error"], "total_scanned": total_scanned, "pages": pages}
            hits = data.get("hits", {})
            hit_list = hits.get("hits", [])
            docs = [h.get("_source", h) for h in hit_list]
            if redact:
                docs = _redact_alert_data(docs, bypass=bypass, reveal_owned=reveal_owned)
            if not docs:
                break
            total_scanned += len(docs)
            pages.append(docs)
            all_docs.extend(docs)
            last_sort = hit_list[-1].get("sort") if hit_list else None
            if len(docs) < page_size or last_sort is None:
                break
            sa = last_sort
        exhausted = total_scanned < max_scanned or (len(hit_list) if hit_list else 0) < page_size
        total_val = data.get("hits", {}).get("total", {}).get("value", total_scanned)
        total_relation = data.get("hits", {}).get("total", {}).get("relation", "eq")
        return {"total_scanned": total_scanned, "pages": pages, "exhausted": exhausted,
                "all_docs": all_docs, "sample_docs": all_docs[:10],
                "total_val": total_val, "total_relation": total_relation}

    result = await _full_scan_paginate(
        params.max_scanned, _fetch_page, initial_search_after, redact=True,
        bypass=params.bypass_redaction,
        reveal_owned=params.reveal_owned,
    )
    if result.get("_error"):
        return json.dumps({"error": result["_error"]}, indent=2)

    total_scanned = result["total_scanned"]
    pages = result["pages"]
    exhausted = result["exhausted"]
    global_total_val = result["total_val"]
    global_total_relation = result["total_relation"]
    all_docs = result["all_docs"]
    sample_docs = result["sample_docs"]

    # Accumulate counters from all scanned docs
    global_srcip_counter: Counter[str] = Counter()
    global_rule_group_counter: Counter[str] = Counter()
    global_rule_counter: Counter[str] = Counter()
    for doc in all_docs:
        ip = (doc.get("data") or {}).get("srcip", "")
        if ip:
            global_srcip_counter[ip] += 1
        rule = doc.get("rule") or {}
        for g in rule.get("groups", []):
            global_rule_group_counter[g] += 1
        rule_id = rule.get("id", "")
        rule_desc = rule.get("description", "")
        if rule_id:
            global_rule_counter[f"{rule_id}: {rule_desc}"] += 1

    coverage = "complete" if exhausted else "partial"
    total_display = (
        f"{global_total_val or 0:,}"
        + ("+" if global_total_relation == "gte" else "")
    )

    if params.response_format == "json":
        output = {
            "domain": params.domain,
            "mode": "full_scan",
            "total": {"value": global_total_val, "relation": global_total_relation},
            "scanned": total_scanned,
            "pages": pages,
            "coverage": coverage,
            "timezone": "UTC",
            "since": since_str,
            "until": until_str,
            "agent": params.agent_name or "all agents",
            "aggregations": {
                "top_srcips": [
                    {"ip": ip, "count": c}
                    for ip, c in global_srcip_counter.most_common(30)
                ],
                "top_rule_groups": [
                    {"group": g, "count": c}
                    for g, c in global_rule_group_counter.most_common(30)
                ],
                "top_rules": [
                    {"rule": r, "count": c}
                    for r, c in global_rule_counter.most_common(20)
                ],
            },
            "sample_alerts": sample_docs,
        }
        return _truncate_if_needed(json.dumps(output, indent=2, ensure_ascii=False))

    #Markdown output
    lines: list[str] = [
        f"#Wazuh Domain Lookup - {params.domain} (Full Scan)",
        "",
        f"**Total matches in indexer**: {total_display}",
        f"**Scanned**: {total_scanned:,} docs across {pages} page(s)",
        f"**Coverage**: {coverage} "
        + ("(all matching alerts retrieved)" if coverage == "complete"
           else f"(hit max_scanned={params.max_scanned:,} limit)"),
        f"**Time window**: {since_str} to {until_str}",
        f"**Agent**: {params.agent_name or 'all agents'}",
        "",
    ]

    if global_srcip_counter:
        lines.append("## Top Source IPs (global)")
        lines.append("| IP | Alert Count |")
        lines.append("|----|-------------|")
        for ip, c in global_srcip_counter.most_common(20):
            lines.append(f"| {_escape_md_table(ip)} | {c:,} |")
        lines.append("")

    if global_rule_group_counter:
        lines.append("## Top Rule Groups (global)")
        lines.append("| Group | Count |")
        lines.append("|-------|-------|")
        for g, c in global_rule_group_counter.most_common(15):
            lines.append(f"| {_escape_md_table(g)} | {c:,} |")
        lines.append("")

    if global_rule_counter:
        lines.append("## Top Rules (global)")
        lines.append("| Rule | Count |")
        lines.append("|------|-------|")
        for r, c in global_rule_counter.most_common(15):
            lines.append(f"| {_escape_md_table(r)} | {c:,} |")
        lines.append("")

    if sample_docs:
        lines.append("## Sample Alerts (first 50 from page 1)")
        lines.append("")
        lines.append("| Time (UTC) | Agent | Rule | Level | Src IP | Account |")
        lines.append("|------------|-------|------|-------|--------|---------|")
        for doc in sample_docs[:20]:
            ts = (doc.get("@timestamp") or "")[:19]
            agent = (doc.get("agent") or {}).get("name", "-")
            rule = doc.get("rule") or {}
            rule_str = f"{rule.get('id', '-')}: {rule.get('description', '-')}"
            level = rule.get("level", "-")
            ip = (doc.get("data") or {}).get("srcip", "-")
            account = (doc.get("data") or {}).get("account", "-")
            lines.append(
                f"| {ts} | {_escape_md_table(agent)} | {_escape_md_table(rule_str)} "
                f"| {level} | {_escape_md_table(ip)} | {_escape_md_table(account)} |"
            )
        lines.append("")

    if coverage != "complete":
        lines.append(
            f"\n**Note:** Results are partial — scan hit the "
            f"`max_scanned={params.max_scanned:,}` limit. "
            f"Increase `max_scanned` (up to 500,000) for full coverage."
        )

    return _truncate_if_needed("\n".join(lines))


@mcp.tool(
    name="wazuh_domain_lookup",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def wazuh_domain_lookup(params: WazuhDomainLookupInput) -> str:
    """Search Wazuh alerts for a specific domain name.

    Queries the structured ``data.domain`` field (boosted) and also searches
    ``full_log`` for the params.domain as a phrase.

    **Two modes**:

    - **Single-page** (default, ``params.max_scanned`` not set): Returns one page of
      results with a ``next_cursor``.  Call repeatedly with the params.cursor to manually
      iterate through all pages.
    - **Full-scan** (set ``params.max_scanned`` to an integer ≥1000): Auto-paginates
      internally across ALL matching pages and returns an aggregated summary
      (global top IPs, top rule groups, top rules).  Set ``params.max_scanned`` high
      enough to cover the time window - the scan stops when the indexer is
      exhausted or the ceiling is hit.

    Args:
        params.domain: Domain to search for (e.g. 'tangerangkota.go.id')
        params.agent_name: Optional agent filter
        params.since: ISO 8601 start in UTC (default: 365 days ago)
        params.until: ISO 8601 end in UTC (default: now)
        params.limit: Max alerts per page in single-page mode (1-10000, default 500)
        params.include_full_log: Include raw log lines (default false — forced false in full-scan mode)
        params.cursor: Pagination params.cursor from previous response
        params.response_format: 'markdown' or 'json'
        params.max_scanned: When set, run full-scan auto-pagination (see above)
        params.keyword: Free-text keyword to further narrow results
        params.bypass_redaction: When true, skip PII/credential redaction
        params.redaction_policy: 'full', 'protect_victim', or 'raw'
        params.reveal_owned: When true, unmask emails/subdomains at owned domains (BLUETEAM_OWNED_DOMAINS)
        params.forensic_token: Forensic unmask token (BLUETEAM_FORENSIC_TOKEN)

    Returns:
        str: Paged alert results (single-page) or aggregated summary (full-scan).

    Example usage:
        - "Search for all alerts involving tangerangkota.go.id"
        - "Get the complete picture for this params.domain over the past 12h — use full-scan"
        - "Show me who's hitting the mail server params.domain"
    """
    _audit_log("wazuh_domain_lookup", {"domain": params.domain, "since": params.since})
    since_str, until_str = _parse_time_window(params.since, params.until)

    search_after: Optional[list] = None
    if params.cursor:
        decoded = _decode_cursor(params.cursor)
        if decoded:
            search_after = decoded.get("search_after")

    # Auto pagination mode - scan ALL pages internally, return aggregate.
    if params.max_scanned is not None:
        return await _wazuh_domain_lookup_full_scan(
            params, since_str, until_str, search_after
        )

    try:
        body = {
            "size": params.limit,
            "query": {"bool": {"filter": [
                {"range": {"@timestamp": {"gte": since_str, "lt": until_str,
                                               "format": "strict_date_optional_time"}}},
                {"query_string": {"query": f"data.domain: {params.domain}", "lenient": True}},
            ]}},
            "sort": [{"@timestamp": "asc"}, {"_id": "asc"}],
        }
        if params.agent_name:
            body["query"]["bool"]["filter"].append({"match": {"agent.name": params.agent_name}})
        if params.keyword:
            body["query"]["bool"]["filter"].append({"query_string": {"query": params.keyword, "lenient": True}})
        if search_after:
            body["search_after"] = search_after
        data = await _wazuh_indexer_post(body)
    except (httpx.HTTPStatusError, httpx.TimeoutException, RuntimeError) as e:
        return _handle_api_error(e, context="wazuh_domain_lookup")

    if isinstance(data.get("error"), str):
        return json.dumps(data, indent=2)

    hits = data.get("hits", {})
    total = hits.get("total", {})
    total_val = total.get("value", 0) if isinstance(total, dict) else total
    total_relation = total.get("relation", "eq") if isinstance(total, dict) else "eq"
    hit_list = hits.get("hits", [])
    docs = [h.get("_source", h) for h in hit_list]
    docs = _redact_alert_data(docs, params=params)

    # Build next cursor
    next_cursor = None
    if hit_list and len(docs) >= params.limit:
        last_sort = hit_list[-1].get("sort")
        if last_sort:
            next_cursor = _encode_cursor({"search_after": last_sort})

    # Aggregations (client-side from the returned page)
    srcip_counter: Counter[str] = Counter()
    rule_group_counter: Counter[str] = Counter()
    rule_counter: Counter[str] = Counter()
    for doc in docs:
        ip = (doc.get("data") or {}).get("srcip", "")
        if ip:
            srcip_counter[ip] += 1
        rule = doc.get("rule") or {}
        for g in rule.get("groups", []):
            rule_group_counter[g] += 1
        rule_id = rule.get("id", "")
        rule_desc = rule.get("description", "")
        if rule_id:
            rule_counter[f"{rule_id}: {rule_desc}"] += 1

    if params.response_format == "json":
        output = {
            "domain": params.domain,
            "total": {"value": total_val, "relation": total_relation},
            "count": len(docs),
            "size": params.limit,
            "next_cursor": next_cursor,
            "timezone": "UTC",
            "since": since_str,
            "until": until_str,
            "alerts": docs,
            "aggregations": {
                "top_srcips": [
                    {"ip": ip, "count": c} for ip, c in srcip_counter.most_common(20)
                ],
                "top_rule_groups": [
                    {"group": g, "count": c} for g, c in rule_group_counter.most_common(20)
                ],
                "top_rules": [
                    {"rule": r, "count": c} for r, c in rule_counter.most_common(10)
                ],
            },
        }
        return _truncate_if_needed(json.dumps(output, indent=2, ensure_ascii=False))

    # Markdown output
    total_display = f"{total_val:,}" + ("+" if total_relation == "gte" else "")
    page_info = f"Page ({len(docs)} of {total_display})"
    lines: list[str] = [
        f"# Wazuh Domain Lookup - {params.domain}",
        "",
        f"**Total matches**: {total_display}",
        f"**{page_info}**",
        f"**Time window**: {since_str} to {until_str}",
        f"**Agent**: {params.agent_name or 'all agents'}",
        "",
        "## Alerts",
        "",
        "| Time (UTC) | Agent | Rule | Level | Src IP | Account |",
        "|------------|-------|------|-------|--------|---------|",
    ]
    for doc in docs:
        ts = (doc.get("@timestamp") or "")[:19]
        agent = (doc.get("agent") or {}).get("name", "-")
        rule = doc.get("rule") or {}
        rule_str = f"{rule.get('id', '-')}: {rule.get('description', '-')}"
        level = rule.get("level", "-")
        ip = (doc.get("data") or {}).get("srcip", "-")
        account = (doc.get("data") or {}).get("account", "-")
        lines.append(f"| {ts} | {_escape_md_table(agent)} | {_escape_md_table(rule_str)} | {level} | {ip} | {_escape_md_table(account)} |")

    lines.append("")
    if srcip_counter:
        lines.append("## Top Source IPs (this page)")
        lines.append("| IP | Alert Count |")
        lines.append("|----|-------------|")
        for ip, c in srcip_counter.most_common(20):
            lines.append(f"| {_escape_md_table(ip)} | {c:,} |")
        lines.append("")

    if rule_group_counter:
        lines.append("## Top Rule Groups (this page)")
        lines.append("| Group | Count |")
        lines.append("|-------|-------|")
        for g, c in rule_group_counter.most_common(10):
            lines.append(f"| {_escape_md_table(g)} | {c:,} |")
        lines.append("")

    if next_cursor:
        lines.append(f"\n**Next params.cursor**: `{next_cursor}`")
    else:
        lines.append("\n**No more pages** - all results returned.")

    return _truncate_if_needed("\n".join(lines))


# WHOIS/RDAP Domain Lookup
class WhoisLookupInput(BaseModel):
    """Input model for blueteam_whois_lookup."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    domain: str = Field(..., min_length=4, max_length=253,
                        description="Domain name to look up (e.g. example.com).")
    response_format: Literal["markdown", "json"] = Field(
        default="markdown", description="'markdown' or 'json'.")

    @field_validator("domain")
    @classmethod
    def validate_domain(cls, v: str) -> str:
        v = v.strip().lower().rstrip(".")
        if not re.match(r"^[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)+$", v):
            raise ValueError(f"'{v}' is not a valid domain name.")
        return v


@mcp.tool(
    name="blueteam_whois_lookup",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": True},
)
async def blueteam_whois_lookup(params: WhoisLookupInput) -> str:
    """Look up domain registration via RDAP (free, no API key required).

    Queries the IANA RDAP bootstrap service for domain ownership, registrar,
    nameservers, and registration dates. RDAP is the modern, structured
    replacement for WHOIS - returns JSON instead of free-text.

    Use this to attribute domains seen in Wazuh alerts, check if a domain
    was recently registered (common in phishing), or find related nameservers.

    **No credentials required** - RDAP is a public protocol.

    **Worked Examples**

    1. *Check a suspicious domain*:
       ``blueteam_whois_lookup(domain="suspicious-login.xyz")``

    2. *Verify ownership of a known-good domain*:
       ``blueteam_whois_lookup(domain="google.com")``

    3. *JSON output for LLM parsing*:
       ``blueteam_whois_lookup(domain="evil-c2.net", response_format="json")``
    """
    _audit_log("blueteam_whois_lookup", {"domain": params.domain})
    domain = params.domain.strip().lower().rstrip(".")

    try:
        resp = await _api_call("get", f"{RDAP_BASE_URL}/domain/{domain}",
                               client_name="http", verify=True,
                               headers={"Accept": "application/json",
                                        "User-Agent": "blue-team-mcp/1.0.0"})
        data = resp.json()
    except Exception as e:
        return json.dumps({"error": f"RDAP lookup failed: {e}", "domain": domain}, indent=2)

    # Extract key fields
    nameservers = []
    for ns in data.get("nameservers", []):
        name = ns.get("ldhName") or ns.get("objectClassName", "?")
        if name:
            nameservers.append(name)

    entities: list[dict] = []
    for ent in data.get("entities", []):
        roles = ent.get("roles", [])
        vcard = ent.get("vcardArray", [[], []])[1] if isinstance(ent.get("vcardArray"), list) else []
        org = ""
        for item in vcard:
            if isinstance(item, list) and len(item) >= 4 and item[0] == "fn":
                org = item[3]
                break
        entities.append({"roles": roles, "name": org or ent.get("handle", "?")})

    events: dict[str, str] = {}
    for ev in data.get("events", []):
        action = ev.get("eventAction", "?")
        events[action] = ev.get("eventDate", "?")[:10]

    if params.response_format == "json":
        return json.dumps({
            "domain": domain,
            "handle": data.get("handle", "?"),
            "status": data.get("status", []),
            "nameservers": nameservers,
            "registrar": next((e["name"] for e in entities if "registrar" in e.get("roles", [])), None),
            "registrant": next((e["name"] for e in entities if "registrant" in e.get("roles", [])), None),
            "dates": events,
        }, indent=2, ensure_ascii=False)

    lines = [
        f"# 🌐 WHOIS Lookup - `{domain}`",
        "",
        f"**Handle**: `{data.get('handle', '?')}`",
        f"**Status**: {', '.join(data.get('status', ['unknown']))}",
        "",
    ]

    if nameservers:
        lines.append("## Nameservers")
        for ns in nameservers[:8]:
            lines.append(f"- `{ns}`")
        lines.append("")

    if events:
        lines.append("## Dates")
        for action, date in sorted(events.items()):
            label = action.replace("_", " ").title()
            lines.append(f"- **{label}**: {date}")
        lines.append("")

    if entities:
        lines.append("## Entities")
        for e in entities[:5]:
            roles_str = ", ".join(e["roles"])
            lines.append(f"- **{roles_str}**: {e['name']}")
        lines.append("")

    # Red flags for LLM analysis
    lines.append("## ⚠️ Red Flags")
    flags = []
    created = events.get("registration", "")
    if created:
        try:
            from datetime import datetime
            age_days = (datetime.utcnow() - datetime.fromisoformat(created)).days
            if age_days < 30:
                flags.append(f"🔴 Domain registered {age_days}d ago — very new (common in phishing)")
            elif age_days < 180:
                flags.append(f"🟡 Domain registered {age_days}d ago — relatively new")
        except Exception:
            pass
    if not nameservers:
        flags.append("🔴 No nameservers — domain may not be resolving")
    if any("serverHold" in s or "inactive" in s for s in data.get("status", [])):
        flags.append("🟡 Domain status includes hold/inactive")
    if not flags:
        flags.append("✅ No obvious red flags detected")
    for f in flags:
        lines.append(f"- {f}")

    return _truncate_if_needed("\n".join(lines))


# SSL Certificate Transparency Lookup
class CrtshLookupInput(BaseModel):
    """Input model for blueteam_crtsh_lookup."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    domain: str = Field(..., min_length=4, max_length=253,
                        description="Domain to search for SSL certificates (e.g. example.com).")
    response_format: Literal["markdown", "json"] = Field(
        default="markdown", description="'markdown' or 'json'.")

    @field_validator("domain")
    @classmethod
    def validate_domain(cls, v: str) -> str:
        v = v.strip().lower().rstrip(".")
        if not re.match(r"^[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)+$", v):
            raise ValueError(f"'{v}' is not a valid domain name.")
        return v


@mcp.tool(
    name="blueteam_crtsh_lookup",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": True},
)
async def blueteam_crtsh_lookup(params: CrtshLookupInput) -> str:
    """Search SSL certificate transparency logs for a domain via crt.sh.

    Returns all SSL/TLS certificates issued for a domain and its subdomains.
    This is a powerful pivoting technique: find sibling domains an attacker
    registered alongside the one you're investigating.

    **No API key required** - crt.sh is a free, public Certificate Transparency log.

    **Worked Examples**

    1. *Find all certs for a suspicious domain*:
       ``blueteam_crtsh_lookup(domain="evil-c2.net")``

    2. *JSON output for automated parsing*:
       ``blueteam_crtsh_lookup(domain="phish-target.com", response_format="json")``

    3. *Pivot from one domain to attacker infrastructure*:
       ``blueteam_crtsh_lookup(domain="malware-drop.xyz")`` — check sibling names
    """
    _audit_log("blueteam_crtsh_lookup", {"domain": params.domain})
    domain = params.domain.strip().lower().rstrip(".")

    try:
        resp = await _api_call("get", f"{CRTSH_BASE_URL}/?q=%25.{domain}&output=json",
                               client_name="http", verify=True,
                               headers={"User-Agent": "blue-team-mcp/1.0.0"})
        entries = resp.json()
    except Exception as e:
        return json.dumps({"error": f"crt.sh lookup failed: {e}", "domain": domain}, indent=2)

    if not isinstance(entries, list):
        entries = []

    # Extract unique name_values (domains covered by certs)
    names: list[str] = []
    issuers: dict[str, int] = {}
    seen = set()
    for e in entries[:500]:
        nv = e.get("name_value", "")
        for name in nv.split("\n"):
            name = name.strip().lower()
            if name and name not in seen:
                seen.add(name)
                names.append(name)
        issuer = e.get("issuer_name", "?")
        # Truncate long issuer names
        issuer_short = issuer[:80] if issuer else "?"
        issuers[issuer_short] = issuers.get(issuer_short, 0) + 1

    # Classify names
    subdomains = [n for n in names if n.endswith(f".{domain}")]
    siblings = [n for n in names if not n.endswith(f".{domain}") and n != domain]

    if params.response_format == "json":
        return json.dumps({
            "domain": domain,
            "total_certs": len(entries),
            "unique_names": len(names),
            "subdomains": subdomains[:50],
            "sibling_domains": siblings[:50],
            "top_issuers": dict(sorted(issuers.items(), key=lambda x: -x[1])[:10]),
        }, indent=2, ensure_ascii=False)

    lines = [
        f"# 🔐 Certificate Transparency — `{domain}`",
        "",
        f"**Total certificates found**: {len(entries):,}",
        f"**Unique names covered**: {len(names):,}",
        "",
    ]

    if subdomains:
        lines.append(f"## Subdomains ({len(subdomains)})")
        for s in subdomains[:25]:
            lines.append(f"- `{s}`")
        if len(subdomains) > 25:
            lines.append(f"- ... and {len(subdomains) - 25} more")
        lines.append("")

    if siblings:
        lines.append(f"## 🔗 Sibling Domains ({len(siblings)}) — potential attacker infrastructure")
        for s in siblings[:25]:
            lines.append(f"- `{s}`")
        if len(siblings) > 25:
            lines.append(f"- ... and {len(siblings) - 25} more")
        lines.append("")

    if issuers:
        lines.append("## Top Issuers")
        for issuer, count in sorted(issuers.items(), key=lambda x: -x[1])[:8]:
            lines.append(f"- `{issuer}`: {count} certs")
        lines.append("")

    if not entries:
        lines.append("✅ No certificates found — domain may not have publicly-trusted TLS certs.")

    return _truncate_if_needed("\n".join(lines))
