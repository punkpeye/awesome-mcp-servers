#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Fail2Ban tools - jail status, banned IP, unban.
"""
from __future__ import annotations
import json, shutil, ipaddress
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, field_validator
from mcp_server import mcp
from mcp_server.core.audit import _audit_log, _truncate_if_needed, _check_rate_limit
from mcp_server.core.redact import _redact_alert_data
from mcp_server.core.subprocess import _run, _tool_not_found


class BypassRedactionInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    bypass_redaction: bool = Field(default=False, description="When true, skip PII/credential redaction for audit investigations")


@mcp.tool(
    name="blueteam_fail2ban_status",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True},
)
async def blueteam_fail2ban_status(params: BypassRedactionInput) -> str:
    """List all active fail2ban jails and their ban counts.

    Args:
        params.bypass_redaction: When true, skip PII/credential redaction

    Returns:
        str: Jail list with banned IP counts
    """
    _audit_log("blueteam_fail2ban_status", {})
    if not shutil.which("fail2ban-client"):
        return _tool_not_found("fail2ban")
    r = _run(["fail2ban-client", "status"])
    return _redact_alert_data(r["stdout"] or r["stderr"], bypass=params.bypass_redaction)


class JailInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    jail: str = Field(..., description="Jail name, e.g. 'sshd', 'nginx-http-auth'")
    bypass_redaction: bool = Field(default=False, description="When true, skip PII/credential redaction for audit investigations")


@mcp.tool(
    name="blueteam_fail2ban_jail_status",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def blueteam_fail2ban_jail_status(params: JailInput) -> str:
    """Get detailed status of a specific fail2ban jail, including all banned IPs.

    Args:
        params.jail: Jail name
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: Jail stats and list of currently banned IPs
    """
    _audit_log("blueteam_fail2ban_jail_status", {"jail": params.jail})
    if not shutil.which("fail2ban-client"):
        return _tool_not_found("fail2ban")
    r = _run(["fail2ban-client", "status", params.jail])
    return _redact_alert_data(r["stdout"] or r["stderr"], params=params)


class UnbanInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    jail: str = Field(..., max_length=64, description="Jail name")
    ip: str = Field(..., max_length=45, description="IP address to unban")
    bypass_redaction: bool = Field(default=False, description="When true, skip PII/credential redaction for audit investigations")

    @field_validator("ip")
    @classmethod
    def validate_ip(cls, v: str) -> str:
        if not v or len(v) > 45:
            raise ValueError("Invalid IP format or length")
        try:
            ipaddress.ip_address(v)
        except ValueError:
            raise ValueError("Invalid IP format") from None
        return v


@mcp.tool(
    name="blueteam_fail2ban_unban",
    annotations={"readOnlyHint": False, "destructiveHint": True, "idempotentHint": False, "openWorldHint": True}
)
async def blueteam_fail2ban_unban(params: UnbanInput) -> str:
    """Unban an IP address from a specific fail2ban jail.
    DESTRUCTIVE: Modifies security state (removes ban).

    Args:
        params.jail: Jail name
        params.ip: IP address to unban
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: Result of unban operation
    """
    if not _check_rate_limit():
        return json.dumps({"error": "Rate limit exceeded"})
    if not shutil.which("fail2ban-client"):
        return _tool_not_found("fail2ban")
    r = _run(["fail2ban-client", "set", params.jail, "unbanip", params.ip])
    out = r["stdout"] or r["stderr"]
    _audit_log("blueteam_fail2ban_unban", {"jail": params.jail, "ip": params.ip}, out[:200])
    return out




