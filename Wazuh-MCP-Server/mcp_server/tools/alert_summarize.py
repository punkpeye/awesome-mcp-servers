#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Alert summarization IoC extraction, rule grouping, MITRE mapping, compact digest.
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
# Auto-extracted from alert_enrichment.py - modular refactor (2026-08-11)
class AlertSummarizeInput(BaseModel):
    """Input model for blueteam_wazuh_alert_summarize."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    srcip: str = Field(
        ...,
        min_length=7,
        max_length=45,
        description="Source IP to summarize alerts for (e.g. '103.107.116.202').",
    )
    agent_name: ValidAgentName = Field(
        default=None,
        max_length=64,
        description="Optional Wazuh agent name filter.",
    )
    since: Optional[str] = Field(
        default="24h",
        max_length=30,
        description="Start of time window. ISO 8601 or relative ('5m','1h','24h','7d','30d').",
    )
    until: Optional[str] = Field(
        default=None,
        max_length=30,
        description="End of time window. Defaults to now.",
    )
    limit: int = Field(
        default=200,
        ge=10,
        le=2000,
        description="Max alerts to fetch for summarization (default 200).",
    )
    response_format: Literal["markdown", "json"] = Field(
        default="markdown",
        description="Output format: 'markdown' (human-readable digest) or 'json'.",
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


@mcp.tool(
    name="blueteam_wazuh_alert_summarize",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
async def blueteam_wazuh_alert_summarize(params: AlertSummarizeInput) -> str:
    """Summarize Wazuh alerts for a source IP into a compact threat digest.

    Extracts IoCs (domains, URLs, user-agents), groups alerts by rule.id
    with counts, computes first_seen / last_seen per rule, and flags
    unusual user-agent strings (old browsers, scripted clients).

    Returns a markdown report or JSON with the structured digest — the LLM
    can reason about attack patterns from the summary without scanning
    raw alert documents.

    **Required Permissions**: Wazuh Indexer user with ``read`` access.

    Args:
        params.redaction_policy: 'full' (shape-based, default), 'protect_victim' (mask victim-owned indicators only), 'raw' (Layer 1 credential strip only, requires BLUETEAM_ALLOW_FORENSIC_BYPASS).
        params.reveal_owned: When true (forensic), expose emails/subdomains at owned domains (BLUETEAM_OWNED_DOMAINS) unmasked; Layer 1 credentials remain masked.
        params.forensic_token: Operator forensic token (matches BLUETEAM_FORENSIC_TOKEN); required for redaction_policy='raw' / bypass_redaction when that env is set.
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    **Worked Examples**

    1. *Basic IP summary*:
       ``blueteam_wazuh_alert_summarize(srcip="103.107.116.202")``

    2. *Focused time window*:
       ``blueteam_wazuh_alert_summarize(srcip="103.107.116.202", since="1h")``

    3. *Single agent only*:
       ``blueteam_wazuh_alert_summarize(srcip="103.107.116.202", agent_name="thezoo-prod")``
    """
    _audit_log("blueteam_wazuh_alert_summarize", {"srcip": params.srcip})
    if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
        return json.dumps({
            "error": "WAZUH_INDEXER_URL and WAZUH_INDEXER_PASSWORD must be set.",
        }, indent=2)

    since_iso, until_iso = _parse_time_window(params.since, params.until)

    must_clauses: list[dict] = [
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
    if params.agent_name:
        must_clauses.append({"match": {"agent.name": params.agent_name.strip()}})

    body = {
        "size": min(params.limit, _WAZUH_INDEXER_MAX_SIZE),
        "sort": [{"@timestamp": {"order": "asc"}}],
        "query": {"bool": {"must": must_clauses}},
        "_source": [
            "@timestamp", "agent.name", "rule.id", "rule.level",
            "rule.description", "rule.groups", "rule.mitre.tactic",
            "data.srcip", "data.domain", "data.url", "data.user_agent",
        ],
    }
    raw = await _wazuh_indexer_post(body)
    if "error" in raw:
        return json.dumps(raw, indent=2)

    hits = raw.get("hits", {}).get("hits", [])
    docs = [_redact_alert_data(h.get("_source", h), params=params)
            for h in hits]

    if not docs:
        result = {"srcip": params.srcip, "total_alerts": 0,
                  "summary": "No alerts found for this IP in the time window."}
        return json.dumps(result, indent=2) if params.response_format == "json" else (
            f"# Alert Digest - {params.srcip}\n\n**No alerts found** in window "
            f"`{since_iso}` -> `{until_iso}`.")

    # IoC extraction
    rule_counts: Counter[str] = Counter()
    rule_descriptions: dict[str, str] = {}
    rule_timestamps: dict[str, list[str]] = {}
    domains: set[str] = set()
    urls: list[dict[str, str]] = []
    uas: Counter[str] = Counter()
    unusual_uas: list[str] = []
    mitre_tactics: set[str] = set()
    first_ts = docs[0].get("@timestamp", "")
    last_ts = docs[-1].get("@timestamp", "")

    for d in docs:
        rid = str(d.get("rule", {}).get("id", "unknown"))
        rule_counts[rid] = rule_counts.get(rid, 0) + 1
        if rid not in rule_descriptions:
            rule_descriptions[rid] = str(d.get("rule", {}).get("description", rid))
        rule_timestamps.setdefault(rid, []).append(str(d.get("@timestamp", "")))

        data = d.get("data", {})
        if isinstance(data, dict):
            dom = str(data.get("domain", "")).strip()
            if dom and dom != "-":
                domains.add(dom)
            url = str(data.get("url", "")).strip()
            if url and url != "-":
                urls.append({"url": url, "ts": str(d.get("@timestamp", ""))})
            ua = str(data.get("user_agent", "")).strip()
            if ua and ua != "-":
                uas[ua] += 1

        mitre = d.get("rule", {}).get("mitre", {})
        if isinstance(mitre, dict):
            tactics = mitre.get("tactic", [])
            if isinstance(tactics, list):
                mitre_tactics.update(tactics)

    # Flag unusual UA
    _UA_SIGNALS = [
        (re.compile(r"Firefox/(?:[1-6]\d|7[0-7])\."), "Old Firefox (pre-78)"),
        (re.compile(r"Chrome/(?:[1-5]\d|6[0-9])\."), "Old Chrome (pre-70)"),
        (re.compile(r"curl|wget|python|go-http|libwww|Java/"), "Scripted/automated client"),
        (re.compile(r"zgrab|masscan|nmap|nikto|sqlmap|ffuf|burp"), "Scanner/exploitation tool"),
    ]
    for ua, _ in uas.most_common(20):
        for pat, label in _UA_SIGNALS:
            if pat.search(ua):
                unusual_uas.append(f"{label}: `{ua[:120]}`")
                break

    # Build response
    if params.response_format == "json":
        result = {
            "srcip": params.srcip,
            "window": {"since": since_iso, "until": until_iso},
            "total_alerts": len(docs),
            "first_seen": first_ts,
            "last_seen": last_ts,
            "rules": [
                {
                    "id": rid,
                    "count": cnt,
                    "description": rule_descriptions.get(rid, ""),
                    "first_seen": rule_timestamps[rid][0],
                    "last_seen": rule_timestamps[rid][-1],
                }
                for rid, cnt in rule_counts.most_common()
            ],
            "iocs": {
                "domains": sorted(domains),
                "urls": urls[:50],
                "top_user_agents": [{"ua": ua, "count": n}
                                    for ua, n in uas.most_common(5)],
            },
            "mitre_tactics": sorted(mitre_tactics),
            "unusual_user_agents": unusual_uas,
        }
        return _truncate_if_needed(json.dumps(result, indent=2, ensure_ascii=False))

    # Markdown digest
    lines = [
        f"# Alert Digest - `{params.srcip}`",
        "",
        f"- **Window**: `{since_iso}` -> `{until_iso}`",
        f"- **Total alerts**: {len(docs)} | **First seen**: `{first_ts}` | **Last seen**: `{last_ts}`",
        "",
        "## Rules Triggered",
        "",
        "| Rule ID | Count | Description | First → Last |",
        "|---------|-------|-------------|--------------|",
    ]
    for rid, cnt in rule_counts.most_common():
        desc = _escape_md_table(rule_descriptions.get(rid, ""))[:80]
        fst = rule_timestamps[rid][0][:19] if rule_timestamps[rid] else "-"
        lst = rule_timestamps[rid][-1][:19] if rule_timestamps[rid] else "-"
        lines.append(f"| {rid} | {cnt} | {desc} | {fst} → {lst} |")

    if domains:
        lines.append("")
        lines.append("## Target Domains")
        for d in sorted(domains):
            lines.append(f"- `{d}`")

    if urls:
        lines.append("")
        lines.append(f"## URLs Accessed ({len(urls)} total, showing first 15)")
        for u in urls[:15]:
            ts_short = u["ts"][:19] if len(u["ts"]) > 19 else u["ts"]
            lines.append(f"- `[{ts_short}]` `{u['url'][:100]}`")
        if len(urls) > 15:
            lines.append(f"- ... and {len(urls) - 15} more")

    if mitre_tactics:
        lines.append("")
        lines.append("## MITRE ATT&CK Tactics")
        for t in sorted(mitre_tactics):
            cat = MITRE_TACTIC_TO_CATEGORY.get(t, "?")
            lines.append(f"- {t} (3-Sum Cat: `{cat}`)")

    if unusual_uas:
        lines.append("")
        lines.append("## ⚠️ Unusual User-Agents Flagged")
        for ua_flag in unusual_uas:
            lines.append(f"- {ua_flag}")

    if uas:
        lines.append("")
        lines.append("## Top User-Agents")
        for ua, n in uas.most_common(3):
            lines.append(f"- ({n}×) `{ua[:100]}`")

    return _truncate_if_needed("\n".join(lines))


# 2: Beacon Detection
