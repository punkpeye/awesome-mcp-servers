#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Shared TTL cache + async rate limiter for threat-intel providers.
Replaces the per-provider `_cache` dict + `_semaphore` + `_last_request`
triplet with two small reusable classes. Each provider configures its own
TTL, max concurrency, and min interval between requests.
"""
from __future__ import annotations
import asyncio, time
from typing import Any


class TTLCache:
    """In-memory TTL cache with LRU eviction.
    Thread-safety note: threat-intel lookups run on a single asyncio event
    loop, so no locking is needed. If the MCP server ever runs multiple
    workers (multi-process), switch to a shared store (Redis/memcached).
    """

    def __init__(self, maxsize: int = 1000):
        self.maxsize = maxsize
        self._data: dict[str, tuple[float, Any]] = {}

    def get(self, key: str) -> Any | None:
        """Return the cached value if present and unexpired, else None."""
        entry = self._data.get(key)
        if entry is None:
            return None
        expiry, value = entry
        if time.monotonic() < expiry:
            return value
        del self._data[key]
        return None

    def set(self, key: str, value: Any, ttl: float) -> None:
        """Store a value with a TTL. Evicts oldest (LRU) when over maxsize."""
        if len(self._data) >= self.maxsize:
            # Evict the first-inserted key (dict preserves insertion order)
            self._data.pop(next(iter(self._data)))
        self._data[key] = (time.monotonic() + ttl, value)

    def __len__(self) -> int:
        return len(self._data)


class AsyncRateLimiter:
    """Async semaphore + min-interval rate limiter (token-bucket-lite).

    Usage::

        limiter = AsyncRateLimiter(max_concurrent=3, min_interval=0.1)
        async with limiter:
            resp = await _api_call(...)

    The ``async with`` block acquires a concurrency slot, waits until at least
    ``min_interval`` seconds have passed since the previous request, and
    records the completion time on exit.
    """

    def __init__(self, max_concurrent: int = 3, min_interval: float = 0.1):
        self._semaphore = asyncio.Semaphore(max_concurrent)
        self.min_interval = min_interval
        self._last_request = 0.0

    async def __aenter__(self) -> "AsyncRateLimiter":
        await self._semaphore.acquire()
        elapsed = time.monotonic() - self._last_request
        if elapsed < self.min_interval:
            await asyncio.sleep(self.min_interval - elapsed)
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        self._last_request = time.monotonic()
        self._semaphore.release()


# Shared namespaced cache + limiter registry
# One backing TTLCache shared across all threat-intel providers; keys are
# namespaced ("provider:key") so each provider keeps its own TTL (passed to
# cache_set) while memory is consolidated in a single store. Rate limiters stay
# per-provider via a registry because different APIs have different
# concurrency / min-interval limits.

_SHARED_CACHE = TTLCache(maxsize=10_000)


def cache_get(namespace: str, key: str) -> Any | None:
    """Return the cached value for a namespaced key, or None if absent/expired."""
    return _SHARED_CACHE.get(f"{namespace}:{key}")


def cache_set(namespace: str, key: str, value: Any, ttl: float) -> None:
    """Store a value under a namespaced key with the provider's TTL."""
    _SHARED_CACHE.set(f"{namespace}:{key}", value, ttl)


_limiters: dict[str, AsyncRateLimiter] = {}


def get_limiter(namespace: str, max_concurrent: int = 3,
                min_interval: float = 0.1) -> AsyncRateLimiter:
    """Return (or lazily create) the rate limiter for a provider namespace."""
    if namespace not in _limiters:
        _limiters[namespace] = AsyncRateLimiter(max_concurrent=max_concurrent,
                                                min_interval=min_interval)
    return _limiters[namespace]


def cache_stats() -> dict:
    """Operational stats for the shared cache + limiter registry."""
    return {
        "cache_entries": len(_SHARED_CACHE),
        "cache_maxsize": _SHARED_CACHE.maxsize,
        "limiter_namespaces": sorted(_limiters.keys()),
    }
