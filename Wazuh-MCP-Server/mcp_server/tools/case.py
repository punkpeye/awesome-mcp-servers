#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Case management create, update, and query durable incident records.
A case groups a whole campaign/incident: srcips, IOCs, and analyst verdicts.
Populate it from `three_sum_correlation` triggers, `blueteam_pivot_suggest`
leads, and `blueteam_mark_investigated` verdicts so an investigation survives beyond a single tool call.
"""
from __future__ import annotations
import json
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field, field_validator
from mcp_server import mcp
from mcp_server.core.audit import _audit_log, _truncate_if_needed
from mcp_server.core.redact import _redact_alert_data
from mcp_server.core import case_store


class CaseCreateInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    title: str = Field(..., min_length=1, max_length=200, description="Case title.")
    srcips: list[str] = Field(default=[], max_length=200,
        description="Source IPs to seed the case with.")
    notes: str = Field(default="", max_length=2000, description="Analyst notes.")


class CaseAddIocsInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    case_id: str = Field(..., min_length=5, max_length=64)
    iocs: list[str] = Field(..., min_length=1, max_length=500,
        description="IOCs (IPs/domains/hashes) to attach.")


class CaseAddVerdictInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    case_id: str = Field(..., min_length=5, max_length=64)
    srcip: str = Field(..., min_length=7, max_length=45)
    verdict: Literal["true_positive", "false_positive", "suspicious", "clean", "unknown"]
    notes: str = Field(default="", max_length=500)


class CaseGetInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    case_id: str = Field(..., min_length=5, max_length=64)
    response_format: Literal["markdown", "json"] = Field(default="markdown")


class CaseListInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    response_format: Literal["markdown", "json"] = Field(default="markdown")


@mcp.tool(
    name="blueteam_case_create",
    annotations={"readOnlyHint": False, "destructiveHint": False,
                 "idempotentHint": False, "openWorldHint": False},
)
async def blueteam_case_create(params: CaseCreateInput) -> str:
    """Create a new investigation case (durable incident record).

    **Worked Examples**
    1. ``blueteam_case_create(title="APT campaign 2026-08", srcips=["103.107.116.202"])``
    """
    _audit_log("blueteam_case_create", {"title": params.title})
    case = case_store.create_case(params.title, params.srcips, params.notes)
    return json.dumps(case, indent=2, ensure_ascii=False)


@mcp.tool(
    name="blueteam_case_add_iocs",
    annotations={"readOnlyHint": False, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": False},
)
async def blueteam_case_add_iocs(params: CaseAddIocsInput) -> str:
    """Attach IOC to an existing case.
    **Worked Examples**
    1. ``blueteam_case_add_iocs(case_id="case_abc123", iocs=["evil.com", "d41d8cd98f00..."])``
    """
    _audit_log("blueteam_case_add_iocs", {"case_id": params.case_id})
    case = case_store.add_iocs(params.case_id, params.iocs)
    if not case:
        return json.dumps({"error": f"Case '{params.case_id}' not found."}, indent=2)
    return json.dumps({"case_id": params.case_id, "iocs": case["iocs"]}, indent=2, ensure_ascii=False)


@mcp.tool(
    name="blueteam_case_add_verdict",
    annotations={"readOnlyHint": False, "destructiveHint": False,
                 "idempotentHint": False, "openWorldHint": False},
)
async def blueteam_case_add_verdict(params: CaseAddVerdictInput) -> str:
    """Record an investigation verdict against a srcip within a case.

    **Worked Examples**
    1. ``blueteam_case_add_verdict(case_id="case_abc123", srcip="103.107.116.202", verdict="true_positive")``
    """
    _audit_log("blueteam_case_add_verdict", {"case_id": params.case_id, "srcip": params.srcip})
    case = case_store.add_verdict(params.case_id, params.srcip, params.verdict, params.notes)
    if not case:
        return json.dumps({"error": f"Case '{params.case_id}' not found."}, indent=2)
    return json.dumps({"case_id": params.case_id, "verdicts": case["verdicts"]}, indent=2, ensure_ascii=False)


@mcp.tool(
    name="blueteam_case_get",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": False},
)
async def blueteam_case_get(params: CaseGetInput) -> str:
    """Fetch a case by ID, with all its IOCs and verdicts.

    **Worked Examples**
    1. ``blueteam_case_get(case_id="case_abc123")``
    """
    _audit_log("blueteam_case_get", {"case_id": params.case_id})
    case = case_store.get_case(params.case_id)
    if not case:
        return json.dumps({"error": f"Case '{params.case_id}' not found."}, indent=2)
    if params.response_format == "json":
        return _truncate_if_needed(json.dumps(_redact_alert_data(case), indent=2, ensure_ascii=False))
    lines = [f"# 🗂️ Case — `{case['case_id']}`", "", f"**Title**: {case['title']}",
             f"**Created**: {case['created_at']}", f"**Updated**: {case['updated_at']}",
             f"**SrcIPs**: {', '.join('`' + i + '`' for i in case.get('srcips', [])) or '—'}",
             f"**IOCs**: {', '.join('`' + i + '`' for i in case.get('iocs', [])) or '—'}", ""]
    if case.get("notes"):
        lines += ["## Notes", case["notes"], ""]
    if case.get("verdicts"):
        lines.append("## Verdicts")
        for v in case["verdicts"]:
            lines.append(f"- `{v['srcip']}` — **{v['verdict']}**" +
                         (f" ({v['notes']})" if v.get("notes") else ""))
        lines.append("")
    timeline = case_store.case_timeline(case["case_id"])
    if timeline:
        lines.append("## Timeline")
        for e in timeline:
            ts = (e.get("ts") or "?")[:19]
            if e["event"] == "case_created":
                lines.append(f"- `{ts}` 🗂️ Case created - {e.get('detail','')}")
            else:
                lines.append(f"- `{ts}` `{e['srcip']}` -> **{e['verdict']}**" +
                             (f" ({e['detail']})" if e.get("detail") else ""))
    return _truncate_if_needed("\n".join(lines))


@mcp.tool(
    name="blueteam_case_list",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": False},
)
async def blueteam_case_list(params: CaseListInput) -> str:
    """List all cases (most recent first).

    **Worked Examples**
    1. ``blueteam_case_list()``
    """
    _audit_log("blueteam_case_list", {})
    cases = case_store.list_cases()
    if params.response_format == "json":
        return _truncate_if_needed(json.dumps(
            _redact_alert_data([{k: c[k] for k in ("case_id", "title", "created_at", "srcips", "iocs")
                                 if k in c} for c in cases]), indent=2, ensure_ascii=False))
    lines = ["# 🗂️ Cases", ""]
    if not cases:
        lines.append("*No cases yet.*")
    for c in cases[:50]:
        lines.append(f"- `{c['case_id']}` - {c['title']} "
                     f"({len(c.get('srcips', []))} srcips, {len(c.get('iocs', []))} IOCs)")
    return _truncate_if_needed("\n".join(lines))
