#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Unified threat intelligence aggregator.

Queries all available threat-intel providers concurrently for a single IOC
(IP / domain / hash) and returns a normalized, aggregated verdict.

Provider coverage:
- CrowdSec CTI       (IP only)             - reputation, behaviors, MITRE
- ThreatFox           (IP/domain/hash)     - malware families, confidence
- AlienVault OTX      (IP/domain/hash/url) - pulses, adversaries, industries
- GreyNoise           (IP only)            - scanner vs business service
- AbuseIPDB           (IP only)            - abuse confidence score
- VirusTotal          (hash/domain)        - detection ratio

Normalizes each into TIProviderResult, then aggregates into TIQueryOutput.
"""
from __future__ import annotations
import json, asyncio, re, os, logging
from typing import Any, Optional, Literal
from pydantic import BaseModel, ConfigDict, Field, field_validator
from mcp_server import (mcp, CROWDSEC_API_KEY_ENV, OTX_API_KEY_ENV,
                        THREATFOX_API_KEY_ENV, ABUSEIPDB_API_KEY,
                        VIRUSTOTAL_API_KEY, GREYNOISE_COMMUNITY_BASE_URL,
                        ABUSEIPDB_BASE_URL, VIRUSTOTAL_BASE_URL)
from mcp_server.core.http_client import _api_call, _is_private_or_reserved, ValidPublicIp
from mcp_server.core.audit import _audit_log, _truncate_if_needed
from mcp_server.threat_intel.otx import _classify_indicator, _normalize_adversary

logger = logging.getLogger("blue_team_mcp.threat_intel_aggregate")

_IP_RE = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
_HASH_RE = re.compile(r"^[a-fA-F0-9]{32}$|^[a-fA-F0-9]{40}$|^[a-fA-F0-9]{64}$")

# Risk level ordering for aggregation
_RISK_ORDER = {"critical": 4, "high": 3, "medium": 2, "low": 1, "none": 0, None: 0}


class TIProviderResult(BaseModel):
    """Normalized result from a single threat-intel provider."""
    provider: str = ""
    indicator: str = ""
    indicator_type: str = "unknown"
    risk_level: Optional[str] = None
    reputation_score: Optional[int] = None
    is_malicious: Optional[bool] = None
    tags: list[str] = Field(default_factory=list)
    attack_techniques: list[str] = Field(default_factory=list)
    malware_families: list[str] = Field(default_factory=list)
    adversaries: list[str] = Field(default_factory=list)
    industries: list[str] = Field(default_factory=list)
    pulses: list[dict] = Field(default_factory=list)
    detail: dict = Field(default_factory=dict)
    error: Optional[str] = None


class TIQueryOutput(BaseModel):
    """Aggregated multi-provider result."""
    indicator: str
    indicator_type: str
    results: list[TIProviderResult] = Field(default_factory=list)
    aggregated_risk_level: Optional[str] = None
    consensus_malicious: int = 0
    errors: list[str] = Field(default_factory=list)


class ThreatIntelAggregateInput(BaseModel):
    """Input model for blueteam_threat_intel_aggregate."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    indicator: str = Field(
        ..., min_length=3, max_length=256,
        description="IOC to analyze: IP address, domain, or file hash (MD5/SHA1/SHA256).",
    )
    response_format: Literal["markdown", "json"] = Field(default="markdown")

    @field_validator("indicator")
    @classmethod
    def validate_indicator(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("indicator must not be empty")
        if _IP_RE.match(v) and _is_private_or_reserved(v):
            raise ValueError(f"'{v}' is a private/reserved IP - this tool only accepts public IOCs.")
        ind_type = _classify_indicator(v)
        if not ind_type:
            raise ValueError(f"Unrecognized IOC type: '{v}'. Supported: IP, domain, hostname, URL, MD5/SHA1/SHA256.")
        return v


# Provider adapters (each returns TIProviderResult, never raises)
async def _crowdsec_provider(indicator: str, ind_type: str) -> TIProviderResult:
    if ind_type != "IPv4" or not os.environ.get(CROWDSEC_API_KEY_ENV):
        return TIProviderResult(provider="crowdsec", indicator=indicator,
                                indicator_type=ind_type, error="not configured" if not os.environ.get(CROWDSEC_API_KEY_ENV) else "unsupported type")
    try:
        from mcp_server.threat_intel.crowdsec import _crowdsec_request
        r = await _crowdsec_request(f"/v2/smoke/{indicator}")
        rep = r.get("reputation", "unknown")
        score = {"malicious": 100, "suspicious": 60, "known": 30, "unknown": 10, "safe": 0}.get(rep, 10)
        risk = {"malicious": "high", "suspicious": "medium", "known": "low", "unknown": "low", "safe": "none"}.get(rep, "low")
        return TIProviderResult(
            provider="crowdsec", indicator=indicator, indicator_type=ind_type,
            risk_level=risk, reputation_score=score,
            is_malicious=(rep == "malicious"),
            tags=[b.get("name", "?") for b in r.get("behaviors", [])[:5]],
            attack_techniques=[m.get("name", "?") for m in r.get("mitre_techniques", [])[:10]],
            detail={"reputation": rep, "as_name": r.get("as_name", "")},
        )
    except Exception as e:
        return TIProviderResult(provider="crowdsec", indicator=indicator,
                                indicator_type=ind_type, error=str(e))


async def _threatfox_provider(indicator: str, ind_type: str) -> TIProviderResult:
    if not os.environ.get(THREATFOX_API_KEY_ENV):
        return TIProviderResult(provider="threatfox", indicator=indicator,
                                indicator_type=ind_type, error="not configured")
    try:
        from mcp_server.threat_intel.threatfox import _threatfox_request
        r = await _threatfox_request(indicator, False)
        items = r.get("data", [])
        if not items:
            return TIProviderResult(provider="threatfox", indicator=indicator,
                                    indicator_type=ind_type, risk_level="none",
                                    reputation_score=0, is_malicious=False)
        conf = max((e.get("confidence_level", 0) for e in items), default=0)
        risk = "high" if conf >= 75 else "medium" if conf >= 50 else "low"
        return TIProviderResult(
            provider="threatfox", indicator=indicator, indicator_type=ind_type,
            risk_level=risk, reputation_score=conf, is_malicious=(conf >= 50),
            malware_families=list({e.get("malware_printable", "?") for e in items if e.get("malware_printable")})[:5],
            tags=[e.get("threat_type_desc", "?") for e in items[:3]],
            detail={"match_count": len(items)},
        )
    except Exception as e:
        return TIProviderResult(provider="threatfox", indicator=indicator,
                                indicator_type=ind_type, error=str(e))


async def _otx_provider(indicator: str, ind_type: str) -> TIProviderResult:
    if not os.environ.get(OTX_API_KEY_ENV):
        return TIProviderResult(provider="otx", indicator=indicator,
                                indicator_type=ind_type, error="not configured")
    try:
        from mcp_server.threat_intel.otx import _otx_request
        r = await _otx_request(indicator, "general")
        pulse_info = r.get("pulse_info", {})
        pulses = pulse_info.get("pulses", [])
        count = pulse_info.get("count", 0)

        # Enrich hashes with the malware section (sample detections, no pulses needed)
        malware_hits = []
        if ind_type == "file":
            try:
                m = await _otx_request(indicator, "malware")
                for sample in m.get("data", []):
                    if isinstance(sample, dict) and sample.get("hash"):
                        malware_hits.append(sample.get("hash", "")[:12])
            except Exception:
                pass  # malware section optional

        if count == 0 and not malware_hits:
            return TIProviderResult(provider="otx", indicator=indicator,
                                    indicator_type=ind_type, risk_level="none",
                                    reputation_score=0, is_malicious=False)
        mf = list({m for p in pulses for m in p.get("malware_families", [])})[:5]
        adv = list({_normalize_adversary(p.get("adversary")) for p in pulses if _normalize_adversary(p.get("adversary"))})[:5]
        attack = list({a for p in pulses for a in p.get("attack_ids", [])})[:10]
        industries = list({i for p in pulses for i in p.get("industries", [])})[:5]
        # Malicious if malware families/adversaries OR direct malware sample hits.
        is_mal = bool(mf or adv or malware_hits)
        risk = "high" if is_mal else "medium"
        return TIProviderResult(
            provider="otx", indicator=indicator, indicator_type=ind_type,
            risk_level=risk,
            reputation_score=min(50 + count * 5 + len(malware_hits) * 10, 100),
            is_malicious=is_mal,
            malware_families=mf, adversaries=adv, attack_techniques=attack,
            industries=industries,
            pulses=[{"name": p.get("name", "?"), "author": (p.get("author") or {}).get("username", "?")}
                    for p in pulses[:5]],
            detail={"pulse_count": count, "malware_samples": malware_hits[:5]},
        )
    except Exception as e:
        return TIProviderResult(provider="otx", indicator=indicator,
                                indicator_type=ind_type, error=str(e))


async def _greynoise_provider(indicator: str, ind_type: str) -> TIProviderResult:
    if ind_type != "IPv4":
        return TIProviderResult(provider="greynoise", indicator=indicator,
                                indicator_type=ind_type, error="unsupported type")
    try:
        r = await _api_call("get", f"{GREYNOISE_COMMUNITY_BASE_URL}/{indicator}",
                            headers={"accept": "application/json"})
        raw = r.json()
        classification = raw.get("classification", "unknown")
        is_mal = classification == "malicious"
        return TIProviderResult(
            provider="greynoise", indicator=indicator, indicator_type=ind_type,
            risk_level="high" if is_mal else "low" if classification == "unknown" else "none",
            reputation_score=100 if is_mal else 0,
            is_malicious=is_mal,
            tags=[classification, "scanner" if raw.get("noise") else "",
                  "business" if raw.get("riot") else ""],
            detail={"name": raw.get("name", ""), "last_seen": raw.get("last_seen", "")},
        )
    except Exception as e:
        return TIProviderResult(provider="greynoise", indicator=indicator,
                                indicator_type=ind_type, error=str(e))


async def _abuseipdb_provider(indicator: str, ind_type: str) -> TIProviderResult:
    if ind_type != "IPv4" or not ABUSEIPDB_API_KEY:
        return TIProviderResult(provider="abuseipdb", indicator=indicator,
                                indicator_type=ind_type, error="not configured" if not ABUSEIPDB_API_KEY else "unsupported type")
    try:
        h = {"Key": ABUSEIPDB_API_KEY, "Accept": "application/json"}
        r = await _api_call("get", f"{ABUSEIPDB_BASE_URL}/check?ipAddress={indicator}&maxAgeInDays=90", headers=h)
        d = r.json().get("data", {})
        conf = d.get("abuseConfidenceScore", 0)
        risk = "high" if conf >= 75 else "medium" if conf >= 50 else "low" if conf >= 25 else "none"
        return TIProviderResult(
            provider="abuseipdb", indicator=indicator, indicator_type=ind_type,
            risk_level=risk, reputation_score=conf, is_malicious=(conf >= 50),
            detail={"total_reports": d.get("totalReports", 0), "last_reported": d.get("lastReportedAt", "")},
        )
    except Exception as e:
        return TIProviderResult(provider="abuseipdb", indicator=indicator,
                                indicator_type=ind_type, error=str(e))


async def _virustotal_provider(indicator: str, ind_type: str) -> TIProviderResult:
    if ind_type not in ("file", "domain") or not VIRUSTOTAL_API_KEY:
        return TIProviderResult(provider="virustotal", indicator=indicator,
                                indicator_type=ind_type, error="not configured" if not VIRUSTOTAL_API_KEY else "unsupported type")
    try:
        vt_type = "files" if ind_type == "file" else "domains"
        h = {"x-apikey": VIRUSTOTAL_API_KEY, "Accept": "application/json"}
        r = await _api_call("get", f"{VIRUSTOTAL_BASE_URL}/{vt_type}/{indicator}", headers=h)
        d = r.json().get("data", {})
        attrs = d.get("attributes", {})
        stats = attrs.get("last_analysis_stats", {})
        mal = stats.get("malicious", 0)
        total = sum(stats.values()) or 1
        score = int(mal / total * 100)
        risk = "high" if score >= 50 else "medium" if score >= 20 else "low" if mal > 0 else "none"
        return TIProviderResult(
            provider="virustotal", indicator=indicator, indicator_type=ind_type,
            risk_level=risk, reputation_score=score, is_malicious=(mal > 0),
            detail={"detections": f"{mal}/{total}", "reputation": attrs.get("reputation", 0)},
        )
    except Exception as e:
        return TIProviderResult(provider="virustotal", indicator=indicator,
                                indicator_type=ind_type, error=str(e))


# Aggregation
def _aggregate(results: list[TIProviderResult]) -> TIQueryOutput:
    """Aggregate per-provider results into a single verdict."""
    # Ignore results with errors for scoring
    valid = [r for r in results if r.error is None]
    errors = [f"{r.provider}: {r.error}" for r in results if r.error]

    if not valid:
        return TIQueryOutput(indicator=results[0].indicator if results else "",
                             indicator_type=results[0].indicator_type if results else "unknown",
                             results=results, aggregated_risk_level=None,
                             consensus_malicious=0, errors=errors)

    malicious_votes = sum(1 for r in valid if r.is_malicious)
    # Weighted risk: take the highest risk level among providers
    highest = max(valid, key=lambda r: _RISK_ORDER.get(r.risk_level, 0))
    aggregated = highest.risk_level

    return TIQueryOutput(
        indicator=valid[0].indicator,
        indicator_type=valid[0].indicator_type,
        results=results,
        aggregated_risk_level=aggregated,
        consensus_malicious=malicious_votes,
        errors=errors,
    )


# MCP Tool
@mcp.tool(
    name="blueteam_threat_intel_aggregate",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": True},
)
async def blueteam_threat_intel_aggregate(params: ThreatIntelAggregateInput) -> str:
    """Aggregate threat intelligence from all available providers for one IOC.

    Queries CrowdSec, ThreatFox, AlienVault OTX, GreyNoise, AbuseIPDB, and
    VirusTotal **concurrently** for a single indicator (IP / domain / hash),
    normalizes each into a unified result, and returns an aggregated verdict.

    This replaces 6 sequential tool calls with one faster and gives a consensus view across independent sources.

    **Worked Examples**

    1. *Full aggregation for a suspicious IP*:
       ``blueteam_threat_intel_aggregate(indicator="140.82.0.86")``

    2. *Aggregate a domain*:
       ``blueteam_threat_intel_aggregate(indicator="evil-c2.example.com")``

    3. *Aggregate a file hash*:
       ``blueteam_threat_intel_aggregate(indicator="<sha256>")``

    **Error Handling**: Providers without API keys are skipped and reported in
    ``errors[]``. Per-provider failures never block the overall aggregation.
    """
    _audit_log("blueteam_threat_intel_aggregate", {"indicator": params.indicator})
    ind_type = _classify_indicator(params.indicator)

    # Query all applicable providers concurrently
    tasks = [
        _crowdsec_provider(params.indicator, ind_type),
        _threatfox_provider(params.indicator, ind_type),
        _otx_provider(params.indicator, ind_type),
        _greynoise_provider(params.indicator, ind_type),
        _abuseipdb_provider(params.indicator, ind_type),
        _virustotal_provider(params.indicator, ind_type),
    ]
    results: list[TIProviderResult] = await asyncio.gather(*tasks)
    output = _aggregate(results)

    if params.response_format == "json":
        return _truncate_if_needed(json.dumps(output.model_dump(), indent=2, default=str))

    # Markdown
    lines = [f"# Threat Intel Aggregate — `{params.indicator}`", "",
             f"**Type**: `{ind_type}` | **Aggregated Risk**: **{output.aggregated_risk_level or 'unknown'}** "
             f"| **Malicious votes**: {output.consensus_malicious}/{len([r for r in results if r.error is None])}",
             "", "| Provider | Risk | Score | Malicious | Malware / Adversary |",
             "|----------|------|-------|-----------|---------------------|"]
    for r in results:
        if r.error:
            lines.append(f"| `{r.provider}` | — | — | — | ⚠️ {r.error[:40]} |")
        else:
            mf = ", ".join(r.malware_families[:2]) or ""
            adv = ", ".join(r.adversaries[:2]) or ""
            detail = f"{mf} {adv}".strip() or "—"
            lines.append(f"| `{r.provider}` | {r.risk_level or '?'} | {r.reputation_score if r.reputation_score is not None else '?'} "
                         f"| {'✅' if r.is_malicious else '❌'} | {detail[:40]} |")

    if output.errors:
        lines.append("")
        lines.append("### ⚠️ Skipped providers")
        for e in output.errors:
            lines.append(f"- {e}")

    # MITRE techniques across providers
    all_techniques = sorted({t for r in results if not r.error for t in r.attack_techniques})
    if all_techniques:
        lines.append("")
        lines.append(f"### 🎯 MITRE ATT&CK Techniques ({len(all_techniques)})")
        lines.append(" | ".join(f"`{t}`" for t in all_techniques[:20]))

    # OTX pulses (campaign context)
    pulses = [p for r in results if not r.error for p in r.pulses]
    if pulses:
        lines.append("")
        lines.append(f"### 🕵️ Campaign Pulses ({len(pulses)})")
        for p in pulses[:5]:
            lines.append(f"- **{p.get('name','?')}** — {p.get('author','?')}")

    return _truncate_if_needed("\n".join(lines))
