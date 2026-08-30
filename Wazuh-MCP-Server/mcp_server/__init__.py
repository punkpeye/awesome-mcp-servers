#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Blue Team MCP Server - shared FastMCP instance, config bootstrap, and constants.
At import time this module:
  1. Configures stderr logging.
  2. Creates the FastMCP server instance (needs MCP_HOST / MCP_PORT from env).
  3. Calls ``init_config()`` from ``mcp_server.core.config`` to build the typed
     Config singleton and validate it (raises ConfigurationError on fatal issues).
  4. Populates backward-compatible module-level vars from the config singleton
     so existing ``from mcp_server import WAZUH_API_URL, ...`` imports keep working.
Modules SHOULD migrate to ``from mcp_server.core.config import config`` over
time; the module-level vars here are a transition shim.
"""
from __future__ import annotations
import os
import sys
import logging

# Logging - stderr only (stdout is the MCP JSON-RPC channel)
logging.basicConfig(
    level=os.environ.get("LOG_LEVEL", "INFO"),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger("blue_team_mcp")

# FastMCP instance - needs host/port before anything else
from mcp.server.fastmcp import FastMCP  # noqa: E402

_SERVER_NAME = os.environ.get("BLUE_TEAM_MCP_SERVER_NAME", "blue_team_mcp").strip().lower()
if os.environ.get("BLUE_TEAM_MCP_SERVER_NAME", "").strip() and os.environ.get("BLUE_TEAM_MCP_SERVER_NAME", "").strip() != _SERVER_NAME:
    logger.warning("BLUE_TEAM_MCP_SERVER_NAME normalized to '%s'.", _SERVER_NAME)

_MCP_HOST = os.environ.get("MCP_HOST", "127.0.0.1")
_MCP_PORT = int(os.environ.get("MCP_PORT", "8000"))
mcp = FastMCP(_SERVER_NAME, host=_MCP_HOST, port=_MCP_PORT)

# Configuration bootstrap - called once at import time.
# Raises ConfigurationError on fatal issues (missing Indexer URL, etc.).
from mcp_server.core.config import init_config  # noqa: E402

_config = init_config()

# Backward-compatible module-level exports - sourced from the Config singleton.
# New code should use ``from mcp_server.core.config import config``.

_c = _config

# Threat Intelligence API keys
ABUSEIPDB_API_KEY   = _c.threat_intel.abuseipdb_api_key
VIRUSTOTAL_API_KEY  = _c.threat_intel.virustotal_api_key
CROWDSEC_API_KEY_ENV = "CROWDSEC_API_KEY"
CROWDSEC_CACHE_TTL   = _c.threat_intel.crowdsec_cache_ttl
GREYNOISE_COMMUNITY_BASE_URL = _c.threat_intel.greynoise_base_url
NETRA_API_KEY_ENV   = "NETRA_API_KEY"
NETRA_VERIFY_SSL    = _c.threat_intel.netra_verify_ssl
ARGUS_API_KEY_ENV   = "ARGUS_API_KEY"
ARGUS_VERIFY_SSL    = _c.threat_intel.argus_verify_ssl
THREATFOX_API_KEY_ENV = "THREATFOX_API_KEY"
THREATFOX_CACHE_TTL   = _c.threat_intel.threatfox_cache_ttl
OTX_API_KEY_ENV = "OTX_API_KEY"
OTX_CACHE_TTL   = _c.threat_intel.otx_cache_ttl
URLHAUS_API_KEY_ENV = "URLHAUS_API_KEY"
URLHAUS_CACHE_TTL   = _c.threat_intel.urlhaus_cache_ttl
HUDSONROCK_API_KEY_ENV = "HUDSONROCK_API_KEY"
RAPIDAPI_KEY_ENV    = "RAPIDAPI_KEY"

# External API Base URLs
CROWDSEC_BASE_URL  = _c.threat_intel.crowdsec_base_url
THREATFOX_BASE_URL = _c.threat_intel.threatfox_base_url
ABUSEIPDB_BASE_URL = _c.threat_intel.abuseipdb_base_url
VIRUSTOTAL_BASE_URL = _c.threat_intel.virustotal_base_url
NETRA_BASE_URL     = _c.threat_intel.netra_base_url
ARGUS_BASE_URL     = _c.threat_intel.argus_base_url
RDAP_BASE_URL      = _c.threat_intel.rdap_base_url
CRTSH_BASE_URL     = _c.threat_intel.crtsh_base_url
OTX_BASE_URL       = _c.threat_intel.otx_base_url
URLHAUS_BASE_URL   = _c.threat_intel.urlhaus_base_url
HUDSONROCK_BASE_URL = _c.threat_intel.hudsonrock_base_url

# Wazuh Manager API
WAZUH_API_URL        = _c.wazuh_manager.url
WAZUH_API_USER       = _c.wazuh_manager.username
WAZUH_API_PASSWORD   = _c.wazuh_manager.password
WAZUH_API_VERIFY_SSL = _c.wazuh_manager.verify_ssl

# Wazuh Indexer / OpenSearch
WAZUH_INDEXER_URL        = _c.wazuh_indexer.url
WAZUH_INDEXER_USER       = _c.wazuh_indexer.username
WAZUH_INDEXER_PASSWORD   = _c.wazuh_indexer.password
WAZUH_INDEXER_VERIFY_SSL = _c.wazuh_indexer.verify_ssl
_WAZUH_INDEXER_MAX_SIZE  = _c.wazuh_indexer.max_size

# Sangfor Blocklist
SANGFOR_BLOCKLIST_URL      = _c.sangfor.url
SANGFOR_BLOCKLIST_TOKEN    = _c.sangfor.token
SANGFOR_BLOCKLIST_TIMEOUT  = _c.sangfor.timeout
SANGFOR_BLOCKLIST_VERIFY_SSL = _c.sangfor.verify_ssl

# Performance & Limits
MAX_LOG_LINES             = _c.limits.max_log_lines
CHARACTER_LIMIT           = _c.limits.character_limit
HTTP_TIMEOUT              = _c.limits.http_timeout
BLUETEAM_ALLOW_UNTRUNCATED = _c.limits.allow_untruncated

# Redaction Layers
BLUETEAM_REDACT_PII       = _c.redaction.redact_pii
BLUETEAM_REDACT_EMAILS    = _c.redaction.redact_emails
BLUETEAM_REDACT_DOMAINS   = _c.redaction.redact_domains
BLUETEAM_REDACT_LOCATIONS = _c.redaction.redact_locations
BLUETEAM_REDACT_UAS       = _c.redaction.redact_uas

# Redaction policy & forensic bypass gate
BLUETEAM_REDACTION_POLICY     = _c.redaction.policy
BLUETEAM_OWNED_DOMAINS        = _c.redaction.owned_domains
BLUETEAM_ALLOW_RUNTIME_DOMAINS = _c.redaction.allow_runtime_domains
BLUETEAM_ALLOW_FORENSIC_BYPASS = _c.redaction.allow_forensic_bypass
BLUETEAM_FORENSIC_TOKEN        = _c.redaction.forensic_token

# Attacker-IOC registry persistence (JSONL)
BLUETEAM_ATTACKER_REGISTRY     = _c.attacker_registry.path
BLUETEAM_ATTACKER_REGISTRY_TTL = _c.attacker_registry.ttl
BLUETEAM_ATTACKER_REGISTRY_MAX = _c.attacker_registry.max_entries

# IOC lifecycle store (JSONL)
BLUETEAM_IOC_STORE     = _c.ioc_store.path
BLUETEAM_IOC_STORE_MAX = _c.ioc_store.max_entries

# Operational hardening
BLUETEAM_EXPORT_RETENTION_DAYS = _c.operational.export_retention_days
BLUETEAM_AUTO_PROMOTE_IPS      = _c.operational.auto_promote_ips
BLUETEAM_EXPORT_DIR            = _c.operational.export_dir

# Audit & Rate Limiting
BLUETEAM_AUDIT_LOG            = _c.audit.audit_log_path
BLUETEAM_RATE_LIMIT            = _c.audit.rate_limit
_INVESTIGATION_HISTORY_FILE    = _c.audit.investigation_history
MITRE_ATTACK_STIX              = _c.audit.mitre_stix_url

# Shared Field Descriptions (string constants - not config values)
_BYPASS_REDACTION_DESC = (
    "When true, skip PII/credential redaction for audit investigations."
)
_REDACTION_POLICY_DESC = (
    "Redaction policy: 'full' (shape-based, default), "
    "'protect_victim' (mask victim-owned indicators only, attacker IOCs intact), "
    "'raw' (Layer 1 credential strip only - requires BLUETEAM_ALLOW_FORENSIC_BYPASS)."
)
_REVEAL_OWNED_DESC = (
    "When true (forensic), expose emails/subdomains at owned domains "
    "(BLUETEAM_OWNED_DOMAINS) unmasked while all other protect_victim masking "
    "stays on. Layer 1 credentials remain masked. Requires BLUETEAM_OWNED_DOMAINS "
    "to be set."
)
_FORENSIC_TOKEN_DESC = (
    "Operator forensic token (matches BLUETEAM_FORENSIC_TOKEN). Required for "
    "redaction_policy='raw' / bypass_redaction when that env is set."
)
_RESPONSE_FORMAT_DESC = "Output format: 'markdown' (default) or 'json'."
_SINCE_DESC  = "ISO 8601 start time in UTC. Defaults to 365 days ago."
_UNTIL_DESC  = "ISO 8601 end time in UTC. Defaults to now."
_AGENT_NAME_DESC = "Optional agent name filter."
