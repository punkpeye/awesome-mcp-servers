#!/usr/bin/env python3
"""Tests for webshell_check.py signature scanner"""
from __future__ import annotations


def test_scan_body_detects_b374k():
    from mcp_server.tools.webshell_check import _scan_body, _verdict
    body = "<html>b374k shell v2.8</html>"
    matches = _scan_body(body)
    assert len(matches) >= 1
    assert any("b374k" in m["family"] for m in matches)


def test_scan_body_detects_eval_base64():
    from mcp_server.tools.webshell_check import _scan_body, _verdict
    body = "<?php eval(base64_decode('cGhwaW5mbygpOw==')); ?>"
    matches = _scan_body(body)
    assert len(matches) >= 1
    assert any("Obfuscated" in m["family"] for m in matches)


def test_scan_body_detects_system_call():
    from mcp_server.tools.webshell_check import _scan_body
    body = "<?php system('id'); ?>"
    matches = _scan_body(body)
    assert len(matches) >= 1
    assert any("system()" in m["family"] for m in matches)


def test_clean_body_returns_empty():
    from mcp_server.tools.webshell_check import _scan_body, _verdict
    body = "<html><body>TangerangKota</body></html>"
    matches = _scan_body(body)
    assert matches == []


def test_verdict_confirmed():
    from mcp_server.tools.webshell_check import _verdict
    assert _verdict([
        {"weight": "high", "family": "b374k"},
        {"weight": "high", "family": "eval+base64"},
    ]) == "CONFIRMED"
    # Single high-weight match with login page -> suspicious, not login_page.
    assert _verdict([
        {"weight": "high", "family": "b374k"},
    ]) == "SUSPICIOUS"


def test_verdict_suspicious():
    from mcp_server.tools.webshell_check import _verdict
    assert _verdict([
        {"weight": "medium", "family": "system()"},
        {"weight": "medium", "family": "exec()"},
    ]) == "SUSPICIOUS"


def test_verdict_login_page():
    from mcp_server.tools.webshell_check import _verdict
    assert _verdict([
        {"weight": "high", "family": "b374k login page", "is_login_page": True},
    ]) == "LOGIN_PAGE"


def test_login_context_extraction():
    from mcp_server.tools.webshell_check import _extract_login_context
    body = """<html><head><title>b374k mini shell v3.2 :: Login</title></head>
    <body><h1>b374k</h1>
    <form method="post" action="">
    <input type="password" name="pass" placeholder="Password">
    <input type="submit" value="Login">
    </form></body></html>"""
    ctx = _extract_login_context(body)
    assert "b374k" in ctx
    assert "password" in ctx.lower()
    assert "TITLE:" in ctx
    assert "FORMS" in ctx


def test_verdict_clean():
    from mcp_server.tools.webshell_check import _verdict
    assert _verdict([]) == "CLEAN"


def test_url_validation_rejects_private_ip():
    from mcp_server.tools.webshell_check import WebshellCheckInput
    from pydantic import ValidationError
    try:
        WebshellCheckInput(url="http://10.0.0.1/shell.php")
        assert False, "Should have raised"
    except ValidationError:
        pass


def test_url_validation_accepts_public_domain():
    from mcp_server.tools.webshell_check import WebshellCheckInput
    ws = WebshellCheckInput(url="https://csirt.tangerangkota.go.id/asu.php")
    assert ws.url == "https://csirt.tangerangkota.go.id/asu.php"


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
