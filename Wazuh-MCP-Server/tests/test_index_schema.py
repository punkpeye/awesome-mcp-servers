#!/usr/bin/env python3
"""Tests for index schema explorer."""
from __future__ import annotations


def test_flatten_props_nested():
    from mcp_server.tools.index_schema import _flatten_props
    props = {
        "data": {"properties": {"srcip": {"type": "keyword"},
                                 "url": {"type": "text", "fields": {"keyword": {"type": "keyword"}}}}},
        "rule": {"properties": {"id": {"type": "keyword"}}},
    }
    out = {}
    _flatten_props("", props, out)
    assert "data.srcip" in out
    assert "data.url" in out
    assert "rule.id" in out


def test_field_info_keyword():
    from mcp_server.tools.index_schema import _field_info
    info = _field_info({"type": "keyword"})
    assert info["type"] == "keyword"
    assert info["has_keyword_subfield"] is False
    assert info["agg_safe"] is True  # plain keyword is aggregation-safe


def test_field_info_text_with_keyword_subfield():
    from mcp_server.tools.index_schema import _field_info
    info = _field_info({"type": "text", "fields": {"keyword": {"type": "keyword"}}})
    assert info["type"] == "text"
    assert info["has_keyword_subfield"] is True
    assert info["agg_safe"] is True  # .keyword sub-field available


def test_field_info_text_no_keyword():
    from mcp_server.tools.index_schema import _field_info
    info = _field_info({"type": "text"})
    assert info["has_keyword_subfield"] is False
    assert info["agg_safe"] is False  # text without .keyword is NOT agg-safe


def test_input_model():
    from mcp_server.tools.index_schema import IndexSchemaInput
    inp = IndexSchemaInput(fields=["data.srcip", "rule.groups"])
    assert inp.fields == ["data.srcip", "rule.groups"]
    inp2 = IndexSchemaInput()  # default
    assert inp2.index == "wazuh-alerts-*"
    assert inp2.fields == []


if __name__ == "__main__":
    import sys, traceback
    tests = [f for f in dir() if f.startswith("test_")]
    passed = 0
    for t in tests:
        try:
            globals()[t]()
            print(f"  PASS {t}")
            passed += 1
        except Exception:
            print(f"  FAIL {t}")
            traceback.print_exc()
    print(f"\n{passed}/{len(tests)} passed")
    sys.exit(0 if passed == len(tests) else 1)
