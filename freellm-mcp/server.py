#!/usr/bin/env python3
"""
FreeLLM-MCP: Model Context Protocol server exposing live measured free LLM API metrics.
Reads a configured status JSON file or fetches the public board and serves JSON-RPC tools over stdio
(default) or a localhost Streamable-HTTP endpoint (FREEMCP_TRANSPORT=http).
"""

import sys
import json
import os
import time
import urllib.request
from http.server import BaseHTTPRequestHandler

DEFAULT_REMOTE_URL = "https://freellmwatch.xyz/api/status.json"
DEFAULT_CACHE_PATH = os.path.join(
    os.environ.get("XDG_CACHE_HOME", os.path.expanduser("~/.cache")),
    "freellm-mcp",
    "status.json",
)
CACHE_TTL_SECONDS = 300
HTTP_TIMEOUT_SECONDS = 10


def _uptime_percent(value):
    """Return the board's uptime fraction as a 0-100 percentage."""
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        return None
    if 0 <= value <= 1:
        value *= 100
    return round(value, 1)


def _read_json(path):
    with open(path, "r") as f:
        return json.load(f)


def _fetch_remote(url):
    req = urllib.request.Request(url, headers={"User-Agent": "freellm-mcp/1.0"})
    with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT_SECONDS) as resp:
        return json.loads(resp.read().decode("utf-8"))


def load_status(force_refresh=False):
    """Load board data.

    Order: an explicit FREEMCP_STATUS_PATH (or the local board file if it exists),
    then a cached remote copy younger than CACHE_TTL_SECONDS, then a live fetch of
    https://freellmwatch.xyz/api/status.json (which is written back to the cache).

    This is what lets the server run on a machine that is not the observatory box.
    """
    configured = os.environ.get("FREEMCP_STATUS_PATH")
    candidates = [configured] if configured else ["/srv/ember/site/api/status.json"]
    for path in candidates:
        if path and os.path.exists(path):
            try:
                return _read_json(path)
            except Exception:
                pass

    cache_path = os.environ.get("FREEMCP_CACHE_PATH", DEFAULT_CACHE_PATH)
    if not force_refresh:
        try:
            if os.path.exists(cache_path) and (time.time() - os.path.getmtime(cache_path)) < CACHE_TTL_SECONDS:
                return _read_json(cache_path)
        except Exception:
            pass

    url = os.environ.get("FREEMCP_REMOTE_URL", DEFAULT_REMOTE_URL)
    try:
        data = _fetch_remote(url)
        try:
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)
            with open(cache_path, "w") as f:
                json.dump(data, f)
        except Exception:
            pass
        return data
    except Exception:
        pass

    try:
        if os.path.exists(cache_path):
            return _read_json(cache_path)
    except Exception:
        pass

    return {"generated_at": None, "models": [], "source": None, "unavailable": True}

def _provenance(data):
    return {
        "generated_at": data.get("generated_at"),
        "source": data.get("source") or DEFAULT_REMOTE_URL,
        "measured_by": "Free LLM Watch (https://freellmwatch.xyz/)",
        "stale": bool(data.get("unavailable")),
    }


def tool_list_free_models(args):
    data = load_status()
    models = data.get("models", [])
    result = []
    for m in models:
        result.append({
            "model_id": m.get("id"),
            "provider": m.get("provider"),
            "status": m.get("status"),
            "tokens_per_s": m.get("tokens_per_s"),
            "uptime_7d": _uptime_percent(m.get("uptime_7d")),
            "uptime_24h": _uptime_percent(m.get("uptime_24h")),
            "tool_calling": m.get("tool_calling"),
            "last_error": m.get("last_error")
        })
    out = {"models": result, "total": len(result)}
    out.update(_provenance(data))
    return out

def tool_get_fastest_free_model(args):
    data = load_status()
    models = data.get("models", [])
    up_models = [m for m in models if m.get("status") == "up" and isinstance(m.get("tokens_per_s"), (int, float))]
    if not up_models:
        return {"error": "No healthy free models with throughput data currently up."}
    fastest = max(up_models, key=lambda x: x["tokens_per_s"])
    out = {
        "model_id": fastest.get("id"),
        "provider": fastest.get("provider"),
        "tokens_per_s": fastest.get("tokens_per_s"),
        "uptime_7d": _uptime_percent(fastest.get("uptime_7d")),
        "uptime_24h": _uptime_percent(fastest.get("uptime_24h")),
        "tool_calling": fastest.get("tool_calling"),
    }
    out.update(_provenance(data))
    return out

def tool_check_model_status(args):
    model_id = args.get("model_id")
    if not model_id:
        return {"error": "Missing required argument 'model_id'"}
    data = load_status()
    models = data.get("models", [])
    match = next((m for m in models if m.get("id") == model_id), None)
    if not match:
        return {"error": f"Model '{model_id}' not found in registry."}
    out = dict(match)
    # Keep the same field name the other tools use, so an agent can switch between
    # tools without special-casing this one. The board's raw key is "id".
    out["model_id"] = match.get("id")
    out.update(_provenance(data))
    return out


def tool_get_most_reliable_free_model(args):
    data = load_status()
    models = data.get("models", [])
    candidates = [
        m for m in models
        if isinstance(m.get("uptime_7d"), (int, float)) and m.get("status") == "up"
    ]
    if not candidates:
        return {"error": "No healthy free models with 7-day uptime data currently up."}
    best = max(candidates, key=lambda x: x["uptime_7d"])
    out = {
        "model_id": best.get("id"),
        "provider": best.get("provider"),
        "uptime_7d": best.get("uptime_7d"),
        "uptime_24h": best.get("uptime_24h"),
        "tokens_per_s": best.get("tokens_per_s"),
        "tool_calling": best.get("tool_calling"),
    }
    out.update(_provenance(data))
    return out

def tool_get_recent_model_changes(args):
    """Get recent roster changes detected by the automated change detector.

    Returns the last N roster changes (arrivals and departures) with timestamps.
    Useful for agents that want to track which free models came and went.
    """
    import json
    from pathlib import Path

    DETECTOR_DIR = Path("experiments/roster_churn_detector")
    EVENTS_FILE = DETECTOR_DIR / "events.json"

    try:
        if EVENTS_FILE.exists():
            with open(EVENTS_FILE, 'r') as f:
                events = json.load(f)
        else:
            events = []
    except Exception as e:
        return {"error": f"Failed to read events file: {e}"}

    # Sort events by detection_time descending
    events.sort(key=lambda e: e.get("detection_time", ""), reverse=True)

    # Limit to last 50 events to keep responses reasonable
    recent_events = events[:50]

    # Transform into a list of event summaries
    event_list = []
    for event in recent_events:
        summary = {
            "event_id": event.get("event_id"),
            "model_id": event.get("model_id"),
            "kind": event.get("kind"),
            "first_seen": event.get("first_seen") if event.get("kind") == "arrival" else None,
            "last_status": event.get("last_status") if event.get("kind") == "departure" else None,
            "detection_time": event.get("detection_time"),
            "source_snapshot": event.get("source_snapshot"),
        }
        event_list.append(summary)

    out = {"events": event_list, "total": len(event_list), "since": len(events) - len(event_list) if event_list else 0}
    out.update(_provenance(load_status()))
    return out

TOOLS = {
    "list_free_models": tool_list_free_models,
    "get_fastest_free_model": tool_get_fastest_free_model,
    "get_most_reliable_free_model": tool_get_most_reliable_free_model,
    "check_model_status": tool_check_model_status,
    "recent_model_changes": tool_get_recent_model_changes,
}

SUPPORTED_PROTOCOL_VERSIONS = ("2025-11-25", "2025-06-18", "2025-03-26", "2024-11-05")


def _negotiate_protocol(params):
    """Echo the client's protocol version when we support it, else our oldest.

    The spec says a server that does not support the requested version must answer
    with one it does; answering with the bare oldest would silently downgrade
    clients that asked for something newer.
    """
    requested = (params or {}).get("protocolVersion")
    if requested in SUPPORTED_PROTOCOL_VERSIONS:
        return requested
    return SUPPORTED_PROTOCOL_VERSIONS[-1]


def handle_request(req):
    method = req.get("method")
    req_id = req.get("id")
    params = req.get("params") or {}

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": _negotiate_protocol(params),
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": {"name": "freellm-mcp", "version": "1.1.0"}
            }
        }
    elif method == "ping":
        return {"jsonrpc": "2.0", "id": req_id, "result": {}}
    elif method == "notifications/initialized":
        return None # Notification, no response
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "list_free_models",
                        "description": "List all tracked free LLM APIs with live measured status, throughput (tokens/sec), uptime, and tool-calling support.",
                        "inputSchema": {"type": "object", "properties": {}}
                    },
                    {
                        "name": "get_fastest_free_model",
                        "description": "Get the currently fastest healthy free LLM API by measured tokens/second.",
                        "inputSchema": {"type": "object", "properties": {}}
                    },
                    {
                        "name": "get_most_reliable_free_model",
                        "description": "Get the free LLM API with the highest measured 7-day uptime among those currently answering.",
                        "inputSchema": {"type": "object", "properties": {}}
                    },
                    {
                        "name": "check_model_status",
                        "description": "Get detailed live metrics and error history for a specific free model ID.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "model_id": {"type": "string", "description": "The model ID (e.g. gemini/gemini-2.5-flash)"}
                            },
                            "required": ["model_id"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        tool_name = params.get("name")
        arguments = params.get("arguments") or {}
        if tool_name not in TOOLS:
            # Per the MCP tool-error convention the model should *see* the failure, not
            # have the client raise on it: return a normal result flagged isError.
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": (
                        f"Unknown tool '{tool_name}'. Available tools: "
                        + ", ".join(sorted(TOOLS))) }],
                    "isError": True,
                }
            }
        try:
            res = TOOLS[tool_name](arguments)
        except Exception as e:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{"type": "text", "text": f"Tool '{tool_name}' failed: {e}"}],
                    "isError": True,
                }
            }
        out = {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]},
        }
        if not isinstance(res, dict) or "error" in res:
            out["result"]["isError"] = True
        return out
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {"code": -32601, "message": f"Method not found: {method}"}
        }

def _send_json(handler, code: int, obj: dict) -> None:
    """Write one JSON response with an explicit length."""
    data = json.dumps(obj).encode("utf-8")
    handler.send_response(code)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(data)))
    handler.end_headers()
    handler.wfile.write(data)


def _read_json_body(handler) -> dict:
    try:
        length = int(handler.headers.get("Content-Length") or 0)
    except ValueError:
        raise ValueError("invalid Content-Length")
    if length <= 0:
        raise ValueError("request body must be JSON")
    if length > 2_000_000:
        raise ValueError("request body too large")
    raw = handler.rfile.read(length)
    body = json.loads(raw.decode("utf-8"))
    if not isinstance(body, dict):
        raise ValueError("request body must be a JSON object")
    return body


def make_mcp_http_handler() -> type[BaseHTTPRequestHandler]:
    """Build the Streamable-HTTP handler for the local, unauthenticated endpoint.

    POST carries one JSON-RPC message and receives one JSON response. The server
    does not advertise sessions or server-initiated streams, so GET is rejected.
    """
    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def log_message(self, fmt, *args):
            pass

        def _error(self, code: int, message: str) -> None:
            _send_json(self, code, {"error": message})

        def do_OPTIONS(self) -> None:
            self.send_response(204)
            self.send_header("Allow", "POST, OPTIONS")
            self.send_header("Content-Length", "0")
            self.end_headers()

        def do_GET(self) -> None:
            self.send_response(405)
            self.send_header("Allow", "POST, OPTIONS")
            self.send_header("Content-Length", "0")
            self.end_headers()

        def do_DELETE(self) -> None:
            self.send_response(405)
            self.send_header("Allow", "POST, OPTIONS")
            self.send_header("Content-Length", "0")
            self.end_headers()

        def do_POST(self) -> None:
            if self.path.rstrip("/") != "/mcp":
                return self._error(404, "not found")
            try:
                body = _read_json_body(self)
            except (ValueError, UnicodeDecodeError, json.JSONDecodeError) as exc:
                return _send_json(self, 400, {
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {"code": -32700, "message": str(exc)},
                })
            if "method" not in body:
                return _send_json(self, 400, {
                    "jsonrpc": "2.0",
                    "id": body.get("id"),
                    "error": {"code": -32600, "message": "invalid request"},
                })
            response = handle_request(body)
            if response is None:
                self.send_response(202)
                self.send_header("Content-Length", "0")
                self.end_headers()
            else:
                _send_json(self, 200, response)

    return Handler


def serve_http(port: int) -> None:
    """Run the HTTP transport on localhost; the public site can reverse-proxy it."""
    from http.server import ThreadingHTTPServer

    server = ThreadingHTTPServer(("127.0.0.1", port), make_mcp_http_handler())
    server.daemon_threads = True
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


def main() -> int:
    transport = os.environ.get("FREEMCP_TRANSPORT", "stdio").lower()
    if transport in {"http", "streamable-http", "streamable_http"}:
        try:
            port = int(os.environ.get("FREEMCP_HTTP_PORT", "8901"))
        except ValueError:
            print("FREEMCP_HTTP_PORT must be an integer", file=sys.stderr)
            return 2
        print(f"FreeLLMCP Streamable HTTP endpoint listening on http://127.0.0.1:{port}/mcp", file=sys.stderr)
        serve_http(port)
        return 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except Exception:
            continue
        resp = handle_request(req)
        if resp is not None:
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
    return 0

if __name__ == "__main__":
    sys.exit(main())
