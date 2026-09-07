#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
AI-agent reconnaissance detection - surfaces LLM-driven scanning/exploit activity.
"""
import json
import re
from typing import Optional, Literal
from pydantic import BaseModel, ConfigDict, Field
from mcp_server import WAZUH_INDEXER_URL, WAZUH_INDEXER_PASSWORD, _BYPASS_REDACTION_DESC
from mcp_server.wazuh.indexer import _wazuh_indexer_post
from mcp_server.wazuh.time_utils import _parse_time_window
from mcp_server.core.tool_decorator import blueteam_tool

# Known + suspicious AI-agent user-agents, matched against ``full_log`` (the raw
# log line, which carries the UA). No ``data.user_agent`` field exists in the
# standard Wazuh alert mapping, so we search ``full_log`` directly.
_AI_UA_QUERY = (
    '(GPTBot OR ClaudeBot OR "ChatGPT-User" OR PerplexityBot OR CCBot OR '
    'anthropic-ai OR cohere-ai OR "OAI-SearchBot" OR Bytespider OR Amazonbot OR '
    'ai-scanner OR autogpt OR langchain OR "llm-agent")'
)

# Paths that indicate probing/exploit rather than benign crawling/indexing.
_SENSITIVE_PATH_RE = re.compile(
    r"(wp-login|wp-json|wp-admin|xmlrpc|actuator|\.env|\.git|/config|graphql|"
    r"backup|/admin|api/v1|phpmyadmin|/shell|cmd\.php|webshell|c99|/upload|/install)",
    re.IGNORECASE,
)


class AiBotReconInput(BaseModel):
    """Input model for blueteam_ai_bot_recon."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    since: Optional[str] = Field(
        default="24h", max_length=30, description="Start of time window (ISO 8601 or relative like '24h').")
    until: Optional[str] = Field(
        default=None, max_length=30, description="End of time window. Defaults to now.")
    top_n: int = Field(
        default=20, ge=1, le=100, description="Number of top source IPs to return.")
    response_format: Literal["markdown", "json"] = Field(
        default="markdown", description="'markdown' or 'json'.")
    bypass_redaction: bool = Field(
        default=False, description=_BYPASS_REDACTION_DESC)


@blueteam_tool(
    name="blueteam_ai_bot_recon",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": False},
)
async def blueteam_ai_bot_recon(params: AiBotReconInput) -> str:
    """Surface AI/LLM-driven reconnaissance and scanning against your perimeter.
    Aggregates Wazuh web-accesslog alerts whose raw log line (``full_log``)
    contains a known AI-agent user-agent (GPTBot, ClaudeBot, ChatGPT-User,
    PerplexityBot, etc.) or a suspicious custom agent string (ai-scanner,
    autogpt, langchain, llm-agent). For each source IP it returns the probed
    paths and flags the subset that look like exploit/sensitive-endpoint probes
    rather than benign crawling an AI agent hitting ``/.env`` or ``/wp-login``
    is attacking, not indexing.
    Pure aggregation (``size: 0``) no alert documents are returned, so no
    PII beyond the attacker's own public IP and requested path is exposed.
    **Required Permissions**: Wazuh Indexer ``read`` access.
    **Rate Limits**: One Indexer ``_search`` call per invocation (aggregation
    only). No external threat intel API is contacted.

    **Worked Examples**

    1. *Who is running an AI agent against us in the last 24h?*:
       ``blueteam_ai_bot_recon()``

    2. *7-day window, top 50 sources, JSON*:
       ``blueteam_ai_bot_recon(since="7d", top_n=50, response_format="json")``

    3. *Narrow to a specific time range*:
       ``blueteam_ai_bot_recon(since="2026-08-01T00:00:00Z", until="2026-08-02T00:00:00Z")``
    """
    if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
        return json.dumps({"error": "WAZUH_INDEXER_URL and WAZUH_INDEXER_PASSWORD must be set."})

    since_iso, until_iso = _parse_time_window(params.since, params.until)

    body = {
        "size": 0,
        "query": {"bool": {"must": [
            {"range": {"@timestamp": {"gte": since_iso, "lt": until_iso,
                                       "format": "strict_date_optional_time"}}},
            {"query_string": {"query": _AI_UA_QUERY,
                              "default_field": "full_log", "lenient": True}},
        ]}},
        "aggs": {
            "by_srcip": {
                "terms": {"field": "data.srcip", "size": params.top_n,
                          "order": {"_count": "desc"}},
                "aggs": {
                    "paths": {"terms": {"field": "data.url", "size": 25}},
                },
            },
        },
    }
    raw = await _wazuh_indexer_post(body)
    if "error" in raw:
        return json.dumps(raw, indent=2)

    buckets = raw.get("aggregations", {}).get("by_srcip", {}).get("buckets", [])

    sources = []
    for b in buckets:
        srcip = b["key"]
        path_buckets = b.get("paths", {}).get("buckets", [])
        paths = [p["key"] for p in path_buckets]
        sensitive = [p for p in paths if _SENSITIVE_PATH_RE.search(p)]
        sensitive_hits = sum(
            p["doc_count"] for p in path_buckets if _SENSITIVE_PATH_RE.search(p["key"])
        )
        sources.append({
            "srcip": srcip,
            "alerts": b["doc_count"],
            "unique_paths": len(paths),
            "sensitive_hits": sensitive_hits,
            "sensitive_paths": sensitive[:10],
            "all_paths": paths[:25],
        })

    if params.response_format == "json":
        return {
            "window": {"since": since_iso, "until": until_iso},
            "ai_agent_sources": len(sources),
            "sources": sources,
        }

    lines = [
        "# 🤖 AI-Agent Recon Detection",
        "",
        f"**Window**: `{since_iso}` -> `{until_iso}`",
        f"**AI-agent sources detected**: {len(sources)}",
        "",
        "| Source IP | Alerts | Sensitive hits | Sensitive paths |",
        "|-----------|--------|----------------|-----------------|",
    ]
    for s in sources:
        sp = ", ".join(f"`{p}`" for p in s["sensitive_paths"][:3]) or "-"
        lines.append(f"| {s['srcip']} | {s['alerts']:,} | {s['sensitive_hits']:,} | {sp} |")
    if not sources:
        lines.append("| *(no AI-agent traffic detected in window)* | - | - | - |")
        lines.append("")
        lines.append("> Try a wider `since` window, or confirm web-accesslog alerts carry a "
                     "user-agent in `full_log`.")
    return "\n".join(lines)
