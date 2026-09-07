#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Typed exception hierarchy for Blue Team MCP Server.

All shared utilities raise these; tools catch them at the MCP boundary 
and format a clean error response for the LLM. No shared function ever returns a bare {"error": "..."} dict.
"""
from __future__ import annotations


class BlueTeamMCPError(Exception):
    """Base exception for all Blue Team MCP Server errors."""


class ConfigurationError(BlueTeamMCPError):
    """Raised at startup when required configuration is missing or invalid.

    These are fatal - the server must not start with broken config.
    """


class WazuhAuthError(BlueTeamMCPError):
    """Raised when JWT authentication with the Wazuh Manager API fails.

    Carries the original httpx exception as __cause__ for debugging.
    """


class WazuhAPIError(BlueTeamMCPError):
    """Raised when the Wazuh Manager or Indexer API returns a non-2xx response.

    Attributes:
        status_code: HTTP status code from the upstream response.
        response_body: Truncated response body text (max 500 chars).
    """

    def __init__(self, message: str, status_code: int = 0, response_body: str = "") -> None:
        super().__init__(message)
        self.status_code = status_code
        self.response_body = response_body


class ThreatIntelError(BlueTeamMCPError):
    """Raised when an external threat-intelligence API call fails.
    Covers CrowdSec, GreyNoise, ThreatFox, AbuseIPDB, VirusTotal,
    Netra, and Argus.  Carries the original exception as __cause__.
    """
