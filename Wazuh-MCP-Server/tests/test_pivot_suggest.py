#!/usr/bin/env python3
"""
Tests for blueteam_pivot_suggest helpers (no graph build, no Wazuh).
"""
from __future__ import annotations
import os

os.environ.setdefault("WAZUH_INDEXER_URL", "https://idx:9200")
os.environ.setdefault("WAZUH_INDEXER_PASSWORD", "pw")

from mcp_server.tools.attack_graph import _classify_ioc, _tool_for_kind


def test_classify_ioc():
    assert _classify_ioc("1.2.3.4") == "ip"
    assert _classify_ioc("2001:db8::1") == "ip"
    assert _classify_ioc("csirt@tangerangkota.go.id") == "email"
    assert _classify_ioc("evil.example.com") == "domain"
    assert _classify_ioc("d41d8cd98f00b204e9800998ecf8427e") == "hash"  # 32-char md5
    assert _classify_ioc("") == "other"


def test_tool_for_kind():
    assert _tool_for_kind("ip") == "blueteam_investigate_ip"
    assert _tool_for_kind("domain") == "blueteam_whois_lookup"
    assert _tool_for_kind("url") == "urlhaus_lookup"
    assert _tool_for_kind("email") == "blueteam_breach_check"
    assert _tool_for_kind("hash") == "urlhaus_hash_lookup"
    assert _tool_for_kind("technique") == "blueteam_stix_analyze"
    assert _tool_for_kind("actor") == "blueteam_stix_analyze"
    # Unknown kind degrades to the generic IP investigation tool.
    assert _tool_for_kind("other") == "blueteam_investigate_ip"
