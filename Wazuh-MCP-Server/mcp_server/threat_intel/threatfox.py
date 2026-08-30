#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
ThreatFox IOC Search - abuse.ch threat intelligence integration.
"""
from __future__ import annotations
import json, logging, time, os, re, asyncio
from typing import Any
import httpx
from pydantic import BaseModel, ConfigDict, Field, field_validator
from mcp_server import mcp, THREATFOX_API_KEY_ENV, THREATFOX_BASE_URL, THREATFOX_CACHE_TTL
from mcp_server.core.http_client import _api_call, _handle_api_error, _is_private_or_reserved
from mcp_server.core.audit import _audit_log, _truncate_if_needed
from mcp_server.threat_intel._cache import cache_get, cache_set, get_limiter

logger = logging.getLogger("blue_team_mcp.threatfox")

# Startup validation - warn if key missing
if not os.environ.get(THREATFOX_API_KEY_ENV):
    logger.warning("%s not set - threatfox_ioc_search will return an error at call time. "
                   "Get a free key at https://threatfox.abuse.ch/api", THREATFOX_API_KEY_ENV)

_threatfox_limiter = get_limiter("threatfox", max_concurrent=3, min_interval=0.1)  # 10 req/sec

# Patterns for detecting IOC type (used for SSRF guard scoping)
_IP_RE = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
_MD5_RE = re.compile(r"^[a-fA-F0-9]{32}$")
_SHA256_RE = re.compile(r"^[a-fA-F0-9]{64}$")


def _get_threatfox_api_key() -> str:
    key = os.environ.get(THREATFOX_API_KEY_ENV, "")
    if not key:
        raise RuntimeError(
            f"{THREATFOX_API_KEY_ENV} not set. "
            "Get a free API key at https://threatfox.abuse.ch/api"
        )
    return key


def _is_ip(ioc: str) -> bool:
    """Check if an IOC string is an IPv4 address (for SSRF guard scoping)."""
    return bool(_IP_RE.match(ioc))


async def _threatfox_request(search_term: str, exact_match: bool = False) -> dict[str, Any]:
    """Query the ThreatFox API with TTL caching.

    Args:
        search_term: IOC to search (IP, domain, or hash).
        exact_match: If True, search for exact IOC only (default: wildcard).

    Returns:
        Parsed API response dict.

    Raises:
        httpx.HTTPStatusError: On HTTP errors.
        httpx.TimeoutException: On timeout.
        RuntimeError: If API key is missing.
    """
    cache_key = f"{search_term}:{exact_match}"
    cached = cache_get("threatfox", cache_key)
    if cached is not None:
        return cached

    async with _threatfox_limiter:
        headers = {
            "Auth-Key": _get_threatfox_api_key(),
            "accept": "application/json",
            "User-Agent": "blue-team-mcp/1.0.0 (TangerangKota-CSIRT)",
            "Content-Type": "application/json",
        }
        body = {"query": "search_ioc", "search_term": search_term, "exact_match": exact_match}
        resp = await _api_call("post", THREATFOX_BASE_URL, headers=headers, json=body)
        data = resp.json()
    cache_set("threatfox", cache_key, data, THREATFOX_CACHE_TTL)
    return data


def _format_threatfox_markdown(search_term: str, data: dict[str, Any]) -> str:
    """Format ThreatFox API response as a human readable markdown threat card.

    Args:
        search_term: The IOC that was searched.
        data: Parsed API response from _threatfox_request().

    Returns:
        Markdown-formatted string.
    """
    query_status = data.get("query_status", "unknown")
    results = data.get("data", [])

    lines = [f"# ThreatFox IOC Search - `{search_term}`", ""]
    lines.append(f"**Status**: `{query_status}` | **Matches**: {len(results)}")

    if query_status != "ok" or not results:
        lines.append("")
        lines.append("_No results found for this IOC._")
        return "\n".join(lines)

    lines.append("")
    for i, entry in enumerate(results[:20], 1):
        lines.append(f"## Match {i}: {entry.get('ioc', '?')}")
        lines.append("")
        lines.append(f"| Field | Value |")
        lines.append(f"|-------|-------|")
        lines.append(f"| Threat Type | **{entry.get('threat_type_desc', entry.get('threat_type', '?'))}** |")
        lines.append(f"| IOC Type | {entry.get('ioc_type_desc', entry.get('ioc_type', '?'))} |")
        lines.append(f"| Malware | `{entry.get('malware_printable', entry.get('malware', '?'))}` |")
        conf = entry.get("confidence_level")
        conf_bar = _confidence_bar(conf) if conf is not None else "?"
        lines.append(f"| Confidence | {conf_bar} {conf}/100 |")
        lines.append(f"| First Seen | {entry.get('first_seen', '?')} |")
        lines.append(f"| Last Seen | {entry.get('last_seen', 'never')} |")

        tags = entry.get("tags")
        if tags:
            lines.append(f"| Tags | {', '.join(f'`{t}`' for t in tags)} |")

        alias = entry.get("malware_alias")
        if alias:
            lines.append(f"| Aliases | {alias} |")

        samples = entry.get("malware_samples", [])
        if samples:
            hashes = ", ".join(
                f"[`{s.get('sha256_hash','?')[:12]}...`]({s.get('malware_bazaar','#')})"
                for s in samples[:5]
            )
            lines.append(f"| Malware Samples | {hashes} |")

        reference = entry.get("reference")
        if reference:
            lines.append(f"| Reference | {reference} |")

        lines.append("")

    if len(results) > 20:
        lines.append(f"_... and {len(results) - 20} more matches. Use `json` format for complete results._")

    return "\n".join(lines)


def _confidence_bar(confidence: int) -> str:
    """Render a visual confidence bar: ████░░ 75%"""
    filled = min(int(confidence / 10), 10)
    return f"`{'█' * filled}{'░' * (10 - filled)}`"


class ThreatFoxSearchInput(BaseModel):
    """Input model for threatfox_ioc_search."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    search_term: str = Field(
        ...,
        min_length=3,
        max_length=256,
        description="IOC to search: IP address, domain name, or file hash (MD5/SHA256).",
    )
    exact_match: bool = Field(
        default=False,
        description="If true, search for the exact IOC only. Default: false (wildcard search).",
    )
    response_format: str = Field(
        default="markdown",
        description="'markdown' for human-readable threat card or 'json' for structured data.",
    )

    @field_validator("search_term")
    @classmethod
    def validate_search_term(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("search_term must not be empty")
        # Reject control characters and null bytes
        if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", v):
            raise ValueError("search_term contains invalid control characters")
        # SSRF guard: if it looks like an IP, validate it's not private
        if _IP_RE.match(v) and _is_private_or_reserved(v):
            raise ValueError(
                f"'{v}' is a private/reserved IP address. "
                "This tool only accepts public IPs for threat intelligence lookup."
            )
        return v


@mcp.tool(
    name="threatfox_ioc_search",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def threatfox_ioc_search(params: ThreatFoxSearchInput) -> str:
    """Search ThreatFox by abuse.ch for malware-associated indicators of compromise.

    Queries the ThreatFox API for any IOC - IP addresses, domain names, or file
    hashes (MD5/SHA256) - and returns associated malware families, threat types,
    confidence levels, and linked malware samples.

    **Required Permissions**: Free ThreatFox API key from https://threatfox.abuse.ch/api

    **Rate Limit**: ThreatFox does not publish a documented rate limit. This tool
    applies a 900-second in-memory cache to conserve quota.

    **Worked Examples**

    1. *Check if an IP is a known C2 server*:
       ``threatfox_ioc_search(search_term="185.220.101.1")``

    2. *Exact-match search for a specific hash*:
       ``threatfox_ioc_search(search_term="b325c92fa540edeb89b95dbfd4400c1cb33599c66859a87aead820e568a2ebe7", exact_match=true)``

    3. *Wildcard domain search*:
       ``threatfox_ioc_search(search_term="evil-c2.example.com")``

    **Error Handling**:
        - Missing API key -> ``"THREATFOX_API_KEY not set"`` at call time
        - Invalid/private IP -> rejected at Pydantic validation
        - ``query_status: "no_results"`` -> empty result set (not an error)
        - HTTP 429 → rate-limit message with retry hint
    """
    if not os.environ.get(THREATFOX_API_KEY_ENV):
        return json.dumps({
            "error": f"{THREATFOX_API_KEY_ENV} not set.",
            "detail": "Get a free API key at https://threatfox.abuse.ch/api",
        }, indent=2)

    _audit_log("threatfox_ioc_search", {"search_term": params.search_term, "exact_match": params.exact_match})

    try:
        raw = await _threatfox_request(params.search_term, params.exact_match)
    except (httpx.HTTPStatusError, httpx.TimeoutException, RuntimeError) as e:
        return _handle_api_error(e, context="threatfox_ioc_search")

    query_status = raw.get("query_status", "error")
    if query_status not in ("ok", "no_results"):
        return json.dumps({
            "error": f"ThreatFox API returned unexpected status: {query_status}",
            "raw": raw,
        }, indent=2)

    if params.response_format == "json":
        return _truncate_if_needed(json.dumps({
            "search_term": params.search_term,
            "exact_match": params.exact_match,
            "query_status": query_status,
            "match_count": len(raw.get("data", [])),
            "results": raw.get("data", []),
        }, indent=2, default=str))

    return _truncate_if_needed(_format_threatfox_markdown(params.search_term, raw))


class ThreatFoxBulkInput(BaseModel):
    """Input model for threatfox_ioc_search_bulk - concurrent multi-IOC lookup."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    search_terms: list[str] = Field(
        ...,
        min_length=1,
        max_length=25,
        description="IOCs to search concurrently (max 25). Accepts IPs, domains, or hashes.",
    )
    exact_match: bool = Field(
        default=False,
        description="If true, search for exact IOCs only. Default: false (wildcard).",
    )
    response_format: str = Field(
        default="markdown",
        description="'markdown' for human-readable summary or 'json' for structured data.",
    )

    @field_validator("search_terms")
    @classmethod
    def validate_search_terms(cls, v: list[str]) -> list[str]:
        cleaned: list[str] = []
        for term in v:
            term = term.strip()
            if not term or len(term) < 3 or len(term) > 256:
                raise ValueError(f"Invalid search term: '{term[:50]}...' — must be 3-256 chars")
            if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", term):
                raise ValueError(f"search_term contains invalid control characters: '{term[:50]}'")
            # SSRF guard for IP-format terms
            if _IP_RE.match(term) and _is_private_or_reserved(term):
                raise ValueError(f"'{term}' is a private/reserved IP address")
            cleaned.append(term)
        return cleaned


@mcp.tool(
    name="threatfox_ioc_search_bulk",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def threatfox_ioc_search_bulk(params: ThreatFoxBulkInput) -> str:
    """Search multiple IOCs against ThreatFox concurrently (max 25).

    Batches IOC lookups using ``asyncio.gather`` for speed. Each IOC is
    independently cached with the same 900-second TTL as single lookups.

    **Required Permissions**: Free ThreatFox API key from https://threatfox.abuse.ch/api

    **Worked Examples**

    1. *Bulk-check attacker IPs from a 3-Sum trigger*:
       ``threatfox_ioc_search_bulk(search_terms=["185.220.101.1", "139.180.203.104"])``

    2. *Check multiple file hashes*:
       ``threatfox_ioc_search_bulk(search_terms=["abc123...", "def456..."], exact_match=true)``

    3. *JSON output for automated pipelines*:
       ``threatfox_ioc_search_bulk(search_terms=["evil.com", "1.2.3.4"], response_format="json")``
    """
    if not os.environ.get(THREATFOX_API_KEY_ENV):
        return json.dumps({
            "error": f"{THREATFOX_API_KEY_ENV} not set.",
            "detail": "Get a free API key at https://threatfox.abuse.ch/api",
        }, indent=2)

    _audit_log("threatfox_ioc_search_bulk", {"count": len(params.search_terms)})

    async def _lookup_one(term: str) -> dict:
        try:
            raw = await _threatfox_request(term, params.exact_match)
            items = raw.get("data", [])
            if not isinstance(items, list):
                items = []
            return {
                "search_term": term,
                "query_status": raw.get("query_status", "error"),
                "matches": len(items),
                "malware": [e.get("malware_printable") or e.get("malware", "?") for e in items[:3]],
                "confidence": max((e.get("confidence_level", 0) for e in items), default=0),
            }
        except (httpx.HTTPStatusError, httpx.TimeoutException, RuntimeError) as e:
            return {"search_term": term, "error": _handle_api_error(e, context=term)}

    results = await __import__("asyncio").gather(*[_lookup_one(t) for t in params.search_terms])

    if params.response_format == "json":
        return _truncate_if_needed(json.dumps({
            "count": len(results),
            "results": results,
        }, indent=2))

    lines = ["# ThreatFox Bulk IOC Search", ""]
    for r in results:
        if "error" in r:
            lines.append(f"- **{r['search_term']}** - ⚠️ {r['error']}")
        elif r["matches"] == 0:
            lines.append(f"- `{r['search_term']}` - clean")
        else:
            lines.append(
                f"- `{r['search_term']}` - {r['matches']} matches, "
                f"malware: {', '.join(r['malware'][:3])}, "
                f"confidence: {r['confidence']}/100"
            )
    return _truncate_if_needed("\n".join(lines))
