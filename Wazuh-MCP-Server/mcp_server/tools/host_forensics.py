#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Host forensics tools: 23 tools for log reading, network, capture, files, hardening, users, processes.
"""
from __future__ import annotations
import json, os, re, shutil, hashlib
from datetime import datetime
from pathlib import Path
from typing import Optional, Literal
from pydantic import BaseModel, ConfigDict, Field
from mcp_server import mcp, MAX_LOG_LINES
from mcp_server.core.audit import _audit_log, _truncate_if_needed, _check_rate_limit
from mcp_server.core.redact import _redact_alert_data
from mcp_server.core.subprocess import _run, _run_async, _sanitize_regex, _validate_path, _validate_bpf_filter, _tail_file, _tool_not_found, ALLOWED_PATH_PREFIXES, CAPTURE_OUTPUT_DIR, MAX_GREP_PATTERN_LENGTH, TIMEOUT

class LogInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    lines: int = Field(default=200, description="Number of recent lines to return", ge=1, le=MAX_LOG_LINES)
    grep: Optional[str] = Field(default=None, max_length=MAX_GREP_PATTERN_LENGTH, description="Optional keyword/regex to filter lines (case-insensitive)")
    bypass_redaction: bool = Field(default=False, description="When true, skip PII/credential redaction for audit investigations")

@mcp.tool(
    name="blueteam_read_auth_log",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def blueteam_read_auth_log(params: LogInput) -> str:
    """Read and optionally filter /var/log/auth.log for SSH, sudo, and PAM events.

    Args:
        params.lines (int): How many tail lines to read (default 200, max 2000)
        params.grep (str, optional): Filter to params.lines containing this pattern
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: Matching log params.lines or error JSON
    """
    _audit_log("blueteam_read_auth_log", {"lines": params.lines})
    log_path = "/var/log/auth.log"
    # Fallback for systems using journald only
    if not Path(log_path).exists():
        cmd = ["journalctl", "-u", "ssh", "-n", str(params.lines), "--no-pager"]
        if params.grep:
            cmd += ["--grep", params.grep]
        r = _run(cmd)
        return _redact_alert_data(r["stdout"] or r["stderr"], params=params)

    content = _tail_file(log_path, params.lines)
    if params.grep:
        safe_grep = _sanitize_regex(params.grep)
        matched = [l for l in content.splitlines() if re.search(safe_grep, l, re.IGNORECASE)]
        return _redact_alert_data("\n".join(matched), params=params) if matched \
            else f"No lines matched filter: {params.grep}"
    return _redact_alert_data(content, params=params)

@mcp.tool(
    name="blueteam_read_syslog",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def blueteam_read_syslog(params: LogInput) -> str:
    """Read /var/log/syslog or journalctl for general system events.

    Args:
        params.lines (int): Lines to return
        params.grep (str, optional): Filter pattern
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: Log content
    """
    _audit_log("blueteam_read_syslog", {"lines": params.lines})
    for path in ["/var/log/syslog", "/var/log/messages"]:
        if Path(path).exists():
            content = _tail_file(path, params.lines)
            if params.grep:
                safe_grep = _sanitize_regex(params.grep)
                lines = [l for l in content.splitlines() if re.search(safe_grep, l, re.IGNORECASE)]
                return _redact_alert_data("\n".join(lines), params=params) if lines else f"No matches for: {params.grep}"
            return _redact_alert_data(content, params=params)
    # Fallback to journalctl
    cmd = ["journalctl", "-n", str(params.lines), "--no-pager"]
    if params.grep:
        cmd += ["--grep", params.grep]
    r = _run(cmd)
    return _redact_alert_data(r["stdout"] or r["stderr"], params=params)

class WebLogInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    server: str = Field(default="nginx", description="Web server: 'nginx' or 'apache'")
    log_type: str = Field(default="access", description="Log type: 'access' or 'error'")
    lines: int = Field(default=200, ge=1, le=MAX_LOG_LINES)
    grep: Optional[str] = Field(default=None, max_length=MAX_GREP_PATTERN_LENGTH, description="Optional filter pattern")
    path: Optional[str] = Field(default=None, max_length=256, description="Override log path. Auto-resolved from server+log_type if omitted.")
    bypass_redaction: bool = Field(default=False, description="When true, skip PII/credential redaction for audit investigations")

@mcp.tool(
    name="blueteam_read_web_log",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def blueteam_read_web_log(params: WebLogInput) -> str:
    """Read nginx or Apache access/error logs. Great for spotting web attacks.

    Args:
        params.server: 'nginx' or 'apache'
        params.log_type: 'access' or 'error'
        params.lines: Lines to read
        params.grep: Optional filter
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: Log params.lines
    """
    _audit_log("blueteam_read_web_log", {"lines": params.lines})
    paths = {
        "nginx": {
            "access": "/var/log/nginx/access.log",
            "error": "/var/log/nginx/error.log",
        },
        "apache": {
            "access": "/var/log/apache2/access.log",
            "error": "/var/log/apache2/error.log",
        },
    }
    server = params.server.lower()
    if server not in paths:
        return json.dumps({"error": f"Unknown server '{params.server}'. Use 'nginx' or 'apache'."})
    log_type = params.log_type.lower()
    if params.log_type not in paths[server]:
        return json.dumps({"error": f"Unknown log type '{params.log_type}'. Use 'access' or 'error'."})

    log_path = params.path if params.path else paths[server][params.log_type]
    content = _tail_file(log_path, params.lines)
    if params.grep:
        safe_grep = _sanitize_regex(params.grep)
        filtered = [l for l in content.splitlines() if re.search(safe_grep, l, re.IGNORECASE)]
        return _redact_alert_data("\n".join(filtered) if filtered else f"No matches for: {params.grep}", params=params)
    return _redact_alert_data(content, params=params)

class JournalInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    unit: Optional[str] = Field(default=None, max_length=64, description="Systemd unit name, e.g. 'sshd', 'nginx', 'cron'")
    since: Optional[str] = Field(default="1 hour ago", max_length=64, description="Time range, e.g. '2 hours ago', '2024-01-15 10:00'")
    lines: int = Field(default=200, ge=1, le=MAX_LOG_LINES)
    grep: Optional[str] = Field(default=None, max_length=MAX_GREP_PATTERN_LENGTH)
    bypass_redaction: bool = Field(default=False, description="When true, skip PII/credential redaction for audit investigations")

@mcp.tool(
    name="blueteam_journalctl",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def blueteam_journalctl(params: JournalInput) -> str:
    """Query systemd journal for any service. Useful for services without flat log files.

    Args:
        params.unit: Systemd unit (omit for all units)
        params.since: Time range string
        params.lines: Max lines
        params.grep: Filter pattern
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: Journal output
    """
    _audit_log("blueteam_journalctl", {"unit": params.unit})
    cmd = ["journalctl", "--no-pager", "-n", str(params.lines)]
    if params.unit:
        cmd += ["-u", params.unit]
    if params.since:
        cmd += ["--since", params.since]
    if params.grep:
        cmd += ["--grep", params.grep]
    r = _run(cmd)
    return _redact_alert_data(r["stdout"] or r["stderr"], params=params)


class BypassRedactionInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    bypass_redaction: bool = Field(default=False, description="When true, skip PII/credential redaction for audit investigations")


# NETWORK MONITORING
@mcp.tool(
    name="blueteam_list_listening_ports",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def blueteam_list_listening_ports(params: BypassRedactionInput) -> str:
    """List all TCP/UDP ports currently listening, with owning process.
    Equivalent to 'ss -tulpn'. Identifies unexpected services.

    Args:
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: Port table with process names and PIDs
    """
    _audit_log("blueteam_list_listening_ports", {})
    r = _run(["ss", "-tulpn"])
    if r["returncode"] != 0:
        r = _run(["netstat", "-tulpn"])
    return _redact_alert_data(r["stdout"] or r["stderr"], bypass=params.bypass_redaction)


@mcp.tool(
    name="blueteam_list_connections",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def blueteam_list_connections(params: BypassRedactionInput) -> str:
    """List all established TCP connections with remote IPs and local processes.
    Useful for spotting unexpected outbound connections (beaconing, exfil).

    Args:
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: Active connection table
    """
    _audit_log("blueteam_list_connections", {})
    r = _run(["ss", "-tnp", "state", "established"])
    if r["returncode"] != 0:
        r = _run(["netstat", "-tnp"])
    return _redact_alert_data(r["stdout"] or r["stderr"], bypass=params.bypass_redaction)


class CaptureInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    interface: str = Field(default="eth0", max_length=32, description="Network interface to capture on")
    count: int = Field(default=100, description="Number of packets to capture", ge=1, le=5000)
    filter_expr: Optional[str] = Field(default=None, max_length=200, description="BPF filter expression, e.g. 'port 80', 'host 10.0.0.5'")
    output_file: Optional[str] = Field(default=None, max_length=256, description="Optional path to save .pcap file (must be under CAPTURE_OUTPUT_DIR)")
    bypass_redaction: bool = Field(default=False, description="When true, return raw internal IPs without RFC1918 masking. Overrides BLUETEAM_REDACT_PII for this call only — use for internal audit investigations.")


@mcp.tool(
    name="blueteam_capture_traffic",
    annotations={"readOnlyHint": False, "destructiveHint": False, "idempotentHint": False, "openWorldHint": True}
)
async def blueteam_capture_traffic(params: CaptureInput) -> str:
    """Capture live network traffic using tcpdump. Requires root or CAP_NET_RAW.
    Read-only for packet inspection; writes pcap files when params.output_file is set.
    Makes network I/O (openWorldHint).

    Args:
        params.interface: Network interface
        params.count: Packet count to capture then stop
        params.filter_expr: BPF filter (optional)
        params.output_file: Save pcap to this params.path (optional, under CAPTURE_OUTPUT_DIR)
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: Packet summary or params.path to saved pcap
    """
    if not _check_rate_limit():
        return json.dumps({"error": "Rate limit exceeded"})
    if not shutil.which("tcpdump"):
        return _tool_not_found("tcpdump")
    if params.filter_expr:
        ok, err = _validate_bpf_filter(params.filter_expr)
        if not ok:
            return json.dumps({"error": err})
    output_path = params.output_file
    if output_path:
        if not output_path.startswith("/"):
            output_path = os.path.join(CAPTURE_OUTPUT_DIR, output_path)
        ok, err = _validate_path(output_path, [CAPTURE_OUTPUT_DIR])
        if not ok:
            return json.dumps({"error": f"output_file must be under {CAPTURE_OUTPUT_DIR}: {err}"})

    cmd = ["tcpdump", "-i", params.interface, "-c", str(params.count), "-nn", "-q"]
    if params.filter_expr:
        cmd.append(params.filter_expr)
    if output_path:
        cmd += ["-w", output_path]

    r = _run(cmd, timeout=60)
    result = r["stdout"] + r["stderr"]
    if output_path and r["returncode"] == 0:
        result = json.dumps({"status": "captured", "file": output_path, "packets": params.count})
    else:
        # Redact internal RFC1918 IP from stdout text output.
        # Connection metadata contains internal endpoint IP; mask them without altering
        # the packet-capture file itself (which is forensic evidence and always unredacted).
        result = _redact_alert_data(result, params=params)
    _audit_log("blueteam_capture_traffic", {"interface": params.interface, "count": params.count}, result[:200])
    return result


class HashFileInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    path: str = Field(..., max_length=4096, description="Absolute path to file to hash (must be under /, /var, /etc, /home, /opt)")
    algorithm: str = Field(default="sha256", description="Hash algorithm: 'md5', 'sha1', 'sha256', 'sha512'")
    bypass_redaction: bool = Field(default=False, description="When true, skip PII/credential redaction for audit investigations")


@mcp.tool(
    name="blueteam_hash_file",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True},
)
async def blueteam_hash_file(params: HashFileInput) -> str:
    """Compute a cryptographic hash of a file. Use to detect tampering.
    Pair with blueteam_lookup_hash_virustotal to check for known malware.

    Args:
        params.path: File params.path
        params.algorithm: Hash algorithm
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: JSON with file params.path, size, hash params.algorithm, and hash value
    """
    algo_map = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha256": hashlib.sha256,
        "sha512": hashlib.sha512,
    }
    algo = params.algorithm.lower()
    if algo not in algo_map:
        return json.dumps({"error": f"Unknown algorithm '{params.algorithm}'. Use: md5, sha1, sha256, sha512"})

    ok, err = _validate_path(params.path, ALLOWED_PATH_PREFIXES)
    if not ok:
        return json.dumps({"error": f"Path not allowed: {err}"})

    p = Path(params.path)
    if not p.exists():
        return json.dumps({"error": f"File not found: {params.path}"})
    if not p.is_file():
        return json.dumps({"error": f"Not a regular file: {params.path}"})

    try:
        h = algo_map[algo]()
        with open(p, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        result = json.dumps({
            "path": str(p),
            "size_bytes": p.stat().st_size,
            "algorithm": algo,
            "hash": h.hexdigest(),
            "modified": datetime.fromtimestamp(p.stat().st_mtime).isoformat(),
        }, indent=2)
        _audit_log("blueteam_hash_file", {"path": params.path, "algorithm": algo}, result[:200])
        return _redact_alert_data(result, params=params)
    except PermissionError:
        return json.dumps({"error": f"Permission denied reading {params.path}"})
    except Exception as e:
        return json.dumps({"error": str(e)})


@mcp.tool(
    name="blueteam_find_suid_files",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def blueteam_find_suid_files(params: BypassRedactionInput) -> str:
    """Find all SUID/SGID binaries on the system. Unexpected SUID files
    can indicate privilege escalation backdoors.

    Args:
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: List of SUID/SGID files with permissions and owner
    """
    _audit_log("blueteam_find_suid_files", {})
    r = _run(["find", "/", "-type", "f", r"-perm", "/6000", "-ls"], timeout=60)
    return _redact_alert_data(r["stdout"] or r["stderr"], bypass=params.bypass_redaction)


@mcp.tool(
    name="blueteam_find_world_writable",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def blueteam_find_world_writable(params: BypassRedactionInput) -> str:
    """Find world-writable files and directories (excluding /proc, /sys, /dev).
    World-writable files in unexpected places are common persistence mechanisms.

    Args:
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: List of world-writable paths
    """
    _audit_log("blueteam_find_world_writable", {})
    cmd = [
        "find", "/",
        "-not", "-path", "/proc/*",
        "-not", "-path", "/sys/*",
        "-not", "-path", "/dev/*",
        "-not", "-path", "/run/*",
        "-perm", "-o+w",
        "-ls"
    ]
    r = _run(cmd, timeout=60)
    return _redact_alert_data(r["stdout"] or r["stderr"], bypass=params.bypass_redaction)


class RootkitInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    tool: str = Field(default="rkhunter", description="Tool to use: 'rkhunter' or 'chkrootkit'")
    bypass_redaction: bool = Field(default=False, description="When true, skip PII/credential redaction for audit investigations")


@mcp.tool(
    name="blueteam_rootkit_scan",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": False, "openWorldHint": True}
)
async def blueteam_rootkit_scan(params: RootkitInput) -> str:
    """Run a rootkit scanner (rkhunter or chkrootkit) to check for known rootkits.

    Args:
        params.tool: Scanner to use
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: Scan output with warnings and clean checks
    """
    _audit_log("blueteam_rootkit_scan", {"scanner": params.scanner})
    tool = params.tool.lower()
    if params.tool == "rkhunter":
        if not shutil.which("rkhunter"):
            return _tool_not_found("rkhunter")
        r = _run(["rkhunter", "--check", "--skip-keypress", "--nocolors"], timeout=120)
    elif params.tool == "chkrootkit":
        if not shutil.which("chkrootkit"):
            return _tool_not_found("chkrootkit")
        r = _run(["chkrootkit"], timeout=120)
    else:
        return json.dumps({"error": f"Unknown params.tool '{params.tool}'. Use 'rkhunter' or 'chkrootkit'"})

    return _redact_alert_data(r["stdout"] or r["stderr"], params=params)


# SYSTEM HARDENING
@mcp.tool(
    name="blueteam_lynis_audit",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": False, "openWorldHint": False}
)
async def blueteam_lynis_audit(params: BypassRedactionInput) -> str:
    """Run a Lynis system hardening audit. Checks hundreds of security controls
    and produces prioritized recommendations. Takes 1-2 minutes.

    Args:
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: Lynis audit output with hardening index and suggestions
    """
    _audit_log("blueteam_lynis_audit", {})
    if not shutil.which("lynis"):
        return _tool_not_found("lynis")
    r = _run(["lynis", "audit", "system", "--quick", "--no-colors"], timeout=180)
    return _redact_alert_data(r["stdout"] or r["stderr"], bypass=params.bypass_redaction)


@mcp.tool(
    name="blueteam_check_updates",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": False, "openWorldHint": True}
)
async def blueteam_check_updates(params: BypassRedactionInput) -> str:
    """Check for available security updates (Debian/Ubuntu: apt, RHEL: dnf/yum).

    Args:
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: List of packages with available updates
    """
    _audit_log("blueteam_check_updates", {})
    if shutil.which("apt"):
        r = _run(["apt", "list", "--upgradeable"], timeout=60)
        return _redact_alert_data(r["stdout"] or r["stderr"], bypass=params.bypass_redaction)
    elif shutil.which("dnf"):
        r = _run(["dnf", "check-update", "--security"], timeout=60)
        return _redact_alert_data(r["stdout"] or r["stderr"], bypass=params.bypass_redaction)
    elif shutil.which("yum"):
        r = _run(["yum", "check-update", "--security"], timeout=60)
        return _redact_alert_data(r["stdout"] or r["stderr"], bypass=params.bypass_redaction)
    return json.dumps({"error": "No supported package manager found (apt, dnf, yum)"})


@mcp.tool(
    name="blueteam_check_open_firewall",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def blueteam_check_open_firewall(params: BypassRedactionInput) -> str:
    """Show current firewall rules (iptables/nftables/ufw). Identifies
    overly permissive rules or missing protections.

    Args:
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: Current firewall ruleset
    """
    _audit_log("blueteam_check_open_firewall", {})
    if shutil.which("ufw"):
        r = _run(["ufw", "status", "verbose"])
        if r["returncode"] == 0:
            return _redact_alert_data(r["stdout"], bypass=params.bypass_redaction)
    if shutil.which("nft"):
        r = _run(["nft", "list", "ruleset"])
        if r["returncode"] == 0:
            return _redact_alert_data(r["stdout"], bypass=params.bypass_redaction)
    r = _run(["iptables", "-L", "-n", "-v"])
    return _redact_alert_data(r["stdout"] or r["stderr"], bypass=params.bypass_redaction)



# USER & SESSION MONITORING
@mcp.tool(
    name="blueteam_who_is_logged_in",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def blueteam_who_is_logged_in(params: BypassRedactionInput) -> str:
    """Show currently logged-in users, their source IPs, and session times.
    Useful for detecting unauthorized active sessions.

    Args:
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: Active user session table
    """
    _audit_log("blueteam_who_is_logged_in", {})
    r = _run(["w", "-h"])
    return _redact_alert_data(r["stdout"] or r["stderr"], bypass=params.bypass_redaction)


@mcp.tool(
    name="blueteam_last_logins",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def blueteam_last_logins(params: BypassRedactionInput) -> str:
    """Show recent login history from /var/log/wtmp. Includes successful
    and failed logins with source IP and timestamps.

    Args:
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: Login history (last 50 entries)
    """
    _audit_log("blueteam_last_logins", {})
    r = _run(["last", "-n", "50", "-a", "-i"])
    return _redact_alert_data(r["stdout"] or r["stderr"], bypass=params.bypass_redaction)


@mcp.tool(
    name="blueteam_failed_logins",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def blueteam_failed_logins(params: BypassRedactionInput) -> str:
    """Show all failed login attempts from /var/log/btmp (lastb).
    High counts from a single IP indicate brute force.

    Args:
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: Failed login history (last 100 entries)
    """
    _audit_log("blueteam_failed_logins", {})
    r = _run(["lastb", "-n", "100", "-a", "-i"])
    if r["returncode"] != 0:
        # Try parsing auth.log directly
        r2 = _run(["grep", "-i", r"failed password\|authentication failure", "/var/log/auth.log"])
        lines = r2["stdout"].splitlines()
        return _redact_alert_data("\n".join(lines[-100:]) if lines else "No failed logins found in auth.log", bypass=params.bypass_redaction)
    return _redact_alert_data(r["stdout"] or r["stderr"], bypass=params.bypass_redaction)


@mcp.tool(
    name="blueteam_sudo_history",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def blueteam_sudo_history(params: BypassRedactionInput) -> str:
    """Show recent sudo command usage from auth.log.
    Identifies privilege escalation abuse.

    Args:
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: Lines from auth.log containing sudo activity
    """
    _audit_log("blueteam_sudo_history", {})
    r = _run(["grep", "sudo:", "/var/log/auth.log"])
    lines = r["stdout"].splitlines()
    return _redact_alert_data("\n".join(lines[-200:]) if lines else "No sudo activity found (or no auth.log)", bypass=params.bypass_redaction)


@mcp.tool(
    name="blueteam_list_users",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def blueteam_list_users(params: BypassRedactionInput) -> str:
    """List all local user accounts with UID, GID, home dir, and shell.
    Highlights users with UID 0 (root-level) and users with login shells.

    Args:
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: JSON array of user accounts with risk flags
    """
    _audit_log("blueteam_list_users", {})
    users = []
    try:
        with open("/etc/passwd") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split(":")
                if len(parts) < 7:
                    continue
                uid = int(parts[2])
                shell = parts[6]
                has_login_shell = shell not in ["/sbin/nologin", "/usr/sbin/nologin", "/bin/false", ""]
                users.append({
                    "username": parts[0],
                    "uid": uid,
                    "gid": int(parts[3]),
                    "home": parts[5],
                    "shell": shell,
                    "flags": {
                        "uid_zero_root": uid == 0,
                        "has_login_shell": has_login_shell,
                        "system_account": uid < 1000 and uid != 0,
                    }
                })
    except Exception as e:
        return json.dumps({"error": str(e)})

    # Sort UID 0 first, then regular users, then system accounts.
    users.sort(key=lambda u: (not u["flags"]["uid_zero_root"], not u["flags"]["has_login_shell"], u["uid"]))
    return _redact_alert_data(json.dumps(users, indent=2), bypass=params.bypass_redaction)


@mcp.tool(
    name="blueteam_check_ssh_authorized_keys",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def blueteam_check_ssh_authorized_keys(params: BypassRedactionInput) -> str:
    """List all SSH authorized_keys files across all user home directories.
    Unexpected keys indicate backdoors or persistence mechanisms.

    Args:
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: JSON with each user's authorized keys (fingerprints)
    """
    _audit_log("blueteam_check_ssh_authorized_keys", {})
    result = {}
    for home in Path("/home").iterdir():
        ak = home / ".ssh" / "authorized_keys"
        if ak.exists():
            try:
                result[home.name] = ak.read_text().strip().splitlines()
            except PermissionError:
                result[home.name] = ["<permission denied>"]

    # Also check root
    root_ak = Path("/root/.ssh/authorized_keys")
    if root_ak.exists():
        try:
            result["root"] = root_ak.read_text().strip().splitlines()
        except PermissionError:
            result["root"] = ["<permission denied>"]

    return _redact_alert_data(json.dumps(result, indent=2) if result else json.dumps({"result": "No authorized_keys files found"}), bypass=params.bypass_redaction)


# PROCESS & CRON ANALYSIS
@mcp.tool(
    name="blueteam_list_processes",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def blueteam_list_processes(params: BypassRedactionInput) -> str:
    """List all running processes with CPU, memory, PID, and command line.
    Useful for spotting unexpected processes or cryptominers.

    Args:
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: Process table sorted by CPU usage
    """
    _audit_log("blueteam_list_processes", {})
    r = _run(["ps", "auxf"])
    return _redact_alert_data(r["stdout"] or r["stderr"], bypass=params.bypass_redaction)


@mcp.tool(
    name="blueteam_list_cron_jobs",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def blueteam_list_cron_jobs(params: BypassRedactionInput) -> str:
    """List all system and user cron jobs. Attackers often add cron jobs
    for persistence. Check for unexpected entries.

    Args:
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: All cron jobs across system and users
    """
    _audit_log("blueteam_list_cron_jobs", {})
    output = []

    # System crontabs
    for path in ["/etc/crontab", "/etc/cron.d/"]:
        p = Path(path)
        if p.is_file():
            output.append(f"=== {path} ===\n{p.read_text()}")
        elif p.is_dir():
            for f in p.iterdir():
                try:
                    output.append(f"=== {f} ===\n{f.read_text()}")
                except Exception:
                    pass

    # User crontabs
    r = _run(["ls", "/var/spool/cron/crontabs"])
    if r["returncode"] == 0:
        for user in r["stdout"].strip().splitlines():
            r2 = _run(["crontab", "-u", user.strip(), "-l"])
            if r2["returncode"] == 0:
                output.append(f"=== crontab for {user} ===\n{r2['stdout']}")

    return _redact_alert_data("\n\n".join(output) if output else "No cron jobs found (or insufficient permissions)", bypass=params.bypass_redaction)


# SYSTEM HEALTH
@mcp.tool(
    name="blueteam_system_health",
    annotations={"readOnlyHint": True, "destructiveHint": False, "idempotentHint": True, "openWorldHint": True}
)
async def blueteam_system_health(params: BypassRedactionInput) -> str:
    """Get an overview of system health: uptime, disk, memory, CPU load.
    Useful baseline before deeper investigation.

    Args:
        params.bypass_redaction: When true, skip PII/credential redaction for audit investigations.

    Returns:
        str: JSON with system vitals
    """
    _audit_log("blueteam_system_health", {})
    uptime = _run(["uptime", "-p"])
    disk = _run(["df", "-h", "--exclude-type=tmpfs", "--exclude-type=devtmpfs"])
    mem = _run(["free", "-h"])
    load = _run(["cat", "/proc/loadavg"])
    hostname = _run(["hostname", "-f"])
    kernel = _run(["uname", "-r"])

    return _redact_alert_data(json.dumps({
        "hostname": hostname["stdout"].strip(),
        "kernel": kernel["stdout"].strip(),
        "uptime": uptime["stdout"].strip(),
        "load_average": load["stdout"].strip(),
        "memory": mem["stdout"],
        "disk": disk["stdout"],
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }, indent=2), bypass=params.bypass_redaction)
