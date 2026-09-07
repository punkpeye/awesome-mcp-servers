#!/usr/bin/env python3
"""Tests for domain permutation, pure generator (deterministic, no network)."""
from __future__ import annotations
import os
os.environ.setdefault("WAZUH_INDEXER_URL", "https://idx:9200")
os.environ.setdefault("WAZUH_INDEXER_PASSWORD", "pw")
from mcp_server.tools.domain_permute import _permute_domain
from pydantic import ValidationError
from mcp_server.tools.domain_permute import DomainPermuteInput


def test_permute_returns_variants():
    v = _permute_domain("tangerangkota.go.id", 200)
    assert len(v) > 0
    assert "tangerangkota.go.id" not in v  # original excluded


def test_permute_includes_homoglyph():
    v = _permute_domain("tangerangkota.go.id", 500)
    # 'o' -> '0' homoglyph should be present somewhere
    assert any("0" in x for x in v)


def test_permute_includes_tld_swap():
    v = _permute_domain("tangerangkota.go.id", 500)
    assert "tangerangkota.com" in v
    assert "tangerangkota.id" in v


def test_permute_is_deterministic():
    assert _permute_domain("example.com", 100) == _permute_domain("example.com", 100)


def test_permute_max_variants_capped():
    assert len(_permute_domain("example.com", 10)) <= 10


def test_input_rejects_no_tld():
    with pytest.raises(ValidationError):
        DomainPermuteInput(domain="nodot")


def test_input_rejects_injection():
    with pytest.raises(ValidationError):
        DomainPermuteInput(domain="evil.com/path")


import pytest
