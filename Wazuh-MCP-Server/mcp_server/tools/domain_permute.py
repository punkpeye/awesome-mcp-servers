#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Domain permutation generate typosquatting/phishing lookalikes of a domain.
Attackers register near-miss domains of a target to phish its users or intercept
email. This tool generates the most likely lookalike variants (omission, swap,
repetition, homoglyph, hyphenation, TLD swap) so an analyst can feed the top
candidates into `blueteam_whois_lookup` / `blueteam_crtsh_lookup` to detect
active typosquatting against the org. Pure stdlib deterministic, no network.
"""
from __future__ import annotations
import json
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field, field_validator
from mcp_server import mcp
from mcp_server.core.audit import _audit_log, _truncate_if_needed

# Homoglyph map (valid in a DNS label): visually-similar digit substitutions.
_HOMOGLYPHS = {"o": "0", "l": "1", "i": "1", "s": "5", "e": "3", "a": "4", "b": "8", "g": "9"}
# Common TLD swaps attackers try against a `.go.id`-style target.
_TLD_SWAPS = ("go.id", "co.id", "id", "com", "net", "org", "info", "online", "site")

def _permute_domain(domain: str, max_variants: int = 100) -> list[str]:
    """Generate lookalike domains for a base domain (deterministic, deduped)."""
    domain = (domain or "").strip().lower().rstrip(".")
    parts = domain.split(".")
    if len(parts) < 2:
        return []
    sld, tld = parts[0], ".".join(parts[1:])
    variants: set[str] = set()

    # 1. Single-character omission
    for i in range(len(sld)):
        if len(sld) > 1:
            variants.add(sld[:i] + sld[i + 1:] + "." + tld)
    # 2. Adjacent character swap
    for i in range(len(sld) - 1):
        chars = list(sld)
        chars[i], chars[i + 1] = chars[i + 1], chars[i]
        variants.add("".join(chars) + "." + tld)
    # 3. Character repetition (fat-finger double press)
    for i in range(len(sld)):
        variants.add(sld[:i + 1] + sld[i] + sld[i + 1:] + "." + tld)
    # 4. Homoglyph substitution (one char at a time)
    for i, ch in enumerate(sld):
        if ch in _HOMOGLYPHS:
            variants.add(sld[:i] + _HOMOGLYPHS[ch] + sld[i + 1:] + "." + tld)
    # 5. Hyphenation
    for i in range(1, len(sld)):
        variants.add(sld[:i] + "-" + sld[i:] + "." + tld)
    # 6. TLD swap
    for t in _TLD_SWAPS:
        if t != tld:
            variants.add(sld + "." + t)

    variants.discard(domain)
    return sorted(variants)[:max_variants]


class DomainPermuteInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    domain: str = Field(..., min_length=4, max_length=256,
        description="Base domain to permute, e.g. 'tangerangkota.go.id'.")
    max_variants: int = Field(default=50, ge=1, le=500,
        description="Max lookalike domains to return.")
    response_format: Literal["markdown", "json"] = Field(default="markdown")

    @field_validator("domain")
    @classmethod
    def validate_domain(cls, v: str) -> str:
        v = v.strip().lower().rstrip(".")
        if not v or any(c in v for c in " \t\n/\\@"):
            raise ValueError(f"Invalid domain: '{v}'")
        if "." not in v:
            raise ValueError(f"Invalid domain (no TLD): '{v}'")
        return v


@mcp.tool(
    name="blueteam_domain_permute",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": True},
)
async def blueteam_domain_permute(params: DomainPermuteInput) -> str:
    """Generate typosquatting/phishing lookalikes of a domain.
    Produces the most likely near-miss domains an attacker would register against
    your org (omission, swap, repetition, homoglyph, hyphenation, TLD swap). Feed
    the top candidates into `blueteam_whois_lookup` / `blueteam_crtsh_lookup` to
    detect active typosquatting. Pure stdlib no network.
    **Worked Examples**
    1. ``blueteam_domain_permute(domain="tangerangkota.go.id")``
    2. ``blueteam_domain_permute(domain="tangerangkota.go.id", max_variants=20, response_format="json")``
    """
    _audit_log("blueteam_domain_permute", {"domain": params.domain})
    variants = _permute_domain(params.domain, params.max_variants)
    if params.response_format == "json":
        return json.dumps({"domain": params.domain, "count": len(variants),
                           "variants": variants}, indent=2, ensure_ascii=False)
    lines = [f"# 🎯 Domain Permutations — `{params.domain}`", "",
             f"**Lookalike domains** ({len(variants)}):", ""]
    for v in variants:
        lines.append(f"- `{v}`")
    lines.append("")
    lines.append("_Feed the top candidates into `blueteam_whois_lookup` / `blueteam_crtsh_lookup` "
                 "to detect active typosquatting._")
    return _truncate_if_needed("\n".join(lines))
