#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
STIX/ATT&CK correlation - maps Wazuh findings to threat actors, TTPs, and campaigns
via the MITRE ATT&CK STIX 2.1 knowledge graph (pure JSON parse, no stix2 dependency).
"""
from __future__ import annotations
import json, os, asyncio, ipaddress
from typing import Literal, Optional
from pydantic import BaseModel, ConfigDict, Field, field_validator
from mcp_server import mcp, WAZUH_INDEXER_URL, WAZUH_INDEXER_PASSWORD
from mcp_server.core.audit import _audit_log, _truncate_if_needed
from mcp_server.core.redact import _redact_alert_data
from mcp_server.wazuh.indexer import _wazuh_indexer_post
from mcp_server.wazuh.time_utils import _parse_time_window

_STIX_PATH = os.environ.get("MITRE_ATTACK_STIX", "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/refs/heads/master/enterprise-attack/enterprise-attack.json")
_STIX_CACHE = os.environ.get("BLUETEAM_STIX_CACHE",
                            "/var/log/blue-team-mcp/mitre_enterprise_attack.json")

# ATT&CK STIX 2.1 loader (lazy mode aul, cached)
_stix_data: dict | None = None
_stix_error: str | None = None


def _fetch_stix_bundle() -> dict:
    """Fetch the ATT&CK STIX bundle from URL or local path; cache to disk."""
    if os.path.exists(_STIX_PATH) and not _STIX_PATH.startswith("http"):
        with open(_STIX_PATH) as f:
            return json.load(f)
    if os.path.exists(_STIX_CACHE):
        with open(_STIX_CACHE) as f:
            return json.load(f)
    # URL fetch via stdlib urllib (no httpx dependency in loader)
    import urllib.request
    req = urllib.request.Request(_STIX_PATH, headers={"User-Agent": "blue-team-mcp/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    try:
        os.makedirs(os.path.dirname(_STIX_CACHE), exist_ok=True)
        with open(_STIX_CACHE, "w") as f:
            json.dump(data, f)
    except Exception:
        pass
    return data


def _load_stix():
    """Load and index the ATT&CK STIX bundle once. Returns (objects_by_id, ...)."""
    global _stix_data, _stix_error
    if _stix_data is not None or _stix_error:
        return
    try:
        bundle = _fetch_stix_bundle()
        objects = bundle.get("objects", [])

        by_id: dict[str, dict] = {}
        by_type: dict[str, list[dict]] = {}
        relationships: list[dict] = []
        for o in objects:
            by_id[o.get("id", "")] = o
            by_type.setdefault(o.get("type", ""), []).append(o)
            if o.get("type") == "relationship":
                relationships.append(o)

        # index relationships: object_id -> list of related objects
        rel_index: dict[str, list[dict]] = {}
        for r in relationships:
            for key in ("source_ref", "target_ref"):
                ref = r.get(key)
                if ref:
                    rel_index.setdefault(ref, []).append(r)

        _stix_data = {"by_id": by_id, "by_type": by_type,
                      "relationships": relationships, "rel_index": rel_index}
    except Exception as e:
        _stix_error = f"Failed to load STIX: {e}"


def _mitre_id(obj: dict) -> str:
    """Extract the MITRE ATT&CK external ID (e.g. T1059.001, G0001, C0025)."""
    for ref in obj.get("external_references", []):
        eid = ref.get("external_id", "")
        if eid and (eid.startswith("T") or eid.startswith("G") or eid.startswith("C")
                    or eid.startswith("S") or eid.startswith("M")):
            return eid
    return obj.get("id", "")


class StixAnalyzeInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    technique_id: Optional[str] = Field(default=None, max_length=20,
        description="MITRE ATT&CK technique ID to look up (e.g. T1059.001, T1003).")
    actor_name: Optional[str] = Field(default=None, max_length=100,
        description="Threat-actor / intrusion-set name or fragment (e.g. 'APT41', 'Lazarus').")
    campaign_name: Optional[str] = Field(default=None, max_length=100,
        description="Campaign name or fragment to look up.")
    indicator: Optional[str] = Field(default=None, max_length=200,
        description="Free-text indicator (IP, domain, malware name) — matches actor/TTP by name overlap.")
    include_actors: bool = Field(default=True, description="Return matched intrusion-sets.")
    include_ttp: bool = Field(default=True, description="Return matched attack-patterns (techniques).")
    include_campaigns: bool = Field(default=True, description="Return matched campaigns.")
    include_mitigations: bool = Field(default=True, description="Return matched courses-of-action.")
    max_relations: int = Field(default=15, ge=1, le=50)
    response_format: Literal["markdown", "json"] = Field(default="markdown")


@mcp.tool(name="blueteam_stix_analyze",
          annotations={"readOnlyHint": True, "destructiveHint": False,
                       "idempotentHint": True, "openWorldHint": True})
async def blueteam_stix_analyze(params: StixAnalyzeInput) -> str:
    """Correlate Wazuh findings with the MITRE ATT&CK STIX 2.1 knowledge graph.

    Maps MITRE technique IDs (from rule.mitre), threat-actor names, and campaigns
    to their relationships: which actors use a technique, which campaigns a TTP
    belongs to, and what mitigations exist.

    **Data source**: MITRE ATT&CK enterprise STIX bundle (set MITRE_ATTACK_STIX).

    **Worked Examples**

    1. *Map a technique to actors + mitigations*:
       ``blueteam_stix_analyze(technique_id="T1059.001")``

    2. *Find which TTPs a threat actor uses*:
       ``blueteam_stix_analyze(actor_name="Lazarus")``

    3. *Correlate a campaign*:
       ``blueteam_stix_analyze(campaign_name="Wizard Spider")``
    """
    _audit_log("blueteam_stix_analyze", {
        "technique_id": params.technique_id, "actor": params.actor_name,
        "campaign": params.campaign_name, "indicator": params.indicator})
    # Offload the blocking bundle fetch/parse off the async event loop.
    await asyncio.to_thread(_load_stix)
    if _stix_error:
        return json.dumps({"error": _stix_error,
                           "hint": "Set MITRE_ATTACK_STIX to the ATT&CK enterprise-attack.json path"},
                          indent=2)
    assert _stix_data is not None
    by_id, by_type, rel_index = _stix_data["by_id"], _stix_data["by_type"], _stix_data["rel_index"]

    # Find matching objects by query
    matched: list[dict] = []
    if params.technique_id:
        tid = params.technique_id.strip().upper()
        for o in by_type.get("attack-pattern", []):
            if _mitre_id(o) == tid:
                matched.append(o)
    if params.actor_name:
        frag = params.actor_name.strip().lower()
        for o in by_type.get("intrusion-set", []):
            if frag in o.get("name", "").lower():
                matched.append(o)
    if params.campaign_name:
        frag = params.campaign_name.strip().lower()
        for o in by_type.get("campaign", []):
            if frag in o.get("name", "").lower():
                matched.append(o)
    if params.indicator and not matched:
        frag = params.indicator.strip().lower()
        for o in by_type.get("intrusion-set", []) + by_type.get("campaign", []):
            if frag in o.get("name", "").lower():
                matched.append(o)

    if not matched:
        return _truncate_if_needed(f"# STIX/ATT&CK — no match\n\nNo object matched the query. "
                                   f"Try a technique ID (T1059), actor name, or campaign name.")

    # Traverse relationships
    seen = set(matched[0]["id"] for m in matched if m.get("id"))
    results: dict[str, list[dict]] = {"actors": [], "ttps": [], "campaigns": [], "mitigations": []}
    frontier = [m.get("id") for m in matched if m.get("id")]
    hops = 0
    while frontier and hops < 2:
        next_frontier = []
        for oid in frontier:
            for rel in rel_index.get(oid, []):
                target = rel.get("target_ref")
                if not target or target in seen:
                    continue
                seen.add(target)
                next_frontier.append(target)
                obj = by_id.get(target)
                if not obj:
                    continue
                t = obj.get("type")
                if t == "intrusion-set" and params.include_actors:
                    results["actors"].append({"name": obj.get("name"), "mitre_id": _mitre_id(obj),
                                              "desc": (obj.get("description") or "")[:150],
                                              "via": rel.get("relationship_type", "related-to")})
                elif t == "attack-pattern" and params.include_ttp:
                    results["ttps"].append({"name": obj.get("name"), "mitre_id": _mitre_id(obj),
                                            "desc": (obj.get("description") or "")[:150]})
                elif t == "campaign" and params.include_campaigns:
                    results["campaigns"].append({"name": obj.get("name"), "mitre_id": _mitre_id(obj),
                                                 "desc": (obj.get("description") or "")[:150]})
                elif t == "course-of-action" and params.include_mitigations:
                    results["mitigations"].append({"name": obj.get("name"),
                                                   "desc": (obj.get("description") or "")[:150]})
        frontier = next_frontier
        hops += 1

    # Cap relation lists
    for k in results:
        results[k] = results[k][:params.max_relations]

    if params.response_format == "json":
        return json.dumps({
            "query": params.model_dump(exclude={"response_format"}),
            "matched": [{"name": o.get("name"), "mitre_id": _mitre_id(o), "type": o.get("type")}
                        for o in matched],
            **results,
        }, indent=2, ensure_ascii=False)

    lines = [f"# 🕵️ STIX/ATT&CK Correlation", "",
             f"**Query**: {json.dumps(params.model_dump(exclude={'response_format'}))}", ""]
    if matched:
        lines.append("## Matched")
        for o in matched:
            lines.append(f"- **{o.get('name')}** (`{_mitre_id(o)}`, {o.get('type')})")
        lines.append("")
    for label, key, icon in [("Threat Actors", "actors", "🦠"), ("Techniques (TTPs)", "ttps", "⚡"),
                             ("Campaigns", "campaigns", "🎯"), ("Mitigations", "mitigations", "🛡️")]:
        items = results[key]
        if items:
            lines.append(f"## {icon} {label} ({len(items)})")
            for it in items:
                extra = f" — {it.get('desc','')}" if it.get('desc') else ""
                lines.append(f"- **{it.get('name')}** (`{it.get('mitre_id','')}`){extra}")
            lines.append("")
    if not any(results.values()):
        lines.append("*No related objects found in the first two relationship hops.*")
    return _truncate_if_needed("\n".join(lines))


# STIX kill-chain correlation per srcip (item 5)
_TACTIC_ORDER = {t: i for i, t in enumerate([
    "reconnaissance", "resource development", "initial access", "execution",
    "persistence", "privilege escalation", "defense evasion", "credential access",
    "discovery", "lateral movement", "collection", "command and control",
    "exfiltration", "impact"])}


def _normalize_tactic(phase_name: str) -> str:
    return (phase_name or "").replace("-", " ").lower()


def _build_killchain(technique_ids: list[str], top_n: int = 20) -> dict:
    """Map observed MITRE technique IDs through the STIX graph into an ordered chain.

    Returns {"techniques": [...], "tactics_seen": [...]} or {"error": ...}.
    Each technique entry: mitre_id, name, tactic, tactic_order, count context,
    related actors / campaigns / mitigations (1 relationship hop).
    """
    _load_stix()
    if _stix_error:
        return {"error": _stix_error}
    if _stix_data is None:
        return {"error": "STIX bundle not loaded"}
    by_id, by_type, rel_index = _stix_data["by_id"], _stix_data["by_type"], _stix_data["rel_index"]
    patterns = by_type.get("attack-pattern", [])

    chain: list[dict] = []
    for tid in technique_ids:
        t = (tid or "").strip().upper()
        if not t:
            continue
        obj = next((o for o in patterns if _mitre_id(o) == t), None)
        if not obj:
            continue
        tactic = "Unknown"
        for kcp in obj.get("kill_chain_phases", []):
            if kcp.get("kill_chain_name") == "mitre-attack":
                tactic = _normalize_tactic(kcp.get("phase_name", "")) or "unknown"
        # 1-hop relationships: actors, campaigns, mitigations.
        # Read the OPPOSITE endpoint: techniques point at actors/campaigns (uses),
        # while mitigations/attribution point AT the technique (mitigates).
        actors: list[dict] = []
        campaigns: list[dict] = []
        mitigations: list[dict] = []
        obj_id = obj.get("id", "")
        for rel in rel_index.get(obj_id, []):
            is_source = rel.get("source_ref") == obj_id
            other = rel.get("target_ref") if is_source else rel.get("source_ref")
            tgt = by_id.get(other)
            if not tgt:
                continue
            tt = tgt.get("type")
            if tt == "intrusion-set":
                actors.append({"name": tgt.get("name"), "mitre_id": _mitre_id(tgt)})
            elif tt == "campaign":
                campaigns.append({"name": tgt.get("name"), "mitre_id": _mitre_id(tgt)})
            elif tt == "course-of-action":
                mitigations.append({"name": tgt.get("name"), "mitre_id": _mitre_id(tgt)})
        chain.append({
            "mitre_id": t,
            "name": obj.get("name"),
            "tactic": tactic,
            "tactic_order": _TACTIC_ORDER.get(tactic, 99),
            "actors": actors[:5],
            "campaigns": campaigns[:5],
            "mitigations": mitigations[:5],
        })

    chain.sort(key=lambda x: (x["tactic_order"], x["mitre_id"]))
    tactics_seen: list[str] = []
    for c in chain:
        if c["tactic"] not in tactics_seen:
            tactics_seen.append(c["tactic"])
    return {"techniques": chain[:top_n], "tactics_seen": tactics_seen}


class StixKillchainInput(BaseModel):
    """Input model for blueteam_stix_killchain."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    srcip: str = Field(..., min_length=7, max_length=45,
                       description="Source IP to build the ATT&CK kill chain for.")
    since: Optional[str] = Field(default="7d", max_length=30,
                                 description="Time window start. ISO 8601 or relative ('24h', '7d').")
    until: Optional[str] = Field(default=None, max_length=30,
                                 description="Time window end. Defaults to now.")
    top_n: int = Field(default=20, ge=1, le=50,
                       description="Max techniques to include in the chain.")
    response_format: Literal["markdown", "json"] = Field(default="markdown")

    @field_validator("srcip")
    @classmethod
    def validate_srcip(cls, v: str) -> str:
        v = v.strip()
        try:
            ipaddress.ip_address(v)
        except ValueError:
            raise ValueError(f"Invalid IP address: '{v}'") from None
        return v


async def _fetch_techniques_for_srcip(srcip: str, since: str | None,
                                      until: str | None) -> tuple[int, list[str]]:
    """Query the indexer for MITRE technique IDs observed for a srcip.

    Returns (total_alerts, technique_ids). Empty list when no rule.mitre.id data
    or no indexer credentials.
    """
    if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
        return 0, []
    since_iso, until_iso = _parse_time_window(since, until)
    body = {
        "size": 0,
        "query": {"bool": {"filter": [
            {"range": {"@timestamp": {"gte": since_iso, "lt": until_iso,
                                       "format": "strict_date_optional_time"}}},
            {"bool": {"should": [
                {"match": {"data.srcip": srcip}},
                {"match": {"data.srcip2": srcip}},
                {"match": {"srcip": srcip}},
                {"match_phrase": {"full_log": srcip}},
            ], "minimum_should_match": 1}},
        ]}},
        "aggs": {"techniques": {"terms": {"field": "rule.mitre.id", "size": 100}}},
    }
    raw = await _wazuh_indexer_post(body)
    if "error" in raw:
        return 0, []
    total = raw.get("hits", {}).get("total", {}).get("value", 0)
    tids = [b.get("key") for b in raw.get("aggregations", {}).get("techniques", {}).get("buckets", [])]
    return total, tids

@mcp.tool(
    name="blueteam_stix_killchain",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": False},
)
async def blueteam_stix_killchain(params: StixKillchainInput) -> str:
    """Build an ATT&CK kill chain for a source IP from observed alerts + the STIX graph.

    Queries the Wazuh Indexer for MITRE technique IDs in this srcip's alerts
    (rule.mitre.id), maps each through the MITRE ATT&CK STIX bundle, orders them
    by kill-chain phase, and annotates actors / campaigns / mitigations per
    technique (1 relationship hop).

    **Required**: Wazuh Indexer credentials + MITRE_ATTACK_STIX (default: MITRE
    enterprise-attack bundle).

    **Worked Examples**

    1. *Kill chain for an attacker IP, last 7 days*:
       ``blueteam_stix_killchain(srcip="103.166.210.53")``

    2. *30-day chain, JSON*:
       ``blueteam_stix_killchain(srcip="185.220.101.1", since="30d", response_format="json")``

    3. *Deep chain (top 50 techniques)*:
       ``blueteam_stix_killchain(srcip="139.180.203.104", since="90d", top_n=50)``
    """
    _audit_log("blueteam_stix_killchain", {"srcip": params.srcip, "since": params.since})
    if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
        return json.dumps({"error": "WAZUH_INDEXER_URL and WAZUH_INDEXER_PASSWORD must be set."}, indent=2)

    since_iso, until_iso = _parse_time_window(params.since, params.until)
    srcip = params.srcip
    total, tids = await _fetch_techniques_for_srcip(params.srcip, params.since, params.until)

    if not tids:
        return _truncate_if_needed(
            f"# ⛓️ STIX Kill Chain — `{srcip}`\n\n**Alerts**: {total:,} | **MITRE techniques observed**: 0\n\n"
            f"No `rule.mitre.id` values in this srcip's alerts for the window. "
            f"Check that rule.mitre is populated on production alerts before trusting kill-chain output.")

    chain = _build_killchain(tids, top_n=params.top_n)
    if "error" in chain:
        return json.dumps(chain, indent=2)

    if params.response_format == "json":
        return _truncate_if_needed(json.dumps(_redact_alert_data({
            "srcip": srcip, "window": {"since": since_iso, "until": until_iso},
            "total_alerts": total, **chain}), indent=2, ensure_ascii=False))

    lines = [f"# ⛓️ STIX Kill Chain — `{srcip}`", "",
             f"**Alerts**: {total:,} | **Tactics observed**: {len(chain['tactics_seen'])} | "
             f"**Techniques**: {len(chain['techniques'])}", ""]
    for c in chain["techniques"]:
        lines.append(f"## {c['tactic'].title()} — `{c['mitre_id']}` — {c['name']}")
        if c["actors"]:
            lines.append(f"  🦠 Actors: {', '.join(a['name'] for a in c['actors'])}")
        if c["campaigns"]:
            lines.append(f"  🎯 Campaigns: {', '.join(a['name'] for a in c['campaigns'])}")
        if c["mitigations"]:
            lines.append(f"  🛡️ Mitigations: {', '.join(a['name'] for a in c['mitigations'])}")
        lines.append("")
    lines.append(f"*Chain for `{srcip}` over [{since_iso} → {until_iso}]. "
                 f"Techniques ordered by ATT&CK kill-chain phase.*")
    return _truncate_if_needed("\n".join(lines))
