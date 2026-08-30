#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Inbound authentication for the HTTP transports (streamable-http / http).
Independent of ``mcp_server/wazuh/auth.py`` (outbound JWT to the Wazuh Manager API).
Scope model (fail-closed):
- ``wazuh:read``  - default, granted to every valid key (read-only tools).
- ``wazuh:write`` - opt-in via MCP_API_KEY_SCOPES; required for tools whose
``readOnlyHint`` annotation is not True (or ``destructiveHint`` is True).
The write-tool set is derived at request time from the FastMCP registry's
tool annotations not a hardcoded allowlist, so a newly added write tool is
automatically protected with nothing extra to update.
"""
from __future__ import annotations
import hashlib
import hmac
import ipaddress
import json
import logging
import os
import secrets
import threading
import time
from collections import deque
from dataclasses import dataclass, field
from typing import Optional
from urllib.parse import urlparse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

logger = logging.getLogger("blue_team_mcp.server_auth")

READ_SCOPE = "wazuh:read"
WRITE_SCOPE = "wazuh:write"
_VALID_SCOPES = (READ_SCOPE, WRITE_SCOPE)

# "btm_" + secrets.token_urlsafe(32)  ->  4 + 43 = 47 chars
API_KEY_PREFIX = "btm_"
API_KEY_LENGTH = 47


@dataclass
class APIKey:
    """A validated inbound API key and it's granted scopes."""
    key_hash: bytes
    scopes: frozenset[str] = field(default_factory=lambda: frozenset({READ_SCOPE}))

    def has_scope(self, scope: str) -> bool:
        return scope in self.scopes


class ServerAuthManager:
    """Validate inbound ``Authorization: Bearer <api-key>`` credentials.
    Reads MCP_API_KEY / MCP_API_KEY_SCOPES from the environment at import.
    The key is stored only as a SHA-256 digest (the key is a 256-bit random
    token, so a plain digest suffices, no HMAC salt required), compared with
    ``hmac.compare_digest`` for constant-time equality.
    """
    def __init__(self) -> None:
        self._keys: dict[str, APIKey] = {}
        self._configured = False
        self._load_from_env()

    @property
    def configured(self) -> bool:
        """True when a well-formed MCP_API_KEY was loaded."""
        return self._configured

    def _load_from_env(self) -> None:
        raw = os.environ.get("MCP_API_KEY", "").strip()
        if not raw:
            return
        if not (raw.startswith(API_KEY_PREFIX) and len(raw) == API_KEY_LENGTH):
            logger.error(
                "MCP_API_KEY format invalid (expected %s<43-char-urlsafe-base64>, %d chars). "
                "Generate with: python3 -c \"import secrets; print('btm_' + secrets.token_urlsafe(32))\". "
                "HTTP transport will treat auth as unconfigured.",
                API_KEY_PREFIX, API_KEY_LENGTH,
            )
            return
        raw_scopes = os.environ.get("MCP_API_KEY_SCOPES", "").strip()
        scopes = frozenset(s for s in raw_scopes.split() if s in _VALID_SCOPES) or frozenset({READ_SCOPE})
        self._keys[raw] = APIKey(key_hash=self._hash(raw), scopes=scopes)
        self._configured = True
        logger.info("Inbound API key loaded (scopes: %s).", " ".join(sorted(scopes)))

    @staticmethod
    def _hash(api_key: str) -> bytes:
        return hashlib.sha256(api_key.encode()).digest()

    def validate_api_key(self, api_key: str) -> Optional[APIKey]:
        """Return the matching APIKey, or None if invalid/unconfigured."""
        if not api_key or not self._configured:
            return None
        digest = self._hash(api_key)
        for key in self._keys.values():
            if hmac.compare_digest(key.key_hash, digest):
                return key
        return None

    def authenticate(self, authorization: Optional[str]) -> Optional[APIKey]:
        """Parse ``Authorization: Bearer <key>`` and validate. None if invalid."""
        if not authorization or not authorization.startswith("Bearer "):
            return None
        return self.validate_api_key(authorization[7:].strip())


# Module
auth_manager = ServerAuthManager()


MAX_BODY_BYTES = 1_000_000   # 1 MB JSON-RPC request cap
MAX_JSON_DEPTH = 100         # reject deeper nesting before json.loads exhausts the stack

_OPEN = (0x5B, 0x7B)    # [ {
_CLOSE = (0x5D, 0x7D)   # ] }
_QUOTE = 0x22           # "
_BACKSLASH = 0x5C       # \


def _max_json_depth(data: bytes) -> int:
    depth = max_depth = 0
    in_string = escaped = False
    for b in data:
        if in_string:
            if escaped:
                escaped = False
            elif b == _BACKSLASH:
                escaped = True
            elif b == _QUOTE:
                in_string = False
        elif b == _QUOTE:
            in_string = True
        elif b in _OPEN:
            depth += 1
            max_depth = max(max_depth, depth)
        elif b in _CLOSE:
            depth -= 1
    return max_depth


def parse_json_body_safe(body: bytes) -> Optional[dict]:
    if len(body) > MAX_BODY_BYTES:
        logger.warning("Rejected oversized JSON-RPC body (%d bytes).", len(body))
        return None
    if _max_json_depth(body) > MAX_JSON_DEPTH:
        logger.warning("Rejected deeply nested JSON-RPC body.")
        return None
    try:
        payload = json.loads(body)
    except ValueError:
        return None
    return payload if isinstance(payload, dict) else None


class SlidingWindowRateLimiter:
    """Per-key sliding-window request limiter (opt-in, 60s window).
    one global lock + a deque of monotonic timestamps per key. Memory
    is bounded by pruning expired hits and sweeping stale keys past 10k clients.
    """

    _MAX_KEYS = 10_000

    def __init__(self, limit: int, window_seconds: float = 60.0):
        self.limit = max(0, int(limit))
        self.window = window_seconds
        self._hits: dict[str, deque] = {}
        self._lock = threading.Lock()

    def allow(self, key: str) -> bool:
        if self.limit <= 0:
            return True
        now = time.monotonic()
        with self._lock:
            dq = self._hits.get(key)
            if dq is None:
                dq = deque()
                self._hits[key] = dq
            while dq and now - dq[0] >= self.window:
                dq.popleft()
            if len(dq) >= self.limit:
                return False
            dq.append(now)
            if len(self._hits) > self._MAX_KEYS:
                stale = [k for k, d in self._hits.items() if not d or now - d[-1] >= self.window]
                for k in stale:
                    self._hits.pop(k, None)
            return True


def _origin_allowed(origin: str, allowed: frozenset[str]) -> bool:
    """True if an Origin header is safe: exact allowlist hit or a loopback origin."""
    if origin in allowed:
        return True
    host = urlparse(origin).hostname
    if host is None:
        return False  # opaque origin (e.g. "null") always reject
    if host.lower() == "localhost":
        return True
    try:
        return ipaddress.ip_address(host).is_loopback
    except ValueError:
        return False


# Inbound HTTP rate limit (requests/min per client IP; 0 = disabled). Separate
# from BLUETEAM_RATE_LIMIT, which gates destructive tools (fail2ban unban,
# tcpdump capture) with a per-minute global cap not request admission.
_http_rate_limit = 0
try:
    _http_rate_limit = max(0, int(os.environ.get("BLUETEAM_HTTP_RATE_LIMIT", "0")))
except ValueError:
    _http_rate_limit = 0
_rate_limiter = SlidingWindowRateLimiter(_http_rate_limit)
_allowed_origins = frozenset(
    o.strip() for o in os.environ.get("BLUETEAM_ALLOWED_ORIGINS", "").split(",") if o.strip()
)


def _write_tool_names() -> frozenset[str]:
    """Derive the write-tool set from FastMCP registry annotations.
    Fail-closed: a tool is write-scoped when readOnlyHint is *not explicitly
    True* (False or None) or destructiveHint is True.
    """
    try:
        from mcp_server import mcp
        tools = getattr(mcp._tool_manager, "_tools", {})
        return frozenset(
            name for name, t in tools.items()
            if (ann := getattr(t, "annotations", None)) is not None
            and (ann.readOnlyHint is not True or ann.destructiveHint is True)
        )
    except Exception as e:  # noqa: BLE001 - fail closed to empty set on registry error
        logger.error("Failed to derive write-tool set: %s", e)
        return frozenset()


class APIAuthMiddleware(BaseHTTPMiddleware):
    """Enforce API-key auth + write scope on the streamable-http transport.
    - 401 when the ``Authorization: Bearer <key>`` header is missing/invalid.
    - 403 when a ``tools/call`` targets a write tool but the key lacks wazuh:write.
    BaseHTTPMiddleware may interfere with SSE streaming responses in
    some Starlette versions. If the streamable-http transport ever serves
    long-lived SSE streams, replace with a pure-ASGI wrapper (header check
    only, no body read) authn still holds, per-request scope can move to a thin ``tools/call`` hook.
    """
    def __init__(self, app, dispatch=None):
        super().__init__(app, dispatch)
        self._write_tools = _write_tool_names()

    async def dispatch(self, request: Request, call_next):
        # 1. Inbound rate limit (per client IP) before any other work.
        client_ip = request.client.host if request.client else "unknown"
        if not _rate_limiter.allow(client_ip):
            return JSONResponse({"error": "Too many requests"}, status_code=429)

        # 2. Origin validation reject cross-origin browser requests.
        origin = request.headers.get("origin")
        if origin is not None and not _origin_allowed(origin, _allowed_origins):
            return JSONResponse({"error": "Forbidden: origin not allowed"}, status_code=403)

        # 3. Inbound API-key auth (only enforced when a key is configured).
        key = None
        if auth_manager.configured:
            key = auth_manager.authenticate(request.headers.get("authorization"))
            if key is None:
                return JSONResponse(
                    {"error": "Unauthorized: valid MCP_API_KEY required"},
                    status_code=401,
                    headers={"WWW-Authenticate": 'Bearer realm="blue_team_mcp"'},
                )

        # 4. Body guard + write scope check (POST only body is cached for downstream).
        if request.method == "POST":
            try:
                body = await request.body()
            except Exception:  # client disconnect / read error reject, don't crash.
                return JSONResponse({"error": "Bad request"}, status_code=400)
            payload = parse_json_body_safe(body)
            if payload is None:
                return JSONResponse({"error": "Invalid or oversized JSON body"}, status_code=400)
            tool_name = None
            if payload.get("method") == "tools/call" and isinstance(payload.get("params"), dict):
                name = (payload.get("params") or {}).get("name")
                tool_name = name if isinstance(name, str) else None
            if key is not None and tool_name and tool_name in self._write_tools and not key.has_scope(WRITE_SCOPE):
                return JSONResponse(
                    {"error": f"Forbidden: tool '{tool_name}' requires '{WRITE_SCOPE}' scope"},
                    status_code=403,
                )

        return await call_next(request)


def serve_authenticated(mcp, host: str, port: int, log_level: str = "INFO") -> None:
    """Serve the streamable-http transport with hardening middleware."""
    import uvicorn
    app = mcp.streamable_http_app()
    # Always install: rate limiting + origin validation apply even without a key;
    # auth itself is a no-op branch unless MCP_API_KEY is configured.
    app.add_middleware(APIAuthMiddleware)
    if not auth_manager.configured:
        logger.warning(
            "MCP_API_KEY not set - serving HTTP transport WITHOUT inbound auth "
            "(loopback only; non-loopback bind is refused at startup)."
        )
    config = uvicorn.Config(app, host=host, port=port, log_level=log_level.lower())
    uvicorn.Server(config).run()


if __name__ == "__main__":   # self-check
    _os = os
    _os.environ["MCP_API_KEY"] = API_KEY_PREFIX + secrets.token_urlsafe(32)
    _os.environ["MCP_API_KEY_SCOPES"] = READ_SCOPE
    _m = ServerAuthManager()
    _raw = _os.environ["MCP_API_KEY"]
    assert _m.configured is True
    _k = _m.validate_api_key(_raw)
    assert _k is not None and _k.has_scope(READ_SCOPE) and not _k.has_scope(WRITE_SCOPE)
    assert _m.validate_api_key(API_KEY_PREFIX + secrets.token_urlsafe(32)) is None  # wrong key
    assert _m.authenticate(None) is None
    assert _m.authenticate("Bearer " + _raw) is not None
    assert _m.authenticate("Bearer wrong") is None
    _os.environ["MCP_API_KEY"] = "short"  # malformed -> unconfigured
    assert ServerAuthManager().configured is False
    print("server_auth self-check OK")
