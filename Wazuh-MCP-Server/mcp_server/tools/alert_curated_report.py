#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Curated threat report - one-call filter -> aggregate -> enrich -> report pipeline
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
from mcp_server.wazuh.indexer import _wazuh_indexer_post, _WAZUH_INDEX_PATTERNS
from mcp_server.wazuh.time_utils import _parse_time_window, _duration_minutes
from mcp_server.threat_intel.crowdsec import _crowdsec_request
from mcp_server.tools.alert_compare import CuratedReportFilters, _build_curated_query

# 1: Alert Summarization
# Auto-extracted from alert_enrichment.py - modular refactor
class CuratedThreatReportInput(BaseModel):
    """Input model for blueteam_curated_threat_report."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    since: Optional[str] = Field(default="24h", max_length=30)
    until: Optional[str] = Field(default=None, max_length=30)
    filters: CuratedReportFilters = Field(default_factory=CuratedReportFilters)
    include_threat_intel: bool = Field(default=True)
    max_entities: int = Field(default=50, ge=10, le=100)
    group_by: Literal["srcip", "domain", "rule.id", "agent"] = Field(default="srcip")
    response_format: Literal["markdown", "json"] = Field(default="markdown")
    bypass_redaction: bool = Field(default=False, description=_BYPASS_REDACTION_DESC)
    redaction_policy: Optional[Literal["full", "protect_victim", "raw"]] = Field(
        default=None,
        description=_REDACTION_POLICY_DESC,
    )
    reveal_owned: bool = Field(default=False, description=_REVEAL_OWNED_DESC)
    forensic_token: Optional[str] = Field(default=None, max_length=128, description=_FORENSIC_TOKEN_DESC)
    compare_since: Optional[str] = Field(default=None, max_length=30)
    investigation_depth: Literal["summary", "enriched", "deep"] = Field(default="enriched")
    deduplicate: bool = Field(default=False)
    time_decay: Literal["none", "linear", "exponential"] = Field(default="none")
    scoring_mode: Literal["volume", "diversity"] = Field(default="volume")


@mcp.tool(
    name="blueteam_curated_threat_report",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": True},
)
async def blueteam_curated_threat_report(params: CuratedThreatReportInput) -> str:
    """Generate a geo/domain/rule-filtered threat intelligence report in one call.

    Combines alert aggregation, IP extraction, and multi-source threat intel
    enrichment into a single structured report. Replace 8-12 sequential LLM
    tool calls with one.

    **Filter dimensions** (any combination, all AND'd):
      • geo_country / geo_country_pattern - GeoLocation.country_name
      • geo_bbox - bounding box "lat1,lon1,lat2,lon2" for area filtering
      • domain / domain_pattern / domain_contains - data.domain
      • rule_ids / rule_level_min / rule_level_max / rule_groups / rule_desc_contains - rule filtering
      • mitre_tactics / mitre_techniques - ATT&CK filtering
      • agent_name / agent_ip / agent_id - target agent
      • decoder - log decoder name (web-accesslog, sysmon, etc.)
      • url_pattern / referrer_pattern / response_codes / response_size_min / response_size_max / http_methods / user_agent_contains - HTTP layer
      • rule_firedtimes_min - persistence signal
      • log_source_pattern - wildcard on location field
      • srcips (include) / exclude_srcips - IP-level
      • min_crowdsec_reputation - pre-filter by threat intel

    **Threat Intel** (best-effort, concurrent):
      Argus (7 upstream sources) + CrowdSec CTI (behaviors, MITRE, CVE) +
      AbuseIPDB (abuse score, reports) + VirusTotal (engine verdicts) +
      GreyNoise Community (scanner/business classification).

    **Required Permissions**: Wazuh Indexer read access. CROWDSEC_API_KEY for
    CrowdSec enrichment. ARGUS_API_KEY for Argus enrichment.

    Args:
        params.redaction_policy: 'full' (shape-based, default), 'protect_victim' (mask
            victim-owned indicators only), 'raw' (Layer 1 credential strip only,
            requires BLUETEAM_ALLOW_FORENSIC_BYPASS).
        params.reveal_owned: When true (forensic), expose emails/subdomains at owned
            domains (BLUETEAM_OWNED_DOMAINS) unmasked; Layer 1 credentials remain masked.
        params.forensic_token: Operator forensic token (matches BLUETEAM_FORENSIC_TOKEN);
            required for redaction_policy='raw' / bypass_redaction when that env is set.
        params.bypass_redaction: When true, skip PII/credential redaction for audit
            investigations.

    **Worked Example**

    1. *Indonesian attackers targeting .go.id domains*:
       ``blueteam_curated_threat_report(filters={"geo_country": "Indonesia", "domain_pattern": "*.go.id"})``

    2. *Critical-severity recon against thezoo-prod*:
       ``blueteam_curated_threat_report(filters={"rule_level_min": 10, "agent_name": "thezoo-prod", "rule_groups": ["recon"]})``

    3. *Visual Studio Code probing from Indonesia*:
       ``blueteam_curated_threat_report(filters={"geo_country": "Indonesia", "url_pattern": "/.vscode/*"})``

    4. *T1083 technique, 7-day window*:
       ``blueteam_curated_threat_report(since="7d", filters={"mitre_techniques": ["T1083"]})``

    5. *Exclude known scanner*:
       ``blueteam_curated_threat_report(filters={"exclude_srcips": ["203.0.113.42"]})``
    """
    _audit_log("blueteam_curated_threat_report", {"filters": str(params.filters)[:200]})
    if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
        return json.dumps({"error": "WAZUH_INDEXER_URL and WAZUH_INDEXER_PASSWORD must be set."}, indent=2)

    since_iso, until_iso = _parse_time_window(params.since, params.until)
    f = params.filters

    # 1: Aggregation query (size: 0, no documents fetched)
    clauses = _build_curated_query(since_iso, until_iso, f)

    # Time-decay weighting via function_score gauss decay on @timestamp
    query_wrapper: dict = {"bool": {"must": clauses}}
    if params.time_decay != "none":
        half_life = max(60, _duration_minutes(since_iso, until_iso) * 15)  # seconds
        decay_config = {"@timestamp": {"origin": until_iso, "scale": f"{half_life:.0f}s",
                                        "decay": 0.5}}
        query_wrapper = {
            "function_score": {
                "query": {"bool": {"must": clauses}},
                "functions": [{"gauss": decay_config}],
                "boost_mode": "replace",
            }
        }

    # Select primary aggregation axis based on group_by
    group_config: dict[str, tuple[str, str]] = {
        "srcip": ("data.srcip.keyword", "top_entities"),
        "domain": ("data.domain.keyword", "top_entities"),
        "rule.id": ("rule.id.keyword", "top_entities"),
        "agent": ("agent.name.keyword", "top_entities"),
    }
    agg_field, agg_name = group_config.get(params.group_by, group_config["srcip"])

    body = {
        "size": 0,
        "query": query_wrapper,
        "aggs": {
            agg_name: {
                "terms": {"field": agg_field, "size": params.max_entities,
                          "order": {"_count": "desc"}},
                "aggs": {
                    "first_seen": {"min": {"field": "@timestamp"}},
                    "last_seen": {"max": {"field": "@timestamp"}},
                    "max_level": {"max": {"field": "rule.level"}},
                    "top_rules": {"terms": {"field": "rule.id", "size": 5}},
                    "top_urls": {"terms": {"field": "data.url", "size": 5}},
                    "sample_geo": {"top_hits": {"size": 1, "_source": {"includes": ["GeoLocation"]}}},
                },
            },
            "total_alerts": {"value_count": {"field": "_id"}},
            "total_with_geo": {"value_count": {"field": "GeoLocation.country_name"}},
            "top_rules": {"terms": {"field": "rule.id", "size": 10}},
            "top_agents": {"terms": {"field": "agent.name", "size": 10}},
            "top_domains": {"terms": {"field": "data.domain", "size": 10}},
            "severity_bands": {
                "range": {"field": "rule.level",
                          "ranges": [{"key": "low", "to": 5},
                                     {"key": "medium", "from": 5, "to": 10},
                                     {"key": "high", "from": 10}]},
            },
        },
    }
    raw = await _wazuh_indexer_post(body)
    if "error" in raw:
        return json.dumps(raw, indent=2)

    aggs = raw.get("aggregations", {})
    total_alerts = aggs.get("total_alerts", {}).get("value", 0)
    total_with_geo = aggs.get("total_with_geo", {}).get("value", 0)
    geo_coverage_pct = round(total_with_geo / total_alerts * 100, 1) if total_alerts > 0 else 0.0
    entity_buckets = aggs.get(agg_name, {}).get("buckets", [])
    rule_buckets = aggs.get("top_rules", {}).get("buckets", [])
    rule_buckets = aggs.get("top_rules", {}).get("buckets", [])
    agent_buckets = aggs.get("top_agents", {}).get("buckets", [])
    domain_buckets = aggs.get("top_domains", {}).get("buckets", [])
    severity = {b["key"]: b["doc_count"] for b in aggs.get("severity_bands", {}).get("buckets", [])}

    # Deduplication: remove child alert wrapper counts
    dedup_note = ""
    if params.deduplicate:
        dedup_body = {
            "size": 0,
            "query": {"bool": {"must": clauses + [
                {"terms": {"rule.id": ["606029", "651"]}},
            ]}},
            "aggs": {"total_children": {"value_count": {"field": "_id"}}},
        }
        try:
            dedup_raw = await _wazuh_indexer_post(dedup_body)
            child_count = (dedup_raw.get("aggregations", {})
                          .get("total_children", {}).get("value", 0))
            total_alerts = max(0, total_alerts - child_count)
            dedup_note = f" ({child_count} Active Response wrappers deduplicated)"
        except Exception:
            dedup_note = ""

    # Compare mode: run second query for previous period
    compare_data: dict[str, Any] = {}
    if params.compare_since:
        try:
            curr_duration = _duration_minutes(since_iso, until_iso)
            window_mins = max(60, curr_duration)
            comp_since_dt = datetime.fromisoformat(since_iso.replace("Z", "+00:00").rstrip("Z"))
            comp_since_iso = (comp_since_dt - timedelta(minutes=window_mins)).strftime("%Y-%m-%dT%H:%M:%SZ")
            comp_until_iso = since_iso

            comp_clauses = _build_curated_query(comp_since_iso, comp_until_iso, f)
            comp_body = {
                "size": 0,
                "query": {"bool": {"must": comp_clauses}},
                "aggs": {
                    agg_name: {"terms": {"field": agg_field, "size": params.max_entities}},
                    "total_alerts": {"value_count": {"field": "_id"}},
                    "severity_bands": {"range": {"field": "rule.level",
                        "ranges": [{"key": "low", "to": 5},
                                   {"key": "medium", "from": 5, "to": 10},
                                   {"key": "high", "from": 10}]}},
                },
            }
            comp_raw = await _wazuh_indexer_post(comp_body)
            if "error" not in comp_raw:
                c_aggs = comp_raw.get("aggregations", {})
                compare_data = {
                    "total_alerts": c_aggs.get("total_alerts", {}).get("value", 0),
                    "entities": len(c_aggs.get(agg_name, {}).get("buckets", [])),
                    "severity": {b["key"]: b["doc_count"]
                        for b in c_aggs.get("severity_bands", {}).get("buckets", [])},
                    "window": {"since": comp_since_iso, "until": comp_until_iso},
                }
        except Exception:
            compare_data = {"error": "comparison_query_failed"}

    # min_crowdsec_reputation pre-filter (Phase 0.5)
    crowdsec_filter_note = ""
    if params.filters.min_crowdsec_reputation and entity_buckets and params.group_by == "srcip" and os.environ.get(CROWDSEC_API_KEY_ENV):
        threshold_rep = params.filters.min_crowdsec_reputation.strip()
        all_ips = [b["key"] for b in entity_buckets]
        cs_verdicts: dict[str, str] = {}
        for ip in all_ips[:50]:
            try:
                cs = await _crowdsec_request(f"/v2/smoke/{ip}")
                cs_verdicts[ip] = cs.get("reputation", "unknown")
            except Exception:
                cs_verdicts[ip] = "lookup_failed"
        before = len(entity_buckets)
        entity_buckets = [b for b in entity_buckets if cs_verdicts.get(b["key"]) == threshold_rep]
        removed = before - len(entity_buckets)
        crowdsec_filter_note = f" (CrowdSec pre-filter '{threshold_rep}': {removed} IPs removed, {len(entity_buckets)} retained)"

    # Diversity re-ranking (when scoring_mode="diversity")
    if params.scoring_mode == "diversity" and entity_buckets:
        # Score each entity by rule group diversity (Shannon entropy * alert_count)
        for b in entity_buckets:
            rule_buckets_inner = b.get("top_rules", {}).get("buckets", [])
            distinct_rules = len(rule_buckets_inner)
            alert_count = b["doc_count"]
            # Diversity score: distinct rules * log(1 + alert_count)
            # rewards multi-phase attackers with moderate volume over noisy single-rule scanners
            import math
            b["_diversity_score"] = distinct_rules * math.log(1 + alert_count)
        entity_buckets.sort(key=lambda b: b.get("_diversity_score", 0), reverse=True)

    # 2: Concurrent threat intel enrichment
    threat_data: dict[str, dict] = {}
    if params.include_threat_intel and entity_buckets and params.group_by == "srcip":
        top_ips = [b["key"] for b in entity_buckets[:min(params.max_entities, 15)]]

        async def _enrich_ip(ip: str) -> tuple[str, dict]:
            result: dict = {}
            # CrowdSec (cached)
            if os.environ.get(CROWDSEC_API_KEY_ENV):
                try:
                    cs = await _crowdsec_request(f"/v2/smoke/{ip}")
                    result["crowdsec"] = {
                        "reputation": cs.get("reputation", "unknown"),
                        "behaviors": [b.get("name", "") for b in cs.get("behaviors", [])],
                        "cves": cs.get("cves", []),
                    }
                except Exception:
                    result["crowdsec"] = {"error": "lookup_failed"}
            # Argus
            if os.environ.get(ARGUS_API_KEY_ENV):
                try:
                    argus_key = os.environ[ARGUS_API_KEY_ENV]
                    argus_resp = await _api_call("post", ARGUS_BASE_URL,
                        headers={"X-API-Key": argus_key, "Content-Type": "application/json"},
                        json={"observable": ip})
                    argus_data = argus_resp.json()
                    argus_reports = argus_data.get("results", {}).get("argus_reports", {}).get("results", {})
                    result["argus"] = {
                        "overall_score": argus_reports.get("scores", 0),
                        "sources": [k for k in argus_data.get("results", {}).keys()
                                    if argus_data["results"][k].get("success")],
                    }
                except Exception:
                    result["argus"] = {"error": "lookup_failed"}
            # AbuseIPDB
            if ABUSEIPDB_API_KEY:
                try:
                    client = await _get_client("http")
                    resp = await client.get(
                        f"{ABUSEIPDB_BASE_URL}/check",
                        headers={"Key": ABUSEIPDB_API_KEY, "Accept": "application/json"},
                        params={"ipAddress": ip, "maxAgeInDays": "90"},
                    )
                    resp.raise_for_status()
                    data = resp.json().get("data", {})
                    result["abuseipdb"] = {
                        "abuse_score": data.get("abuseConfidenceScore"),
                        "total_reports": data.get("totalReports"),
                        "country": data.get("countryCode"),
                    }
                except Exception:
                    result["abuseipdb"] = {"error": "lookup_failed"}
            # VirusTotal
            if VIRUSTOTAL_API_KEY:
                try:
                    client = await _get_client("http")
                    resp = await client.get(
                        f"{VIRUSTOTAL_BASE_URL}/ip_addresses/{ip}",
                        headers={"x-apikey": VIRUSTOTAL_API_KEY, "Accept": "application/json"},
                    )
                    resp.raise_for_status()
                    vt_data = resp.json().get("data", {}).get("attributes", {})
                    stats = vt_data.get("last_analysis_stats", {})
                    result["virustotal"] = {
                        "malicious": stats.get("malicious", 0),
                        "suspicious": stats.get("suspicious", 0),
                        "harmless": stats.get("harmless", 0),
                        "total_engines": sum(stats.values()) if stats else 0,
                    }
                except Exception:
                    result["virustotal"] = {"error": "lookup_failed"}
            return (ip, result)

        enrich_results = await asyncio.gather(*[_enrich_ip(ip) for ip in top_ips])
        threat_data = dict(enrich_results)

    # 3: Format report
    if params.response_format == "json":
        result = {
            "window": {"since": since_iso, "until": until_iso},
            "filters_applied": f.model_dump(exclude_none=True),
            "total_alerts": total_alerts,
            "severity": severity,
            "top_rules": [{"id": b["key"], "count": b["doc_count"]} for b in rule_buckets],
            "top_agents": [{"name": b["key"], "count": b["doc_count"]} for b in agent_buckets],
            "top_domains": [{"domain": b["key"], "count": b["doc_count"]} for b in domain_buckets],
            "dedup_note": dedup_note if dedup_note else None,
            "compare": compare_data if compare_data else None,
            "attackers": [
                {
                    "ip": b["key"],
                    "alerts": b["doc_count"],
                    "max_level": int(b.get("max_level", {}).get("value", 0)),
                    "first_seen": b.get("first_seen", {}).get("value_as_string", ""),
                    "last_seen": b.get("last_seen", {}).get("value_as_string", ""),
                    "top_rules": [r["key"] for r in b.get("top_rules", {}).get("buckets", [])],
                    "top_urls": list(set(u["key"] for u in b.get("top_urls", {}).get("buckets", [])))[:5],
                    "threat_intel": threat_data.get(b["key"], {}),
                }
                for b in entity_buckets[:params.max_entities]
            ],
        }
        return _truncate_if_needed(json.dumps(_redact_alert_data(result, params=params), indent=2, ensure_ascii=False))

    # Markdown report
    filter_desc_parts: list[str] = []
    for field_name in ["geo_country", "domain_pattern", "domain_contains", "rule_ids",
                        "rule_level_min", "rule_level_max", "rule_groups",
                        "rule_desc_contains", "mitre_tactics", "mitre_techniques",
                        "agent_name", "agent_ip", "agent_id", "decoder",
                        "url_pattern", "referrer_pattern",
                        "response_size_min", "response_size_max",
                        "rule_firedtimes_min", "log_source_pattern",
                        "response_codes", "http_methods", "user_agent_contains",
                        "geo_bbox", "exclude_srcips"]:
        val = getattr(f, field_name, None)
        if val:
            filter_desc_parts.append(f"`{field_name}={val}`")
    filter_desc = ", ".join(filter_desc_parts) if filter_desc_parts else "(none — all alerts)"

    lines = [
        f"# 🛡️ Curated Threat Report",
        "",
        f"**Window**: `{since_iso}` -> `{until_iso}`",
        f"**Filters**: {filter_desc}",
        "",
        "---",
        "",
        "## 📊 Executive Summary",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Total alerts matching filters | **{total_alerts:,}** |",
        f"| Unique entities | **{len(entity_buckets)}** |",
        f"| High-severity (L10+) | {severity.get('high', 0):,} |",
        f"| Medium-severity (L5-9) | {severity.get('medium', 0):,} |",
        f"| Low-severity (L1-4) | {severity.get('low', 0):,} |",
        f"| Unique rules triggered | {len(rule_buckets)} |",
        f"| Agents targeted | {len(agent_buckets)} |",
        f"| GeoIP coverage | {total_with_geo:,} of {total_alerts:,} ({geo_coverage_pct}%) |",
        f"| Dedup note | {dedup_note or 'none'} |",
        f"| CrowdSec filter | {crowdsec_filter_note or 'none'} |",
        "",
    ]
    # Comparison delta table
    if compare_data and "error" not in compare_data:
        prev_total = compare_data.get("total_alerts", 0)
        delta = total_alerts - prev_total
        delta_pct = (delta / prev_total * 100) if prev_total > 0 else float("inf")
        arrow = "↑" if delta > 0 else "↓" if delta < 0 else "—"
        lines.append("")
        lines.append("## 📈 Comparison vs Previous Period")
        lines.append("")
        lines.append("| Metric | Current | Previous | Δ |")
        lines.append("|--------|---------|----------|---|")
        lines.append(f"| Total alerts | {total_alerts:,} | {prev_total:,} | {delta:+,} ({delta_pct:+.0f}%) {arrow} |")
        prev_entities = compare_data.get("entities", 0)
        e_delta = len(entity_buckets) - prev_entities
        lines.append(f"| Unique entities | {len(entity_buckets)} | {prev_entities} | {e_delta:+} |")
        prev_sev = compare_data.get("severity", {})
        for sev_key in ["high", "medium", "low"]:
            cur_s = severity.get(sev_key, 0)
            prev_s = prev_sev.get(sev_key, 0)
            s_delta = cur_s - prev_s
            lines.append(f"| {sev_key.title()} severity | {cur_s:,} | {prev_s:,} | {s_delta:+,} |")
        lines.append("")

    # Top entities table - heading changes based on group_by
    entity_labels: dict[str, str] = {
        "srcip": ("🔴 Top Attackers", "IP", "Alerts"),
        "domain": ("🌐 Top Targeted Domains", "Domain", "Alerts"),
        "rule.id": ("🔥 Top Rules Triggered", "Rule ID", "Alerts"),
        "agent": ("🖥️ Most Targeted Agents", "Agent", "Alerts"),
    }
    section_title, col_name, col_alerts = entity_labels.get(params.group_by, entity_labels["srcip"])

    if entity_buckets:
        lines.append(f"## {section_title}")
        lines.append("")
        if params.group_by == "srcip":
            lines.append(f"| {col_name} | {col_alerts} | Max Lvl | Threat Intel | Top Rules | First → Last |")
            lines.append("|----|--------|---------|-------------|-----------|-------------|")
            for b in entity_buckets[:30]:
                key = b["key"]
                alerts = b["doc_count"]
                lvl = int(b.get("max_level", {}).get("value", 0))
                rules = ", ".join(f"`{r['key']}`" for r in b.get("top_rules", {}).get("buckets", [])[:2])
                fst = (b.get("first_seen", {}).get("value_as_string", "") or "")[:19]
                lst = (b.get("last_seen", {}).get("value_as_string", "") or "")[:19]
                ti = threat_data.get(key, {})
                ti_parts = []
                cs = ti.get("crowdsec", {})
                if cs and "error" not in cs:
                    ti_parts.append(f"CS:`{cs.get('reputation','?')}`")
                arg = ti.get("argus", {})
                if arg and "error" not in arg and arg.get("overall_score"):
                    ti_parts.append(f"Arg:{arg['overall_score']}")
                ab = ti.get("abuseipdb", {})
                if ab and "error" not in ab and ab.get("abuse_score") is not None:
                    ti_parts.append(f"AB:{ab['abuse_score']}%")
                vt = ti.get("virustotal", {})
                if vt and "error" not in vt:
                    ti_parts.append(f"VT:{vt.get('malicious',0)}/{vt.get('total_engines',0)}")
                ti_str = " ".join(ti_parts) if ti_parts else "-"
                lines.append(f"| `{key}` | {alerts:,} | {lvl} | {ti_str} | {rules} | {fst} → {lst} |")
        else:
            lines.append(f"| {col_name} | {col_alerts} | Top Rules | First → Last |")
            lines.append("|----|--------|-----------|-------------|")
            for b in entity_buckets[:30]:
                key = b["key"]
                alerts = b["doc_count"]
                rules = ", ".join(f"`{r['key']}`" for r in b.get("top_rules", {}).get("buckets", [])[:3])
                fst = (b.get("first_seen", {}).get("value_as_string", "") or "")[:19]
                lst = (b.get("last_seen", {}).get("value_as_string", "") or "")[:19]
                lines.append(f"| `{key}` | {alerts:,} | {rules} | {fst} → {lst} |")

    if rule_buckets:
        lines.append("")
        lines.append("## 🔥 Top Rules")
        for b in rule_buckets:
            lines.append(f"- `{b['key']}` — {b['doc_count']:,} alerts")

    if domain_buckets:
        lines.append("")
        lines.append("## 🌐 Top Targeted Domains")
        for b in domain_buckets[:10]:
            lines.append(f"- `{b['key']}` — {b['doc_count']:,} alerts")

    if agent_buckets:
        lines.append("")
        lines.append("## 🖥️ Most Targeted Agents")
        for b in agent_buckets[:10]:
            lines.append(f"- `{b['key']}` — {b['doc_count']:,} alerts")

    lines.append("")
    lines.append("## 🛠️ Recommended Actions")

    high_entities = [b for b in entity_buckets if int(b.get("max_level", {}).get("value", 0)) >= 10]
    if high_entities:
        lines.append(f"1. 🚨 {len(high_entities)} entities triggered critical-severity rules — initiate incident response")
    for b in entity_buckets[:5]:
        ip = b["key"]
        ti = threat_data.get(ip, {})
        cs = ti.get("crowdsec", {})
        if cs and cs.get("reputation") == "malicious":
            lines.append(f"2. Block `{ip}` — confirmed malicious by CrowdSec")
            break
    else:
        lines.append("2. Review top-10 IPs in external threat intel platforms for confirmation")
    lines.append(f"3. Total {len(entity_buckets)} unique entities — add high-severity offenders to watchlist")

    # Deep investigation: auto-chain attack chain analysis
    if params.investigation_depth == "deep" and entity_buckets and params.group_by == "srcip":
        deep_ips = []
        for b in entity_buckets[:10]:
            key = b["key"]
            lvl = int(b.get("max_level", {}).get("value", 0))
            ti = threat_data.get(key, {})
            cs = ti.get("crowdsec", {})
            if lvl >= 10 or (cs.get("reputation") == "malicious" and "error" not in cs):
                deep_ips.append(key)

        if deep_ips:
            lines.append("")
            lines.append("## 🔬 Deep Investigation (Auto-Chained)")
            lines.append("")
            lines.append(f"*{len(deep_ips)} qualifying IPs (max_level≥10 or CrowdSec=malicious)*")
            lines.append("")

            async def _chain_for_ip(ip):
                cbody = {"size": 500, "sort": [{"@timestamp": {"order": "asc"}}],
                    "query": {"bool": {"must": [
                        {"range": {"@timestamp": {"gte": since_iso, "lt": until_iso,
                                                 "format": "strict_date_optional_time"}}},
                        {"bool": {"should": [{"match": {"data.srcip": ip}},
                                            {"match_phrase": {"full_log": ip}}],
                                  "minimum_should_match": 1}},
                    ]}},
                    "_source": ["@timestamp", "rule.id", "rule.description"]}
                cr = await _wazuh_indexer_post(cbody)
                if "error" in cr:
                    return (ip, None)
                hits = cr.get("hits", {}).get("hits", [])
                rule_seq = [str(h.get("_source", {}).get("rule", {}).get("id", "?")) for h in hits]
                # compress consecutive duplicates
                comp = []
                for r in rule_seq:
                    if not comp or r != comp[-1]:
                        comp.append(r)
                rc = Counter(rule_seq)
                return (ip, {"total": len(hits), "chain": comp[:15], "top": rc.most_common(4)})

            chain_results = await asyncio.gather(*[_chain_for_ip(ip) for ip in deep_ips])
            for ip, ci in chain_results:
                if ci is None:
                    continue
                lines.append(f"### `{ip}`")
                lines.append(f"- Alerts: {ci['total']} | Chain: `{' → '.join(ci['chain'][:10])}`")
                top_str = ", ".join(f"`{r}`({c})" for r, c in ci["top"][:4])
                lines.append(f"- Top rules: {top_str}")
                lines.append("")

    lines.append("")
    lines.append("---")
    lines.append(f"*Report generated by blue_team_mcp (Wazuh Ft. AI by TangerangKota-CSIRT) at {datetime.utcnow().isoformat()[:19]}Z*")

    return _truncate_if_needed(_redact_alert_data("\n".join(lines), params=params))
