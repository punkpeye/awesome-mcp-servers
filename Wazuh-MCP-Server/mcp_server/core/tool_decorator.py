#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Decorator that wraps @mcp.tool with cross-cutting SOC concerns.
Usage:
    @blueteam_tool(
        name="blueteam_my_tool",
        annotations={"readOnlyHint": True, "destructiveHint": False,
                      "idempotentHint": True, "openWorldHint": False},
        audit=True,      # log every invocation to BLUETEAM_AUDIT_LOG
        truncate=True,   # cap response at CHARACTER_LIMIT
        redact=True,     # apply 6-layer PII masking by default (opt out with redact=False)
    )
    async def blueteam_my_tool(params: MyInput) -> str:
        ...
The decorator applies: audit -> call -> catch BlueTeamMCPError -> redact -> truncate.
The original function signature is preserved so FastMCP generates the correct tool schema.
"""
from __future__ import annotations
import functools
import inspect
import json
import time
from typing import Any, Callable
from mcp_server import mcp
from mcp_server.core.audit import _audit_log, _truncate_if_needed
from mcp_server.core.redact import _redact_alert_data
from mcp_server.core.exceptions import BlueTeamMCPError
from mcp_server.core import metrics

# Sensible defaults - every blue-team tool is read-only unless overridden
_READ_ONLY_ANNOTATIONS = {
    "readOnlyHint": True,
    "destructiveHint": False,
    "idempotentHint": True,
    "openWorldHint": False,
}


def _make_params_dict(params: Any) -> dict:
    """Extract a safe dict from a Pydantic model or raw dict for audit logging."""
    if params is None:
        return {}
    if isinstance(params, dict):
        return dict(params)
    if hasattr(params, "model_dump"):
        try:
            return params.model_dump()
        except Exception:
            pass
    return {}


# Public decorator
def blueteam_tool(
    name: str,
    annotations: dict | None = None,
    *,
    audit: bool = True,
    truncate: bool = True,
    redact: bool = True,
) -> Callable:
    """Register a FastMCP tool with automatic audit, truncation, and error handling.
    Args:
        name: MCP tool name (e.g. ``"blueteam_wazuh_agents"``).
        annotations: MCP tool hints dict.  Defaults to read-only blue-team safe values.
        audit: If True, log every invocation to ``BLUETEAM_AUDIT_LOG``.
        truncate: If True, cap the response at ``CHARACTER_LIMIT`` with a cursor hint.
        redact: If True (default), apply 6-layer PII/credential masking to the result
            (str/dict/list). This is the uniform security boundary - opt out with
            redact=False only for tools returning attacker-only data that
            _redact_alert_data already keeps visible under protect_victim.

    Returns:
        A decorator that wraps the async function and registers it with FastMCP.
    """
    ann = dict(_READ_ONLY_ANNOTATIONS)
    if annotations:
        ann.update(annotations)

    def decorator(func):
        # Snapshot the original signature so FastMCP generates the correct schema.
        try:
            _sig = inspect.signature(func)
        except (ValueError, TypeError):
            _sig = None

        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            _t0 = time.monotonic()
            params = args[0] if args else None

            # pre-call: audit
            if audit:
                pd = _make_params_dict(params)
                _audit_log(name, {k: v for k, v in pd.items()
                                  if k not in ("api_key", "key")})

            # call
            try:
                result = await func(*args, **kwargs)
            except BlueTeamMCPError as e:
                return json.dumps(
                    {"error": str(e), "type": type(e).__name__},
                    indent=2, ensure_ascii=False,
                )

            # timing
            metrics.record_timing(name, (time.monotonic() - _t0) * 1000)

            # post-call: redact (default ON uniform security boundary)
            if redact:
                result = _redact_alert_data(result, params=params)
                if not isinstance(result, str):
                    result = json.dumps(result, indent=2, ensure_ascii=False)

            # post-call: truncate (nearly always)
            if truncate:
                bypass_char = (
                    getattr(params, "bypass_character_limit", False)
                    if params is not None and hasattr(params, "bypass_character_limit")
                    else False
                )
                result_str = result if isinstance(result, str) else str(result)
                result = _truncate_if_needed(result_str, bypass=bypass_char)

            return result

        # Preserve the original signature for FastMCP schema generation.
        if _sig is not None:
            wrapper.__signature__ = _sig

        # Carry the original function's annotations and module so FastMCP's
        # func_metadata() can resolve Pydantic input-model types via the tool
        # module's import namespace (rather than this decorator module's).
        # functools.wraps already copies __annotations__, __module__, __name__,
        # __doc__, and __wrapped__ — but under `from __future__ import annotations`
        # those are deferred strings, and FastMCP resolves via __globals__ (which is
        # read-only on Python 3.12+). Resolve the strings into real types here.
        def _resolve_annotations(anns, globalns):
            out = {}
            for k, v in (anns or {}).items():
                if isinstance(v, str):
                    try:
                        out[k] = eval(v, globalns)
                    except Exception:
                        out[k] = v  # unresolvable,leave as-is.
                else:
                    out[k] = v
            return out

        wrapper.__annotations__ = _resolve_annotations(func.__annotations__, func.__globals__)
        wrapper.__module__ = func.__module__

        # Register with FastMCP.
        return mcp.tool(name=name, annotations=ann)(wrapper)

    return decorator
