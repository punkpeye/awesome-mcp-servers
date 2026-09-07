#!/usr/bin/env python3
"""
© TangerangKota-CSIRT (NAuliajati)
Preventive Guardrail Linter - blue_team_server.py
Catches the regression patterns that caused every production outage:
  1. UNBOUND - bare model fields in params: functions
  2. DRIFT - params.field used alongside bare field (inconsistency = near-certain bug)
  3. OVERATCH - params. injected on loop/comprehension vars
  4. ORDER - eager eval refs defined below their dependency
  5. IMPORT - runtime-evaluated types missing from imports
  6. CLOSURE - inner functions referencing params fields as free variables
  7. KWARG - call-site keyword args missing from the callee's signature (TypeError class)

Usage:
  python3 check_guardrails.py             # exit 0=clean, 1=warnings
  python3 check_guardrails.py --strict    # exit 2 on any issue (CI mode)
  python3 check_guardrails.py --json       # JSON output for CI integration
"""

from __future__ import annotations
import ast
import json
import re
import sys
from pathlib import Path

# Source files to lint: the MCP package tree (adapted from the blue_team_server.py)
# monolith version - this repo is modular, so every .py under mcp_server/ dir is scanned).
FILES = [Path(__file__).parent / "main.py"] + sorted((Path(__file__).parent / "mcp_server").rglob("*.py"))
FILES = [f for f in FILES if "__pycache__" not in str(f)]



def _func_models(tree: ast.AST) -> dict[str, str]:
    """Map function_name -> model_name for all params: ModelName functions."""
    fm = {}
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        for arg in node.args.args:
            if arg.arg == 'params' and arg.annotation:
                if isinstance(arg.annotation, ast.Name):
                    fm[node.name] = arg.annotation.id
                elif isinstance(arg.annotation, ast.Constant):
                    fm[node.name] = arg.annotation.value.strip('"')
    return fm


def _params_fields(func_node: ast.AST) -> set[str]:
    """Return all field names accessed via params.xxx in a function."""
    fields = set()
    for child in ast.walk(func_node):
        if isinstance(child, ast.Attribute) and isinstance(child.value, ast.Name) and child.value.id == 'params':
            fields.add(child.attr)
    return fields


def _is_loop_or_local(var: str, func_node: ast.AST) -> bool:
    """Check if a name is assigned locally (for-loop, assignment, def param)."""
    for child in ast.walk(func_node):
        if isinstance(child, ast.Assign):
            for target in child.targets:
                if isinstance(target, ast.Name) and target.id == var:
                    return True
        if isinstance(child, ast.For) and isinstance(child.target, ast.Name) and child.target.id == var:
            return True
        if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for a in child.args.args:
                if a.arg == var:
                    return True  # inner function param, not a free var
    return False


# Check 1: UNBOUND - bare model fields
def check_unbound(source: str, lines: list[str]) -> list[dict]:
    issues = []
    tree = ast.parse(source)
    fm = _func_models(tree)

    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if node.name not in fm:
            continue
        pfields = _params_fields(node)
        if not pfields:
            continue

        for child in ast.walk(node):
            if not isinstance(child, ast.Name) or not isinstance(child.ctx, ast.Load):
                continue
            if child.id not in pfields:
                continue
            if _is_loop_or_local(child.id, node):
                continue

            issues.append({
                'check': 'UNBOUND',
                'func': node.name,
                'line': child.lineno,
                'field': child.id,
                'context': lines[child.lineno - 1].strip()[:80],
            })

    return issues


# Check 2: DRIFT - params.field + bare field in same function (highest-signal)
def check_drift(source: str, lines: list[str]) -> list[dict]:
    issues = []
    tree = ast.parse(source)
    fm = _func_models(tree)

    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if node.name not in fm:
            continue
        pfields = _params_fields(node)
        if not pfields:
            continue

        for field in pfields:
            has_params = False
            has_bare = False
            bare_lines = []

            for child in ast.walk(node):
                if isinstance(child, ast.Attribute) and isinstance(child.value, ast.Name) and child.value.id == 'params' and child.attr == field:
                    has_params = True
                if isinstance(child, ast.Name) and isinstance(child.ctx, ast.Load) and child.id == field:
                    if not _is_loop_or_local(field, node):
                        has_bare = True
                        bare_lines.append(str(child.lineno))

            if has_params and has_bare:
                for bl in bare_lines:
                    issues.append({
                        'check': 'DRIFT',
                        'func': node.name,
                        'line': int(bl),
                        'field': field,
                        'detail': f"'params.{field}' also used - bare '{field}' is likely a bug",
                        'context': lines[int(bl) - 1].strip()[:80],
                    })

    return issues


# Check 3: OVERATCH - params.xxx on loop vars
def check_overaggressive(source: str, lines: list[str]) -> list[dict]:
    issues = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('#') or '"""' in stripped:
            continue
        m = re.match(r'\s*for params\.(\w+) in', stripped)
        if m:
            issues.append({
                'check': 'OVERATCH',
                'line': i + 1,
                'field': m.group(1),
                'context': stripped[:80],
            })
    return issues


# Check 4: ORDER - eager eval ref before definition

def check_order(source: str, lines: list[str]) -> list[dict]:
    issues = []
    func_lines = {}
    for i, line in enumerate(lines):
        m = re.match(r'^\s*def (\w+)\(', line)
        if m:
            func_lines[m.group(1)] = i + 1
        m = re.match(r'^\s*(\w+)\s*=\s*Annotated\[.*?AfterValidator\((\w+)\)', line)
        if m:
            ref = m.group(2)
            if ref not in func_lines or func_lines[ref] > i + 1:
                issues.append({
                    'check': 'ORDER',
                    'line': i + 1,
                    'field': m.group(1),
                    'detail': f"AfterValidator({ref}) ref but {ref} defined at line {func_lines.get(ref, '?')}",
                })
    return issues


# Check 5: IMPORT - missing runtime imports

def check_imports(source: str, lines: list[str]) -> list[dict]:
    issues = []
    tree = ast.parse(source)
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add((alias.asname or alias.name).split('.')[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                for alias in node.names:
                    imports.add(alias.asname or alias.name)

    for node in ast.walk(tree):
        if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Name) and node.value.id == 'Literal':
            if 'Literal' not in imports:
                issues.append({
                    'check': 'IMPORT',
                    'line': node.lineno,
                    'detail': "Literal[...] used but 'Literal' not in typing import",
                })

    return issues


# Check 6: CLOSURE - inner func free variables

def check_closure(source: str, lines: list[str]) -> list[dict]:
    issues = []
    tree = ast.parse(source)
    fm = _func_models(tree)

    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if node.name not in fm:
            continue

        local_names = set()
        for arg in node.args.args:
            local_names.add(arg.arg)
        for child in ast.walk(node):
            if isinstance(child, ast.Assign):
                for t in child.targets:
                    if isinstance(t, ast.Name):
                        local_names.add(t.id)
            if isinstance(child, ast.For):
                if isinstance(child.target, ast.Name):
                    local_names.add(child.target.id)

        for child in ast.walk(node):
            if not isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)) or child is node:
                continue
            inner_params = {arg.arg for arg in child.args.args}
            for gc in ast.walk(child):
                if isinstance(gc, ast.Name) and isinstance(gc.ctx, ast.Load):
                    if gc.id not in inner_params and gc.id not in local_names:
                        if gc.id in ('srcip', 'agent_name', 'domain', 'since', 'until',
                                      'cursor', 'response_format', 'limit', 'keyword',
                                      'bypass_redaction', 'bypass_character_limit'):
                            issues.append({
                                'check': 'CLOSURE',
                                'func': f'{node.name}::{child.name}',
                                'line': gc.lineno,
                                'field': gc.id,
                                'context': lines[gc.lineno - 1].strip()[:80],
                            })
    return issues


# Runner
def check_unexpected_kwargs(source: str, lines: list[str]) -> list[dict]:
    """KWARG - call-site keyword args must exist in the callee's signature.

    Catches `params=params` passed to a local helper whose signature has no
    `params` param (the wazuh_domain._full_scan_paginate TypeError class).
    pyflakes misses this for closure-defined callees, so the gate checks it.
    """
    tree = ast.parse(source)
    # {func_name: set(param_names)} for ALL functions (module-level + nested).
    # Name collisions union the params (conservative: fewer false positives).
    sigs: dict[str, set[str]] = {}
    catchall: set[str] = set()  # functions with **kwargs - any kwarg legal
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            params = {a.arg for a in node.args.args} | {a.arg for a in node.args.kwonlyargs}
            if node.args.kwarg is not None:
                catchall.add(node.name)
            sigs[node.name] = sigs.get(node.name, set()) | params
    issues: list[dict] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name):
            continue
        callee = node.func.id
        if callee not in sigs or callee in catchall:
            continue
        if any(kw.arg is None for kw in node.keywords):  # **expr at call site
            continue
        for kw in node.keywords:
            if kw.arg is not None and kw.arg not in sigs[callee]:
                issues.append({
                    "check": "KWARG",
                    "line": node.lineno,
                    "func": callee,
                    "field": kw.arg,
                    "context": f"unexpected keyword argument '{kw.arg}' for {callee}()",
                })
    return issues


def check_redaction(source: str, lines: list[str]) -> list[dict]:
    """REDACT (warning): flag @mcp.tool handlers that reference PII-bearing fields
    (full_log, data.*, email, agent.name, srcuser/dstuser) without calling
    _redact_alert_data. These are candidates for @blueteam_tool migration."""
    tree = ast.parse(source)
    pii_markers = ("full_log", "data.srcip", "data.domain", "data.url",
                   "email", "agent.name", "srcuser", "dstuser", "data.user_agent")
    issues = []
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        is_mcp_tool = any(
            isinstance(d, ast.Call) and isinstance(d.func, ast.Attribute)
            and d.func.attr == "tool" and isinstance(d.func.value, ast.Name)
            and d.func.value.id == "mcp"
            for d in node.decorator_list
        )
        if not is_mcp_tool:
            continue
        calls_redact = any(
            isinstance(c, ast.Call) and isinstance(c.func, ast.Name)
            and c.func.id == "_redact_alert_data"
            for c in ast.walk(node)
        )
        if calls_redact:
            continue
        src = ast.get_source_segment(source, node) or ""
        if any(m in src for m in pii_markers):
            issues.append({
                "check": "REDACT",
                "func": node.name,
                "line": node.lineno,
                "detail": "MCP tool references PII fields but does not call _redact_alert_data",
                "context": lines[node.lineno - 1].strip()[:80],
            })
    return issues


CHECKS = [
    ('Unbound locals (missing params.)', check_unbound),
    ('Drift (params.x + bare x = bug)', check_drift),
    ('Over-aggressive params. on loops', check_overaggressive),
    ('Eager evaluation order', check_order),
    ('Missing runtime imports', check_imports),
    ('Closure free variable leaks', check_closure),
    ('Unexpected keyword args (KWARG)', check_unexpected_kwargs),
]


def main() -> int:
    if not FILES:
        print("ERROR: no source files found under mcp_server/")
        return 2

    json_out = '--json' in sys.argv
    strict = '--strict' in sys.argv
    all_issues = []
    clean = 0
    redact_warnings: list[dict] = []

    for path in FILES:
        source = path.read_text()
        lines = source.split('\n')
        for r in check_redaction(source, lines):
            r['file'] = str(path.relative_to(Path(__file__).parent))
            redact_warnings.append(r)
        for name, check_fn in CHECKS:
            result = check_fn(source, lines)
            for r in result:
                r['file'] = str(path.relative_to(Path(__file__).parent))
            if result:
                all_issues.extend(result)
                if not json_out:
                    print(f"\n{'='*60}")
                    print(f"{name} ({path.name}): {len(result)} issue(s)")
                    print(f"{'='*60}")
                    for r in result:
                        ctx = r.get('context', r.get('detail', ''))
                        loc = f"{r.get('func','')}@" if 'func' in r else ""
                        print(f"[{r['check']}] {r.get('file','')} {loc}{r.get('line','')}: {r.get('field','')} -> {ctx}")
            else:
                clean += 1
                if not json_out:
                    print(f"{name} ({path.name}): clean")

    if json_out:
        print(json.dumps({'total': len(all_issues), 'issues': all_issues,
                          'redact_warnings': len(redact_warnings)}, indent=2))
        return 0 if len(all_issues) == 0 else (2 if strict else 1)

    # REDACT warnings, informational (not gating): candidates for @blueteam_tool migration.
    if redact_warnings and not json_out:
        print(f"\n{'='*60}")
        print(f"REDACT warnings (PII-touching @mcp.tool tools without _redact_alert_data): {len(redact_warnings)}")
        print(f"{'='*60}")
        for r in redact_warnings[:30]:
            print(f"[REDACT] {r['file']} {r['func']}@{r['line']} -> {r['detail']}")
        if len(redact_warnings) > 30:
            print(f"... and {len(redact_warnings) - 30} more")

    print(f"\n{'='*60}")
    print(f"{clean}/{len(FILES) * len(CHECKS)} filexcheck passes clean. {len(all_issues)} total issue(s).")
    if len(all_issues) == 0:
        print("All guardrails passed.")
        return 0
    return 2 if strict else 1

if __name__ == "__main__":
    sys.exit(main())
