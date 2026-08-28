#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
GreyNoise Community API - free, no key required.
"""
from __future__ import annotations
import json
from pydantic import BaseModel, ConfigDict, Field
from typing import Literal
import httpx
from mcp_server import mcp, GREYNOISE_COMMUNITY_BASE_URL
from mcp_server.core.http_client import _api_call, ValidPublicIp
from mcp_server.core.audit import _audit_log, _truncate_if_needed


class GreyNoiseContextInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    ip: ValidPublicIp = Field(..., description="Public IP to check against GreyNoise Community")
    response_format: Literal["markdown", "json"] = Field(default="markdown", description="'markdown' or 'json'")


@mcp.tool(name="greynoise_ip_context", annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True})
async def greynoise_ip_context(params: GreyNoiseContextInput) -> str:
    """Check if an IP is a known internet scanner or business service (free, no auth).

    Args:
        params.ip: Public IP to check
        params.response_format: 'markdown' or 'json'
    """
    _audit_log("greynoise_ip_context", {"ip": params.ip})
    headers = {"accept": "application/json", "User-Agent": "blue-team-mcp/1.0.0"}
    try:
        resp = await _api_call("get", f"{GREYNOISE_COMMUNITY_BASE_URL}/{params.ip}", headers=headers)
        raw = resp.json()
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raw = {"ip": params.ip, "noise": False, "riot": False,
                   "classification": "unknown", "message": "No data in GreyNoise Community dataset"}
        else:
            raise
    if params.response_format == "json":
        return _truncate_if_needed(json.dumps(raw, indent=2))
    lines = [f"# GreyNoise Community - {params.ip}", "",
             f"- **Noise**: {'Yes' if raw.get('noise') else 'No'}",
             f"- **RIOT**: {'Yes' if raw.get('riot') else 'No'}",
             f"- **Classification**: `{raw.get('classification','unknown')}`"]
    return _truncate_if_needed("\n".join(lines))
