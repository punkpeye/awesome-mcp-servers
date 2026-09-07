#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
JARM / TLS fingerprint - active TLS server fingerprinting (no API key).
JARM (Salesforce's TLS server fingerprint) sends crafted TLS ClientHello
probes and hashes the ServerHello fields. C2 frameworks and malware families
negotiate TLS in characteristic ways, so identical JARM hashes indicate the
same underlying software. This stdlib implementation probes the server with multiple TLS configurations
and hashes the negotiated cipher + version + certificate properties. It is a
*TLS fingerprint* in the spirit of JARM - not a byte-for-byte reproduction of
Salesforce's 10-probe algorithm (which requires raw ClientHello crafting that Python's ssl module does not expose).
Use it to fingerprint attacker infrastructure and C2 servers.
"""
from __future__ import annotations
import asyncio, hashlib, json, socket, ssl
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field, field_validator
from mcp_server import mcp
from mcp_server.core.audit import _audit_log, _truncate_if_needed
from mcp_server.core.http_client import _is_private_or_reserved


class JarmFingerprintInput(BaseModel):
    """Input model for jarm_fingerprint."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    host: str = Field(
        ..., min_length=3, max_length=256,
        description="Hostname or IP to fingerprint, e.g. 'evil-c2.example.com'.",
    )
    port: int = Field(
        default=443, ge=1, le=65535,
        description="TLS port (default 443).",
    )
    timeout: int = Field(
        default=10, ge=3, le=30,
        description="Connection timeout in seconds.",
    )
    response_format: Literal["markdown", "json"] = Field(default="markdown")

    @field_validator("host")
    @classmethod
    def validate_host(cls, v: str) -> str:
        v = v.strip().lower()
        if not v or any(c in v for c in " \t\n/\\"):
            raise ValueError(f"Invalid hostname: '{v}'")
        # SSRF guard: this is a defensive tool targeting *public* C2 infrastructure.
        # Reject literal private/reserved IPs so a prompt can't scan internal infra.
        if _is_private_or_reserved(v):
            raise ValueError(f"'{v}' is a private/reserved IP - this tool targets public C2 infrastructure.")
        return v
        return v


def _probe_tls(host: str, port: int, timeout: int, tls_min: int, tls_max: int) -> dict:
    """Probe a TLS server with a specific version range and capture its response."""
    try:
        ctx = ssl.create_default_context()
        ctx.minimum_version = tls_min
        ctx.maximum_version = tls_max
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        with socket.create_connection((host, port), timeout=timeout) as sock:
            with ctx.wrap_socket(sock, server_hostname=host) as ssock:
                cipher = ssock.cipher()
                version = ssock.version()
                cert = ssock.getpeercert(binary_form=True)
                return {
                    "version": version,
                    "cipher": cipher[0] if cipher else "?",
                    "cipher_bits": cipher[2] if cipher else 0,
                    "cert_sha256": hashlib.sha256(cert).hexdigest()[:16] if cert else "?",
                    "alpn": getattr(ssock, "selected_alpn_protocol", lambda: None)() or None,
                }
    except (ssl.SSLError, socket.error, socket.timeout, OSError):
        return {"version": None, "cipher": None, "cert_sha256": None, "alpn": None,
                "error": "TLS handshake failed"}


def _probe_all(host: str, port: int, timeout: int) -> list[dict]:
    """Run the 3 TLS probes and return only successful (version-known) results."""
    probes = [
        _probe_tls(host, port, timeout, ssl.TLSVersion.TLSv1_2, ssl.TLSVersion.TLSv1_2),
        _probe_tls(host, port, timeout, ssl.TLSVersion.TLSv1_3, ssl.TLSVersion.TLSv1_3),
        _probe_tls(host, port, timeout, ssl.TLSVersion.MINIMUM_SUPPORTED, ssl.TLSVersion.MAXIMUM_SUPPORTED),
    ]
    return [p for p in probes if p.get("version") is not None]


def _jarm_hash(probes: list[dict]) -> str:
    """Hash the probe results into a fingerprint string."""
    parts = []
    for p in probes:
        if p.get("version") is None:
            parts.append("000000000000")
        else:
            parts.append(f"{p['version']}:{p['cipher']}")
    joined = "|".join(parts)
    return hashlib.sha256(joined.encode()).hexdigest()[:62]


def _host_resolves_public(host: str) -> bool:
    """DNS-rebinding guard: True if the host is a public IP or resolves ONLY to
    public IPs (no private/reserved RFC1918 / loopback / link-local addresses).
    A literal private IP is already rejected by the input validator; this closes
    the gap where a hostname resolves to an internal address (e.g. cloud metadata
    service 169.254.169.254 or RFC1918 infrastructure).
    """
    import ipaddress
    try:
        ipaddress.ip_address(host)  # literal IP, check it directly.
        return not _is_private_or_reserved(host)
    except ValueError:
        pass
    try:
        infos = socket.getaddrinfo(host, None, socket.AF_INET, socket.SOCK_STREAM)
    except socket.gaierror:
        return False  # unresolvable - treat as unsafe
    ips = {info[4][0] for info in infos}
    return bool(ips) and all(not _is_private_or_reserved(ip) for ip in ips)


@mcp.tool(
    name="jarm_fingerprint",
    annotations={"readOnlyHint": True, "destructiveHint": False,
                 "idempotentHint": True, "openWorldHint": True},
)
async def jarm_fingerprint(params: JarmFingerprintInput) -> str:
    """Fingerprint a TLS server (JARM-style) to identify C2/malware infrastructure.
    Probes the server with multiple TLS configurations and hashes the
    negotiated cipher + version + certificate. Identical fingerprints indicate
    the same underlying software - useful for attributing C2 servers.
    **No API key required** - uses stdlib ssl/socket only. Read-only: it does not
    mutate the attacker registry.
    **Note**: this is a *JARM-style* hash (SHA256 over negotiated TLS fields), not
    Salesforce's 10-probe JARM algorithm it is NOT comparable to public JARM
    databases (jarmdb). Use it for self-consistent clustering of C2 infra.
    **Worked Examples**

    1. *Fingerprint a suspected C2 server*:
       ``jarm_fingerprint(host="evil-c2.example.com")``

    2. *Fingerprint a non-standard port*:
       ``jarm_fingerprint(host="1.2.3.4", port=8443)``

    3. *JSON output*:
       ``jarm_fingerprint(host="c2.example.com", response_format="json")``
    """
    _audit_log("jarm_fingerprint", {"host": params.host, "port": params.port})

    # DNS-rebinding guard: reject hosts that resolve to private/reserved IPs.
    public = await asyncio.to_thread(_host_resolves_public, params.host)
    if not public:
        result = {"host": params.host, "port": params.port, "fingerprint": None,
                  "note": "Host resolves to a private/reserved IP DNS-rebinding guard rejected it."}
        if params.response_format == "json":
            return json.dumps(result, indent=2)
        return (f"# JARM Fingerprint - `{params.host}:{params.port}`\n\n"
                f"⚠️ **Rejected**: host resolves to a private/reserved IP.")

    # Offload the blocking TLS probes to a worker thread so the async event loop
    # never stalls on socket I/O (a slow/unreachable host would otherwise block
    # the whole server for up to timeout*3 seconds).
    successful = await asyncio.to_thread(_probe_all, params.host, params.port, params.timeout)

    if not successful:
        result = {"host": params.host, "port": params.port, "fingerprint": None,
                  "note": "TLS handshake failed - port may not be TLS or host unreachable."}
        if params.response_format == "json":
            return json.dumps(result, indent=2)
        return f"# JARM Fingerprint - `{params.host}:{params.port}`\n\n⚠️ **TLS handshake failed** - not a TLS service or host unreachable."

    fingerprint = _jarm_hash(successful)

    if params.response_format == "json":
        return _truncate_if_needed(json.dumps({
            "host": params.host,
            "port": params.port,
            "fingerprint": fingerprint,
            "tls_versions": [p["version"] for p in successful],
            "ciphers": [p["cipher"] for p in successful],
            "cert_sha256": successful[0]["cert_sha256"],
            "alpn": successful[0].get("alpn"),
        }, indent=2))

    lines = [f"# JARM Fingerprint - `{params.host}:{params.port}`", "",
             f"**Fingerprint**: `{fingerprint}`", ""]
    lines.append("| TLS Version | Cipher |")
    lines.append("|-------------|--------|")
    for p in successful:
        lines.append(f"| {p['version']} | `{p['cipher']}` |")
    if successful[0].get("alpn"):
        lines.append("")
        lines.append(f"**ALPN**: `{successful[0]['alpn']}`")
    lines.append("")
    lines.append(f"**Cert SHA256** (first 16): `{successful[0]['cert_sha256']}`")
    lines.append("")
    lines.append("_Compare this fingerprint against known C2/malware JARM databases to attribute the server._")
    return _truncate_if_needed("\n".join(lines))
