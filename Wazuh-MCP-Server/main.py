#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
Blue Team Wazuh MCP Server - entry point.
Startup order (must not be reordered):
1. Parse CLI args, set MCP_HOST / MCP_PORT env vars.
2. Import mcp_server - triggers FastMCP creation + init_config().
3. init_auth_manager() - initialize JWT token manager singleton.
4. register_all_tools() - import tool modules; gating is enforced here.
5. mcp.run() - start the selected transport.
"""

import argparse
import ipaddress
import os
import sys


def _is_loopback(host: str) -> bool:
    """True if host is a loopback address (safe to serve unauthenticated)."""
    try:
        return ipaddress.ip_address(host).is_loopback
    except ValueError:
        return host.lower() in ("localhost", "127.0.0.1", "::1")


def _start_http_transport(host: str, port: int, log_level: str) -> None:
    """Start streamable-http, enforcing the inbound auth bind guard.
    Refuse a non-loopback bind without a configured MCP_API_KEY. When a key is
    configured, auth is enforced on every request (loopback included).
    """
    from mcp_server import mcp
    from mcp_server.core.exceptions import ConfigurationError
    from mcp_server.core.server_auth import auth_manager, serve_authenticated

    if not _is_loopback(host) and not auth_manager.configured:
        raise ConfigurationError(
            f"Refusing to bind HTTP transport to non-loopback address '{host}' "
            "without a configured MCP_API_KEY. Generate one with:\n"
            "python3 -c \"import secrets; print('btm_' + secrets.token_urlsafe(32))\"\n"
            "then set MCP_API_KEY (MCP_API_KEY_SCOPES='wazuh:read wazuh:write'), "
            "or bind to 127.0.0.1."
        )
    serve_authenticated(mcp, host, port, log_level=log_level)


def main() -> None:
    # 1: CLI args (before FastMCP construction)
    parser = argparse.ArgumentParser(
        description="blue_team_mcp - SOC automation MCP server for Wazuh"
    )
    parser.add_argument(
        "--transport", choices=["stdio", "streamable_http", "http"],
        default=os.environ.get("MCP_TRANSPORT", "stdio"),
    )
    parser.add_argument("--host", default=os.environ.get("MCP_HOST", "127.0.0.1"))
    parser.add_argument("--port", type=int, default=int(os.environ.get("MCP_PORT", "8000")))
    args = parser.parse_args()

    os.environ["MCP_HOST"] = args.host
    os.environ["MCP_PORT"] = str(args.port)

    # 2: Import mcp_server - triggers FastMCP creation + init_config() in __init__.py
    from mcp_server import mcp, logger

    # 3: Initialize Wazuh auth manager singleton
    from mcp_server.core.config import config
    from mcp_server.wazuh.auth import init_auth_manager
    if config is not None:
        init_auth_manager(
            url=config.wazuh_manager.url,
            username=config.wazuh_manager.username,
            password=config.wazuh_manager.password,
            verify_ssl=config.wazuh_manager.verify_ssl,
        )

    # 4: Register tools
    from mcp_server.tools import register_all_tools
    register_all_tools()

    # 5: Start transport
    tool_count = len(getattr(mcp._tool_manager, "_tools", {}))
    logger.info("%d tools registered. Starting %s transport on %s:%s",
                tool_count, args.transport, args.host, args.port)

    if args.transport in ("streamable_http", "http"):
        _start_http_transport(args.host, args.port, config.server.log_level if config else "INFO")
    else:
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
