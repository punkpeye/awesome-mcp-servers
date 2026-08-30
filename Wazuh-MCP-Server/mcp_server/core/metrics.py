#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Prometheus /metrics instrumentation - zero-dependency counters.

Instrumented choke points (one line each):
  - _audit_log()                     -> tool call counters (all audited tools)
  - response_pipeline()              -> per-tool duration (pipeline tools)
  - _redact_alert_data() gate raise  -> forensic-bypass rejections
  - _check_rate_limit() hit          -> rate-limit rejections

Rendered by the `metrics://prometheus` MCP resource in tools/metrics.py.
"""
from __future__ import annotations
import threading

_calls: dict[str, int] = {}
_durations: dict[str, float] = {}   # {tool: total_ms}
_pipeline_calls: dict[str, int] = {}
_gate_failures = 0
_rate_limit_hits = 0
_lock = threading.Lock()


def record_call(tool: str) -> None:
    """Increment the call counter for a tool (audit path)."""
    with _lock:
        _calls[tool] = _calls.get(tool, 0) + 1


def record_timing(tool: str, duration_ms: float) -> None:
    """Record a completed pipeline execution duration."""
    with _lock:
        _durations[tool] = _durations.get(tool, 0.0) + duration_ms
        _pipeline_calls[tool] = _pipeline_calls.get(tool, 0) + 1


def record_gate_failure() -> None:
    global _gate_failures
    with _lock:
        _gate_failures += 1


def record_rate_limit_hit() -> None:
    global _rate_limit_hits
    with _lock:
        _rate_limit_hits += 1


def snapshot() -> dict:
    """JSON-safe snapshot (used by the metrics resource + tests)."""
    with _lock:
        return {
            "tool_calls": dict(_calls),
            "pipeline": {
                "tools": dict(_pipeline_calls),
                "duration_ms_total": dict(_durations),
            },
            "redaction_gate_failures": _gate_failures,
            "rate_limit_hits": _rate_limit_hits,
        }


def _q(name: str) -> str:
    """Escape a Prometheus label value."""
    return name.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")


def render_prometheus() -> str:
    """Render the Prometheus text exposition format."""
    with _lock:
        lines = [
            "# HELP blue_team_mcp_tool_calls_total Tool calls recorded via the audit path.",
            "# TYPE blue_team_mcp_tool_calls_total counter",
        ]
        for tool, n in sorted(_calls.items()):
            lines.append(f'blue_team_mcp_tool_calls_total{{tool="{_q(tool)}"}} {n}')
        lines += [
            "# HELP blue_team_mcp_pipeline_calls_total response_pipeline tool executions.",
            "# TYPE blue_team_mcp_pipeline_calls_total counter",
        ]
        for tool, n in sorted(_pipeline_calls.items()):
            lines.append(f'blue_team_mcp_pipeline_calls_total{{tool="{_q(tool)}"}} {n}')
        lines += [
            "# HELP blue_team_mcp_pipeline_duration_ms_total Cumulative pipeline execution time.",
            "# TYPE blue_team_mcp_pipeline_duration_ms_total counter",
        ]
        for tool, ms in sorted(_durations.items()):
            lines.append(f'blue_team_mcp_pipeline_duration_ms_total{{tool="{_q(tool)}"}} {ms:.1f}')
        lines.append("# HELP blue_team_mcp_redaction_gate_failures_total Forensic bypass attempts rejected.")
        lines.append("# TYPE blue_team_mcp_redaction_gate_failures_total counter")
        lines.append(f"blue_team_mcp_redaction_gate_failures_total {_gate_failures}")
        lines.append("# HELP blue_team_mcp_rate_limit_hits_total Rate-limit rejections.")
        lines.append("# TYPE blue_team_mcp_rate_limit_hits_total counter")
        lines.append(f"blue_team_mcp_rate_limit_hits_total {_rate_limit_hits}")

    # registry / store sizes (imported lazily to avoid import cycles)
    try:
        from mcp_server.core.attacker_registry import registry_stats as _reg_stats
        lines.append("# HELP blue_team_mcp_attacker_registry_entries Registered attacker IOCs.")
        lines.append("# TYPE blue_team_mcp_attacker_registry_entries gauge")
        lines.append(f"blue_team_mcp_attacker_registry_entries {_reg_stats()['entries']}")
    except Exception:
        pass
    try:
        from mcp_server.core.ioc_store import ioc_stats as _ioc_stats
        lines.append("# HELP blue_team_mcp_ioc_store_entries Recorded IOC lifecycle entries.")
        lines.append("# TYPE blue_team_mcp_ioc_store_entries gauge")
        lines.append(f"blue_team_mcp_ioc_store_entries {_ioc_stats()['entries']}")
    except Exception:
        pass
    return "\n".join(lines) + "\n"
