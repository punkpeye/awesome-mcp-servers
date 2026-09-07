#!/usr/bin/env python3
"""
Tests for jarm_fingerprint, pure helpers, input validation, and try to implement SSRF guard.
No network: the TLS probe is exercised via its error path only.
"""
from __future__ import annotations
import os
os.environ.setdefault("WAZUH_INDEXER_URL", "https://idx:9200")
os.environ.setdefault("WAZUH_INDEXER_PASSWORD", "pw")

import ssl
import pytest
from mcp_server.tools import jarm as j


def test_jarm_hash_is_deterministic():
    probes = [
        {"version": "TLSv1.2", "cipher": "ECDHE-RSA-AES256-GCM-SHA384"},
        {"version": "TLSv1.3", "cipher": "TLS_AES_256_GCM_SHA384"},
    ]
    assert j._jarm_hash(probes) == j._jarm_hash(probes)
    assert len(j._jarm_hash(probes)) == 62


def test_jarm_hash_differs_on_different_input():
    a = j._jarm_hash([{"version": "TLSv1.2", "cipher": "A"}])
    b = j._jarm_hash([{"version": "TLSv1.3", "cipher": "B"}])
    assert a != b


def test_jarm_hash_handles_failed_probes():
    h = j._jarm_hash([{"version": None, "cipher": None}])
    assert len(h) == 62  # failed probes hash deterministically, never crash


def test_probe_all_returns_empty_on_connection_refused():
    # An unreachable host (no TLS) -> every probe fails -> empty list
    out = j._probe_all("127.0.0.1", 1, 3)  # port 1 refused quickly
    assert out == []


def test_host_validator_rejects_private_ip():
    from pydantic import ValidationError
    with pytest.raises(ValidationError):
        j.JarmFingerprintInput(host="192.168.1.1")  # SSRF guard: private IP rejected
    with pytest.raises(ValidationError):
        j.JarmFingerprintInput(host="10.0.0.5")


def test_host_validator_accepts_public_and_hostname():
    assert j.JarmFingerprintInput(host="evil-c2.example.com").host == "evil-c2.example.com"
    assert j.JarmFingerprintInput(host="8.8.8.8").host == "8.8.8.8"


def test_host_validator_rejects_injection_chars():
    from pydantic import ValidationError
    with pytest.raises(ValidationError):
        j.JarmFingerprintInput(host="evil.com/path")


def test_dns_rebinding_guard_literal_ips():
    # Literal private/reserved IPs must be rejected by the resolution guard too.
    assert j._host_resolves_public("192.168.1.1") is False
    assert j._host_resolves_public("127.0.0.1") is False
    assert j._host_resolves_public("169.254.169.254") is False
    assert j._host_resolves_public("8.8.8.8") is True
