#!/usr/bin/env python3
"""
Shared pytest fixtures for Wazuh-MCP-Server tests.
Provides mock httpx clients, config objects, and async event loop support
following the REF repository's conftest.py pattern.
"""
from __future__ import annotations

import os
import pytest
import httpx
from unittest.mock import AsyncMock, MagicMock


@pytest.fixture(autouse=True)
def _clean_env():
    """Reset env vars before each test to prevent cross-test leakage."""
    saved = dict(os.environ)
    yield
    os.environ.clear()
    os.environ.update(saved)


@pytest.fixture
def minimal_env():
    """Minimal environment for tests that need Wazuh config."""
    os.environ.setdefault("WAZUH_INDEXER_URL", "https://indexer:9200")
    os.environ.setdefault("WAZUH_INDEXER_PASSWORD", "test-indexer-pass")
    os.environ.setdefault("WAZUH_API_URL", "https://manager:55000")
    os.environ.setdefault("WAZUH_API_PASSWORD", "test-manager-pass")
    os.environ.setdefault("BLUETEAM_REDACTION_POLICY", "full")


@pytest.fixture
def mock_httpx_client():
    """Return an AsyncMock that mimics httpx.AsyncClient.
    Use this to intercept API calls without network access.
    """
    client = AsyncMock(spec=httpx.AsyncClient)
    client.is_closed = False
    return client


@pytest.fixture
def mock_response():
    """Factory for creating mock httpx.Response objects."""

    def _make(status_code=200, json_data=None, text="", headers=None):
        resp = MagicMock(spec=httpx.Response)
        resp.status_code = status_code
        resp.json.return_value = json_data or {}
        resp.text = text
        resp.headers = headers or httpx.Headers({})
        resp.raise_for_status = MagicMock()
        if status_code >= 400:
            resp.raise_for_status.side_effect = httpx.HTTPStatusError(
                "error", request=MagicMock(), response=resp
            )
        return resp

    return _make


@pytest.fixture
def config_singleton():
    """Return a validated Config singleton for tests.
    Requires minimal_env fixture values to be set.
    """
    from mcp_server.core.config import Config

    return Config.from_env()
