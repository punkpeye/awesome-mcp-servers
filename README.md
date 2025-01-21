# Awesome MCP Servers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of awesome Model Context Protocol (MCP) servers.

* [What is MCP?](#what-is-mcp)
* [Tutorials](#tutorials)
* [Server Implementations](#server-implementations)
* [Frameworks](#frameworks)
* [Tips & Tricks](#tips-and-tricks)

## What is MCP?

[MCP](https://modelcontextprotocol.io/) is an open protocol that enables AI models to securely interact with local and remote resources through standardized server implementations. This list focuses on production-ready and experimental MCP servers that extend AI capabilities through file access, database connections, API integrations, and other contextual services.

## Tutorials

* [Model Context Protocol (MCP) Quickstart](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
* [Setup Claude Desktop App to Use a SQLite Database](https://youtu.be/wxCCzo9dGj0)

## Community

* [Discord Server](https://discord.gg/TFE8FmjCdS)

## Legend

* – official implementation
* – Python codebase
* – TypeScript codebase
* – Go codebase
* - Cloud Service
* - Local Service

## Server Implementations

* - [Browser Automation](#browser-automation)
* - [Cloud Platforms](#cloud-platforms)
* - [Communication](#communication)
* - [Customer Data Platforms](#customer-data-platforms)
* - [Databases](#databases)
* - [File Systems](#file-systems)
* - [Knowledge & Memory](#knowledge--memory)
* - [Location Services](#location-services)
* - [Monitoring](#monitoring)
* - [Search](#search)
* - [Travel & Transportation](#travel-and-transportation)
* - [Version Control](#version-control)
* - [Other Tools and Integrations](#other-tools-and-integrations)

### - <a name="browser-automation"></a>Browser Automation

Web content access and automation capabilities. Enables searching, scraping, and processing web content in AI-friendly formats.
- [@executeautomation/playwright-mcp-server](https://github.com/executeautomation/mcp-playwright) - An MCP server using Playwright for browser automation and webscrapping
- [@automatalabs/mcp-server-playwright](https://github.com/Automata-Labs-team/MCP-Server-Playwright) - An MCP server for browser automation using Playwright 
- [@modelcontextprotocol/server-puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) - Browser automation for web scraping and interaction
- [@kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) - Fetch YouTube subtitles and transcripts for AI analysis

### - <a name="cloud-platforms"></a>Cloud Platforms

Cloud platform service integration. Enables management and interaction with cloud infrastructure and services.

- [Cloudflare MCP Server](https://github.com/cloudflare/mcp-server-cloudflare) - Integration with Cloudflare services including Workers, KV, R2, and D1
- [Kubernetes MCP Server](https://github.com/strowk/mcp-k8s-go) - Kubernetes cluster operations through MCP

### - <a name="communication"></a>Communication

Integration with communication platforms for message management and channel operations. Enables AI models to interact with team communication tools.

- [@modelcontextprotocol/server-slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack) - Slack workspace integration for channel management and messaging
- [@modelcontextprotocol/server-bluesky](https://github.com/keturiosakys/bluesky-context-server) - Bluesky instance integration for querying and interaction
- [MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite) - Integration with gmail and Google Calendar. 

### - <a name="customer-data-platforms"></a>Customer Data Platforms

Provides access to customer profiles inside of customer data platforms

- [sergehuber/inoyu-mcp-unomi-server](https://github.com/sergehuber/inoyu-mcp-unomi-server) - An MCP server to access and updates profiles on an Apache Unomi CDP server.

### - <a name="databases"></a>Databases

Secure database access with schema inspection capabilities. Enables querying and analyzing data with configurable security controls including read-only access.

- [LucasHild/mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery) - BigQuery database integration with schema inspection and query capabilities
- [ergut/mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server) - Server implementation for Google BigQuery integration that enables direct BigQuery database access and querying capabilities
- [designcomputer/mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server) - MySQL database integration with configurable access controls, schema inspection, and comprehensive security guidelines
- [@modelcontextprotocol/server-postgres](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) - PostgreSQL database integration with schema inspection and query capabilities
- [@modelcontextprotocol/server-sqlite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) - SQLite database operations with built-in analysis features
- [ktanaka101/mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb) - DuckDB database integration with schema inspection and query capabilities

### - <a name="file-systems"></a>File Systems

Provides direct access to local file systems with configurable permissions. Enables AI models to read, write, and manage files within specified directories.

- [@modelcontextprotocol/server-filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) - Direct local file system access.
- [@modelcontextprotocol/server-google-drive](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive) - Google Drive integration for listing, reading, and searching files
- [mark3labs/mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server) - Golang implementation for local file system access.

### - <a name="knowledge--memory"></a>Knowledge & Memory

Persistent memory storage using knowledge graph structures. Enables AI models to maintain and query structured information across sessions.
- [@modelcontextprotocol/server-memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) - Knowledge graph-based persistent memory system for maintaining context

### - <a name="location-services"></a>Location Services

Geographic and location-based services integration. Enables access to mapping data, directions, and place information.

- [@modelcontextprotocol/server-google-maps](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps) - Google Maps integration for location services, routing, and place details

### - <a name="monitoring"></a>Monitoring

Access and analyze application monitoring data. Enables AI models to review error reports and performance metrics.

- [@modelcontextprotocol/server-sentry](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry) - Sentry.io integration for error tracking and performance monitoring
- [@modelcontextprotocol/server-raygun](https://github.com/MindscapeHQ/mcp-server-raygun) - Raygun API V3 integration for crash reporting and real user monitoring

### - <a name="search"></a>Search

- [@modelcontextprotocol/server-brave-search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) - Web search capabilities using Brave's Search API
- [@angheljf/nyt](https://github.com/angheljf/nyt) - Search articles using the NYTimes API
- [@modelcontextprotocol/server-fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) - Efficient web content fetching and processing for AI consumption
- [ac3xx/mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi) - Kagi search API integration
- [theishangoswami/exa-mcp-server](https://github.com/theishangoswami/exa-mcp-server) - Exa AI Search API
- [exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) – A Model Context Protocol (MCP) server lets AI assistants like Claude use the Exa AI Search API for web searches. This setup allows AI models to get real-time web information in a safe and controlled way.
- [fatwang2/search1api-mcp](https://github.com/fatwang2/search1api-mcp) - Search via search1api (requires paid API key)
- [Tomatio13/mcp-server-tavily](https://github.com/Tomatio13/mcp-server-tavily) – Tavily AI search API
- [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) - Search ArXiv research papers
- [DeepSeek MCP Server](https://www.npmjs.com/package/deepseek-mcp-server) - MCP server for DeepSeek's powerful language models, including the R1 model. Provides chat completion capabilities with configurable parameters.

### - <a name="travel-and-transportation"></a>Travel & Transportation

Access to travel and transportation information. Enables querying schedules, routes, and real-time travel data.

- [NS Travel Information MCP Server](https://github.com/r-huijts/ns-mcp-server) - Access Dutch Railways (NS) travel information, schedules, and real-time updates

### - <a name="version-control"></a>Version Control

Interact with Git repositories and version control platforms. Enables repository management, code analysis, pull request handling, issue tracking, and other version control operations through standardized APIs.

- [@modelcontextprotocol/server-github](https://github.com/modelcontextprotocol/servers/tree/main/src/github) - GitHub API integration for repository management, PRs, issues, and more
- [@modelcontextprotocol/server-gitlab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab) - GitLab platform integration for project management and CI/CD operations
- [@modelcontextprotocol/server-git](https://github.com/modelcontextprotocol/servers/tree/main/src/git) - Direct Git repository operations including reading, searching, and analyzing local repositories

### - <a name="other-tools-and-integrations"></a>Other Tools and Integrations

- [pierrebrunelle/mcp-server-openai](https://github.com/pierrebrunelle/mcp-server-openai) - Query OpenAI models directly from Claude using MCP protocol
- [@modelcontextprotocol/server-everything](https://github.com/modelcontextprotocol/servers/tree/main/src/everything) - MCP server that exercises all the features of the MCP protocol
- [baba786/phabricator-mcp-server](https://github.com/baba786/phabricator-mcp-server) - Interacting with Phabricator API
- [MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) - Interacting with Obsidian via REST API
- [calclavia/mcp-obsidian](https://github.com/calclavia/mcp-obsidian) - This is a connector to allow Claude Desktop (or any MCP client) to read and search any directory containing Markdown notes (such as an Obsidian vault).
- [anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube) - Fetch YouTube subtitles
- [danhilse/notion_mcp](https://github.com/danhilse/notion_mcp) - Integrates with Notion's API to manage personal todo lists
- [rusiaaman/wcgw](https://github.com/rusiaaman/wcgw/blob/main/src/wcgw/client/mcp_server/Readme.md) - Autonomous shell execution, computer control and coding agent. (Mac)
- [reeeeemo/ancestry-mcp](https://github.com/reeeeemo/ancestry-mcp) - Allows the AI to read .ged files and genetic data
- [sirmews/apple-notes-mcp](https://github.com/sirmews/apple-notes-mcp) - Allows the AI to read from your local Apple Notes database (macOS only)
- [anjor/coinmarket-mcp-server](https://github.com/anjor/coinmarket-mcp-server) - Coinmarket API integration to fetch cryptocurrency listings and quotes
- [suekou/mcp-notion-server](https://github.com/suekou/mcp-notion-server) - Interacting with Notion API
- [amidabuddha/unichat-mcp-server](https://github.com/amidabuddha/unichat-mcp-server) - Send requests to OpenAI, MistralAI, Anthropic, xAI, or Google AI using MCP protocol via tool or predefined prompts. Vendor API key required
- [g0t4/mcp-server-commands](https://github.com/g0t4/mcp-server-commands) - Run commands and include their output. Tools and Prompts.
- [evalstate/mcp-miro](https://github.com/evalstate/mcp-miro) - Access MIRO whiteboards, bulk create and read items. Requires OAUTH key for REST API.
- [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) - Natural language search and content access for Confluence workspaces
- [pyroprompts/any-chat-completions-mcp](https://github.com/pyroprompts/any-chat-completions-mcp) - Chat with any other OpenAI SDK Compatible Chat Completions API, like Perplexity, Groq, xAI and more
- [anaisbetts/mcp-installer](https://github.com/anaisbetts/mcp-installer) -  An MCP server that installs other MCP servers for you.

## Frameworks

- [Genkit MCP](https://github.com/firebase/genkit/tree/main/js/plugins/mcp) – Provides integration between [Genkit](https://github.com/firebase/genkit/tree/main) and the Model Context Protocol (MCP).
- [@modelcontextprotocol/server-langchain](https://github.com/rectalogic/langchain-mcp) - Provides MCP tool calling support in LangChain, allowing for the integration of MCP tools into LangChain workflows.
- [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go) - Golang SDK for building MCP Servers and Clients.
- [FastMCP](https://github.com/jlowin/fastmcp) - A high-level framework for building MCP servers in Python
- [mcp-rs-template](https://github.com/linux-china/mcp-rs-template) - MCP CLI server template for Rust

## Clients

- [SecretiveShell/MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge) an openAI middleware proxy to use mcp in any existing openAI compatible client
- [zed-industries/zed](https://github.com/zed-industries/zed) multiplayer code editor from the creators of atom
- [firebase/genkit](https://github.com/firebase/genkit) agent and data transformation framework
- [continuedev/continue](https://github.com/continuedev/continue) vscode auto complete and chat tool (full feature support)

## Tips and Tricks

### Official prompt to inform LLMs how to use MCP

Want to ask Claude about Model Context Protocol?

Create a Project, then add this file to it:

https://modelcontextprotocol.io/llms-full.txt

Now Claude can answer questions about writing MCP servers and how they work

- https://www.reddit.com/r/ClaudeAI/comments/1h3g01r/want_to_ask_claude_about_model_context_protocol/

## Star History

<a href="https://star-history.com/#punkpeye/awesome-mcp-servers&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date" />
 </picture>
</a>
