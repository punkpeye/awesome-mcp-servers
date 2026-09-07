#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
3-Sum correlation orchestrator, IP investigation, aggregate analysis, enrichment
"""
import json, asyncio, time, math, os
from datetime import datetime, timedelta
from typing import Optional, Literal, Any
from collections import Counter
from pydantic import field_validator, BaseModel, ConfigDict, Field
from mcp_server import (mcp, WAZUH_INDEXER_URL, WAZUH_INDEXER_PASSWORD, _WAZUH_INDEXER_MAX_SIZE,
                        _INVESTIGATION_HISTORY_FILE, CROWDSEC_API_KEY_ENV, ARGUS_API_KEY_ENV,
                        _BYPASS_REDACTION_DESC, _REDACTION_POLICY_DESC, _REVEAL_OWNED_DESC, _FORENSIC_TOKEN_DESC)
from mcp_server.core.audit import _audit_log, _truncate_if_needed, _escape_md_table
from mcp_server.core.http_client import _api_call, _handle_api_error, ValidPublicIp
from mcp_server.core.redact import _redact_alert_data
from mcp_server.core.constants import MITRE_TACTIC_TO_CATEGORY
from mcp_server.core.validators import ValidAgentName, ValidRuleGroups, ValidKeyword
from mcp_server.wazuh.indexer import _wazuh_indexer_post, _wazuh_indexer_msearch, _WAZUH_INDEX_PATTERNS, _KEYWORD_SEARCH_FIELDS, _SRCIP_FIELD_PATHS
from mcp_server.wazuh.time_utils import _parse_time_window, _auto_bucket_interval, _duration_minutes
from mcp_server.threat_intel.crowdsec import _crowdsec_request
from mcp_server.core.attacker_registry import register_attacker_ioc, register_attacker_ips
from mcp_server.core.ioc_store import record_iocs
from mcp_server.tools.investigation_history import _read_history
from mcp_server.correlation.three_sum_core import (evaluate_engine_a, evaluate_engine_b, format_evaluation_dict,
    normalize_srcip_to_cidr, DEFAULT_THRESHOLD_SCORE, DEFAULT_Z_THRESHOLD, DEFAULT_WINDOW_MINUTES,
    DEFAULT_SPARSE_FLOOR, evaluate_baseline_drift, evaluate_multi_resolution, _MULTI_RES_TIERS)

# IOC limit for attack-graph cluster context
_GRAPH_MAX_IOCS = 500
# Engine A graph-integration boost factors
_PPR_BOOST_FACTOR = 5.0      # total += ppr_score * factor
_CONFIRMED_BONUS = 2.0       # flat bonus for registry confirmed attacker IOCs

# MITRE ATT&CK dynamic classification helpers (three_sum_core)
from mcp_server.correlation.three_sum_core import (tactics_for_category,
    compute_mitre_risk, category_default_weight, build_category_techniques,
    compute_technique_risk)
from mcp_server.core.false_positive_kb import false_positive_iocs
from mcp_server.core import case_store

async def _build_cluster_context() -> dict:
    """Attack-graph context for Engine A: cluster_map, ppr_scores, confirmed_ips.
    Built from the IOC store + attacker registry (store-backed, no indexer needed):
      - cluster_map: {ip: {cluster member IPs}} for multi-node co-occurrence clusters
      - ppr_scores: personalized-PageRank suspicion scores (confirmed-seeded)
      - confirmed_ips: registry-confirmed attacker IOCs
    """
    from mcp_server.core.attack_graph import (build_attack_graph, extract_clusters,
                                              suspicion_rank)
    G = await build_attack_graph(since_days=30, min_count=1,
                                 max_iocs=_GRAPH_MAX_IOCS, include_stix=False)
    cluster_map: dict[str, set[str]] = {}
    for comp in extract_clusters(G):
        members = set(comp)
        for m in members:
            cluster_map[m] = members
    ranked = suspicion_rank(G, top_n=_GRAPH_MAX_IOCS)
    ppr_scores = {r["ioc"]: r["score"] for r in ranked if r.get("kind") == "ip"}
    confirmed_ips = {n for n, d in G.nodes(data=True) if d.get("confirmed")}
    return {"cluster_map": cluster_map, "ppr_scores": ppr_scores,
            "confirmed_ips": confirmed_ips}


async def _load_mitre_technique_map() -> dict[str, list[str]]:
    """Resolve technique ID -> [tactic names] from the MITRE ATT&CK STIX bundle.
    Reads the enterprise-attack.json kill_chain_phases (via the cached loader in
    stix_correlation) so technique classification tracks ATT&CK framework updates
    with no code change. Returns {} on any load failure (classification degrades
    gracefully to rule.mitre.tactic + rule.groups only).
    """
    from mcp_server.tools import stix_correlation as stix
    await asyncio.to_thread(stix._load_stix)
    if stix._stix_error or not stix._stix_data:
        return {}
    technique_tactics: dict[str, list[str]] = {}
    for ap in stix._stix_data.get("by_type", {}).get("attack-pattern", []):
        eid = stix._mitre_id(ap)
        if not eid:
            continue
        for kcp in ap.get("kill_chain_phases", []):
            if kcp.get("kill_chain_name") == "mitre-attack":
                t = (kcp.get("phase_name") or "").strip()
                if t and t not in technique_tactics.get(eid, []):
                    technique_tactics.setdefault(eid, []).append(t)
    return technique_tactics


# Wazuh Indexer index patterns (OpenSearch)
# Correlation tools (hand-migrated)
import json, asyncio, time, math
from datetime import datetime, timedelta
from pydantic import BaseModel, ConfigDict, Field, field_validator
from mcp_server import (WAZUH_INDEXER_URL, WAZUH_INDEXER_PASSWORD, _WAZUH_INDEXER_MAX_SIZE,
                        CROWDSEC_API_KEY_ENV, ARGUS_API_KEY_ENV, _INVESTIGATION_HISTORY_FILE,
                        _BYPASS_REDACTION_DESC, _REDACTION_POLICY_DESC, _REVEAL_OWNED_DESC, _FORENSIC_TOKEN_DESC)
from mcp_server.core.audit import _audit_log, _truncate_if_needed, _escape_md_table
from mcp_server.core.http_client import _api_call, _handle_api_error
from mcp_server.core.constants import MITRE_TACTIC_TO_CATEGORY, _last_eval_time, _last_eval_result
from mcp_server.core.validators import ValidAgentName, ValidRuleGroups, ValidKeyword
from mcp_server.wazuh.indexer import _wazuh_indexer_post, _wazuh_indexer_msearch, _WAZUH_INDEX_PATTERNS, _KEYWORD_SEARCH_FIELDS, _SRCIP_FIELD_PATHS
from mcp_server.wazuh.time_utils import _parse_time_window, _auto_bucket_interval, _duration_minutes
from mcp_server.threat_intel.crowdsec import _crowdsec_request
from mcp_server.core.attacker_registry import register_attacker_ioc, register_attacker_ips
from mcp_server.core.ioc_store import record_iocs
from mcp_server.core.tool_decorator import blueteam_tool
from mcp_server.correlation.three_sum_core import (evaluate_engine_a, evaluate_engine_b, format_evaluation_dict,
    normalize_srcip_to_cidr, DEFAULT_THRESHOLD_SCORE, DEFAULT_Z_THRESHOLD, DEFAULT_WINDOW_MINUTES,
    DEFAULT_SPARSE_FLOOR, evaluate_baseline_drift, evaluate_multi_resolution, _MULTI_RES_TIERS)


# Aggregate Analysis
class AggregateAnalysisInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    mode: str = Field(default="summary")
    since: Optional[str] = Field(default="24h", max_length=30)
    until: Optional[str] = Field(default=None, max_length=30)
    agent_name: ValidAgentName = Field(default=None, max_length=64)
    rule_groups: ValidRuleGroups = Field(default=None)
    rule_level_min: Optional[int] = Field(default=None, ge=1, le=16)
    keyword: ValidKeyword = Field(default=None, max_length=1024)
    top_n: int = Field(default=10, ge=3, le=50)
    rule_cis: ValidRuleGroups = Field(default=None, description="Filter by CIS benchmark (e.g. '1.1.1,2.2.2')")
    rule_pci_dss: ValidRuleGroups = Field(default=None, description="Filter by PCI DSS requirement")
    rule_gdpr: ValidRuleGroups = Field(default=None, description="Filter by GDPR article")
    rule_hipaa: ValidRuleGroups = Field(default=None, description="Filter by HIPAA control")
    rule_nist_800_53: ValidRuleGroups = Field(default=None, description="Filter by NIST 800-53 control")
    response_format: str = Field(default="markdown")
    redaction_policy: Optional[Literal["full", "protect_victim", "raw"]] = Field(
        default=None,
        description=_REDACTION_POLICY_DESC,
    )
    reveal_owned: bool = Field(default=False, description=_REVEAL_OWNED_DESC)
    forensic_token: Optional[str] = Field(default=None, max_length=128, description=_FORENSIC_TOKEN_DESC)
    bypass_redaction: bool = Field(default=False)

    @field_validator("mode")
    @classmethod
    def validate_mode(cls, v):
        if v.strip().lower() not in ("topology","anomaly","correlation","trend","summary"):
            raise ValueError("mode must be: topology, anomaly, correlation, trend, summary. "
                             "For top rules/srcips/agents by keyword, use blueteamWazuhIndexerSearch "
                             "or wazuhAlertFocusedCrawl instead.")
        return v.strip().lower()


@mcp.tool(
    name="wazuh_alert_aggregate_analysis",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": False}
)
async def wazuh_alert_aggregate_analysis(params: AggregateAnalysisInput) -> str:
    """Zero-doc statistical analysis of Wazuh alerts across the full index.

    Args:
        params.redaction_policy: 'full' (shape-based, default), 'protect_victim' (mask victim-owned indicators only), 'raw' (Layer 1 credential strip only, requires BLUETEAM_ALLOW_FORENSIC_BYPASS).
        params.reveal_owned: When true (forensic), expose emails/subdomains at owned domains (BLUETEAM_OWNED_DOMAINS) unmasked; Layer 1 credentials remain masked.
        params.forensic_token: Operator forensic token (matches BLUETEAM_FORENSIC_TOKEN); required for redaction_policy='raw' / bypass_redaction when that env is set.
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.
    """
    _audit_log("wazuh_alert_aggregate_analysis", {"mode": params.mode})
    if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
        return json.dumps({"error": "WAZUH_INDEXER_URL and WAZUH_INDEXER_PASSWORD must be set."}, indent=2)
    since_str, until_str = _parse_time_window(params.since, params.until)
    filters = [{"range": {"@timestamp": {"gte": since_str, "lt": until_str, "format": "strict_date_optional_time"}}}]
    if params.agent_name: filters.append({"match": {"agent.name": params.agent_name}})
    if params.rule_groups:
        groups = [g.strip() for g in params.rule_groups.split(",") if g.strip()]
        if groups: filters.append({"terms": {"rule.groups": groups}})
    if params.rule_level_min is not None: filters.append({"range": {"rule.level": {"gte": params.rule_level_min}}})
    compliance_fields = []
    for field, param in [("rule.cis", params.rule_cis), ("rule.pci_dss", params.rule_pci_dss),
                          ("rule.gdpr", params.rule_gdpr), ("rule.hipaa", params.rule_hipaa),
                          ("rule.nist_800_53", params.rule_nist_800_53)]:
        if param:
            vals = [v.strip() for v in param.split(",") if v.strip()]
            if vals:
                filters.append({"terms": {field: vals}})
            else:
                filters.append({"exists": {"field": field}})
                compliance_fields.append(field)
    if params.keyword:
        k = params.keyword.strip()
        parts = [f'{f}: ({k})^{b}' if b else f'{f}: ({k})' for f, b in _KEYWORD_SEARCH_FIELDS[:8]]
        filters.append({"query_string": {"query": " OR ".join(parts), "default_operator": "AND", "lenient": True}})
    body = {"size": 0, "query": {"bool": {"filter": filters}},
            "aggs": {"top_srcips": {"terms": {"field": "data.srcip", "size": params.top_n}},
                     "top_rules": {"terms": {"field": "rule.id", "size": params.top_n}},
                     "top_agents": {"terms": {"field": "agent.name", "size": params.top_n}},
                     "severity_bands": {"range": {"field": "rule.level",
                         "ranges": [{"key":"low","to":5},{"key":"medium","from":5,"to":10},{"key":"high","from":10}]}}}}
    # Add compliance breakdown aggregations if any compliance fields active
    for cf in compliance_fields:
        body["aggs"][f"compliance_{cf.split('.')[-1]}"] = {"terms": {"field": cf, "size": 20}}
    raw = await _wazuh_indexer_post(body)
    if "error" in raw: return json.dumps(raw, indent=2)

    # AUTO-FALLBACK: this deployment's `string_as_keyword` dynamic template maps
    # strings to PLAIN `keyword` (no `.keyword` sub-field). If the .keyword
    # aggregations return empty buckets while documents exist, retry with the
    # plain field names (prevents the silent empty-bucket false-negative).
    aggs = raw.get("aggregations", {})
    total = raw.get("hits", {}).get("total", {}).get("value", 0)
    buckets_empty = (
        not aggs.get("top_srcips", {}).get("buckets")
        and not aggs.get("top_rules", {}).get("buckets")
        and not aggs.get("top_agents", {}).get("buckets")
    )
    if total > 0 and buckets_empty:
        # Retry with plain keyword field names (no .keyword suffix)
        body["aggs"]["top_srcips"] = {"terms": {"field": "data.srcip", "size": params.top_n}}
        body["aggs"]["top_rules"] = {"terms": {"field": "rule.id", "size": params.top_n}}
        body["aggs"]["top_agents"] = {"terms": {"field": "agent.name", "size": params.top_n}}
        raw2 = await _wazuh_indexer_post(body)
        if "error" not in raw2:
            raw = raw2
            aggs = raw.get("aggregations", {})
            total = raw.get("hits", {}).get("total", {}).get("value", 0)
    if params.response_format == "json":
        return _truncate_if_needed(json.dumps({"total": total, "aggregations": aggs}, indent=2))
    sev = {b["key"]: b["doc_count"] for b in aggs.get("severity_bands", {}).get("buckets", [])}
    lines = [f"# Aggregate Analysis ({params.mode})", "", f"**Total alerts**: {total:,}", "",
             "## Severity", f"- Low: {sev.get('low',0):,}", f"- Medium: {sev.get('medium',0):,}",
             f"- High: {sev.get('high',0):,}", "", "## Top Source IPs"]
    for b in aggs.get("top_srcips", {}).get("buckets", [])[:10]:
        lines.append(f"- `{b['key']}`: {b['doc_count']:,}")
    return _truncate_if_needed("\n".join(lines))


# Three-Sum Correlation
class ThreeSumCorrelationInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    engine_a_enabled: bool = Field(default=True)
    engine_b_enabled: bool = Field(default=True)
    time_window_minutes: int = Field(default=DEFAULT_WINDOW_MINUTES, ge=5)
    threshold_score: int = Field(default=DEFAULT_THRESHOLD_SCORE, ge=6, le=200,
        description="Engine A trigger threshold (rule.level x MITRE tactic weight, summed across A/B/C). "
                    "Default 35 ~ requires a cross-category chain or multiple high-severity alerts; "
                    "a single C2 alert (~25-32) stays below it.")
    z_score_threshold: float = Field(default=DEFAULT_Z_THRESHOLD, ge=1.0, le=5.0)
    response_format: str = Field(default="markdown")
    throttle: int = Field(default=0, ge=0)
    use_mitre: bool = Field(default=True,
        description="Primary: classify alerts dynamically from the MITRE ATT&CK STIX bundle. "
                    "rule.mitre.tactic maps via MITRE_TACTIC_TO_CATEGORY; rule.mitre.id "
                    "(technique) resolves to a tactic via the STIX kill_chain_phases. "
                    "rule.groups is only a fallback for alerts with no MITRE data. "
                    "False = legacy rule.groups-only matching.")
    category_a_groups: list[str] = Field(default=["web","attack","scan","recon","accesslog"],
        description="Fallback rule.groups tokens for Category A (recon) - used ONLY when an "
                    "alert has no rule.mitre.tactic.")
    category_b_groups: list[str] = Field(default=["authentication_failures","bruteforce","blocklist","zimbra","spam","postfix"],
        description="Fallback rule.groups tokens for Category B (access anomaly).")
    category_c_groups: list[str] = Field(default=["firewall_drop","exfiltration","overflow","opencti","backdoor","defacement"],
        description="Fallback rule.groups tokens for Category C (c2/exfil).")
    category_a_label: str = Field(default="recon")
    category_b_label: str = Field(default="access_anomaly")
    category_c_label: str = Field(default="c2_exfil")
    cidr_normalize: bool = Field(default=False)
    exclude_srcips: list[str] = Field(default=[])
    follow_up: str = Field(default="none")
    create_case: bool = Field(default=False,
        description="When Engine A triggers, auto-create a case (blueteam_case_*) seeded with "
                    "the trigger IPs so the investigation persists as an incident record.")
    use_attack_graph: bool = Field(default=False,
        description="Consume the attack graph: cluster-aware category intersection "
                    "(campaign-level APT detection - a cluster spanning all 3 categories "
                    "triggers even when no single IP does), PPR suspicion boost, and "
                    "registry-confirmed IOC bonus.")
    engine_b_sparse_floor: int = Field(default=10, ge=0,
        description="Engine B sparse-category guard: sources with fewer total events than "
                    "this floor contribute Z=0 (prevents single-event spikes in quiet "
                    "categories from driving detections). 0 disables.")
    engine_b_use_mad: bool = Field(default=False,
        description="Use Median Absolute Deviation for Z-scores instead of mean/stddev. "
                    "More robust to bursty alert volumes from maintenance windows.")
    engine_b_shoulder_ratio: float = Field(default=0.6, ge=0.0, le=1.0,
        description="Adjacent-bucket confirmation ratio for Engine B. A Z-score spike must "
                    "have at least one adjacent bucket with Z >= threshold x ratio. "
                    "Filters single-bucket noise. 0 disables.")
    cat_a_weight: float = Field(default=1.0, ge=0.0, le=10.0,
        description="Optional per-category scalar on top of dynamic MITRE tactic weighting "
                    "(default 1.0 = no extra weighting).")
    cat_b_weight: float = Field(default=1.0, ge=0.0, le=10.0,
        description="Optional per-category scalar for Category B.")
    cat_c_weight: float = Field(default=1.0, ge=0.0, le=10.0,
        description="Optional per-category scalar for Category C (strongest APT signal).")
    bypass_redaction: bool = Field(default=False,
        description="Accepted for API consistency. 3-Sum returns computed scores, not raw alert PII.")
    redaction_policy: Optional[Literal["full", "protect_victim", "raw"]] = Field(
        default=None,
        description=_REDACTION_POLICY_DESC,
    )
    reveal_owned: bool = Field(default=False, description=_REVEAL_OWNED_DESC)
    forensic_token: Optional[str] = Field(default=None, max_length=128, description=_FORENSIC_TOKEN_DESC)
    multi_resolution: bool = Field(default=False)
    cross_agent: bool = Field(
        default=False,
        description="When true, correlate alerts by (srcip x agent.name) instead of srcip only. "
                    "Detects lateral movement where same IP targets multiple agents.",
    )


_three_sum_global_throttle = {"time": 0.0, "result": None}


@blueteam_tool(
    name="three_sum_correlation",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def three_sum_correlation(params: ThreeSumCorrelationInput) -> str:
    """Evaluate 3-Sum APT detection across 3 Wazuh alert categories.

    **Engine A - Multi-IoC Risk Thresholding**: Finds source IPs appearing in
    all 3 alert categories, sums per-category risk scores, and flags those
    exceeding ``threshold_score``.

    **Engine B - 3-Source Volumetric Z-Score**: Queries per-minute alert
    counts for all 3 categories, computes rolling μ/σ, and flags buckets
    where all 3 simultaneously exceed ``z_score_threshold``.

    **follow_up**: When set to ``"threat_intel"``, automatically enriches
    the top 10 trigger IPs with CrowdSec and ThreatFox lookups.
    """
    if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
        return {"error": "WAZUH_INDEXER_URL and WAZUH_INDEXER_PASSWORD must be set."}
    start_time = time.monotonic()

    # Throttle gate
    if params.throttle > 0 and _three_sum_global_throttle["time"] > 0:
        elapsed = start_time - _three_sum_global_throttle["time"]
        if elapsed < params.throttle:
            return dict(_three_sum_global_throttle["result"] or {})

    # Feedback loop: auto-exclude FP-verified IPs from the investigation history
    # and the false-positive knowledge base (a dedicated, TTL suppression set).
    exclude_set: set[str] = set(params.exclude_srcips or [])
    if _INVESTIGATION_HISTORY_FILE:
        try:
            history = _read_history()
            for ip, entry in history.items():
                if entry.get("verdict") == "false_positive":
                    exclude_set.add(ip)
        except Exception:
            pass
    try:
        exclude_set |= false_positive_iocs()
    except Exception:
        pass

    # Time window
    since_dt = datetime.utcnow() - timedelta(minutes=params.time_window_minutes)
    until_dt = datetime.utcnow()
    since_iso = since_dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    until_iso = until_dt.strftime("%Y-%m-%dT%H:%M:%SZ")

    categories = [("A", params.category_a_label, params.category_a_groups),
                  ("B", params.category_b_label, params.category_b_groups),
                  ("C", params.category_c_label, params.category_c_groups)]

    # Dynamic MITRE technique -> tactic resolution from the ATT&CK STIX bundle.
    technique_tactics: dict[str, list[str]] = {}
    category_techniques: dict[str, list[str]] = {"A": [], "B": [], "C": []}
    if params.use_mitre:
        technique_tactics = await _load_mitre_technique_map()
        category_techniques = build_category_techniques(technique_tactics)

    # Shared query builder (Engine A + B). MITRE-first: rule.mitre.tactic is the
    # primary axis (via MITRE_TACTIC_TO_CATEGORY); rule.mitre.id (technique) is
    # resolved through the STIX kill_chain_phases; rule.groups is a fallback only
    # for alerts carrying no MITRE data at all.
    def _tactic_terms(category: str) -> list[str]:
        variants: list[str] = []
        for t in tactics_for_category(category):
            variants += [t, t.lower(), t.lower().replace(" ", "-")]
        return variants

    def _build_filter(category: str, groups: list[str], since: str = since_iso,
                      until: str = until_iso) -> dict:
        if params.use_mitre:
            mitre_clauses = [
                {"terms": {"rule.mitre.tactic": _tactic_terms(category)}},
                {"terms": {"rule.mitre.tactic.keyword": _tactic_terms(category)}},
            ]
            # Technique-ID classification (STIX-resolved), applied only when the
            # alert lacks a tactic annotation (tactic takes precedence).
            tech_ids = category_techniques.get(category, [])
            if tech_ids:
                mitre_clauses.append({"bool": {
                    "must": [{"bool": {"should": [
                        {"terms": {"rule.mitre.id": tech_ids}},
                        {"terms": {"rule.mitre.id.keyword": tech_ids}},
                    ], "minimum_should_match": 1}}],
                    "must_not": [{"exists": {"field": "rule.mitre.tactic"}}],
                }})
            group_clauses = [
                {"terms": {"rule.groups": groups}},
                {"terms": {"rule.groups.keyword": groups}},
            ]
            category_match = {"bool": {"should": [
                *mitre_clauses,
                # Fallback: rule.groups only for alerts with NO MITRE data at all
                {"bool": {"must": group_clauses,
                          "must_not": [{"exists": {"field": "rule.mitre.tactic"}},
                                        {"exists": {"field": "rule.mitre.id"}}]}},
            ], "minimum_should_match": 1}}
        else:
            category_match = {"bool": {"should": [
                {"terms": {"rule.groups": groups}},
                {"terms": {"rule.groups.keyword": groups}},
            ], "minimum_should_match": 1}}
        return {"bool": {"filter": [
            {"range": {"@timestamp": {"gte": since, "lt": until,
                                       "format": "strict_date_optional_time"}}},
            category_match,
        ]}}

    engine_a_results = None
    engine_b_results = None
    ctx = None
    if params.use_attack_graph:
        ctx = await _build_cluster_context()

    # ENGINE A - Multi-IoC Risk Thresholding (dynamic MITRE scoring)
    if params.engine_a_enabled:
        def _agg() -> dict:
            aggs = {"level_sum": {"sum": {"field": "rule.level"}}}
            if params.use_mitre:
                aggs["by_tactic"] = {
                    "terms": {"field": "rule.mitre.tactic", "size": 32},
                    "aggs": {"level_sum": {"sum": {"field": "rule.level"}}},
                }
                aggs["by_technique"] = {
                    "filter": {"bool": {
                        "must": [{"exists": {"field": "rule.mitre.id"}}],
                        "must_not": [{"exists": {"field": "rule.mitre.tactic"}}],
                    }},
                    "aggs": {"techs": {"terms": {"field": "rule.mitre.id", "size": 100},
                                       "aggs": {"level_sum": {"sum": {"field": "rule.level"}}}}},
                }
                aggs["no_mitre"] = {
                    "filter": {"bool": {"must_not": [
                        {"exists": {"field": "rule.mitre.tactic"}},
                        {"exists": {"field": "rule.mitre.id"}},
                    ]}},
                    "aggs": {"level_sum": {"sum": {"field": "rule.level"}}},
                }
            return aggs

        def _score_bucket(b: dict, category: str) -> float:
            """Dynamic risk score = rule.level x MITRE tactic weight. Tactic-annotated
            alerts use their tactic's weight; technique-only alerts use the STIX-resolved
            technique weight; no-MITRE alerts use the category's mean tactic weight."""
            if not params.use_mitre:
                return float(b.get("level_sum", {}).get("value", 0) or 0) * category_default_weight(category)
            total = 0.0
            for tb in b.get("by_tactic", {}).get("buckets", []) or []:
                total += compute_mitre_risk(tb.get("level_sum", {}).get("value", 0) or 0, tb.get("key"))
            for tech in (b.get("by_technique", {}).get("techs", {}).get("buckets", []) or []):
                total += compute_technique_risk(tech.get("level_sum", {}).get("value", 0) or 0,
                                                tech.get("key"), technique_tactics, category)
            total += (b.get("no_mitre", {}).get("level_sum", {}).get("value", 0) or 0) * category_default_weight(category)
            return total

        async def _fetch_srcips(category, label, groups):
            """Engine A srcips per category with dynamic rule.level x tactic-weight scoring.
            Falls back to single-field terms when multi_terms is unavailable."""
            warning = None
            body = {"size": 0, "query": _build_filter(category, groups),
                    "aggs": {"unique_srcips": {
                        "multi_terms": {"terms": [{"field": f} for f in _SRCIP_FIELD_PATHS],
                                         "size": 10000},
                        "aggs": _agg()}}}
            raw = await _wazuh_indexer_post(body)
            if "error" in raw or not raw.get("aggregations", {}).get("unique_srcips"):
                warning = (f"multi_terms agg unavailable or empty for '{label}' "
                           f"(index may not support it) - fell back to {_SRCIP_FIELD_PATHS[0]}")
                raw = await _wazuh_indexer_post({
                    "size": 0, "query": _build_filter(category, groups),
                    "aggs": {"unique_srcips": {
                        "terms": {"field": _SRCIP_FIELD_PATHS[0], "size": 10000},
                        "aggs": _agg()}}})
                if "error" in raw:
                    return (label, [], warning + " ; single-field fallback also failed")
            buckets = raw.get("aggregations", {}).get("unique_srcips", {}).get("buckets", [])
            entries = []
            for b in buckets:
                key = b.get("key")
                ip = next((v for v in key if v is not None), "0.0.0.0") if isinstance(key, list) else key
                if ip and ip != "0.0.0.0":
                    entries.append((ip, round(_score_bucket(b, category), 2)))
            return (label, entries, warning)

        fetched = await asyncio.gather(*[_fetch_srcips(c, l, g) for c, l, g in categories])
        srcips_by_label = {}
        engine_a_warnings: list[str] = []
        engine_a_query_failures = 0
        for l, e, w in fetched:
            srcips_by_label[l] = e
            if w:
                engine_a_warnings.append(w)
                if "also failed" in w:
                    engine_a_query_failures += 1

        triggers, stats = evaluate_engine_a(
            srcips_by_label.get(params.category_a_label, []),
            srcips_by_label.get(params.category_b_label, []),
            srcips_by_label.get(params.category_c_label, []),
            threshold_score=params.threshold_score,
            exclude_srcips=list(exclude_set) if exclude_set else None,
            cidr_normalize=params.cidr_normalize,
            cluster_map=ctx["cluster_map"] if ctx else None,
            ppr_scores=ctx["ppr_scores"] if ctx else None,
            ppr_boost_factor=_PPR_BOOST_FACTOR if ctx else 0.0,
            confirmed_ips=ctx["confirmed_ips"] if ctx else None,
            confirmed_bonus=_CONFIRMED_BONUS if ctx else 0.0,
            cat_a_weight=params.cat_a_weight,
            cat_b_weight=params.cat_b_weight,
            cat_c_weight=params.cat_c_weight,
        )
        register_attacker_ips([t["ip"] for t in triggers if t.get("ip")], source="engine_a")
        record_iocs([t["ip"] for t in triggers if t.get("ip")], source="engine_a")
        if params.create_case and triggers:
            trigger_ips = [t["ip"] for t in triggers if t.get("ip")]
            case = case_store.create_case(
                title=f"3-Sum APT — {len(triggers)} trigger(s)", srcips=trigger_ips)
            case_store.add_iocs(case["case_id"], trigger_ips)
            stats["case_id"] = case["case_id"]
        if engine_a_warnings:
            stats["warnings"] = engine_a_warnings  # surfaced, never silent
        engine_a_results = (triggers, stats)

    # ENGINE B - 3-Source Volumetric Z-Score
    if params.engine_b_enabled:
        # Compute auto-bucket interval: target ~60 buckets
        dur_minutes = params.time_window_minutes
        if dur_minutes <= 60:
            bucket_interval = "1m"
        elif dur_minutes <= 360:
            bucket_interval = "5m"
        elif dur_minutes <= 1440:
            bucket_interval = "15m"
        else:
            bucket_interval = "1h"

        async def _fetch_time_buckets(category, groups):
            body = {"size": 0, "query": _build_filter(category, groups),
                    "aggs": {"over_time": {"date_histogram": {
                        "field": "@timestamp", "fixed_interval": bucket_interval,
                        "min_doc_count": 0,
                        "extended_bounds": {"min": since_iso, "max": until_iso}}}}}
            raw = await _wazuh_indexer_post(body)
            if "error" in raw:
                return ([], True)
            return (raw.get("aggregations", {}).get("over_time", {}).get("buckets", []), False)

        async def _count_lockouts():
            """Account-lockout volume signal (advisory metadata, never a scoring input).

            Multi-field content match (rule-agnostic): Wazuh decoders store lock events
            in different fields, so match "locked" across the common ones + full_log.
            """
            lock_filter = _build_filter("B", params.category_b_groups)["bool"]["filter"] + [{
                "bool": {"should": [
                    {"match": {"data.error": "locked"}},
                    {"match": {"data.data.error": "locked"}},
                    {"match_phrase": {"full_log": "account is locked"}},
                    {"match_phrase": {"full_log": "account locked"}},
                    {"match_phrase": {"full_log": "locked out"}},
                    {"match": {"data.zimbra_error": "locked"}},
                ], "minimum_should_match": 1}}]
            body = {"size": 0, "query": {"bool": {"filter": lock_filter}}}
            raw = await _wazuh_indexer_post(body)
            if "error" in raw:
                return 0
            total = raw.get("hits", {}).get("total", {})
            return total.get("value", 0) if isinstance(total, dict) else total

        (buckets_a, err_a), (buckets_b, err_b), (buckets_c, err_c), lockouts = await asyncio.gather(
            _fetch_time_buckets("A", params.category_a_groups),
            _fetch_time_buckets("B", params.category_b_groups),
            _fetch_time_buckets("C", params.category_c_groups),
            _count_lockouts(),
        )

        engine_b_query_failures = sum(1 for e in (err_a, err_b, err_c) if e)

        anomalies, b_stats = evaluate_engine_b(
            buckets_a, buckets_b, buckets_c,
            z_score_threshold=params.z_score_threshold,
            sparse_floor=params.engine_b_sparse_floor,
            use_mad=params.engine_b_use_mad,
            shoulder_ratio=params.engine_b_shoulder_ratio,
        )
        b_stats["account_lockouts_observed"] = lockouts  # advisory, not a scoring input
        engine_b_results = (anomalies, b_stats)

    # UNIFIED SCORING
    result = format_evaluation_dict(
        since_iso, until_iso,
        engine_a_results=engine_a_results,
        engine_b_results=engine_b_results,
        evaluation_time_ms=(time.monotonic() - start_time) * 1000,
    )

    # DEGRADATION DETECTION - surface total Indexer failure so the LLM
    # agent is never told "NONE / 0 triggers" when the Indexer was simply down.
    engine_a_degraded = (params.engine_a_enabled and engine_a_query_failures == 3)
    engine_b_degraded = (params.engine_b_enabled and engine_b_query_failures == 3)
    if params.engine_a_enabled and not params.engine_b_enabled and engine_a_degraded:
        result["_degraded"] = True
        result["_degradation_reason"] = (
            "Engine A: all 3 source-IP queries against the Wazuh Indexer failed "
            "(Indexer may be unreachable). Engine B is disabled. "
            "Results are unreliable - severity=NONE may indicate an outage, not a clean window.")
    elif params.engine_b_enabled and not params.engine_a_enabled and engine_b_degraded:
        result["_degraded"] = True
        result["_degradation_reason"] = (
            "Engine B: all 3 time-bucket queries against the Wazuh Indexer failed "
            "(Indexer may be unreachable). Engine A is disabled. "
            "Results are unreliable - anomaly_count=0 may indicate an outage, not a clean window.")
    elif engine_a_degraded and engine_b_degraded:
        result["_degraded"] = True
        result["_degradation_reason"] = (
            "Both Engine A (3 source-IP queries) and Engine B (3 time-bucket queries) "
            "failed against the Wazuh Indexer. The Indexer is likely unreachable. "
            "All correlation results are unreliable - treat severity=NONE as unknown, not clean.")
    elif engine_a_degraded or engine_b_degraded:
        parts = []
        if engine_a_degraded:
            parts.append("Engine A (all 3 source-IP queries failed)")
        if engine_b_degraded:
            parts.append("Engine B (all 3 time-bucket queries failed)")
        result["_degraded"] = True
        result["_degradation_reason"] = (
            "Partial Indexer failure: " + "; ".join(parts) + ". "
            "The working engine's results are reliable; the failed engine's results "
            "(0 triggers/anomalies) should NOT be interpreted as a clean signal.")

    # MULTI-RESOLUTION - re-run at 1h and 24h windows, cross-tier analysis.
    if params.multi_resolution:
        tier_results = [result]  # current run is the 7d tier
        for tier in _MULTI_RES_TIERS[:-1]:  # 1h, 24h (7d already done)
            tier_since = datetime.utcnow() - timedelta(minutes=tier["window_minutes"])
            tier_since_iso = tier_since.strftime("%Y-%m-%dT%H:%M:%SZ")

            # Build per-tier filter (MITRE-first, reuse the shared builder)
            def _tier_filter(category, groups):
                return _build_filter(category, groups, tier_since_iso, until_iso)

            # Engine A at this tier
            tier_a_results = None
            if params.engine_a_enabled:
                async def _tier_fetch(category, label, groups):
                    w = None
                    body = {"size": 0, "query": _tier_filter(category, groups),
                            "aggs": {"unique_srcips": {"multi_terms": {
                                "terms": [{"field": f} for f in _SRCIP_FIELD_PATHS], "size": 10000},
                                "aggs": _agg()}}}
                    raw = await _wazuh_indexer_post(body)
                    if "error" in raw or not raw.get("aggregations", {}).get("unique_srcips"):
                        w = f"multi_terms fallback at {tier['label']}"
                        raw = await _wazuh_indexer_post({
                            "size": 0, "query": _tier_filter(category, groups),
                            "aggs": {"unique_srcips": {
                                "terms": {"field": _SRCIP_FIELD_PATHS[0], "size": 10000},
                                "aggs": _agg()}}})
                        if "error" in raw:
                            return (label, [], w + " also failed")
                    buckets = raw.get("aggregations", {}).get("unique_srcips", {}).get("buckets", [])
                    entries = []
                    for b in buckets:
                        key = b.get("key")
                        ip = next((v for v in key if v is not None), "0.0.0.0") if isinstance(key, list) else key
                        if ip and ip != "0.0.0.0":
                            entries.append((ip, round(_score_bucket(b, category), 2)))
                    return (label, entries, w)
                fet = await asyncio.gather(*[_tier_fetch(c, l, g) for c, l, g in categories])
                sbl = {}
                for l, e, _ in fet:
                    sbl[l] = e
                tta, tts = evaluate_engine_a(
                    sbl.get(params.category_a_label, []), sbl.get(params.category_b_label, []),
                    sbl.get(params.category_c_label, []),
                    threshold_score=tier["threshold_score"],
                    exclude_srcips=list(exclude_set) if exclude_set else None,
                    cat_a_weight=params.cat_a_weight, cat_b_weight=params.cat_b_weight,
                    cat_c_weight=params.cat_c_weight,
                )
                tier_a_results = (tta, tts)

            # Engine B at this tier
            tier_b_results = None
            if params.engine_b_enabled:
                tier_dur = tier["window_minutes"]
                if tier_dur <= 60:
                    bi = "1m"
                elif tier_dur <= 360:
                    bi = "5m"
                else:
                    bi = "15m"
                async def _tier_buckets_batched(cat_groups_list):
                    """Batch all Engine B tier queries into one _msearch call."""
                    bodies = []
                    for category, groups in cat_groups_list:
                        bodies.append({"size": 0, "query": _tier_filter(category, groups),
                            "aggs": {"over_time": {"date_histogram": {
                                "field": "@timestamp", "fixed_interval": bi,
                                "min_doc_count": 0,
                                "extended_bounds": {"min": tier_since_iso, "max": until_iso}}}}})
                    results = await _wazuh_indexer_msearch(bodies)
                    out = []
                    for r in results:
                        if isinstance(r, dict) and "error" in r:
                            out.append(([], True))
                        else:
                            out.append((r.get("aggregations", {}).get("over_time", {}).get("buckets", []), False))
                    return out
                tba, tbb, tbc = await _tier_buckets_batched([
                    ("A", params.category_a_groups), ("B", params.category_b_groups), ("C", params.category_c_groups)])
                anomalies, bstats = evaluate_engine_b(
                    tba[0], tbb[0], tbc[0],
                    z_score_threshold=tier["z_score_threshold"],
                    sparse_floor=params.engine_b_sparse_floor,
                    use_mad=params.engine_b_use_mad,
                    shoulder_ratio=params.engine_b_shoulder_ratio,
                )
                tier_b_results = (anomalies, bstats)

            tier_result = format_evaluation_dict(tier_since_iso, until_iso,
                engine_a_results=tier_a_results, engine_b_results=tier_b_results,
                evaluation_time_ms=0)
            tier_results.append(tier_result)

        result["multi_resolution"] = evaluate_multi_resolution(tier_results)

    # Auto-enrich top triggers with threat intel.
    if params.follow_up == "threat_intel" and engine_a_results:
        triggers, _ = engine_a_results
        top_ips = [t["ip"] for t in triggers[:10] if t.get("ip")]
        if top_ips:
            enrichment = await _enrich_ips(top_ips)
            result["enrichment"] = enrichment

    _three_sum_global_throttle["time"] = time.monotonic()
    _three_sum_global_throttle["result"] = result
    return result


async def _enrich_ips(ips: list[str]) -> dict[str, dict]:
    """Enrich a list of IPs with CrowdSec + ThreatFox concurrently.
    Best-effort - individual failures are surfaced inline but never block
    the overall enrichment pass.
    """
    register_attacker_ips(ips, source="enrichment")  # queried IOCs are attacker candidates - keep unmasked
    async def _crowdsec_one(ip: str) -> dict | None:
        try:
            raw = await _crowdsec_request(f"/v2/smoke/{ip}")
            return {"reputation": raw.get("reputation", "unknown"),
                    "behaviors": [b.get("name", "?") for b in raw.get("behaviors", [])[:3]]}
        except Exception:
            return None

    async def _threatfox_one(ip: str) -> dict | None:
        try:
            from mcp_server.threat_intel.threatfox import _threatfox_request
            raw = await _threatfox_request(ip, False)
            items = raw.get("data", [])
            if not items:
                return None
            return {"malware": items[0].get("malware_printable", "?"),
                    "confidence": items[0].get("confidence_level", 0),
                    "threat_type": items[0].get("threat_type_desc", "?")}
        except Exception:
            return None

    tasks = []
    for ip in ips:
        tasks.append(_crowdsec_one(ip))
        tasks.append(_threatfox_one(ip))

    results = await asyncio.gather(*tasks)
    enriched: dict[str, dict] = {}
    for i, ip in enumerate(ips):
        cs = results[i * 2]
        tf = results[i * 2 + 1]
        entry: dict = {}
        if cs:
            entry["crowdsec"] = cs
        if tf:
            entry["threatfox"] = tf
        if entry:
            enriched[ip] = entry
    return enriched


# Cross-Tool IP Investigation
class InvestigateIpInput(BaseModel):
    """Input model for blueteam_investigate_ip."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    srcip: str = Field(..., min_length=7, max_length=45,
                       description="Source IP to investigate.")
    since: str | None = Field(default="24h", max_length=30,
                               description="Time window. ISO 8601 or relative ('24h', '7d').")
    response_format: Literal["markdown", "json"] = Field(
        default="markdown", description="'markdown' or 'json'.")


@mcp.tool(
    name="blueteam_investigate_ip",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": False},
)
async def blueteam_investigate_ip(params: InvestigateIpInput) -> str:
    """Run a comprehensive IP investigation - alert profile, timeline, and geo.
    Combines three indexer queries in parallel:
    1. Alert count + top rules (like alert summarization)
    2. Hourly timeline (for pattern/beacon detection)
    3. Geo distribution (country-level attack origin)

    Use this as a first-look triage tool. For deeper analysis, follow up with
    ``blueteam_threat_card``, ``blueteam_attack_chain``, and ``blueteam_unified_threat_score``.

    **Worked Examples**

    1. *Quick triage of a suspicious IP*:
       ``blueteam_investigate_ip(srcip="103.107.116.202")``

    2. *7-day investigation*:
       ``blueteam_investigate_ip(srcip="185.220.101.1", since="7d")``

    3. *JSON output for automated processing*:
       ``blueteam_investigate_ip(srcip="10.0.0.55", response_format="json")``
    """
    _audit_log("blueteam_investigate_ip", {"srcip": params.srcip, "since": params.since})
    if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
        return json.dumps({"error": "WAZUH_INDEXER_URL and WAZUH_INDEXER_PASSWORD must be set."}, indent=2)

    since_iso, until_iso = _parse_time_window(params.since or "24h", None)
    srcip = params.srcip.strip()

    # Build shared filter
    base_filter = [
        {"range": {"@timestamp": {"gte": since_iso, "lt": until_iso,
                                   "format": "strict_date_optional_time"}}},
        {"bool": {"should": [
            {"match": {"data.srcip": srcip}},
            {"match_phrase": {"full_log": srcip}},
        ], "minimum_should_match": 1}},
    ]

    async def _fetch_summary():
        body = {"size": 0, "query": {"bool": {"filter": base_filter}},
                "aggs": {
                    "top_rules": {"terms": {"field": "rule.id", "size": 10}},
                    "top_agents": {"terms": {"field": "agent.name", "size": 10}},
                    "severity": {"range": {"field": "rule.level",
                        "ranges": [{"key": "low", "to": 5}, {"key": "medium", "from": 5, "to": 10},
                                   {"key": "high", "from": 10}]}},
                }}
        return await _wazuh_indexer_post(body)

    async def _fetch_timeline():
        body = {"size": 0, "query": {"bool": {"filter": base_filter}},
                "aggs": {"over_time": {"date_histogram": {
                    "field": "@timestamp", "fixed_interval": "1h",
                    "min_doc_count": 0,
                    "extended_bounds": {"min": since_iso, "max": until_iso}}}}}
        return await _wazuh_indexer_post(body)

    async def _fetch_geo():
        body = {"size": 0, "query": {"bool": {"filter": base_filter + [
                    {"exists": {"field": "GeoLocation.country_name"}}]}},
                "aggs": {"by_country": {"terms": {
                    "field": "GeoLocation.country_name", "size": 10}}}}
        return await _wazuh_indexer_post(body)

    summary_raw, timeline_raw, geo_raw = await asyncio.gather(
        _fetch_summary(), _fetch_timeline(), _fetch_geo())

    # Parse results
    total = summary_raw.get("hits", {}).get("total", {}).get("value", 0)
    s_aggs = summary_raw.get("aggregations", {})
    t_aggs = timeline_raw.get("aggregations", {})
    g_aggs = geo_raw.get("aggregations", {})

    if params.response_format == "json":
        return json.dumps({
            "srcip": srcip,
            "window": {"since": since_iso, "until": until_iso},
            "total_alerts": total,
            "top_rules": [{"id": b["key"], "count": b["doc_count"]}
                          for b in s_aggs.get("top_rules", {}).get("buckets", [])],
            "top_agents": [{"name": b["key"], "count": b["doc_count"]}
                           for b in s_aggs.get("top_agents", {}).get("buckets", [])],
            "severity": {b["key"]: b["doc_count"]
                         for b in s_aggs.get("severity", {}).get("buckets", [])},
            "timeline": [{"ts": b.get("key_as_string", "?")[:16],
                          "count": b.get("doc_count", 0)}
                         for b in t_aggs.get("over_time", {}).get("buckets", [])],
            "geo": [{"country": b["key"], "count": b["doc_count"]}
                    for b in g_aggs.get("by_country", {}).get("buckets", [])],
        }, indent=2, ensure_ascii=False)

    # Build markdown report
    lines = [
        f"# 🔎 IP Investigation - `{srcip}`",
        "",
        f"**Window**: `{since_iso}` → `{until_iso}`",
        f"**Total alerts**: {total:,}",
        "",
    ]

    # Severity breakdown
    sev = {b["key"]: b["doc_count"] for b in s_aggs.get("severity", {}).get("buckets", [])}
    if sev:
        lines.append("## Severity")
        lines.append(f"- 🔴 High (L10+): {sev.get('high', 0):,}")
        lines.append(f"- 🟡 Medium (L5-9): {sev.get('medium', 0):,}")
        lines.append(f"- 🟢 Low (L1-4): {sev.get('low', 0):,}")
        lines.append("")

    # Top rules
    top_rules = s_aggs.get("top_rules", {}).get("buckets", [])
    if top_rules:
        lines.append("## Top Rules")
        lines.append("| Rule ID | Alerts |")
        lines.append("|---------|--------|")
        for b in top_rules[:10]:
            lines.append(f"| `{b['key']}` | {b['doc_count']:,} |")
        lines.append("")

    # Timeline sparkline
    timeline_buckets = t_aggs.get("over_time", {}).get("buckets", [])
    if timeline_buckets:
        max_count = max((b.get("doc_count", 0) for b in timeline_buckets), default=1)
        lines.append("## Hourly Timeline")
        for b in timeline_buckets:
            ts = b.get("key_as_string", "?")[:16]
            count = b.get("doc_count", 0)
            bar_len = int(count / max(max_count, 1) * 30) if max_count > 0 else 0
            bar = "█" * bar_len if bar_len > 0 else "▁"
            lines.append(f"`{ts}` {count:>5,} {bar}")
        lines.append("")

    # Geo
    geo_buckets = g_aggs.get("by_country", {}).get("buckets", [])
    if geo_buckets:
        lines.append("## Top Countries")
        lines.append("| Country | Alerts |")
        lines.append("|---------|--------|")
        for b in geo_buckets[:8]:
            lines.append(f"| {b['key']} | {b['doc_count']:,} |")
        lines.append("")

    # Target agents
    top_agents = s_aggs.get("top_agents", {}).get("buckets", [])
    if top_agents:
        lines.append("## Target Agents")
        for b in top_agents[:8]:
            lines.append(f"- `{b['key']}`: {b['doc_count']:,} alerts")
        lines.append("")

    if total == 0:
        lines.append("✅ **No alerts found** for this IP in the selected time window.")
    else:
        lines.append("---")
        lines.append(f"*Follow up with `blueteam_threat_card(srcip='{srcip}')` for threat intel enrichment,*")
        lines.append(f"*`blueteam_attack_chain(srcip='{srcip}')` for kill-chain analysis, or*")
        lines.append(f"*`blueteam_unified_threat_score(ip='{srcip}')` for multi-source scoring.*")

    return _truncate_if_needed("\n".join(lines))
