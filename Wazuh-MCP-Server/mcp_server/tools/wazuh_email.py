#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Wazuh email lookup tool - scan alerts for email addresses
"""
from __future__ import annotations
import json, re, logging
from typing import Optional, Literal
from collections import Counter
import httpx
from pydantic import BaseModel, ConfigDict, Field
from mcp_server import (mcp, WAZUH_INDEXER_URL, WAZUH_INDEXER_PASSWORD,
                        _WAZUH_INDEXER_MAX_SIZE, _BYPASS_REDACTION_DESC, _REDACTION_POLICY_DESC, _REVEAL_OWNED_DESC, _FORENSIC_TOKEN_DESC)
from mcp_server.core.audit import _audit_log, _truncate_if_needed, _escape_md_table
from mcp_server.core.http_client import _handle_api_error
from mcp_server.core.redact import _redact_alert_data
from mcp_server.core.validators import ValidAgentName, ValidKeyword, ValidRuleGroups
from mcp_server.wazuh.time_utils import _parse_time_window
from mcp_server.wazuh.indexer import _wazuh_indexer_post

# Email extraction helper (shared with wazuh_compromised.py)
_EMAIL_PATTERN = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', re.IGNORECASE)


def _extract_emails_from_doc(doc: dict) -> list[str]:
    """Extract email addresses from alert document fields."""
    emails: list[str] = []
    seen = set()
    for field in ("data.account", "data.email", "data.srcuser", "data.dstuser", "full_log"):
        val = doc
        for key in field.split("."):
            val = val.get(key, "") if isinstance(val, dict) else ""
        if isinstance(val, str):
            for m in _EMAIL_PATTERN.findall(val):
                e = m.lower()
                if e not in seen:
                    seen.add(e)
                    emails.append(e)
    return emails

class WazuhEmailLookupInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    agent_name: ValidAgentName = Field(
        default=None,
        max_length=64,
        description="Optional agent name filter (e.g. 'mailbox-new'). Omit to search all agents.",
    )
    since: Optional[str] = Field(
        default=None,
        max_length=30,
        description="Start of time window - ISO 8601 ('2026-07-07T00:00:00Z') or relative "
                    "('5m', '1h', '24h', '7d', '30d'). Defaults to 365 days ago if omitted.",
    )
    until: Optional[str] = Field(
        default=None,
        max_length=30,
        description="End of time window - ISO 8601 or relative expression. Defaults to now if omitted.",
    )
    top_n: int = Field(
        default=100,
        description="Number of top email addresses to return, ranked by frequency.",
        ge=1,
        le=500,
    )
    rule_groups: ValidRuleGroups = Field(
        default=None,
        max_length=1024,
        description="Comma-separated rule groups to filter by "
                    "(e.g. 'authentication_failed,brute_force'). "
                    "Omit to search all rule groups.",
    )
    max_scanned: int = Field(
        default=50000,
        description="Maximum number of alert documents to scan internally. "
                    "Higher values give more accurate counts but take longer.",
        ge=100,
        le=200000,
    )
    response_format: Literal["markdown", "json"] = Field(
        default="markdown",
        description="'markdown' for human-readable report, 'json' for structured data.",
    )
    keyword: ValidKeyword = Field(
        default=None,
        max_length=1024,
        description="Free-text keyword search to further narrow email results. "
                    "Same syntax as blueteam_wazuh_indexer_search.",
    )
    bypass_redaction: bool = Field(
        default=False,
        description="Bypass PII redaction for audit investigations (Layer 1 credentials stay masked).",
    )
    redaction_policy: Optional[Literal["full", "protect_victim", "raw"]] = Field(
        default=None,
        description=_REDACTION_POLICY_DESC,
    )
    reveal_owned: bool = Field(default=False, description=_REVEAL_OWNED_DESC)
    forensic_token: Optional[str] = Field(default=None, max_length=128, description=_FORENSIC_TOKEN_DESC)



@mcp.tool(
    name="wazuh_email_lookup",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def wazuh_email_lookup(params: WazuhEmailLookupInput) -> str:
    """Search Wazuh alerts for email addresses and rank top-N most frequently seen.

    Scans the ``full_log`` field (raw log line) and the structured ``data.account``
    field (Zimbra alerts) for email-address-like strings.  Aggregates every unique
    address with its occurrence count, associated source IPs, and the rule groups
    it appears in.  Results are sorted by frequency descending.

    Querying the full year requires scanning many documents.  The internal scanner
    pages through alerts using ``search_after`` cursors params.until either the Indexer
    is exhausted or ``params.max_scanned`` documents have been processed.

    Args:
        params.agent_name: Optional agent to filter (e.g. 'mailbox-new')
        params.since: ISO 8601 start (default: 365 days ago)
        params.until: ISO 8601 end (default: now)
        params.top_n: How many top emails to return (1-500, default 100)
        params.rule_groups: Comma-separated groups filter
        params.max_scanned: Hard cap on documents scanned (1000-200000, default 50000)
        params.keyword: Free-text keyword to further narrow results
        params.response_format: 'markdown' or 'json'
        params.bypass_redaction: When true, skip PII/credential redaction
        params.redaction_policy: 'full', 'protect_victim', or 'raw'
        params.reveal_owned: When true, unmask emails/subdomains at owned domains (BLUETEAM_OWNED_DOMAINS)
        params.forensic_token: Forensic unmask token (BLUETEAM_FORENSIC_TOKEN)

    Returns:
        str: Ranked table of email addresses with counts, unique IPs,
        and associated rule categories.  Summary statistics are included.

    Example usage:
        - "Find the top 100 most compromised email addresses in the last year"
        - "Show me the most targeted mailboxes on agent mailbox-new"
    """
    _audit_log("wazuh_email_lookup", {"since": params.since})
    since_str, until_str = _parse_time_window(params.since, params.until)

    rule_group_list: Optional[list[str]] = None
    if params.rule_groups:
        rule_group_list = [g.strip() for g in params.rule_groups.split(",") if g.strip()]

    email_counter: Counter[str] = Counter()
    email_srcips: dict[str, set[str]] = {}    # email -> set of srcip
    email_rules: dict[str, set[str]] = {}     # email -> set of "rule_id: description"
    email_groups: dict[str, set[str]] = {}    # email -> set of rule groups
    email_first_seen: dict[str, str] = {}     # email -> earliest timestamp
    email_last_seen: dict[str, str] = {}      # email -> latest timestamp

    total_scanned = 0
    search_after: Optional[list] = None
    page_size = 1000
    try:
        while total_scanned < params.max_scanned:
            body = {
                "size": page_size,
                "query": {"bool": {"filter": [
                    {"range": {"@timestamp": {"gte": since_str, "lt": until_str,
                                                   "format": "strict_date_optional_time"}}},
                ]}},
                "sort": [{"@timestamp": "asc"}, {"_id": "asc"}],
            }
            if params.agent_name:
                body["query"]["bool"]["filter"].append({"match": {"agent.name": params.agent_name}})
            if rule_group_list:
                body["query"]["bool"]["filter"].append({"terms": {"rule.groups": rule_group_list}})
            if params.keyword:
                body["query"]["bool"]["filter"].append({"query_string": {"query": params.keyword, "lenient": True}})
            if search_after:
                body["search_after"] = search_after
            data = await _wazuh_indexer_post(body)
            if "error" in data:
                error_msg = data["error"]
                # If already collected some data, return partial results. (Aul Adjust)
                if total_scanned > 0:
                    break
                return json.dumps(data, indent=2)

            hits = data.get("hits", {})
            hit_list = hits.get("hits", [])
            docs = [h.get("_source", h) for h in hit_list]
            docs = _redact_alert_data(docs, params=params)
            if not docs:
                break

            for doc in docs:
                emails = _extract_emails_from_doc(doc)
                ts = doc.get("@timestamp", "")
                srcip = (doc.get("data") or {}).get("srcip", "")
                rule = doc.get("rule") or {}
                rule_id = rule.get("id", "")
                rule_desc = rule.get("description", "")
                groups = tuple(rule.get("groups", []))

                for email in emails:
                    email_counter[email] += 1
                    if srcip:
                        email_srcips.setdefault(email, set()).add(srcip)
                    if rule_id:
                        email_rules.setdefault(email, set()).add(f"{rule_id}: {rule_desc}")
                    for g in groups:
                        email_groups.setdefault(email, set()).add(g)
                    if email not in email_first_seen or (ts and ts < email_first_seen[email]):
                        email_first_seen[email] = ts
                    if email not in email_last_seen or (ts and ts > email_last_seen[email]):
                        email_last_seen[email] = ts

            total_scanned += len(docs)

            # Advance cursor or stop if exhausted
            if len(docs) < page_size:
                break
            last_sort = hit_list[-1].get("sort") if hit_list else None
            if last_sort:
                search_after = last_sort
            else:
                break

    except (httpx.HTTPStatusError, httpx.TimeoutException, RuntimeError) as e:
        if total_scanned == 0:
            return _handle_api_error(e, context="wazuh_email_lookup")
        # Partial results on transient error during pagination
        logging.getLogger(__name__).warning(
            "wazuh_email_lookup: error after %d docs scanned: %s", total_scanned, e
        )

    # Rank by frequency
    top_emails = email_counter.most_common(params.top_n)

    # Stats
    total_unique = len(email_counter)
    total_with_auth_fail = sum(
        1 for e in email_counter
        if any("authentication_fail" in g.lower() for g in email_groups.get(e, set()))
    )
    total_with_brute_force = sum(
        1 for e in email_counter
        if any("brute" in g.lower() for g in email_groups.get(e, set()))
    )
    high_freq = sum(1 for _, c in email_counter.items() if c >= 10)

    if params.response_format == "json":
        results = []
        for email, count in top_emails:
            results.append({
                "email": email,
                "count": count,
                "unique_srcips": len(email_srcips.get(email, set())),
                "top_srcips": sorted(email_srcips.get(email, set()))[:20],
                "rule_groups": sorted(email_groups.get(email, set())),
                "top_rules": sorted(email_rules.get(email, set()))[:10],
                "first_seen": email_first_seen.get(email),
                "last_seen": email_last_seen.get(email),
            })
        output = {
            "results": results,
            "summary": {
                "total_emails_found": total_unique,
                "documents_scanned": total_scanned,
                "time_window": {"since": since_str, "until": until_str},
                "auth_failure_emails": total_with_auth_fail,
                "brute_force_emails": total_with_brute_force,
                "emails_with_10plus_appearances": high_freq,
            },
            "query": {
                "agent_name": params.agent_name,
                "rule_groups": params.rule_groups,
                "since": since_str,
                "until": until_str,
                "max_scanned": params.max_scanned,
            },
        }
        return _truncate_if_needed(json.dumps(output, indent=2, ensure_ascii=False))

    # Markdown output
    lines: list[str] = [
        f"# Wazuh Email Lookup - Top {len(top_emails)} Emails",
        "",
        f"**Time window**: {since_str} to {until_str}",
        f"**Documents scanned**: {total_scanned:,}",
        f"**Unique emails found**: {total_unique:,}",
        f"**Agent**: {params.agent_name or 'all agents'}",
        f"**Rule groups**: {params.rule_groups or 'all'}",
        "",
        "## Top Email Addresses",
        "",
        "| # | Email | Count | Unique IPs | Top Rule Groups |",
        "|---|-------|-------|------------|-----------------|",
    ]
    for i, (email, count) in enumerate(top_emails, 1):
        ips = len(email_srcips.get(email, set()))
        top_groups = ", ".join(sorted(email_groups.get(email, set()))[:4])
        lines.append(f"| {i} | {_escape_md_table(email)} | {count:,} | {ips} | {_escape_md_table(top_groups)} |")

    lines.extend([
        "",
        "## Summary Statistics",
        f"- Total unique emails: {total_unique:,}",
        f"- Emails appearing in auth-failure rules: {total_with_auth_fail:,}",
        f"- Emails appearing in brute-force rules: {total_with_brute_force:,}",
        f"- Emails with ≥10 appearances: {high_freq:,}",
        "",
        "## Search Parameters",
        f"- Query: `full_log` contains email pattern (`*@*.*`) OR `data.account` contains `@`",
        f"- Max documents scanned: {params.max_scanned:,}",
        f"- Page size: {page_size}",
    ])
    return _truncate_if_needed("\n".join(lines))
