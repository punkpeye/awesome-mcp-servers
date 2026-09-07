#!/usr/bin/env python3
"""Tests for stealer_log_check — parse helper + input validation (no network)."""
from __future__ import annotations
import os
os.environ.setdefault("WAZUH_INDEXER_URL", "https://idx:9200")
os.environ.setdefault("WAZUH_INDEXER_PASSWORD", "pw")

import pytest
from mcp_server.tools.stealer_log import _parse_stealer_logs, StealerLogInput
from pydantic import ValidationError


def test_parse_stealer_logs_normalizes():
    raw = {"stealer_logs": [
        {"date_compromised": "2024-01-01", "malware": "RedLine",
         "computer_name": "victim-pc", "operating_system": "Windows",
         "infected_ips": ["1.2.3.4", "5.6.7.8", "9.9.9.9", "8.8.8.8", "7.7.7.7", "6.6.6.6"],
         "credentials": [{"a": 1}, {"a": 2}, {"a": 3}]},
    ]}
    out = _parse_stealer_logs(raw)
    assert len(out) == 1
    assert out[0]["malware"] == "RedLine"
    assert out[0]["credential_count"] == 3
    assert out[0]["infected_ips"] == ["1.2.3.4", "5.6.7.8", "9.9.9.9", "8.8.8.8", "7.7.7.7"]  # capped at 5


def test_parse_stealer_logs_empty():
    assert _parse_stealer_logs({}) == []
    assert _parse_stealer_logs({"stealer_logs": "not-a-list"}) == []


def test_input_rejects_invalid_email():
    with pytest.raises(ValidationError):
        StealerLogInput(email="not-an-email")


def test_input_accepts_email():
    assert StealerLogInput(email="CSIRT@Tangerangkota.go.id").email == "csirt@tangerangkota.go.id"
