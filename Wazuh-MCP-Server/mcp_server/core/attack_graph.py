#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Attacker relationship graph (networkx) - converged from the IOC lifecycle store,
attacker registry, and (optionally) STIX kill-chain data.
Graph:
nodes  = IOCs (ip/domain/url/email/hash) + STIX techniques/actors/campaigns
edges  = co-occurrence (IOCs observed in the same extraction/trigger batch), STIX usage edges (technique <-> actor / campaign)
Analytics (blueteam_attack_graph tool):
- connected components -> campaign clusters
- degree centrality     -> hub IOCs
- betweenness centrality-> bridge IOCs (links otherwise-unrelated clusters)
- shortest path         -> srcip <-> actor bridging
"""
from __future__ import annotations
import json, os, time
import networkx as nx
from mcp_server.core.ioc_store import query_iocs
from mcp_server.core.attacker_registry import is_attacker_ioc

_SNAPSHOT_PATH = os.environ.get("BLUETEAM_CAMPAIGN_SNAPSHOTS", "")

# TTL cache for build_attack_graph, the graph is rebuilt from the IOC store on
# every pivot_suggest/attack_graph call; memoize for a short window so repeated
# calls in one investigation don't re-query + re-cluster. Callers only read the
# returned graph (centrality/clustering), so sharing the object is safe.
_GRAPH_CACHE_TTL = float(os.environ.get("BLUETEAM_GRAPH_CACHE_TTL", "60"))
_GRAPH_CACHE: dict = {"ts": 0.0, "key": None, "graph": None}


async def build_attack_graph(since_days: int = 30, min_count: int = 1,
                             max_iocs: int = 1000, include_stix: bool = True,
                             stix_ips_cap: int = 3) -> nx.Graph:
    """Build the attacker relationship graph from the IOC store.
    include_stix: enrich up to `stix_ips_cap` confirmed IPs with MITRE
    technique/actor/campaign nodes via the STIX graph (requires indexer
    credentials; degrades silently without them).
    """
    cache_key = (since_days, min_count, max_iocs, include_stix, stix_ips_cap)
    now = time.monotonic()
    if (_GRAPH_CACHE["key"] == cache_key and _GRAPH_CACHE["graph"] is not None
            and now - _GRAPH_CACHE["ts"] < _GRAPH_CACHE_TTL):
        return _GRAPH_CACHE["graph"]

    hits = query_iocs(since_days=since_days, min_count=min_count, top_n=max_iocs,
                      include_batches=True)
    G = nx.Graph()
    for h in hits:
        G.add_node(h["ioc"], kind=h["kind"], weight=h["decay_weight"], count=h["count"],
                   confirmed=is_attacker_ioc(h["ioc"]),
                   batches=set(h.get("batches", [])))
    # Co-occurrence edges: IOC sharing extraction/trigger batches.
    # Inverted-index approach: O(b x k²) where b = batch count, k = avg IOCs per
    # batch. Dramatically faster than the O(n²) all-pairs nested loop when the
    # batch count is much smaller than the IOC count (the common case).
    batch_to_iocs: dict[int, list[str]] = {}
    for node in G.nodes:
        for bid in G.nodes[node].get("batches", ()):
            batch_to_iocs.setdefault(bid, []).append(node)
    for bid, iocs in batch_to_iocs.items():
        if len(iocs) < 2:
            continue
        # Edges per batch: connect each pair once
        for i in range(len(iocs)):
            for j in range(i + 1, len(iocs)):
                existing = G.get_edge_data(iocs[i], iocs[j])
                if existing:
                    existing["weight"] = existing.get("weight", 0) + 1
                else:
                    G.add_edge(iocs[i], iocs[j], weight=1, source="cooccur")
    if include_stix:
        await _add_stix_edges(G, cap=stix_ips_cap)
    _GRAPH_CACHE.update({"ts": time.monotonic(), "key": cache_key, "graph": G})
    return G


async def _add_stix_edges(G: nx.Graph, cap: int = 3) -> None:
    """Attach MITRE technique/actor/campaign nodes for confirmed attacker IPs."""
    confirmed_ips = [n for n, d in G.nodes(data=True)
                     if d.get("kind") == "ip" and d.get("confirmed")][:cap]
    if not confirmed_ips:
        return
    try:
        from mcp_server.tools.stix_correlation import (
            _load_stix, _build_killchain, _fetch_techniques_for_srcip)
        _load_stix()
    except Exception:
        return  # no STIX bundle / indexer - degrade gracefully
    for ip in confirmed_ips:
        try:
            _, tids = await _fetch_techniques_for_srcip(ip, "30d", None)
        except Exception:
            continue
        if not tids:
            continue
        chain = _build_killchain(tids, top_n=20)
        if "error" in chain:
            continue
        for c in chain["techniques"]:
            tid = c["mitre_id"]
            if not G.has_node(tid):
                G.add_node(tid, kind="technique", weight=1.0, count=0,
                           confirmed=False, batches=set())
            G.add_edge(ip, tid, weight=1.0, source="stix")
            for label in ("actors", "campaigns"):
                for a in c.get(label, []):
                    key = f"{label[:-1]}::{a['mitre_id'] or a['name']}"
                    if not G.has_node(key):
                        G.add_node(key, kind=label[:-1], weight=1.0, count=0,
                                   confirmed=False, batches=set())
                    G.add_edge(tid, key, weight=1.0, source="stix")


def analyze_attack_graph(G: nx.Graph, top_n: int = 10) -> dict:
    """Components, hub IOCs (degree), bridge IOCs (betweenness, approximate)."""
    comps = sorted((c for c in nx.connected_components(G) if len(c) > 1),
                   key=len, reverse=True)
    degree = dict(G.degree())
    n = G.number_of_nodes()
    if n >= 2:
        # Scale k with graph size: 10% of nodes, capped between 10-200.
        # Small graphs need a higher fraction; large graphs use sampling.
        k = max(10, min(int(n * 0.1), 200))
        bc = nx.betweenness_centrality(G, k=k)
    else:
        bc = {}
    top_hubs = sorted(degree, key=degree.get, reverse=True)[:top_n]
    top_bridges = sorted(bc, key=bc.get, reverse=True)[:top_n]

    # Edge betweenness: critical connections between otherwise-unrelated clusters.
    # High edge betweenness = campaign boundary edges - severing them isolates clusters.
    if n >= 2 and G.number_of_edges() >= 1:
        k_edges = max(10, min(int(G.number_of_edges() * 0.05), 100))
        ebc = nx.edge_betweenness_centrality(G, k=k_edges, seed=42)
        top_edges = sorted(ebc, key=ebc.get, reverse=True)[:top_n]
    else:
        top_edges = []

    return {
        "num_nodes": n,
        "num_edges": G.number_of_edges(),
        "num_components": len(comps),
        "top_components": [
            {"size": len(c), "members": sorted(c)[:25],
             "confirmed": sum(1 for x in c if G.nodes[x].get("confirmed"))}
            for c in comps[:top_n]],
        "top_hubs": [{"ioc": i, "degree": degree[i], "kind": G.nodes[i].get("kind"),
                      "confirmed": G.nodes[i].get("confirmed")} for i in top_hubs],
        "top_bridges": [{"ioc": i, "betweenness": round(bc[i], 4),
                         "kind": G.nodes[i].get("kind")} for i in top_bridges],
        "top_edge_bridges": [{"source": u, "target": v,
                                "betweenness": round(ebc[(u, v)], 4),
                                "kind_u": G.nodes[u].get("kind"),
                                "kind_v": G.nodes[v].get("kind")}
                               for u, v in top_edges],
    }


def _personalized_pagerank(G: nx.Graph, personalization: dict, alpha: float = 0.85,
                           max_iter: int = 100, tol: float = 1e-6) -> dict:
    """Power-iteration personalized PageRank for undirected graphs.
    Avoids the scipy dependency networkx 3.x unconditionally requires for
    nx.pagerank. Teleport (1-alpha) to the personalization distribution
    (normalized); alpha spread equally across neighbors.
    """
    nodes = list(G.nodes)
    n = len(nodes)
    if n == 0:
        return {}
    out_deg = {node: max(G.degree(node), 1) for node in nodes}
    pers = {node: personalization.get(node, 0.0) for node in nodes}
    s = sum(pers.values())
    if s <= 0:
        pers = {node: 1.0 / n for node in nodes}
    else:
        pers = {node: v / s for node, v in pers.items()}
    p = {node: 1.0 / n for node in nodes}
    for _ in range(max_iter):
        new_p = {node: (1.0 - alpha) * pers[node] for node in nodes}
        for node in nodes:
            for nbr in G.neighbors(node):
                new_p[nbr] += alpha * p[node] / out_deg[node]
        err = sum(abs(new_p[node] - p[node]) for node in nodes)
        p = new_p
        if err < tol:
            break
    return p


def suspicion_rank(G: nx.Graph, alpha: float = 0.85, top_n: int = 10) -> list[dict]:
    """Personalized PageRank seeded on confirmed attacker IOC.
    Spreads suspicion across co-occurrence/STIX edges: unconfirmed IOCs that sit
    close to confirmed attackers rank high. Returns ranked entries with
    confirmed-neighbor context.
    """
    confirmed = [n for n, d in G.nodes(data=True) if d.get("confirmed")]
    if not confirmed:
        return []
    personalization = {n: 1.0 for n in confirmed}
    pr = _personalized_pagerank(G, personalization, alpha=alpha)
    ranked = [{"ioc": n, "score": round(pr[n], 4), "kind": G.nodes[n].get("kind"),
               "confirmed": G.nodes[n].get("confirmed"),
               "confirmed_neighbors": [x for x in G.neighbors(n)
                                        if G.nodes[x].get("confirmed")][:5]}
              for n in pr]
    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked[:top_n]


def extract_clusters(G: nx.Graph) -> list[list[str]]:
    """Multi-node connected components as member lists (campaign clusters)."""
    return [sorted(c) for c in nx.connected_components(G) if len(c) > 1]


def save_snapshot(G: nx.Graph, window_days: int) -> None:
    """Append a component snapshot to the campaign watch JSONL."""
    if not _SNAPSHOT_PATH:
        return
    entry = {"ts": round(time.time(), 3), "window_days": window_days,
             "num_nodes": G.number_of_nodes(), "num_edges": G.number_of_edges(),
             "clusters": extract_clusters(G)}
    try:
        import os as _os
        from pathlib import Path as _Path
        path = _Path(_SNAPSHOT_PATH)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except OSError:
        pass


def load_last_snapshot() -> dict | None:
    """Return the most recent snapshot entry, or None."""
    if not _SNAPSHOT_PATH:
        return None
    try:
        from pathlib import Path as _Path
        path = _Path(_SNAPSHOT_PATH)
        if not path.exists():
            return None
        last = None
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                last = json.loads(line)
            except ValueError:
                continue
        return last
    except OSError:
        return None


def diff_campaigns(prev: dict | None, cur: list[list[str]]) -> dict:
    """Diff current clusters against the previous snapshot.
    Returns new clusters (no overlap with previous), and growth events
    (previous cluster that gained members).
    """
    new_clusters: list[list[str]] = []
    growth: list[dict] = []
    if not prev:
        return {"new_clusters": cur, "growth": []}
    prev_clusters = prev.get("clusters", [])
    matched_prev = set()
    for ccur in cur:
        curset = set(ccur)
        best_pj, best_overlap = None, 0
        for pj, pprev in enumerate(prev_clusters):
            overlap = len(curset & set(pprev))
            if overlap > best_overlap:
                best_overlap, best_pj = overlap, pj
        if best_pj is not None and best_overlap > 0:
            matched_prev.add(best_pj)
            added = curset - set(prev_clusters[best_pj])
            if added:
                growth.append({"previous_size": len(prev_clusters[best_pj]),
                               "current_size": len(curset),
                               "added": sorted(added)})
        else:
            new_clusters.append(ccur)
    return {"new_clusters": new_clusters, "growth": growth}


def shortest_path_between(G: nx.Graph, a: str, b: str) -> list[str] | None:
    """Shortest path between two IOCs (case-insensitive node lookup)."""
    na = next((x for x in G.nodes if x.lower() == (a or "").strip().lower()), None)
    nb = next((x for x in G.nodes if x.lower() == (b or "").strip().lower()), None)
    if na is None or nb is None or na == nb:
        return None
    try:
        return nx.shortest_path(G, na, nb)
    except nx.NetworkXNoPath:
        return None
