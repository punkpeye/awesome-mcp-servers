#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
RapidAPI capability lookups - three providers over a shared RapidAPI transport:
1. blueteam_ip_blacklist  - Apiverve IP Blacklist Lookup (is this srcip on a blacklist?)
2. blueteam_ioc_search    - RapidAPI IOC Search (malware/IOC matches for a srcip)
3. blueteam_breach_check  - RapidAPI Breach Check (was this email in a known breach?)
All three accept the indicator (srcip / attacker IP / email) directly so the LLM can feed
values pulled from Wazuh alerts without any extra plumbing. Responses are handled
dynamically - the raw JSON is returned verbatim plus a normalized envelope, so unknown or
changing third-party schemas never break the tool.
"""
from __future__ import annotations
import json, os, re
from typing import Any, Literal
from urllib.parse import quote
import httpx
from pydantic import BaseModel, ConfigDict, Field, field_validator
from mcp_server import mcp, RAPIDAPI_KEY_ENV
from mcp_server.core.http_client import _api_call, _handle_api_error, ValidPublicIp
from mcp_server.core.audit import _audit_log, _truncate_if_needed
from mcp_server.core.redact import _redact_alert_data
from mcp_server.threat_intel._cache import cache_get, cache_set, get_limiter

# RapidAPI host endpoints (The key is shared via RAPIDAPI_KEY).
_IP_BLACKLIST_HOST = "ip-blacklist-lookup-api-apiverve.p.rapidapi.com"
_IOC_SEARCH_HOST = "ioc-search.p.rapidapi.com"
_BREACH_CHECK_HOST = "breachcheck-api.p.rapidapi.com"

_limiter = get_limiter("rapidapi", max_concurrent=3, min_interval=0.15)  # RapidAPI free tier ~5 req/s

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def _rapidapi_headers(host: str) -> dict[str, str]:
    key = os.environ.get(RAPIDAPI_KEY_ENV)
    if not key:
        raise RuntimeError(
            f"{RAPIDAPI_KEY_ENV} not set. Get a key at https://rapidapi.com (subscribe to the"
            f"three providers: Apiverve IP Blacklist, IOC Search, Breach Check)."
        )
    return {
        "x-rapidapi-key": key,
        "x-rapidapi-host": host,
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "blue-team-mcp/1.0 (TangerangKota-CSIRT)",
    }


async def _rapidapi_get(host: str, path: str, ttl: int = 1800) -> dict[str, Any]:
    """GET a RapidAPI endpoint with TTL caching + rate limiting. Returns parsed JSON."""
    cache_key = f"{host}{path}"
    cached = cache_get("rapidapi", cache_key)
    if cached is not None:
        return cached
    async with _limiter:
        resp = await _api_call("get", f"https://{host}{path}", headers=_rapidapi_headers(host))
        data = resp.json()
    cache_set("rapidapi", cache_key, data, ttl)
    return data


def _dynamic_markdown(title: str, raw: dict[str, Any]) -> str:
    """Render a third-party JSON body without assuming a fixed schema.
    Surfaces common keys (status/message/data/result/matches/total/found) when present and
    falls back to a pretty-printed full body when the shape is unrecognized — so a schema
    change upstream never produces an empty or crashing report.
    """
    lines = [f"# {title}", ""]
    recognized = 0
    for key in ("status", "message", "total", "found", "result", "data", "matches"):
        if key in raw:
            recognized += 1
            value = raw[key]
            if isinstance(value, (dict, list)):
                lines.append(f"**{key}**")
                lines.append("```json")
                lines.append(json.dumps(value, indent=2, ensure_ascii=False))
                lines.append("```")
            else:
                lines.append(f"- **{key}**: {value}")
    if recognized == 0:
        lines.append("```json")
        lines.append(json.dumps(raw, indent=2, ensure_ascii=False))
        lines.append("```")
    return _truncate_if_needed("\n".join(lines))


def _envelope(query: str, source: str, raw: dict[str, Any], params=None) -> str:
    """Normalized JSON envelope: query + source + the dynamic raw body (redacted)."""
    return json.dumps(_redact_alert_data(
        {"query": query, "source": source, "result": raw}, params=params),
        indent=2, ensure_ascii=False)


def _sanitize_breach(raw: dict[str, Any]) -> dict[str, Any]:
    """Reduce a breach-check response to non-PII metadata only.
    Breach dumps can carry names, phone numbers, physical addresses, and leaked
    passwords none of which the shape-based redaction layers catch (they only
    match emails/domains/IPs). We surface only the verdict + breach metadata
    (name/date/data-classes already public) and drop raw PII.
    """
    out: dict[str, Any] = {}
    for k in ("found", "breached", "is_breached", "breach"):
        if k in raw and isinstance(raw[k], (bool, int)):
            out["breached"] = bool(raw[k])
            break
    breaches = raw.get("breaches") or raw.get("data") or raw.get("result")
    if isinstance(breaches, list):
        meta = []
        for b in breaches:
            if isinstance(b, dict):
                safe = {k: b[k] for k in ("name", "title", "breach_date", "date",
                                          "domain", "data_classes", "description")
                        if k in b}
                if safe:
                    meta.append(safe)
            elif isinstance(b, str):
                meta.append({"name": b})
        if meta:
            out["breaches"] = meta[:10]
    return out


class _IpInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    ip: ValidPublicIp = Field(..., min_length=3, max_length=45,
                              description="Source IP (attacker srcip) from a Wazuh alert.")
    response_format: Literal["markdown", "json"] = Field(default="markdown")


class BreachCheckInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    email: str = Field(..., min_length=6, max_length=254,
                       description="Email address to check (e.g. an official 'user_x@mail.go.id' account from Wazuh).")
    response_format: Literal["markdown", "json"] = Field(default="markdown")

    @field_validator("email")
    @classmethod
    def _validate_email(cls, v: str) -> str:
        v = v.strip()
        if not _EMAIL_RE.match(v):
            raise ValueError(f"Invalid email address: '{v}'")
        return v


@mcp.tool(name="blueteam_ip_blacklist",
          annotations={"readOnlyHint": True, "destructiveHint": False,
                       "idempotentHint": True, "openWorldHint": True})
async def blueteam_ip_blacklist(params: _IpInput) -> str:
    """Check whether a source IP is present on blacklists (IP Blacklist Lookup).

    Feed the `srcip` from a Wazuh alert directly. Returns the blacklist verdict for the IP.
    Requires `RAPIDAPI_KEY` (subscribe to "IP Blacklist Lookup" by Apiverve on RapidAPI).

    **Worked Examples**
    1. ``blueteam_ip_blacklist(ip="103.107.116.202")``
    2. ``blueteam_ip_blacklist(ip="185.220.101.1", response_format="json")``
    """
    _audit_log("blueteam_ip_blacklist", {"ip": params.ip})
    try:
        raw = await _rapidapi_get(_IP_BLACKLIST_HOST, f"/v1/ipblacklistlookup?ip={quote(params.ip)}")
    except (httpx.HTTPStatusError, httpx.TimeoutException, RuntimeError, ValueError) as e:
        return _handle_api_error(e, context="blueteam_ip_blacklist")
    if params.response_format == "json":
        return _envelope(params.ip, "apiverve_ip_blacklist", raw, params=params)
    return _redact_alert_data(_dynamic_markdown(f"IP Blacklist - {params.ip}", raw), params=params)


@mcp.tool(name="blueteam_ioc_search",
          annotations={"readOnlyHint": True, "destructiveHint": False,
                       "idempotentHint": True, "openWorldHint": True})
async def blueteam_ioc_search(params: _IpInput) -> str:
    """Search IOC databases for a source IP (RapidAPI IOC Search).

    Feed the `srcip` from a Wazuh alert. Returns matched malware/IOC records for the IP.
    Requires `RAPIDAPI_KEY` (subscribe to "IOC Search" on RapidAPI).

    **Worked Examples**
    1. ``blueteam_ioc_search(ip="103.107.116.202")``
    2. ``blueteam_ioc_search(ip="185.220.101.1", response_format="json")``
    """
    _audit_log("blueteam_ioc_search", {"ip": params.ip})
    try:
        raw = await _rapidapi_get(_IOC_SEARCH_HOST, f"/rapid/v1/ioc/search/ip?query={quote(params.ip)}")
    except (httpx.HTTPStatusError, httpx.TimeoutException, RuntimeError, ValueError) as e:
        return _handle_api_error(e, context="blueteam_ioc_search")
    if params.response_format == "json":
        return _envelope(params.ip, "rapidapi_ioc_search", raw, params=params)
    return _redact_alert_data(_dynamic_markdown(f"IOC Search - {params.ip}", raw), params=params)


@mcp.tool(name="blueteam_breach_check",
          annotations={"readOnlyHint": True, "destructiveHint": False,
                       "idempotentHint": True, "openWorldHint": True})
async def blueteam_breach_check(params: BreachCheckInput) -> str:
    """Check whether an email address appeared in a known data breach (RapidAPI Breach Check).

    Feed an official email (`email dinas`, e.g. ``user_x@tangerangkota.go.id``) from a Wazuh
    compromised-email alert. Returns the breach status for the address.
    Requires `RAPIDAPI_KEY` (subscribe to "Breach Check" on RapidAPI).

    **Worked Examples**
    1. ``blueteam_breach_check(email="csirt@tangerangkota.go.id")``
    2. ``blueteam_breach_check(email="csirt@tangerangkota.go.id", response_format="json")``
    """
    _audit_log("blueteam_breach_check", {"email": params.email})
    try:
        raw = await _rapidapi_get(_BREACH_CHECK_HOST, f"/email-check?email={quote(params.email)}")
    except (httpx.HTTPStatusError, httpx.TimeoutException, RuntimeError, ValueError) as e:
        return _handle_api_error(e, context="blueteam_breach_check")
    if params.response_format == "json":
        return _envelope(params.email, "rapidapi_breach_check", _sanitize_breach(raw), params=params)
    return _redact_alert_data(_dynamic_markdown(f"Breach Check — {params.email}", _sanitize_breach(raw)), params=params)
