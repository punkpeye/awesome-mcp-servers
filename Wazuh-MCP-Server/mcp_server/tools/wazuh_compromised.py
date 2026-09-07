#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Wazuh compromised emails analysis tool
"""
from __future__ import annotations
import json, re, os, asyncio, logging
from typing import Optional, Literal
from collections import Counter
import httpx
from pydantic import BaseModel, ConfigDict, Field, field_validator
from mcp_server import (mcp, WAZUH_INDEXER_URL, WAZUH_INDEXER_PASSWORD,
                        _WAZUH_INDEXER_MAX_SIZE, _BYPASS_REDACTION_DESC, _REVEAL_OWNED_DESC,
                        NETRA_API_KEY_ENV, NETRA_VERIFY_SSL, NETRA_BASE_URL, _AGENT_NAME_DESC,
                        _SINCE_DESC, _RESPONSE_FORMAT_DESC, _UNTIL_DESC)
from mcp_server.core.audit import _audit_log, _truncate_if_needed, _escape_md_table
from mcp_server.core.redact import _redact_alert_data
from mcp_server.core.http_client import _api_call, _handle_api_error
from mcp_server.wazuh.indexer import _wazuh_indexer_post, _WAZUH_INDEX_PATTERNS, _KEYWORD_SEARCH_FIELDS
from mcp_server.wazuh.time_utils import _parse_time_window, _auto_bucket_interval, _duration_minutes
from mcp_server.tools.wazuh_email import _extract_emails_from_doc
from mcp_server.core.validators import ValidAgentName, ValidKeyword

class WazuhCompromisedEmailsAnalysisInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    emails: list[str] = Field(
        default=[],
        max_length=50,
        description="List of email addresses to analyze (e.g. from wazuh_email_lookup). "
                    "If empty, auto-discovers compromised emails from the indexer.",
    )
    agent_name: ValidAgentName = Field(
        default=None,
        max_length=64,
        description=_AGENT_NAME_DESC,
    )
    since: Optional[str] = Field(
        default=None,
        max_length=30,
        description=_SINCE_DESC,
    )
    until: Optional[str] = Field(
        default=None,
        max_length=30,
        description=_UNTIL_DESC,
    )
    top_ips: int = Field(
        default=20,
        description="Number of top attacker IPs to return, ranked by alert count.",
        ge=1,
        le=100,
    )
    enrich_with_netra: bool = Field(
        default=False,
        description="If true, query Netra for each attacker IP (adds latency). "
                    "Rate limiting applies. Only top 10 IPs are enriched.",
    )
    keyword: ValidKeyword = Field(
        default=None,
        max_length=1024,
        description="Free-text keyword search to further narrow results. "
                    "Same syntax as blueteam_wazuh_indexer_search.",
    )
    response_format: Literal["markdown", "json"] = Field(
        default="markdown",
        description="_RESPONSE_FORMAT_DESC",
    )
    reveal_owned: bool = Field(default=False, description=_REVEAL_OWNED_DESC)

    @field_validator("emails")
    @classmethod
    def validate_emails(cls, v: list[str]) -> list[str]:
        cleaned: list[str] = []
        for email in v:
            email = email.strip()
            if not email:
                continue
            if len(email) > 254:
                raise ValueError(f"Email too long: {email[:50]}...")
            if "@" not in email or ".." in email:
                raise ValueError(f"Invalid email format: {email}")
            cleaned.append(email.lower())
        if not cleaned:
            raise ValueError("At least one valid email address is required")
        return cleaned


@mcp.tool(
    name="wazuh_compromised_emails_analysis",
    annotations={
        "readOnlyHint": True,
        "destructiveHint": False,
        "idempotentHint": True,
        "openWorldHint": True,
    },
)
async def wazuh_compromised_emails_analysis(params: WazuhCompromisedEmailsAnalysisInput) -> str:
    """Correlate compromised email addresses with attacker IPs from Wazuh alerts.
    Given a list of email addresses (typically sourced from ``wazuh_email_lookup``),
    queries the Wazuh Indexer for alerts mentioning any of them, extracts and ranks
    the source IPs involved, and optionally enriches the top attacker IPs through
    Netra Threat Intelligence.

    Netra enrichment is **disabled by default** because it adds latency and consumes
    Netra API quota.  Set ``enrich_with_netra=true`` to enable it (max 10 IPs
    enriched regardless of ``params.top_ips``).

    Args:
        params.emails: List of email addresses to analyze (max 50; empty = auto-discover compromised emails from the indexer)
        params.agent_name: Optional agent filter
        params.since: ISO 8601 start (default: 365 days ago)
        params.until: ISO 8601 end (default: now)
        params.top_ips: Number of top attacker IPs to rank (1-100, default 20)
        params.enrich_with_netra: Query Netra for top IPs (default false)
        params.response_format: 'markdown' or 'json'
        params.reveal_owned: When true, unmask emails/subdomains at owned domains (BLUETEAM_OWNED_DOMAINS)

    Returns:
        str: Ranked attacker IP list with targeted email counts, plus per-email
        breakdown.  If params.enrich_with_netra is true, Netra threat scores are included
        for the top 10 IPs.

    Example usage:
        - "Take the top 5 params.emails from the lookup and find who's attacking them"
        - "Enrich the attacker IPs for these compromised accounts through Netra"
    """
    _audit_log("wazuh_compromised_emails_analysis", {"top_ips": params.top_ips, "since": params.since})
    since_str, until_str = _parse_time_window(params.since, params.until)

    # Auto-discover compromised emails when none provided (LLM convenience)
    if not params.emails:
        from mcp_server.tools.wazuh_email import wazuh_email_lookup, WazuhEmailLookupInput
        try:
            lookup_out = await wazuh_email_lookup(WazuhEmailLookupInput(
                since=params.since, until=params.until,
                top_n=min(params.top_ips, 50), response_format="json"))
            lookup = json.loads(lookup_out)
            # wazuh_email_lookup returns {"results": [{email, count, ...}], ...}
            discovered = [e.get("email") for e in lookup.get("results", []) if e.get("email")]
            params.emails = discovered[:50]
            _audit_log("wazuh_compromised_emails_analysis.auto_discover",
                       {"count": len(params.emails)})
        except Exception as e:
            return json.dumps({"error": f"Auto-discovery failed and no emails provided: {e}"},
                              indent=2)
        if not params.emails:
            return json.dumps({"error": "No compromised emails found in the window. "
                                        "Provide explicit emails=[] list or widen the time window."},
                              indent=2)

    ip_counter: Counter[str] = Counter()
    ip_to_emails: dict[str, set[str]] = {}  # IP -> set of targeted params.emails
    email_to_ips: dict[str, Counter[str]] = {}  # email -> IP counter
    email_alert_counts: Counter[str] = Counter()  # email -> total alert count
    total_scanned = 0

    # Fan out across email batches (max 25 per API call)
    batch_size = 25
    try:
        for i in range(0, len(params.emails), batch_size):
            batch = params.emails[i:i + batch_size]
            search_after: Optional[list] = None
            page_size = 1000
            batch_scanned = 0
            max_batch_scanned = 20000  # per-batch cap to prevent runaway

            while batch_scanned < max_batch_scanned:
                body = {
                    "size": page_size,
                    "query": {"bool": {"filter": [
                        {"range": {"@timestamp": {"gte": since_str, "lt": until_str,
                                                       "format": "strict_date_optional_time"}}},
                        {"bool": {"should": [{"match": {"data.account": e}} for e in batch],
                                   "minimum_should_match": 1}},
                    ]}},
                    "sort": [{"@timestamp": "asc"}, {"_id": "asc"}],
                }
                if params.agent_name:
                    body["query"]["bool"]["filter"].append({"match": {"agent.name": params.agent_name}})
                if params.keyword:
                    body["query"]["bool"]["filter"].append({"query_string": {"query": params.keyword, "lenient": True}})
                if search_after:
                    body["search_after"] = search_after
                data = await _wazuh_indexer_post(body)
                if "error" in data:
                    # Accumulate partial results
                    break

                hits = data.get("hits", {})
                hit_list = hits.get("hits", [])
                docs = [h.get("_source", h) for h in hit_list]
                docs = _redact_alert_data(docs, bypass=False, reveal_owned=params.reveal_owned)
                if not docs:
                    break

                for doc in docs:
                    srcip = (doc.get("data") or {}).get("srcip", "")
                    # Also extract emails from this doc for association
                    doc_emails = _extract_emails_from_doc(doc)
                    # Intersect with our target list
                    matched = set(doc_emails) & set(params.emails)
                    if not matched:
                        continue

                    if srcip:
                        ip_counter[srcip] += 1
                        ip_to_emails.setdefault(srcip, set()).update(matched)
                        for email in matched:
                            email_to_ips.setdefault(email, Counter())[srcip] += 1
                            email_alert_counts[email] += 1

                batch_scanned += len(docs)
                total_scanned += len(docs)

                if len(docs) < page_size:
                    break
                last_sort = hit_list[-1].get("sort") if hit_list else None
                if last_sort:
                    search_after = last_sort
                else:
                    break

    except (httpx.HTTPStatusError, httpx.TimeoutException, RuntimeError) as e:
        if total_scanned == 0:
            return _handle_api_error(e, context="wazuh_compromised_emails_analysis")
        logging.getLogger(__name__).warning(
            "wazuh_compromised_emails_analysis: error after %d docs: %s", total_scanned, e
        )

    top_ips = ip_counter.most_common(params.top_ips)

    # Netra enrichment for top IPs (max 10)
    netra_results: dict[str, dict] = {}
    if params.enrich_with_netra:
        enrich_count = min(len(top_ips), 10)
        netra_key = os.environ.get(NETRA_API_KEY_ENV, "")
        for ip, _ in top_ips[:enrich_count]:
            try:
                netra_resp = await _api_call("get", f"{NETRA_BASE_URL}/analysis/{ip}",
                    headers={"X-API-Key": netra_key, "Accept": "application/json"},
                    verify=NETRA_VERIFY_SSL)
                raw = netra_resp.json()
                data = raw.get("data", {})
                results = data.get("results", {})
                ts = results.get("threat_score", {})
                ai = results.get("ai_insight", {})
                vt = results.get("virustotal", {})
                ab = results.get("abuseipdb", {})
                geo = results.get("ipapi", {})
                netra_results[ip] = {
                    "threat_score": ts.get("score"),
                    "threat_level": ts.get("level"),
                    "breakdown": ts.get("breakdown"),
                    "ai_assessment": ai.get("assessment"),
                    "ai_confidence": ai.get("confidence"),
                    "virustotal_malicious": vt.get("malicious"),
                    "virustotal_total": vt.get("total"),
                    "abuseipdb_confidence": ab.get("abuseConfidenceScore"),
                    "abuseipdb_total_reports": ab.get("totalReports"),
                    "country": (geo.get("location") or {}).get("country"),
                    "country_name": geo.get("country_name"),
                    "isp": geo.get("isp"),
                }
                # Rate limit : 1s delay between Netra calls
                await asyncio.sleep(1)
            except (httpx.HTTPStatusError, httpx.TimeoutException, Exception) as e:
                netra_results[ip] = {"error": str(e)}

    if params.response_format == "json":
        attacker_ips = []
        for ip, count in top_ips:
            entry: dict = {
                "ip": ip,
                "alert_count": count,
                "targeted_emails": sorted(ip_to_emails.get(ip, set())),
                "targeted_email_count": len(ip_to_emails.get(ip, set())),
            }
            if ip in netra_results:
                entry["netra"] = netra_results[ip]
            attacker_ips.append(entry)

        per_email: dict[str, dict] = {}
        for email in params.emails:
            ips_for_email = email_to_ips.get(email, Counter())
            per_email[email] = {
                "total_alerts": email_alert_counts.get(email, 0),
                "attacker_ips": [
                    {"ip": ip, "count": c}
                    for ip, c in ips_for_email.most_common(20)
                ],
            }

        output = {
            "emails_analyzed": params.emails,
            "total_alerts_scanned": total_scanned,
            "top_attacker_ips": attacker_ips,
            "per_email": per_email,
            "enrichment_enabled": params.enrich_with_netra,
            "time_window": {"since": since_str, "until": until_str},
        }
        return _truncate_if_needed(json.dumps(output, indent=2, ensure_ascii=False))

    # Markdown output
    lines: list[str] = [
        "# Compromised Email Analysis",
        "",
        f"**Time window**: {since_str} to {until_str}",
        f"**Emails analyzed**: {len(params.emails)}",
        f"**Agent**: {params.agent_name or 'all agents'}",
        f"**Alerts scanned**: {total_scanned:,}",
        "",
        "## Top Attacker IPs",
        "",
    ]
    if params.enrich_with_netra:
        lines.append(
            "| # | IP | Alert Count | Targeted Emails | Netra Score | Netra Level | Country |"
        )
        lines.append(
            "|---|----|------------|-----------------|-------------|-------------|---------|"
        )
        for i, (ip, count) in enumerate(top_ips, 1):
            targeted = len(ip_to_emails.get(ip, set()))
            nr = netra_results.get(ip, {})
            score = nr.get("threat_score", "-")
            level = nr.get("threat_level", "-")
            country = nr.get("country_name") or nr.get("country") or "-"
            lines.append(
                f"| {i} | {_escape_md_table(ip)} | {count:,} | {targeted} | {score} | {_escape_md_table(str(level))} | {_escape_md_table(str(country))} |"
            )
    else:
        lines.append(
            "| # | IP | Alert Count | Targeted Emails |"
        )
        lines.append(
            "|---|----|------------|-----------------|"
        )
        for i, (ip, count) in enumerate(top_ips, 1):
            targeted = len(ip_to_emails.get(ip, set()))
            lines.append(f"| {i} | {_escape_md_table(ip)} | {count:,} | {targeted} |")

    lines.append("")
    lines.append("## Per-Email Summary")
    lines.append("")
    for email in params.emails:
        alert_count = email_alert_counts.get(email, 0)
        lines.append(f"### {email} ({alert_count:,} alerts)")
        ips_for_email = email_to_ips.get(email, Counter())
        if ips_for_email:
            lines.append("| IP | Count | Netra Level |")
            lines.append("|----|-------|-------------|")
            for ip, c in ips_for_email.most_common(10):
                level = (netra_results.get(ip) or {}).get("threat_level", "-")
                lines.append(f"| {_escape_md_table(ip)} | {c:,} | {_escape_md_table(str(level))} |")
        else:
            lines.append("_No attacker IPs found for this email._")
        lines.append("")

    if params.enrich_with_netra and netra_results:
        lines.append("## Netra Enrichment (top attacker IPs)")
        lines.append("")
        for ip, nr in netra_results.items():
            if "error" in nr:
                lines.append(f"### {ip} — Error: {nr['error']}")
                continue
            score = nr.get("threat_score", "-")
            level = nr.get("threat_level", "-")
            ai = nr.get("ai_assessment") or "No AI assessment available"
            vt = f"{nr.get('virustotal_malicious', '-')}/{nr.get('virustotal_total', '-')}"
            ab = (
                f"Confidence {nr.get('abuseipdb_confidence', '-')}%, "
                f"{nr.get('abuseipdb_total_reports', '-')} reports"
            )
            country = nr.get("country_name") or nr.get("country") or "-"
            isp = nr.get("isp") or "-"
            lines.append(f"### {ip} — Threat Level: {level} (Score: {score}/100)")
            lines.append(f"- **AI Assessment**: {ai}")
            lines.append(f"- **VirusTotal**: {vt} malicious")
            lines.append(f"- **AbuseIPDB**: {ab}")
            lines.append(f"- **Country**: {country}   |   **ISP**: {isp}")
            lines.append("")
    elif params.enrich_with_netra and not netra_results:
        lines.append("## Netra Enrichment")
        lines.append("")
        lines.append(
            "_Netra enrichment was enabled but no results were obtained. "
            "Check that NETRA_API_KEY is set._"
        )
    else:
        lines.append(
            "_Netra enrichment was disabled. Set `enrich_with_netra=true` to enable "
            "threat intelligence enrichment for attacker IPs._"
        )

    return _truncate_if_needed("\n".join(lines))


