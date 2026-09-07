#!/usr/bin/env python3
"""Tests for OTX AlienVault integration - classifier + pulse extraction."""
from __future__ import annotations


def test_classify_ipv4():
    from mcp_server.threat_intel.otx import _classify_indicator
    assert _classify_indicator("140.82.0.86") == "IPv4"


def test_classify_md5():
    from mcp_server.threat_intel.otx import _classify_indicator
    assert _classify_indicator("b325c92fa540edeb89b95dbfd4400c1c") == "file"


def test_classify_sha256():
    from mcp_server.threat_intel.otx import _classify_indicator
    assert _classify_indicator("a" * 64) == "file"


def test_classify_domain():
    from mcp_server.threat_intel.otx import _classify_indicator
    assert _classify_indicator("evil-c2.example.com") == "domain"


def test_classify_url():
    from mcp_server.threat_intel.otx import _classify_indicator
    assert _classify_indicator("https://evil.com/malware.exe") == "url"


def test_classify_hostname():
    from mcp_server.threat_intel.otx import _classify_indicator
    assert _classify_indicator("webserver01") == "hostname"


def test_classify_unknown():
    from mcp_server.threat_intel.otx import _classify_indicator
    assert _classify_indicator("not a valid ioc!") == ""


def test_extract_pulse_summary():
    from mcp_server.threat_intel.otx import _extract_pulse_summary
    pulses = [{
        "name": "Test Pulse",
        "author": {"username": "analyst1"},
        "created": "2026-01-01T00:00:00",
        "modified": "2026-01-02T00:00:00",
        "tags": ["c2", "malware"],
        "malware_families": ["Emotet"],
        "adversary": "APT41",
        "industries": ["Government"],
        "attack_ids": ["T1190", "T1059"],
        "targeted_countries": ["ID"],
        "indicator_count": 15,
    }]
    summary = _extract_pulse_summary(pulses)
    assert len(summary) == 1
    s = summary[0]
    assert s["name"] == "Test Pulse"
    assert s["author"] == "analyst1"
    assert s["malware_families"] == ["Emotet"]
    assert s["adversary"] == "APT41"
    assert "T1190" in s["attack_ids"]


def test_otx_input_validation_rejects_private_ip():
    from mcp_server.tools.otx_lookup import OtxLookupInput
    from pydantic import ValidationError
    try:
        OtxLookupInput(indicator="10.0.0.1")
        assert False, "Should have raised"
    except ValidationError:
        pass


def test_otx_input_validation_accepts_public():
    from mcp_server.tools.otx_lookup import OtxLookupInput
    inp = OtxLookupInput(indicator="140.82.0.86", section="general")
    assert inp.indicator == "140.82.0.86"


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
