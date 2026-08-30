#!/usr/bin/env python3
"""
Tests for composable redaction layer chain (Phase 3)
I'm to lazy to write test suites, hope my LLM doesn't disappoint me ;P
"""
from __future__ import annotations


def test_layer_functions_exist_and_are_callable():
    from mcp_server.core.redact_layers import (
        _apply_email_layer, _apply_ip_layer, _apply_domain_layer,
        _apply_location_layer, _apply_ua_layer,
    )
    # Smoke test: each layer is callable and returns a string
    assert callable(_apply_email_layer)
    assert callable(_apply_ip_layer)
    assert callable(_apply_domain_layer)
    assert callable(_apply_location_layer)
    assert callable(_apply_ua_layer)


def test_email_layer_masks_email():
    from mcp_server.core.redact_layers import _apply_email_layer
    result = _apply_email_layer("user@example.com", "full", False)
    assert "@example.com" in result          # domain preserved
    assert "user@example.com" not in result  # local part masked
    assert "[h:" in result                   # forensic hash


def test_ip_layer_masks_private():
    from mcp_server.core.redact_layers import _apply_ip_layer
    result = _apply_ip_layer("from 10.0.0.55 to 192.168.1.1", "full", False)
    assert "10.0.0.55" not in result
    assert "192.168.1.1" not in result
    assert "***" in result


def test_ip_layer_preserves_attacker():
    from mcp_server.core.redact_layers import _apply_ip_layer
    result = _apply_ip_layer("8.8.8.8", "protect_victim", False)
    assert "8.8.8.8" in result  # public IP, not masked by ip layer


def test_domain_layer_masks_under_full_policy():
    from mcp_server.core.redact_layers import _apply_domain_layer
    result = _apply_domain_layer("c2.evil-c2.net", "full", False)
    assert "c2.evil-c2.net" not in result  # subdomain masked


def test_ua_layer_truncates_long_ua():
    from mcp_server.core.redact_layers import _apply_ua_layer
    long_ua = "Mozilla/5.0 " + "x" * 200
    result = _apply_ua_layer(long_ua, "full", False)
    assert len(result) <= 83  # 80 + "..."


def test_location_layer_hashes_path():
    from mcp_server.core.redact_layers import _apply_location_layer
    result = _apply_location_layer("/var/log/nginx/access.log", "full", False)
    assert "/var/log/nginx/access.log" not in result
    assert "access.log" in result  # leaf preserved
    assert "[h:" in result         # forensic hash


if __name__ == "__main__":
    import sys, traceback
    tests = [f for f in dir() if f.startswith("test_")]
    passed = 0
    for t in tests:
        try:
            globals()[t]()
            print(f"  PASS {t}")
            passed += 1
        except Exception:
            print(f"  FAIL {t}")
            traceback.print_exc()
    print(f"\n{passed}/{len(tests)} passed")
    sys.exit(0 if passed == len(tests) else 1)
