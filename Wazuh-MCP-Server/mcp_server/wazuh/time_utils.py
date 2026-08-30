#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Time window parsing, relative deltas, auto bucket intervals.
"""
from __future__ import annotations
import re
from datetime import datetime, timedelta
from typing import Optional

_RELATIVE_TIME_RE = re.compile(r"^(\d+)([smhdw])$")
_ISO_TIME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}")

_UNIT_MAP = {"s": "seconds", "m": "minutes", "h": "hours", "d": "days", "w": "weeks"}


def _relative_delta(n: int, unit: str) -> timedelta:
    if unit not in _UNIT_MAP:
        return timedelta(days=365)
    return timedelta(**{_UNIT_MAP[unit]: n})


def _parse_now_math(expr: str, now: datetime) -> datetime:
    """Resolve an OpenSearch date-math expression ('now', 'now-24h', 'now-7d/d')."""
    body = expr[3:].lower().split("/")[0]  # strip 'now' and any '/d' rounding suffix
    dt = now
    for m in re.finditer(r"([+-])(\d+)([smhdw])", body):
        sign, n, unit = m.group(1), int(m.group(2)), m.group(3)
        delta = _relative_delta(n, unit)
        dt = dt - delta if sign == "-" else dt + delta
    return dt


def _parse_time_window(
    since: Optional[str], until: Optional[str], default_back: timedelta = timedelta(days=365),
) -> tuple[str, str]:
    now = datetime.utcnow()

    def _resolve(expr: str, default: datetime) -> datetime:
        expr = expr.strip()
        if not expr:
            return default
        if _ISO_TIME_RE.match(expr):
            return datetime.fromisoformat(expr.replace("Z", "+00:00").rstrip("Z"))
        m = _RELATIVE_TIME_RE.match(expr)
        if m:
            return now - _relative_delta(int(m.group(1)), m.group(2))
        if expr.lower().startswith("now"):
            return _parse_now_math(expr, now)
        return default

    until_dt = _resolve(until, now) if until else now
    since_dt = _resolve(since, now - default_back) if since else (now - default_back)
    fmt = "%Y-%m-%dT%H:%M:%SZ"
    return since_dt.strftime(fmt), until_dt.strftime(fmt)


def _duration_minutes(since: str, until: str) -> float:
    try:
        s = datetime.fromisoformat(since.replace("Z", "+00:00").rstrip("Z"))
        u = datetime.fromisoformat(until.replace("Z", "+00:00").rstrip("Z"))
        return (u - s).total_seconds() / 60.0
    except Exception:
        return 60.0


def _auto_bucket_interval(window_duration_minutes: float) -> str:
    raw = window_duration_minutes / 100
    if raw <= 1: return "1m"
    elif raw <= 5: return "5m"
    elif raw <= 15: return "15m"
    elif raw <= 60: return "1h"
    elif raw <= 360: return "6h"
    else: return "1d"
