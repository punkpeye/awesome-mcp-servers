#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
In-memory + JSONL-persistent attacker-IOC registry.

Values registered here are treated as confirmed/suspected attacker indicators
and are EXEMPTED from shape-based masking in the redaction pipeline (never from
Layer 1 credential stripping - credentials stay masked everywhere).

Populated by:
  - 3-Sum Engine A trigger IPs (three_sum_correlation)
  - Threat-intel enrichment lookups (CrowdSec / ThreatFox)
  - True-positive investigation verdicts (blueteam_mark_investigated)

Persistence (BLUETEAM_ATTACKER_REGISTRY=path, optional):
  - JSONL entries {"ioc", "ts", "source"} appended atomically (tmp+rename).
  - TTL: BLUETEAM_ATTACKER_REGISTRY_TTL seconds (default 7d, 0 = never expire);
    expired entries are skipped on lookup and pruned on flush.
  - Cap: BLUETEAM_ATTACKER_REGISTRY_MAX entries (default 10000); oldest evicted.
"""
from __future__ import annotations
import ipaddress, json, logging, os, time
from pathlib import Path

logger = logging.getLogger("blue_team_mcp.attacker_registry")

_REGISTRY_PATH = os.environ.get("BLUETEAM_ATTACKER_REGISTRY", "")
_REGISTRY_TTL = int(os.environ.get("BLUETEAM_ATTACKER_REGISTRY_TTL", "604800"))
_REGISTRY_MAX = int(os.environ.get("BLUETEAM_ATTACKER_REGISTRY_MAX", "10000"))

# {ioc: {"ts": float, "source": str}} - normalized (lowercased) keys
_ENTRIES: dict[str, dict] = {}
# Derived fast-lookup sets (exact IPs/full values + parent domains for suffix match)
_ATTACKER_EXACT: set[str] = set()
_ATTACKER_DOMAINS: set[str] = set()

# Lazy-sweep guard: sweep at most once per 60s to avoid O(n) on every is_attacker_ioc()
_LAST_SWEEP = 0.0
_SWEEP_INTERVAL = 60.0

_SEP_CHARS = " /\\"


def _looks_like_ip(v: str) -> bool:
    try:
        ipaddress.ip_address(v)
        return True
    except ValueError:
        return False


def _looks_like_domain(v: str) -> bool:
    return "." in v and not any(c in v for c in _SEP_CHARS)


def _classify(v: str) -> str:
    """Return 'ip' | 'email' | 'domain' | 'other'."""
    if _looks_like_ip(v):
        return "ip"
    if "@" in v:
        return "email"
    if _looks_like_domain(v):
        return "domain"
    return "other"


def _add_entry(ioc: str, source: str) -> None:
    """Insert a normalized entry into memory + derived sets."""
    _ENTRIES[ioc] = {"ts": time.time(), "source": source}
    kind = _classify(ioc)
    if kind == "domain":
        _ATTACKER_DOMAINS.add(ioc)
    elif kind == "email":
        dom = ioc.rsplit("@", 1)[-1]
        if _looks_like_domain(dom):
            _ATTACKER_DOMAINS.add(dom)
        _ATTACKER_EXACT.add(ioc)
    else:
        _ATTACKER_EXACT.add(ioc)


def _expired(entry: dict) -> bool:
    return _REGISTRY_TTL > 0 and (time.time() - entry["ts"]) > _REGISTRY_TTL


def _sweep_expired(force: bool = False) -> int:
    """Drop expired entries from memory; return count removed.
    Uses a 'lazy guard' - sweeps at most once per _SWEEP_INTERVAL seconds
    unless ``force=True`` (used by flush/clear paths).
    """
    global _LAST_SWEEP
    if not force:
        now = time.time()
        if now - _LAST_SWEEP < _SWEEP_INTERVAL:
            return 0
        _LAST_SWEEP = now
    else:
        _LAST_SWEEP = time.time()
    stale = [ioc for ioc, e in _ENTRIES.items() if _expired(e)]
    for ioc in stale:
        _remove_entry(ioc)
    return len(stale)


def _remove_entry(ioc: str) -> None:
    _ENTRIES.pop(ioc, None)
    _ATTACKER_EXACT.discard(ioc)
    _ATTACKER_DOMAINS.discard(ioc)


def _flush() -> None:
    """Rewrite the JSONL file atomically with the current (pruned) entries."""
    if not _REGISTRY_PATH:
        return
    # sweep expired + enforce cap: keep most-recent MAX entries
    _sweep_expired(force=True)
    if _REGISTRY_MAX > 0 and len(_ENTRIES) > _REGISTRY_MAX:
        for ioc in sorted(_ENTRIES, key=lambda k: _ENTRIES[k]["ts"])[:len(_ENTRIES) - _REGISTRY_MAX]:
            _remove_entry(ioc)
    try:
        path = Path(_REGISTRY_PATH)
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".jsonl.tmp")
        with open(tmp, "w", encoding="utf-8") as f:
            for ioc, e in sorted(_ENTRIES.items()):
                f.write(json.dumps({"ioc": ioc, "ts": round(e["ts"], 3), "source": e["source"]},
                                   ensure_ascii=False) + "\n")
        os.replace(tmp, path)
    except Exception:
        logger.warning("attacker registry flush failed", exc_info=True)


def _load() -> None:
    """Load persisted entries at import time."""
    if not _REGISTRY_PATH:
        return
    try:
        path = Path(_REGISTRY_PATH)
        if not path.exists():
            return
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                e = json.loads(line)
                ioc = (e.get("ioc") or "").strip().lower()
                ts = float(e.get("ts", 0))
                src = str(e.get("source", "persisted"))
                if not ioc:
                    continue
                if _REGISTRY_TTL > 0 and (time.time() - ts) > _REGISTRY_TTL:
                    continue  # expired on load
                _ENTRIES[ioc] = {"ts": ts, "source": src}
                kind = _classify(ioc)
                if kind == "domain":
                    _ATTACKER_DOMAINS.add(ioc)
                elif kind == "email":
                    dom = ioc.rsplit("@", 1)[-1]
                    if _looks_like_domain(dom):
                        _ATTACKER_DOMAINS.add(dom)
                    _ATTACKER_EXACT.add(ioc)
                else:
                    _ATTACKER_EXACT.add(ioc)
            except (ValueError, TypeError):
                continue
        if _ENTRIES:
            logger.info("attacker registry loaded %d entries from %s", len(_ENTRIES), _REGISTRY_PATH)
    except OSError:
        logger.warning("attacker registry load failed: %s", _REGISTRY_PATH)


def register_attacker_ioc(value: str, source: str = "manual") -> None:
    """Register a single attacker indicator (IP, domain, or email)."""
    v = (value or "").strip().lower()
    if not v:
        return
    _add_entry(v, source)
    _flush()


def register_attacker_ips(values: list[str], source: str = "manual") -> None:
    for v in values or []:
        register_attacker_ioc(v, source=source)


def register_attacker_domains(values: list[str], source: str = "manual") -> None:
    for v in values or []:
        register_attacker_ioc(v, source=source)


def is_attacker_ioc(value: str) -> bool:
    """True if value (or its domain) is a registered, unexpired attacker indicator.
    Lazy-sweeps expired entries (at most once per 60s) before checking.
    """
    _sweep_expired()  # lazy guard: O(1) unless interval elapsed
    v = (value or "").strip().lower()
    if not v:
        return False
    if v in _ATTACKER_EXACT:
        return True
    dom = v.rsplit("@", 1)[-1] if "@" in v else v
    # Match: exact domain OR exactly one subdomain level (e.g. www.evil.com)
    # matches evil.com, but subdo.evil.com does not).
    for d in _ATTACKER_DOMAINS:
        if dom == d:
            return True
        if dom.endswith("." + d):
            prefix = dom[:-(len(d) + 1)]
            if "." not in prefix:  # exactly one subdomain level
                return True
    return False


def registry_stats() -> dict:
    """Operational stats: size, TTL, cap, sources."""
    _sweep_expired(force=True)  # explicit diagnostic - always sweep
    sources: dict[str, int] = {}
    for e in _ENTRIES.values():
        sources[e["source"]] = sources.get(e["source"], 0) + 1
    return {
        "entries": len(_ENTRIES),
        "ttl_seconds": _REGISTRY_TTL,
        "max_entries": _REGISTRY_MAX,
        "persisted_path": _REGISTRY_PATH or None,
        "sources": sources,
    }


def clear_attacker_registry() -> None:
    """Clear all entries from memory (and the file if configured)."""
    _ENTRIES.clear()
    _ATTACKER_EXACT.clear()
    _ATTACKER_DOMAINS.clear()
    if _REGISTRY_PATH:
        try:
            Path(_REGISTRY_PATH).unlink(missing_ok=True)
        except OSError:
            pass


_load()
