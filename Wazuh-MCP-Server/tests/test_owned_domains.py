#!/usr/bin/env python3
"""
Tests for owned-domain management - get/set + redaction-memo invalidation.
"""
from __future__ import annotations
import os
os.environ.setdefault("WAZUH_INDEXER_URL", "https://idx:9200")
os.environ.setdefault("WAZUH_INDEXER_PASSWORD", "pw")
from mcp_server.core import redact


def test_set_and_get_owned_domains():
    redact.set_owned_domains("Example.COM, gov.example.org")
    assert redact.get_owned_domains() == {"example.com", "gov.example.org"}


def test_set_clears_redaction_memo():
    redact.set_owned_domains("victim.example.com")
    redact._REDACT_MEMO.clear()
    redact._redact_alert_data("email user@example.com")
    assert len(redact._REDACT_MEMO) >= 1
    redact.set_owned_domains("other.example.org")  # must invalidate cached masks
    assert len(redact._REDACT_MEMO) == 0


def test_protect_victim_masks_owned_keeps_attacker(monkeypatch):
    # The server default may be 'full' (or the fail-safe may have fired) - set the
    # policy explicitly on the module so this test is independent of import order.
    monkeypatch.setattr(redact, "BLUETEAM_REDACTION_POLICY", "protect_victim")
    redact.set_owned_domains("victim.example.com")
    owned = redact._redact_alert_data("csirt@victim.example.com")
    attacker = redact._redact_alert_data("bad@evil.com")
    assert "csirt@victim.example.com" not in owned   # owned email masked
    assert "bad@evil.com" in attacker                # attacker email kept


import pytest

# To lazy to build this sh*t xD kidding...
@pytest.mark.asyncio
async def test_set_owned_domains_gated(monkeypatch):
    import mcp_server.tools.owned_domains as od
    monkeypatch.setattr(od, "BLUETEAM_ALLOW_RUNTIME_DOMAINS", False)
    redact.set_owned_domains("before.example.com")
    result = await od.blueteam_set_owned_domains(od.OwnedDomainsSetInput(domains="evil.com"))
    assert "disabled" in result.lower()
    assert redact.get_owned_domains() == {"before.example.com"}  # unchanged


@pytest.mark.asyncio
async def test_set_owned_domains_allowed(monkeypatch):
    import mcp_server.tools.owned_domains as od
    monkeypatch.setattr(od, "BLUETEAM_ALLOW_RUNTIME_DOMAINS", True)
    result = await od.blueteam_set_owned_domains(od.OwnedDomainsSetInput(domains="evil.com"))
    assert "updated" in result.lower()
    assert redact.get_owned_domains() == {"evil.com"}
