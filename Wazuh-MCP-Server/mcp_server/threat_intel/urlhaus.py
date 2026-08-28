#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
URLhaus - abuse.ch malware URL database integration.
URLhaus tracks URLs that distribute malware. Complements blueteam_check_webshell:
that tool finds suspicious URLs on your infrastructure; this tool tells you if
those URLs are known malware distributors.
Endpoints (POST JSON):
/url/ - query a single URL or host
/payload/ - query a malware payload (MD5/SHA256)
"""
from __future__ import annotations
import json, logging, time, os, asyncio
from typing import Any
import httpx
from mcp_server import URLHAUS_API_KEY_ENV, URLHAUS_BASE_URL, URLHAUS_CACHE_TTL
from mcp_server.core.http_client import _api_call, _handle_api_error
from mcp_server.core.audit import _audit_log, _truncate_if_needed
from mcp_server.threat_intel._cache import cache_get, cache_set, get_limiter

logger = logging.getLogger("blue_team_mcp.urlhaus")

_urlhaus_limiter = get_limiter("urlhaus", max_concurrent=3, min_interval=0.2)  # 5 req/sec


def _get_urlhaus_api_key() -> str:
    return os.environ.get(URLHAUS_API_KEY_ENV, "")


async def _urlhaus_request(body: dict) -> dict[str, Any]:
    """POST to URLhaus /url/ endpoint with TTL caching + rate limiting."""
    return await _urlhaus_post("url/", body)


async def _urlhaus_payload_request(file_hash: str) -> dict[str, Any]:
    """POST to URLhaus /payload/ endpoint - file hash (MD5/SHA256) lookup.
    Returns ``signature`` (malware family name), file_type, detection ratio.
    """
    import re as _re
    if _re.match(r"^[A-Za-z0-9]{32}$", file_hash):
        body = {"md5_hash": file_hash}
    elif _re.match(r"^[A-Za-z0-9]{64}$", file_hash):
        body = {"sha256_hash": file_hash}
    else:
        return {"query_status": "illegal_hash"}
    return await _urlhaus_post("payload/", body)


async def _urlhaus_post(endpoint: str, body: dict) -> dict[str, Any]:
    """Shared POST helper for URLhaus endpoints (url/ and payload/)."""
    cache_key = f"{endpoint}:{json.dumps(body, sort_keys=True)}"
    cached = cache_get("urlhaus", cache_key)
    if cached is not None:
        return cached

    async with _urlhaus_limiter:
        headers = {
            "accept": "application/json",
            "User-Agent": "blue-team-mcp/1.0.0 (TangerangKota-CSIRT)",
            "Content-Type": "application/json",
        }
        key = _get_urlhaus_api_key()
        if key:
            headers["Auth-Key"] = key
        resp = await _api_call("post", URLHAUS_BASE_URL + endpoint, headers=headers, json=body)
        data = resp.json()

    cache_set("urlhaus", cache_key, data, URLHAUS_CACHE_TTL)
    return data


def _format_urlhaus_markdown(result: dict) -> str:
    """Format a URLhaus result as markdown."""
    lines = []
    query_status = result.get("query_status", "unknown")
    lines.append(f"**Status**: `{query_status}`")

    if query_status == "no_results":
        return " ".join(lines) + "\n\n_No known malware distribution found._"

    url_status = result.get("url_status", "?")
    threat = result.get("threat", "?")
    tags = result.get("tags", [])
    urlhaus_ref = result.get("urlhaus_reference", "")

    lines.append(f"**URL Status**: `{url_status}` | **Threat**: `{threat}`")
    if tags:
        lines.append(f"**Tags**: {', '.join(f'`{t}`' for t in tags[:10])}")
    if urlhaus_ref:
        lines.append(f"**Reference**: {urlhaus_ref}")

    # Payloads (malware samples)
    payloads = result.get("payloads", [])
    if payloads:
        lines.append(f"**Malware Payloads**: {len(payloads)}")
        for p in payloads[:5]:
            lines.append(f"- `{p.get('response_md5','?')[:12]}...` - {p.get('signature','?')} ({p.get('file_type','?')})")

    return "\n".join(lines)
