#!/usr/bin/env python3
"""
Tests for mcp_server/core/redact.py - 6-layer PII redaction pipeline.
IMPORTANT: Module-level constants are read at import time from os.environ.
Set env vars BEFORE importing.  Some tests monkey-patch module attrs for
raw/forensic policy tests that need runtime toggles.
"""
from __future__ import annotations

import os

os.environ.setdefault("WAZUH_INDEXER_URL", "https://idx:9200")
os.environ.setdefault("WAZUH_INDEXER_PASSWORD", "pw")
os.environ.setdefault("BLUETEAM_REDACTION_POLICY", "full")
os.environ.setdefault("BLUETEAM_OWNED_DOMAINS", "")
os.environ.setdefault("BLUETEAM_ALLOW_FORENSIC_BYPASS", "false")
os.environ.setdefault("BLUETEAM_FORENSIC_TOKEN", "")

import pytest
from unittest.mock import patch

import mcp_server.core.redact as _redact_mod
from mcp_server.core.redact import (
    _redact_alert_data,
    _strip_credentials,
    _is_owned_domain,
    _resolve_policy,
    _is_hostname_candidate,
    _mask_domain,
)


class TestCredentialStripping:

    def test_strips_bearer_in_log_text(self):
        """Bearer token in full log-line format is stripped."""
        result = _strip_credentials("Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.abc.def")
        assert "REDACTED" in result
        assert "eyJhbGci" not in result

    def test_strips_api_key_in_log_text(self):
        result = _strip_credentials("x-api-key: sk-abc123def456")
        assert "API_KEY_REDACTED" in result

    def test_strips_jwt_token(self):
        result = _strip_credentials("token=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.xxx")
        assert "JWT_REDACTED" in result

    def test_strips_password_param(self):
        result = _strip_credentials("password=supersecret123")
        assert "PASSWORD_REDACTED" in result
        assert "supersecret123" not in result

    def test_preserves_non_credential_text(self):
        text = "srcip=8.8.8.8 user=admin action=login"
        result = _strip_credentials(text)
        assert "8.8.8.8" in result
        assert "admin" in result

    def test_recursive_list_strip(self):
        data = ["safe", "Authorization: Bearer xyz", {"key": "password=secret"}]
        result = _strip_credentials(data)
        assert result[0] == "safe"
        assert "REDACTED" in result[1]
        assert "PASSWORD_REDACTED" in result[2]["key"]


class TestEmailRedaction:

    def test_full_policy_masks_emails(self):
        data = "Contact admin@example.com"
        result = _redact_alert_data(data, policy="full")
        assert "admin@example.com" not in result


class TestIPMasking:

    def test_masks_rfc1918_ips(self):
        data = "srcip=192.168.1.100 dstip=10.0.0.5"
        result = _redact_alert_data(data, policy="full")
        assert "192.168.1.100" not in result
        assert "10.0.0.5" not in result

    def test_preserves_public_ips(self):
        data = "srcip=8.8.8.8 dstip=1.1.1.1"
        result = _redact_alert_data(data, policy="full")
        assert "8.8.8.8" in result
        assert "1.1.1.1" in result

    def test_masks_loopback(self):
        data = "error from 127.0.0.1: connection refused"
        result = _redact_alert_data(data, policy="full")
        assert "127.0.0.1" not in result

    def test_public_ips_always_preserved(self):
        data = "attacker_ip=45.33.32.156"
        result = _redact_alert_data(data, policy="full")
        assert "45.33.32.156" in result


class TestDomainMasking:

    def test_masks_third_level_subdomain(self):
        """_mask_domain masks subdomains of 3+ parts (e.g. admin.example.com)."""
        assert _mask_domain("admin.example.com") != "admin.example.com"
        assert "example.com" in _mask_domain("admin.example.com")  # TLD visible

    def test_preserves_two_part_domain(self):
        """2-part domains (evil.cn) are NOT masked — only subdomains are."""
        assert _mask_domain("evil.cn") == "evil.cn"

    def test_full_policy_masks_subdomain_in_text(self):
        data = "curl http://admin.internal.corp/shell.sh"
        result = _redact_alert_data(data, policy="full")
        # admin.internal.corp is 3-part -> should be masked
        assert "admin.internal.corp" not in result


class TestPolicyResolution:

    def test_defaults_to_env(self):
        assert _resolve_policy(False, None, None) == "full"

    def test_bypass_flag_overrides(self):
        assert _resolve_policy(True, None, None) == "raw"

    def test_explicit_policy_wins(self):
        assert _resolve_policy(False, None, "protect_victim") == "protect_victim"

    def test_invalid_policy_raises(self):
        with pytest.raises(ValueError, match="must be one of"):
            _resolve_policy(False, None, "bogus")


class TestHostnameCandidate:

    def test_rejects_alpha_only(self):
        assert _is_hostname_candidate("web") is False

    def test_accepts_with_digit(self):
        assert _is_hostname_candidate("db1") is True

    def test_accepts_with_hyphen(self):
        assert _is_hostname_candidate("web-01") is True


class TestRawPolicyGate:

    def test_raw_policy_strips_credentials(self):
        """Raw policy strips credentials, preserves everything else."""
        with patch.object(_redact_mod, "BLUETEAM_ALLOW_FORENSIC_BYPASS", True):
            data = "Authorization: Bearer abc123 user=admin ip=192.168.1.1"
            result = _redact_alert_data(data, policy="raw")
            assert "REDACTED" in result
            assert "admin" in result
            assert "192.168.1.1" in result

    def test_raw_rejected_when_disabled(self):
        with patch.object(_redact_mod, "BLUETEAM_ALLOW_FORENSIC_BYPASS", False):
            with pytest.raises(ValueError, match="BLUETEAM_ALLOW_FORENSIC_BYPASS"):
                _redact_alert_data("test", policy="raw")


class TestOwnedDomainDetection:

    def test_exact_match(self):
        with patch.object(_redact_mod, "_OWNED_DOMAINS", {"tangerangkota.go.id"}):
            assert _is_owned_domain("tangerangkota.go.id") is True

    def test_subdomain_match(self):
        with patch.object(_redact_mod, "_OWNED_DOMAINS", {"tangerangkota.go.id"}):
            assert _is_owned_domain("mail.tangerangkota.go.id") is True

    def test_unrelated_not_owned(self):
        with patch.object(_redact_mod, "_OWNED_DOMAINS", {"tangerangkota.go.id"}):
            assert _is_owned_domain("evil.cn") is False
