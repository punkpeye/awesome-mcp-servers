#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
IP comparison via 0-doc aggregations with verdict
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
from mcp_server.core.validators import ValidAgentName, ValidKeyword, ValidRuleGroups, ValidAgentId
from mcp_server.wazuh.indexer import _wazuh_indexer_post, _WAZUH_INDEX_PATTERNS
from mcp_server.wazuh.time_utils import _parse_time_window, _duration_minutes
from mcp_server.threat_intel.crowdsec import _crowdsec_request

# 1: Alert Summarization
# Auto-extracted from alert_enrichment.py - modular refactor (2026-08-11)
class AlertCompareInput(BaseModel):
    """Input model for blueteam_wazuh_alert_compare."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    srcip_a: str = Field(
        ...,
        min_length=7,
        max_length=45,
        description="First source IP to compare.",
    )
    srcip_b: str = Field(
        ...,
        min_length=7,
        max_length=45,
        description="Second source IP to compare.",
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
    response_format: Literal["markdown", "json"] = Field(
        default="markdown",
        description="Output format: 'markdown' (side-by-side) or 'json'.",
    )


@mcp.tool(
    name="blueteam_wazuh_alert_compare",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
async def blueteam_wazuh_alert_compare(params: AlertCompareInput) -> str:
    """Compare alert profiles of two source IP side-by-side.
    Fetches alert counts, top rules, max severity, MITRE tactics, and
    beacon scores for both IPs and returns a structured comparison with
    a verdict on which IP is more suspicious.
    Saves the LLM from orchestrating 4+ sequential calls to analyze two
    IPs independently.

    **Required Permissions**: Wazuh Indexer ``read`` access.

    **Worked Examples**

    1. *Compare two suspicious IPs*:
       ``blueteam_wazuh_alert_compare(srcip_a="103.107.116.202", srcip_b="185.220.101.1")``

    2. *7-day comparison*:
       ``blueteam_wazuh_alert_compare(srcip_a="10.0.0.5", srcip_b="10.0.0.99", since="7d")``
    """
    _audit_log("blueteam_wazuh_alert_compare",
               {"srcip_a": params.srcip_a, "srcip_b": params.srcip_b})
    if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
        return json.dumps({
            "error": "WAZUH_INDEXER_URL and WAZUH_INDEXER_PASSWORD must be set.",
        }, indent=2)

    since_iso, until_iso = _parse_time_window(params.since, params.until)

    async def _profile_ip(ip: str) -> dict[str, Any]:
        body = {
            "size": 0,
            "query": {
                "bool": {
                    "must": [
                        {"range": {"@timestamp": {"gte": since_iso, "lt": until_iso,
                                                 "format": "strict_date_optional_time"}}},
                        {"bool": {
                            "should": [
                                {"match": {"data.srcip": ip.strip()}},
                                {"match_phrase": {"full_log": ip.strip()}},
                            ],
                            "minimum_should_match": 1,
                        }},
                    ]
                }
            },
            "aggs": {
                "top_rules": {"terms": {"field": "rule.id", "size": 5}},
                "by_level": {
                    "range": {
                        "field": "rule.level",
                        "ranges": [
                            {"key": "low", "to": 5},
                            {"key": "medium", "from": 5, "to": 10},
                            {"key": "high", "from": 10},
                        ],
                    }
                },
                "top_agents": {"terms": {"field": "agent.name", "size": 5}},
            },
        }
        raw = await _wazuh_indexer_post(body)
        if "error" in raw:
            return {"srcip": ip, "error": raw["error"]}
        total = raw.get("hits", {}).get("total", {})
        total_val = total.get("value", 0) if isinstance(total, dict) else total
        aggs = raw.get("aggregations", {})
        return {
            "srcip": ip,
            "total_alerts": total_val,
            "top_rules": [
                {"id": b["key"], "count": b["doc_count"]}
                for b in aggs.get("top_rules", {}).get("buckets", [])
            ],
            "severity": {
                b["key"]: b["doc_count"]
                for b in aggs.get("by_level", {}).get("buckets", [])
            },
            "agents": [
                {"name": b["key"], "count": b["doc_count"]}
                for b in aggs.get("top_agents", {}).get("buckets", [])
            ],
        }

    profile_a, profile_b = await asyncio.gather(
        _profile_ip(params.srcip_a), _profile_ip(params.srcip_b),
    )

    if params.response_format == "json":
        result = {
            "window": {"since": since_iso, "until": until_iso},
            "ip_a": profile_a,
            "ip_b": profile_b,
        }
        # Determine which is more suspicious
        a_score = profile_a.get("total_alerts", 0)
        b_score = profile_b.get("total_alerts", 0)
        if a_score > b_score * 2:
            result["verdict"] = f"{params.srcip_a} is significantly more active"
        elif b_score > a_score * 2:
            result["verdict"] = f"{params.srcip_b} is significantly more active"
        else:
            result["verdict"] = "Both IPs show comparable activity levels"
        return _truncate_if_needed(json.dumps(result, indent=2, ensure_ascii=False))

    # Markdown side-by-side
    a_total = profile_a.get("total_alerts", 0)
    b_total = profile_b.get("total_alerts", 0)
    a_rules = ", ".join(f"`{r['id']}`({r['count']})"
                         for r in profile_a.get("top_rules", [])[:3]) or "-"
    b_rules = ", ".join(f"`{r['id']}`({r['count']})"
                         for r in profile_b.get("top_rules", [])[:3]) or "-"
    a_sev = profile_a.get("severity", {})
    b_sev = profile_b.get("severity", {})
    a_high = a_sev.get("high", 0)
    b_high = b_sev.get("high", 0)
    a_agents = len(profile_a.get("agents", []))
    b_agents = len(profile_b.get("agents", []))

    # Verdict
    if a_total > b_total * 2 and a_high > b_high:
        verdict = f"🔴**{params.srcip_a}** is significantly more threatening"
    elif b_total > a_total * 2 and b_high > a_high:
        verdict = f"🔴**{params.srcip_b}** is significantly more threatening"
    elif a_total > b_total:
        verdict = f"🟡**{params.srcip_a}** has more activity - investigate first"
    elif b_total > a_total:
        verdict = f"🟡**{params.srcip_b}** has more activity - investigate first"
    else:
        verdict = "🟢Both IPs show comparable activity"

    lines = [
        f"# Alert Comparison",
        "",
        f"**Window**: `{since_iso}` → `{until_iso}`",
        "",
        f"| Metric | `{params.srcip_a}` | `{params.srcip_b}` |",
        f"|--------|{'-' * (len(params.srcip_a) + 4)}|{'-' * (len(params.srcip_b) + 4)}|",
        f"| Total alerts | **{a_total}** | **{b_total}** |",
        f"| High severity (L10+) | {a_high} | {b_high} |",
        f"| Medium severity (L5-9) | {a_sev.get('medium', 0)} | {b_sev.get('medium', 0)} |",
        f"| Low severity (L1-4) | {a_sev.get('low', 0)} | {b_sev.get('low', 0)} |",
        f"| Agents targeted | {a_agents} | {b_agents} |",
        f"| Top rules | {a_rules} | {b_rules} |",
        "",
        f"### Verdict",
        f"{verdict}",
    ]

    return _truncate_if_needed("\n".join(lines))


# Geo-Aware Curated Threat Intelligence Pipeline (AUL Adjust)
# Composable filter specification - any combination of dimensions can be AND'd.
# Cross-source deduplication patterns (parent-child alert relationships).
# Each entry: (child_rule_id_regex, parent_rule_field_path_in_nested_alert)
# When deduplicate=True, child alerts matching these patterns are subtracted
# from aggregate counts to prevent double-counting.
_DEDUP_PATTERNS: list[tuple[str, str]] = [
    ("606029", "data.parameters.alert.rule.id"),  # Active Response wraps its trigger
    ("651",   "data.parameters.alert.rule.id"),   # Ossec agent-spawned alerts
]

# Maps directly to OpenSearch bool.must/filter clauses inside _build_curated_query().
class CuratedReportFilters(BaseModel):
    """Filter specification for blueteam_curated_threat_report. Every field is
    optional — only specified filters are applied. All filters are AND'd together.
    """
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    # Geo dimension
    geo_country: Optional[str] = Field(
        default=None, max_length=60,
        description="Exact match on GeoLocation.country_name, e.g. 'Indonesia'.")
    geo_country_pattern: Optional[str] = Field(
        default=None, max_length=60,
        description="Wildcard match, e.g. 'Indo*'.")

    # Domain dimension
    domain: Optional[str] = Field(
        default=None, max_length=253,
        description="Exact match on data.domain, e.g. 'bangjaka.tangerangkota.go.id'.")
    domain_pattern: Optional[str] = Field(
        default=None, max_length=253,
        description="Wildcard on data.domain, e.g. '*.tangerangkota.go.id'.")
    domain_contains: Optional[str] = Field(
        default=None, max_length=253,
        description="Substring match on data.domain, e.g. 'tangerangkota'.")

    # Rule dimension
    rule_ids: Optional[list[str]] = Field(default=None, max_length=30,
        description="Specific rule IDs, e.g. ['600029','606029'].")
    rule_level_min: Optional[int] = Field(default=None, ge=1, le=16,
        description="Minimum rule.level (severity floor).")
    rule_level_max: Optional[int] = Field(default=None, ge=1, le=16,
        description="Maximum rule.level (severity ceiling).")
    rule_groups: Optional[list[str]] = Field(default=None,
        description="Wazuh rule.groups tokens, e.g. ['recon','firewall_drop'].")
    mitre_tactics: Optional[list[str]] = Field(default=None,
        description="MITRE ATT&CK tactics, e.g. ['Discovery','Collection'].")
    mitre_techniques: Optional[list[str]] = Field(default=None,
        description="MITRE technique IDs, e.g. ['T1083','T1552'].")

    # Agent dimension
    agent_name: Optional[str] = Field(default=None, max_length=64,
        description="Target agent name, e.g. 'thezoo-prod'.")
    agent_ip: Optional[str] = Field(default=None, max_length=45,
        description="Target agent internal IP, e.g. '172.16.10.135'.")
    agent_id: ValidAgentId = Field(default=None, max_length=5,
        description="Target agent ID, e.g. '227' (zero-padded to 3 digits).")
    decoder: Optional[str] = Field(default=None, max_length=64,
        description="Decoder name, e.g. 'web-accesslog', 'ar_log_json', 'sysmon'.")

    # HTTP dimension
    url_pattern: Optional[str] = Field(default=None, max_length=1024,
        description="Wildcard on data.url, e.g. '/.vscode/*'.")
    response_codes: Optional[list[str]] = Field(default=None,
        description="HTTP response codes, e.g. ['403','404'].")
    http_methods: Optional[list[str]] = Field(default=None,
        description="HTTP methods, e.g. ['POST','PUT'].")
    user_agent_contains: Optional[str] = Field(default=None, max_length=512,
        description="Substring in data.user_agent, e.g. 'Firefox'.")
    referrer_pattern: Optional[str] = Field(default=None, max_length=1024,
        description="Wildcard on data.referrer, e.g. '*tangerangkota*'.")
    response_size_min: Optional[int] = Field(default=None, ge=0,
        description="Minimum data.response_size in bytes (exfil indicator).")
    response_size_max: Optional[int] = Field(default=None, ge=0,
        description="Maximum data.response_size in bytes.")

    # Rule description dimension
    rule_desc_contains: Optional[str] = Field(default=None, max_length=512,
        description="Substring in rule.description, e.g. 'sensitive files'.")
    rule_firedtimes_min: Optional[int] = Field(default=None, ge=1,
        description="Minimum rule.firedtimes (persistence signal — rule triggered at least N times).")
    log_source_pattern: Optional[str] = Field(default=None, max_length=512,
        description="Wildcard on location field, e.g. '/containers/*/logs/*' to filter by log source path.")

    # Geo bounding box
    geo_bbox: Optional[str] = Field(default=None, max_length=80,
        description="Geo bounding box: 'lat1,lon1,lat2,lon2' (bottom-left, top-right). "
                    "Filters GeoLocation.location within box, e.g. '-7.0,106.5,-5.5,107.0' "
                    "for Jabodetabek area. Only alerts with GeoIP data are matched.")

    # IP dimension
    srcips: Optional[list[str]] = Field(default=None, max_length=25,
        description="Specific IPs to INCLUDE (max 25).")
    exclude_srcips: Optional[list[str]] = Field(default=None, max_length=25,
        description="IPs to EXCLUDE, e.g. known scanners.")

    # Threat intel pre-filter
    min_crowdsec_reputation: Optional[str] = Field(default=None,
        description="Pre-filter: only IPs with this CrowdSec reputation "
                    "('malicious','suspicious','safe','unknown'). "
                    "Requires CROWDSEC_API_KEY and adds per-IP API calls.")


def _build_curated_query(
    since_iso: str, until_iso: str, f: CuratedReportFilters,
) -> list[dict]:
    """Translate CuratedReportFilters into OpenSearch bool.must clauses.

    Each non-None filter field becomes an AND clause. Returns a list of
    OpenSearch query/filter dicts ready for a bool.must array.
    """
    clauses: list[dict] = [
        {"range": {"@timestamp": {"gte": since_iso, "lt": until_iso,
                                   "format": "strict_date_optional_time"}}},
    ]
    # Geo
    if f.geo_country:
        clauses.append({"term": {"GeoLocation.country_name": f.geo_country.strip()}})
    if f.geo_country_pattern:
        clauses.append({"wildcard": {"GeoLocation.country_name": f.geo_country_pattern.strip()}})

    # Domain
    if f.domain:
        clauses.append({"match": {"data.domain": f.domain.strip()}})
    if f.domain_pattern:
        clauses.append({"wildcard": {"data.domain.keyword": f.domain_pattern.strip()}})
    if f.domain_contains:
        clauses.append({"wildcard": {"data.domain.keyword": f"*{f.domain_contains.strip()}*"}})

    # Rule
    if f.rule_ids:
        clauses.append({"terms": {"rule.id.keyword": [r.strip() for r in f.rule_ids]}})
    if f.rule_level_min is not None:
        clauses.append({"bool": {"should": [
            {"range": {"rule.level": {"gte": f.rule_level_min}}},
        ], "minimum_should_match": 1}})
    if f.rule_level_max is not None:
        clauses.append({"bool": {"should": [
            {"range": {"rule.level": {"lte": f.rule_level_max}}},
        ], "minimum_should_match": 1}})
    if f.rule_groups:
        clauses.append({"bool": {"should": [
            {"terms": {"rule.groups": f.rule_groups}},
            {"terms": {"rule.groups.keyword": f.rule_groups}},
        ], "minimum_should_match": 1}})
    if f.mitre_tactics:
        clauses.append({"terms": {"rule.mitre.tactic": f.mitre_tactics}})
    if f.mitre_techniques:
        clauses.append({"terms": {"rule.mitre.id": f.mitre_techniques}})

    # Agent
    if f.agent_name:
        clauses.append({"match": {"agent.name": f.agent_name.strip()}})
    if f.agent_ip:
        clauses.append({"match": {"agent.ip": f.agent_ip.strip()}})
    if f.agent_id:
        clauses.append({"match": {"agent.id": f.agent_id.strip()}})
    if f.decoder:
        clauses.append({"term": {"decoder.name": f.decoder.strip()}})

    # HTTP
    if f.url_pattern:
        clauses.append({"wildcard": {"data.url.keyword": f.url_pattern.strip()}})
    if f.response_codes:
        clauses.append({"terms": {"data.response_code": f.response_codes}})
    if f.http_methods:
        clauses.append({"terms": {"data.method": f.http_methods}})
    if f.user_agent_contains:
        clauses.append({"wildcard": {"data.user_agent.keyword":
                                     f"*{f.user_agent_contains.strip()}*"}})
    if f.referrer_pattern:
        clauses.append({"wildcard": {"data.referrer.keyword": f.referrer_pattern.strip()}})
    if f.response_size_min is not None:
        clauses.append({"range": {"data.response_size": {"gte": f.response_size_min}}})
    if f.response_size_max is not None:
        clauses.append({"range": {"data.response_size": {"lte": f.response_size_max}}})

    # Rule description free-text
    if f.rule_desc_contains:
        clauses.append({"wildcard": {"rule.description.keyword":
                                     f"*{f.rule_desc_contains.strip()}*"}})
    if f.rule_firedtimes_min is not None:
        clauses.append({"range": {"rule.firedtimes": {"gte": f.rule_firedtimes_min}}})
    if f.log_source_pattern:
        clauses.append({"wildcard": {"location.keyword": f.log_source_pattern.strip()}})

    # Geo bounding box
    if f.geo_bbox:
        parts = [p.strip() for p in f.geo_bbox.split(",")]
        if len(parts) == 4:
            try:
                lat1, lon1, lat2, lon2 = float(parts[0]), float(parts[1]), float(parts[2]), float(parts[3])
                clauses.append({"bool": {"must": [
                    {"range": {"GeoLocation.location.lat": {"gte": min(lat1, lat2), "lte": max(lat1, lat2)}}},
                    {"range": {"GeoLocation.location.lon": {"gte": min(lon1, lon2), "lte": max(lon1, lon2)}}},
                ]}})
            except ValueError:
                pass  # invalid bbox -> skip filter silently

    # IP inclusion/exclusion
    if f.srcips:
        ip_clauses = []
        for ip in f.srcips:
            ip = ip.strip()
            if ip:
                ip_clauses.append({"bool": {"should": [
                    {"match": {"data.srcip": ip}},
                    {"match_phrase": {"full_log": ip}},
                ], "minimum_should_match": 1}})
        clauses.extend(ip_clauses)
    if f.exclude_srcips:
        for ip in f.exclude_srcips:
            ip = ip.strip()
            if ip:
                clauses.append({"bool": {"must_not": {"match": {"data.srcip": ip}}}})

    return clauses


# G-2: Geo Distribution
