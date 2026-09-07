#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Wazuh alert timeline tool - time bucketed aggregation
"""
from __future__ import annotations
import json, re
from typing import Optional, Literal
import httpx
from pydantic import BaseModel, ConfigDict, Field, field_validator, field_validator
from mcp_server import (mcp, WAZUH_INDEXER_URL, WAZUH_INDEXER_PASSWORD,
                        _BYPASS_REDACTION_DESC, _RESPONSE_FORMAT_DESC, _AGENT_NAME_DESC,
                        _REDACTION_POLICY_DESC, _REVEAL_OWNED_DESC, _FORENSIC_TOKEN_DESC)
from mcp_server.core.audit import _audit_log, _truncate_if_needed, _escape_md_table
from mcp_server.core.redact import _redact_alert_data
from mcp_server.core.http_client import _handle_api_error
from mcp_server.wazuh.indexer import _wazuh_indexer_post, _WAZUH_INDEX_PATTERNS
from mcp_server.wazuh.time_utils import _parse_time_window, _auto_bucket_interval, _duration_minutes
from mcp_server.core.validators import ValidAgentName, ValidRuleGroups, ValidKeyword

class WazuhAlertTimelineInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    since: str = Field(
        default="1h",
        max_length=30,
        description="Start of time window - ISO 8601 ('2026-07-07T00:00:00Z') or relative "
                    "('5m', '1h', '24h', '7d', '30d'). Default: '1h'.",
    )
    until: Optional[str] = Field(
        default=None,
        max_length=30,
        description="End of time window - ISO 8601 or relative. Defaults to now.",
    )
    bucket: str = Field(
        default="auto",
        max_length=10,
        description="Bucket size: '1m', '5m', '15m', '1h', '6h', '1d', or 'auto'. "
                    "'auto' picks based on window: ≤1h->1m, ≤24h->15m, ≤7d->1h, ≤30d->6h, ≤365d->1d.",
    )
    agent_name: ValidAgentName = Field(
        default=None,
        max_length=64,
        description=_AGENT_NAME_DESC,
    )
    rule_groups: ValidRuleGroups = Field(
        default=None,
        max_length=1024,
        description="Comma-separated rule groups to filter by (e.g. 'brute_force,authentication_failed').",
    )
    rule_level_min: Optional[int] = Field(
        default=None,
        ge=1,
        le=16,
        description="Minimum rule level (e.g., 8 for medium+ severity).",
    )
    keyword: ValidKeyword = Field(
        default=None,
        max_length=1024,
        description="Free-text keyword search to narrow the timeline. Same syntax as "
                    "blueteam_wazuh_indexer_search supports +term, -term, OR, *wildcard*, "
                    '\"exact phrase\". Example: \'gambling OR "brute force"\'',
    )
    response_format: Literal["markdown", "json"] = Field(
        default="markdown",
        description="'markdown' for human-readable timeline, 'json' for structured bucket data.",
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


    @field_validator("bucket")
    @classmethod
    def validate_bucket(cls, v: str) -> str:
        v = v.strip().lower()
        if v == "auto":
            return v
        if not re.match(r"^(\d+[smhd]|auto)$", v):
            raise ValueError("bucket: use 'auto', '1m', '5m', '15m', '1h', '6h', or '1d'")
        return v



@mcp.tool(
    name="wazuh_alert_timeline",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def wazuh_alert_timeline(params: WazuhAlertTimelineInput) -> str:
    """Return a time-bucketed breakdown of Wazuh alerts using OpenSearch date_histogram.

    Instead of fetching individual alert documents, this tool asks the Indexer to
    params.bucket alert counts by time interval (per minute, per 15 minutes, per hour, etc.)
    directly on the server - fast, even across millions of documents.

    Each params.bucket includes:
    - Total alert count
    - Count by severity band (low ≤4, medium 5-9, high ≥10)
    - Top rules, top source IPs, and top agents within that params.bucket

    Args:
        params.since: Start of time window (default '1h').  Accepts ISO 8601 or relative
                     expressions ('5m', '1h', '24h', '7d', '30d').
        params.until: End of time window.  Defaults to now.
        params.bucket: Bucket size '1m', '5m', '15m', '1h', '6h', '1d', or 'auto'.
        params.agent_name: Optional agent filter.
        params.rule_groups: Optional comma-separated rule groups filter.
        params.rule_level_min: Only count alerts at or above this severity.
        params.keyword: Optional free-text keyword filter (e.g. 'gambling OR "brute force"').
        params.response_format: 'markdown' or 'json'.
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.
        params.redaction_policy: 'full' (shape-based, default), 'protect_victim' (mask victim-owned indicators only), 'raw' (Layer 1 credential strip only, requires BLUETEAM_ALLOW_FORENSIC_BYPASS).
        params.reveal_owned: When true (forensic), expose emails/subdomains at owned domains (BLUETEAM_OWNED_DOMAINS) unmasked; Layer 1 credentials remain masked.
        params.forensic_token: Operator forensic token (matches BLUETEAM_FORENSIC_TOKEN); required for redaction_policy='raw' / bypass_redaction when that env is set.

    Returns:
        str: Timeline table with per-params.bucket counts, severity bands, and top indicators.

    Example usage:
        - "Show me the alert timeline for the last hour"
        - "Break down yesterday's brute force alerts by 15-minute intervals"
        - "What's the attack volume trend over the last 7 days?"
    """
    _audit_log("wazuh_alert_timeline", {"since": params.since, "bucket": params.bucket})
    since_str, until_str = _parse_time_window(params.since, params.until)

    # Determine bucket interval
    if params.bucket == "auto":
        dur = _duration_minutes(since_str, until_str)
        bucket_interval = _auto_bucket_interval(dur)
    else:
        bucket_interval = params.bucket

    rule_group_list: Optional[list[str]] = None
    if params.rule_groups:
        rule_group_list = [g.strip() for g in params.rule_groups.split(",") if g.strip()]

    try:
        body = {
            "size": 0,
            "query": {"bool": {"filter": [
                {"range": {"@timestamp": {"gte": since_str, "lt": until_str,
                                               "format": "strict_date_optional_time"}}},
            ]}},
            "aggs": {"over_time": {"date_histogram": {
                "field": "@timestamp",
                "fixed_interval": bucket_interval,
                "min_doc_count": 0,
                "extended_bounds": {"min": since_str, "max": until_str},
            }}},
        }
        if params.agent_name:
            body["query"]["bool"]["filter"].append({"match": {"agent.name": params.agent_name}})
        if rule_group_list:
            body["query"]["bool"]["filter"].append({"terms": {"rule.groups": rule_group_list}})
        if params.rule_level_min is not None:
            body["query"]["bool"]["filter"].append({"range": {"rule.level": {"gte": params.rule_level_min}}})
        if params.keyword:
            body["query"]["bool"]["filter"].append({"query_string": {"query": params.keyword, "default_field": "full_log", "lenient": True}})
        if params.geo_country if hasattr(params, 'geo_country') else None:
            body["query"]["bool"]["filter"].append({"match": {"GeoLocation.country_name": params.geo_country}})
        data = await _wazuh_indexer_post(body)
    except (httpx.HTTPStatusError, httpx.TimeoutException, RuntimeError) as e:
        return _handle_api_error(e, context="wazuh_alert_timeline")

    if isinstance(data.get("error"), str):
        return json.dumps(data, indent=2)

    aggs = data.get("aggregations", {})
    timeline = aggs.get("alerts_over_time", {})
    buckets = timeline.get("buckets", [])

    if not buckets:
        return (
            "# Alert Timeline — No Data\n\n"
            f"**Window**: {since_str} → {until_str}\n"
            f"**Bucket**: {bucket_interval}\n\n"
            "_No alerts matched the query in this time window._"
        )

    total_alerts = sum(b.get("doc_count", 0) for b in buckets)
    buckets = _redact_alert_data(buckets, reveal_owned=params.reveal_owned)  # mask victim emails/IP/domains in bucket keys

    if params.response_format == "json":
        return _truncate_if_needed(json.dumps({
            "window": {"since": since_str, "until": until_str},
            "bucket_interval": bucket_interval,
            "total_buckets": len(buckets),
            "total_alerts": total_alerts,
            "buckets": [
                {
                    "key": b.get("key_as_string", b.get("key", "")),
                    "doc_count": b.get("doc_count", 0),
                    "by_level": {
                        r.get("key", ""): r.get("doc_count", 0)
                        for r in (b.get("by_level", {}) or {}).get("buckets", [])
                    },
                    "top_rules": [
                        {"key": r.get("key", ""), "count": r.get("doc_count", 0)}
                        for r in (b.get("top_rules", {}) or {}).get("buckets", [])
                    ],
                    "top_srcips": [
                        {"key": r.get("key", ""), "count": r.get("doc_count", 0)}
                        for r in (b.get("top_srcips", {}) or {}).get("buckets", [])
                    ],
                    "top_agents": [
                        {"key": r.get("key", ""), "count": r.get("doc_count", 0)}
                        for r in (b.get("top_agents", {}) or {}).get("buckets", [])
                    ],
                }
                for b in buckets
            ],
        }, indent=2, ensure_ascii=False))

    # Markdown
    dur_str = f"{_duration_minutes(since_str, until_str):.0f} min" if _duration_minutes(since_str, until_str) < 120 else f"{_duration_minutes(since_str, until_str) / 60:.1f}h"
    lines: list[str] = [
        f"# Alert Timeline Last {dur_str}",
        f"**Window**: {since_str} -> {until_str}  |  **Bucket**: {bucket_interval}  |  **Total alerts**: {total_alerts:,}",
        "",
        "| Time (UTC) | Total | Low (≤4) | Med (5-9) | High (≥10) | Top Rule | Top Src IP |",
        "|------------|-------|----------|-----------|------------|----------|-----------|",
    ]

    for b in buckets:
        key = b.get("key_as_string", b.get("key", ""))
        ts = key[:16] if len(key) >= 16 else key  # e.g. "2026-07-07T18:00"
        total = b.get("doc_count", 0)
        by_level = {}
        for lv in (b.get("by_level", {}) or {}).get("buckets", []):
            by_level[lv.get("key", "")] = lv.get("doc_count", 0)
        low = by_level.get("low", 0)
        med = by_level.get("medium", 0)
        high = by_level.get("high", 0)
        top_rules = [
            r.get("key", "")[:30]
            for r in ((b.get("top_rules") or {}).get("buckets") or [])
        ]
        top_rule = top_rules[0] if top_rules else "-"
        top_srcips = [
            r.get("key", "")
            for r in ((b.get("top_srcips") or {}).get("buckets") or [])
        ]
        top_ip = top_srcips[0] if top_srcips else "-"
        lines.append(f"| {ts} | {total} | {low} | {med} | {high} | {_escape_md_table(top_rule)} | {_escape_md_table(top_ip)} |")

    # Peak analysis
    peak = max(buckets, key=lambda b: b.get("doc_count", 0)) if buckets else None
    quiet = min(buckets, key=lambda b: b.get("doc_count", 0)) if buckets else None

    lines.append("")
    lines.append("## Peak Activity")
    if peak:
        peak_key = peak.get("key_as_string", peak.get("key", ""))[:16]
        peak_count = peak.get("doc_count", 0)
        lines.append(f"- **Peak**: {peak_key} — {peak_count:,} alerts")
    if quiet:
        quiet_key = quiet.get("key_as_string", quiet.get("key", ""))[:16]
        quiet_count = quiet.get("doc_count", 0)
        lines.append(f"- **Quietest**: {quiet_key} — {quiet_count:,} alerts")

    # Per severity totals
    all_low = sum(
        next((r.get("doc_count", 0) for r in (b.get("by_level", {}) or {}).get("buckets", []) if r.get("key") == "low"), 0)
        for b in buckets
    )
    all_med = sum(
        next((r.get("doc_count", 0) for r in (b.get("by_level", {}) or {}).get("buckets", []) if r.get("key") == "medium"), 0)
        for b in buckets
    )
    all_high = sum(
        next((r.get("doc_count", 0) for r in (b.get("by_level", {}) or {}).get("buckets", []) if r.get("key") == "high"), 0)
        for b in buckets
    )
    lines.extend([
        "",
        "## Severity Summary",
        f"- Low (≤4): {all_low:,} ({all_low / max(total_alerts, 1) * 100:.0f}%)",
        f"- Medium (5-9): {all_med:,} ({all_med / max(total_alerts, 1) * 100:.0f}%)",
        f"- High (≥10): {all_high:,} ({all_high / max(total_alerts, 1) * 100:.0f}%)",
        "",
        "## Query Parameters",
        f"- Since: `{params.since}`",
        f"- Bucket: `{bucket_interval}`",
        f"- Agent: {params.agent_name or 'all'}",
        f"- Rule groups: {params.rule_groups or 'all'}",
        f"- Min level: {params.rule_level_min or 'none'}",
    ])

    return _truncate_if_needed("\n".join(lines))
