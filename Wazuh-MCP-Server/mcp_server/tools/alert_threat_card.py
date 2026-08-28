#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Threat cards single-call report: alerts + CrowdSec/GreyNoise + MITRE + actions.
"""
from __future__ import annotations
import json, re, math, asyncio, os
from datetime import datetime, timedelta
from typing import Optional, Literal, Any
from collections import Counter
from pydantic import BaseModel, ConfigDict, Field, field_validator
from mcp_server import (mcp, WAZUH_INDEXER_URL, WAZUH_INDEXER_PASSWORD,
                        _WAZUH_INDEXER_MAX_SIZE, _BYPASS_REDACTION_DESC, _REDACTION_POLICY_DESC, _REVEAL_OWNED_DESC, _FORENSIC_TOKEN_DESC,
                        CROWDSEC_API_KEY_ENV, ARGUS_API_KEY_ENV,
                        ABUSEIPDB_API_KEY, VIRUSTOTAL_API_KEY,
                        GREYNOISE_COMMUNITY_BASE_URL, ABUSEIPDB_BASE_URL,
                        VIRUSTOTAL_BASE_URL, ARGUS_BASE_URL)
from mcp_server.core.audit import _audit_log, _truncate_if_needed, _escape_md_table
from mcp_server.core.http_client import ValidPublicIp
from mcp_server.core.redact import _redact_alert_data
from mcp_server.core.http_client import _api_call, _get_client
from mcp_server.core.validators import ValidAgentName, ValidKeyword, ValidRuleGroups
from mcp_server.core.constants import MITRE_TACTIC_TO_CATEGORY
from mcp_server.wazuh.indexer import _wazuh_indexer_post, _WAZUH_INDEX_PATTERNS
from mcp_server.wazuh.time_utils import _parse_time_window, _duration_minutes
from mcp_server.threat_intel.crowdsec import _crowdsec_request

# 1: Alert Summarization
# Auto-extracted from alert_enrichment.py - modular refactor by Aul
class ThreatCardInput(BaseModel):
    """Input model for blueteam_threat_card."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    srcip: ValidPublicIp = Field(
        ...,
        min_length=7,
        max_length=45,
        description="Source IP to generate a comprehensive threat card for.",
    )
    since: Optional[str] = Field(
        default="24h",
        max_length=30,
        description="Start of time window.",
    )
    until: Optional[str] = Field(
        default=None,
        max_length=30,
        description="End of time window. Defaults to now.",
    )
    include_threat_intel: bool = Field(
        default=True,
        description="Include CrowdSec and GreyNoise reputation lookups (may add ~2s latency).",
    )
    redaction_policy: Optional[Literal["full", "protect_victim", "raw"]] = Field(
        default=None,
        description=_REDACTION_POLICY_DESC,
    )
    reveal_owned: bool = Field(default=False, description=_REVEAL_OWNED_DESC)
    forensic_token: Optional[str] = Field(default=None, max_length=128, description=_FORENSIC_TOKEN_DESC)
    bypass_redaction: bool = Field(
        default=False,
        description=_BYPASS_REDACTION_DESC,
    )
    response_format: Literal["markdown", "json"] = Field(
        default="markdown",
        description="'markdown' (default, human-readable) or 'json'.",
    )


@mcp.tool(
    name="blueteam_threat_card",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def blueteam_threat_card(params: ThreatCardInput) -> str:
    """Generate a comprehensive threat card for a source IP.
    Collapses alert summarization, attack chain analysis, MITRE ATT&CK
    mapping, and threat intelligence (CrowdSec + GreyNoise) into a single
    structured report. Designed as the one-stop triage tool the LLM can
    understand the full threat context in one call.

    **Required Permissions**: Wazuh Indexer ``read`` access.
    CrowdSec/GreyNoise lookups are best-effort (fail gracefully if keys
    are not configured).

    Args:
        params.redaction_policy: 'full' (shape-based, default), 'protect_victim' (mask victim-owned indicators only), 'raw' (Layer 1 credential strip only, requires BLUETEAM_ALLOW_FORENSIC_BYPASS).
        params.reveal_owned: When true (forensic), expose emails/subdomains at owned domains (BLUETEAM_OWNED_DOMAINS) unmasked; Layer 1 credentials remain masked.
        params.forensic_token: Operator forensic token (matches BLUETEAM_FORENSIC_TOKEN); required for redaction_policy='raw' / bypass_redaction when that env is set.
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    **Worked Examples**

    1. *Default 24h card*:
       ``blueteam_threat_card(srcip="103.107.116.202")``

    2. *7-day forensic card*:
       ``blueteam_threat_card(srcip="103.107.116.202", since="7d")``

    3. *Skip threat intel for speed*:
       ``blueteam_threat_card(srcip="103.107.116.202", include_threat_intel=false)``
    """
    _audit_log("blueteam_threat_card", {"srcip": params.srcip})
    if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
        return json.dumps({
            "error": "WAZUH_INDEXER_URL and WAZUH_INDEXER_PASSWORD must be set.",
        }, indent=2)

    since_iso, until_iso = _parse_time_window(params.since, params.until)

    # Fetch alerts for this IP
    body = {
        "size": 500,
        "sort": [{"@timestamp": {"order": "asc"}}],
        "query": {
            "bool": {
                "must": [
                    {"range": {"@timestamp": {"gte": since_iso, "lt": until_iso,
                                             "format": "strict_date_optional_time"}}},
                    {"bool": {
                        "should": [
                            {"match": {"data.srcip": params.srcip.strip()}},
                            {"match_phrase": {"full_log": params.srcip.strip()}},
                        ],
                        "minimum_should_match": 1,
                    }},
                ]
            }
        },
        "_source": [
            "@timestamp", "agent.name", "rule.id", "rule.level",
            "rule.description", "rule.groups", "rule.mitre.tactic",
            "data.srcip", "data.domain", "data.url", "data.user_agent",
        ],
    }

    # Fetch alerts + threat intel concurrently
    async def _fetch_alerts():
        raw = await _wazuh_indexer_post(body)
        if "error" in raw:
            return raw
        return [h.get("_source", h) for h in raw.get("hits", {}).get("hits", [])]

    async def _fetch_crowdsec():
        if not params.include_threat_intel or not os.environ.get(CROWDSEC_API_KEY_ENV):
            return None
        try:
            return await _crowdsec_request(f"/v2/smoke/{params.srcip}")
        except Exception:
            return None

    async def _fetch_greynoise():
        if not params.include_threat_intel:
            return None
        try:
            headers = {"accept": "application/json", "User-Agent": "blue-team-mcp/1.0.0"}
            resp = await _api_call("get", f"{GREYNOISE_COMMUNITY_BASE_URL}/{params.srcip}", headers=headers)
            return resp.json()
        except Exception:
            return None

    docs, crowdsec_data, greynoise_data = await asyncio.gather(
        _fetch_alerts(), _fetch_crowdsec(), _fetch_greynoise(),
    )

    if isinstance(docs, dict) and "error" in docs:
        return json.dumps(docs, indent=2)

    docs = _redact_alert_data(docs, params=params)

    if not docs:
        return "# Threat Card - `" + params.srcip + "`\n\n**No alerts found** for this IP in the selected time window."

    # Extract common data
    rule_counts: Counter[str] = Counter()
    rule_descs: dict[str, str] = {}
    mitre_tactics: set[str] = set()
    domains: set[str] = set()
    urls: list[str] = []
    levels: list[int] = []
    agents: set[str] = set()
    first_ts = str(docs[0].get("@timestamp", ""))[:19]
    last_ts = str(docs[-1].get("@timestamp", ""))[:19]

    for d in docs:
        r = d.get("rule", {})
        rid = str(r.get("id", "unknown"))
        rule_counts[rid] += 1
        if rid not in rule_descs:
            rule_descs[rid] = str(r.get("description", rid))
        lvl = r.get("level")
        if isinstance(lvl, (int, str)):
            try: levels.append(int(lvl))
            except (ValueError, TypeError): pass
        mitre = r.get("mitre", {})
        if isinstance(mitre, dict):
            tactics = mitre.get("tactic", [])
            if isinstance(tactics, list): mitre_tactics.update(tactics)
        data = d.get("data", {})
        if isinstance(data, dict):
            dom = str(data.get("domain", "")).strip()
            if dom and dom != "-": domains.add(dom)
            url = str(data.get("url", "")).strip()
            if url and url != "-": urls.append(url)
        ag = d.get("agent", {})
        if isinstance(ag, dict) and ag.get("name"): agents.add(str(ag["name"]))

    max_level = max(levels) if levels else 0
    avg_level = sum(levels) / len(levels) if levels else 0.0

    # Format output
    if params.response_format == "json":
        return _truncate_if_needed(json.dumps({
            "srcip": params.srcip,
            "window": {"since": since_iso, "until": until_iso},
            "total_events": len(docs),
            "first_seen": first_ts,
            "last_seen": last_ts,
            "max_level": max_level,
            "avg_level": round(avg_level, 1),
            "rules": [{"id": rid, "count": cnt, "description": rule_descs.get(rid, "")}
                      for rid, cnt in rule_counts.most_common(10)],
            "targeted_domains": sorted(domains),
            "urls_probed": list(set(urls))[:50],
            "mitre_tactics": sorted(mitre_tactics),
            "agents": sorted(agents),
            "threat_intel": {"crowdsec": crowdsec_data, "greynoise": greynoise_data},
        }, indent=2, ensure_ascii=False))

    # Markdown threat card
    lines = [
        f"# 🛡️ Threat Card - `{params.srcip}`",
        "",
        f"**Window**: `{since_iso}` -> `{until_iso}` | **Total events**: {len(docs)}",
        "",
        "---",
        "",
    ]

    if not docs:
        lines.append("## No alerts found")
        lines.append(f"No Wazuh alerts for `{params.srcip}` in this time window.")
        return "\n".join(lines)

    # Section 1: Executive Summary
    lines.append("## 📊 Executive Summary")
    lines.append("")
    lines.append(f"| Field | Value |")
    lines.append(f"|-------|-------|")
    lines.append(f"| Total alerts | {len(docs)} |")
    lines.append(f"| Unique rules | {len(rule_counts)} |")
    lines.append(f"| Max rule level | {max_level} |")
    lines.append(f"| Avg rule level | {avg_level:.1f} |")
    lines.append(f"| Agents targeted | {len(agents)} ({', '.join(sorted(agents)[:3])}{"..." if len(agents) > 3 else ""}) |")
    lines.append(f"| First seen | `{first_ts}` |")
    lines.append(f"| Last seen | `{last_ts}` |")
    lines.append("")

    # Section 2: MITRE ATT&CK
    if mitre_tactics:
        lines.append("## 🎯 MITRE ATT&CK Tactics")
        lines.append("")
        lines.append("| Tactic | 3-Sum Category |")
        lines.append("|--------|---------------|")
        for t in sorted(mitre_tactics):
            cat = MITRE_TACTIC_TO_CATEGORY.get(t, "?")
            lines.append(f"| {t} | `{cat}` |")
        lines.append("")

    # Section 3: Rules Fired
    lines.append("## 🔥 Rules Triggered")
    lines.append("")
    lines.append("| Rule ID | Count | Description |")
    lines.append("|---------|-------|-------------|")
    for rid, cnt in rule_counts.most_common(10):
        desc = _escape_md_table(rule_descs.get(rid, ""))[:80]
        lines.append(f"| {rid} | {cnt} | {desc} |")
    lines.append("")

    # Section 4: Targeted Resources
    if domains:
        lines.append("## 🌐 Targeted Domains")
        for d in sorted(domains):
            lines.append(f"- `{d}`")
        lines.append("")
    if urls:
        lines.append(f"## 🔗 URLs Probed ({len(urls)} unique)")
        for u in sorted(set(urls))[:10]:
            lines.append(f"- `{u[:120]}`")
        if len(set(urls)) > 10:
            lines.append(f"- ... and {len(set(urls)) - 10} more")
        lines.append("")

    # Section 5: Threat Intelligence
    if crowdsec_data or greynoise_data:
        lines.append("## 🌍 External Threat Intelligence")
        lines.append("")
    if crowdsec_data:
        rep = crowdsec_data.get("reputation", "unknown")
        behaviors = [b.get("name", "") for b in crowdsec_data.get("behaviors", [])]
        lines.append(f"- **CrowdSec**: reputation `{rep}`")
        if behaviors:
            lines.append(f"- Behaviors: {', '.join(behaviors[:5])}")
        cves = crowdsec_data.get("cves", [])
        if cves:
            lines.append(f"- Related CVEs: {', '.join(cves[:5])}")
    if greynoise_data:
        noise = greynoise_data.get("noise")
        riot = greynoise_data.get("riot")
        classification = greynoise_data.get("classification", "unknown")
        lines.append(f"- **GreyNoise**: classification `{classification}`")
        if noise:
            lines.append(f"- Internet scanner: ✅ (background noise)")
        if riot:
            lines.append(f"- Known business service: ✅ (likely benign)")
    if crowdsec_data or greynoise_data:
        lines.append("")

    # Section 6: Recommended Actions
    lines.append("## 🛠️ Recommended Actions")
    lines.append("")

    # Heuristic recommendations based on alert patterns
    if max_level >= 12:
        lines.append("1. **🚨 IMMEDIATE**: Critical-severity alerts detected — initiate incident response")
        lines.append(f"2. Block `{params.srcip}` at perimeter firewall immediately")
    elif max_level >= 10:
        lines.append(f"1. **⚠️ HIGH**: Block `{params.srcip}` at perimeter firewall")
        lines.append("2. Review affected agent logs for signs of compromise")
    elif max_level >= 6:
        lines.append(f"1. **📋 MEDIUM**: Monitor `{params.srcip}` and add to watchlist")
        lines.append("2. Review web/app logs for suspicious request patterns")
    else:
        lines.append(f"1. **ℹ️ LOW**: `{params.srcip}` shows low-severity activity")
        lines.append("2. No immediate action required — continue monitoring")

    if crowdsec_data and crowdsec_data.get("reputation") == "malicious":
        lines.append("3. CrowdSec confirms malicious — escalate block priority")
    if len(agents) > 1:
        lines.append(f"4. IP targeted {len(agents)} agents — check for lateral movement")
    if len(mitre_tactics) >= 3:
        lines.append("5. Multiple MITRE tactics observed — full compromise assessment recommended")

    lines.append("")
    lines.append("---")
    lines.append(f"*Card generated by blue_team_mcp at {datetime.utcnow().isoformat()[:19]}Z*")

    return _truncate_if_needed("\n".join(lines))


# F-6: Alert Comparison
