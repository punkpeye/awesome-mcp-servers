#!/usr/bin/env python3
"""
Tests for mcp_server/core/http_client.py - retry logic, client pool, error handling.
"""
from __future__ import annotations
import asyncio
import pytest
import httpx
from unittest.mock import AsyncMock, MagicMock, patch
from mcp_server.core.http_client import (
    _get_client,
    _api_call,
    _handle_api_error,
    _is_private_or_reserved,
    _validate_public_ip,
    ValidPublicIp,
)


class TestClientPool:
    """Tests for _get_client - pooled httpx.AsyncClient management."""

    @pytest.mark.asyncio
    async def test_creates_client_lazily(self):
        """_get_client creates a new client on first call."""
        client = await _get_client("test-pool", verify=True)
        assert isinstance(client, httpx.AsyncClient)
        assert not client.is_closed

    @pytest.mark.asyncio
    async def test_reuses_client_same_name(self):
        """Same pool name returns the same client instance."""
        c1 = await _get_client("reuse-test", verify=True)
        c2 = await _get_client("reuse-test", verify=True)
        assert c1 is c2

    @pytest.mark.asyncio
    async def test_different_names_different_clients(self):
        """Different pool names create different clients."""
        c1 = await _get_client("pool-a", verify=True)
        c2 = await _get_client("pool-b", verify=False)
        assert c1 is not c2

    @pytest.mark.asyncio
    async def test_recreates_closed_client(self):
        """If client.is_closed, a new one is created."""
        c1 = await _get_client("recreate-test", verify=True)
        await c1.aclose()  # is_closed is a read-only property - close for real
        c2 = await _get_client("recreate-test", verify=True)
        assert c1 is not c2


class TestRetryLogic:
    """Tests for _api_call - retry on 5xx, 429, and network errors."""
    @pytest.mark.asyncio
    async def test_success_first_attempt(self, mock_response):
        """Returns response on first successful attempt."""
        resp = mock_response(status_code=200, json_data={"ok": True})
        with patch.object(httpx.AsyncClient, "get", AsyncMock(return_value=resp)):
            result = await _api_call("get", "http://test/api", client_name="retry-ok")
            assert result.json() == {"ok": True}

    @pytest.mark.asyncio
    async def test_retries_on_5xx(self, mock_response):
        """Retries once on 5xx, succeeds on second attempt."""
        fail = mock_response(status_code=503)
        ok = mock_response(status_code=200, json_data={"recovered": True})
        mock_get = AsyncMock(side_effect=[fail, ok])
        with patch.object(httpx.AsyncClient, "get", mock_get):
            # Override raise_for_status on the fail response to actually raise
            fail.raise_for_status.side_effect = httpx.HTTPStatusError(
                "503", request=MagicMock(), response=fail
            )
            with patch("asyncio.sleep", AsyncMock()):
                result = await _api_call("get", "http://test/api", client_name="retry-5xx")
                assert result.json() == {"recovered": True}
                assert mock_get.call_count == 2

    @pytest.mark.asyncio
    async def test_raises_after_two_5xx(self, mock_response):
        """Raises after two consecutive 5xx responses."""
        fail1 = mock_response(status_code=503)
        fail2 = mock_response(status_code=503)
        fail1.raise_for_status.side_effect = httpx.HTTPStatusError(
            "503a", request=MagicMock(), response=fail1
        )
        fail2.raise_for_status.side_effect = httpx.HTTPStatusError(
            "503b", request=MagicMock(), response=fail2
        )
        mock_get = AsyncMock(side_effect=[fail1, fail2])
        with patch.object(httpx.AsyncClient, "get", mock_get):
            with patch("asyncio.sleep", AsyncMock()):
                with pytest.raises(httpx.HTTPStatusError):
                    await _api_call("get", "http://test/api", client_name="retry-fail")

    @pytest.mark.asyncio
    async def test_retries_on_429_with_retry_after(self, mock_response):
        """Honors Retry-After header on 429, retries once."""
        fail = mock_response(
            status_code=429,
            headers=httpx.Headers({"Retry-After": "2"}),
        )
        ok = mock_response(status_code=200, json_data={"throttled": False})
        fail.raise_for_status.side_effect = httpx.HTTPStatusError(
            "429", request=MagicMock(), response=fail
        )
        mock_get = AsyncMock(side_effect=[fail, ok])
        sleep_mock = AsyncMock()
        with patch.object(httpx.AsyncClient, "get", mock_get):
            with patch("asyncio.sleep", sleep_mock):
                result = await _api_call("get", "http://test/api", client_name="retry-429")
                sleep_mock.assert_called_once_with(2.0)
                assert result.json() == {"throttled": False}

    @pytest.mark.asyncio
    async def test_429_caps_retry_after_at_30s(self, mock_response):
        """Retry-After values > 30s are capped at 30s."""
        fail = mock_response(
            status_code=429,
            headers=httpx.Headers({"Retry-After": "999"}),
        )
        fail.raise_for_status.side_effect = httpx.HTTPStatusError(
            "429", request=MagicMock(), response=fail
        )
        ok = mock_response(status_code=200, json_data={"ok": True})
        mock_get = AsyncMock(side_effect=[fail, ok])
        sleep_mock = AsyncMock()
        with patch.object(httpx.AsyncClient, "get", mock_get):
            with patch("asyncio.sleep", sleep_mock):
                await _api_call("get", "http://test/api", client_name="retry-429-cap")
                sleep_mock.assert_called_once_with(30.0)

    @pytest.mark.asyncio
    async def test_retries_on_timeout(self):
        """Retries once on TimeoutException."""
        ok_resp = MagicMock(spec=httpx.Response)
        ok_resp.status_code = 200
        ok_resp.json.return_value = {"ok": True}
        ok_resp.raise_for_status = MagicMock()
        mock_get = AsyncMock(side_effect=[httpx.TimeoutException("timeout"), ok_resp])
        with patch.object(httpx.AsyncClient, "get", mock_get):
            with patch("asyncio.sleep", AsyncMock()):
                result = await _api_call("get", "http://test/api", client_name="retry-timeout")
                assert result.json() == {"ok": True}

    @pytest.mark.asyncio
    async def test_no_retry_on_4xx_except_429(self, mock_response):
        """Does NOT retry on 4xx errors other than 429."""
        fail = mock_response(status_code=400)
        fail.raise_for_status.side_effect = httpx.HTTPStatusError(
            "400", request=MagicMock(), response=fail
        )
        mock_get = AsyncMock(side_effect=[fail])
        with patch.object(httpx.AsyncClient, "get", mock_get):
            with pytest.raises(httpx.HTTPStatusError):
                await _api_call("get", "http://test/api", client_name="retry-4xx")
            assert mock_get.call_count == 1  # no retry

    @pytest.mark.asyncio
    async def test_configurable_max_retries(self, mock_response):
        """max_retries=2 -> up to 3 attempts before giving up. LoL"""
        fail1 = mock_response(status_code=503)
        fail2 = mock_response(status_code=503)
        ok = mock_response(status_code=200, json_data={"ok": True})
        for f in (fail1, fail2):
            f.raise_for_status.side_effect = httpx.HTTPStatusError("503", request=MagicMock(), response=f)
        mock_get = AsyncMock(side_effect=[fail1, fail2, ok])
        with patch.object(httpx.AsyncClient, "get", mock_get):
            with patch("asyncio.sleep", AsyncMock()):
                result = await _api_call("get", "http://test/api", client_name="retry-max", max_retries=2)
                assert result.json() == {"ok": True}
                assert mock_get.call_count == 3


class TestErrorHandling:
    """Tests for _handle_api_error - human-readable error formatting."""
    def test_400_bad_request(self):
        resp = MagicMock(spec=httpx.Response)
        resp.status_code = 400
        exc = httpx.HTTPStatusError("bad", request=MagicMock(), response=resp)
        msg = _handle_api_error(exc)
        assert "400" in msg
        assert "parameters" in msg.lower()

    def test_401_unauthorized(self):
        resp = MagicMock(spec=httpx.Response)
        resp.status_code = 401
        exc = httpx.HTTPStatusError("unauth", request=MagicMock(), response=resp)
        msg = _handle_api_error(exc)
        assert "401" in msg
        assert "api key" in msg.lower()

    def test_404_not_found(self):
        resp = MagicMock(spec=httpx.Response)
        resp.status_code = 404
        exc = httpx.HTTPStatusError("nf", request=MagicMock(), response=resp)
        msg = _handle_api_error(exc)
        assert "404" in msg

    def test_timeout(self):
        exc = httpx.TimeoutException("timed out")
        msg = _handle_api_error(exc)
        assert "timed out" in msg.lower()

    def test_runtime_error(self):
        exc = RuntimeError("custom error")
        msg = _handle_api_error(exc)
        assert "custom error" in msg

    def test_context_prefix(self):
        exc = RuntimeError("something")
        msg = _handle_api_error(exc, context="crowdsec")
        assert msg.startswith("[crowdsec]")


class TestIPValidation:
    """Tests for SSRF guard - _is_private_or_reserved, _validate_public_ip."""
    def test_private_ipv4_detected(self):
        assert _is_private_or_reserved("192.168.1.1") is True
        assert _is_private_or_reserved("10.0.0.1") is True
        assert _is_private_or_reserved("172.16.0.1") is True
        assert _is_private_or_reserved("127.0.0.1") is True

    def test_public_ipv4_passes(self):
        assert _is_private_or_reserved("8.8.8.8") is False
        assert _is_private_or_reserved("1.1.1.1") is False

    def test_invalid_ip_returns_false(self):
        """Invalid IP strings are not private - they fail format validation elsewhere."""
        assert _is_private_or_reserved("not-an-ip") is False

    def test_validate_public_ip_accepts_public(self):
        assert _validate_public_ip("8.8.8.8") == "8.8.8.8"

    def test_validate_public_ip_rejects_private(self):
        with pytest.raises(ValueError, match="private/reserved"):
            _validate_public_ip("192.168.1.1")

    def test_valid_public_ip_type(self):
        """ValidPublicIp annotated type works with Pydantic."""
        from pydantic import BaseModel

        class TestModel(BaseModel):
            ip: ValidPublicIp

        m = TestModel(ip="8.8.8.8")
        assert m.ip == "8.8.8.8"

        with pytest.raises(ValueError):
            TestModel(ip="10.0.0.1")
