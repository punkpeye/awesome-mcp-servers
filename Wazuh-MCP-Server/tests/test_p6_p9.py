#!/usr/bin/env python3
"""Tests for stealer log and JARM"""
from __future__ import annotations


def test_stealer_log_email_validation():
    from mcp_server.tools.stealer_log import StealerLogInput
    from pydantic import ValidationError
    inp = StealerLogInput(email="Csirt@TangerangKota.go.id")
    assert inp.email == "csirt@tangerangkota.go.id"  # lower-case
    try:
        StealerLogInput(email="not-an-email")
        assert False, "Should have raised"
    except ValidationError:
        pass


def test_parse_stealer_logs():
    from mcp_server.tools.stealer_log import _parse_stealer_logs
    raw = {"stealer_logs": [
        {"date_compromised": "2026-01-01", "malware": "REDLINE",
         "computer_name": "PC1", "operating_system": "Windows 10",
         "infected_ips": ["1.2.3.4"], "credentials": [{"account": "a@b.c"}]},
    ]}
    logs = _parse_stealer_logs(raw)
    assert len(logs) == 1
    assert logs[0]["malware"] == "REDLINE"
    assert logs[0]["credential_count"] == 1


def test_parse_stealer_logs_empty():
    from mcp_server.tools.stealer_log import _parse_stealer_logs
    assert _parse_stealer_logs({}) == []
    assert _parse_stealer_logs({"stealer_logs": "not-a-list"}) == []


def test_jarm_host_validation():
    from mcp_server.tools.jarm import JarmFingerprintInput
    from pydantic import ValidationError
    inp = JarmFingerprintInput(host="Evil-C2.Example.com")
    assert inp.host == "evil-c2.example.com"
    try:
        JarmFingerprintInput(host="bad host with spaces")
        assert False, "Should have raised"
    except ValidationError:
        pass


def test_jarm_hash_deterministic():
    from mcp_server.tools.jarm import _jarm_hash
    probes = [{"version": "TLSv1.3", "cipher": "TLS_AES_256_GCM_SHA384"}]
    h1 = _jarm_hash(probes)
    h2 = _jarm_hash(probes)
    assert h1 == h2  # deterministic
    assert len(h1) == 62  # 62-char JARM-like hash


def test_jarm_hash_failed_probe():
    from mcp_server.tools.jarm import _jarm_hash
    probes = [{"version": None, "cipher": None, "error": "failed"}]
    h = _jarm_hash(probes)
    assert len(h) == 62


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
