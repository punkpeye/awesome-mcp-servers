#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Wazuh vulnerability, syscheck (FIM), compliance, and geo heatmap tools.
"""
from __future__ import annotations
import json
from typing import Optional, Literal
from pydantic import BaseModel, ConfigDict, Field
from mcp_server import mcp, WAZUH_INDEXER_URL, WAZUH_INDEXER_PASSWORD, _REDACTION_POLICY_DESC, _REVEAL_OWNED_DESC, _FORENSIC_TOKEN_DESC
from mcp_server.core.audit import _audit_log, _truncate_if_needed
from mcp_server.core.redact import _redact_alert_data
from mcp_server.wazuh.indexer import _wazuh_indexer_post, _WAZUH_INDEX_PATTERNS
from mcp_server.wazuh.time_utils import _parse_time_window
from mcp_server.core.validators import ValidAgentName

# Vulnerability Search
class VulnerabilityInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    since: str | None = Field(default="30d", max_length=30)
    until: str | None = Field(default=None, max_length=30)
    agent_name: ValidAgentName = Field(default=None, max_length=64)
    cve: str | None = Field(default=None, max_length=20, description="Filter by CVE ID (e.g. CVE-2024-1234)")
    severity: str | None = Field(default=None, max_length=20, description="Filter by severity: Critical, High, Medium, Low")
    top_n: int = Field(default=20, ge=3, le=100)
    response_format: Literal["markdown", "json"] = Field(default="markdown")


@mcp.tool(name="blueteam_wazuh_vulnerabilities",
          annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": False})
async def blueteam_wazuh_vulnerabilities(params: VulnerabilityInput) -> str:
    """Query Wazuh vulnerability scanning results from the indexer.

    Searches ``wazuh-states-vulnerabilities-*`` index for CVE findings.
    Returns top vulnerable agents, CVE breakdown, and severity distribution.

    **Worked Examples**

    1. *All vulnerabilities last 30 days*:
       ``blueteam_wazuh_vulnerabilities()``

    2. *Filter by CVE*:
       ``blueteam_wazuh_vulnerabilities(cve="CVE-2024-6387", since="90d")``

    3. *Critical only on a specific agent*:
       ``blueteam_wazuh_vulnerabilities(severity="Critical", agent_name="dc01-prod")``
    """
    _audit_log("blueteam_wazuh_vulnerabilities", {"cve": params.cve, "severity": params.severity})
    if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
        return json.dumps({"error": "WAZUH_INDEXER_URL and WAZUH_INDEXER_PASSWORD must be set."}, indent=2)
    since_iso, until_iso = _parse_time_window(params.since, params.until)
    filters = [{"range": {"@timestamp": {"gte": since_iso, "lt": until_iso, "format": "strict_date_optional_time"}}}]
    if params.agent_name:
        filters.append({"match": {"agent.name": params.agent_name}})
    if params.cve:
        filters.append({"match": {"vulnerability.cve": params.cve.strip().upper()}})
    if params.severity:
        filters.append({"match": {"vulnerability.severity": params.severity.strip()}})
    body = {"size": 0, "query": {"bool": {"filter": filters}},
            "aggs": {"by_cve": {"terms": {"field": "vulnerability.cve", "size": params.top_n,
                                          "order": {"_count": "desc"}}},
                     "by_agent": {"terms": {"field": "agent.name", "size": params.top_n}},
                     "by_severity": {"terms": {"field": "vulnerability.severity", "size": 10}}}}
    raw = await _wazuh_indexer_post(body, index_pattern=_WAZUH_INDEX_PATTERNS["vulnerabilities"])
    if "error" in raw:
        return json.dumps(raw, indent=2)
    aggs = _redact_alert_data(raw.get("aggregations", {}))
    total = raw.get("hits", {}).get("total", {}).get("value", 0)
    if params.response_format == "json":
        return json.dumps({"total": total, "aggregations": aggs}, indent=2, ensure_ascii=False)
    lines = [f"# 🛡️ Vulnerability Scan — `{since_iso}` → `{until_iso}`", "",
             f"**Total findings**: {total:,}", ""]
    sev = aggs.get("by_severity", {}).get("buckets", [])
    if sev:
        lines.append("## Severity")
        for s in sev:
            lines.append(f"- **{s['key']}**: {s['doc_count']:,}")
        lines.append("")
    cves = aggs.get("by_cve", {}).get("buckets", [])
    if cves:
        lines.append(f"## Top CVEs ({len(cves)})")
        lines.append("| CVE | Count |")
        lines.append("|-----|-------|")
        for c in cves[:20]:
            lines.append(f"| `{c['key']}` | {c['doc_count']:,} |")
        lines.append("")
    agents = aggs.get("by_agent", {}).get("buckets", [])
    if agents:
        lines.append("## Affected Agents")
        for a in agents[:15]:
            lines.append(f"- `{a['key']}`: {a['doc_count']:,} findings")
    return _truncate_if_needed("\n".join(lines))


# Syscheck / FIM
class SyscheckInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    since: str | None = Field(default="24h", max_length=30)
    until: str | None = Field(default=None, max_length=30)
    agent_name: ValidAgentName = Field(default=None, max_length=64)
    event_type: str | None = Field(default=None, max_length=20,
                                    description="Filter: added, modified, deleted")
    path_filter: str | None = Field(default=None, max_length=256,
                                     description="Filter by file path (wildcard, e.g. '/etc/*')")
    top_n: int = Field(default=20, ge=3, le=50)
    response_format: Literal["markdown", "json"] = Field(default="markdown")


@mcp.tool(name="blueteam_wazuh_syscheck",
          annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": False})
async def blueteam_wazuh_syscheck(params: SyscheckInput) -> str:
    """Query Wazuh File Integrity Monitoring (syscheck) events from the indexer.

    Detects file changes - additions, modifications, deletions across agents.
    Essential for finding unauthorized file modifications, backdoor persistence,
    and configuration tampering.

    **Worked Examples**

    1. *All FIM events last 24h*:
       ``blueteam_wazuh_syscheck()``

    2. *Modified files under /etc/*:
       ``blueteam_wazuh_syscheck(event_type="modified", path_filter="/etc/*", since="7d")``

    3. *Deleted files on a specific agent*:
       ``blueteam_wazuh_syscheck(event_type="deleted", agent_name="web-prod", since="24h")``
    """
    _audit_log("blueteam_wazuh_syscheck", {"event_type": params.event_type, "path_filter": params.path_filter})
    if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
        return json.dumps({"error": "WAZUH_INDEXER_URL and WAZUH_INDEXER_PASSWORD must be set."}, indent=2)
    since_iso, until_iso = _parse_time_window(params.since, params.until)
    filters = [{"range": {"@timestamp": {"gte": since_iso, "lt": until_iso, "format": "strict_date_optional_time"}}}]
    if params.agent_name:
        filters.append({"match": {"agent.name": params.agent_name}})
    if params.event_type:
        filters.append({"match": {"syscheck.event": params.event_type.strip()}})
    if params.path_filter:
        filters.append({"wildcard": {"syscheck.path": params.path_filter.strip()}})
    body = {"size": 0, "query": {"bool": {"filter": filters}},
            "aggs": {"by_agent": {"terms": {"field": "agent.name", "size": params.top_n}},
                     "by_event": {"terms": {"field": "syscheck.event", "size": 3}},
                     "by_path": {"terms": {"field": "syscheck.path", "size": params.top_n,
                                           "order": {"_count": "desc"}}}}}
    raw = await _wazuh_indexer_post(body)
    if "error" in raw:
        return json.dumps(raw, indent=2)
    aggs = _redact_alert_data(raw.get("aggregations", {}))
    total = raw.get("hits", {}).get("total", {}).get("value", 0)
    if params.response_format == "json":
        return json.dumps({"total": total, "aggregations": aggs}, indent=2, ensure_ascii=False)
    lines = [f"# 📁 FIM / Syscheck — `{since_iso}` → `{until_iso}`", "",
             f"**Total events**: {total:,}", ""]
    evt = aggs.get("by_event", {}).get("buckets", [])
    if evt:
        lines.append("## Event Types")
        for e in evt:
            lines.append(f"- **{e['key']}**: {e['doc_count']:,}")
        lines.append("")
    paths = aggs.get("by_path", {}).get("buckets", [])
    if paths:
        lines.append(f"## Top Changed Paths ({len(paths)})")
        lines.append("| Path | Count |")
        lines.append("|------|-------|")
        for p in paths[:20]:
            lines.append(f"| `{p['key']}` | {p['doc_count']:,} |")
        lines.append("")
    agents = aggs.get("by_agent", {}).get("buckets", [])
    if agents:
        lines.append("## By Agent")
        for a in agents[:15]:
            lines.append(f"- `{a['key']}`: {a['doc_count']:,} events")
    if total == 0:
        lines.append("✅ No FIM events found in this window.")
    return _truncate_if_needed("\n".join(lines))


# Compliance
COMPLIANCE_FIELDS = {"cis": "rule.cis", "pci_dss": "rule.pci_dss", "gdpr": "rule.gdpr",
                      "hipaa": "rule.hipaa", "nist": "rule.nist_800_53"}

class ComplianceInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    since: str | None = Field(default="30d", max_length=30)
    until: str | None = Field(default=None, max_length=30)
    agent_name: ValidAgentName = Field(default=None, max_length=64)
    framework: str = Field(default="all", max_length=20,
                           description="Compliance framework: all, cis, pci_dss, gdpr, hipaa, nist")
    top_n: int = Field(default=20, ge=3, le=50)
    response_format: Literal["markdown", "json"] = Field(default="markdown")


@mcp.tool(name="blueteam_wazuh_compliance",
          annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": False})
async def blueteam_wazuh_compliance(params: ComplianceInput) -> str:
    """Summarize Wazuh alerts by compliance framework (CIS, PCI DSS, GDPR, HIPAA, NIST 800-53).

    Wazuh maps rules to compliance controls. This tool aggregates alerts by
    framework, showing which controls have the most findings essential for
    audit preparation and compliance gap analysis.

    **Worked Examples**

    1. *All frameworks overview*:
       ``blueteam_wazuh_compliance()``

    2. *PCI DSS only*:
       ``blueteam_wazuh_compliance(framework="pci_dss", since="90d")``

    3. *CIS on a specific agent*:
       ``blueteam_wazuh_compliance(framework="cis", agent_name="db-prod")``
    """
    _audit_log("blueteam_wazuh_compliance", {"framework": params.framework})
    if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
        return json.dumps({"error": "WAZUH_INDEXER_URL and WAZUH_INDEXER_PASSWORD must be set."}, indent=2)
    since_iso, until_iso = _parse_time_window(params.since, params.until)
    filters = [{"range": {"@timestamp": {"gte": since_iso, "lt": until_iso, "format": "strict_date_optional_time"}}}]
    if params.agent_name:
        filters.append({"match": {"agent.name": params.agent_name}})
    # Select framework fields
    if params.framework == "all":
        frameworks = list(COMPLIANCE_FIELDS.keys())
    elif params.framework in COMPLIANCE_FIELDS:
        frameworks = [params.framework]
    else:
        return json.dumps({"error": f"Unknown framework '{params.framework}'. Valid: all, {', '.join(COMPLIANCE_FIELDS)}"}, indent=2)
    aggs = {}
    if len(frameworks) > 1:
        # framework="all" -> OR the exists filters (alerts with ANY compliance mapping)
        filters.append({"bool": {"should": [{"exists": {"field": COMPLIANCE_FIELDS[fw]}}
                                             for fw in frameworks],
                                    "minimum_should_match": 1}})
    else:
        filters.append({"exists": {"field": COMPLIANCE_FIELDS[frameworks[0]]}})
    for fw in frameworks:
        aggs[f"by_{fw}"] = {"terms": {"field": COMPLIANCE_FIELDS[fw], "size": params.top_n}}
    body = {"size": 0, "query": {"bool": {"filter": filters}}, "aggs": aggs}
    raw = await _wazuh_indexer_post(body)
    if "error" in raw:
        return json.dumps(raw, indent=2)
    aggs_result = _redact_alert_data(raw.get("aggregations", {}))
    total = raw.get("hits", {}).get("total", {}).get("value", 0)
    if params.response_format == "json":
        return json.dumps({"total": total, "aggregations": aggs_result}, indent=2, ensure_ascii=False)
    lines = [f"# 📋 Compliance Summary - `{since_iso}` -> `{until_iso}`", "",
             f"**Framework**: {params.framework}", f"**Total alerts with compliance data**: {total:,}", ""]
    for fw in frameworks:
        buckets = aggs_result.get(f"by_{fw}", {}).get("buckets", [])
        if buckets:
            fw_label = fw.upper().replace("_", " ")
            lines.append(f"## {fw_label}")
            lines.append("| Control | Alerts |")
            lines.append("|---------|--------|")
            for b in buckets[:15]:
                lines.append(f"| `{b['key']}` | {b['doc_count']:,} |")
            lines.append("")
    if total == 0:
        lines.append("✅ No alerts with compliance mappings found.")
    return _truncate_if_needed("\n".join(lines))


# Geo Heatmap
class GeoHeatmapInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    since: str | None = Field(default="24h", max_length=30)
    until: str | None = Field(default=None, max_length=30)
    srcip: str | None = Field(default=None, max_length=45)
    top_n: int = Field(default=30, ge=3, le=100)
    response_format: Literal["markdown", "json"] = Field(default="markdown")
    bypass_redaction: bool = Field(default=False,
        description="Accepted for API consistency. Heatmap returns aggregates only (no raw PII).")
    redaction_policy: Optional[Literal["full", "protect_victim", "raw"]] = Field(
        default=None,
        description=_REDACTION_POLICY_DESC,
    )
    reveal_owned: bool = Field(default=False, description=_REVEAL_OWNED_DESC)
    forensic_token: Optional[str] = Field(default=None, max_length=128, description=_FORENSIC_TOKEN_DESC)


@mcp.tool(name="blueteam_wazuh_geo_heatmap",
          annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": False})
async def blueteam_wazuh_geo_heatmap(params: GeoHeatmapInput) -> str:
    """Generate attack coordinate and city-level geo heatmap data.

    Aggregates alerts by GeoLocation.city_name with latitude/longitude
    coordinates for external heatmap visualization (e.g. Leaflet, Kepler.gl).
    Returns top attacking cities with coordinates, alert counts, and IP counts.

    Args:
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.
        params.redaction_policy: 'full' (shape-based, default), 'protect_victim' (mask victim-owned indicators only), 'raw' (Layer 1 credential strip only, requires BLUETEAM_ALLOW_FORENSIC_BYPASS).
        params.reveal_owned: When true (forensic), expose emails/subdomains at owned domains (BLUETEAM_OWNED_DOMAINS) unmasked; Layer 1 credentials remain masked.
        params.forensic_token: Operator forensic token (matches BLUETEAM_FORENSIC_TOKEN); required for redaction_policy='raw' / bypass_redaction when that env is set.

    **Worked Examples**

    1. *Global attack heatmap last 24h*:
       ``blueteam_wazuh_geo_heatmap()``

    2. *Heatmap for a specific attacker IP*:
       ``blueteam_wazuh_geo_heatmap(srcip="103.166.210.53", since="7d")``

    3. *JSON output for visualization tool*:
       ``blueteam_wazuh_geo_heatmap(response_format="json")``
    """
    _audit_log("blueteam_wazuh_geo_heatmap", {"srcip": params.srcip})
    if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
        return json.dumps({"error": "WAZUH_INDEXER_URL and WAZUH_INDEXER_PASSWORD must be set."}, indent=2)
    since_iso, until_iso = _parse_time_window(params.since, params.until)
    filters = [{"range": {"@timestamp": {"gte": since_iso, "lt": until_iso, "format": "strict_date_optional_time"}}},
               {"exists": {"field": "GeoLocation.location"}}]
    if params.srcip:
        filters.append({"bool": {"should": [{"match": {"data.srcip": params.srcip.strip()}},
                                             {"match_phrase": {"full_log": params.srcip.strip()}}],
                                  "minimum_should_match": 1}})
    body = {"size": 0, "query": {"bool": {"filter": filters}},
            "aggs": {"by_city": {"terms": {"field": "GeoLocation.city_name", "size": params.top_n,
                                           "order": {"_count": "desc"}},
                                 "aggs": {"lat": {"avg": {"field": "GeoLocation.latitude"}},
                                          "lon": {"avg": {"field": "GeoLocation.longitude"}},
                                          "unique_ips": {"cardinality": {"field": "data.srcip",
                                                                         "precision_threshold": 40000}}}}}}
    raw = await _wazuh_indexer_post(body)
    if "error" in raw:
        return json.dumps(raw, indent=2)
    aggs = _redact_alert_data(raw.get("aggregations", {}), reveal_owned=params.reveal_owned)
    total = raw.get("hits", {}).get("total", {}).get("value", 0)
    buckets = aggs.get("by_city", {}).get("buckets", [])
    if params.response_format == "json":
        return json.dumps({"total": total, "cities": [
            {"city": b["key"], "alerts": b["doc_count"],
             "lat": round(b.get("lat", {}).get("value") or 0, 4),
             "lon": round(b.get("lon", {}).get("value") or 0, 4),
             "unique_ips": b.get("unique_ips", {}).get("value", 0)}
            for b in buckets
        ]}, indent=2, ensure_ascii=False)
    lines = [f"# 🗺️ Geo Heatmap - `{since_iso}` -> `{until_iso}`", "",
             f"**Total alerts with coordinates**: {total:,}", ""]
    if params.srcip:
        lines.append(f"**Source IP filter**: `{params.srcip}`")
    lines.extend(["", "| City | Alerts | Lat | Lon | Unique IPs |",
                   "|------|--------|-----|-----|------------|"])
    for b in buckets[:25]:
        lat = round(b.get("lat", {}).get("value") or 0, 2)
        lon = round(b.get("lon", {}).get("value") or 0, 2)
        ips = b.get("unique_ips", {}).get("value", 0)
        lines.append(f"| {b['key']} | {b['doc_count']:,} | {lat} | {lon} | {ips:,} |")
    if total == 0:
        lines.append("| *(no data)* | - | - | - | - |")
    return _truncate_if_needed("\n".join(lines))
