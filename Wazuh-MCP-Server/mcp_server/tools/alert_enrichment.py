#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Alert enrichment tools - curated report, threat card, attack chain, beacon detect, summarize, compare
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
from mcp_server.core.http_client import _api_call, _get_client, _handle_api_error
from mcp_server.core.validators import ValidAgentName, ValidKeyword, ValidRuleGroups
from mcp_server.wazuh.indexer import _wazuh_indexer_post, _WAZUH_INDEX_PATTERNS
from mcp_server.wazuh.time_utils import _parse_time_window, _duration_minutes
from mcp_server.threat_intel.crowdsec import _crowdsec_request

# 1: Alert Summarization
# Standalone threat-intel + Sangfor + unified scoring tools (remaining after alert-enrichment modular split)
async def blueteam_lookup_ip_abuseipdb(ip: ValidPublicIp, max_age_days: int = 90, response_format: str = "markdown") -> str:
    """Check IP reputation via AbuseIPDB."""
    _audit_log("blueteam_lookup_ip_abuseipdb", {"ip": ip})
    from mcp_server import ABUSEIPDB_API_KEY
    if not ABUSEIPDB_API_KEY:
        return json.dumps({"error": "ABUSEIPDB_API_KEY not set."})
    try:
        client = await _get_client("http")
        resp = await client.get(f"{ABUSEIPDB_BASE_URL}/check",
                                 headers={"Key": ABUSEIPDB_API_KEY, "Accept": "application/json"},
                                 params={"ipAddress": ip, "maxAgeInDays": str(max_age_days)})
        resp.raise_for_status()
        data = resp.json().get("data", {})
        if response_format == "json":
            return _truncate_if_needed(json.dumps({"ip": ip, "abuse_score": data.get("abuseConfidenceScore"), "total_reports": data.get("totalReports"), "country": data.get("countryCode")}, indent=2))
        return _truncate_if_needed(f"# AbuseIPDB - {ip}\n\n- **Abuse Score**: {data.get('abuseConfidenceScore','?')}%\n- **Reports**: {data.get('totalReports','?')}\n- **Country**: {data.get('countryCode','?')}")
    except Exception as e:
        return _handle_api_error(e, context="abuseipdb")


class VirusTotalHashInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    hash: str = Field(..., max_length=64, description="File hash (MD5/SHA1/SHA256)")
    response_format: str = Field(default="markdown", description="'markdown' or 'json'")


# VirusTotal Hash
@mcp.tool(
    name="blueteam_lookup_hash_virustotal",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def blueteam_lookup_hash_virustotal(params: VirusTotalHashInput) -> str:
    """Check file hash reputation via VirusTotal.

    Args:
        params.hash: File hash (MD5/SHA1/SHA256)
        params.response_format: 'markdown' or 'json'
    """
    _audit_log("blueteam_lookup_hash_virustotal", {"hash": params.hash})
    from mcp_server import VIRUSTOTAL_API_KEY
    if not VIRUSTOTAL_API_KEY:
        return json.dumps({"error": "VIRUSTOTAL_API_KEY not set."})
    try:
        client = await _get_client("http")
        resp = await client.get(f"{VIRUSTOTAL_BASE_URL}/files/{params.hash}",
                                 headers={"x-apikey": VIRUSTOTAL_API_KEY, "Accept": "application/json"})
        resp.raise_for_status()
        data = resp.json().get("data", {}).get("attributes", {})
        stats = data.get("last_analysis_stats", {})
        if params.response_format == "json":
            return _truncate_if_needed(json.dumps({"hash": params.hash, "malicious": stats.get("malicious", 0), "suspicious": stats.get("suspicious", 0), "harmless": stats.get("harmless", 0)}, indent=2))
        return _truncate_if_needed(f"# VirusTotal Hash - {params.hash}\n\n- **Malicious**: {stats.get('malicious',0)}\n- **Suspicious**: {stats.get('suspicious',0)}\n- **Harmless**: {stats.get('harmless',0)}")
    except Exception as e:
        return _handle_api_error(e, context="virustotal")


class VirusTotalDomainInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    domain: str = Field(..., max_length=253, description="Domain name")
    response_format: str = Field(default="markdown", description="'markdown' or 'json'")


# VirusTotal Domain
@mcp.tool(
    name="blueteam_lookup_domain_virustotal",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def blueteam_lookup_domain_virustotal(params: VirusTotalDomainInput) -> str:
    """Check domain reputation via VirusTotal.

    Args:
        params.domain: Domain name
        params.response_format: 'markdown' or 'json'
    """
    _audit_log("blueteam_lookup_domain_virustotal", {"domain": params.domain})
    from mcp_server import VIRUSTOTAL_API_KEY
    if not VIRUSTOTAL_API_KEY:
        return json.dumps({"error": "VIRUSTOTAL_API_KEY not set."})
    try:
        client = await _get_client("http")
        resp = await client.get(f"{VIRUSTOTAL_BASE_URL}/domains/{params.domain}",
                                 headers={"x-apikey": VIRUSTOTAL_API_KEY, "Accept": "application/json"})
        resp.raise_for_status()
        data = resp.json().get("data", {}).get("attributes", {})
        stats = data.get("last_analysis_stats", {})
        if params.response_format == "json":
            return _truncate_if_needed(json.dumps({"domain": params.domain, "malicious": stats.get("malicious", 0), "suspicious": stats.get("suspicious", 0), "harmless": stats.get("harmless", 0)}, indent=2))
        return _truncate_if_needed(f"# VirusTotal Domain - {params.domain}\n\n- **Malicious**: {stats.get('malicious',0)}\n- **Suspicious**: {stats.get('suspicious',0)}\n- **Harmless**: {stats.get('harmless',0)}")
    except Exception as e:
        return _handle_api_error(e, context="virustotal")


class ArgusIpLookupInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    ip: ValidPublicIp = Field(..., description="Public IP to query")
    response_format: str = Field(default="markdown", description="'markdown' or 'json'")


# Argus
@mcp.tool(
    name="argus_ip_lookup",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def argus_ip_lookup(params: ArgusIpLookupInput) -> str:
    """Query Argus Threat Intelligence (TangerangKota-CSIRT) aggregating 7 sources.

    Args:
        params.ip: Public IP to query
        params.response_format: 'markdown' or 'json'
    """
    _audit_log("argus_ip_lookup", {"ip": params.ip})
    from mcp_server import ARGUS_API_KEY_ENV, ARGUS_VERIFY_SSL, ARGUS_BASE_URL
    api_key = os.environ.get(ARGUS_API_KEY_ENV, "")
    if not api_key:
        return json.dumps({"error": "ARGUS_API_KEY must be set."})
    try:
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json", "accept": "application/json"}
        resp = await _api_call("post", ARGUS_BASE_URL, client_name="argus", verify=ARGUS_VERIFY_SSL,
                                headers=headers, json={"observable": params.ip})
        if not resp.content:
            return json.dumps({"error": "Argus API returned empty response"})
        raw = resp.json()
        if params.response_format == "json":
            return _truncate_if_needed(json.dumps(raw, indent=2))
        results = raw.get("results", {})
        argus_reports = results.get("argus_reports", {}).get("results", {})
        abuse = results.get("abuseipdb", {}).get("results", {})
        score = argus_reports.get("scores", 0)
        sources = [k for k in results.keys() if results[k].get("success")]
        lines = [f"# Argus - {params.ip}", "",
                 f"- **Score**: {score}",
                 f"- **Sources**: {', '.join(sources)}",
                 ""]
        if abuse:
            lines.append(f"- **AbuseIPDB Confidence**: {abuse.get('abuseConfidenceScore', 0)}%")
            lines.append(f"- **ISP**: {abuse.get('isp', '?')}")
            lines.append(f"- **Country**: {abuse.get('countryName', '?')}")
        return _truncate_if_needed("\n".join(lines))
    except Exception as e:
        return _handle_api_error(e, context="argus")


class NetraIpAnalysisInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    ip: ValidPublicIp = Field(..., description="Public IP to analyze")
    response_format: str = Field(default="markdown", description="'markdown' or 'json'")
    bypass_redaction: bool = Field(default=False, description="When true, skip PII/credential redaction")


# Netra
@mcp.tool(
    name="netra_ip_analysis",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def netra_ip_analysis(params: NetraIpAnalysisInput) -> str:
    """Query Netra Threat Intelligence for IP analysis.

    Args:
        params.ip: Public IP to analyze
        params.response_format: 'markdown' or 'json'
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.
    """
    _audit_log("netra_ip_analysis", {"ip": params.ip})
    from mcp_server import NETRA_API_KEY_ENV, NETRA_VERIFY_SSL, NETRA_BASE_URL
    api_key = os.environ.get(NETRA_API_KEY_ENV, "")
    if not api_key:
        return json.dumps({"error": "NETRA_API_KEY not set."})
    try:
        headers = {"X-API-Key": api_key, "accept": "application/json"}
        resp = await _api_call("get", f"{NETRA_BASE_URL}/analysis/{params.ip}", headers=headers)
        raw = resp.json()
        if params.response_format == "json":
            return _truncate_if_needed(json.dumps(raw, indent=2))
        data = raw.get("data", {}).get("results", {})
        ts = data.get("threat_score", {})
        ai = data.get("ai_insight", {})
        ipapi = data.get("ipapi", {}).get("results", {})
        score = ts.get("score", 0)
        level = ts.get("level", "?")
        sources_ok = ts.get("sources_available", [])
        sources_fail = ts.get("sources_failed", [])
        lines = [f"# Netra — {params.ip}", "",
                 f"- **Score**: {score} ({level})",
                 f"- **Sources OK**: {', '.join(sources_ok) if sources_ok else 'none'}",
                 f"- **Sources Failed**: {', '.join(sources_fail) if sources_fail else 'none'}",
                 ""]
        if ipapi:
            lines.append(f"- **ISP**: {ipapi.get('isp', '?')}")
            lines.append(f"- **Country**: {ipapi.get('country', '?')} ({ipapi.get('city', '?')})")
        if ai.get("success"):
            lines.append(f"- **AI Insight**: {ai.get('insight', '?')[:200]}")
        return _truncate_if_needed("\n".join(lines))
    except Exception as e:
        return _handle_api_error(e, context="netra")


# Sangfor Blocklist
class SangforBlocklistCheckInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    ip: ValidPublicIp = Field(..., min_length=3, max_length=45)
    response_format: str = Field(default="markdown")

class SangforBlocklistListInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    limit: int = Field(default=100, ge=1, le=1000000)
    date_start: str = Field(default="", max_length=24,
                            description="Start date. ISO 8601 (e.g. 2026-08-18T17:27:00Z) or YYYY-MM-DD HH:MM:SS. Defaults to 30 days ago.")
    date_end: str = Field(default="", max_length=24,
                          description="End date. ISO 8601 (e.g. 2026-08-19T17:27:00Z) or YYYY-MM-DD HH:MM:SS. Defaults to now.")
    response_format: str = Field(default="markdown")

@mcp.tool(
    name="sangfor_blocklist_check",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def sangfor_blocklist_check(params: SangforBlocklistCheckInput) -> str:
    """Check if an IP is currently blocked by Sangfor firewall."""
    _audit_log("sangfor_blocklist_check", {"ip": params.ip})
    from mcp_server import SANGFOR_BLOCKLIST_URL, SANGFOR_BLOCKLIST_TOKEN, SANGFOR_BLOCKLIST_VERIFY_SSL
    if not SANGFOR_BLOCKLIST_TOKEN or not SANGFOR_BLOCKLIST_URL:
        return json.dumps({"error": "SANGFOR_BLOCKLIST_TOKEN and SANGFOR_BLOCKLIST_URL must be set."})
    try:
        headers = {"Authorization": f"Bearer {SANGFOR_BLOCKLIST_TOKEN}", "accept": "application/json"}
        resp = await _api_call("get", f"{SANGFOR_BLOCKLIST_URL}/check/{params.ip}", headers=headers)
        raw = resp.json()
        if isinstance(raw, list):
            raw = {"blocked": len(raw) > 0, "entries": raw}
        if params.response_format == "json":
            return _truncate_if_needed(json.dumps(raw, indent=2))
        blocked = raw.get("blocked", False)
        return _truncate_if_needed(f"# Sangfor Blocklist - {params.ip}\n\n- **Blocked**: {blocked}")
    except Exception as e:
        return _handle_api_error(e, context="sangfor")

@mcp.tool(
    name="sangfor_blocklist_list",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def sangfor_blocklist_list(params: SangforBlocklistListInput) -> str:
    """List IPs blocked by Sangfor firewall, optionally filtered by timestamp."""
    _audit_log("sangfor_blocklist_list", {"limit": params.limit,
               "date_start": params.date_start, "date_end": params.date_end})
    from mcp_server import SANGFOR_BLOCKLIST_URL, SANGFOR_BLOCKLIST_TOKEN, SANGFOR_BLOCKLIST_VERIFY_SSL
    if not SANGFOR_BLOCKLIST_TOKEN or not SANGFOR_BLOCKLIST_URL:
        return json.dumps({"error": "SANGFOR_BLOCKLIST_TOKEN and SANGFOR_BLOCKLIST_URL must be set."})
    try:
        headers = {"Authorization": f"Bearer {SANGFOR_BLOCKLIST_TOKEN}", "accept": "application/json"}
        # Build query string with date filters (only when provided)
        query = [f"limit={params.limit}"]
        if params.date_start:
            query.append(f"date_start={params.date_start}")
        if params.date_end:
            query.append(f"date_end={params.date_end}")
        url = f"{SANGFOR_BLOCKLIST_URL}/list?" + "&".join(query)
        resp = await _api_call("get", url, headers=headers)
        raw = resp.json()
        if isinstance(raw, list):
            raw = {"blocked": len(raw) > 0, "count": len(raw), "entries": raw}
        if params.response_format == "json":
            return _truncate_if_needed(json.dumps(raw, indent=2))
        items = raw if isinstance(raw, list) else raw.get("data", [])
        return _truncate_if_needed(f"# Sangfor Blocklist ({len(items)} IPs)\n\n" + "\n".join(f"- `{i.get('ip_address','?')}`" for i in items[:50]))
    except Exception as e:
        return _handle_api_error(e, context="sangfor_list")


# Unified Threat Confidence Scoring
class UnifiedThreatScoreInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    ip: ValidPublicIp = Field(..., min_length=7, max_length=45, description="Public IP to score.")
    response_format: str = Field(default="markdown", description="'markdown' or 'json'.")

    @field_validator("ip")
    @classmethod
    def validate_ip(cls, v: str) -> str:
        v = v.strip()
        try:
            __import__("ipaddress").ip_address(v)
        except ValueError as exc:
            raise ValueError(f"Invalid IP: '{v}'") from exc
        if __import__("ipaddress").ip_address(v).is_private:
            raise ValueError(f"'{v}' is a private IP - this tool accepts public IPs only.")
        return v


@mcp.tool(
    name="blueteam_unified_threat_score",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True},
)
async def blueteam_unified_threat_score(params: UnifiedThreatScoreInput) -> str:
    """Query multiple threat intel sources and return a unified confidence score.

    Aggregates CrowdSec + ThreatFox + AbuseIPDB into a single weighted verdict
    (0.0–1.0) eliminating the need for 3+ sequential LLM tool calls per IP.
    """
    _audit_log("blueteam_unified_threat_score", {"ip": params.ip})

    async def _crowdsec(ip):
        try:
            from mcp_server.threat_intel.crowdsec import _crowdsec_request
            r = await _crowdsec_request(f"/v2/smoke/{ip}"); rep = r.get("reputation","unknown")
            m = {"malicious":1.0,"suspicious":0.5,"known":0.2,"unknown":0.1,"safe":0.0}
            return m.get(rep,0.1), {"reputation":rep,"behaviors":[b.get("name","?") for b in r.get("behaviors",[])[:3]]}
        except Exception: return 0.0, {}

    async def _threatfox(ip):
        try:
            from mcp_server.threat_intel.threatfox import _threatfox_request
            r = await _threatfox_request(ip,False); items = r.get("data",[])
            if not items: return 0.0, {}
            c = max(e.get("confidence_level",0) for e in items)/100.0
            return c, {"malware":items[0].get("malware_printable","?"),"threat_type":items[0].get("threat_type_desc","?"),"confidence":items[0].get("confidence_level",0)}
        except Exception: return 0.0, {}

    async def _abuseipdb(ip):
        try:
            from mcp_server import ABUSEIPDB_API_KEY
            if not ABUSEIPDB_API_KEY: return 0.0, {}
            h = {"Key":ABUSEIPDB_API_KEY,"Accept":"application/json"}
            r = await _api_call("get",f"{ABUSEIPDB_BASE_URL}/check?ipAddress={ip}&maxAgeInDays=90",headers=h)
            d = r.json().get("data",{})
            s = d.get("abuseConfidenceScore",0)/100.0
            return s, {"confidence":d.get("abuseConfidenceScore",0),"total_reports":d.get("totalReports",0)}
        except Exception: return 0.0, {}

    cs_s, cs_d = await _crowdsec(params.ip)
    tf_s, tf_d = await _threatfox(params.ip)
    ab_s, ab_d = await _abuseipdb(params.ip)

    w = {"crowdsec":0.35,"threatfox":0.35,"abuseipdb":0.30}
    parts = []
    if cs_d: parts.append((cs_s*w["crowdsec"], w["crowdsec"]))
    if tf_d: parts.append((tf_s*w["threatfox"], w["threatfox"]))
    if ab_d: parts.append((ab_s*w["abuseipdb"], w["abuseipdb"]))
    uw = sum(p[1] for p in parts)
    unified = sum(p[0] for p in parts)/uw if uw>0 else 0.0

    if unified>=0.8: v="CRITICAL - Active threat, escalate immediately"
    elif unified>=0.5: v="HIGH - Likely malicious, investigate"
    elif unified>=0.2: v="MEDIUM - Suspicious, monitor"
    elif parts: v="LOW — Probably benign"
    else: v="UNKNOWN - No threat intel sources available"

    if params.response_format=="json":
        return _truncate_if_needed(json.dumps({"ip":params.ip,"unified_score":round(unified,2),"verdict":v,
            "sources":{"crowdsec":{"score":round(cs_s,2),**cs_d} if cs_d else None,
                       "threatfox":{"score":round(tf_s,2),**tf_d} if tf_d else None,
                       "abuseipdb":{"score":round(ab_s,2),**ab_d} if ab_d else None},
            "scoring_model":{"weights":w,"used_weight":round(uw,2)}},indent=2))

    lines=[f"# Unified Threat Score - `{params.ip}`","",f"**Score**: {unified:.2f}  |  **Verdict**: {v}","","| Source | Score | Details |","|--------|-------|---------|"]
    if cs_d: lines.append(f"| CrowdSec | {cs_s:.2f} | `{cs_d.get('reputation','?')}` — {', '.join(cs_d.get('behaviors',[])[:2])} |")
    else: lines.append("| CrowdSec | - | ⚠️ Not configured |")
    if tf_d: lines.append(f"| ThreatFox | {tf_s:.2f} | `{tf_d.get('malware','?')}` ({tf_d.get('threat_type','?')}, conf={tf_d.get('confidence','?')}) |")
    else: lines.append("| ThreatFox | - | ⚠️ Not configured |")
    if ab_d: lines.append(f"| AbuseIPDB | {ab_s:.2f} | {ab_d.get('confidence',0)}% confidence, {ab_d.get('total_reports',0)} reports |")
    else: lines.append("| AbuseIPDB | - | ⚠️ Not configured |")
    return _truncate_if_needed("\n".join(lines))
