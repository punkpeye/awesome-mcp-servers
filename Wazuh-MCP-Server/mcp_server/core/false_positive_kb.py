#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
False-positive knowledge base - a persistent, TTL'd suppression set of IOC
(IPs, domains, hashes) that analysts have marked as false positives.

Unlike the investigation history (a full audit trail), this store is a
*fast-lookup* suppression set: the 3-Sum correlation engine consults it before
scoring to auto-exclude known-noisy indicators (CDNs, public DNS, scanners,
shared infrastructure), so the same false positive never re-triggers Engine A.

Populated by:
- blueteam_mark_investigated(verdict="false_positive")

Consumed by:
- three_sum_correlation (auto-merged into exclude_srcips)

Persistence (BLUETEAM_FALSE_POSITIVE_KB=path, optional):
- JSONL entries {"ioc", "ts", "source", "reason"} appended atomically (tmp+rename).
- TTL: BLUETEAM_FALSE_POSITIVE_TTL seconds (default 30d, 0 = never expire);
    expired entries are skipped on lookup and pruned on flush. A TTL means a
    once-noisy indicator that later turns malicious can re-enter detection.
- Cap: BLUETEAM_FALSE_POSITIVE_MAX entries (default 5000); oldest evicted.
"""
from __future__ import annotations
import json, logging, os, time
from pathlib import Path

logger = logging.getLogger("blue_team_mcp.false_positive_kb")

_KB_PATH = os.environ.get("BLUETEAM_FALSE_POSITIVE_KB", "")
_KB_TTL = int(os.environ.get("BLUETEAM_FALSE_POSITIVE_TTL", "2592000"))  # 30 days
_KB_MAX = int(os.environ.get("BLUETEAM_FALSE_POSITIVE_MAX", "5000"))

# {ioc: {"ts": float, "source": str, "reason": str}} - normalized (lowercased) keys
_ENTRIES: dict[str, dict] = {}

# Sweep guard: sweep at most once per 60s to avoid O(n) on every lookup.
_LAST_SWEEP = 0.0
_SWEEP_INTERVAL = 60.0


def _norm(v: str) -> str:
    return (v or "").strip().lower()


def _expired(entry: dict) -> bool:
    return _KB_TTL > 0 and (time.time() - entry["ts"]) > _KB_TTL


def _sweep(force: bool = False) -> int:
    """Drop expired entries from memory; return count removed."""
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
        _ENTRIES.pop(ioc, None)
    return len(stale)


def _flush() -> None:
    """Rewrite the JSONL file atomically with the current entries"""
    if not _KB_PATH:
        return
    _sweep(force=True)
    if _KB_MAX > 0 and len(_ENTRIES) > _KB_MAX:
        for ioc in sorted(_ENTRIES, key=lambda k: _ENTRIES[k]["ts"])[:len(_ENTRIES) - _KB_MAX]:
            _ENTRIES.pop(ioc, None)
    try:
        path = Path(_KB_PATH)
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".jsonl.tmp")
        with open(tmp, "w", encoding="utf-8") as f:
            for ioc, e in sorted(_ENTRIES.items()):
                f.write(json.dumps({"ioc": ioc, "ts": round(e["ts"], 3),
                                    "source": e["source"], "reason": e["reason"]},
                                   ensure_ascii=False) + "\n")
        os.replace(tmp, path)
    except Exception:
        logger.warning("false_positive_kb flush failed", exc_info=True)


def _load() -> None:
    """Load persisted entries at import time"""
    if not _KB_PATH:
        return
    try:
        path = Path(_KB_PATH)
        if not path.exists():
            return
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                e = json.loads(line)
                ioc = _norm(e.get("ioc", ""))
                if not ioc:
                    continue
                ts = float(e.get("ts", 0))
                if _KB_TTL > 0 and (time.time() - ts) > _KB_TTL:
                    continue  # expired on load
                _ENTRIES[ioc] = {"ts": ts, "source": str(e.get("source", "persisted")),
                                 "reason": str(e.get("reason", ""))}
            except (ValueError, TypeError):
                continue
        if _ENTRIES:
            logger.info("false_positive_kb loaded %d entries from %s", len(_ENTRIES), _KB_PATH)
    except OSError:
        logger.warning("false_positive_kb load failed: %s", _KB_PATH)


def register_false_positive(ioc: str, source: str = "manual", reason: str = "") -> None:
    """Register an IOC (IP/domain/hash) as a known false positive."""
    v = _norm(ioc)
    if not v:
        return
    _ENTRIES[v] = {"ts": time.time(), "source": source, "reason": (reason or "")[:512]}
    _flush()


def is_false_positive(ioc: str) -> bool:
    """True if the IOC is a registered, unexpired false positive."""
    _sweep()
    return _norm(ioc) in _ENTRIES


def false_positive_iocs() -> set[str]:
    """All active (unexpired) false-positive IOCs - feed into 3-Sum exclude_srcips"""
    _sweep()
    return set(_ENTRIES.keys())


def false_positive_stats() -> dict:
    """Operational stats: size, TTL, cap, sources"""
    _sweep(force=True)
    sources: dict[str, int] = {}
    for e in _ENTRIES.values():
        sources[e["source"]] = sources.get(e["source"], 0) + 1
    return {
        "entries": len(_ENTRIES),
        "ttl_seconds": _KB_TTL,
        "max_entries": _KB_MAX,
        "persisted_path": _KB_PATH or None,
        "sources": sources,
    }


def clear_false_positive_kb() -> None:
    """Clear all entries from memory"""
    _ENTRIES.clear()
    if _KB_PATH:
        try:
            Path(_KB_PATH).unlink(missing_ok=True)
        except OSError:
            pass


_load()
