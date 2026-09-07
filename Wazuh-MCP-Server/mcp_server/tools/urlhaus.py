#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
URLhaus MCP tools - malware URL database lookup.
"""
from __future__ import annotations
import json, re
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field, field_validator
import httpx
from mcp_server import mcp, URLHAUS_API_KEY_ENV
from mcp_server.core.audit import _audit_log, _truncate_if_needed
from mcp_server.core.http_client import _handle_api_error
from mcp_server.threat_intel.urlhaus import (_urlhaus_request, _urlhaus_payload_request,
                                             _format_urlhaus_markdown)

_HASH_RE = re.compile(r"^[a-fA-F0-9]{32}$|^[a-fA-F0-9]{64}$")


class UrlhausLookupInput(BaseModel):
    """Input model for urlhaus_lookup."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    url: str = Field(
        ..., min_length=5, max_length=2048,
        description="URL to check for malware distribution, e.g. 'http://evil.com/malware.exe'.",
    )
    response_format: Literal["markdown", "json"] = Field(default="markdown")


@mcp.tool(
    name="urlhaus_lookup",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": True},
)
async def urlhaus_lookup(params: UrlhausLookupInput) -> str:
    """Check if a URL is a known malware distributor via URLhaus (abuse.ch).

    Complements ``blueteam_check_webshell``: that tool finds suspicious URLs on
    your infrastructure; this tool tells you if those exact URLs are known to
    distribute malware.

    **Required Permissions**: URLhaus works WITHOUT an API key (rate-limited).
    Set ``URLHAUS_API_KEY`` to raise the rate limit.

    **Worked Examples**

    1. *Check a suspicious URL found during webshell scan*:
       ``urlhaus_lookup(url="http://149.129.255.141/owl/login.php")``

    2. *JSON output*:
       ``urlhaus_lookup(url="http://evil.com/payload.exe", response_format="json")``
    """
    _audit_log("urlhaus_lookup", {"url": params.url})

    try:
        raw = await _urlhaus_request({"url": params.url})
    except (httpx.HTTPStatusError, httpx.TimeoutException) as e:
        return _handle_api_error(e, context="urlhaus_lookup")

    if params.response_format == "json":
        return _truncate_if_needed(json.dumps(raw, indent=2, default=str))

    lines = [f"# URLhaus - `{params.url}`", ""]
    lines.append(_format_urlhaus_markdown(raw))
    return _truncate_if_needed("\n".join(lines))


class UrlhausHashInput(BaseModel):
    """Input model for urlhaus_hash_lookup."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    file_hash: str = Field(
        ..., min_length=32, max_length=64,
        description="File hash to look up: MD5 (32 hex) or SHA256 (64 hex).",
    )
    response_format: Literal["markdown", "json"] = Field(default="markdown")

    @field_validator("file_hash")
    @classmethod
    def validate_hash(cls, v: str) -> str:
        v = v.strip().lower()
        if not re.match(r"^[a-f0-9]{32}$|^[a-f0-9]{64}$", v):
            raise ValueError("file_hash must be a valid MD5 (32 hex) or SHA256 (64 hex)")
        return v


@mcp.tool(
    name="urlhaus_hash_lookup",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": True},
)
async def urlhaus_hash_lookup(params: UrlhausHashInput) -> str:
    """Look up a file hash (MD5/SHA256) in URLhaus malware payload database.

    Returns the malware signature (family name), file type, first/last seen,
    VirusTotal detection ratio, and associated URLs. Complements
    ``threatfox_ioc_search`` with URLhaus's specific malware payload data.

    **Required Permissions**: URLhaus works WITHOUT an API key (rate-limited).
    Set ``URLHAUS_API_KEY`` to raise the limit.

    **Worked Examples**

    1. *Check an MD5 hash*:
       ``urlhaus_hash_lookup(file_hash="b325c92fa540edeb89b95dbfd4400c1c")``

    2. *Check a SHA256 hash*:
       ``urlhaus_hash_lookup(file_hash="<64-char-sha256>")``
    """
    _audit_log("urlhaus_hash_lookup", {"file_hash": params.file_hash})

    try:
        raw = await _urlhaus_payload_request(params.file_hash)
    except (httpx.HTTPStatusError, httpx.TimeoutException) as e:
        return _handle_api_error(e, context="urlhaus_hash_lookup")

    if raw.get("query_status") == "illegal_hash":
        return json.dumps({"error": "Invalid file hash format."}, indent=2)

    if params.response_format == "json":
        return _truncate_if_needed(json.dumps(raw, indent=2, default=str))

    if raw.get("query_status") == "no_results":
        return f"# URLhaus Payload - `{params.file_hash}`\n\n_No known malware payload found._"

    lines = [f"# URLhaus Payload - `{params.file_hash}`", ""]
    lines.append(f"| Field | Value |")
    lines.append(f"|-------|-------|")
    lines.append(f"| Signature | **{raw.get('signature', '?')}** |")
    lines.append(f"| File Type | {raw.get('file_type', '?')} |")
    lines.append(f"| First Seen | {raw.get('firstseen', '?')} |")
    lines.append(f"| Last Seen | {raw.get('lastseen', '?')} |")
    vt = raw.get("virustotal", {})
    if vt:
        lines.append(f"| VirusTotal | {vt.get('result', '?')} ({vt.get('percent', '?')}) |")
    urls = raw.get("urls", [])
    if urls:
        lines.append(f"| Associated URLs | {len(urls)} |")
        for u in urls[:5]:
            lines.append(f"| | `{u.get('url', '?')}` ({u.get('url_status', '?')}) |")
    return _truncate_if_needed("\n".join(lines))


class UrlhausBulkInput(BaseModel):
    """Input model for urlhaus_lookup_bulk."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    urls: list[str] = Field(
        ..., min_length=1, max_length=20,
        description="URLs to check concurrently (max 20).",
    )
    response_format: Literal["markdown", "json"] = Field(default="markdown")


@mcp.tool(
    name="urlhaus_lookup_bulk",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": True},
)
async def urlhaus_lookup_bulk(params: UrlhausBulkInput) -> str:
    """Check multiple URLs against URLhaus concurrently (max 20).

    **Worked Examples**

    1. *Bulk-check URLs from a webshell scan*:
       ``urlhaus_lookup_bulk(urls=["http://asu.com/x.php", "http://jnck.com/y.php"])``
    """
    _audit_log("urlhaus_lookup_bulk", {"count": len(params.urls)})

    async def _one(url: str) -> dict:
        try:
            raw = await _urlhaus_request({"url": url})
            return {
                "url": url,
                "query_status": raw.get("query_status", "error"),
                "url_status": raw.get("url_status", "?"),
                "threat": raw.get("threat", "?"),
                "malware_payloads": len(raw.get("payloads", [])),
            }
        except (httpx.HTTPStatusError, httpx.TimeoutException) as e:
            return {"url": url, "error": _handle_api_error(e, context=url)}

    import asyncio
    results = await asyncio.gather(*[_one(u) for u in params.urls])

    if params.response_format == "json":
        return _truncate_if_needed(json.dumps({"count": len(results), "results": results}, indent=2))

    lines = ["# URLhaus Bulk Lookup", ""]
    for r in results:
        if "error" in r:
            lines.append(f"- `{r['url']}` — ⚠️ {r['error']}")
        elif r["query_status"] == "no_results":
            lines.append(f"- `{r['url']}` — clean")
        else:
            lines.append(f"- `{r['url']}` — `{r['url_status']}` | `{r['threat']}` | {r['malware_payloads']} payloads")
    return _truncate_if_needed("\n".join(lines))
