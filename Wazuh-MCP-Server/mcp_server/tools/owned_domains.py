#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Owned-domain management view + set the victim domains used by `protect_victim` redaction.
These domains are what the redaction pipeline treats as *victim infrastructure*:
under `protect_victim`, only emails/subdomains at these domains are masked, while
attacker IOCs (IPs, domains, payloads, country) stay visible. The persistent
default is the `BLUETEAM_OWNED_DOMAINS` env var; `blueteam_set_owned_domains`
updates it at runtime (in-memory only, until restart).
"""
from __future__ import annotations
import json, re
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field, field_validator
from mcp_server import mcp, BLUETEAM_REDACTION_POLICY, BLUETEAM_ALLOW_RUNTIME_DOMAINS
from mcp_server.core.audit import _audit_log, _truncate_if_needed
from mcp_server.core.redact import get_owned_domains, set_owned_domains

_DOMAIN_RE = re.compile(
    r"^[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?"
    r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$"
)


class OwnedDomainsViewInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    response_format: Literal["markdown", "json"] = Field(default="markdown")


@mcp.tool(
    name="blueteam_owned_domains",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": False},
)
async def blueteam_owned_domains(params: OwnedDomainsViewInput) -> str:
    """Show the active redaction policy and the configured owned (victim) domains.

    Under `protect_victim`, only these domains' emails/subdomains are masked - attacker
    IOCs stay visible. Configure them via the `BLUETEAM_OWNED_DOMAINS` env var
    (comma-separated) or at runtime via `blueteam_set_owned_domains`.

    **Worked Examples**
    1. ``blueteam_owned_domains()``
    2. ``blueteam_owned_domains(response_format="json")``
    """
    _audit_log("blueteam_owned_domains", {})
    domains = sorted(get_owned_domains())
    policy = BLUETEAM_REDACTION_POLICY
    active = policy == "protect_victim" and bool(domains)
    if params.response_format == "json":
        return json.dumps({
            "policy": policy,
            "owned_domains": domains,
            "protect_victim_active": active,
        }, indent=2, ensure_ascii=False)

    lines = ["# 🏛️ Owned Domains (victim infrastructure)", "",
             f"- **Policy**: `{policy}`",
             f"- **Owned domains**: {', '.join('`' + d + '`' for d in domains) if domains else '*(none)*'}",
             f"- **protect_victim active**: {'✅ yes' if active else '❌ no'}"]
    if policy == "protect_victim" and not domains:
        lines.append("")
        lines.append("⚠️ `protect_victim` is set but no owned domains are configured - "
                     "the server falls back to `full`. Set `BLUETEAM_OWNED_DOMAINS`.")
    return _truncate_if_needed("\n".join(lines))


class OwnedDomainsSetInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    domains: str = Field(..., min_length=1, max_length=1024,
        description="Comma-separated owned (victim) domain names, e.g. 'tangerangkota.go.id,evil.com'.")

    @field_validator("domains")
    @classmethod
    def _validate_domains(cls, v: str) -> str:
        parts = [d.strip().lower().rstrip(".") for d in v.split(",") if d.strip()]
        if not parts:
            raise ValueError("At least one domain is required.")
        for d in parts:
            if not _DOMAIN_RE.match(d):
                raise ValueError(f"Invalid domain: '{d}'")
        return ",".join(parts)


@mcp.tool(
    name="blueteam_set_owned_domains",
    annotations={"readOnlyHint": False, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": False},
)
async def blueteam_set_owned_domains(params: OwnedDomainsSetInput) -> str:
    """Set the runtime owned (victim) domains used by `protect_victim` redaction.
    Operator action - changes which emails/subdomains are masked. In-memory only:
    the change lasts until restart; set `BLUETEAM_OWNED_DOMAINS` for a persistent default.
    **Worked Examples**
    1. ``blueteam_set_owned_domains(domains="tangerangkota.go.id")``
    2. ``blueteam_set_owned_domains(domains="anu.example.org,anuan.example.com")``
    """
    _audit_log("blueteam_set_owned_domains", {"domains": params.domains})
    if not BLUETEAM_ALLOW_RUNTIME_DOMAINS:
        return json.dumps({
            "error": "Runtime owned-domain updates are disabled.",
            "detail": "Set BLUETEAM_ALLOW_RUNTIME_DOMAINS=true to enable this operator action. "
                      "Use BLUETEAM_OWNED_DOMAINS for the persistent default.",
        }, indent=2, ensure_ascii=False)
    new_set = set_owned_domains(params.domains)
    return json.dumps({
        "status": "updated",
        "owned_domains": sorted(new_set),
        "policy": BLUETEAM_REDACTION_POLICY,
        "note": "In-memory only - set BLUETEAM_OWNED_DOMAINS for a persistent default.",
    }, indent=2, ensure_ascii=False)
