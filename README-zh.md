
# 精选的 MCP 服务器 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

精选的优秀模型上下文协议 (MCP) 服务器列表。

* [什么是MCP？](#what-is-mcp)
* [教程](#tutorials)
* [Server 实现](#server-implementations)
* [框架](#frameworks)
* [提示和技巧](#tips-and-tricks)

## 什么是MCP？

[MCP](https://modelcontextprotocol.io/) 是一种开放协议，通过标准化的服务器实现，使 AI 模型能够安全地与本地和远程资源进行交互。此列表重点关注可用于生产和实验性的 MCP 服务器，这些服务器通过文件访问、数据库连接、API 集成和其他上下文服务来扩展 AI 功能。

## 教程

* [Model Context Protocol (MCP) 快速开始](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
* [设置 Claude 桌面应用程序以使用 SQLite 数据库](https://youtu.be/wxCCzo9dGj0)

## 社区

* [r/mcp Reddit](https://www.reddit.com/r/mcp)
* [Discord 服务](https://glama.ai/mcp/discord)

## 说明

* 🎖️ – 正式实施
* 🐍 – Python 代码库
* 📇 – TypeScript 代码库
* 🏎️ – Go 代码库
* ☁️ - 云服务
* 🏠 - 本地服务

## 服务器实现

* 📂 - [浏览器自动化](#browser-automation)
* ☁️ - [云平台](#cloud-platforms)
* 💬 - [社交](#communication)
* 👤 - [数据平台](#customer-data-platforms)
* 🗄️ - [数据库](#databases)
* 🛠️ - [开发者工具](#developer-tools)
* 📂 - [文件系统](#file-systems)
* 🧠 - [知识与记忆](#knowledge--memory)
* 🗺️ - [位置服务](#location-services)
* 📊 - [监测](#monitoring)
* 🔎 - [搜索](#search)
* 🔄 - [旅行与交通](#travel-and-transportation)
* 🔄 - [版本控制](#version-control)
* 🛠️ - [其他工具和集成](#other-tools-and-integrations)

### 📂 <a name="browser-automation"></a>浏览器自动化

Web 内容访问和自动化功能。支持以 AI 友好格式搜索、抓取和处理 Web 内容。

- [@executeautomation/playwright-mcp-server](https://github.com/executeautomation/mcp-playwright) 🌐⚡️ - 使用 Playwright 进行浏览器自动化和网页抓取的 MCP 服务器
- [@automatalabs/mcp-server-playwright](https://github.com/Automata-Labs-team/MCP-Server-Playwright) 🌐🖱️ - 使用 Playwright 实现浏览器自动化的 MCP 服务器
- [@modelcontextprotocol/server-puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) 📇 🏠 - 用于网页抓取和交互的浏览器自动化
- [@kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) 📇 ☁️ - 获取 YouTube 字幕和文字记录以供 AI 分析

### ☁️ <a name="cloud-platforms"></a>云平台

云平台服务集成。实现与云基础设施和服务的管理和交互。

- [Cloudflare MCP Server](https://github.com/cloudflare/mcp-server-cloudflare) 🎖️ 📇 ☁️ - 与 Cloudflare 服务集成，包括 Workers、KV、R2 和 D1
- [Kubernetes MCP Server](https://github.com/strowk/mcp-k8s-go) - 🏎️ ☁️ 通过 MCP 操作 Kubernetes 集群

### 💬 <a name="communication"></a>社交

与通讯平台集成，实现消息管理和渠道运营。使AI模型能够与团队沟通工具进行交互。

- [@modelcontextprotocol/server-slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack) 📇 ☁️ - 用于频道管理和消息传递的 Slack 工作区集成
- [@modelcontextprotocol/server-bluesky](https://github.com/keturiosakys/bluesky-context-server) 📇 ☁️ - Bluesky 实例集成，用于查询和交互
- [MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite) - 🐍 ☁️ - 与 Gmail 和 Google 日历集成。

### 👤 <a name="customer-data-platforms"></a>数据平台

提供对客户数据平台内客户资料的访问

- [sergehuber/inoyu-mcp-unomi-server](https://github.com/sergehuber/inoyu-mcp-unomi-server) 📇 ☁️ - MCP 服务器用于访问和更新 Apache Unomi CDP 服务器上的配置文件。

### 🗄️ <a name="databases"></a>数据库

具有模式检查功能的安全数据库访问。支持使用可配置的安全控制（包括只读访问）查询和分析数据。

- [LucasHild/mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery) 🐍 ☁️ - BigQuery 数据库集成了架构检查和查询功能
- [ergut/mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server) 📇 ☁️ - Google BigQuery 集成的服务器实现，可实现直接 BigQuery 数据库访问和查询功能
- [designcomputer/mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server) 🐍 🏠 - MySQL 数据库集成可配置的访问控制、模式检查和全面的安全指南
- [@modelcontextprotocol/server-postgres](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) 📇 🏠 - PostgreSQL 数据库集成了模式检查和查询功能
- [@modelcontextprotocol/server-sqlite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) 🐍 🏠 - 具有内置分析功能的 SQLite 数据库操作
- [ktanaka101/mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb) 🐍 🏠 - DuckDB 数据库集成了模式检查和查询功能

### 📂 <a name="file-systems"></a>文件系统

提供对本地文件系统的直接访问，并具有可配置的权限。使 AI 模型能够读取、写入和管理指定目录中的文件。

- [@modelcontextprotocol/server-filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) 📇 🏠 - 直接访问本地文件系统。
- [@modelcontextprotocol/server-google-drive](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive) 📇 ☁️ - Google Drive 集成，用于列出、阅读和搜索文件
- [mark3labs/mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server) 🏎️ 🏠 - 用于本地文件系统访问的 Golang 实现。

### 🧠 <a name="knowledge--memory"></a>知识与记忆

使用知识图谱结构的持久内存存储。使 AI 模型能够跨会话维护和查询结构化信息。

- [@modelcontextprotocol/server-memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) 📇 🏠 - 基于知识图谱的长期记忆系统用于维护上下文

### 🗺️ <a name="location-services"></a>位置服务

地理和基于位置的服务集成。支持访问地图数据、方向和位置信息。

- [@modelcontextprotocol/server-google-maps](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps) 📇 ☁️ - Google 地图集成，提供位置服务、路线规划和地点详细信息

### 📊 <a name="monitoring"></a>监测

访问和分析应用程序监控数据。使 AI 模型能够审查错误报告和性能指标。

- [@modelcontextprotocol/server-sentry](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry) 🐍 ☁️ - Sentry.io 集成用于错误跟踪和性能监控
- [@modelcontextprotocol/server-raygun](https://github.com/MindscapeHQ/mcp-server-raygun) 📇 ☁️ - Raygun API V3 集成用于崩溃报告和真实用户监控

### 🔎 <a name="search"></a>搜索

- [@modelcontextprotocol/server-brave-search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) 📇 ☁️ - 使用 Brave 的搜索 API 实现网页搜索功能
- [@angheljf/nyt](https://github.com/angheljf/nyt) 📇 ☁️ - 使用 NYTimes API 搜索文章
- [@modelcontextprotocol/server-fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) 🐍 🏠 ☁️ - 高效获取和处理网页内容，供 AI 使用
- [ac3xx/mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi) 📇 ☁️ - Kagi 搜索 API 集成
- [theishangoswami/exa-mcp-server](https://github.com/theishangoswami/exa-mcp-server) 📇 ☁️ - Exa AI 搜索 API
- [exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) 🎖️ 📇 ☁️ – 模型上下文协议 (MCP) 服务器让 Claude 等 AI 助手可以使用 Exa AI Search API 进行网络搜索。此设置允许 AI 模型以安全且可控的方式获取实时网络信息。
- [fatwang2/search1api-mcp](https://github.com/fatwang2/search1api-mcp) 📇 ☁️ - 通过 search1api 搜索（需要付费 API 密钥）
- [Tomatio13/mcp-server-tavily](https://github.com/Tomatio13/mcp-server-tavily) ☁️ 🐍 – Tavily AI 搜索 API
- [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) ☁️ 🐍 - 搜索 ArXiv 研究论文

### 🚆 <a name="travel-and-transportation"></a>旅行与交通

访问旅行和交通信息。可以查询时刻表、路线和实时旅行数据。

- [NS Travel Information MCP Server](https://github.com/r-huijts/ns-mcp-server) 📇 ☁️ - 了解荷兰铁路 (NS) 的旅行信息、时刻表和实时更新

### 🔄 <a name="version-control"></a>版本控制

与 Git 存储库和版本控制平台交互。通过标准化 API 实现存储库管理、代码分析、拉取请求处理、问题跟踪和其他版本控制操作。

- [@modelcontextprotocol/server-github](https://github.com/modelcontextprotocol/servers/tree/main/src/github) 📇 ☁️ - GitHub API集成用于仓库管理、PR、问题等
- [@modelcontextprotocol/server-gitlab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab) 📇 ☁️ 🏠 - GitLab平台集成用于项目管理和CI/CD操作
- [@modelcontextprotocol/server-git](https://github.com/modelcontextprotocol/servers/tree/main/src/git) 🐍 🏠 - 直接的Git仓库操作，包括读取、搜索和分析本地仓库

### 🛠️ <a name="other-tools-and-integrations"></a>其他工具和集成

- [mrjoshuak/godoc-mcp](https://github.com/mrjoshuak/godoc-mcp) 🏎️ 🏠 - 高效的 Go 文档服务器，让 AI 助手可以智能访问包文档和类型，而无需阅读整个源文件
- [pierrebrunelle/mcp-server-openai](https://github.com/pierrebrunelle/mcp-server-openai) 🐍 ☁️ - 直接从Claude查询OpenAI模型，使用MCP协议
- [@modelcontextprotocol/server-everything](https://github.com/modelcontextprotocol/servers/tree/main/src/everything) 📇 🏠 - MCP服务器，涵盖MCP协议的所有功能
- [baba786/phabricator-mcp-server](https://github.com/baba786/phabricator-mcp-server) 🐍 ☁️ - 与Phabricator API交互
- [MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) 🐍 ☁️ 🏠 - 通过REST API与Obsidian交互
- [calclavia/mcp-obsidian](https://github.com/calclavia/mcp-obsidian) 📇 🏠 - 这是一个连接器，允许Claude Desktop（或任何MCP客户端）读取和搜索包含Markdown笔记的目录（如Obsidian库）。
- [anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube) 📇 ☁️ - 获取YouTube字幕
- [danhilse/notion_mcp](https://github.com/danhilse/notion_mcp) 🐍 ☁️ - 与Notion API集成，管理个人待办事项列表
- [rusiaaman/wcgw](https://github.com/rusiaaman/wcgw/blob/main/src/wcgw/client/mcp_server/Readme.md) 🐍 🏠 - 自动化shell执行、计算机控制和编码代理。（Mac）
- [reeeeemo/ancestry-mcp](https://github.com/reeeeemo/ancestry-mcp) 🐍 🏠 - 允许AI读取.ged文件和基因数据
- [sirmews/apple-notes-mcp](https://github.com/sirmews/apple-notes-mcp) 🐍 🏠 - 允许AI读取本地Apple Notes数据库（仅限macOS）
- [anjor/coinmarket-mcp-server](https://github.com/anjor/coinmarket-mcp-server) 🐍 🏠 - Coinmarket API集成，用于获取加密货币列表和报价
- [suekou/mcp-notion-server](https://github.com/suekou/mcp-notion-server) 📇 🏠 - 与Notion API交互
- [amidabuddha/unichat-mcp-server](https://github.com/amidabuddha/unichat-mcp-server) 🐍/📇 ☁️ - 使用MCP协议通过工具或预定义的提示发送请求给OpenAI、MistralAI、Anthropic、xAI或Google AI。需要供应商API密钥
- [g0t4/mcp-server-commands](https://github.com/g0t4/mcp-server-commands) 📇 🏠 - 执行命令并包括其输出。工具和提示。
- [evalstate/mcp-miro](https://github.com/evalstate/mcp-miro) 📇 ☁️ - 访问MIRO白板，批量创建和读取项目。需要REST API的OAUTH密钥。
- [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) 🐍 ☁️ - Confluence工作区的自然语言搜索和内容访问
- [pyroprompts/any-chat-completions-mcp](https://github.com/pyroprompts/any-chat-completions-mcp) - 与任何其他OpenAI SDK兼容的聊天完成API对话，例如Perplexity、Groq、xAI等
- [anaisbetts/mcp-installer](https://github.com/anaisbetts/mcp-installer) 🐍 🏠 -  一个MCP服务器，可以为您安装其他MCP服务器
- [tanigami/mcp-server-perplexity](https://github.com/tanigami/mcp-server-perplexity) 🐍 ☁️ - 与 Perplexity API 交互。
- [future-audiences/wikimedia-enterprise-model-context-protocol](https://gitlab.wikimedia.org/repos/future-audiences/wikimedia-enterprise-model-context-protocol) 🐍 ☁️  - 维基百科文章查找 API

## 框架

- [Genkit MCP](https://github.com/firebase/genkit/tree/main/js/plugins/mcp) 📇 – 提供[Genkit](https://github.com/firebase/genkit/tree/main)与模型上下文协议（MCP）之间的集成。
- [@modelcontextprotocol/server-langchain](https://github.com/rectalogic/langchain-mcp) 🐍 - 提供LangChain中的MCP工具调用支持，允许将MCP工具集成到LangChain工作流中。
- [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go) 🏎️ - 用于构建MCP服务器和客户端的Golang SDK。
- [FastMCP](https://github.com/jlowin/fastmcp) 🐍 - 一个用于在Python中构建MCP服务器的高级框架。
- [mcp-rs-template](https://github.com/linux-china/mcp-rs-template) 🦀 - Rust的MCP CLI服务器模板

## 客户端

- [SecretiveShell/MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge) 🐍 一个OpenAI中间件代理，用于在任何现有的OpenAI兼容客户端中使用MCP。
- [3choff/MCP-Chatbot](https://github.com/3choff/mcp-chatbot) 一个简单但功能强大的⭐CLI聊天机器人，它将工具服务器与任何与OpenAI兼容的LLM API集成。
- [zed-industries/zed](https://github.com/zed-industries/zed) 来自Atom创作者的多人协作代码编辑器。
- [firebase/genkit](https://github.com/firebase/genkit) 代理和数据转换框架。
- [continuedev/continue](https://github.com/continuedev/continue) vscode自动补全和聊天工具（支持完整功能）。

## 提示和技巧

### 官方提示关于 LLM 如何使用 MCP

想向 Claude 询问模型上下文协议相关技术吗？

创建一个项目，然后将此文件添加到其中：

https://modelcontextprotocol.io/llms-full.txt

现在 Claude 可以回答有关编写 MCP 服务器及其工作原理的问题

- https://www.reddit.com/r/ClaudeAI/comments/1h3g01r/want_to_ask_claude_about_model_context_protocol/

## 收藏历史

<a href="https://star-history.com/#punkpeye/awesome-mcp-servers&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date" />
 </picture>
</a>
