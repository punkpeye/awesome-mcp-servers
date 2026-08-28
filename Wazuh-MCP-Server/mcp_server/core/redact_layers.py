#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
PII redaction pipeline 6 layers. Layer 1 (credentials) Never bypassable.

Three redaction policies (BLUETEAM_REDACTION_POLICY env / per-call param):
  - "full" (default):   shape-based masking - emails, private IPs, ALL domains,
                        paths, UAs. Registered attacker IOCs are exempt.
  - "protect_victim":   mask ONLY victim-owned indicators - emails/domains at
                        owned domains (BLUETEAM_OWNED_DOMAINS), private IPs,
                        paths, identity fields, agent names. Attacker domains,
                        attacker emails and payload contents stay intact.
  - "raw":              Layer 1 credential strip ONLY. Hard-gated behind
                        BLUETEAM_ALLOW_FORENSIC_BYPASS (default false).
"""
from __future__ import annotations
import hashlib, re
from typing import Any

# Lazy imports from redact.py to avoid circular import.
# Each layer function imports only what it needs at call time.


def _apply_email_layer(data: str, pol: str, reveal: bool) -> str:
    from mcp_server.core.redact import _should_mask_email, _hash_email_for_audit, _REDACT_EMAIL_RE
    def _redact_email(m: re.Match) -> str:
        local, domain = m.group(1), m.group(2)
        full_email = f"{local}@{domain}"
        if not _should_mask_email(full_email, pol, reveal):
            return m.group(0)
        forensic_hash = _hash_email_for_audit(full_email)
        if len(local) <= 2:
            rlocal = local[0] + "*" * (len(local) - 1)
        else:
            rlocal = local[0] + "*" * max(1, len(local) - 2) + local[-1]
        return f"{rlocal}@{domain} [h:{forensic_hash}]"
    return _REDACT_EMAIL_RE.sub(_redact_email, data)


def _apply_ip_layer(data: str, pol: str, _reveal: bool) -> str:
    from mcp_server.core.redact import _should_mask_ip
    def _redact_internal_ip(m: re.Match) -> str:
        ip = m.group(0)
        if not _should_mask_ip(ip, pol):
            return ip
        octets = ip.split(".")
        if octets[0] == "10":
            return f"10.{'***'}.{'***'}.{octets[3]}"
        elif octets[0] == "172" and 16 <= int(octets[1]) <= 31:
            return f"172.{octets[1]}.{'***'}.{octets[3]}"
        elif octets[0] == "192" and octets[1] == "168":
            return f"192.168.{'***'}.{octets[3]}"
        elif octets[0] == "127":
            return f"127.{'***'}.{'***'}.{octets[3]}"
        elif octets[0] == "169" and octets[1] == "254":
            return f"169.254.{'***'}.{octets[3]}"
        return ip
    data = re.sub(
        r"\b(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|"
        r"172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3}|"
        r"192\.168\.\d{1,3}\.\d{1,3}|"
        r"127\.\d{1,3}\.\d{1,3}\.\d{1,3}|"
        r"169\.254\.\d{1,3}\.\d{1,3})\b",
        _redact_internal_ip, data,
    )
    return re.sub(r"\b::1\b", "<LOOPBACK_REDACTED>", data)


def _apply_domain_layer(data: str, pol: str, reveal: bool) -> str:
    from mcp_server.core.redact import _should_mask_domain, _mask_domain
    return re.sub(
        r"(?<![@\w])([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?"
        r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*"
        r"\.(?:[a-zA-Z]{2,}|xn--[a-zA-Z0-9]+))\b",
        lambda m: _mask_domain(m.group(1)) if _should_mask_domain(m.group(1), pol, reveal)
        else m.group(0),
        data,
    )


def _apply_location_layer(data: str, _pol: str, _reveal: bool) -> str:
    from mcp_server.core.redact import _REDACT_SALT
    def _redact_log_path(m: re.Match) -> str:
        path = m.group(0)
        parts = path.rstrip("/").split("/")
        leaf = parts[-1] if len(parts) > 1 else path
        path_hash = hashlib.sha256(f"{_REDACT_SALT}:{path}".encode()).hexdigest()[:6]
        return f".../{leaf} [h:{path_hash}]"
    return re.sub(r"/(?:[a-zA-Z0-9._-]+/){2,}[a-zA-Z0-9._-]+", _redact_log_path, data)


def _apply_ua_layer(data: str, _pol: str, _reveal: bool) -> str:
    if len(data) > 80 and re.search(r"Mozilla|Chrome|Safari|Firefox|curl|wget|python", data):
        return data[:80] + "..."
    return data

