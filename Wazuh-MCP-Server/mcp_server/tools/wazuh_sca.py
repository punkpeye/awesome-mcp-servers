#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Wazuh SCA (Security Configuration Assessment) tools.

Exposes Wazuh Manager SCA endpoints for agent compliance scanning:
  - blueteam_wazuh_get_agent_sca       - list SCA scan results for an agent
  - blueteam_wazuh_get_sca_policy_checks - detailed check results per policy
  - blueteam_wazuh_list_sca_policies     - policy inventory for an agent

All tools use @blueteam_tool for automatic audit logging, exception handling,
and response truncation.

NOTE: No ``from __future__ import annotations`` — required for @blueteam_tool
      type resolution (see wazuh_siem.py for rationale).
"""

import json
from typing import Optional, Literal

from pydantic import BaseModel, ConfigDict, Field

from mcp_server.core.tool_decorator import blueteam_tool
from mcp_server.wazuh.auth import _wazuh_api_get


# blueteam_wazuh_get_agent_sca - list SCA scan results per agent
class AgentSCAInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    agent_id: str = Field(..., min_length=3, max_length=16,
                           description="Wazuh agent ID (required)")
    name: Optional[str] = Field(default=None, max_length=128,
                                 description="Filter by SCA policy name")
    description: Optional[str] = Field(default=None, max_length=256,
                                        description="Filter by policy description")
    references: Optional[str] = Field(default=None, max_length=128,
                                       description="Filter by references")
    search: Optional[str] = Field(default=None, max_length=128)
    select: Optional[str] = Field(default=None, max_length=256)
    sort: Optional[str] = Field(default=None)
    q: Optional[str] = Field(default=None, max_length=256)
    distinct: bool = Field(default=False)
    limit: int = Field(default=50, ge=1, le=500)
    offset: int = Field(default=0, ge=0)
    response_format: Literal["markdown", "json"] = Field(default="markdown")


@blueteam_tool(name="blueteam_wazuh_get_agent_sca")
async def blueteam_wazuh_get_agent_sca(params: AgentSCAInput) -> str:
    """Get SCA (Security Configuration Assessment) scan results for a Wazuh agent.

    Returns policy-level scan summaries — pass, fail, score per policy.
    Use ``blueteam_wazuh_get_sca_policy_checks`` for per-check details.
    """
    api: dict[str, str] = {
        "limit": str(params.limit),
        "offset": str(params.offset),
    }
    if params.name:         api["name"] = params.name
    if params.description:  api["description"] = params.description
    if params.references:   api["references"] = params.references
    if params.search:       api["search"] = params.search
    if params.select:       api["select"] = params.select
    if params.sort:         api["sort"] = params.sort
    if params.q:            api["q"] = params.q
    if params.distinct:     api["distinct"] = "true"

    data = await _wazuh_api_get(f"/sca/{params.agent_id}", api)
    items = data.get("data", {}).get("affected_items", [])
    total = data.get("data", {}).get("total_affected_items", len(items))

    if params.response_format == "json":
        return json.dumps({
            "agent_id": params.agent_id,
            "total": total,
            "policies": items[:params.limit],
        }, indent=2)

    lines = [f"# SCA Scan Results — Agent `{params.agent_id}` ({len(items)} policies)", ""]
    for p in items[:30]:
        name = p.get("name", "?")
        score = p.get("score", 0)
        p_pass = p.get("pass", 0)
        p_fail = p.get("fail", 0)
        lines.append(
            f"- **{name}** — score: {score}% "
            f"(pass: {p_pass}, fail: {p_fail})"
        )
    return "\n".join(lines)


# blueteam_wazuh_get_sca_policy_checks - per-check details
class SCAPolicyChecksInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    agent_id: str = Field(..., min_length=3, max_length=16)
    policy_id: str = Field(..., min_length=1, max_length=64,
                            description="SCA policy ID from get_agent_sca results")
    title: Optional[str] = Field(default=None, max_length=256)
    description: Optional[str] = Field(default=None, max_length=512)
    rationale: Optional[str] = Field(default=None, max_length=256)
    remediation: Optional[str] = Field(default=None, max_length=256)
    result: Optional[str] = Field(default=None,
                                   description="Filter: passed, failed, not_applicable")
    condition: Optional[str] = Field(default=None, max_length=256)
    search: Optional[str] = Field(default=None, max_length=128)
    select: Optional[str] = Field(default=None, max_length=256)
    sort: Optional[str] = Field(default=None)
    q: Optional[str] = Field(default=None, max_length=256)
    distinct: bool = Field(default=False)
    limit: int = Field(default=100, ge=1, le=500)
    offset: int = Field(default=0, ge=0)
    response_format: Literal["markdown", "json"] = Field(default="markdown")


@blueteam_tool(name="blueteam_wazuh_get_sca_policy_checks")
async def blueteam_wazuh_get_sca_policy_checks(params: SCAPolicyChecksInput) -> str:
    """Get detailed SCA policy check results for a specific policy on an agent.

    Each check includes the rule title, result (passed/failed), rationale,
    and remediation guidance.  Use after ``blueteam_wazuh_get_agent_sca``
    to drill into a specific policy.
    """
    api: dict[str, str] = {
        "limit": str(params.limit),
        "offset": str(params.offset),
    }
    if params.title:        api["title"] = params.title
    if params.description:  api["description"] = params.description
    if params.rationale:    api["rationale"] = params.rationale
    if params.remediation:  api["remediation"] = params.remediation
    if params.result:       api["result"] = params.result
    if params.condition:    api["condition"] = params.condition
    if params.search:       api["search"] = params.search
    if params.select:       api["select"] = params.select
    if params.sort:         api["sort"] = params.sort
    if params.q:            api["q"] = params.q
    if params.distinct:     api["distinct"] = "true"

    path = f"/sca/{params.agent_id}/checks/{params.policy_id}"
    data = await _wazuh_api_get(path, api)
    items = data.get("data", {}).get("affected_items", [])
    total = data.get("data", {}).get("total_affected_items", len(items))

    if params.response_format == "json":
        return json.dumps({
            "agent_id": params.agent_id,
            "policy_id": params.policy_id,
            "total": total,
            "checks": items[:params.limit],
        }, indent=2)

    # Summary stats
    passed = sum(1 for c in items if c.get("result") == "passed")
    failed = sum(1 for c in items if c.get("result") == "failed")
    lines = [
        f"# SCA Checks — Agent `{params.agent_id}` / Policy `{params.policy_id}`",
        f"Total: {len(items)} checks — ✅ {passed} passed, ❌ {failed} failed",
        "",
    ]
    for c in items[:30]:
        result_icon = "✅" if c.get("result") == "passed" else "❌"
        title = str(c.get("title", c.get("description", "?")))[:80]
        lines.append(f"- {result_icon} {title}")
        if c.get("rationale"):
            lines.append(f"  Rationale: {str(c['rationale'])[:120]}")
    return "\n".join(lines)


# blueteam_wazuh_list_sca_policies - policy-level inventory
class SCAPoliciesInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    agent_id: str = Field(..., min_length=3, max_length=16)
    response_format: Literal["markdown", "json"] = Field(default="markdown")


@blueteam_tool(name="blueteam_wazuh_list_sca_policies")
async def blueteam_wazuh_list_sca_policies(params: SCAPoliciesInput) -> str:
    """List all SCA policies scanned on a given agent.
    Returns policy IDs, names, and pass/fail/score summaries.
    Delegates to ``blueteam_wazuh_get_agent_sca`` with a large limit.
    """
    api = {"limit": "500", "offset": "0"}
    data = await _wazuh_api_get(f"/sca/{params.agent_id}", api)
    items = data.get("data", {}).get("affected_items", [])

    if params.response_format == "json":
        return json.dumps({
            "agent_id": params.agent_id,
            "count": len(items),
            "policies": [
                {
                    "policy_id": p.get("policy_id", p.get("id", "?")),
                    "name": p.get("name", "?"),
                    "score": p.get("score", 0),
                    "pass": p.get("pass", 0),
                    "fail": p.get("fail", 0),
                }
                for p in items
            ],
        }, indent=2)

    lines = [f"# SCA Policies - Agent `{params.agent_id}` ({len(items)})", ""]
    for p in items:
        pid = p.get("policy_id", p.get("id", "?"))
        name = p.get("name", "?")
        score = p.get("score", 0)
        p_pass = p.get("pass", 0)
        p_fail = p.get("fail", 0)
        lines.append(
            f"- `{pid}` — **{name}** — score: {score}% "
            f"(✅ {p_pass}, ❌ {p_fail})"
        )
    return "\n".join(lines)
