#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Alert-driven playbook runner - langgraph supervisor dispatching hunts + investigations.
"""
from __future__ import annotations
import json
from typing import Literal, Optional
from pydantic import BaseModel, ConfigDict, Field, model_validator
from mcp_server import mcp
from mcp_server.core.audit import _audit_log, _truncate_if_needed
from mcp_server.core.redact import _redact_alert_data
from mcp_server.agents.playbook_graph import run_playbook, _THREAT_HUNT_TEMPLATES


class PlaybookRunInput(BaseModel):
    """Input model for blueteam_playbook_run."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    alert_text: Optional[str] = Field(default=None, max_length=100000,
        description="Raw alert text / full_log to start from.")
    rule_id: Optional[str] = Field(default=None, max_length=16,
        description="Wazuh rule ID that fired (used for playbook selection context).")
    technique: Optional[str] = Field(default=None, max_length=20,
        description="MITRE technique ID (e.g. T1059.001) — drives template selection.")
    rule_groups: Optional[str] = Field(default=None, max_length=200,
        description="Comma-separated rule groups (e.g. 'powershell,sysmon') - drives template selection.")
    srcip: Optional[str] = Field(default=None, min_length=7, max_length=45,
        description="Known source IP (overrides hunt-picked srcip when provided).")
    template_name: Optional[str] = Field(default=None, max_length=40,
        description="Explicit threat-hunt template to run. One of: "
                    f"{', '.join(sorted(_THREAT_HUNT_TEMPLATES))}.")
    window: str = Field(default="24h", max_length=30,
        description="Time window for hunt + investigation steps.")
    use_attack_graph: bool = Field(default=True,
        description="Run the 3-Sum correlation in graph mode (cluster-aware APT detection, "
                    "PPR suspicion boost, confirmed-IOC).")
    generate_report: bool = Field(default=False,
        description="Generate a .docx SOC report at the end.")
    report_dir: str = Field(default="/tmp", max_length=200,
        description="Directory for the generated report.")
    record_verdict: bool = Field(default=False,
        description="Record an investigation verdict for the selected srcip.")
    verdict_label: Literal["true_positive", "false_positive", "suspicious", "clean", "unknown"] = Field(
        default="suspicious", description="Verdict to record when record_verdict=true.")
    response_format: Literal["markdown", "json"] = Field(
        default="markdown", description="'markdown' (default) or 'json'.")

    @model_validator(mode="after")
    def require_target(self):
        if not any([self.alert_text, self.rule_id, self.technique,
                    self.rule_groups, self.srcip, self.template_name]):
            raise ValueError("Provide at least one of: alert_text, rule_id, technique, "
                             "rule_groups, srcip, template_name.")
        return self


@mcp.tool(
    name="blueteam_playbook_run",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": False},
)
async def blueteam_playbook_run(params: PlaybookRunInput) -> str:
    """Run an alert-driven hunting + investigation playbook (langgraph supervisor).

    Selects the matching threat-hunt template from the alert context (MITRE
    technique > rule groups > explicit template > fallback), runs the hunt,
    picks the top source IP, retries once with the generic c2_beacon template
    if the targeted hunt finds nothing, then dispatches the full G2 investigation
    workflow (extract -> enrich -> correlate -> attack graph -> kill-chain -> baseline
    -> report/verdict). Degraded steps are reported, never silent.

    **Worked Examples**

    1. *Investigate a PowerShell alert*:
       ``blueteam_playbook_run(rule_groups="powershell,sysmon", window="7d")``

    2. *Technique-driven hunt*:
       ``blueteam_playbook_run(technique="T1059.001", window="24h")``

    3. *Explicit template + report + verdict*:
       ``blueteam_playbook_run(template_name="c2_beacon", generate_report=true, record_verdict=true)``
    """
    _audit_log("blueteam_playbook_run", {"rule_id": params.rule_id,
                                         "technique": params.technique,
                                         "template_name": params.template_name})
    result = await run_playbook(
        alert_text=params.alert_text,
        rule_id=params.rule_id,
        technique=params.technique,
        rule_groups=params.rule_groups,
        srcip=params.srcip,
        template_name=params.template_name,
        window=params.window,
        use_attack_graph=params.use_attack_graph,
        generate_report=params.generate_report,
        report_dir=params.report_dir,
        record_verdict=params.record_verdict,
        verdict_label=params.verdict_label,
    )
    if params.response_format == "json":
        return _truncate_if_needed(json.dumps(_redact_alert_data(result), indent=2, ensure_ascii=False))

    lines = [f"# 🎯 Playbook Run — `{result.get('template')}`", "",
             "| Step | Status |", "|------|--------|"]
    for s in result.get("steps", []):
        status = "⚠️" if "degraded" in s or "failed" in s else "✅"
        lines.append(f"| {status} | {s} |")
    if result.get("hunt_total_alerts") is not None:
        lines += ["", "## Hunt",
                  f"- **Template**: `{result.get('template')}`",
                  f"- **Matching alerts**: {result['hunt_total_alerts']}",
                  f"- **Source IPs**: {', '.join(result.get('hunt_srcips', [])) or 'none'}",
                  f"- **Selected**: `{result.get('selected_srcip') or '—'}`"]
    inv = result.get("investigation")
    if inv:
        lines += ["", "## Investigation"]
        for s in inv.get("steps", []):
            lines.append(f"- {s}")
        if inv.get("errors"):
            lines.append("")
            lines.append("### Degraded")
            for e in inv["errors"]:
                lines.append(f"- ⚠️ `{e}`")
    if result.get("errors"):
        lines += ["", "## Playbook Errors"]
        for e in result["errors"]:
            lines.append(f"- ⚠️ `{e}`")
    return _truncate_if_needed("\n".join(lines))
