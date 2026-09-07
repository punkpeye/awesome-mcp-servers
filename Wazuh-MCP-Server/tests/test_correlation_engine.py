#!/usr/bin/env python3
"""
Tests for mcp_server/correlation/three_sum_core.py - pure-computation module.
Matches actual API: evaluate_engine_a returns (hits, meta) with hits having
``ip``, ``score_a``, ``score_b``, ``score_c``, ``total`` keys.
"""
from __future__ import annotations
import os
os.environ.setdefault("WAZUH_INDEXER_URL", "https://idx:9200")
os.environ.setdefault("WAZUH_INDEXER_PASSWORD", "pw")
os.environ.setdefault("BLUETEAM_REDACTION_POLICY", "full")

import pytest
from mcp_server.correlation.three_sum_core import (
    evaluate_engine_a,
    evaluate_engine_b,
    format_evaluation_dict,
    normalize_srcip_to_cidr,
)


class TestNormalizeSrcip:

    def test_default_prefix_24(self):
        result = normalize_srcip_to_cidr("192.168.1.100")
        assert result == "192.168.1.0/24"

    def test_custom_prefix(self):
        result = normalize_srcip_to_cidr("10.0.0.50", prefix=16)
        assert result == "10.0.0.0/16"

    def test_invalid_ip_returns_original(self):
        result = normalize_srcip_to_cidr("not-an-ip")
        assert result == "not-an-ip"

    def test_empty_string(self):
        result = normalize_srcip_to_cidr("")
        assert result == ""


class TestSigmaZeroGuard:

    def test_sigma_zero_returns_empty(self):
        buckets = [{"doc_count": 5} for _ in range(10)]
        hits, _meta = evaluate_engine_b(
            buckets_a=buckets, buckets_b=buckets, buckets_c=buckets,
            z_score_threshold=2.5,
        )
        assert len(hits) == 0


class TestEngineAIntersection:

    def test_empty_inputs(self):
        hits, _meta = evaluate_engine_a([], [], [], threshold_score=10)
        assert hits == []

    def test_no_intersection(self):
        hits, _meta = evaluate_engine_a(
            [("1.1.1.1", 5)], [("2.2.2.2", 5)], [("3.3.3.3", 5)],
            threshold_score=10,
        )
        assert hits == []

    def test_three_way_intersection(self):
        hits, _meta = evaluate_engine_a(
            [("1.1.1.1", 5)], [("1.1.1.1", 5)], [("1.1.1.1", 5)],
            threshold_score=10,
        )
        assert len(hits) == 1
        assert hits[0]["ip"] == "1.1.1.1"

    def test_score_below_threshold_filtered(self):
        hits, _meta = evaluate_engine_a(
            [("1.1.1.1", 1)], [("1.1.1.1", 1)], [("1.1.1.1", 1)],
            threshold_score=10,
        )
        assert len(hits) == 0

    def test_exclude_srcips(self):
        hits, _meta = evaluate_engine_a(
            [("1.1.1.1", 20), ("2.2.2.2", 20)],
            [("1.1.1.1", 20), ("2.2.2.2", 20)],
            [("1.1.1.1", 20), ("2.2.2.2", 20)],
            threshold_score=10,
            exclude_srcips=["1.1.1.1"],
        )
        excluded = [h for h in hits if h["ip"] == "1.1.1.1"]
        assert len(excluded) == 0


class TestFormatEvaluation:

    def test_empty_results(self):
        result = format_evaluation_dict(([], {}), ([], {}))
        assert isinstance(result, dict)

    def test_has_engine_keys(self):
        result = format_evaluation_dict(
            ([{"ip": "1.1.1.1", "score_a": 5, "score_b": 5, "score_c": 5, "total": 15}], {}),
            ([], {}),
        )
        assert "engine_a" in result
        assert "engine_b" in result
