#!/usr/bin/env python3

"""Tests for prompt_router.py - BM25 prompt-to-tool routing."""

from __future__ import annotations

def test_tokenize_strips_punctuation():
    from mcp_server.tools.prompt_router import _tokenize
    tokens = _tokenize("Brute-force SSH on mail.server!")
    # Hyphen and dot are kept as part of tokens
    assert "brute-force" in tokens
    assert "ssh" in tokens
    assert "mail.server" in tokens
    # "on" is 2 chars kept
    assert "on" in tokens
    # Short tokens filtered out
    tokens2 = _tokenize("a b c")
    assert tokens2 == []  # all 1-char, filtered.


def test_mini_bm25_basic():
    from mcp_server.tools.prompt_router import _MiniBM25
    corpus = [
        "beacon detect C2 callback periodic traffic",
        "alert summarize IoC extraction rule grouping",
        "email lookup compromised account phishing",
    ]
    bm = _MiniBM25(corpus)
    # "beacon" should match doc 0 best
    results = bm.score("beacon")
    assert len(results) > 0
    assert results[0][0] == 0  # first doc
    # "phishing email" should match doc 2 best
    results2 = bm.score("phishing email account")
    assert results2[0][0] == 2


def test_mini_bm25_empty_corpus():
    from mcp_server.tools.prompt_router import _MiniBM25
    bm = _MiniBM25([])
    assert bm.n == 0
    assert bm.score("anything") == []


def test_mini_bm25_idf_rarity():
    from mcp_server.tools.prompt_router import _MiniBM25
    # "rare" appears in 1 doc, "alert" appears in 2 docs
    corpus = [
        "alert summary alert alert",  # doc 0
        "alert beacon rare term",      # doc 1
    ]
    bm = _MiniBM25(corpus)
    # "rare" appears in 1 doc → higher IDF
    # "alert" appears in 2 docs → lower IDF
    assert "rare" in bm.idf
    assert "alert" in bm.idf
    assert bm.idf["rare"] > bm.idf["alert"]


def test_router_singleton():
    from mcp_server.tools.prompt_router import _get_router
    r1 = _get_router()
    r2 = _get_router()
    assert r1 is r2


def test_route_mode():
    from mcp_server.tools.prompt_router import _get_router
    router = _get_router()
    results = router.route("brute force SSH authentication", top_k=3)
    assert isinstance(results, list)
    if results:
        assert "tool" in results[0]
        assert "score" in results[0]
        assert "matched_tokens" in results[0]


def test_buckets_mode():
    from mcp_server.tools.prompt_router import _get_router
    router = _get_router()
    result = router.token_buckets("C2 beacon DNS tunneling exfiltration")
    assert "buckets" in result
    assert "unmatched_tokens" in result
    if result["buckets"]:
        first = list(result["buckets"].values())[0]
        assert "tokens" in first
        assert "score" in first


def test_unmatched_tokens_surfaced():
    from mcp_server.tools.prompt_router import _get_router
    router = _get_router()
    result = router.token_buckets("xyzzy_nonexistent_token_abc123")
    # The token "xyzzy_nonexistent_token_abc123" should be in unmatched
    all_unmatched = result.get("unmatched_tokens", [])
    # All tokens are likely unmatched since this is gibberish
    assert len(all_unmatched) > 0


if __name__ == "__main__":
    import sys
    import traceback
    tests = [f for f in dir() if f.startswith("test_")]
    passed = 0
    for t in tests:
        try:
            globals()[t]()
            print(f"PASS {t}")
            passed += 1
        except Exception:
            print(f"FAIL {t}")
            traceback.print_exc()
    print(f"\n{passed}/{len(tests)} passed")
    sys.exit(0 if passed == len(tests) else 1)
