#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Shared Pydantic validators and Annotated type aliases.
"""
from __future__ import annotations
import re
from typing import Optional, Annotated
from pydantic import AfterValidator
from mcp_server import _AGENT_NAME_DESC
from mcp_server import _SINCE_DESC
from mcp_server import _UNTIL_DESC
from mcp_server import _RESPONSE_FORMAT_DESC
from mcp_server import _BYPASS_REDACTION_DESC, _RESPONSE_FORMAT_DESC, _SINCE_DESC, _UNTIL_DESC, _AGENT_NAME_DESC

_AGENT_NAME_SAFE_RE = re.compile(r"^[a-zA-Z0-9_\-\.]+$")

# Practical email regex for extraction from log fields - covers >99% of real addresses
# Handles dots-in-local-part, plus-sign aliases, and multi-level TLDs
_EMAIL_RE = re.compile(
    r'[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?'
    r'(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}'
)

def _validate_keyword_field(v: Optional[str]) -> Optional[str]:
    """Shared keyword validator strip, reject null bytes / control chars."""
    if v is not None:
        v = v.strip()
        if not v:
            return None
        if len(v) > 1024:
            raise ValueError("keyword too long (max 1024)")
        if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", v):
            raise ValueError("keyword contains invalid control characters")
    return v

def _validate_agent_name_field(v: Optional[str]) -> Optional[str]:
    """Shared agent_name validator strip, length-check, safe-chars-only."""
    if v is not None:
        v = v.strip()
        if not v:
            return None
        if len(v) > 64:
            raise ValueError("agent_name too long (max 64)")
        if not _AGENT_NAME_SAFE_RE.match(v):
            raise ValueError("agent_name: use only letters, numbers, hyphen, underscore, dot")
    return v


def _validate_rule_groups_field(v: Optional[str]) -> Optional[str]:
    """Shared rule_groups validator - comma-split, strip, safe-chars-only."""
    if v is not None:
        v = v.strip()
        if not v:
            return None
        for g in v.split(","):
            g = g.strip()
            if not g:
                raise ValueError("Empty rule group name in comma-separated list")
            if not _AGENT_NAME_SAFE_RE.match(g):
                raise ValueError(f"Invalid rule group name: '{g}'")
    return v

# Annotated types for reusable field validation (replaces per-model validators)
ValidKeyword = Annotated[Optional[str], AfterValidator(_validate_keyword_field)]
ValidAgentName = Annotated[Optional[str], AfterValidator(_validate_agent_name_field)]
ValidRuleGroups = Annotated[Optional[str], AfterValidator(_validate_rule_groups_field)]


# Wazuh agent ID numeric 0-99999, zero-padded to 3 digits ('1' -> '001').
# Wazuh stores agent.id padded; an exact-match term on '1' silently returns nothing.
_AGENT_ID_RE = re.compile(r"^\d{1,5}$")


def _validate_agent_id_field(v: Optional[str]) -> Optional[str]:
    """Normalize a Wazuh agent ID: strip, validate numeric 0-99999, zfill(3)."""
    if v is None:
        return None
    v = v.strip()
    if not v:
        return None
    if not _AGENT_ID_RE.match(v):
        raise ValueError(f"agent_id must be numeric (0-99999), got '{v}'")
    return v.zfill(3)


# Timestamp ISO 8601, relative duration ('24h'), or OpenSearch date math ('now-24h').
_ISO_TS_RE = re.compile(r"^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:?\d{2})?)?$")
_RELATIVE_TS_RE = re.compile(r"^\d+[smhdw]$")
_NOW_MATH_RE = re.compile(r"^now([+-]\d+[smhdw])*(/\w+)?$", re.IGNORECASE)


def _validate_timestamp_field(v: Optional[str]) -> Optional[str]:
    """Validate a timestamp: ISO 8601, relative ('24h'), or date math ('now-24h').
    Normalizes a leading 'NOW'/'now' to lowercase (the parser requires it).
    """
    if v is None:
        return None
    v = v.strip()
    if not v:
        return None
    if v.lower().startswith("now"):
        normalized = "now" + v[3:]
        if not _NOW_MATH_RE.match(normalized):
            raise ValueError(f"invalid date math '{v}' (e.g. now-24h, now-7d/d)")
        return normalized
    if _ISO_TS_RE.match(v) or _RELATIVE_TS_RE.match(v):
        return v
    raise ValueError(
        f"invalid timestamp '{v}' — use ISO 8601, relative ('24h'), or date math ('now-24h')"
    )


ValidAgentId = Annotated[Optional[str], AfterValidator(_validate_agent_id_field)]
ValidTimestamp = Annotated[Optional[str], AfterValidator(_validate_timestamp_field)]
