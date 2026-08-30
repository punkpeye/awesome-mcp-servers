#!/usr/bin/env python3
"""
Validator unit tests agent_id zfill + timestamp date-math/ISO.
"""
import os

os.environ.setdefault("WAZUH_INDEXER_URL", "https://indexer:9200")
os.environ.setdefault("WAZUH_INDEXER_PASSWORD", "x")

import pytest

from mcp_server.core.validators import _validate_agent_id_field, _validate_timestamp_field
from mcp_server.wazuh.time_utils import _parse_time_window


def test_agent_id_zfill():
    assert _validate_agent_id_field("1") == "001"
    assert _validate_agent_id_field("227") == "227"
    assert _validate_agent_id_field("99999") == "99999"
    assert _validate_agent_id_field(" 42 ") == "042"
    assert _validate_agent_id_field(None) is None
    assert _validate_agent_id_field("") is None


def test_agent_id_rejects_non_numeric():
    with pytest.raises(ValueError):
        _validate_agent_id_field("abc")
    with pytest.raises(ValueError):
        _validate_agent_id_field("12a")
    with pytest.raises(ValueError):
        _validate_agent_id_field("123456")  # > 5 digits


def test_timestamp_valid():
    assert _validate_timestamp_field("24h") == "24h"
    assert _validate_timestamp_field("7d") == "7d"
    assert _validate_timestamp_field("2026-08-18") == "2026-08-18"
    assert _validate_timestamp_field("2026-08-18T17:27:00Z") == "2026-08-18T17:27:00Z"
    assert _validate_timestamp_field("now-24h") == "now-24h"
    assert _validate_timestamp_field("now-7d/d") == "now-7d/d"
    assert _validate_timestamp_field("NOW-24h") == "now-24h"  # normalized
    assert _validate_timestamp_field(None) is None


def test_timestamp_rejects_garbage():
    with pytest.raises(ValueError):
        _validate_timestamp_field("garbage")
    with pytest.raises(ValueError):
        _validate_timestamp_field("now-24x")  # bad unit


def test_parse_time_window_date_math():
    from datetime import datetime
    since, until = _parse_time_window("now-24h", None)
    s = datetime.fromisoformat(since.replace("Z", "+00:00"))
    u = datetime.fromisoformat(until.replace("Z", "+00:00"))
    delta = (u - s).total_seconds()
    assert 86000 <= delta <= 86401  # ~24h
