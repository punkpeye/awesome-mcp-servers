#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
DSL query tool - raw OpenSearch aggregation queries
"""
from __future__ import annotations
import json, re
from typing import Optional, Literal, Any
import httpx
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator
from mcp_server import mcp, logger, WAZUH_INDEXER_URL, WAZUH_INDEXER_PASSWORD, CHARACTER_LIMIT, _REVEAL_OWNED_DESC
from mcp_server.core.audit import _audit_log, _truncate_if_needed
from mcp_server.core.redact import _redact_alert_data
from mcp_server.core.http_client import _handle_api_error
from mcp_server.wazuh.indexer import _wazuh_indexer_post, _WAZUH_INDEX_PATTERNS


def _check_no_scripts(obj, path: str = "root") -> None:
    """Reject scripted aggregations - security boundary against injection."""
    if isinstance(obj, dict):
        if "script" in obj:
            raise ValueError(f"Scripted aggregation rejected at {path}")
        for k, v in obj.items():
            _check_no_scripts(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            _check_no_scripts(v, f"{path}[{i}]")

class DslQueryInput(BaseModel):
    """Input model for wazuh_alert_dsl_query - structured OpenSearch DSL, aggregation-only.

    Two input paths (mutually exclusive):
    1. **Structured (preferred)**: pass ``aggs`` (and optionally ``query``) as native JSON
       objects. Pydantic validates the shape; the server serializes to the OpenSearch wire
       format. No JSON-in-JSON escaping - safe for LLM callers.
    2. **Raw string (deprecated)**: pass ``query_json`` as a pre-serialized DSL string.
       Requires correct double-escaping for nested quotes. Use only for backward compat.
    """
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def coerce_string_params(cls, data: Any) -> Any:
        """Auto-parse JSON-string params - MCP clients sometimes send args as raw JSON strings."""
        if isinstance(data, str):
            import json as _json
            try:
                data = _json.loads(data)
            except _json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON: {e.msg} at position {e.pos}. Check commas and braces.")
        return data

    # Structured path
    aggs: Optional[dict[str, Any]] = Field(
        default=None,
        description=(
            "OpenSearch aggregation tree as a native JSON object. "
            "Example: {\"by_agent\": {\"terms\": {\"field\": \"agent.name\", \"size\": 50}}}. "
            "Pass this (not query_json) for all new queries — the server serializes to the "
            "wire format, eliminating the JSON-in-JSON escaping trap."
        ),
    )
    query: Optional[dict[str, Any]] = Field(
        default=None,
        description=(
            "Optional query filter dict (same shape as OpenSearch query DSL). "
            "Example: {\"bool\": {\"must\": [{\"range\": {\"@timestamp\": {\"gte\": \"now-6h\"}}}]}}. "
            "Only valid when ``aggs`` is set."
        ),
    )

    # Raw string path (deprecated - *backward compat only)
    query_json: Optional[str] = Field(
        default=None,
        min_length=5,
        max_length=10240,
        description=(
            "[DEPRECATED] Raw OpenSearch DSL JSON string. Prefer ``aggs`` + ``query`` instead. "
            "MUST use 'size': 0 (aggregation-only). "
            "When using this path, Painless script quotes require quadruple backslash escaping "
            "(\\\\\") to survive JSON-in-JSON double-serialization."
        ),
    )

    index_pattern: str = Field(
        default="wazuh-alerts-*",
        max_length=128,
        description="OpenSearch index pattern (default 'wazuh-alerts-*'). "
                    "Also accepts 'wazuh-events-*', 'wazuh-states-vulnerabilities-*'.",
    )
    response_format: Literal["markdown", "json"] = Field(
        default="json",
        description="'json' (default, machine-readable) or 'markdown'.",
    )
    reveal_owned: bool = Field(default=False, description=_REVEAL_OWNED_DESC)

    @model_validator(mode="after")
    def require_exactly_one_input_path(self):
        """Mutually exclusive: structured (aggs) or raw (query_json), not both, not neither."""
        has_aggs = self.aggs is not None
        has_query_json = self.query_json is not None
        if has_aggs and has_query_json:
            raise ValueError(
                "Pass either 'aggs' (structured, preferred) or 'query_json' (raw, deprecated), not both."
            )
        if not has_aggs and not has_query_json:
            raise ValueError(
                "Either 'aggs' (structured, preferred) or 'query_json' (raw, deprecated) is required."
            )
        if self.query is not None and not has_aggs:
            raise ValueError("'query' is only valid when 'aggs' is set, not with 'query_json'.")
        return self

    @field_validator("aggs")
    @classmethod
    def validate_aggs(cls, v: Optional[dict]) -> Optional[dict]:
        """Reject scripted aggregations in the structured path."""
        if v is not None:
            if not v:
                raise ValueError("'aggs' must contain at least one aggregation.")
            _check_no_scripts(v, "aggs")
        return v

    @field_validator("query")
    @classmethod
    def validate_query(cls, v: Optional[dict]) -> Optional[dict]:
        """Reject scripted queries in the structured path - same boundary as aggs."""
        if v is not None:
            _check_no_scripts(v, "query")
        return v

    @field_validator("query_json")
    @classmethod
    def validate_dsl(cls, v: Optional[str]) -> Optional[str]:
        """Parse the JSON and enforce size: 0 - no document hits allowed. Deprecated path."""
        if v is None:
            return v
        try:
            parsed = json.loads(v)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in query_json: {e}") from e

        # Enforce aggregation-only: size must be 0
        size_val = parsed.get("size", 10)  # OpenSearch defaults size to 10
        if size_val != 0:
            raise ValueError(
                f"query_json has 'size': {size_val}. This tool only accepts size: 0 "
                "(aggregation-only queries). To retrieve raw alert documents, use "
                "wazuh_alert_focused_crawl instead."
            )

        # Must contain 'aggs' or 'aggregations'
        if "aggs" not in parsed and "aggregations" not in parsed:
            raise ValueError(
                "query_json must contain 'aggs' or 'aggregations' key. "
                "This tool is for aggregation queries only."
            )

        _check_no_scripts(parsed)
        return v

    @field_validator("index_pattern")
    @classmethod
    def validate_index_pattern(cls, v: str) -> str:
        v = v.strip()
        # Allow only safe index patterns: alphanumeric, *, -, _
        if not re.match(r"^[a-zA-Z0-9*_\-.,]+$", v):
            raise ValueError(
                "index_pattern must be a valid OpenSearch index pattern "
                "(e.g. 'wazuh-alerts-*', 'wazuh-events-*')"
            )
        return v


@mcp.tool(
    name="wazuh_alert_dsl_query",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def wazuh_alert_dsl_query(params: DslQueryInput) -> str:
    """Execute a raw OpenSearch DSL aggregation query against the Wazuh Indexer.

    This is an **aggregation-only** escape hatch for analytical questions that
    don't fit the pre-built ``wazuh_alert_aggregate_analysis`` modes. The input
    DSL must use ``"size": 0`` - raw document retrieval is rejected at validation
    time. Scripted aggregations are also blocked for security.

    **Two input paths** (mutually exclusive):
    - **Structured (preferred)**: pass ``params.aggs`` (and optionally ``params.query``)
      as native JSON objects. The server serializes to the OpenSearch wire format -
      no JSON-in-JSON escaping required. Safe for LLM callers.
    - **Raw string (deprecated)**: pass ``params.query_json`` as a pre-serialized DSL
      string. Requires correct double-escaping for nested quotes.

    Use this when you need a specific OpenSearch aggregation (percentiles,
    geo_distance, nested, reverse_nested, etc.) that the built-in tools
    do not expose.

    Args:
        params.aggs: OpenSearch aggregation tree as a native dict (preferred path).
        params.query: Optional query filter dict (only with ``aggs``).
        params.query_json: [DEPRECATED] Raw OpenSearch DSL JSON string.
        params.index_pattern: Index pattern (default 'wazuh-alerts-*').
        params.response_format: 'json' (default) or 'markdown'.
        params.reveal_owned: When true (forensic), expose emails/subdomains at owned
            domains (BLUETEAM_OWNED_DOMAINS) unmasked while all other protect_victim
            masking stays on. Layer 1 credentials remain masked.

    Returns:
        str: OpenSearch aggregation response (JSON by default, markdown on request).

    Example usage (structured path):
        - aggs={"by_agent": {"terms": {"field": "agent.name", "size": 50}}}
        - aggs={"hourly": {"date_histogram": {"field": "@timestamp", "fixed_interval": "1h"}}},
          query={"bool": {"must": [{"range": {"@timestamp": {"gte": "now-24h"}}}]}}

    Example usage (deprecated raw path):
        - query_json='{"size":0,"aggs":{"by_agent":{"terms":{"field":"agent.name"}}}}'

    Error Handling:
        - Invalid JSON → rejected at Pydantic validation
        - ``size`` > 0 → rejected with guidance to use wazuh_alert_focused_crawl
        - Scripted aggs → rejected for security
        - HTTP errors → surfaced through the circuit breaker

    Docs: https://opensearch.org/docs/latest/aggregations/
    """
    _audit_log("wazuh_alert_dsl_query", {"index": params.index_pattern})

    # Build the DSL body - structured path (preferred) or raw path (deprecated)
    if params.aggs is not None:
        body: dict[str, Any] = {"size": 0, "aggs": params.aggs}
        if params.query is not None:
            body["query"] = params.query
    else:
        logger.warning("wazuh_alert_dsl_query: query_json (raw string) path is deprecated. "
                       "Use 'aggs' + 'query' dicts instead to avoid JSON-in-JSON escaping issues.")
        body = json.loads(params.query_json)  # type: ignore[arg-type]

    try:
        data = await _wazuh_indexer_post(
            body,
            index_pattern=params.index_pattern,
        )
    except (httpx.HTTPStatusError, httpx.TimeoutException, RuntimeError) as e:
        return _handle_api_error(e, context="wazuh_alert_dsl_query")

    if params.response_format == "markdown":
        if isinstance(data.get("error"), str):
            return f"# DSL Query Error\n\n**Error**: {data['error']}\n\n**Detail**: {data.get('detail', 'N/A')}"
        aggs = data.get("aggregations", data.get("aggs", {}))
        return f"# DSL Query Result\n\n**Index**: {params.index_pattern}\n\n```json\n{json.dumps(_redact_alert_data(aggs, reveal_owned=params.reveal_owned), indent=2, default=str)[:CHARACTER_LIMIT]}\n```"

    return _truncate_if_needed(json.dumps(_redact_alert_data(data, reveal_owned=params.reveal_owned), indent=2, default=str))
