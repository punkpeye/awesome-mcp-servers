#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
HudsonRock stealer-log check - is this email in a known stealer log.
Answers the most urgent SOC question: "has this employee's password already
been stolen by malware?" HudsonRock's Cavalier API indexes credentials exfiltrated
by info-stealers (RedLine, Raccoon, Vidar, etc.).
Free tier (no key): preview search limited/redacted results.
Full API (HUDSONROCK_API_KEY): complete stealer-log records.
Endpoint (free Cavalier):
- GET {HUDSONROCK_BASE_URL}/preview/search-by-login?email=user@example.com
"""
from typing import Optional, Literal
from urllib.parse import quote
import json, os, re
from pydantic import BaseModel, ConfigDict, Field, field_validator
import httpx
from mcp_server import mcp, HUDSONROCK_API_KEY_ENV, HUDSONROCK_BASE_URL
from mcp_server.core.http_client import _api_call, _handle_api_error
from mcp_server.core.tool_decorator import blueteam_tool

_EMAIL_RE = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


class StealerLogInput(BaseModel):
    """Input model for stealer_log_check."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    email: str = Field(
        ..., min_length=6, max_length=256,
        description="Email address to check against stealer logs, e.g. 'csirt@tangerangkota.go.id'.",
    )
    response_format: Literal["markdown", "json"] = Field(default="markdown")

    @field_validator("email")
    @classmethod
    def validate_email(cls, v: str) -> str:
        v = v.strip().lower()
        if not _EMAIL_RE.match(v):
            raise ValueError(f"Invalid email address: '{v}'")
        return v


def _parse_stealer_logs(raw: dict) -> list[dict]:
    """Normalize HudsonRock response into a flat list of stealer-log hits."""
    logs = raw.get("stealer_logs", [])
    if not isinstance(logs, list):
        return []
    out = []
    for log in logs:
        if not isinstance(log, dict):
            continue
        out.append({
            "date_compromised": log.get("date_compromised", "?"),
            "malware": log.get("malware", "?"),
            "computer_name": log.get("computer_name", "?"),
            "operating_system": log.get("operating_system", "?"),
            "infected_ips": log.get("infected_ips", [])[:5],
            "credential_count": len(log.get("credentials", []) or []),
        })
    return out


@blueteam_tool(
    name="stealer_log_check",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": True},
)
async def stealer_log_check(params: StealerLogInput) -> str:
    """Check if an email appears in known stealer logs (HudsonRock).

    Queries HudsonRock's Cavalier API for credentials exfiltrated by info-stealer
    malware (RedLine, Raccoon, Vidar, etc.). If the email is found, the password
    is actively circulating on the dark web - reset it immediately.

    **Required Permissions**: free (no key) for preview results, or
    ``HUDSONROCK_API_KEY`` for complete records.

    **Worked Examples**

    1. *Check a compromised dinas email*:
       ``stealer_log_check(email="csirt@tangerangkota.go.id")``

    2. *JSON output*:
       ``stealer_log_check(email="user@example.com", response_format="json")``
    """
    api_key = os.environ.get(HUDSONROCK_API_KEY_ENV, "")
    if api_key:
        # Full API - requires key, different auth header
        url = f"https://api.hudsonrock.com/v1/search-by-login?email={quote(params.email)}"
        headers = {"api-key": api_key, "accept": "application/json",
                   "User-Agent": "blue-team-mcp/1.0.0 (TangerangKota-CSIRT)"}
    else:
        # Free Cavalier preview endpoint
        url = f"{HUDSONROCK_BASE_URL}/preview/search-by-login?email={quote(params.email)}"
        headers = {"accept": "application/json",
                   "User-Agent": "blue-team-mcp/1.0.0 (TangerangKota-CSIRT)"}

    try:
        resp = await _api_call("get", url, headers=headers)
        raw = resp.json()
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            return json.dumps({"email": params.email, "found": False,
                               "stealer_logs": [], "note": "No stealer-log hits."}, indent=2)
        return _handle_api_error(e, context="stealer_log_check")
    except httpx.TimeoutException as e:
        return _handle_api_error(e, context="stealer_log_check")

    logs = _parse_stealer_logs(raw)
    found = len(logs) > 0

    if params.response_format == "json":
        return json.dumps({
            "email": params.email,
            "found": found,
            "stealer_log_count": len(logs),
            "stealer_logs": logs,
            "api_tier": "full" if api_key else "preview",
        }, indent=2)

    lines = [f"# Stealer Log Check - `{params.email}`", ""]
    if not found:
        lines.append("✅ **No stealer-log hits** - this email has not been observed in known info-stealer exfiltration.")
        return "\n".join(lines)

    lines.append(f"🔴 **FOUND in {len(logs)} stealer log(s)** - credentials are circulating. **Reset password immediately.**")
    lines.append("")
    lines.append("| Compromised | Malware | Machine | OS | Infected IPs |")
    lines.append("|-------------|---------|---------|----|--------------|")
    for log in logs:
        lines.append(f"| {log['date_compromised']} | `{log['malware']}` | {log['computer_name']} "
                     f"| {log['operating_system']} | {', '.join(log['infected_ips'][:3])} |")

    if not api_key:
        lines.append("")
        lines.append("_Preview tier (no API key) - set `HUDSONROCK_API_KEY` for full credential details._")

    return "\n".join(lines)
