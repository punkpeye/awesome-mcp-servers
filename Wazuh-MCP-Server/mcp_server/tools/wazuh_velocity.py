#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Wazuh attack velocity tool - dual window comparison
"""
from __future__ import annotations
import json, re, asyncio
from datetime import datetime, timedelta
from typing import Optional, Literal
from pydantic import BaseModel, ConfigDict, Field, field_validator
from mcp_server import (mcp, WAZUH_INDEXER_URL, WAZUH_INDEXER_PASSWORD,
                        _BYPASS_REDACTION_DESC, _RESPONSE_FORMAT_DESC, _AGENT_NAME_DESC,
                        _REDACTION_POLICY_DESC, _REVEAL_OWNED_DESC, _FORENSIC_TOKEN_DESC)
from mcp_server.core.audit import _audit_log, _truncate_if_needed, _escape_md_table
from mcp_server.core.redact import _redact_alert_data
from mcp_server.core.http_client import _handle_api_error
from mcp_server.wazuh.indexer import _wazuh_indexer_post, _WAZUH_INDEX_PATTERNS
from mcp_server.wazuh.time_utils import (_parse_time_window, _auto_bucket_interval,
                                          _duration_minutes, _RELATIVE_TIME_RE, _relative_delta)
from mcp_server.core.validators import ValidAgentName, ValidRuleGroups, ValidKeyword

class WazuhAttackVelocityInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    window: str = Field(
        default="1h",
        max_length=10,
        description="Window size for comparison - relative expression: '15m', '1h', '6h', '24h'. "
                    "'1h' compares the last hour against the hour before that.",
    )
    agent_name: ValidAgentName = Field(
        default=None,
        max_length=64,
        description=_AGENT_NAME_DESC,
    )
    rule_groups: ValidRuleGroups = Field(
        default=None,
        max_length=1024,
        description="Comma-separated rule groups to filter by.",
    )
    bucket: str = Field(
        default="auto",
        max_length=10,
        description="Bucket size within each window: '1m', '5m', '15m', '1h', or 'auto'.",
    )
    keyword: ValidKeyword = Field(
        default=None,
        max_length=1024,
        description="Free-text keyword search to narrow the analysis. Same syntax as "
                    "blueteam_wazuh_indexer_search.",
    )
    response_format: Literal["markdown", "json"] = Field(
        default="markdown",
        description="_RESPONSE_FORMAT_DESC",
    )
    bypass_redaction: bool = Field(
        default=False, description=_BYPASS_REDACTION_DESC,
    )
    redaction_policy: Optional[Literal["full", "protect_victim", "raw"]] = Field(
        default=None,
        description=_REDACTION_POLICY_DESC,
    )
    reveal_owned: bool = Field(default=False, description=_REVEAL_OWNED_DESC)
    forensic_token: Optional[str] = Field(default=None, max_length=128, description=_FORENSIC_TOKEN_DESC)


    @field_validator("window")
    @classmethod
    def validate_window(cls, v: str) -> str:
        if not _RELATIVE_TIME_RE.match(v.strip()):
            raise ValueError(
                "window must be a relative expression: '15m', '1h', '6h', '24h', '7d'"
            )
        return v.strip()

@mcp.tool(
    name="wazuh_attack_velocity",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def wazuh_attack_velocity(params: WazuhAttackVelocityInput = WazuhAttackVelocityInput()) -> str:
    """Compare two adjacent time windows to detect attack acceleration or deceleration.

    Queries the Wazuh Indexer for two adjacent windows of equal duration (current
    and previous), computes per-bucket deltas, and scores the overall trend:
    **accelerating** (>+25%), **steady** (-25% to +25%), or **decelerating** (<−25%).

    Also reports the top accelerating rules and source IPs across the two windows.

    Args:
        params.window: Window size - relative expression like '15m', '1h', '6h', '24h'.
                      '1h' compares the last hour against the hour before it.
        params.agent_name: Optional agent filter.
        params.rule_groups: Optional comma-separated rule groups filter.
        params.bucket: Bucket granularity within each params.window. 'auto' picks based on
                      params.window size.
        params.response_format: 'markdown' or 'json'.
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.
        params.redaction_policy: 'full' (shape-based, default), 'protect_victim' (mask victim-owned indicators only), 'raw' (Layer 1 credential strip only, requires BLUETEAM_ALLOW_FORENSIC_BYPASS).
        params.reveal_owned: When true (forensic), expose emails/subdomains at owned domains (BLUETEAM_OWNED_DOMAINS) unmasked; Layer 1 credentials remain masked.
        params.forensic_token: Operator forensic token (matches BLUETEAM_FORENSIC_TOKEN); required for redaction_policy='raw' / bypass_redaction when that env is set.

    Returns:
        str: Velocity report with trend classification, per-bucket comparison table,
        and top accelerating rules / source IPs.

    Example usage:
        - "Is the brute force attack on the mail server speeding up?"
        - "Compare the last hour's alert volume to the previous hour"
    """
    _audit_log("wazuh_attack_velocity", {"window": params.window})

    if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
        return json.dumps({"error": "WAZUH_INDEXER_URL and WAZUH_INDEXER_PASSWORD must be set."}, indent=2)

    window_str = params.window.strip()
    m = _RELATIVE_TIME_RE.match(window_str)
    if not m:
        return json.dumps({"error": f"Invalid window: '{window_str}'. Use '15m', '1h', '6h', '24h'."}, indent=2)
    n, unit = int(m.group(1)), m.group(2)
    window_delta = _relative_delta(n, unit)

    now = datetime.utcnow()
    current_start = now - window_delta
    current_end = now
    previous_start = current_start - window_delta
    previous_end = current_start

    fmt = "%Y-%m-%dT%H:%M:%SZ"
    current_since = current_start.strftime(fmt)
    current_until = current_end.strftime(fmt)
    previous_since = previous_start.strftime(fmt)
    previous_until = previous_end.strftime(fmt)

    # Determine bucket interval
    dur_minutes = window_delta.total_seconds() / 60.0
    bucket_interval = params.bucket if params.bucket != "auto" else _auto_bucket_interval(dur_minutes)

    def _build_query(since: str, until: str) -> dict:
        must: list[dict] = [
            {"range": {"@timestamp": {"gte": since, "lt": until,
                                        "format": "strict_date_optional_time"}}},
        ]
        if params.agent_name:
            must.append({"match": {"agent.name": params.agent_name}})
        if params.rule_groups:
            groups = [g.strip() for g in params.rule_groups.split(",") if g.strip()]
            if groups:
                must.append({"terms": {"rule.groups": groups}})
        if params.keyword:
            kw = params.keyword.strip()
            must.append({"query_string": {"query": f"full_log: ({kw})", "lenient": True}})
        return {
            "size": 0,
            "query": {"bool": {"filter": must}},
            "aggs": {
                "over_time": {
                    "date_histogram": {
                        "field": "@timestamp",
                        "fixed_interval": bucket_interval,
                        "min_doc_count": 0,
                    },
                    "aggs": {
                        "top_rules": {"terms": {"field": "rule.id", "size": 5}},
                        "top_srcips": {"terms": {"field": "data.srcip", "size": 5}},
                    },
                }
            },
        }

    try:
        current_raw, previous_raw = await asyncio.gather(
            _wazuh_indexer_post(_build_query(current_since, current_until)),
            _wazuh_indexer_post(_build_query(previous_since, previous_until)),
        )
    except Exception as e:
        return _handle_api_error(e, context="wazuh_attack_velocity")

    if "error" in current_raw:
        return json.dumps(current_raw, indent=2)
    if "error" in previous_raw:
        return json.dumps(previous_raw, indent=2)

    current_buckets = current_raw.get("aggregations", {}).get("over_time", {}).get("buckets", [])
    previous_buckets = previous_raw.get("aggregations", {}).get("over_time", {}).get("buckets", [])
    current_buckets = _redact_alert_data(current_buckets, reveal_owned=params.reveal_owned)  # mask victim identifiers in bucket keys
    previous_buckets = _redact_alert_data(previous_buckets, reveal_owned=params.reveal_owned)

    current_total = sum(b.get("doc_count", 0) for b in current_buckets)
    previous_total = sum(b.get("doc_count", 0) for b in previous_buckets)

    # Trend classification
    if previous_total == 0:
        if current_total == 0:
            trend = "inactive"
            delta_pct = 0.0
        else:
            trend = "new_activity"
            delta_pct = 100.0
    else:
        delta_pct = ((current_total - previous_total) / previous_total) * 100
        if delta_pct > 25:
            trend = "accelerating"
        elif delta_pct < -25:
            trend = "decelerating"
        else:
            trend = "steady"

    # Top rules and IPs across both windows
    def _collect_top(agg_key: str, buckets: list[dict]) -> dict[str, int]:
        result: dict[str, int] = {}
        for b in buckets:
            for item in (b.get(agg_key, {}) or {}).get("buckets", []):
                key = item.get("key", "?")
                result[key] = result.get(key, 0) + item.get("doc_count", 0)
        return result

    top_rules = sorted(
        {** _collect_top("top_rules", current_buckets),
         **_collect_top("top_rules", previous_buckets)}.items(),
        key=lambda x: x[1], reverse=True,
    )[:10]
    top_ips = sorted(
        {**_collect_top("top_srcips", current_buckets),
         **_collect_top("top_srcips", previous_buckets)}.items(),
        key=lambda x: x[1], reverse=True,
    )[:10]

    if params.response_format == "json":
        return _truncate_if_needed(json.dumps({
            "window": {"size": window_str, "current": {"since": current_since, "until": current_until},
                       "previous": {"since": previous_since, "until": previous_until}},
            "bucket_interval": bucket_interval,
            "trend": trend,
            "delta_pct": round(delta_pct, 1),
            "current_total": current_total,
            "previous_total": previous_total,
            "top_rules": [{"rule_id": k, "count": v} for k, v in top_rules],
            "top_srcips": [{"ip": k, "count": v} for k, v in top_ips],
        }, indent=2))

    # Markdown output
    trend_emoji = {"accelerating": "🔺", "decelerating": "🔻", "steady": "➡️",
                   "new_activity": "🆕", "inactive": "⏸️"}
    lines = [
        f"# Attack Velocity - {trend_emoji.get(trend, '')} {trend.replace('_', ' ').title()}",
        "",
        f"**Window**: {window_str}  |  **Bucket**: {bucket_interval}",
        f"**Current**: {current_since} -> {current_until}",
        f"**Previous**: {previous_since} -> {previous_until}",
        "",
        f"| Period | Alert Count |",
        f"|--------|-------------|",
        f"| Current | {current_total:,} |",
        f"| Previous | {previous_total:,} |",
        f"| **Delta** | **{delta_pct:+.1f}%** |",
        "",
    ]

    if top_rules:
        lines.append("## Top Rules (combined)")
        lines.append("")
        lines.append("| Rule ID | Alert Count |")
        lines.append("|---------|-------------|")
        for rid, cnt in top_rules[:8]:
            lines.append(f"| `{_escape_md_table(rid)}` | {cnt:,} |")
        lines.append("")

    if top_ips:
        lines.append("## Top Source IPs (combined)")
        lines.append("")
        lines.append("| IP | Alert Count |")
        lines.append("|----|-------------|")
        for ip, cnt in top_ips[:8]:
            lines.append(f"| `{_escape_md_table(ip)}` | {cnt:,} |")
        lines.append("")

    if trend == "accelerating":
        lines.append("⚠️ **Attack activity is accelerating** - investigate immediately.")
    elif trend == "new_activity":
        lines.append("🆕 **New activity detected** - no prior baseline for comparison.")

    return _truncate_if_needed("\n".join(lines))
