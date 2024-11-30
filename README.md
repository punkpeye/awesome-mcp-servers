# Awesome MCP Servers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of awesome Model Context Protocol (MCP) servers.

* [What is MCP?](#what-is-mcp)
* [Tutorials](#tutorials)
* [Server Implementations](#server-implementations)
* [Frameworks](#frameworks)

## What is MCP?

[MCP](https://modelcontextprotocol.io/) is an open protocol that enables AI models to securely interact with local and remote resources through standardized server implementations. This list focuses on production-ready and experimental MCP servers that extend AI capabilities through file access, database connections, API integrations, and other contextual services.

## Tutorials

* [Model Context Protocol (MCP) Quickstart](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)

## Server Implementations

* 📂 - [Browser Automation](#browser-automation)
* ☁️ - [Cloud Platforms](#cloud-platforms)
* 💬 - [Communication](#communication)
* 🗄️ - [Databases](#databases)
* 📂 - [File Systems](#file-systems)
* 🧠 - [Knowledge & Memory](#knowledge--memory)
* 🗺️ - [Location Services](#location-services)
* 📊 - [Monitoring](#monitoring)
* 🔎 - [Search](#search)
* 🔄 - [Version Control](#version-control)
* 🛠️ - [Other Tools and Integrations](#other-tools-and-integrations)

### 📂 <a name="browser-automation"></a>Browser Automation <sup>[top⇈](#server-implementations)</sup>

> Web content access and automation capabilities. Enables searching, scraping, and processing web content in AI-friendly formats.
- [@modelcontextprotocol/server-puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) - Browser automation for web scraping and interaction


### ☁️ <a name="cloud-platforms"></a>Cloud Platforms <sup>[top⇈](#server-implementations)</sup>

> Cloud platform service integration. Enables management and interaction with cloud infrastructure and services.

- [Cloudflare MCP Server](https://github.com/cloudflare/mcp-server-cloudflare) - Integration with Cloudflare services including Workers, KV, R2, and D1

<br />

### 💬 <a name="communication"></a>Communication <sup>[top⇈](#server-implementations)</sup>

> Integration with communication platforms for message management and channel operations. Enables AI models to interact with team communication tools.

- [@modelcontextprotocol/server-slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack) - Slack workspace integration for channel management and messaging

<br />

### 🗄️ <a name="databases"></a>Databases <sup>[top⇈](#server-implementations)</sup>

> Secure database access with schema inspection capabilities. Enables querying and analyzing data while maintaining read-only safety by default.

- [@modelcontextprotocol/server-postgres](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) - PostgreSQL database integration with schema inspection and query capabilities
- [@modelcontextprotocol/server-sqlite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) - SQLite database operations with built-in analysis features

<br />

### 📂 <a name="file-systems"></a>File Systems <sup>[top⇈](#server-implementations)</sup>

> Provides direct access to local file systems with configurable permissions. Enables AI models to read, write, and manage files within specified directories.

- [@modelcontextprotocol/server-filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) - Direct local file system access.
- [mark3labs/mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server) - Golang implementation for local file system access.

<br />

## 🧠 <a name="knowledge--memory"></a>Knowledge & Memory <sup>[top⇈](#server-implementations)</sup>

> Persistent memory storage using knowledge graph structures. Enables AI models to maintain and query structured information across sessions.
- [@modelcontextprotocol/server-memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) - Knowledge graph-based persistent memory system for maintaining context

<br />

### 🗺️ <a name="location-services"></a>Location Services <sup>[top⇈](#server-implementations)</sup>

> Geographic and location-based services integration. Enables access to mapping data, directions, and place information.

- [@modelcontextprotocol/server-google-maps](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps) - Google Maps integration for location services, routing, and place details


<br />

### 📊 <a name="monitoring"></a>Monitoring <sup>[top⇈](#server-implementations)</sup>

> Access and analyze application monitoring data. Enables AI models to review error reports and performance metrics.

- [@modelcontextprotocol/server-sentry](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry) - Sentry.io integration for error tracking and performance monitoring

<br />

## 🔎 <a name="search"></a>Search <sup>[top⇈](#server-implementations)</sup>
> Web search capabilities.

- [@modelcontextprotocol/server-brave-search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) - Web search capabilities using Brave's Search API
- [@modelcontextprotocol/server-fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) - Efficient web content fetching and processing for AI consumption
- [ac3xx/mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi) - Kagi search API integration
- [theishangoswami/exa-mcp-server](https://github.com/theishangoswami/exa-mcp-server) - Exa AI Search API


<br />

### 🔄 <a name="version-control"></a>Version Control <sup>[top⇈](#server-implementations)</sup>

> Interact with Git repositories and version control platforms. Enables repository management, code analysis, pull request handling, issue tracking, and other version control operations through standardized APIs.

- [@modelcontextprotocol/server-github](https://github.com/modelcontextprotocol/servers/tree/main/src/github) - GitHub API integration for repository management, PRs, issues, and more
- [@modelcontextprotocol/server-gitlab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab) - GitLab platform integration for project management and CI/CD operations
- [@modelcontextprotocol/server-git](https://github.com/modelcontextprotocol/servers/tree/main/src/git) - Direct Git repository operations including reading, searching, and analyzing local repositories

<br />


### 🛠️ <a name="other-tools-and-integrations"></a>Other Tools and Integrations <sup>[top⇈](#server-implementations)</sup>

- [pierrebrunelle/mcp-server-openai](https://github.com/pierrebrunelle/mcp-server-openai) - Query OpenAI models directly from Claude using MCP protocol
- [baba786/phabricator-mcp-server](https://github.com/baba786/phabricator-mcp-server) - Interacting with Phabricator API
- [MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) - Interacting with Obsidian via REST API
- [anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube) - Fetch YouTube subtitles
- [danhilse/notion_mcp](https://github.com/danhilse/notion_mcp) - Integrates with Notion's API to manage personal todo lists

## Frameworks

- [Genkit MCP](https://github.com/firebase/genkit/tree/main/js/plugins/mcp) – Provides integration between [Genkit](https://github.com/firebase/genkit/tree/main) and the Model Context Protocol (MCP).
