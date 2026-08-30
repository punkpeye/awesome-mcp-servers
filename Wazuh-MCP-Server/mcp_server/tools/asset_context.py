#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
CMDB asset context - answers "what is this asset, how critical, who owns it".
Reads a JSON inventory file (BLUETEAM_CMDB_FILE) that operators maintain.
When the LLM sees an attacker targeting a subdomain, this tool gives the
internal context needed to prioritize response.

File format (JSON array):
[
  {
    "host": "csirt.tangerangkota.go.id",
    "name": "CSIRT Portal",
    "owner": "Dinas Komunikasi",
    "criticality": "high",       # high | medium | low
    "environment": "production", # production | staging | dev
    "purpose": "Public information portal"
  },
  ...
]
"""
from __future__ import annotations
import json, os
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field
from mcp_server import mcp
from mcp_server.core.audit import _audit_log, _truncate_if_needed

_CMDB_FILE = os.environ.get("BLUETEAM_CMDB_FILE", "")

_CMDB_CACHE: dict[str, list[dict]] = {}
_CMDB_CACHE_MTIME: float = 0.0


def _load_cmdb() -> list[dict]:
    """Load the CMDB inventory file (cached by mtime)."""
    global _CMDB_CACHE, _CMDB_CACHE_MTIME
    if not _CMDB_FILE:
        return []
    try:
        mtime = os.path.getmtime(_CMDB_FILE)
        if _CMDB_CACHE and mtime == _CMDB_CACHE_MTIME:
            return _CMDB_CACHE
        with open(_CMDB_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            return []
        _CMDB_CACHE = data
        _CMDB_CACHE_MTIME = mtime
        return data
    except (OSError, ValueError):
        return []


def _find_asset(host: str) -> dict | None:
    """Find an asset by exact host match, then subdomain/suffix match."""
    assets = _load_cmdb()
    host_l = (host or "").strip().lower()
    if not host_l:
        return None
    # Exact match first
    for a in assets:
        if (a.get("host", "") or "").lower() == host_l:
            return a
    # Subdomain match: csirt.tangerangkota.go.id matches tangerangkota.go.id
    for a in assets:
        ah = (a.get("host", "") or "").lower()
        if ah and (host_l == ah or host_l.endswith("." + ah)):
            return a
    return None


class AssetContextInput(BaseModel):
    """Input model for blueteam_asset_context."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    host: str = Field(
        ..., min_length=3, max_length=256,
        description="Hostname/subdomain to look up, e.g. 'ppid.tangerangkota.go.id'.",
    )
    response_format: Literal["markdown", "json"] = Field(default="markdown")


@mcp.tool(
    name="blueteam_asset_context",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": False},
)
async def blueteam_asset_context(params: AssetContextInput) -> str:
    """Look up internal asset context for a hostname/subdomain.

    Answers "what is this asset, how critical is it, who owns it" — essential
    context when an attacker is targeting a subdomain. Reads from
    ``BLUETEAM_CMDB_FILE`` (a JSON inventory you maintain).

    **Required Permissions**: Set ``BLUETEAM_CMDB_FILE`` to a JSON file path.

    **Worked Examples**

    1. *Get context for an attacked subdomain*:
       ``blueteam_asset_context(host="ppid.tangerangkota.go.id")``

    2. *JSON output*:
       ``blueteam_asset_context(host="ppid.tangerangkota.go.id", response_format="json")``
    """
    _audit_log("blueteam_asset_context", {"host": params.host})

    if not _CMDB_FILE:
        return json.dumps({
            "error": "BLUETEAM_CMDB_FILE not set.",
            "detail": "Set it to a JSON file path containing your subdomain inventory.",
        }, indent=2)

    asset = _find_asset(params.host)

    if asset is None:
        if params.response_format == "json":
            return json.dumps({"host": params.host, "found": False}, indent=2)
        return f"# Asset Context — `{params.host}`\n\n_No asset found in CMDB. Add it to {_CMDB_FILE}._"

    if params.response_format == "json":
        return json.dumps({"host": params.host, "found": True, "asset": asset}, indent=2)

    lines = [f"# Asset Context - `{params.host}`", ""]
    lines.append(f"| Field | Value |")
    lines.append(f"|-------|-------|")
    lines.append(f"| Name | **{asset.get('name', '?')}** |")
    lines.append(f"| Owner | {asset.get('owner', '?')} |")
    lines.append(f"| Criticality | **{asset.get('criticality', '?')}** |")
    lines.append(f"| Environment | {asset.get('environment', '?')} |")
    if asset.get("purpose"):
        lines.append(f"| Purpose | {asset['purpose']} |")
    return _truncate_if_needed("\n".join(lines))
