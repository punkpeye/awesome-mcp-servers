#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Attacker relationship graph tool - campaign clusters, hub/bridge IOCs, paths.
"""
from __future__ import annotations
import json
from typing import Literal, Optional
from pydantic import BaseModel, ConfigDict, Field
from mcp_server import mcp
from mcp_server.core.audit import _audit_log, _truncate_if_needed
from mcp_server.core.redact import _redact_alert_data
from mcp_server.core.attack_graph import (build_attack_graph, analyze_attack_graph,
                                           shortest_path_between, suspicion_rank,
                                           extract_clusters, save_snapshot,
                                           load_last_snapshot, diff_campaigns, _SNAPSHOT_PATH)


class AttackGraphInput(BaseModel):
    """Input model for blueteam_attack_graph."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    window_days: int = Field(default=30, ge=1, le=3650,
        description="Look-back window for IOCs (default 30 days).")
    min_count: int = Field(default=1, ge=1,
        description="Minimum observation count for an IOC to enter the graph.")
    max_iocs: int = Field(default=500, ge=10, le=2000,
        description="Max IOC nodes to include (cap keeps analytics fast).")
    top_n: int = Field(default=10, ge=1, le=50,
        description="Max components / hubs / bridges to report.")
    include_stix: bool = Field(default=True,
        description="Enrich confirmed attacker IPs with STIX technique/actor edges "
                    "(requires indexer credentials; skipped gracefully if unavailable).")
    path_from: Optional[str] = Field(default=None, max_length=256,
        description="First IOC for a shortest-path query (e.g. an IP).")
    path_to: Optional[str] = Field(default=None, max_length=256,
        description="Second IOC for a shortest-path query (e.g. an actor name).")
    response_format: Literal["markdown", "json"] = Field(
        default="markdown", description="'markdown' (default) or 'json'.")


@mcp.tool(
    name="blueteam_attack_graph",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": False},
)
async def blueteam_attack_graph(params: AttackGraphInput) -> str:
    """Analyze the attacker relationship graph - campaign clusters, hubs, bridges.

    Builds a networkx graph from the IOC lifecycle store (co-occurrence edges:
    IOCs seen in the same extraction/trigger batch) plus optional STIX edges for
    confirmed attacker IPs. Reports:

    - **Connected components** - candidate campaign clusters (which IOCs hang
      together) with confirmed-IOC counts.
    - **Hub IOCs** - highest degree (most co-occurrence links).
    - **Bridge IOCs** - highest betweenness (links otherwise-unrelated clusters).
    - **Shortest path** (path_from + path_to) - e.g. srcip to a threat actor.

    **Worked Examples**

    1. *Campaign clusters, last 30 days*:
       ``blueteam_attack_graph(window_days=30)``

    2. *Hub IOCs only, 7 days*:
       ``blueteam_attack_graph(window_days=7, top_n=15)``

    3. *Bridge between an IP and an actor*:
       ``blueteam_attack_graph(path_from="103.166.210.53", path_to="APT41")``
    """
    _audit_log("blueteam_attack_graph", {"window_days": params.window_days,
                                         "path_from": params.path_from})
    G = await build_attack_graph(since_days=params.window_days,
                                 min_count=params.min_count,
                                 max_iocs=params.max_iocs,
                                 include_stix=params.include_stix)
    analysis = analyze_attack_graph(G, top_n=params.top_n)
    ranked = suspicion_rank(G, top_n=params.top_n)
    analysis["suspicion_ranked"] = [r for r in ranked if not r.get("confirmed")][:params.top_n]

    path = None
    if params.path_from and params.path_to:
        path = shortest_path_between(G, params.path_from, params.path_to)

    result = {"graph": analysis, "path": path}
    if params.response_format == "json":
        return _truncate_if_needed(json.dumps(
            _redact_alert_data(result), indent=2, ensure_ascii=False))

    lines = [f"# 🕸️ Attacker Relationship Graph", "",
             f"**Nodes**: {analysis['num_nodes']} | **Edges**: {analysis['num_edges']} | "
             f"**Components**: {analysis['num_components']}", ""]
    if analysis["top_components"]:
        lines.append(f"## Campaign Clusters ({len(analysis['top_components'])} largest)")
        for i, c in enumerate(analysis["top_components"], 1):
            lines.append(f"- **Cluster {i}** ({c['size']} nodes, {c['confirmed']} confirmed): "
                         f"{', '.join(c['members'][:10])}")
        lines.append("")
    if analysis["top_hubs"]:
        lines.append("## Hub IOCs (most co-occurrence)")
        for h in analysis["top_hubs"]:
            mark = "✅" if h.get("confirmed") else "·"
            lines.append(f"- {mark} `{h['ioc']}` ({h.get('kind')}) - degree {h['degree']}")
        lines.append("")
    if analysis["top_bridges"]:
        lines.append("## Bridge IOCs (highest betweenness)")
        for b in analysis["top_bridges"]:
            lines.append(f"- `{b['ioc']}` ({b.get('kind')}) - betweenness {b['betweenness']}")
        lines.append("")
    if analysis.get("suspicion_ranked"):
        lines.append("## Suspicion-Ranked Unconfirmed IOCs (PPR from confirmed attackers)")
        for r in analysis["suspicion_ranked"]:
            nbrs = ", ".join(r.get("confirmed_neighbors", [])) or "—"
            lines.append(f"- `{r['ioc']}` ({r.get('kind')}) - score {r['score']} | near: {nbrs}")
        lines.append("")
    if path:
        lines.append("## Shortest Path")
        lines.append(" → ".join(f"`{p}`" for p in path))
        lines.append("")
    if analysis["num_nodes"] == 0:
        lines.append("_No IOCs in the store for this window. Run `blueteam_extract_iocs` "
                     "or `three_sum_correlation` first._")
    return _truncate_if_needed("\n".join(lines))


def _classify_ioc(v: str) -> str:
    """Best effort IOC kind for a bare input value (ip/domain/email/hash/other)."""
    import ipaddress
    v = (v or "").strip()
    if not v:
        return "other"
    try:
        ipaddress.ip_address(v)
        return "ip"
    except ValueError:
        pass
    if "@" in v:
        return "email"
    low = v.lower()
    if len(v) in (32, 40, 64) and all(c in "0123456789abcdef" for c in low):
        return "hash"
    if "." in v:
        return "domain"
    return "other"


def _tool_for_kind(kind: str) -> str:
    """Map an IOC kind to the recommended MCP tool for the next pivot."""
    return {
        "ip": "blueteam_investigate_ip",
        "domain": "blueteam_whois_lookup",
        "url": "urlhaus_lookup",
        "email": "blueteam_breach_check",
        "hash": "urlhaus_hash_lookup",
        "technique": "blueteam_stix_analyze",
        "actor": "blueteam_stix_analyze",
        "campaign": "blueteam_stix_analyze",
    }.get(kind or "other", "blueteam_investigate_ip")


class PivotSuggestInput(BaseModel):
    """Input model for blueteam_pivot_suggest."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    ioc: str = Field(..., min_length=3, max_length=256,
        description="Starting IOC (IP, domain, hash, email) to pivot from.")
    window_days: int = Field(default=30, ge=1, le=3650,
        description="Look-back window for the IOC graph (default 30 days).")
    max_iocs: int = Field(default=500, ge=10, le=2000,
        description="Max IOC nodes to include in the graph.")
    top_n: int = Field(default=8, ge=1, le=20,
        description="Max pivot suggestions to return.")
    response_format: Literal["markdown", "json"] = Field(default="markdown")


@mcp.tool(
    name="blueteam_pivot_suggest",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": False},
)
async def blueteam_pivot_suggest(params: PivotSuggestInput) -> str:
    """Suggest the next investigation step for an IOC, driven by the attack graph.

    Builds the IOC co-occurrence graph and, using personalized PageRank (seeded on
    confirmed attacker IOCs) + connected-component clusters, returns ranked pivot
    recommendations: co-occurring neighbors, same-campaign IOCs, and - when the IOC is
    unconfirmed - its shortest path to a confirmed attacker. Each suggestion names the
    concrete MCP tool to call next, turning a fixed pipeline into an adaptive one.

    **Worked Examples**

    1. *Pivot from an attacker IP*:
       ``blueteam_pivot_suggest(ioc="103.107.116.202")``

    2. *Pivot from a suspicious domain*:
       ``blueteam_pivot_suggest(ioc="evil.jnck.com", window_days=14)``

    3. *Machine-readable suggestions*:
       ``blueteam_pivot_suggest(ioc="185.220.101.1", response_format="json")``
    """
    _audit_log("blueteam_pivot_suggest", {"ioc": params.ioc, "window_days": params.window_days})
    target = params.ioc.strip()
    G = await build_attack_graph(since_days=params.window_days, min_count=1,
                                 max_iocs=params.max_iocs, include_stix=True)
    node = next((x for x in G.nodes if x.lower() == target.lower()), None)
    kind = G.nodes[node].get("kind") if node else _classify_ioc(target)

    ranked = suspicion_rank(G, top_n=params.top_n * 3)
    ranked_by_ioc = {r["ioc"]: r for r in ranked}
    clusters = extract_clusters(G)

    suggestions: list[dict] = []
    nearest_path: list[str] | None = None

    if node is None:
        # IOC not yet in the graph, enrich it, then chase the global hot leads.
        suggestions.append({"action": "enrich_self", "target": target, "kind": kind,
                            "reason": "not yet in the IOC graph enrich it first",
                            "tool": _tool_for_kind(kind)})
        for r in ranked:
            if r.get("confirmed"):
                continue
            suggestions.append({"action": "pivot_lead", "target": r["ioc"],
                                "kind": r.get("kind"),
                                "reason": f"suspicion score {r['score']} (near confirmed attackers)",
                                "tool": _tool_for_kind(r.get("kind", "ip"))})
    else:
        confirmed_self = G.nodes[node].get("confirmed", False)
        if not confirmed_self:
            confirmed = [n for n, d in G.nodes(data=True) if d.get("confirmed")]
            paths = [p for p in (shortest_path_between(G, node, c) for c in confirmed) if p]
            nearest_path = min(paths, key=len) if paths else None
            hops = (len(nearest_path) - 1) if nearest_path else None
            reason = "unconfirmed" + (f"- {hops} hop(s) from a confirmed attacker" if hops is not None else "")
            suggestions.append({"action": "investigate_self", "target": target, "kind": kind,
                                "reason": reason, "tool": _tool_for_kind(kind)})
        # Co-occurrence neighbors (strongest weighted edges first).
        nbrs = sorted(G.neighbors(node),
                      key=lambda n: G[node][n].get("weight", 0), reverse=True)[:params.top_n]
        for n in nbrs:
            w = G[node][n].get("weight", 0)
            nkind = G.nodes[n].get("kind", "other")
            suggestions.append({"action": "pivot_neighbor", "target": n, "kind": nkind,
                                "reason": f"co-occurred {w}x in the same batch",
                                "tool": _tool_for_kind(nkind)})
        # Same campaign cluster (excluding self).
        cluster = next((c for c in clusters if node in c), None)
        if cluster:
            for m in [x for x in cluster if x != node][:params.top_n]:
                mkind = G.nodes[m].get("kind", "other")
                suggestions.append({"action": "pivot_cluster", "target": m, "kind": mkind,
                                    "reason": "same campaign cluster",
                                    "tool": _tool_for_kind(mkind)})

    result = {
        "ioc": target,
        "in_graph": node is not None,
        "kind": kind,
        "suspicion_score": ranked_by_ioc.get(node, {}).get("score") if node else None,
        "nearest_confirmed_path": nearest_path,
        "suggestions": suggestions[:params.top_n],
    }

    if params.response_format == "json":
        return _truncate_if_needed(json.dumps(_redact_alert_data(result), indent=2, ensure_ascii=False))

    lines = [f"# 🧭 Pivot Suggestions - `{target}`", "",
             f"- **Kind**: {kind} | **In graph**: {'yes' if result['in_graph'] else 'no'}", ""]
    if result.get("suspicion_score") is not None:
        lines.append(f"- **Suspicion score**: {result['suspicion_score']}")
    if result.get("nearest_confirmed_path"):
        lines.append(f"- **Nearest confirmed attacker**: "
                     f"{' -> '.join(f'`{p}`' for p in result['nearest_confirmed_path'])}")
    lines.append("")
    if not suggestions:
        lines.append("_No suggestions - the IOC graph is empty for this window. "
                     "Run `blueteam_extract_iocs` or `three_sum_correlation` first._")
    else:
        lines.append("## Ranked Next Steps")
        for i, s in enumerate(suggestions, 1):
            lines.append(f"{i}. **{s['action']}** `{s['target']}` ({s.get('kind')}) — "
                         f"{s['reason']}")
            lines.append(f"-> call `{s['tool']}`")
    return _truncate_if_needed("\n".join(lines))


class CampaignWatchInput(BaseModel):
    """Input model for blueteam_campaign_watch."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    window_days: int = Field(default=30, ge=1, le=3650,
        description="Look-back window for the current graph snapshot.")
    min_count: int = Field(default=1, ge=1,
        description="Minimum observation count for an IOC to enter the graph.")
    max_iocs: int = Field(default=500, ge=10, le=2000,
        description="Max IOC nodes to include.")
    top_n: int = Field(default=10, ge=1, le=50,
        description="Max new/growing clusters to report.")
    response_format: Literal["markdown", "json"] = Field(
        default="markdown", description="'markdown' (default) or 'json'.")


@mcp.tool(
    name="blueteam_campaign_watch",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": False, "openWorldHint": False},
)
async def blueteam_campaign_watch(params: CampaignWatchInput) -> str:
    """Detect campaign evolution: new clusters and growth in existing clusters.

    Snapshots the attack-graph components (IOC co-occurrence clusters) to
    BLUETEAM_CAMPAIGN_SNAPSHOTS (JSONL) and diffs against the previous run:

    - **New clusters** - campaign clusters with no overlap with the previous snapshot.
    - **Growth** - previous clusters that gained members (active campaign expansion).

    **Worked Examples**

    1. *What changed since the last snapshot?*:
       ``blueteam_campaign_watch()``

    2. *7-day watch, larger graph*:
       ``blueteam_campaign_watch(window_days=7, max_iocs=1000)``
    """
    _audit_log("blueteam_campaign_watch", {"window_days": params.window_days})
    if not _SNAPSHOT_PATH:
        return json.dumps({"error": "BLUETEAM_CAMPAIGN_SNAPSHOTS is not set.",
                           "detail": "Set it to a writable JSONL path to enable campaign watch."}, indent=2)

    G = await build_attack_graph(since_days=params.window_days,
                                 min_count=params.min_count,
                                 max_iocs=params.max_iocs,
                                 include_stix=False)  # IOC clusters only (deterministic)
    prev = load_last_snapshot()
    clusters = extract_clusters(G)
    diff = diff_campaigns(prev, clusters)
    save_snapshot(G, params.window_days)

    result = {
        "window_days": params.window_days,
        "num_nodes": G.number_of_nodes(),
        "num_edges": G.number_of_edges(),
        "num_clusters": len(clusters),
        "new_clusters": [c[:25] for c in diff["new_clusters"][:params.top_n]],
        "growth": diff["growth"][:params.top_n],
        "has_previous_snapshot": prev is not None,
    }
    if params.response_format == "json":
        return _truncate_if_needed(json.dumps(_redact_alert_data(result), indent=2, ensure_ascii=False))

    lines = [f"# 📈 Campaign Watch", "",
             f"**Nodes**: {result['num_nodes']} | **Clusters**: {result['num_clusters']} | "
             f"**Baseline snapshot**: {'yes' if result['has_previous_snapshot'] else 'no (first run)'}", ""]
    if result["new_clusters"]:
        lines.append(f"## 🆕 New Clusters ({len(result['new_clusters'])})")
        for i, c in enumerate(result["new_clusters"], 1):
            lines.append(f"- **Cluster {i}** ({len(c)} nodes): {', '.join(c[:10])}")
        lines.append("")
    if result["growth"]:
        lines.append(f"## 📈 Growing Clusters ({len(result['growth'])})")
        for g in result["growth"]:
            lines.append(f"- {g['previous_size']} -> {g['current_size']} nodes; added: "
                         f"{', '.join(g['added'][:10])}")
        lines.append("")
    if not result["new_clusters"] and not result["growth"]:
        lines.append("_No cluster changes since the last snapshot._")
    return _truncate_if_needed("\n".join(lines))
