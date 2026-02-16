# Awesome MCP Servers ![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)

A curated list of awesome Model Context Protocol (MCP) servers. MCP is an open protocol that enables AI models to securely interact with local and remote resources through standardized server implementations. This list focuses on production-ready and experimental MCP servers that extend AI capabilities through file access, database connections, API integrations, and other contextual services.

<br />

## ⚠️ Security Warning

> [!WARNING]
>  When running MCP servers without proper sandboxing, they can execute arbitrary code on your system with the same permissions as the host process. This creates significant security risks.
>
> **Security Risks:**
> - **System Access**: Full access to files, network, and system resources
> - **Code Execution**: Can run any command on your machine
> - **Prompt Injection**: Malicious prompts could trigger unintended server actions
> - **Data Exposure**: Sensitive data may be accessed or leaked
>
> **Best Practices:**
> - Use official implementations (marked with ⭐) when available
> - Run servers in VMs or isolated environments
> - Review code before installation
> - Limit permissions to minimum required
> - Monitor server activity

<br />

## Examples of Supported Clients

|                                                                                                                                                                                          | MCP Host                                                                    | Documentation                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| [<div align="center"><img src="https://github.com/user-attachments/assets/b0ea1e57-df16-4b04-9276-1980e17ab6ec" height="20"/></div>](https://www.claudedesktop.com/)                                                                       | [Claude Desktop](https://claude.ai)                            | [Claude x MCP](https://modelcontextprotocol.io/quickstart)                                           |
| [<div align="center"><img src="https://zed.dev/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo_icon.d67dc948.webp&w=64&q=100" height="20"/></div>](https://zed.dev/)                                                          | [Zed Editor](https://zed.dev/)                                              | [Zed x MCP](https://zed.dev/blog/mcp)                                                      |
| [<div align="center"><img src="https://storage.googleapis.com/sourcegraph-assets/docs/images/cody/cody-logomark-default.svg" height="20"/></div>](https://sourcegraph.com/cody)          | [Sourcegraph Cody](https://sourcegraph.com/cody)                            | [Cody x MCP](https://sourcegraph.com/blog/cody-supports-anthropic-model-context-protocol) |
| [<div align="center"><img src="https://cdn.prod.website-files.com/663e06c56841363663ffbbcf/664c918ec47bacdd3acdc167_favicon%408x.png" height="20"/></div>](https://sourcegraph.com/cody) | [Continue](https://www.continue.dev/)                                       | [Continue x MCP](https://blog.continue.dev/model-context-protocol)                                  |
| [<div align="center"><img src="https://github.com/user-attachments/assets/211d0c2b-04de-471e-b1ed-97da94a58d82" height="20"/></div>](https://github.com/Upsonic/gpt-computer-assistant)  | [GPT Computer Assistant](https://github.com/Upsonic/gpt-computer-assistant) | [GCA x MCP](https://github.com/Upsonic/gpt-computer-assistant)                                      |
| [<div align="center"><img src="https://raw.githubusercontent.com/danny-avila/LibreChat/0855677a36d76cafa5e064b7e346eb3f74c6af2a/client/public/assets/logo.svg" height="20"/></div>](https://www.librechat.ai/) | [LibreChat](https://www.librechat.ai/) | [LibreChat Agents x MCP](https://www.librechat.ai/docs/features/agents#model-context-protocol-mcp) |
| [<div align="center"><img src="https://cursor.com/favicon.ico" height="20"/></div>](https://www.cursor.com/) | [Cursor](https://www.cursor.com/) | [Cursor x MCP](https://docs.cursor.com/advanced/model-context-protocol) |
| [<div align="center"><img src="https://www.enconvo.com/favicon.ico" height="20"/></div>](https://www.enconvo.com/) | [Enconvo](https://www.enconvo.com/) | [Enconvo x MCP](https://docs.enconvo.com/docs/features/model-context-protocol) |
| [<div align="center"><img src="https://block.github.io/goose/img/logo_light.png" height="20"/></div>](https://block.github.io/goose/) | [Goose](https://block.github.io/goose/) | [Goose x MCP](https://block.github.io/goose/docs/getting-started/using-extensions) | 
| [<div align="center"><img src="https://raw.githubusercontent.com/evilsocket/search/refs/heads/main/logo.png" height="20"/></div>](https://github.com/evilsocket/nerve) | [Nerve](https://github.com/evilsocket/nerve) | [Nerve x MCP](https://github.com/evilsocket/nerve/blob/main/docs/index.md#%EF%B8%8F-adding-tools) | 
| [<div align="center"><img src="https://raw.githubusercontent.com/mcp-router/mcp-router/refs/heads/main/static/img/logo.svg" height="20"/></div>](https://mcp-router.net) | [MCP Router](https://github.com/mcp-router/mcp-router) | [MCP Router x MCP](https://mcp-router.net) |
| [<div align="center"><img src="https://raw.githubusercontent.com/pietrozullo/mcp-use/refs/heads/main/docs/favicon.svg" height="20"/></div>](https://github.com/pietrozullo/mcp-use) | [mcp-use](https://github.com/pietrozullo/mcp-use) | [mcp-use x MCP](https://docs.mcp-use.io/introduction) |
| [<div align="center"><img src="https://wassist.app/whatsmcp.png" height="20"/></div>](https://wassist.app/mcp/) | [WhatsMCP](https://wassist.app/mcp/) | [WhatsApp x MCP](https://wassist.app/mcp/) |
| [<div align="center"><img src="https://github.com/user-attachments/assets/7d5442e5-4542-4942-afde-a55d5288a40c" height="20"/></div>](https://code.visualstudio.com/) | [Visual Studio Code](https://code.visualstudio.com/) | [VS Code x MCP](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) |

<br />

## Server Implementations

- 📂 - [File Systems](#file-systems)
- 📦 - [Sandbox & Virtualization](#virtualization)
- 🔄 - [Version Control](#version-control)
- ☁️ - [Cloud Storage](#cloud-storage)
- 🗄️ - [Databases](#databases)
- 💬 - [Communication](#communication)
- 📈 - [Monitoring](#monitoring)
- 🔍 - [Search & Web](#search-web)
- 🗺️ - [Location Services](#location-services)
- 🎯 - [Marketing](#marketing)
- 📝 - [Note Taking](#note-taking)
- ⚡ - [Cloud Platforms](#cloud-platforms)
- ⚙️ - [Workflow Automation](#workflow-automation)
- 🤖 - [System Automation](#system-automation)
- 📱 - [Social Media](#social-media)
- 🎮 - [Gaming](#gaming)
- 💹 - [Finance](#finance)
- 🧬 - [Research & Data](#research-data)
- 🤝 - [AI Services](#ai-services)
- 💻 - [Development Tools](#development-tools)
- 📊 - [Data Visualization](#data-visualization)
- 🆔 - [Identity](#identity)
- 🔗 - [Aggregators](#aggregators)
- 💬 - [Language & Translation](#language)
- 🔒 - [Security](#security)
- 🔌 - [IoT](#iot)
- 🧑‍🎨 - [Art & Literature](#art-literature)
- 🛒 - [E-Commerce](#e-commerce)
- 📦 - [Data Platforms](#data-platforms)
- 🤖 - [Robotics & Physical AI](#robotics)

<sup><details>

<summary>Legend</summary>

- <sup>⭐</sup> Official protocol implementation
- <sup>1</sup> First implementation (when multiple implementations exist)
- <sup>2</sup> Second implementation
- <sup>3</sup> Third implementation
- <sup>n</sup> Subsequent implementations
</details></sup>

<br />

## Tools & Utilities

See [Helpful Tools & Utilities](#helpful-tools-&-utilities) section for tools to help manage, configure, and work with MCP servers.

<br />

## 📂 <a name="file-systems"></a>File Systems

> Provides direct access to local file systems with configurable permissions. Enables AI models to read, write, and manage files within specified directories.
- <img src="https://cdn.simpleicons.org/files/4CAF50" height="14"/> [Backup](https://github.com/hexitex/MCP-Backup-Server) - Provides file and folder backup and restoration capabilities for AI agents and code editing tools
- <img src="https://cdn.simpleicons.org/files/9AD1ED" height="14"/> [FileStash](https://github.com/mickael-kerjean/filestash/tree/master/server/plugin/plg_handler_mcp) - Remote Storage Access: SFTP, S3, FTP, SMB, NFS, WebDAV, GIT, FTPS, gcloud, azure blob, sharepoint, etc... 
- <img src="https://cdn.simpleicons.org/files/2196F3" height="14"/> [FileSystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)<sup><sup>1</sup></sup> - Direct local file system access
- <img src="https://cdn.simpleicons.org/files/4A90E2" height="14"/> [FileSystem](https://github.com/mark3labs/mcp-filesystem-server)<sup><sup>2</sup></sup> - Golang implementation for local file system access
- <img src="https://cdn.simpleicons.org/files/4CAF50" height="14"/> [Everything Search](https://github.com/mamertofabian/mcp-everything-search) - Lightning-fast Windows file search powered by Everything SDK
- <img src="https://cdn.simpleicons.org/files/4CAF50" height="14"/> [fast-filesystem-mcp](https://github.com/efforthye/fast-filesystem-mcp) - Advanced filesystem operations with large file handling capabilities and Claude-optimized features. Provides fast file reading/writing, sequential reading for large files, directory operations, file search, and streaming writes with backup & recovery.
- <img src="https://cdn.simpleicons.org/files/4CAF50" height="14"/> [llm-context](https://github.com/cyberchitta/llm-context.py) - Share code context with LLMs via Model Context Protocol or clipboard

<br />

## 📦 <a name="virtualization"></a>Sandbox & Virtualization

> Secure sandbox environments for code execution and testing. Enables safe execution of code snippets and development workflows.

- <img src="https://docs.microsandbox.dev/favicon.ico" height="14"/> [Microsandbox](https://github.com/microsandbox/microsandbox)<sup><sup>⭐</sup></sup> - Self-hosted platform for secure execution of AI code. Great for Code Interpreter, Data Analysis, Browser Use.
- <img src="https://e2b.dev/favicon.ico" height="14"/> [E2B](https://github.com/e2b-dev/mcp-server)<sup><sup>⭐</sup></sup> - Secure cloud development environments for AI agents. Enables safe code execution and testing in isolated containers.
- <img src="https://cdn.simpleicons.org/docker/0db7ed" height="14"/> [Docker](https://github.com/QuantGeekDev/docker-mcp) - An MCP server for Docker operations, enabling seamless container and compose stack management.

<br />

## 🔄 <a name="version-control"></a>Version Control

> Interact with Git repositories and version control platforms. Enables repository management, code analysis, pull request handling, issue tracking, and other version control operations through standardized APIs.

- <img src="https://cdn.simpleicons.org/github/8A8A8A" height="14"/> [GitHub](https://github.com/github/github-mcp-server)<sup><sup>1</sup></sup> - GitHub API integration for repository management, PRs, issues, and more
- <img src="https://cdn.simpleicons.org/github/8A8A8A" height="14"/> [GitHub](https://github.com/kurdin/github-repos-manager-mcp)<sup><sup>2</sup></sup> - Token-based GitHub automation management. No Docker for optimal performance, Flexible configuration for fine-grained control, 80+ tools with direct API integration.
- <img src="https://cdn.simpleicons.org/gitlab/FC6D26" height="14"/> [GitLab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab) - GitLab platform integration for project management and CI/CD operations
- <img src="https://cdn.simpleicons.org/git/F05032" height="14"/> [Git](https://github.com/modelcontextprotocol/servers/tree/main/src/git) - Direct Git repository operations including reading, searching, and analyzing local repositories
- <img src="https://cdn.simpleicons.org/phabricator/5865F2" height="14"/> [Phabricator](https://github.com/baba786/phabricator-mcp-server) - Phabricator API integration for repository and project management
- <img src="https://cdn.simpleicons.org/git/F05032" height="14"/> [Gitingest-MCP](https://github.com/puravparab/Gitingest-MCP) - Gitingest integration providing prompt friendly summmaries of Github repos


<br />

## ☁ <a name="cloud-storage"></a>Cloud Storage

> Access and manage files stored in cloud storage platforms. Enables searching, reading, and organizing cloud-stored documents and data.

- <img src="https://cdn.simpleicons.org/googledrive/4285F4" height="14"/> [Google Drive](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive) - Google Drive integration for file access, search, and management
- <img src="https://www.box.com/themes/custom/box/favicons/favicon.ico" height="14"/> [Box](https://developer.box.com/guides/box-mcp/)<sup><sup>⭐</sup></sup> - Box MCP Server allows third party AI agents from platforms like Copilot Studio, Cursor, Claude for Desktop to access Box content seamlessly. It extends the agent's capabilities by allowing it to perform actions related to content stored in Box.
- <img src="https://framerusercontent.com/images/ijlYG00LOcMD6zR1XLMxHbAwZkM.png" height="14" /> [VideoDB](https://github.com/video-db/agent-toolkit/tree/main/modelcontextprotocol)<sup><sup>⭐</sup></sup> - A serverless video database to easily store, index, search, and stream videos. VideoDB uses AI to automatically tag scenes, generate accurate transcriptions, and quickly retrieve video moments with simple queries.
- <img src="https://www.microsoft.com/favicon.ico" height="14"/> [Microsoft 365](https://github.com/softeria/ms-365-mcp-server) - MCP server that connects to the whole Microsoft 365 suite (Microsoft Office, Outlook, etc.) using Graph API (including mail, files, Excel, calendar)

<br />

## 🗄️ <a name="databases"></a>Databases

> Secure database access with schema inspection capabilities. Enables querying and analyzing data while maintaining read-only safety by default.

- <img src="https://cdn.simpleicons.org/postgresql/5865F2" height="14"/> [PostgreSQL](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) - PostgreSQL database integration with schema inspection and query capabilities
- <img src="https://cdn.simpleicons.org/sqlite/0F80CC" height="14"/> [SQLite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) - SQLite database operations with built-in analysis features
- <img src="https://cdn.simpleicons.org/duckdb/FDC000" height="14"/> [DuckDB](https://github.com/ktanaka101/mcp-server-duckdb) - DuckDB database integration with schema inspection and query capabilities
- <img src="https://cdn.simpleicons.org/libreoffice/18A303" height="14"/> [Excel](https://github.com/haris-musa/excel-mcp-server) - Excel workbook manipulation including data reading/writing, worksheet management, formatting, charts, and pivot tables
- <img src="https://cdn.simpleicons.org/googlebigquery/669DF6" height="14"/> [BigQuery](https://github.com/LucasHild/mcp-server-bigquery)<sup><sup>1</sup></sup> - BigQuery database integration with schema inspection and query capabilities
- <img src="https://cdn.simpleicons.org/googlebigquery/669DF6" height="14"/> [BigQuery](https://github.com/ergut/mcp-bigquery-server)<sup><sup>2</sup></sup> - A BigQuery MCP server for read-only SQL queries and schema exploration (available on npm)
- <img src="https://neon.tech/favicon.ico" height="14"/> [Neon](https://github.com/neondatabase/mcp-server-neon)<sup><sup>⭐</sup></sup> - Neon MCP Server. Allows natural language interactions with Neon for database management.
- <img src="https://qdrant.tech/img/brand-resources-logos/logomark.svg" height="14"/> [Qdrant](https://github.com/qdrant/mcp-server-qdrant/)<sup><sup>⭐</sup></sup> - A Qdrant MCP server for keeping and retrieving memories in the Qdrant vector search engine.
- <img src="https://cdn.simpleicons.org/mongodb/47A248" height="14"/> [MongoDB](https://github.com/kiliczsh/mcp-mongo-server) - A Model Context Protocol Server for querying and analyzing MongoDB collections.
- <img src="https://cdn.simpleicons.org/mongodb/47A248" height="14"/> [MongoDB Lens](https://github.com/furey/mongodb-lens) - Full featured MCP Server for MongoDB databases.
- <img src="https://cdn.simpleicons.org/mysql" height="14"/> [MySQL](https://github.com/designcomputer/mysql_mcp_server) - MySQL database integration with configurable access controls and schema inspection
- <img src="https://cdn.simpleicons.org/airtable" height="14"/> [Airtable](https://github.com/domdomegg/airtable-mcp-server) - Read and write access to Airtable databases, with schema inspection.
- <img src="https://cdn.simpleicons.org/snowflake" height="14"/> [Snowflake](https://github.com/isaacwasserman/mcp-snowflake-server) - Snowflake database integration with read/write capabilities and insight tracking.
- <img src="https://jiejue.obs.ap-southeast-1.myhuaweicloud.com/20250209205317622.webp" height="14"/> [DBUtils](https://github.com/donghao1393/mcp-dbutils) - A unified database access service for MCP that seamlessly integrates PostgreSQL and SQLite with a clean abstraction layer.
- <img src="https://www.pingcap.com/favicon.ico" height="14"/> [TiDB](https://github.com/c4pt0r/mcp-server-tidb) - MCP server implementation for TiDB (serverless) database.
- <img src="https://cdn.nocodb.com/marketing-site/20250120104552/images/favicon.png" height="14"/> [NocoDB](https://github.com/edwinbernadus/nocodb-mcp-server) - Read and write access to NocoDB database.
- <img src="https://www.couchbase.com/wp-content/uploads/2023/10/couchbase-favicon.svg" height="14"/> [Couchbase](https://github.com/Couchbase-Ecosystem/mcp-server-couchbase)<sup><sup>⭐</sup></sup> - MCP server to interact with the data stored in Couchbase clusters including natural language querying. 
- <img src="https://avatars.githubusercontent.com/u/1529926?s=48&v=4" height="14"/> [Redis](https://github.com/redis/mcp-redis)<sup><sup>⭐</sup></sup> - A natural language interface designed for agentic applications to efficiently manage and search data in Redis.
- <img src="https://framerusercontent.com/images/ijlYG00LOcMD6zR1XLMxHbAwZkM.png" height="14" /> [VideoDB Director](https://github.com/video-db/agent-toolkit/tree/main/modelcontextprotocol)<sup><sup>⭐</sup></sup> - Create AI-powered video workflows including automatic editing, content moderation, voice cloning, highlight generation, and searchable video moments—all accessible via simple APIs and intuitive chat-based interfaces.

<br />

## 💬 <a name="communication"></a>Communication

> Integration with communication platforms for message management and channel operations. Enables AI models to interact with team communication tools.

- <img src="https://cdn.simpleicons.org/slack/E01E5A" height="14"/> [Slack](https://github.com/korotovsky/slack-mcp-server) - The most powerful MCP Slack Server with Stdio and SSE transports, Proxy support and no permission requirements on Slack Workspace.
- <img src="https://www.line.me/favicon-32x32.png" height="14" /> [LINE Official Account](https://github.com/line/line-bot-mcp-server)<sup><sup>⭐</sup></sup> - Integrates the LINE Messaging API to connect an AI Agent to the LINE Official Account.
- <img src="https://cdn.simpleicons.org/linear/5E6AD2" height="14"/> [Linear](https://github.com/jerhadf/linear-mcp-server) - Linear MCP Server. Provides integration with Linear's issue tracking system through MCP.
- <img src="https://cdn.simpleicons.org/atlassian/0052CC" height="14"/> [Atlassian](https://github.com/sooperset/mcp-atlassian) - Comprehensive integration with Atlassian suite including Confluence for documentation management and Jira for issue tracking.
- <img src="https://carbonvoice.app/favicon.ico" height="14"/> [Carbon Voice](https://github.com/PhononX/cv-mcp-server)<sup><sup>⭐</sup></sup> - MCP Server that connects AI Agents to [Carbon Voice](https://getcarbon.app). Create, manage, and interact with voice messages, conversations, direct messages, folders, voice memos, AI actions and more in [Carbon Voice](https://getcarbon.app).
- <img src="https://m2tg1pnwn0.ufs.sh/f/GMqNN8nd9I8l9tUbmif1CnFX8Baqr7mHeicYu0AULDyNVWJE" height="14"/> [ntfy](https://github.com/gitmotion/ntfy-me-mcp) - An ntfy MCP server for sending/fetching ntfy notifications to your self-hosted ntfy.sh server from AI Agents 📤 (supports secure token auth & more - use with npx or docker!)

<br />

## 📈 <a name="monitoring"></a>Monitoring

> Access and analyze application monitoring data. Enables AI models to review error reports and performance metrics.

- <img src="https://metoro.io/static/images/logos/Metoro.svg" height="14"/> [Metoro](https://github.com/metoro-io/metoro-mcp-server) - Query and interact with kubernetes environments monitored by Metoro
- <img src="https://raygun.com/favicon.ico" height="14"/> [Raygun](https://github.com/MindscapeHQ/mcp-server-raygun) - Raygun API V3 integration for crash reporting and real user monitoring
- <img src="https://cdn.simpleicons.org/sentry/546E7A" height="14"/> [Sentry](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry) - Sentry.io integration for error tracking and performance monitoring
- <img src="https://cdn.simpleicons.org/letsencrypt/003A70" height="14"/> [sslmon](https://github.com/firesh/sslmon-mcp) - Domain/HTTPS/SSL domain registration information and SSL certificate monitoring capabilities. Query domain registration and expiration information, and SSL certificate information and validity status for any domain.
- <img src="https://aiops.drdroid.io/favicon.ico" height="14"/> [Signoz](https://github.com/DrDroidLab/signoz-mcp-server) - Comprehensive integration with [Signoz APIs](https://signoz.io/docs/userguide/apis/) and [documentation](https://signoz.io/docs/) for monitoring, observability, and debugging tasks related to your Signoz instances.
- <img src="https://avatars.githubusercontent.com/u/174736222?s=200&v=4" height="14"/> [VictoriaMetrics](https://github.com/VictoriaMetrics-Community/mcp-victoriametrics) - Comprehensive integration with [VictoriaMetrics APIs](https://docs.victoriametrics.com/victoriametrics/url-examples/) and [documentation](https://docs.victoriametrics.com/) for monitoring, observability, and debugging tasks related to your VictoriaMetrics instances.

<br />

## 🔍 <a name="search-web"></a>Search & Web

> Web content access and automation capabilities. Enables searching, scraping, and processing web content in AI-friendly formats.

- <img src="https://cdn.simpleicons.org/puppeteer/00D8A2" height="14"/> [Puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) - Browser automation for web scraping and interaction
- <img src="https://cdn.simpleicons.org/brave/FB542B" height="14"/> [Brave Search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) - Web search capabilities using Brave's Search API
- <img src="https://github.com/user-attachments/assets/5d9346e8-7821-4202-80cd-25e0678d3400" height="14"/> [Bright Data](https://github.com/luminati-io/brightdata-mcp) - Discover, extract, and interact with the web - one interface powering automated access across the public internet.
- <img src="https://avatars.githubusercontent.com/u/204530939?s=200&v=4" height="14"/> [Dumpling AI](https://github.com/Dumpling-AI/mcp-server-dumplingai) - Access data, web scraping, and document conversion APIs by [Dumpling AI](https://www.dumplingai.com/)
- <img src="https://cdn.simpleicons.org/curl/00ADD8" height="14"/> [Fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) - Efficient web content fetching and processing for AI consumption
- <img src="https://cdn.simpleicons.org/kagi/4173FF" height="14"/> [Kagi Search](https://github.com/ac3xx/mcp-servers-kagi) - TypeScript-based MCP server that integrates the Kagi Search API
- <img src="https://www.tryleap.ai/assets/integrations/exa.svg" height="14"/> [Exa Search](https://github.com/exa-labs/exa-mcp-server)<sup><sup>⭐</sup></sup> - Integration with Exa AI Search API for real-time web information retrieval
- <img src="https://cdn.simpleicons.org/newyorktimes/E34234" height="14"/> [NYTimes](https://github.com/angheljf/nyt) - Search articles using the NYTimes API
- <img src="https://cdn.simpleicons.org/googlenews/4285F4" height="14"/> [Google News](https://github.com/ChanMeng666/server-google-news) - Google News search with automatic categorization, multi-language support, and comprehensive search options
- <img src="https://avatars.githubusercontent.com/u/175926811?v=4" height="14"/> [Scrapeless](https://github.com/scrapeless-ai/scrapeless-mcp-server) - The Scrapeless Model Context Protocol service acts as an MCP server connector to the Google SERP API, enabling web search within the MCP ecosystem without leaving it. 
- <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Vector_search_icon.svg/800px-Vector_search_icon.svg.png" height="14"/> [Search1API](https://github.com/fatwang2/search1api-mcp) - Search via search1api (requires paid API key)
- <img src="https://github.com/user-attachments/assets/3c1cb503-11cc-4172-ac4e-73497b5eb3b8" height = "14"> [RivalSearchMCP](https://github.com/damionrashford/RivalSearchMCP) - A powerful MCP server providing a suite of tools for web search, content discovery, and automated research workflows.
- <img src="https://tavily.com/favicon.ico" height="14"/> [Tavily](https://github.com/Tomatio13/mcp-server-tavily) - Tavily AI search API integration
- <img src="https://cdn.simpleicons.org/arxiv/B31B1B" height="14"/> [ArXiv](https://github.com/blazickjp/arxiv-mcp-server) - Search ArXiv research papers
- <img src="https://github.com/user-attachments/assets/6f9c9a70-01c8-4255-abbe-66faf146970e" height="14"> [PapersWithCode](https://github.com/hbg/mcp-paperswithcode) - Search research papers, conferences, and codebases through PapersWithCode API
- <img src="https://playwright.dev/img/playwright-logo.svg" height="14"/> [Playwright](https://github.com/executeautomation/mcp-playwright) - A Model Context Protocol server that provides browser automation capabilities using Playwright.
- <img src="https://cdn.simpleicons.org/searxng" height="14"/> [Websearch](https://github.com/mnhlt/WebSearch-MCP) - Self-hosted Websearch service.
- <img src="https://cdn.simpleicons.org/firefoxbrowser" height="14"/> [Browser Control](https://github.com/eyalzh/browser-control-mcp) - An MCP server paired with a browser extension allowing local browser control. 
- <img src="https://blog.apify.com/content/images/2025/02/Apify_logo.png" height="14"/> [Apify Actors](https://github.com/apify/actors-mcp-server) - Use 4,000+ pre-built cloud tools, known as Actors, to extract data from websites, e-commerce, social media, search engines, maps, and more.
- <img src="https://blog.apify.com/content/images/2025/02/Apify_logo.png" height="14"/> [RAG Web Browser](https://github.com/apify/mcp-server-rag-web-browser) - An MCP server for Apify's open-source RAG Web Browser Actor to perform web searches, scrape URLs, and return content in Markdown.
- <img src="https://framerusercontent.com/images/0Bw7GwbNXUBxOAp9pyM0VPOlphg.png" height="14" /> [Skyvern](https://github.com/Skyvern-AI/skyvern/tree/main/integrations/mcp) - MCP to let Claude or your own LLM control your browser
- <img src="https://searx.space/favicon.png" height="14" /> [Ihor-Sokoliuk/MCP-SearXNG](https://github.com/ihor-sokoliuk/mcp-searxng) - A Model Context Protocol Server for [SearXNG](https://docs.searxng.org)
- <img src="https://pragmar.com/media/static/images/mcp-server-webcrawl/favicon.png" height="14" /> [mcp-server-webcrawl](https://github.com/pragmar/mcp-server-webcrawl) - Advanced search and retrieval for web crawler data. Supports WARC, wget, Katana, SiteOne, and InterroBot crawlers.

<br />

## 🗺️ <a name="location-services"></a>Location Services

> Geographic and location-based services integration. Enables access to mapping data, directions, and place information.

- <img src="https://campertunity.com/assets/icon/favicon.ico" height="14"/> [Campertunity](https://github.com/campertunity/mcp-server) - Search campgrounds around the world on campertunity, check availability, and provide booking links
- <img src="https://cdn.simpleicons.org/googlemaps/4285F4" height="14"/> [Google Maps](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps) - Google Maps integration for location services, routing, and place details
- <img src="https://static.iplocate.io/custom/logo-square-rounded.png" height="14"/> [IPLocate](https://github.com/iplocate/mcp-server-iplocate) - Look up IP address geolocation, network information, detect proxies and VPNs, and find abuse contact details using IPLocate.io
- <img src="https://www.ip2location.io/favicon.ico" height="14"/> [IP2Location.io](https://github.com/ip2location/mcp-ip2location-io) - IP2Location.io API integration to retrieve the geolocation information for an IP address.
- <img src="https://www.qgis.org/styleguide/visual/qgis-logo.svg" height="14"/> [QGIS](https://github.com/jjsantos01/qgis_mcp) - connects QGIS Desktop to Claude AI through the MCP. This integration enables prompt-assisted project creation, layer loading, code execution, and more.


<br />

## 🎯 <a name="marketing"></a>Marketing

> Tools that help marketers write better content and run better campaigns.

- <img src="https://cdn.simpleicons.org/analytics/4285F4" height="14"/> [Agent Mindshare](https://agentmindshare.com) - Track and monitor AI agent mindshare across platforms - measure brand visibility in AI conversations.
- <img src="https://openstrategypartners.com/fileadmin/Bilder/logo/OSP_logo_colors_green1.png" height="14"/> [Open Strategy Partners Marketing Tools](https://github.com/open-strategy-partners/osp_marketing_tools)<sup><sup>⭐</sup></sup> - a standardized editing code system, writing guidelines, web metadata generator, and product communication framework.
- <img src="https://cdn.simpleicons.org/fathom/9187FF" height="14"/> [Fathom Analytics](https://github.com/mackenly/mcp-fathom-analytics) - Access Fathom Analytics data and reports about your sites
- <img src="https://static.xx.fbcdn.net/rsrc.php/y9/r/tL_v571NdZ0.svg" height="14"/> [Facebook Ads](https://github.com/gomarble-ai/facebook-ads-mcp-server) - MCP server acting as an interface to the Facebook Ads, enabling programmatic access to Facebook Ads data and management features.
- <img src="https://img.icons8.com/?size=48&id=ui4CTPMMDCFh&format=png" height="14"/> [Google Ads](https://github.com/gomarble-ai/google-ads-mcp-server) - MCP server acting as an interface to the Google Ads, enabling programmatic access to Google Ads data and management features.
<br />

## 📝 <a name="note-taking"></a>Note Taking

> Integration with note-taking applications and personal knowledge management tools. Enables access to notes, documents, and personal information stores.
- <img src="https://static.wikia.nocookie.net/logopedia/images/2/25/Apple_Books_%28iOS%29_2024_dark.svg/revision/latest?cb=20240616234654" height="14"/> [Apple Books](https://github.com/vgnshiyer/apple-books-mcp) - Transform your Apple Books to a queryable knowledge base.
- <img src="https://github.com/onebirdrocks/ebook-mcp/raw/refs/heads/main/favicon.png" alt="ebook-mcp Logo" height="14" /> [eBook-mcp](https://github.com/onebirdrocks/ebook-mcp) - A lightweight MCP server that allows LLMs to read and interact with your personal PDF and EPUB ebooks on your local machine. Ideal for building AI reading assistants or chat-based ebook interfaces.
- <img src="https://cdn.simpleicons.org/obsidian/7C3AED" height="14"/> [Obsidian](https://github.com/MarkusPfundstein/mcp-obsidian)<sup><sup>1</sup></sup> - Obsidian vault integration with tools for file management, search, and content manipulation
- <img src="https://cdn.simpleicons.org/obsidian/7C3AED" height="14"/> [Obsidian](https://github.com/calclavia/mcp-obsidian)<sup><sup>2</sup></sup> - Alternative implementation for reading and searching Markdown notes
- <img src="https://cdn.simpleicons.org/notion/787878" height="14"/> [Notion](https://github.com/danhilse/notion_mcp)<sup><sup>1</sup></sup> - Notion API integration for managing personal todo lists and notes
- <img src="https://cdn.simpleicons.org/notion/787878" height="14"/> [Notion](https://github.com/suekou/mcp-notion-server)<sup><sup>2</sup></sup> - Alternative implementation for Notion API integration
- <img src="https://cdn.simpleicons.org/apple/999999" height="14"/> [Apple Notes](https://github.com/sirmews/apple-notes-mcp) - Read from local Apple Notes database (macOS only)
- <img src="https://pipedream.com/s.v0/app_Noh9dw/logo/orig" height="14"/> [Slite](https://github.com/fajarmf/slite-mcp) - Model Context Protocol server for Slite integration. Search and retrieve notes, browse note hierarchies, and access content from your Slite workspace.
- <img src="https://cdn.simpleicons.org/todoist/E44332" height="14"/> [Todoist](https://github.com/abhiz123/todoist-mcp-server) - An MCP server implementation for Todoist, enabling natural language task management.
- <img src="https://cdn.simpleicons.org/googlekeep/FFBB00" height="14"/> [Google Keep](https://github.com/feuerdev/keep-mcp) - Read, create, update and delete Google Keep notes.

<br />

## ⚡ <a name="cloud-platforms"></a>Cloud Platforms

> Cloud platform service integration. Enables management and interaction with cloud infrastructure and services.

- <img src="https://cdn.simpleicons.org/cloudflare/F38020" height="14"/> [Cloudflare](https://github.com/cloudflare/mcp-server-cloudflare)<sup><sup>⭐</sup></sup> - Integration with Cloudflare services including Workers, KV, R2, and D1
- <img src="https://cdn.simpleicons.org/kubernetes/326CE5" height="14"/> [Kubernetes](https://github.com/strowk/mcp-k8s-go)<sup><sup>1</sup></sup> - Kubernetes cluster operations through MCP
- <img src="https://cdn.simpleicons.org/kubernetes/326CE5" height="14"/> [Kubernetes](https://github.com/weibaohui/k8m)<sup><sup>2</sup></sup> - Kubernetes  multi-cluster  management and operations, featuring a management ui, logging, and nearly 50 built-in tools covering common DevOps and development scenarios. Supports both standard and CRD resources.
- <img src="https://cdn.simpleicons.org/kubernetes/326CE5" height="14"/> [MKP](https://github.com/StacklokLabs/mkp)<sup><sup>3</sup></sup> - Model Kontext Protocol Server for Kubernetes with native Go implementation, direct API integration, and comprehensive resource management
- <img src="https://tinybird.co/favicon.ico" height="14"/> [Tinybird](https://github.com/tinybirdco/mcp-tinybird)<sup><sup>⭐</sup></sup> - Interact with a Tinybird Workspace from any MCP client.

<br />

## ⚙️ <a name="workflow-automation"></a>Workflow Automation

> Integration with workflow automation platforms allows AI models to execute workflows and retrieve data back to their systems.

- <img src="https://www.make.com/favicon.ico" height="14"/> [Make](https://github.com/integromat/make-mcp-server)<sup><sup>⭐</sup></sup> - Turn Make scenarios into callable tools for AI assistants.
- <img src="https://www.taskade.com/favicon.ico" height="14"/> [Taskade MCP](https://github.com/taskade/mcp)<sup><sup>⭐</sup></sup> - Official Taskade MCP server + OpenAPI → MCP codegen to build AI agent tools from any API and connect Taskade to Claude, Cursor, and more.

<br />

## 🤖 <a name="system-automation"></a>System Automation

> Tools for shell access, system control, and task automation. Enables AI models to execute commands and interact with the operating system.

- <img src="https://api.iconify.design/mdi:console.svg?color=%2390EE90" height="14"/> [Shell](https://github.com/rusiaaman/wcgw) - Autonomous shell execution and computer control (Mac)
- <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Windows_logo_-_2021.svg/1024px-Windows_logo_-_2021.svg.png" height="14"/> [Windows CLI](https://github.com/SimonB97/win-cli-mcp-server) - Windows CLI MCP Server for secure command-line interactions on Windows systems, enabling controlled access to PowerShell, CMD, and Git Bash shells.
- <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Windows_logo_-_2021.svg/1024px-Windows_logo_-_2021.svg.png" height="14"/> [Windows Control](https://github.com/Cheffromspace/nutjs-windows-control) - Windows automation MCP server providing mouse, keyboard, screen capture, clipboard, and window management capabilities using NutJS.
- <img src="https://cdn.simpleicons.org/gnometerminal/2196F3" height="14"/> [Command Line](https://github.com/phialsbasement/cmd-mcp-server) - MCP server allowing any and all command execution over CMD(BE CAREFUL).
- <img src="https://cdn.simpleicons.org/apple/999999" height="14"/> [Apple Shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts) - An MCP Server Integration with Apple Shortcuts
- <img src="https://cdn.simpleicons.org/gnometerminal/2196F3" height="14"/> [Interactive Terminal](https://github.com/amol21p/mcp-interactive-terminal) - Real interactive terminal sessions for REPLs, SSH, database clients, and any interactive CLI — with clean text output via xterm-headless, smart completion detection, and multi-layer security.

<br />

## 📱 <a name="social-media"></a>Social Media

> Integration with social media platforms and content sharing services. Enables interaction with social networks and content platforms.

- <img src="https://cdn.simpleicons.org/bluesky/0085FF" height="14"/> [BlueSky](https://github.com/keturiosakys/bluesky-context-server) - Bluesky API integration for querying and searching feeds and posts
- <img src="https://cdn.simpleicons.org/youtube/FF0000" height="14"/> [YouTube](https://github.com/anaisbetts/mcp-youtube)<sup><sup>1</sup></sup> - YouTube integration using yt-dlp for subtitle downloading and video analysis
- <img src="https://cdn.simpleicons.org/youtube/FF0000" height="14"/> [YouTube](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript)<sup><sup>2</sup></sup> - Alternative implementation for fetching YouTube subtitles and transcripts
- <img src="https://cdn.simpleicons.org/spotify/1DB954" height="14"/> [Spotify](https://github.com/varunneal/spotify-mcp) - Connects with Spotify for playback control and track/album/artist/playlist management.
- <img src="https://cdn.worldvectorlogo.com/logos/tiktok-icon-2.svg" height="14"/> [TikTok](https://github.com/Seym0n/tiktok-mcp) - TikTok integration for getting post details and video's subtitles

<br />

## 🎮 <a name="gaming"></a>Gaming

> Gaming data and Game Development tools.

- <img src="https://cdn.simpleicons.org/unity/899499" height="14"/> [Unity Engine](https://github.com/IvanMurzak/Unity-MCP)<sup><sup>1</sup></sup> - Tools for Unity Editor and for a game made with Unity
- <img src="https://cdn.simpleicons.org/unity/899499" height="14"/> [UnityEngine](https://github.com/CoderGamester/mcp-unity)<sup><sup>2</sup></sup> - Unity3d Game Engine integration for game development
- <img src="https://cdn.simpleicons.org/unity/899499" height="14"/> [Unity Engine](https://github.com/codemaestroai/advanced-unity-mcp)<sup><sup>3</sup></sup> - Advanced Unity MCP from Code Maestro. Build, debug, profile, and manage assets, scenes, and scripts with natural language via MCP.

<br />

## 💹 <a name="finance"></a>Finance

> Financial data and cryptocurrency information services.

- <img src="https://docs.octagonagents.com/logo.svg" alt="Octagon Logo" height="14"/> [Octagon](https://github.com/OctagonAI/octagon-mcp-server)<sup><sup>⭐</sup></sup> - Deliver real-time market intelligence with extensive private and public market data.
- <img src="https://cdn.simpleicons.org/coinmarketcap/FF8C00" height="14"/> [CoinMarket](https://github.com/anjor/coinmarket-mcp-server) - Coinmarket API integration for cryptocurrency data
- <img src="https://www.chargebee.com/static/resources/brand/favicon.png" height="14"> [Chargebee](https://github.com/chargebee/agentkit/tree/main/modelcontextprotocol)<sup><sup>⭐</sup></sup> - MCP Server that connects AI agents to [Chargebee platform](https://www.chargebee.com).
- <img src="https://dexpaprika.com/favicon.ico" height="14"/> [DexPaprika](https://github.com/donbagger/dexpaprika-mcp-server)<sup><sup>⭐</sup></sup> - Comprehensive cryptocurrency and DEX data API across multiple blockchains, providing real-time token pricing, liquidity pools, and OHLCV data for market analysis
- <img src="https://www.mercadopago.com/favicon.ico" height="14" alt="MercadoPago Logo" /> [Mercado Pago](https://mcp.mercadopago.com/) - Mercado Pago's official MCP server, offering tools to interact with our API, simplifing tasks and product integration.
- <img src="https://www.paypalobjects.com/webstatic/mktg/logo/pp_cc_mark_74x46.jpg" height="14"> [PayPal](https://github.com/paypal/agent-toolkit/tree/main/modelcontextprotocol)<sup><sup>⭐</sup></sup> - The PayPal Agent Toolkit enables popular agent frameworks including Model Context Protocol (MCP) to integrate with PayPal APIs through function calling.
- <img src="https://cdn.simpleicons.org/stripe" height="14"/> [Stripe](https://github.com/stripe/agent-toolkit/tree/main)<sup><sup>⭐</sup></sup> - Allows you to integrate with Stripe APIs
- <img src="https://pub.pbkrs.com/files/202211/TNosrY77nCxm6rtU/logo-without-title.svg" height="14"/> [LongPort OpenAPI](https://github.com/longportapp/openapi/tree/main/mcp)<sup><sup>⭐</sup></sup> - Provides real-time stock market data, provides AI access analysis and trading capabilities through MCP.
- <img src="https://zbd.gg/favicon.ico" height="14"/> [ZBD](https://github.com/zebedeeio/zbd-payments-typescript-sdk/tree/main/packages/mcp-server)<sup><sup>⭐</sup></sup> - Interact with ZBD's payment processing APIs for instant global payments with Bitcoin and Lightning Network

<br />

## 🧬 <a name="research-data"></a>Research & Data

> Access to research papers, genetic data, and specialized datasets.

- <img src="https://cdn.simpleicons.org/arxiv/B31B1B" height="14"/> [ArXiv](https://github.com/blazickjp/arxiv-mcp-server) - Search ArXiv research papers
- <img src="https://api.iconify.design/mdi:dna.svg?color=%23E34234" height="14"/> [Ancestry](https://github.com/reeeeemo/ancestry-mcp) - Read .ged files and genetic data
- <img src="https://probe.dev/favicon.ico" height="14"/> [Probe.dev](https://mcp.probe.dev) - Professional media analysis and validation MCP server with FFprobe, MediaInfo, and comprehensive reporting capabilities
- <img src="https://cdn.simpleicons.org/apple/7ED957" height="14"/> [OpenNutrition](https://github.com/deadletterq/mcp-opennutrition) - Search 300,000+ foods, nutrition facts, and barcodes from the OpenNutrition database
- <img src="https://congressmcp.lawgiver.ai/favicon.svg" height="14"/> [Congress](https://github.com/amurshak/congressMCP) - Query and reeason about legislative data from Congress.gov

<br />

## 🤝 <a name="ai-services"></a>AI Services

> Integration with AI and machine learning services.

- <img src="https://agentset.ai/screenshots/logo.png" height="14"/> [Agentset AI](https://github.com/agentset-ai/mcp-server) -  RAG on your data using MCP protocol
- <img src="https://cdn.simpleicons.org/openai/00A67E" height="14"/> [OpenAI](https://github.com/pierrebrunelle/mcp-server-openai) - Query OpenAI models directly from Claude using MCP protocol
- <img src="https://cdn.simpleicons.org/openai/00A67E" height="14"/> [OpenAI Compatible Chat](https://github.com/pyroprompts/any-chat-completions-mcp) - Chat with models from OpenAI-compatible APIs (Perplexity, Groq, xAI, etc.)
- <img src="https://cdn.simpleicons.org/perplexity" height="14"/> [Perplexity](https://github.com/tanigami/mcp-server-perplexity) Chat with Perplexity via MCP
- <img src="https://cloud.llamaindex.ai/favicon.ico" height="14"/> [LlamaCloud](https://github.com/run-llama/mcp-server-llamacloud) - LlamaCloud MCP Server. A TypeScript-based MCP server connecting to a managed index on LlamaCloud.
- <img src="https://huggingface.co/favicon.ico" height="14"/> [HuggingFace Spaces](https://github.com/evalstate/mcp-hfspace) - Use HuggingFace spaces from your MCP Client. Supports Images, Audio, Text and more.
- <img src="https://piapi.ai/piapi_favicon.webp" height="14"> [PiAPI](https://github.com/apinetwork/piapi-mcp-server) - PiAPI MCP server makes user able to generate media content with Midjourney/Flux/Kling/Hunyuan/Udio/Trellis directly from Claude or any other MCP-compatible apps.
- <img src="https://www.chronulus.com/favicon/chronulus-logo-blue-on-alpha-square-128x128.ico" alt="Chronulus AI Logo" height="14" width="14"> [Chronulus AI](https://github.com/ChronulusAI/chronulus-mcp) -  Predict anything with Chronulus AI multimodal forecasting and prediction agents ([Watch Demos on Youtube](https://youtube.com/playlist?list=PLPLu09ZbT8KKS04V6SSm2Acjv43FKq329&si=n2YER2in4gOqwssY)).
- <img src="https://www.creatify.ai/favicon.ico" height="14"/> [Creatify](https://github.com/TSavo/creatify-mcp) - MCP Server that exposes Creatify AI API capabilities for AI video generation, including avatar videos, URL-to-video conversion, text-to-speech, and AI-powered editing tools.
- <img src="https://www.svgrepo.com/show/495208/data.svg" height="14"/> [ZenML](https://github.com/zenml-io/mcp-zenml)<sup><sup>⭐</sup></sup> - Chat with your MLOps and LLMOps pipelines using the [ZenML](https://www.zenml.io) MCP server

<br />

## 💻 <a name="development-tools"></a>Development Tools

> Tools and servers that assist with software development workflows. Enables integration with development-related services and APIs.

- <img src="https://www.svgrepo.com/show/107853/uranus.svg" height="14"/> [CentralMind/Gateway](https://github.com/centralmind/gateway) - MCP and MCP SSE Server that automatically generate production ready API based on database schema and data. Supports PostgreSQL, Clickhouse, MySQL, Snowflake, BigQuery, Supabase
- <img src="http://currents.dev/favicon.ico" height="14"/> [Currents](https://github.com/currents-dev/currents-mcp)<sup><sup>⭐</sup></sup> - Enable AI Agents to fix Playwright test failures reported to [Currents](https://currents.dev).
- 🐙 [Octocode](https://github.com/bgauryy/octocode-mcp) -  AI-powered developer assistant that enables advanced research, analysis and discovery and code generation across GitHub and NPM realms in realtime.
- <img src="https://raw.githubusercontent.com/kadykov/mcp-openapi-schema-explorer/main/assets/logo-400.png" height="14"/> [OpenAPI Schema Explorer](https://github.com/kadykov/mcp-openapi-schema-explorer) - Token-efficient access to OpenAPI/Swagger specs via MCP Resources.
- <img src="https://raw.githubusercontent.com/open-rpc/design/master/icons/open-rpc-logo-noText/open-rpc-logo-noText%20(PNG)/256x256.png" height="14"/> [OpenRPC](https://github.com/shanejonas/openrpc-mpc-server) - A Model Context Protocol server that provides JSON-RPC functionality through OpenRPC.
- <img src="https://cdn.simpleicons.org/postman" height="14" /> [Postman](https://github.com/delano/postman-mcp-server) - Interact with [Postman API](https://www.postman.com/postman/postman-public-workspace/).
- <img src="https://marketing.qasphere.com/images/logo/qasphere-square-512.png" height="14" /> [QA Sphere](https://github.com/Hypersequent/qasphere-mcp)<sup><sup>⭐</sup></sup> - Integration with QA Sphere test management system, enabling LLMs to discover, summarize, and interact with test cases directly from AI-powered IDEs
- <img src="https://raw.githubusercontent.com/marimo-team/marimo/main/docs/_static/marimo-logotype-thick.svg" height="14" /> [marimo](https://github.com/marimo-team/codemirror-mcp)<sup><sup>⭐</sup></sup> - CodeMirror extension that implements the Model Context Protocol (MCP) for resource mentions and prompt commands.
- <img src="https://static.figma.com/app/icon/1/favicon.ico" height="14" /> [Figma](https://github.com/GLips/Figma-Context-MCP) - Paste a link to your Figma design to get its data in a ready-to-implement format.
- <img src="https://www.comet.com/favicon.ico" height="14" /> [Comet Opik](https://github.com/comet-ml/opik-mcp)<sup><sup>⭐</sup></sup> - Query and interact with LLM observability and telemetry captured by [Opik](https://github.com/comet-ml/opik) using natural language.
- <img src="https://vscode.dev/static/stable/favicon.ico" height="14" /> [VSCode Devtools](https://github.com/biegehydra/BifrostMCP) - Connect to VSCode ide and allows using semantic tools like `find_usages`
- <img src="https://mastra.ai/favicon/icon.svg" height="14" /> [Mastra/mcp](https://github.com/mastra-ai/mastra/tree/main/packages/mcp)<sup><sup>⭐</sup></sup> - Provides AI assistants with direct access to Mastra.ai's complete knowledge base.
- <img src="https://github.com/user-attachments/assets/9d517481-c4cd-4b6c-903a-878531c9d881" height="14" /> [Bucket](https://github.com/bucketco/bucket-javascript-sdk/tree/main/packages/cli#model-context-protocol) - Flag features, manage company data, and control feature access using [Bucket](https://bucket.co)
- <img src="https://edgeone.ai/favicon.ico" height="14" /> [EdgeOne Pages](https://github.com/TencentEdgeOne/edgeone-pages-mcp) - A MCP service for deploying HTML content to EdgeOne Pages and obtaining a publicly accessible URL.
- <img src="https://cdn.jsdelivr.net/gh/jsdelivr/globalping-media@refs/heads/master/icons/android-chrome-192x192.png" height="14" /> [Globalping MCP](https://github.com/jsdelivr/globalping-mcp-server)<sup><sup>⭐</sup></sup> - Access a network of thousands of probes to run network commands like ping, traceroute, mtr, http and DNS resolve.
- <img src="https://gitkraken.com/favicon.ico" height="14" /> [GitKraken](https://github.com/gitkraken/gk-cli)<sup><sup>⭐</sup></sup> - A CLI for interacting with GitKraken APIs. Includes an MCP server via gk mcp that not only wraps GitKraken APIs, but also Jira, GitHub, GitLab, and more. Works with local tools and remote services.
-  <img src="[https://intayer.org/fav](https://intlayer.org/favicon-32x32.png)" height="14" /> [aymericzip/intlayer](https://github.com/aymericzip/intlayer) - A MCP Server that enhance your IDE with AI-powered assistance for Intlayer i18n / CMS tool: smart CLI access, docs.
- <img src="https://cdn.simpleicons.org/jira/0052CC" height="14"/> [tom28881/mcp-jira-server](https://github.com/tom28881/mcp-jira-server) - Comprehensive TypeScript MCP server for Jira with 20+ tools covering complete project management workflow: issue CRUD, sprint management, comments/history, attachments, batch operations. Features universal field auto-detection, full Czech/localization support, and date parsing with multiple formats. Created by [Tomáš Gregorovič](https://www.linkedin.com/in/tomáš-g-8423b61a2/).
- <img src="https://maven.apache.org/images/maven-logo-black-on-white.png" height="14"/>  [Maven Tools MCP](https://github.com/arvindand/maven-tools-mcp) - Maven Central dependency intelligence for JVM build tools (Maven, Gradle, SBT, Mill) with Context7 integration for documentation support.
- <img src="https://defang.io/favicon.png" height="14" /> [DefangLabs/defang](https://github.com/DefangLabs/defang) - CLI and MCP server for building and deploying Docker Compose-compatible projects to your own AWS, GCP, or DigitalOcean account.

<br />

## 📊 <a name="data-visualization"></a>Data Visualization

> Tools for creating and managing data visualizations. Enables generation of charts, graphs, and other visual representations of data.

- <img src="https://vega.github.io/favicon.ico" height="14"/> [VegaLite](https://github.com/isaacwasserman/mcp-vegalite-server) - Generate visualizations from fetched data using the VegaLite format and renderer.
- <img src="https://mdn.alipayobjects.com/huamei_qa8qxu/afts/img/A*ZFK8SrovcqgAAAAAAAAAAAAAemJ7AQ/original" height="14"/> [Chart](https://github.com/antvis/mcp-server-chart) - A Model Context Protocol server for generating visual charts using [AntV](https://github.com/antvis).
- <img src="https://echarts.apache.org/zh/images/favicon.png" height="14"/> [ECharts](https://github.com/hustcc/mcp-echarts) - Generate visual charts using [Apache ECharts](https://echarts.apache.org/) with AI MCP dynamically.
- <img src="https://mermaid.js.org/favicon.svg" height="14"/> [Mermaid](https://github.com/hustcc/mcp-mermaid) - Generate [mermaid](https://mermaid.js.org/) diagram and chart with AI MCP dynamically.
- <img src="https://cdn.simpleicons.org/git/F05032" height="14"/> [unified-diff-mcp](https://github.com/gorosun/unified-diff-mcp) - Generate visual diff comparisons from text changes with HTML/PNG export. Perfect for code reviews and document analysis with side-by-side visualization.

<br />

## 🆔 <a name="identity"></a>Identity

> Tools for identity and access management. Enables user authentication, authorization.

- <img src="https://upload.wikimedia.org/wikipedia/commons/2/29/Keycloak_Logo.png" height="14"/> [Keycloak](https://github.com/ChristophEnglisch/keycloak-model-context-protocol) - MCP server implementation for managing Keycloak users, groups, and realms using natural language queries.

<br />

## 🔗 <a name="aggregators"></a>Aggregators

> Tools for accessing many apps and tools through a single MCP server..

- <img height="12" width="12" src="https://github.com/mcpjungle/MCPJungle/blob/main/assets/logo.png" alt="MCPJungle Logo" /> [MCPJungle](https://github.com/mcpjungle/MCPJungle) - Self-hosted MCP Registry and Proxy for enterprise AI Agents.

- <img height="12" width="12" src="https://platform.composio.dev/favicon.ico" alt="Composio Logo"> **[Rube](https://rube.composio.dev)** - Rube is a Model Context Protocol (MCP) server that connects your AI tools to 500+ apps like Gmail, Slack, GitHub, and Notion. Simply install it in your AI client, authenticate once with your apps, and start asking your AI to perform real actions like "Send an email" or "Create a task."

- <img height="12" width="12" src="https://pipedream.com/favicon.ico" alt="Pipedream Logo" /> [Pipedream](https://github.com/PipedreamHQ/pipedream/tree/master/modelcontextprotocol) - Connect with 2,500 APIs with 8,000+ prebuilt tools, and manage servers for your users, in your own app.
 
- <img height="12" width="12" src="https://cdn.zapier.com/zapier/images/favicon.ico" alt="Zapier Logo" /> [Zapier](https://zapier.com/mcp) - Connect your AI Agents to 8,000 apps instantly.

<br />

## 💬 <a name="language"></a>Language & Translation

> Provides real-time translation of text, documents, and content between multiple languages.

- <img src="https://laratranslate.com/favicon.ico" height="14"/> [Lara](https://github.com/translated/lara-mcp)<sup><sup>⭐</sup></sup> - MCP Server for Lara Translate API, enabling powerful translation capabilities with support for language detection and context-aware translations

<br />

## 🔒 <a name="security"></a>Security

> Tools for security needs. Enables securing code, finding vulnerabilies.

- <img src="https://semgrep.dev/favicon.ico" height="14"/> [Semgrep](https://github.com/semgrep/mcp) - A MCP server for using [Semgrep](https://github.com/semgrep/semgrep) to scan code for security vulnerabilities.
- <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Microsoft_Entra_ID_color_icon.svg/120px-Microsoft_Entra_ID_color_icon.svg.png" height="14"/> [Microsoft Entra ID](https://github.com/hieuttmmo/entraid-mcp-server) - A MCP server for interacting with EntraID through Microsoft Graph API. It is designed for extensibility, maintainability, and security, supporting advanced queries for users, sign-in logs, MFA status, privileged users and more.
- <img src="https://www.netwrix.com/favicon.ico" height="14"/> [Netwrix](https://github.com/netwrix/mcp-server-naa)<sup><sup>⭐</sup></sup> - A FastMCP-based server for [Netwrix Access Analyzer](https://www.netwrix.com/access-analyzer.html) data analysis, designed for enhanced data analysis capabilities.
- <img src="https://osv.dev/favicon.ico" height="14"/> [OSV](https://github.com/StacklokLabs/osv-mcp) - Access the OSV (Open Source Vulnerabilities) database for vulnerability information. Query vulnerabilities by package version or commit, batch query multiple packages, and get detailed vulnerability information by ID.
- <img src="https://vulert.com/favicon.ico" height="14"> [Vulert](vulert.com) - Vulert secures software by detecting vulnerabilities in open-source dependencies—without accessing your code. It supports Js, PHP, Java, Python, and more
- <img src="https://cdn.worldvectorlogo.com/logos/thales-1.svg" height="14"/> [CDSP](https://github.com/sanyambassi/ciphertrust-manager-mcp-server) - MCP server for Thales CipherTrust Manager integration, enabling secure key management, cryptographic operations, and compliance monitoring through AI assistants.
- <img src="https://cdn.worldvectorlogo.com/logos/thales-1.svg" height="14"/> [CAKM](https://github.com/sanyambassi/thales-cdsp-cakm-mcp-server) - MCP server for Thales CDSP CAKM integration, enabling secure key management, cryptographic operations, and compliance monitoring through AI assistants for Ms SQL and Oracle Databases.
- <img src="https://cdn.worldvectorlogo.com/logos/thales-1.svg" height="14"/> [CRDP](https://github.com/sanyambassi/thales-cdsp-crdp-mcp-server) - MCP server for Thales CipherTrust Manager RestFul Data Protection service.
- <img src="https://cdn.worldvectorlogo.com/logos/thales-1.svg" height="14"/> [CSM](https://github.com/sanyambassi/thales-cdsp-csm-mcp-server) - MCP server for Thales CipherTrust Secrets Management

<br />

## 🔌 <a name="iot"></a>IoT

> Tools that integrate with Internet of Things connectivity.

- <img src="https://avatars.githubusercontent.com/u/66228869?s=200&v=4" height="14"/> [Coreflux MQTT](https://github.com/CorefluxCommunity/CorefluxMCPServer) - MCP server for the Coreflux MQTT broker, enabling AI agents to transfom the broker into a automation hub and interact with IoT devices and messaging systems through the MQTT protocol. 

<br />

## 🧑‍🎨 <a name="art-literature"></a>Art & Literature

> Art and literature services.

- <img src="https://openlibrary.org/static/images/openlibrary-logo-tighter.svg" height="14"/> [MCP Open Library](https://github.com/8enSmith/mcp-open-library) - A Model Context Protocol (MCP) server for the Internet Archive's Open Library API that enables AI assistants to search for book and author information.

<br />

## 🛒 <a name="e-commerce"></a>E-Commerce

> E-Commerce platforms.

- <img src="https://www.mercadolibre.com.ar/favicon.ico" height="14" alt="MercadoLibre Logo" /> [Mercado Libre](https://mcp.mercadolibre.com/) - Mercado Libre's official MCP server, offering tools to interact with our marketplace, simplifying tasks and product integration.
- <img src="https://shopsavvy.com/favicon.ico" height="14" alt="ShopSavvy Logo" /> **[ShopSavvy](https://github.com/shopsavvy/shopsavvy-mcp-server)**<sup><sup>⭐</sup></sup> - Complete product and pricing data solution for AI assistants. Search for products by barcode/ASIN/URL, access detailed product metadata, access comprehensive pricing data from thousands of retailers, view and track price history, and more. Published as `@shopsavvy/mcp-server`.

<br />

## 📦 <a name="data-platforms"></a>Data Platforms

> Platforms for orchestrating, transforming, and managing data pipelines. Enables AI agents to interact with complex ETL/ELT workflows, unify disparate data sources, and drive automated data operations across cloud and hybrid environments.

- <img height="12" width="12" src="https://connection.keboola.com/favicon.ico" alt="Keboola Logo" /> **[Keboola](https://github.com/keboola/keboola-mcp-server)**<sup><sup>⭐</sup></sup> - Build robust data workflows, integrations, and analytics on a single intuitive platform.

<br />

## 🤖 <a name="robotics"></a>Robotics & Physical AI

> Robotics, drones and physical AI.

- <img height="14" src="https://avatars.githubusercontent.com/u/224125194?s=200&v=4" alt="Extelligence Logo"> [Bagel](https://github.com/Extelligence-ai/bagel) - ChatGPT for physical data. Troubleshoot your robots and drones with natural language. No fuss.

<br />

# Tools & Utilities

> Tools that help manage, configure, and work with MCP servers. These utilities simplify the installation process and improve the user experience.

### Server Managers

- [mcp-get](https://github.com/michaellatman/mcp-get) - CLI tool for installing and managing MCP servers. Simplifies server installation and configuration for Claude Desktop.
  - Supports NPM-based servers
  - Automatic configuration generation
  - Easy server management
- [mxcp](http://github.com/raw-labs/mxcp) - Open-source framework for building secure, testable, enterprise-grade MCP tools from SQL or Python on top of dbt + DuckDB.
- [Remote MCP](https://github.com/ssut/Remote-MCP) - Solution to Remote MCP Communication, enabling effortless integration for centralized management of Model Context
- [yamcp](https://github.com/hamidra/yamcp) - A Model Context Workspace Manager. Oraganize your MCP servers in local workspaces (coding, design, research, ...), scan, monitor, and integrate each workspace with AI apps via a unified CLI.
- [ToolHive](https://github.com/StacklokLabs/toolhive) - A lightweight utility designed to simplify the deployment and management of MCP servers, ensuring ease of use, consistency, and security through containerization.

<br />

Please read the [contribution guidelines](CONTRIBUTING.md) if you want to contribute.

---

### License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Stephen Akinyemi](https://github.com/appcypher) has waived all copyright and related or neighboring rights to this work.
