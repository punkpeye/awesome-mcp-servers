#!/usr/bin/env python3
"""
Tests for the false-positive knowledge base (pure store no network, no Wazuh).
Hope my LLM doing greate during test processing, cause i'm to lazy write a test case.;P
"""
from __future__ import annotations
import os, time

# Env must be set BEFORE importing the module (it reads env at import time).
os.environ.setdefault("WAZUH_INDEXER_URL", "https://idx:9200")
os.environ.setdefault("WAZUH_INDEXER_PASSWORD", "pw")
os.environ["BLUETEAM_FALSE_POSITIVE_KB"] = "/tmp/test_false_positive_kb.jsonl"
os.environ["BLUETEAM_FALSE_POSITIVE_TTL"] = "1"  # 1s TTL so _expired is deterministic

from mcp_server.core import false_positive_kb as fpkb


def test_register_and_lookup():
    fpkb.clear_false_positive_kb()
    fpkb.register_false_positive("1.2.3.4", source="test", reason="scanner")
    assert fpkb.is_false_positive("1.2.3.4")
    assert not fpkb.is_false_positive("5.6.7.8")


def test_normalization():
    fpkb.clear_false_positive_kb()
    fpkb.register_false_positive("EVIL.COM", source="test")
    assert fpkb.is_false_positive("evil.com")


def test_false_positive_iocs_feed():
    fpkb.clear_false_positive_kb()
    fpkb.register_false_positive("1.1.1.1", source="test")
    fpkb.register_false_positive("2.2.2.2", source="test")
    assert {"1.1.1.1", "2.2.2.2"} <= fpkb.false_positive_iocs()


def test_stats_and_expiry_predicate():
    fpkb.clear_false_positive_kb()
    fpkb.register_false_positive("9.9.9.9", source="test")
    assert fpkb.false_positive_stats()["entries"] >= 1
    # Directly exercise the TTL predicate (1s TTL set above).
    assert fpkb._expired({"ts": time.time() - 10})      # 10s old -> expired
    assert not fpkb._expired({"ts": time.time()})       # fresh -> active


def test_stats_shape():
    fpkb.clear_false_positive_kb()
    stats = fpkb.false_positive_stats()
    assert {"entries", "ttl_seconds", "max_entries", "persisted_path", "sources"} <= set(stats)
