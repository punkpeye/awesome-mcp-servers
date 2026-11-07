# -*- coding: utf-8 -*-
"""三域医研 · 本地 MCP Server（stdio）

定位（2026-11-06 v2）
--------------------
**本地客户端形态**。与远程 MCP（服务端 app/api/routes/open_mcp.py）**同一语义、互补场景**：

  · 本地 stdio（本文件）：客户端能拉起本地子进程时用 —— Claude Desktop / Claude Code / Cline / 任何本机脚本。
    优点：不依赖网络长连接、密钥留在本机环境变量、断网恢复简单。
  · 远程 HTTP（另一个组件）：Dify / Coze / 云端 agent —— 它们**无法**拉起本地进程。

v2 相对 v1 的三处改进
--------------------
1. **每个动作一个独立工具**（`sanyu_act_roc`、`sanyu_act_primer_design`…）。
   v1 只有 list/run 两个通用工具 ⇒ agent 要先 list 再 run，多一次往返、且模型常忘记先 list。
   现在工具名 + 参数 schema 直接出现在 agent 工具列表里，一次调用到位。
   （仍保留 `sanyu_list_actions` / `sanyu_run_action` 作为兜底与总览）
2. **协议版本升到 2025-06-18**，同时向下兼容 2025-03-26 / 2024-11-05 的 initialize。
3. **启动即拉目录**：首次 tools/list 前拉一次动作目录并**进程内缓存 5 分钟**，
   目录变更不需要重装客户端。拉不到就用兜底两工具，**绝不因此让整个 MCP 起不来**。

设计铁律
--------
1. 本文件不含任何统计/生信算法 —— 只转发。
2. engine_status / data_source 原样透出，不因「agent 不好理解」就抹掉。
3. 失败如实返回（含 hint_fields），不伪造成功；写动作由服务端 403 拒绝，本地不做二次判断。
4. 仅依赖标准库：`python sanyu_mcp.py` 可直接运行，无需 pip install。

运行
----
    SANYU_API_KEY=sk-sanyu-xxx python sanyu_mcp.py              # stdio 服务
    SANYU_API_KEY=sk-sanyu-xxx python sanyu_mcp.py --selftest   # 自检
    SANYU_API_KEY=sk-sanyu-xxx python sanyu_mcp.py --list       # 打印目录后退出

客户端配置（Claude Desktop / Claude Code）
    {
      "mcpServers": {
        "sanyu-research": {
          "command": "python",
          "args": ["/绝对路径/sanyu_mcp.py"],
          "env": { "SANYU_API_KEY": "sk-sanyu-xxx" }
        }
      }
    }
"""
from __future__ import annotations

import json
import os
import sys
import time
import traceback
import urllib.error
import urllib.request

VERSION = "2.0.0"
PROTOCOL_VERSION = "2025-06-18"
SUPPORTED_PROTOCOLS = ("2025-06-18", "2025-03-26", "2024-11-05")
DEFAULT_BASE = "https://sanyu.wentangkeji.com"
TIMEOUT = 180
CATALOG_TTL = 300          # 目录缓存 5 分钟

_CATALOG = {"ts": 0.0, "actions": []}


# ── HTTP（标准库） ────────────────────────────────────────────────────────
def _base() -> str:
    return (os.environ.get("SANYU_BASE_URL") or DEFAULT_BASE).rstrip("/")


def _key() -> str:
    return (os.environ.get("SANYU_API_KEY") or "").strip()


def _call(path: str, method: str = "GET", body=None):
    url = _base() + path
    data = json.dumps(body, ensure_ascii=False).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Accept", "application/json")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    k = _key()
    if k:
        req.add_header("Authorization", "Bearer " + k)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.status, json.loads(r.read().decode("utf-8", "replace") or "{}")
    except urllib.error.HTTPError as e:
        try:
            payload = json.loads(e.read().decode("utf-8", "replace") or "{}")
        except Exception:
            payload = {"error": "http_%d" % e.code}
        return e.code, payload
    except Exception as e:
        return 0, {"error": "network_error", "message": str(e)[:200]}


# ── 结果包装 ──────────────────────────────────────────────────────────────
def _ok(text: str):
    return {"content": [{"type": "text", "text": text}], "isError": False}


def _err(text: str):
    return {"content": [{"type": "text", "text": text}], "isError": True}


# ── 动作目录（带缓存） ────────────────────────────────────────────────────
def fetch_catalog(force: bool = False):
    """拉白名单动作目录。失败返回 []（不影响 list/run 兜底工具）。"""
    now = time.time()
    if not force and _CATALOG["actions"] and now - _CATALOG["ts"] < CATALOG_TTL:
        return _CATALOG["actions"]
    status, body = _call("/api/open/v1/actions")
    if status != 200:
        return _CATALOG["actions"] or []
    acts = body.get("actions") or []
    _CATALOG["actions"] = acts
    _CATALOG["ts"] = now
    return acts


# ── 工具 1：目录总览 ──────────────────────────────────────────────────────
def tool_list_actions(_args=None):
    if not _key():
        return _err("缺少 SANYU_API_KEY。请在三域「设置 → API 密钥」生成后配置到环境变量。")
    acts = fetch_catalog(force=True)
    if not acts:
        status, body = _call("/api/open/v1/actions")
        return _err("获取动作目录失败（HTTP %s）：%s"
                    % (status, json.dumps(body, ensure_ascii=False)[:300]))

    lines = [
        "# 三域医研 · 真算法动作目录（v1，共 %d 个）" % len(acts),
        "",
        "这些动作全部由真实算法引擎执行，不是大模型推算。",
        "每次执行的返回都带 engine_status（real/unavailable）与 data_source，请如实转述。",
        "",
        "两种调用方式（推荐第一种）：",
        "  · 直接调对应工具，如 `sanyu_act_roc`（参数见其 schema）",
        "  · 或通用入口 `sanyu_run_action(action_id=\"act_roc\", args={...})`",
        "",
    ]
    stage = None
    for a in sorted(acts, key=lambda x: (x.get("stage") or "", x.get("id") or "")):
        s = a.get("stage") or "其他"
        if s != stage:
            lines.append("## %s" % s)
            stage = s
        params = a.get("params") or {}
        req = [k for k, v in params.items() if isinstance(v, dict) and v.get("required")]
        lines.append("- `%s`（工具名 `%s`）— %s"
                     % (a.get("id"), _tool_name(a.get("id") or ""), a.get("name") or ""))
        if a.get("when"):
            lines.append("    适用：%s" % a["when"])
        if a.get("returns"):
            lines.append("    产出：%s" % a["returns"])
        lines.append("    必填：%s ｜ 计费：%d 分 ｜ verified：%s"
                     % ("、".join(req) if req else "无", int(a.get("cost") or 0),
                        "是" if a.get("verified") else "否"))
    return _ok("\n".join(lines))


# ── 工具 2：通用执行 ──────────────────────────────────────────────────────
def _fmt_result(body):
    """把开放 API 响应渲染成人/agent 都能读的文本。"""
    if body.get("success") is None and body.get("error"):
        return _err("执行失败：%s" % json.dumps(body, ensure_ascii=False)[:300])

    result = body.get("result")
    pretty = json.dumps(result, ensure_ascii=False, indent=2) if result is not None else "（无返回体）"
    if len(pretty) > 6000:
        pretty = pretty[:6000] + "\n...（已截断，完整结果见审计编号）"

    lines = [
        "动作：%s" % body.get("action"),
        "执行结果：%s" % ("成功" if body.get("success") else "失败"),
        # 🔴 这两行是平台信誉所在，必须原样转述给用户
        "引擎状态：%s（real=真算法实跑 / unavailable=引擎不可用 / error=执行出错）"
        % body.get("engine_status"),
        "数据来源：%s" % body.get("data_source"),
        "计费：%d 分 ｜ 审计编号：%s ｜ 耗时：%s ms"
        % (int(body.get("cost") or 0), body.get("audit_id"), body.get("latency_ms")),
    ]
    if body.get("warnings"):
        lines.append("提示：%s" % "；".join(str(w) for w in body["warnings"]))
    if body.get("error"):
        lines.append("错误：%s" % body["error"])
    if body.get("hint_fields"):
        lines.append("缺少参数：%s（补齐后重试即可，本次未扣分）" % "、".join(body["hint_fields"]))
    lines += ["", "结果：", pretty]
    text = "\n".join(lines)
    return _ok(text) if body.get("success") else _err(text)


def _do_run(action_id, payload):
    status, body = _call("/api/open/v1/run/" + action_id, "POST", payload or {})
    if status == 401:
        return _err("API Key 无效或已撤销，请重新生成。")
    if status == 403:
        d = body.get("detail") if isinstance(body, dict) else body
        msg = d.get("message") if isinstance(d, dict) else str(d)
        # 2026-11-07：原写死"30 个"，扩容后会对外报错数（实测已到 106）
        _n = len(_CATALOG.get("actions") or []) or "全部"
        return _err("该动作未开放（v1 共开放 %s 个纯计算动作，可用 sanyu_list_actions 查看）：%s"
                    % (_n, msg or status))
    if status == 429:
        d = body.get("detail") if isinstance(body, dict) else body
        msg = d.get("message") if isinstance(d, dict) else str(d)
        return _err("调用额度或频率已达上限：%s" % (msg or "请稍后再试"))
    if status != 200:
        return _err("执行失败（HTTP %s）：%s" % (status, json.dumps(body, ensure_ascii=False)[:300]))
    return _fmt_result(body)


def tool_run_action(args):
    args = args or {}
    action_id = str(args.get("action_id") or "").strip()
    payload = args.get("args") or {}
    if not action_id:
        return _err("缺少 action_id。可先调用 sanyu_list_actions 查看可用动作。")
    if isinstance(payload, str):
        try:
            payload = json.loads(payload)
        except Exception:
            return _err("args 必须是 JSON 对象")
    if not isinstance(payload, dict):
        return _err("args 必须是 JSON 对象")
    return _do_run(action_id, payload)


# ── 动态工具：每个动作一个 ────────────────────────────────────────────────
def _tool_name(action_id: str) -> str:
    """act_roc → sanyu_act_roc（MCP 工具名只允许 [a-zA-Z0-9_-]，act_ 已合规）。"""
    return action_id if action_id.startswith("sanyu_") else "sanyu_" + action_id


def _param_schema(spec):
    """把 actions.json 的参数描述转成 JSON Schema。"""
    if not isinstance(spec, dict):
        return {"type": "string"}
    t = spec.get("type", "string")
    js = {"type": t if t in ("string", "number", "integer", "boolean", "array", "object") else "string"}
    desc = spec.get("desc")
    if desc:
        js["description"] = desc
    if t == "array" and isinstance(spec.get("items"), dict):
        it = spec["items"].get("type", "string")
        js["items"] = {"type": it if it in ("string", "number", "integer", "boolean", "object") else "string"}
    if spec.get("enum"):
        js["enum"] = spec["enum"]
    return js


def _action_tools(acts):
    """把目录转成「一动作一工具」的 MCP 工具定义。"""
    out = []
    for a in acts:
        aid = a.get("id") or ""
        if not aid:
            continue
        params = a.get("params") or {}
        props, required = {}, []
        for pname, spec in params.items():
            props[pname] = _param_schema(spec)
            if isinstance(spec, dict) and spec.get("required"):
                required.append(pname)
        desc = "[%s] %s" % (a.get("stage") or "三域医研", a.get("name") or aid)
        if a.get("when"):
            desc += "｜适用：%s" % a["when"]
        if a.get("returns"):
            desc += "｜产出：%s" % a["returns"]
        desc += "｜计费 %d 分｜真实算法引擎执行，返回带 engine_status" % int(a.get("cost") or 0)
        out.append({
            "name": _tool_name(aid),
            "description": desc[:900],
            "inputSchema": {"type": "object", "properties": props, "required": required},
            "_action_id": aid,
        })
    return out


_STATIC_TOOLS = [
    {
        "name": "sanyu_list_actions",
        "description": (
            "列出三域医研平台上全部可用的**真算法**动作（v1 白名单，覆盖统计分析 / 生信解读 / "
            "组学 / 序列湿实验 / 动物实验 / 药理毒理 / 文献检索 / 方案设计），含每个动作的参数、必填项与单次计费。"
            "这些动作由真实算法引擎执行（手写 MCTS、DESeq2-like 负二项、FlowSOM、真 Vina/Scanpy/BLAST/STRING），"
            "不是大模型推算。**动作总数为动态值**，以本次返回为准，不要假设固定数量。"
            "不确定该用哪个工具时先调它总览。"
        ),
        "inputSchema": {"type": "object", "properties": {}, "required": []},
        "_action_id": None,
    },
    {
        "name": "sanyu_run_action",
        "description": (
            "通用执行入口：按 action_id 执行任意已开放的真算法动作。"
            "已有对应专用工具（如 sanyu_act_roc）时优先用专用工具。"
            "返回体含 engine_status（real/unavailable/error）与 data_source，请如实转述。"
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "action_id": {"type": "string",
                              "description": "动作 id，如 act_roc / act_deg_analyze"},
                "args": {"type": "object", "description": "动作参数对象"},
            },
            "required": ["action_id"],
        },
        "_action_id": None,
    },
]


def all_tools():
    """静态兜底工具 + 每个动作一个专用工具。目录拉不到时只剩静态两个。"""
    acts = fetch_catalog()
    return _STATIC_TOOLS + _action_tools(acts)


def dispatch(name, args):
    """工具调用分发。"""
    if name == "sanyu_list_actions":
        return tool_list_actions(args)
    if name == "sanyu_run_action":
        return tool_run_action(args)
    if name.startswith("sanyu_act_"):
        return _do_run(name[len("sanyu_"):], args or {})
    return _err("未知工具：%s。可调用 sanyu_list_actions 查看可用工具。" % name)


# ── JSON-RPC ──────────────────────────────────────────────────────────────
def handle(msg: dict):
    method = msg.get("method")
    mid = msg.get("id")
    params = msg.get("params") or {}

    if mid is None and isinstance(method, str) and method.startswith("notifications/"):
        return None

    def ok(result):
        return {"jsonrpc": "2.0", "id": mid, "result": result}

    def err(code, message):
        return {"jsonrpc": "2.0", "id": mid, "error": {"code": code, "message": message}}

    if method == "initialize":
        # 回显客户端请求的版本（若在支持列表内），否则回我们最高版本
        req_v = str(params.get("protocolVersion") or "")
        ver = req_v if req_v in SUPPORTED_PROTOCOLS else PROTOCOL_VERSION
        return ok({
            "protocolVersion": ver,
            "capabilities": {"tools": {"listChanged": False}},
            "serverInfo": {"name": "sanyu-research", "version": VERSION},
            "instructions": (
                "三域医研真算法科研平台（本地 MCP）。提供由真实算法引擎执行的动作："
                "统计检验 / 生信与组学 / 序列设计 / 动物实验 / 药理毒理 / 文献检索 / 方案设计，"
                "不是大模型推算。每个动作都是一等工具（sanyu_act_*），参数与必填项见其 inputSchema；"
                "动作总数以 tools/list 或 sanyu_list_actions 的返回为准（动态值）。"
                "每次执行返回 engine_status（real/unavailable/error）与 data_source，请如实转述；"
                "失败不扣积分。判成功请看 success 字段，不要只看 HTTP 状态。"
            ),
        })
    if method == "tools/list":
        tools = [{k: v for k, v in t.items() if not k.startswith("_")} for t in all_tools()]
        return ok({"tools": tools})
    if method == "tools/call":
        name = params.get("name")
        try:
            return ok(dispatch(name, params.get("arguments") or {}))
        except Exception as e:
            return ok(_err("工具执行异常：%s: %s" % (type(e).__name__, str(e)[:200])))
    if method == "ping":
        return ok({})
    if method in ("logging/setLevel", "resources/list", "prompts/list"):
        return ok({})
    return err(-32601, "不支持的方法：%s" % method)


def serve():
    """stdio 主循环：逐行读 JSON-RPC，逐行写响应。"""
    # 启动自检：没配 key 时写到 **stderr**（stdout 是协议通道，绝不能混文本）
    # 否则用户只会看到 2 个兜底工具，不知道是自己没配密钥。
    if not _key():
        sys.stderr.write(
            "[sanyu-mcp] 警告：未设置 SANYU_API_KEY —— 能列出工具但无法执行任何动作。\n"
            "[sanyu-mcp] 请到 https://sanyu.wentangkeji.com/api-keys 生成 sk-sanyu-xxx，\n"
            "[sanyu-mcp] 写进客户端的 env 配置里再重启。\n")
        sys.stderr.flush()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except Exception:
            sys.stdout.write(json.dumps(
                {"jsonrpc": "2.0", "id": None,
                 "error": {"code": -32700, "message": "JSON 解析失败"}}, ensure_ascii=False) + "\n")
            sys.stdout.flush()
            continue
        try:
            resp = handle(msg)
        except Exception:
            traceback.print_exc(file=sys.stderr)
            resp = {"jsonrpc": "2.0", "id": msg.get("id"),
                    "error": {"code": -32603, "message": "内部错误"}}
        if resp is not None:
            sys.stdout.write(json.dumps(resp, ensure_ascii=False) + "\n")
            sys.stdout.flush()


# ── 自检 / 目录打印 ───────────────────────────────────────────────────────
def selftest():
    print("base:", _base())
    print("key :", ("已配置 " + _key()[:16] + "...") if _key() else "未配置")
    print("ver :", VERSION, "| protocol:", PROTOCOL_VERSION)
    print()

    tools = all_tools()
    dyn = [t for t in tools if t.get("_action_id")]
    print("工具总数:", len(tools), "（静态 2 + 动作专用 %d）" % len(dyn))
    if dyn:
        print("示例专用工具:", [t["name"] for t in dyn[:5]])
        t0 = dyn[0]
        print("  其一 schema 必填:", t0["inputSchema"].get("required"))

    print()
    r = tool_list_actions()
    print("== sanyu_list_actions ==", "isError:", r["isError"])
    print(r["content"][0]["text"][:400])

    print()
    r2 = dispatch("sanyu_act_primer_tm",
                  {"sequence": "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"})
    print("== 专用工具 sanyu_act_primer_tm ==", "isError:", r2["isError"])
    print(r2["content"][0]["text"][:400])

    print()
    r3 = dispatch("sanyu_act_writing_one_click", {})
    print("== 写动作必须被拒 ==", "isError:", r3["isError"], "|",
          r3["content"][0]["text"][:120])
    return 0


def print_catalog():
    """打印动作目录。

    🔴 2026-11-06：原实现失败时**静默输出 0 行**（key 无效 → 401 → 兜底 2 个通用工具 →
    过滤掉无 _action_id 的 → 什么都没有），用户会以为客户端坏了。现在必须说清原因，
    并且用非 0 退出码，让脚本/CI 也能判断。
    """
    if not _key():
        print("缺少 SANYU_API_KEY。请到 https://sanyu.wentangkeji.com/api-keys "
              "生成 sk-sanyu-xxx，再设为环境变量。", file=sys.stderr)
        return 2

    acts = fetch_catalog(force=True)
    if not acts:
        status, body = _call("/api/open/v1/actions")
        detail = body.get("detail") if isinstance(body, dict) else None
        if isinstance(detail, dict):
            msg = detail.get("message") or detail.get("error") or str(detail)
        else:
            msg = str(detail or body or "")[:200]
        print("拉取动作目录失败（HTTP %s）：%s" % (status, msg), file=sys.stderr)
        if status == 401:
            print("→ 这把 key 无效或已被撤销。请到 https://sanyu.wentangkeji.com/api-keys "
                  "重新生成（明文只显示一次）。", file=sys.stderr)
        elif status == 0:
            print("→ 网络不通。检查本机网络，或确认 SANYU_BASE_URL（当前 %s）是否可达。"
                  % _base(), file=sys.stderr)
        else:
            print("→ 服务端异常，稍后重试；若持续如此请把上面这行报给平台方。", file=sys.stderr)
        return 1

    n = 0
    for t in all_tools():
        if t.get("_action_id"):
            print("%-30s %s" % (t["name"], t["description"][:80]))
            n += 1
    # 汇总写 stderr，保持 stdout 只有纯列表（方便管道 / diff）
    print("\n共 %d 个动作。直接运行 `python sanyu_mcp.py` 即为本机 MCP 服务。" % n,
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        raise SystemExit(selftest())
    if "--list" in sys.argv:
        raise SystemExit(print_catalog())
    serve()
