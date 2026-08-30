#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Subprocess execution, path validation, BPF filtering, tool helpers.
"""
from __future__ import annotations
import asyncio, os, re, subprocess, json
from pathlib import Path
from typing import List, Dict, Any, Optional

TIMEOUT = 30
MAX_GREP_PATTERN_LENGTH = 200
ALLOWED_PATH_PREFIXES = [
    p.strip() for p in os.environ.get("BLUETEAM_ALLOWED_PATHS", "/var:/etc:/home:/opt:/usr").split(":")
    if p.strip()
]
CAPTURE_OUTPUT_DIR = os.environ.get("BLUETEAM_CAPTURE_DIR", "/tmp")
_BPF_SAFE_RE = re.compile(r"^[a-zA-Z0-9\.\s\-\_\:\(\)]+$")
_BPF_FORBIDDEN = (" -w", "-w ", " -r", "-r ", "|", ";", "&&", "||", "`", "$(")


# Subprocess execution
def _run(cmd: List[str], timeout: int = TIMEOUT) -> Dict[str, Any]:
    """Run a shell command and return stdout/stderr/returncode dict."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return {"stdout": result.stdout, "stderr": result.stderr, "returncode": result.returncode}
    except subprocess.TimeoutExpired:
        return {"stdout": "", "stderr": f"Command timed out after {timeout}s", "returncode": -1}
    except FileNotFoundError:
        return {"stdout": "", "stderr": f"Command not found: {cmd[0]}", "returncode": -1}
    except Exception as e:
        return {"stdout": "", "stderr": str(e), "returncode": -1}


async def _run_async(cmd: List[str], timeout: int = TIMEOUT) -> Dict[str, Any]:
    """Non-blocking wrapper around _run() — offloads subprocess to a thread pool."""
    return await asyncio.to_thread(_run, cmd, timeout)


def _tool_not_found(tool: str) -> str:
    return json.dumps({
        "error": f"'{tool}' is not installed or not in PATH.",
        "fix": f"Install it with: sudo apt install {tool} (Debian/Ubuntu)"
    }, indent=2)


def _tail_file(path: str, lines: int) -> str:
    """Return last N lines of a file, with error handling."""
    p = Path(path)
    if not p.exists():
        return json.dumps({"error": f"File not found: {path}"})
    r = _run(["tail", "-n", str(lines), path])
    return r["stdout"] or r["stderr"]


# Input validation
def _sanitize_regex(pattern: str) -> str:
    """Sanitize grep pattern to mitigate ReDoS. Use simple substring when regex metacharacters present."""
    if not pattern:
        return pattern
    if len(pattern) > MAX_GREP_PATTERN_LENGTH:
        return pattern[:MAX_GREP_PATTERN_LENGTH]
    dangerous = set("+*{?()[]|^$")
    if any(c in pattern for c in dangerous):
        return re.escape(pattern)
    return pattern


def _validate_path(path: str, allowed_prefixes: List[str], allow_symlinks: bool = False) -> tuple[bool, str]:
    """Validate path is under allowed prefixes. Returns (ok, error_msg)."""
    try:
        resolved = Path(path).resolve()
    except Exception:
        return False, "Invalid path"
    if ".." in path:
        return False, "Path traversal (..) not allowed"
    for prefix in allowed_prefixes:
        prefix_path = Path(prefix).resolve()
        try:
            resolved.relative_to(prefix_path)
            return True, ""
        except ValueError:
            continue
    return False, f"Path not under allowed prefixes: {allowed_prefixes}"


def _validate_bpf_filter(expr: str) -> tuple[bool, str]:
    """Validate BPF filter expression to prevent argument injection."""
    if not expr:
        return True, ""
    if len(expr) > 200:
        return False, "BPF filter too long"
    lower = expr.lower()
    for fb in _BPF_FORBIDDEN:
        if fb in lower or fb in expr:
            return False, "BPF filter contains forbidden characters (no -w, -r, shell meta)"
    if not _BPF_SAFE_RE.match(expr):
        return False, "BPF filter contains invalid characters"
    return True, ""
