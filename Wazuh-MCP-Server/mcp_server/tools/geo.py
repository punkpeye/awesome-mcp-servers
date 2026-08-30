#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Geo distribution tool - country-level attack ranking
"""
import json
from typing import Optional, Literal
from pydantic import BaseModel, ConfigDict, Field
from mcp_server import mcp, WAZUH_INDEXER_URL, WAZUH_INDEXER_PASSWORD, _BYPASS_REDACTION_DESC
from mcp_server.wazuh.indexer import _wazuh_indexer_post, _WAZUH_INDEX_PATTERNS
from mcp_server.wazuh.time_utils import _parse_time_window

from mcp_server.core.tool_decorator import blueteam_tool

class GeoDistributionInput(BaseModel):
    """Input model for blueteam_wazuh_geo_distribution."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    since: Optional[str] = Field(default="24h", max_length=30,
        description="Start of time window.")
    until: Optional[str] = Field(default=None, max_length=30,
        description="End of time window. Defaults to now.")
    top_n: int = Field(default=15, ge=3, le=50,
        description="Number of top countries/cities to return.")
    granularity: Literal["country", "city"] = Field(
        default="country", description="Aggregate by country_name or city_name.")
    response_format: Literal["markdown", "json"] = Field(
        default="markdown", description="'markdown' or 'json'.")
    bypass_redaction: bool = Field(
        default=False, description=_BYPASS_REDACTION_DESC)


@blueteam_tool(
    name="blueteam_wazuh_geo_distribution",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": False},
)
async def blueteam_wazuh_geo_distribution(params: GeoDistributionInput) -> str:
    """Show top attacking countries by alert volume using Wazuh GeoIP data.

    Pure aggregation - zero documents fetched (size: 0). Returns a country
    ranking with alert counts and unique IP counts. Uses Wazuh Indexer's
    built-in GeoLocation.country_name field.

    **Required Permissions**: Wazuh Indexer read access.

    **Worked Examples**

    1. *Last 24h*:
       ``blueteam_wazuh_geo_distribution()``

    2. *Last 7 days, top 25*:
       ``blueteam_wazuh_geo_distribution(since="7d", top_n=25)``

    3. *Specific date range*:
       ``blueteam_wazuh_geo_distribution(since="2026-07-17T00:00:00Z", until="2026-07-18T00:00:00Z")``
    """
    if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
        return json.dumps({"error": "WAZUH_INDEXER_URL and WAZUH_INDEXER_PASSWORD must be set."})

    since_iso, until_iso = _parse_time_window(params.since, params.until)

    is_city = params.granularity == "city"
    geo_field = "GeoLocation.city_name" if is_city else "GeoLocation.country_name"
    geo_label = "City" if is_city else "Country"

    body = {
        "size": 0,
        "query": {"bool": {"filter": [
            {"range": {"@timestamp": {"gte": since_iso, "lt": until_iso,
                                       "format": "strict_date_optional_time"}}},
            {"exists": {"field": geo_field}},
        ]}},
        "aggs": {
            "by_geo": {
                "terms": {"field": geo_field, "size": params.top_n,
                          "order": {"_count": "desc"}},
                "aggs": {
                    "unique_ips": {
                        "cardinality": {"field": "data.srcip",
                                        "precision_threshold": 40000},
                    },
                    "top_rules": {
                        "terms": {"field": "rule.id", "size": 3},
                    },
                },
            },
            "total_with_geo": {"value_count": {"field": geo_field}},
        },
    }
    raw = await _wazuh_indexer_post(body)
    if "error" in raw:
        return raw

    aggs = raw.get("aggregations", {})
    total_with_geo = aggs.get("total_with_geo", {}).get("value", 0)
    buckets = aggs.get("by_geo", {}).get("buckets", [])

    if params.response_format == "json":
        return json.dumps({
            "window": {"since": since_iso, "until": until_iso},
            "granularity": params.granularity,
            "total_alerts_with_geo": total_with_geo,
            geo_label.lower() + "s": [
                {"name": b["key"], "alerts": b["doc_count"],
                 "unique_ips": b.get("unique_ips", {}).get("value", 0),
                 "top_rules": [r["key"] for r in b.get("top_rules", {}).get("buckets", [])]}
                for b in buckets
            ],
        }, indent=2, ensure_ascii=False)

    lines = [
        f"# {'🏙️' if is_city else '🌍'} Attack Geography — `{since_iso}` → `{until_iso}`",
        "",
        f"**Granularity**: {geo_label}",
        f"**Alerts with GeoIP data**: {total_with_geo:,}",
        "",
        f"| {geo_label} | Alerts | Unique IPs | Top Rules |",
        "|---------|--------|------------|-----------|",
    ]
    for b in buckets:
        ips = b.get("unique_ips", {}).get("value", 0)
        rules = ", ".join(f"`{r['key']}`" for r in b.get("top_rules", {}).get("buckets", [])[:2]) or "-"
        lines.append(f"| {b['key']} | {b['doc_count']:,} | {ips:,} | {rules} |")

    if not buckets:
        lines.append("| *(no data)* | - | - | - |")
        lines.append("")
        lines.append("> ⚠️ GeoIP enrichment may not be enabled on this Wazuh Indexer. "
                     "Check that the GeoIP processor is configured.")

    return "\n".join(lines)
