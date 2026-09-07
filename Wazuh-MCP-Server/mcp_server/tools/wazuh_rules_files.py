#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Wazuh Rule File tools - list rule files and retrieve raw XML content.

Exposes Wazuh Manager rule-file endpoints:
  - blueteam_wazuh_get_rule_files - list custom/loaded rule files
  - blueteam_wazuh_get_rule_file_content - raw XML content of a rule file

Useful for LLM-driven rule analysis, compliance auditing, and debugging
false positives by inspecting the exact rule logic.
NOTE: No ``from __future__ import annotations`` - required for @blueteam_tool, type resolution (see wazuh_siem.py for rationale).
"""

import json
from typing import Optional, Literal

from pydantic import BaseModel, ConfigDict, Field

from mcp_server.core.tool_decorator import blueteam_tool
from mcp_server.wazuh.auth import _wazuh_api_get


# blueteam_wazuh_get_rule_files - list rule files
class RuleFilesInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    filename: Optional[str] = Field(default=None, max_length=128,
                                     description="Filter by filename (comma-separated)")
    relative_dirname: Optional[str] = Field(default=None, max_length=256,
                                             description="Filter by relative directory")
    status: Optional[str] = Field(default=None,
                                   description="Filter: enabled, disabled, all")
    search: Optional[str] = Field(default=None, max_length=128)
    select: Optional[str] = Field(default=None, max_length=256)
    sort: Optional[str] = Field(default=None)
    q: Optional[str] = Field(default=None, max_length=256)
    distinct: bool = Field(default=False)
    limit: int = Field(default=50, ge=1, le=500)
    offset: int = Field(default=0, ge=0)
    response_format: Literal["markdown", "json"] = Field(default="markdown")


@blueteam_tool(name="blueteam_wazuh_get_rule_files")
async def blueteam_wazuh_get_rule_files(params: RuleFilesInput) -> str:
    """List Wazuh rule files loaded on the Manager.

    Returns filenames, status, and download paths.  Use
    ``blueteam_wazuh_get_rule_file_content`` to retrieve the raw XML.
    """
    api: dict[str, str] = {
        "limit": str(params.limit),
        "offset": str(params.offset),
    }
    if params.filename:          api["filename"] = params.filename
    if params.relative_dirname:  api["relative_dirname"] = params.relative_dirname
    if params.status:            api["status"] = params.status
    if params.search:            api["search"] = params.search
    if params.select:            api["select"] = params.select
    if params.sort:              api["sort"] = params.sort
    if params.q:                 api["q"] = params.q
    if params.distinct:          api["distinct"] = "true"

    data = await _wazuh_api_get("/rules/files", api)
    items = data.get("data", {}).get("affected_items", [])
    total = data.get("data", {}).get("total_affected_items", len(items))

    if params.response_format == "json":
        return json.dumps({
            "total": total,
            "files": items[:params.limit],
        }, indent=2)

    lines = [f"# Wazuh Rule Files ({len(items)})", ""]
    for f in items[:30]:
        name = f.get("filename", "?")
        status = f.get("status", "?")
        path = f.get("relative_dirname", "")
        full = f"{path}/{name}" if path else name
        lines.append(f"- `{full}` — status: {status}")
    return "\n".join(lines)


# blueteam_wazuh_get_rule_file_content - raw XML content
class RuleFileContentInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    filename: str = Field(..., min_length=1, max_length=256,
                           description="Rule filename, e.g. '0015-ossec_rules.xml'")
    raw: bool = Field(default=True,
                       description="When true, returns raw XML. When false, returns JSON metadata.")
    relative_dirname: Optional[str] = Field(default=None, max_length=256,
                                             description="Relative directory, e.g. 'rules' or 'etc/rules'")
    response_format: Literal["markdown", "json"] = Field(default="markdown")


@blueteam_tool(name="blueteam_wazuh_get_rule_file_content")
async def blueteam_wazuh_get_rule_file_content(params: RuleFileContentInput) -> str:
    """Retrieve the raw XML content of a Wazuh rule file.

    When ``raw=True`` (default), returns XML suitable for LLM analysis.
    When ``raw=False``, returns structured JSON metadata about the file.

    Use ``blueteam_wazuh_get_rule_files`` first to discover available filenames.
    """
    api: dict[str, str] = {}
    if params.raw:
        api["raw"] = "true"
    if params.relative_dirname:
        api["relative_dirname"] = params.relative_dirname

    data = await _wazuh_api_get(f"/rules/files/{params.filename}", api)

    if params.raw:
        # When raw=true, the API returns the XML as a 'content' key
        content = data.get("content", "") if isinstance(data, dict) else str(data)
        if params.response_format == "json":
            return json.dumps({
                "filename": params.filename,
                "raw": True,
                "content": content,
            }, indent=2)
        # Markdown: wrap in code block
        if len(content) > 50000:
            content = content[:50000] + "\n\n... [truncated — file exceeds 50KB]"
        return f"# Rule File: `{params.filename}`\n\n```xml\n{content}\n```"
    else:
        if params.response_format == "json":
            return json.dumps(data, indent=2)
        items = data.get("data", {}).get("affected_items", [data.get("data", data)])
        return json.dumps(items, indent=2)
