#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
F-2: Beacon detection - inter-arrival time analysis, CV scoring, period estimation
"""
from __future__ import annotations
import json, re, math, asyncio, os
from datetime import datetime, timedelta
from typing import Optional, Literal, Any
from collections import Counter
from pydantic import BaseModel, ConfigDict, Field, field_validator
from mcp_server import (mcp, WAZUH_INDEXER_URL, WAZUH_INDEXER_PASSWORD,
                        _WAZUH_INDEXER_MAX_SIZE, _BYPASS_REDACTION_DESC, _REDACTION_POLICY_DESC, _REVEAL_OWNED_DESC, _FORENSIC_TOKEN_DESC,
                        CROWDSEC_API_KEY_ENV, ARGUS_API_KEY_ENV,
                        ABUSEIPDB_API_KEY, VIRUSTOTAL_API_KEY,
                        GREYNOISE_COMMUNITY_BASE_URL, ABUSEIPDB_BASE_URL,
                        VIRUSTOTAL_BASE_URL, ARGUS_BASE_URL)
from mcp_server.core.audit import _audit_log, _truncate_if_needed, _escape_md_table
from mcp_server.core.http_client import ValidPublicIp
from mcp_server.core.redact import _redact_alert_data
from mcp_server.core.http_client import _api_call, _get_client
from mcp_server.core.validators import ValidAgentName, ValidKeyword, ValidRuleGroups
from mcp_server.wazuh.indexer import _wazuh_indexer_post, _WAZUH_INDEX_PATTERNS
from mcp_server.wazuh.time_utils import _parse_time_window, _duration_minutes
from mcp_server.threat_intel.crowdsec import _crowdsec_request

# IPs to exclude from beacon detection (comma-separated, e.g. monitoring agents, heartbeats)
_BEACON_EXCLUDE_IPS: set[str] = {
    ip.strip() for ip in os.environ.get("BLUETEAM_BEACON_EXCLUDE_IPS", "").split(",") if ip.strip()
}

# 2: Beacon Detection
# Auto-extracted from alert_enrichment.py - modular refactor (2026-08-11 - AUL Tuning)
class BeaconDetectInput(BaseModel):
    """Input model for blueteam_beacon_detect."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    srcip: str = Field(
        ...,
        min_length=7,
        max_length=45,
        description="Source IP to analyze for C2 beaconing patterns.",
    )
    since: Optional[str] = Field(
        default="24h",
        max_length=30,
        description="Start of time window. ISO 8601 or relative.",
    )
    until: Optional[str] = Field(
        default=None,
        max_length=30,
        description="End of time window. Defaults to now.",
    )
    cv_threshold: float = Field(
        default=0.35,
        ge=0.0,
        le=1.0,
        description="Coefficient of variation threshold. CV < threshold -> regular beaconing. "
                    "Lower = stricter (0.15 for tight beacons, 0.35 for relaxed).",
    )
    min_events: int = Field(
        default=5,
        ge=3,
        le=1000,
        description="Minimum events required to compute beacon score.",
    )
    response_format: Literal["markdown", "json"] = Field(
        default="markdown",
        description="Output format: 'markdown' or 'json'.",
    )


@mcp.tool(
    name="blueteam_beacon_detect",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
async def blueteam_beacon_detect(params: BeaconDetectInput) -> str:
    """Detect C2 beaconing patterns via inter-arrival time analysis.
    Fetches ``@timestamp`` for all alerts from a given source IP, computes
    inter-arrival gaps, and calculates the coefficient of variation (CV =
    σ/μ). A low CV with consistent intervals is the statistical signature
    of periodic beaconing — a hallmark of C2 callbacks.

    Returns beacon score (0.0-1.0), estimated period, gap statistics,
    and a timeline summary.

    **Required Permissions**: Wazuh Indexer user with ``read`` access.

    **Worked Examples**

    1. *Default 24h scan*:
       ``blueteam_beacon_detect(srcip="103.107.116.202")``

    2. *7-day window, stricter threshold*:
       ``blueteam_beacon_detect(srcip="103.107.116.202", since="7d", cv_threshold=0.15)``

    3. *Short window for rapid beaconing*:
       ``blueteam_beacon_detect(srcip="103.107.116.202", since="1h", min_events=10)``
    """
    _audit_log("blueteam_beacon_detect", {"srcip": params.srcip})
    # Exclude known benign periodic IPs (monitoring, heartbeats)
    if params.srcip.strip() in _BEACON_EXCLUDE_IPS:
        return json.dumps({"srcip": params.srcip, "beacon_score": 0.0,
                           "verdict": "benign",
                           "note": "IP in BLUETEAM_BEACON_EXCLUDE_IPS — known health-check/monitoring"},
                          indent=2)
    if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
        return json.dumps({
            "error": "WAZUH_INDEXER_URL and WAZUH_INDEXER_PASSWORD must be set.",
        }, indent=2)

    since_iso, until_iso = _parse_time_window(params.since, params.until)

    body = {
        "size": 2000,
        "sort": [{"@timestamp": {"order": "asc"}}],
        "query": {
            "bool": {
                "must": [
                    {"range": {"@timestamp": {"gte": since_iso, "lt": until_iso,
                                             "format": "strict_date_optional_time"}}},
                    {"bool": {
                        "should": [
                            {"match": {"data.srcip": params.srcip.strip()}},
                            {"match_phrase": {"full_log": params.srcip.strip()}},
                        ],
                        "minimum_should_match": 1,
                    }},
                ]
            }
        },
        "_source": ["@timestamp"],
    }
    raw = await _wazuh_indexer_post(body)
    if "error" in raw:
        return json.dumps(raw, indent=2)

    hits = raw.get("hits", {}).get("hits", [])
    if len(hits) < params.min_events:
        result = {
            "srcip": params.srcip,
            "beacon_score": 0.0,
            "verdict": "insufficient_data",
            "detail": f"Only {len(hits)} events - need at least {params.min_events}.",
        }
        return json.dumps(result, indent=2) if params.response_format == "json" else (
            f"# Beacon Detection - `{params.srcip}`\n\n"
            f"**Insufficient data**: {len(hits)} events (need ≥{params.min_events}). "
            f"Expand the time window and retry.")

    # Parse timestamps into epoch seconds
    timestamps: list[float] = []
    for h in hits:
        ts = h.get("_source", {}).get("@timestamp", "")
        try:
            dt = datetime.fromisoformat(str(ts).replace("Z", "+00:00"))
            timestamps.append(dt.timestamp())
        except (ValueError, TypeError):
            continue

    if len(timestamps) < params.min_events:
        result = {
            "srcip": params.srcip,
            "beacon_score": 0.0,
            "verdict": "unparseable_timestamps",
            "detail": f"Only {len(timestamps)} parseable timestamps from {len(hits)} hits.",
        }
        return json.dumps(result, indent=2) if params.response_format == "json" else (
            f"# Beacon Detection - `{params.srcip}`\n\n"
            f"**Could not parse enough timestamps**: {len(timestamps)} valid from {len(hits)} total.")

    # Inter-arrival analysis
    gaps = [timestamps[i] - timestamps[i - 1] for i in range(1, len(timestamps))]
    n = len(gaps)
    mean_gap = sum(gaps) / n
    variance = sum((g - mean_gap) ** 2 for g in gaps) / n
    stddev = math.sqrt(variance)
    cv = stddev / mean_gap if mean_gap > 0 else float("inf")

    # Beacon score: 1.0 = perfect periodicity, 0.0 = random
    # clamp CV to [0, 1] range via sigmoid-like decay
    beacon_score = max(0.0, min(1.0, 1.0 - (cv / 0.5)))

    # Estimate period - use median for robustness against outliers
    sorted_gaps = sorted(gaps)
    median_gap = sorted_gaps[n // 2] if n > 0 else 0.0
    period_secs = round(median_gap)

    # Detect multiple period candidates (e.g. 60s + 300s harmonics)
    gap_counter: Counter[int] = Counter()
    for g in gaps:
        gap_counter[int(round(g))] += 1
    top_periods = gap_counter.most_common(3)

    verdict = (
        "strong_beacon" if beacon_score >= 0.8 else
        "likely_beacon" if beacon_score >= 0.5 else
        "possible_beacon" if beacon_score >= 0.25 else
        "no_beacon"
    )

    if params.response_format == "json":
        result = {
            "srcip": params.srcip,
            "window": {"since": since_iso, "until": until_iso},
            "total_events": len(timestamps),
            "gaps": {
                "count": n,
                "mean_seconds": round(mean_gap, 1),
                "median_seconds": round(median_gap, 1),
                "stddev_seconds": round(stddev, 1),
                "cv": round(cv, 3),
            },
            "beacon_score": round(beacon_score, 3),
            "verdict": verdict,
            "estimated_period_seconds": period_secs,
            "top_periods": [{"seconds": p, "count": c} for p, c in top_periods],
            "timeline_preview": [
                {"ts": datetime.utcfromtimestamp(t).isoformat() + "Z",
                 "gap_from_prev_s": round(gaps[i - 1], 1) if i > 0 else None}
                for i, t in enumerate(timestamps[:20])
            ],
        }
        return _truncate_if_needed(json.dumps(result, indent=2, ensure_ascii=False))

    # Markdown report Format
    verdict_icon = {"strong_beacon": "🔴", "likely_beacon": "🟠",
                     "possible_beacon": "🟡", "no_beacon": "🟢"}
    lines = [
        f"# Beacon Detection — `{params.srcip}`",
        "",
        f"- **Verdict**: {verdict_icon.get(verdict, '')} **{verdict.replace('_', ' ').title()}**",
        f"- **Beacon Score**: `{beacon_score:.3f}` (0.0 = random, 1.0 = perfect periodicity)",
        f"- **Events**: {len(timestamps)} over {since_iso} → {until_iso}",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Mean gap | {mean_gap:.1f}s |",
        f"| Median gap | {median_gap:.1f}s |",
        f"| StdDev | {stddev:.1f}s |",
        f"| CV (σ/μ) | {cv:.3f} |",
        "",
    ]
    if period_secs > 0:
        period_display = (
            f"{period_secs}s" if period_secs < 120 else
            f"{period_secs / 60:.1f}m" if period_secs < 3600 else
            f"{period_secs / 3600:.1f}h"
        )
        lines.append(f"**Estimated period**: ~{period_display}")

    if top_periods:
        lines.append("")
        lines.append("## Top Period Candidates")
        for secs, cnt in top_periods:
            d = f"{secs}s" if secs < 120 else f"{secs / 60:.1f}m"
            lines.append(f"- {d} — {cnt} occurrences")

    lines.append("")
    lines.append("## Gap Distribution (first 20 events)")
    lines.append("```")
    for i, t in enumerate(timestamps[:20]):
        ts_str = datetime.utcfromtimestamp(t).isoformat()[:19] + "Z"
        gap_str = f"+{gaps[i - 1]:.0f}s" if i > 0 else "start"
        bar = "█" * min(40, int(gaps[i - 1] / max(1, mean_gap) * 10)) if i > 0 else ""
        lines.append(f"  {ts_str}  {gap_str:>8s}  {bar}")
    if len(timestamps) > 20:
        lines.append(f"  ... and {len(timestamps) - 20} more events")
    lines.append("```")

    return _truncate_if_needed("\n".join(lines))


# F-3: Attack Chain Analysis
