#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Wazuh Manager JWT authentication + API GET helper.

Refactored (Phase 1): instance-scoped JWT manager with 60s expiry buffer,
typed exception propagation (WazuhAuthError, WazuhAPIError) replacing the
legacy {"error": "..."} dict-return pattern.

Callers (tool modules) are expected to catch WazuhAuthError / WazuhAPIError
at the MCP boundary and format a clean error response for the LLM.
"""
from __future__ import annotations

import time
import logging
from typing import Optional, Dict

import httpx

from mcp_server.core.exceptions import WazuhAuthError, WazuhAPIError, ConfigurationError

logger = logging.getLogger("blue_team_mcp.wazuh")

# Late import - _api_call lives in http_client.py which imports from
# mcp_server.__init__; resolving it here at call time avoids the circular
# import that would occur if we imported at module level.
_api_call = None  # type: ignore[assignment]

def _resolve_api_call():
    global _api_call
    if _api_call is None:
        from mcp_server.core.http_client import _api_call as _fn
        _api_call = _fn


# WazuhAuthManager - instance-scoped JWT lifecycle
class WazuhAuthManager:
    """Manages JWT authentication for a single Wazuh Manager instance.
    Token is cached in-memory and refreshed proactively when within 60 seconds
    of expiry, preventing mid-request token expiration under concurrent tool
    calls.  Wazuh's default JWT validity is 900 seconds.

    All authentication failures raise :exc:`WazuhAuthError`.
    """

    _TOKEN_TTL = 900          # Wazuh Manager default JWT validity (seconds)
    _REFRESH_BUFFER = 60      # Refresh when fewer than this many seconds remain

    def __init__(
        self,
        url: str,
        username: str,
        password: str,
        verify_ssl: bool = True,
    ) -> None:
        if not url:
            raise ConfigurationError("Wazuh Manager URL is required for WazuhAuthManager")
        self._url = url.rstrip("/")
        self._username = username
        self._password = password
        self._verify_ssl = verify_ssl
        self._token: Optional[str] = None
        self._expiry: float = 0.0

    # Public API
    async def get_token(self) -> str:
        """Return a valid JWT, refreshing if expired or near expiry.
        Raises:
            WazuhAuthError: If authentication fails.
        """
        now = time.monotonic()
        if self._token is not None and (self._expiry - now) > self._REFRESH_BUFFER:
            return self._token
        return await self._refresh()

    async def api_get(self, path: str, params: Optional[Dict[str, str]] = None) -> Dict:
        """Perform an authenticated GET request to the Wazuh Manager API.

        Args:
            path: API path starting with ``/`` (e.g. ``/agents``).
            params: Optional query-string parameters.

        Returns:
            Parsed JSON response body as a dict.

        Raises:
            WazuhAuthError: If JWT authentication fails.
            WazuhAPIError: If the Manager API returns a non-2xx status.
        """
        token = await self.get_token()
        url = f"{self._url}{path}"
        try:
            _resolve_api_call()
            resp = await _api_call(  # type: ignore[misc]
                "get", url,
                client_name="wazuh",
                verify=self._verify_ssl,
                headers={"Authorization": f"Bearer {token}"},
                params=params or {},
            )
            return resp.json()
        except httpx.HTTPStatusError as e:
            raise WazuhAPIError(
                f"Wazuh Manager API returned HTTP {e.response.status_code} for {path}",
                status_code=e.response.status_code,
                response_body=e.response.text[:500],
            ) from e
        except (httpx.TimeoutException, httpx.ConnectError, httpx.RemoteProtocolError) as e:
            raise WazuhAPIError(
                f"Wazuh Manager API unreachable at {self._url}: {e}",
            ) from e
        except WazuhAPIError:  # re-raise our own
            raise

    # Internal
    async def _refresh(self) -> str:
        """Obtain a fresh JWT from the Manager's security endpoint."""
        url = f"{self._url}/security/user/authenticate?raw=true"
        try:
            _resolve_api_call()
            resp = await _api_call(  # type: ignore[misc]
                "post", url,
                client_name="wazuh",
                verify=self._verify_ssl,
                auth=(self._username, self._password),
            )
        except httpx.HTTPStatusError as e:
            self._invalidate()
            raise WazuhAuthError(
                f"Wazuh authentication rejected (HTTP {e.response.status_code}). "
                f"Check WAZUH_API_USER / WAZUH_API_PASSWORD."
            ) from e
        except (httpx.TimeoutException, httpx.ConnectError, httpx.RemoteProtocolError) as e:
            self._invalidate()
            raise WazuhAuthError(
                f"Wazuh Manager unreachable during authentication at {self._url}: {e}"
            ) from e

        raw_token = resp.text.strip().strip('"')
        if not raw_token:
            self._invalidate()
            raise WazuhAuthError("Wazuh Manager returned an empty JWT token.")

        self._token = raw_token
        self._expiry = time.monotonic() + self._TOKEN_TTL
        logger.debug("JWT refreshed — expires in %ds (buffer: %ds).",
                      self._TOKEN_TTL, self._REFRESH_BUFFER)
        return self._token

    def _invalidate(self) -> None:
        """Clear cached credentials after a failure."""
        self._token = None
        self._expiry = 0.0


# Module-level singleton and init
_auth_manager: Optional[WazuhAuthManager] = None
def init_auth_manager(
    url: str,
    username: str,
    password: str,
    verify_ssl: bool = True,
) -> WazuhAuthManager:
    """Initialize the module-level WazuhAuthManager singleton.
    Called once at server startup from ``main()`` after config is validated.
    If Manager credentials are not configured (no URL or no password), the
    singleton remains ``None`` and all module-level functions raise
    ``ConfigurationError`` when called.
    """
    global _auth_manager
    if url and password:
        _auth_manager = WazuhAuthManager(
            url=url, username=username, password=password, verify_ssl=verify_ssl,
        )
        logger.info("WazuhAuthManager initialized for %s as '%s'.", url, username)
    else:
        _auth_manager = None
        logger.info("WazuhAuthManager NOT initialized — Manager tools will be unavailable.")
    return _auth_manager

# Module level helpers - thin wrappers for backward compatibility with tools
async def _wazuh_get_token() -> str:
    """Obtain a valid JWT from the singleton auth manager.

    Raises:
        ConfigurationError: If ``init_auth_manager`` was never called.
        WazuhAuthError: If authentication fails.
    """
    if _auth_manager is None:
        raise ConfigurationError(
            "WazuhAuthManager not initialized. "
            "Ensure WAZUH_API_URL and WAZUH_API_PASSWORD are set and init_auth_manager() "
            "was called at startup."
        )
    return await _auth_manager.get_token()


async def _wazuh_api_get(path: str, params: Optional[Dict[str, str]] = None) -> Dict:
    """Call the Wazuh Manager API GET endpoint.

    Args:
        path: API path starting with ``/``.
        params: Optional query-string parameters.

    Returns:
        Parsed JSON response body.

    Raises:
        ConfigurationError: If auth manager was not initialized.
        WazuhAuthError: If JWT authentication fails.
        WazuhAPIError: If the Manager returns a non-2xx response.
    """
    if _auth_manager is None:
        raise ConfigurationError(
            "WazuhAuthManager not initialized — cannot call Manager API. "
            "Set WAZUH_API_URL and WAZUH_API_PASSWORD."
        )
    return await _auth_manager.api_get(path, params)
