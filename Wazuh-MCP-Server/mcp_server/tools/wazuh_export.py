#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Server-side Wazuh alert export - streams documents directly to disk via OpenSearch scroll API.
"""
from __future__ import annotations
import json, os, asyncio, time
from datetime import datetime, timezone
from pathlib import Path
from pydantic import BaseModel, ConfigDict, Field
from mcp_server import mcp, WAZUH_INDEXER_URL, WAZUH_INDEXER_USER, WAZUH_INDEXER_PASSWORD, WAZUH_INDEXER_VERIFY_SSL, BLUETEAM_EXPORT_RETENTION_DAYS, _BYPASS_REDACTION_DESC, _FORENSIC_TOKEN_DESC, BLUETEAM_ALLOW_FORENSIC_BYPASS, BLUETEAM_FORENSIC_TOKEN
from mcp_server.core.audit import _audit_log
from mcp_server.core.redact import _redact_alert_data
from mcp_server.wazuh.time_utils import _parse_time_window
from mcp_server.wazuh.indexer import _WAZUH_INDEX_PATTERNS

_EXPORT_DIR = os.environ.get("BLUETEAM_EXPORT_DIR", "/var/log/blue-team-mcp/exports")


class WazuhExportInput(BaseModel):
    """Input model for blueteam_wazuh_export."""
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    since: str | None = Field(default="24h", max_length=30,
                               description="Time window start. ISO 8601 or relative ('24h', '7d', '90d').")
    until: str | None = Field(default=None, max_length=30,
                               description="Time window end. Defaults to now.")
    agent_name: str | None = Field(default=None, max_length=64,
                                    description="Optional agent name filter.")
    srcip: str | None = Field(default=None, max_length=45,
                               description="Optional source IP filter.")
    keyword: str | None = Field(default=None, max_length=1024,
                                  description="Optional keyword search in full_log.")
    rule_groups: str | None = Field(default=None, max_length=512,
                                     description="Comma-separated rule groups filter.")
    max_docs: int = Field(default=0, ge=0,
                          description="Max documents to export. 0 = unlimited.")
    bypass_redaction: bool = Field(default=False, description=_BYPASS_REDACTION_DESC)
    forensic_token: str | None = Field(default=None, max_length=128, description=_FORENSIC_TOKEN_DESC)


class _ScrollClient:
    """Minimal OpenSearch scroll client - avoids httpx for this specific use case."""
    def __init__(self, base_url: str, user: str, password: str, verify: bool):
        import httpx
        self.base_url = base_url.rstrip("/")
        self.auth = (user, password)
        self.verify = verify
        self._client: httpx.AsyncClient | None = None

    async def _get_client(self) -> "httpx.AsyncClient":
        if self._client is None:
            import httpx
            self._client = httpx.AsyncClient(timeout=httpx.Timeout(120.0), verify=self.verify)
        return self._client

    async def open_scroll(self, index: str, body: dict, scroll: str = "5m") -> dict:
        client = await self._get_client()
        resp = await client.post(f"{self.base_url}/{index}/_search?scroll={scroll}",
                                  auth=self.auth, json=body,
                                  headers={"Content-Type": "application/json"})
        resp.raise_for_status()
        return resp.json()

    async def continue_scroll(self, scroll_id: str, scroll: str = "5m") -> dict:
        client = await self._get_client()
        resp = await client.post(f"{self.base_url}/_search/scroll",
                                  auth=self.auth,
                                  json={"scroll": scroll, "scroll_id": scroll_id},
                                  headers={"Content-Type": "application/json"})
        resp.raise_for_status()
        return resp.json()

    async def clear_scroll(self, scroll_id: str) -> None:
        try:
            client = await self._get_client()
            await client.delete(f"{self.base_url}/_search/scroll",
                               auth=self.auth,
                               json={"scroll_id": scroll_id},
                               headers={"Content-Type": "application/json"})
        except Exception:
            pass

    async def close(self):
        if self._client:
            await self._client.aclose()
            self._client = None


@mcp.tool(
    name="blueteam_wazuh_export",
    annotations={"readOnlyHint": False, "destructiveHint": False,
                 "idempotentHint": False, "openWorldHint": False},
)
async def blueteam_wazuh_export(params: WazuhExportInput) -> str:
    """Export Wazuh alerts to a JSONL file on the server using OpenSearch scroll API.

    Streams ALL matching documents directly to disk - no in-memory accumulation.
    Handles millions of documents without OOM. Returns the file path for further
    processing with ``blueteamReadSyslog`` or direct filesystem access.

    **Result**: JSONL file at {BLUETEAM_EXPORT_DIR}/export_<timestamp>.jsonl

    Args:
        params.since: Time window start (ISO 8601 or relative, e.g. '24h').
        params.until: Time window end (defaults to now).
        params.agent_name: Optional agent name filter.
        params.srcip: Optional source IP filter.
        params.keyword: Optional free-text keyword in full_log.
        params.rule_groups: Comma-separated rule groups filter.
        params.max_docs: Max documents to export (0 = unlimited).
        params.bypass_redaction: When true, write RAW (unmasked) data. Requires
            BLUETEAM_ALLOW_FORENSIC_BYPASS=true on the server.
        params.forensic_token: Operator token (matches BLUETEAM_FORENSIC_TOKEN),
            required when bypass_redaction=true and that env is set.

    **Worked Examples**

    1. *Export last 24h (protect_victim-masked by default)*:
       ``blueteam_wazuh_export(since="24h")``

    2. *Export 90 days for a specific IP*:
       ``blueteam_wazuh_export(since="90d", srcip="103.166.210.53")``

    3. *Export with keyword filter, max 100k docs*:
       ``blueteam_wazuh_export(since="7d", keyword="locked OR brute", max_docs=100000)``

    4. *Forensic raw export (HUMAN ONLY - unmasked subdomains/emails)*:
       ``blueteam_wazuh_export(since="24h", bypass_redaction=true, forensic_token="<token>")``
    """
    _audit_log("blueteam_wazuh_export", {"since": params.since, "max_docs": params.max_docs})
    # Forensic bypass gate: requires BLUETEAM_ALLOW_FORENSIC_BYPASS=true + matching token
    if params.bypass_redaction:
        if not BLUETEAM_ALLOW_FORENSIC_BYPASS:
            return json.dumps({"error": "bypass_redaction requires BLUETEAM_ALLOW_FORENSIC_BYPASS=true on the server."}, indent=2)
        if BLUETEAM_FORENSIC_TOKEN:
            if not params.forensic_token or params.forensic_token != BLUETEAM_FORENSIC_TOKEN:
                return json.dumps({"error": "forensic_token required for bypass_redaction."}, indent=2)
    if not WAZUH_INDEXER_URL or not WAZUH_INDEXER_PASSWORD:
        return json.dumps({"error": "WAZUH_INDEXER_URL and WAZUH_INDEXER_PASSWORD must be set."}, indent=2)

    since_iso, until_iso = _parse_time_window(params.since, params.until)
    export_dir = Path(_EXPORT_DIR)
    export_dir.mkdir(parents=True, exist_ok=True)

    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    filepath = export_dir / f"export_{ts}.jsonl"

    # Build query
    must: list[dict] = [
        {"range": {"@timestamp": {"gte": since_iso, "lt": until_iso,
                                   "format": "strict_date_optional_time"}}},
    ]
    if params.agent_name:
        must.append({"match": {"agent.name": params.agent_name.strip()}})
    if params.srcip:
        must.append({"bool": {"should": [
            {"match": {"data.srcip": params.srcip.strip()}},
            {"match_phrase": {"full_log": params.srcip.strip()}},
        ], "minimum_should_match": 1}})
    if params.rule_groups:
        groups = [g.strip() for g in params.rule_groups.split(",") if g.strip()]
        if groups:
            must.append({"terms": {"rule.groups": groups}})
    if params.keyword:
        must.append({"query_string": {"query": params.keyword.strip(), "lenient": True}})

    body = {"size": 5000, "query": {"bool": {"must": must}},
            "sort": [{"@timestamp": "asc"}, {"_id": "asc"}]}

    scroll = _ScrollClient(WAZUH_INDEXER_URL, WAZUH_INDEXER_USER,
                            WAZUH_INDEXER_PASSWORD, WAZUH_INDEXER_VERIFY_SSL)

    total_exported = 0
    scroll_id: str | None = None
    error_msg: str | None = None
    total_val = 0

    try:
        result = await scroll.open_scroll(_WAZUH_INDEX_PATTERNS["alerts"], body)
        scroll_id = result.get("_scroll_id")
        hits = result.get("hits", {})
        total_val = hits.get("total", {}).get("value", 0) if isinstance(hits.get("total"), dict) else 0

        with open(filepath, "w", encoding="utf-8") as f:
            while True:
                hit_list = hits.get("hits", [])
                if not hit_list:
                    break
                for h in hit_list:
                    doc = h.get("_source", h)
                    # Apply redaction policy: raw if bypass_redaction, else protect_victim default
                    if not params.bypass_redaction:
                        doc = _redact_alert_data(doc, policy="protect_victim")
                    else:
                        doc = _redact_alert_data(doc, bypass=True,
                                                  forensic_token=params.forensic_token)
                    f.write(json.dumps(doc, ensure_ascii=False, default=str) + "\n")
                    total_exported += 1
                    if params.max_docs > 0 and total_exported >= params.max_docs:
                        break
                if params.max_docs > 0 and total_exported >= params.max_docs:
                    break
                if not scroll_id:
                    break
                result = await scroll.continue_scroll(scroll_id)
                scroll_id = result.get("_scroll_id")
                hits = result.get("hits", {})

    except Exception as e:
        error_msg = str(e)
    finally:
        if scroll_id:
            await scroll.clear_scroll(scroll_id)
        await scroll.close()

    file_size = filepath.stat().st_size if filepath.exists() else 0

    # Retention: prune old export_*.jsonl files when BLUETEAM_EXPORT_RETENTION_DAYS > 0
    if BLUETEAM_EXPORT_RETENTION_DAYS > 0:
        cutoff = time.time() - BLUETEAM_EXPORT_RETENTION_DAYS * 86400
        try:
            for old in export_dir.glob("export_*.jsonl"):
                try:
                    if old.stat().st_mtime < cutoff:
                        old.unlink()
                except OSError:
                    pass
        except OSError:
            pass

    return json.dumps({
        "status": "completed" if not error_msg else "partial",
        "error": error_msg,
        "total_matching": total_val,
        "exported": total_exported,
        "file": str(filepath),
        "size_bytes": file_size,
        "size_mb": round(file_size / (1024 * 1024), 2),
        "window": {"since": since_iso, "until": until_iso},
    }, indent=2, ensure_ascii=False)
