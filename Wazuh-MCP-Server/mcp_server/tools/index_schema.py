#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Index schema explorer — discover field names/types before building aggregations.

Prevents the most common silent false-negative: querying ``field.keyword``
when the index stores ``field`` as a plain ``keyword`` type (or vice versa).
"""
from __future__ import annotations
import json, re
from typing import Optional, Literal, Any
from pydantic import BaseModel, ConfigDict, Field

from mcp_server import mcp
from mcp_server.core.audit import _audit_log, _truncate_if_needed
from mcp_server.wazuh.indexer import _wazuh_indexer_mapping, _WAZUH_INDEX_PATTERNS

# Common Wazuh fields the SOC workflow queries — pre-listed for convenience
_COMMON_FIELDS = [
    "data.srcip", "data.srcip2", "data.src_ip", "data.client_ip", "data.remote_ip",
    "data.source_ip", "data.ip", "srcip",
    "data.domain", "data.url", "data.account", "data.error", "data.user_agent",
    "rule.id", "rule.level", "rule.groups", "rule.description", "rule.mitre.id",
    "rule.mitre.tactic", "rule.mitre.technique",
    "agent.name", "agent.id", "agent.ip",
    "GeoLocation.country_name", "GeoLocation.city_name", "GeoLocation.location",
    "@timestamp", "full_log", "decoder.name", "location",
]


def _flatten_props(prefix: str, props: dict, out: dict) -> None:
    """Recursively flatten nested ``properties`` into dotted field paths."""
    for name, spec in props.items():
        path = f"{prefix}.{name}" if prefix else name
        if isinstance(spec, dict) and "properties" in spec:
            _flatten_props(path, spec["properties"], out)
            continue
        out[path] = spec


def _field_info(spec: dict) -> dict:
    """Extract type + keyword sub-field presence from a mapping spec."""
    ftype = spec.get("type", "object")
    has_keyword = False
    fields = spec.get("fields", {})
    if "keyword" in fields:
        has_keyword = True
    return {"type": ftype, "has_keyword_subfield": has_keyword,
            "agg_safe": (ftype in ("keyword", "long", "integer", "double", "date", "boolean", "ip")
                         or has_keyword)}


class IndexSchemaInput(BaseModel):
    """Input model for blueteam_index_schema."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    index: str = Field(
        default="wazuh-alerts-*",
        max_length=128,
        description="Index pattern: 'wazuh-alerts-*' (alerts), 'wazuh-events-*', "
                    "or 'wazuh-states-vulnerabilities-*'.",
    )
    fields: list[str] = Field(
        default=[],
        max_length=50,
        description="Specific dotted fields to inspect (e.g. ['data.srcip', 'rule.groups']). "
                    "Empty = list ALL fields in the index mapping.",
    )
    response_format: Literal["markdown", "json"] = Field(default="markdown")


@mcp.tool(
    name="blueteam_index_schema",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": False},
)
async def blueteam_index_schema(params: IndexSchemaInput) -> str:
    """Discover Wazuh Indexer field names and types before building queries.

    Returns each field's type and whether it has a ``.keyword`` sub-field.
    Use this BEFORE aggregation queries to avoid the silent false-negative
    where ``field.keyword`` doesn't exist (index stores plain ``keyword``).

    **Worked Examples**

    1. *Inspect specific fields for aggregation safety*:
       ``blueteam_index_schema(fields=["data.srcip", "rule.groups", "agent.name"])``

    2. *List the full mapping*:
       ``blueteam_index_schema(index="wazuh-alerts-*")``

    3. *JSON output*:
       ``blueteam_index_schema(fields=["rule.id"], response_format="json")``
    """
    _audit_log("blueteam_index_schema", {"index": params.index, "fields": params.fields})

    raw = await _wazuh_indexer_mapping(params.index)
    if isinstance(raw, dict) and "error" in raw:
        return json.dumps(raw, indent=2)

    # Merge all indices' mappings into one flattened dict
    all_fields: dict[str, dict] = {}
    for index_name, index_body in raw.items():
        props = index_body.get("mappings", {}).get("properties", {})
        _flatten_props("", props, all_fields)

    # Determine target fields
    if params.fields:
        targets = params.fields
    else:
        targets = sorted(all_fields.keys())

    results = []
    for f in targets:
        spec = all_fields.get(f)
        if spec is None:
            results.append({"field": f, "exists": False,
                            "type": None, "has_keyword_subfield": False,
                            "agg_safe": False})
        else:
            info = _field_info(spec)
            results.append({"field": f, "exists": True, **info})

    if params.response_format == "json":
        return _truncate_if_needed(json.dumps({
            "index": params.index,
            "total_fields_in_mapping": len(all_fields),
            "queried_fields": len(results),
            "results": results,
        }, indent=2))

    lines = [f"# Index Schema — `{params.index}`", "",
             f"**Total fields in mapping**: {len(all_fields)}", ""]
    lines.append("| Field | Type | .keyword? | Agg-Safe |")
    lines.append("|-------|------|-----------|----------|")
    for r in results:
        if not r["exists"]:
            lines.append(f"| `{r['field']}` | ❌ NOT FOUND | — | — |")
        else:
            kw = "✅" if r["has_keyword_subfield"] else "—"
            agg = "✅" if r["agg_safe"] else "⚠️ use .keyword or re-map"
            lines.append(f"| `{r['field']}` | `{r['type']}` | {kw} | {agg} |")
    lines.append("")
    lines.append("_Tip: `agg_safe=✅` means the field can be used directly in a `terms` aggregation._")
    return _truncate_if_needed("\n".join(lines))
