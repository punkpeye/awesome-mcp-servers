#!/usr/bin/env python3
"""Test indexer query cache and case timeline"""
from __future__ import annotations
import os

os.environ.setdefault("WAZUH_INDEXER_URL", "https://idx:9200")
os.environ.setdefault("WAZUH_INDEXER_PASSWORD", "pw")

import pytest
from mcp_server.core import case_store
import mcp_server.wazuh.indexer as idx


class _FakeResp:
    def __init__(self, data): self._data = data
    def json(self): return self._data


@pytest.mark.asyncio
async def test_indexer_cache_dedupes(monkeypatch):
    idx._INDEXER_CACHE.clear()
    calls = []

    async def fake_post(method, url, **kw):
        calls.append(url)
        return _FakeResp({"hits": {"total": {"value": 1}}})

    monkeypatch.setattr(idx, "_api_call", fake_post)
    body = {"size": 0, "query": {"match_all": {}}}
    r1 = await idx._wazuh_indexer_post(body)
    r2 = await idx._wazuh_indexer_post(body)
    assert r1 == r2
    assert len(calls) == 1  # identical query served from cache


@pytest.mark.asyncio
async def test_indexer_cache_distinguishes_queries(monkeypatch):
    idx._INDEXER_CACHE.clear()
    calls = []

    async def fake_post(method, url, **kw):
        calls.append(url)
        return _FakeResp({"hits": {"total": {"value": 1}}})

    monkeypatch.setattr(idx, "_api_call", fake_post)
    await idx._wazuh_indexer_post({"size": 0, "query": {"match_all": {}}})
    await idx._wazuh_indexer_post({"size": 0, "query": {"term": {"rule.id": "1"}}})
    assert len(calls) == 2  # different bodies -> different cache keys


def test_case_timeline_chronological():
    case_store._cases.clear()
    cid = case_store.create_case("Timeline test")["case_id"]
    case_store.add_verdict(cid, "1.2.3.4", "suspicious", "first")
    case_store.add_verdict(cid, "5.6.7.8", "true_positive", "second")
    tl = case_store.case_timeline(cid)
    assert tl[0]["event"] == "case_created"
    assert [e["event"] for e in tl[1:]] == ["verdict", "verdict"]
    assert tl[1]["srcip"] == "1.2.3.4"  # chronological order preserved


def test_case_timeline_missing_case():
    case_store._cases.clear()
    assert case_store.case_timeline("case_missing") == []
