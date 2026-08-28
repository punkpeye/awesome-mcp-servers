#!/usr/bin/env python3
"""Tests for graph cache + metrics snapshot (pure / in-memory)."""
from __future__ import annotations
import os
os.environ.setdefault("WAZUH_INDEXER_URL", "https://idx:9200")
os.environ.setdefault("WAZUH_INDEXER_PASSWORD", "pw")
import pytest
import mcp_server.core.attack_graph as ag
from mcp_server.core.metrics import snapshot, record_call


def test_graph_cache_populates():
    ag._GRAPH_CACHE.clear()
    ag._GRAPH_CACHE.update({"ts": 0.0, "key": None, "graph": None})
    # build with empty IOC store -> empty graph, but the cache must be stamped.
    import asyncio
    G = asyncio.run(ag.build_attack_graph(since_days=1, max_iocs=10, include_stix=False))
    assert ag._GRAPH_CACHE["graph"] is G
    assert ag._GRAPH_CACHE["key"] is not None


def test_graph_cache_hit():
    # Repeated build with the same key + fresh ts returns the SAME object (cache hit).
    ag._GRAPH_CACHE["ts"] = __import__("time").monotonic()
    G1 = ag._GRAPH_CACHE["graph"]
    import asyncio
    G2 = asyncio.run(ag.build_attack_graph(since_days=1, max_iocs=10, include_stix=False))
    assert G1 is G2  # cache hit - no rebuild


def test_metrics_snapshot_shape():
    record_call("test_tool")
    snap = snapshot()
    assert "tool_calls" in snap
    assert "redaction_gate_failures" in snap
    assert "rate_limit_hits" in snap
    assert "pipeline" in snap
