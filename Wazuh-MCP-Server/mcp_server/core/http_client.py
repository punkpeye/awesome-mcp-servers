#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
HTTP client pool, unified API call helper, error handling, IP validation.
"""
from __future__ import annotations
import asyncio, ipaddress, json, logging, random, time
from typing import Any, Dict, Optional, Annotated
import httpx
from pydantic import AfterValidator
from mcp_server import WAZUH_INDEXER_VERIFY_SSL
from mcp_server import HTTP_TIMEOUT, WAZUH_API_VERIFY_SSL, WAZUH_INDEXER_VERIFY_SSL, ARGUS_VERIFY_SSL

logger = logging.getLogger("blue_team_mcp.http")

# http2 requires the optional 'h2' package (httpx[http2] extra). Degrade to
# http/1.1 gracefully when it's absent (e.g. minimal test/CI environments), so
# the server never fails to boot just because the optional dependency is missing.
try:
    import h2  # noqa: F401
    _HTTP2 = True
except ImportError:
    _HTTP2 = False

# Private / reserved IP ranges threat-intel tools are for public IPs only
_PRIVATE_NETWORKS: list = []

# Shared HTTP clients by name, pooled per SSL trust domain.
_clients: dict[str, httpx.AsyncClient] = {}

_MSEARCH_FALLBACK_ERROR: dict = {"error": "_msearch_failed"}

# Client pool
async def _get_client(
    name: str,
    verify: bool = True,
    max_keepalive: int = 20,
    max_connections: int = 100,
) -> httpx.AsyncClient:
    """Return a pooled httpx.AsyncClient by name"""
    if name not in _clients or _clients[name].is_closed:
        _clients[name] = httpx.AsyncClient(
            timeout=httpx.Timeout(HTTP_TIMEOUT),
            limits=httpx.Limits(max_keepalive_connections=max_keepalive, max_connections=max_connections),
            verify=verify,
            http2=_HTTP2,
        )
    return _clients[name]

# Circuit breaker (per pool fail fast)
class CircuitOpenError(httpx.ConnectError):
    """Raised by ``_api_call`` when the per-pool circuit breaker is open.
    Subclasses ``httpx.ConnectError`` so existing ``except httpx.ConnectError``
    handlers (Wazuh auth/indexer) already catch it as "upstream unreachable".
    """


class CircuitBreaker:
    """Fail-fast breaker keyed per HTTP client pool.
    Counts consecutive upstream failures (5xx / transport errors). After
    ``failure_threshold`` it opens and refuses new requests for ``recovery_timeout`` seconds, then allows a single half-open trial.
    A 429 (throttle) and any 4xx (client error) are no failures, prove the dependency responded, so they never count against the breaker. 
    A 4xx during a half-open trial closes the breaker.
    All state transitions are synchronous (no ``await``), so they are atomic
    within a single-threaded event loop, no lock required.
    """

    def __init__(self, failure_threshold: int = 5, recovery_timeout: float = 60.0, name: str = "http") -> None:
        self.name = name
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self._failures = 0
        self._opened_at = 0.0
        self._half_open = False

    @property
    def open(self) -> bool:
        return self._failures >= self.failure_threshold

    @property
    def failures(self) -> int:
        return self._failures

    def before_call(self) -> bool:
        """Return True if a request may proceed; False to fail fast."""
        if not self.open:
            return True
        if time.monotonic() - self._opened_at < self.recovery_timeout:
            return False
        if self._half_open:
            return False  # a trial is already.
        self._half_open = True  # allow exactly one trial
        return True

    def on_success(self) -> None:
        was_open = self.open
        self._failures = 0
        self._opened_at = 0.0
        self._half_open = False
        if was_open:
            logger.info("circuit breaker '%s' CLOSED", self.name)

    def on_failure(self) -> None:
        was_open = self.open
        self._failures += 1
        self._opened_at = time.monotonic()
        self._half_open = False
        if self.open and not was_open:
            logger.warning(
                "circuit breaker '%s' OPEN after %d consecutive failures",
                self.name, self._failures,
            )

    def on_throttled(self) -> None:
        """429 - upstream throttling, not an outage. Don't count; re-arm the trial."""
        self._half_open = False
        self._opened_at = time.monotonic()

    def on_liveness(self) -> None:
        """4xx - a completed HTTP response proves the dependency is reachable."""
        if self._half_open:
            self._failures = 0
            self._opened_at = 0.0
            self._half_open = False
            logger.info("circuit breaker '%s' CLOSED (liveness proven by 4xx)", self.name)


# Per-pool breakers, keyed by the same client_name as _clients.
_breakers: dict[str, CircuitBreaker] = {}


def _get_breaker(name: str) -> CircuitBreaker:
    if name not in _breakers:
        _breakers[name] = CircuitBreaker(name=name)
    return _breakers[name]


# Unified API call
async def _api_call(method: str, url: str, *, client_name: str = "http", verify: bool = True,
                    max_retries: int = 1, backoff: float = 0.2, **kw) -> httpx.Response:
    """Unified async HTTP helper. Returns raw response - caller calls .json() or .text.
    Retries (default once, configurable via max_retries) on 5xx server errors, network
    failures (jittered backoff), and 429 rate limits (honors Retry-After when present).
    A per-pool circuit breaker fails fast (CircuitOpenError) when an upstream is
    repeatedly down, so outages don't pile up retries/timeouts across all tools.
    """
    client = await _get_client(client_name, verify=verify)
    breaker = _get_breaker(client_name)
    last_exc: Exception | None = None
    for attempt in range(1 + max_retries):
        if not breaker.before_call():
            raise CircuitOpenError(
                f"circuit breaker open for '{client_name}' "
                f"({breaker.failures} consecutive failures) try again shortly"
            )
        try:
            resp = await getattr(client, method.lower())(url, **kw)
            resp.raise_for_status()
            breaker.on_success()
            return resp
        except httpx.HTTPStatusError as e:
            status = e.response.status_code
            if status == 429:
                breaker.on_throttled()
                if attempt < max_retries:
                    retry_after = e.response.headers.get("Retry-After")
                    try:
                        delay = min(float(retry_after), 30.0) if retry_after else backoff
                    except ValueError:
                        delay = backoff
                    await asyncio.sleep(delay)
                    last_exc = e
                    continue
                raise
            if 400 <= status < 500:
                breaker.on_liveness()
                raise
            # 5xx genuine upstream failure
            breaker.on_failure()
            if attempt < max_retries:
                await asyncio.sleep(backoff + random.uniform(0, 0.2))
                last_exc = e
                continue
            raise
        except (httpx.TimeoutException, httpx.ConnectError, httpx.RemoteProtocolError) as e:
            breaker.on_failure()
            if attempt < max_retries:
                await asyncio.sleep(backoff + random.uniform(0, 0.2))
                last_exc = e
                continue
            raise
    raise last_exc  # type: ignore[misc]


# Error handling
def _handle_api_error(e: Exception, context: str = "") -> str:
    """Consistent, actionable error formatting for all API-based tools."""
    prefix = f"[{context}] " if context else ""
    if isinstance(e, CircuitOpenError):
        return f"{prefix}Error: {e}"
    if isinstance(e, httpx.HTTPStatusError):
        status = e.response.status_code
        if status == 400:
            return f"{prefix}Error: Bad request (400) - the API rejected the parameters. Try a smaller limit."
        if status == 401:
            return f"{prefix}Error: Invalid or missing API key (401). Check your environment variables."
        if status == 404:
            return f"{prefix}Error: No data found for this target (404)."
        if status == 429:
            retry_after = e.response.headers.get("Retry-After")
            hint = f"Retry after {retry_after} seconds." if retry_after else ""
            return f"{prefix}Error: Rate limit reached (429).{hint}"
        return f"{prefix}Error: API request failed with status {status}."
    if isinstance(e, httpx.TimeoutException):
        return f"{prefix}Error: Request timed out after {HTTP_TIMEOUT}s. Try again."
    if isinstance(e, RuntimeError):
        return f"{prefix}Error: {e}"
    logger.exception("Unexpected error in %s", context)
    return f"{prefix}Error: Unexpected error ({type(e).__name__})."


# IP validation
def _is_private_or_reserved(ip: str) -> bool:
    """Check whether an IP belongs to a private or reserved range (not routable)."""
    try:
        return ipaddress.ip_address(ip).is_private
    except ValueError:
        return False


def _validate_public_ip(v: str) -> str:
    """Reject private/reserved IP for public threat-intel tools (SSRF guard/prevention)."""
    if _is_private_or_reserved(v):
        raise ValueError(
            f"'{v}' is a private/reserved IP address."
            "This tool only accepts public IPs for threat intelligence lookup."
        )
    return v


ValidPublicIp = Annotated[str, AfterValidator(_validate_public_ip)]
