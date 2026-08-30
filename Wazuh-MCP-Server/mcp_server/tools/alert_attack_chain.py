#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
F-3: Attack chain analysis — rule-to-rule transition graphs, kill-chain pattern matching
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
from mcp_server.core.constants import _KNOWN_ATTACK_CHAINS
from mcp_server.wazuh.indexer import _wazuh_indexer_post, _WAZUH_INDEX_PATTERNS
from mcp_server.wazuh.time_utils import _parse_time_window, _duration_minutes
from mcp_server.threat_intel.crowdsec import _crowdsec_request

# 1: Alert Summarization
# Auto-extracted from alert_enrichment.py - modular refactor (2026-08-11 - AUL)
class AttackChainInput(BaseModel):
    """Input model for blueteam_attack_chain."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    srcip: str = Field(
        ...,
        min_length=7,
        max_length=45,
        description="Source IP to analyze for attack progression chains.",
    )
    since: Optional[str] = Field(
        default="24h",
        max_length=30,
        description="Start of time window.",
    )
    until: Optional[str] = Field(
        default=None,
        max_length=30,
        description="End of time window.",
    )
    min_transitions: int = Field(
        default=2,
        ge=2,
        le=100,
        description="Minimum rule transitions to consider a chain.",
    )
    response_format: Literal["markdown", "json"] = Field(
        default="markdown",
        description="Output format: 'markdown' or 'json'.",
    )


@mcp.tool(
    name="blueteam_attack_chain",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": False,
    },
)
async def blueteam_attack_chain(params: AttackChainInput) -> str:
    """Analyze rule-to-rule transitions to reconstruct attack kill-chain progression.

    Fetches all alerts for a source IP ordered by timestamp, builds a
    Markov transition graph of ``rule.id`` sequences, and matches observed
    transitions against known attack chains (recon -> bruteforce -> access -> C2/response).

    Returns matched chains with confidence scores, the full transition
    matrix, and a timeline of key transitions.

    **Required Permissions**: Wazuh Indexer user with ``read`` access.

    **Worked Examples**

    1. *Default 24h*:
       ``blueteam_attack_chain(srcip="103.107.116.202")``

    2. *7-day forensic window*:
       ``blueteam_attack_chain(srcip="103.107.116.202", since="7d")``

    3. *Require 3+ transitions*:
       ``blueteam_attack_chain(srcip="103.107.116.202", min_transitions=3)``
    """
    _audit_log("blueteam_attack_chain", {"srcip": params.srcip})
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
        "_source": ["@timestamp", "rule.id", "rule.description", "rule.level", "rule.mitre.tactic"],
    }
    raw = await _wazuh_indexer_post(body)
    if "error" in raw:
        return json.dumps(raw, indent=2)

    hits = raw.get("hits", {}).get("hits", [])
    docs = [h.get("_source", h) for h in hits]

    if len(docs) < params.min_transitions:
        result = {
            "srcip": params.srcip,
            "total_events": len(docs),
            "verdict": "insufficient_data",
            "detail": f"Need at least {params.min_transitions} rule transitions.",
        }
        return json.dumps(result, indent=2) if params.response_format == "json" else (
            f"# Attack Chain — `{params.srcip}`\n\n"
            f"**Insufficient data**: {len(docs)} events (need ≥{params.min_transitions} transitions).")

    # Build rule sequence and transition matrix
    rule_seq: list[str] = []
    rule_info: dict[str, dict[str, str]] = {}
    for d in docs:
        rid = str(d.get("rule", {}).get("id", "unknown"))
        rule_seq.append(rid)
        if rid not in rule_info:
            rule_info[rid] = {
                "description": str(d.get("rule", {}).get("description", rid)),
                "level": str(d.get("rule", {}).get("level", "?")),
            }

    # Compress consecutive duplicates (Aul Adjusted : same rule firing repeatedly = persistence, not a transition)
    compressed: list[str] = [rule_seq[0]]
    for rid in rule_seq[1:]:
        if rid != compressed[-1]:
            compressed.append(rid)

    transitions: list[tuple[str, str]] = []
    for i in range(len(compressed) - 1):
        transitions.append((compressed[i], compressed[i + 1]))

    # Count transitions
    trans_counter: Counter[tuple[str, str]] = Counter(transitions)

    # Match against known attack chains
    chain_matches: list[dict[str, Any]] = []
    for chain in _KNOWN_ATTACK_CHAINS:
        chain_ids = [rid for rid, _ in transitions]
        # Check if the compressed sequence contains the ordered pattern
        # Use a subsequence match: each phase must appear in order, not necessarily consecutive
        pattern = chain["pattern"]
        seq_idx = 0
        matched_ids: list[str] = []
        for rid in compressed:
            if seq_idx < len(pattern) and pattern[seq_idx].search(rid):
                matched_ids.append(rid)
                seq_idx += 1
        if seq_idx >= 2:  # at least 2 phases matched
            # Compute observed phase-by-phase transition details
            phase_detail: list[dict[str, Any]] = []
            for j in range(len(matched_ids) - 1):
                phase_detail.append({
                    "from_phase": chain["phases"][j],
                    "to_phase": chain["phases"][j + 1],
                    "from_rule": matched_ids[j],
                    "to_rule": matched_ids[j + 1],
                })
            adjusted_conf = chain["confidence"] * min(1.0, seq_idx / len(pattern))
            chain_matches.append({
                "chain_id": chain["id"],
                "description": chain["description"],
                "confidence": round(adjusted_conf, 2),
                "phases_matched": seq_idx,
                "phases_total": len(pattern),
                "matched_rules": matched_ids[:8],
                "phase_transitions": phase_detail,
            })
    chain_matches.sort(key=lambda c: c["confidence"], reverse=True)

    if params.response_format == "json":
        result = {
            "srcip": params.srcip,
            "window": {"since": since_iso, "until": until_iso},
            "total_events": len(docs),
            "unique_rules": len(rule_info),
            "transitions_observed": len(transitions),
            "compressed_sequence": compressed[:50],
            "rule_info": rule_info,
            "top_transitions": [
                {"from": f, "to": t, "count": c}
                for (f, t), c in trans_counter.most_common(15)
            ],
            "chain_matches": chain_matches,
        }
        return _truncate_if_needed(json.dumps(result, indent=2, ensure_ascii=False))

    # Markdown report
    lines = [
        f"# Attack Chain — `{params.srcip}`",
        "",
        f"- **Window**: `{since_iso}` → `{until_iso}`",
        f"- **Events**: {len(docs)} → {len(compressed)} distinct rule transitions",
        f"- **Unique rules triggered**: {len(rule_info)}",
        "",
    ]

    if chain_matches:
        lines.append("## 🎯 Matched Kill-Chain Patterns")
        lines.append("")
        for cm in chain_matches[:5]:
            conf_bar = "█" * int(cm["confidence"] * 10) + "░" * (10 - int(cm["confidence"] * 10))
            lines.append(f"### {cm['chain_id']} (confidence: {cm['confidence']:.2f})")
            lines.append(f"`[{conf_bar}]`")
            lines.append(f"{cm['description']}")
            lines.append(f"- **Phases matched**: {cm['phases_matched']}/{cm['phases_total']}")
            # Draw ASCII chain
            arrow_parts: list[str] = []
            for pt in cm.get("phase_transitions", []):
                arrow_parts.append(
                    f"`{pt['from_phase']}`[{pt['from_rule']}] → "
                    f"`{pt['to_phase']}`[{pt['to_rule']}]"
                )
            lines.append(f"- **Path**: {' → '.join(arrow_parts) if arrow_parts else '(see matched_rules)'}")
            lines.append("")
    else:
        lines.append("## No known attack chain matched")
        lines.append("")

    # Compressed sequence visualization
    lines.append("## Rule Transition Sequence")
    lines.append("")
    lines.append("```")
    for i, rid in enumerate(compressed[:30]):
        info = rule_info.get(rid, {})
        desc = info.get("description", "?")[:70]
        lvl = info.get("level", "?")
        arrow = " → " if i < len(compressed[:30]) - 1 else ""
        lines.append(f"  [{lvl}] {rid} ({desc}){arrow}")
    if len(compressed) > 30:
        lines.append(f"  ... and {len(compressed) - 30} more transitions")
    lines.append("```")

    # Top transitions table
    if trans_counter:
        lines.append("")
        lines.append("## Top Rule Transitions")
        lines.append("")
        lines.append("| From | To | Count |")
        lines.append("|------|----|-------|")
        for (f, t), c in trans_counter.most_common(10):
            lines.append(f"| `{f}` | `{t}` | {c} |")

    return _truncate_if_needed("\n".join(lines))


# 5: Threat Card Generation (AUL Adjusted)
