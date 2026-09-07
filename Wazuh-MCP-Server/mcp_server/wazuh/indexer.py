#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Wazuh Indexer (OpenSearch) query helpers - _search, _msearch, cursor pagination.
"""
from __future__ import annotations
import base64, json, logging, os, time
from typing import Dict, Optional, List
import httpx

logger = logging.getLogger("blue_team_mcp.indexer")

from mcp_server import (WAZUH_INDEXER_URL, WAZUH_INDEXER_USER, WAZUH_INDEXER_PASSWORD,
                         WAZUH_INDEXER_VERIFY_SSL, _WAZUH_INDEXER_MAX_SIZE)
from mcp_server.core.http_client import _api_call

_WAZUH_INDEX_PATTERNS = {"alerts": "wazuh-alerts-*", "events": "wazuh-events-*",
                           "vulnerabilities": "wazuh-states-vulnerabilities-*"}
_KEYWORD_SEARCH_FIELDS: list[tuple[str, int]] = [
    ("full_log", 3), ("rule.description", 2), ("rule.info", 2),
    ("data.srcip", 2), ("data.srcip2", 2), ("srcip", 2),
    ("rule.cve", 2), ("data.command", 1), ("data.protocol", 1),
    ("data.url", 0), ("data.domain", 0), ("data.user_agent", 0), ("data.referrer", 0),
]
_SRCIP_FIELD_PATHS: list[str] = [
    "data.srcip.keyword", "data.srcip", "data.src_ip.keyword", "data.client_ip.keyword",
    "data.remote_ip.keyword", "data.source_ip.keyword", "data.ip.keyword", "srcip.keyword",
]
_MSEARCH_FALLBACK_ERROR: dict = {"error": "_msearch_failed"}

# (3-Sum, pivot, threat-card) re-fire identical aggregations within seconds;
# dedupe those round-trips. TTL is deliberately short so relative time windows
# (now-24h) don't serve stale results. Errors are never cached.
_INDEXER_CACHE_TTL = float(os.environ.get("BLUETEAM_INDEXER_CACHE_TTL", "30"))
_INDEXER_CACHE: dict = {}  # {cache_key: (expiry_monotonic, response)}


async def _wazuh_indexer_mapping(index_pattern: Optional[str] = None) -> Dict:
    """Fetch index field mappings from the OpenSearch _mapping endpoint.
    Returns the raw mapping dict keyed by index name. Used by the schema
    explorer tool to discover field names/types before building aggregations
    (prevents the `.keyword` vs `keyword` field-mapping false-negative class).
    """
    if index_pattern is None:
        index_pattern = _WAZUH_INDEX_PATTERNS["alerts"]
    if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
        return {"error": "WAZUH_INDEXER_URL and WAZUH_INDEXER_PASSWORD must be set."}
    url = f"{WAZUH_INDEXER_URL}/{index_pattern}/_mapping"
    try:
        resp = await _api_call("get", url, client_name="indexer", verify=WAZUH_INDEXER_VERIFY_SSL,
                                auth=(WAZUH_INDEXER_USER, WAZUH_INDEXER_PASSWORD),
                                headers={"Content-Type": "application/json"})
        return resp.json()
    except httpx.HTTPStatusError as e:
        return {"error": f"Indexer API error: {e.response.status_code}", "detail": e.response.text[:500]}
    except Exception as e:
        return {"error": str(e)}


async def _wazuh_indexer_post(body: dict, index_pattern: Optional[str] = None) -> Dict:
    if index_pattern is None:
        index_pattern = _WAZUH_INDEX_PATTERNS["alerts"]
    if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
        return {"error": "WAZUH_INDEXER_URL and WAZUH_INDEXER_PASSWORD must be set."}
    cache_key = (index_pattern, json.dumps(body, sort_keys=True, default=str))
    now = time.monotonic()
    cached = _INDEXER_CACHE.get(cache_key)
    if cached and now < cached[0]:
        return cached[1]
    url = f"{WAZUH_INDEXER_URL}/{index_pattern}/_search"
    try:
        resp = await _api_call("post", url, client_name="indexer", verify=WAZUH_INDEXER_VERIFY_SSL,
                                auth=(WAZUH_INDEXER_USER, WAZUH_INDEXER_PASSWORD),
                                json=body, headers={"Content-Type": "application/json"})
        data = resp.json()
        if _INDEXER_CACHE_TTL > 0:
            _INDEXER_CACHE[cache_key] = (now + _INDEXER_CACHE_TTL, data)
            if len(_INDEXER_CACHE) > 1000:  # bound the cache
                _INDEXER_CACHE.pop(next(iter(_INDEXER_CACHE)))
        return data
    except httpx.HTTPStatusError as e:
        return {"error": f"Indexer API error: {e.response.status_code}", "detail": e.response.text[:500]}
    except Exception as e:
        return {"error": str(e)}


async def _wazuh_indexer_msearch(bodies: list[dict], index_pattern: Optional[str] = None) -> list[dict]:
    if index_pattern is None:
        index_pattern = _WAZUH_INDEX_PATTERNS["alerts"]
    if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
        return [{"error": "Not configured"}] * len(bodies)
    if not bodies:
        return []
    url = f"{WAZUH_INDEXER_URL}/{index_pattern}/_msearch"
    header = json.dumps({"index": index_pattern, "allow_partial_search_results": True})
    parts = []
    for b in bodies:
        parts.append(header)
        parts.append(json.dumps(b, separators=(",", ":"), default=str))
    ndjson = "\n".join(parts) + "\n"
    if not ndjson.endswith("\n"):
        ndjson += "\n"
    try:
        resp = await _api_call("post", url, client_name="indexer", verify=WAZUH_INDEXER_VERIFY_SSL,
                                auth=(WAZUH_INDEXER_USER, WAZUH_INDEXER_PASSWORD),
                                content=ndjson.encode("utf-8"),
                                headers={"Content-Type": "application/x-ndjson"})
        raw = resp.json()
        if isinstance(raw, dict) and "responses" in raw:
            responses = raw["responses"]
            # Per-response granularity: each response may independently
            # succeed or fail. Return individual error dicts for failed
            # queries so callers can distinguish partial failures.
            out: list[dict] = []
            for i, r in enumerate(responses):
                if isinstance(r, dict) and "error" in r:
                    out.append({"error": f"_msearch query {i} failed: {r['error'].get('reason', str(r['error']))}"})
                elif isinstance(r, dict) and "status" in r and r.get("status", 200) >= 400:
                    out.append({"error": f"_msearch query {i} HTTP {r['status']}",
                               "detail": str(r.get("error", {}))[:300]})
                else:
                    out.append(r)
            while len(out) < len(bodies):
                out.append({"error": f"_msearch query {len(out)}: no response"})
            return out
        return [raw] if not isinstance(raw, list) else raw
    except Exception as e:
        logger.warning("_msearch failed (%s) - returning per-query error dicts", e)
        # Per-query fallback: each body gets its own error dict rather than
        # a single blanket error. This lets callers that can handle partial
        # failures (e.g. 3-Sum with one category down) continue working.
        return [{"error": f"_msearch failed: {e}"}] * len(bodies)


# Cursor pagination (base64-encoded JSON)
def _encode_cursor(data: dict) -> str:
    """Encode a dict as a base64 cursor string for pagination tokens."""
    return base64.urlsafe_b64encode(json.dumps(data, separators=(",", ":")).encode()).decode().rstrip("=")


def _decode_cursor(cursor: str) -> dict | None:
    """Decode a base64 cursor string back to a dict. Returns None on invalid input."""
    try:
        padded = cursor + "=" * (4 - len(cursor) % 4)
        return json.loads(base64.urlsafe_b64decode(padded))
    except Exception:
        return None
