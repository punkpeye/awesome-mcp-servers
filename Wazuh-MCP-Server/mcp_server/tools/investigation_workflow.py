#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Investigation workflow tool - runs the langgraph SOC investigation end-to-end.
"""
from __future__ import annotations
import json, ipaddress
from typing import Literal, Optional
from pydantic import BaseModel, ConfigDict, Field, field_validator
from mcp_server import mcp
from mcp_server.core.audit import _audit_log, _truncate_if_needed
from mcp_server.core.redact import _redact_alert_data
from mcp_server.agents.investigation_graph import run_investigation


class InvestigationWorkflowInput(BaseModel):
    """Input model for blueteam_investigation_workflow."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    alert_text: Optional[str] = Field(default=None, max_length=100000,
        description="Raw alert text / full_log to start from. IOCs are extracted and recorded.")
    srcip: Optional[str] = Field(default=None, min_length=7, max_length=45,
        description="Source IP to investigate (enables 3-Sum + STIX kill-chain steps).")
    window: str = Field(default="24h", max_length=30,
        description="Time window for indexer steps ('24h', '7d', ISO 8601).")
    use_attack_graph: bool = Field(default=True,
        description="Run the 3-Sum correlation in graph mode: cluster-aware category "
                    "intersection (campaign-level APT detection), PPR suspicion boost, "
                    "and registry-confirmed IOC.")
    generate_report: bool = Field(default=False,
        description="Generate a .docx SOC report at the end (requires officecli + writable report_dir).")
    report_dir: str = Field(default="/tmp", max_length=200,
        description="Directory for the generated report (used when generate_report=true).")
    record_verdict: bool = Field(default=False,
        description="Record an investigation verdict for srcip (requires srcip + BLUETEAM_INVESTIGATION_HISTORY).")
    verdict_label: Literal["true_positive", "false_positive", "suspicious", "clean", "unknown"] = Field(
        default="suspicious", description="Verdict to record when record_verdict=true.")
    response_format: Literal["markdown", "json"] = Field(
        default="markdown", description="'markdown' (default) or 'json'.")

    @field_validator("srcip")
    @classmethod
    def validate_srcip(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        v = v.strip()
        try:
            ipaddress.ip_address(v)
        except ValueError:
            raise ValueError(f"Invalid IP address: '{v}'") from None
        return v

    @field_validator("alert_text")
    @classmethod
    def require_target(cls, v: Optional[str], info):
        """At least one target required: alert_text or srcip."""
        srcip = info.data.get("srcip")
        if not v and not srcip:
            raise ValueError("Provide either 'alert_text' or 'srcip' to start an investigation.")
        return v


@mcp.tool(
    name="blueteam_investigation_workflow",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": False},
)
async def blueteam_investigation_workflow(params: InvestigationWorkflowInput) -> str:
    """Run the full SOC investigation workflow (langgraph) end-to-end.

    Orchestrates the platform's analyzers as a stateful graph:
    extract IOCs -> threat-intel enrichment -> 3-Sum correlation -> attack graph ->
    STIX kill-chain (if srcip) -> baseline drift (if 3-Sum flagged) -> optional
    report + verdict. Steps without required credentials degrade gracefully and
    are reported in `errors`.

    **Worked Examples**

    1. *Triage an alert log line*:
       ``blueteam_investigation_workflow(alert_text="srcip=103.166.210.53 url=http://evil.com/x")``

    2. *Full IP investigation, 7-day window*:
       ``blueteam_investigation_workflow(srcip="185.220.101.1", window="7d")``

    3. *Investigate + generate a report + record verdict*:
       ``blueteam_investigation_workflow(srcip="103.107.116.202", generate_report=true, record_verdict=true, verdict_label="suspicious")``
    """
    _audit_log("blueteam_investigation_workflow", {"srcip": params.srcip, "window": params.window})
    result = await run_investigation(
        alert_text=params.alert_text,
        srcip=params.srcip,
        window=params.window,
        use_attack_graph=params.use_attack_graph,
        generate_report=params.generate_report,
        report_dir=params.report_dir,
        record_verdict=params.record_verdict,
        verdict_label=params.verdict_label,
    )
    if params.response_format == "json":
        return _truncate_if_needed(json.dumps(_redact_alert_data(result), indent=2, ensure_ascii=False))

    lines = [f"# 🔎 Investigation Workflow — `{params.srcip or 'alert'}`", "",
             "| Step | Status |", "|------|--------|"]
    for s in result.get("steps", []):
        status = "⚠️" if "degraded" in s or "failed" in s else "✅"
        lines.append(f"| {status} | {s} |")
    if result.get("errors"):
        lines.append("")
        lines.append("## Degraded / Failed Steps")
        for e in result["errors"]:
            lines.append(f"- ⚠️ `{e}`")
    corr = result.get("correlation")
    if corr:
        lines += ["", "## 3-Sum Correlation",
                  f"- **Engine A triggers**: {corr.get('engine_a_triggers', 0)}",
                  f"- **Engine B anomalies**: {corr.get('engine_b_anomalies', 0)}",
                  f"- **Severity**: {corr.get('severity', 'NONE')}"]
    if result.get("attack_graph"):
        ag = result["attack_graph"].get("graph", {})
        lines += ["", "## Attack Graph",
                  f"- **Nodes**: {ag.get('num_nodes', 0)} | **Edges**: {ag.get('num_edges', 0)} | "
                  f"**Campaign clusters**: {ag.get('num_components', 0)}"]
    if result.get("killchain"):
        lines += ["", f"## STIX Kill Chain — tactics: {', '.join(result['killchain'])}"]
    if result.get("report_path"):
        lines += ["", f"📄 **Report**: `{result['report_path']}`"]
    if result.get("verdict"):
        lines += ["", f"⚖️ **Verdict**: `{result['verdict'].get('status')}`"]
    return _truncate_if_needed("\n".join(lines))
