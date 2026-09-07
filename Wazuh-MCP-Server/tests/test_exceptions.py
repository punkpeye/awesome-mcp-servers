#!/usr/bin/env python3
"""
Tests for mcp_server/core/exceptions.py - exception hierarchy.
"""
from __future__ import annotations
import pytest
from mcp_server.core.exceptions import (
    BlueTeamMCPError,
    ConfigurationError,
    WazuhAuthError,
    WazuhAPIError,
    ThreatIntelError,
)

class TestExceptionHierarchy:
    """Verify the exception class tree and attribute contracts."""
    def test_all_inherit_from_base(self):
        """Every exception is a BlueTeamMCPError."""
        assert issubclass(ConfigurationError, BlueTeamMCPError)
        assert issubclass(WazuhAuthError, BlueTeamMCPError)
        assert issubclass(WazuhAPIError, BlueTeamMCPError)
        assert issubclass(ThreatIntelError, BlueTeamMCPError)

    def test_catch_base_catches_all(self):
        """BlueTeamMCPError catches all subclasses."""
        for exc_cls in [ConfigurationError, WazuhAuthError, WazuhAPIError, ThreatIntelError]:
            try:
                raise exc_cls("test")
            except BlueTeamMCPError:
                pass  # expected
            else:
                pytest.fail(f"{exc_cls.__name__} not caught by BlueTeamMCPError")

    def test_wazuh_api_error_carries_attributes(self):
        """WazuhAPIError stores status_code and response_body."""
        e = WazuhAPIError("gateway timeout", status_code=504, response_body="<html>...</html>")
        assert e.status_code == 504
        assert e.response_body == "<html>...</html>"
        assert "gateway timeout" in str(e)

    def test_wazuh_api_error_defaults(self):
        """WazuhAPIError defaults status_code=0, response_body=''."""
        e = WazuhAPIError("generic")
        assert e.status_code == 0
        assert e.response_body == ""

    def test_configuration_error_is_catchable_by_base(self):
        """ConfigurationError raised at startup is catchable."""
        with pytest.raises(BlueTeamMCPError):
            raise ConfigurationError("invalid config")

    def test_threat_intel_error_chains_cause(self):
        """ThreatIntelError carries the original exception as __cause__."""
        original = RuntimeError("connection refused")
        try:
            raise ThreatIntelError("CrowdSec lookup failed") from original
        except ThreatIntelError as e:
            assert e.__cause__ is original
