#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Webshell checker - curl + signature scan against unmasked forensic URLs
Used after blueteam_wazuh_export (forensic unmasking) to confirm whether a URL hosts an active webshell or backdoor
"""
from __future__ import annotations
import json, re, uuid, os
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field, field_validator
from mcp_server import mcp
from mcp_server.core.audit import _audit_log, _truncate_if_needed
from mcp_server.core.attacker_registry import register_attacker_ioc
from mcp_server.core.subprocess import _run_async

# Webshell signature patterns - community-maintained, extend as needed.
_SIGNATURES: list[tuple[str, str, str]] = [
    # (regex pattern, shell family, weight)
    (r"b374k", "b374k PHP shell", "high"),
    (r"c99(mad|shell|\s)", "c99 PHP shell", "high"),
    (r"r57\s*shell", "r57 PHP shell", "high"),
    (r"WSO\s*(2\.\d|Web\s*Shell)", "WSO web shell", "high"),
    (r"FilesMAn|FilesMan", "File Manager shell", "high"),
    (r"<\?php\s+system\s*\(.+\)", "Generic PHP system() backdoor", "medium"),
    (r"<\?php\s+exec\s*\(.+\)", "Generic PHP exec() backdoor", "medium"),
    (r"<\?php\s+passthru\s*\(.+\)", "Generic PHP passthru() backdoor", "medium"),
    (r"<\?php\s+shell_exec\s*\(.+\)", "Generic PHP shell_exec() backdoor", "medium"),
    (r"eval\s*\(\s*(base64_decode|str_rot13|gzinflate|gzuncompress)\s*\(", "Obfuscated PHP backdoor", "high"),
    (r"<\?php\s+assert\s*\(.+\)", "PHP assert() backdoor", "medium"),
    (r"<title>.*?(Shell|Web\s*Shell|Backdoor|Hacked|Owned).*?</title>", "Shell HTML title tag", "low"),
    (r"password.*?<input.*?type.*?password", "Password-protected form (generic)", "low"),
    (r"Reverse\s*Shell|bind\s*shell|connect[-_]back", "Reverse/bind shell indicator", "high"),
    (r"alfa.*?rex|alfarex", "Alfa-Rex PHP shell", "high"),
    (r"wp2shell|wp-2-shell|wp_to_shell", "wp2shell exploit tool", "high"),
    (r"dragonshell|dragon.*?shell", "Dragon PHP shell", "high"),
    (r"indonesian.*?shell|shell.*?indonesia", "Indonesian webshell variant", "medium"),
    (r"Symlink\s*Bypass|symlink\s*race", "Symlink race condition shell", "medium"),
    (r"Config\s*Grabber|config.*?grab", "Config grabber tool", "low"),
]

# Shell-specific login page signatures - unique HTML/CSS patterns of known shells.
# When matched, the tool exposes the login page HTML for LLM classification.
_LOGIN_SHELL_SIGNATURES: list[tuple[str, str, str]] = [
    (r"<title>b374k.*?(login|shell|mini)", "b374k login page", "high"),
    (r"<title>c99.*?(login|shell)", "c99 login page", "high"),
    (r"<title>r57.*?shell", "r57 login page", "high"),
    (r"<title>WSO.*?(Login|Shell)", "WSO login page", "high"),
    (r"<title>.*?Dragon.*?(Login|Shell|Panel)", "Dragon shell login", "high"),
    (r"<title>.*?Alfa.*?(Login|Shell|Panel)", "Alfa-Rex login page", "high"),
    (r"<title>.*?(Mini|MiniShell|Micro).*?(Shell|Login)", "Mini shell login", "high"),
    (r"<title>pr[yi]v8", "Priv8 shell login", "high"),
    (r"<title>Symlink.*?(Login|Bypass|Panel)", "Symlink shell login", "high"),
    (r"method.*?post.*?action.*?(login|auth|check)", "Generic POST auth form", "low"),
    (r"type.*?password.*?name.*?pass", "Password field in form", "low"),
]


class WebshellCheckInput(BaseModel):
    """Input model for blueteam_check_webshell."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    url: str = Field(
        ..., min_length=10, max_length=2048,
        description="Full URL to check, e.g. 'https://csirt.tangerangkota.go.id/uploads/shell.php'.",
    )
    timeout: int = Field(
        default=10, ge=3, le=60,
        description="cURL timeout in seconds.",
    )
    follow_redirects: bool = Field(
        default=True,
        description="Follow HTTP redirects (curl -L).",
    )
    max_body_scan_bytes: int = Field(
        default=65536, ge=1024, le=262144,
        description="Max bytes of response body to scan for signatures.",
    )
    response_format: Literal["markdown", "json"] = Field(
        default="markdown",
        description="Output format.",
    )

    @field_validator("url")
    @classmethod
    def validate_url(cls, v: str) -> str:
        v = v.strip()
        if not v.startswith(("http://", "https://")):
            raise ValueError(f"URL must start with http:// or https://, got: {v!r}")
        # Reject private/reserved IPs in URL host
        from urllib.parse import urlparse
        import ipaddress
        host = urlparse(v).hostname
        if host:
            try:
                ip = ipaddress.ip_address(host)
            except ValueError:
                ip = None  # not an IP - domain name, allowed
            if ip is not None and (ip.is_private or ip.is_loopback or ip.is_reserved or ip.is_link_local):
                raise ValueError(f"URL host is a private/reserved IP: {host}. This tool only accepts public hosts.")
        return v


def _scan_body(body: str) -> list[dict]:
    """Scan response body for webshell signatures + login page patterns."""
    matches: list[dict] = []
    for pattern, family, weight in _SIGNATURES:
        hits = len(re.findall(pattern, body, re.IGNORECASE))
        if hits > 0:
            matches.append({
                "signature": pattern[:50],
                "family": family,
                "weight": weight,
                "hit_count": hits,
            })
    for pattern, family, weight in _LOGIN_SHELL_SIGNATURES:
        hits = len(re.findall(pattern, body, re.IGNORECASE))
        if hits > 0:
            matches.append({
                "signature": pattern[:50],
                "family": family,
                "weight": weight,
                "hit_count": hits,
                "is_login_page": True,
            })
    return matches


def _has_login_page(matches: list[dict]) -> bool:
    return any(m.get("is_login_page") for m in matches)


def _extract_login_context(body: str, max_chars: int = 1500) -> str:
    """Extract key HTML elements for LLM classification of login pages."""
    title = re.search(r"<title>(.*?)</title>", body, re.IGNORECASE)
    forms = re.findall(r"<form[^>]*>.*?</form>", body, re.IGNORECASE | re.DOTALL)
    inputs = re.findall(r"<input[^>]*>", body, re.IGNORECASE)
    headings = re.findall(r"<h[1-6][^>]*>.*?</h[1-6]>", body, re.IGNORECASE)
    parts = []
    if title:
        parts.append(f"TITLE: {title.group(1)[:200]}")
    if headings:
        parts.append(f"HEADINGS: {' | '.join(h[:100] for h in headings[:5])}")
    if inputs:
        parts.append(f"INPUTS ({len(inputs)}): {' | '.join(i[:80] for i in inputs[:10])}")
    if forms:
        parts.append(f"FORMS ({len(forms)}): {' | '.join(f[:150] for f in forms[:3])}")
    return "\n".join(parts)[:max_chars]


def _verdict(matches: list[dict]) -> str:
    if not matches:
        return "CLEAN"
    high = sum(1 for m in matches if m["weight"] == "high" and not m.get("is_login_page"))
    medium = sum(1 for m in matches if m["weight"] == "medium" and not m.get("is_login_page"))
    login_high = sum(1 for m in matches if m.get("is_login_page") and m["weight"] == "high")
    if high >= 2 or (high >= 1 and medium >= 2):
        return "CONFIRMED"
    if high >= 1 or medium >= 2:
        return "SUSPICIOUS"
    if login_high >= 1:
        return "LOGIN_PAGE"  # no active shell code - just a login form, need LLM classification
    if matches:
        return "LOW_RISK"
    return "CLEAN"


@mcp.tool(
    name="blueteam_check_webshell",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": True},
)
async def blueteam_check_webshell(params: WebshellCheckInput) -> str:
    """Check a URL for active webshell or backdoor via curl + signature scan.

    Uses ``curl`` to fetch the URL, then scans the response body against
    20 community-maintained webshell signature patterns (b374k, c99, r57, WSO, alfa-rex, eval+base64, obfuscated backdoors, etc.).

    Intended for use AFTER forensic unmasking - feed it the raw
    unmasked URLs from ``blueteam_wazuh_export`` to confirm whether
    a webshell is actively hosted on your infrastructure.

    **SSRF Protection**: Private/reserved IPs in the URL host are rejected.

    **Worked Examples**

    1. *Check a suspicious URL*:
       ``blueteam_check_webshell(url="https://csirt.tangerangkota.go.id/uploads/alfa-rex.php")``

    2. *Deep scan with extended timeout*:
       ``blueteam_check_webshell(url="https://subdomain.tangerangkota.go.id/shell.php", timeout=30)``

    3. *JSON output for automated pipeline*:
       ``blueteam_check_webshell(url="https://...", response_format="json")``
    """
    _audit_log("blueteam_check_webshell", {"url": params.url, "timeout": params.timeout})
    body_file = f"/tmp/webshell_check_{uuid.uuid4().hex}.body"

    # _run_async expects a LIST of args, not a shell string.
    cmd = ["curl", "-s", "--insecure", "--max-time", str(params.timeout)]
    if params.follow_redirects:
        cmd.append("-L")
    cmd += [
        "-o", body_file,
        "-w", "HTTP_STATUS:%{http_code}\nCONTENT_TYPE:%{content_type}\nSIZE:%{size_download}\n",
        params.url,
    ]

    result = await _run_async(cmd, timeout=int(params.timeout) + 5)

    # Parse curl output
    status = 0
    content_type = ""
    size_download = 0
    for line in result["stdout"].split("\n"):
        if line.startswith("HTTP_STATUS:"):
            try:
                status = int(line.split(":", 1)[1].strip())
            except ValueError:
                pass
        elif line.startswith("CONTENT_TYPE:"):
            content_type = line.split(":", 1)[1].strip() if ":" in line else ""
        elif line.startswith("SIZE:"):
            try:
                size_download = int(line.split(":", 1)[1].strip())
            except ValueError:
                pass

    # Read and scan body
    matches: list[dict] = []
    body_sample = ""
    body_read_error: str | None = None
    try:
        with open(body_file, "r", encoding="utf-8", errors="replace") as f:
            body_sample = f.read(params.max_body_scan_bytes)
        matches = _scan_body(body_sample)
    except FileNotFoundError:
        body_read_error = "Body file not found - curl may have failed before writing."
    except Exception as e:
        body_read_error = f"Body read error: {e}"

    # Cleanup body file
    try:
        os.unlink(body_file)
    except OSError:
        pass

    v = _verdict(matches)

    # Auto-register confirmed webshell URL as attacker IOC
    if v == "CONFIRMED":
        register_attacker_ioc(params.url, source="webshell_check")

    if params.response_format == "json":
        return json.dumps({
            "url": params.url,
            "http_status": status,
            "content_type": content_type,
            "download_size_bytes": size_download,
            "curl_exit_code": result["returncode"],
            "curl_stderr": result["stderr"][:200] if result["stderr"] else None,
            "matched_signatures": matches,
            "verdict": v,
            "body_read_error": body_read_error,
        }, indent=2, ensure_ascii=False)

    # Markdown output
    lines = [
        f"# 🕵️ Webshell Check - `{params.url}`",
        "",
        f"**HTTP Status**: `{status}` | **Content-Type**: `{content_type}` | "
        f"**Size**: {size_download:,} bytes | **curl exit**: {result['returncode']}",
        "",
    ]

    if body_read_error:
        lines.append(f"⚠️ {body_read_error}")
        lines.append("")

    if v == "CONFIRMED":
        lines.append(f"## 🔴 Verdict: CONFIRMED - Active Webshell Detected")
        lines.append(f"**URL auto-registered** in attacker IOC registry for unmasking protection.")
    elif v == "LOGIN_PAGE":
        lines.append(f"## 🔐 Verdict: LOGIN_PAGE - Password-Protected Shell Login Detected")
        lines.append(f"**Classify this login page based on the HTML context below:**")
        lines.append(f"- Is this a known webshell family login (b374k, c99, WSO, etc.)?")
        lines.append(f"- Or is this a legitimate application login (WordPress, Django, custom app)?")
        lines.append(f"- If confirmed as a shell login, register the URL as an attacker IOC.")
        lines.append("")
        login_ctx = _extract_login_context(body_sample)
        if login_ctx:
            lines.append(f"### 🔍 Login Page HTML Context\n```html\n{login_ctx}\n```")
    elif v == "LOW_RISK":
        lines.append(f"## 🟢 Verdict: LOW_RISK — Minor Indicators Only")
    else:
        lines.append(f"## ✅ Verdict: CLEAN - No Webshell Signatures Found")

    if matches:
        lines.append("")
        lines.append("| Signature | Family | Weight | Hits |")
        lines.append("|-----------|--------|--------|------|")
        for m in sorted(matches, key=lambda x: (-{"high": 3, "medium": 2, "low": 1}[x["weight"]], -x["hit_count"])):
            lines.append(f"| `{m['signature']}` | {m['family']} | {m['weight']} | {m['hit_count']} |")

    if result["stderr"]:
        lines.append("")
        lines.append("### curl stderr")
        lines.append(f"```\n{result['stderr'][:500]}\n```")

    return _truncate_if_needed("\n".join(lines))
