#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
IOC lifecycle store - JSONL-persistent record of discovered IOCs with
time-decayed recency scoring (reuses three_sum_core.compute_time_decay_weight).

Feeds:
  - blueteam_extract_iocs (extracted indicators from alert text)
  - 3-Sum Engine A trigger IPs (confirmed attacker indicators)

Queries return IOCs ranked by (decay_weight, count) so the LLM can prioritize
active IOCs without re-querying the indexer.

Persistence: BLUETEAM_IOC_STORE (JSONL, atomic rewrite), cap
BLUETEAM_IOC_STORE_MAX (default 50000, oldest evicted).
"""
from __future__ import annotations
import ipaddress, json, logging, os, re, time
from datetime import datetime, timezone
from pathlib import Path
from mcp_server.correlation.three_sum_core import compute_time_decay_weight
from mcp_server import BLUETEAM_AUTO_PROMOTE_IPS

logger = logging.getLogger("blue_team_mcp.ioc_store")

_STORE_PATH = os.environ.get("BLUETEAM_IOC_STORE", "")
_STORE_MAX = int(os.environ.get("BLUETEAM_IOC_STORE_MAX", "50000"))
_STORE_TTL = int(os.environ.get("BLUETEAM_IOC_STORE_TTL", "7776000"))  # 90 days
_BATCH_CAP = 10  # max co-occurrence batches remembered per IOC
_STORE_MIN_DECAY_EVICT = 0.01  # only TTL-evict entries with negligible decay

# {ioc: {"kind", "first_ts", "last_ts", "count", "source"}} — normalized keys
_ENTRIES: dict[str, dict] = {}

_HASH_RE = re.compile(r"^[a-fA-F0-9]{32}(?:[a-fA-F0-9]{8}|[a-fA-F0-9]{24})?$")  # md5/sha1/sha256


def _classify(ioc: str) -> str:
    try:
        ipaddress.ip_address(ioc)
        return "ip"
    except ValueError:
        pass
    if ioc.startswith(("http://", "https://")):
        return "url"
    if "@" in ioc:
        return "email"
    if _HASH_RE.fullmatch(ioc):
        return "hash"
    if "." in ioc and " " not in ioc:
        return "domain"
    return "other"


def _now() -> float:
    return time.time()


def _iso(ts: float) -> str:
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _maybe_promote() -> None:
    """Auto-promote consistently-observed IPs (count >= 3, decay >= 0.8) to the
    attacker registry so they stay unmasked. Opt-in: BLUETEAM_AUTO_PROMOTE_IPS=true.
    """
    if not BLUETEAM_AUTO_PROMOTE_IPS:
        return
    try:
        from mcp_server.core.attacker_registry import register_attacker_ioc
    except ImportError:
        return
    for ioc, e in _ENTRIES.items():
        if e["kind"] != "ip" or e["count"] < 3:
            continue
        if compute_time_decay_weight(_iso(e["first_ts"]), _iso(e["last_ts"])) >= 0.8:
            register_attacker_ioc(ioc, source="auto_promote")


def record_ioc(ioc: str, source: str = "extract") -> None:
    """Record one IOC observation (bump count + last_seen on repeat)."""
    v = (ioc or "").strip().lower()
    if not v or len(v) > 256:
        return
    now = _now()
    if v in _ENTRIES:
        e = _ENTRIES[v]
        e["count"] += 1
        e["last_ts"] = now
    else:
        _ENTRIES[v] = {"kind": _classify(v), "first_ts": now, "last_ts": now,
                       "count": 1, "source": source, "batches": []}
    _flush()


def record_iocs(iocs: list[str], source: str = "extract", batch_id: int | None = None) -> None:
    """Record a batch of IOCs in one flush.
    batch_id (default: current ms timestamp) tags the batch for co-occurrence
    edges in the attack graph - IOCs seen in the same extraction/trigger set are linked.
    """
    if not iocs:
        return
    now = _now()
    bid = batch_id if batch_id is not None else int(now * 1000)
    for ioc in iocs:
        v = (ioc or "").strip().lower()
        if not v or len(v) > 256:
            continue
        if v in _ENTRIES:
            e = _ENTRIES[v]
            e["count"] += 1
            e["last_ts"] = now
            if bid not in e["batches"]:
                e["batches"].append(bid)
                e["batches"] = e["batches"][-_BATCH_CAP:]
        else:
            _ENTRIES[v] = {"kind": _classify(v), "first_ts": now, "last_ts": now,
                           "count": 1, "source": source, "batches": [bid]}
    _flush()
    _maybe_promote()


def query_iocs(kind: str | None = None, since_days: int | None = None,
               min_count: int = 1, top_n: int = 50,
               include_batches: bool = False) -> list[dict]:
    """Ranked IOC list: filter by kind / recency / min_count, sorted by decay then count."""
    cutoff = _now() - (since_days * 86400) if since_days else None
    out = []
    for ioc, e in _ENTRIES.items():
        if kind and e["kind"] != kind:
            continue
        if cutoff is not None and e["last_ts"] < cutoff:
            continue
        if e["count"] < min_count:
            continue
        weight = compute_time_decay_weight(_iso(e["first_ts"]), _iso(e["last_ts"]))
        age_days = round((_now() - e["last_ts"]) / 86400, 1)
        row = {"ioc": ioc, "kind": e["kind"], "count": e["count"],
               "first_seen": _iso(e["first_ts"]), "last_seen": _iso(e["last_ts"]),
               "decay_weight": round(weight, 3), "age_days": age_days}
        if include_batches:
            row["batches"] = list(e.get("batches", []))
        out.append(row)
    out.sort(key=lambda x: (x["decay_weight"], x["count"]), reverse=True)
    return out[:top_n]


def ioc_stats() -> dict:
    kinds: dict[str, int] = {}
    total_count = 0
    for e in _ENTRIES.values():
        kinds[e["kind"]] = kinds.get(e["kind"], 0) + 1
        total_count += e["count"]
    return {"entries": len(_ENTRIES), "kinds": kinds, "total_observations": total_count,
            "persisted_path": _STORE_PATH or None, "max_entries": _STORE_MAX}


def clear_ioc_store() -> None:
    _ENTRIES.clear()
    if _STORE_PATH:
        try:
            Path(_STORE_PATH).unlink(missing_ok=True)
        except OSError:
            pass


def _flush() -> None:
    if not _STORE_PATH:
        return
    now = _now()
    # TTL eviction: entries older than TTL with negligible decay are dead weight.
    # Old entries still receiving hits (high count/decay) are kept regardless.
    if _STORE_TTL > 0:
        stale_ttl = []
        for ioc, e in _ENTRIES.items():
            age = now - e["last_ts"]
            if age > _STORE_TTL:
                w = compute_time_decay_weight(_iso(e["first_ts"]), _iso(e["last_ts"]))
                if w < _STORE_MIN_DECAY_EVICT:
                    stale_ttl.append(ioc)
        for ioc in stale_ttl:
            del _ENTRIES[ioc]
    # Cap enforcement: evict entries with the LOWEST decay weight first.
    # Among equally-decayed entries, evict the oldest last-seen.
    # This preserves high-signal IOCs (frequently observed, high decay)
    # over low-signal ones even when both are within TTL.
    if _STORE_MAX > 0 and len(_ENTRIES) > _STORE_MAX:
        ranked = []
        for ioc, e in _ENTRIES.items():
            w = compute_time_decay_weight(_iso(e["first_ts"]), _iso(e["last_ts"]))
            ranked.append((w, e["last_ts"], ioc))
        ranked.sort(key=lambda x: (x[0], x[1]))  # asc: worst decay, then oldest
        for _, _, ioc in ranked[:len(_ENTRIES) - _STORE_MAX]:
            del _ENTRIES[ioc]
    try:
        path = Path(_STORE_PATH)
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".jsonl.tmp")
        with open(tmp, "w", encoding="utf-8") as f:
            for ioc, e in sorted(_ENTRIES.items()):
                f.write(json.dumps({"ioc": ioc, "kind": e["kind"],
                                    "first_ts": round(e["first_ts"], 3),
                                    "last_ts": round(e["last_ts"], 3),
                                    "count": e["count"], "source": e["source"],
                                    "batches": list(e.get("batches", []))},
                                   ensure_ascii=False) + "\n")
        os.replace(tmp, path)
    except Exception:
        logger.warning("ioc store flush failed", exc_info=True)


def _load() -> None:
    if not _STORE_PATH:
        return
    try:
        path = Path(_STORE_PATH)
        if not path.exists():
            return
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                e = json.loads(line)
                ioc = (e.get("ioc") or "").strip().lower()
                if not ioc:
                    continue
                _ENTRIES[ioc] = {"kind": str(e.get("kind", _classify(ioc))),
                                 "first_ts": float(e.get("first_ts", 0)),
                                 "last_ts": float(e.get("last_ts", 0)),
                                 "count": int(e.get("count", 1)),
                                 "source": str(e.get("source", "persisted")),
                                 "batches": list(e.get("batches", []))[:_BATCH_CAP] if isinstance(e.get("batches"), list) else []}
            except (ValueError, TypeError):
                continue
        if _ENTRIES:
            logger.info("ioc store loaded %d entries from %s", len(_ENTRIES), _STORE_PATH)
    except OSError:
        logger.warning("ioc store load failed: %s", _STORE_PATH)


_load()
