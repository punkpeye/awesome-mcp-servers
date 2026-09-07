#!/usr/bin/env python3
"""Tests for URLhaus + CMDB asset context."""
from __future__ import annotations


def test_urlhaus_hash_input_model():
    from mcp_server.tools.urlhaus import UrlhausHashInput
    # Valid MD5
    inp = UrlhausHashInput(file_hash="b325c92fa540edeb89b95dbfd4400c1c")
    assert inp.file_hash == "b325c92fa540edeb89b95dbfd4400c1c"
    # Valid SHA256 (lowercased)
    inp2 = UrlhausHashInput(file_hash="A" * 64)
    assert inp2.file_hash == "a" * 64


def test_urlhaus_hash_input_rejects_invalid():
    from mcp_server.tools.urlhaus import UrlhausHashInput
    from pydantic import ValidationError
    try:
        UrlhausHashInput(file_hash="not-a-hash")
        assert False, "Should have raised"
    except ValidationError:
        pass


def test_urlhaus_input_model():
    from mcp_server.tools.urlhaus import UrlhausLookupInput
    inp = UrlhausLookupInput(url="http://evil.com/malware.exe")
    assert inp.url == "http://evil.com/malware.exe"


def test_urlhaus_bulk_input_model():
    from mcp_server.tools.urlhaus import UrlhausBulkInput
    inp = UrlhausBulkInput(urls=["http://a.com/x.php", "http://b.com/y.php"])
    assert len(inp.urls) == 2


def test_cmdb_find_exact_match():
    from mcp_server.tools.asset_context import _load_cmdb, _find_asset
    import json, tempfile, os
    assets = [{"host": "csirt.tangerangkota.go.id", "name": "CSIRT Portal",
               "owner": "Dinas Komunikasi & Informatika", "criticality": "high",
               "environment": "production"}]
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(assets, f)
        path = f.name
    try:
        # Monkeypatch the module's _CMDB_FILE
        import mcp_server.tools.asset_context as ac
        ac._CMDB_FILE = path
        ac._CMDB_CACHE = {}
        ac._CMDB_CACHE_MTIME = 0
        asset = _find_asset("csirt.tangerangkota.go.id")
        assert asset is not None
        assert asset["name"] == "CSIRT Portal"
        assert asset["criticality"] == "high"
    finally:
        os.unlink(path)
        ac._CMDB_FILE = ""


def test_cmdb_find_subdomain_match():
    from mcp_server.tools.asset_context import _find_asset
    import json, tempfile, os
    assets = [{"host": "tangerangkota.go.id", "name": "Root domain",
               "owner": "Diskominfo", "criticality": "medium"}]
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(assets, f)
        path = f.name
    try:
        import mcp_server.tools.asset_context as ac
        ac._CMDB_FILE = path
        ac._CMDB_CACHE = {}
        ac._CMDB_CACHE_MTIME = 0
        # Subdomain matches root domain
        asset = _find_asset("csirt.tangerangkota.go.id")
        assert asset is not None
        assert asset["host"] == "tangerangkota.go.id"
    finally:
        os.unlink(path)
        ac._CMDB_FILE = ""


def test_cmdb_not_found():
    from mcp_server.tools.asset_context import _find_asset
    import json, tempfile, os
    assets = [{"host": "known.tangerangkota.go.id", "name": "Known"}]
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(assets, f)
        path = f.name
    try:
        import mcp_server.tools.asset_context as ac
        ac._CMDB_FILE = path
        ac._CMDB_CACHE = {}
        ac._CMDB_CACHE_MTIME = 0
        assert _find_asset("unknown.example.com") is None
    finally:
        os.unlink(path)
        ac._CMDB_FILE = ""


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
