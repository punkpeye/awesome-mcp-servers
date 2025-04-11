# Awesome MCP Servers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![ไทย](https://img.shields.io/badge/Thai-Click-blue)](README-th.md)
[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![繁體中文](https://img.shields.io/badge/繁體中文-點擊查看-orange)](README-zh_TW.md)
[![简体中文](https://img.shields.io/badge/简体中文-点击查看-orange)](README-zh.md)
[![日本語](https://img.shields.io/badge/日本語-クリック-青)](README-ja.md)
[![한국어](https://img.shields.io/badge/한국어-클릭-yellow)](README-ko.md)
[![Discord](https://img.shields.io/discord/1312302100125843476?logo=discord&label=discord)](https://glama.ai/mcp/discord)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/mcp?style=flat&logo=reddit&label=subreddit)](https://www.reddit.com/r/mcp/)

A curated list of awesome Model Context Protocol (MCP) servers.

* [What is MCP?](#what-is-mcp)
* [Clients](#clients)
* [Tutorials](#tutorials)
* [Community](#community)
* [Legend](#legend)
* [Server Implementations](#server-implementations)
* [Frameworks](#frameworks)
* [Utilities](#utilities)
* [Tips & Tricks](#tips-and-tricks)

## What is MCP?

[MCP](https://modelcontextprotocol.io/) is an open protocol that enables AI models to securely interact with local and remote resources through standardized server implementations. This list focuses on production-ready and experimental MCP servers that extend AI capabilities through file access, database connections, API integrations, and other contextual services.

## Clients

Checkout [awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients/) and [glama.ai/mcp/clients](https://glama.ai/mcp/clients).

> [!TIP]
> [Glama Chat](https://glama.ai/chat) is a multi-modal AI client with MCP support & [AI gateway](https://glama.ai/gateway).

## Tutorials

* [Model Context Protocol (MCP) Quickstart](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
* [Setup Claude Desktop App to Use a SQLite Database](https://youtu.be/wxCCzo9dGj0)

## Community

* [r/mcp Reddit](https://www.reddit.com/r/mcp)
* [Discord Server](https://glama.ai/mcp/discord)

## Legend

* 🎖️ – official implementation
* programming language
  * 🐍 – Python codebase
  * 📇 – TypeScript codebase
  * 🏎️ – Go codebase
  * 🦀 – Rust codebase
  * #️⃣ - C# Codebase
  * ☕ - Java codebase
* scope
  * ☁️ - Cloud Service
  * 🏠 - Local Service
  * 📟 - Embedded Systems
* operating system
  * 🍎 – For macOS
  * 🪟 – For Windows
  * 🐧 - For Linux

> [!NOTE]
> Confused about Local 🏠 vs Cloud ☁️?
> * Use local when MCP server is talking to a locally installed software, e.g. taking control over Chrome browser.
> * Use network when MCP server is talking to remote APIs, e.g. weather API.

## Server Implementations

> [!NOTE]
> We now have a [web-based directory](https://glama.ai/mcp/servers) that is synced with the repository.

* 🔗 - [Aggregators](#aggregators)
* 🎨 - [Art & Culture](#art-and-culture)
* 📂 - [Browser Automation](#browser-automation)
* ☁️ - [Cloud Platforms](#cloud-platforms)
* 👨‍💻 - [Code Execution](#code-execution)
* 🤖 - [Coding Agents](#coding-agents)
* 🖥️ - [Command Line](#command-line)
* 💬 - [Communication](#communication)
* 👤 - [Customer Data Platforms](#customer-data-platforms)
* 🗄️ - [Databases](#databases)
* 📊 - [Data Platforms](#data-platforms)
* 🛠️ - [Developer Tools](#developer-tools)
* 🧮 - [Data Science Tools](#data-science-tools)
* 📟 - [Embedded system](#embedded-system)
* 📂 - [File Systems](#file-systems)
* 💰 - [Finance & Fintech](#finance--fintech)
* 🎮 - [Gaming](#gaming)
* 🧠 - [Knowledge & Memory](#knowledge--memory)
* 🗺️ - [Location Services](#location-services)
* 🎯 - [Marketing](#marketing)
* 📊 - [Monitoring](#monitoring)
* 🔎 - [Search & Data Extraction](#search)
* 🔒 - [Security](#security)
* 🏃 - [Sports](#sports)
* 🎧 - [Support & Service Management](#support-and-service-management)
* 🌎 - [Translation Services](#translation-services)
* 🚆 - [Travel & Transportation](#travel-and-transportation)
* 🔄 - [Version Control](#version-control)
* 🛠️ - [Other Tools and Integrations](#other-tools-and-integrations)


### 🔗 <a name="aggregators"></a>Aggregators

Servers for accessing many apps and tools through a single MCP server.

- [julien040/anyquery](https://github.com/julien040/anyquery) 🏎️ 🏠 ☁️ - Query more than 40 apps with one binary using SQL. It can also connect to your PostgreSQL, MySQL, or SQLite compatible database. Local-first and private by design.
- [PipedreamHQ/pipedream](https://github.com/PipedreamHQ/pipedream/tree/master/modelcontextprotocol) ☁️ 🏠 - Connect with 2,500 APIs with 8,000+ prebuilt tools, and manage servers for your users, in your own app.
- [OpenMCP](https://github.com/wegotdocs/open-mcp) 📇 🏠 🍎 🪟 🐧 - Turn a web API into an MCP server in 10 seconds and add it to the open source registry: https://open-mcp.org
- [VeriTeknik/pluggedin-mcp-proxy](https://github.com/VeriTeknik/pluggedin-mcp-proxy)  📇 🏠 - A comprehensive proxy server that combines multiple MCP servers into a single interface with extensive visibility features. It provides discovery and management of tools, prompts, resources, and templates across servers, plus a playground for debugging when building MCP servers.
- [MetaMCP](https://github.com/metatool-ai/metatool-app) 📇 ☁️ 🏠 🍎 🪟 🐧 - MetaMCP is the one unified middleware MCP server that manages your MCP connections with GUI.

### 🎨 <a name="art-and-culture"></a>Art & Culture

Access and explore art collections, cultural heritage, and museum databases. Enables AI models to search and analyze artistic and cultural content.

- [abhiemj/manim-mcp-server](https://github.com/abhiemj/manim-mcp-server) 🐍 🏠 🪟 🐧 - A local MCP server that generates animations using Manim.
- [burningion/video-editing-mcp](https://github.com/burningion/video-editing-mcp) 🐍 - Add, Analyze, Search, and Generate Video Edits from your Video Jungle Collection
- [djalal/quran-mcp-server](https://github.com/djalal/quran-mcp-server) 📇 ☁️ MCP server to interact with Quran.com corpus via the official REST API v4.
- [r-huijts/rijksmuseum-mcp](https://github.com/r-huijts/rijksmuseum-mcp) 📇 ☁️ - Rijksmuseum API integration for artwork search, details, and collections
- [r-huijts/oorlogsbronnen-mcp](https://github.com/r-huijts/oorlogsbronnen-mcp) 📇 ☁️ - Oorlogsbronnen (War Sources) API integration for accessing historical WWII records, photographs, and documents from the Netherlands (1940-1945)
- [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) 🐍 - MCP server integration for DaVinci Resolve providing powerful tools for video editing, color grading, media management, and project control
- [yuna0x0/anilist-mcp](https://github.com/yuna0x0/anilist-mcp) 📇 ☁️ - A MCP server integrating AniList API for anime and manga information
- [diivi/aseprite-mcp](https://github.com/diivi/aseprite-mcp) 🐍 🏠 - MCP server using the Aseprite API to create pixel art


### 📂 <a name="browser-automation"></a>Browser Automation

Web content access and automation capabilities. Enables searching, scraping, and processing web content in AI-friendly formats.

- [34892002/bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js) 📇 🏠 - A MCP server that supports searching for Bilibili content. Provides LangChain integration examples and test scripts.
- [automatalabs/mcp-server-playwright](https://github.com/Automata-Labs-team/MCP-Server-Playwright) 🐍 - An MCP server for browser automation using Playwright
- [blackwhite084/playwright-plus-python-mcp](https://github.com/blackwhite084/playwright-plus-python-mcp) 🐍 - An MCP python server using Playwright for browser automation,more suitable for llm
- [browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) 🎖️ 📇 - Automate browser interactions in the cloud (e.g. web navigation, data extraction, form filling, and more)
- [browsermcp/mcp](https://github.com/browsermcp/mcp) 📇 🏠 - Automate your local Chrome browser
- [co-browser/browser-use-mcp-server](https://github.com/co-browser/browser-use-mcp-server) 🐍 - browser-use packaged as an MCP server with SSE transport. includes a dockerfile to run chromium in docker + a vnc server.
- [executeautomation/playwright-mcp-server](https://github.com/executeautomation/mcp-playwright) 📇 - An MCP server using Playwright for browser automation and webscrapping
- [eyalzh/browser-control-mcp](https://github.com/eyalzh/browser-control-mcp) 📇 🏠 - An MCP server paired with a browser extension that enables LLM clients to control the user's browser (Firefox).
- [fradser/mcp-server-apple-reminders](https://github.com/FradSer/mcp-server-apple-reminders) 📇 🏠 🍎 - An MCP server for interacting with Apple Reminders on macOS
- [getrupt/ashra-mcp](https://github.com/getrupt/ashra-mcp) 🐍 🏠 - Extract structured data from any website. Just prompt and get JSON.
- [kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) 📇 ☁️ - Fetch YouTube subtitles and transcripts for AI analysis
- [kimtth/mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing) 🐍 🏠 - A `minimal` server/client MCP implementation using Azure OpenAI and Playwright.
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) - Official Microsoft Playwright MCP server, enabling LLMs to interact with web pages through structured accessibility snapshots
- [modelcontextprotocol/server-puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) 📇 🏠 - Browser automation for web scraping and interaction
- [ndthanhdev/mcp-browser-kit](https://github.com/ndthanhdev/mcp-browser-kit) 📇 🏠 - An MCP Server for interacting with manifest v2 compatible browsers.
- [pskill9/web-search](https://github.com/pskill9/web-search) 📇 🏠 - An MCP server that enables free web searching using Google search results, with no API keys required.
- [recursechat/mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts) 📇 🏠 🍎 - An MCP Server Integration with Apple Shortcuts

### ☁️ <a name="cloud-platforms"></a>Cloud Platforms

Cloud platform service integration. Enables management and interaction with cloud infrastructure and services.

- [alexbakers/mcp-ipfs](https://github.com/alexbakers/mcp-ipfs) 📇 ☁️ - upload and manipulation of IPFS storage
- [alexei-led/aws-mcp-server](https://github.com/alexei-led/aws-mcp-server) 🐍 ☁️ - A lightweight but powerful server that enables AI assistants to execute AWS CLI commands, use Unix pipes, and apply prompt templates for common AWS tasks in a safe Docker environment with multi-architecture support
- [alexei-led/k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server) 🐍 - A lightweight yet robust server that empowers AI assistants to securely execute Kubernetes CLI commands (`kubectl`, `helm`, `istioctl`, and `argocd`) using Unix pipes in a safe Docker environment with multi-architecture support.
- [bright8192/esxi-mcp-server](https://github.com/bright8192/esxi-mcp-server) 🐍 ☁️ - A VMware ESXi/vCenter management server based on MCP (Model Control Protocol), providing simple REST API interfaces for virtual machine management.
- [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) 🎖️ 📇 ☁️ - Integration with Cloudflare services including Workers, KV, R2, and D1
- [flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) - 📇 ☁️/🏠 Typescript implementation of Kubernetes cluster operations for pods, deployments, services.
- [hardik-id/azure-resource-graph-mcp-server](https://github.com/hardik-id/azure-resource-graph-mcp-server) - 📇 ☁️/🏠 - A Model Context Protocol server for querying and analyzing Azure resources at scale using Azure Resource Graph, enabling AI assistants to explore and monitor Azure infrastructure.
- [jdubois/azure-cli-mcp](https://github.com/jdubois/azure-cli-mcp) - A wrapper around the Azure CLI command line that allows you to talk directly to Azure
- [johnneerdael/netskope-mcp](https://github.com/johnneerdael/netskope-mcp) ☁️ - An MCP to give access to all Netskope Private Access components within a Netskope Private Access environments including detailed setup information and LLM examples on usage.
- [johnneerdael/netskope-mcp](https://github.com/johnneerdael/netskope-mcp) 🔒 ☁️ - An MCP to give access to all Netskope Private Access components within a Netskope Private Access environments including detailed setup information and LLM examples on usage.
- [manusa/Kubernetes MCP Server](https://github.com/manusa/kubernetes-mcp-server) - 🏎️ 🏠 A powerful Kubernetes MCP server with additional support for OpenShift. Besides providing CRUD operations for **any** Kubernetes resource, this server provides specialized tools to interact with your cluster.
- [nwiizo/tfmcp](https://github.com/nwiizo/tfmcp) - 🦀 🏠 - A Terraform MCP server allowing AI assistants to manage and operate Terraform environments, enabling reading configurations, analyzing plans, applying configurations, and managing Terraform state.
- [rohitg00/kubectl-mcp-server](https://github.com/rohitg00/kubectl-mcp-server) - 🐍 ☁️/🏠 A Model Context Protocol (MCP) server for Kubernetes that enables AI assistants like Claude, Cursor, and others to interact with Kubernetes clusters through natural language.
- [strowk/mcp-k8s-go](https://github.com/strowk/mcp-k8s-go) - 🏎️ ☁️/🏠 Kubernetes cluster operations through MCP
- [thunderboltsid/mcp-nutanix](https://github.com/thunderboltsid/mcp-nutanix) - 🏎️ 🏠/☁️ Go-based MCP Server for interfacing with Nutanix Prism Central resources.
- [weibaohui/k8m](https://github.com/weibaohui/k8m) - 🏎️ ☁️/🏠 Provides MCP multi-cluster Kubernetes management and operations, featuring a management interface, logging, and nearly 50 built-in tools covering common DevOps and development scenarios. Supports both standard and CRD resources.
- [weibaohui/kom](https://github.com/weibaohui/kom) - 🏎️ ☁️/🏠 Provides MCP multi-cluster Kubernetes management and operations. It can be integrated as an SDK into your own project and includes nearly 50 built-in tools covering common DevOps and development scenarios. Supports both standard and CRD resources.
- [wenhuwang/mcp-k8s-eye](https://github.com/wenhuwang/mcp-k8s-eye) 🏎️ ☁️/🏠 MCP Server for kubernetes management, and analyze your cluster, application health
- [erikhoward/adls-mcp-server](https://github.com/erikhoward/adls-mcp-server) - 🐍 ☁️/🏠 MCP Server for Azure Data Lake Storage. It can perform manage containers, read/write/upload/download operations on container files and manage file metadata.
- [silenceper/mcp-k8s](https://github.com/silenceper/mcp-k8s) 🏎️ ☁️/🏠 MCP-K8S is an AI-driven Kubernetes resource management tool that allows users to operate any resources in Kubernetes clusters through natural language interaction, including native resources (like Deployment, Service) and custom resources (CRD). No need to memorize complex commands - just describe your needs, and AI will accurately execute the corresponding cluster operations, greatly enhancing the usability of Kubernetes.

### 👨‍💻 <a name="code-execution"></a>Code Execution

Code execution servers. Allow LLMs to execute code in a secure environment, e.g. for coding agents.

- [pydantic/pydantic-ai/mcp-run-python](https://github.com/pydantic/pydantic-ai/tree/main/mcp-run-python) 🐍🏠- Run Python code in a secure sandbox via MCP tool calls
- [yepcode/mcp-server-js](https://github.com/yepcode/mcp-server-js) 🎖️ 📇 ☁️ - Execute any LLM-generated code in a secure and scalable sandbox environment and create your own MCP tools using JavaScript or Python, with full support for NPM and PyPI packages

### 🤖 <a name="coding-agents"></a>Coding Agents

Full coding agents that enable LLMs to read, edit, and execute code and solve general programming tasks completely autonomously.

- [oraios/serena](https://github.com/oraios/serena)🐍🏠 - A fully-featured coding agent that relies on symbolic code operations by using language servers.
- [ezyang/codemcp](https://github.com/ezyang/codemcp) 🐍🏠 - Coding agent with basic read, write and command line tools.
- [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) 📇🏠 - Enhanced file-system and search tools, commands and prompts specific for coding.

### 🖥️ <a name="command-line"></a>Command Line

Run commands, capture output and otherwise interact with shells and command line tools.

- [ferrislucas/iterm-mcp](https://github.com/ferrislucas/iterm-mcp) 🖥️ 🛠️ 💬 - A Model Context Protocol server that provides access to iTerm. You can run commands and ask questions about what you see in the iTerm terminal.
- [g0t4/mcp-server-commands](https://github.com/g0t4/mcp-server-commands) 📇 🏠 - Run any command with `run_command` and `run_script` tools.
- [maxim-saplin/mcp_safe_local_python_executor](https://github.com/maxim-saplin/mcp_safe_local_python_executor) - Safe Python interpreter based on HF Smolagents `LocalPythonExecutor`
- [MladenSU/cli-mcp-server](https://github.com/MladenSU/cli-mcp-server) 🐍 🏠 - Command line interface with secure execution and customizable security policies
- [OthmaneBlial/term_mcp_deepseek](https://github.com/OthmaneBlial/term_mcp_deepseek) 🐍 🏠 - A DeepSeek MCP-like Server for Terminal
- [tumf/mcp-shell-server](https://github.com/tumf/mcp-shell-server) - A secure shell command execution server implementing the Model Context Protocol (MCP)
- [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) 📇 🏠 🍎 🪟 🐧 - A swiss-army-knife that can manage/execute programs and read/write/search/edit code and text files.

### 💬 <a name="communication"></a>Communication

Integration with communication platforms for message management and channel operations. Enables AI models to interact with team communication tools.

- [AbdelStark/nostr-mcp](https://github.com/AbdelStark/nostr-mcp) ☁️ - A Nostr MCP server that allows to interact with Nostr, enabling posting notes, and more.
- [adhikasp/mcp-twikit](https://github.com/adhikasp/mcp-twikit) 🐍 ☁️ - Interact with Twitter search and timeline
- [agentmail-toolkit/mcp](https://github.com/agentmail-to/agentmail-toolkit/tree/main/mcp) 🐍 💬 - An MCP server to create inboxes on the fly to send, receive, and take actions on email. We aren't AI agents for email, but email for AI Agents.
- [arpitbatra123/mcp-googletasks](https://github.com/arpitbatra123/mcp-googletasks) 📇 ☁️ - An MCP server to interface with the Google Tasks API
- [carterlasalle/mac_messages_mcp](https://github.com/carterlasalle/mac_messages_mcp) 🏠 🍎 🚀 - An MCP server that securely interfaces with your iMessage database via the Model Context Protocol (MCP), allowing LLMs to query and analyze iMessage conversations. It includes robust phone number validation, attachment processing, contact management, group chat handling, and full support for sending and receiving messages.
- [chaindead/telegram-mcp](https://github.com/chaindead/telegram-mcp) 🏎️ 🏠 - Telegram API integration for accessing user data, managing dialogs (chats, channels, groups), retrieving messages, and handling read status
- [elie222/inbox-zero](https://github.com/elie222/inbox-zero/tree/main/apps/mcp-server) 🐍 ☁️ - An MCP server for Inbox Zero. Adds functionality on top of Gmail like finding out which emails you need to reply to or need to follow up on.
- [gotoolkits/wecombot](https://github.com/gotoolkits/mcp-wecombot-server.git) 🚀 ☁️ - An MCP server application that sends various types of messages to the WeCom group robot.
- [hannesrudolph/imessage-query-fastmcp-mcp-server](https://github.com/hannesrudolph/imessage-query-fastmcp-mcp-server) 🐍 🏠 🍎 - An MCP server that provides safe access to your iMessage database through Model Context Protocol (MCP), enabling LLMs to query and analyze iMessage conversations with proper phone number validation and attachment handling
- [jagan-shanmugam/mattermost-mcp-host](https://github.com/jagan-shanmugam/mattermost-mcp-host) 🐍 🏠 - A MCP server along with MCP host that provides access to Mattermost teams, channels and messages. MCP host is integrated as a bot in Mattermost with access to MCP servers that can be configured. 
- [lharries/whatsapp-mcp](https://github.com/lharries/whatsapp-mcp) 🐍 ☁️ - An MCP server for WhatsApp, search and send through pesonal and group messages
- [lharries/whatsapp-mcp](https://github.com/lharries/whatsapp-mcp) 🐍 🏎️ - An MCP server for searching your personal WhatsApp messages, contacts and sending messages to individuals or groups
- [MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite) 🐍 ☁️ - Integration with gmail and Google Calendar.
- [modelcontextprotocol/server-bluesky](https://github.com/keturiosakys/bluesky-context-server) 📇 ☁️ - Bluesky instance integration for querying and interaction
- [modelcontextprotocol/server-slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack) 📇 ☁️ - Slack workspace integration for channel management and messaging
- [sawa-zen/vrchat-mcp](https://github.com/sawa-zen/vrchat-mcp) - 📇 🏠 This is an MCP server for interacting with the VRChat API. You can retrieve information about friends, worlds, avatars, and more in VRChat.
- [takumi0706/google-calendar-mcp](https://github.com/takumi0706/google-calendar-mcp) 📇 ☁️ - An MCP server to interface with the Google Calendar API. Based on TypeScript.
- [teddyzxcv/ntfy-mcp](https://github.com/teddyzxcv/ntfy-mcp) - The MCP server that keeps you informed by sending the notification on phone using ntfy
- [userad/didlogic_mcp](https://github.com/UserAd/didlogic_mcp) 🐍 ☁️ - An MCP server for [DIDLogic](https://didlogic.com). Adds functionality to manage SIP endpoints, numbers and destinations.
- [zcaceres/gtasks-mcp](https://github.com/zcaceres/gtasks-mcp) 📇 ☁️ - An MCP server to Manage Google Tasks
- [InditexTech/mcp-teams-server](https://github.com/InditexTech/mcp-teams-server) 🐍 ☁️ - MCP server that integrates Microsoft Teams messaging (read, post, mention, list members and threads)
- [softeria/ms-365-mcp-server](https://github.com/softeria/ms-365-mcp-server) 📇 ☁️ - MCP server that connects to the whole Microsoft 365 suite using Graph API (including mail, files, Excel, calendar)

### 👤 <a name="customer-data-platforms"></a>Customer Data Platforms

Provides access to customer profiles inside of customer data platforms

- [iaptic/mcp-server-iaptic](https://github.com/iaptic/mcp-server-iaptic) 🎖️ 📇 ☁️ - Connect with [iaptic](https://www.iaptic.com) to ask about your Customer Purchases, Transaction data and App Revenue statistics.
- [OpenDataMCP/OpenDataMCP](https://github.com/OpenDataMCP/OpenDataMCP) 🐍 ☁️ - Connect any Open Data to any LLM with Model Context Protocol.
- [sergehuber/inoyu-mcp-unomi-server](https://github.com/sergehuber/inoyu-mcp-unomi-server) 📇 ☁️ - An MCP server to access and updates profiles on an Apache Unomi CDP server.
- [tinybirdco/mcp-tinybird](https://github.com/tinybirdco/mcp-tinybird) 🐍 ☁️ - An MCP server to interact with a Tinybird Workspace from any MCP client.

### 🗄️ <a name="databases"></a>Databases

Secure database access with schema inspection capabilities. Enables querying and analyzing data with configurable security controls including read-only access.

- [Aiven-Open/mcp-aiven](https://github.com/Aiven-Open/mcp-aiven) - 🐍 ☁️ 🎖️ -  Navigate your [Aiven projects](https://go.aiven.io/mcp-server) and interact with the PostgreSQL®, Apache Kafka®, ClickHouse® and OpenSearch® services
- [alexanderzuev/supabase-mcp-server](https://github.com/alexander-zuev/supabase-mcp-server) - Supabase MCP Server with support for SQL query execution and database exploration tools
- [aliyun/alibabacloud-tablestore-mcp-server](https://github.com/aliyun/alibabacloud-tablestore-mcp-server) ☕ 🐍 ☁️ - MCP service for Tablestore, features include adding documents, semantic search for documents based on vectors and scalars, RAG-friendly, and serverless.
- [benborla29/mcp-server-mysql](https://github.com/benborla/mcp-server-mysql) ☁️ 🏠 - MySQL database integration in NodeJS with configurable access controls and schema inspection
- [bytebase/dbhub](https://github.com/bytebase/dbhub) 📇 🏠 – Universal database MCP server supporting mainstream databases.
- [c4pt0r/mcp-server-tidb](https://github.com/c4pt0r/mcp-server-tidb) 🐍 ☁️ - TiDB database integration with schema inspection and query capabilities
- [Canner/wren-engine](https://github.com/Canner/wren-engine) 🐍 🦀 🏠 - The Semantic Engine for Model Context Protocol(MCP) Clients and AI Agents
- [centralmind/gateway](https://github.com/centralmind/gateway) 🏎️ 🏠 🍎 🪟 - MCP and MCP SSE Server that automatically generate API based on database schema and data. Supports PostgreSQL, Clickhouse, MySQL, Snowflake, BigQuery, Supabase
- [chroma-core/chroma-mcp](https://github.com/chroma-core/chroma-mcp) 🎖️ 🐍 ☁️ 🏠 - Chroma MCP server to access local and cloud Chroma instances for retrieval capabilities
- [ClickHouse/mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse) 🐍 ☁️ - ClickHouse database integration with schema inspection and query capabilities
- [confluentinc/mcp-confluent](https://github.com/confluentinc/mcp-confluent) 🐍 ☁️ - Confluent integration to interact with Confluent Kafka and Confluent Cloud REST APIs.
- [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) 🐍 🏠 - MCP Server implementation that provides Elasticsearch interaction
- [Dataring-engineering/mcp-server-trino](https://github.com/Dataring-engineering/mcp-server-trino) 🐍 ☁️ - Trino MCP Server to query and access data from Trino Clusters.
- [designcomputer/mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server) 🐍 🏠 - MySQL database integration with configurable access controls, schema inspection, and comprehensive security guidelines
- [domdomegg/airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server) 📇 🏠 - Airtable database integration with schema inspection, read and write capabilities
- [edwinbernadus/nocodb-mcp-server](https://github.com/edwinbernadus/nocodb-mcp-server) 📇 ☁️ - Nocodb database integration, read and write capabilities
- [ergut/mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server) 📇 ☁️ - Server implementation for Google BigQuery integration that enables direct BigQuery database access and querying capabilities
- [f4ww4z/mcp-mysql-server](https://github.com/f4ww4z/mcp-mysql-server) 🐍 🏠 - Node.js-based MySQL database integration that provides secure MySQL database operations
- [fireproof-storage/mcp-database-server](https://github.com/fireproof-storage/mcp-database-server) 📇 ☁️ - Fireproof ledger database with multi-user sync
- [FreePeak/db-mcp-server](https://github.com/FreePeak/db-mcp-server) 🏎️ 🏠 – A high-performance multi-database MCP server built with Golang, supporting MySQL & PostgreSQL (NoSQL coming soon). Includes built-in tools for query execution, transaction management, schema exploration, query building, and performance analysis, with seamless Cursor integration for enhanced database workflows.
- [furey/mongodb-lens](https://github.com/furey/mongodb-lens) 📇 🏠 - MongoDB Lens: Full Featured MCP Server for MongoDB Databases
- [gannonh/firebase-mcp](https://github.com/gannonh/firebase-mcp) 🔥 ⛅️ - Firebase services including Auth, Firestore and Storage.
- [get-convex/convex-backend](https://stack.convex.dev/convex-mcp-server) 📇 ☁️ - Convex database integration to introspect tables, functions, and run oneoff queries ([Source](https://github.com/get-convex/convex-backend/blob/main/npm-packages/convex/src/cli/mcp.ts))
- [GreptimeTeam/greptimedb-mcp-server](https://github.com/GreptimeTeam/greptimedb-mcp-server) 🐍 🏠 - MCP Server for querying GreptimeDB.
- [hannesrudolph/sqlite-explorer-fastmcp-mcp-server](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server) 🐍 🏠 - An MCP server that provides safe, read-only access to SQLite databases through Model Context Protocol (MCP). This server is built with the FastMCP framework, which enables LLMs to explore and query SQLite databases with built-in safety features and query validation.
- [idoru/influxdb-mcp-server](https://github.com/idoru/influxdb-mcp-server) 📇 ☁️ 🏠 - Run queries against InfluxDB OSS API v2.
- [isaacwasserman/mcp-snowflake-server](https://github.com/isaacwasserman/mcp-snowflake-server) 🐍 ☁️ - Snowflake integration implementing read and (optional) write operations as well as insight tracking
- [joshuarileydev/supabase-mcp-server](https://github.com/joshuarileydev/supabase) - Supabase MCP Server for managing and creating projects and organisations in Supabase
- [jovezhong/mcp-timeplus](https://github.com/jovezhong/mcp-timeplus) 🐍 ☁️ - MCP server for Apache Kafka and Timeplus. Able to list Kafka topics, poll Kafka messages, save Kafka data locally and query streaming data with SQL via Timeplus
- [KashiwaByte/vikingdb-mcp-server](https://github.com/KashiwaByte/vikingdb-mcp-server) 🐍 ☁️ - VikingDB integration with collection and index introduction, vector store and search capabilities.
- [kiliczsh/mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server) 📇 🏠 - A Model Context Protocol Server for MongoDB
- [ktanaka101/mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb) 🐍 🏠 - DuckDB database integration with schema inspection and query capabilities
- [LucasHild/mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery) 🐍 ☁️ - BigQuery database integration with schema inspection and query capabilities
- [mcp-server-jdbc](https://github.com/quarkiverse/quarkus-mcp-servers/tree/main/jdbc) ☕ 🏠 - Connect to any JDBC-compatible database and query, insert, update, delete, and more.
- [memgraph/mcp-memgraph](https://github.com/memgraph/mcp-memgraph) 🐍 🏠 - Memgraph MCP Server - includes a tool to run a query against Memgraph and a schema resource.
- [modelcontextprotocol/server-postgres](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) 📇 🏠 - PostgreSQL database integration with schema inspection and query capabilities
- [modelcontextprotocol/server-sqlite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) 🐍 🏠 - SQLite database operations with built-in analysis features
- [neo4j-contrib/mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j) 🐍 🏠 - Model Context Protocol with Neo4j (Run queries, Knowledge Graph Memory, Manaage Neo4j Aura Instances)
- [neondatabase/mcp-server-neon](https://github.com/neondatabase/mcp-server-neon) 📇 ☁️ — An MCP Server for creating and managing Postgres databases using Neon Serverless Postgres
- [niledatabase/nile-mcp-server](https://github.com/niledatabase/nile-mcp-server) MCP server for Nile's Postgres platform - Manage and query Postgres databases, tenants, users, auth using LLMs
- [openlink/mcp-server-odbc](https://github.com/OpenLinkSoftware/mcp-odbc-server) 🐍 🏠 - An MCP server for generic Database Management System (DBMS) Connectivity via the Open Database Connectivity (ODBC) protocol
- [openlink/mcp-server-sqlalchemy](https://github.com/OpenLinkSoftware/mcp-sqlalchemy-server) 🐍 🏠 - An MCP server for generic Database Management System (DBMS) Connectivity via SQLAlchemy using Python ODBC (pyodbc)
- [pab1it0/adx-mcp-server](https://github.com/pab1it0/adx-mcp-server) 🐍 ☁️ - Query and analyze Azure Data Explorer databases
- [pab1it0/prometheus-mcp-server](https://github.com/pab1it0/prometheus-mcp-server) 🐍 ☁️ -  Query and analyze Prometheus, open-source monitoring system.
- [qdrant/mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant) 🐍 🏠 - A Qdrant MCP server
- [QuantGeekDev/mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp) 📇 🏠 - MongoDB integration that enables LLMs to interact directly with databases.
- [rashidazarang/airtable-mcp](https://github.com/rashidazarang/airtable-mcp) 🐍 ☁️ - Connect AI tools directly to Airtable. Query, create, update, and delete records using natural language. Features include base management, table operations, schema manipulation, record filtering, and data migration through a standardized MCP interface.
- [runekaagaard/mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy) 🐍 🏠 - Universal SQLAlchemy-based database integration supporting PostgreSQL, MySQL, MariaDB, SQLite, Oracle, MS SQL Server and many more databases. Features schema and relationship inspection, and large dataset analysis capabilities.
- [sirmews/mcp-pinecone](https://github.com/sirmews/mcp-pinecone) 🐍 ☁️ - Pinecone integration with vector search capabilities
- [supabase-community/supabase-mcp](https://github.com/supabase-community/supabase-mcp) 🎖️ 📇 ☁️ - Official Supabase MCP server to connect AI assistants directly with your Supabase project and allows them to perform tasks like managing tables, fetching config, and querying data.
- [TheRaLabs/legion-mcp](https://github.com/TheRaLabs/legion-mcp) 🐍 🏠 Universal database MCP server supporting multiple database types including PostgreSQL, Redshift, CockroachDB, MySQL, RDS MySQL, Microsoft SQL Server, BigQuery, Oracle DB, and SQLite.
- [tinybirdco/mcp-tinybird](https://github.com/tinybirdco/mcp-tinybird) 🐍 ☁️ - Tinybird integration with query and API capabilities
- [tradercjz/dolphindb-mcp-server](https://github.com/tradercjz/dolphindb-mcp-server) 🐍 ☁️ - TDolphinDB database integration with schema inspection and query capabilities
- [weaviate/mcp-server-weaviate](https://github.com/weaviate/mcp-server-weaviate) 🐍 📇 ☁️ - An MCP Server to connect to your Weaviate collections as a knowledge base as well as using Weaviate as a chat memory store.
- [XGenerationLab/xiyan_mcp_server](https://github.com/XGenerationLab/xiyan_mcp_server) 📇 ☁️ — An MCP server that supports fetching data from a database using natural language queries, powered by XiyanSQL as the text-to-SQL LLM.
- [xing5/mcp-google-sheets](https://github.com/xing5/mcp-google-sheets) 🐍 ☁️ - A Model Context Protocol server for interacting with Google Sheets. This server provides tools to create, read, update, and manage spreadsheets through the Google Sheets API.
- [Zhwt/go-mcp-mysql](https://github.com/Zhwt/go-mcp-mysql) 🏎️ 🏠 – Easy to use, zero dependency MySQL MCP server built with Golang with configurable readonly mode and schema inspection.
- [zilliztech/mcp-server-milvus](https://github.com/zilliztech/mcp-server-milvus) 🐍 🏠 ☁️ - MCP Server for Milvus / Zilliz, making it possible to interact with your database.

### 📊 <a name="data-platforms"></a>Data Platforms

Data Platforms for data integration, transformation and pipeline orchestration.

- [flowcore/mcp-flowcore-platform](https://github.com/flowcore-io/mcp-flowcore-platform) 🎖️📇☁️🏠 - Interact with Flowcore to perform actions, ingest data, and analyse, cross reference and utilise any data in your data cores, or in public data cores; all with human language.
- [JordiNei/mcp-databricks-server](https://github.com/JordiNeil/mcp-databricks-server) - Connect to Databricks API, allowing LLMs to run SQL queries, list jobs, and get job status.
- [jwaxman19/qlik-mcp](https://github.com/jwaxman19/qlik-mcp) 📇 ☁️ - MCP Server for Qlik Cloud API that enables querying applications, sheets, and extracting data from visualizations with comprehensive authentication and rate limiting support.
- [keboola/keboola-mcp-server](https://github.com/keboola/keboola-mcp-server) - interact with Keboola Connection Data Platform. This server provides tools for listing and accessing data from Keboola Storage API.

### 💻 <a name="developer-tools"></a>Developer Tools

Tools and integrations that enhance the development workflow and environment management.

- [21st-dev/Magic-MCP](https://github.com/21st-dev/magic-mcp) - Create crafted UI components inspired by the best 21st.dev design engineers.
- [Hypersequent/qasphere-mcp](https://github.com/Hypersequent/qasphere-mcp) 🎖️ 📇 ☁️ - Integration with [QA Sphere](https://qasphere.com/) test management system, enabling LLMs to discover, summarize, and interact with test cases directly from AI-powered IDEs
- [admica/FileScopeMCP](https://github.com/admica/FileScopeMCP) 🐍 📇 🦀 - Analyzes your codebase identifying important files based on dependency relationships. Generates diagrams and importance scores, helping AI assistants understand the codebase.
- [ambar/simctl-mcp](https://github.com/ambar/simctl-mcp) 📇 🏠 🍎 A MCP server implementation for iOS Simulator control.
- [api7/apisix-mcp](https://github.com/api7/apisix-mcp) 🎖️ 📇 🏠 MCP Server that support for querying and managing all resource in [Apache APISIX](https://github.com/apache/apisix).
- [automation-ai-labs/mcp-link](https://github.com/automation-ai-labs/mcp-link) 🏎️ 🏠 - Seamlessly Integrate Any API with AI Agents (with OpenAPI Schema)
- [davidlin2k/pox-mcp-server](https://github.com/davidlin2k/pox-mcp-server) 🐍 🏠 - MCP server for the POX SDN controller to provides network control and management capabilities.
- [Comet-ML/Opik-MCP](https://github.com/comet-ml/opik-mcp) 🎖️ 📇 ☁️ 🏠 - Use natural language to explore LLM observability, traces, and monitoring data captured by Opik.
- [davidlin2k/pox-mcp-server](https://github.com/davidlin2k/pox-mcp-server) 🐍 🏠 - MCP server for the POX SDN controller to provides network control and management capabilities. 
- [delano/postman-mcp-server](https://github.com/delano/postman-mcp-server) 📇 ☁️ - Interact with [Postman API](https://www.postman.com/postman/postman-public-workspace/)
- [flipt-io/mcp-server-flipt](https://github.com/flipt-io/mcp-server-flipt) 📇 🏠 - Enable AI assistants to interact with your feature flags in [Flipt](https://flipt.io).
- [GLips/Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) 📇 🏠 - Provide coding agents direct access to Figma data to help them one-shot design implementation.
- [gofireflyio/firefly-mcp](https://github.com/gofireflyio/firefly-mcp) 🎖️ 📇 ☁️ - Integrates, discovers, manages, and codifies cloud resources with [Firefly](https://firefly.ai).
- [Govcraft/rust-docs-mcp-server](https://github.com/Govcraft/rust-docs-mcp-server) 🦀 🏠 - Provides up-to-date documentation context for a specific Rust crate to LLMs via an MCP tool, using semantic search (embeddings) and LLM summarization.
- [haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server) 🐍 🏠 - An Excel manipulation server providing workbook creation, data operations, formatting, and advanced features (charts, pivot tables, formulae).
- [higress-group/higress-ops-mcp-server](https://github.com/higress-group/higress-ops-mcp-server) 🐍 🏠 - MCP server that provides comprehensive tools for managing [Higress](https://github.com/alibaba/higress) gateway configurations and operations.
- [hijaz/postmancer](https://github.com/hijaz/postmancer) 📇 🏠 - A MCP server for replacing Rest Clients like Postman/Insomnia, by allowing your LLM to maintain and use api collections.
- [hloiseaufcms/mcp-gopls](https://github.com/hloiseaufcms/mcp-gopls) 🏎️ 🏠 - A MCP server for interacting with [Go's Language Server Protocol (gopls)](https://github.com/golang/tools/tree/master/gopls) and benefit from advanced Go code analysis features.
- [hungthai1401/bruno-mcp](https://github.com/hungthai1401/bruno-mcp) 📇 🏠 - A MCP server for interacting with [Bruno API Client](https://www.usebruno.com/).
- [hyperb1iss/droidmind](https://github.com/hyperb1iss/droidmind) 🐍 🏠 - Control Android devices with AI through MCP, enabling device control, debugging, system analysis, and UI automation with a comprehensive security framework.
- [IlyaGulya/gradle-mcp-server](https://github.com/IlyaGulya/gradle-mcp-server) 🏠 - Gradle integration using the Gradle Tooling API to inspect projects, execute tasks, and run tests with per-test result reporting
- [InhiblabCore/mcp-image-compression](https://github.com/InhiblabCore/mcp-image-compression) 🐍 🏠 - MCP server for local compression of various image formats.
- [ios-simulator-mcp](https://github.com/joshuayoes/ios-simulator-mcp) 📇 🏠 🍎 - A Model Context Protocol (MCP) server for interacting with iOS simulators. This server allows you to interact with iOS simulators by getting information about them, controlling UI interactions, and inspecting UI elements.
- [InditexTech/mcp-server-simulator-ios-idb](https://github.com/InditexTech/mcp-server-simulator-ios-idb) 📇 🏠 🍎 - A Model Context Protocol (MCP) server that enables LLMs to interact with iOS simulators (iPhone, iPad, etc.) through natural language commands.
- [j4c0bs/mcp-server-sql-analyzer](https://github.com/j4c0bs/mcp-server-sql-analyzer) 🐍 - MCP server that provides SQL analysis, linting, and dialect conversion using [SQLGlot](https://github.com/tobymao/sqlglot)
- [jasonjmcghee/claude-debugs-for-you](https://github.com/jasonjmcghee/claude-debugs-for-you) 📇 🏠 - An MCP Server and VS Code Extension which enables (language agnostic) automatic debugging via breakpoints and expression evaluation.
- [jetbrains/mcpProxy](https://github.com/JetBrains/mcpProxy) 🎖️ 📇 🏠 - Connect to JetBrains IDE
- [qainsights/jmeter-mcp-server](https://github.com/QAInsights/jmeter-mcp-server) 🐍 🏠 - JMeter MCP Server for performance testing
- [Jktfe/serveMyAPI](https://github.com/Jktfe/serveMyAPI) 📇 🏠 🍎 - A personal MCP (Model Context Protocol) server for securely storing and accessing API keys across projects using the macOS Keychain.
- [joshuarileydev/app-store-connect-mcp-server](https://github.com/JoshuaRileyDev/app-store-connect-mcp-server) 📇 🏠 - An MCP server to communicate with the App Store Connect API for iOS Developers
- [joshuarileydev/simulator-mcp-server](https://github.com/JoshuaRileyDev/simulator-mcp-server) 📇 🏠 - An MCP server to control iOS Simulators
- [qainsights/k6-mcp-server](https://github.com/QAInsights/k6-mcp-server) 🐍 🏠 - Grafana k6 MCP Server for performance testing
- [lamemind/mcp-server-multiverse](https://github.com/lamemind/mcp-server-multiverse) 📇 🏠 🛠️ - A middleware server that enables multiple isolated instances of the same MCP servers to coexist independently with unique namespaces and configurations.
- [langfuse/mcp-server-langfuse](https://github.com/langfuse/mcp-server-langfuse) 🐍 🏠 - MCP server to access and manage LLM application prompts created with [Langfuse]([https://langfuse.com/](https://langfuse.com/docs/prompts/get-started)) Prompt Management.
- [mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp) 📇 🏠 🐧 🍎 - MCP Server for Android/iOS application and device automation, development and app scraping. Simulator/Emulator/Physical devices like iPhone, Google Pixel, Samsung supported. 
- [qainsights/locust-mcp-server](https://github.com/QAInsights/locust-mcp-server) 🐍 🏠 - Locust MCP Server for performance testing
- [mrexodia/user-feedback-mcp](https://github.com/mrexodia/user-feedback-mcp) 🐍 🏠 - Simple MCP Server to enable a human-in-the-loop workflow in tools like Cline and Cursor.
- [OctoMind-dev/octomind-mcp](https://github.com/OctoMind-dev/octomind-mcp) - 📇 ☁️ lets your preferred AI agent create & run fully managed [Octomind](https://www.octomind.dev/) end-to-end tests from your codebase or other data sources like Jira, Slack or TestRail.
- [pskill9/website-downloader](https://github.com/pskill9/website-downloader) 🗄️ 🚀 - This MCP server provides a tool to download entire websites using wget. It preserves the website structure and converts links to work locally.
- [utensils/mcp-nixos](https://github.com/utensils/mcp-nixos) 🐍 🏠 - MCP server providing accurate information about NixOS packages, system options, Home Manager configurations, and nix-darwin macOS settings to prevent AI hallucinations.
- [QuantGeekDev/docker-mcp](https://github.com/QuantGeekDev/docker-mcp) 🏎️ 🏠 - Docker container management and operations through MCP
- [ckreiling/mcp-server-docker](https://github.com/ckreiling/mcp-server-docker) 🐍 🏠 - Integrate with Docker to manage containers, images, volumes, and networks.
- [r-huijts/xcode-mcp-server](https://github.com/r-huijts/xcode-mcp-server) 📇 🏠 🍎 - Xcode integration for project management, file operations, and build automation
- [ReAPI-com/mcp-openapi](https://github.com/ReAPI-com/mcp-openapi) 📇 🏠 - MCP server that lets LLMs know everything about your OpenAPI specifications to discover, explain and generate code/mock data
- [Rootly-AI-Labs/Rootly-MCP-server](https://github.com/Rootly-AI-Labs/Rootly-MCP-server) 🎖️🐍☁️🍎 - MCP server for the incident management platform [Rootly](https://rootly.com/).
- [sammcj/mcp-package-version](https://github.com/sammcj/mcp-package-version) 📇 🏠 - An MCP Server to help LLMs suggest the latest stable package versions when writing code.
* [sapientpants/deepsource-mcp-server](https://github.com/sapientpants/deepsource-mcp-server) 📇 ☁️ 🏠 - A Model Context Protocol (MCP) server that integrates with DeepSource to provide AI assistants with access to code quality metrics, issues, and quality gate statuses
- [sapientpants/sonarqube-mcp-server](https://github.com/sapientpants/sonarqube-mcp-server) 🦀 ☁️ 🏠 - A Model Context Protocol (MCP) server that integrates with SonarQube to provide AI assistants with access to code quality metrics, issues, and quality gate statuses
- [SDGLBL/mcp-claude-code](https://github.com/SDGLBL/mcp-claude-code) 🐍 🏠 - An implementation of Claude Code capabilities using MCP, enabling AI code understanding, modification, and project analysis with comprehensive tool support.
- [snaggle-ai/openapi-mcp-server](https://github.com/snaggle-ai/openapi-mcp-server) 🏎️ 🏠 - Connect any HTTP/REST API server using an Open API spec (v3)
- [stass/lldb-mcp](https://github.com/stass/lldb-mcp) 🐍 🏠 🐧 🍎 - A MCP server for LLDB enabling AI binary and core file analysis, debugging, disassembling.
- [tumf/mcp-text-editor](https://github.com/tumf/mcp-text-editor) 🐍 🏠 - A line-oriented text file editor. Optimized for LLM tools with efficient partial file access to minimize token usage.
- [vivekvells/mcp-pandoc](https://github.com/vivekVells/mcp-pandoc) 🗄️ 🚀 - MCP server for seamless document format conversion using Pandoc, supporting Markdown, HTML, PDF, DOCX (.docx), csv and more.
- [VSCode Devtools](https://github.com/biegehydra/BifrostMCP) 📇 - Connect to VSCode ide and use semantic tools like `find_usages`
- [xcodebuild](https://github.com/ShenghaiWang/xcodebuild) 🍎 Build iOS Xcode workspace/project and feed back errors to llm.
- [xzq.xu/jvm-mcp-server](https://github.com/xzq-xu/jvm-mcp-server) 📇 🏠  - An implementation project of a JVM-based MCP (Model Context Protocol) server.
- [yangkyeongmo@/mcp-server-apache-airflow](https://github.com/yangkyeongmo/mcp-server-apache-airflow) 🐍 🏠 - MCP server that connects to [Apache Airflow](https://airflow.apache.org/) using official client.
- [YuChenSSR/mindmap-mcp-server](https://github.com/YuChenSSR/mindmap-mcp-server) 🐍 🏠 - A Model Context Protocol (MCP) server for generating a beautiful interactive mindmap.
- [YuChenSSR/multi-ai-advisor](https://github.com/YuChenSSR/multi-ai-advisor-mcp) 📇 🏠 - A Model Context Protocol (MCP) server that queries multiple Ollama models and combines their responses, providing diverse AI perspectives on a single question.
- [yWorks/mcp-typescribe](https://github.com/yWorks/mcp-typescribe) 📇 🏠 - MCP server that provides Typescript API information efficiently to the agent to enable it to work with untrained APIs
- [zcaceres/fetch-mcp](https://github.com/zcaceres/fetch-mcp) 📇 🏠 - An MCP server to flexibly fetch JSON, text, and HTML data
- [zenml-io/mcp-zenml](https://github.com/zenml-io/mcp-zenml) 🐍 🏠 ☁️ - An MCP server to connect with your [ZenML](https://www.zenml.io) MLOps and LLMOps pipelines
- [idosal/git-mcp](https://github.com/idosal/git-mcp) 📇 ☁️ - [gitmcp.io](https://gitmcp.io/) is a generic remote MCP server to connect to ANY [GitHub](https://www.github.com) repository or project for documentation
- [tgeselle/bugsnag-mcp](https://github.com/tgeselle/bugsnag-mcp) 📇 ☁️ - An MCP server for interacting with [Bugsnag](https://www.bugsnag.com/)
- [jordandalton/restcsv-mcp-server](https://github.com/JordanDalton/RestCsvMcpServer) 📇 ☁️ - An MCP server for CSV files.

### 🧮 <a name="data-science-tools"></a>Data Science Tools

Integrations and tools designed to simplify data exploration, analysis and enhance data science workflows.

- [ChronulusAI/chronulus-mcp](https://github.com/ChronulusAI/chronulus-mcp) 🐍 ☁️ - Predict anything with Chronulus AI forecasting and prediction agents.
- [reading-plus-ai/mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration) 🐍 ☁️ - Enables autonomous data exploration on .csv-based datasets, providing intelligent insights with minimal effort.
- [zcaceres/markdownify-mcp](https://github.com/zcaceres/markdownify-mcp) 📇 🏠 - An MCP server to convert almost any file or web content into Markdown
- [jjsantos01/jupyter-notebook-mcp](https://github.com/jjsantos01/jupyter-notebook-mcp) 🐍 🏠 - connects Jupyter Notebook to Claude AI, allowing Claude to directly interact with and control Jupyter Notebooks.

### 📟 <a name="embedded-system"></a>Embedded System

Provides access to documentation and shortcuts for working on embedded devices.

- [horw/esp-mcp](https://github.com/horw/esp-mcp) 📟 - Workflow for fixing build issues in ESP32 series chips using ESP-IDF.

### 📂 <a name="file-systems"></a>File Systems

Provides direct access to local file systems with configurable permissions. Enables AI models to read, write, and manage files within specified directories.

- [cyberchitta/llm-context.py](https://github.com/cyberchitta/llm-context.py) 🐍 🏠 - Share code context with LLMs via MCP or clipboard
- [exoticknight/mcp-file-merger](https://github.com/exoticknight/mcp-file-merger) 🏎️ 🏠 - File merger tool, suitable for AI chat length limits.
- [filesystem@quarkiverse/quarkus-mcp-servers](https://github.com/quarkiverse/quarkus-mcp-servers/tree/main/filesystem) ☕ 🏠 - A filesystem allowing for browsing and editing files implemented in Java using Quarkus. Available as jar or native image.
- [hmk/box-mcp-server](https://github.com/hmk/box-mcp-server) 📇 ☁️ - Box integration for listing, reading and searching files
- [mamertofabian/mcp-everything-search](https://github.com/mamertofabian/mcp-everything-search) 🐍 🏠 🪟 - Fast Windows file search using Everything SDK
- [mark3labs/mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server) 🏎️ 🏠 - Golang implementation for local file system access.
- [microsoft/markitdown](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp) 🎖️ 🐍 🏠 - MCP tool access to MarkItDown -- a library that converts many file formats (local or remote) to Markdown for LLM consumption.
- [modelcontextprotocol/server-filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) 📇 🏠 - Direct local file system access.
- [modelcontextprotocol/server-google-drive](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive) 📇 ☁️ - Google Drive integration for listing, reading, and searching files
- [Xuanwo/mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal) 🐍 🏠 ☁️ - Access any storage with Apache OpenDAL™

### 💰 <a name="finance--fintech"></a>Finance & Fintech

Financial data access and analysis tools. Enables AI models to work with market data, trading platforms, and financial information.

- [anjor/coinmarket-mcp-server](https://github.com/anjor/coinmarket-mcp-server) 🐍 ☁️ - Coinmarket API integration to fetch cryptocurrency listings and quotes
- [bankless/onchain-mcp](https://github.com/Bankless/onchain-mcp/) 📇 ☁️ - Bankless Onchain API to interact with smart contracts, query transaction and token information
- [base/base-mcp](https://github.com/base/base-mcp) 🎖️ 📇 ☁️ - Base Network integration for onchain tools, allowing interaction with Base Network and Coinbase API for wallet management, fund transfers, smart contracts, and DeFi operations
- [berlinbra/alpha-vantage-mcp](https://github.com/berlinbra/alpha-vantage-mcp) 🐍 ☁️ - Alpha Vantage API integration to fetch both stock and crypto information
- [ahnlabio/bicscan-mcp](https://github.com/ahnlabio/bicscan-mcp) 🎖️ 🐍 ☁️ - Risk score / asset holdings of EVM blockchain address (EOA, CA, ENS) and even domain names.
- [bitteprotocol/mcp](https://github.com/BitteProtocol/mcp) 📇 - Bitte Protocol integration to run AI Agents on several blockchains.
- [chargebee/mcp](https://github.com/chargebee/agentkit/tree/main/modelcontextprotocol) 🎖️ 📇 ☁️ - MCP Server that connects AI agents to [Chargebee platform](https://www.chargebee.com/).
- [codex-data/codex-mcp](https://github.com/Codex-Data/codex-mcp) 🎖️ 📇 ☁️ - [Codex API](https://www.codex.io) integration for real-time enriched blockchain and market data on 60+ networks
- [coinpaprika/dexpaprika-mcp](https://github.com/chargebee/agentkit/tree/main/modelcontextprotocol) 🎖️ 📇 ☁️ 🍎 🪟 🐧 - Coinpaprika's DexPaprika MCP server exposes high-performance [DexPaprika API](https://docs.dexpaprika.com) covering 20+ chains and 5M+ tokens with real time pricing, liquidity pool data & historical OHLCV data, providing AI agents standardized access to comprehensive market data through Model Context Protocol.
- [ferdousbhai/investor-agent](https://github.com/ferdousbhai/investor-agent) 🐍 ☁️ - Yahoo Finance integration to fetch stock market data including options recommendations
- [ferdousbhai/tasty-agent](https://github.com/ferdousbhai/tasty-agent) 🐍 ☁️ - Tastyworks API integration to handle trading activities on Tastytrade
- [getalby/nwc-mcp-server](https://github.com/getalby/nwc-mcp-server) 📇 🏠 - Bitcoin Lightning wallet integration powered by Nostr Wallet Connect
- [heurist-network/heurist-mesh-mcp-server](https://github.com/heurist-network/heurist-mesh-mcp-server) 🎖️ ⛅️ 🏠 🐍 - Access specialized web3 AI agents for blockchain analysis, smart contract security auditing, token metrics evaluation, and on-chain interactions through the Heurist Mesh network. Provides comprehensive tools for DeFi analysis, NFT valuation, and transaction monitoring across multiple blockchains
- [kukapay/crypto-feargreed-mcp](https://github.com/kukapay/crypto-feargreed-mcp) 🐍 ☁️ -  Providing real-time and historical Crypto Fear & Greed Index data.
- [kukapay/crypto-indicators-mcp](https://github.com/kukapay/crypto-indicators-mcp) 🐍 ☁️ - An MCP server providing a range of cryptocurrency technical analysis indicators and strategie.
- [kukapay/crypto-portfolio-mcp](https://github.com/kukapay/crypto-portfolio-mcp) 🐍 ☁️ - An MCP server for tracking and managing cryptocurrency portfolio allocations.
- [kukapay/crypto-sentiment-mcp](https://github.com/kukapay/crypto-sentiment-mcp) 🐍 ☁️ - An MCP server that delivers cryptocurrency sentiment analysis to AI agents.
- [kukapay/cryptopanic-mcp-server](https://github.com/kukapay/cryptopanic-mcp-server) 🐍 ☁️ - Providing latest cryptocurrency news to AI agents, powered by CryptoPanic.
- [kukapay/dune-analytics-mcp](https://github.com/kukapay/dune-analytics-mcp) 🐍 ☁️ -  A mcp server that bridges Dune Analytics data to AI agents.
- [kukapay/freqtrade-mcp](https://github.com/kukapay/freqtrade-mcp) 🐍 ☁️ - An MCP server that integrates with the Freqtrade cryptocurrency trading bot.
- [kukapay/jupiter-mcp](https://github.com/kukapay/jupiter-mcp) 🐍 ☁️ - An MCP server for executing token swaps on the Solana blockchain using Jupiter's new Ultra API.
- [kukapay/pancakeswap-poolspy-mcp](https://github.com/kukapay/pancakeswap-poolspy-mcp) 🐍 ☁️ -  An MCP server that tracks newly created pools on Pancake Swap.
- [kukapay/rug-check-mcp](https://github.com/kukapay/rug-check-mcp) 🐍 ☁️ - An MCP server that detects potential risks in Solana meme tokens.
- [kukapay/thegraph-mcp](https://github.com/kukapay/thegraph-mcp) 🐍 ☁️ -  An MCP server that powers AI agents with indexed blockchain data from The Graph.
- [kukapay/token-minter-mcp](https://github.com/kukapay/token-minter-mcp) 🐍 ☁️ -  An MCP server providing tools for AI agents to mint ERC-20 tokens across multiple blockchains.
- [kukapay/token-revoke-mcp](https://github.com/kukapay/token-revoke-mcp) 🐍 ☁️ - An MCP server for checking and revoking ERC-20 token allowances across multiple blockchains.
- [kukapay/uniswap-poolspy-mcp](https://github.com/kukapay/uniswap-poolspy-mcp) 🐍 ☁️ -  An MCP server that tracks newly created liquidity pools on Uniswap across multiple blockchains.
- [kukapay/uniswap-trader-mcp](https://github.com/kukapay/uniswap-trader-mcp) 🐍 ☁️ -  An MCP server for AI agents to automate token swaps on Uniswap DEX across multiple blockchains.
- [kukapay/whale-tracker-mcp](https://github.com/kukapay/whale-tracker-mcp) 🐍 ☁️ -  A mcp server for tracking cryptocurrency whale transactions.
- [laukikk/alpaca-mcp](https://github.com/laukikk/alpaca-mcp) 🐍 ☁️ - An MCP Server for the Alpaca trading API to manage stock and crypto portfolios, place trades, and access market data.
- [longportapp/openapi](https://github.com/longportapp/openapi/tree/main/mcp) - 🐍 ☁️ - LongPort OpenAPI provides real-time stock market data, provides AI access analysis and trading capabilities through MCP.
- [mcpdotdirect/evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server) 📇 ☁️ - Comprehensive blockchain services for 30+ EVM networks, supporting native tokens, ERC20, NFTs, smart contracts, transactions, and ENS resolution.
- [mcpdotdirect/starknet-mcp-server](https://github.com/mcpdotdirect/starknet-mcp-server) 📇 ☁️ - Comprehensive Starknet blockchain integration with support for native tokens (ETH, STRK), smart contracts, StarknetID resolution, and token transfers.
- [minhyeoky/mcp-server-ledger](https://github.com/minhyeoky/mcp-server-ledger) 🐍 🏠 -  A ledger-cli integration for managing financial transactions and generating reports.
- [openMF/mcp-mifosx](https://github.com/openMF/mcp-mifosx) ☁️ 🏠 -  A core banking integration for managing clients, loans, savings, shares, financial transactions and generating financial reports.
- [narumiruna/yfinance-mcp](https://github.com/narumiruna/yfinance-mcp) 🐍 ☁️ - An MCP server that uses yfinance to obtain information from Yahoo Finance.
- [pwh-pwh/coin-mcp-server](https://github.com/pwh-pwh/coin-mcp-server) 🐍 ☁️ -  Bitget API to fetch cryptocurrency price.
- [QuantGeekDev/coincap-mcp](https://github.com/QuantGeekDev/coincap-mcp) 📇 ☁️ - Real-time cryptocurrency market data integration using CoinCap's public API, providing access to crypto prices and market information without API keys
- [SaintDoresh/Crypto-Trader-MCP-ClaudeDesktop](https://github.com/SaintDoresh/Crypto-Trader-MCP-ClaudeDesktop.git) 🐍 ☁️ - An MCP tool that provides cryptocurrency market data using the CoinGecko API.
- [SaintDoresh/YFinance-Trader-MCP-ClaudeDesktop](https://github.com/SaintDoresh/YFinance-Trader-MCP-ClaudeDesktop.git) 🐍 ☁️ - An MCP tool that provides stock market data and analysis using the Yahoo Finance API.
- [unibaseio/beeper-mcp](https://github.com/unibaseio/beeper-mcp) 🐍 - Beeper provides transactions on BSC, including balance/token transfers, token swaps in Pancakeswap and beeper reward claims.
- [janswist/mcp-dexscreener](https://github.com/janswist/mcp-dexscreener) 📇 ☁️ - Real-time on-chain market prices using open and free Dexscreener API

### 🎮 <a name="gaming"></a>Gaming

Integration with gaming related data, game engines, and services
- [CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity) 📇 #️⃣ 🏠 - MCP Server for Unity3d Game Engine integration for game development
- [Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp) 📇 🏠 - A MCP server for interacting with the Godot game engine, providing tools for editing, running, debugging, and managing scenes in Godot projects.
- [pab1ito/chess-mcp](https://github.com/pab1it0/chess-mcp) 🐍 ☁️ - Access Chess.com player data, game records, and other public information through standardized MCP interfaces, allowing AI assistants to search and analyze chess information.
- [rishijatia/fantasy-pl-mcp](https://github.com/rishijatia/fantasy-pl-mcp/) 🐍 ☁️ - An MCP server for real-time Fantasy Premier League data and analysis tools.

### 🧠 <a name="knowledge--memory"></a>Knowledge & Memory

Persistent memory storage using knowledge graph structures. Enables AI models to maintain and query structured information across sessions.

- [CheMiguel23/MemoryMesh](https://github.com/CheMiguel23/MemoryMesh) 📇 🏠 - Enhanced graph-based memory with a focus on AI role-play and story generation
- [graphlit-mcp-server](https://github.com/graphlit/graphlit-mcp-server) 📇 ☁️ - Ingest anything from Slack, Discord, websites, Google Drive, Linear or GitHub into a Graphlit project - and then search and retrieve relevant knowledge within an MCP client like Cursor, Windsurf or Cline.
- [hannesrudolph/mcp-ragdocs](https://github.com/hannesrudolph/mcp-ragdocs) 🐍 🏠 - An MCP server implementation that provides tools for retrieving and processing documentation through vector search, enabling AI assistants to augment their responses with relevant documentation context
- [kaliaboi/mcp-zotero](https://github.com/kaliaboi/mcp-zotero) 📇 ☁️ - A connector for LLMs to work with collections and sources on your Zotero Cloud
- [mcp-summarizer](https://github.com/0xshellming/mcp-summarizer) 📕 ☁️ - AI Summarization MCP Server, Support for multiple content types: Plain text, Web pages, PDF documents, EPUB books, HTML content
- [mem0ai/mem0-mcp](https://github.com/mem0ai/mem0-mcp) 🐍 🏠 - A Model Context Protocol server for Mem0 that helps manage coding preferences and patterns, providing tools for storing, retrieving and semantically handling code implementations, best practices and technical documentation in IDEs like Cursor and Windsurf
- [modelcontextprotocol/server-memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) 📇 🏠 - Knowledge graph-based persistent memory system for maintaining context
- [pinecone-io/assistant-mcp](https://github.com/pinecone-io/assistant-mcp) 🎖️ 🦀 ☁️ - Connects to your Pinecone Assistant and gives the agent context from its knowledge engine.
- [topoteretes/cognee](https://github.com/topoteretes/cognee/tree/dev/cognee-mcp) 📇 🏠 - Memory manager for AI apps and Agents using various graph and vector stores and allowing ingestion from 30+ data sources
- [unibaseio/membase-mcp](https://github.com/unibaseio/membase-mcp) 📇 ☁️ - Save and query your agent memory in distributed way by Membase
- [entanglr/zettelkasten-mcp](https://github.com/entanglr/zettelkasten-mcp) 🐍 🏠 - A Model Context Protocol (MCP) server that implements the Zettelkasten knowledge management methodology, allowing you to create, link, and search atomic notes through Claude and other MCP-compatible clients.

### 🗺️ <a name="location-services"></a>Location Services

Location-based services and mapping tools. Enables AI models to work with geographic data, weather information, and location-based analytics.

- [briandconnelly/mcp-server-ipinfo](https://github.com/briandconnelly/mcp-server-ipinfo) 🐍 ☁️  - IP address geolocation and network information using IPInfo API
- [jagan-shanmugam/open-streetmap-mcp](https://github.com/jagan-shanmugam/open-streetmap-mcp) 🐍 🏠 - An OpenStreetMap MCP server with location-based services and geospatial data.
- [kukapay/nearby-search-mcp](https://github.com/kukapay/nearby-search-mcp) 🐍 ☁️ - An MCP server for nearby place searches with IP-based location detection.
- [modelcontextprotocol/server-google-maps](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps) 📇 ☁️ - Google Maps integration for location services, routing, and place details
- [QGIS MCP](https://github.com/jjsantos01/qgis_mcp) - connects QGIS Desktop to Claude AI through the MCP. This integration enables prompt-assisted project creation, layer loading, code execution, and more.
- [SaintDoresh/Weather-MCP-ClaudeDesktop](https://github.com/SaintDoresh/Weather-MCP-ClaudeDesktop.git) 🐍 ☁️ - An MCP tool that provides real-time weather data, forecasts, and historical weather information using the OpenWeatherMap API.
- [SecretiveShell/MCP-timeserver](https://github.com/SecretiveShell/MCP-timeserver) 🐍 🏠 - Access the time in any timezone and get the current local time
- [webcoderz/MCP-Geo](https://github.com/webcoderz/MCP-Geo) 🐍 🏠 - Geocoding MCP server for nominatim, ArcGIS, Bing

### 🎯 <a name="marketing"></a>Marketing

Tools for creating and editing marketing content, working with web meta data, product positioning, and editing guides.

- [Open Strategy Partners Marketing Tools](https://github.com/open-strategy-partners/osp_marketing_tools) 🐍 🏠 - A suite of marketing tools from Open Strategy Partners including writing style, editing codes, and product marketing value map creation.

### 📊 <a name="monitoring"></a>Monitoring

Access and analyze application monitoring data. Enables AI models to review error reports and performance metrics.

- [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) 🎖️ 🐍 🏠 ☁️ - Search dashboards, investigate incidents and query datasources in your Grafana instance
- [hyperb1iss/lucidity-mcp](https://github.com/hyperb1iss/lucidity-mcp) 🐍 🏠 - Enhance AI-generated code quality through intelligent, prompt-based analysis across 10 critical dimensions from complexity to security vulnerabilities
- [last9/last9-mcp-server](https://github.com/last9/last9-mcp-server) - Seamlessly bring real-time production context—logs, metrics, and traces—into your local environment to auto-fix code faster
- [metoro-io/metoro-mcp-server](https://github.com/metoro-io/metoro-mcp-server) 🎖️ 🏎️ ☁️ - Query and interact with kubernetes environments monitored by Metoro
- [MindscapeHQ/server-raygun](https://github.com/MindscapeHQ/mcp-server-raygun) 📇 ☁️ - Raygun API V3 integration for crash reporting and real user monitoring
- [modelcontextprotocol/server-sentry](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry) 🐍 ☁️ - Sentry.io integration for error tracking and performance monitoring
- [pydantic/logfire-mcp](https://github.com/pydantic/logfire-mcp) 🎖️ 🐍 ☁️ - Provides access to OpenTelemetry traces and metrics through Logfire
- [seekrays/mcp-monitor](https://github.com/seekrays/mcp-monitor) 🏎️ 🏠 - A system monitoring tool that exposes system metrics via the Model Context Protocol (MCP). This tool allows LLMs to retrieve real-time system information through an MCP-compatible interface.（support CPU、Memory、Disk、Network、Host、Process）

### 🔎 <a name="search"></a>Search & Data Extraction

- [0xdaef0f/job-searchoor](https://github.com/0xDAEF0F/job-searchoor) 📇 🏠 - An MCP server for searching job listings with filters for date, keywords, remote work options, and more.
- [ac3xx/mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi) 📇 ☁️ - Kagi search API integration
- [andybrandt/mcp-simple-arxiv](https://github.com/andybrandt/mcp-simple-arxiv) - 🐍 ☁️  MCP for LLM to search and read papers from arXiv
- [andybrandt/mcp-simple-pubmed](https://github.com/andybrandt/mcp-simple-pubmed) - 🐍 ☁️  MCP to search and read medical / life sciences papers from PubMed.
- [angheljf/nyt](https://github.com/angheljf/nyt) 📇 ☁️ - Search articles using the NYTimes API
- [apify/mcp-server-rag-web-browser](https://github.com/apify/mcp-server-rag-web-browser) 📇 ☁️ - An MCP server for Apify's open-source RAG Web Browser Actor to perform web searches, scrape URLs, and return content in Markdown.
- [Bigsy/Clojars-MCP-Server](https://github.com/Bigsy/Clojars-MCP-Server) 📇 ☁️ - Clojars MCP Server for upto date dependency information of Clojure libraries
- [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) ☁️ 🐍 - Search ArXiv research papers
- [chanmeng/google-news-mcp-server](https://github.com/ChanMeng666/server-google-news) 📇 ☁️ - Google News integration with automatic topic categorization, multi-language support, and comprehensive search capabilities including headlines, stories, and related topics through [SerpAPI](https://serpapi.com/).
- [ConechoAI/openai-websearch-mcp](https://github.com/ConechoAI/openai-websearch-mcp/) 🐍 🏠 ☁️ - This is a Python-based MCP server that provides OpenAI `web_search` build-in tool.
- [devflowinc/trieve](https://github.com/devflowinc/trieve/tree/main/clients/mcp-server) 🎖️ 📇 ☁️ 🏠 - Crawl, embed, chunk, search, and retrieve information from datasets through [Trieve](https://trieve.ai)
- [Dumpling-AI/mcp-server-dumplingai](https://github.com/Dumpling-AI/mcp-server-dumplingai) 🎖️ 📇 ☁️ - Access data, web scraping, and document conversion APIs by [Dumpling AI](https://www.dumplingai.com/)
- [erithwik/mcp-hn](https://github.com/erithwik/mcp-hn) 🐍 ☁️ - An MCP server to search Hacker News, get top stories, and more.
- [exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) 🎖️ 📇 ☁️ – A Model Context Protocol (MCP) server lets AI assistants like Claude use the Exa AI Search API for web searches. This setup allows AI models to get real-time web information in a safe and controlled way.
- [fatwang2/search1api-mcp](https://github.com/fatwang2/search1api-mcp) 📇 ☁️ - Search via search1api (requires paid API key)
- [genomoncology/biomcp](https://github.com/genomoncology/biomcp) 🐍 ☁️ - Biomedical research server providing access to PubMed, ClinicalTrials.gov, and MyVariant.info.
- [hellokaton/unsplash-mcp-server](https://github.com/hellokaton/unsplash-mcp-server)) 🐍 ☁️ - A MCP server for Unsplash image search.
- [Ihor-Sokoliuk/MCP-SearXNG](https://github.com/ihor-sokoliuk/mcp-searxng) 📇 🏠/☁️ - A Model Context Protocol Server for [SearXNG](https://docs.searxng.org)
- [jae-jae/fetcher-mcp](https://github.com/jae-jae/fetcher-mcp) 📇 🏠 - MCP server for fetching web page content using Playwright headless browser, supporting Javascript rendering and intelligent content extraction, and outputting Markdown or HTML format.
- [jae-jae/g-search-mcp](https://github.com/jae-jae/g-search-mcp) 📇 🏠 - A powerful MCP server for Google search that enables parallel searching with multiple keywords simultaneously.
- [leehanchung/bing-search-mcp](https://github.com/leehanchung/bing-search-mcp) 📇 ☁️ - Web search capabilities using Microsoft Bing Search API
- [kagisearch/kagimcp](https://github.com/kagisearch/kagimcp) ☁️ 📇 – Official Kagi Search MCP Server
- [kshern/mcp-tavily](https://github.com/kshern/mcp-tavily.git) ☁️ 📇 – Tavily AI search API
- [modelcontextprotocol/server-brave-search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) 📇 ☁️ - Web search capabilities using Brave's Search API
- [modelcontextprotocol/server-fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) 🐍 🏠 ☁️ - Efficient web content fetching and processing for AI consumption
- [mzxrai/mcp-webresearch](https://github.com/mzxrai/mcp-webresearch) 🔍📚 - Search Google and do deep web research on any topic
- [nickclyde/duckduckgo-mcp-server](https://github.com/nickclyde/duckduckgo-mcp-server) 🐍 ☁️ - Web search using DuckDuckGo
- [reading-plus-ai/mcp-server-deep-research](https://github.com/reading-plus-ai/mcp-server-deep-research) 📇 ☁️ - MCP server providing OpenAI/Perplexity-like autonomous deep research, structured query elaboration, and concise reporting.
- [SecretiveShell/MCP-searxng](https://github.com/SecretiveShell/MCP-searxng) 🐍 🏠 - An MCP Server to connect to searXNG instances
- [takashiishida/arxiv-latex-mcp](https://github.com/takashiishida/arxiv-latex-mcp) 🐍 ☁️ - Get the LaTeX source of arXiv papers to handle mathematical content and equations
- [the0807/GeekNews-MCP-Server](https://github.com/the0807/GeekNews-MCP-Server) 🐍 ☁️ - An MCP Server that retrieves and processes news data from the GeekNews site.
- [tinyfish-io/agentql-mcp](https://github.com/tinyfish-io/agentql-mcp) 🎖️ 📇 ☁️ - MCP server that provides [AgentQL](https://agentql.com)'s data extraction capabilities.
- [Tomatio13/mcp-server-tavily](https://github.com/Tomatio13/mcp-server-tavily) ☁️ 🐍 – Tavily AI search API
- [vectorize-io/vectorize-mcp-server](https://github.com/vectorize-io/vectorize-mcp-server/) ☁️ 📇 - [Vectorize](https://vectorize.io) MCP server for advanced retrieval, Private Deep Research, Anything-to-Markdown file extraction and text chunking.
- [zhsama/duckduckgo-mcp-server](https://github.com/zhsama/duckduckgo-mpc-server/) 📇 🏠 ☁️ - This is a TypeScript-based MCP server that provides DuckDuckGo search functionality.
- [zoomeye-ai/mcp_zoomeye](https://github.com/zoomeye-ai/mcp_zoomeye) 📇 ☁️ - Querying network asset information by ZoomEye MCP Server

### 🔒 <a name="security"></a>Security

- [13bm/GhidraMCP](https://github.com/13bm/GhidraMCP) 🐍 ☕ 🏠 - MCP server for integrating Ghidra with AI assistants. This plugin enables binary analysis, providing tools for function inspection, decompilation, memory exploration, and import/export analysis via the Model Context Protocol.
- [atomicchonk/roadrecon_mcp_server](https://github.com/atomicchonk/roadrecon_mcp_server) 🐍 🪟 🏠 MCP server for analyzing ROADrecon gather results from Azure tenant enumeration
- [BurtTheCoder/mcp-dnstwist](https://github.com/BurtTheCoder/mcp-dnstwist) 📇 🪟 ☁️ - MCP server for dnstwist, a powerful DNS fuzzing tool that helps detect typosquatting, phishing, and corporate espionage.
- [BurtTheCoder/mcp-maigret](https://github.com/BurtTheCoder/mcp-maigret) 📇 🪟 ☁️ - MCP server for maigret, a powerful OSINT tool that collects user account information from various public sources. This server provides tools for searching usernames across social networks and analyzing URLs.
- [BurtTheCoder/mcp-shodan](https://github.com/BurtTheCoder/mcp-shodan) 📇 🪟 ☁️ - MCP server for querying the Shodan API and Shodan CVEDB. This server provides tools for IP lookups, device searches, DNS lookups, vulnerability queries, CPE lookups, and more.
- [BurtTheCoder/mcp-virustotal](https://github.com/BurtTheCoder/mcp-virustotal) 📇 🪟 ☁️ - MCP server for querying the VirusTotal API. This server provides tools for scanning URLs, analyzing file hashes, and retrieving IP address reports.
- [fosdickio/binary_ninja_mcp](https://github.com/fosdickio/binary_ninja_mcp) 🐍 🏠 🍎 🪟 🐧 - A Binary Ninja plugin, MCP server, and bridge that seamlessly integrates [Binary Ninja](https://binary.ninja) with your favorite MCP client.  It enables you to automate the process of performing binary analysis and reverse engineering.
- [fr0gger/MCP_Security](https://github.com/fr0gger/MCP_Security) 📇 ☁️ - MCP server for querying the ORKL API. This server provides tools for fetching threat reports, analyzing threat actors, and retrieving intelligence sources.
- [qianniuspace/mcp-security-audit](https://github.com/qianniuspace/mcp-security-audit) 📇 ☁️ A powerful MCP (Model Context Protocol) Server that audits npm package dependencies for security vulnerabilities. Built with remote npm registry integration for real-time security checks.
- [semgrep/mcp](https://github.com/semgrep/mcp) 📇 ☁️ Allow AI agents to scan code for security vulnerabilites using [Semgrep](https://semgrep.dev).
- [mrexodia/ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp) 🐍 🏠 - MCP server for IDA Pro, allowing you to perform binary analysis with AI assistants. This plugin implement decompilation, disassembly and allows you to generate malware analysis reports automatically.
- [rad-security/mcp-server](https://github.com/rad-security/mcp-server) 📇 ☁️ - MCP server for RAD Security, providing AI-powered security insights for Kubernetes and cloud environments. This server provides tools for querying the Rad Security API and retrieving security findings, reports, runtime data and many more.
- [securityfortech/secops-mcp](https://github.com/securityfortech/secops-mcp) 🐍 🏠 - All-in-one security testing toolbox that brings together popular open source tools through a single MCP interface. Connected to an AI agent, it enables tasks like pentesting, bug bounty hunting, threat hunting, and more.
- [roadwy/cve-search_mcp](https://github.com/roadwy/cve-search_mcp) 🐍 🏠 - A Model Context Protocol (MCP) server for querying the CVE-Search API. This server provides comprehensive access to CVE-Search, browse vendor and product、get CVE per CVE-ID、get the last updated CVEs.
- [nickpending/mcp-recon](https://github.com/nickpending/mcp-recon) 🏎️ 🏠 - Conversational recon interface and MCP server powered by httpx and asnmap. Supports various reconnaissance levels for domain analysis, security header inspection, certificate analysis, and ASN lookup.
- [Gaffx/volatility-mcp](https://github.com/Gaffx/volatility-mcp) - MCP server for Volatility 3.x, allowing you to perform memory forensics analysis with AI assistant. Experience memory forensics without barriers as plugins like pslist and netscan become accessible through clean REST APIs and LLMs.

### 🏃 <a name="sports"></a>Sports

Tools for accessing sports-related data, results, and statistics.

- [r-huijts/firstcycling-mcp](https://github.com/r-huijts/firstcycling-mcp) 📇 ☁️ - Access cycling race data, results, and statistics through natural language. Features include retrieving start lists, race results, and rider information from firstcycling.com.
- [r-huijts/strava-mcp](https://github.com/r-huijts/strava-mcp) 📇 ☁️ - A Model Context Protocol (MCP) server that connects to Strava API, providing tools to access Strava data through LLMs
  
### 🎧 <a name="support-and-service-management"></a>Support & Service Management

Tools for managing customer support, IT service management, and helpdesk operations.

- [effytech/freshdesk-mcp](https://github.com/effytech/freshdesk_mcp) 🐍 ☁️ - MCP server that integrates with Freshdesk, enabling AI models to interact with Freshdesk modules and perform various support operations.
- [nguyenvanduocit/jira-mcp](https://github.com/nguyenvanduocit/jira-mcp) 🏎️ ☁️ - A Go-based MCP connector for Jira that enables AI assistants like Claude to interact with Atlassian Jira. This tool provides a seamless interface for AI models to perform common Jira operations including issue management, sprint planning, and workflow transitions.

### 🌎 <a name="translation-services"></a>Translation Services

Translation tools and services to enable AI assistants to translate content between different languages.

- [translated/lara-mcp](https://github.com/translated/lara-mcp) 🎖️ 📇 ☁️ - MCP Server for Lara Translate API, enabling powerful translation capabilities with support for language detection and context-aware translations.

### 🚆 <a name="travel-and-transportation"></a>Travel & Transportation

Access to travel and transportation information. Enables querying schedules, routes, and real-time travel data.

- [Airbnb MCP Server](https://github.com/openbnb-org/mcp-server-airbnb) 📇 ☁️ - Provides tools to search Airbnb and get listing details.
- [KyrieTangSheng/mcp-server-nationalparks](https://github.com/KyrieTangSheng/mcp-server-nationalparks) 📇 ☁️ - National Park Service API integration providing latest information of park details, alerts, visitor centers, campgrounds, and events for U.S. National Parks
- [NS Travel Information MCP Server](https://github.com/r-huijts/ns-mcp-server) 📇 ☁️ - Access Dutch Railways (NS) travel information, schedules, and real-time updates
- [pab1it0/tripadvisor-mcp](https://github.com/pab1it0/tripadvisor-mcp) 📇 🐍 - A MCP server that enables LLMs to interact with Tripadvisor API, supporting location data, reviews, and photos through standardized MCP interfaces

### 🔄 <a name="version-control"></a>Version Control

Interact with Git repositories and version control platforms. Enables repository management, code analysis, pull request handling, issue tracking, and other version control operations through standardized APIs.

- [adhikasp/mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest) 🐍 🏠 - Read and analyze GitHub repositories with your LLM
- [ddukbg/github-enterprise-mcp](https://github.com/ddukbg/github-enterprise-mcp) 📇 ☁️ 🏠 - MCP server for GitHub Enterprise API integration
- [gitea/gitea-mcp](https://gitea.com/gitea/gitea-mcp) 🎖️ 🏎️ ☁️ 🏠 🍎 🪟 🐧 - Interactive with Gitea instances with MCP.
- [kopfrechner/gitlab-mr-mcp](https://github.com/kopfrechner/gitlab-mr-mcp) 📇 ☁️ - Interact seamlessly with issues and merge requests of your GitLab projects.
- [modelcontextprotocol/server-git](https://github.com/modelcontextprotocol/servers/tree/main/src/git) 🐍 🏠 - Direct Git repository operations including reading, searching, and analyzing local repositories
- [modelcontextprotocol/server-github](https://github.com/modelcontextprotocol/servers/tree/main/src/github) 📇 ☁️ - GitHub API integration for repository management, PRs, issues, and more
- [modelcontextprotocol/server-gitlab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab) 📇 ☁️ 🏠 - GitLab platform integration for project management and CI/CD operations
- [oschina/mcp-gitee](https://github.com/oschina/gitee) 🏎️ ☁️ 🏠 - Gitee API integration, repository, issue, and pull request management, and more.
- [Tiberriver256/mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops) 📇 ☁️ - Azure DevOps integration for repository management, work items, and pipelines.

### 🛠️ <a name="other-tools-and-integrations"></a>Other Tools and Integrations

- [AbdelStark/bitcoin-mcp](https://github.com/AbdelStark/bitcoin-mcp) - ₿ A Model Context Protocol (MCP) server that enables AI models to interact with Bitcoin, allowing them to generate keys, validate addresses, decode transactions, query the blockchain, and more.
- [akseyh/bear-mcp-server](https://github.com/akseyh/bear-mcp-server) - Allows the AI to read from your Bear Notes (macOS only)
- [allenporter/mcp-server-home-assistant](https://github.com/allenporter/mcp-server-home-assistant) 🐍 🏠 - Expose all Home Assistant voice intents through a Model Context Protocol Server allowing home control.
- [Amazon Bedrock Nova Canvas](https://github.com/zxkane/mcp-server-amazon-bedrock) 📇 ☁️ - Use Amazon Nova Canvas model for image generation.
- [amidabuddha/unichat-mcp-server](https://github.com/amidabuddha/unichat-mcp-server) 🐍/📇 ☁️ - Send requests to OpenAI, MistralAI, Anthropic, xAI, Google AI or DeepSeek using MCP protocol via tool or predefined prompts. Vendor API key required
- [anaisbetts/mcp-installer](https://github.com/anaisbetts/mcp-installer) 🐍 🏠 -  An MCP server that installs other MCP servers for you.
- [anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube) 📇 ☁️ - Fetch YouTube subtitles
- [andybrandt/mcp-simple-openai-assistant](https://github.com/andybrandt/mcp-simple-openai-assistant) - 🐍 ☁️  MCP to talk to OpenAI assistants (Claude can use any GPT model as his assitant)
- [andybrandt/mcp-simple-timeserver](https://github.com/andybrandt/mcp-simple-timeserver) 🐍 🏠☁️ - An MCP server that allows checking local time on the client machine or current UTC time from an NTP server
- [anjor/coinmarket-mcp-server](https://github.com/anjor/coinmarket-mcp-server) 🐍 🏠 - Coinmarket API integration to fetch cryptocurrency listings and quotes
- [apify/actors-mcp-server](https://github.com/apify/actors-mcp-server) 📇 ☁️ - Use 3,000+ pre-built cloud tools, known as Actors, to extract data from websites, e-commerce, social media, search engines, maps, and more
- [apinetwork/piapi-mcp-server](https://github.com/apinetwork/piapi-mcp-server) 📇 ☁️ PiAPI MCP server makes user able to generate media content with Midjourney/Flux/Kling/Hunyuan/Udio/Trellis directly from Claude or any other MCP-compatible apps.
- [awkoy/replicate-flux-mcp](https://github.com/awkoy/replicate-flux-mcp) 📇 ☁️ - Provides the ability to generate images via Replicate's API.
- [awwaiid/mcp-server-taskwarrior](https://github.com/awwaiid/mcp-server-taskwarrior) 🏠 📇 - An MCP server for basic local taskwarrior usage (add, update, remove tasks)
- [baba786/phabricator-mcp-server](https://github.com/baba786/phabricator-mcp-server) 🐍 ☁️ - Interacting with Phabricator API
- [Badhansen/notion-mcp](https://github.com/Badhansen/notion-mcp) 🐍 ☁️ - A Model Context Protocol (MCP) server that integrates with Notion's API to manage personal todo lists efficiently.
- [bart6114/my-bear-mcp-server](https://github.com/bart6114/my-bear-mcp-server/) 📇 🏠 🍎 - Allows to read notes and tags for the Bear Note taking app, through a direct integration with Bear's sqlitedb.
- [billster45/mcp-chatgpt-responses](https://github.com/billster45/mcp-chatgpt-responses) 🐍 ☁️ - MCP server for Claude to talk to ChatGPT and use its web search capability.
- [blurrah/mcp-graphql](https://github.com/blurrah/mcp-graphql) 📇 ☁️ - Allows the AI to query GraphQL servers
- [calclavia/mcp-obsidian](https://github.com/calclavia/mcp-obsidian) 📇 🏠 - This is a connector to allow Claude Desktop (or any MCP client) to read and search any directory containing Markdown notes (such as an Obsidian vault).
- [chrishayuk/mcp-cli](https://github.com/chrishayuk/mcp-cli) 🐍 🏠 - Yet another CLI tool for testing MCP servers
- [danhilse/notion_mcp](https://github.com/danhilse/notion_mcp) 🐍 ☁️ - Integrates with Notion's API to manage personal todo lists
- [evalstate/mcp-miro](https://github.com/evalstate/mcp-miro) 📇 ☁️ - Access MIRO whiteboards, bulk create and read items. Requires OAUTH key for REST API.
- [future-audiences/wikimedia-enterprise-model-context-protocol](https://gitlab.wikimedia.org/repos/future-audiences/wikimedia-enterprise-model-context-protocol) 🐍 ☁️  - Wikipedia Article lookup API
- [githejie/mcp-server-calculator](https://github.com/githejie/mcp-server-calculator) 🐍 🏠 - This server enables LLMs to use calculator for precise numerical calculations
- [gotoolkits/DifyWorkflow](https://github.com/gotoolkits/mcp-difyworkflow-server) - 🏎️ ☁️ Tools to the query and execute of Dify workflows
- [hiromitsusasaki/raindrop-io-mcp-server](https://github.com/hiromitsusasaki/raindrop-io-mcp-server) 📇 ☁️ - An integration that allows LLMs to interact with Raindrop.io bookmarks using the Model Context Protocol (MCP).
- [hmk/attio-mcp-server](https://github.com/hmk/attio-mcp-server) - 📇 ☁️ Allows AI clients to manage records and notes in Attio CRM
- [isaacwasserman/mcp-vegalite-server](https://github.com/isaacwasserman/mcp-vegalite-server) 🐍 🏠 - Generate visualizations from fetched data using the VegaLite format and renderer.
- [ivo-toby/contentful-mcp](https://github.com/ivo-toby/contentful-mcp) 📇 🏠 - Update, create, delete content, content-models and assets in your Contentful Space
- [j3k0/speech.sh](https://github.com/j3k0/speech.sh/blob/main/MCP_README.md) 🏠 - Let the agent speak things out loud, notify you when he's done working with a quick summary
- [jagan-shanmugam/climatiq-mcp-server](https://github.com/jagan-shanmugam/climatiq-mcp-server) 🐍 🏠 - A Model Context Protocol (MCP) server for accessing the Climatiq API to calculate carbon emissions. This allows AI assistants to perform real-time carbon calculations and provide climate impact insights.
- [joshuarileydev/mac-apps-launcher-mcp-server](https://github.com/JoshuaRileyDev/mac-apps-launcher) 📇 🏠 - An MCP server to list and launch applications on MacOS
- [kelvin6365/plane-mcp-server](https://github.com/kelvin6365/plane-mcp-server) - 🏎️ 🏠 This MCP Server will help you to manage projects and issues through [Plane's](https://plane.so) API
- [kenliao94/mcp-server-rabbitmq](https://github.com/kenliao94/mcp-server-rabbitmq) 🐍 🏠 - Enable interaction (admin operation, message enqueue/dequeue) with RabbitMQ
- [kj455/mcp-kibela](https://github.com/kj455/mcp-kibela) - 📇 ☁️ Allows AI models to interact with [Kibela](https://kibe.la/)
- [KS-GEN-AI/confluence-mcp-server](https://github.com/KS-GEN-AI/confluence-mcp-server) 📇 ☁️ 🍎 🪟 - Get Confluence data via CQL and read pages.
- [KS-GEN-AI/jira-mcp-server](https://github.com/KS-GEN-AI/jira-mcp-server) 📇 ☁️ 🍎 🪟 - Read jira data via JQL and api and execute requests to create and edit tickets.
- [lciesielski/mcp-salesforce](https://github.com/lciesielski/mcp-salesforce-example) 🏠 ☁️ - MCP server with basic demonstration of interactions with Salesforce instance
- [louiscklaw/hko-mcp](https://github.com/louiscklaw/hko-mcp) 📇 🏠 - MCP server with basic demonstration of getting weather from Hong Kong Observatory
- [evalstate/mcp-hfspace](https://github.com/evalstate/mcp-hfspace) 📇 ☁️ - Use HuggingFace Spaces directly from Claude. Use Open Source Image Generation, Chat, Vision tasks and more. Supports Image, Audio and text uploads/downloads.
- [magarcia/mcp-server-giphy](https://github.com/magarcia/mcp-server-giphy) 📇 ☁️ - Search and retrieve GIFs from Giphy's vast library through the Giphy API.
- [integromat/make-mcp-server](https://github.com/integromat/make-mcp-server) 🎖️ 📇 🏠 - Turn your [Make](https://www.make.com/) scenarios into callable tools for AI assistants.
- [marcelmarais/Spotify](https://github.com/marcelmarais/spotify-mcp-server) - 📇 🏠 Control Spotify playback and manage playlists.
- [MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) 🐍 ☁️ 🏠 - Interacting with Obsidian via REST API
- [mcp-server-jfx](https://github.com/quarkiverse/quarkus-mcp-servers/tree/main/jfx) ☕ 🏠 - Draw on JavaFX canvas.
- [mediar-ai/screenpipe](https://github.com/mediar-ai/screenpipe) - 🎖️ 🦀 🏠 🍎 Local-first system capturing screen/audio with timestamped indexing, SQL/embedding storage, semantic search, LLM-powered history analysis, and event-triggered actions - enables building context-aware AI agents through a NextJS plugin ecosystem.
- [modelcontextprotocol/server-everything](https://github.com/modelcontextprotocol/servers/tree/main/src/everything) 📇 🏠 - MCP server that exercises all the features of the MCP protocol
- [mrjoshuak/godoc-mcp](https://github.com/mrjoshuak/godoc-mcp) 🏎️ 🏠 - Token-efficient Go documentation server that provides AI assistants with smart access to package docs and types without reading entire source files
- [mzxrai/mcp-openai](https://github.com/mzxrai/mcp-openai) 📇 ☁️ - Chat with OpenAI's smartest models
- [NakaokaRei/swift-mcp-gui](https://github.com/NakaokaRei/swift-mcp-gui.git) 🏠 🍎 - MCP server that can execute commands such as keyboard input and mouse movement
- [nguyenvanduocit/all-in-one-model-context-protocol](https://github.com/nguyenvanduocit/all-in-one-model-context-protocol) 🏎️ 🏠 - Some useful tools for developer, almost everything an engineer need: confluence, Jira, Youtube, run script, knowledge base RAG, fetch URL, Manage youtube channel, emails, calendar, gitlab
- [NON906/omniparser-autogui-mcp](https://github.com/NON906/omniparser-autogui-mcp) - 🐍 Automatic operation of on-screen GUI.
- [pierrebrunelle/mcp-server-openai](https://github.com/pierrebrunelle/mcp-server-openai) 🐍 ☁️ - Query OpenAI models directly from Claude using MCP protocol
- [pskill9/hn-server](https://github.com/pskill9/hn-server) - 📇 ☁️ Parses the HTML content from news.ycombinator.com (Hacker News) and provides structured data for different types of stories (top, new, ask, show, jobs).
- [PV-Bhat/vibe-check-mcp-server](https://github.com/PV-Bhat/vibe-check-mcp-server) 📇 ☁️ - An MCP server that prevents cascading errors and scope creep by calling a "Vibe-check" agent to ensure user alignment.
- [pwh-pwh/cal-mcp](https://github.com/pwh-pwh/cal-mcp) - An MCP server for Mathematical expression calculation
- [pyroprompts/any-chat-completions-mcp](https://github.com/pyroprompts/any-chat-completions-mcp) - Chat with any other OpenAI SDK Compatible Chat Completions API, like Perplexity, Groq, xAI and more
- [reeeeemo/ancestry-mcp](https://github.com/reeeeemo/ancestry-mcp) 🐍 🏠 - Allows the AI to read .ged files and genetic data
- [rember/rember-mcp](https://github.com/rember/rember-mcp) 📇 🏠 - Create spaced repetition flashcards in [Rember](https://rember.com) to remember anything you learn in your chats.
- [roychri/mcp-server-asana](https://github.com/roychri/mcp-server-asana) - 📇 ☁️ This Model Context Protocol server implementation of Asana allows you to talk to Asana API from MCP Client such as Anthropic's Claude Desktop Application, and many more.
- [rusiaaman/wcgw](https://github.com/rusiaaman/wcgw/blob/main/src/wcgw/client/mcp_server/Readme.md) 🐍 🏠 - Autonomous shell execution, computer control and coding agent. (Mac)
- [SecretiveShell/MCP-wolfram-alpha](https://github.com/SecretiveShell/MCP-wolfram-alpha) 🐍 ☁️ - An MCP server for querying wolfram alpha API.
- [Seym0n/tiktok-mcp](https://github.com/Seym0n/tiktok-mcp) 📇 ☁️ - Interact with TikTok videos
- [sirmews/apple-notes-mcp](https://github.com/sirmews/apple-notes-mcp) 🐍 🏠 - Allows the AI to read from your local Apple Notes database (macOS only)
- [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) 🐍 ☁️ - MCP server for Atlassian products (Confluence and Jira). Supports Confluence Cloud, Jira Cloud, and Jira Server/Data Center. Provides comprehensive tools for searching, reading, creating, and managing content across Atlassian workspaces.
- [suekou/mcp-notion-server](https://github.com/suekou/mcp-notion-server) 📇 🏠 - Interacting with Notion API
- [tacticlaunch/mcp-linear](https://github.com/tacticlaunch/mcp-linear) 📇 ☁️ 🍎 🪟 🐧 - Integrates with Linear project management system
- [tanigami/mcp-server-perplexity](https://github.com/tanigami/mcp-server-perplexity) 🐍 ☁️ - Interacting with Perplexity API.
- [tevonsb/homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp) 📇 🏠 - Access Home Assistant data and control devices (lights, switches, thermostats, etc).
- [tomekkorbak/oura-mcp-server](https://github.com/tomekkorbak/oura-mcp-server) 🐍 ☁️ - An MCP server for Oura, an app for tracking sleep
- [kw510/strava-mcp](https://github.com/kw510/strava-mcp) 📇 ☁️ - An MCP server for Strava, an app for tracking physical exercise
- [wanaku-ai/wanaku](https://github.com/wanaku-ai/wanaku) - ☁️ 🏠 The Wanaku MCP Router is a SSE-based MCP server that provides an extensible routing engine that allows integrating your enterprise systems with AI agents.
- [wong2/mcp-cli](https://github.com/wong2/mcp-cli) 📇 🏠 - CLI tool for testing MCP servers
- [ws-mcp](https://github.com/nick1udwig/ws-mcp) - Wrap MCP servers with a WebSocket (for use with [kitbitz](https://github.com/nick1udwig/kibitz))
- [yuna0x0/hackmd-mcp](https://github.com/yuna0x0/hackmd-mcp) 📇 ☁️ - Allows AI models to interact with [HackMD](https://hackmd.io)
- [ZeparHyfar/mcp-datetime](https://github.com/ZeparHyfar/mcp-datetime) - MCP server providing date and time functions in various formats
- [zueai/mcp-manager](https://github.com/zueai/mcp-manager) 📇 ☁️ - Simple Web UI to install and manage MCP servers for Claude Desktop App.
- [HenryHaoson/Yuque-MCP-Server](https://github.com/HenryHaoson/Yuque-MCP-Server) - 📇 ☁️ A Model-Context-Protocol (MCP) server for integrating with Yuque API, allowing AI models to manage documents, interact with knowledge bases, search content, and access analytics data from the Yuque platform.

## Frameworks

- [FastMCP](https://github.com/jlowin/fastmcp) 🐍 - A high-level framework for building MCP servers in Python
- [FastMCP](https://github.com/punkpeye/fastmcp) 📇 - A high-level framework for building MCP servers in TypeScript
- [Foxy Contexts](https://github.com/strowk/foxy-contexts) 🏎️ - Golang library to write MCP Servers declaratively with functional testing included
- [gabfr/waha-api-mcp-server](https://github.com/gabfr/waha-api-mcp-server) 📇 - An MCP server with openAPI specs for using the WhatsApp unnoficial API (https://waha.devlike.pro/ - also open source: https://github.com/devlikeapro/waha
- [Genkit MCP](https://github.com/firebase/genkit/tree/main/js/plugins/mcp) 📇 – Provides integration between [Genkit](https://github.com/firebase/genkit/tree/main) and the Model Context Protocol (MCP).
- [http4k MCP SDK](https://mcp.http4k.org) 🐍 - Functional, testable Kotlin SDK based around the popular [http4k](https://http4k.org) Web toolkit. Supports new HTTP Streaming protocol.
- [lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent) 🤖 🔌 - Build effective agents with MCP servers using simple, composable patterns.
- [LiteMCP](https://github.com/wong2/litemcp) 📇 - A high-level framework for building MCP servers in JavaScript/TypeScript
- [marimo-team/codemirror-mcp](https://github.com/marimo-team/codemirror-mcp) - CodeMirror extension that implements the Model Context Protocol (MCP) for resource mentions and prompt commands.
- [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go) 🏎️ - Golang SDK for building MCP Servers and Clients.
- [mcp-framework](https://github.com/QuantGeekDev/mcp-framework) 📇 - Fast and elegant TypeScript framework for building MCP servers
- [mcp-proxy](https://github.com/punkpeye/mcp-proxy) - 📇 A TypeScript SSE proxy for MCP servers that use `stdio` transport.
- [mcp-rs-template](https://github.com/linux-china/mcp-rs-template) 🦀 - MCP CLI server template for Rust
- [metoro-io/mcp-golang](https://github.com/metoro-io/mcp-golang) 🏎️ - Golang framework for building MCP Servers, focussed on type safety
- [mullerhai/sakura-mcp](https://github.com/mullerhai/sakura-mcp) 🦀 ☕ - Scala MCP Framework for Build effective agents with MCP servers and MCP clients shade from modelcontextprotocol.io.
- [paulotaylor/voyp-mcp](https://github.com/paulotaylor/voyp-mcp) 📇 - VOYP - Voice Over Your Phone MCP Server for making calls.
- [poem-web/poem-mcpserver](https://github.com/poem-web/poem/tree/master/poem-mcpserver) 🦀 - MCP Server implementation for Poem.
- [quarkiverse/quarkus-mcp-server](https://github.com/quarkiverse/quarkus-mcp-server) ☕ - Java SDK for building MCP servers using Quarkus.
- [rectalogic/langchain-mcp](https://github.com/rectalogic/langchain-mcp) 🐍 - Provides MCP tool calling support in LangChain, allowing for the integration of MCP tools into LangChain workflows.
- [ribeirogab/simple-mcp](https://github.com/ribeirogab/simple-mcp) 📇 - A simple TypeScript library for creating MCP servers.
- [salty-flower/ModelContextProtocol.NET](https://github.com/salty-flower/ModelContextProtocol.NET) #️⃣ 🏠 - A C# SDK for building MCP servers on .NET 9 with NativeAOT compatibility ⚡ 🔌
- [spring-ai-mcp](https://github.com/spring-projects-experimental/spring-ai-mcp) ☕ 🌱 - Java SDK and Spring Framework integration for building MCP client and MCP servers with various, plugable, transport options.
- [spring-projects-experimental/spring-ai-mcp](https://github.com/spring-projects-experimental/spring-ai-mcp) ☕ 🌱 - Java SDK and Spring Framework integration for building MCP client and MCP servers with various, plugable, transport options.
- [Template MCP Server](https://github.com/mcpdotdirect/template-mcp-server) 📇 - A CLI tool to create a new Model Context Protocol server project with TypeScript support, dual transport options, and an extensible structure
- [sendaifun/solana-mcp-kit](https://github.com/sendaifun/solana-agent-kit/tree/main/examples/agent-kit-mcp-server) - Solana MCP SDK

## Utilities

- [boilingdata/mcp-server-and-gw](https://github.com/boilingdata/mcp-server-and-gw) 📇 - An MCP stdio to HTTP SSE transport gateway with example server and MCP client.
- [f/MCPTools](https://github.com/f/mcptools) 🔨 - A command-line development tool for inspecting and interacting with MCP servers with extra features like mocks and proxies.
- [flux159/mcp-chat](https://github.com/flux159/mcp-chat) 📇🖥️ - A CLI based client to chat and connect with any MCP server. Useful during development & testing of MCP servers.
- [isaacwasserman/mcp-langchain-ts-client](https://github.com/isaacwasserman/mcp-langchain-ts-client) 📇 – Use MCP provided tools in LangChain.js
- [kukapay/whattimeisit-mcp](https://github.com/kukapay/whattimeisit-mcp) 🐍 ☁️ - A lightweight mcp server that tells you exactly what time is it.
- [kukapay/whereami-mcp](https://github.com/kukapay/whereami-mcp) 🐍 ☁️ -  A lightweight mcp server that tells you exactly where you are based on your current IP.
- [kukapay/whoami-mcp](https://github.com/kukapay/whoami-mcp) 🐍 🏠 - A lightweight MCP server that tells you exactly who you are.
- [lightconetech/mcp-gateway](https://github.com/lightconetech/mcp-gateway) 📇 - A gateway demo for MCP SSE Server.
- [mark3labs/mcphost](https://github.com/mark3labs/mcphost) 🏎️ -  A CLI host application that enables Large Language Models (LLMs) to interact with external tools through the Model Context Protocol (MCP).
- [MCP-Connect](https://github.com/EvalsOne/MCP-Connect) 📇 - A tiny tool that enables cloud-based AI services to access local Stdio based MCP servers by HTTP/HTTPS requests.
- [SecretiveShell/MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge) 🐍 – an openAI middleware proxy to use mcp in any existing openAI compatible client
- [sparfenyuk/mcp-proxy](https://github.com/sparfenyuk/mcp-proxy) 🐍 – An MCP stdio to SSE transport gateawy.
- [TBXark/mcp-proxy](https://github.com/TBXark/mcp-proxy) 🏎️ - An MCP proxy server that aggregates and serves multiple MCP resource servers through a single http server.
- [upsonic/gpt-computer-assistant](https://github.com/Upsonic/gpt-computer-assistant) 🐍 – framework to build vertical AI agent
- [JoshuaSiraj/mcp_auto_register](https://github.com/JoshuaSiraj/mcp_auto_register) 🐍 – tool to automate the registration of functions and classes from a python package into a FastMCP instance.

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
