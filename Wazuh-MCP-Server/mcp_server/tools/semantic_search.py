#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Semantic search - BM25 lexical ranking over Wazuh rule descriptions.
Zero external dependencies. Pure Python BM25 implementation.
"""
from __future__ import annotations
import json, math, re
from typing import Optional, Literal
from collections import defaultdict
from pydantic import BaseModel, ConfigDict, Field
from mcp_server import mcp, WAZUH_INDEXER_URL, WAZUH_INDEXER_PASSWORD
from mcp_server.core.audit import _audit_log, _truncate_if_needed
from mcp_server.core.redact import _redact_alert_data
from mcp_server.wazuh.indexer import _wazuh_indexer_post, _WAZUH_INDEX_PATTERNS
from mcp_server.wazuh.time_utils import _parse_time_window

# BM25
# BM25(D, Q) = Σ IDF(q_i) · TF(q_i, D)
# IDF(q_i) = ln((N - n_i + 0.5) / (n_i + 0.5) + 1)
# TF(q_i, D) = f(q_i, D) · (k1 + 1) / (f(q_i, D) + k1 · (1 - b + b · |D| / avgdl))
_K1 = 1.5
_B = 0.75

class _BM25:
    """Minimal BM25 Okapi scorer over a text corpus."""
    def __init__(self, corpus: list[str]):
        self.corpus = corpus
        self.n = len(corpus)
        self.tokenized = [_tokenize(d) for d in corpus]
        self.doc_len = [len(t) for t in self.tokenized]
        # avgdl guard: empty corpus or all-empty docs must not divide by zero (Aul adjust)
        self.avgdl = sum(self.doc_len) / max(self.n, 1) or 1e-9
        # Pre-compute IDF per term
        df: dict[str, int] = defaultdict(int)
        for tokens in self.tokenized:
            for t in set(tokens):
                df[t] += 1
        self.idf = {t: math.log((self.n - c + 0.5) / (c + 0.5) + 1)
                     for t, c in df.items()}

    def score(self, query: str) -> list[tuple[int, float]]:
        q_tokens = _tokenize(query)
        scores: list[tuple[int, float]] = []
        for idx, doc_tokens in enumerate(self.tokenized):
            dl = self.doc_len[idx]
            if dl == 0:
                continue  # empty doc -> score 0 (also protects the length-normalized TF - by Aul)
            # One-pass term-frequency dict per doc (O(dl)) instead of
            # doc_tokens.count(qt) per query term (O(q*dl)).
            tf: dict[str, int] = {}
            for t in doc_tokens:
                tf[t] = tf.get(t, 0) + 1
            score = 0.0
            for qt in q_tokens:
                if qt not in self.idf:
                    continue
                f = tf.get(qt, 0)
                if f == 0:
                    continue
                tfv = f * (_K1 + 1) / (f + _K1 * (1 - _B + _B * dl / self.avgdl))
                score += self.idf[qt] * tfv
            if score > 0:
                scores.append((idx, score))
        scores.sort(key=lambda x: -x[1])
        return scores


def _tokenize(text: str) -> list[str]:
    """Lowercase, split, remove short tokens and punctuation."""
    text = re.sub(r"[^a-z0-9\s._-]", " ", text.lower())
    tokens = [t.strip("._-") for t in text.split() if len(t.strip("._-")) >= 2]
    return tokens


# Wazuh Rule Corpus
# Static fallback corpus - used when Wazuh API is unavailable.
# Replaced by live rules on first successful API call.
_STATIC_RULE_CORPUS: list[dict] = [
    # Auth / Brute Force
    {"id": "5710", "desc": "SSHD brute force authentication failure", "groups": "authentication_failed,bruteforce"},
    {"id": "5712", "desc": "SSHD brute force detected", "groups": "authentication_failed,bruteforce"},
    {"id": "5716", "desc": "SSHD authentication failed", "groups": "authentication_failed"},
    {"id": "5551", "desc": "Multiple authentication failures from same source", "groups": "authentication_failed,bruteforce"},
    {"id": "60106", "desc": "Multiple Windows logon failures", "groups": "windows,authentication_failed,bruteforce"},
    # Web Attacks
    {"id": "31100", "desc": "Web server SQL injection attempt", "groups": "web,attack,sql_injection"},
    {"id": "31103", "desc": "Web server path traversal attempt", "groups": "web,attack,path_traversal"},
    {"id": "31108", "desc": "Web server command injection attempt", "groups": "web,attack,command_injection"},
    {"id": "31151", "desc": "Web server PHP file upload attempt", "groups": "web,attack,php"},
    {"id": "31500", "desc": "Web server remote code execution attempt", "groups": "web,attack,rce"},
    {"id": "604042", "desc": "Generic webshell or malicious PHP script detected", "groups": "web,attack,webshell"},
    # Recon / Scanning
    {"id": "600029", "desc": "Nmap scan detection multiple ports from single source", "groups": "recon,scan,nmap"},
    {"id": "33100", "desc": "Network port scan detected", "groups": "recon,scan"},
    {"id": "5760", "desc": "SSHD port scanning detected", "groups": "recon,scan,ssh"},
    # Malware / C2
    {"id": "606029", "desc": "C2 indicator detected active response triggered", "groups": "c2,active_response"},
    {"id": "640", "desc": "Possible malware or rootkit detected by rkhunter", "groups": "malware,rootkit"},
    {"id": "641", "desc": "File integrity change detected syscheck", "groups": "syscheck,fim"},
    # Windows Events
    {"id": "60100", "desc": "Windows event log cleared", "groups": "windows,defense_evasion"},
    {"id": "60204", "desc": "Windows privilege escalation attempt", "groups": "windows,privilege_escalation"},
    # Exploitation
    {"id": "33500", "desc": "Denial of service attack detected", "groups": "dos,attack"},
    # Data Exfiltration
    {"id": "700", "desc": "Large data transfer possible exfiltration", "groups": "exfiltration"},
    {"id": "701", "desc": "DNS tunneling exfiltration detected", "groups": "dns,exfiltration,tunneling"},
    # Suspicious Activity
    {"id": "510", "desc": "Suspicious cron job created", "groups": "cron,persistence"},
    {"id": "530", "desc": "Suspicious SUID binary detected", "groups": "suid,privilege_escalation"},
    {"id": "550", "desc": "Suspicious network connection to known bad IP", "groups": "network,c2"},
    {"id": "560", "desc": "Suspicious PowerShell execution", "groups": "powershell,windows,execution"},
    # Linux
    {"id": "5500", "desc": "PAM authentication failure", "groups": "pam,authentication_failed"},
    {"id": "5502", "desc": "Sudo command executed", "groups": "sudo,privilege_escalation"},
    # Compliance
    {"id": "800", "desc": "CIS benchmark compliance check failed", "groups": "cis,compliance"},
    {"id": "801", "desc": "PCI DSS compliance violation detected", "groups": "pci_dss,compliance"},
]

# Live corpus builder (calls Wazuh API for full rule set)
def _build_bm25_from_corpus(corpus: list[dict]) -> _BM25:
    """Build BM25 index from a rule corpus."""
    texts = [f"{r['id']} {r['desc']} {r['groups']}" for r in corpus]
    return _BM25(texts)

_bm25_index: _BM25 = _build_bm25_from_corpus(_STATIC_RULE_CORPUS)
_bm25_corpus: list[dict] = _STATIC_RULE_CORPUS
_bm25_live_loaded = False


async def _try_load_live_corpus():
    """Fetch rules from Wazuh API and rebuild BM25 index. Falls back to static."""
    global _bm25_index, _bm25_corpus, _bm25_live_loaded
    if _bm25_live_loaded:
        return
    _bm25_live_loaded = True
    try:
        from mcp_server import WAZUH_API_URL, WAZUH_API_PASSWORD
        if not WAZUH_API_URL or not WAZUH_API_PASSWORD:
            raise RuntimeError("Wazuh API not configured")
        from mcp_server.wazuh.auth import _wazuh_api_get
        data = await _wazuh_api_get("/rules", {"limit": "500", "sort": "-level"})
        if isinstance(data.get("error"), str):
            raise RuntimeError(data["error"])
        items = data.get("data", {}).get("affected_items", [])
        if len(items) < 10:
            raise RuntimeError(f"Only {len(items)} rules returned")
        live_corpus = []
        for r in items:
            live_corpus.append({
                "id": str(r.get("id", "?")),
                "desc": str(r.get("description", ""))[:100],
                "groups": ",".join(r.get("groups", [])) if r.get("groups") else "",
            })
        _bm25_corpus = live_corpus
        _bm25_index = _build_bm25_from_corpus(live_corpus)
    except Exception:
        # Fall back to static corpus
        _bm25_corpus = _STATIC_RULE_CORPUS
        _bm25_index = _build_bm25_from_corpus(_STATIC_RULE_CORPUS)

# Semantic Search Tool
class SemanticSearchInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    query: str = Field(..., min_length=2, max_length=512,
                       description="Natural language query (English or Indonesian).")
    since: str | None = Field(default="24h", max_length=30)
    until: str | None = Field(default=None, max_length=30)
    source: Literal["rules", "alerts"] = Field(default="rules",
        description="rules = BM25 on Wazuh rule descriptions (fast). alerts = BM25 on actual alert documents (deep).")
    top_k: int = Field(default=10, ge=3, le=100,
        description="Number of results to return.")
    srcip: str | None = Field(default=None, max_length=45,
        description="Optional exact source-IP filter. When set with source='alerts', BM25 ranks "
                    "ONLY alerts from this IP (exact field filter on data.srcip — the IP itself "
                    "is NOT added to the BM25 corpus).")
    response_format: Literal["markdown", "json"] = Field(default="markdown")


@mcp.tool(name="blueteam_semantic_search",
          annotations={"readOnlyHint": True, "destructiveHint": False,
                       "idempotentHint": True, "openWorldHint": False})
async def blueteam_semantic_search(params: SemanticSearchInput) -> str:
    """Semantic search over Wazuh rules using BM25 lexical ranking.

    Matches natural language queries against Wazuh rule descriptions and returns
    the most relevant rule IDs. Use this BEFORE querying alerts — find which
    rules match "credential theft" or "serangan webshell" then use
    ``blueteamWazuhIndexerSearch`` to retrieve the actual alerts.

    **Worked Examples**

    1. *Find rules about brute force (fast)*:
       ``blueteam_semantic_search(query="brute force SSH", source="rules")``

    2. *Search actual alerts for webshell activity (deep)*:
       ``blueteam_semantic_search(query="serangan webshell", source="alerts", since="7d")``

    3. *Deep search with auto-scaled scanning*:
       ``blueteam_semantic_search(query="ransomware", source="alerts", since="30d")``
       (Auto-scans up to 50K alerts, reports total available)

    4. *Hybrid: rank alerts semantically but only from one attacker IP*:
       ``blueteam_semantic_search(query="webshell", source="alerts", srcip="117.247.110.24", since="7d")``
       (Exact data.srcip filter — the IP stays OUT of the BM25 corpus)
    """
    _audit_log("blueteam_semantic_search", {"query": params.query, "source": params.source, "top_k": params.top_k})

    if params.source == "alerts":
        return await _semantic_search_alerts(params)

    # source="rules"
    await _try_load_live_corpus()
    results = _bm25_index.score(params.query)[:params.top_k]

    if params.response_format == "json":
        matches = [{"rule_id": _bm25_corpus[idx]["id"],
                     "description": _bm25_corpus[idx]["desc"],
                     "groups": _bm25_corpus[idx]["groups"],
                     "bm25_score": round(score, 4)}
                   for idx, score in results]
        return json.dumps({"query": params.query, "source": "rules", "matches": matches},
                          indent=2, ensure_ascii=False)

    lines = [f"# 🔍 Semantic Search - `{params.query}`", "",
             f"**Source**: rules | **Top {len(results)} matches**:", "",
             "| Rule ID | BM25 Score | Description | Groups |",
             "|---------|-----------|-------------|--------|"]
    for idx, score in results[:params.top_k]:
        r = _bm25_corpus[idx]
        lines.append(f"| `{r['id']}` | {score:.3f} | {r['desc'][:60]} | {r['groups'][:40]} |")
    lines.append("")
    lines.append("*Gunakan `blueteamWazuhIndexerSearch` dengan rule ID dari hasil di atas untuk melihat alert terkait.*")
    return _truncate_if_needed("\n".join(lines))


async def _semantic_search_alerts(params: SemanticSearchInput) -> str:
    """Fetch alerts, get total count, auto-scale scan, build ephemeral BM25, rank top-K."""
    if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
        return json.dumps({"error": "WAZUH_INDEXER_URL and WAZUH_INDEXER_PASSWORD must be set."}, indent=2)

    since_iso, until_iso = _parse_time_window(params.since, params.until)

    # Shared must-clauses: time range + optional EXACT srcip filter (IP stays out of BM25 corpus)
    must: list[dict] = [
        {"range": {"@timestamp": {"gte": since_iso, "lt": until_iso,
                                   "format": "strict_date_optional_time"}}},
    ]
    if params.srcip:
        must.append({"bool": {"should": [
            {"match": {"data.srcip": params.srcip.strip()}},
            {"match": {"data.srcip2": params.srcip.strip()}},
            {"match": {"srcip": params.srcip.strip()}},
        ], "minimum_should_match": 1}})

    # Step 1: Get total count (size:0, instant)
    count_body = {"size": 0, "query": {"bool": {"must": must}}}
    raw_count = await _wazuh_indexer_post(count_body)
    total_val = raw_count.get("hits", {}).get("total", {}).get("value", 0) if isinstance(
        raw_count.get("hits", {}).get("total"), dict) else 0

    _MAX_SCAN = 50000
    if total_val <= _MAX_SCAN:
        max_scan = total_val
    else:
        max_scan = _MAX_SCAN

    # Step 2: Fetch documents
    page_size = min(1000, max_scan)
    all_docs: list[dict] = []
    total_val = 0
    search_after = None

    while len(all_docs) < max_scan:
        body = {"size": min(page_size, max_scan - len(all_docs)),
                "_source": ["@timestamp", "rule.id", "rule.description", "rule.level",
                            "rule.groups", "data.srcip", "data.url", "data.domain",
                            "agent.name", "full_log"],
                "sort": [{"@timestamp": {"order": "desc"}}, {"_id": "asc"}],
                "query": {"bool": {"must": must}}}
        if search_after:
            body["search_after"] = search_after
        raw = await _wazuh_indexer_post(body)
        if "error" in raw:
            break
        hits = raw.get("hits", {})
        hit_list = hits.get("hits", [])
        docs = [h.get("_source", h) for h in hit_list]
        if not docs:
            break
        all_docs.extend(docs)
        total_val = hits.get("total", {}).get("value", len(all_docs)) if isinstance(hits.get("total"), dict) else len(all_docs)
        last_sort = hit_list[-1].get("sort") if hit_list else None
        if len(docs) < page_size or last_sort is None:
            break
        search_after = last_sort

    if not all_docs:
        return _truncate_if_needed(f"# 🔍 Semantic Search — `{params.query}`\n\n**Source**: alerts | **Scanned**: 0 documents\n\n✅ No alerts found in this time window.")

    # Build ephemeral BM25 from alert text fields
    corpus: list[str] = []
    for d in all_docs:
        parts = [
            str(d.get("rule", {}).get("description", "")),
            str(d.get("rule", {}).get("groups", "")),
            str(d.get("data", {}).get("url", "")),
            str(d.get("data", {}).get("domain", "")),
            str(d.get("full_log", ""))[:500],
        ]
        corpus.append(" ".join(parts))

    bm25_alerts = _BM25(corpus)
    results = bm25_alerts.score(params.query)[:params.top_k]
    # Redact before any field is returned - same pipeline as every other data tool.
    redacted_docs = _redact_alert_data(all_docs)

    if params.response_format == "json":
        top_docs = []
        for idx, score in results:
            d = redacted_docs[idx]
            rule = d.get("rule", {})
            data = d.get("data", {})
            top_docs.append({
                "bm25_score": round(score, 4),
                "@timestamp": d.get("@timestamp", "?"),
                "rule_id": rule.get("id", "?"),
                "rule_description": str(rule.get("description", ""))[:80],
                "srcip": data.get("srcip", ""),
                "url": data.get("url", ""),
                "domain": data.get("domain", ""),
                "agent": d.get("agent", {}).get("name", ""),
            })
        return json.dumps({
            "query": params.query, "source": "alerts",
            "scanned": len(all_docs), "total_available": total_val,
            "matches": top_docs,
        }, indent=2, ensure_ascii=False)

    lines = [f"# 🔍 Semantic Search - `{params.query}`", "",
             f"**Source**: alerts | **Scanned**: {len(all_docs):,} | **Total available**: {total_val:,}",
             "", "| # | BM25 | Time | Rule | IP | Detail |",
             "|---|------|------|------|----|--------|"]
    for rank, (idx, score) in enumerate(results, 1):
        d = redacted_docs[idx]
        rule = d.get("rule", {})
        data = d.get("data", {})
        ts = str(d.get("@timestamp", "?"))[:16]
        rid = rule.get("id", "?")
        ip = data.get("srcip", "-")
        detail = (data.get("url") or data.get("domain") or
                  str(rule.get("description", ""))[:50])
        lines.append(f"| {rank} | {score:.3f} | {ts} | `{rid}` | `{ip}` | {detail} |")
    lines.append("")
    if len(all_docs) < total_val:
        lines.append(f"*Scanned {len(all_docs):,} of {total_val:,} alerts. Narrow time window for full coverage.*")
    return _truncate_if_needed("\n".join(lines))
