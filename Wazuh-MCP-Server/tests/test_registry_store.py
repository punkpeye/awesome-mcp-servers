#!/usr/bin/env python3
"""
Tests for Phase 2-4: domain matching (exact+1 subdomain), decay-weighted eviction.
I'm to lazy to write test suites, hope my LLM doesn't disappoint me ;P
"""
from __future__ import annotations


def test_domain_exact_match():
    """is_attacker_ioc should match exact domain."""
    # This test needs an attacker registered first.
    # We test the matching logic directly via _classify + domain logic.
    from mcp_server.core.attacker_registry import register_attacker_ioc, is_attacker_ioc, clear_attacker_registry
    clear_attacker_registry()
    register_attacker_ioc("evil.com", source="test")
    assert is_attacker_ioc("evil.com") is True


def test_domain_one_subdomain_match():
    """is_attacker_ioc should match exactly one subdomain level."""
    from mcp_server.core.attacker_registry import register_attacker_ioc, is_attacker_ioc, clear_attacker_registry
    clear_attacker_registry()
    register_attacker_ioc("evil.com", source="test")
    assert is_attacker_ioc("www.evil.com") is True
    assert is_attacker_ioc("mail.evil.com") is True


def test_domain_deep_subdomain_rejected():
    """is_attacker_ioc should NOT match deep subdomains (2+ levels)."""
    from mcp_server.core.attacker_registry import register_attacker_ioc, is_attacker_ioc, clear_attacker_registry
    clear_attacker_registry()
    register_attacker_ioc("evil.com", source="test")
    assert is_attacker_ioc("deep.sub.evil.com") is False
    assert is_attacker_ioc("also.not.evil.com") is False


def test_domain_unregistered_not_matched():
    from mcp_server.core.attacker_registry import is_attacker_ioc, clear_attacker_registry
    clear_attacker_registry()
    assert is_attacker_ioc("benign.com") is False
    assert is_attacker_ioc("www.benign.com") is False


def test_decay_weighted_eviction_sort_order():
    """Decay-weighted eviction: lowest decay evicted first."""
    from mcp_server.correlation.three_sum_core import compute_time_decay_weight
    from datetime import datetime, timezone
    # IOCs with different ages
    now = datetime.now(timezone.utc)
    recent_ts = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    old_ts = "2020-01-01T00:00:00Z"
    w_recent = compute_time_decay_weight(recent_ts, recent_ts)
    w_old = compute_time_decay_weight(old_ts, old_ts)
    assert w_recent > 0.9  # very recent -> high weight
    assert w_old < 0.01     # very old -> near-zero weight


if __name__ == "__main__":
    import sys, traceback
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
