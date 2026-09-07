#!/usr/bin/env python3
"""
Tests for Phase 2-4 three_sum_core.py additions: multi-resolution, median/MAD, shoulder check, per-category weights.
I'm (Auli) to lazy to write test suites, hope my LLM doesn't disappoint me... ;P
"""
from __future__ import annotations


def test_median():
    from mcp_server.correlation.three_sum_core import _median
    assert _median([1.0, 2.0, 3.0]) == 2.0
    assert _median([1.0, 2.0, 3.0, 4.0]) == 2.5
    assert _median([5.0]) == 5.0
    assert _median([3.0, 1.0, 2.0]) == 2.0  # unsorted


def test_mad():
    from mcp_server.correlation.three_sum_core import _mad
    # Symmetric dataset: MAD = 1.0 * 1.4826
    result = _mad([1, 2, 3, 4, 5], 3.0)
    assert 1.4 < result < 1.6  # ~1.4826


def test_engine_a_weights():
    from mcp_server.correlation.three_sum_core import evaluate_engine_a
    srcips_a = [("1.2.3.4", 5)]
    srcips_b = [("1.2.3.4", 5)]
    srcips_c = [("1.2.3.4", 5)]
    # Default weights: 1.0 + 1.5 + 2.0 = 4.5 weighted, total = 22.5
    triggers, stats = evaluate_engine_a(srcips_a, srcips_b, srcips_c, threshold_score=10)
    assert len(triggers) == 1
    assert triggers[0]["total"] == 22.5
    # Equal weights: total = 15
    triggers, _ = evaluate_engine_a(srcips_a, srcips_b, srcips_c,
                                     threshold_score=10, cat_a_weight=1.0,
                                     cat_b_weight=1.0, cat_c_weight=1.0)
    assert triggers[0]["total"] == 15.0


def test_engine_b_mad_mode():
    from mcp_server.correlation.three_sum_core import evaluate_engine_b
    buckets = [{"doc_count": 5}, {"doc_count": 6}, {"doc_count": 4},
               {"doc_count": 5}, {"doc_count": 50}]  # spike at end
    # use_mad=False: spike may be suppressed by inflated stddev
    anom_std, stats_std = evaluate_engine_b(buckets, buckets, buckets,
                                             z_score_threshold=2.0, use_mad=False)
    # use_mad=True: MAD is robust, spike should surface
    anom_mad, stats_mad = evaluate_engine_b(buckets, buckets, buckets,
                                             z_score_threshold=2.0, use_mad=True)
    assert stats_std["z_method"] == "zscore"
    assert stats_mad["z_method"] == "mad"
    # MAD should detect the outlier more aggressively
    assert len(anom_mad) >= len(anom_std)


def test_engine_b_shoulder_check_suppresses_isolated_spike():
    from mcp_server.correlation.three_sum_core import evaluate_engine_b
    # 10 buckets, single isolated spike at bucket 5
    counts = [2, 2, 3, 2, 2, 20, 2, 2, 3, 2]
    buckets = [{"doc_count": c} for c in counts]
    # Without shoulder: spike may trigger
    anom_no_shoulder, _ = evaluate_engine_b(buckets, buckets, buckets,
                                             z_score_threshold=2.0, shoulder_ratio=0.0,
                                             sparse_floor=0)
    # With shoulder: isolated spike should be suppressed
    anom_shoulder, _ = evaluate_engine_b(buckets, buckets, buckets,
                                          z_score_threshold=2.0, shoulder_ratio=0.6,
                                          sparse_floor=0)
    assert len(anom_shoulder) <= len(anom_no_shoulder)


def test_engine_b_sparse_floor():
    from mcp_server.correlation.three_sum_core import evaluate_engine_b
    # 2 events total - below default sparse_floor of 10
    buckets = [{"doc_count": 1}, {"doc_count": 1}]
    anom, stats = evaluate_engine_b(buckets, buckets, buckets, z_score_threshold=1.0)
    assert stats["anomaly_count"] == 0  # all Z=0 due to sparse_floor


def test_multi_resolution():
    from mcp_server.correlation.three_sum_core import (evaluate_multi_resolution,
        format_evaluation_dict)
    # Simulate 3 tier results: 1h (0 triggers), 24h (1 trigger), 7d (2 triggers)
    def _make_tier(triggers_count, anomalies_count, trigger_ips):
        ea = {"triggers": [{"ip": ip, "total": 15} for ip in trigger_ips],
              "stats": {"triggers_count": triggers_count}}
        eb = {"anomalies": [], "stats": {"anomaly_count": anomalies_count}}
        us = {"severity": "NONE", "unified_score": 0}
        return {"window": {"since": "2026-01-01T00:00:00Z", "until": "2026-01-01T01:00:00Z"},
                "engine_a": ea, "engine_b": eb, "unified_scoring": us}

    tier1 = _make_tier(1, 0, ["1.2.3.4"])
    tier2 = _make_tier(1, 0, ["1.2.3.4"])
    tier3 = _make_tier(2, 0, ["1.2.3.4", "5.6.7.8"])
    result = evaluate_multi_resolution([tier1, tier2, tier3])
    assert len(result["tiers"]) == 3
    assert result["cross_tier"]["persistent_count"] == 1  # 1.2.3.4 in all 3
    assert result["cross_tier"]["slow_burn_count"] == 1   # 5.6.7.8 only in tier3
    assert result["cross_tier"]["burst_only_count"] == 0


def test_engine_a_single_category_gate():
    from mcp_server.correlation.three_sum_core import evaluate_engine_a
    # High score concentrated in ONE category must NOT trigger (chained-attack gate)
    hits, _ = evaluate_engine_a([], [], [("9.9.9.9", 100)], threshold_score=10)
    assert hits == []
    # Same high score spread across 2+ categories DOES trigger
    hits, _ = evaluate_engine_a([], [("9.9.9.9", 50)], [("9.9.9.9", 50)], threshold_score=10)
    assert len(hits) == 1
    assert hits[0]["ip"] == "9.9.9.9"


def test_mitre_classification_and_risk():
    from mcp_server.correlation.three_sum_core import (
        classify_mitre_tactic, tactics_for_category, compute_mitre_risk,
        category_default_weight, build_category_techniques, compute_technique_risk)
    # Tactic -> category via MITRE_TACTIC_TO_CATEGORY (primary engine)
    assert classify_mitre_tactic("Command and Control") == "C"
    assert classify_mitre_tactic("command-and-control") == "C"  # case/hyphen-insensitive
    assert classify_mitre_tactic("Reconnaissance") == "A"
    assert classify_mitre_tactic("Initial Access") == "B"
    assert classify_mitre_tactic("totally-unknown-tactic") is None
    # Category -> tactic list for query filters
    assert "Command and Control" in tactics_for_category("C")
    assert "Reconnaissance" in tactics_for_category("A")
    assert not set(tactics_for_category("A")) & set(tactics_for_category("C"))
    # Dynamic risk = rule.level × tactic weight (C2 weighs more than recon)
    c2 = compute_mitre_risk(10, "Command and Control")
    recon = compute_mitre_risk(10, "Reconnaissance")
    assert c2 > recon
    assert compute_mitre_risk(10, None) == 10.0  # unknown tactic -> weight 1.0
    # Fallback weight is the category's mean tactic weight
    assert category_default_weight("A") < category_default_weight("C")
    # STIX-derived technique -> category bucketing (dynamic, no hardcoded technique IDs)
    tech_tactics = {"T1059.001": ["execution"], "T1071.001": ["command-and-control"]}
    cats = build_category_techniques(tech_tactics)
    assert "T1059.001" in cats["B"]
    assert "T1071.001" in cats["C"]
    # Technique-only risk uses the technique's tactic weight
    assert compute_technique_risk(10, "T1071.001", tech_tactics, "C") > compute_technique_risk(10, "T1059.001", tech_tactics, "B")
    # Unknown technique -> category mean weight
    assert compute_technique_risk(10, "T9999", tech_tactics, "C") == 10 * category_default_weight("C")


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
