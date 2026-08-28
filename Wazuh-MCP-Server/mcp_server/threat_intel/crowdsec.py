#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
CrowdSec CTI - single + bulk IP reputation
"""
from __future__ import annotations
import json, logging, time, os, asyncio
from typing import Any
import httpx
from pydantic import BaseModel, ConfigDict, Field, field_validator, field_validator
from mcp_server import mcp, CROWDSEC_API_KEY_ENV, CROWDSEC_CACHE_TTL, CROWDSEC_BASE_URL
from mcp_server.core.http_client import _api_call, _handle_api_error, _is_private_or_reserved, ValidPublicIp
from mcp_server.core.audit import _audit_log, _truncate_if_needed
from mcp_server.threat_intel._cache import cache_get, cache_set, get_limiter

logger = logging.getLogger("blue_team_mcp.crowdsec")
_crowdsec_limiter = get_limiter("crowdsec", max_concurrent=3, min_interval=0.1)  # 10 req/sec


def _get_crowdsec_api_key() -> str:
    key = os.environ.get(CROWDSEC_API_KEY_ENV)
    if not key:
        raise RuntimeError(f"{CROWDSEC_API_KEY_ENV} not set. Get a free key at https://www.crowdsec.net/en/user/profile")
    return key


async def _crowdsec_request(path: str) -> dict[str, Any]:
    cached = cache_get("crowdsec", path)
    if cached is not None:
        return cached
    async with _crowdsec_limiter:
        headers = {"x-api-key": _get_crowdsec_api_key(), "accept": "application/json",
                   "User-Agent": "blue-team-mcp/1.0.0 (TangerangKota-CSIRT)"}
        url = f"{CROWDSEC_BASE_URL}{path}"
        resp = await _api_call("get", url, headers=headers)
        data = resp.json()
    cache_set("crowdsec", path, data, CROWDSEC_CACHE_TTL)
    return data


def _format_crowdsec_markdown(ip: str, raw: dict) -> str:
    lines = [f"# CrowdSec Reputation - {ip}", ""]
    lines.append(f"- **Reputation**: {raw.get('reputation', 'unknown')}")
    if raw.get("as_name"): lines.append(f"- **ASN**: {raw['as_name']}")
    for b in raw.get("behaviors") or []:
        lines.append(f"- **{b.get('name','?')}**{' - ' + b.get('label','') if b.get('label') else ''}")
    for m in raw.get("mitre_techniques") or []:
        lines.append(f"- MITRE: {m.get('name','?')} ({m.get('label','')})")
    return "\n".join(lines)


class CrowdsecIpReputationInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    ip: ValidPublicIp = Field(..., min_length=3, max_length=45)
    response_format: str = Field(default="markdown")


@mcp.tool(name="crowdsec_ip_reputation", annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True})
async def crowdsec_ip_reputation(params: CrowdsecIpReputationInput) -> str:
    _audit_log("crowdsec_ip_reputation", {"ip": params.ip})
    try:
        raw = await _crowdsec_request(f"/v2/smoke/{params.ip}")
    except (httpx.HTTPStatusError, httpx.TimeoutException, RuntimeError) as e:
        return _handle_api_error(e, context="crowdsec_ip_reputation")
    if params.response_format == "json":
        return json.dumps({"ip": params.ip, "reputation": raw.get("reputation","unknown"),
                           "behaviors": raw.get("behaviors",[]), "cves": raw.get("cves",[])}, indent=2)
    return _truncate_if_needed(_format_crowdsec_markdown(params.ip, raw))


class CrowdsecIpReputationBulkInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    ips: list[str] = Field(..., min_length=1, max_length=25)
    response_format: str = Field(default="markdown")

    @field_validator("ips")
    @classmethod
    def validate_ips(cls, v):
        import ipaddress
        for ip in v:
            try:
                addr = ipaddress.ip_address(ip.strip())
            except ValueError:
                raise ValueError(f"Invalid IP: {ip}")
            if addr.is_private:
                raise ValueError(f"'{ip.strip()}' is a private/reserved IP - bulk lookup accepts public IPs only.")
        return v


@mcp.tool(name="crowdsec_ip_reputation_bulk", annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True})
async def crowdsec_ip_reputation_bulk(params: CrowdsecIpReputationBulkInput) -> str:
    import asyncio
    _audit_log("crowdsec_ip_reputation_bulk", {"count": len(params.ips)})

    async def _lookup_one(ip: str) -> dict:
        try:
            raw = await _crowdsec_request(f"/v2/smoke/{ip.strip()}")
            return {"ip": ip, "reputation": raw.get("reputation","unknown"),
                    "behaviors": raw.get("behaviors",[]), "cves": raw.get("cves",[])}
        except Exception as e:
            return {"ip": ip, "error": _handle_api_error(e, context=ip)}

    results = await asyncio.gather(*[_lookup_one(ip) for ip in params.ips])
    if params.response_format == "json":
        return json.dumps(results, indent=2)
    lines = ["# CrowdSec Bulk Reputation", ""]
    for r in results:
        if "error" in r:
            lines.append(f"- **{r['ip']}** - ⚠️ {r['error']}")
        else:
            lines.append(f"- **{r['ip']}** - `{r['reputation']}`")
    return _truncate_if_needed("\n".join(lines))
