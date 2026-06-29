[![ไทย](https://img.shields.io/badge/Thai-Click-blue)](README-th.md)
[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![繁體中文](https://img.shields.io/badge/繁體中文-點擊查看-orange)](README-zh_TW.md)
[![简体中文](https://img.shields.io/badge/简体中文-点击查看-orange)](README-zh.md)
[![日本語](https://img.shields.io/badge/日本語-クリック-青)](README-ja.md)
[![한국어](https://img.shields.io/badge/한국어-클릭-yellow)](README-ko.md)
[![Português Brasileiro](https://img.shields.io/badge/Português_Brasileiro-Clique-green)](README-pt_BR.md)
[![Discord](https://img.shields.io/discord/1312302100125843476?logo=discord&label=discord)](https://glama.ai/mcp/discord)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/mcp?style=flat&logo=reddit&label=subreddit)](https://www.reddit.com/r/mcp/)

> [!IMPORTANT]
> [Awesome MCP Servers](https://glama.ai/mcp/servers) web directory.

A curated list of awesome Model Context Protocol (MCP) servers.

* [What is MCP?](#what-is-mcp)
* [Clients](#clients)
* [Tutorials](#tutorials)
* [Community](#community)
* [Legend](#legend)
* [Server Implementations](#server-implementations)
* [Frameworks](#frameworks)
* [Tips & Tricks](#tips-and-tricks)

## What is MCP?

[MCP](https://modelcontextprotocol.io/) is an open protocol that enables AI models to securely interact with local and remote resources through standardized server implementations. This list focuses on production-ready and experimental MCP servers that extend AI capabilities through file access, database connections, API integrations, and other contextual services.

## Clients

Checkout [awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients/) and [glama.ai/mcp/clients](https://glama.ai/mcp/clients).

## Tutorials

* [Tool Definition Quality Score (TDQS)](https://github.com/glama-ai/tool-definition-quality-score)
* [Model Context Protocol (MCP) Quickstart](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
* [Setup Claude Desktop App to Use a SQLite Database](https://youtu.be/wxCCzo9dGj0)

## Community

* [r/mcp Reddit](https://www.reddit.com/r/mcp)
* [Discord Server](https://glama.ai/mcp/discord)

## Legend

* 🎖️ – official implementation
* programming language
  * 🐍 – Python codebase
  * 📇 – TypeScript (or JavaScript) codebase
  * 🏎️ – Go codebase
  * 🦀 – Rust codebase
  * #️⃣ - C# Codebase
  * ☕ - Java codebase
  * 🌊 – C/C++ codebase
  * 💎 - Ruby codebase

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
> * Use cloud when MCP server is talking to remote APIs, e.g. weather API.

## Server Implementations

> [!NOTE]
> We now have a [web-based directory](https://glama.ai/mcp/servers) that is synced with the repository.

* 🔗 - [Aggregators](#aggregators)
* 🎨 - [Art & Culture](#art-and-culture)
* 📐 - [Architecture & Design](#architecture-and-design)
* 📂 - [Browser Automation](#browser-automation)
* 🧬 - [Biology Medicine and Bioinformatics](#bio)
* ☁️ - [Cloud Platforms](#cloud-platforms)
* 👨‍💻 - [Code Execution](#code-execution)
* 🤖 - [Coding Agents](#coding-agents)
* 🖥️ - [Command Line](#command-line)
* 💬 - [Communication](#communication)
* 🗣️ - [Conversational AI](#conversational-ai)
* 🔑 - [Cryptography](#cryptography)
* 👤 - [Customer Data Platforms](#customer-data-platforms)
* 🗄️ - [Databases](#databases)
* 📊 - [Data Platforms](#data-platforms)
* 🚚 - [Delivery](#delivery)
* 🛠️ - [Developer Tools](#developer-tools)
* 🧮 - [Data Science Tools](#data-science-tools)
* 📊 - [Data Visualization](#data-visualization)
* 📟 - [Embedded system](#embedded-system)
* 🎓 - [Education](#education)
* 🛒 - [E-Commerce](#e-commerce)
* 🌳 - [Environment & Nature](#environment-and-nature)
* 📂 - [File Systems](#file-systems)
* 💰 - [Finance & Fintech](#finance--fintech)
* 🎮 - [Gaming](#gaming)
* 🏠 - [Home Automation](#home-automation)
* 🧠 - [Knowledge & Memory](#knowledge--memory)
* ⚖️ - [Legal](#legal)
* 🗺️ - [Location Services](#location-services)
* 🎯 - [Marketing](#marketing)
* 📊 - [Monitoring](#monitoring)
* 🎥 - [Multimedia Process](#multimedia-process)
* 🖥️ - [OS Automation](#os-automation)
* 📋 - [Product Management](#product-management)
* 🏠 - [Real Estate](#real-estate)
* 🔬 - [Research](#research)
* 🔎 - [Search & Data Extraction](#search)
* 🔒 - [Security](#security)
* 🌐 - [Social Media](#social-media)
* 🔮 - [Spirituality & Esoterica](#spirituality-and-esoterica)
* 🏃 - [Sports](#sports)
* 🎧 - [Support & Service Management](#support-and-service-management)
* 🌎 - [Translation Services](#translation-services)
* 🎧 - [Text-to-Speech](#text-to-speech)
* 🎙️ - [Speech-to-Text](#speech-to-text)
* 🚆 - [Travel & Transportation](#travel-and-transportation)
* 🔄 - [Version Control](#version-control)
* 🏢 - [Workplace & Productivity](#workplace-and-productivity)
* 🛠️ - [Other Tools and Integrations](#other-tools-and-integrations)

### 🔗 <a name="aggregators"></a>Aggregators

Servers for accessing many apps and tools through a single MCP server.

- [forgemeshlabs/coinopai-mcp](https://github.com/forgemeshlabs/coinopai-mcp) [![forgemeshlabs/coinopai-mcp MCP server](https://glama.ai/mcp/servers/forgemeshlabs/coinopai-mcp/badges/score.svg)](https://glama.ai/mcp/servers/forgemeshlabs/coinopai-mcp) 📇 - Local stdio MCP server for x402-powered paid crypto intelligence: preflight checks, trade decisions with `decision_id`, later audit against real prices, risk state, signal history, and agent automation search over USDC micropayments on Base.
- [1mcp/agent](https://github.com/1mcp-app/agent) 📇 ☁️ 🏠 🍎 🪟 🐧 - A unified Model Context Protocol server implementation that aggregates multiple MCP servers into one.
- [2s-io/sdk](https://github.com/2s-io/sdk) [![2s-io/sdk MCP server](https://glama.ai/mcp/servers/2s-io/sdk/badges/score.svg)](https://glama.ai/mcp/servers/2s-io/sdk) 📇 ☁️ 🍎 🪟 🐧 - Unified API for AI agents — 180+ tools across geocoding, weather (NWS), climate stations (NOAA), earthquakes (USGS), tides (NOAA), points of interest (OpenStreetMap), patents (USPTO ODP), US case law (CourtListener / Free Law Project), Federal Register, Wikipedia, scientific papers (arXiv / PubMed / Semantic Scholar), AI summarize / translate / extract / screenshot / image-describe, image compression, DNS / WHOIS, crypto address-validate + EVM gas oracle, OFAC sanctions screening, US Census ACS demographics, airport / ZIP lookup. Sub-cent to a few cents per call in USDC on Base via x402 — no API keys, no signup. `npx -y @2sio/mcp`
- [8randonpickart5/alderpost-mcp](https://github.com/8randonpickart5/alderpost-mcp) [![alderpost-mcp MCP server](https://glama.ai/mcp/servers/8randonpickart5/alderpost-mcp/badges/score.svg)](https://glama.ai/mcp/servers/8randonpickart5/alderpost-mcp) 📇 ☁️ - 8 bundled intelligence endpoints (security, company, threat, compliance, sales, sports, property, health) via x402 micropayments on Base.
- [GTCC777/pulsenetwork-mcp](https://github.com/GTCC777/pulsenetwork-mcp) [![GTCC777/pulsenetwork-mcp MCP server](https://glama.ai/mcp/servers/GTCC777/pulsenetwork-mcp/badges/score.svg)](https://glama.ai/mcp/servers/GTCC777/pulsenetwork-mcp) 📇 - One MCP server exposing 66 specialized intelligence APIs (660+ endpoints) — finance, crypto, legal, immigration, healthcare cost, real estate, tax, climate, sports, science, and more — each an x402 pay-per-call tool in USDC on Base and Solana. Includes a `discover` meta-tool over the whole network and a cross-vertical referral graph. No API keys. `npx mcp-pulsenetwork`
- [tadas-github/a2asearch-mcp](https://github.com/tadas-github/a2asearch-mcp) [![tadas-github/a2asearch-mcp MCP server](https://glama.ai/mcp/servers/tadas-github/a2asearch-mcp/badges/score.svg)](https://glama.ai/mcp/servers/tadas-github/a2asearch-mcp) 📇 ☁️ - MCP server to search 4,800+ MCP servers, AI agents, CLI tools and agent skills. Install: `npx -y a2asearch-mcp`. Ask Claude: "Find MCP servers for database access". Free, no auth required.
- [Aganium/agenium](https://github.com/Aganium/agenium) 📇 ☁️ 🍎 🪟 🐧 - Bridge any MCP server to the agent:// network — DNS-like identity, discovery, and trust for AI agents. Makes your tools discoverable and callable by other agents via `agent://` URIs with mTLS, trust scores, and capability search.
- [elisymlabs/elisym](https://github.com/elisymlabs/elisym) [![elisymlabs/elisym MCP server](https://glama.ai/mcp/servers/elisymlabs/elisym/badges/score.svg)](https://glama.ai/mcp/servers/elisymlabs/elisym) 📇 ☁️ 🍎 🪟 🐧 - AI agent discovery and marketplace on Nostr with Solana payments (SOL, USDC). NIP-89 discovery, NIP-90 jobs, NIP-44 v2 encryption, on-chain micropayments.
- [espadaw/Agent47](https://github.com/espadaw/Agent47) 📇 ☁️ - Unified job aggregator for AI agents across 9+ platforms (x402, RentAHuman, Virtuals, etc).
- [doggychip/agentforge](https://github.com/doggychip/agentforge) [![doggychip/agentforge MCP server](https://glama.ai/mcp/servers/doggychip/agentforge/badges/score.svg)](https://glama.ai/mcp/servers/doggychip/agentforge) 📇 ☁️ - Unified API gateway and marketplace for 300+ AI agents. One API key, REST + streaming, 90% creator revenue share, health monitoring. Self-hostable (MIT).
- [AgentHotspot](https://github.com/AgentHotspot/agenthotspot-mcp) 🐍 ☁️ 🏠 🍎 🪟 🐧 - Search, integrate and monetize MCP connectors on the AgentHotspot MCP marketplace
- [garasegae/aiskillstore](https://github.com/garasegae/aiskillstore) [![garasegae/aiskillstore MCP server](https://glama.ai/mcp/servers/garasegae/aiskillstore/badges/score.svg)](https://glama.ai/mcp/servers/garasegae/aiskillstore) ☁️ - Agent-first skill marketplace where AI agents discover, purchase, and integrate skills via MCP protocol. Supports 7+ platforms including Claude, hGPT, and Gemini.
- [alexanderclapp/clirank-mcp-server](https://github.com/alexanderclapp/clirank-mcp-server) [![alexanderclapp/clirank-mcp-server MCP server](https://glama.ai/mcp/servers/alexanderclapp/clirank-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/alexanderclapp/clirank-mcp-server) 📇 ☁️ 🍎 🪟 🐧 - API intelligence for AI coding agents. 387 APIs scored on agent-friendliness with tools to recommend, compare, check scores, and discover APIs. Install: `npx clirank-mcp-server`. Web: [clirank.dev](https://clirank.dev).
- [Work90210/APIFold](https://github.com/Work90210/APIFold) [![Work90210/APIFold MCP server](https://glama.ai/mcp/servers/Work90210/APIFold/badges/score.svg)](https://glama.ai/mcp/servers/Work90210/APIFold) 📇 ☁️ - Turn any REST API into a hosted MCP server. 18 free public servers (GitHub, Stripe, Slack, OpenAI, Notion, and more) — no setup required, bring your own API key.
- [alexar76/aimarket-plugins](https://github.com/alexar76/aimarket-plugins) [![alexar76/aimarket-plugins MCP server](https://glama.ai/mcp/servers/alexar76/aimarket-plugins/badges/score.svg)](https://glama.ai/mcp/servers/alexar76/aimarket-plugins) 📇 ☁️ 🏠 🍎 🪟 🐧 - **aimarket-mcp-packager** hub plugin: turn AIMarket capabilities into self-hosted MCP servers (Docker image + `mcp_manifest` + Claude Desktop `mcpServers` config). Part of 15-plugin AIMarket Hub ([modelmarket.dev](https://modelmarket.dev)); protocol discovery at `/.well-known/ai-market.json`. Install: `pip install aimarket-mcp-packager`.
- [rhein1/agoragentic-integrations](https://github.com/rhein1/agoragentic-integrations) [![agoragentic-integrations MCP server](https://glama.ai/mcp/servers/@rhein1/agoragentic-integrations/badges/score.svg)](https://glama.ai/mcp/servers/@rhein1/agoragentic-integrations) 📇 ☁️ - Agent-to-agent marketplace where AI agents discover, invoke, and pay for services from other agents using USDC on Base L2.
- [arikusi/deepseek-mcp-server](https://github.com/arikusi/deepseek-mcp-server) [![deepseek-mcp-server MCP server](https://glama.ai/mcp/servers/arikusi/deepseek-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/arikusi/deepseek-mcp-server) 📇 ☁️ 🍎 🪟 🐧 - MCP server for DeepSeek AI with chat, reasoning, multi-turn sessions, function calling, thinking mode, and cost tracking.
- [ariekogan/ateam-mcp](https://github.com/ariekogan/ateam-mcp) 📇 ☁️ 🏠 🍎 🪟 🐧 - Build, validate, and deploy multi-agent AI solutions on the ADAS platform. Design skills with tools, manage solution lifecycle, and connect from any AI environment via stdio or HTTP.
- [askbudi/roundtable](https://github.com/askbudi/roundtable) 📇 ☁️ 🏠 🍎 🪟 🐧 - Meta-MCP server that unifies multiple AI coding assistants (Codex, Claude Code, Cursor, Gemini) through intelligent auto-discovery and standardized MCP interface, providing zero-configuration access to the entire AI coding ecosystem.
- [blockrunai/blockrun-mcp](https://github.com/blockrunai/blockrun-mcp) 📇 ☁️ 🍎 🪟 🐧 - Access 30+ AI models (GPT-5, Claude, Gemini, Grok, DeepSeek) without API keys. Pay-per-use via x402 micropayments with USDC on Base.
- [cinderwright-ai/cinderwright-api](https://github.com/cinderwright-ai/cinderwright-api) [![Score](https://glama.ai/mcp/servers/cinderwright-ai/cinderwright-api/badges/score.svg)](https://glama.ai/mcp/servers/cinderwright-ai/cinderwright-api) 📇 ☁️ - x402 Discovery Hub. Search engine for the agent economy with 1450+ services indexed. Pay with USDC on Base via x402.
- [Continuum-AI-Corp/orcarouter-mcp-server](https://github.com/Continuum-AI-Corp/orcarouter-mcp-server) [![Continuum-AI-Corp/orcarouter-mcp-server MCP server](https://glama.ai/mcp/servers/Continuum-AI-Corp/orcarouter-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/Continuum-AI-Corp/orcarouter-mcp-server) 📇 ☁️ 🏠 🍎 🪟 🐧 - Browse 160+ LLM models (OpenAI, Anthropic, Google, Qwen, DeepSeek, …) with live pricing — no API key required for catalog tools. Routes chat completions through the OrcaRouter gateway with automatic fallback. `npx -y @orcarouter/mcp`.
- [Data-Everything/mcp-server-templates](https://github.com/Data-Everything/mcp-server-templates) 📇 🏠 🍎 🪟 🐧 - One server. All tools. A unified MCP platform that connects many apps, tools, and services behind one powerful interface—ideal for local devs or production agents.
- [depwire/depwire](https://github.com/depwire/depwire) [![depwire/depwire MCP server](https://glama.ai/mcp/servers/depwire/depwire/badges/score.svg)](https://glama.ai/mcp/servers/depwire/depwire) 📇 🐍 🏎️ 🦀 🌊 🏠 - Dependency graph + 15 MCP tools for AI coding assistants. Parses TypeScript, JavaScript, Python, Go, Rust, and C. Arc diagram visualization, health scoring, dead code detection, and temporal graph.
- [duaraghav8/MCPJungle](https://github.com/duaraghav8/MCPJungle) 🏎️ 🏠 - Self-hosted MCP Server registry for enterprise AI Agents
- [edgarriba/prolink](https://github.com/edgarriba/prolink) 🐍 ☁️ 🏠 🍎 🪟 🐧 - Agent-to-agent marketplace middleware — MCP-native discovery, negotiation, and transaction between AI agents
- [entire-vc/evc-spark-mcp](https://github.com/entire-vc/evc-spark-mcp) [![evc-spark-mcp MCP server](https://glama.ai/mcp/servers/entire-vc/evc-spark-mcp/badges/score.svg)](https://glama.ai/mcp/servers/entire-vc/evc-spark-mcp) 📇 ☁️ 🏠 🍎 🪟 🐧 - Search and discover AI agents, skills, prompts, bundles and MCP connectors from a curated catalog of 4500+ assets.
- [glenngillen/mcpmcp-server](https://github.com/glenngillen/mcpmcp-server) ☁️ 📇 🍎 🪟 🐧 - A list of MCP servers so you can ask your client which servers you can use to improve your daily workflow.
- [gpu-bridge/mcp-server](https://github.com/gpu-bridge/mcp-server) [![gpu-bridge-mcp-server MCP server](https://glama.ai/mcp/servers/gpu-bridge/mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/gpu-bridge/mcp-server) 📇 ☁️ 🍎 🪟 🐧 - Unified GPU inference API with 30 AI services (LLM, image gen, video, TTS, whisper, embeddings, reranking, OCR) as MCP tools. Pay-per-use via x402 USDC or API key credits.
-  [carlosahumada89/govrider-mcp-server](https://github.com/carlosahumada89/govrider-mcp-server) [![@carlosahumada89-govrider-mcp-server MCP server](https://glama.ai/mcp/servers/@carlosahumada89-govrider-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/@carlosahumada89-govrider-mcp-server) ☁️  📇 - Match your tech product or consulting service to thousands of live government tenders, RFPs, grants, and frameworks from 25+ official sources worldwide.
- [gzoonet/cortex](https://github.com/gzoonet/cortex) [![gzoo-cortex MCP server](https://glama.ai/mcp/servers/@gzoonet/gzoo-cortex/badges/score.svg)](https://glama.ai/mcp/servers/@gzoonet/gzoo-cortex) 📇 🏠 - Local-first knowledge graph for developers. Watches project files, extracts entities and relationships via LLMs, builds a queryable knowledge graph with web dashboard and CLI. Provides 4 MCP tools: get_status, list_projects, find_entity, query_cortex.
- [hamflx/imagen3-mcp](https://github.com/hamflx/imagen3-mcp) 📇 🏠 🪟 🍎 🐧 - A powerful image generation tool using Google's Imagen 3.0 API through MCP. Generate high-quality images from text prompts with advanced photography, artistic, and photorealistic controls.
- [hashgraph-online/hashnet-mcp-js](https://github.com/hashgraph-online/hashnet-mcp-js) 📇 ☁️ 🍎 🪟 🐧 - MCP server for the Registry Broker. Discover, register, and chat with AI agents on the Hashgraph network.
- [HelpCode-ai/anythingmcp](https://github.com/HelpCode-ai/anythingmcp) [![HelpCode-ai/anythingmcp MCP server](https://glama.ai/mcp/servers/HelpCode-ai/anythingmcp/badges/score.svg)](https://glama.ai/mcp/servers/HelpCode-ai/anythingmcp) 📇 🏠 ☁️ 🍎 🪟 🐧 - Self-hosted source-available MCP gateway and API-to-MCP bridge. Converts REST, SOAP/WSDL, GraphQL, and SQL/NoSQL databases (PostgreSQL, MySQL, MariaDB, MSSQL, Oracle, MongoDB, SQLite) into MCP tools — no SDK, no code. Imports OpenAPI / Postman / WSDL / GraphQL specs; bridges multiple MCP servers behind one endpoint. Ships with 29 pre-built adapters (DHL, DATEV, Weclapp, Personio, Handelsregister, Shopware 6, VIES, OpenPLZ, Bundesbank, etc.). OAuth2 (PKCE + Client Credentials), Bearer, API Key, WS-Security, TLS certs. AES-256-GCM credential encryption, full audit log, per-user MCP API keys, tool-level RBAC.
- [isaac-levine/forage](https://github.com/isaac-levine/forage) 📇 🏠 🍎 🪟 🐧 - Self-improving tool discovery for AI agents. Searches registries, installs MCP servers as subprocesses, and persists tool knowledge across sessions — no restarts needed.
- [jabbawocky/proposalcraft](https://github.com/jabbawocky/proposalcraft) [![jabbawocky/proposalcraft MCP server](https://glama.ai/mcp/servers/jabbawocky/proposalcraft/badges/score.svg)](https://glama.ai/mcp/servers/jabbawocky/proposalcraft) 📇 🏠 🍎 🪟 🐧 - MCP server that drafts client proposals in your own voice. Save 2-3 of your winning proposals, paste a new brief, and Claude generates a ready-to-send draft. No API key, no cloud — local storage only. `npx -y github:jabbawocky/proposalcraft`
- [jaspertvdm/mcp-server-gemini-bridge](https://github.com/jaspertvdm/mcp-server-gemini-bridge) 🐍 ☁️ - Bridge to Google Gemini API. Access Gemini Pro and Flash models through MCP.
- [jaspertvdm/mcp-server-ollama-bridge](https://github.com/jaspertvdm/mcp-server-ollama-bridge) 🐍 🏠 - Bridge to local Ollama LLM server. Run Llama, Mistral, Qwen and other local models through MCP.
- [jaspertvdm/mcp-server-openai-bridge](https://github.com/jaspertvdm/mcp-server-openai-bridge) 🐍 ☁️ - Bridge to OpenAI API. Access GPT-4, GPT-4o and other OpenAI models through MCP.
- [Jovancoding/Network-AI](https://github.com/Jovancoding/Network-AI) [![network](https://glama.ai/mcp/servers/Jovancoding/network-ai/badges/score.svg)](https://glama.ai/mcp/servers/Jovancoding/network-ai) 📇 🏠 🍎 🪟 🐧 - Multi-agent orchestration MCP server with race-condition-safe shared blackboard. 20+ MCP tools: blackboard read/write, agent spawn/stop, FSM transitions, budget tracking, token management, and audit log query. `npx network-ai-server --port 3001`.
- [julien040/anyquery](https://github.com/julien040/anyquery) 🏎️ 🏠 ☁️ - Query more than 40 

... [OUTPUT TRUNCATED - 959032 chars omitted out of 1009032 total] ...

matze/gemot MCP server](https://glama.ai/mcp/servers/justinstimatze/gemot/badges/score.svg)](https://glama.ai/mcp/servers/justinstimatze/gemot) 🏎️ 🏠 ☁️ - Structured deliberation server for multi-agent coordination. Agents submit positions, vote on a 5-point scale, and receive analysis identifying cruxes (key disagreements), opinion clusters, bridging statements, and consensus. Two-engine pipeline (LLM text analysis + PCA vote clustering) inspired by Polis and Talk to the City.
- [k-jarzyna/mcp-miro](https://github.com/k-jarzyna/mcp-miro) 📇 ☁️ - Miro MCP server, exposing all functionalities available in official Miro SDK
- [kelvin6365/plane-mcp-server](https://github.com/kelvin6365/plane-mcp-server) - 🏎️ 🏠 This MCP Server will help you to manage projects and issues through [Plane's](https://plane.so) API
- [kenliao94/mcp-server-rabbitmq](https://github.com/kenliao94/mcp-server-rabbitmq) 🐍 🏠 - Enable interaction (admin operation, message enqueue/dequeue) with RabbitMQ
- [kiarash-portfolio-mcp](https://kiarash-adl.pages.dev/.well-known/mcp.llmfeed.json) – WebMCP-enabled portfolio with Ed25519 signed discovery. AI agents can query projects, skills, and execute terminal commands. Built on Cloudflare Pages Functions.
- [kimtth/mcp-remote-call-ping-pong](https://github.com/kimtth/mcp-remote-call-ping-pong) 🐍 🏠 - An experimental and educational app for Ping-pong server demonstrating remote MCP (Model Context Protocol) calls
- [kiwamizamurai/mcp-kibela-server](https://github.com/kiwamizamurai/mcp-kibela-server) - 📇 ☁️ Powerfully interact with Kibela API.
- [kj455/mcp-kibela](https://github.com/kj455/mcp-kibela) - 📇 ☁️ Allows AI models to interact with [Kibela](https://kibe.la/)
- [Klavis-AI/YouTube](https://github.com/Klavis-AI/klavis/tree/main/mcp_servers/youtube) 🐍 📇 - Extract and convert YouTube video information.
- [KS-GEN-AI/confluence-mcp-server](https://github.com/KS-GEN-AI/confluence-mcp-server) 📇 ☁️ 🍎 🪟 - Get Confluence data via CQL and read pages.
- [KS-GEN-AI/jira-mcp-server](https://github.com/KS-GEN-AI/jira-mcp-server) 📇 ☁️ 🍎 🪟 - Read jira data via JQL and api and execute requests to create and edit tickets.
- [kw510/strava-mcp](https://github.com/kw510/strava-mcp) 📇 ☁️ - An MCP server for Strava, an app for tracking physical exercise
- [latex-mcp-server](https://github.com/Yeok-c/latex-mcp-server) - An MCP Server to compile latex, download/organize/read cited papers, run visualization scripts and add figures/tables to latex.
- [louiscklaw/hko-mcp](https://github.com/louiscklaw/hko-mcp) 📇 🏠 - MCP server with basic demonstration of getting weather from Hong Kong Observatory
- [magarcia/mcp-server-giphy](https://github.com/magarcia/mcp-server-giphy) 📇 ☁️ - Search and retrieve GIFs from Giphy's vast library through the Giphy API.
- [MAG-Cie/mcp-microsoft-todo](https://github.com/MAG-Cie/mcp-microsoft-todo) [![MAG-Cie/mcp-microsoft-todo MCP server](https://glama.ai/mcp/servers/MAG-Cie/mcp-microsoft-todo/badges/score.svg)](https://glama.ai/mcp/servers/MAG-Cie/mcp-microsoft-todo) 📇 🏠 🍎 🪟 🐧 - Microsoft To Do task management via Microsoft Graph API. MSAL device code flow (no client secret needed), persisted token cache, full MCP safety annotations.
- [marcelmarais/Spotify](https://github.com/marcelmarais/spotify-mcp-server) - 📇 🏠 Control Spotify playback and manage playlists.
- [MariusAure/needhuman-mcp](https://github.com/MariusAure/needhuman-mcp) [![need-human MCP server](https://glama.ai/mcp/servers/@MariusAure/need-human/badges/score.svg)](https://glama.ai/mcp/servers/@MariusAure/need-human) 📇 ☁️ - Human-as-a-Service for AI agents — submit tasks (accept ToS, create accounts, verify identity) to a real human when the agent gets stuck.
- [MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) 🐍 ☁️ 🏠 - Interacting with Obsidian via REST API
- [mediar-ai/screenpipe](https://github.com/mediar-ai/screenpipe) - 🎖️ 🦀 🏠 🍎 Local-first system capturing screen/audio with timestamped indexing, SQL/embedding storage, semantic search, LLM-powered history analysis, and event-triggered actions - enables building context-aware AI agents through a NextJS plugin ecosystem.
- [metorial/metorial](https://github.com/metorial/metorial) - 🎖️ 📇 ☁️ Connect AI agents to 600+ integrations with a single interface - OAuth, scaling, and monitoring included
- [modelcontextprotocol/server-everything](https://github.com/modelcontextprotocol/servers/tree/main/src/everything) 📇 🏠 - MCP server that exercises all the features of the MCP protocol
- [MonadsAG/capsulecrm-mcp](https://github.com/MonadsAG/capsulecrm-mcp) - 📇 ☁️ Allows AI clients to manage contacts, opportunities and tasks in Capsule CRM including Claude Desktop ready DTX-file
- [mrjoshuak/godoc-mcp](https://github.com/mrjoshuak/godoc-mcp) 🏎️ 🏠 - Token-efficient Go documentation server that provides AI assistants with smart access to package docs and types without reading entire source files
- [Mtehabsim/ScreenPilot](https://github.com/Mtehabsim/ScreenPilot) 🐍 🏠 - enables AI to fully control and access GUI interactions by providing tools for mouse and keyboard, ideal for general automation, education, and experimentation.
- [muammar-yacoob/GMail-Manager-MCP](https://github.com/muammar-yacoob/GMail-Manager-MCP#readme) 📇 ☁️ 🏠 🍎 🪟 🐧 - Connects Claude Desktop to your Gmail so you can start managing your inbox using natural language. Bulk delete promos & newsletters, organize labels and get useful insights.
- [mzxrai/mcp-openai](https://github.com/mzxrai/mcp-openai) 📇 ☁️ - Chat with OpenAI's smartest models
- [nach-dakwale/instadomain-mcp](https://github.com/nach-dakwale/instadomain-mcp) [![nach-dakwale/instadomain-mcp MCP server](https://glama.ai/mcp/servers/nach-dakwale/instadomain-mcp/badges/score.svg)](https://glama.ai/mcp/servers/nach-dakwale/instadomain-mcp) 🐍 ☁️ - Domain registration for AI agents. Check availability, buy domains (Stripe or x402 crypto), and auto-configure Cloudflare DNS. Zero setup required.
- [NakaokaRei/swift-mcp-gui](https://github.com/NakaokaRei/swift-mcp-gui.git) 🏠 🍎 - MCP server that can execute commands such as keyboard input and mouse movement
- [nanana-app/mcp-server-nano-banana](https://github.com/nanana-app/mcp-server-nano-banana) 🐍 🏠 🍎 🪟 🐧 - AI image generation using Google Gemini's nano banana model.
- [nguyenvanduocit/all-in-one-model-context-protocol](https://github.com/nguyenvanduocit/all-in-one-model-context-protocol) 🏎️ 🏠 - Some useful tools for developer, almost everything an engineer need: confluence, Jira, Youtube, run script, knowledge base RAG, fetch URL, Manage youtube channel, emails, calendar, gitlab
- [NON906/omniparser-autogui-mcp](https://github.com/NON906/omniparser-autogui-mcp) - 🐍 Automatic operation of on-screen GUI.
- [offorte/offorte-mcp-server](https://github.com/offorte/offorte-mcp-server) 🎖️ 📇 ☁️ 🍎 🪟 🐧 - The Offorte Proposal Software MCP server enables creation and sending of business proposals.
- [olalonde/mcp-human](https://github.com/olalonde/mcp-human) 📇 ☁️ - When your LLM needs human assistance (through AWS Mechanical Turk)
- [olgasafonova/productplan-mcp-server](https://github.com/olgasafonova/productplan-mcp-server) 🏎️ ☁️ - Query ProductPlan roadmaps. Access OKRs, ideas, launches, and timeline data.
- [orellazi/coda-mcp](https://github.com/orellazri/coda-mcp) 📇 ☁️ - MCP server for [Coda](https://coda.io/)
- [osinmv/funciton-lookup-mcp](https://github.com/osinmv/function-lookup-mcp) 🐍 🏠 🍎 🐧 - MCP server for function signature lookups.
- [osulivan/skill4agent-mcp-server](https://github.com/osulivan/skill4agent-mcp-server) [![osulivan/skill4agent-mcp-server MCP server](https://glama.ai/mcp/servers/osulivan/skill4agent-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/osulivan/skill4agent-mcp-server) 📇 ☁️ - MCP Server for skill4agent - Search, view, and install AI skills in AI conversations.
- [Pantrist-dev/pantrist-mcp](https://github.com/Pantrist-dev/pantrist-mcp) [![Pantrist-dev/pantrist-mcp MCP server](https://glama.ai/mcp/servers/Pantrist-dev/pantrist-mcp/badges/score.svg)](https://glama.ai/mcp/servers/Pantrist-dev/pantrist-mcp) 🎖️ 📇 ☁️ - Manage your pantry, shopping lists, recipes, and weekly meal plan with Pantrist. Add and check off items, track stock, plan meals from your saved recipes. Full OAuth 2.1 + PKCE with dynamic client registration; hosted at `mcp.pantrist.app` or self-host the Streamable-HTTP / stdio transports.
- [pierrebrunelle/mcp-server-openai](https://github.com/pierrebrunelle/mcp-server-openai) 🐍 ☁️ - Query OpenAI models directly from Claude using MCP protocol
- [PSPDFKit/nutrient-dws-mcp-server](https://github.com/PSPDFKit/nutrient-dws-mcp-server) [![nutrient-dws-mcp-server MCP server](https://glama.ai/mcp/servers/@PSPDFKit/nutrient-dws-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/@PSPDFKit/nutrient-dws-mcp-server) 📇 ☁️ 🍎 🪟 🐧 - MCP server for the Nutrient DWS Processor API. Convert, merge, redact, sign, OCR, watermark, and extract data from PDFs and Office documents via natural language. Works with Claude Desktop, LangGraph, and OpenAI Agents.
- [PSPDFKit/nutrient-document-engine-mcp-server](https://github.com/PSPDFKit/nutrient-document-engine-mcp-server) [![nutrient-document-engine-mcp-server MCP server](https://glama.ai/mcp/servers/@PSPDFKit/nutrient-document-engine-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/@PSPDFKit/nutrient-document-engine-mcp-server) 📇 🏠 🍎 🪟 🐧 - Self-hosted MCP server for Nutrient Document Engine. On-premises document processing with natural language control — designed for HIPAA, SOC 2, and GDPR compliance.
- [pskill9/hn-server](https://github.com/pskill9/hn-server) - 📇 ☁️ Parses the HTML content from news.ycombinator.com (Hacker News) and provides structured data for different types of stories (top, new, ask, show, jobs).
- [PV-Bhat/vibe-check-mcp-server](https://github.com/PV-Bhat/vibe-check-mcp-server) 📇 ☁️ - An MCP server that prevents cascading errors and scope creep by calling a "Vibe-check" agent to ensure user alignment.
- [pwh-pwh/cal-mcp](https://github.com/pwh-pwh/cal-mcp) - An MCP server for Mathematical expression calculation
- [pyroprompts/any-chat-completions-mcp](https://github.com/pyroprompts/any-chat-completions-mcp) - Chat with any other OpenAI SDK Compatible Chat Completions API, like Perplexity, Groq, xAI and more
- [quarkiverse/mcp-server-jfx](https://github.com/quarkiverse/quarkus-mcp-servers/tree/main/jfx) ☕ 🏠 - Draw on JavaFX canvas.
- [QuentinCody/shopify-storefront-mcp-server](https://github.com/QuentinCody/shopify-storefront-mcp-server) 🐍 ☁️ - Unofficial MCP server that allows AI agents to discover Shopify storefronts and interact with them to fetch products, collections, and other store data through the Storefront API.
- [r-huijts/ethics-check-mcp](https://github.com/r-huijts/ethics-check-mcp) 🐍 🏠 - MCP server for comprehensive ethical analysis of AI conversations, detecting bias, harmful content, and providing critical thinking assessments with automated pattern learning
- [rae-api-com/rae-mcp](https://github.com/rae-api-com/rae-mcp) - 🏎️ ☁️ 🍎 🪟 🐧 MCP Server to connect your preferred model with https://rae-api.com, Roya Academy of Spanish Dictionary
- [Rai220/think-mcp](https://github.com/Rai220/think-mcp) 🐍 🏠 - Enhances any agent's reasoning capabilities by integrating the think-tools, as described in [Anthropic's article](https://www.anthropic.com/engineering/claude-think-tool).
- [reeeeemo/ancestry-mcp](https://github.com/reeeeemo/ancestry-mcp) 🐍 🏠 - Allows the AI to read .ged files and genetic data
- [rember/rember-mcp](https://github.com/rember/rember-mcp) 📇 🏠 - Create spaced repetition flashcards in [Rember](https://rember.com) to remember anything you learn in your chats.
- [ReplenishRadar/MCP](https://github.com/ReplenishRadar/MCP) [![ReplenishRadar/MCP MCP server](https://glama.ai/mcp/servers/ReplenishRadar/MCP/badges/score.svg)](https://glama.ai/mcp/servers/ReplenishRadar/MCP) 📇 ☁️ - Multi-channel inventory intelligence for Shopify and Amazon sellers. 28 tools for stockout risk, demand forecasts, purchase order lifecycle, and sales analytics. Human-in-the-loop: all write operations create drafts only.
- [roychri/mcp-server-asana](https://github.com/roychri/mcp-server-asana) - 📇 ☁️ This Model Context Protocol server implementation of Asana allows you to talk to Asana API from MCP Client such as Anthropic's Claude Desktop Application, and many more.
- [rusiaaman/wcgw](https://github.com/rusiaaman/wcgw/blob/main/src/wcgw/client/mcp_server/Readme.md) 🐍 🏠 - Autonomous shell execution, computer control and coding agent. (Mac)
- [SecretiveShell/MCP-wolfram-alpha](https://github.com/SecretiveShell/MCP-wolfram-alpha) 🐍 ☁️ - An MCP server for querying wolfram alpha API.
- [Seym0n/tiktok-mcp](https://github.com/Seym0n/tiktok-mcp) 📇 ☁️ - Interact with TikTok videos
- [Shopify/dev-mcp](https://github.com/Shopify/dev-mcp) 📇 ☁️ - Model Context Protocol (MCP) server that interacts with Shopify Dev.
- [simonpainter/netbox-mcp](https://github.com/simonpainter/netbox-mcp) 🐍 ☁️ - MCP server for interacting with NetBox API.
- [sirmews/apple-notes-mcp](https://github.com/sirmews/apple-notes-mcp) 🐍 🏠 - Allows the AI to read from your local Apple Notes database (macOS only)
 - [rogertheunissenmerge-oss/mcp-server](https://github.com/rogertheunissenmerge-oss/mcp-server) [![rogertheunissenmerge-oss/mcp-server MCP server](https://glama.ai/mcp/servers/rogertheunissenmerge-oss/mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/rogertheunissenmerge-oss/mcp-server) 📇 ☁️ - Wine pairing intelligence for AI assistants. 7 MCP tools for sommelier-grade wine recommendations powered by a proprietary Wine DNA algorithm. Pair wines with meals, ingredients, or recipe URLs. Supports API key and x402 (USDC on Base) payments.
- [suekou/mcp-notion-server](https://github.com/suekou/mcp-notion-server) 📇 🏠 - Interacting with Notion API
- [kirvigen/notion-private-api-mcp](https://github.com/kirvigen/notion-private-api-mcp) [![kirvigen/notion-private-api-mcp MCP server](https://glama.ai/mcp/servers/kirvigen/notion-private-api-mcp/badges/score.svg)](https://glama.ai/mcp/servers/kirvigen/notion-private-api-mcp) 📇 🏠 🍎 🪟 🐧 - Unofficial Notion server via the private API (token_v2): full read/write across your entire workspace with no integration token and no per-page sharing.
- [Swih/mistral-mcp](https://github.com/Swih/mistral-mcp) [![Swih/mistral-mcp MCP server](https://glama.ai/mcp/servers/Swih/mistral-mcp/badges/score.svg)](https://glama.ai/mcp/servers/Swih/mistral-mcp) 📇 ☁️ 🍎 🪟 🐧 - MCP server exposing 22 Mistral AI capabilities (chat, OCR, audio, vision, agents, embeddings, moderation, classification, files, batch) with dual transport (stdio + Streamable HTTP), structured outputs on every tool, and 6 curated French/English prompts with argument completion. Vendor API key required.
- [tacticlaunch/mcp-linear](https://github.com/tacticlaunch/mcp-linear) 📇 ☁️ 🍎 🪟 🐧 - Integrates with Linear project management system
- [tan-yong-sheng/ai-vision-mcp](https://github.com/tan-yong-sheng/ai-vision-mcp) - 📇 🏠 🍎 🪟 🐧 - Multimodal AI vision MCP server for image, video, and object detection analysis. Enables UI/UX evaluation, visual regression testing, and interface understanding using Google Gemini and Vertex AI.
- [tanigami/mcp-server-perplexity](https://github.com/tanigami/mcp-server-perplexity) 🐍 ☁️ - Interacting with Perplexity API.
- [tevonsb/homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp) 📇 🏠 - Access Home Assistant data and control devices (lights, switches, thermostats, etc).
- [TheoBrigitte/mcp-time](https://github.com/TheoBrigitte/mcp-time) 🏎️ 🏠 🍎 🪟 🐧 - MCP server which provides utilities to work with time and dates, with natural language, multiple formats and timezone convertion capabilities.
- [thingsboard/thingsboard-mcp](https://github.com/thingsboard/thingsboard-mcp) 🎖️ ☕ ☁️ 🏠 🍎 🪟 🐧 - The ThingsBoard MCP Server provides a natural language interface for LLMs and AI agents to interact with your ThingsBoard IoT platform.
- [thinq-connect/thinqconnect-mcp](https://github.com/thinq-connect/thinqconnect-mcp) 🎖️ 🐍 ☁️ - Interact with LG ThinQ smart home devices and appliances through the ThinQ Connect MCP server.
- [tjclaude88/mcp-bling](https://github.com/tjclaude88/mcp-bling) [![tjclaude88/mcp-bling MCP server](https://glama.ai/mcp/servers/tjclaude88/mcp-bling/badges/score.svg)](https://glama.ai/mcp/servers/tjclaude88/mcp-bling) 📇 🏠 🍎 🪟 🐧 - Give AI agents a persistent identity and cross-platform visual style. Includes WOW (Weird Office Workers) random-identity generator with rarity tiers and screenshot-ready share cards. `npx -y bling-bag`
- [tomekkorbak/oura-mcp-server](https://github.com/tomekkorbak/oura-mcp-server) 🐍 ☁️ - An MCP server for Oura, an app for tracking sleep
- [Tommertom/plugwise-mcp](https://github.com/Tommertom/plugwise-mcp) 📇 🏠 🍎 🪟 🐧 - TypeScript-based smart home automation server for Plugwise devices with automatic network discovery. Features comprehensive device control for thermostats, switches, smart plugs, energy monitoring, multi-hub management, and real-time climate/power consumption tracking via local network integration.
- [tqiqbal/mcp-confluence-server](https://github.com/tqiqbal/mcp-confluence-server) 🐍 - A Model Context Protocol (MCP) server for interacting with Confluence Data Center via REST API.
- [ttommyth/interactive-mcp](https://github.com/ttommyth/interactive-mcp) 📇 🏠 🍎 🪟 🐧 - Enables interactive LLM workflows by adding local user prompts and chat capabilities directly into the MCP loop.
- [tumf/web3-mcp](https://github.com/tumf/web3-mcp) 🐍 ☁️ - An MCP server implementation wrapping Ankr Advanced API. Access to NFT, token, and blockchain data across multiple chains including Ethereum, BSC, Polygon, Avalanche, and more.
- [W3Ship/w3ship-mcp-server](https://github.com/baskcart/w3ship-mcp-server) [![w3ship-mcp-server MCP server](https://glama.ai/mcp/servers/@baskcart/w3ship-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/@baskcart/w3ship-mcp-server) 📇 ☁️ 🏠 - AI-powered commerce MCP server with 22 tools: shopping cart (TMF663), orders (TMF622), shipment tracking (TMF621), session booking, Uniswap swaps, P2P marketplace, promo pickup, and cryptographic identity (SLH-DSA/ECDSA). No passwords — your wallet IS your account.
- [ujisati/anki-mcp](https://github.com/ujisati/anki-mcp) 🐍 🏠 - Manage your Anki collection with AnkiConnect & MCP
- [UnitVectorY-Labs/mcp-graphql-forge](https://github.com/UnitVectorY-Labs/mcp-graphql-forge) 🏎️ ☁️ 🍎 🪟 🐧 - A lightweight, configuration-driven MCP server that exposes curated GraphQL queries as modular tools, enabling intentional API interactions from your agents.
- [wanaku-ai/wanaku](https://github.com/wanaku-ai/wanaku) - ☁️ 🏠 The Wanaku MCP Router is a SSE-based MCP server that provides an extensible routing engine that allows integrating your enterprise systems with AI agents.
- [megberts/mcp-websitepublisher-ai](https://github.com/megberts/mcp-websitepublisher-ai) ☁️ - Build and publish websites through AI conversation. 27 MCP tools for pages, assets, entities, records and integrations. Remote server with OAuth 2.1 auto-discovery, works with Claude, ChatGPT, Mistral/Le Chat and Cursor.
- [wishfinity/wishfinity-mcp-plusw](https://github.com/wishfinity/wishfinity-mcp-plusw) 📇 ☁️ 🏠 - Universal wishlist for AI shopping experiences. Save any product URL from any store to a wishlist. Works with Claude, ChatGPT, LangChain, n8n, and any MCP client.
- [wong2/mcp-cli](https://github.com/wong2/mcp-cli) 📇 🏠 - CLI tool for testing MCP servers
- [ws-mcp](https://github.com/nick1udwig/ws-mcp) - Wrap MCP servers with a WebSocket (for use with [kitbitz](https://github.com/nick1udwig/kibitz))
- [0xMassi/webclaw](https://github.com/0xMassi/webclaw) [![webclaw MCP server](https://glama.ai/mcp/servers/0xMassi/webclaw/badges/score.svg)](https://glama.ai/mcp/servers/0xMassi/webclaw) 🦀 🏠 🍎 🐧 - Web content extraction for AI agents. 10 tools: scrape, crawl, map, batch, extract, summarize, diff, brand, search, research. TLS fingerprinting bypasses anti-bot without a browser. 67% fewer tokens than raw HTML. `npx create-webclaw` auto-configures Claude, Cursor, Windsurf, Codex, OpenCode.
- [yuna0x0/hackmd-mcp](https://github.com/yuna0x0/hackmd-mcp) 📇 ☁️ - Allows AI models to interact with [HackMD](https://hackmd.io)
- [ZeparHyfar/mcp-datetime](https://github.com/ZeparHyfar/mcp-datetime) - MCP server providing date and time functions in various formats
- [zueai/mcp-manager](https://github.com/zueai/mcp-manager) 📇 ☁️ - Simple Web UI to install and manage MCP servers for Claude Desktop App.
- [us-all/mlflow-mcp-server](https://github.com/us-all/mlflow-mcp-server) [![us-all/mlflow-mcp-server MCP server](https://glama.ai/mcp/servers/us-all/mlflow-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/us-all/mlflow-mcp-server) 📇 🏠 🍎 🪟 🐧 - MLflow — 82 tools across experiments, runs, registered models, model versions, traces, assessments. MLflow 3 GenAI traces support and 5 workflow Prompts (analyze-failed-traces, promote-best-run, compare-top-runs).
- [SPL-BGU/PlanningCopilot](https://github.com/SPL-BGU/PlanningCopilot) [![planning-copilot MCP server](https://glama.ai/mcp/servers/SPL-BGU/planning-copilot/badges/score.svg)](https://glama.ai/mcp/servers/SPL-BGU/planning-copilot) 🐍🏠 - A tool-augmented LLM system for the full PDDL planning pipeline, improving reliability without domain-specific training.
- [yyyhy/nash-arena](https://github.com/yyyhy/nash-arena) [![yyyhy/nash-arena MCP server](https://glama.ai/mcp/servers/yyyhy/nash-arena/badges/score.svg)](https://glama.ai/mcp/servers/yyyhy/nash-arena) 🐍 ☁️ - A Chess and Card Game Arena For LLM, Agents can battle in game by mcp
- [aarifmms/keyblind](https://github.com/aarifmms/keyblind) [![aarifmms/keyblind MCP server](https://glama.ai/mcp/servers/aarifmms/keyblind/badges/score.svg)](https://glama.ai/mcp/servers/aarifmms/keyblind) 📇 🏠 🍎 🪟 🐧 - Encrypted secrets vault with MCP for AI agents. Secrets resolved at runtime, never leaked to LLM conversations.
- [wundervault/wundervault-mcp](https://github.com/wundervault/wundervault-mcp) [![wundervault/wundervault-mcp MCP server](https://glama.ai/mcp/servers/wundervault/wundervault-mcp/badges/score.svg)](https://glama.ai/mcp/servers/wundervault/wundervault-mcp) 📇 ☁️ - Zero-knowledge secret vault for AI agents: use API keys, passwords, and SSH keys to run real commands (exec/rsync) with the secret injected into a single command — never returned to the model or shown in chat. Client-side AES-256-GCM, per-agent scoping, append-only audit log.
- [Skill Hub](https://github.com/rdone4425/skill) — AI Agent Skills navigator: 2,594+ skills across 8 platforms, with MCP-compatible skills.
## Frameworks

> [!NOTE]
> More frameworks, utilities, and other developer tools are available at https://github.com/punkpeye/awesome-mcp-devtools
> - [Nyrok/flompt](https://github.com/Nyrok/flompt) [![flompt MCP server](https://glama.ai/mcp/servers/@nyrok/flompt/badges/score.svg)](https://glama.ai/mcp/servers/@nyrok/flompt) 🐍 ☁️ - Visual AI prompt builder MCP server. Decompose any prompt into 12 semantic blocks and compile to Claude-optimized XML. Tools: `decompose_prompt`, `compile_prompt`. Setup: `claude mcp add flompt https://flompt.dev/mcp/`

- [escapeboy/agent-fleet-o](https://github.com/escapeboy/agent-fleet-o) [![escapeboy/agent-fleet-o MCP server](https://glama.ai/mcp/servers/escapeboy/agent-fleet-o/badges/score.svg)](https://glama.ai/mcp/servers/escapeboy/agent-fleet-o) ☁️ 🏠 - AI Agent Mission Control with 200+ MCP tools. Manage agents, experiments, workflows, crews, skills, and more via stdio + HTTP/SSE. Self-hosted, open-source (AGPL-3.0). Remote server: `https://fleetq.net/mcp`
- [Epistates/TurboMCP](https://github.com/Epistates/turbomcp) 🦀 - TurboMCP SDK: Enterprise MCP SDK in Rust
- [heymrun/heym](https://github.com/heymrun/heym) [![heymrun/heym MCP server](https://glama.ai/mcp/servers/heymrun/heym/badges/score.svg)](https://glama.ai/mcp/servers/heymrun/heym) 🐍 📇 🏠 - Source-available, self-hosted AI workflow automation platform. Build multi-agent, RAG, and tool-using pipelines on a visual canvas, then expose any workflow as an MCP server (stdio/SSE/Streamable HTTP), or call external MCP servers from the agent node.
- [zhangpanda/gomcp](https://github.com/zhangpanda/gomcp) [![zhangpanda/gomcp MCP server](https://glama.ai/mcp/servers/zhangpanda/gomcp/badges/score.svg)](https://glama.ai/mcp/servers/zhangpanda/gomcp) 🏎️ - A Gin-like framework for building MCP servers in Go. Struct-tag auto schema, middleware chain, auth, tool groups, adapters for Gin/OpenAPI/gRPC, async tasks, Inspector UI.
- [kioie/tiny-go-mcp-server](https://github.com/kioie/tiny-go-mcp-server) [![tiny-go-mcp-server MCP server](https://glama.ai/mcp/servers/kioie/tiny-go-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/kioie/tiny-go-mcp-server) 🏎️ 🏠 🍎 🪟 🐧 - Minimal Go wrapper on the official [modelcontextprotocol/go-sdk](https://github.com/modelcontextprotocol/go-sdk) for stdio MCP servers: struct-tag JSON Schema inference, `tinymcp` library, reference binary `tiny-go-mcp`, ~5MB static builds. For teams that want go-sdk compliance with minimal boilerplate (`go get github.com/kioie/tiny-go-mcp-server/tinymcp@v1.0.0`).
- [joinwell52-AI/FCoP](https://github.com/joinwell52-AI/FCoP) [![FCoP MCP server](https://glama.ai/mcp/servers/joinwell52-AI/FCoP/badges/score.svg)](https://glama.ai/mcp/servers/joinwell52-AI/FCoP/score) 🐍 🏠 - File-based Coordination Protocol: behavior governance layer for multi-agent teams. 45 MCP tools (write_task, write_report, write_issue, write_review, lifecycle claim/submit/approve…). Agents coordinate via structured Markdown files (\_lifecycle/\) — no message broker, no database, just the filesystem. Official MCP Registry: io.github.joinwell52-AI/fcop (v3.2.5). pip install fcop-mcp
- [FastMCP](https://github.com/jlowin/fastmcp) 🐍 - A high-level framework for building MCP servers in Python
- [jamjet-labs/jamjet](https://github.com/jamjet-labs/jamjet) [![jamjet-labs/jamjet MCP server](https://glama.ai/mcp/servers/jamjet-labs/jamjet/badges/score.svg)](https://glama.ai/mcp/servers/jamjet-labs/jamjet) 🦀 🐍 - Durable, agent-native AI runtime with native MCP client + server and A2A support. Rust core for performance, Python authoring for ergonomics. Features graph-based workflows, durable execution, and multi-agent coordination.
- [FastMCP](https://github.com/punkpeye/fastmcp) 📇 - A high-level framework for building MCP servers in TypeScript
- [SonAIengine/graph-tool-call](https://github.com/SonAIengine/graph-tool-call) [![graph-tool-call MCP server](https://glama.ai/mcp/servers/SonAIengine/graph-tool-call/badges/score.svg)](https://glama.ai/mcp/servers/SonAIengine/graph-tool-call) 🐍 🏠 - When tool count exceeds LLM context limits, accuracy collapses (248 tools → 12%). graph-tool-call builds a tool graph from OpenAPI/MCP specs and retrieves multi-step workflows via hybrid search (BM25 + graph traversal + embedding), recovering accuracy to 82% with 79% fewer tokens. Zero dependencies. Also works as an MCP Proxy — aggregate multiple MCP servers behind 3 meta-tools.
- [vinkius-labs/mcp-fusion](https://github.com/vinkius-labs/mcp-fusion) 📇 [![Glama](https://glama.ai/mcp/servers/badge/@vinkius-labs/mcp-fusion)](https://glama.ai/mcp/servers/@vinkius-labs/mcp-fusion) - A TypeScript framework for building production-ready MCP servers with automatic tool discovery, multi-transport support (stdio/SSE/HTTP), built-in validation, and zero-config setup.
- [MervinPraison/praisonai-mcp](https://github.com/MervinPraison/praisonai-mcp) 🐍 - AI Agents framework with 64+ built-in tools for search, memory, workflows, code execution, and file operations. Turn any AI assistant into a multi-agent system with MCP.
- [rocketride-org/rocketride-server](https://github.com/rocketride-org/rocketride-server) [![rocketride-org/rocketride-server MCP server](https://glama.ai/mcp/servers/rocketride-org/rocketride-server/badges/score.svg)](https://glama.ai/mcp/servers/rocketride-org/rocketride-server) 📇 🏠 - MCP server that exposes RocketRide AI pipelines as tools for Claude, Cursor, and Windsurf. Self-hosted, open-source pipeline tool with multi-LLM support.
- [shaqmughal/seekstone](https://github.com/shaqmughal/seekstone) 📇 🏠 🍎 🪟 🐧 - Filesystem-direct Obsidian MCP server with low context-tax. Reads your vault directly from disk — no Local REST API plugin required. ~575× smaller payloads than the REST plugin. 8 tools. `npx -y obsidian-mcp-seekstone` (also: `npx -y seekstone`)
- [vivek081166/japan-utils-mcp](https://github.com/vivek081166/japan-utils-mcp) [![vivek081166/japan-utils-mcp MCP server](https://glama.ai/mcp/servers/vivek081166/japan-utils-mcp/badges/score.svg)](https://glama.ai/mcp/servers/vivek081166/japan-utils-mcp) 🐍 🏠 🍎 🪟 🐧 - Japan-specific utilities for AI agents: era ↔ Western year conversion (令和8年 ↔ 2026), kanji-to-romaji transliteration, 7-digit postal code lookup, national holiday calendar, hiragana ↔ katakana conversion, full-width ↔ half-width normalization, and statistical Japanese name splitting. 9 tools, MIT licensed, installable via `uvx japan-utils-mcp`.

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
