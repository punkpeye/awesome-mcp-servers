import json
import os
import tempfile
import pytest
from server import handle_request, load_status, make_mcp_http_handler

@pytest.fixture
def mock_status_file():
    sample_data = {
        "generated_at": "2026-09-21T19:00:00Z",
        "models": [
            {
                "id": "test/model-fast",
                "provider": "test",
                "status": "up",
                "tokens_per_s": 85.5,
                "uptime_7d": 0.99,
                "uptime_24h": 1.0,
                "tool_calling": True,
                "last_error": None
            },
            {
                "id": "test/model-slow",
                "provider": "test",
                "status": "up",
                "tokens_per_s": 20.0,
                "uptime_7d": 90.0,
                "tool_calling": False,
                "last_error": None
            },
            {
                "id": "test/model-down",
                "provider": "test",
                "status": "down",
                "tokens_per_s": None,
                "uptime_7d": 40.0,
                "tool_calling": False,
                "last_error": "rate limit 429"
            }
        ]
    }
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as tf:
        json.dump(sample_data, tf)
        temp_name = tf.name
    
    os.environ["FREEMCP_STATUS_PATH"] = temp_name
    yield temp_name
    if os.path.exists(temp_name):
        os.unlink(temp_name)

def test_initialize(mock_status_file):
    req = {"jsonrpc": "2.0", "id": 1, "method": "initialize"}
    resp = handle_request(req)
    assert resp["result"]["serverInfo"]["name"] == "freellm-mcp"

def test_tools_list(mock_status_file):
    req = {"jsonrpc": "2.0", "id": 2, "method": "tools/list"}
    resp = handle_request(req)
    tools = resp["result"]["tools"]
    names = [t["name"] for t in tools]
    assert "list_free_models" in names
    assert "get_fastest_free_model" in names
    assert "check_model_status" in names

def test_tool_call_list_free_models(mock_status_file):
    req = {
        "jsonrpc": "2.0",
        "id": 3,
        "method": "tools/call",
        "params": {"name": "list_free_models", "arguments": {}}
    }
    resp = handle_request(req)
    content = json.loads(resp["result"]["content"][0]["text"])
    assert content["total"] == 3

def test_tool_call_get_fastest_free_model(mock_status_file):
    req = {
        "jsonrpc": "2.0",
        "id": 4,
        "method": "tools/call",
        "params": {"name": "get_fastest_free_model", "arguments": {}}
    }
    resp = handle_request(req)
    content = json.loads(resp["result"]["content"][0]["text"])
    assert content["model_id"] == "test/model-fast"
    assert content["tokens_per_s"] == 85.5

def test_tool_call_check_model_status(mock_status_file):
    req = {
        "jsonrpc": "2.0",
        "id": 5,
        "method": "tools/call",
        "params": {"name": "check_model_status", "arguments": {"model_id": "test/model-down"}}
    }
    resp = handle_request(req)
    content = json.loads(resp["result"]["content"][0]["text"])
    assert content["status"] == "down"
    assert content["last_error"] == "rate limit 429"


def test_check_model_status_exposes_model_id_alias(mock_status_file):
    """Every tool must speak the same field name.

    The board's raw key is `id`; agents that got `model_id` from list_free_models
    must be able to feed it straight back into check_model_status and get it echoed.
    """
    req = {
        "jsonrpc": "2.0",
        "id": 6,
        "method": "tools/call",
        "params": {"name": "check_model_status", "arguments": {"model_id": "test/model-slow"}},
    }
    content = json.loads(handle_request(req)["result"]["content"][0]["text"])
    assert content["model_id"] == "test/model-slow"
    assert content["tokens_per_s"] == 20.0
    assert "Free LLM Watch" in content["measured_by"]


def test_get_fastest_free_model_carries_provenance(mock_status_file):
    """A number without its source is not evidence: every payload names the measurer."""
    req = {"jsonrpc": "2.0", "id": 7, "method": "tools/call",
           "params": {"name": "get_fastest_free_model", "arguments": {}}}
    content = json.loads(handle_request(req)["result"]["content"][0]["text"])
    assert content["model_id"] == "test/model-fast"
    assert "Free LLM Watch" in content["measured_by"]
    assert content["generated_at"] == "2026-09-21T19:00:00Z"
    assert content["stale"] is False


def test_list_free_models_normalizes_uptime_fractions(mock_status_file):
    """The board stores fractions; agents receive human-readable percentages."""
    req = {
        "jsonrpc": "2.0", "id": 10, "method": "tools/call",
        "params": {"name": "list_free_models", "arguments": {}},
    }
    content = json.loads(handle_request(req)["result"]["content"][0]["text"])
    assert content["models"][0]["uptime_7d"] == 99.0
    assert content["models"][0]["uptime_24h"] == 100.0


def test_negotiates_newest_handshake_version(mock_status_file):
    """A client asking for a version we support must get that version back."""
    for requested in ("2025-11-25", "2025-06-18", "2024-11-05"):
        req = {"jsonrpc": "2.0", "id": 8, "method": "initialize",
               "params": {"protocolVersion": requested}}
        assert handle_request(req)["result"]["protocolVersion"] == requested
    # An unknown future version must not be echoed back as if we spoke it.
    req = {"jsonrpc": "2.0", "id": 9, "method": "initialize",
           "params": {"protocolVersion": "2099-01-01"}}
    assert handle_request(req)["result"]["protocolVersion"] == "2024-11-05"



# --- HTTP transport path (FREEMCP_TRANSPORT=http) ---------------------------
# Added 2026-09-25 after a splice made make_mcp_http_handler return None and
# crashed the http transport with no test coverage. This exercises the whole
# POST /mcp round-trip over a real socket.

def test_http_transport_answers_initialize(mock_status_file):
    from http.server import ThreadingHTTPServer
    import threading
    import urllib.request
    import urllib.error

    handler = make_mcp_http_handler()
    assert handler is not None, "make_mcp_http_handler must return a handler class"

    httpd = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    httpd.daemon_threads = True
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    try:
        port = httpd.server_address[1]
        url = f"http://127.0.0.1:{port}/mcp"
        req = urllib.request.Request(
            url,
            data=json.dumps({"jsonrpc": "2.0", "id": 1, "method": "initialize"}).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
        resp = json.loads(urllib.request.urlopen(req, timeout=5).read().decode("utf-8"))
        assert resp["result"]["serverInfo"]["name"] == "freellm-mcp"
        assert resp["id"] == 1

        # A tools/call through the same socket proves the full round-trip works.
        req2 = urllib.request.Request(
            url,
            data=json.dumps({
                "jsonrpc": "2.0", "id": 2, "method": "tools/call",
                "params": {"name": "list_free_models", "arguments": {}},
            }).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
        resp2 = json.loads(urllib.request.urlopen(req2, timeout=5).read().decode("utf-8"))
        content = json.loads(resp2["result"]["content"][0]["text"])
        assert content["total"] == 3
    finally:
        httpd.shutdown()
        httpd.server_close()


def test_http_transport_rejects_wrong_path(mock_status_file):
    from http.server import ThreadingHTTPServer
    import threading
    import urllib.request
    import urllib.error

    handler = make_mcp_http_handler()
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    httpd.daemon_threads = True
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    try:
        port = httpd.server_address[1]
        url = f"http://127.0.0.1:{port}/not-mcp"
        req = urllib.request.Request(
            url,
            data=b'{"jsonrpc":"2.0","id":1,"method":"initialize"}',
            headers={"Content-Type": "application/json"},
        )
        try:
            urllib.request.urlopen(req, timeout=5)
            assert False, "expected 404 on wrong path"
        except urllib.error.HTTPError as e:
            assert e.code == 404
    finally:
        httpd.shutdown()
        httpd.server_close()
