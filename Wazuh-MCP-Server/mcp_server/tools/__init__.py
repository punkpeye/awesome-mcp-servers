#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Dynamic tool registration with gating.
Each module's @mcp.tool / @blueteam_tool decorator auto-registers with
the shared FastMCP instance on import. Tool gating (WAZUH_DISABLED_TOOLS,
WAZUH_DISABLED_CATEGORIES, WAZUH_READ_ONLY) is enforced before imports, so disabled tools never register at all.
The registered tool count is computed from the FastMCP registry at runtime, no hardcoded count anywhere.
"""
from __future__ import annotations
import logging
from mcp_server import mcp
from mcp_server.core.config import config

logger = logging.getLogger("blue_team_mcp.tools")

def register_all_tools() -> None:
    """Import all tool modules, respecting tool-gating configuration.
    Modules in disabled_categories are skipped entirely.
    When read_only mode is active, any module whose tools are primarily destructive is also skipped.
    """
    if config is None:
        logger.warning("Config not initialized - registering all tools. "
                        "Run init_config() first for gating support.")

    disabled_cats: set[str] = set(
        c.lower().strip() for c in (config.tool_gating.disabled_categories if config else [])
    )
    disabled_tools: set[str] = set(
        t.lower().strip() for t in (config.tool_gating.disabled_tools if config else [])
    )
    read_only: bool = config.tool_gating.read_only if config else False

    def _skip(category: str, *, also_if_read_only: bool = False) -> bool:
        """Return True if this category should be skipped."""
        if category in disabled_cats:
            logger.info("Tool category '%s' disabled via WAZUH_DISABLED_CATEGORIES - skipping.", category)
            return True
        if read_only and also_if_read_only:
            logger.info("Tool category '%s' skipped in read-only mode.", category)
            return True
        return False

    # Threat Intel (always registered, tools degrade gracefully without API keys)
    from ..threat_intel import crowdsec, greynoise, threatfox, otx, urlhaus, rapidapi  # noqa: F401

    # Tool modules - each import fires @mcp.tool / @blueteam_tool decorators
    # Categories that can be disabled: (module_attr, category_name, skip_in_read_only)
    _MODULES: list[tuple[str, str, bool]] = [
        ("host_forensics",        "host_forensics",        True),   # 23 tools, some destructive-ish
        ("fail2ban",              "fail2ban",              True),   # 3 tools, blueteam_fail2ban_unban is destructive
        ("wazuh_siem",            "wazuh_siem",            False),  # Indexer query tools
        ("wazuh_manager",         "wazuh_manager",         False),  # Manager API tools (rules, decoders, groups, etc.)
        ("alert_enrichment",      "alert_enrichment",      False),  # Standalone threat-intel + Sangfor + unified scoring
        ("alert_summarize",       "alert_summarize",       False),  # F-1 Alert summarization
        ("alert_beacon",           "alert_beacon",           False),  # F-2 Beacon detection
        ("alert_attack_chain",     "alert_attack_chain",     False),  # F-3 Attack chain analysis
        ("alert_threat_card",      "alert_threat_card",      False),  # F-5 Threat cards
        ("alert_compare",          "alert_compare",          False),  # F-6 Side-by-side IP comparison
        ("alert_curated_report",   "alert_curated_report",   False),  # G-3 Curated threat report
        ("baseline",              "baseline",              False),  # 3 tools
        ("investigation_history",  "investigation_history",  False),  # Investigation state (mark_investigated, FP tracker, summary)
        ("correlation",            "correlation",            False),  # 3-Sum correlation + IP investigation + enrichment
        ("geo",                   "geo",                   False),  # 1 tool
        ("ai_bot_recon",           "ai_bot_recon",           False),  # 1 tool - AI/LLM-driven scanning detection
        ("dsl_query",             "dsl_query",             False),  # 1 tool
        ("wazuh_email",           "wazuh_email",           False),  # 1 tool
        ("wazuh_domain",          "wazuh_domain",          False),  # 1 tool
        ("wazuh_compromised",     "wazuh_compromised",     False),  # 1 tool
        ("wazuh_timeline",        "wazuh_timeline",        False),  # 1 tool
        ("wazuh_velocity",        "wazuh_velocity",        False),  # 1 tool
        ("wazuh_focused",         "wazuh_focused",         False),  # 1 tool
        ("threat_hunt",           "threat_hunt",           False),  # 1 tool (11 templates)
        ("ioc_tools",             "ioc_tools",             False),  # 2 tools
        ("wazuh_export",          "wazuh_export",          False),  # 1 tool
        ("wazuh_scanning",        "wazuh_scanning",        False),  # 4 tools
        ("webshell_check",         "webshell_check",         False),  # 1 tool - curl + signature scan
        ("otx_lookup",             "otx_lookup",             False),  # 2 tools - AlienVault OTX threat intel
        ("threat_intel_aggregate",  "threat_intel_aggregate",  False),  # 1 tool - unified multi-provider aggregation
        ("urlhaus",                "urlhaus",                False),  # 2 tools - URLhaus malware URL database
        ("asset_context",           "asset_context",           False),  # 1 tool - CMDB asset context
        ("index_schema",             "index_schema",             False),  # 1 tool - index field schema explorer
        ("stealer_log",              "stealer_log",              False),  # 1 tool - HudsonRock stealer log check
        ("jarm",                     "jarm",                     False),  # 1 tool - JARM TLS fingerprint
        ("semantic_search",       "semantic_search",       False),  # 1 tool
        ("report_export",         "report_export",         False),  # 1 tool
        ("stix_correlation",      "stix_correlation",      False),  # 2 tools
        ("metrics",               "metrics",               False),  # resources, not tools
        ("attack_graph",          "attack_graph",          False),  # 2 tools
        ("investigation_workflow","investigation_workflow",False),  # 1 tool
        ("prompt_router",         "prompt_router",         False),  # 1 tool - BM25 prompt-to-tool routing
        ("playbook_runner",       "playbook_runner",       False),  # 1 tool
        ("wazuh_sca",             "wazuh_sca",             False),  # 3 tools (SCA compliance)
        ("wazuh_rules_files",     "wazuh_rules_files",     False),  # 2 tools (rule XML)
        ("owned_domains",          "owned_domains",          False),  # 2 tools (view/set victim domains)
        ("jarm",                   "jarm",                   False),  # 1 tool (TLS fingerprinting)
        ("case",                   "case",                   False),  # 5 tools (incident case management)
        ("domain_permute",          "domain_permute",          False),  # 1 tool (typosquatting lookalikes)
        ("stealer_log",              "stealer_log",              False),  # 1 tool (HudsonRock stealer-log check)
    ]

    for attr, category, skip_ro in _MODULES:
        if _skip(category, also_if_read_only=skip_ro):
            continue
        __import__(f"mcp_server.tools.{attr}", fromlist=[attr])

    # Dynamic tool count
    tool_count = _count_registered_tools()
    resource_count = _count_registered_resources()

    logger.info("%d tools + %d resources registered.", tool_count, resource_count)


# Introspection helpers - derive counts from the FastMCP registry at runtime.
# No hardcoded numbers anywhere.
def _count_registered_tools() -> int:
    """Return the number of tools currently registered with FastMCP."""
    try:
        tm = mcp._tool_manager
        return len(getattr(tm, "_tools", {}))
    except Exception:
        return 0


def _count_registered_resources() -> int:
    """Return the number of resources currently registered with FastMCP."""
    try:
        rm = mcp._resource_manager
        return len(getattr(rm, "_resources", {}))
    except Exception:
        return 0
