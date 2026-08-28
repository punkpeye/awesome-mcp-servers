#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Investigation history + false positive tracker + summary tools
"""
from __future__ import annotations
import json, os
from datetime import datetime, timedelta
from typing import Optional, Literal
from collections import Counter
from pydantic import field_validator, BaseModel, ConfigDict, Field
from mcp_server import (mcp, _INVESTIGATION_HISTORY_FILE)
from mcp_server.core.audit import _audit_log, _truncate_if_needed
from mcp_server.core.attacker_registry import register_attacker_ioc
from mcp_server.core.false_positive_kb import (register_false_positive,
    false_positive_iocs, false_positive_stats, is_false_positive)
from mcp_server.core import case_store

_INVESTIGATION_HISTORY_MAX_ENTRIES = int(os.environ.get("BLUETEAM_INVESTIGATION_HISTORY_MAX_ENTRIES", "10000"))


class MarkInvestigatedInput(BaseModel):
    """Input model for blueteam_mark_investigated."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    srcip: str = Field(..., min_length=7, max_length=45,
        description="Source IP being investigated.")
    verdict: Literal["true_positive", "false_positive", "suspicious", "clean", "unknown"] = Field(
        ..., description="Investigation verdict.")
    notes: str = Field(default="", max_length=1024,
        description="Analyst notes (max 1024 chars).")
    case_id: str = Field(default="", max_length=64,
        description="Optional case ID - if set, this verdict is also recorded on that case.")


@mcp.tool(
    name="blueteam_mark_investigated",
    annotations={"readOnlyHint": False, "destructiveHint": False,
                 "idempotentHint": False, "openWorldHint": False},
)
async def blueteam_mark_investigated(params: MarkInvestigatedInput) -> str:
    """Record an IP investigation verdict in the persistent JSONL history.
    Appends a timestamped entry to BLUETEAM_INVESTIGATION_HISTORY. This is the
    only tool that writes investigation state - all other tools (curated reports,
    threat cards, beacon detection) are read-only.

    **Required**: BLUETEAM_INVESTIGATION_HISTORY env var set to a writable path.

    **Worked Examples**

    1. *Mark malicious*:
       ``blueteam_mark_investigated(srcip="103.107.116.202", verdict="true_positive", notes="CrowdSec confirmed - C2 beaconing")``

    2. *Mark false positive*:
       ``blueteam_mark_investigated(srcip="8.8.8.8", verdict="false_positive", notes="Google DNS - scanner noise")``
    """
    _audit_log("blueteam_mark_investigated", {"srcip": params.srcip, "verdict": params.verdict})
    if params.verdict == "true_positive":
        register_attacker_ioc(params.srcip, source="verdict")  # confirmed attacker - keep IOC unmasked
    if params.verdict == "false_positive":
        register_false_positive(params.srcip, source="verdict", reason=params.notes)  # auto-suppress in 3-Sum
    if params.case_id:
        case_store.add_verdict(params.case_id, params.srcip, params.verdict, params.notes)  # P8: case wiring
    if not _INVESTIGATION_HISTORY_FILE:
        return json.dumps({"error": "BLUETEAM_INVESTIGATION_HISTORY env var not set.",
                           "detail": "Set this to a writable JSONL file path for investigation persistence."}, indent=2)
    entry = {
        "ts": datetime.utcnow().isoformat() + "Z",
        "srcip": params.srcip.strip(),
        "verdict": params.verdict,
        "notes": params.notes[:1024],
    }
    if not _append_history(entry):
        return json.dumps({"error": "Failed to write history file.",
                           "detail": f"Check {_INVESTIGATION_HISTORY_FILE} is writable."}, indent=2)
    return json.dumps({"status": "recorded", "entry": entry}, indent=2)


class FalsePositiveTrackerInput(BaseModel):
    """Input model for blueteam_false_positive_tracker."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    rule_id: str = Field(..., max_length=16,
        description="Wazuh rule ID to check, e.g. '600029'.")
    since: Optional[str] = Field(default="30d", max_length=30,
        description="Time window. ISO 8601 or relative ('7d', '30d').")
    response_format: Literal["markdown", "json"] = Field(
        default="markdown", description="'markdown' or 'json'.")


@mcp.tool(
    name="blueteam_false_positive_tracker",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": False},
)
async def blueteam_false_positive_tracker(params: FalsePositiveTrackerInput) -> str:
    """Count how often a Wazuh rule fired but was later marked false-positive.

    Parses BLUETEAM_INVESTIGATION_HISTORY to find IPs investigated with
    verdict="false_positive", then cross-references rule_id from investigation
    summaries. Helps SOC tune noisy Wazuh rules.

    **Worked Examples**

    1. *Check rule 600029*:
       ``blueteam_false_positive_tracker(rule_id="600029", since="30d")``
    """
    _audit_log("blueteam_false_positive_tracker", {"rule_id": params.rule_id})
    if not _INVESTIGATION_HISTORY_FILE:
        return json.dumps({"error": "BLUETEAM_INVESTIGATION_HISTORY not set."}, indent=2)
    since_dt = datetime.utcnow() - timedelta(days=30 if params.since == "30d" else 7)
    history = _read_history()
    fp_ips = {ip for ip, e in history.items()
              if e.get("verdict") == "false_positive"
              and e.get("ts", "") >= since_dt.strftime("%Y-%m-%d")}
    # Cross-reference: count rule_id mentions in FP summaries
    fp_count = 0
    fp_ips_list: list[str] = []
    for ip, e in history.items():
        if ip not in fp_ips:
            continue
        summary = e.get("summary", {})
        rules = summary.get("rules", [])
        if isinstance(rules, list):
            for r in rules:
                if isinstance(r, dict) and str(r.get("id", "")) == params.rule_id:
                    fp_count += 1
                    fp_ips_list.append(ip)
                    break
    if params.response_format == "json":
        return json.dumps({"rule_id": params.rule_id, "false_positive_count": fp_count,
                           "ips": fp_ips_list[:50]}, indent=2)
    return (f"# False Positive Tracker — Rule `{params.rule_id}`\n\n"
            f"- **False positive verdicts**: {fp_count}\n"
            f"- **IPs flagged**: {', '.join(f'`{ip}`' for ip in fp_ips_list[:10]) if fp_ips_list else 'none'}\n"
            f"- **Window**: since {since_dt.strftime('%Y-%m-%d')}\n")


class InvestigationSummaryInput(BaseModel):
    """Input model for blueteam_investigation_summary."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    since: Optional[str] = Field(default="7d", max_length=30,
        description="Time window. ISO 8601 or relative.")
    response_format: Literal["markdown", "json"] = Field(
        default="markdown", description="'markdown' or 'json'.")


@mcp.tool(
    name="blueteam_investigation_summary",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": False},
)
async def blueteam_investigation_summary(params: InvestigationSummaryInput) -> str:
    """Dashboard: unique IPs investigated, verdict breakdown, analyst notes.

    Reads BLUETEAM_INVESTIGATION_HISTORY and aggregates recent investigations.
    Prevents redundant re-analysis by showing which IPs already have verdicts.

    **Worked Examples**

    1. *Last 7 days*:
       ``blueteam_investigation_summary()``

    2. *Last 30 days*:
       ``blueteam_investigation_summary(since="30d")``
    """
    _audit_log("blueteam_investigation_summary", {"since": params.since})
    if not _INVESTIGATION_HISTORY_FILE:
        return json.dumps({"error": "BLUETEAM_INVESTIGATION_HISTORY not set."}, indent=2)
    since_dt = datetime.utcnow() - timedelta(days=7 if params.since == "7d" else 30)
    history = _read_history()
    recent = {ip: e for ip, e in history.items()
              if e.get("ts", "")[:10] >= since_dt.strftime("%Y-%m-%d")}
    verdicts: Counter[str] = Counter()
    for e in recent.values():
        verdicts[e.get("verdict", "unknown")] += 1

    if params.response_format == "json":
        return json.dumps({
            "window_since": since_dt.strftime("%Y-%m-%d"),
            "total_investigated": len(recent),
            "verdicts": dict(verdicts),
            "ips": sorted(recent.keys()),
        }, indent=2)

    lines = [
        f"# Investigation Summary - Since {since_dt.strftime('%Y-%m-%d')}",
        "",
        f"**Total IPs investigated**: {len(recent)}",
        "",
        "| Verdict | Count |",
        "|---------|-------|",
    ]
    for v, c in verdicts.most_common():
        lines.append(f"| {v} | {c} |")
    if recent:
        lines.append("")
        lines.append("## Recent Investigations")
        for ip, e in sorted(recent.items(), key=lambda x: x[1].get("ts", ""), reverse=True)[:15]:
            ts = e.get("ts", "?")[:19]
            v = e.get("verdict", "?")
            notes = (e.get("notes", "") or "")[:60]
            lines.append(f"- `[{ts}]` `{ip}` — {v}" + (f" ({notes})" if notes else ""))
    return _truncate_if_needed("\n".join(lines))


# Investigation History read/write helpers (shared across tools)
def _read_history() -> dict[str, dict]:
    """Read investigation history from JSONL file. Returns {ip: latest_entry}."""
    if not _INVESTIGATION_HISTORY_FILE:
        return {}
    history: dict[str, dict] = {}
    try:
        with open(_INVESTIGATION_HISTORY_FILE) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                entry = json.loads(line)
                ip = entry.get("srcip", "")
                if ip:
                    history[ip] = entry
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return history


def _append_history(entry: dict) -> bool:
    """Append an investigation entry to the history file, tail-truncating to max entries."""
    if not _INVESTIGATION_HISTORY_FILE:
        return False
    try:
        with open(_INVESTIGATION_HISTORY_FILE, "a") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        if _INVESTIGATION_HISTORY_MAX_ENTRIES > 0:
            with open(_INVESTIGATION_HISTORY_FILE) as f:
                lines = f.readlines()
            if len(lines) > _INVESTIGATION_HISTORY_MAX_ENTRIES:
                with open(_INVESTIGATION_HISTORY_FILE, "w") as f:
                    f.writelines(lines[-_INVESTIGATION_HISTORY_MAX_ENTRIES:])
        return True
    except Exception:
        return False


def _write_history(srcip: str, verdict: str, summary: dict) -> None:
    """Append an investigation entry to the history file."""
    entry = {"ts": datetime.utcnow().isoformat() + "Z", "srcip": srcip,
             "verdict": verdict, "summary": summary}
    _append_history(entry)


class InvestigationHistoryInput(BaseModel):
    """Input model for blueteam_investigation_history."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    srcip: str = Field(..., min_length=7, max_length=45,
        description="Source IP to check investigation history for.")
    response_format: Literal["markdown", "json"] = Field(
        default="markdown", description="'markdown' or 'json'.")


@mcp.tool(
    name="blueteam_investigation_history",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": False},
)
async def blueteam_investigation_history(params: InvestigationHistoryInput) -> str:
    """Check if an IP was previously investigated and what the verdict was.

    Reads from BLUETEAM_INVESTIGATION_HISTORY (JSONL file). Returns the last
    investigation entry for the IP with timestamp, verdict, and summary.

    **Required**: BLUETEAM_INVESTIGATION_HISTORY env var pointing to a writable
    JSONL file. Without it, returns empty history.

    **Worked Examples**

    1. *Check prior investigation*:
       ``blueteam_investigation_history(srcip="103.107.116.202")``

    2. *Verify if IP is new*:
       ``blueteam_investigation_history(srcip="185.220.101.1")``
    """
    _audit_log("blueteam_investigation_history", {"srcip": params.srcip})
    history = _read_history()
    entry = history.get(params.srcip.strip())

    if params.response_format == "json":
        return json.dumps({
            "srcip": params.srcip,
            "previously_investigated": entry is not None,
            "last_entry": entry,
        }, indent=2, ensure_ascii=False)

    if entry:
        ts = entry.get("ts", "?")[:19]
        verdict = entry.get("verdict", "unknown")
        summary = entry.get("summary", {})
        return (
            f"# Investigation History - `{params.srcip}`\n\n"
            f"- **Last analyzed**: {ts}\n"
            f"- **Verdict**: {verdict}\n"
            f"- **Summary**: {json.dumps(summary, indent=2)}\n\n"
            f"_History file: {_INVESTIGATION_HISTORY_FILE}_"
        )
    return (
        f"# Investigation History - `{params.srcip}`\n\n"
        f"**No prior investigation found**. This IP has not been analyzed before.\n\n"
        f"_History file: {_INVESTIGATION_HISTORY_FILE or '(not configured)'}_"
    )


# Graph-integration scoring constants (Engine A)
_PPR_BOOST_FACTOR = 5.0      # total += ppr_score * factor
_CONFIRMED_BONUS = 2.0       # flat bonus for registry-confirmed attacker IOCs


class FalsePositiveKbInput(BaseModel):
    """Input model for blueteam_false_positive_kb."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    response_format: Literal["markdown", "json"] = Field(
        default="markdown", description="'markdown' or 'json'.")


@mcp.tool(
    name="blueteam_false_positive_kb",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": False},
)
async def blueteam_false_positive_kb(params: FalsePositiveKbInput) -> str:
    """List the false-positive knowledge base - IOC the 3-Sum engine auto-suppresses.

    Shows active (unexpired) false-positive IOCs and their sources. These are
    auto-excluded from `three_sum_correlation` results via the FP knowledge base.
    Populated by `blueteam_mark_investigated(verdict="false_positive")`.

    **Worked Examples**

    1. *See what the engine is suppressing*:
       ``blueteam_false_positive_kb()``

    2. *Machine-readable list*:
       ``blueteam_false_positive_kb(response_format="json")``
    """
    _audit_log("blueteam_false_positive_kb", {})
    iocs = sorted(false_positive_iocs())
    stats = false_positive_stats()
    if params.response_format == "json":
        return json.dumps({"stats": stats, "iocs": iocs}, indent=2, ensure_ascii=False)
    lines = ["# False-Positive Knowledge Base", "",
             f"- **Active entries**: {stats['entries']}",
             f"- **TTL**: {stats['ttl_seconds']}s",
             f"- **Path**: {stats['persisted_path'] or '(not persisted)'}", ""]
    if iocs:
        lines.append("## Suppressed IOCs")
        for i in iocs[:100]:
            lines.append(f"- `{i}`")
        if len(iocs) > 100:
            lines.append(f"- … and {len(iocs) - 100} more")
    else:
        lines.append("*No false positives recorded.*")
    return _truncate_if_needed("\n".join(lines))
