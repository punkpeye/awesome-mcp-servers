#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Threat hunting query templates - named DSL templates for common adversary techniques.
"""
from __future__ import annotations
import json
from typing import Optional, Literal
from pydantic import BaseModel, ConfigDict, Field
from mcp_server import mcp, WAZUH_INDEXER_URL, WAZUH_INDEXER_PASSWORD
from mcp_server.core.audit import _audit_log, _truncate_if_needed
from mcp_server.core.redact import _redact_alert_data
from mcp_server.wazuh.indexer import _wazuh_indexer_post, _WAZUH_INDEX_PATTERNS
from mcp_server.wazuh.time_utils import _parse_time_window
from mcp_server.core.validators import ValidAgentName

# Threat Hunting Templates
# Each template is a function (query_body, description) that builds an OpenSearch
# DSL aggregation query given time window, optional agent, and optional srcip.
_THREAT_HUNT_TEMPLATES: dict[str, dict] = {
    "encoded_powershell": {
        "description": "Base64-encoded PowerShell commands - common in fileless malware and C2 stagers.",
        "mitre": "T1059.001 / T1027",
        "query": lambda since, until, agent, srcip: {
            "size": 0,
            "query": {"bool": {"filter": _base_filters(since, until, agent, srcip) + [
                {"query_string": {"query": "powershell AND (-enc OR -EncodedCommand OR FromBase64String)",
                                  "default_field": "full_log", "lenient": True}},
            ]}},
            "aggs": {
                "by_agent": {"terms": {"field": "agent.name", "size": 20}},
                "by_hour": {"date_histogram": {"field": "@timestamp", "fixed_interval": "1h",
                              "min_doc_count": 0, "extended_bounds": {"min": since, "max": until}}},
            },
        },
    },
    "lsass_access": {
        "description": "Process access to LSASS - credential dumping via Mimikatz, procdump, or task manager.",
        "mitre": "T1003.001",
        "query": lambda since, until, agent, srcip: {
            "size": 0,
            "query": {"bool": {"filter": _base_filters(since, until, agent, srcip) + [
                {"query_string": {"query": "lsass OR (procdump AND lsass) OR (comsvcs AND MiniDump)",
                                  "default_field": "full_log", "lenient": True}},
            ]}},
            "aggs": {
                "by_agent": {"terms": {"field": "agent.name", "size": 20}},
                "by_rule": {"terms": {"field": "rule.id", "size": 15}},
            },
        },
    },
    "kerberoasting": {
        "description": "Kerberos TGS-REQ for service principals - SPN scanning / Kerberoasting.",
        "mitre": "T1558.003",
        "query": lambda since, until, agent, srcip: {
            "size": 0,
            "query": {"bool": {"filter": _base_filters(since, until, agent, srcip) + [
                {"query_string": {"query": "(kerberos AND TGS) OR (event_id:4769) OR kerberoast",
                                  "default_field": "full_log", "lenient": True}},
            ]}},
            "aggs": {
                "by_srcip": {"terms": {"field": "data.srcip", "size": 20}},
                "by_agent": {"terms": {"field": "agent.name", "size": 20}},
            },
        },
    },
    "suspicious_scheduled_tasks": {
        "description": "Scheduled task creation - persistence via schtasks, at, or cron. Look for random task names.",
        "mitre": "T1053",
        "query": lambda since, until, agent, srcip: {
            "size": 0,
            "query": {"bool": {"filter": _base_filters(since, until, agent, srcip) + [
                {"query_string": {"query": "schtasks OR (at.exe AND /create) OR (crontab AND -l)",
                                  "default_field": "full_log", "lenient": True}},
            ]}},
            "aggs": {
                "by_agent": {"terms": {"field": "agent.name", "size": 20}},
                "by_hour": {"date_histogram": {"field": "@timestamp", "fixed_interval": "1h",
                              "min_doc_count": 0, "extended_bounds": {"min": since, "max": until}}},
            },
        },
    },
    "wmi_persistence": {
        "description": "WMI event subscriptions — __EventFilter, __EventConsumer, CommandLineEventConsumer — classic APT persistence.",
        "mitre": "T1546.003",
        "query": lambda since, until, agent, srcip: {
            "size": 0,
            "query": {"bool": {"filter": _base_filters(since, until, agent, srcip) + [
                {"query_string": {"query": "(WMI AND EventFilter) OR CommandLineEventConsumer OR __EventConsumer OR (wmic AND /namespace)",
                                  "default_field": "full_log", "lenient": True}},
            ]}},
            "aggs": {
                "by_agent": {"terms": {"field": "agent.name", "size": 20}},
                "by_srcip": {"terms": {"field": "data.srcip", "size": 20}},
            },
        },
    },
    "suspicious_parent": {
        "description": "Office/browser spawning shell/script interpreter - macro-based malware delivery.",
        "mitre": "T1204.002 / T1059",
        "query": lambda since, until, agent, srcip: {
            "size": 0,
            "query": {"bool": {"filter": _base_filters(since, until, agent, srcip) + [
                {"query_string": {"query": "(winword OR excel OR powerpnt OR outlook OR chrome OR msedge) AND (cmd.exe OR powershell OR wscript OR cscript OR mshta)",
                                  "default_field": "full_log", "lenient": True}},
            ]}},
            "aggs": {
                "by_agent": {"terms": {"field": "agent.name", "size": 20}},
                "by_rule": {"terms": {"field": "rule.id", "size": 15}},
            },
        },
    },
    "dns_tunneling": {
        "description": "Abnormally long DNS queries - potential DNS tunneling / exfiltration.",
        "mitre": "T1048.001 / T1572",
        "query": lambda since, until, agent, srcip: {
            "size": 0,
            "query": {"bool": {"filter": _base_filters(since, until, agent, srcip) + [
                {"query_string": {"query": "dns AND (length OR query) AND (TXT OR MX OR CNAME OR AAAA)",
                                  "default_field": "full_log", "lenient": True}},
            ]}},
            "aggs": {
                "by_srcip": {"terms": {"field": "data.srcip", "size": 20}},
                "by_hour": {"date_histogram": {"field": "@timestamp", "fixed_interval": "1h",
                              "min_doc_count": 0, "extended_bounds": {"min": since, "max": until}}},
            },
        },
    },
    "credential_dumping": {
        "description": "Credential dumping tools - Mimikatz, comsvcs.dll, reg save SAM, /etc/shadow access.",
        "mitre": "T1003",
        "query": lambda since, until, agent, srcip: {
            "size": 0,
            "query": {"bool": {"filter": _base_filters(since, until, agent, srcip) + [
                {"query_string": {"query": "mimikatz OR (comsvcs AND MiniDump) OR (reg AND save AND SAM) OR (procdump AND lsass) OR (/etc/shadow)",
                                  "default_field": "full_log", "lenient": True}},
            ]}},
            "aggs": {
                "by_agent": {"terms": {"field": "agent.name", "size": 20}},
                "by_rule": {"terms": {"field": "rule.id", "size": 15}},
            },
        },
    },
    "lateral_movement": {
        "description": "Lateral movement - psexec, wmiexec, smbexec, winrm, SSH from unusual sources.",
        "mitre": "T1021 / T1570",
        "query": lambda since, until, agent, srcip: {
            "size": 0,
            "query": {"bool": {"filter": _base_filters(since, until, agent, srcip) + [
                {"query_string": {"query": "psexec OR wmiexec OR smbexec OR (Invoke-Command AND -ComputerName) OR (ssh AND -o StrictHostKeyChecking=no)",
                                  "default_field": "full_log", "lenient": True}},
            ]}},
            "aggs": {
                "by_srcip": {"terms": {"field": "data.srcip", "size": 30}},
                "by_dstip": {"terms": {"field": "data.dstip", "size": 20, "missing": "N/A"}},
            },
        },
    },
    "c2_beacon": {
        "description": "Regular-interval outbound connections - C2 beaconing detection. Use with 24h+ window.",
        "mitre": "T1071 / T1095",
        "query": lambda since, until, agent, srcip: {
            "size": 0,
            "query": {"bool": {"filter": _base_filters(since, until, agent, srcip) + [
                {"query_string": {"query": "(outbound OR egress) AND (beacon OR heartbeat OR keepalive OR checkin)",
                                  "default_field": "full_log", "lenient": True}},
            ]}},
            "aggs": {
                "by_srcip": {"terms": {"field": "data.srcip", "size": 30}},
                "by_hour": {"date_histogram": {"field": "@timestamp", "fixed_interval": "1h",
                              "min_doc_count": 0, "extended_bounds": {"min": since, "max": until}}},
            },
        },
    },
    "web_shells": {
        "description": "Web shell detection - suspicious PHP/ASP/JSP files, POST to unusual paths.",
        "mitre": "T1505.003",
        "query": lambda since, until, agent, srcip: {
            "size": 0,
            "query": {"bool": {"filter": _base_filters(since, until, agent, srcip) + [
                {"query_string": {"query": "(eval AND base64_decode) OR (system AND $_POST) OR (cmd.exe AND .php) OR (whoami AND .jsp)",
                                  "default_field": "full_log", "lenient": True}},
            ]}},
            "aggs": {
                "by_srcip": {"terms": {"field": "data.srcip", "size": 20}},
                "by_url": {"terms": {"field": "data.url", "size": 15, "missing": "N/A"}},
            },
        },
    },
}


def _base_filters(since: str, until: str, agent: str | None, srcip: str | None) -> list[dict]:
    """Build shared time + optional agent/srcip filter clauses."""
    filters: list[dict] = [
        {"range": {"@timestamp": {"gte": since, "lt": until,
                                   "format": "strict_date_optional_time"}}},
    ]
    if agent:
        filters.append({"match": {"agent.name": agent.strip()}})
    if srcip:
        filters.append({"bool": {"should": [
            {"match": {"data.srcip": srcip.strip()}},
            {"match_phrase": {"full_log": srcip.strip()}},
        ], "minimum_should_match": 1}})
    return filters


class ThreatHuntInput(BaseModel):
    """Input model for blueteam_threat_hunt."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    template: str = Field(
        ..., description=f"Template name. One of: {', '.join(sorted(_THREAT_HUNT_TEMPLATES))}.")
    since: str = Field(default="24h", max_length=30,
                       description="Time window start (ISO 8601 or relative like '24h', '7d').")
    until: str | None = Field(default=None, max_length=30,
                               description="Time window end. Defaults to now.")
    agent_name: ValidAgentName = Field(default=None, max_length=64,
                                        description="Optional agent name to scope the hunt.")
    srcip: str | None = Field(default=None, max_length=45,
                               description="Optional source IP to scope the hunt.")
    response_format: Literal["markdown", "json"] = Field(
        default="markdown", description="'markdown' or 'json'.")


@mcp.tool(
    name="blueteam_threat_hunt",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": False},
)
async def blueteam_threat_hunt(params: ThreatHuntInput) -> str:
    """Run a named threat hunting query against Wazuh alert data.

    Provides 11 pre-built OpenSearch aggregation queries for common adversary
    techniques. Each template targets a specific MITRE technique with optimized
    query_string syntax. Results include agent/rule/srcip breakdowns plus
    time-series histograms for pattern detection.

    **No raw DSL needed** - the LLM picks a template and the tool builds the query.

    **Templates**: encoded_powershell, lsass_access, kerberoasting,
    suspicious_scheduled_tasks, wmi_persistence, suspicious_parent,
    dns_tunneling, credential_dumping, lateral_movement, c2_beacon, web_shells.

    **Worked Examples**

    1. *Hunt for encoded PowerShell in the last 24h*:
       ``blueteam_threat_hunt(template="encoded_powershell")``

    2. *Check for credential dumping on a specific agent*:
       ``blueteam_threat_hunt(template="credential_dumping", agent_name="dc01-prod", since="7d")``

    3. *Scan lateral movement from a suspicious IP*:
       ``blueteam_threat_hunt(template="lateral_movement", srcip="10.0.1.55", since="3d")``
    """
    _audit_log("blueteam_threat_hunt", {"template": params.template})
    if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
        return json.dumps({"error": "WAZUH_INDEXER_URL and WAZUH_INDEXER_PASSWORD must be set."},
                          indent=2)

    tmpl = _THREAT_HUNT_TEMPLATES.get(params.template.strip().lower())
    if not tmpl:
        return json.dumps({
            "error": f"Unknown template '{params.template}'.",
            "available": sorted(_THREAT_HUNT_TEMPLATES),
        }, indent=2)

    since_iso, until_iso = _parse_time_window(params.since, params.until)
    body = tmpl["query"](since_iso, until_iso, params.agent_name, params.srcip)
    raw = await _wazuh_indexer_post(body)
    if "error" in raw:
        return json.dumps(raw, indent=2)

    total = raw.get("hits", {}).get("total", {}).get("value", 0)
    aggs = _redact_alert_data(raw.get("aggregations", {}))

    if params.response_format == "json":
        return json.dumps({
            "template": params.template,
            "mitre": tmpl["mitre"],
            "description": tmpl["description"],
            "window": {"since": since_iso, "until": until_iso},
            "total_matching_alerts": total,
            "aggregations": {k: v for k, v in aggs.items()},
        }, indent=2, ensure_ascii=False)

    # Build markdown summary
    lines = [
        f"# 🔍 Threat Hunt - `{params.template}`",
        "",
        f"**MITRE**: {tmpl['mitre']}",
        f"**Description**: {tmpl['description']}",
        f"**Window**: `{since_iso}` → `{until_iso}`",
        f"**Total matching alerts**: {total:,}",
        "",
    ]

    if params.agent_name:
        lines.append(f"**Agent filter**: `{params.agent_name}`")
    if params.srcip:
        lines.append(f"**Source IP filter**: `{params.srcip}`")
    lines.append("")

    # Agent breakdown
    by_agent = aggs.get("by_agent", {}).get("buckets", [])
    if by_agent:
        lines.append("## By Agent")
        lines.append("| Agent | Alerts |")
        lines.append("|-------|--------|")
        for b in by_agent[:10]:
            lines.append(f"| `{b['key']}` | {b['doc_count']:,} |")
        lines.append("")

    # Source IP breakdown
    by_srcip = aggs.get("by_srcip", {}).get("buckets", [])
    if by_srcip:
        lines.append("## By Source IP")
        lines.append("| IP | Alerts |")
        lines.append("|----|--------|")
        for b in by_srcip[:15]:
            lines.append(f"| `{b['key']}` | {b['doc_count']:,} |")
        lines.append("")

    # Rule breakdown
    by_rule = aggs.get("by_rule", {}).get("buckets", [])
    if by_rule:
        lines.append("## By Rule")
        lines.append("| Rule ID | Alerts |")
        lines.append("|---------|--------|")
        for b in by_rule[:10]:
            lines.append(f"| `{b['key']}` | {b['doc_count']:,} |")
        lines.append("")

    # Time histogram
    by_hour = aggs.get("by_hour", {}).get("buckets", [])
    if by_hour:
        lines.append("## Hourly Trend")
        max_count = max((b.get("doc_count", 0) for b in by_hour), default=1)
        for b in by_hour:
            ts = b.get("key_as_string", "?")[:16]
            count = b.get("doc_count", 0)
            bar_len = int(count / max(max_count, 1) * 30) if max_count > 0 else 0
            bar = "█" * bar_len if bar_len > 0 else "▁"
            lines.append(f"  `{ts}`  {count:>6,}  {bar}")
        lines.append("")

    # Destination IP breakdown (lateral movement only)
    by_dstip = aggs.get("by_dstip", {}).get("buckets", [])
    if by_dstip:
        lines.append("## By Destination IP")
        lines.append("| Destination | Alerts |")
        lines.append("|-------------|--------|")
        for b in by_dstip[:10]:
            lines.append(f"| `{b['key']}` | {b['doc_count']:,} |")
        lines.append("")

    # URL breakdown (web shells only)
    by_url = aggs.get("by_url", {}).get("buckets", [])
    if by_url:
        lines.append("## By URL")
        for b in by_url[:10]:
            lines.append(f"- `{b['key']}`: {b['doc_count']:,} alerts")
        lines.append("")

    if total == 0:
        lines.append("**No matches found** — this technique was not detected in the window.")

    return _truncate_if_needed("\n".join(lines))
