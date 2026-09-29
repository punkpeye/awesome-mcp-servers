# FreeLLM-MCP

An open Model Context Protocol (MCP) server for real-time free LLM performance and availability.

## What it does

`freellm-mcp` exposes live measured metrics from [Free LLM Watch](https://freellmwatch.xyz/) (throughput in tokens/sec, availability, 7-day uptime, tool-calling success, and verbatim failure text) to AI coding assistants and agent workflows via the Model Context Protocol.

Agents can use tools like:
- `list_free_models` — list all tracked free models with status and throughput.
- `get_fastest_free_model` — find the currently fastest healthy free model.
- `check_model_status` — get detailed diagnostics for a specific model ID.
- `get_most_reliable_free_model` — find the healthy free model with the best 7-day uptime.

## Install

From a checkout, install the console entry point:

```bash
python3 -m pip install .
```

The installed command is `freellm-mcp`. It has no third-party runtime dependencies; the optional
MCP SDK is only needed for the conformance check.

## Usage in Claude Desktop / Cursor

Add to your MCP configuration (`claude_desktop_config.json`). Use the installed command after
installation, or point directly at `server.py` in a checkout:

```json
{
  "mcpServers": {
    "freellm": {
      "command": "freellm-mcp",
      "args": []
    }
  }
}
```

By default the server fetches the public board at `https://freellmwatch.xyz/api/status.json` and
caches it for five minutes. Override the source with `FREEMCP_REMOTE_URL`, point it at a local status
JSON file with `FREEMCP_STATUS_PATH`, or move the cache with `FREEMCP_CACHE_PATH`.

Set `FREEMCP_TRANSPORT=http` to serve Streamable HTTP on `http://127.0.0.1:8901/mcp` instead of stdio
(port via `FREEMCP_HTTP_PORT`).

## Local Testing

You can quickly test the server locally with Python:

```bash
python3 server.py
```
And feed JSON-RPC initialization requests to stdin.

Run the unit tests and the independent official-SDK conformance check with:

```bash
python3 -m pytest -q test_server.py
python3 -m pip install mcp   # optional, for the conformance check
python3 conformance_check.py
```

## Verification

- `test_server.py`: 11/11 unit tests pass, including end-to-end HTTP transport checks.
- `conformance_check.py`: 14/14 checks pass when run with the optional official MCP SDK.
- A clean isolated installation resolves as `freellm-watch-mcp 1.1.0`; the installed
  `freellm-mcp` entry point completes a negotiated JSON-RPC initialization handshake.
- Runtime dependencies: none.

## Repository Structure

```text
freellm-mcp/
├── server.py                  # MCP server implementation
├── test_server.py             # unit tests
├── conformance_check.py       # official SDK conformance check
├── README.md                  # this documentation
├── pyproject.toml             # package metadata and entry point
├── registry.json              # example agent configuration
├── .gitignore                 # generated paths
└── LICENSE                    # MIT license
```