# Blue Team MCP Server (Wazuh SIEM)

A defensive MCP server for Claude Desktop / any MCP client — the blue-team counterpart to
offensive tooling. **123 tools + 4 resources** across Wazuh SIEM, multi-provider threat
intelligence, MITRE-driven 3-Sum APT correlation, attack graphing, LangGraph investigation
workflows, and host forensics. Read-only by default.

**Programmer**: `NAuliajati` (`csirt[at]tangerangkota[.]go[.]id`)

---

## Architecture

```
main.py -> mcp_server/  (package)
                 ├─ core/          HTTP client, redaction, audit, config, attack graph, IOC store
                 ├─ wazuh/         Indexer (OpenSearch) + Manager API (JWT auth)
                 ├─ correlation/   3-Sum engine (pure computation, MITRE-driven)
                 ├─ threat_intel/  CrowdSec, ThreatFox, OTX, URLhaus, GreyNoise + shared cache
                 ├─ agents/        LangGraph investigation + playbook workflows
                 └─ tools/         49 tool modules
```

Every tool call flows through a single pipeline in the `@blueteam_tool` decorator — the three
most-connected nodes in the code graph:

```
audit (_audit_log) -> call -> redact (_redact_alert_data) -> truncate (_truncate_if_needed)
```

All outbound HTTP flows through a per-pool circuit breaker (`http_client.CircuitBreaker`:
5 consecutive failures -> open, 60s cooldown, single half-open trial). 429 and 4xx never count
as failures, so an outage on one upstream fails fast instead of stacking retries across tools.

| Transport | Use case |
|-----------|----------|
| `stdio` | Local subprocess / SSH pipe (default) |
| `streamable_http` | Remote HTTP service (`http://<host>:<port>/mcp`) — requires `MCP_API_KEY` beyond `127.0.0.1` (bind guard enforced) |

---

## Quick Start

```bash
git clone <repo> && cd Wazuh-MCP-Server
sudo bash setup.sh                    # deps, venv, wrapper at /opt/blue-team-mcp

# configure (edit /opt/blue-team-mcp/config.env)
export WAZUH_INDEXER_URL="https://<host>:9200"
export WAZUH_INDEXER_USER="admin"
export WAZUH_INDEXER_PASSWORD="<indexer-password>"
export WAZUH_API_URL="https://<host>:55000"      # optional — Manager API tools
export WAZUH_API_USER="wazuh-wui"
export WAZUH_API_PASSWORD="<api-password>"
export CROWDSEC_API_KEY="<key>"                  # optional — threat intel (free)
# inbound auth for the HTTP transport (REQUIRED when binding beyond 127.0.0.1)
export MCP_API_KEY="btm_<43-char-base64>"        # generate: python3 -c "import secrets; print('btm_' + secrets.token_urlsafe(32))"
export MCP_API_KEY_SCOPES="wazuh:read wazuh:write"   # optional — default wazuh:read (read-only)

# run (stdio)
mcp-server-blueteam

# or remote HTTP (MCP_API_KEY is mandatory here — the server refuses to bind otherwise)
MCP_TRANSPORT=streamable_http MCP_HOST=0.0.0.0 MCP_PORT=8001 \
  MCP_API_KEY="btm_<43-char-base64>" mcp-server-blueteam
```

Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "blue-team-mcp": {
      "command": "ssh",
      "args": ["-i", "~/.ssh/id_ed25519", "user@DEFENDER_HOST", "mcp-server-blueteam"],
      "transport": "stdio"
    }
  }
}
```

---

## Configuration

Credentials come from environment variables, validated at startup. Every threat-intel key is
optional — tools degrade gracefully without them.

| Area | Variables | Notes |
|------|-----------|-------|
| Wazuh Indexer | `WAZUH_INDEXER_URL` / `_USER` / `_PASSWORD` | OpenSearch (9200) — alert/event data |
| Wazuh Manager | `WAZUH_API_URL` / `_USER` / `_PASSWORD` | Manager API (55000) — rules/agents/config |
| TLS | `WAZUH_INDEXER_VERIFY_SSL`, `WAZUH_API_VERIFY_SSL` | default `true` |
| Threat intel | `CROWDSEC_API_KEY`, `THREATFOX_API_KEY`, `OTX_API_KEY`, `URLHAUS_API_KEY`, `ABUSEIPDB_API_KEY`, `VIRUSTOTAL_API_KEY`, `NETRA_API_KEY`, `ARGUS_API_KEY`, `RAPIDAPI_KEY`, `HUDSONROCK_API_KEY` | 9 providers + RapidAPI + HudsonRock; all optional |
| Redaction | `BLUETEAM_REDACTION_POLICY`, `BLUETEAM_OWNED_DOMAINS`, `BLUETEAM_REDACT_*` | see Security & Privacy |
| Forensic gate | `BLUETEAM_ALLOW_FORENSIC_BYPASS`, `BLUETEAM_FORENSIC_TOKEN` | default `false` / empty |
| Inbound auth | `MCP_API_KEY`, `MCP_API_KEY_SCOPES` | pre-shared API key + scopes for `streamable_http` |
| Inbound hardening | `BLUETEAM_HTTP_RATE_LIMIT`, `BLUETEAM_ALLOWED_ORIGINS` | per-IP sliding-window rate limit (req/min, `0`=off) + Origin allowlist (loopback always allowed) |
| Audit & persistence | `BLUETEAM_AUDIT_LOG`, `BLUETEAM_IOC_STORE`, `BLUETEAM_ATTACKER_REGISTRY`, `BLUETEAM_FALSE_POSITIVE_KB`, `BLUETEAM_CASE_STORE`, `BLUETEAM_CMDB_FILE` | JSONL audit trail + stores (optional) |
| Gating | `WAZUH_READ_ONLY`, `WAZUH_DISABLED_CATEGORIES`, `WAZUH_DISABLED_TOOLS` | skip destructive tools / tool categories |

---

## Capabilities

### Wazuh SIEM
Alert search (`blueteam_wazuh_indexer_search`, `wazuh_alert_dsl_query`), zero-doc statistical
aggregations, schema discovery (`blueteam_index_schema`), domain/email/geo/syscheck/compliance
lookups, and Manager API tools (rules, decoders, groups, agents, security events).

### 3-Sum APT Correlation
`three_sum_correlation` runs two engines plus unified scoring:
- **Engine A** — MITRE-driven multi-IoC risk thresholding. Alerts classify by `rule.mitre.tactic`
  (via `MITRE_TACTIC_TO_CATEGORY`) and `rule.mitre.id` (resolved through the ATT&CK STIX bundle),
  scored as `rule.level × tactic weight`, and gated by a **≥2-category chained-attack rule**
  (`threshold_score` default 35).
- **Engine B** — 3-source volumetric Z-score (MAD + shoulder-check) flagging simultaneous spikes.
- Plus multi-resolution (1h/24h/7d), unified severity scoring, and Indexer degradation detection.

### Threat Intelligence
9 providers — CrowdSec, ThreatFox, OTX, URLhaus, GreyNoise, AbuseIPDB, VirusTotal, Netra, Argus —
with a unified `blueteam_threat_intel_aggregate` (concurrent fan-out) and a weighted
`blueteam_unified_threat_score`. Plus `stealer_log_check` (HudsonRock) and `jarm_fingerprint`
(TLS fingerprint for C2/malware attribution, no API key), and 3 RapidAPI lookups
(`blueteam_ip_blacklist`, `blueteam_ioc_search`, `blueteam_breach_check`).

### Alert Enrichment
`blueteam_wazuh_alert_summarize`, `blueteam_beacon_detect`, `blueteam_attack_chain`,
`blueteam_threat_card`, `blueteam_wazuh_alert_compare`, `blueteam_curated_threat_report`.

### Investigation, Graphs & Workflows
`blueteam_investigate_ip`, `blueteam_attack_graph` (networkx clusters + PageRank),
`blueteam_pivot_suggest`, `blueteam_campaign_watch`, `blueteam_stix_killchain`,
`blueteam_investigation_workflow` and `blueteam_playbook_run` (LangGraph), plus a
false-positive knowledge base (`blueteam_false_positive_kb`) that auto-suppresses known-noisy
IOCs in 3-Sum.

### Host & Domain Forensics
WHOIS / CRT.sh, IOC extraction, JARM fingerprinting, typosquatting detection
(`blueteam_domain_permute`), webshell scanning, server-side JSONL export, DOCX/XLSX/PPTX report
export, and 23 host-forensics tools (log readers, fail2ban, rootkit scan, lynis, process/cron/users).

---

## Security & Privacy

### Inbound authentication (streamable_http)

`streamable_http` is protected by a pre-shared API key in `mcp_server/core/server_auth.py`:

- `MCP_API_KEY` — format `btm_<43-char-urlsafe-base64>` (47 chars). Stored only as a SHA-256
  digest, compared with `hmac.compare_digest` (constant-time).
- `MCP_API_KEY_SCOPES` — default `wazuh:read` (read-only). Add `wazuh:write` to unlock the 9
  write tools (`blueteam_fail2ban_unban`, `blueteam_case_*`, `blueteam_set_owned_domains`,
  `blueteam_mark_investigated`, `blueteam_wazuh_export`, `blueteam_export_report`,
  `blueteam_capture_traffic`). Fail-closed: no scope ⇒ read-only.
- **Bind guard** (`main.py::_start_http_transport`): a non-loopback bind without `MCP_API_KEY`
  raises `ConfigurationError` and refuses to start. Loopback stays auth-less only when no key is
  configured; when a key is set it is enforced on every request.
- **JSON depth guard** (`parse_json_body_safe`): every POST body is capped at 1 MB
  (`MAX_BODY_BYTES`) and rejected if nesting exceeds 100 levels (`MAX_JSON_DEPTH`) *before*
  `json.loads` runs — blocks the stack-exhaustion DoS from deeply nested JSON-RPC payloads.
- **Inbound rate limiter** (`SlidingWindowRateLimiter`): per-client-IP sliding-window cap
  (`BLUETEAM_HTTP_RATE_LIMIT`, requests/min, default `0` = disabled) → `429` on excess. Distinct
  from `BLUETEAM_RATE_LIMIT`, which gates destructive tools (fail2ban unban, tcpdump capture)
  with a per-minute global cap.
- **Origin validation** (`_origin_allowed`): an `Origin` header must be a loopback origin or in
  `BLUETEAM_ALLOWED_ORIGINS` (comma-separated exact origins), else `403`. Blocks browser-based
  DNS-rebinding / localhost-exfiltration. Requests without an `Origin` header (non-browser
  clients) are unaffected. The middleware is always installed — rate limiting + origin validation
  apply even on an auth-less loopback bind.

### Redaction policy

Three-state policy (`BLUETEAM_REDACTION_POLICY`, default **`protect_victim`**):

| Policy | Behavior |
|--------|----------|
| `full` | Shape-based masking of emails, private IPs, all domains, paths, user-agents — conservative fallback when `protect_victim` has no owned domains |
| `protect_victim` | Mask only victim-owned indicators (owned domains, private IPs, identities); attacker IOCs stay visible. Recommended for SOC triage. |
| `raw` | Layer-1 credential strip only — hard-gated behind `BLUETEAM_ALLOW_FORENSIC_BYPASS=true` + `BLUETEAM_FORENSIC_TOKEN` |

Layer 1 (credential stripping) applies in **all** states and is never bypassable. The
attacker-IOC registry (`core/attacker_registry.py`) exempts confirmed attacker indicators from
shape-based masking — never from Layer 1.

Two-tier unmasking on top of the policy:
- **Tier 1 — `reveal_owned=true`** — reveals only owned `*.tangerangkota.go.id` assets to the LLM,
  and unmask owned-domain bucket keys in the aggregation tools (including
  `wazuh_alert_dsl_query`). Never expands beyond `BLUETEAM_OWNED_DOMAINS`.
- **Tier 2 — `bypass_redaction=true` + `forensic_token`** — writes raw data **to disk**; the LLM
  receives only the file path, never the raw content.

Set `BLUETEAM_OWNED_DOMAINS` to your org's domains (comma-separated, e.g. `tangerangkota.go.id`).
Inspect with `blueteam_owned_domains`; update at runtime with `blueteam_set_owned_domains`
(gated by `BLUETEAM_ALLOW_RUNTIME_DOMAINS=true`, default off).

---

## SOC Analysis Prompt (copy-paste for your LLM)

A ready-to-paste prompt for a **local** LLM connected to this MCP server. Two output formats —
**Markdown** (inline) and **DOCX** (requires `officecli`, `blueteam_export_report`).

```
⚠️ Calling convention & guardrails (read once — prevents "Field required" errors and false positives):
- Every tool takes a SINGLE ``params`` object. FastMCP double-nests it:
    tool_invoke(name="<tool>", params={"params": {"field": value, ...}})
  Call tool_inspect FIRST to read a tool's exact signature; never skip inspect on an unused tool.
- Default model = protect_victim: the LLM sees attacker public IPs/payloads/rule/severity/MITRE,
  never internal emails, subdomains, private IPs (RFC1918), or internal paths.
- A private/RFC1918 srcip (10.x, 172.16-31.x, 192.168.x) is INTERNAL, never an attacker — do not
  run threat-intel on it (those tools reject private IPs by design — SSRF guard).
- reveal_owned=true (Tier 1, LLM-safe): reveals only *.tangerangkota.go.id + @tangerangkota.go.id.
  Accepted by the alert/aggregation tools — wazuh_domain_lookup, wazuh_alert_focused_crawl,
  wazuh_email_lookup, wazuh_alert_dsl_query (unmasks owned-domain bucket keys), and others —
  never expands beyond BLUETEAM_OWNED_DOMAINS.
- bypass_redaction=true + forensic_token (Tier 2, HUMAN ONLY): writes raw data to disk via
  blueteam_wazuh_export; the LLM sees only the file path.
- ⚠️ NEVER pass redaction_policy="raw" OR bypass_redaction=true in a tool call — both are
  HUMAN-ONLY and gated behind the operator forensic token, which the LLM does NOT hold. The
  call fails with "requires the operator forensic token". For owned-domain visibility use
  reveal_owned=true (above, no token); full raw forensics is blueteam_wazuh_export run by the
  analyst on the server.
- redaction_policy="protect_victim" is accepted by 13 tools (blueteam_curated_threat_report,
  blueteam_threat_card, blueteam_wazuh_alert_summarize, blueteam_wazuh_alerts,
  blueteam_wazuh_geo_heatmap, blueteam_wazuh_indexer_search, three_sum_correlation,
  wazuh_alert_aggregate_analysis, wazuh_alert_focused_crawl, wazuh_alert_timeline,
  wazuh_attack_velocity, wazuh_domain_lookup, wazuh_email_lookup). blueteam_wazuh_export uses
  bypass_redaction (NOT redaction_policy). Other tools reject redaction_policy — drop it and retry.
  (Separately, wazuh_alert_dsl_query accepts reveal_owned=true but NOT redaction_policy.)
- blueteam_wazuh_export writes to BLUETEAM_EXPORT_DIR (default /var/log/blue-team-mcp/exports/)
  with an AUTO-GENERATED filename (export_<timestamp>.jsonl). It has NO ``path`` parameter —
  do not pass one (it will be rejected). Only blueteam_export_report accepts a ``path``.

LANGKAH 0  — Index schema (before any aggregation):
blueteam_index_schema(fields=["data.srcip","rule.id","rule.groups","agent.name",
  "data.domain","data.url","GeoLocation.city_name"], response_format="json")

LANGKAH 1  — Full overview + own-asset forensics:
blueteam_curated_threat_report(since="24h", investigation_depth="deep",
  response_format="json", redaction_policy="protect_victim")
wazuh_domain_lookup(domain="tangerangkota.go.id", since="24h", reveal_owned=true,
  response_format="json", max_scanned=10000)

LANGKAH 2  — Per attacker (top 10): threat card + attack chain
blueteam_threat_card(srcip=<ip>, since="24h")
blueteam_attack_chain(srcip=<ip>, since="24h")

LANGKAH 3  — Unified threat intel:
blueteam_threat_intel_aggregate(indicator=<ip>, response_format="json")
argus_ip_lookup(ip=<ip>); otx_lookup(indicator=<ip>, section="general")
blueteam_ip_blacklist(ip=<ip>); blueteam_ioc_search(ip=<ip>)   # RapidAPI

LANGKAH 4  — 3-Sum APT + auto-enrich + case:
three_sum_correlation(time_window_minutes=1440, follow_up="threat_intel",
  multi_resolution=true, create_case=true, response_format="json",
  redaction_policy="protect_victim")

LANGKAH 5  — Attack graph + pivot + campaign:
blueteam_attack_graph(window_days=30, top_n=20, response_format="json")
blueteam_pivot_suggest(ioc=<top_attacker_ip>)
blueteam_campaign_watch(response_format="json")

LANGKAH 6  — LangGraph investigation + verdict:
blueteam_investigation_workflow(alert_text="<...>", srcip=<ip>, window="24h",
  use_attack_graph=true, generate_report=false, record_verdict=true, verdict_label="suspicious")
blueteam_mark_investigated(srcip=<ip>, verdict="<verdict>", case_id=<case_id>)

LANGKAH 7  — Compromised emails + breach/stealer check:
wazuh_compromised_emails_analysis(since="24h", response_format="json")
blueteam_breach_check(email=<email_dinas>); stealer_log_check(email=<email_dinas>)

LANGKAH 8  — MITRE kill-chain + C2 fingerprinting:
blueteam_stix_killchain(srcip=<ip>, since="24h")
jarm_fingerprint(host=<c2_domain_or_ip>, response_format="json")
blueteam_domain_permute(domain="tangerangkota.go.id")   # typosquatting lookalikes

LANGKAH 9  — Suppression, telemetry, case review:
blueteam_false_positive_kb(); blueteam_owned_domains(); blueteam_metrics()
blueteam_case_list(); blueteam_case_get(case_id=<case_id>)

LANGKAH 10 — Geo heatmap:
blueteam_wazuh_geo_heatmap(since="24h", response_format="json")

Supplementary tools (by category — the full 123-tool set; LANGKAH 0–10 is the default path):

- Alert search/aggregation: blueteam_wazuh_indexer_search, blueteam_wazuh_alerts,
  wazuh_alert_aggregate_analysis, wazuh_alert_focused_crawl, wazuh_alert_dsl_query,
  wazuh_alert_timeline, wazuh_attack_velocity, blueteam_wazuh_alert_summarize,
  blueteam_wazuh_alert_compare.
- Threat intel: crowdsec_ip_reputation(/bulk), threatfox_ioc_search(/bulk),
  greynoise_ip_context, netra_ip_analysis, otx_lookup_bulk, urlhaus_lookup(/bulk),
  urlhaus_hash_lookup, blueteam_lookup_domain_virustotal, blueteam_lookup_hash_virustotal,
  blueteam_unified_threat_score, blueteam_mitre_lookup.
- Baselines & anomaly: blueteam_baseline_profile, blueteam_baseline_drift,
  blueteam_calendar_heatmap, blueteam_beacon_detect.
- Wazuh Manager (agents/rules/config): blueteam_wazuh_agents, blueteam_wazuh_agents_summary,
  blueteam_wazuh_get_cluster_nodes, blueteam_wazuh_get_rules, blueteam_wazuh_get_groups,
  blueteam_wazuh_get_decoders, blueteam_wazuh_get_security_events, blueteam_wazuh_manager_logs,
  blueteam_wazuh_get_rule_files, blueteam_wazuh_get_rule_file_content,
  blueteam_wazuh_get_agent_sca, blueteam_wazuh_list_sca_policies, blueteam_wazuh_get_sca_policy_checks.
- Compliance/SCA/vuln: blueteam_wazuh_syscheck, blueteam_wazuh_compliance,
  blueteam_wazuh_vulnerabilities.
- Host forensics: blueteam_read_auth_log, blueteam_read_syslog, blueteam_read_web_log,
  blueteam_failed_logins, blueteam_last_logins, blueteam_who_is_logged_in,
  blueteam_find_suid_files, blueteam_find_world_writable, blueteam_list_connections,
  blueteam_list_listening_ports, blueteam_list_processes, blueteam_list_cron_jobs,
  blueteam_list_users, blueteam_hash_file, blueteam_journalctl, blueteam_rootkit_scan,
  blueteam_lynis_audit, blueteam_system_health, blueteam_sudo_history,
  blueteam_check_open_firewall, blueteam_check_ssh_authorized_keys, blueteam_check_updates,
  blueteam_fail2ban_status, blueteam_fail2ban_jail_status, blueteam_fail2ban_unban,
  blueteam_capture_traffic.
- Domain/asset: blueteam_whois_lookup, blueteam_crtsh_lookup, blueteam_asset_context.
- Case/IOC/history: blueteam_case_create, blueteam_case_add_iocs, blueteam_case_add_verdict,
  blueteam_case_list, blueteam_case_get, blueteam_extract_iocs, blueteam_ioc_lifecycle,
  blueteam_investigate_ip, blueteam_playbook_run, blueteam_investigation_history,
  blueteam_investigation_summary, blueteam_false_positive_tracker.
- Geo: blueteam_wazuh_geo_distribution (by country).
- Forensics/scanning/other: blueteam_check_webshell, blueteam_semantic_search,
  blueteam_threat_hunt, blueteam_stix_analyze, blueteam_prompt_route.
- AI/LLM attack detection: blueteam_ai_bot_recon (AI-agent user-agents probing exploit paths).
- Sangfor blocklist: sangfor_blocklist_check(ip=<ip>) for a single IP;
  sangfor_blocklist_list(limit=…, date_start="YYYY-MM-DD HH:MM:SS", date_end=…) for the list —
  no ``since`` / ``offset`` params (use date_start/date_end).

—— FORMAT MARKDOWN: compose the report from steps 1–10 (ringkasan → subdomain → IOC →
   threat intel → 3-Sum → attack graph → LangGraph → email → MITRE → geo).

—— FORMAT DOCX (officecli): blueteam_export_report(format="docx", title="<...>",
   path="/var/log/blue-team-mcp/exports/laporan_24jam_<date>.docx", docx_sections=[...])

—— FORENSIC EXPORT (HUMAN ONLY): blueteam_wazuh_export(since="24h", bypass_redaction=true,
   forensic_token="<BLUETEAM_FORENSIC_TOKEN>")
   → streams to /var/log/blue-team-mcp/exports/export_<timestamp>.jsonl (filename auto-generated;
     NO ``path`` parameter). WITHOUT ``bypass_redaction=true`` the export is protect_victim-masked
     (subdomains stay masked). Analyst reads the file on the server (cat/jq); the LLM assists only
     with REDACTED analysis.
```

---

## Requirements

- Python 3.11+
- `mcp`, `httpx[http2]`, `pydantic`, `networkx`, `langgraph`, `officecli-sdk`
- See `requirements.txt`.

---

## Development

- Before merge: `python3 check_guardrails.py --strict` must exit 0, and logging stays on stderr.
