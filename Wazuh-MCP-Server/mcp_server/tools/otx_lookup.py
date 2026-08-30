#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
OTX AlienVault MCP tools - pulse-based threat intel lookup.
"""
from __future__ import annotations
import json, os, re
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field, field_validator
import httpx
from mcp_server import mcp, OTX_API_KEY_ENV
from mcp_server.core.audit import _audit_log, _truncate_if_needed
from mcp_server.core.http_client import _handle_api_error, _is_private_or_reserved
from mcp_server.threat_intel.otx import (
    _otx_request, _classify_indicator, _extract_pulse_summary,
    _format_otx_markdown, _format_geo_markdown, _normalize_adversary,
)


class OtxLookupInput(BaseModel):
    """Input model for otx_lookup."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    indicator: str = Field(
        ..., min_length=3, max_length=256,
        description="IOC to look up: IPv4/IPv6, domain, hostname, URL, or file hash (MD5/SHA1/SHA256).",
    )
    section: Literal["general", "geo", "reputation", "malware", "url_list", "passive_dns"] = Field(
        default="general",
        description="OTX data section. 'general' = pulses + reputation (recommended). "
                    "'geo' = geolocation. 'malware' = malware samples. "
                    "'passive_dns' = passive DNS history. 'url_list' = URLs in pulses.",
    )
    response_format: Literal["markdown", "json"] = Field(
        default="markdown",
        description="Output format.",
    )

    @field_validator("indicator")
    @classmethod
    def validate_indicator(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("indicator must not be empty")
        if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", v):
            raise ValueError("indicator contains invalid control characters")
        # SSRF guard: private IPs rejected for public threat-intel
        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", v) and _is_private_or_reserved(v):
            raise ValueError(f"'{v}' is a private/reserved IP address")
        if not _classify_indicator(v):
            raise ValueError(f"Unrecognized IOC type: '{v}'. Supported: IP, domain, hostname, URL, MD5/SHA1/SHA256.")
        return v


@mcp.tool(
    name="otx_lookup",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": True},
)
async def otx_lookup(params: OtxLookupInput) -> str:
    """Look up an IOC in AlienVault OTX (Open Threat Exchange).
    OTX is the largest open threat intel community. Unlike reputation-only
    feeds, OTX returns *pulses* - curated IOC collections with malware families,
    adversaries, industries, and MITRE ATT&CK technique IDs. This provides
    attribution and campaign context (who is attacking, with what malware,
    targeting which industries).

    **Required Permissions**: Free OTX API key from https://otx.alienvault.com

    **Worked Examples**

    1. *Check an attacker IP for campaign context*:
       ``otx_lookup(indicator="140.82.0.86")``

    2. *Get geolocation of an IP*:
       ``otx_lookup(indicator="140.82.0.86", section="geo")``

    3. *Passive DNS history of a domain*:
       ``otx_lookup(indicator="evil-c2.example.com", section="passive_dns")``
    """
    if not os.environ.get(OTX_API_KEY_ENV):
        return json.dumps({
            "error": f"{OTX_API_KEY_ENV} not set.",
            "detail": "Get a free key at https://otx.alienvault.com/api",
        }, indent=2)

    _audit_log("otx_lookup", {"indicator": params.indicator, "section": params.section})

    try:
        raw = await _otx_request(params.indicator, params.section)
    except (httpx.HTTPStatusError, httpx.TimeoutException, RuntimeError) as e:
        return _handle_api_error(e, context="otx_lookup")

    if isinstance(raw, dict) and "error" in raw:
        return json.dumps(raw, indent=2)

    ind_type = _classify_indicator(params.indicator)

    if params.response_format == "json":
        if params.section == "general":
            pulses = raw.get("pulse_info", {}).get("pulses", [])
            result = {
                "indicator": params.indicator,
                "indicator_type": ind_type,
                "pulse_count": raw.get("pulse_info", {}).get("count", 0),
                "pulses": _extract_pulse_summary(pulses),
            }
        else:
            result = {"indicator": params.indicator, "indicator_type": ind_type,
                      "section": params.section, "data": raw}
        return _truncate_if_needed(json.dumps(result, indent=2, default=str))

    # Markdown
    if params.section == "general":
        pulses = raw.get("pulse_info", {}).get("pulses", [])
        return _truncate_if_needed(_format_otx_markdown(params.indicator, ind_type, raw, pulses))
    if params.section == "geo":
        return _truncate_if_needed(_format_geo_markdown(params.indicator, raw))

    # Other sections - generic JSON dump
    return _truncate_if_needed(json.dumps(raw, indent=2, default=str))


class OtxBulkInput(BaseModel):
    """Input model for otx_lookup_bulk."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    indicators: list[str] = Field(
        ..., min_length=1, max_length=20,
        description="IOCs to look up concurrently (max 20).",
    )
    response_format: Literal["markdown", "json"] = Field(default="markdown")

    @field_validator("indicators")
    @classmethod
    def validate_indicators(cls, v: list[str]) -> list[str]:
        cleaned = []
        for term in v:
            term = term.strip()
            if not term or len(term) < 3 or len(term) > 256:
                raise ValueError(f"Invalid indicator: '{term[:50]}'")
            if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", term) and _is_private_or_reserved(term):
                raise ValueError(f"'{term}' is a private/reserved IP")
            if not _classify_indicator(term):
                raise ValueError(f"Unrecognized IOC type: '{term}'")
            cleaned.append(term)
        return cleaned


@mcp.tool(
    name="otx_lookup_bulk",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": True},
)
async def otx_lookup_bulk(params: OtxBulkInput) -> str:
    """Look up multiple IOCs against AlienVault OTX concurrently (max 20).

    **Worked Examples**

    1. *Bulk-check attacker IPs for campaign attribution*:
       ``otx_lookup_bulk(indicators=["140.82.0.86", "144.217.241.177"])``

    2. *JSON output*:
       ``otx_lookup_bulk(indicators=["evil.com", "1.2.3.4"], response_format="json")``
    """
    if not os.environ.get(OTX_API_KEY_ENV):
        return json.dumps({"error": f"{OTX_API_KEY_ENV} not set."}, indent=2)

    _audit_log("otx_lookup_bulk", {"count": len(params.indicators)})

    async def _one(ind: str) -> dict:
        try:
            raw = await _otx_request(ind, "general")
            pulses = raw.get("pulse_info", {}).get("pulses", [])
            return {
                "indicator": ind,
                "indicator_type": _classify_indicator(ind),
                "pulse_count": raw.get("pulse_info", {}).get("count", 0),
                "malware_families": list({m for p in pulses for m in p.get("malware_families", [])})[:5],
                "adversaries": list({_normalize_adversary(p.get("adversary")) for p in pulses if _normalize_adversary(p.get("adversary"))})[:5],
            }
        except (httpx.HTTPStatusError, httpx.TimeoutException, RuntimeError) as e:
            return {"indicator": ind, "error": _handle_api_error(e, context=ind)}

    import asyncio
    results = await asyncio.gather(*[_one(i) for i in params.indicators])

    if params.response_format == "json":
        return _truncate_if_needed(json.dumps({"count": len(results), "results": results}, indent=2))

    lines = ["# OTX Bulk Lookup", ""]
    for r in results:
        if "error" in r:
            lines.append(f"- `{r['indicator']}` - ⚠️ {r['error']}")
        elif r["pulse_count"] == 0:
            lines.append(f"- `{r['indicator']}` - clean (0 pulses)")
        else:
            mf = ", ".join(r.get("malware_families", [])[:3]) or "none"
            adv = ", ".join(r.get("adversaries", [])[:3]) or "none"
            lines.append(f"- `{r['indicator']}` — {r['pulse_count']} pulses | malware: {mf} | adversary: {adv}")
    return _truncate_if_needed("\n".join(lines))
