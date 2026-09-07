#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Case store - persistent JSONL incident records.
A case is a durable, queryable incident object that ties together the srcips,
IOCs, and investigation verdicts produced by the 3-Sum engine, pivot suggestions,
and analyst triage. Unlike the flat per-IP investigation history, a case groups a
whole campaign/incident into one record.
Persistence (BLUETEAM_CASE_STORE=path, optional):
- JSONL, one case object per line, rewritten atomically on change (tmp+rename).
- Cap: BLUETEAM_CASE_MAX (default 500); newest cases kept.
"""
from __future__ import annotations
import json, os, uuid, logging
from pathlib import Path
from datetime import datetime, timezone

logger = logging.getLogger("blue_team_mcp.case_store")

_CASE_PATH = os.environ.get("BLUETEAM_CASE_STORE", "")
_CASE_MAX = int(os.environ.get("BLUETEAM_CASE_MAX", "500"))

# {case_id: case}
_cases: dict[str, dict] = {}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _new_id() -> str:
    return "case_" + uuid.uuid4().hex[:12]


def _flush() -> None:
    if not _CASE_PATH:
        return
    try:
        path = Path(_CASE_PATH)
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".jsonl.tmp")
        ordered = sorted(_cases.values(), key=lambda c: c.get("created_at", ""), reverse=True)[:_CASE_MAX]
        with open(tmp, "w", encoding="utf-8") as f:
            for c in ordered:
                f.write(json.dumps(c, ensure_ascii=False) + "\n")
        os.replace(tmp, path)
    except Exception:
        logger.warning("case store flush failed", exc_info=True)


def _load() -> None:
    if not _CASE_PATH:
        return
    try:
        path = Path(_CASE_PATH)
        if not path.exists():
            return
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                c = json.loads(line)
                if c.get("case_id"):
                    _cases[c["case_id"]] = c
            except (ValueError, TypeError):
                continue
    except OSError:
        logger.warning("case store load failed: %s", _CASE_PATH)


def create_case(title: str, srcips: list[str] | None = None, notes: str = "") -> dict:
    cid = _new_id()
    now = _now()
    case = {
        "case_id": cid,
        "title": (title or "").strip()[:200] or cid,
        "created_at": now,
        "updated_at": now,
        "srcips": sorted(set(srcips or [])),
        "iocs": [],
        "verdicts": [],
        "notes": (notes or "")[:2000],
    }
    _cases[cid] = case
    _flush()
    return case


def add_iocs(case_id: str, iocs: list[str]) -> dict | None:
    case = _cases.get(case_id)
    if not case:
        return None
    existing = set(case.get("iocs", []))
    case["iocs"] = sorted(existing | {i for i in iocs if i})
    case["updated_at"] = _now()
    _flush()
    return case


def add_verdict(case_id: str, srcip: str, verdict: str, notes: str = "") -> dict | None:
    case = _cases.get(case_id)
    if not case:
        return None
    case.setdefault("verdicts", []).append({
        "srcip": srcip, "verdict": verdict, "notes": (notes or "")[:500], "ts": _now(),
    })
    if srcip and srcip not in case.setdefault("srcips", []):
        case["srcips"] = sorted(case["srcips"] + [srcip])
    case["updated_at"] = _now()
    _flush()
    return case


def get_case(case_id: str) -> dict | None:
    return _cases.get(case_id)


def list_cases() -> list[dict]:
    return sorted(_cases.values(), key=lambda c: c.get("created_at", ""), reverse=True)


def case_timeline(case_id: str) -> list[dict]:
    """Chronological event timeline for a case (creation + verdicts)."""
    case = _cases.get(case_id)
    if not case:
        return []
    events = [{"ts": case.get("created_at", ""), "event": "case_created",
               "detail": case.get("title", "")}]
    for v in case.get("verdicts", []):
        events.append({"ts": v.get("ts", ""), "event": "verdict",
                       "srcip": v.get("srcip", ""), "verdict": v.get("verdict", ""),
                       "detail": v.get("notes", "")})
    events.sort(key=lambda e: e.get("ts", ""))
    return events


def case_stats() -> dict:
    return {"cases": len(_cases), "path": _CASE_PATH or None, "max": _CASE_MAX}


_load()
