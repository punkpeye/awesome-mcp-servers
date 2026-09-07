#!/usr/bin/env python3
"""
Tests for RapidAPI capability lookups - pure helpers + input validation.
No network calls: the request helper and tools are exercised indirectly.
Hope my LLM doing greate during test processing, cause i'm to lazy write a test case...;P
"""
from __future__ import annotations
import os
os.environ.setdefault("WAZUH_INDEXER_URL", "https://idx:9200")
os.environ.setdefault("WAZUH_INDEXER_PASSWORD", "pw")
import json
import pytest
from mcp_server.threat_intel import rapidapi as r


def test_headers_require_key():
    os.environ.pop("RAPIDAPI_KEY", None)
    with pytest.raises(RuntimeError):
        r._rapidapi_headers("example.p.rapidapi.com")


def test_headers_include_key():
    os.environ["RAPIDAPI_KEY"] = "test-key"
    h = r._rapidapi_headers("example.p.rapidapi.com")
    assert h["x-rapidapi-key"] == "test-key"
    assert h["x-rapidapi-host"] == "example.p.rapidapi.com"
    assert h["Accept"] == "application/json"


def test_dynamic_markdown_recognizes_keys():
    out = r._dynamic_markdown("T", {"status": "blacklisted", "total": 3})
    assert "blacklisted" in out
    assert "total" in out


def test_dynamic_markdown_falls_back_to_json():
    out = r._dynamic_markdown("T", {"unrecognized_shape": {"nested": [1, 2, 3]}})
    assert "```json" in out  # unknown schema -> dump full body rather than crash


def test_envelope_wraps_raw():
    d = json.loads(r._envelope("1.2.3.4", "apiverve_ip_blacklist", {"a": 1}))
    assert d == {"query": "1.2.3.4", "source": "apiverve_ip_blacklist", "result": {"a": 1}}


def test_breach_email_validation():
    from pydantic import ValidationError
    with pytest.raises(ValidationError):
        r.BreachCheckInput(email="not-an-email")
    assert r.BreachCheckInput(email="csirt@tangerangkota.go.id").email == "csirt@tangerangkota.go.id"


def test_ip_input_rejects_private():
    from pydantic import ValidationError
    with pytest.raises(ValidationError):
        r._IpInput(ip="192.168.1.1")  # RFC1918 -> public-IP validator rejects


def test_envelope_redacts_email():
    # S1 fix: the JSON envelope now runs the uniform redaction boundary, so a
    # victim email never reaches the LLM unredacted (breach-check PII leak).
    raw = {"email": "csirt@tangerangkota.go.id", "breaches": ["Adobe"]}
    out = r._envelope("csirt@tangerangkota.go.id", "rapidapi_breach_check", raw)
    assert "csirt@tangerangkota.go.id" not in out  # email masked
    assert "Adobe" in out  # non-PII breach name stays visible


def test_envelope_keeps_public_ip():
    # Public attacker IPs are NOT masked (protect_victim keeps attacker IOCs visible).
    out = r._envelope("103.107.116.202", "apiverve_ip_blacklist", {"ip": "103.107.116.202"})
    assert "103.107.116.202" in out


def test_sanitize_breach_strips_pii():
    # S7: leaked passwords/phones/addresses must be dropped; only verdict + metadata stay.
    raw = {"breached": True, "breaches": [
        {"name": "Adobe", "date": "2013", "leaked_password": "hunter2", "phone": "555-1234"},
    ]}
    out = r._sanitize_breach(raw)
    assert out["breached"] is True
    assert out["breaches"] == [{"name": "Adobe", "date": "2013"}]  # PII stripped
    assert "hunter2" not in json.dumps(out) and "555-1234" not in json.dumps(out)


def test_sanitize_breach_string_list():
    out = r._sanitize_breach({"found": True, "data": ["Adobe", "LinkedIn"]})
    assert out["breached"] is True
    assert out["breaches"] == [{"name": "Adobe"}, {"name": "LinkedIn"}]


def test_sanitize_breach_unknown_shape():
    # Unknown shape -> empty dict (nothing unsafe leaks).
    assert r._sanitize_breach({"unexpected": "shape"}) == {}
