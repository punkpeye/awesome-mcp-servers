#!/usr/bin/env python3
"""
Circuit breaker unit tests
"""
import os
import time

# Minimal env so importing mcp_server.core.http_client passes config validation.
os.environ.setdefault("WAZUH_INDEXER_URL", "https://indexer:9200")
os.environ.setdefault("WAZUH_INDEXER_PASSWORD", "test-indexer-pass")

from mcp_server.core.http_client import CircuitBreaker, CircuitOpenError  # noqa: E402


def _breaker(threshold=3, recovery=60.0):
    return CircuitBreaker(failure_threshold=threshold, recovery_timeout=recovery)


def test_opens_after_threshold():
    b = _breaker()
    b.on_failure()
    b.on_failure()
    assert b.open is False
    assert b.before_call() is True       # 2 < 3, still closed
    b.on_failure()                        # 3rd failure -> open
    assert b.open is True
    assert b.before_call() is False       # fail fast while cooling down


def test_success_resets_counter():
    b = _breaker()
    b.on_failure()
    b.on_failure()
    b.on_success()
    assert b.failures == 0
    assert b.open is False
    assert b.before_call() is True


def test_4xx_and_429_do_not_count_as_failures():
    b = _breaker()
    b.on_liveness()    # 4xx - completed response proves liveness
    b.on_throttled()   # 429 - throttle, not outage
    assert b.failures == 0
    assert b.open is False


def test_half_open_allows_single_trial():
    b = _breaker(threshold=1, recovery=0.05)
    b.on_failure()                        # open immediately
    assert b.before_call() is False       # cooling down
    time.sleep(0.1)                       # recovery elapses
    assert b.before_call() is True        # half open trial granted
    assert b.before_call() is False       # only one trial allowed
    b.on_success()
    assert b.before_call() is True        # closed again


def test_4xx_during_half_open_closes_breaker():
    b = _breaker(threshold=1, recovery=0.05)
    b.on_failure()                        # open
    time.sleep(0.1)
    assert b.before_call() is True        # half-open
    b.on_liveness()                       # 4xx proves dependency alive
    assert b.open is False
    assert b.failures == 0


def test_circuit_open_error_is_connect_error():
    # So existing `except httpx.ConnectError` handlers (Wazuh auth/indexer) catch it.
    import httpx

    assert issubclass(CircuitOpenError, httpx.ConnectError)
