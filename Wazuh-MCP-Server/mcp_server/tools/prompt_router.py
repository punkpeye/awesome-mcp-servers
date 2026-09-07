#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Prompt-to-tool routing via BM25 lexical ranking over MCP tool descriptions.
Without external dependencies - stdlib-only BM25 reuses the pattern from semantic_search.py.

Given a natural-language security prompt (e.g. "brute force SSH on mail server"),
tokenizes it, scores each token's IDF against the tool corpus, buckets tokens by
their strongest tool association, and returns a ranked tool invocation plan.
"""
from __future__ import annotations
import json, math, re, logging
from collections import defaultdict
from pydantic import BaseModel, ConfigDict, Field
from mcp_server import mcp

logger = logging.getLogger("blue_team_mcp.prompt_router")

# Minimal BM25 + tokenizer (same algorithm as semantic_search.py)
_K1 = 1.5
_B = 0.75


def _tokenize(text: str) -> list[str]:
    """Lowercase, split, remove short tokens and punctuation."""
    text = re.sub(r"[^a-z0-9\s._-]", " ", text.lower())
    return [t.strip("._-") for t in text.split() if len(t.strip("._-")) >= 2]


class _MiniBM25:
    """Minimal BM25 Okapi scorer - same math as semantic_search._BM25."""
    def __init__(self, corpus: list[str]):
        self.corpus = corpus
        self.n = len(corpus)
        self.tokenized = [_tokenize(d) for d in corpus]
        self.doc_len = [len(t) for t in self.tokenized]
        self.avgdl = sum(self.doc_len) / max(self.n, 1) or 1e-9
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
                continue
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


# Tool corpus builder
def _build_tool_corpus() -> list[dict]:
    """Harvest tool name + docstring + param info from the FastMCP registry.
    Returns a list of dicts with keys: name, description, text (the BM25 document).
    Built lazily on first call so all @mcp.tool decorators have fired.
    """
    tools: list[dict] = []
    try:
        registered = getattr(mcp._tool_manager, "_tools", {})
    except Exception:
        registered = {}
    for name, tool in sorted(registered.items()):
        desc = (getattr(tool, "description", "") or "").strip()
        # Take the first paragraph of the docstring - the summary
        first_para = desc.split("\n\n")[0] if desc else ""
        # Extract parameter names for additional signal
        params = []
        try:
            input_schema = getattr(tool, "inputSchema", None)
            if input_schema and "properties" in (input_schema or {}):
                params = list(input_schema["properties"].keys())
        except Exception:
            pass
        param_str = " ".join(params)
        text = f"{name} {first_para} {param_str}".strip()
        tools.append({
            "name": name,
            "description": first_para[:120],
            "text": text,
        })
    return tools


# Prompt Router
class PromptRouter:
    """BM25-based prompt-to-tool router.
    Builds a BM25 index over all registered MCP tool descriptions at init time.
    ``route()`` returns ranked tool suggestions. ``token_buckets()`` groups prompt
    words by their strongest tool association.
    """

    def __init__(self):
        self.tool_corpus: list[dict] = _build_tool_corpus()
        corpus_texts = [t["text"] for t in self.tool_corpus]
        self.bm25 = _MiniBM25(corpus_texts) if corpus_texts else None
        logger.info("PromptRouter: %d tools indexed", len(self.tool_corpus))

    def route(self, prompt: str, top_k: int = 5) -> list[dict]:
        """Rank tools by BM25 relevance to the prompt. Returns top-K matches."""
        if not self.bm25 or not self.tool_corpus:
            return []
        results = []
        for idx, score in self.bm25.score(prompt)[:top_k]:
            t = self.tool_corpus[idx]
            # Find which prompt tokens matched this tool
            prompt_tokens = set(_tokenize(prompt))
            doc_tokens = set(self.bm25.tokenized[idx])
            matched = sorted(prompt_tokens & doc_tokens)
            results.append({
                "rank": len(results) + 1,
                "tool": t["name"],
                "score": round(score, 2),
                "description": t["description"],
                "matched_tokens": matched,
            })
        return results

    def token_buckets(self, prompt: str) -> dict:
        """Group prompt tokens into buckets by their strongest tool association.

        Each token is assigned to the tool whose corpus document gives it the
        highest TF (term frequency). Buckets are sorted by combined IDF score.
        """
        tokens = _tokenize(prompt)
        if not self.bm25 or not self.tool_corpus:
            return {"buckets": {}, "unmatched_tokens": tokens}

        buckets: dict[str, dict] = {}
        unmatched: list[str] = []

        for token in tokens:
            if token not in self.bm25.idf:
                unmatched.append(token)
                continue
            # Find which tool doc gives this token the highest TF
            best_tool = None
            best_tf = 0.0
            for i, doc_tokens in enumerate(self.bm25.tokenized):
                if len(doc_tokens) == 0:
                    continue
                tf = doc_tokens.count(token) / len(doc_tokens)
                if tf > best_tf:
                    best_tf = tf
                    best_tool = self.tool_corpus[i]["name"]
            if best_tool:
                buckets.setdefault(best_tool, {"tokens": [], "score": 0.0,
                                               "description": ""})
                buckets[best_tool]["tokens"].append(token)
                buckets[best_tool]["score"] += self.bm25.idf[token]
                if not buckets[best_tool]["description"]:
                    for t in self.tool_corpus:
                        if t["name"] == best_tool:
                            buckets[best_tool]["description"] = t["description"]
                            break

        # Sort buckets by score descending
        sorted_buckets = dict(
            sorted(buckets.items(), key=lambda x: -x[1]["score"])
        )
        # Round scores
        for v in sorted_buckets.values():
            v["score"] = round(v["score"], 2)

        return {"buckets": sorted_buckets, "unmatched_tokens": unmatched}


# Singleton built lazily on first tool call
_router: PromptRouter | None = None


def _get_router() -> PromptRouter:
    global _router
    if _router is None:
        _router = PromptRouter()
    return _router


# MCP Tool
class PromptRouteInput(BaseModel):
    """Input model for blueteam_prompt_route."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    prompt: str = Field(
        ..., min_length=3, max_length=1024,
        description="Natural-language security prompt to route to Wazuh tools.",
    )
    mode: str = Field(
        default="route",
        description="'route' = ranked tool list, 'buckets' = token-to-tool grouping.",
    )
    top_k: int = Field(
        default=5, ge=1, le=20,
        description="Max tools to return in 'route' mode.",
    )


@mcp.tool(
    name="blueteam_prompt_route",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": False},
)
def blueteam_prompt_route(params: PromptRouteInput) -> str:
    """Map a natural-language security prompt to the most relevant Wazuh MCP tools.

    Uses BM25 lexical ranking over all registered tool descriptions. Breaks the
    prompt into key terms, scores each against the tool corpus, and returns a
    ranked list of suggested tools. In 'buckets' mode, groups prompt words by
    their strongest tool association.

    **Worked Examples**

    1. *Route a brute-force prompt*:
       ``blueteam_prompt_route(prompt="brute force SSH on mail server")``

    2. *Token bucketing for workflow planning*:
       ``blueteam_prompt_route(prompt="C2 beaconing with DNS tunneling", mode="buckets")``

    3. *Top-10 tools for ransomware investigation*:
       ``blueteam_prompt_route(prompt="ransomware encryption files locked", top_k=10)``
    """
    router = _get_router()

    if params.mode == "buckets":
        result = router.token_buckets(params.prompt)
        return json.dumps({
            "prompt": params.prompt,
            "mode": "buckets",
            **result,
        }, indent=2, ensure_ascii=False)

    # Default: route mode
    ranked = router.route(params.prompt, top_k=params.top_k)
    return json.dumps({
        "prompt": params.prompt,
        "mode": "route",
        "tools_indexed": len(router.tool_corpus),
        "results": ranked,
    }, indent=2, ensure_ascii=False)
