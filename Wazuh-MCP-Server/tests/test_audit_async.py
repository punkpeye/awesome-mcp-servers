#!/usr/bin/env python3
"""
Tests for the async audit writer _audit_log enqueues (non-blocking), and flush_audit_log drains the queue to disk.
"""
from __future__ import annotations
import os, json
os.environ.setdefault("WAZUH_INDEXER_URL", "https://idx:9200")
os.environ.setdefault("WAZUH_INDEXER_PASSWORD", "pw")
import mcp_server.core.audit as a


def _drain_queue():
    while True:
        try:
            a._AUDIT_QUEUE.get_nowait()
        except a.queue.Empty:
            break


def test_audit_log_enqueues_and_flushes(monkeypatch, tmp_path):
    logfile = tmp_path / "audit.jsonl"
    monkeypatch.setattr(a, "BLUETEAM_AUDIT_LOG", str(logfile))
    monkeypatch.setattr(a, "_AUDIT_WORKER_STARTED", True)  # deterministic: no daemon thread
    _drain_queue()

    a._audit_log("tool_a", {"ip": "1.2.3.4"}, "result one")
    a._audit_log("tool_b", {"ip": "5.6.7.8"}, "result two")
    a.flush_audit_log()

    lines = [json.loads(l) for l in logfile.read_text().strip().splitlines()]
    assert [e["tool"] for e in lines] == ["tool_a", "tool_b"]


def test_audit_log_redacts_params(monkeypatch, tmp_path):
    logfile = tmp_path / "audit.jsonl"
    monkeypatch.setattr(a, "BLUETEAM_AUDIT_LOG", str(logfile))
    monkeypatch.setattr(a, "_AUDIT_WORKER_STARTED", True)
    _drain_queue()

    a._audit_log("t", {"email": "csirt@tangerangkota.go.id"}, "")
    a.flush_audit_log()

    line = json.loads(logfile.read_text().strip().splitlines()[0])
    # victim email in params must be masked before hitting disk
    assert "csirt@tangerangkota.go.id" not in json.dumps(line["params"])


def test_flush_empty_queue_is_noop(monkeypatch, tmp_path):
    logfile = tmp_path / "audit.jsonl"
    monkeypatch.setattr(a, "BLUETEAM_AUDIT_LOG", str(logfile))
    monkeypatch.setattr(a, "_AUDIT_WORKER_STARTED", True)
    _drain_queue()
    a.flush_audit_log()  # nothing queued must not crash or create the file
    assert not logfile.exists()
