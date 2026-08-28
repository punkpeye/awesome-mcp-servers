#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Typed configuration for Blue Team MCP Server.
Replaces the ~60 import-time os.environ reads in mcp_server/__init__.py
with structured dataclasses that validate at startup and raise
ConfigurationError on invalid values.
All defaults are production-safe: localhost bind, TLS on, redaction on.
"""
from __future__ import annotations
import os
import logging
from dataclasses import dataclass, field
from typing import Optional
from mcp_server.core.exceptions import ConfigurationError

logger = logging.getLogger("blue_team_mcp.config")


# Helper
def _bool(v: str, default: bool = False) -> bool:
    """Parse an env-var string as a boolean."""
    if not v:
        return default
    return v.strip().lower() in ("1", "true", "yes")

# Nested config groups - one dataclass per trust domain
@dataclass
class ServerConfig:
    """MCP transport and binding configuration."""
    host: str = "127.0.0.1"
    port: int = 8000
    server_name: str = "blue_team_mcp"
    log_level: str = "INFO"

    @classmethod
    def from_env(cls) -> "ServerConfig":
        name = os.environ.get("BLUE_TEAM_MCP_SERVER_NAME", "blue_team_mcp").strip().lower()
        return cls(
            host=os.environ.get("MCP_HOST", "127.0.0.1"),
            port=int(os.environ.get("MCP_PORT", "8000")),
            server_name=name,
            log_level=os.environ.get("LOG_LEVEL", "INFO"),
        )

    def validate(self) -> None:
        if not self.server_name:
            raise ConfigurationError("BLUE_TEAM_MCP_SERVER_NAME must not be empty")


@dataclass
class WazuhManagerConfig:
    """Wazuh Manager API connection parameters."""
    url: str = ""
    username: str = "wazuh-wui"
    password: str = ""
    verify_ssl: bool = True

    @classmethod
    def from_env(cls) -> "WazuhManagerConfig":
        return cls(
            url=os.environ.get("WAZUH_API_URL", "").rstrip("/"),
            username=os.environ.get("WAZUH_API_USER", "wazuh-wui"),
            password=os.environ.get("WAZUH_API_PASSWORD", ""),
            verify_ssl=_bool(os.environ.get("WAZUH_API_VERIFY_SSL", "true"), True),
        )

    def validate(self) -> None:
        """Manager API is optional - tools degrade gracefully when unset."""
        if self.url and not self.password:
            raise ConfigurationError(
                "WAZUH_API_URL is set but WAZUH_API_PASSWORD is empty -"
                "Manager API tools will fail."
            )


@dataclass
class WazuhIndexerConfig:
    """Wazuh Indexer / OpenSearch connection parameters."""
    url: str = ""
    username: str = "admin"
    password: str = ""
    verify_ssl: bool = True
    max_size: int = 10000

    @classmethod
    def from_env(cls) -> "WazuhIndexerConfig":
        return cls(
            url=os.environ.get("WAZUH_INDEXER_URL", "").rstrip("/"),
            username=os.environ.get("WAZUH_INDEXER_USER", "admin"),
            password=os.environ.get("WAZUH_INDEXER_PASSWORD", ""),
            verify_ssl=_bool(os.environ.get("WAZUH_INDEXER_VERIFY_SSL", "true"), True),
            max_size=int(os.environ.get("WAZUH_INDEXER_MAX_SIZE", "10000")),
        )

    def validate(self) -> None:
        if not self.url:
            raise ConfigurationError(
                "WAZUH_INDEXER_URL is required - Indexer tools cannot function without it."
            )
        if not self.password:
            raise ConfigurationError(
                "WAZUH_INDEXER_PASSWORD is required - Indexer tools cannot authenticate."
            )


@dataclass
class ThreatIntelConfig:
    """External threat-intelligence API keys and endpoints."""
    # CrowdSec
    crowdsec_api_key: str = ""
    crowdsec_cache_ttl: int = 900
    crowdsec_base_url: str = "https://cti.api.crowdsec.net"
    # GreyNoise
    greynoise_base_url: str = "https://api.greynoise.io/v3/community"
    # ThreatFox
    threatfox_api_key: str = ""
    threatfox_cache_ttl: int = 900
    threatfox_base_url: str = "https://threatfox-api.abuse.ch/api/v1/"
    # AbuseIPDB
    abuseipdb_api_key: str = ""
    abuseipdb_base_url: str = "https://api.abuseipdb.com/api/v2"
    # VirusTotal
    virustotal_api_key: str = ""
    virustotal_base_url: str = "https://www.virustotal.com/api/v3"
    # Netra
    netra_api_key: str = ""
    netra_verify_ssl: bool = False
    netra_base_url: str = "https://netra.fbi.gov:8013/api/v1"
    # Argus
    argus_api_key: str = ""
    argus_verify_ssl: bool = False
    argus_base_url: str = "http://localhost:8088/lookup-jobs"
    # RDAP / crt.sh
    rdap_base_url: str = "https://rdap.org"
    crtsh_base_url: str = "https://crt.sh"
    # AlienVault OTX
    otx_api_key: str = ""
    otx_cache_ttl: int = 1800
    otx_base_url: str = "https://otx.alienvault.com"
    # URLhaus
    urlhaus_api_key: str = ""
    urlhaus_cache_ttl: int = 1800
    urlhaus_base_url: str = "https://urlhaus-api.abuse.ch/v1/"
    # HudsonRock (stealer logs)
    hudsonrock_api_key: str = ""
    hudsonrock_base_url: str = "https://cavalier.hudsonrock.com/api/json/v2"
    # RapidAPI capability lookups (IP blacklist, IOC search, breach check)
    rapidapi_key: str = ""
    rapidapi_cache_ttl: int = 1800

    @classmethod
    def from_env(cls) -> "ThreatIntelConfig":
        return cls(
            crowdsec_api_key=os.environ.get("CROWDSEC_API_KEY", ""),
            crowdsec_cache_ttl=int(os.environ.get("CROWDSEC_CACHE_TTL", "900")),
            crowdsec_base_url=os.environ.get("CROWDSEC_BASE_URL", "https://cti.api.crowdsec.net"),
            greynoise_base_url=os.environ.get("GREYNOISE_BASE_URL", "https://api.greynoise.io/v3/community"),
            threatfox_api_key=os.environ.get("THREATFOX_API_KEY", ""),
            threatfox_cache_ttl=int(os.environ.get("THREATFOX_CACHE_TTL", "900")),
            threatfox_base_url=os.environ.get("THREATFOX_BASE_URL", "https://threatfox-api.abuse.ch/api/v1/"),
            abuseipdb_api_key=os.environ.get("ABUSEIPDB_API_KEY", ""),
            abuseipdb_base_url=os.environ.get("ABUSEIPDB_BASE_URL", "https://api.abuseipdb.com/api/v2"),
            virustotal_api_key=os.environ.get("VIRUSTOTAL_API_KEY", ""),
            virustotal_base_url=os.environ.get("VIRUSTOTAL_BASE_URL", "https://www.virustotal.com/api/v3"),
            netra_api_key=os.environ.get("NETRA_API_KEY", ""),
            netra_verify_ssl=_bool(os.environ.get("NETRA_VERIFY_SSL", "false")),
            netra_base_url=os.environ.get("NETRA_BASE_URL", "https://netra.fbi.gov:8013/api/v1"),
            argus_api_key=os.environ.get("ARGUS_API_KEY", ""),
            argus_verify_ssl=_bool(os.environ.get("ARGUS_VERIFY_SSL", "false")),
            argus_base_url=os.environ.get("ARGUS_BASE_URL", "http://localhost:8088/lookup-jobs"),
            rdap_base_url=os.environ.get("RDAP_BASE_URL", "https://rdap.org"),
            crtsh_base_url=os.environ.get("CRTSH_BASE_URL", "https://crt.sh"),
            otx_api_key=os.environ.get("OTX_API_KEY", ""),
            otx_cache_ttl=int(os.environ.get("OTX_CACHE_TTL", "1800")),
            otx_base_url=os.environ.get("OTX_BASE_URL", "https://otx.alienvault.com"),
            urlhaus_api_key=os.environ.get("URLHAUS_API_KEY", ""),
            urlhaus_cache_ttl=int(os.environ.get("URLHAUS_CACHE_TTL", "1800")),
            urlhaus_base_url=os.environ.get("URLHAUS_BASE_URL", "https://urlhaus-api.abuse.ch/v1/"),
            hudsonrock_api_key=os.environ.get("HUDSONROCK_API_KEY", ""),
            hudsonrock_base_url=os.environ.get("HUDSONROCK_BASE_URL", "https://cavalier.hudsonrock.com/api/json/v2"),
            rapidapi_key=os.environ.get("RAPIDAPI_KEY", ""),
            rapidapi_cache_ttl=int(os.environ.get("RAPIDAPI_CACHE_TTL", "1800")),
        )

    def validate(self) -> None:
        """Threat-intel keys are all optional - tools degrade gracefully."""
        pass


@dataclass
class SangforConfig:
    """Sangfor blocklist integration parameters."""
    url: str = ""
    token: str = ""
    timeout: float = 15.0
    verify_ssl: bool = False

    @classmethod
    def from_env(cls) -> "SangforConfig":
        return cls(
            url=os.environ.get("SANGFOR_BLOCKLIST_URL", "").rstrip("/"),
            token=os.environ.get("SANGFOR_BLOCKLIST_TOKEN", ""),
            timeout=float(os.environ.get("SANGFOR_BLOCKLIST_TIMEOUT", "15")),
            verify_ssl=_bool(os.environ.get("SANGFOR_BLOCKLIST_VERIFY_SSL", "false")),
        )

    def validate(self) -> None:
        pass


@dataclass
class RedactionConfig:
    """PII redaction policy and layer toggles."""
    policy: str = "full"     # full | protect_victim | raw
    redact_pii: bool = True
    redact_emails: bool = True
    redact_domains: bool = True
    redact_locations: bool = True
    redact_uas: bool = True
    owned_domains: str = ""
    allow_runtime_domains: bool = False   # gate for blueteam_set_owned_domains
    allow_forensic_bypass: bool = False
    forensic_token: str = ""

    _VALID_POLICIES = frozenset({"full", "protect_victim", "raw"})

    @classmethod
    def from_env(cls) -> "RedactionConfig":
        return cls(
            policy=os.environ.get("BLUETEAM_REDACTION_POLICY", "full").strip().lower(),
            redact_pii=_bool(os.environ.get("BLUETEAM_REDACT_PII", "true"), True),
            redact_emails=_bool(os.environ.get("BLUETEAM_REDACT_EMAILS", "true"), True),
            redact_domains=_bool(os.environ.get("BLUETEAM_REDACT_DOMAINS", "true"), True),
            redact_locations=_bool(os.environ.get("BLUETEAM_REDACT_LOCATIONS", "true"), True),
            redact_uas=_bool(os.environ.get("BLUETEAM_REDACT_UAS", "true"), True),
            owned_domains=os.environ.get("BLUETEAM_OWNED_DOMAINS", ""),
            allow_runtime_domains=_bool(os.environ.get("BLUETEAM_ALLOW_RUNTIME_DOMAINS", "false")),
            allow_forensic_bypass=_bool(os.environ.get("BLUETEAM_ALLOW_FORENSIC_BYPASS", "false")),
            forensic_token=os.environ.get("BLUETEAM_FORENSIC_TOKEN", ""),
        )

    def validate(self) -> None:
        if self.policy not in self._VALID_POLICIES:
            raise ConfigurationError(
                f"BLUETEAM_REDACTION_POLICY={self.policy!r} is invalid. "
                f"Must be one of: {', '.join(sorted(self._VALID_POLICIES))}."
            )
        if self.policy == "raw" and not self.allow_forensic_bypass:
            raise ConfigurationError(
                "BLUETEAM_REDACTION_POLICY='raw' requires "
                "BLUETEAM_ALLOW_FORENSIC_BYPASS=true."
            )
        # Fail-safe: 'protect_victim' with no owned domains masks NOTHING (every
        # email/domain is treated as attacker). Fall back to 'full' to prevent
        # accidental PII leaks, so operators know to set owned domains.
        if self.policy == "protect_victim" and not self.owned_domains.strip():
            logger.warning(
                "BLUETEAM_REDACTION_POLICY='protect_victim' requires BLUETEAM_OWNED_DOMAINS, "
                "but it is empty - falling back to 'full' to prevent accidental PII leaks. "
                "Set BLUETEAM_OWNED_DOMAINS to a comma-separated list of your owned domains "
                "(e.g. tangerangkota.go.id)."
            )
            self.policy = "full"
        if self.allow_forensic_bypass and self.forensic_token:
            # Token is set - validate it's non-empty and reasonable length
            if len(self.forensic_token) < 8:
                raise ConfigurationError(
                    "BLUETEAM_FORENSIC_TOKEN must be at least 8 characters." # use openssl rand fot generate it.
                )


@dataclass
class AttackerRegistryConfig:
    """Attacker-IOC registry persistence (JSONL)."""
    path: str = ""
    ttl: int = 604800     # 7 days; 0 = never expire
    max_entries: int = 10000

    @classmethod
    def from_env(cls) -> "AttackerRegistryConfig":
        return cls(
            path=os.environ.get("BLUETEAM_ATTACKER_REGISTRY", ""),
            ttl=int(os.environ.get("BLUETEAM_ATTACKER_REGISTRY_TTL", "604800")),
            max_entries=int(os.environ.get("BLUETEAM_ATTACKER_REGISTRY_MAX", "10000")),
        )

    def validate(self) -> None:
        pass


@dataclass
class IOCStoreConfig:
    """IOC lifecycle store persistence (JSONL)."""
    path: str = ""
    max_entries: int = 50000

    @classmethod
    def from_env(cls) -> "IOCStoreConfig":
        return cls(
            path=os.environ.get("BLUETEAM_IOC_STORE", ""),
            max_entries=int(os.environ.get("BLUETEAM_IOC_STORE_MAX", "50000")),
        )

    def validate(self) -> None:
        pass


@dataclass
class OperationalConfig:
    """Operational hardening and lifecycle parameters."""
    export_retention_days: int = 0       # 0 = keep forever
    auto_promote_ips: bool = False
    export_dir: str = "/var/log/blue-team-mcp/exports"

    @classmethod
    def from_env(cls) -> "OperationalConfig":
        return cls(
            export_retention_days=int(os.environ.get("BLUETEAM_EXPORT_RETENTION_DAYS", "0")),
            auto_promote_ips=_bool(os.environ.get("BLUETEAM_AUTO_PROMOTE_IPS", "false")),
            export_dir=os.environ.get("BLUETEAM_EXPORT_DIR", "/var/log/blue-team-mcp/exports"),
        )

    def validate(self) -> None:
        if self.export_retention_days < 0:
            raise ConfigurationError("BLUETEAM_EXPORT_RETENTION_DAYS must be >= 0")


@dataclass
class AuditConfig:
    """Audit logging and rate-limiting parameters."""
    audit_log_path: str = ""
    rate_limit: int = 0                  # 0 = no rate limiting
    investigation_history: str = ""
    mitre_stix_url: str = (
        "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/"
        "refs/heads/master/enterprise-attack/enterprise-attack.json"
    )

    @classmethod
    def from_env(cls) -> "AuditConfig":
        return cls(
            audit_log_path=os.environ.get("BLUETEAM_AUDIT_LOG", ""),
            rate_limit=int(os.environ.get("BLUETEAM_RATE_LIMIT", "0")),
            investigation_history=os.environ.get("BLUETEAM_INVESTIGATION_HISTORY", ""),
            mitre_stix_url=os.environ.get(
                "MITRE_ATTACK_STIX",
                "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/"
                "refs/heads/master/enterprise-attack/enterprise-attack.json",
            ),
        )

    def validate(self) -> None:
        if self.rate_limit < 0:
            raise ConfigurationError("BLUETEAM_RATE_LIMIT must be >= 0")


@dataclass
class LimitsConfig:
    """Performance and safety limits."""
    character_limit: int = 100000
    http_timeout: float = 30.0
    allow_untruncated: bool = False
    max_log_lines: int = 2000

    @classmethod
    def from_env(cls) -> "LimitsConfig":
        return cls(
            character_limit=int(os.environ.get("BLUETEAM_CHARACTER_LIMIT", "100000")),
            http_timeout=30.0,
            allow_untruncated=_bool(os.environ.get("BLUETEAM_ALLOW_UNTRUNCATED", "false")),
            max_log_lines=2000,
        )

    def validate(self) -> None:
        if self.character_limit < 1000:
            raise ConfigurationError("BLUETEAM_CHARACTER_LIMIT must be at least 1000")
        if self.http_timeout <= 0:
            raise ConfigurationError("HTTP_TIMEOUT must be > 0")


@dataclass
class ToolGatingConfig:
    """Tool enable/disable and read-only enforcement."""
    disabled_tools: list[str] = field(default_factory=list)
    disabled_categories: list[str] = field(default_factory=list)
    read_only: bool = False

    @classmethod
    def from_env(cls) -> "ToolGatingConfig":
        tools_str = os.environ.get("WAZUH_DISABLED_TOOLS", "")
        categories_str = os.environ.get("WAZUH_DISABLED_CATEGORIES", "")
        return cls(
            disabled_tools=[t.strip() for t in tools_str.split(",") if t.strip()],
            disabled_categories=[c.strip() for c in categories_str.split(",") if c.strip()],
            read_only=_bool(os.environ.get("WAZUH_READ_ONLY", "false")),
        )

    def validate(self) -> None:
        pass


# Top level Config aggregating all groups
@dataclass
class Config:
    """Master configuration aggregating all sub-config groups.

    Usage:
        config = Config.from_env()
        config.validate()          # raises ConfigurationError on invalid values
        config.emit_warnings()     # logs warnings for non-fatal issues
    """

    server: ServerConfig = field(default_factory=ServerConfig)
    wazuh_manager: WazuhManagerConfig = field(default_factory=WazuhManagerConfig)
    wazuh_indexer: WazuhIndexerConfig = field(default_factory=WazuhIndexerConfig)
    threat_intel: ThreatIntelConfig = field(default_factory=ThreatIntelConfig)
    sangfor: SangforConfig = field(default_factory=SangforConfig)
    redaction: RedactionConfig = field(default_factory=RedactionConfig)
    attacker_registry: AttackerRegistryConfig = field(default_factory=AttackerRegistryConfig)
    ioc_store: IOCStoreConfig = field(default_factory=IOCStoreConfig)
    operational: OperationalConfig = field(default_factory=OperationalConfig)
    audit: AuditConfig = field(default_factory=AuditConfig)
    limits: LimitsConfig = field(default_factory=LimitsConfig)
    tool_gating: ToolGatingConfig = field(default_factory=ToolGatingConfig)

    @classmethod
    def from_env(cls) -> "Config":
        """Build a fully-populated Config from environment variables."""
        return cls(
            server=ServerConfig.from_env(),
            wazuh_manager=WazuhManagerConfig.from_env(),
            wazuh_indexer=WazuhIndexerConfig.from_env(),
            threat_intel=ThreatIntelConfig.from_env(),
            sangfor=SangforConfig.from_env(),
            redaction=RedactionConfig.from_env(),
            attacker_registry=AttackerRegistryConfig.from_env(),
            ioc_store=IOCStoreConfig.from_env(),
            operational=OperationalConfig.from_env(),
            audit=AuditConfig.from_env(),
            limits=LimitsConfig.from_env(),
            tool_gating=ToolGatingConfig.from_env(),
        )

    def validate(self) -> None:
        """Validate all config groups. Raises ConfigurationError on the first fatal issue."""
        self.server.validate()
        self.wazuh_manager.validate()
        self.wazuh_indexer.validate()
        self.threat_intel.validate()
        self.sangfor.validate()
        self.redaction.validate()
        self.attacker_registry.validate()
        self.ioc_store.validate()
        self.operational.validate()
        self.audit.validate()
        self.limits.validate()
        self.tool_gating.validate()

    def emit_warnings(self) -> None:
        """Log warnings for non-fatal configuration issues.

        Call AFTER validate() succeeds - these are advisory, not blocking.
        """
        if not self.wazuh_manager.url:
            logger.warning("WAZUH_API_URL not set - Manager API tools disabled.")
        if not self.wazuh_manager.verify_ssl:
            logger.warning("WAZUH_API_VERIFY_SSL disabled - TLS OFF for Wazuh Manager API.")
        if not self.wazuh_indexer.verify_ssl:
            logger.warning("WAZUH_INDEXER_VERIFY_SSL disabled - TLS OFF for Wazuh Indexer.")
        if not self.threat_intel.crowdsec_api_key:
            logger.warning("CROWDSEC_API_KEY not set - CrowdSec tools disabled.")
        if not self.threat_intel.abuseipdb_api_key:
            logger.warning("ABUSEIPDB_API_KEY not set - AbuseIPDB lookup disabled.")
        if not self.threat_intel.virustotal_api_key:
            logger.warning("VIRUSTOTAL_API_KEY not set - VirusTotal lookups disabled.")
        if not self.threat_intel.rapidapi_key:
            logger.warning("RAPIDAPI_KEY not set - RapidAPI lookups (IP blacklist / IOC search / breach check) disabled.")
        if self.limits.allow_untruncated:
            logger.warning("BLUETEAM_ALLOW_UNTRUNCATED=true - character-limit bypass ENABLED.")
        if self.redaction.allow_forensic_bypass:
            logger.warning(
                "BLUETEAM_ALLOW_FORENSIC_BYPASS=true - forensic raw output enabled "
                "(bypass_redaction/redaction_policy='raw' will be honored)."
            )


# Module-level singleton - initialized by mcp_server/__init__.py at startup
config: Optional[Config] = None
def init_config() -> Config:
    """Build, validate, and store the global Config singleton.
    Called once at server startup, before any tools are registered.
    Returns the config instance (also available as module-level ``config``).
    """
    global config
    config = Config.from_env()
    config.validate()
    config.emit_warnings()
    logger.info(
        "Configuration validated - Manager=%s, Indexer=%s, %d threat-intel providers.",
        "enabled" if config.wazuh_manager.url else "disabled",
        "enabled" if config.wazuh_indexer.url else "disabled",
        sum(1 for k in [
            config.threat_intel.crowdsec_api_key,
            config.threat_intel.threatfox_api_key,
            config.threat_intel.abuseipdb_api_key,
            config.threat_intel.virustotal_api_key,
            config.threat_intel.netra_api_key,
            config.threat_intel.argus_api_key,
            config.threat_intel.rapidapi_key,
        ] if k),
    )
    return config
