#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Shared global constants and state used across Wazuh tools and correlation engine.
Centralizes module-global variables that were scattered across the monolith.
Import from here instead of duplicating across tool modules.
Note: _WAZUH_INDEX_PATTERNS, _KEYWORD_SEARCH_FIELDS, _SRCIP_FIELD_PATHS now live in ``mcp_server.wazuh.indexer``.
"""
from __future__ import annotations
import re
from typing import Any, Dict, List, Tuple, Optional

# MITRE ATT&CK tactic -> 3-Sum category mapping
MITRE_TACTIC_TO_CATEGORY: Dict[str, str] = {
    "Reconnaissance":          "A",
    "Resource Development":    "A",
    "Discovery":               "A",
    "Lateral Movement":        "B",
    "Initial Access":          "B",
    "Credential Access":       "B",
    "Privilege Escalation":    "B",
    "Defense Evasion":         "B",
    "Execution":               "B",
    "Persistence":             "C",
    "Command and Control":     "C",
    "Exfiltration":            "C",
    "Impact":                  "C",
    "Collection":              "C",
}

# MITRE ATT&CK tactic -> APT signal weight (dynamic risk scoring, MCP-TAXONOMY-V2).
# Higher = stronger APT indicator. C2/exfil/impact weigh most; recon weighs least.
MITRE_TACTIC_WEIGHTS: Dict[str, float] = {
    "Reconnaissance":        0.5,
    "Resource Development":  0.5,
    "Discovery":             0.7,
    "Initial Access":        1.0,
    "Execution":             1.2,
    "Persistence":           1.5,
    "Privilege Escalation":  1.3,
    "Defense Evasion":       1.4,
    "Credential Access":     1.2,
    "Lateral Movement":      1.3,
    "Collection":            1.2,
    "Command and Control":   2.5,
    "Exfiltration":          2.0,
    "Impact":                1.8,
}

# Known attack chain patterns (for blueteam_attack_chain)
_KNOWN_ATTACK_CHAINS: list[dict[str, Any]] = [
    {
        "id": "recon_to_bruteforce",
        "phases": ["recon", "bruteforce"],
        "pattern": [re.compile(r"^(600029|5710|5760|60100|33100)$"),
                     re.compile(r"^(5710|5712|5716|5760|6020|5551)$")],
        "description": "Reconnaissance -> Brute-force / credential attack",
        "confidence": 0.75,
    },
    {
        "id": "recon_to_exploit",
        "phases": ["recon", "exploit"],
        "pattern": [re.compile(r"^(600029|5710|5760|60100|33100)$"),
                     re.compile(r"^(31100|31300|31500|31700|33300|33800)$")],
        "description": "Reconnaissance -> Exploitation / payload delivery",
        "confidence": 0.80,
    },
    {
        "id": "bruteforce_to_access",
        "phases": ["bruteforce", "access"],
        "pattern": [re.compile(r"^(5710|5712|5716|5760|6020|5551)$"),
                     re.compile(r"^(5500|5501|5502|5503|60106|60122)$")],
        "description": "Brute-force -> Successful authentication",
        "confidence": 0.90,
    },
    {
        "id": "recon_to_c2",
        "phases": ["recon", "c2_response"],
        "pattern": [re.compile(r"^(600029|5710|5760|60100|33100)$"),
                     re.compile(r"^(606029|510|520|530|540|550|560)$")],
        "description": "Reconnaissance -> Active Response / C2 trigger",
        "confidence": 0.60,
    },
    {
        "id": "full_kill_chain",
        "phases": ["recon", "bruteforce", "access", "c2_response"],
        "pattern": [
            re.compile(r"^(600029|5710|5760|60100|33100)$"),
            re.compile(r"^(5710|5712|5716|5760|6020|5551)$"),
            re.compile(r"^(5500|5501|5502|5503|60106|60122)$"),
            re.compile(r"^(606029|510|520|530|540|550|560)$"),
        ],
        "description": "Full kill-chain: Recon -> Brute-force -> Access -> C2/Response",
        "confidence": 0.95,
    },
]

# Deduplication patterns (parent child alert relationships)
_DEDUP_PATTERNS: list[tuple[str, str]] = [
    ("606029", "data.parameters.alert.rule.id"),
    ("651",   "data.parameters.alert.rule.id"),
]

# Wazuh log tag mapping (for blueteam_wazuh_manager_logs)
_WAZUH_LOG_TAG = {
    "alerts": "wazuh-analysisd",
    "api": "wazuh-api",
    "cluster": "wazuh-clusterd",
    "integrations": "wazuh-integratord",
}

# Wazuh alerts local file path
_WAZUH_ALERTS_PATH = "/var/ossec/logs/alerts/alerts.json"
_WAZUH_ALERTS_MAX_LINES = 2000

# Sangfor blockmode severity labels
_BLOCKMODE_SEVERITY: dict[str, str] = {
    "30m": "Temporary / Low Priority",
    "1h": "Temporary / Low Priority",
    "2h": "Temporary / Low Priority",
    "3d": "Active Mitigation / Medium Priority",
    "7d": "Active Mitigation / Medium Priority",
    "permanent": "Hard Block / High Priority",
}

# Correlation engine throttle state
_last_eval_time: float = 0.0
_last_eval_result: Optional[Dict[str, Any]] = None
