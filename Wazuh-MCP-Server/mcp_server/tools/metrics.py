#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Prometheus /metrics resource - exposes blue-team-mcp telemetry in Prometheus
text exposition format via the `metrics://prometheus` MCP resource.
"""
from __future__ import annotations
import json
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field
from mcp_server import mcp
from mcp_server.core.metrics import render_prometheus, snapshot
from mcp_server.core.audit import _audit_log, _truncate_if_needed


@mcp.resource("metrics://prometheus")
async def prometheus_metrics() -> str:
    """Prometheus text exposition of server telemetry.
    Counter/gauge families:
      - blue_team_mcp_tool_calls_total{tool}        - audit-path call counters
      - blue_team_mcp_pipeline_calls_total{tool}    - response_pipeline executions
      - blue_team_mcp_pipeline_duration_ms_total{tool}
      - blue_team_mcp_redaction_gate_failures_total - forensic bypass rejections
      - blue_team_mcp_rate_limit_hits_total
      - blue_team_mcp_attacker_registry_entries     - gauge
      - blue_team_mcp_ioc_store_entries             - gauge
    Consumable directly by Prometheus (text/plain; version=0.0.4) or via the
    JSON snapshot at `metrics://prometheus/json`.
    """
    return render_prometheus()


@mcp.resource("metrics://prometheus/json")
async def prometheus_metrics_json() -> str:
    """JSON snapshot of server telemetry (machine-readable variant)."""
    import json
    return json.dumps(snapshot(), indent=2, ensure_ascii=False)


class MetricsInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    response_format: Literal["markdown", "json"] = Field(default="markdown")


@mcp.tool(
    name="blueteam_metrics",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": False},
)
async def blueteam_metrics(params: MetricsInput) -> str:
    """Show server telemetry per-tool call counts, latency, and guard counters.
    Surfaces the same data as the `metrics://prometheus` resource in a form the
    LLM can read directly: top tools by call count, top tools by cumulative
    latency, and redaction-gate / rate-limit rejections. Use it to find slow or
    hot tools from inside a conversation.
    **Worked Examples**
    1. ``blueteam_metrics()``
    2. ``blueteam_metrics(response_format="json")``
    """
    _audit_log("blueteam_metrics", {})
    snap = snapshot()
    if params.response_format == "json":
        return json.dumps(snap, indent=2, ensure_ascii=False)

    calls = snap.get("tool_calls", {})
    durations = snap.get("pipeline", {}).get("duration_ms_total", {})
    lines = ["# 📊 Server Metrics", "",
             f"- **Redaction gate failures**: {snap.get('redaction_gate_failures', 0)}",
             f"- **Rate-limit hits**: {snap.get('rate_limit_hits', 0)}", ""]
    if calls:
        lines.append("## Top Tools by Calls")
        for tool, n in sorted(calls.items(), key=lambda kv: -kv[1])[:10]:
            lines.append(f"- `{tool}` - {n}")
        lines.append("")
    if durations:
        lines.append("## Top Tools by Cumulative Latency")
        for tool, ms in sorted(durations.items(), key=lambda kv: -kv[1])[:10]:
            lines.append(f"- `{tool}` - {ms:.0f} ms")
    if not calls and not durations:
        lines.append("*No tool calls recorded yet.*")
    return _truncate_if_needed("\n".join(lines))
