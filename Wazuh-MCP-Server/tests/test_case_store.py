#!/usr/bin/env python3
"""Tests for the case store - create/add/get/list (pure, in-memory)."""
from __future__ import annotations
import os

os.environ.setdefault("WAZUH_INDEXER_URL", "https://idx:9200")
os.environ.setdefault("WAZUH_INDEXER_PASSWORD", "pw")

from mcp_server.core import case_store


def test_create_and_get_case():
    case_store._cases.clear()
    c = case_store.create_case("Test Case", ["1.2.3.4"], "note")
    cid = c["case_id"]
    assert cid.startswith("case_")
    got = case_store.get_case(cid)
    assert got["title"] == "Test Case"
    assert got["srcips"] == ["1.2.3.4"]


def test_add_iocs_dedups():
    case_store._cases.clear()
    cid = case_store.create_case("IOC test")["case_id"]
    case_store.add_iocs(cid, ["evil.com", "evil.com", "d41d8cd98f00b204e9800998ecf8427e"])
    assert case_store.get_case(cid)["iocs"] == ["d41d8cd98f00b204e9800998ecf8427e", "evil.com"]


def test_add_verdict_appends():
    case_store._cases.clear()
    cid = case_store.create_case("Verdict test")["case_id"]
    case_store.add_verdict(cid, "5.6.7.8", "true_positive", "c2 beacon")
    got = case_store.get_case(cid)
    assert len(got["verdicts"]) == 1
    assert got["verdicts"][0]["verdict"] == "true_positive"
    assert "5.6.7.8" in got["srcips"]


def test_get_missing_case_is_none():
    case_store._cases.clear()
    assert case_store.get_case("case_nonexistent") is None


def test_list_cases():
    case_store._cases.clear()
    case_store.create_case("A")
    case_store.create_case("B")
    assert len(case_store.list_cases()) == 2
