# Awesome MCP Servers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

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
> Read [The State of MCP in 2025](https://glama.ai/blog/2025-12-07-the-state-of-mcp-in-2025) report.

> [!IMPORTANT]
> [Awesome MCP Servers](https://glama.ai/mcp/servers) web directory.

> [!IMPORTANT]
> Test servers using [MCP Inspector](https://glama.ai/mcp/inspector?servers=%5B%7B%22id%22%3A%22test%22%2C%22name%22%3A%22test%22%2C%22requestTimeout%22%3A10000%2C%22url%22%3A%22https%3A%2F%2Fmcp-test.glama.ai%2Fmcp%22%7D%5D).

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
* 👤 - [Customer Data Platforms](#customer-data-platforms)
* 🗄️ - [Databases](#databases)
* 📊 - [Data Platforms](#data-platforms)
* 🚚 - [Delivery](#delivery)
* 🛠️ - [Developer Tools](#developer-tools)
* 🧮 - [Data Science Tools](#data-science-tools)
* 📟 - [Embedded system](#embedded-system)
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
* 📋 - [Product Management](#product-management)
* 🔬 - [Research](#research)
* 🔎 - [Search & Data Extraction](#search)
* 🔒 - [Security](#security)
* 🌐 - [Social Media](#social-media)
* 🏃 - [Sports](#sports)
* 🎧 - [Support & Service Management](#support-and-service-management)
* 🌎 - [Translation Services](#translation-services)
* 🎧 - [Text-to-Speech](#text-to-speech)
* 🚆 - [Travel & Transportation](#travel-and-transportation)
* 🔄 - [Version Control](#version-control)
* 🏢 - [Workplace & Productivity](#workplace-and-productivity)
* 🛠️ - [Other Tools and Integrations](#other-tools-and-integrations)


### 🔗 <a name="aggregators"></a>Aggregators

Servers for accessing many apps and tools through a single MCP server.

- [1mcp/agent](https://github.com/1mcp-app/agent) 📇 ☁️ 🏠 🍎 🪟 🐧 - A unified Model Context Protocol server implementation that aggregates multiple MCP servers into one.
- [Aganium/agenium](https://github.com/Aganium/agenium) 📇 ☁️ 🍎 🪟 🐧 - Bridge any MCP server to the agent:// network — DNS-like identity, discovery, and trust for AI agents. Makes your tools discoverable and callable by other agents via `agent://` URIs with mTLS, trust scores, and capability search.
- [espadaw/Agent47](https://github.com/espadaw/Agent47) 📇 ☁️ - Unified job aggregator for AI agents across 9+ platforms (x402, RentAHuman, Virtuals, etc).
- [AgentHotspot](https://github.com/AgentHotspot/agenthotspot-mcp) 🐍 ☁️ 🏠 🍎 🪟 🐧 - Search, integrate and monetize MCP connectors on the AgentHotspot MCP marketplace
- [ariekogan/ateam-mcp](https://github.com/ariekogan/ateam-mcp) 📇 ☁️ 🏠 🍎 🪟 🐧 - Build, validate, and deploy multi-agent AI solutions on the ADAS platform. Design skills with tools, manage solution lifecycle, and connect from any AI environment via stdio or HTTP.
- [askbudi/roundtable](https://github.com/askbudi/roundtable) 📇 ☁️ 🏠 🍎 🪟 🐧 - Meta-MCP server that unifies multiple AI coding assistants (Codex, Claude Code, Cursor, Gemini) through intelligent auto-discovery and standardized MCP interface, providing zero-configuration access to the entire AI coding ecosystem.
- [blockrunai/blockrun-mcp](https://github.com/blockrunai/blockrun-mcp) 📇 ☁️ 🍎 🪟 🐧 - Access 30+ AI models (GPT-5, Claude, Gemini, Grok, DeepSeek) without API keys. Pay-per-use via x402 micropayments with USDC on Base.
- [Data-Everything/mcp-server-templates](https://github.com/Data-Everything/mcp-server-templates) 📇 🏠 🍎 🪟 🐧 - One server. All tools. A unified MCP platform that connects many apps, tools, and services behind one powerful interface—ideal for local devs or production agents.
- [duaraghav8/MCPJungle](https://github.com/duaraghav8/MCPJungle) 🏎️ 🏠 - Self-hosted MCP Server registry for enterprise AI Agents
- [edgarriba/prolink](https://github.com/edgarriba/prolink) 🐍 ☁️ 🏠 🍎 🪟 🐧 - Agent-to-agent marketplace middleware — MCP-native discovery, negotiation, and transaction between AI agents
- [glenngillen/mcpmcp-server](https://github.com/glenngillen/mcpmcp-server) ☁️ 📇 🍎 🪟 🐧 - A list of MCP servers so you can ask your client which servers you can use to improve your daily workflow.
- [hamflx/imagen3-mcp](https://github.com/hamflx/imagen3-mcp) 📇 🏠 🪟 🍎 🐧 - A powerful image generation tool using Google's Imagen 3.0 API through MCP. Generate high-quality images from text prompts with advanced photography, artistic, and photorealistic controls.
- [hashgraph-online/hashnet-mcp-js](https://github.com/hashgraph-online/hashnet-mcp-js) 📇 ☁️ 🍎 🪟 🐧 - MCP server for the Registry Broker. Discover, register, and chat with AI agents on the Hashgraph network.
- [isaac-levine/forage](https://github.com/isaac-levine/forage) 📇 🏠 🍎 🪟 🐧 - Self-improving tool discovery for AI agents. Searches registries, installs MCP servers as subprocesses, and persists tool knowledge across sessions — no restarts needed.
- [jaspertvdm/mcp-server-gemini-bridge](https://github.com/jaspertvdm/mcp-server-gemini-bridge) 🐍 ☁️ - Bridge to Google Gemini API. Access Gemini Pro and Flash models through MCP.
- [jaspertvdm/mcp-server-ollama-bridge](https://github.com/jaspertvdm/mcp-server-ollama-bridge) 🐍 🏠 - Bridge to local Ollama LLM server. Run Llama, Mistral, Qwen and other local models through MCP.
- [jaspertvdm/mcp-server-openai-bridge](https://github.com/jaspertvdm/mcp-server-openai-bridge) 🐍 ☁️ - Bridge to OpenAI API. Access GPT-4, GPT-4o and other OpenAI models through MCP.
- [julien040/anyquery](https://github.com/julien040/anyquery) 🏎️ 🏠 ☁️ - Query more than 40 apps with one binary using SQL. It can also connect to your PostgreSQL, MySQL, or SQLite compatible database. Local-first and private by design.
- [juspay/neurolink](https://github.com/juspay/neurolink) 📇 ☁️ 🏠 🍎 🪟 🐧 - Making enterprise AI infrastructure universally accessible. Edge-first platform unifying 12 providers and 100+ models with multi-agent orchestration, HITL workflows, guardrails middleware, and context summarization.
- [K-Dense-AI/claude-skills-mcp](https://github.com/K-Dense-AI/claude-skills-mcp) 🐍 ☁️ 🏠 🍎 🪟 🐧 - Intelligent search capabilities to let every model and client use [Claude Agent Skills](https://www.anthropic.com/news/skills) like native.
- [khalidsaidi/ragmap](https://github.com/khalidsaidi/ragmap) 📇 ☁️ 🏠 🍎 🪟 🐧 - MapRag: RAG-focused subregistry + MCP server to discover and route to retrieval-capable MCP servers using structured constraints and explainable ranking.
- [merterbak/Grok-MCP](https://github.com/merterbak/Grok-MCP) 🐍 ☁️ 🍎 🪟 🐧 - MCP server for xAI's [Grok API](https://docs.x.ai/docs/overview) with agentic tool calling, image generation, vision, and file support.
- [metatool-ai/metatool-app](https://github.com/metatool-ai/metatool-app) 📇 ☁️ 🏠 🍎 🪟 🐧 - MetaMCP is the one unified middleware MCP server that manages your MCP connections with GUI.
- [mindsdb/mindsdb](https://github.com/mindsdb/mindsdb) - Connect and unify data across various platforms and databases with [MindsDB as a single MCP server](https://docs.mindsdb.com/mcp/overview).
- [oxgeneral/agentnet](https://github.com/oxgeneral/agentnet) 🐍 ☁️ 🍎 🪟 🐧 - Agent-to-agent referral network where AI agents discover, recommend, and refer users to each other. Features bilateral trust model, credit economy, and 7 MCP tools for agent registration, discovery, and referral tracking.
- [particlefuture/MCPDiscovery](https://github.com/particlefuture/1mcpserver) 🐍 ☁️ 🏠 🍎 🪟 - MCP of MCPs. Automatic discovery and configure MCP servers on your local machine. 
- [PipedreamHQ/pipedream](https://github.com/PipedreamHQ/pipedream/tree/master/modelcontextprotocol) ☁️ 🏠 - Connect with 2,500 APIs with 8,000+ prebuilt tools, and manage servers for your users, in your own app.
- [portel-dev/ncp](https://github.com/portel-dev/ncp) 📇 ☁️ 🏠 🍎 🪟 🐧 - NCP orchestrates your entire MCP ecosystem through intelligent discovery, eliminating token overhead while maintaining 98.2% accuracy.
- [profullstack/mcp-server](https://github.com/profullstack/mcp-server) 📇 ☁️ 🏠 🍎 🪟 🐧 - A comprehensive MCP server aggregating 20+ tools including SEO optimization, document conversion, domain lookup, email validation, QR generation, weather data, social media posting, security scanning, and more developer utilities.
- [sitbon/magg](https://github.com/sitbon/magg) 🍎 🪟 🐧 ☁️ 🏠 🐍 - Magg: A meta-MCP server that acts as a universal hub, allowing LLMs to autonomously discover, install, and orchestrate multiple MCP servers - essentially giving AI assistants the power to extend their own capabilities on-demand.
- [sonnyflylock/voxie-ai-directory-mcp](https://github.com/sonnyflylock/voxie-ai-directory-mcp) 📇 ☁️ - AI Phone Number Directory providing access to AI services via webchat. Query Voxie AI personas and third-party services like ChatGPT, with instant webchat URLs for free interactions.
- [SureScaleAI/openai-gpt-image-mcp](https://github.com/SureScaleAI/openai-gpt-image-mcp) 📇 ☁️ - OpenAI GPT image generation/editing MCP server.
- [sxhxliang/mcp-access-point](https://github.com/sxhxliang/mcp-access-point) 📇 ☁️ 🏠 🍎 🪟 🐧 - Turn a web service into an MCP server in one click without making any code changes.
- [TheLunarCompany/lunar#mcpx](https://github.com/TheLunarCompany/lunar/tree/main/mcpx) 📇 🏠  ☁️ 🍎 🪟 🐧 - MCPX is a production-ready, open-source gateway to manage MCP servers at scale—centralize tool discovery, access controls, call prioritization, and usage tracking to simplify agent workflows.
- [thinkchainai/mcpbundles](https://github.com/thinkchainai/mcpbundles) - MCP Bundles: Create custom bundles of tools and connect providers with OAuth or API keys. Use one MCP server across thousands of integrations, with programmatic tool calling and MCP UI for managing bundles and credentials.
- [tigranbs/mcgravity](https://github.com/tigranbs/mcgravity) 📇 🏠 - A proxy tool for composing multiple MCP servers into one unified endpoint. Scale your AI tools by load balancing requests across multiple MCP servers, similar to how Nginx works for web servers.
- [VeriTeknik/pluggedin-mcp-proxy](https://github.com/VeriTeknik/pluggedin-mcp-proxy)  📇 🏠 - A comprehensive proxy server that combines multiple MCP servers into a single interface with extensive visibility features. It provides discovery and management of tools, prompts, resources, and templates across servers, plus a playground for debugging when building MCP servers.
- [ViperJuice/mcp-gateway](https://github.com/ViperJuice/mcp-gateway) 🐍 🏠 🍎 🪟 🐧 - A meta-server for minimal Claude Code tool bloat with progressive disclosure and dynamic server provisioning. Exposes 9 stable meta-tools, auto-starts Playwright and Context7, and can dynamically provision 25+ MCP servers on-demand from a curated manifest.
- [WayStation-ai/mcp](https://github.com/waystation-ai/mcp) ☁️ 🍎 🪟 - Seamlessly and securely connect Claude Desktop and other MCP hosts to your favorite apps (Notion, Slack, Monday, Airtable, etc.). Takes less than 90 secs.
- [wegotdocs/open-mcp](https://github.com/wegotdocs/open-mcp) 📇 🏠 🍎 🪟 🐧 - Turn a web API into an MCP server in 10 seconds and add it to the open source registry: https://open-mcp.org
- [YangLiangwei/PersonalizationMCP](https://github.com/YangLiangwei/PersonalizationMCP) 🐍 ☁️ 🏠 🍎 🪟 🐧 - Comprehensive personal data aggregation MCP server with Steam, YouTube, Bilibili, Spotify, Reddit and other platforms integrations. Features OAuth2 authentication, automatic token management, and 90+ tools for gaming, music, video, and social platform data access.

### 🚀 <a name="aerospace-and-astrodynamics"></a>Aerospace & Astrodynamics

- [IO-Aerospace-software-community/mcp-server](https://github.com/IO-Aerospace-software-engineering/mcp-server) #️⃣ ☁️/🏠 🐧 - IO Aerospace MCP Server: a .NET-based MCP server for aerospace & astrodynamics — ephemeris, orbital conversions, DSS tools, time conversions, and unit/math utilities. Supports STDIO and SSE transports; Docker and native .NET deployment documented.

### 🎨 <a name="art-and-culture"></a>Art & Culture

Access and explore art collections, cultural heritage, and museum databases. Enables AI models to search and analyze artistic and cultural content.

- [8enSmith/mcp-open-library](https://github.com/8enSmith/mcp-open-library) 📇 ☁️ - A MCP server for the Open Library API that enables AI assistants to search for book information.
- [abhiemj/manim-mcp-server](https://github.com/abhiemj/manim-mcp-server) 🐍 🏠 🪟 🐧 - A local MCP server that generates animations using Manim.
- [austenstone/myinstants-mcp](https://github.com/austenstone/myinstants-mcp) 📇 ☁️ 🏠 🍎 🪟 🐧 - A soundboard MCP server with millions of meme sounds from myinstants.com. Search, play, and browse categories — let your AI agent play vine boom when code compiles. `npx myinstants-mcp`
- [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) 🐍 - MCP server for working with Blender
- [aliafsahnoudeh/shahnameh-mcp-server](https://github.com/aliafsahnoudeh/shahnameh-mcp-server) 🐍 🏠 🍎 🪟 🐧 - MCP server for accessing the Shahnameh (Book of Kings) Persian epic poem by Ferdowsi, including sections, verses and explanations.
- [asmith26/jupytercad-mcp](https://github.com/asmith26/jupytercad-mcp) 🐍 🏠 🍎 🪟 🐧 - An MCP server for [JupyterCAD](https://github.com/jupytercad/JupyterCAD) that allows you to control it using LLMs/natural language.
- [burningion/video-editing-mcp](https://github.com/burningion/video-editing-mcp) 🐍 - Add, Analyze, Search, and Generate Video Edits from your Video Jungle Collection
- [cantian-ai/bazi-mcp](https://github.com/cantian-ai/bazi-mcp) 📇 🏠 ☁️ 🍎 🪟 - Provides comprehensive and accurate Bazi (Chinese Astrology) charting and analysis
- [ConstantineB6/comfy-pilot](https://github.com/ConstantineB6/comfy-pilot) 🐍 🏠 - MCP server for ComfyUI that lets AI agents view, edit, and run node-based image generation workflows with an embedded terminal.
- [cswkim/discogs-mcp-server](https://github.com/cswkim/discogs-mcp-server) 📇 ☁️ - MCP server to interact with the Discogs API
- [diivi/aseprite-mcp](https://github.com/diivi/aseprite-mcp) 🐍 🏠 - MCP server using the Aseprite API to create pixel art
- [djalal/quran-mcp-server](https://github.com/djalal/quran-mcp-server) 📇 ☁️ MCP server to interact with Quran.com corpus via the official REST API v4.
- [drakonkat/wizzy-mcp-tmdb](https://github.com/drakonkat/wizzy-mcp-tmdb) 📇 ☁️ - A MCP server for The Movie Database API that enables AI assistants to search and retrieve movie, TV show, and person information.
- [GenWaveLLC/svgmaker-mcp](https://github.com/GenWaveLLC/svgmaker-mcp) 📇 ☁️ - Provides AI-driven SVG generation and editing via natural language, with real-time updates and secure file handling.
- [khglynn/spotify-bulk-actions-mcp](https://github.com/khglynn/spotify-bulk-actions-mcp) 🐍 ☁️ - Bulk Spotify operations with confidence-scored song matching, batch playlist creation from CSV/podcast lists, and library exports for discovering your most-saved artists and albums.
- [mikechao/metmuseum-mcp](https://github.com/mikechao/metmuseum-mcp) 📇 ☁️ - Metropolitan Museum of Art Collection API integration to search and display artworks in the collection.
- [molanojustin/smithsonian-mcp](https://github.com/molanojustin/smithsonian-mcp) 🐍 ☁️ - MCP server that provides AI assistants with access to the Smithsonian Institution's Open Access collections.
- [OctoEverywhere/mcp](https://github.com/OctoEverywhere/mcp) #️⃣ ☁️ - A 3D printer MCP server that allows for getting live printer state, webcam snapshots, and printer control.
- [omni-mcp/isaac-sim-mcp](https://github.com/omni-mcp/isaac-sim-mcp) 📇 ☁️ - A MCP Server and an extension enables natural language control of NVIDIA Isaac Sim, Lab, OpenUSD and etc.
- [PatrickPalmer/MayaMCP](https://github.com/PatrickPalmer/MayaMCP) 🐍 🏠 - MCP server for Autodesk Maya
- [peek-travel/mcp-intro](https://github.com/peek-travel/mcp-intro) ☁️ 🍎 🪟 🐧 - Remote MCP Server for discovering and planning experiences, at home and on vacation
- [r-huijts/oorlogsbronnen-mcp](https://github.com/r-huijts/oorlogsbronnen-mcp) 📇 ☁️ - Oorlogsbronnen (War Sources) API integration for accessing historical WWII records, photographs, and documents from the Netherlands (1940-1945)
- [r-huijts/rijksmuseum-mcp](https://github.com/r-huijts/rijksmuseum-mcp) 📇 ☁️ - Rijksmuseum API integration for artwork search, details, and collections
- [raveenb/fal-mcp-server](https://github.com/raveenb/fal-mcp-server) 🐍 ☁️ - Generate AI images, videos, and music using Fal.ai models (FLUX, Stable Diffusion, MusicGen) directly in Claude Desktop
- [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) 🐍 - MCP server integration for DaVinci Resolve providing powerful tools for video editing, color grading, media management, and project control
- [TwelveTake-Studios/reaper-mcp](https://github.com/TwelveTake-Studios/reaper-mcp) 🐍 🏠 🍎 🪟 🐧 - MCP server enabling AI assistants to control REAPER DAW for mixing, mastering, MIDI composition, and full music production with 129 tools
- [yuna0x0/anilist-mcp](https://github.com/yuna0x0/anilist-mcp) 📇 ☁️ - A MCP server integrating AniList API for anime and manga information
- [yuvalsuede/agent-media](https://github.com/yuvalsuede/agent-media) 📇 ☁️ 🍎 🪟 🐧 - CLI and MCP server for AI video and image generation with unified access to 7 models (Kling, Veo, Sora, Seedance, Flux, Grok Imagine). Provides 9 tools for generating, managing, and browsing media.


### 📐 <a name="architecture-and-design"></a>Architecture & Design

Design and visualize software architecture, system diagrams, and technical documentation. Enables AI models to generate professional diagrams and architectural documentation.

- [betterhyq/mermaid-grammer-inspector-mcp](https://github.com/betterhyq/mermaid_grammer_inspector_mcp) 📇 🏠 🍎 🪟 🐧 - A Model Context Protocol (MCP) server for validating Mermaid diagram syntax and providing comprehensive grammar checking capabilities
- [GittyBurstein/mermaid-mcp-server](https://github.com/GittyBurstein/mermaid-mcp-server) 🐍 ☁️ - MCP server that turns local projects or GitHub repositories into Mermaid diagrams and renders them via Kroki.
- [Narasimhaponnada/mermaid-mcp](https://github.com/Narasimhaponnada/mermaid-mcp) 📇 ☁️ 🍎 🪟 🐧 - AI-powered Mermaid diagram generation with 22+ diagram types including flowcharts, sequence diagrams, class diagrams, ER diagrams, architecture diagrams, state machines, and more. Features 50+ pre-built templates, advanced layout engines, SVG/PNG/PDF exports, and seamless integration with GitHub Copilot, Claude, and any MCP-compatible client. Install via NPM: `npm install -g @narasimhaponnada/mermaid-mcp-server`

### <a name="bio"></a>Biology, Medicine and Bioinformatics

- [cafferychen777/ChatSpatial](https://github.com/cafferychen777/ChatSpatial) 🐍 🏠 - MCP server for spatial transcriptomics analysis with 60+ integrated methods covering cell annotation, deconvolution, spatial statistics, and visualization.
- [dnaerys/onekgpd-mcp](https://github.com/dnaerys/onekgpd-mcp) ☕ ☁️ 🍎 🪟 🐧- real-time access to 1000 Genomes Project dataset
- [genomoncology/biomcp](https://github.com/genomoncology/biomcp) 🐍 ☁️ - Biomedical research MCP server providing access to PubMed, ClinicalTrials.gov, and MyVariant.info.
- [hlydecker/ucsc-genome-mcp](https://github.com/hlydecker/ucsc-genome-mcp) 🐍 ☁️ - MCP server to interact with the UCSC Genome Browser API, letting you find genomes, chromosomes, and more.
- [JamesANZ/medical-mcp](https://github.com/JamesANZ/medical-mcp) 📇 🏠 - An MCP server that provides access to medical information, drug databases, and healthcare resources. Enables AI assistants to query medical data, drug interactions, and clinical guidelines.
- [longevity-genie/biothings-mcp](https://github.com/longevity-genie/biothings-mcp) 🐍 🏠 ☁️ - MCP server to interact with the BioThings API, including genes, genetic variants, drugs, and taxonomic information.
- [longevity-genie/gget-mcp](https://github.com/longevity-genie/gget-mcp) 🐍 🏠 ☁️ - MCP server providing a powerful bioinformatics toolkit for genomics queries and analysis, wrapping the popular `gget` library.
- [longevity-genie/opengenes-mcp](https://github.com/longevity-genie/opengenes-mcp) 🎖️ 🐍 🏠 ☁️ - MCP server for a queryable database for aging and longevity research from the OpenGenes project.
- [longevity-genie/synergy-age-mcp](https://github.com/longevity-genie/synergy-age-mcp) 🎖️ 🐍 🏠 ☁️ - MCP server for the SynergyAge database of synergistic and antagonistic genetic interactions in longevity.
- [OHNLP/omop_mcp](https://github.com/OHNLP/omop_mcp) 🐍 🏠 ☁️ - Map clinical terminology to OMOP concepts using LLMs for healthcare data standardization and interoperability.
- [the-momentum/apple-health-mcp-server](https://github.com/the-momentum/apple-health-mcp-server) 🐍 🏠 🍎 🪟 🐧 - An MCP server that provides access to exported data from Apple Health. Data analytics included.
- [the-momentum/fhir-mcp-server](https://github.com/the-momentum/fhir-mcp-server) 🐍 🏠 ☁️ - MCP Server that connects AI agents to FHIR servers. One example use case is querying patient history in natural language.
- [wso2/fhir-mcp-server](https://github.com/wso2/fhir-mcp-server) 🐍 🏠 ☁️ - Model Context Protocol server for Fast Healthcare Interoperability Resources (FHIR) APIs. Provides seamless integration with FHIR servers, enabling AI assistants to search, retrieve, create, update, and analyze clinical healthcare data with SMART-on-FHIR authentication support.

### 📂 <a name="browser-automation"></a>Browser Automation

Web content access and automation capabilities. Enables searching, scraping, and processing web content in AI-friendly formats.

- [34892002/bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js) 📇 🏠 - A MCP server that supports searching for Bilibili content. Provides LangChain integration examples and test scripts.
- [agent-infra/mcp-server-browser](https://github.com/bytedance/UI-TARS-desktop/tree/main/packages/agent-infra/mcp-servers/browser) 📇 🏠 - Browser automation capabilities using Puppeteer, both support local and remote browser connection.
- [automatalabs/mcp-server-playwright](https://github.com/Automata-Labs-team/MCP-Server-Playwright) 🐍 - An MCP server for browser automation using Playwright
- [BB-fat/browser-use-rs](https://github.com/BB-fat/browser-use-rs) 🦀 Lightweight browser automation MCP server in Rust with zero dependencies.
- [blackwhite084/playwright-plus-python-mcp](https://github.com/blackwhite084/playwright-plus-python-mcp) 🐍 - An MCP python server using Playwright for browser automation,more suitable for llm
- [browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) 🎖️ 📇 - Automate browser interactions in the cloud (e.g. web navigation, data extraction, form filling, and more)
- [browsermcp/mcp](https://github.com/browsermcp/mcp) 📇 🏠 - Automate your local Chrome browser
- [brutalzinn/simple-mcp-selenium](https://github.com/brutalzinn/simple-mcp-selenium) 📇 🏠 - An MCP Selenium Server for controlling browsers using natural language in Cursor IDE. Perfect for testing, automation, and multi-user scenarios.
- [co-browser/browser-use-mcp-server](https://github.com/co-browser/browser-use-mcp-server) 🐍 - browser-use packaged as an MCP server with SSE transport. includes a dockerfile to run chromium in docker + a vnc server.
- [eat-pray-ai/yutu](https://github.com/eat-pray-ai/yutu) 🏎️ 🏠 🍎 🐧 🪟 - A fully functional MCP server and CLI for YouTube to automate YouTube operation
- [executeautomation/playwright-mcp-server](https://github.com/executeautomation/mcp-playwright) 📇 - An MCP server using Playwright for browser automation and webscrapping
- [eyalzh/browser-control-mcp](https://github.com/eyalzh/browser-control-mcp) 📇 🏠 - An MCP server paired with a browser extension that enables LLM clients to control the user's browser (Firefox).
- [fradser/mcp-server-apple-reminders](https://github.com/FradSer/mcp-server-apple-reminders) 📇 🏠 🍎 - An MCP server for interacting with Apple Reminders on macOS
- [freema/firefox-devtools-mcp](https://github.com/freema/firefox-devtools-mcp) 📇 🏠 - Firefox browser automation via WebDriver BiDi for testing, scraping, and browser control. Supports snapshot/UID-based interactions, network monitoring, console capture, and screenshots.
- [getrupt/ashra-mcp](https://github.com/getrupt/ashra-mcp) 📇 🏠 - Extract structured data from any website. Just prompt and get JSON.
- [hanzili/comet-mcp](https://github.com/hanzili/comet-mcp) 📇 🏠 🍎 - Connect to Perplexity Comet browser for agentic web browsing, deep research, and real-time task monitoring.
- [LarryWalkerDEV/mcp-immostage](https://github.com/LarryWalkerDEV/mcp-immostage) 📇 ☁️ - AI virtual staging for real estate. Stage empty rooms, beautify floor plans into 3D renders, classify room images, generate property descriptions, and get style recommendations.
- [imprvhub/mcp-browser-agent](https://github.com/imprvhub/mcp-browser-agent) 📇 🏠 - A Model Context Protocol (MCP) integration that provides Claude Desktop with autonomous browser automation capabilities.
- [kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) 📇 ☁️ - Fetch YouTube subtitles and transcripts for AI analysis
- [kimtth/mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing) 🐍 🏠 - A `minimal` server/client MCP implementation using Azure OpenAI and Playwright.
- [lightpanda-io/gomcp](https://github.com/lightpanda-io/gomcp) 🏎 🏠/☁️ 🐧/🍎 - An MCP server in Go for Lightpanda, the ultra fast headless browser designed for web automation
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) - Official Microsoft Playwright MCP server, enabling LLMs to interact with web pages through structured accessibility snapshots
- [modelcontextprotocol/server-puppeteer](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/puppeteer) 📇 🏠 - Browser automation for web scraping and interaction
- [ndthanhdev/mcp-browser-kit](https://github.com/ndthanhdev/mcp-browser-kit) 📇 🏠 - An MCP Server that enables AI assistants to interact with your local browsers.
- [olostep/olostep-mcp-server](https://github.com/olostep/olostep-mcp-server) 📇 ☁️ - Web scraping, crawling, and search API. Extract content in Markdown/JSON, batch process 10k URLs, and get AI-powered answers with citations.
- [operative_sh/web-eval-agent](https://github.com/Operative-Sh/web-eval-agent) 🐍 🏠 🍎 - An MCP Server that autonomously debugs web applications with browser-use browser agents
- [Pantheon-Security/chrome-mcp-secure](https://github.com/Pantheon-Security/chrome-mcp-secure) 📇 🏠 🍎 🪟 🐧 - Security-hardened Chrome automation with post-quantum encryption (ML-KEM-768 + ChaCha20-Poly1305), secure credential vault, memory scrubbing, and audit logging. 22 tools for browser automation and secure logins.
- [PhungXuanAnh/selenium-mcp-server](https://github.com/PhungXuanAnh/selenium-mcp-server) 🐍 🏠 🍎 🪟 🐧 - A Model Context Protocol server providing web automation capabilities through Selenium WebDriver
- [pskill9/web-search](https://github.com/pskill9/web-search) 📇 🏠 - An MCP server that enables free web searching using Google search results, with no API keys required.
- [recursechat/mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts) 📇 🏠 🍎 - An MCP Server Integration with Apple Shortcuts
- [Retio-ai/pagemap](https://github.com/Retio-ai/Retio-pagemap) 🐍 🏠 - Compresses ~100K-token HTML into 2-5K-token structured maps while preserving every actionable element. AI agents can read and interact with any web page at 97% fewer tokens.
- [serkan-ozal/browser-devtools-mcp](https://github.com/serkan-ozal/browser-devtools-mcp) 📇 - An MCP Server enables AI assistants to autonomously test, debug, and validate web applications.
- [softvoyagers/pageshot-api](https://github.com/softvoyagers/pageshot-api) 📇 ☁️ - Free webpage screenshot capture API with format, viewport, and dark mode options. No API key required.
- [xspadex/bilibili-mcp](https://github.com/xspadex/bilibili-mcp.git) 📇 🏠 - A FastMCP-based tool that fetches Bilibili's trending videos and exposes them via a standard MCP interface.

### ☁️ <a name="cloud-platforms"></a>Cloud Platforms

Cloud platform service integration. Enables management and interaction with cloud infrastructure and services.

- [4everland/4everland-hosting-mcp](https://github.com/4everland/4everland-hosting-mcp) 🎖️ 📇 🏠 🍎 🐧 - An MCP server implementation for 4EVERLAND Hosting enabling instant deployment of AI-generated code to decentralized storage networks like Greenfield, IPFS, and Arweave.
- [aashari/mcp-server-aws-sso](https://github.com/aashari/mcp-server-aws-sso) 📇 ☁️ 🏠 - AWS Single Sign-On (SSO) integration enabling AI systems to securely interact with AWS resources by initiating SSO login, listing accounts/roles, and executing AWS CLI commands using temporary credentials.
- [alexbakers/mcp-ipfs](https://github.com/alexbakers/mcp-ipfs) 📇 ☁️ - upload and manipulation of IPFS storage
- [alexei-led/aws-mcp-server](https://github.com/alexei-led/aws-mcp-server) 🐍 ☁️ - A lightweight but powerful server that enables AI assistants to execute AWS CLI commands, use Unix pipes, and apply prompt templates for common AWS tasks in a safe Docker environment with multi-architecture support
- [alexei-led/k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server) 🐍 - A lightweight yet robust server that empowers AI assistants to securely execute Kubernetes CLI commands (`kubectl`, `helm`, `istioctl`, and `argocd`) using Unix pipes in a safe Docker environment with multi-architecture support.
- [aliyun/alibaba-cloud-ops-mcp-server](https://github.com/aliyun/alibaba-cloud-ops-mcp-server) 🎖️ 🐍 ☁️ - A MCP server that enables AI assistants to operation resources on Alibaba Cloud, supporting ECS, Cloud Monitor, OOS and widely used cloud products.
- [awslabs/mcp](https://github.com/awslabs/mcp) 🎖️ ☁️ - AWS MCP servers for seamless integration with AWS services and resources.
- [bright8192/esxi-mcp-server](https://github.com/bright8192/esxi-mcp-server) 🐍 ☁️ - A VMware ESXi/vCenter management server based on MCP (Model Control Protocol), providing simple REST API interfaces for virtual machine management.
- [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) 🎖️ 📇 ☁️ - Integration with Cloudflare services including Workers, KV, R2, and D1
- [cyclops-ui/mcp-cyclops](https://github.com/cyclops-ui/mcp-cyclops) 🎖️ 🏎️ ☁️ - An MCP server that allows AI agents to manage Kubernetes resources through Cyclops abstraction
- [elementfm/mcp](https://gitlab.com/elementfm/mcp) 🎖️ 🐍 📇 🏠 ☁️ - Open source podcast hosting platform
- [elevy99927/devops-mcp-webui](https://github.com/elevy99927/devops-mcp-webui) 🐍 ☁️/🏠 - MCP Server for Kubernetes integrated with Open-WebUI, bridging the gap between DevOps and non-technical teams. Supports `kubectl` and `helm` operations through natural-language commands.
- [erikhoward/adls-mcp-server](https://github.com/erikhoward/adls-mcp-server) 🐍 ☁️/🏠 - MCP Server for Azure Data Lake Storage. It can perform manage containers, read/write/upload/download operations on container files and manage file metadata.
- [espressif/esp-rainmaker-mcp](https://github.com/espressif/esp-rainmaker-mcp) 🎖️ 🐍 🏠 ☁️ 📟 - Official Espressif MCP Server to manage and control ESP RainMaker Devices.
- [flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) 📇 ☁️/🏠 - Typescript implementation of Kubernetes cluster operations for pods, deployments, services.
- [hardik-id/azure-resource-graph-mcp-server](https://github.com/hardik-id/azure-resource-graph-mcp-server) 📇 ☁️/🏠 - A Model Context Protocol server for querying and analyzing Azure resources at scale using Azure Resource Graph, enabling AI assistants to explore and monitor Azure infrastructure.
- [hashicorp/terraform-mcp-server](https://github.com/hashicorp/terraform-mcp-server) - 🎖️🏎️☁️ - The official Terraform MCP Server seamlessly integrates with the Terraform ecosystem, enabling provider discovery, module analysis, and direct Registry API integration for advanced Infrastructure as Code workflows.
- [jasonwilbur/cloud-cost-mcp](https://github.com/jasonwilbur/cloud-cost-mcp) 📇 ☁️ 🍎 🪟 🐧 - Multi-cloud pricing comparison across AWS, Azure, GCP, and OCI with 2,700+ instance types. Real-time pricing from public APIs, workload calculators, and migration savings estimator.
- [jasonwilbur/oci-pricing-mcp](https://github.com/jasonwilbur/oci-pricing-mcp) 📇 ☁️ - Oracle Cloud Infrastructure pricing data with 602 products, cost calculators, and cross-provider comparisons. One-command install for Claude.
- [jdubois/azure-cli-mcp](https://github.com/jdubois/azure-cli-mcp) - A wrapper around the Azure CLI command line that allows you to talk directly to Azure
- [johnneerdael/netskope-mcp](https://github.com/johnneerdael/netskope-mcp) 🔒 ☁️ - An MCP to give access to all Netskope Private Access components within a Netskope Private Access environments including detailed setup information and LLM examples on usage.
- [kestra-io/mcp-server-python](https://github.com/kestra-io/mcp-server-python) 🐍 ☁️ - Implementation of MCP server for [Kestra](https://kestra.io) workflow orchestration platform.
- [liquidmetal-ai/raindrop-mcp](https://docs.liquidmetal.ai/tutorials/claude-code-mcp-setup/) 📇 ☁️ - The best way to deploy cloud infrastructure using Claude Code and MCP.
- [liveblocks/liveblocks-mcp-server](https://github.com/liveblocks/liveblocks-mcp-server) 🎖️ 📇 ☁️ - Create, modify, and delete different aspects of [Liveblocks](https://liveblocks.io) such as rooms, threads, comments, notifications, and more. Additionally, it has read access to Storage and Yjs.
- [localstack/localstack-mcp-server](https://github.com/localstack/localstack-mcp-server) 🎖️ 📇 🏠 - A MCP server for LocalStack to manage local AWS environments, including lifecycle operations, infra deployments, log analysis, fault injection, and state management.
- [manusa/Kubernetes MCP Server](https://github.com/manusa/kubernetes-mcp-server) 🏎️ 🏠 A - powerful Kubernetes MCP server with additional support for OpenShift. Besides providing CRUD operations for **any** Kubernetes resource, this server provides specialized tools to interact with your cluster.
- [Nebula-Block-Data/nebulablock-mcp-server](https://github.com/Nebula-Block-Data/nebulablock-mcp-server) 📇 🏠 - integrates with the fastmcp library to expose the full range of NebulaBlock API functionalities as accessible tools
- [nwiizo/tfmcp](https://github.com/nwiizo/tfmcp) - 🦀 🏠 - A Terraform MCP server allowing AI assistants to manage and operate Terraform environments, enabling reading configurations, analyzing plans, applying configurations, and managing Terraform state.
- [openstack-kr/python-openstackmcp-server](https://github.com/openstack-kr/python-openstackmcp-server) 🐍 ☁️ - OpenStack MCP server for cloud infrastructure management based on openstacksdk.
- [pibblokto/cert-manager-mcp-server](https://github.com/pibblokto/cert-manager-mcp-server) 🐍 🍎/🐧 ☁️ - mcp server for [cert-manager](https://github.com/cert-manager/cert-manager) management and troubleshooting
- [portainer/portainer-mcp](https://github.com/portainer/portainer-mcp) 🏎️ ☁️/🏠 - A powerful MCP server that enables AI assistants to seamlessly interact with Portainer instances, providing natural language access to container management, deployment operations, and infrastructure monitoring capabilities.
- [pulumi/mcp-server](https://github.com/pulumi/mcp-server) 🎖️ 📇 🏠 - MCP server for interacting with Pulumi using the Pulumi Automation API and Pulumi Cloud API. Enables MCP clients to perform Pulumi operations like retrieving package information, previewing changes, deploying updates, and retrieving stack outputs programmatically.
- [pythonanywhere/pythonanywhere-mcp-server](https://github.com/pythonanywhere/pythonanywhere-mcp-server) 🐍 🏠 - MCP server implementation for PythonAnywhere cloud platform.
- [qiniu/qiniu-mcp-server](https://github.com/qiniu/qiniu-mcp-server) 🐍 ☁️ - A MCP built on Qiniu Cloud products, supporting access to Qiniu Cloud Storage, media processing services, etc.
- [redis/mcp-redis-cloud](https://github.com/redis/mcp-redis-cloud) 📇 ☁️ - Manage your Redis Cloud resources effortlessly using natural language. Create databases, monitor subscriptions, and configure cloud deployments with simple commands.
- [reza-gholizade/k8s-mcp-server](https://github.com/reza-gholizade/k8s-mcp-server) 🏎️ ☁️/🏠 - A Kubernetes Model Context Protocol (MCP) server that provides tools for interacting with Kubernetes clusters through a standardized interface, including API resource discovery, resource management, pod logs, metrics, and events.
- [rohitg00/kubectl-mcp-server](https://github.com/rohitg00/kubectl-mcp-server) 🐍 ☁️/🏠 - A Model Context Protocol (MCP) server for Kubernetes that enables AI assistants like Claude, Cursor, and others to interact with Kubernetes clusters through natural language.
- [rrmistry/tilt-mcp](https://github.com/rrmistry/tilt-mcp) 🐍 🏠 🍎 🪟 🐧 - A Model Context Protocol server that integrates with Tilt to provide programmatic access to Tilt resources, logs, and management operations for Kubernetes development environments.
- [silenceper/mcp-k8s](https://github.com/silenceper/mcp-k8s) 🏎️ ☁️/🏠 - MCP-K8S is an AI-driven Kubernetes resource management tool that allows users to operate any resources in Kubernetes clusters through natural language interaction, including native resources (like Deployment, Service) and custom resources (CRD). No need to memorize complex commands - just describe your needs, and AI will accurately execute the corresponding cluster operations, greatly enhancing the usability of Kubernetes.
- [Spaceship MCP](https://github.com/bartwaardenburg/spaceship-mcp) 📇 ☁️ - Manage domains, DNS records, contacts, marketplace listings, and more via the Spaceship API
- [spre-sre/lumino-mcp-server](https://github.com/spre-sre/lumino-mcp-server) 🐍 ☁️ - AI-powered SRE observability for Kubernetes and OpenShift with 40+ tools for Tekton pipeline debugging, log analysis, root cause analysis, and predictive monitoring.
- [StacklokLabs/mkp](https://github.com/StacklokLabs/mkp) 🏎️ ☁️ - MKP is a Model Context Protocol (MCP) server for Kubernetes that allows LLM-powered applications to interact with Kubernetes clusters. It provides tools for listing and applying Kubernetes resources through the MCP protocol.
- [StacklokLabs/ocireg-mcp](https://github.com/StacklokLabs/ocireg-mcp) 🏎️ ☁️ - An SSE-based MCP server that allows LLM-powered applications to interact with OCI registries. It provides tools for retrieving information about container images, listing tags, and more.
- [strowk/mcp-k8s-go](https://github.com/strowk/mcp-k8s-go) 🏎️ ☁️/🏠 - Kubernetes cluster operations through MCP
- [TencentCloudBase/CloudBase-AI-ToolKit](https://github.com/TencentCloudBase/CloudBase-AI-ToolKit) 📇 ☁️ 🏠 🍎 🪟 🐧 - One-stop backend services for WeChat Mini-Programs and full-stack apps. Provides specialized MCP tools for serverless cloud functions, databases, and one-click deployment to production with China market access through WeChat ecosystem.
- [thunderboltsid/mcp-nutanix](https://github.com/thunderboltsid/mcp-nutanix) 🏎️ 🏠/☁️ - Go-based MCP Server for interfacing with Nutanix Prism Central resources.
- [trilogy-group/aws-pricing-mcp](https://github.com/trilogy-group/aws-pricing-mcp) 🏎️ ☁️/🏠 - Get up-to-date EC2 pricing information with one call. Fast. Powered by a pre-parsed AWS pricing catalogue.
- [txn2/kubefwd](https://github.com/txn2/kubefwd) 🏎️ 🏠 - Kubernetes bulk port forwarding with service discovery, /etc/hosts management, traffic monitoring, and pod log streaming
- [VmLia/books-mcp-server](https://github.com/VmLia/books-mcp-server) 📇 ☁️ - This is an MCP server used for querying books, and it can be applied in common MCP clients, such as Cherry Studio.
- [weibaohui/k8m](https://github.com/weibaohui/k8m) 🏎️ ☁️/🏠 - Provides MCP multi-cluster Kubernetes management and operations, featuring a management interface, logging, and nearly 50 built-in tools covering common DevOps and development scenarios. Supports both standard and CRD resources.
- [weibaohui/kom](https://github.com/weibaohui/kom) 🏎️ ☁️/🏠 - Provides MCP multi-cluster Kubernetes management and operations. It can be integrated as an SDK into your own project and includes nearly 50 built-in tools covering common DevOps and development scenarios. Supports both standard and CRD resources.
- [wenhuwang/mcp-k8s-eye](https://github.com/wenhuwang/mcp-k8s-eye) 🏎️ ☁️/🏠 - MCP Server for kubernetes management, and analyze your cluster, application health

### 👨‍💻 <a name="code-execution"></a>Code Execution

Code execution servers. Allow LLMs to execute code in a secure environment, e.g. for coding agents.

- [alfonsograziano/node-code-sandbox-mcp](https://github.com/alfonsograziano/node-code-sandbox-mcp) 📇 🏠 – A Node.js MCP server that spins up isolated Docker-based sandboxes for executing JavaScript snippets with on-the-fly npm dependency installation and clean teardown
- [alvii147/piston-mcp](https://github.com/alvii147/piston-mcp) 🐍 ☁️ 🐧 🍎 🪟 - MCP server that lets LLMs execute code through the Piston remote code execution engine, with a zero-config `uv` setup and a ready-to-use Claude Desktop config example.
- [ckanthony/openapi-mcp](https://github.com/ckanthony/openapi-mcp) 🏎️ ☁️ - OpenAPI-MCP: Dockerized MCP Server to allow your AI agent to access any API with existing api docs.
- [dagger/container-use](https://github.com/dagger/container-use) 🏎️ 🏠 🐧 🍎 🪟 - Containerized environments for coding agents. Multiple agents can work independently, isolated in fresh containers and git branches. No conflicts, many experiments. Full execution history, terminal access to agent environments, git workflow. Any agent/model/infra stack.
- [gwbischof/outsource-mcp](https://github.com/gwbischof/outsource-mcp) 🐍 ☁️ - Give your AI assistant its own AI assistants. For example: "Could you ask openai to generate an image of a dog?"
- [hileamlakB/PRIMS](https://github.com/hileamlakB/PRIMS) 🐍 🏠 – A Python Runtime Interpreter MCP Server that executes user-submitted code in an isolated environment.
- [ouvreboite/openapi-to-mcp](https://github.com/ouvreboite/openapi-to-mcp) #️⃣ ☁️ - Lightweight MCP server to access any API using their OpenAPI specification. Supports OAuth2 and full JSON schema parameters and request body.
- [pydantic/pydantic-ai/mcp-run-python](https://github.com/pydantic/pydantic-ai/tree/main/mcp-run-python) 🐍 🏠 - Run Python code in a secure sandbox via MCP tool calls
- [r33drichards/mcp-js](https://github.com/r33drichards/mcp-js) 🦀 🏠 🐧 🍎 - A Javascript code execution sandbox that uses v8 to isolate code to run AI generated javascript locally without fear. Supports heap snapshotting for persistent sessions.
- [yepcode/mcp-server-js](https://github.com/yepcode/mcp-server-js) 🎖️ 📇 ☁️ - Execute any LLM-generated code in a secure and scalable sandbox environment and create your own MCP tools using JavaScript or Python, with full support for NPM and PyPI packages

### 🤖 <a name="coding-agents"></a>Coding Agents

Full coding agents that enable LLMs to read, edit, and execute code and solve general programming tasks completely autonomously.

- [agentic-mcp-tools/owlex](https://github.com/agentic-mcp-tools/owlex) 🐍 🏠 🍎 🪟 🐧 - AI council server: query CLI agents (Claude Code, Codex, Gemini, and OpenCode) in parallel with deliberation rounds
- [alpadalar/netops-mcp](https://github.com/alpadalar/netops-mcp) 🐍 🏠 - Comprehensive DevOps and networking MCP server providing standardized access to essential infrastructure tools. Features network monitoring, system diagnostics, automation workflows, and infrastructure management with AI-powered operational insights.
- [askbudi/roundtable](https://github.com/askbudi/roundtable) 🐍 🏠 - Zero-configuration MCP server that unifies multiple AI coding assistants (Claude Code, Cursor, Codex) through intelligent auto-discovery and standardized interface. Essential infrastructure for autonomous agent development and multi-AI collaboration workflows.
- [automateyournetwork/pyATS_MCP](https://github.com/automateyournetwork/pyATS_MCP) - Cisco pyATS server enabling structured, model-driven interaction with network devices.
- [aybelatchane/mcp-server-terminal](https://github.com/aybelatchane/mcp-server-terminal) 🦀 🏠 🍎 🪟 🐧 - Playwright for terminals - interact with TUI/CLI applications through structured Terminal State Tree representation with element detection.
- [aymericzip/intlayer](https://github.com/aymericzip/intlayer) 📇 ☁️ 🏠 - A MCP Server that enhance your IDE with AI-powered assistance for Intlayer i18n / CMS tool: smart CLI access, access to the docs.
- [spyrae/claude-concilium](https://github.com/spyrae/claude-concilium) 📇 🏠 🍎 🪟 🐧 - Multi-agent AI consultation framework for Claude Code. Three MCP servers wrapping CLI tools (Codex, Gemini, Qwen) for parallel code review and problem-solving with fallback chains and error detection. Includes ready-to-use Claude Code skill.
- [blakerouse/ssh-mcp](https://github.com/blakerouse/ssh-mcp) 🏎️ 🏠 🍎 🪟 🐧 - MCP server exposing SSH control for Linux and Windows servers. Allows long running commands and the ability to perform commands on multiple hosts at the same time.
- [doggybee/mcp-server-leetcode](https://github.com/doggybee/mcp-server-leetcode) 📇 ☁️ - An MCP server that enables AI models to search, retrieve, and solve LeetCode problems. Supports metadata filtering, user profiles, submissions, and contest data access.
- [eirikb/any-cli-mcp-server](https://github.com/eirikb/any-cli-mcp-server) 📇 🏠 - Universal MCP server that transforms any CLI tool into an MCP server. Works with any CLI that has `--help` output, supports caching for performance.
- [ezyang/codemcp](https://github.com/ezyang/codemcp) 🐍 🏠 - Coding agent with basic read, write and command line tools.
- [elhamid/llm-council](https://github.com/elhamid/llm-council) 🐍 🏠 - Multi-LLM deliberation with anonymized peer review. Runs a 3-stage council: parallel responses → anonymous ranking → synthesis. Based on Andrej Karpathy's LLM Council concept.
- [ferrislucas/iterm-mcp](https://github.com/ferrislucas/iterm-mcp) 🖥️ 🛠️ 💬 - A Model Context Protocol server that provides access to iTerm. You can run commands and ask questions about what you see in the iTerm terminal.
- [g0t4/mcp-server-commands](https://github.com/g0t4/mcp-server-commands) 📇 🏠 - Run any command with `run_command` and `run_script` tools.
- [gabrielmaialva33/winx-code-agent](https://github.com/gabrielmaialva33/winx-code-agent) 🦀 🏠 - A high-performance Rust reimplementation of WCGW for code agents, providing shell execution and advanced file management capabilities for LLMs via MCP.
- [irskep/persistproc](https://github.com/irskep/persistproc) 🐍 🏠 - MCP server + command line tool that allows agents to see & control long-running processes like web servers. Start, stop, restart, read logs.
- [jinzcdev/leetcode-mcp-server](https://github.com/jinzcdev/leetcode-mcp-server) 📇 ☁️ - MCP server enabling automated access to **LeetCode**'s programming problems, solutions, submissions and public data with optional authentication for user-specific features (e.g., notes), supporting both `leetcode.com` (global) and `leetcode.cn` (China) sites.
- [juehang/vscode-mcp-server](https://github.com/juehang/vscode-mcp-server) 📇 🏠 - A MCP Server that allows AI such as Claude to read from the directory structure in a VS Code workspace, see problems picked up by linter(s) and the language server, read code files, and make edits.
- [louis030195/terminator-mcp-agent](https://github.com/mediar-ai/terminator/tree/main/terminator-mcp-agent) 🦀 📇 🏠 🍎 🪟 🐧 - Desktop GUI automation using accessibility APIs. Control Windows, macOS, and Linux applications without vision models or screenshots. Supports workflow recording, structured data extraction, and browser DOM inspection.
- [maxim-saplin/mcp_safe_local_python_executor](https://github.com/maxim-saplin/mcp_safe_local_python_executor) - Safe Python interpreter based on HF Smolagents `LocalPythonExecutor`
- [micl2e2/code-to-tree](https://github.com/micl2e2/code-to-tree) 🌊 🏠 📟 🐧 🪟 🍎 - A single-binary MCP server that converts source code into AST, regardless of language.
- [misiektoja/kill-process-mcp](https://github.com/misiektoja/kill-process-mcp) 🐍 🏠 🍎 🪟 🐧 - List and terminate OS processes via natural language queries
- [MladenSU/cli-mcp-server](https://github.com/MladenSU/cli-mcp-server) 🐍 🏠 - Command line interface with secure execution and customizable security policies
- [nesquikm/mcp-rubber-duck](https://github.com/nesquikm/mcp-rubber-duck) 📇 🏠 ☁️ - An MCP server that bridges to multiple OpenAI-compatible LLMs - your AI rubber duck debugging panel for explaining problems to various AI "ducks" and getting different perspectives
- [nihalxkumar/arch-mcp](https://github.com/nihalxkumar/arch-mcp) 🐍 🏠 🐧 - Arch Linux MCP Server to the Arch Linux ecosystem of the Arch Wiki, AUR, and official repositories for AI-assisted Arch Linux usage on Arch and non-Arch systems. Features include searching Arch Wiki and AUR, getting package info, checking for updates, installing packages securely, and analyzing PKGBUILDs.
- [ooples/mcp-console-automation](https://github.com/ooples/mcp-console-automation) 📇 🏠 🍎 🪟 🐧 - Production-ready MCP server for AI-driven console automation and monitoring. 40 tools for session management, SSH, testing, monitoring, and background jobs. Like Playwright for terminal applications.
- [oraios/serena](https://github.com/oraios/serena) 🐍 🏠 - A fully-featured coding agent that relies on symbolic code operations by using language servers.
- [OthmaneBlial/term_mcp_deepseek](https://github.com/OthmaneBlial/term_mcp_deepseek) 🐍 🏠 - A DeepSeek MCP-like Server for Terminal
- [pdavis68/RepoMapper](https://github.com.mcas.ms/pdavis68/RepoMapper) 🐧 🪟 🍎 - An MCP server (and command-line tool) to provide a dynamic map of chat-related files from the repository with their function prototypes and related files in order of relevance. Based on the "Repo Map" functionality in Aider.chat
- [religa/multi-mcp](https://github.com/religa/multi_mcp) 🐍 🍎 🪟 🐧 - Parallel multi-model code review, security analysis, and AI debate with ChatGPT, Claude, and Gemini. Orchestrates multiple LLMs for compare, consensus, and OWASP Top 10 security checks.
- [rinadelph/Agent-MCP](https://github.com/rinadelph/Agent-MCP) 🐍 🏠 - A framework for creating multi-agent systems using MCP for coordinated AI collaboration, featuring task management, shared context, and RAG capabilities.
- [shashankss1205/codegraphcontext](https://github.com/Shashankss1205/CodeGraphContext) 🐍 🏠 🍎 🪟 🐧 An MCP server that indexes local code into a graph database to provide context to AI assistants with a graphical code visualizations for humans.
- [sim-xia/blind-auditor](https://github.com/Sim-xia/Blind-Auditor) 🐍 🏠 🍎 🪟 🐧 - A zero-cost MCP server that forces AI to self-correct generation messages using prompt injection, independent self-audition and context isolation.
- [sim-xia/skill-cortex-server](https://github.com/Sim-xia/skill-cortex-server) 🐍 🏠 🍎 🪟 🐧 - An MCP server that enable all IDEs/CLIs to access Claude Code Skills capabilities.
- [sonirico/mcp-shell](https://github.com/sonirico/mcp-shell) - 🏎️ 🏠 🍎 🪟 🐧 Give hands to AI. MCP server to run shell commands securely, auditably, and on demand on isolated environments like docker.
- [stippi/code-assistant](https://github.com/stippi/code-assistant) 🦀 🏠 - Coding agent with basic list, read, replace_in_file, write, execute_command and web search tools. Supports multiple projects concurrently.
- [SunflowersLwtech/mcp_creator_growth](https://github.com/SunflowersLwtech/mcp_creator_growth) 🐍 🏠 🍎 🪟 🐧 - Intelligent learning sidecar for AI coding assistants. Helps developers learn from AI-generated code changes through interactive blocking quizzes and provides agents with persistent project-specific debugging memory using silent RAG tools. Features 56% token optimization and multi-language support.
- [tiianhk/MaxMSP-MCP-Server](https://github.com/tiianhk/MaxMSP-MCP-Server) 🐍 🏠 🎵 🎥 - A coding agent for Max (Max/MSP/Jitter), which is a visual programming language for music and multimedia.
- [tufantunc/ssh-mcp](https://github.com/tufantunc/ssh-mcp) 📇 🏠 🐧 🪟 - MCP server exposing SSH control for Linux and Windows servers via Model Context Protocol. Securely execute remote shell commands with password or SSH key authentication.
- [tumf/mcp-shell-server](https://github.com/tumf/mcp-shell-server) - A secure shell command execution server implementing the Model Context Protocol (MCP)
- [VertexStudio/developer](https://github.com/VertexStudio/developer) 🦀 🏠 🍎 🪟 🐧 - Comprehensive developer tools for file editing, shell command execution, and screen capture capabilities
- [wende/cicada](https://github.com/wende/cicada) 🐍 🏠 🍎 🪟 🐧 - Code Intelligence for Elixir: module search, function tracking, and PR attribution through tree-sitter AST parsing
- [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) 📇 🏠 🍎 🪟 🐧 - A swiss-army-knife that can manage/execute programs and read/write/search/edit code and text files.
- [x51xxx/codex-mcp-tool](https://github.com/x51xxx/codex-mcp-tool) 📇 ☁️ - MCP server that connects your IDE or AI assistant to Codex CLI for code analysis and editing with support for multiple models (gpt-5-codex, o3, codex-1)
- [x51xxx/copilot-mcp-server](https://github.com/x51xxx/copilot-mcp-server) 📇 ☁️ - MCP server that connects your IDE or AI assistant to GitHub Copilot CLI for code analysis, review, and batch processing
### 🖥️ <a name="command-line"></a>Command Line
Run commands, capture output and otherwise interact with shells and command line tools.

- [danmartuszewski/hop](https://github.com/danmartuszewski/hop) 🏎️ 🖥️ - Fast SSH connection manager with TUI dashboard and MCP server for discovering, searching, and executing commands on remote hosts.

### 💬 <a name="communication"></a>Communication

Integration with communication platforms for message management and channel operations. Enables AI models to interact with team communication tools.

- [AbdelStark/nostr-mcp](https://github.com/AbdelStark/nostr-mcp) ☁️ - A Nostr MCP server that allows to interact with Nostr, enabling posting notes, and more.
- [adhikasp/mcp-twikit](https://github.com/adhikasp/mcp-twikit) 🐍 ☁️ - Interact with Twitter search and timeline
- [agentmail-toolkit/mcp](https://github.com/agentmail-to/agentmail-toolkit/tree/main/mcp) 🐍 💬 - An MCP server to create inboxes on the fly to send, receive, and take actions on email. We aren't AI agents for email, but email for AI Agents.
- [areweai/tsgram-mcp](https://github.com/areweai/tsgram-mcp) - TSgram: Telegram + Claude with local workspace access on your phone in typescript. Read, write, and vibe code on the go!
- [arpitbatra123/mcp-googletasks](https://github.com/arpitbatra123/mcp-googletasks) 📇 ☁️ - An MCP server to interface with the Google Tasks API
- [Cactusinhand/mcp_server_notify](https://github.com/Cactusinhand/mcp_server_notify) 🐍 🏠 - A MCP server that send desktop notifications with sound effect when agent tasks are completed.
- [carterlasalle/mac_messages_mcp](https://github.com/carterlasalle/mac_messages_mcp) 🏠 🍎 🚀 - An MCP server that securely interfaces with your iMessage database via the Model Context Protocol (MCP), allowing LLMs to query and analyze iMessage conversations. It includes robust phone number validation, attachment processing, contact management, group chat handling, and full support for sending and receiving messages.
- [chaindead/telegram-mcp](https://github.com/chaindead/telegram-mcp) 🏎️ 🏠 - Telegram API integration for accessing user data, managing dialogs (chats, channels, groups), retrieving messages, and handling read status
- [chigwell/telegram-mcp](https://github.com/chigwell/telegram-mcp) 🐍 🏠 - Telegram API integration for accessing user data, managing dialogs (chats, channels, groups), retrieving messages, sending messages and handling read status.
- [codefuturist/email-mcp](https://github.com/codefuturist/email-mcp) 📇 ☁️ 🍎 🪟 🐧 - IMAP/SMTP email MCP server with 42 tools for reading, searching, sending, scheduling, and managing emails across multiple accounts. Supports IMAP IDLE push, AI triage, desktop notifications, and auto-detects providers like Gmail, Outlook, and iCloud.
- [conarti/mattermost-mcp](https://github.com/conarti/mattermost-mcp) 📇 ☁️ - MCP server for Mattermost API. List channels, read/post messages, manage threads and reactions, monitor topics. Supports flexible configuration via CLI args, environment variables, or config files.
- [Danielpeter-99/calcom-mcp](https://github.com/Danielpeter-99/calcom-mcp) 🐍 🏠 - MCP server for Calcom. Manage event types, create bookings, and access Cal.com scheduling data through LLMs.
- [discourse/discourse-mcp](https://github.com/discourse/discourse-mcp) 🎖️ 💎 ☁️ 🏠 💬 🍎 🪟 🐧 - Official Discourse MCP server for forum integration. Search topics, read posts, manage categories and tags, discover users, and interact with Discourse communities.
- [elie222/inbox-zero](https://github.com/elie222/inbox-zero/tree/main/apps/mcp-server) 🐍 ☁️ - An MCP server for Inbox Zero. Adds functionality on top of Gmail like finding out which emails you need to reply to or need to follow up on.
- [FastAlertNow/mcp-server](https://github.com/FastAlertNow/mcp-server) 🎖️ 📇 ☁️ - Official Model Context Protocol (MCP) server for FastAlert. This server allows AI agents (like Claude, ChatGPT, and Cursor) to list of your channels and send notifications directly through the FastAlert API.
- [gerkensm/callcenter.js-mcp](https://github.com/gerkensm/callcenter.js-mcp) 📇 ☁️ - An MCP server to make phone calls using VoIP/SIP and OpenAI's Realtime API and observe the transcript.
- [gitmotion/ntfy-me-mcp](https://github.com/gitmotion/ntfy-me-mcp) 📇 ☁️ 🏠 - An ntfy MCP server for sending/fetching ntfy notifications to your self-hosted ntfy server from AI Agents 📤 (supports secure token auth & more - use with npx or docker!)
- [gotoolkits/wecombot](https://github.com/gotoolkits/mcp-wecombot-server.git) 🚀 ☁️ - An MCP server application that sends various types of messages to the WeCom group robot.
- [hannesrudolph/imessage-query-fastmcp-mcp-server](https://github.com/hannesrudolph/imessage-query-fastmcp-mcp-server) 🐍 🏠 🍎 - An MCP server that provides safe access to your iMessage database through Model Context Protocol (MCP), enabling LLMs to query and analyze iMessage conversations with proper phone number validation and attachment handling
- [i-am-bee/acp-mcp](https://github.com/i-am-bee/acp-mcp) 🐍 💬 - An MCP server acting as an adapter into the [ACP](https://agentcommunicationprotocol.dev) ecosystem. Seamlessly exposes ACP agents to MCP clients, bridging the communication gap between the two protocols.
- [InditexTech/mcp-teams-server](https://github.com/InditexTech/mcp-teams-server) 🐍 ☁️ - MCP server that integrates Microsoft Teams messaging (read, post, mention, list members and threads)
- [Infobip/mcp](https://github.com/infobip/mcp) 🎖️ ☁️ - Official Infobip MCP server for integrating Infobip global cloud communication platform. It equips AI agents with communication superpowers, allowing them to send and receive SMS and RCS messages, interact with WhatsApp and Viber, automate communication workflows, and manage customer data, all in a production-ready environment.
- [jagan-shanmugam/mattermost-mcp-host](https://github.com/jagan-shanmugam/mattermost-mcp-host) 🐍 🏠 - A MCP server along with MCP host that provides access to Mattermost teams, channels and messages. MCP host is integrated as a bot in Mattermost with access to MCP servers that can be configured.
- [jaipandya/producthunt-mcp-server](https://github.com/jaipandya/producthunt-mcp-server) 🐍 🏠 - MCP server for Product Hunt. Interact with trending posts, comments, collections, users, and more.
- [jaspertvdm/mcp-server-rabel](https://github.com/jaspertvdm/mcp-server-rabel) 🐍 ☁️ 🏠 - AI-to-AI messaging via I-Poll protocol and AInternet. Enables agents to communicate using .aint domains, semantic messaging, and trust-based routing.
- [joinly-ai/joinly](https://github.com/joinly-ai/joinly) 🐍☁️ - MCP server to interact with browser-based meeting platforms (Zoom, Teams, Google Meet). Enables AI agents to send bots to online meetings, gather live transcripts, speak text, and send messages in the meeting chat.
- [jtalk22/slack-mcp-server](https://github.com/jtalk22/slack-mcp-server) 📇 ☁️ 🏠 🍎 🪟 🐧 - Your complete Slack context for Claude—DMs, channels, threads, search. No OAuth apps, no admin approval. `--setup` and done, 11 tools, auto-refresh.
- [keturiosakys/bluesky-context-server](https://github.com/keturiosakys/bluesky-context-server) 📇 ☁️ - Bluesky instance integration for querying and interaction
- [khan2a/telephony-mcp-server](https://github.com/khan2a/telephony-mcp-server) 🐍 💬 - MCP Telephony server for automating voice calls with Speech-to-Text and Speech Recognition to summarize call conversations. Send and receive SMS, detect voicemail, and integrate with Vonage APIs for advanced telephony workflows.
- [korotovsky/slack-mcp-server](https://github.com/korotovsky/slack-mcp-server) 📇 ☁️ - The most powerful MCP server for Slack Workspaces.
- [lharries/whatsapp-mcp](https://github.com/lharries/whatsapp-mcp) 🐍 🏎️ - An MCP server for searching your personal WhatsApp messages, contacts and sending messages to individuals or groups
- [line/line-bot-mcp-server](https://github.com/line/line-bot-mcp-server) 🎖 📇 ☁️ - MCP Server for Integrating LINE Official Account
- [Leximo-AI/leximo-ai-call-assistant-mcp-server](https://github.com/Leximo-AI/leximo-ai-call-assistant-mcp-server) 📇 ☁️ - Make AI-powered phone calls on your behalf — book reservations, schedule appointments, and view call transcripts
- [madbonez/caldav-mcp](https://github.com/madbonez/caldav-mcp) 🐍 ☁️ - Universal MCP server for CalDAV protocol integration. Works with any CalDAV-compatible calendar server including Yandex Calendar, Google Calendar (via CalDAV), Nextcloud, ownCloud, Apple iCloud, and others. Supports creating events with recurrence, categories, priority, attendees, reminders, searching events, and retrieving events by UID.
- [marlinjai/email-mcp](https://github.com/marlinjai/email-mcp) 📇 ☁️ 🏠 - Unified MCP server for email across Gmail (REST API), Outlook (Microsoft Graph), iCloud, and generic IMAP/SMTP. 24 tools for search, send, organize, and batch-manage emails with built-in OAuth2 and encrypted credential storage.
- [OverQuotaAI/chatterboxio-mcp-server](https://github.com/OverQuotaAI/chatterboxio-mcp-server) 📇 ☁️ - MCP server implementation for ChatterBox.io, enabling AI agents to send bots to online meetings (Zoom, Google Meet) and obtain transcripts and recordings.
- [PhononX/cv-mcp-server](https://github.com/PhononX/cv-mcp-server) 🎖️ 📇 🏠 ☁️ 🍎 🪟 🐧 - MCP Server that connects AI Agents to [Carbon Voice](https://getcarbon.app). Create, manage, and interact with voice messages, conversations, direct messages, folders, voice memos, AI actions and more in [Carbon Voice](https://getcarbon.app).
- [saseq/discord-mcp](https://github.com/SaseQ/discord-mcp) ☕ 📇 🏠 💬 - A MCP server for the Discord integration. Enable your AI assistants to seamlessly interact with Discord. Enhance your Discord experience with powerful automation capabilities.
- [sawa-zen/vrchat-mcp](https://github.com/sawa-zen/vrchat-mcp) - 📇 🏠 This is an MCP server for interacting with the VRChat API. You can retrieve information about friends, worlds, avatars, and more in VRChat.
- [softeria/ms-365-mcp-server](https://github.com/softeria/ms-365-mcp-server) 📇 ☁️ - MCP server that connects to Microsoft Office and the whole Microsoft 365 suite using Graph API (including Outlook, mail, files, Excel, calendar)
- [teddyzxcv/ntfy-mcp](https://github.com/teddyzxcv/ntfy-mcp) - The MCP server that keeps you informed by sending the notification on phone using ntfy
- [trycourier/courier-mcp](https://github.com/trycourier/courier-mcp) 🎖️ 💬 ☁️ 🛠️ 📇 🤖 - Build multi-channel notifications into your product, send messages, update lists, invoke automations, all without leaving your AI coding space.
- [userad/didlogic_mcp](https://github.com/UserAd/didlogic_mcp) 🐍 ☁️ - An MCP server for [DIDLogic](https://didlogic.com). Adds functionality to manage SIP endpoints, numbers and destinations.
- [wyattjoh/imessage-mcp](https://github.com/wyattjoh/imessage-mcp) 📇 🏠 🍎 - A Model Context Protocol server for reading iMessage data from macOS.
- [wyattjoh/jmap-mcp](https://github.com/wyattjoh/jmap-mcp) 📇 ☁️ - A Model Context Protocol (MCP) server that provides tools for interacting with JMAP (JSON Meta Application Protocol) email servers. Built with Deno and using the jmap-jam client library.
- [YCloud-Developers/ycloud-whatsapp-mcp-server](https://github.com/YCloud-Developers/ycloud-whatsapp-mcp-server) 📇 🏠 - MCP server for WhatsApp Business Platform by YCloud.
- [zcaceres/gtasks-mcp](https://github.com/zcaceres/gtasks-mcp) 📇 ☁️ - An MCP server to Manage Google Tasks
- [ztxtxwd/open-feishu-mcp-server](https://github.com/ztxtxwd/open-feishu-mcp-server) 📇 ☁️ 🏠 - A Model Context Protocol (MCP) server with built-in Feishu OAuth authentication, supporting remote connections and providing comprehensive Feishu document management tools including block creation, content updates, and advanced features.


### 👤 <a name="customer-data-platforms"></a>Customer Data Platforms

Provides access to customer profiles inside of customer data platforms

- [antv/mcp-server-chart](https://github.com/antvis/mcp-server-chart) 🎖️ 📇 ☁️ - A Model Context Protocol server for generating visual charts using [AntV](https://github.com/antvis).
- [hustcc/mcp-echarts](https://github.com/hustcc/mcp-echarts) 📇 🏠 - Generate visual charts using [Apache ECharts](https://echarts.apache.org) with AI MCP dynamically.
- [hustcc/mcp-mermaid](https://github.com/hustcc/mcp-mermaid) 📇 🏠 - Generate [mermaid](https://mermaid.js.org/) diagram and chart with AI MCP dynamically.
- [iaptic/mcp-server-iaptic](https://github.com/iaptic/mcp-server-iaptic) 🎖️ 📇 ☁️ - Connect with [iaptic](https://www.iaptic.com) to ask about your Customer Purchases, Transaction data and App Revenue statistics.
- [OpenDataMCP/OpenDataMCP](https://github.com/OpenDataMCP/OpenDataMCP) 🐍 ☁️ - Connect any Open Data to any LLM with Model Context Protocol.
- [QuackbackIO/quackback](https://github.com/QuackbackIO/quackback) 📇 ☁️ - Open-source customer feedback platform with built-in MCP server. Agents can search feedback, triage posts, update statuses, create and comment on posts, vote, manage roadmaps, merge duplicates, and publish changelogs.
- [sergehuber/inoyu-mcp-unomi-server](https://github.com/sergehuber/inoyu-mcp-unomi-server) 📇 ☁️ - An MCP server to access and updates profiles on an Apache Unomi CDP server.
- [tinybirdco/mcp-tinybird](https://github.com/tinybirdco/mcp-tinybird) 🐍 ☁️ - An MCP server to interact with a Tinybird Workspace from any MCP client.
- [saurabhsharma2u/search-console-mcp](https://github.com/saurabhsharma2u/search-console-mcp)  - An MCP server to interact with Google Search Console and Bing Webmasters.

### 🗄️ <a name="databases"></a>Databases

Secure database access with schema inspection capabilities. Enables querying and analyzing data with configurable security controls including read-only access.

- [Aiven-Open/mcp-aiven](https://github.com/Aiven-Open/mcp-aiven) - 🐍 ☁️ 🎖️ -  Navigate your [Aiven projects](https://go.aiven.io/mcp-server) and interact with the PostgreSQL®, Apache Kafka®, ClickHouse® and OpenSearch® services
- [alexanderzuev/supabase-mcp-server](https://github.com/alexander-zuev/supabase-mcp-server) - Supabase MCP Server with support for SQL query execution and database exploration tools
- [aliyun/alibabacloud-tablestore-mcp-server](https://github.com/aliyun/alibabacloud-tablestore-mcp-server) ☕ 🐍 ☁️ - MCP service for Tablestore, features include adding documents, semantic search for documents based on vectors and scalars, RAG-friendly, and serverless.
- [amineelkouhen/mcp-cockroachdb](https://github.com/amineelkouhen/mcp-cockroachdb) 🐍 ☁️ - A Model Context Protocol server for managing, monitoring, and querying data in [CockroachDB](https://cockroachlabs.com).
- [benborla29/mcp-server-mysql](https://github.com/benborla/mcp-server-mysql) ☁️ 🏠 - MySQL database integration in NodeJS with configurable access controls and schema inspection
- [bram2w/baserow](https://github.com/bram2w/baserow) - Baserow database integration with table search, list, and row create, read, update, and delete capabilities.
- [c4pt0r/mcp-server-tidb](https://github.com/c4pt0r/mcp-server-tidb) 🐍 ☁️ - TiDB database integration with schema inspection and query capabilities
- [Canner/wren-engine](https://github.com/Canner/wren-engine) 🐍 🦀 🏠 - The Semantic Engine for Model Context Protocol(MCP) Clients and AI Agents
- [centralmind/gateway](https://github.com/centralmind/gateway) 🏎️ 🏠 🍎 🪟 - MCP and MCP SSE Server that automatically generate API based on database schema and data. Supports PostgreSQL, Clickhouse, MySQL, Snowflake, BigQuery, Supabase
- [ChristianHinge/dicom-mcp](https://github.com/ChristianHinge/dicom-mcp) 🐍 ☁️ 🏠 - DICOM integration to query, read, and move medical images and reports from PACS and other DICOM compliant systems.
- [chroma-core/chroma-mcp](https://github.com/chroma-core/chroma-mcp) 🎖️ 🐍 ☁️ 🏠 - Chroma MCP server to access local and cloud Chroma instances for retrieval capabilities
- [ClickHouse/mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse) 🐍 ☁️ - ClickHouse database integration with schema inspection and query capabilities
- [confluentinc/mcp-confluent](https://github.com/confluentinc/mcp-confluent) 🐍 ☁️ - Confluent integration to interact with Confluent Kafka and Confluent Cloud REST APIs.
- [Couchbase-Ecosystem/mcp-server-couchbase](https://github.com/Couchbase-Ecosystem/mcp-server-couchbase) 🎖️ 🐍 ☁️ 🏠 - Couchbase MCP server provides unfied access to both Capella cloud and self-managed clusters for document operations, SQL++ queries and natural language data analysis.
- [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) 🐍 🏠 - MCP Server implementation that provides Elasticsearch interaction
- [crystaldba/postgres-mcp](https://github.com/crystaldba/postgres-mcp) 🐍 🏠 - All-in-one MCP server for Postgres development and operations, with tools for performance analysis, tuning, and health checks
- [Dataring-engineering/mcp-server-trino](https://github.com/Dataring-engineering/mcp-server-trino) 🐍 ☁️ - Trino MCP Server to query and access data from Trino Clusters.
- [davewind/mysql-mcp-server](https://github.com/dave-wind/mysql-mcp-server) 🏎️ 🏠 A – user-friendly read-only mysql mcp server for cursor and n8n...
- [designcomputer/mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server) 🐍 🏠 - MySQL database integration with configurable access controls, schema inspection, and comprehensive security guidelines
- [domdomegg/airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server) 📇 🏠 - Airtable database integration with schema inspection, read and write capabilities
- [edwinbernadus/nocodb-mcp-server](https://github.com/edwinbernadus/nocodb-mcp-server) 📇 ☁️ - Nocodb database integration, read and write capabilities
- [ergut/mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server) 📇 ☁️ - Server implementation for Google BigQuery integration that enables direct BigQuery database access and querying capabilities
- [f4ww4z/mcp-mysql-server](https://github.com/f4ww4z/mcp-mysql-server) 📇 🏠 - Node.js-based MySQL database integration that provides secure MySQL database operations
- [ferrants/memvid-mcp-server](https://github.com/ferrants/memvid-mcp-server) 🐍 🏠 - Python Streamable HTTP Server you can run locally to interact with [memvid](https://github.com/Olow304/memvid) storage and semantic search.
- [fireproof-storage/mcp-database-server](https://github.com/fireproof-storage/mcp-database-server) 📇 ☁️ - Fireproof ledger database with multi-user sync
- [freema/mcp-gsheets](https://github.com/freema/mcp-gsheets) 📇 ☁️ - MCP server for Google Sheets API integration with comprehensive reading, writing, formatting, and sheet management capabilities.
- [FreePeak/db-mcp-server](https://github.com/FreePeak/db-mcp-server) 🏎️ 🏠 – A high-performance multi-database MCP server built with Golang, supporting MySQL & PostgreSQL (NoSQL coming soon). Includes built-in tools for query execution, transaction management, schema exploration, query building, and performance analysis, with seamless Cursor integration for enhanced database workflows.
- [furey/mongodb-lens](https://github.com/furey/mongodb-lens) 📇 🏠 - MongoDB Lens: Full Featured MCP Server for MongoDB Databases
- [gannonh/firebase-mcp](https://github.com/gannonh/firebase-mcp) 🔥 ⛅️ - Firebase services including Auth, Firestore and Storage.
- [get-convex/convex-backend](https://stack.convex.dev/convex-mcp-server) 📇 ☁️ - Convex database integration to introspect tables, functions, and run oneoff queries ([Source](https://github.com/get-convex/convex-backend/blob/main/npm-packages/convex/src/cli/mcp.ts))
- [gigamori/mcp-run-sql-connectorx](https://github.com/gigamori/mcp-run-sql-connectorx) 🐍 ☁️ 🏠 🍎 🪟 🐧 - An MCP server that executes SQL via ConnectorX and streams the result to a CSV or Parquet file. Supports PostgreSQL, MariaDB, BigQuery, RedShift, MS SQL Server, etc.
- [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox) 🏎️ ☁️ - Open source MCP server specializing in easy, fast, and secure tools for Databases.
- [GreptimeTeam/greptimedb-mcp-server](https://github.com/GreptimeTeam/greptimedb-mcp-server) 🐍 🏠 - MCP Server for querying GreptimeDB.
- [hannesrudolph/sqlite-explorer-fastmcp-mcp-server](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server) 🐍 🏠 - An MCP server that provides safe, read-only access to SQLite databases through Model Context Protocol (MCP). This server is built with the FastMCP framework, which enables LLMs to explore and query SQLite databases with built-in safety features and query validation.
- [henilcalagiya/google-sheets-mcp](https://github.com/henilcalagiya/google-sheets-mcp) 🐍 🏠 - Your AI Assistant's Gateway to Google Sheets! 25 powerful tools for seamless Google Sheets automation via MCP.
- [hydrolix/mcp-hydrolix](https://github.com/hydrolix/mcp-hydrolix) 🎖️ 🐍 ☁️ - Hydrolix time-series datalake integration providing schema exploration and query capabilities to LLM-based workflows.
- [idoru/influxdb-mcp-server](https://github.com/idoru/influxdb-mcp-server) 📇 ☁️ 🏠 - Run queries against InfluxDB OSS API v2.
- [InfluxData/influxdb3_mcp_server](https://github.com/influxdata/influxdb3_mcp_server) 🎖️ 📇 🏠 ☁️ - Official MCP server for InfluxDB 3 Core/Enterprise/Cloud Dedicated
- [isaacwasserman/mcp-snowflake-server](https://github.com/isaacwasserman/mcp-snowflake-server) 🐍 ☁️ - Snowflake integration implementing read and (optional) write operations as well as insight tracking
- [iunera/druid-mcp-server](https://github.com/iunera/druid-mcp-server) ☕ ☁️ 🏠 - Comprehensive MCP server for Apache Druid that provides extensive tools, resources, and prompts for managing and analyzing Druid clusters.
- [JaviMaligno/postgres_mcp](https://github.com/JaviMaligno/postgres_mcp) 🐍 🏠 - PostgreSQL MCP server with 14 tools for querying, schema exploration, and table analysis. Features security-first design with SQL injection prevention and read-only by default.
- [JaviMaligno/postgres_mcp](https://github.com/JaviMaligno/postgres_mcp) 🐍 🏠 - PostgreSQL MCP server with 14 tools for querying, schema exploration, and table analysis. Features security-first design with SQL injection prevention and read-only by default.
- [joshuarileydev/supabase-mcp-server](https://github.com/joshuarileydev/supabase) - Supabase MCP Server for managing and creating projects and organisations in Supabase
- [jovezhong/mcp-timeplus](https://github.com/jovezhong/mcp-timeplus) 🐍 ☁️ - MCP server for Apache Kafka and Timeplus. Able to list Kafka topics, poll Kafka messages, save Kafka data locally and query streaming data with SQL via Timeplus
- [jparkerweb/mcp-sqlite](https://github.com/jparkerweb/mcp-sqlite) 📇 🏠 - Model Context Protocol (MCP) server that provides comprehensive SQLite database interaction capabilities.
- [KashiwaByte/vikingdb-mcp-server](https://github.com/KashiwaByte/vikingdb-mcp-server) 🐍 ☁️ - VikingDB integration with collection and index introduction, vector store and search capabilities.
- [kiliczsh/mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server) 📇 🏠 - A Model Context Protocol Server for MongoDB
- [ktanaka101/mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb) 🐍 🏠 - DuckDB database integration with schema inspection and query capabilities
- [LucasHild/mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery) 🐍 ☁️ - BigQuery database integration with schema inspection and query capabilities
- [memgraph/mcp-memgraph](https://github.com/memgraph/ai-toolkit/tree/main/integrations/mcp-memgraph) 🐍 🏠 - Memgraph MCP Server - includes a tool to run a query against Memgraph and a schema resource.
- [mbentham/SqlAugur](https://github.com/mbentham/SqlAugur) #️⃣ 🏠 🪟 🐧 - SQL Server MCP server with AST-based query validation, read-only safety, schema exploration, ER diagram generation, and DBA toolkit integration (First Responder Kit, DarlingData, sp_WhoIsActive).
- [modelcontextprotocol/server-postgres](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/postgres) 📇 🏠 - PostgreSQL database integration with schema inspection and query capabilities
- [modelcontextprotocol/server-sqlite](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/sqlite) 🐍 🏠 - SQLite database operations with built-in analysis features
- [montumodi/mongodb-atlas-mcp-server](https://github.com/montumodi/mongodb-atlas-mcp-server) 📇 ☁️ 🪟 🍎 🐧 - A Model Context Protocol (MCP) that provides access to the MongoDB Atlas API. This server wraps the `mongodb-atlas-api-client` package to expose MongoDB Atlas functionality through MCP tools.
- [neo4j-contrib/mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j) 🐍 🏠 - Model Context Protocol with Neo4j (Run queries, Knowledge Graph Memory, Manaage Neo4j Aura Instances)
- [neondatabase/mcp-server-neon](https://github.com/neondatabase/mcp-server-neon) 📇 ☁️ — An MCP Server for creating and managing Postgres databases using Neon Serverless Postgres
- [niledatabase/nile-mcp-server](https://github.com/niledatabase/nile-mcp-server) MCP server for Nile's Postgres platform - Manage and query Postgres databases, tenants, users, auth using LLMs
- [openlink/mcp-server-jdbc](https://github.com/OpenLinkSoftware/mcp-jdbc-server) 🐍 🏠 - An MCP server for generic Database Management System (DBMS) Connectivity via the Java Database Connectivity (JDBC) protocol
- [openlink/mcp-server-odbc](https://github.com/OpenLinkSoftware/mcp-odbc-server) 🐍 🏠 - An MCP server for generic Database Management System (DBMS) Connectivity via the Open Database Connectivity (ODBC) protocol
- [openlink/mcp-server-sqlalchemy](https://github.com/OpenLinkSoftware/mcp-sqlalchemy-server) 🐍 🏠 - An MCP server for generic Database Management System (DBMS) Connectivity via SQLAlchemy using Python ODBC (pyodbc)
- [pab1it0/adx-mcp-server](https://github.com/pab1it0/adx-mcp-server) 🐍 ☁️ - Query and analyze Azure Data Explorer databases
- [pab1it0/prometheus-mcp-server](https://github.com/pab1it0/prometheus-mcp-server) 🐍 ☁️ -  Query and analyze Prometheus, open-source monitoring system.
- [pgtuner_mcp](https://github.com/isdaniel/pgtuner_mcp) 🐍🗄️ - provides AI-powered PostgreSQL performance tuning capabilities.
- [pilat/mcp-datalink](https://github.com/pilat/mcp-datalink) 📇 🏠 - MCP server for secure database access (PostgreSQL, MySQL, SQLite) with parameterized queries and schema inspection
- [planetscale/mcp](https://github.com/planetscale/cli?tab=readme-ov-file#mcp-server-integration) - The PlanetScale CLI includes an MCP server that provides AI tools direct access to your PlanetScale databases.
- [prisma/mcp](https://github.com/prisma/mcp) 📇 ☁️ 🏠 - Gives LLMs the ability to manage Prisma Postgres databases (e.g. spin up new databases and run migrations or queries).
- [qdrant/mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant) 🐍 🏠 - A Qdrant MCP server
- [QuantGeekDev/mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp) 📇 🏠 - MongoDB integration that enables LLMs to interact directly with databases.
- [quarkiverse/mcp-server-jdbc](https://github.com/quarkiverse/quarkus-mcp-servers/tree/main/jdbc) ☕ 🏠 - Connect to any JDBC-compatible database and query, insert, update, delete, and more.
- [rashidazarang/airtable-mcp](https://github.com/rashidazarang/airtable-mcp) 🐍 ☁️ - Connect AI tools directly to Airtable. Query, create, update, and delete records using natural language. Features include base management, table operations, schema manipulation, record filtering, and data migration through a standardized MCP interface.
- [redis/mcp-redis](https://github.com/redis/mcp-redis) 🐍 🏠 - The Redis official MCP Server offers an interface to manage and search data in Redis.
- [runekaagaard/mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy) 🐍 🏠 - Universal SQLAlchemy-based database integration supporting PostgreSQL, MySQL, MariaDB, SQLite, Oracle, MS SQL Server and many more databases. Features schema and relationship inspection, and large dataset analysis capabilities.
- [s2-streamstore/s2-sdk-typescript](https://github.com/s2-streamstore/s2-sdk-typescript) 🎖️ 📇 ☁️ - Official MCP server for the S2.dev serverless stream platform.
- [schemacrawler/SchemaCrawler-MCP-Server-Usage](https://github.com/schemacrawler/SchemaCrawler-MCP-Server-Usage) 🎖️ ☕ – Connect to any relational database, and be able to get valid SQL, and ask questions like what does a certain column prefix mean.
- [SidneyBissoli/ibge-br-mcp](https://github.com/SidneyBissoli/ibge-br-mcp) 📇 ☁️ - Brazilian Census Bureau (IBGE) data server with 23 tools for demographics, geography, economics, and statistics. Covers localities, SIDRA tables, Census data, population projections, and geographic meshes.
- [sirmews/mcp-pinecone](https://github.com/sirmews/mcp-pinecone) 🐍 ☁️ - Pinecone integration with vector search capabilities
- [skysqlinc/skysql-mcp](https://github.com/skysqlinc/skysql-mcp) 🎖️ ☁️ - Serverless MariaDB Cloud DB MCP server. Tools to launch, delete, execute SQL and work with DB level AI agents for accurate text-2-sql and conversations.
- [Snowflake-Labs/mcp](https://github.com/Snowflake-Labs/mcp) 🐍 ☁️ - Open-source MCP server for Snowflake from official Snowflake-Labs supports prompting Cortex Agents, querying structured & unstructured data, object management, SQL execution, semantic view querying, and more. RBAC, fine-grained CRUD controls, and all authentication methods supported.
- [subnetmarco/pgmcp](https://github.com/subnetmarco/pgmcp) 🏎️ 🏠 - Natural language PostgreSQL queries with automatic streaming, read-only safety, and universal database compatibility.
- [supabase-community/supabase-mcp](https://github.com/supabase-community/supabase-mcp) 🎖️ 📇 ☁️ - Official Supabase MCP server to connect AI assistants directly with your Supabase project and allows them to perform tasks like managing tables, fetching config, and querying data.
- [TheRaLabs/legion-mcp](https://github.com/TheRaLabs/legion-mcp) 🐍 🏠 Universal database MCP server supporting multiple database types including PostgreSQL, Redshift, CockroachDB, MySQL, RDS MySQL, Microsoft SQL Server, BigQuery, Oracle DB, and SQLite.
- [tradercjz/dolphindb-mcp-server](https://github.com/tradercjz/dolphindb-mcp-server) 🐍 ☁️ - TDolphinDB database integration with schema inspection and query capabilities
- [tuannvm/mcp-trino](https://github.com/tuannvm/mcp-trino) 🏎️ ☁️ - A Go implementation of a Model Context Protocol (MCP) server for Trino
- [VictoriaMetrics-Community/mcp-victorialogs](https://github.com/VictoriaMetrics-Community/mcp-victorialogs) 🎖️ 🏎️ 🏠 - Provides comprehensive integration with your [VictoriaLogs instance APIs](https://docs.victoriametrics.com/victorialogs/querying/#http-api) and [documentation](https://docs.victoriametrics.com/victorialogs/) for working with logs, investigating and debugging tasks related to your VictoriaLogs instances.
- [weaviate/mcp-server-weaviate](https://github.com/weaviate/mcp-server-weaviate) 🐍 📇 ☁️ - An MCP Server to connect to your Weaviate collections as a knowledge base as well as using Weaviate as a chat memory store.
- [wenb1n-dev/mysql_mcp_server_pro](https://github.com/wenb1n-dev/mysql_mcp_server_pro)  🐍 🏠 - Supports SSE, STDIO; not only limited to MySQL's CRUD functionality; also includes database exception analysis capabilities; controls database permissions based on roles; and makes it easy for developers to extend tools with customization
- [wenb1n-dev/SmartDB_MCP](https://github.com/wenb1n-dev/SmartDB_MCP)  🐍 🏠 - A universal database MCP server supporting simultaneous connections to multiple databases. It provides tools for database operations, health analysis, SQL optimization, and more. Compatible with mainstream databases including MySQL, PostgreSQL, SQL Server, MariaDB, Dameng, and Oracle. Supports Streamable HTTP, SSE, and STDIO; integrates OAuth 2.0; and is designed for easy customization and extension by developers.
- [wenerme/wener-mssql-mcp](https://github.com/wenerme/wode/tree/develop/packages/wener-mssql-mcp) 📇 🏠 - MSSQL database integration with schema inspection and query capabilities
- [xexr/mcp-libsql](https://github.com/Xexr/mcp-libsql) 📇 🏠 ☁️ - Production-ready MCP server for libSQL databases with comprehensive security and management tools.
- [XGenerationLab/xiyan_mcp_server](https://github.com/XGenerationLab/xiyan_mcp_server) 📇 ☁️ — An MCP server that supports fetching data from a database using natural language queries, powered by XiyanSQL as the text-to-SQL LLM.
- [xing5/mcp-google-sheets](https://github.com/xing5/mcp-google-sheets) 🐍 ☁️ - A Model Context Protocol server for interacting with Google Sheets. This server provides tools to create, read, update, and manage spreadsheets through the Google Sheets API.
- [yannbrrd/simple_snowflake_mcp](https://github.com/YannBrrd/simple_snowflake_mcp) 🐍 ☁️ - Simple Snowflake MCP server that works behind a corporate proxy. Read and write (optional) operations
- [ydb/ydb-mcp](https://github.com/ydb-platform/ydb-mcp) 🎖️ 🐍 ☁️ - MCP server for interacting with [YDB](https://ydb.tech) databases
- [yincongcyincong/VictoriaMetrics-mcp-server](https://github.com/yincongcyincong/VictoriaMetrics-mcp-server) 🐍 🏠 - An MCP server for interacting with VictoriaMetrics database.
- [Zhwt/go-mcp-mysql](https://github.com/Zhwt/go-mcp-mysql) 🏎️ 🏠 – Easy to use, zero dependency MySQL MCP server built with Golang with configurable readonly mode and schema inspection.
- [zilliztech/mcp-server-milvus](https://github.com/zilliztech/mcp-server-milvus) 🐍 🏠 ☁️ - MCP Server for Milvus / Zilliz, making it possible to interact with your database.

### 📊 <a name="data-platforms"></a>Data Platforms

Data Platforms for data integration, transformation and pipeline orchestration.

- [alkemiai/alkemi-mcp](https://github.com/alkemi-ai/alkemi-mcp) 📇 ☁️ - MCP Server for natural language querying of Snowflake, Google BigQuery, and DataBricks Data Products through Alkemi.ai.
- [avisangle/method-crm-mcp](https://github.com/avisangle/method-crm-mcp) 🐍 ☁️ 🏠 🍎 🪟 🐧 - Production-ready MCP server for Method CRM API integration with 20 comprehensive tools for tables, files, users, events, and API key management. Features rate limiting, retry logic, and dual transport support (stdio/HTTP).
- [aywengo/kafka-schema-reg-mcp](https://github.com/aywengo/kafka-schema-reg-mcp) 🐍 ☁️ 🏠 🍎 🪟 🐧 - Comprehensive Kafka Schema Registry MCP server with 48 tools for multi-registry management, schema migration, and enterprise features.
- [bruno-portfolio/agrobr-mcp](https://github.com/bruno-portfolio/agrobr-mcp) 🐍 ☁️ - Brazilian agricultural data for LLMs — prices, crop estimates, climate, deforestation from 19 public sources via CEPEA, CONAB, IBGE, INPE and B3.
- [dbt-labs/dbt-mcp](https://github.com/dbt-labs/dbt-mcp) 🎖️ 🐍 🏠 ☁️ - Official MCP server for [dbt (data build tool)](https://www.getdbt.com/product/what-is-dbt) providing integration with dbt Core/Cloud CLI, project metadata discovery, model information, and semantic layer querying capabilities.
- [flowcore/mcp-flowcore-platform](https://github.com/flowcore-io/mcp-flowcore-platform) 🎖️ 📇 ☁️ 🏠 - Interact with Flowcore to perform actions, ingest data, and analyse, cross reference and utilise any data in your data cores, or in public data cores; all with human language.
- [JordiNei/mcp-databricks-server](https://github.com/JordiNeil/mcp-databricks-server) 🐍 ☁️ - Connect to Databricks API, allowing LLMs to run SQL queries, list jobs, and get job status.
- [jwaxman19/qlik-mcp](https://github.com/jwaxman19/qlik-mcp) 📇 ☁️ - MCP Server for Qlik Cloud API that enables querying applications, sheets, and extracting data from visualizations with comprehensive authentication and rate limiting support.
- [keboola/keboola-mcp-server](https://github.com/keboola/keboola-mcp-server) 🐍 - interact with Keboola Connection Data Platform. This server provides tools for listing and accessing data from Keboola Storage API.
- [mattijsdp/dbt-docs-mcp](https://github.com/mattijsdp/dbt-docs-mcp) 🐍 🏠 - MCP server for dbt-core (OSS) users as the official dbt MCP only supports dbt Cloud. Supports project metadata, model and column-level lineage and dbt documentation.
- [meal-inc/bonnard-cli](https://github.com/meal-inc/bonnard-cli) 📇 ☁️ - Ultra-fast to deploy agentic-first MCP-ready semantic layer. Let your data be like water.
- [Osseni94/keyneg-mcp](https://github.com/Osseni94/keyneg-mcp) 🐍 🏠 - Enterprise-grade sentiment analysis with 95+ labels, keyword extraction, and batch processing for AI agents
- [Osseni94/oyemi-mcp](https://github.com/Osseni94/oyemi-mcp) 🐍 🏠 - Deterministic semantic word encoding and valence/sentiment analysis using 145K+ word lexicon. Provides word-to-code mapping, semantic similarity, synonym/antonym lookup with zero runtime NLP dependencies.
- [paracetamol951/caisse-enregistreuse-mcp-server](https://github.com/paracetamol951/caisse-enregistreuse-mcp-server) 🏠 🐧 🍎 ☁️ - Allows you to automate or monitor business operations, sales recorder, POS software, CRM.
- [saikiyusuke/registep-mcp](https://github.com/saikiyusuke/registep-mcp) 📇 ☁️ - AI-powered POS & sales analytics MCP server with 67 tools for Airレジ, スマレジ, and BASE EC integration. Provides store management, sales data querying, AI chat analysis, and weather correlation features.
- [yashshingvi/databricks-genie-MCP](https://github.com/yashshingvi/databricks-genie-MCP) 🐍 ☁️ - A server that connects to the Databricks Genie API, allowing LLMs to ask natural language questions, run SQL queries, and interact with Databricks conversational agents.


### 💻 <a name="developer-tools"></a>Developer Tools

Tools and integrations that enhance the development workflow and environment management.

- [21st-dev/Magic-MCP](https://github.com/21st-dev/magic-mcp) - Create crafted UI components inspired by the best 21st.dev design engineers.
- [a-25/ios-mcp-code-quality-server](https://github.com/a-25/ios-mcp-code-quality-server) 📇 🏠 🍎 - iOS code quality analysis and test automation server. Provides comprehensive Xcode test execution, SwiftLint integration, and detailed failure analysis. Operates in both CLI and MCP server modes for direct developer usage and AI assistant integration.
- [AaronVick/ECHO_RIFT_MCP](https://github.com/AaronVick/ECHO_RIFT_MCP) 📇 ☁️ - MCP server for EchoRift infrastructure primitives (BlockWire, CronSynth, Switchboard, Arbiter). Makes EchoRift's agent infrastructure callable as MCP tools so any MCP client can treat EchoRift like a native capability layer.
- [aashari/mcp-server-atlassian-bitbucket](https://github.com/aashari/mcp-server-atlassian-bitbucket) 📇 ☁️ - Atlassian Bitbucket Cloud integration. Enables AI systems to interact with repositories, pull requests, workspaces, and code in real time.
- [aashari/mcp-server-atlassian-confluence](https://github.com/aashari/mcp-server-atlassian-confluence) 📇 ☁️ - Atlassian Confluence Cloud integration. Enables AI systems to interact with Confluence spaces, pages, and content with automatic ADF to Markdown conversion.
- [aashari/mcp-server-atlassian-jira](https://github.com/aashari/mcp-server-atlassian-jira) 📇 ☁️ - Atlassian Jira Cloud integration. Enables AI systems to interact with Jira projects, issues, comments, and related development information in real time.
- [abrinsmead/mindpilot-mcp](https://github.com/abrinsmead/mindpilot-mcp) 📇 🏠 - Visualizes code, architecture and other concepts as mermaid diagrams in a locally hosted web app. Just ask your agent to "show me this in a diagram".
- [admica/FileScopeMCP](https://github.com/admica/FileScopeMCP) 🐍 📇 🦀 - Analyzes your codebase identifying important files based on dependency relationships. Generates diagrams and importance scores, helping AI assistants understand the codebase.
- [agent-hanju/char-index-mcp](https://github.com/agent-hanju/char-index-mcp) 🐍 🏠 ☁️ 🍎 🪟 🐧 - Precise character-level string indexing for LLMs. Provides tools for finding, extracting, and manipulating text by exact character position to solve position-based operations.
- [akramIOT/MCP_AI_SOC_Sher](https://github.com/akramIOT/MCP_AI_SOC_Sher)  🐍 ☁️ 📇 - MCP Server to do dynamic AI SOC Security Threat analysis for a  Text2SQL  AI Agent.
- [aktsmm/skill-ninja-mcp-server](https://github.com/aktsmm/skill-ninja-mcp-server) 📇 🏠 🍎 🪟 🐧 - Agent Skill Ninja for MCP: Search, install, and manage AI agent skills (SKILL.md files) from GitHub repositories. Features workspace analysis for personalized recommendations and supports 140+ pre-indexed skills.
- [alimo7amed93/webhook-tester-mcp](https://github.com/alimo7amed93/webhook-tester-mcp)  🐍 ☁️ – A FastMCP-based server for interacting with webhook-test.com. Enables users to create, retrieve, and delete webhooks locally using Claude.
- [ambar/simctl-mcp](https://github.com/ambar/simctl-mcp) 📇 🏠 🍎 A MCP server implementation for iOS Simulator control.
- [api7/apisix-mcp](https://github.com/api7/apisix-mcp) 🎖️ 📇 🏠 MCP Server that support for querying and managing all resource in [Apache APISIX](https://github.com/apache/apisix).
- [ArchAI-Labs/fastmcp-sonarqube-metrics](https://github.com/ArchAI-Labs/fastmcp-sonarqube-metrics) 🐍 🏠 🪟 🐧 🍎 -  A Model Context Protocol (MCP) server that provides a set of tools for retrieving information about SonarQube projects like metrics (actual and historical), issues, health status.
- [artmann/package-registry-mcp](https://github.com/artmann/package-registry-mcp) 🏠 📇 🍎 🪟 🐧 - MCP server for searching and getting up-to-date information about NPM, Cargo, PyPi, and NuGet packages.
- [arvindand/maven-tools-mcp](https://github.com/arvindand/maven-tools-mcp) ☕ ☁️ 🏠 🍎 🪟 🐧 - Universal Maven Central dependency intelligence for JVM build tools (Maven, Gradle, SBT, Mill). Features bulk operations, version comparison, stability filtering, dependency age analysis, release patterns, and Context7 integration for upgrade guidance.
- [augmnt/augments-mcp-server](https://github.com/augmnt/augments-mcp-server) 📇 ☁️ 🏠 - Transform Claude Code with intelligent, real-time access to 90+ framework documentation sources. Get accurate, up-to-date code generation that follows current best practices for React, Next.js, Laravel, FastAPI, Tailwind CSS, and more.
- [automation-ai-labs/mcp-link](https://github.com/automation-ai-labs/mcp-link) 🏎️ 🏠 - Seamlessly Integrate Any API with AI Agents (with OpenAPI Schema)
- [avisangle/jenkins-mcp-server](https://github.com/avisangle/jenkins-mcp-server) 🐍 🏠 🍎 🪟 🐧 - Enterprise-grade Jenkins CI/CD integration with multi-tier caching, pipeline monitoring, artifact management, and batch operations. Features 21 MCP tools for job management, build status tracking, and queue management with CSRF protection and 2FA support.
- [axliupore/mcp-code-runner](https://github.com/axliupore/mcp-code-runner) 📇 🏠 - An MCP server for running code locally via Docker and supporting multiple programming languages.
- [azer/react-analyzer-mcp](https://github.com/azer/react-analyzer-mcp) 📇 🏠 - Analyze React code locally, generate docs / llm.txt for whole project at once
- [back1ply/agent-skill-loader](https://github.com/back1ply/agent-skill-loader) 📇 🏠 - Dynamically load Claude Code skills into AI agents without copying files. Discover, read, and install skills on demand.
- [bbonnin/openapi-to-mcp](https://github.com/bbonnin/openapi-to-mcp) ☕ 🏠 🍎 🪟 🐧 - MCP server that automatically converts any OpenAPI/Swagger specification into a set of usable MCP tools. Unlike manual tool definition, this approach auto-generates tools directly from the Swagger spec, ensuring consistency, reducing maintenance effort, and preventing mismatches between the tools and the actual API.
- [bgauryy/octocode-mcp](https://github.com/bgauryy/octocode-mcp) ☁️ 📇 🍎 🪟 🐧 - AI-powered developer assistant that enables advanced research, analysis and discovery across GitHub and NPM realms in realtime.
- [bitrise-io/bitrise-mcp](https://github.com/bitrise-io/bitrise-mcp) 🎖️ 🐍 ☁️ 🍎 🪟 🐧 - MCP Server for the [Bitrise](https://bitrise.io) API, enabling app management, build operations, artifact management and more.
- [BrainGrid MCP](https://docs.braingrid.ai/mcp-server/installation) 🎖️☁️ - [BrainGrid](https://braingrid.ai) MCP is the Product Management Agent that writes your specs, plans your features, and creates engineering-grade tasks your coding tools can build reliably.
- [BrunoKrugel/echo-mcp](https://github.com/BrunoKrugel/echo-mcp) 🏎️ ☁️ 📟 🪟 🐧 🍎 - A zero-configuration Go library to automatically expose any existing Echo web framework APIs as MCP tools.
- [buildkite/buildkite-mcp-server](https://github.com/buildkite/buildkite-mcp-server) 🎖️ 🏎️ 🏠 ☁️ 🍎 🪟 🐧 - Official MCP server for Buildkite. Create new pipelines, diagnose and fix failures, trigger builds, monitor job queues, and more.
- [Chunkydotdev/bldbl-mcp](https://github.com/chunkydotdev/bldbl-mcp) 📇 ☁️ 🍎 🪟 🐧 - Official MCP server for Buildable AI-powered development platform [bldbl.dev](https://bldbl.dev). Enables AI assistants to manage tasks, track progress, get project context, and collaborate with humans on software projects.
- [CircleCI/mcp-server-circleci](https://github.com/CircleCI-Public/mcp-server-circleci) 📇 ☁️ Enable AI Agents to fix build failures from CircleCI.
- [cjo4m06/mcp-shrimp-task-manager](https://github.com/cjo4m06/mcp-shrimp-task-manager) 📇 ☁️ 🏠 – A programming-focused task management system that boosts coding agents like Cursor AI with advanced task memory, self-reflection, and dependency management. [ShrimpTaskManager](https://cjo4m06.github.io/mcp-shrimp-task-manager)
- [ckanthony/gin-mcp](https://github.com/ckanthony/gin-mcp) 🏎️ ☁️ 📟 🪟 🐧 🍎 - A zero-configuration Go library to automatically expose existing Gin web framework APIs as MCP tools.
- [ckreiling/mcp-server-docker](https://github.com/ckreiling/mcp-server-docker) 🐍 🏠 - Integrate with Docker to manage containers, images, volumes, and networks.
- [ClaudeCodeNavi/claudecodenavi-mcp](https://github.com/saikiyusuke/claudecodenavi-mcp) 📇 ☁️ - Claude Code knowledge platform & marketplace MCP server. Search and share snippets, prompts, Q&A solutions, error fixes, and MCP server configurations from the ClaudeCodeNavi community.
- [CodeLogicIncEngineering/codelogic-mcp-server](https://github.com/CodeLogicIncEngineering/codelogic-mcp-server) 🎖️ 🐍 ☁️ 🍎 🪟 🐧 - Official MCP server for CodeLogic, providing access to code dependency analytics, architectural risk analysis, and impact assessment tools.
- [Comet-ML/Opik-MCP](https://github.com/comet-ml/opik-mcp) 🎖️ 📇 ☁️ 🏠 - Use natural language to explore LLM observability, traces, and monitoring data captured by Opik.
- [conan-io/conan-mcp](https://github.com/conan-io/conan-mcp) 🎖️ 🐍 🏠 🍎 🪟 🐧 - Official MCP server for Conan C/C++ package manager. Create projects, manage dependencies, check licenses, and scan for security vulnerabilities.
- [ConfigCat/mcp-server](https://github.com/configcat/mcp-server) 🎖️ 📇 ☁️ - MCP server for interacting with ConfigCat feature flag platform. Supports managing feature flags, configs, environments, products and organizations.
- [context-rot-detection](https://github.com/milos-product-maker/context-rot-detection) 📇 🏠 - Gives AI agents self-awareness about their cognitive state. Monitors token utilization, context quality degradation, and session fatigue. Returns health scores (0-100) and recovery recommendations based on model-specific degradation curves.
- [cqfn/aibolit-mcp-server](https://github.com/cqfn/aibolit-mcp-server) ☕ - Helping Your AI Agent Identify Hotspots for Refactoring; Help AI Understand How to 'Make Code Better'
- [currents-dev/currents-mcp](https://github.com/currents-dev/currents-mcp) 🎖️ 📇 ☁️ Enable AI Agents to fix Playwright test failures reported to [Currents](https://currents.dev).
- [Daghis/teamcity-mcp](https://github.com/Daghis/teamcity-mcp) 📇 ☁️ 🍎 🪟 🐧 - MCP server for JetBrains TeamCity with 87 tools for builds, tests, agents, and CI/CD pipeline management. Features dual-mode operation (dev/full) and runtime mode switching.
- [dannote/figma-use](https://github.com/dannote/figma-use) 📇 🏠 - Full Figma control: create shapes, text, components, set styles, auto-layout, variables, export. 80+ tools.
- [davidan90/time-node-mcp](https://github.com/davidan90/time-node-mcp) 📇 🏠 - Timezone-aware date and time operations with support for IANA timezones, timezone conversion, and Daylight Saving Time handling.
- [davidlin2k/pox-mcp-server](https://github.com/davidlin2k/pox-mcp-server) 🐍 🏠 - MCP server for the POX SDN controller to provides network control and management capabilities.
- [delano/postman-mcp-server](https://github.com/delano/postman-mcp-server) 📇 ☁️ - Interact with [Postman API](https://www.postman.com/postman/postman-public-workspace/)
- [deploy-mcp/deploy-mcp](https://github.com/alexpota/deploy-mcp) 📇 ☁️ 🏠 - Universal deployment tracker for AI assistants with live status badges and deployment monitoring
- [docker/hub-mcp](https://github.com/docker/hub-mcp) 🎖️ 📇 ☁️ 🏠 - Official MCP server to interact with Docker Hub, providing access to repositories, hub search and Docker Hardened Images
- [dorukardahan/twitterapi-docs-mcp](https://github.com/dorukardahan/twitterapi-docs-mcp) 📇 🏠 - Offline access to TwitterAPI.io documentation for AI assistants. 52 API endpoints, guides, pricing info, and authentication docs.
- [efremidze/swift-patterns-mcp](https://github.com/efremidze/swift-patterns-mcp) 📇 🏠 🍎 🪟 🐧 - An MCP server providing curated Swift and SwiftUI best practices from leading iOS developers, including patterns and real-world code examples from Swift by Sundell, SwiftLee, and other trusted sources.
- [endorhq/cli](https://github.com/endorhq/cli) 📇 ☁️ 🏠 🪟 🐧 🍎 - Endor lets your AI agents run services like MariaDB, Postgres, Redis, Memcached, Alpine, or Valkey in isolated sandboxes. Get pre-configured applications that boot in less than 5 seconds.
- [ericbrown/project-context-mcp](https://github.com/ericbrown/project-context-mcp) 🐍 🏠 - Exposes `.context/` folder files as MCP resources, giving Claude Code instant access to project documentation via `@` mentions.
- [etsd-tech/mcp-pointer](https://github.com/etsd-tech/mcp-pointer) 📇 🏠 🍎 🪟 🐧 - Visual DOM element selector for agentic coding tools. Chrome extension + MCP server bridge for Claude Code, Cursor, Windsurf etc. Option+Click to capture elements.
- [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) 📇 ☁️ 🏠 - AI-powered task management system for AI-driven development. Features PRD parsing, task expansion, multi-provider support (Claude, OpenAI, Gemini, Perplexity, xAI), and selective tool loading for optimized context usage.
- [flipt-io/mcp-server-flipt](https://github.com/flipt-io/mcp-server-flipt) 📇 🏠 - Enable AI assistants to interact with your feature flags in [Flipt](https://flipt.io).
- [freema/mcp-design-system-extractor](https://github.com/freema/mcp-design-system-extractor) 📇 🏠 - Extracts component information from Storybook design systems. Provides HTML, styles, props, dependencies, theme tokens and component metadata for AI-powered design system analysis.
- [gitkraken/gk-cli](https://github.com/gitkraken/gk-cli) 🎖️ 🏎️ 🏠 ☁️ 🍎 🪟 🐧 - A CLI for interacting with GitKraken APIs. Includes an MCP server via `gk mcp` that not only wraps GitKraken APIs, but also Jira, GitHub, GitLab, and more. Works with local tools and remote services.
- [GLips/Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) 📇 🏠 - Provide coding agents direct access to Figma data to help them one-shot design implementation.
- [gofireflyio/firefly-mcp](https://github.com/gofireflyio/firefly-mcp) 🎖️ 📇 ☁️ - Integrates, discovers, manages, and codifies cloud resources with [Firefly](https://firefly.ai).
- [gorosun/unified-diff-mcp](https://github.com/gorosun/unified-diff-mcp) 📇 🏠 - Generate and visualize unified diff comparisons with beautiful HTML/PNG output, supporting side-by-side and line-by-line views for filesystem dry-run integration
- [Govcraft/rust-docs-mcp-server](https://github.com/Govcraft/rust-docs-mcp-server) 🦀 🏠 - Provides up-to-date documentation context for a specific Rust crate to LLMs via an MCP tool, using semantic search (embeddings) and LLM summarization.
- [HainanZhao/mcp-gitlab-jira](https://github.com/HainanZhao/mcp-gitlab-jira) 📇 ☁️ 🏠 - Unified MCP server for GitLab and Jira: manage projects, merge requests, files, releases and tickets with AI agents.
- [haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server) 🐍 🏠 - An Excel manipulation server providing workbook creation, data operations, formatting, and advanced features (charts, pivot tables, formulae).
- [hechtcarmel/jetbrains-debugger-mcp-plugin](https://github.com/hechtcarmel/jetbrains-debugger-mcp-plugin) ☕ 🏠 - A JetBrains IDE plugin that exposes an MCP server, giving AI coding assistants full programmatic control over the debugger.
- [hechtcarmel/jetbrains-index-mcp-plugin](https://github.com/hechtcarmel/jetbrains-index-mcp-plugin) ☕ 🏠 - A JetBrains IDE plugin that exposes an MCP server, enabling AI coding assistants to leverage the IDE's indexing and refactoring capabilities (rename, safe delete, find references, call hierarchy, type hierarchy, diagnostics and more).
- [higress-group/higress-ops-mcp-server](https://github.com/higress-group/higress-ops-mcp-server) 🐍 🏠 - MCP server that provides comprehensive tools for managing [Higress](https://github.com/alibaba/higress) gateway configurations and operations.
- [hijaz/postmancer](https://github.com/hijaz/postmancer) 📇 🏠 - A MCP server for replacing Rest Clients like Postman/Insomnia, by allowing your LLM to maintain and use api collections.
- [hloiseaufcms/mcp-gopls](https://github.com/hloiseaufcms/mcp-gopls) 🏎️ 🏠 - A MCP server for interacting with [Go's Language Server Protocol (gopls)](https://github.com/golang/tools/tree/master/gopls) and benefit from advanced Go code analysis features.
- [hoklims/stacksfinder-mcp](https://github.com/hoklims/stacksfinder-mcp) 📇 🏠 🍎 🪟 🐧 - Deterministic tech stack recommendations with 6-dimension scoring. Analyze, compare technologies, get optimal stack suggestions for any project type. 10 tools (4 free, 6 Pro).
- [hungthai1401/bruno-mcp](https://github.com/hungthai1401/bruno-mcp) 📇 🏠 - A MCP server for interacting with [Bruno API Client](https://www.usebruno.com/).
- [hyperb1iss/droidmind](https://github.com/hyperb1iss/droidmind) 🐍 🏠 - Control Android devices with AI through MCP, enabling device control, debugging, system analysis, and UI automation with a comprehensive security framework.
- [Hypersequent/qasphere-mcp](https://github.com/Hypersequent/qasphere-mcp) 🎖️ 📇 ☁️ - Integration with [QA Sphere](https://qasphere.com/) test management system, enabling LLMs to discover, summarize, and interact with test cases directly from AI-powered IDEs
- [idosal/git-mcp](https://github.com/idosal/git-mcp) 📇 ☁️ - [gitmcp.io](https://gitmcp.io/) is a generic remote MCP server to connect to ANY [GitHub](https://www.github.com) repository or project for documentation
- [IlyaGulya/gradle-mcp-server](https://github.com/IlyaGulya/gradle-mcp-server) 🏠 - Gradle integration using the Gradle Tooling API to inspect projects, execute tasks, and run tests with per-test result reporting
- [InditexTech/mcp-server-simulator-ios-idb](https://github.com/InditexTech/mcp-server-simulator-ios-idb) 📇 🏠 🍎 - A Model Context Protocol (MCP) server that enables LLMs to interact with iOS simulators (iPhone, iPad, etc.) through natural language commands.
- [InhiblabCore/mcp-image-compression](https://github.com/InhiblabCore/mcp-image-compression) 🐍 🏠 - MCP server for local compression of various image formats.
- [InsForge/insforge-mcp](https://github.com/InsForge/insforge-mcp) 📇 ☁️ - AI-native backend-as-a-service platform enabling AI agents to build and manage full-stack applications. Provides Auth, Database (PostgreSQL), Storage, and Functions as production-grade infrastructure, reducing MVP development time from weeks to hours.
- [Inspizzz/jetbrains-datalore-mcp](https://github.com/inspizzz/jetbrains-datalore-mcp) 🐍 ☁️ - MCP server for interacting with cloud deployments of Jetbrains Datalore platform. Fully incorporated Datalore API ( run, run interactively, get run data, fetch files )
- [ios-simulator-mcp](https://github.com/joshuayoes/ios-simulator-mcp) 📇 🏠 🍎 - A Model Context Protocol (MCP) server for interacting with iOS simulators. This server allows you to interact with iOS simulators by getting information about them, controlling UI interactions, and inspecting UI elements.
- [isaacphi/mcp-language-server](https://github.com/isaacphi/mcp-language-server) 🏎️ 🏠 - MCP Language Server helps MCP enabled clients navigate codebases more easily by giving them access to semantic tools like get definition, references, rename, and diagnostics.
- [IvanAmador/vercel-ai-docs-mcp](https://github.com/IvanAmador/vercel-ai-docs-mcp) 📇 🏠 - A Model Context Protocol (MCP) server that provides AI-powered search and querying capabilities for the Vercel AI SDK documentation.
- [j4c0bs/mcp-server-sql-analyzer](https://github.com/j4c0bs/mcp-server-sql-analyzer) 🐍 - MCP server that provides SQL analysis, linting, and dialect conversion using [SQLGlot](https://github.com/tobymao/sqlglot)
- [JamesANZ/system-prompts-mcp-server](https://github.com/JamesANZ/system-prompts-mcp-server) 📇 🏠 🍎 🪟 🐧 - Exposes a large catalog of coding assistant prompts as MCP tools with model-aware suggestions and persona activation to emulate agents like Cursor or Devin.
- [janreges/ai-distiller-mcp](https://github.com/janreges/ai-distiller) 🏎️ 🏠 - Extracts essential code structure from large codebases into AI-digestible format, helping AI agents write code that correctly uses existing APIs on the first attempt.
- [jasonjmcghee/claude-debugs-for-you](https://github.com/jasonjmcghee/claude-debugs-for-you) 📇 🏠 - An MCP Server and VS Code Extension which enables (language agnostic) automatic debugging via breakpoints and expression evaluation.
- [jaspertvdm/mcp-server-tibet](https://github.com/jaspertvdm/mcp-server-tibet) 🐍 ☁️ 🏠 - TIBET provenance tracking for AI decisions. Cryptographic audit trails with ERIN/ERAAN/EROMHEEN/ERACHTER intent logging for compliance.
- [jetbrains/mcpProxy](https://github.com/JetBrains/mcpProxy) 🎖️ 📇 🏠 - Connect to JetBrains IDE
- [Jktfe/serveMyAPI](https://github.com/Jktfe/serveMyAPI) 📇 🏠 🍎 - A personal MCP (Model Context Protocol) server for securely storing and accessing API keys across projects using the macOS Keychain.
- [jordandalton/restcsv-mcp-server](https://github.com/JordanDalton/RestCsvMcpServer) 📇 ☁️ - An MCP server for CSV files.
- [joshuarileydev/app-store-connect-mcp-server](https://github.com/JoshuaRileyDev/app-store-connect-mcp-server) 📇 🏠 - An MCP server to communicate with the App Store Connect API for iOS Developers
- [joshuarileydev/simulator-mcp-server](https://github.com/JoshuaRileyDev/simulator-mcp-server) 📇 🏠 - An MCP server to control iOS Simulators
- [Jpisnice/shadcn-ui-mcp-server](https://github.com/Jpisnice/shadcn-ui-mcp-server) 📇 🏠 - MCP server that gives AI assistants seamless access to shadcn/ui v4 components, blocks, demos, and metadata.
- [jsdelivr/globalping-mcp-server](https://github.com/jsdelivr/globalping-mcp-server) 🎖️ 📇 ☁️ - The Globalping MCP server provides users and LLMs access to run network tools like ping, traceroute, mtr, HTTP and DNS resolve from thousands of locations around the world.
- [kadykov/mcp-openapi-schema-explorer](https://github.com/kadykov/mcp-openapi-schema-explorer) 📇 ☁️ 🏠 - Token-efficient access to OpenAPI/Swagger specs via MCP Resources.
- [kindly-software/kdb](https://github.com/kindly-software/kdb) 🦀 ☁️ - AI-powered time-travel debugger with bidirectional execution replay, audit-compliant hash-chain logging, and SIMD-accelerated stack unwinding. Free Hobby tier available.
- [LadislavSopko/mcp-ai-server-visual-studio](https://github.com/LadislavSopko/mcp-ai-server-visual-studio) #️⃣ 🏠 🪟 - MCP AI Server for Visual Studio. 20 Roslyn-powered tools giving AI assistants semantic code navigation, symbol search, inheritance trees, call graphs, safe rename, build/test execution. Works with Claude, Codex, Gemini, Cursor, Copilot, Windsurf, Cline.
- [lamemind/mcp-server-multiverse](https://github.com/lamemind/mcp-server-multiverse) 📇 🏠 🛠️ - A middleware server that enables multiple isolated instances of the same MCP servers to coexist independently with unique namespaces and configurations.
- [langfuse/mcp-server-langfuse](https://github.com/langfuse/mcp-server-langfuse) 🐍 🏠 - MCP server to access and manage LLM application prompts created with [Langfuse]([https://langfuse.com/](https://langfuse.com/docs/prompts/get-started)) Prompt Management.
- [linuxsuren/atest-mcp-server](https://github.com/LinuxSuRen/atest-mcp-server) 📇 🏠 🐧 - An MCP server to manage test suites and cases, which is an alternative to Postman.
- [linw1995/nvim-mcp](https://github.com/linw1995/nvim-mcp) 🦀 🏠 🍎 🪟 🐧  -  A MCP server to interact with Neovim
- [louis030195/gptzero-mcp](https://github.com/louis030195/gptzero-mcp) 📇 ☁️ 🍎 🪟 🐧 - AI detection for text content with GPTZero API. Detect AI-generated text, get confidence scores, multilingual support (French/Spanish), and detailed probability breakdowns.
- [lpigeon/ros-mcp-server](https://github.com/lpigeon/ros-mcp-server) 🐍 🏠 🍎 🪟 🐧 - The ROS MCP Server supports robot control by converting user-issued natural language commands into ROS or ROS2 control commands.
- [lpigeon/unitree-go2-mcp-server](https://github.com/lpigeon/unitree-go2-mcp-server) 🐍 🏠 🐧 - The Unitree Go2 MCP Server is a server built on the MCP that enables users to control the Unitree Go2 robot using natural language commands interpreted by a LLM.
- [madhan-g-p/DevDocs-MCP](https://github.com/madhan-g-p/DevDocs-MCP) 📇 🏠 🍎 🐧 - DevDocs-MCP is a MCP server that provides version-pinned, deterministic documentation sourced from [DevDocs.io](https://devdocs.io) in offline mode
- [mattjegan/swarmia-mcp](https://github.com/mattjegan/swarmia-mcp) 🐍 🏠 🍎 🐧 - Read-only MCP server to help gather metrics from [Swarmia](swarmia.com) for quick reporting.
- [meanands/npm-package-docs-mcp](https://github.com/meanands/npm-package-docs-mcp) ☁️ - MCP Server that provides up-to-date documentation for npm packages by fetching the latest README doc from the package's GitHub repository or the README.
- [MerabyLabs/promptarchitect-mcp](https://github.com/MerabyLabs/promptarchitect-mcp) 📇 ☁️ 🍎 🪟 🐧 - Workspace-aware prompt engineering. Refines, analyzes and generates prompts based on your project's tech stack, dependencies and context. Free to use.
- [mhmzdev/Figma-Flutter-MCP](https://github.com/mhmzdev/Figma-Flutter-MCP) 📇 🏠 - Provide coding agents direct access to Figma data to help them write Flutter code for building apps including assets exports, widgets maintenance and full screens implementations.
- [mihaelamj/cupertino](https://github.com/mihaelamj/cupertino) 🏠 🍎 - Apple Documentation MCP Server. Search Apple developer docs, Swift Evolution proposals, and 600+ sample code projects with full-text search.
- [MikeRecognex/mcp-codebase-index](https://github.com/MikeRecognex/mcp-codebase-index) 🐍 🏠 🍎 🪟 🐧 - Structural codebase indexer exposing 17 query tools (functions, classes, imports, dependency graphs, change impact) via MCP. Zero dependencies.
- [mmorris35/devplan-mcp-server](https://github.com/mmorris35/devplan-mcp-server) 📇 ☁️ - Generate comprehensive, paint-by-numbers development plans using the [ClaudeCode-DevPlanBuilder](https://github.com/mmorris35/ClaudeCode-DevPlanBuilder) methodology. Creates PROJECT_BRIEF.md, DEVELOPMENT_PLAN.md, and CLAUDE.md.
- [mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp) 📇 🏠 🐧 🍎 - MCP Server for Android/iOS application and device automation, development and app scraping. Simulator/Emulator/Physical devices like iPhone, Google Pixel, Samsung supported.
- [mrexodia/user-feedback-mcp](https://github.com/mrexodia/user-feedback-mcp) 🐍 🏠 - Simple MCP Server to enable a human-in-the-loop workflow in tools like Cline and Cursor.
- [mumez/pharo-smalltalk-interop-mcp-server](https://github.com/mumez/pharo-smalltalk-interop-mcp-server) 🐍 🏠 - Pharo Smalltalk integration enabling code evaluation, class/method introspection, package management, test execution, and project installation for interactive development with Pharo images.
- [n8daniels/RulesetMCP](https://github.com/n8daniels/RulesetMCP) 📇 🏠 - Weight-On-Wheels for AI - keeps agents grounded in your project's rules. Query coding standards, validate snippets, and get task-specific guidance from version-controlled rule files.
- [narumiruna/gitingest-mcp](https://github.com/narumiruna/gitingest-mcp) 🐍 🏠 - A MCP server that uses [gitingest](https://github.com/cyclotruc/gitingest) to convert any Git repository into a simple text digest of its codebase.
- [neilberkman/editorconfig_mcp](https://github.com/neilberkman/editorconfig_mcp) 📇 🏠 - Formats files using `.editorconfig` rules, acting as a proactive formatting gatekeeper to ensure AI-generated code adheres to project-specific formatting standards from the start.
- [Neo1228/spring-boot-starter-swagger-mcp](https://github.com/Neo1228/spring-boot-starter-swagger-mcp) ☕ ☁️ 🏠 - Turn your Spring Boot application into an MCP server instantly by reusing existing Swagger/OpenAPI documentation.
- [OctoMind-dev/octomind-mcp](https://github.com/OctoMind-dev/octomind-mcp) 📇 ☁️ - lets your preferred AI agent create & run fully managed [Octomind](https://www.octomind.dev/) end-to-end tests from your codebase or other data sources like Jira, Slack or TestRail.
- [ooples/token-optimizer-mcp](https://github.com/ooples/token-optimizer-mcp) 📇 🏠 ☁️ 🍎 🪟 🐧 - Intelligent token optimization achieving 95%+ reduction through caching, compression, and 80+ smart tools for API optimization, code analysis, and real-time monitoring.
- [OpenZeppelin/contracts-wizard](https://github.com/OpenZeppelin/contracts-wizard/tree/master/packages/mcp) - A Model Context Protocol (MCP) server that allows AI agents to generate secure smart contracts in multiples languages based on [OpenZeppelin Wizard templates](https://wizard.openzeppelin.com/).
- [opslevel/opslevel-mcp](https://github.com/opslevel/opslevel-mcp) 🎖️ 🏎️ ☁️ 🪟 🍎 🐧 - Official MCP Server for [OpsLevel](https://www.opslevel.com)
- [optimaquantum/claude-critical-rules-mcp](https://github.com/optimaquantum/claude-critical-rules-mcp) 📇 ☁️ 🏠 🍎 🪟 🐧 - Automatic enforcement of critical rules for Claude AI preventing 96 documented failure patterns. Provides compliance verification checklist and rules summary via MCP tools.
- [paracetamol951/P-Link-MCP](https://github.com/paracetamol951/P-Link-MCP) 🏠 🐧 🍎 ☁️ - Implementation of HTTP 402 (payment required http code) relying on Solana
- [picahq/mcp](https://github.com/picahq/mcp) 🎖️ 🦀 📇 ☁️ - One MCP for all your integrations — powered by [Pica](https://www.picaos.com), the infrastructure for intelligent, collaborative agents.
- [posthog/mcp](https://github.com/posthog/mcp) 🎖️ 📇 ☁️ - An MCP server for interacting with PostHog analytics, feature flags, error tracking and more.
- [pylonapi/pylon-mcp](https://github.com/pylonapi/pylon-mcp) 📇 ☁️ - x402-native API gateway with 20+ capabilities (web-extract, web-search, translate, image-generate, screenshot, PDF, OCR, and more) payable with USDC on Base. No API keys — agents pay per call via HTTP 402.
- [Pratyay/mac-monitor-mcp](https://github.com/Pratyay/mac-monitor-mcp) 🐍 🏠 🍎 - Identifies resource-intensive processes on macOS and provides performance improvement suggestions.
- [PromptExecution/cratedocs-mcp](https://github.com/promptexecution/cratedocs-mcp) 🦀 🏠 - Outputs short-form Rust crate derived traits,interfaces, etc. from AST (uses same api as rust-analyzer), output limits (token estimation) & crate docs w/regex stripping.
- [promptexecution/just-mcp](https://github.com/promptexecution/just-mcp) 🦀 🏠 - Justfile integration that enables LLMs to execute any CLI or script commands with parameters safely and easily, with environment variable support and comprehensive testing.
- [pskill9/website-downloader](https://github.com/pskill9/website-downloader) 🗄️ 🚀 - This MCP server provides a tool to download entire websites using wget. It preserves the website structure and converts links to work locally.
- [PSU3D0/spreadsheet-mcp](https://github.com/PSU3D0/spreadsheet-mcp) 🦀 🏠 🪟 - High-performance, token-efficient spreadsheet analysis/editing (xlsx/xlsm) with region detection, structured reads, formula/style inspection, forking mechanics, and recalculation. Cross-platform.
- [public-ui/kolibri](https://github.com/public-ui/kolibri) 📇 ☁️ 🏠 - Streaming KoliBri MCP server (NPM: `@public-ui/mcp`) delivering 200+ guaranteed accessible web component samples, specs, docs, and scenarios via hosted HTTP endpoint or local `kolibri-mcp` CLI.
- [pzalutski-pixel/javalens-mcp](https://github.com/pzalutski-pixel/javalens-mcp) ☕ 🏠 - 56 semantic Java analysis tools via Eclipse JDT. Compiler-accurate navigation, refactoring, find references, call hierarchy, and code metrics for AI agents.
- [pzalutski-pixel/sharplens-mcp](https://github.com/pzalutski-pixel/sharplens-mcp) #️⃣ 🏠 - 58 semantic C#/.NET analysis tools via Roslyn. Navigation, refactoring, find usages, and code intelligence for AI agents.
- [qainsights/jmeter-mcp-server](https://github.com/QAInsights/jmeter-mcp-server) 🐍 🏠 - JMeter MCP Server for performance testing
- [qainsights/k6-mcp-server](https://github.com/QAInsights/k6-mcp-server) 🐍 🏠 - Grafana k6 MCP Server for performance testing
- [qainsights/locust-mcp-server](https://github.com/QAInsights/locust-mcp-server) 🐍 🏠 - Locust MCP Server for performance testing
- [QuantGeekDev/docker-mcp](https://github.com/QuantGeekDev/docker-mcp) 🏎️ 🏠 - Docker container management and operations through MCP
- [r-huijts/xcode-mcp-server](https://github.com/r-huijts/xcode-mcp-server) 📇 🏠 🍎 - Xcode integration for project management, file operations, and build automation
- [ReAPI-com/mcp-openapi](https://github.com/ReAPI-com/mcp-openapi) 📇 🏠 - MCP server that lets LLMs know everything about your OpenAPI specifications to discover, explain and generate code/mock data
- [reflagcom/mcp](https://github.com/reflagcom/javascript/tree/main/packages/cli#model-context-protocol) 🎖️ 📇 ☁️ - Flag features directly from chat in your IDE with [Reflag](https://reflag.com).
- [Rootly-AI-Labs/Rootly-MCP-server](https://github.com/Rootly-AI-Labs/Rootly-MCP-server) 🎖️ 🐍 ☁️ 🍎 - MCP server for the incident management platform [Rootly](https://rootly.com/).
- [rsdouglas/janee](https://github.com/rsdouglas/janee) 📇 🏠 🍎 🪟 🐧 - Self-evolving MCP server that generates and improves its own tools at runtime. Built on FastMCP, Janee uses LLM-driven tool generation to dynamically create, test, and refine MCP tools from natural language descriptions — enabling AI agents to extend their own capabilities on the fly.
- [ryan0204/github-repo-mcp](https://github.com/Ryan0204/github-repo-mcp) 📇 ☁️ 🪟 🐧 🍎 - GitHub Repo MCP allow your AI assistants browse GitHub repositories, explore directories, and view file contents.
- [sammcj/mcp-package-version](https://github.com/sammcj/mcp-package-version) 📇 🏠 - An MCP Server to help LLMs suggest the latest stable package versions when writing code.
- [sapientpants/sonarqube-mcp-server](https://github.com/sapientpants/sonarqube-mcp-server) 🦀 ☁️ 🏠 - A Model Context Protocol (MCP) server that integrates with SonarQube to provide AI assistants with access to code quality metrics, issues, and quality gate statuses
- [sbroenne/mcp-server-excel](https://github.com/sbroenne/mcp-server-excel) #️⃣ 🏠 🪟 - Full-featured Excel MCP server. 173 operations: Power Query, DAX, VBA, PivotTables, Tables, Charts, ranges, formatting. 100% Excel compatibility - uses Excel app instead of creating .xlsx files. Windows only.
- [SDGLBL/mcp-claude-code](https://github.com/SDGLBL/mcp-claude-code) 🐍 🏠 - An implementation of Claude Code capabilities using MCP, enabling AI code understanding, modification, and project analysis with comprehensive tool support.
- [selvage-lab/selvage](https://github.com/selvage-lab/selvage) 🐍 🏠 - LLM-based code review MCP server with AST-powered smart context extraction. Supports Claude, GPT, Gemini, and 20+ models via OpenRouter.
- [sequa-ai/sequa-mcp](https://github.com/sequa-ai/sequa-mcp) 📇 ☁️ 🐧 🍎 🪟 - Stop stitching context for Copilot and Cursor. With Sequa MCP, your AI tools know your entire codebase and docs out of the box.
- [shadcn/studio MCP](https://shadcnstudio.com/mcp) - Integrate shadcn/studio MCP Server directly into your favorite IDE and craft stunning shadcn/ui Components, Blocks and Pages inspired by shadcn/studio.
- [SimplyLiz/CodeMCP](https://github.com/SimplyLiz/CodeMCP) 🏎️ 🏠 🍎 🪟 🐧 - Code intelligence MCP server with 80+ tools for semantic code search, impact analysis, call graphs, ownership detection, and architectural understanding. Supports Go, TypeScript, Python, Rust, Java via SCIP indexing.
- [simplypixi/bugbug-mcp-server](https://github.com/simplypixi/bugbug-mcp-server) ☁️ - MCP for BugBug API, to manage test and suites on BugBug
- [skullzarmy/vibealive](https://github.com/skullzarmy/vibealive) 📇 🏠 🍎 🪟 🐧 — Full-featured utility to test Next.js projects for unused files and APIs, with an MCP server that exposes project analysis tools to AI assistants.
- [snaggle-ai/openapi-mcp-server](https://github.com/snaggle-ai/openapi-mcp-server) 🏎️ 🏠 - Connect any HTTP/REST API server using an Open API spec (v3)
- [softvoyagers/linkshrink-api](https://github.com/softvoyagers/linkshrink-api) 📇 ☁️ - Free privacy-first URL shortener API with analytics and link management. No API key required.
- [softvoyagers/ogforge-api](https://github.com/softvoyagers/ogforge-api) 📇 ☁️ - Free Open Graph image generator API with themes, Lucide icons, and custom layouts. No API key required.
- [softvoyagers/pagedrop-api](https://github.com/softvoyagers/pagedrop-api) 📇 ☁️ - Free instant HTML hosting API with paste, file upload, and ZIP deploy support. No API key required.
- [softvoyagers/pdfspark-api](https://github.com/softvoyagers/pdfspark-api) 📇 ☁️ - Free HTML/URL to PDF conversion API powered by Playwright. No API key required.
- [softvoyagers/qrmint-api](https://github.com/softvoyagers/qrmint-api) 📇 ☁️ - Free styled QR code generator API with custom colors, logos, frames, and batch generation. No API key required.
- [spacecode-ai/SpaceBridge-MCP](https://github.com/spacecode-ai/SpaceBridge-MCP) 🐍 🏠 🍎 🐧 - Bring structure and preserve context in vibe coding by automatically tracking issues.
- [srijanshukla18/xray](https://github.com/srijanshukla18/xray) 🐍 🏠 - Progressive code-intelligence MCP server: map project structure, fuzzy-find symbols, and assess change-impact across Python, JS/TS, and Go (powered by `ast-grep`).
- [st3v3nmw/sourcerer-mcp](https://github.com/st3v3nmw/sourcerer-mcp) 🏎️ ☁️ - MCP for semantic code search & navigation that reduces token waste
- [stass/lldb-mcp](https://github.com/stass/lldb-mcp) 🐍 🏠 🐧 🍎 - A MCP server for LLDB enabling AI binary and core file analysis, debugging, disassembling.
- [storybookjs/addon-mcp](https://github.com/storybookjs/addon-mcp) 📇 🏠 - Help agents automatically write and test stories for your UI components.
- [TamarEngel/jira-github-mcp](https://github.com/TamarEngel/jira-github-mcp) - MCP server that integrates Jira and GitHub to automate end-to-end developer workflows, from issue tracking to branches, commits, pull requests, and merges inside the IDE.
- [TCSoftInc/testcollab-mcp-server](https://github.com/TCSoftInc/testcollab-mcp-server) ☁️ - Manage test cases in TestCollab directly from your AI coding assistant. List, create, and update test cases with filtering, sorting, and pagination support.
- [TencentEdgeOne/edgeone-pages-mcp](https://github.com/TencentEdgeOne/edgeone-pages-mcp) 📇 ☁️ - An MCP service for deploying HTML content to EdgeOne Pages and obtaining a publicly accessible URL.
- [testdino-hq/testdino-mcp](https://github.com/testdino-hq/testdino-mcp) 🎖️ 📇 ☁️ - Connects your TestDino testrun/testcase data to AI agents so you can review runs, debug failures, and manage manual test cases using natural language.
- [tgeselle/bugsnag-mcp](https://github.com/tgeselle/bugsnag-mcp) 📇 ☁️ - An MCP server for interacting with [Bugsnag](https://www.bugsnag.com/)
- [themesberg/flowbite-mcp](https://github.com/themesberg/flowbite-mcp) 📇 🏠 🍎 🪟 🐧 - MCP server that provides AI assistance for an open-source UI framework based on Tailwind CSS
- [tipdotmd/tip-md-x402-mcp-server](https://github.com/tipdotmd/tip-md-x402-mcp-server) 📇 ☁️ - MCP server for cryptocurrency tipping through AI interfaces using x402 payment protocol and CDP Wallet.
- [Tommertom/awesome-ionic-mcp](https://github.com/Tommertom/awesome-ionic-mcp) 📇 🏠 - Your Ionic coding buddy enabled via MCP – build awesome mobile apps using React/Angular/Vue or even Vanilla JS!
- [tosin2013/mcp-adr-analysis-server](https://github.com/tosin2013/mcp-adr-analysis-server) 📇 ☁️ 🏠 - AI-powered architectural analysis server for software projects. Provides technology stack detection, ADR management, security checks, enhanced TDD workflow, and deployment readiness validation with support for multiple AI models.
- [tumf/mcp-text-editor](https://github.com/tumf/mcp-text-editor) 🐍 🏠 - A line-oriented text file editor. Optimized for LLM tools with efficient partial file access to minimize token usage.
- [ukkit/memcord](https://github.com/ukkit/memcord) 🐍 🏠 🐧 🍎 - A MCP server that keeps your chat history organized and searchable—with AI-powered summaries, secure memory, and full control.
- [utensils/mcp-nixos](https://github.com/utensils/mcp-nixos) 🐍 🏠 - MCP server providing accurate information about NixOS packages, system options, Home Manager configurations, and nix-darwin macOS settings to prevent AI hallucinations.
- [V0v1kkk/DotNetMetadataMcpServer](https://github.com/V0v1kkk/DotNetMetadataMcpServer) #️⃣ 🏠 🍎 🪟 🐧 - Provides AI agents with detailed type information from .NET projects including assembly exploration, namespace discovery, type reflection, and NuGet integration
- [valado/pantheon-mcp](https://github.com/valado/pantheon-mcp) 🤖 - MCP server providing task specific agentic instructions. No more outdated Markdown files and synchronisation overhead.
- [var-gg/mcp](https://github.com/var-gg/mcp) 📇 ☁️ - Enforces team naming consistency for AI-generated code via Cursor MCP integration. [Guide ↗](https://var.gg)
- [vasayxtx/mcp-prompt-engine](https://github.com/vasayxtx/mcp-prompt-engine) 🏎️ 🏠 🪟️ 🐧 🍎 - MCP server for managing and serving dynamic prompt templates using elegant and powerful text template engine.
- [veelenga/claude-mermaid](https://github.com/veelenga/claude-mermaid/) 📇 🏠 🍎 🪟 🐧 - A Mermaid diagram rendering MCP server for Claude Code with live reload functionality, supporting multiple export formats (SVG, PNG, PDF) and themes.
- [vercel/next-devtools-mcp](https://github.com/vercel/next-devtools-mcp) 🎖️ 📇 🏠 - Official Next.js MCP server for coding agents. Provides runtime diagnostics, route inspection, dev server logs, docs search, and upgrade guides. Requires Next.js 16+ dev server for full runtime features.
- [vezlo/src-to-kb](https://github.com/vezlo/src-to-kb) 📇 🏠 ☁️ - Convert source code repositories into searchable knowledge bases with AI-powered search using GPT-5, intelligent chunking, and OpenAI embeddings for semantic code understanding.
- [vivekvells/mcp-pandoc](https://github.com/vivekVells/mcp-pandoc) 🗄️ 🚀 - MCP server for seamless document format conversion using Pandoc, supporting Markdown, HTML, PDF, DOCX (.docx), csv and more.
- [VSCode Devtools](https://github.com/biegehydra/BifrostMCP) 📇 - Connect to VSCode ide and use semantic tools like `find_usages`
- [Webvizio/mcp](https://github.com/Webvizio/mcp) 🎖️ 📇 - Automatically converts feedback and bug reports from websites and web apps into actionable, context-enriched developer tasks. Delivered straight to your AI coding tools, the Webvizio MCP Server ensures your AI agent has all the data it needs to solve tasks with speed and accuracy.
- [WiseVision/mcp_server_ros_2](https://github.com/wise-vision/mcp_server_ros_2) 🐍 🤖 - MCP server for ROS2 enabling AI-driven robotics applications and services.
- [wn01011/llm-token-tracker](https://github.com/wn01011/llm-token-tracker) 📇 🏠 🍎 🪟 🐧 - Token usage tracker for OpenAI and Claude APIs with MCP support, real-time session tracking, and accurate pricing for 2025 models
- [Wolfe-Jam/claude-faf-mcp](https://github.com/Wolfe-Jam/claude-faf-mcp) 📇 🏠 - First & only persistent project context MCP. Provides .faf (Foundational AI-context Format) Project DNA with 33+ tools, Podium scoring (0-100%), and format-driven architecture. Official Anthropic Registry. 10k+ npm downloads.
- [Wolfe-Jam/faf-mcp](https://github.com/Wolfe-Jam/faf-mcp) 📇 🏠 - Universal persistent project context for Cursor, Windsurf, Cline, VS Code, and all MCP-compatible platforms (including Claude Desktop). IANA-registered format (application/vnd.faf+yaml). 17 native tools, AI-readiness scoring.
- [Wooonster/hocr_mcp_server](https://github.com/Wooonster/hocr_mcp_server) 🐍 🏠 – A fastAPI-based FastMCP server with a Vue frontend that sends uploaded images to VLM via the MCP to quickly extract handwritten mathematical formulas as clean LaTeX code.
- [wyattjoh/jsr-mcp](https://github.com/wyattjoh/jsr-mcp) 📇 ☁️ - Model Context Protocol server for the JSR (JavaScript Registry)
- [xcodebuild](https://github.com/ShenghaiWang/xcodebuild) 🍎 Build iOS Xcode workspace/project and feed back errors to llm.
- [XixianLiang/HarmonyOS-mcp-server](https://github.com/XixianLiang/HarmonyOS-mcp-server) 🐍 🏠 - Control HarmonyOS-next devices with AI through MCP. Support device control and UI automation.
- [xzq.xu/jvm-mcp-server](https://github.com/xzq-xu/jvm-mcp-server) 📇 🏠  - An implementation project of a JVM-based MCP (Model Context Protocol) server.
- [yangkyeongmo@/mcp-server-apache-airflow](https://github.com/yangkyeongmo/mcp-server-apache-airflow) 🐍 🏠 - MCP server that connects to [Apache Airflow](https://airflow.apache.org/) using official client.
- [yanmxa/scriptflow-mcp](https://github.com/yanmxa/scriptflow-mcp) 📇 🏠 - A script workflow management system that transforms complex, repetitive AI interactions into persistent, executable scripts. Supports multi-language execution (Bash, Python, Node.js, TypeScript) with guaranteed consistency and reduced hallucination risks.
- [yikakia/godoc-mcp-server](https://github.com/yikakia/godoc-mcp-server) 🏎️ ☁️ 🪟 🐧 🍎 - Query Go package information on pkg.go.dev
- [yiwenlu66/PiloTY](https://github.com/yiwenlu66/PiloTY) 🐍 🏠 - AI pilot for PTY operations enabling agents to control interactive terminals with stateful sessions, SSH connections, and background process management
- [YuChenSSR/mindmap-mcp-server](https://github.com/YuChenSSR/mindmap-mcp-server) 🐍 🏠 - A Model Context Protocol (MCP) server for generating a beautiful interactive mindmap.
- [YuChenSSR/multi-ai-advisor](https://github.com/YuChenSSR/multi-ai-advisor-mcp) 📇 🏠 - A Model Context Protocol (MCP) server that queries multiple Ollama models and combines their responses, providing diverse AI perspectives on a single question.
- [Yutarop/ros-mcp](https://github.com/Yutarop/ros-mcp) 🐍 🏠 🐧 - MCP server that supports ROS2 topics, services, and actions communication, and controls robots using natural language.
- [yWorks/mcp-typescribe](https://github.com/yWorks/mcp-typescribe) 📇 🏠 - MCP server that provides Typescript API information efficiently to the agent to enable it to work with untrained APIs
- [zaizaizhao/mcp-swagger-server](https://github.com/zaizaizhao/mcp-swagger-server) 📇 ☁️ 🏠 - A Model Context Protocol (MCP) server that converts OpenAPI/Swagger specifications to MCP format, enabling AI assistants to interact with REST APIs through standardized protocol.
- [zcaceres/fetch-mcp](https://github.com/zcaceres/fetch-mcp) 📇 🏠 - An MCP server to flexibly fetch JSON, text, and HTML data
- [zelentsov-dev/asc-mcp](https://github.com/zelentsov-dev/asc-mcp) 🏠 🍎 - App Store Connect API server with 208 tools for managing apps, builds, TestFlight, subscriptions, reviews, and more — directly from any MCP client.
- [zenml-io/mcp-zenml](https://github.com/zenml-io/mcp-zenml) 🐍 🏠 ☁️ - An MCP server to connect with your [ZenML](https://www.zenml.io) MLOps and LLMOps pipelines
- [zillow/auto-mobile](https://github.com/zillow/auto-mobile) 📇 🏠 🐧  - Tool suite built around an MCP server for Android automation for developer workflow and testing
- [ztuskes/garmin-documentation-mcp-server](https://github.com/ztuskes/garmin-documentation-mcp-server) 📇 🏠 – Offline Garmin Connect IQ SDK documentation with comprehensive search and API examples

### 🔒 <a name="delivery"></a>Delivery

- [jordandalton/doordash-mcp-server](https://github.com/JordanDalton/DoorDash-MCP-Server) 🐍 – DoorDash Delivery (Unofficial)
- [aarsiv-groups/shipi-mcp-server](https://github.com/aarsiv-groups/shipi-mcp-server) 📇 ☁️ - Shipi MCP server to create shipments, track packages, and compare rates with 18 tools for various carriers. Supports [remote MCP](https://mcp.myshipi.com/api/mcp).

### 🧮 <a name="data-science-tools"></a>Data Science Tools

Integrations and tools designed to simplify data exploration, analysis and enhance data science workflows.

- [abhiphile/fermat-mcp](https://github.com/abhiphile/fermat-mcp) 🐍 🏠 🍎 🪟 🐧 - The ultimate math engine unifying SymPy, NumPy & Matplotlib in one powerful server. Perfect for developers & researchers needing symbolic algebra, numerical computing, and data visualization.
- [arrismo/kaggle-mcp](https://github.com/arrismo/kaggle-mcp) 🐍 ☁️ - Connects to Kaggle, ability to download and analyze datasets.
- [avisangle/calculator-server](https://github.com/avisangle/calculator-server) 🏎️ 🏠 - A comprehensive Go-based MCP server for mathematical computations, implementing 13 mathematical tools across basic arithmetic, advanced functions, statistical analysis, unit conversions, and financial calculations.
- [bradleylab/stella-mcp](https://github.com/bradleylab/stella-mcp) 🐍 🏠 - Create, read, validate, and save Stella system dynamics models (.stmx files in XMILE format) for scientific simulation and modeling.
- [Bright-L01/networkx-mcp-server](https://github.com/Bright-L01/networkx-mcp-server) 🐍 🏠 - The first NetworkX integration for Model Context Protocol, enabling graph analysis and visualization directly in AI conversations. Supports 13 operations including centrality algorithms, community detection, PageRank, and graph visualization.
- [ChronulusAI/chronulus-mcp](https://github.com/ChronulusAI/chronulus-mcp) 🐍 ☁️ - Predict anything with Chronulus AI forecasting and prediction agents.
- [clouatre-labs/math-mcp-learning-server](https://github.com/clouatre-labs/math-mcp-learning-server) 🐍 ☁️ 🏠 🍎 🪟 🐧 - Educational MCP server for math operations, statistics, visualization, and persistent workspaces. Built with FastMCP 2.0.
- [DataEval/dingo](https://github.com/DataEval/dingo) 🎖️ 🐍 🏠 🍎 🪟 🐧 - MCP server for the Dingo: a comprehensive data quality evaluation tool. Server Enables interaction with Dingo's rule-based and LLM-based evaluation capabilities and rules&prompts listing.
- [datalayer/jupyter-mcp-server](https://github.com/datalayer/jupyter-mcp-server) 🐍 🏠 - Model Context Protocol (MCP) Server for Jupyter.
- [growthbook/growthbook-mcp](https://github.com/growthbook/growthbook-mcp) 🎖️ 📇 🏠 🪟 🐧 🍎 — Tools for creating and interacting with GrowthBook feature flags and experiments.
- [HumanSignal/label-studio-mcp-server](https://github.com/HumanSignal/label-studio-mcp-server) 🎖️ 🐍 ☁️ 🪟 🐧 🍎 - Create, manage, and automate Label Studio projects, tasks, and predictions for data labeling workflows.
- [jjsantos01/jupyter-notebook-mcp](https://github.com/jjsantos01/jupyter-notebook-mcp) 🐍 🏠 - connects Jupyter Notebook to Claude AI, allowing Claude to directly interact with and control Jupyter Notebooks.
- [kdqed/zaturn](https://github.com/kdqed/zaturn) 🐍 🏠 🪟 🐧 🍎 - Link multiple data sources (SQL, CSV, Parquet, etc.) and ask AI to analyze the data for insights and visualizations.
- [mckinsey/vizro-mcp](https://github.com/mckinsey/vizro/tree/main/vizro-mcp) 🎖️ 🐍 🏠 - Tools and templates to create validated and maintainable data charts and dashboards.
- [optuna/optuna-mcp](https://github.com/optuna/optuna-mcp) 🎖️ 🐍 🏠 🐧 🍎 - Official MCP server enabling seamless orchestration of hyperparameter search and other optimization tasks with [Optuna](https://optuna.org/).
- [phisanti/MCPR](https://github.com/phisanti/MCPR) 🏠 🍎 🪟 🐧 - Model Context Protocol for R: enables AI agents to participate in interactive live R sessions.
- [phuongrealmax/code-guardian](https://github.com/phuongrealmax/code-guardian) 📇 🏠 - AI-powered code refactor engine with 80+ MCP tools for code analysis, hotspot detection, complexity metrics, persistent memory, and automated refactoring plans.
- [pramod/kaggle](https://github.com/KrishnaPramodParupudi/kaggle-mcp-server) 🐍 - This Kaggle MCP Server makes Kaggle more accessible by letting you browse competitions, leaderboards, models, datasets, and kernels directly within MCP, streamlining discovery for data scientists and developers.
- [reading-plus-ai/mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration) 🐍 ☁️ - Enables autonomous data exploration on .csv-based datasets, providing intelligent insights with minimal effort.
- [subelsky/bundler_mcp](https://github.com/subelsky/bundler_mcp) 💎 🏠 - Enables agents to query local information about dependencies in a Ruby project's `Gemfile`.
- [zcaceres/markdownify-mcp](https://github.com/zcaceres/markdownify-mcp) 📇 🏠 - An MCP server to convert almost any file or web content into Markdown

### 📟 <a name="embedded-system"></a>Embedded System

Provides access to documentation and shortcuts for working on embedded devices.

- [0x1abin/matter-controller-mcp](https://github.com/0x1abin/matter-controller-mcp) 📇 📟 - An MCP server for Matter Controller, enabling AI agents to control and interact with Matter devices.
- [adancurusul/embedded-debugger-mcp](https://github.com/adancurusul/embedded-debugger-mcp) 🦀 📟 - A Model Context Protocol server for embedded debugging with probe-rs - supports ARM Cortex-M, RISC-V debugging via J-Link, ST-Link, and more
- [adancurusul/serial-mcp-server](https://github.com/adancurusul/serial-mcp-server) 🦀 📟 - A comprehensive MCP server for serial port communication
- [horw/esp-mcp](https://github.com/horw/esp-mcp) 📟 - Workflow for fixing build issues in ESP32 series chips using ESP-IDF.
- [kukapay/modbus-mcp](https://github.com/kukapay/modbus-mcp) 🐍 📟 - An MCP server that standardizes and contextualizes industrial Modbus data.
- [kukapay/opcua-mcp](https://github.com/kukapay/opcua-mcp) 🐍 📟 - An MCP server that connects to OPC UA-enabled industrial systems.
- [stack-chan/stack-chan](https://github.com/stack-chan/stack-chan) 📇 📟 - A JavaScript-driven M5Stack-embedded super-kawaii robot with MCP server functionality for AI-controlled interactions and emotions.
- [yoelbassin/gnuradioMCP](https://github.com/yoelbassin/gnuradioMCP) 🐍 📟 🏠 - An MCP server for GNU Radio that enables LLMs to autonomously create and modify RF `.grc` flowcharts.

### 🌳 <a name="environment-and-nature"></a>Environment & Nature

Provides access to environmental data and nature-related tools, services and information.

- [aliafsahnoudeh/wildfire-mcp-server](https://github.com/aliafsahnoudeh/wildfire-mcp-server) 🐍 ☁️ 🍎 🪟 🐧 - MCP server for detecting, monitoring, and analyzing potential wildfires globally using multiple data sources including NASA FIRMS, OpenWeatherMap, and Google Earth Engine.

### 📂 <a name="file-systems"></a>File Systems

Provides direct access to local file systems with configurable permissions. Enables AI models to read, write, and manage files within specified directories.

- [8b-is/smart-tree](https://github.com/8b-is/smart-tree) 🦀 🏠 🍎 🪟 🐧 - AI-native directory visualization with semantic analysis, ultra-compressed formats for AI consumption, and 10x token reduction. Supports quantum-semantic mode with intelligent file categorization.
- [box/mcp-server-box-remote](https://github.com/box/mcp-server-box-remote/) 🎖️ ☁️ - The Box MCP server allows third party AI agents to securely and seamlessly access Box content and use tools such as search, asking questions from files and folders, and data extraction.
- [cyberchitta/llm-context.py](https://github.com/cyberchitta/llm-context.py) 🐍 🏠 - Share code context with LLMs via MCP or clipboard
- [efforthye/fast-filesystem-mcp](https://github.com/efforthye/fast-filesystem-mcp) 📇 🏠 🍎 🪟 🐧 - Advanced filesystem operations with large file handling capabilities and Claude-optimized features. Provides fast file reading/writing, sequential reading for large files, directory operations, file search, and streaming writes with backup & recovery.
- [exoticknight/mcp-file-merger](https://github.com/exoticknight/mcp-file-merger) 🏎️ 🏠 - File merger tool, suitable for AI chat length limits.
- [filesystem@quarkiverse/quarkus-mcp-servers](https://github.com/quarkiverse/quarkus-mcp-servers/tree/main/filesystem) ☕ 🏠 - A filesystem allowing for browsing and editing files implemented in Java using Quarkus. Available as jar or native image.
- [hmk/box-mcp-server](https://github.com/hmk/box-mcp-server) 📇 ☁️ - Box integration for listing, reading and searching files
- [isaacphi/mcp-gdrive](https://github.com/isaacphi/mcp-gdrive) 📇 ☁️ - Model Context Protocol (MCP) Server for reading from Google Drive and editing Google Sheets.
- [j0hanz/filesystem-context-mcp-server](https://github.com/j0hanz/filesystem-context-mcp-server) 📇 🏠 - Read-only MCP server for secure filesystem exploration, searching, and analysis with symlink protection.
- [jeannier/homebrew-mcp](https://github.com/jeannier/homebrew-mcp) 🐍 🏠 🍎 - Control your macOS Homebrew setup using natural language via this MCP server. Simply manage your packages, or ask for suggestions, troubleshoot brew issues etc.
- [mamertofabian/mcp-everything-search](https://github.com/mamertofabian/mcp-everything-search) 🐍 🏠 🪟 - Fast Windows file search using Everything SDK
- [MarceauSolutions/md-to-pdf-mcp](https://github.com/MarceauSolutions/md-to-pdf-mcp) 🐍 🏠 🍎 🪟 🐧 - Convert Markdown files to professional PDFs with customizable themes, headers, footers, and styling
- [mark3labs/mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server) 🏎️ 🏠 - Golang implementation for local file system access.
- [mickaelkerjean/filestash](https://github.com/mickael-kerjean/filestash/tree/master/server/plugin/plg_handler_mcp) 🏎️ ☁️ - Remote Storage Access: SFTP, S3, FTP, SMB, NFS, WebDAV, GIT, FTPS, gcloud, azure blob, sharepoint, etc.
- [microsoft/markitdown](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp) 🎖️ 🐍 🏠 - MCP tool access to MarkItDown -- a library that converts many file formats (local or remote) to Markdown for LLM consumption.
- [modelcontextprotocol/server-filesystem](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/filesystem) 📇 🏠 - Direct local file system access.
- [willianpinho/large-file-mcp](https://github.com/willianpinho/large-file-mcp) 📇 🏠 🍎 🪟 🐧 - Production-ready MCP server for intelligent handling of large files with smart chunking, navigation, streaming capabilities, regex search, and built-in LRU caching.
- [Xuanwo/mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal) 🐍 🏠 ☁️ - Access any storage with Apache OpenDAL™
- [xxczaki/local-history-mcp](https://github.com/xxczaki/local-history/mcp) 📇 🏠 🍎 🪟 🐧  - MCP server for accessing VS Code/Cursor Local History

### 💰 <a name="finance--fintech"></a>Finance & Fintech

- [@iiatlas/hledger-mcp](https://github.com/iiAtlas/hledger-mcp) 📇 🏠 🍎 🪟 - Double entry plain text accounting, right in your LLM! This MCP enables comprehensive read, and (optional) write access to your local [HLedger](https://hledger.org/) accounting journals.
- [aaronjmars/web3-research-mcp](https://github.com/aaronjmars/web3-research-mcp) 📇 ☁️ - Deep Research for crypto - free & fully local
- [ahmetsbilgin/finbrain-mcp](https://github.com/ahmetsbilgin/finbrain-mcp) 🎖️ 🐍 ☁️ 🏠 - Access institutional-grade alternative financial data directly in your LLM workflows.
- [ahnlabio/bicscan-mcp](https://github.com/ahnlabio/bicscan-mcp) 🎖️ 🐍 ☁️ - Risk score / asset holdings of EVM blockchain address (EOA, CA, ENS) and even domain names.
- [alchemy/alchemy-mcp-server](https://github.com/alchemyplatform/alchemy-mcp-server) 🎖️ 📇 ☁️ - Allow AI agents to interact with Alchemy's blockchain APIs.
- [anjor/coinmarket-mcp-server](https://github.com/anjor/coinmarket-mcp-server) 🐍 ☁️ - Coinmarket API integration to fetch cryptocurrency listings and quotes
- [araa47/jupiter-mcp](https://github.com/araa47/jupiter-mcp) 🐍 ☁️ - Jupiter API Access (allow AI to Trade Tokens on Solana + Access Balances + Search Tokens + Create Limit Orders )
- [ariadng/metatrader-mcp-server](https://github.com/ariadng/metatrader-mcp-server) 🐍 🏠 🪟 - Enable AI LLMs to execute trades using MetaTrader 5 platform
- [armorwallet/armor-crypto-mcp](https://github.com/armorwallet/armor-crypto-mcp) 🐍 ☁️ - MCP to interface with multiple blockchains, staking, DeFi, swap, bridging, wallet management, DCA, Limit Orders, Coin Lookup, Tracking and more.
- [bankless/onchain-mcp](https://github.com/Bankless/onchain-mcp/) 📇 ☁️ - Bankless Onchain API to interact with smart contracts, query transaction and token information
- [bolivian-peru/baozi-mcp](https://github.com/bolivian-peru/baozi-mcp) 📇 ☁️ - 68 tools for AI agents to interact with Solana prediction markets on [Baozi.bet](https://baozi.bet) — browse markets, place bets, claim winnings, create markets, and earn affiliate commissions.
- [base/base-mcp](https://github.com/base/base-mcp) 🎖️ 📇 ☁️ - Base Network integration for onchain tools, allowing interaction with Base Network and Coinbase API for wallet management, fund transfers, smart contracts, and DeFi operations
- [berlinbra/alpha-vantage-mcp](https://github.com/berlinbra/alpha-vantage-mcp) 🐍 ☁️ - Alpha Vantage API integration to fetch both stock and crypto information
- [bitteprotocol/mcp](https://github.com/BitteProtocol/mcp) 📇 - Bitte Protocol integration to run AI Agents on several blockchains.
- [bubilife1202/crossfin](https://github.com/bubilife1202/crossfin) 📇 ☁️ - Korean & global crypto exchange routing, arbitrage signals, and x402 USDC micropayments for AI agents. 16 tools, 9 exchanges, 11 bridge coins.
- [carsol/monarch-mcp-server](https://github.com/carsol/monarch-mcp-server) 🐍 ☁️ - MCP server providing read-only access to Monarch Money financial data, enabling AI assistants to analyze transactions, budgets, accounts, and cashflow data with MFA support.
- [chargebee/mcp](https://github.com/chargebee/agentkit/tree/main/modelcontextprotocol) 🎖️ 📇 ☁️ - MCP Server that connects AI agents to [Chargebee platform](https://www.chargebee.com/).
- [codex-data/codex-mcp](https://github.com/Codex-Data/codex-mcp) 🎖️ 📇 ☁️ - [Codex API](https://www.codex.io) integration for real-time enriched blockchain and market data on 60+ networks
- [coinpaprika/dexpaprika-mcp](https://github.com/coinpaprika/dexpaprika-mcp) 🎖️ 📇 ☁️ 🍎 🪟 🐧 - Coinpaprika's DexPaprika MCP server exposes high-performance [DexPaprika API](https://docs.dexpaprika.com) covering 20+ chains and 5M+ tokens with real time pricing, liquidity pool data & historical OHLCV data, providing AI agents standardized access to comprehensive market data through Model Context Protocol.
- [decidefyi/decide](https://github.com/decidefyi/decide) 📇 ☁️ - Deterministic refund eligibility notary MCP server. Returns ALLOWED / DENIED / UNKNOWN for subscription refunds (Adobe, Spotify, etc.) via a stateless rules engine.
- [debtstack-ai/debtstack-python](https://github.com/debtstack-ai/debtstack-python) 🐍 ☁️ - Corporate debt structure data for AI agents. Search 250+ issuers, 5,000+ bonds with leverage ratios, seniority, covenants, guarantor chains, and FINRA TRACE pricing.
- [doggybee/mcp-server-ccxt](https://github.com/doggybee/mcp-server-ccxt) 📇 ☁️ - An MCP server for accessing real-time crypto market data and trading via 20+ exchanges using the CCXT library. Supports spot, futures, OHLCV, balances, orders, and more.
- [Handshake58/DRAIN-marketplace](https://github.com/Handshake58/DRAIN-marketplace) 📇 ☁️ - Open marketplace for AI services — LLMs, image/video generation, web scraping, model hosting, data extraction, and more. Agents pay per use with USDC micropayments on Polygon. No API keys, no subscriptions.
- [etbars/vibetrader-mcp](https://github.com/etbars/vibetrader-mcp) 🐍 ☁️ - AI-powered trading bot platform. Create automated trading strategies with natural language via Alpaca brokerage.
- [Fan Token Intel MCP](https://github.com/BrunoPessoa22/chiliz-marketing-intel) 🐍 ☁️ - 67+ tools for fan token intelligence: whale flows, signal scores, sports calendar, backtesting, DEX trading, social sentiment. SSE transport with Bearer auth.
- [ferdousbhai/investor-agent](https://github.com/ferdousbhai/investor-agent) 🐍 ☁️ - Yahoo Finance integration to fetch stock market data including options recommendations
- [ferdousbhai/tasty-agent](https://github.com/ferdousbhai/tasty-agent) 🐍 ☁️ - Tastyworks API integration to handle trading activities on Tastytrade
- [ferdousbhai/wsb-analyst-mcp](https://github.com/ferdousbhai/wsb-analyst-mcp) 🐍 ☁️ - Reddit integration to analyze content on WallStreetBets community
- [fernikolic/clawdentials](https://github.com/fernikolic/clawdentials) 📇 ☁️ - Trust layer for AI agent commerce — escrow-protected payments, verifiable reputation scores, and Nostr identity (NIP-05) for agents. Supports USDC, USDT, and BTC (Cashu).
- [financialdatanet/mcp-server](https://github.com/financialdatanet/mcp-server) 🐍 🏠 🪟 🐧 - [FinancialData.Net](https://financialdata.net/) MCP server allows you to retrieve end-of-day and intraday stock market data, company financial statements, insider and institutional trading data, sustainability data, earnings releases, and much more.
- [finmap-org/mcp-server](https://github.com/finmap-org/mcp-server) - [finmap.org](https://finmap.org/) MCP server provides comprehensive historical data from the US, UK, Russian and Turkish stock exchanges. Access sectors, tickers, company profiles, market cap, volume, value, and trade counts, as well as treemap and histogram visualizations.
- [getAlby/mcp](https://github.com/getAlby/mcp) 🎖️ 📇 ☁️ 🏠 - Connect any bitcoin lightning wallet to your agent to send and receive instant payments globally.
- [getalby/nwc-mcp-server](https://github.com/getalby/nwc-mcp-server) 📇 🏠 - Bitcoin Lightning wallet integration powered by Nostr Wallet Connect
- [glaksmono/finbud-data-mcp](https://github.com/glaksmono/finbud-data-mcp/tree/main/packages/mcp-server) 📇 ☁️ 🏠 - Access comprehensive, real-time financial data (stocks, options, crypto, forex) via developer-friendly, AI-native APIs offering unbeatable value.
- [heurist-network/heurist-mesh-mcp-server](https://github.com/heurist-network/heurist-mesh-mcp-server) 🎖️ ⛅️ 🏠 🐍 - Access specialized web3 AI agents for blockchain analysis, smart contract security auditing, token metrics evaluation, and on-chain interactions through the Heurist Mesh network. Provides comprehensive tools for DeFi analysis, NFT valuation, and transaction monitoring across multiple blockchains
- [hive-intel/hive-crypto-mcp](https://github.com/hive-intel/hive-crypto-mcp) 📇 ☁️ 🏠 - Hive Intelligence: Ultimate cryptocurrency MCP for AI assistants with unified access to crypto, DeFi, and Web3 analytics
- [hoqqun/stooq-mcp](https://github.com/hoqqun/stooq-mcp) 🦀 ☁️ - Fetch real-time stock prices from Stooq without API keys. Supports global markets (US, Japan, UK, Germany).
- [HuggingAGI/mcp-baostock-server](https://github.com/HuggingAGI/mcp-baostock-server) 🐍 ☁️ - MCP server based on baostock, providing access and analysis capabilities for Chinese stock market data.
- [intentos-labs/beeper-mcp](https://github.com/intentos-labs/beeper-mcp) 🐍 - Beeper provides transactions on BSC, including balance/token transfers, token swaps in Pancakeswap and beeper reward claims.
- [JamesANZ/bitcoin-mcp](https://github.com/JamesANZ/bitcoin-mcp) 📇 🏠 - An MCP server that enables AI models to query the Bitcoin blockchain.
- [JamesANZ/evm-mcp](https://github.com/JamesANZ/evm-mcp) 📇 ☁️ - An MCP server that provides complete access to Ethereum Virtual Machine (EVM) JSON-RPC methods. Works with any EVM-compatible node provider including Infura, Alchemy, QuickNode, local nodes, and more.
- [JamesANZ/prediction-market-mcp](https://github.com/JamesANZ/prediction-market-mcp) 📇 ☁️ - An MCP server that provides real-time prediction market data from multiple platforms including Polymarket, PredictIt, and Kalshi. Enables AI assistants to query current odds, prices, and market information through a unified interface.
- [janswist/mcp-dexscreener](https://github.com/janswist/mcp-dexscreener) 📇 ☁️ - Real-time on-chain market prices using open and free Dexscreener API
- [jjlabsio/korea-stock-mcp](https://github.com/jjlabsio/korea-stock-mcp) 📇 ☁️ - An MCP Server for Korean stock analysis using OPEN DART API and KRX API
- [kukapay/binance-alpha-mcp](https://github.com/kukapay/binance-alpha-mcp) 🐍 ☁️ - An MCP server for tracking Binance Alpha trades, helping AI agents optimize alpha point accumulation.
- [kukapay/bitcoin-utxo-mcp](https://github.com/kukapay/bitcoin-utxo-mcp) 🐍 ☁️ - An MCP server that tracks Bitcoin's Unspent Transaction Outputs (UTXO) and block statistics.
- [kukapay/blockbeats-mcp](https://github.com/kukapay/blockbeats-mcp) 🐍 ☁️ -  An MCP server that delivers blockchain news and in-depth articles from BlockBeats for AI agents.
- [kukapay/blocknative-mcp](https://github.com/kukapay/blocknative-mcp) 🐍 ☁️ -  Providing real-time gas price predictions across multiple blockchains, powered by Blocknative.
- [kukapay/bridge-metrics-mcp](https://github.com/kukapay/bridge-metrics-mcp) 📇 ☁️ - Providing real-time cross-chain bridge metrics.
- [kukapay/bridge-rates-mcp](https://github.com/kukapay/bridge-rates-mcp) 📇 ☁️ - Delivering real-time cross-chain bridge rates and optimal transfer routes to onchain AI agents.
- [kukapay/chainlink-feeds-mcp](https://github.com/kukapay/chainlink-feeds-mcp) 📇 ☁️ -  Providing real-time access to Chainlink's decentralized on-chain price feeds.
- [kukapay/chainlist-mcp](https://github.com/kukapay/chainlist-mcp) 📇 ☁️ -  An MCP server that gives AI agents fast access to verified EVM chain information, including RPC URLs, chain IDs, explorers, and native tokens.
- [kukapay/cointelegraph-mcp](https://github.com/kukapay/cointelegraph-mcp) 🐍 ☁️ -  Providing real-time access to the latest news from Cointelegraph.
- [kukapay/crypto-feargreed-mcp](https://github.com/kukapay/crypto-feargreed-mcp) 🐍 ☁️ -  Providing real-time and historical Crypto Fear & Greed Index data.
- [kukapay/crypto-funds-mcp](https://github.com/kukapay/crypto-funds-mcp) 🐍 ☁️ -  Providing AI agents with structured, real-time data on cryptocurrency investment funds.
- [kukapay/crypto-indicators-mcp](https://github.com/kukapay/crypto-indicators-mcp) 🐍 ☁️ - An MCP server providing a range of cryptocurrency technical analysis indicators and strategie.
- [kukapay/crypto-liquidations-mcp](https://github.com/kukapay/crypto-liquidations-mcp) 🐍 ☁️ - Streams real-time cryptocurrency liquidation events from Binance.
- [kukapay/crypto-news-mcp](https://github.com/kukapay/crypto-news-mcp) 🐍 ☁️ - An MCP server that provides real-time cryptocurrency news sourced from NewsData for AI agents.
- [kukapay/crypto-orderbook-mcp](https://github.com/kukapay/crypto-orderbook-mcp) 🐍 ☁️ - Analyzing order book depth and imbalance across major crypto exchanges.
- [kukapay/crypto-pegmon-mcp](https://github.com/kukapay/crypto-pegmon-mcp) 🐍 ☁️ -  Tracking stablecoin peg integrity across multiple blockchains.
- [kukapay/crypto-portfolio-mcp](https://github.com/kukapay/crypto-portfolio-mcp) 🐍 ☁️ - An MCP server for tracking and managing cryptocurrency portfolio allocations.
- [kukapay/crypto-projects-mcp](https://github.com/kukapay/crypto-projects-mcp) 🐍 ☁️ - Providing cryptocurrency project data from Mobula.io to AI agents.
- [kukapay/crypto-rss-mcp](https://github.com/kukapay/crypto-rss-mcp) 🐍 ☁️ - An MCP server that aggregates real-time cryptocurrency news from multiple RSS feeds.
- [kukapay/crypto-sentiment-mcp](https://github.com/kukapay/crypto-sentiment-mcp) 🐍 ☁️ - An MCP server that delivers cryptocurrency sentiment analysis to AI agents.
- [kukapay/crypto-stocks-mcp](https://github.com/kukapay/crypto-stocks-mcp) 🐍 ☁️ - An MCP server that tracks real-time data for major crypto-related stocks.
- [kukapay/crypto-trending-mcp](https://github.com/kukapay/crypto-trending-mcp) 🐍 ☁️ - Tracking the latest trending tokens on CoinGecko.
- [kukapay/crypto-whitepapers-mcp](https://github.com/kukapay/crypto-whitepapers-mcp) 🐍 ☁️ - Serving as a structured knowledge base of crypto whitepapers.
- [kukapay/cryptopanic-mcp-server](https://github.com/kukapay/cryptopanic-mcp-server) 🐍 ☁️ - Providing latest cryptocurrency news to AI agents, powered by CryptoPanic.
- [kukapay/dao-proposals-mcp](https://github.com/kukapay/dao-proposals-mcp) 🐍 ☁️ - An MCP server that aggregates live governance proposals from major DAOs.
- [kukapay/defi-yields-mcp](https://github.com/kukapay/defi-yields-mcp) 🐍 ☁️ - An MCP server for AI agents to explore DeFi yield opportunities.
- [kukapay/dex-pools-mcp](https://github.com/kukapay/dex-pools-mcp) 🐍 ☁️ - An MCP server that provides AI agents with real-time access to DEX liquidity pool data.
- [kukapay/dexscreener-trending-mcp](https://github.com/kukapay/dexscreener-trending-mcp) 📇 ☁️ - Provides real-time trending tokens from DexScreener.
- [kukapay/dune-analytics-mcp](https://github.com/kukapay/dune-analytics-mcp) 🐍 ☁️ -  A mcp server that bridges Dune Analytics data to AI agents.
- [kukapay/etf-flow-mcp](https://github.com/kukapay/etf-flow-mcp) 🐍 ☁️ -  Delivering crypto ETF flow data to power AI agents' decision-making.
- [kukapay/ethereum-validator-queue-mcp](https://github.com/kukapay/ethereum-validator-queue-mcp) 🐍 ☁️ -  An MCP server that tracks Ethereum’s validator activation and exit queues in real time.
- [kukapay/freqtrade-mcp](https://github.com/kukapay/freqtrade-mcp) 🐍 ☁️ - An MCP server that integrates with the Freqtrade cryptocurrency trading bot.
- [kukapay/funding-rates-mcp](https://github.com/kukapay/funding-rates-mcp) 🐍 ☁️ - Providing real-time funding rate data across major crypto exchanges.
- [kukapay/hyperliquid-info-mcp](https://github.com/kukapay/hyperliquid-info-mcp) 🐍 ☁️ - An MCP server that provides real-time data and insights from the Hyperliquid perp DEX for use in bots, dashboards, and analytics.
- [kukapay/hyperliquid-whalealert-mcp](https://github.com/kukapay/hyperliquid-whalealert-mcp) 🐍 ☁️ - An MCP server that provides real-time whale alerts on Hyperliquid, flagging positions with a notional value exceeding $1 million.
- [kukapay/jupiter-mcp](https://github.com/kukapay/jupiter-mcp) 🐍 ☁️ - An MCP server for executing token swaps on the Solana blockchain using Jupiter's new Ultra API.
- [kukapay/pancakeswap-poolspy-mcp](https://github.com/kukapay/pancakeswap-poolspy-mcp) 🐍 ☁️ -  An MCP server that tracks newly created pools on Pancake Swap.
- [kukapay/polymarket-predictions-mcp](https://github.com/kukapay/polymarket-predictions-mcp) 🐍 ☁️ - An MCP server that delivers real-time market odds from Polymarket.
- [kukapay/pumpswap-mcp](https://github.com/kukapay/pumpswap-mcp) 🐍 ☁️ - Enabling AI agents to interact with PumpSwap for real-time token swaps and automated on-chain trading.
- [kukapay/raydium-launchlab-mcp](https://github.com/kukapay/raydium-launchlab-mcp) 🐍 ☁️ - An MCP server that enables AI agents to launch, buy, and sell tokens on the Raydium Launchpad(aka LaunchLab).
- [kukapay/rug-check-mcp](https://github.com/kukapay/rug-check-mcp) 🐍 ☁️ - An MCP server that detects potential risks in Solana meme tokens.
- [kukapay/stargate-bridge-mcp](https://github.com/kukapay/stargate-bridge-mcp) 📇 ☁️ - An MCP server that enables cross-chain token transfers via the Stargate protocol.
- [kukapay/sui-trader-mcp](https://github.com/kukapay/sui-trader-mcp) 📇 ☁️ - An MCP server designed for AI agents to perform optimal token swaps on the Sui blockchain.
- [kukapay/thegraph-mcp](https://github.com/kukapay/thegraph-mcp) 🐍 ☁️ -  An MCP server that powers AI agents with indexed blockchain data from The Graph.
- [kukapay/token-minter-mcp](https://github.com/kukapay/token-minter-mcp) 🐍 ☁️ -  An MCP server providing tools for AI agents to mint ERC-20 tokens across multiple blockchains.
- [kukapay/token-revoke-mcp](https://github.com/kukapay/token-revoke-mcp) 🐍 ☁️ - An MCP server for checking and revoking ERC-20 token allowances across multiple blockchains.
- [kukapay/twitter-username-changes-mcp](https://github.com/kukapay/twitter-username-changes-mcp) 🐍 ☁️ - An MCP server that tracks the historical changes of Twitter usernames.
- [kukapay/uniswap-poolspy-mcp](https://github.com/kukapay/uniswap-poolspy-mcp) 🐍 ☁️ -  An MCP server that tracks newly created liquidity pools on Uniswap across multiple blockchains.
- [kukapay/uniswap-price-mcp](https://github.com/kukapay/uniswap-price-mcp) 📇 ☁️ -  An MCP server that tracks newly created liquidity pools on Uniswap across multiple blockchains.
- [kukapay/uniswap-trader-mcp](https://github.com/kukapay/uniswap-trader-mcp) 🐍 ☁️ -  An MCP server that delivers real-time token prices from Uniswap V3 across multiple chains.
- [kukapay/wallet-inspector-mcp](https://github.com/kukapay/wallet-inspector-mcp) 🐍 ☁️ -  An MCP server that empowers AI agents to inspect any wallet’s balance and onchain activity across major EVM chains and Solana chain.
- [kukapay/web3-jobs-mcp](https://github.com/kukapay/web3-jobs-mcp) 🐍 ☁️ -  An MCP server that provides AI agents with real-time access to curated Web3 jobs.
- [kukapay/whale-tracker-mcp](https://github.com/kukapay/whale-tracker-mcp) 🐍 ☁️ -  A mcp server for tracking cryptocurrency whale transactions.
- [klever-io/mcp-klever-vm](https://github.com/klever-io/mcp-klever-vm) 🎖️ 📇 ☁️ - Klever blockchain MCP server for smart contract development, on-chain data exploration, account and asset queries, transaction analysis, and contract deployment tooling.
- [laukikk/alpaca-mcp](https://github.com/laukikk/alpaca-mcp) 🐍 ☁️ - An MCP Server for the Alpaca trading API to manage stock and crypto portfolios, place trades, and access market data.
- [lightningfaucet/mcp-server](https://github.com/lightningfaucet/mcp-server) 📇 ☁️ - AI Agent Bitcoin wallet with L402 payments - operators fund agents, agents make autonomous Lightning Network payments.
- [lnbits/LNbits-MCP-Server](https://github.com/lnbits/LNbits-MCP-Server) - Am MCP server for LNbits Lightning Network wallet integration.
- [logotype/fixparser](https://gitlab.com/logotype/fixparser) 🎖 📇 ☁️ 🏠 📟  - FIX Protocol (send orders, market data, etc.) written in TypeScript.
- [longportapp/openapi](https://github.com/longportapp/openapi/tree/main/mcp) - 🐍 ☁️ - LongPort OpenAPI provides real-time stock market data, provides AI access analysis and trading capabilities through MCP.
- [Mattbusel/Reddit-Options-Trader-ROT-](https://github.com/Mattbusel/Reddit-Options-Trader-ROT-) 🐍 ☁️ - The first financial intelligence MCP server. Live AI-scored trading signals from Reddit, SEC filings, FDA approvals, Congressional trades, and 15+ sources. 7 tools, 2 resources, hosted remotely, free, no API key required.
- [mcpdotdirect/evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server) 📇 ☁️ - Comprehensive blockchain services for 30+ EVM networks, supporting native tokens, ERC20, NFTs, smart contracts, transactions, and ENS resolution.
- [mcpdotdirect/starknet-mcp-server](https://github.com/mcpdotdirect/starknet-mcp-server) 📇 ☁️ - Comprehensive Starknet blockchain integration with support for native tokens (ETH, STRK), smart contracts, StarknetID resolution, and token transfers.
- [minhyeoky/mcp-server-ledger](https://github.com/minhyeoky/mcp-server-ledger) 🐍 🏠 -  A ledger-cli integration for managing financial transactions and generating reports.
- [narumiruna/yfinance-mcp](https://github.com/narumiruna/yfinance-mcp) 🐍 ☁️ - An MCP server that uses yfinance to obtain information from Yahoo Finance.
- [nckhemanth0/subscription-tracker-mcp](https://github.com/nckhemanth0/subscription-tracker-mcp) 🐍 ☁️ 🏠 - MCP server for intelligent subscription management with Gmail + MySQL integration.
- [nikicat/mcp-wallet-signer](https://github.com/nikicat/mcp-wallet-signer) 📇 🏠 - Non-custodial EVM wallet MCP — routes transactions to browser wallets (MetaMask, etc.) for signing. Private keys never leave the browser; every action requires explicit user approval via EIP-6963.
- [OctagonAI/octagon-mcp-server](https://github.com/OctagonAI/octagon-mcp-server) 🐍 ☁️ - Octagon AI Agents to integrate private and public market data
- [oerc-s/primordia](https://github.com/oerc-s/primordia) 📇 ☁️ - AI agent economic settlement. Verify receipts, emit meters (FREE). Net settlements, credit lines, audit-grade balance sheets (PAID/402).
- [olgasafonova/gleif-mcp-server](https://github.com/olgasafonova/gleif-mcp-server) 🏎️ ☁️ - Access the Global Legal Entity Identifier (LEI) database for company verification, KYC, and corporate ownership research via GLEIF's public API.
- [openMF/mcp-mifosx-self-service](https://github.com/openMF/mcp-mifosx-self-service) 🐍 ☁️  - A self-service integration for user registration, authentication, account management, transactions, and third-party transfers with Apache Fineract.
- [openMF/mcp-mifosx](https://github.com/openMF/mcp-mifosx) ☁️ 🏠 -  A core banking integration for managing clients, loans, savings, shares, financial transactions and generating financial reports.
- [polygon-io/mcp_polygon)](https://github.com/polygon-io/mcp_polygon)) 🐍 ☁️ -  An MCP server that provides access to [Polygon.io](https://polygon.io/) financial market data APIs for stocks, indices, forex, options, and more.
- [pricepertoken/mcp-server](https://pricepertoken.com/mcp) 📇 ☁️ - LLM API pricing comparison and benchmarks across 100+ models from 30+ providers including OpenAI, Anthropic, Google, and Meta. No API key required.
- [pwh-pwh/coin-mcp-server](https://github.com/pwh-pwh/coin-mcp-server) 🐍 ☁️ -  Bitget API to fetch cryptocurrency price.
- [QuantConnect/mcp-server](https://github.com/QuantConnect/mcp-server) 🐍 ☁️ – A Dockerized Python MCP server that bridges your local AI (e.g., Claude Desktop, etc) with the QuantConnect API—empowering you to create projects, backtest strategies, manage collaborators, and deploy live-trading workflows directly via natural-language prompts.
- [QuantGeekDev/coincap-mcp](https://github.com/QuantGeekDev/coincap-mcp) 📇 ☁️ - Real-time cryptocurrency market data integration using CoinCap's public API, providing access to crypto prices and market information without API keys
- [QuentinCody/braintree-mcp-server](https://github.com/QuentinCody/braintree-mcp-server) 🐍 - Unofficial PayPal Braintree payment gateway MCP Server for AI agents to process payments, manage customers, and handle transactions securely.
- [Regenerating-World/pix-mcp](https://github.com/Regenerating-World/pix-mcp) 📇 ☁️ - Generate Pix QR codes and copy-paste strings with fallback across multiple providers (Efí, Cielo, etc.) for Brazilian instant payments.
- [RomThpt/xrpl-mcp-server](https://github.com/RomThpt/mcp-xrpl) 📇 ☁️ - MCP server for the XRP Ledger that provides access to account information, transaction history, and network data. Allows querying ledger objects, submitting transactions, and monitoring the XRPL network.
- [SaintDoresh/Crypto-Trader-MCP-ClaudeDesktop](https://github.com/SaintDoresh/Crypto-Trader-MCP-ClaudeDesktop.git) 🐍 ☁️ - An MCP tool that provides cryptocurrency market data using the CoinGecko API.
- [SaintDoresh/YFinance-Trader-MCP-ClaudeDesktop](https://github.com/SaintDoresh/YFinance-Trader-MCP-ClaudeDesktop.git) 🐍 ☁️ - An MCP tool that provides stock market data and analysis using the Yahoo Finance API.
- [shareseer/shareseer-mcp-server](https://github.com/shareseer/shareseer-mcp-server) 🏎️ ☁️ - MCP to Access SEC filings, financials & insider trading data in real time using [ShareSeer](https://shareseer.com)
- [softvoyagers/fakturka-api](https://github.com/softvoyagers/fakturka-api) 📇 ☁️ - Free Polish VAT invoice generator API (Faktura VAT) with PDF output and preview. No API key required.
- [tatumio/blockchain-mcp](https://github.com/tatumio/blockchain-mcp) ☁️ - MCP server for Blockchain Data. It provides access to Tatum's blockchain API across 130+ networks with tools including RPC Gateway and Blockchain Data insights.
- [ThomasMarches/substrate-mcp-rs](https://github.com/ThomasMarches/substrate-mcp-rs) 🦀 🏠 - An MCP server implementation to interact with Substrate-based blockchains. Built with Rust and interfacing the [subxt](https://github.com/paritytech/subxt) crate.
- [tooyipjee/yahoofinance-mcp](https://github.com/tooyipjee/yahoofinance-mcp.git) 📇 ☁️ - TS version of yahoo finance mcp.
- [traceloop/opentelemetry-mcp-server](https://github.com/traceloop/opentelemetry-mcp-server.git) - 🐍🏠 - An MCP server for connecting to any OpenTelemetry backend (Datadog, Grafana, Dynatrace, Traceloop, etc.).
- [Trade-Agent/trade-agent-mcp](https://github.com/Trade-Agent/trade-agent-mcp.git) 🎖️ ☁️ - Trade stocks and crypto on common brokerages (Robinhood, E*Trade, Coinbase, Kraken) via Trade Agent's MCP server.
- [trayders/trayd-mcp](https://github.com/trayders/trayd-mcp) 🐍 ☁️ - Trade Robinhood through natural language. Portfolio analysis, real-time quotes, and order execution via Claude Code.
- [twelvedata/mcp](https://github.com/twelvedata/mcp) 🐍 ☁️ - Interact with [Twelve Data](https://twelvedata.com) APIs to access real-time and historical financial market data for your AI agents.
- [wowinter13/solscan-mcp](https://github.com/wowinter13/solscan-mcp) 🦀 🏠 - An MCP tool for querying Solana transactions using natural language with Solscan API.
- [Wuye-AI/mcp-server-wuye-ai](https://github.com/wuye-ai/mcp-server-wuye-ai) 🎖️ 📇 ☁️ - An MCP server that interact with capabilities of the CRIC Wuye AI platform, an intelligent assistant specifically for the property management industry.
- [XeroAPI/xero-mcp-server](https://github.com/XeroAPI/xero-mcp-server) 📇 ☁️ – An MCP server that integrates with Xero's API, allowing for standardized access to Xero's accounting and business features.
- [yamariki-hub/japan-corporate-mcp](https://github.com/yamariki-hub/japan-corporate-mcp) 🐍 ☁️ - Japanese corporate data via government APIs (gBizINFO, EDINET, e-Stat). Search companies, financials, patents, subsidies, procurement, and government statistics.
- [xpaysh/awesome-x402](https://github.com/xpaysh/awesome-x402) ☁️ - Curated directory of x402 payment protocol resources, MCP servers, and tools for HTTP 402-based USDC payments on Base, Arbitrum, and other EVM chains.
- [zlinzzzz/finData-mcp-server](https://github.com/zlinzzzz/finData-mcp-server) 🐍 ☁️ - An MCP server for accessing professional financial data, supporting multiple data providers such as Tushare.
- [zolo-ryan/MarketAuxMcpServer](https://github.com/Zolo-Ryan/MarketAuxMcpServer) 📇 ☁️ - MCP server for comprehensive market and financial news search with advanced filtering by symbols, industries, countries, and date ranges.

### 🎮 <a name="gaming"></a>Gaming

Integration with gaming related data, game engines, and services

- [CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity) #️⃣ 🏠 - MCP Server for Unity3d Game Engine integration for game development
- [Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp) 📇 🏠 - A MCP server for interacting with the Godot game engine, providing tools for editing, running, debugging, and managing scenes in Godot projects.
- [ddsky/gamebrain-api-clients](https://github.com/ddsky/gamebrain-api-clients) ☁️ - Search and discover hundreds of thousands of video games on any platform through the [GameBrain API](https://gamebrain.co/api).
- [hkaanengin/opendota-mcp-server](https://github.com/hkaanengin/opendota-mcp-server) 🐍 🏠 ☁️ - MCP server providing AI assistants with access to Dota 2 statistics via OpenDota API. 20+ tools for player stats, hero data, and match    analysis with natural language support.
- [IvanMurzak/Unity-MCP](https://github.com/IvanMurzak/Unity-MCP) #️⃣ 🏠 🍎 🪟 🐧 - MCP Server for Unity Editor and for a game made with Unity
- [jiayao/mcp-chess](https://github.com/jiayao/mcp-chess) 🐍 🏠 - A MCP server playing chess against LLMs.
- [kkjdaniel/bgg-mcp](https://github.com/kkjdaniel/bgg-mcp) 🏎️ ☁️ - An MCP server that enables interaction with board game related data via the BoardGameGeek API (XML API2).
- [opgginc/opgg-mcp](https://github.com/opgginc/opgg-mcp) 📇 ☁️ - Access real-time gaming data across popular titles like League of Legends, TFT, and Valorant, offering champion analytics, esports schedules, meta compositions, and character statistics.
- [pab1ito/chess-mcp](https://github.com/pab1it0/chess-mcp) 🐍 ☁️ - Access Chess.com player data, game records, and other public information through standardized MCP interfaces, allowing AI assistants to search and analyze chess information.
- [rishijatia/fantasy-pl-mcp](https://github.com/rishijatia/fantasy-pl-mcp/) 🐍 ☁️ - An MCP server for real-time Fantasy Premier League data and analysis tools.
- [sonirico/mcp-stockfish](https://github.com/sonirico/mcp-stockfish) - 🏎️ 🏠 🍎 🪟 🐧️ MCP server connecting AI systems to Stockfish chess engine.
- [stefan-xyz/mcp-server-runescape](https://github.com/stefan-xyz/mcp-server-runescape) 📇 - An MCP server with tools for interacting with RuneScape (RS) and Old School RuneScape (OSRS) data, including item prices, player hiscores, and more.
- [tomholford/mcp-tic-tac-toe](https://github.com/tomholford/mcp-tic-tac-toe) 🏎️ 🏠 - Play Tic Tac Toe against an AI opponent using this MCP server.
- [youichi-uda/godot-mcp-pro](https://github.com/youichi-uda/godot-mcp-pro) 📇 🏠 🍎 🪟 🐧 - Premium MCP server for Godot game engine with 84 tools for scene editing, scripting, animation, tilemap, shader, input simulation, and runtime debugging.

### 🏠 <a name="home-automation"></a>Home Automation

Control smart home devices, home network equipment, and automation systems.

- [kambriso/fritzbox-mcp-server](https://github.com/kambriso/fritzbox-mcp-server) 🏎️ 🏠 - Control AVM FRITZ!Box routers - manage devices, WiFi, network settings, parental controls, and schedule time-delayed actions

### 🧠 <a name="knowledge--memory"></a>Knowledge & Memory

Persistent memory storage using knowledge graph structures. Enables AI models to maintain and query structured information across sessions.

- [0xshellming/mcp-summarizer](https://github.com/0xshellming/mcp-summarizer) 📕 ☁️ - AI Summarization MCP Server, Support for multiple content types: Plain text, Web pages, PDF documents, EPUB books, HTML content
- [20alexl/mini_claude](https://github.com/20alexl/mini_claude) 🐍 🏠 - Persistent memory and guardrails for Claude Code. Features mistake tracking, loop detection, scope guard, and hooks that block risky edits. Runs locally with Ollama.
- [agentic-mcp-tools/memora](https://github.com/agentic-mcp-tools/memora) 🐍 🏠 ☁️ - Persistent memory with knowledge graph visualization, semantic/hybrid search, cloud sync (S3/R2), and cross-session context management.
- [apecloud/ApeRAG](https://github.com/apecloud/ApeRAG) 🐍 ☁️ 🏠 - Production-ready RAG platform combining Graph RAG, vector search, and full-text search. Best choice for building your own Knowledge Graph and for Context Engineering
- [bh-rat/context-awesome](https://github.com/bh-rat/context-awesome) 📇 ☁️ 🏠 - MCP server for querying 8,500+ curated awesome lists (1M+ items) and fetching the best resources for your agent.
- [bitbonsai/mcp-obsidian](https://github.com/bitbonsai/mcp-obsidian) 📇 🏠 🍎 🪟 🐧 - Universal AI bridge for Obsidian vaults using MCP. Provides safe read/write access to notes with 11 comprehensive methods for vault operations including search, batch operations, tag management, and frontmatter handling. Works with Claude, ChatGPT, and any MCP-compatible AI assistant.
- [bluzername/lennys-quotes](https://github.com/bluzername/lennys-quotes) 📇 🏠 - Query 269 episodes of Lenny's Podcast for product management wisdom. Search 51,000+ transcript segments with YouTube timestamps. Perfect for PRDs, strategy, and PM career advice.
- [cameronrye/openzim-mcp](https://github.com/cameronrye/openzim-mcp) 🐍 🏠 - Modern, secure MCP server for accessing ZIM format knowledge bases offline. Enables AI models to search and navigate Wikipedia, educational content, and other compressed knowledge archives with smart retrieval, caching, and comprehensive API.
- [CanopyHQ/phloem](https://github.com/CanopyHQ/phloem) 🏎️ 🏠 🍎 🪟 🐧 - Local-first AI memory with causal graphs and citation verification. Semantic search, confidence decay when code drifts, and zero network connections. Works across Claude Code, Cursor, VS Code, and 7 more MCP clients.
- [chatmcp/mcp-server-chatsum](https://github.com/chatmcp/mcp-server-chatsum) - Query and summarize your chat messages with AI prompts.
- [CheMiguel23/MemoryMesh](https://github.com/CheMiguel23/MemoryMesh) 📇 🏠 - Enhanced graph-based memory with a focus on AI role-play and story generation
- [contextstream/mcp-server](https://www.npmjs.com/package/@contextstream/mcp-server) 📇 ☁️ 🍎 🪟 🐧 - Universal persistent memory for AI coding tools. Semantic code search, knowledge graphs, impact analysis, decision tracking, and 60+ MCP tools. Works across Cursor, Claude Code, Windsurf, and any MCP client.
- [conversation-handoff-mcp](https://github.com/trust-delta/conversation-handoff-mcp) 📇 🏠 - Hand off conversation context between Claude Desktop projects and across MCP clients. Memory-based, no file clutter.
- [cryptosquanch/legends-mcp](https://github.com/cryptosquanch/legends-mcp) 📇 🏠 🍎 🪟 🐧 - Chat with 36 legendary founders & investors (Elon Musk, Warren Buffett, Steve Jobs, CZ). AI personas with authentic voices, frameworks, and principles. No API key required.
- [deusXmachina-dev/memorylane](https://github.com/deusXmachina-dev/memorylane) 📇 ☁️ 🏠 🍎 - Desktop app that captures screen activity via event-driven screenshots, stores AI-generated summaries and OCR text locally in SQLite, and exposes your activity history to AI assistants via MCP with semantic search, timeline browsing, and event detail retrieval.
- [dodopayments/contextmcp](https://github.com/dodopayments/context-mcp) 📇 ☁️ 🏠 - Self-hosted MCP server that indexes documentation from various sources and serves it to AI Agents with semantic search.
- [doobidoo/MCP-Context-Provider](https://github.com/doobidoo/MCP-Context-Provider) 📇 🏠 - Static server that provides persistent tool-specific context and rules for AI models
- [doobidoo/mcp-memory-service](https://github.com/doobidoo/mcp-memory-service) 📇 🏠 - Universal memory service providing semantic search, persistent storage, and autonomous memory consolidation
- [entanglr/zettelkasten-mcp](https://github.com/entanglr/zettelkasten-mcp) 🐍 🏠 - A Model Context Protocol (MCP) server that implements the Zettelkasten knowledge management methodology, allowing you to create, link, and search atomic notes through Claude and other MCP-compatible clients.
- [g1itchbot8888-del/agent-memory](https://github.com/g1itchbot8888-del/agent-memory) 🐍 🏠 - Three-layer memory system for agents (identity/active/archive) with semantic search, graph relationships, conflict detection, and LearningMachine. Built by an agent, for agents. No API keys required.
- [ErebusEnigma/context-memory](https://github.com/ErebusEnigma/context-memory) 🐍 🏠 🍎 🪟 🐧 - Persistent, searchable context storage across Claude Code sessions using SQLite FTS5. Save sessions with AI-generated summaries, two-tier full-text search, checkpoint recovery, and a web dashboard.
- [GistPad-MCP](https://github.com/lostintangent/gistpad-mcp) 📇 🏠 - Use GitHub Gists to manage and access your personal knowledge, daily notes, and reusable prompts. This acts as a companion to https://gistpad.dev and the [GistPad VS Code extension](https://aka.ms/gistpad).
- [GetCacheOverflow/CacheOverflow](https://github.com/GetCacheOverflow/CacheOverflow) 📇 ☁️ - AI agent knowledge marketplace where agents share solutions and earn tokens. Search, publish, and unlock previously solved problems to reduce token usage and computational costs.
- [graphlit-mcp-server](https://github.com/graphlit/graphlit-mcp-server) 📇 ☁️ - Ingest anything from Slack, Discord, websites, Google Drive, Linear or GitHub into a Graphlit project - and then search and retrieve relevant knowledge within an MCP client like Cursor, Windsurf or Cline.
- [hannesrudolph/mcp-ragdocs](https://github.com/hannesrudolph/mcp-ragdocs) 🐍 🏠 - An MCP server implementation that provides tools for retrieving and processing documentation through vector search, enabling AI assistants to augment their responses with relevant documentation context
- [harrison/ai-counsel](https://github.com/harrison/ai-counsel) - 🐍 🏠 🍎 🪟 🐧 - Deliberative consensus engine enabling multi-round debate between AI models with structured voting, convergence detection, and persistent decision graph memory.
- [HatmanStack/ragstack-mcp](https://github.com/HatmanStack/RAGStack-Lambda/tree/main/src/ragstack-mcp) 🐍 ☁️ 🍎 🪟 🐧 - MCP server for RAGStack serverless knowledge bases. Search, chat with AI-generated answers, upload documents/media, scrape websites, and analyze metadata through an AWS-powered RAG pipeline (Lambda, Bedrock, S3, DynamoDB).
- [hifriendbot/cogmemai-mcp](https://github.com/hifriendbot/cogmemai-mcp) 📇 ☁️ 🍎 🪟 🐧 - Persistent cognitive memory for Claude Code. Cloud-first with semantic search, AI-powered extraction, and project scoping. Zero local databases.
- [JamesANZ/cross-llm-mcp](https://github.com/JamesANZ/cross-llm-mcp) 📇 🏠 - An MCP server that enables cross-LLM communication and memory sharing, allowing different AI models to collaborate and share context across conversations.
- [JamesANZ/memory-mcp](https://github.com/JamesANZ/memory-mcp) 📇 🏠 - An MCP server that stores and retrieves memories from multiple LLMs using MongoDB. Provides tools for saving, retrieving, adding, and clearing conversation memories with timestamps and LLM identification.
- [jcdickinson/simplemem](https://github.com/jcdickinson/simplemem) 🏎️ ☁️ 🐧 - A simple memory tool for coding agents using DuckDB and VoyageAI.
- [jinzcdev/markmap-mcp-server](https://github.com/jinzcdev/markmap-mcp-server) 📇 🏠 - An MCP server built on [markmap](https://github.com/markmap/markmap) that converts **Markdown** to interactive **mind maps**. Supports multi-format exports (PNG/JPG/SVG), live browser preview, one-click Markdown copy, and dynamic visualization features.
- [kaliaboi/mcp-zotero](https://github.com/kaliaboi/mcp-zotero) 📇 ☁️ - A connector for LLMs to work with collections and sources on your Zotero Cloud
- [linxule/lotus-wisdom-mcp](https://github.com/linxule/lotus-wisdom-mcp) 📇 🏠 ☁️ - Contemplative problem-solving using the Lotus Sutra's wisdom framework. Multi-perspective reasoning with skillful means, non-dual recognition, and meditation pauses. Available as local stdio or remote Cloudflare Worker.
- [louis030195/easy-obsidian-mcp](https://github.com/louis030195/easy-obsidian-mcp) 📇 🏠 🍎 🪟 🐧 - Interact with Obsidian vaults for knowledge management. Create, read, update, and search notes. Works with local Obsidian vaults using filesystem access.
- [mattjoyce/mcp-persona-sessions](https://github.com/mattjoyce/mcp-persona-sessions) 🐍 🏠 - Enable AI assistants to conduct structured, persona-driven sessions including interview preparation, personal reflection, and coaching conversations. Built-in timer management and performance evaluation tools.
- [mem0ai/mem0-mcp](https://github.com/mem0ai/mem0-mcp) 🐍 🏠 - A Model Context Protocol server for Mem0 that helps manage coding preferences and patterns, providing tools for storing, retrieving and semantically handling code implementations, best practices and technical documentation in IDEs like Cursor and Windsurf
- [michael-denyer/memory-mcp](https://github.com/michael-denyer/memory-mcp) 🐍 🏠 🍎 🪟 🐧 - Two-tier memory with hot cache (instant injection) and cold semantic search. Auto-promotes frequently-used patterns, extracts knowledge from Claude outputs, and organizes via knowledge graph relationships.
- [mercurialsolo/counsel-mcp](https://github.com/mercurialsolo/counsel-mcp) 📇 ☁️ 🏠 🍎 🪟 🐧 - Connect AI agents to the Counsel API for strategic reasoning, multi-perspective debate analysis, and interactive advisory sessions.
- [modelcontextprotocol/server-memory](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/memory) 📇 🏠 - Knowledge graph-based persistent memory system for maintaining context
- [MWGMorningwood/Central-Memory-MCP](https://github.com/MWGMorningwood/Central-Memory-MCP) 📇 ☁️ - An Azure PaaS-hostable MCP server that provides a workspace-grounded knowledge graph for multiple developers using Azure Functions MCP triggers and Table storage.
- [MyAgentHubs/aimemo](https://github.com/MyAgentHubs/aimemo) 🏎️ 🏠 🍎 🪟 🐧 - Zero-dependency MCP memory server. Single binary, 100% local, no Docker.
- [nicholasglazer/gnosis-mcp](https://github.com/nicholasglazer/gnosis-mcp) 🐍 🏠 - Zero-config MCP server for searchable documentation. Loads markdown into SQLite (default) or PostgreSQL with FTS5/tsvector keyword search and optional pgvector hybrid semantic search.
- [nonatofabio/local-faiss-mcp](https://github.com/nonatofabio/local_faiss_mcp) 🐍 🏠 🍎 🐧 - Local FAISS vector database for RAG with document ingestion (PDF/TXT/MD/DOCX), semantic search, re-ranking, and CLI tools for indexing and querying
- [olgasafonova/mediawiki-mcp-server](https://github.com/olgasafonova/mediawiki-mcp-server) 🏎️ ☁️ 🏠 🍎 🪟 🐧 - Connect to any MediaWiki wiki (Wikipedia, Fandom, corporate wikis). 33+ tools for search, read, edit, link analysis, revision history, and Markdown conversion. Supports stdio and HTTP transport.
- [omega-memory/omega-memory](https://github.com/omega-memory/omega-memory) 🐍 🏠 🍎 🪟 🐧 - Persistent memory for AI coding agents with semantic search, auto-capture, cross-session learning, and intelligent forgetting. 12 MCP tools, local-first.
- [pallaprolus/mendeley-mcp](https://github.com/pallaprolus/mendeley-mcp) 🐍 ☁️ - MCP server for Mendeley reference manager. Search your library, browse folders, get document metadata, search the global catalog, and add papers to your collection.
- [Pantheon-Security/notebooklm-mcp-secure](https://github.com/Pantheon-Security/notebooklm-mcp-secure) 📇 🏠 🍎 🪟 🐧 - Security-hardened NotebookLM MCP with post-quantum encryption (ML-KEM-768), GDPR/SOC2/CSSF compliance, and 14 security layers. Query Google's Gemini-grounded research from Claude and AI agents.
- [pi22by7/In-Memoria](https://github.com/pi22by7/In-Memoria) 📇 🦀 🏠 🍎 🐧 🪟 - Persistent intelligence infrastructure for agentic development that gives AI coding assistants cumulative memory and pattern learning. Hybrid TypeScript/Rust implementation with local-first storage using SQLite + SurrealDB for semantic analysis and incremental codebase understanding.
- [pfillion42/memviz](https://github.com/pfillion42/memviz) 📇 🏠 🍎 🪟 🐧 - Visual explorer for [MCP Memory Service](https://github.com/doobidoo/mcp-memory-service) SQLite-vec databases. Browse, search, filter, edit memories with dashboard, timeline, UMAP projection, semantic clustering, duplicate detection, and association graph.
- [pinecone-io/assistant-mcp](https://github.com/pinecone-io/assistant-mcp) 🎖️ 🦀 ☁️ - Connects to your Pinecone Assistant and gives the agent context from its knowledge engine.
- [pomazanbohdan/memory-mcp-1file](https://github.com/pomazanbohdan/memory-mcp-1file) 🦀 🏠 🍎 🪟 🐧 - A self-contained Memory server with single-binary architecture (embedded DB & models, no dependencies). Provides persistent semantic and graph-based memory for AI agents.
- [ragieai/mcp-server](https://github.com/ragieai/ragie-mcp-server) 📇 ☁️ - Retrieve context from your [Ragie](https://www.ragie.ai) (RAG) knowledge base connected to integrations like Google Drive, Notion, JIRA and more.
- [redleaves/context-keeper](https://github.com/redleaves/context-keeper) 🏎️ 🏠 ☁️ 🍎 🪟 🐧 - LLM-driven context and memory management with wide-recall + precise-reranking RAG architecture. Features multi-dimensional retrieval (vector/timeline/knowledge graph), short/long-term memory, and complete MCP support (HTTP/WebSocket/SSE).
- [shinpr/mcp-local-rag](https://github.com/shinpr/mcp-local-rag) 📇 🏠 - Privacy-first document search server running entirely locally. Supports semantic search over PDFs, DOCX, TXT, and Markdown files with LanceDB vector storage and local embeddings - no API keys or cloud services required.
- [Smart-AI-Memory/empathy-framework](https://github.com/Smart-AI-Memory/empathy-framework) 🐍 🏠 - Five-level AI collaboration system with persistent memory and anticipatory capabilities. MCP-native integration for Claude and other LLMs with local-first architecture via MemDocs.
- [smith-and-web/obsidian-mcp-server](https://github.com/smith-and-web/obsidian-mcp-server) 📇 🏠 🍎 🪟 🐧 - SSE-enabled MCP server for remote Obsidian vault management with 29 tools for notes, directories, frontmatter, tags, search, and link operations. Docker-ready with health monitoring.
- [TechDocsStudio/biel-mcp](https://github.com/TechDocsStudio/biel-mcp) 📇 ☁️ - Let AI tools like Cursor, VS Code, or Claude Desktop answer questions using your product docs. Biel.ai provides the RAG system and MCP server.
- [tomohiro-owada/devrag](https://github.com/tomohiro-owada/devrag) 🏎️ 🏠 🍎 🪟 🐧 - Lightweight local RAG MCP server for semantic vector search over markdown documents. Reduces token consumption by 40x with sqlite-vec and multilingual-e5-small embeddings. Supports filtered search by directory and filename patterns.
- [topoteretes/cognee](https://github.com/topoteretes/cognee/tree/dev/cognee-mcp) 📇 🏠 - Memory manager for AI apps and Agents using various graph and vector stores and allowing ingestion from 30+ data sources
- [timowhite88/farnsworth-syntek](https://github.com/timowhite88/farnsworth-syntek) 📇 ☁️ - 7-layer recursive agent memory with context branching, holographic recall, dream consolidation, and on-chain persistence. MCP-native with 10 tools for persistent agent cognition.
- [topskychen/tilde](https://github.com/topskychen/tilde) 🐍 🏠 - Your AI agents' home directory — privacy-first MCP server for portable AI identity. Configure once, use everywhere. It supports profile management, skills, resume import, and team sync.
- [TeamSafeAI/LIFE](https://github.com/TeamSafeAI/LIFE) 🐍 🏠 - Persistent identity architecture for AI agents. 16 MCP servers covering drives, emotional relationships, semantic memory with decay, working threads, learned patterns, journal, genesis (identity discovery), creative collision engine, forecasting, and voice. Zero dependencies beyond Python 3.8. Built across 938 conversations.
- [unibaseio/membase-mcp](https://github.com/unibaseio/membase-mcp) 📇 ☁️ - Save and query your agent memory in distributed way by Membase
- [upstash/context7](https://github.com/upstash/context7) 📇 ☁️ - Up-to-date code documentation for LLMs and AI code editors.
- [varun29ankuS/shodh-memory](https://github.com/varun29ankuS/shodh-memory) 🦀 🏠 - Cognitive memory for AI agents with Hebbian learning, 3-tier architecture, and knowledge graphs. Single ~15MB binary, runs offline on edge devices.
- [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) 🐍 ☁️ 🏠 - Hindsight: Agent Memory That Works Like Human Memory - Built for AI Agents to manage Long Term Memory

### ⚖️ <a name="legal"></a>Legal

Access to legal information, legislation, and legal databases. Enables AI models to search and analyze legal documents and regulatory information.

- [buildsyncinc/gibs-mcp](https://github.com/buildsyncinc/gibs-mcp) 🐍 ☁️ - Regulatory compliance (AI Act, GDPR, DORA) with article-level citations
- [JamesANZ/us-legal-mcp](https://github.com/JamesANZ/us-legal-mcp) 📇 ☁️ - An MCP server that provides comprehensive US legislation.

### 🗺️ <a name="location-services"></a>Location Services

Location-based services and mapping tools. Enables AI models to work with geographic data, weather information, and location-based analytics.

- [briandconnelly/mcp-server-ipinfo](https://github.com/briandconnelly/mcp-server-ipinfo) 🐍 ☁️  - IP address geolocation and network information using IPInfo API
- [cqtrinv/trinvmcp](https://github.com/cqtrinv/trinvmcp) 📇 ☁️ - Explore French communes and cadastral parcels based on name and surface
- [devilcoder01/weather-mcp-server](https://github.com/devilcoder01/weather-mcp-server) 🐍 ☁️ - Access real-time weather data for any location using the WeatherAPI.com API, providing detailed forecasts and current conditions.
- [ip2location/mcp-ip2location-io](https://github.com/ip2location/mcp-ip2location-io) 🐍 ☁️  - Official IP2Location.io MCP server to obtain the geolocation, proxy and network information of an IP address utilizing IP2Location.io API.
- [ipfind/ipfind-mcp-server](https://github.com/ipfind/ipfind-mcp-server) 🐍 ☁️ - IP Address location service using the [IP Find](https://ipfind.com) API
- [ipfred/aiwen-mcp-server-geoip](https://github.com/ipfred/aiwen-mcp-server-geoip) 🐍 📇 ☁️ – MCP Server for the Aiwen IP Location, Get user network IP location, get IP details (country, province, city, lat, lon, ISP, owner, etc.)
- [iplocate/mcp-server-iplocate](https://github.com/iplocate/mcp-server-iplocate) 🎖️ 📇 🏠  - Look up IP address geolocation, network information, detect proxies and VPNs, and find abuse contact details using IPLocate.io
- [isdaniel/mcp_weather_server](https://github.com/isdaniel/mcp_weather_server) 🐍 ☁️ - Get weather information from https://api.open-meteo.com API.
- [jagan-shanmugam/open-streetmap-mcp](https://github.com/jagan-shanmugam/open-streetmap-mcp) 🐍 🏠 - An OpenStreetMap MCP server with location-based services and geospatial data.
- [kukapay/nearby-search-mcp](https://github.com/kukapay/nearby-search-mcp) 🐍 ☁️ - An MCP server for nearby place searches with IP-based location detection.
- [mahdin75/geoserver-mcp](https://github.com/mahdin75/geoserver-mcp) 🏠 – A Model Context Protocol (MCP) server implementation that connects LLMs to the GeoServer REST API, enabling AI assistants to interact with geospatial data and services.
- [mahdin75/gis-mcp](https://github.com/mahdin75/gis-mcp) 🏠 – A Model Context Protocol (MCP) server implementation that connects Large Language Models (LLMs) to GIS operations using GIS libraries, enabling AI assistants to perform accurate geospatial operations and transformations.
- [matbel91765/gis-mcp-server](https://github.com/matbel91765/gis-mcp-server) 🐍 🏠 🍎 🪟 🐧 - Geospatial tools for AI agents: geocoding, routing, elevation, spatial analysis, and file I/O (Shapefile, GeoJSON, GeoPackage)
- [modelcontextprotocol/server-google-maps](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/google-maps) 📇 ☁️ - Google Maps integration for location services, routing, and place details
- [QGIS MCP](https://github.com/jjsantos01/qgis_mcp) - connects QGIS Desktop to Claude AI through the MCP. This integration enables prompt-assisted project creation, layer loading, code execution, and more.
- [rossshannon/Weekly-Weather-mcp](https://github.com/rossshannon/weekly-weather-mcp.git) 🐍 ☁️ - Weekly Weather MCP server which returns 7 full days of detailed weather forecasts anywhere in the world.
- [SaintDoresh/Weather-MCP-ClaudeDesktop](https://github.com/SaintDoresh/Weather-MCP-ClaudeDesktop.git) 🐍 ☁️ - An MCP tool that provides real-time weather data, forecasts, and historical weather information using the OpenWeatherMap API.
- [SecretiveShell/MCP-timeserver](https://github.com/SecretiveShell/MCP-timeserver) 🐍 🏠 - Access the time in any timezone and get the current local time
- [stadiamaps/stadiamaps-mcp-server-ts](https://github.com/stadiamaps/stadiamaps-mcp-server-ts) 📇 ☁️ - A MCP server for Stadia Maps' Location APIs - Lookup addresses, places with geocoding, find time zones, create routes and static maps
- [TimLukaHorstmann/mcp-weather](https://github.com/TimLukaHorstmann/mcp-weather) 📇 ☁️  - Accurate weather forecasts via the AccuWeather API (free tier available).
- [trackmage/trackmage-mcp-server](https://github.com/trackmage/trackmage-mcp-server) 📇 - Shipment tracking api and logistics management capabilities through the [TrackMage API] (https://trackmage.com/)
- [webcoderz/MCP-Geo](https://github.com/webcoderz/MCP-Geo) 🐍 🏠 - Geocoding MCP server for nominatim, ArcGIS, Bing

### 🎯 <a name="marketing"></a>Marketing

Tools for creating and editing marketing content, working with web meta data, product positioning, and editing guides.

- [AdsMCP/tiktok-ads-mcp-server](https://github.com/AdsMCP/tiktok-ads-mcp-server) 🐍 ☁️ - A Model Context Protocol server for TikTok Ads API integration, enabling AI assistants to manage campaigns, analyze performance metrics, handle audiences and creatives with OAuth authentication flow.
- [alexey-pelykh/lhremote](https://github.com/alexey-pelykh/lhremote) 📇 🏠 - Open-source CLI and MCP server for LinkedHelper automation — 32 tools for campaign management, messaging, and profile queries via Chrome DevTools Protocol.
- [BlockRunAI/x-grow](https://github.com/BlockRunAI/x-grow) 📇 ☁️ - X/Twitter algorithm optimizer with post drafting, review scoring, and AI image generation for maximum engagement.
- [shensi8312/blogburst-mcp-server](https://github.com/shensi8312/blogburst-mcp-server) 📇 ☁️ - AI content generation, repurposing, and multi-platform publishing with [BlogBurst](https://blogburst.ai). Generate blogs, repurpose content for 9+ platforms (Twitter, LinkedIn, Reddit, Bluesky, Threads, Telegram, Discord, TikTok, YouTube), get trending topics, and publish directly.
- [gomarble-ai/facebook-ads-mcp-server](https://github.com/gomarble-ai/facebook-ads-mcp-server) 🐍 ☁️ - MCP server acting as an interface to the Facebook Ads, enabling programmatic access to Facebook Ads data and management features.
- [gomarble-ai/google-ads-mcp-server](https://github.com/gomarble-ai/google-ads-mcp-server) 🐍 ☁️ - MCP server acting as an interface to the Google Ads, enabling programmatic access to Google Ads data and management features.
- [louis030195/apollo-io-mcp](https://github.com/louis030195/apollo-io-mcp) 📇 ☁️ 🍎 🪟 🐧 - B2B sales intelligence and prospecting with Apollo.io. Search for prospects, enrich contacts with emails and phone numbers, discover companies by industry and size, and access Apollo's database of 275M+ contacts.
- [marketplaceadpros/amazon-ads-mcp-server](https://github.com/MarketplaceAdPros/amazon-ads-mcp-server) 📇 ☁️  - Enables tools to interact with Amazon Advertising, analyzing campaign metrics and configurations.
- [MatiousCorp/google-ad-manager-mcp](https://github.com/MatiousCorp/google-ad-manager-mcp) 🐍 ☁️ - Google Ad Manager API integration for managing campaigns, orders, line items, creatives, and advertisers with bulk upload support.
- [open-strategy-partners/osp_marketing_tools](https://github.com/open-strategy-partners/osp_marketing_tools) 🐍 🏠 - A suite of marketing tools from Open Strategy Partners including writing style, editing codes, and product marketing value map creation.
- [pipeboard-co/meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) 🐍 ☁️ 🏠 - Meta Ads automation that just works. Trusted by 10,000+ businesses to analyze performance, test creatives, optimize spend, and scale results — simply and reliably.
- [stape-io/google-tag-manager-mcp-server](https://github.com/stape-io/google-tag-manager-mcp-server) 📇 ☁️ – This server supports remote MCP connections, includes built-in Google OAuth, and provide an interface to the Google Tag Manager API.
- [stape-io/stape-mcp-server](https://github.com/stape-io/stape-mcp-server) 📇 ☁️ – This project implements an MCP (Model Context Protocol) server for the Stape platform. It allows interaction with the Stape API using AI assistants like Claude or AI-powered IDEs like Cursor.
- [tomba-io/tomba-mcp-server](https://github.com/tomba-io/tomba-mcp-server) 📇 ☁️ - Email discovery, verification, and enrichment tools. Find email addresses, verify deliverability, enrich contact data, discover authors and LinkedIn profiles, validate phone numbers, and analyze technology stacks.

### 📊 <a name="monitoring"></a>Monitoring

Access and analyze application monitoring data. Enables AI models to review error reports and performance metrics.

- [Alog/alog-mcp](https://github.com/saikiyusuke/alog-mcp) 📇 ☁️ - AI agent activity logger & monitor MCP server with 20 tools. Post logs, create articles, manage social interactions, and monitor AI agent activities on the Alog platform.
- [avivsinai/langfuse-mcp](https://github.com/avivsinai/langfuse-mcp) 🐍 ☁️ - Query Langfuse traces, debug exceptions, analyze sessions, and manage prompts. Full observability toolkit for LLM applications.
- [dynatrace-oss/dynatrace-mcp](https://github.com/dynatrace-oss/dynatrace-mcp) 🎖️ 📇 ☁️ 🍎 🪟 🐧 - Leverage AI-driven observability, security, and automation to analyze anomalies, logs, traces, events, metrics.
- [edgedelta/edgedelta-mcp-server](https://github.com/edgedelta/edgedelta-mcp-server) 🎖️ 🏎️ ☁️ – Interact with Edge Delta anomalies, query logs / patterns / events, and pinpoint root causes and optimize your pipelines.
- [ejcho623/agent-breadcrumbs](https://github.com/ejcho623/agent-breadcrumbs) 📇 ☁️ 🏠 - Unified agent work logging and observability across ChatGPT, Claude, Cursor, Codex, and OpenClaw with config-first schemas and pluggable sinks.
- [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp) 🐍 ☁️ - Sentry.io integration for error tracking and performance monitoring
- [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) 🎖️ 🐍 🏠 ☁️ - Search dashboards, investigate incidents and query datasources in your Grafana instance
- [hyperb1iss/lucidity-mcp](https://github.com/hyperb1iss/lucidity-mcp) 🐍 🏠 - Enhance AI-generated code quality through intelligent, prompt-based analysis across 10 critical dimensions from complexity to security vulnerabilities
- [imprvhub/mcp-status-observer](https://github.com/imprvhub/mcp-status-observer) 📇 ☁️ -  Model Context Protocol server for monitoring Operational Status of major digital platforms in Claude Desktop.
- [inspektor-gadget/ig-mcp-server](https://github.com/inspektor-gadget/ig-mcp-server) 🏎️ ☁️ 🏠 🐧 🪟 🍎 - Debug your Container and Kubernetes workloads with an AI interface powered by eBPF.
- [inventer-dev/mcp-internet-speed-test](https://github.com/inventer-dev/mcp-internet-speed-test) 🐍 ☁️ - Internet speed testing with network performance metrics including download/upload speed, latency, jitter analysis, and CDN server detection with geographic mapping
- [last9/last9-mcp-server](https://github.com/last9/last9-mcp-server) - Seamlessly bring real-time production context—logs, metrics, and traces—into your local environment to auto-fix code faster
- [metoro-io/metoro-mcp-server](https://github.com/metoro-io/metoro-mcp-server) 🎖️ 🏎️ ☁️ - Query and interact with kubernetes environments monitored by Metoro
- [MindscapeHQ/server-raygun](https://github.com/MindscapeHQ/mcp-server-raygun) 📇 ☁️ - Raygun API V3 integration for crash reporting and real user monitoring
- [mpeirone/zabbix-mcp-server](https://github.com/mpeirone/zabbix-mcp-server) 🐍 ☁️ 🐧 🪟 🍎 - Zabbix integration for hosts, items, triggers, templates, problems, data and more.
- [netdata/netdata#Netdata](https://github.com/netdata/netdata/blob/master/src/web/mcp/README.md) 🎖️ 🏠 ☁️ 📟 🍎 🪟 🐧 - Discovery, exploration, reporting and root cause analysis using all observability data, including metrics, logs, systems, containers, processes, and network connections
- [pydantic/logfire-mcp](https://github.com/pydantic/logfire-mcp) 🎖️ 🐍 ☁️ - Provides access to OpenTelemetry traces and metrics through Logfire
- [seekrays/mcp-monitor](https://github.com/seekrays/mcp-monitor) 🏎️ 🏠 - A system monitoring tool that exposes system metrics via the Model Context Protocol (MCP). This tool allows LLMs to retrieve real-time system information through an MCP-compatible interface.（support CPU、Memory、Disk、Network、Host、Process）
- [speedofme-dev/speedofme-mcp](https://www.npmjs.com/package/@speedofme/mcp) 📇 ☁️ 🍎 🪟 🐧 - Official SpeedOf.Me server for accurate internet speed tests via 129 global Fastly edge servers with analytics dashboard and local history
- [TANTIOPE/datadog-mcp-server](https://github.com/TANTIOPE/datadog-mcp-server) 📇 ☁️ 🍎 🪟 🐧 - MCP server providing comprehensive Datadog observability access for AI assistants. Features grep-like log search, APM trace filtering with duration/status/error queries, smart sampling modes for token efficiency, and cross-correlation between logs, traces, and metrics.
- [tumf/grafana-loki-mcp](https://github.com/tumf/grafana-loki-mcp) 🐍 🏠 - An MCP server that allows querying Loki logs through the Grafana API.
- [utapyngo/sentry-mcp-rs](https://github.com/utapyngo/sentry-mcp-rs) 🦀 ☁️ - Fast and minimal Sentry MCP server written in Rust
- [VictoriaMetrics-Community/mcp-victoriametrics](https://github.com/VictoriaMetrics-Community/mcp-victoriametrics) 🎖️ 🏎️ 🏠 - Provides comprehensive integration with your [VictoriaMetrics instance APIs](https://docs.victoriametrics.com/victoriametrics/url-examples/) and [documentation](https://docs.victoriametrics.com/) for monitoring, observability, and debugging tasks related to your VictoriaMetrics instances
- [yshngg/pmcp](https://github.com/yshngg/pmcp) 🏎️ ☁️ 🏠 🍎 🪟 🐧 - A Prometheus Model Context Protocol Server.

### 🎥 <a name="multimedia-process"></a>Multimedia Process

Provides the ability to handle multimedia, such as audio and video editing, playback, format conversion, also includes video filters, enhancements, and so on

- [1000ri-jp/atsurae](https://github.com/1000ri-jp/atsurae) 🐍 ☁️ 🍎 🪟 🐧 - AI-powered video editing MCP server with 10 tools for timeline editing, 5-layer compositing, semantic operations, and FFmpeg rendering (1920x1080, 30fps H.264+AAC).
- [AIDC-AI/Pixelle-MCP](https://github.com/AIDC-AI/Pixelle-MCP) 🐍 📇 🏠 🎥 🔊 🖼️ - An omnimodal AIGC framework that seamlessly converts ComfyUI workflows into MCP tools with zero code, enabling full-modal support for Text, Image, Sound, and Video generation with Chainlit-based web interface.
- [ananddtyagi/gif-creator-mcp](https://github.com/ananddtyagi/gif-creator-mcp/tree/main) 📇 🏠 - A MCP server for creating GIFs from your videos.
- [bogdan01m/zapcap-mcp-server](https://github.com/bogdan01m/zapcap-mcp-server) 🐍 ☁️ - MCP server for ZapCap API providing video caption and B-roll generation via natural language
- [quietnotion/barevalue-mcp](https://github.com/quietnotion/barevalue-mcp) 📇 ☁️ 🍎 🪟 🐧 - AI podcast editing as a service. Upload raw audio or submit a URL, get back edited episodes with filler words removed, noise reduction, transcripts, show notes, and social clips. Includes webhooks for automation.
- [elestirelbilinc-sketch/vap-showcase](https://github.com/elestirelbilinc-sketch/vap-showcase) 🐍 ☁️ 🍎 🪟 🐧 - AI media generation (Flux, Veo, Suno) with cost control. Pre-commit pricing, budget enforcement, reserve-burn-refund billing.
- [stass/exif-mcp](https://github.com/stass/exif-mcp) 📇 🏠 🐧 🍎 🪟 - A MCP server that allows one to examine image metadata like EXIF, XMP, JFIF and GPS.  This provides foundation for LLM-powered search and analysis of photo librares and image collections.
- [strato-space/media-gen-mcp](https://github.com/strato-space/media-gen-mcp) 📇 ☁️ 🏠 - TypeScript MCP server for OpenAI Images/Videos and Google GenAI (Veo) media generation, editing, and asset downloads.
- [sunriseapps/imagesorcery-mcp](https://github.com/sunriseapps/imagesorcery-mcp) 🐍 🏠 🐧 🍎 🪟 - ComputerVision-based 🪄 sorcery of image recognition and editing tools for AI assistants.
- [Tommertom/sonos-ts-mcp](https://github.com/Tommertom/sonos-ts-mcp) 📇 🏠 🍎 🪟 🐧 - Comprehensive Sonos audio system control through pure TypeScript implementation. Features complete device discovery, multi-room playback management, queue control, music library browsing, alarm management, real-time event subscriptions, and audio EQ settings. Includes 50+ tools for seamless smart home audio automation via UPnP/SOAP protocols.
- [torrentclaw/torrentclaw-mcp](https://github.com/torrentclaw/torrentclaw-mcp) 🎖️ 📇 ☁️ - Search and discover movies and TV shows with torrent links, quality scoring, streaming availability, and cast/crew metadata.
- [video-creator/ffmpeg-mcp](https://github.com/video-creator/ffmpeg-mcp.git) 🎥 🔊 - Using ffmpeg command line to achieve an mcp server, can be very convenient, through the dialogue to achieve the local video search, tailoring, stitching, playback and other functions
- [video-edit-mcp](https://github.com/Aditya2755/video-edit-mcp) 🐍 🏠 🍎 🪟 - Comprehensive video and audio editing MCP server with advanced operations including trimming, merging, effects, overlays, format conversion, audio processing, YouTube downloads, and smart memory management for chaining operations without intermediate files
- [TopazLabs/topaz-mcp](https://github.com/TopazLabs/topaz-mcp) 📇 ☁️ 🍎 🪟 🐧 - AI image enhancement (upscaling, denoising, sharpening) via Topaz Labs API. Supports 8 models including Standard V2, Wonder 2, Bloom, and Recover 3.

### 📋 <a name="product-management"></a>Product Management

Tools for product planning, customer feedback analysis, and prioritization.

- [dkships/pm-copilot](https://github.com/dkships/pm-copilot) 📇 ☁️ - Triangulates HelpScout support tickets and ProductLift feature requests to generate prioritized product plans. Scores themes by convergence (same signal in both sources = 2x boost), scrubs PII, and accepts business metrics from other MCP servers via `kpi_context` for composable prioritization.

### 🔬 <a name="research"></a>Research

Tools for conducting research, surveys, interviews, and data collection.

- [Embassy-of-the-Free-Mind/sourcelibrary-v2](https://github.com/Embassy-of-the-Free-Mind/sourcelibrary-v2/tree/main/mcp-server) 📇 ☁️ - Search and cite rare historical texts (alchemy, Hermeticism, Renaissance philosophy) with DOI-backed academic citations from [Source Library](https://sourcelibrary.org)
- [mnemox-ai/idea-reality-mcp](https://github.com/mnemox-ai/idea-reality-mcp) 🐍 ☁️ 🍎 🪟 🐧 - Pre-build reality check for AI coding agents. Scans GitHub and Hacker News to detect market saturation before your AI starts building, returning a reality signal score (0-100), duplicate likelihood, and similar projects.
- [ovlabs/mcp-server-originalvoices](https://github.com/ovlabs/mcp-server-originalvoices) 📇 ☁️ - Instantly understand what real users think and why by querying our network of 1:1 Digital Twins - each representing a real person. Give your AI agents authentic human context to ground outputs, improve creative, and make smarter decisions.
- [Pantheon-Security/notebooklm-mcp-secure](https://github.com/Pantheon-Security/notebooklm-mcp-secure) 📇 🏠 🍎 🪟 🐧 - Query Google NotebookLM from Claude/AI agents with 14 security hardening layers. Session-based conversations, notebook library management, and source-grounded research responses.
- [pminervini/deep-research-mcp](https://github.com/pminervini/deep-research-mcp) 🐍 ☁️ 🏠 - Deep research MCP server for OpenAI Responses API or Open Deep Research (smolagents), with web search and code interpreter support.
- [thinkchainai/agentinterviews_mcp](https://github.com/thinkchainai/agentinterviews_mcp) - Conduct AI-powered qualitative research interviews and surveys at scale with [Agent Interviews](https://agentinterviews.com). Create interviewers, manage research projects, recruit participants, and analyze interview data through MCP.

### 🔎 <a name="RAG"></a>end to end RAG platforms

- [gogabrielordonez/mcp-ragchat](https://github.com/gogabrielordonez/mcp-ragchat) 📇 🏠 - Add RAG-powered AI chat to any website with one command. Local vector store, multi-provider LLM (OpenAI/Anthropic/Gemini), self-contained chat server and embeddable widget.
- [poll-the-people/customgpt-mcp](https://github.com/Poll-The-People/customgpt-mcp) 🐍 🏠 ☁️ - An MCP server for accessing all of CustomGPT.ai's anti-hallucination RAG-as-a-service API endpoints.
- [vectara/vectara-mcp](https://github.com/vectara/vectara-mcp) 🐍 🏠 ☁️ - An MCP server for accessing Vectara's trusted RAG-as-a-service platform.

### 🔎 <a name="search"></a>Search & Data Extraction

- [0xdaef0f/job-searchoor](https://github.com/0xDAEF0F/job-searchoor) 📇 🏠 - An MCP server for searching job listings with filters for date, keywords, remote work options, and more.
- [hanselhansel/aeo-cli](https://github.com/hanselhansel/aeo-cli) 🐍 🏠 - Audit URLs for AI crawler readiness — checks robots.txt, llms.txt, JSON-LD schema, and content density with 0-100 AEO scoring.
- [Aas-ee/open-webSearch](https://github.com/Aas-ee/open-webSearch) 🐍 📇 ☁️ - Web search using free multi-engine search (NO API KEYS REQUIRED) — Supports Bing, Baidu, DuckDuckGo, Brave, Exa, and CSDN.
- [ac3xx/mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi) 📇 ☁️ - Kagi search API integration
- [adawalli/nexus](https://github.com/adawalli/nexus) 📇 ☁️ - AI-powered web search server using Perplexity Sonar models with source citations. Zero-install setup via NPX.
- [ananddtyagi/webpage-screenshot-mcp](https://github.com/ananddtyagi/webpage-screenshot-mcp) 📇 🏠 - A MCP server for taking screenshots of webpages to use as feedback during UI developement.
- [andybrandt/mcp-simple-arxiv](https://github.com/andybrandt/mcp-simple-arxiv) - 🐍 ☁️  MCP for LLM to search and read papers from arXiv
- [andybrandt/mcp-simple-pubmed](https://github.com/andybrandt/mcp-simple-pubmed) - 🐍 ☁️  MCP to search and read medical / life sciences papers from PubMed.
- [angheljf/nyt](https://github.com/angheljf/nyt) 📇 ☁️ - Search articles using the NYTimes API
- [apify/mcp-server-rag-web-browser](https://github.com/apify/mcp-server-rag-web-browser) 📇 ☁️ - An MCP server for Apify's open-source RAG Web Browser Actor to perform web searches, scrape URLs, and return content in Markdown.
- [Bigsy/Clojars-MCP-Server](https://github.com/Bigsy/Clojars-MCP-Server) 📇 ☁️ - Clojars MCP Server for upto date dependency information of Clojure libraries
- [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) ☁️ 🐍 - Search ArXiv research papers
- [boikot-xyz/boikot](https://github.com/boikot-xyz/boikot) 🦀☁️ - Model Context Protocol Server for looking up company ethics information. Learn about the ethical and unethical actions of major companies.
- [brave/brave-search-mcp-server](https://github.com/brave/brave-search-mcp-server) 📇 ☁️ - Web search capabilities using Brave's Search API
- [cameronrye/activitypub-mcp](https://github.com/cameronrye/activitypub-mcp) 📇 🏠 🐧 🍎 🪟 - A comprehensive MCP server that enables LLMs to explore and interact with the Fediverse through ActivityPub protocol. Features WebFinger discovery, timeline fetching, instance exploration, and cross-platform support for Mastodon, Pleroma, Misskey, and other ActivityPub servers.
- [cameronrye/gopher-mcp](https://github.com/cameronrye/gopher-mcp) 🐍 🏠 - Modern, cross-platform MCP server enabling AI assistants to browse and interact with both Gopher protocol and Gemini protocol resources safely and efficiently. Features dual protocol support, TLS security, and structured content extraction.
- [cevatkerim/unsplash-mcp](https://github.com/cevatkerim/unsplash-mcp) 🐍 ☁️ - Unsplash photo search with proper attribution. Returns ready-to-use attribution text and HTML for each photo, making it easy for LLMs to build content pages with properly credited images. Includes search, random photos, and download tracking.
- [chanmeng/google-news-mcp-server](https://github.com/ChanMeng666/server-google-news) 📇 ☁️ - Google News integration with automatic topic categorization, multi-language support, and comprehensive search capabilities including headlines, stories, and related topics through [SerpAPI](https://serpapi.com/).
- [chasesaurabh/mcp-page-capture](https://github.com/chasesaurabh/mcp-page-capture) 📇 🏠 - MCP server that captures webpage screenshots, with viewport or full-page options and base64 PNG output.
- [ConechoAI/openai-websearch-mcp](https://github.com/ConechoAI/openai-websearch-mcp/) 🐍 🏠 ☁️ - This is a Python-based MCP server that provides OpenAI `web_search` build-in tool.
- [ConechoAI/openai-websearch-mcp](https://github.com/ConechoAI/openai-websearch-mcp/) 🐍 🏠 ☁️ - This is a Python-based MCP server that provides OpenAI `web_search` built-in tool.
- [Crawleo/Crawleo-MCP](https://github.com/Crawleo/Crawleo-MCP) ☁️ 🐍 – Crawleo Search & Crawl API
- [Crawleo/Crawleo-MCP](https://github.com/Crawleo/Crawleo-MCP) ☁️ 🐍 – Crawleo search & Crawling API
- [czottmann/kagi-ken-mcp](https://github.com/czottmann/kagi-ken-mcp) 📇 ☁️ - Work with Kagi *without* API access (you'll need to be a customer, tho). Searches and summarizes. Uses Kagi session token for easy authentication.
- [DappierAI/dappier-mcp](https://github.com/DappierAI/dappier-mcp) 🐍 ☁️ - Enable fast, free real-time web search and access premium data from trusted media brands—news, financial markets, sports, entertainment, weather, and more. Build powerful AI agents with Dappier.
- [deadletterq/mcp-opennutrition](https://github.com/deadletterq/mcp-opennutrition) 📇 🏠 - Local MCP server for searching 300,000+ foods, nutrition facts, and barcodes from the OpenNutrition database.
- [dealx/mcp-server](https://github.com/DealExpress/mcp-server) ☁️ - MCP Server for DealX platform
- [devflowinc/trieve](https://github.com/devflowinc/trieve/tree/main/clients/mcp-server) 🎖️ 📇 ☁️ 🏠 - Crawl, embed, chunk, search, and retrieve information from datasets through [Trieve](https://trieve.ai)
- [dorukardahan/domain-search-mcp](https://github.com/dorukardahan/domain-search-mcp) 📇 ☁️ - Fast domain availability aggregator with pricing. Checks Porkbun, Namecheap, GoDaddy, RDAP & WHOIS. Includes bulk search, registrar comparison, AI-powered suggestions, and social media handle checking.
- [Dumpling-AI/mcp-server-dumplingai](https://github.com/Dumpling-AI/mcp-server-dumplingai) 🎖️ 📇 ☁️ - Access data, web scraping, and document conversion APIs by [Dumpling AI](https://www.dumplingai.com/)
- [emicklei/melrose-mcp](https://github.com/emicklei/melrose-mcp) 🏎️ 🏠 - Plays [Melrōse](https://melrōse.org) music expressions as MIDI
- [echology-io/decompose](https://github.com/echology-io/decompose) 🐍 🏠 🍎 🪟 🐧 - Decompose text into classified semantic units with authority, risk, attention scores, and entity extraction. No LLM. Deterministic. Works as MCP server or CLI.
- [erithwik/mcp-hn](https://github.com/erithwik/mcp-hn) 🐍 ☁️ - An MCP server to search Hacker News, get top stories, and more.
- [exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) 🎖️ 📇 ☁️ – A Model Context Protocol (MCP) server lets AI assistants like Claude use the Exa AI Search API for web searches. This setup allows AI models to get real-time web information in a safe and controlled way.
- [fatwang2/search1api-mcp](https://github.com/fatwang2/search1api-mcp) 📇 ☁️ - Search via search1api (requires paid API key)
- [format37/youtube_mcp](https://github.com/format37/youtube_mcp) 🐍 ☁️ – MCP server that transcribes YouTube videos to text. Uses yt-dlp to download audio and OpenAI's Whisper-1 for more precise transcription than youtube captions. Provide a YouTube URL and get back the full transcript splitted by chunks for long videos.
- [gemy411/multi-research-agents](https://github.com/gemy411/multi-agents-research) ☁️ - a KTOR server/ MCP server written in Kotlin applying multi-agents schools in a flexible research system to be used with coding or for research any general case.
- [genomoncology/biomcp](https://github.com/genomoncology/biomcp) 🐍 ☁️ - Biomedical research server providing access to PubMed, ClinicalTrials.gov, and MyVariant.info.
- [gregm711/agent-domain-service-mcp](https://github.com/gregm711/agent-domain-service-mcp) 📇 ☁️ - AI-powered domain brainstorming, analysis, and availability checking via AgentDomainService.com. Generate creative domain names from descriptions, get AI scoring for brandability/memorability, and check real-time availability with pricing. No API keys required.
- [hbg/mcp-paperswithcode](https://github.com/hbg/mcp-paperswithcode) - 🐍 ☁️ MCP to search through PapersWithCode API
- [hellokaton/unsplash-mcp-server](https://github.com/hellokaton/unsplash-mcp-server)) 🐍 ☁️ - A MCP server for Unsplash image search.
- [Himalayas-App/himalayas-mcp](https://github.com/Himalayas-App/himalayas-mcp) 📇 ☁️ - Access tens of thousands of remote job listings and company information. This public MCP server provides real-time access to Himalayas' remote jobs database.
- [Ihor-Sokoliuk/MCP-SearXNG](https://github.com/ihor-sokoliuk/mcp-searxng) 📇 🏠/☁️ - A Model Context Protocol Server for [SearXNG](https://docs.searxng.org)
- [imprvhub/mcp-claude-hackernews](https://github.com/imprvhub/mcp-claude-hackernews) 📇 🏠 ☁️ - An integration that allows Claude Desktop to interact with Hacker News using the Model Context Protocol (MCP).
- [imprvhub/mcp-domain-availability](https://github.com/imprvhub/mcp-domain-availability) 🐍 ☁️ - A Model Context Protocol (MCP) server that enables Claude Desktop to check domain availability across 50+ TLDs. Features DNS/WHOIS verification, bulk checking, and smart suggestions. Zero-clone installation via uvx.
- [imprvhub/mcp-rss-aggregator](https://github.com/imprvhub/mcp-rss-aggregator) 📇 ☁️ 🏠 - Model Context Protocol Server for aggregating RSS feeds in Claude Desktop.
- [isnow890/naver-search-mcp](https://github.com/isnow890/naver-search-mcp) 📇 ☁️ - MCP server for Naver Search API integration, supporting blog, news, shopping search and DataLab analytics features.
- [jae-jae/fetcher-mcp](https://github.com/jae-jae/fetcher-mcp) 📇 🏠 - MCP server for fetching web page content using Playwright headless browser, supporting Javascript rendering and intelligent content extraction, and outputting Markdown or HTML format.
- [jae-jae/g-search-mcp](https://github.com/jae-jae/g-search-mcp) 📇 🏠 - A powerful MCP server for Google search that enables parallel searching with multiple keywords simultaneously.
- [jhomen368/overseerr-mcp](https://github.com/jhomen368/overseerr-mcp) 📇 ☁️ 🏠 - Integrate AI assistants with Overseerr for automated media discovery, requests, and management in Plex ecosystems.
- [joelio/stocky](https://github.com/joelio/stocky) 🐍 ☁️ 🏠 - An MCP server for searching and downloading royalty-free stock photography from Pexels and Unsplash. Features multi-provider search, rich metadata, pagination support, and async performance for AI assistants to find and access high-quality images.
- [just-every/mcp-read-website-fast](https://github.com/just-every/mcp-read-website-fast) 📇 🏠 - Fast, token-efficient web content extraction for AI agents - converts websites to clean Markdown while preserving links. Features Mozilla Readability, smart caching, polite crawling with robots.txt support, and concurrent fetching.
- [just-every/mcp-screenshot-website-fast](https://github.com/just-every/mcp-screenshot-website-fast) 📇 🏠 - Fast screenshot capture tool optimized for Claude Vision API. Automatically tiles full pages into 1072x1072 chunks for optimal AI processing with configurable viewports and wait strategies for dynamic content.
- [kagisearch/kagimcp](https://github.com/kagisearch/kagimcp) ☁️ 📇 – Official Kagi Search MCP Server
- [kehvinbehvin/json-mcp-filter](https://github.com/kehvinbehvin/json-mcp-filter) ️🏠 📇 – Stop bloating your LLM context. Query & Extract only what you need from your JSON files.
- [kimdonghwi94/Web-Analyzer-MCP](https://github.com/kimdonghwi94/web-analyzer-mcp) 🐍 🏠 🍎 🪟 🐧 - Extracts clean web content for RAG and provides Q&A about web pages.
- [kshern/mcp-tavily](https://github.com/kshern/mcp-tavily.git) ☁️ 📇 – Tavily AI search API
- [leehanchung/bing-search-mcp](https://github.com/leehanchung/bing-search-mcp) 📇 ☁️ - Web search capabilities using Microsoft Bing Search API
- [lfnovo/content-core](https://github.com/lfnovo/content-core) 🐍 🏠 - Extract content from URLs, documents, videos, and audio files using intelligent auto-engine selection. Supports web pages, PDFs, Word docs, YouTube transcripts, and more with structured JSON responses.
- [Linked-API/linkedapi-mcp](https://github.com/Linked-API/linkedapi-mcp) 🎖️ 📇 ☁️ - MCP server that lets AI assistants control LinkedIn accounts and retrieve real-time data.
- [linxule/mineru-mcp](https://github.com/linxule/mineru-mcp) 📇 ☁️ - MCP server for MinerU document parsing API. Parse PDFs, images, DOCX, and PPTX with OCR (109 languages), batch processing (200 docs), page ranges, and local file upload. 73% token reduction with structured output.
- [luminati-io/brightdata-mcp](https://github.com/luminati-io/brightdata-mcp) 📇 ☁️ - Discover, extract, and interact with the web - one interface powering automated access across the public internet.
- [mikechao/brave-search-mcp](https://github.com/mikechao/brave-search-mcp) 📇 ☁️ - Web, Image, News, Video, and Local Point of Interest search capabilities using Brave's Search API
- [modelcontextprotocol/server-fetch](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/fetch) 🐍 🏠 ☁️ - Efficient web content fetching and processing for AI consumption
- [mzxrai/mcp-webresearch](https://github.com/mzxrai/mcp-webresearch) 🔍 📚 - Search Google and do deep web research on any topic
- [nickclyde/duckduckgo-mcp-server](https://github.com/nickclyde/duckduckgo-mcp-server) 🐍 ☁️ - Web search using DuckDuckGo
- [nkapila6/mcp-local-rag](https://github.com/nkapila6/mcp-local-rag) 🏠 🐍 - "primitive" RAG-like web search model context protocol (MCP) server that runs locally. No APIs needed.
- [nyxn-ai/NyxDocs](https://github.com/nyxn-ai/NyxDocs) 🐍 ☁️ 🏠 - Specialized MCP server for cryptocurrency project documentation management with multi-blockchain support (Ethereum, BSC, Polygon, Solana).
- [OctagonAI/octagon-deep-research-mcp](https://github.com/OctagonAI/octagon-deep-research-mcp) 🎖️ 📇 ☁️ 🏠 - Lightning-Fast, High-Accuracy Deep Research Agent
- [olostep/olostep-mcp-server](https://github.com/olostep/olostep-mcp-server) 📇 ☁️ - API to search, extract and structure web data. Web scraping, AI-powered answers with citations, batch processing (10k URLs), and autonomous site crawling.
- [parallel-web/search-mcp](https://github.com/parallel-web/search-mcp) ☁️ 🔎 - Highest Accuracy Web Search for AI
- [parallel-web/task-mcp](https://github.com/parallel-web/task-mcp) ☁️ 🔎 - Highest Accuracy Deep Research and Batch Tasks MCP
- [Pearch-ai/mcp_pearch](https://github.com/Pearch-ai/mcp_pearch) 🎖️ 🐍 ☁️ - Best people search engine that reduces the time spent on talent discovery
- [peter-j-thompson/semanticapi-mcp](https://github.com/peter-j-thompson/semanticapi-mcp) 🐍 ☁️ - Natural language API discovery — search 700+ API capabilities, get endpoints, auth setup, and code snippets. Supports auto-discovery of new APIs.
- [pragmar/mcp-server-webcrawl](https://github.com/pragmar/mcp-server-webcrawl) 🐍 🏠 - Advanced search and retrieval for web crawler data. Supports WARC, wget, Katana, SiteOne, and InterroBot crawlers.
- [QuentinCody/catalysishub-mcp-server](https://github.com/QuentinCody/catalysishub-mcp-server) 🐍 - Unofficial MCP server for searching and retrieving scientific data from the Catalysis Hub database, providing access to computational catalysis research and surface reaction data.
- [r-huijts/opentk-mcp](https://github.com/r-huijts/opentk-mcp) 📇 ☁️ - Access Dutch Parliament (Tweede Kamer) information including documents, debates, activities, and legislative cases through structured search capabilities (based on opentk project by Bert Hubert)
- [reading-plus-ai/mcp-server-deep-research](https://github.com/reading-plus-ai/mcp-server-deep-research) 📇 ☁️ - MCP server providing OpenAI/Perplexity-like autonomous deep research, structured query elaboration, and concise reporting.
- [ricocf/mcp-wolframalpha](https://github.com/ricocf/mcp-wolframalpha) 🐍 🏠 ☁️ - An MCP server lets AI assistants use the Wolfram Alpha API for real-time access to computational knowledge and data.
- [sascharo/gxtract](https://github.com/sascharo/gxtract) 🐍 ☁️ 🪟 🐧 🍎 - GXtract is a MCP server designed to integrate with VS Code and other compatible editors. It provides a suite of tools for interacting with the GroundX platform, enabling you to leverage its powerful document understanding capabilities directly within your development environment.
- [scrapeless-ai/scrapeless-mcp-server](https://github.com/scrapeless-ai/scrapeless-mcp-server) 🐍 ☁️ - The Scrapeless Model Context Protocol service acts as an MCP server connector to the Google SERP API, enabling web search within the MCP ecosystem without leaving it.
- [searchcraft-inc/searchcraft-mcp-server](https://github.com/searchcraft-inc/searchcraft-mcp-server) 🎖️ 📇 ☁️ - Official MCP server for managing Searchcraft clusters, creating a search index, generating an index dynamically given a data file and for easily importing data into a search index given a feed or local json file.
- [SecretiveShell/MCP-searxng](https://github.com/SecretiveShell/MCP-searxng) 🐍 🏠 - An MCP Server to connect to searXNG instances
- [serkan-ozal/driflyte-mcp-server](https://github.com/serkan-ozal/driflyte-mcp-server) 🎖️ 📇 ☁️ 🏠 - The Driflyte MCP Server exposes tools that allow AI assistants to query and retrieve topic-specific knowledge from recursively crawled and indexed web pages.
- [serpapi/serpapi-mcp](https://github.com/serpapi/serpapi-mcp) 🐍 ☁️ 🏠 🍎 🪟 🐧 - SerpApi MCP Server for Google and other search engine results. Provides multi-engine search across Google, Bing, Yahoo, DuckDuckGo, YouTube, eBay, and more with real-time weather data, stock market information, and flexible JSON response modes.
- [shopsavvy/shopsavvy-mcp-server](https://github.com/shopsavvy/shopsavvy-mcp-server) 🎖️ 📇 ☁️ - Complete product and pricing data solution for AI assistants. Search for products by barcode/ASIN/URL, access detailed product metadata, access comprehensive pricing data from thousands of retailers, view and track price history, and more.
- [softvoyagers/linkmeta-api](https://github.com/softvoyagers/linkmeta-api) 📇 ☁️ - Free URL metadata extraction API (Open Graph, Twitter Cards, favicons, JSON-LD). No API key required.
- [ssatama/rescuedogs-mcp-server](https://github.com/ssatama/rescuedogs-mcp-server) 📇 ☁️ - Search and discover rescue dogs from European and UK organizations with AI-powered personality matching and detailed profiles.
- [takashiishida/arxiv-latex-mcp](https://github.com/takashiishida/arxiv-latex-mcp) 🐍 ☁️ - Get the LaTeX source of arXiv papers to handle mathematical content and equations
- [the0807/GeekNews-MCP-Server](https://github.com/the0807/GeekNews-MCP-Server) 🐍 ☁️ - An MCP Server that retrieves and processes news data from the GeekNews site.
- [theagenttimes/tat-mcp-server](https://github.com/theagenttimes/tat-mcp-server) 🐍 ☁️ - Query articles, verified statistics, wire feed, and social tools from [The Agent Times](https://theagenttimes.com), the AI-native newspaper covering the agent economy. 13 tools including search, comments, citations, and agent leaderboards. No API key required.
- [tianqitang1/enrichr-mcp-server](https://github.com/tianqitang1/enrichr-mcp-server) 📇 ☁️ - A MCP server that provides gene set enrichment analysis using the Enrichr API
- [tinyfish-io/agentql-mcp](https://github.com/tinyfish-io/agentql-mcp) 🎖️ 📇 ☁️ - MCP server that provides [AgentQL](https://agentql.com)'s data extraction capabilities.
- [Tomatio13/mcp-server-tavily](https://github.com/Tomatio13/mcp-server-tavily) ☁️ 🐍 – Tavily AI search API
- [urlbox/urlbox-mcp-server](https://github.com/urlbox/urlbox-mcp-server/) - 📇 🏠 A reliable MCP server for generating and managing screenshots, PDFs, and videos, performing AI-powered screenshot analysis, and extracting web content (Markdown, metadata, and HTML) via the [Urlbox](https://urlbox.com) API.
- [vectorize-io/vectorize-mcp-server](https://github.com/vectorize-io/vectorize-mcp-server/) ☁️ 📇 - [Vectorize](https://vectorize.io) MCP server for advanced retrieval, Private Deep Research, Anything-to-Markdown file extraction and text chunking.
- [vitorpavinato/ncbi-mcp-server](https://github.com/vitorpavinato/ncbi-mcp-server) 🐍 ☁️ 🏠 - Comprehensive NCBI/PubMed literature search server with advanced analytics, caching, MeSH integration, related articles discovery, and batch processing for all life sciences and biomedical research.
- [webscraping-ai/webscraping-ai-mcp-server](https://github.com/webscraping-ai/webscraping-ai-mcp-server) 🎖️ 📇 ☁️ - Interact with [WebScraping.ai](https://webscraping.ai) for web data extraction and scraping.
- [webpeel/webpeel](https://github.com/webpeel/webpeel) 📇 ☁️ 🏠 - Smart web fetcher for AI agents with auto-escalation from HTTP to headless browser to stealth mode. Includes 9 MCP tools: fetch, search, crawl, map, extract, batch, screenshot, jobs, and agent. Achieved 100% success rate on a 30-URL benchmark.
- [yamanoku/baseline-mcp-server](https://github.com/yamanoku/baseline-mcp-server) 📇 🏠 - MCP server that searches Baseline status using Web Platform API
- [zhsama/duckduckgo-mcp-server](https://github.com/zhsama/duckduckgo-mcp-server/) 📇 🏠 ☁️ - This is a TypeScript-based MCP server that provides DuckDuckGo search functionality.
- [zlatkoc/youtube-summarize](https://github.com/zlatkoc/youtube-summarize) 🐍 ☁️ - MCP server that fetches YouTube video transcripts and optionally summarizes them. Supports multiple transcript formats (text, JSON, SRT, WebVTT), multi-language retrieval, and flexible YouTube URL parsing.
- [zoomeye-ai/mcp_zoomeye](https://github.com/zoomeye-ai/mcp_zoomeye) 📇 ☁️ - Querying network asset information by ZoomEye MCP Server

### 🔒 <a name="security"></a>Security

- [13bm/GhidraMCP](https://github.com/13bm/GhidraMCP) 🐍 ☕ 🏠 - MCP server for integrating Ghidra with AI assistants. This plugin enables binary analysis, providing tools for function inspection, decompilation, memory exploration, and import/export analysis via the Model Context Protocol.
- [82ch/MCP-Dandan](https://github.com/82ch/MCP-Dandan) 🐍 📇 🏠 🍎 🪟 🐧 - Real-time security framework for MCP servers that detects and blocks malicious AI agent behavior by analyzing tool call patterns and intent across multiple threat detection engines.
- [adeptus-innovatio/solvitor-mcp](https://github.com/Adeptus-Innovatio/solvitor-mcp) 🦀 🏠 - Solvitor MCP server provides tools to access reverse engineering tools that help developers extract IDL files from closed-source Solana smart contracts and decompile them.
- [agntor/mcp](https://github.com/agntor/mcp) 📇 ☁️ 🍎 🪟 🐧 - MCP audit server for agent discovery and certification. Provides trust and payment rail for AI agents including identity verification, escrow, settlement, and reputation management.
- [AIM-Intelligence/AIM-Guard-MCP](https://github.com/AIM-Intelligence/AIM-MCP) 📇 🏠 🍎 🪟 🐧 - Security-focused MCP server that provides safety guidelines and content analysis for AI agents.
- [atomicchonk/roadrecon_mcp_server](https://github.com/atomicchonk/roadrecon_mcp_server) 🐍 🪟 🏠 MCP server for analyzing ROADrecon gather results from Azure tenant enumeration
- [behrensd/mcp-firewall](https://github.com/behrensd/mcp-firewall) 📇 🏠 🍎 🪟 🐧 - Deterministic security proxy (iptables for MCP) that intercepts tool calls, enforces YAML policies, scans for secret leakage, and logs everything. No AI, no cloud.
- [BurtTheCoder/mcp-dnstwist](https://github.com/BurtTheCoder/mcp-dnstwist) 📇 🪟 ☁️ - MCP server for dnstwist, a powerful DNS fuzzing tool that helps detect typosquatting, phishing, and corporate espionage.
- [BurtTheCoder/mcp-maigret](https://github.com/BurtTheCoder/mcp-maigret) 📇 🪟 ☁️ - MCP server for maigret, a powerful OSINT tool that collects user account information from various public sources. This server provides tools for searching usernames across social networks and analyzing URLs.
- [BurtTheCoder/mcp-shodan](https://github.com/BurtTheCoder/mcp-shodan) 📇 🪟 ☁️ - MCP server for querying the Shodan API and Shodan CVEDB. This server provides tools for IP lookups, device searches, DNS lookups, vulnerability queries, CPE lookups, and more.
- [BurtTheCoder/mcp-virustotal](https://github.com/BurtTheCoder/mcp-virustotal) 📇 🪟 ☁️ - MCP server for querying the VirusTotal API. This server provides tools for scanning URLs, analyzing file hashes, and retrieving IP address reports.
- [Chimera-Protocol/csl-core](https://github.com/Chimera-Protocol/csl-core) 🐍 🏠 🍎 🪟 🐧 - Deterministic AI safety policy engine with Z3 formal verification. Write, verify, and enforce machine-verifiable constraints for AI agents via MCP.
- [co-browser/attestable-mcp-server](https://github.com/co-browser/attestable-mcp-server) 🐍 🏠 ☁️ 🐧 - An MCP server running inside a trusted execution environment (TEE) via Gramine, showcasing remote attestation using [RA-TLS](https://gramine.readthedocs.io/en/stable/attestation.html). This allows an MCP client to verify the server before conencting.
- [cyntrisec/cyntrisec-cli](https://github.com/cyntrisec/cyntrisec-cli) 🐍 🏠 - Local-first AWS security analyzer that discovers attack paths and generates remediations using graph theory.
- [dkvdm/onepassword-mcp-server](https://github.com/dkvdm/onepassword-mcp-server) - An MCP server that enables secure credential retrieval from 1Password to be used by Agentic AI.
- [firstorderai/authenticator_mcp](https://github.com/firstorderai/authenticator_mcp) 📇 🏠 🍎 🪟 🐧 – A secure MCP (Model Context Protocol) server that enables AI agents to interact with the Authenticator App.
- [forest6511/secretctl](https://github.com/forest6511/secretctl) 🏎️ 🏠 🍎 🪟 🐧 - AI-safe secrets manager with MCP integration. Run commands with credentials injected as environment variables - AI agents never see plaintext secrets. Features output sanitization, AES-256-GCM encryption, and Argon2id key derivation.
- [fosdickio/binary_ninja_mcp](https://github.com/fosdickio/binary_ninja_mcp) 🐍 🏠 🍎 🪟 🐧 - A Binary Ninja plugin, MCP server, and bridge that seamlessly integrates [Binary Ninja](https://binary.ninja) with your favorite MCP client.  It enables you to automate the process of performing binary analysis and reverse engineering.
- [fr0gger/MCP_Security](https://github.com/fr0gger/MCP_Security) 📇 ☁️ - MCP server for querying the ORKL API. This server provides tools for fetching threat reports, analyzing threat actors, and retrieving intelligence sources.
- [Gaffx/volatility-mcp](https://github.com/Gaffx/volatility-mcp) - MCP server for Volatility 3.x, allowing you to perform memory forensics analysis with AI assistant. Experience memory forensics without barriers as plugins like pslist and netscan become accessible through clean REST APIs and LLMs.
- [gbrigandi/mcp-server-cortex](https://github.com/gbrigandi/mcp-server-cortex) 🦀 🏠 🚨 🍎 🪟 🐧 - A Rust-based MCP server to integrate Cortex, enabling observable analysis and automated security responses through AI.
- [gbrigandi/mcp-server-thehive](https://github.com/gbrigandi/mcp-server-thehive) 🦀 🏠 🚨 🍎 🪟 🐧 - A Rust-based MCP server to integrate TheHive, facilitating collaborative security incident response and case management via AI.
- [gbrigandi/mcp-server-wazuh](https://github.com/gbrigandi/mcp-server-wazuh) 🦀 🏠 🚨 🍎 🪟 🐧 - A Rust-based MCP server bridging Wazuh SIEM with AI assistants, providing real-time security alerts and event data for enhanced contextual understanding.
- [girste/mcp-cybersec-watchdog](https://github.com/girste/mcp-cybersec-watchdog) 🐍 🏠 🐧 - Comprehensive Linux server security audit with 89 CIS Benchmark controls, NIST 800-53, and PCI-DSS compliance checks. Real-time monitoring with anomaly detection across 23 analyzers: firewall, SSH, fail2ban, Docker, CVE, rootkit, SSL/TLS, filesystem, network, and more.
- [gridinsoft/mcp-inspector](https://github.com/gridinsoft/mcp-inspector) 📇 ☁️ 🍎 🪟 🐧 - MCP server for domain and URL security analysis powered by GridinSoft Inspector, enabling AI agents to verify website and link safety.
- [HaroldFinchIFT/vuln-nist-mcp-server](https://github.com/HaroldFinchIFT/vuln-nist-mcp-server) 🐍 ☁️️ 🍎 🪟 🐧 - A Model Context Protocol (MCP) server for querying NIST National Vulnerability Database (NVD) API endpoints.
- [hieutran/entraid-mcp-server](https://github.com/hieuttmmo/entraid-mcp-server) 🐍 ☁️ - A MCP server for Microsoft Entra ID (Azure AD) directory, user, group, device, sign-in, and security operations via Microsoft Graph Python SDK.
- [intruder-io/intruder-mcp](https://github.com/intruder-io/intruder-mcp) 🐍 ☁️ - MCP server to access [Intruder](https://www.intruder.io/), helping you identify, understand, and fix security vulnerabilities in your infrastructure.
- [jaspertvdm/mcp-server-inject-bender](https://github.com/jaspertvdm/mcp-server-inject-bender) 🐍 ☁️ 🏠 - Security through absurdity: transforms SQL injection and XSS attempts into harmless comedy responses using AI-powered humor defense.
- [jtang613/GhidrAssistMCP](https://github.com/jtang613/GhidrAssistMCP) ☕ 🏠 - A native Model Context Protocol server for Ghidra. Includes GUI configuration and logging, 31 powerful tools and no external dependencies.
- [jyjune/mcp_vms](https://github.com/jyjune/mcp_vms) 🐍 🏠 🪟 - A Model Context Protocol (MCP) server designed to connect to a CCTV recording program (VMS) to retrieve recorded and live video streams. It also provides tools to control the VMS software, such as showing live or playback dialogs for specific channels at specified times.
- [LaurieWired/GhidraMCP](https://github.com/LaurieWired/GhidraMCP) ☕ 🏠 - A Model Context Protocol server for Ghidra that enables LLMs to autonomously reverse engineer applications. Provides tools for decompiling binaries, renaming methods and data, and listing methods, classes, imports, and exports.
- [mariocandela/beelzebub](https://github.com/mariocandela/beelzebub) ☁️ - Beelzebub is a honeypot framework that lets you build honeypot tools using MCP. Its purpose is to detect prompt injection or malicious agent behavior. The underlying idea is to provide the agent with tools it would never use in its normal work.
- [mobb-dev/mobb-vibe-shield-mcp](https://github.com/mobb-dev/bugsy?tab=readme-ov-file#model-context-protocol-mcp-server) 🎖️ 📇 ☁️ 🍎 🪟 🐧 - [Mobb Vibe Shield](https://vibe.mobb.ai/) identifies and remediates vulnerabilities in both human and AI-written code, ensuring your applications remain secure without slowing development.
- [mrexodia/ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp) 🐍 🏠 - MCP server for IDA Pro, allowing you to perform binary analysis with AI assistants. This plugin implement decompilation, disassembly and allows you to generate malware analysis reports automatically.
- [nickpending/mcp-recon](https://github.com/nickpending/mcp-recon) 🏎️ 🏠 - Conversational recon interface and MCP server powered by httpx and asnmap. Supports various reconnaissance levels for domain analysis, security header inspection, certificate analysis, and ASN lookup.
- [panther-labs/mcp-panther](https://github.com/panther-labs/mcp-panther) 🎖️ 🐍 ☁️ 🍎 - MCP server that enables security professionals to interact with Panther's SIEM platform using natural language for writing detections, querying logs, and managing alerts.
- [pullkitsan/mobsf-mcp-server](https://github.com/pullkitsan/mobsf-mcp-server) 🦀 🏠 🍎 🪟 🐧 - A MCP server for MobSF which can be used for static and dynamic analysis of Android and iOS application.
- [qianniuspace/mcp-security-audit](https://github.com/qianniuspace/mcp-security-audit) 📇 ☁️ A powerful MCP (Model Context Protocol) Server that audits npm package dependencies for security vulnerabilities. Built with remote npm registry integration for real-time security checks.
- [rad-security/mcp-server](https://github.com/rad-security/mcp-server) 📇 ☁️ - MCP server for RAD Security, providing AI-powered security insights for Kubernetes and cloud environments. This server provides tools for querying the Rad Security API and retrieving security findings, reports, runtime data and many more.
- [radareorg/r2mcp](https://github.com/radareorg/radare2-mcp) 🍎🪟🐧🏠🌊 - MCP server for Radare2 disassembler. Provides AI with capability to disassemble and look into binaries for reverse engineering.
- [roadwy/cve-search_mcp](https://github.com/roadwy/cve-search_mcp) 🐍 🏠 - A Model Context Protocol (MCP) server for querying the CVE-Search API. This server provides comprehensive access to CVE-Search, browse vendor and product、get CVE per CVE-ID、get the last updated CVEs.
- [safedep/vet](https://github.com/safedep/vet/blob/main/docs/mcp.md) 🎖️ 🏎️ ☁️ 🍎 🪟 🐧 - vet-mcp checks open source packages—like those suggested by AI coding tools—for vulnerabilities and malicious code. It supports npm and PyPI, and runs locally via Docker or as a standalone binary for fast, automated vetting.
- [samvas-codes/dawshund_mcp](https://github.com/samvas-codes/dawshund_mcp) ☁️ 🏠 - An MCP server based on dAWShund to enumerate AWS IAM data, analyze effective permissions, and visualize access relationships across users, roles, and resources. Built for cloud security engineers who want fast, easy and effective insights into AWS identity risk.
- [sanyambassi/ciphertrust-manager-mcp-server](https://github.com/sanyambassi/ciphertrust-manager-mcp-server) 🐍 ☁️ 🏠 🐧 🪟 - MCP server for Thales CipherTrust Manager integration, enabling secure key management, cryptographic operations, and compliance monitoring through AI assistants.
- [sanyambassi/thales-cdsp-cakm-mcp-server](https://github.com/sanyambassi/thales-cdsp-cakm-mcp-server) 🐍 ☁️ 🏠 🐧 🪟 - MCP server for Thales CDSP CAKM integration, enabling secure key management, cryptographic operations, and compliance monitoring through AI assistants for Ms SQL and Oracle Databases.
- [sanyambassi/thales-cdsp-crdp-mcp-server](https://github.com/sanyambassi/thales-cdsp-crdp-mcp-server) 📇 ☁️ 🏠 🐧 🪟 - MCP server for Thales CipherTrust Manager RestFul Data Protection service.
- [securityfortech/secops-mcp](https://github.com/securityfortech/secops-mcp) 🐍 🏠 - All-in-one security testing toolbox that brings together popular open source tools through a single MCP interface. Connected to an AI agent, it enables tasks like pentesting, bug bounty hunting, threat hunting, and more.
- [semgrep/mcp](https://github.com/semgrep/mcp) 📇 ☁️ Allow AI agents to scan code for security vulnerabilites using [Semgrep](https://semgrep.dev).
- [slouchd/cyberchef-api-mcp-server](https://github.com/slouchd/cyberchef-api-mcp-server) 🐍 ☁️ - MCP server for interacting with the CyberChef server API which will allow an MCP client to utilise the CyberChef operations.
- [snyk/studio-mcp](https://github.com/snyk/studio-mcp) 🎖️ 📇 ☁️ 🍎 🪟 🐧 - Embeds Snyk's security engines into agentic workflows. Secures AI-generated code in real-time and accelerates the fixing vulnerability backlogs.
- [StacklokLabs/osv-mcp](https://github.com/StacklokLabs/osv-mcp) 🏎️ ☁️ - Access the OSV (Open Source Vulnerabilities) database for vulnerability information. Query vulnerabilities by package version or commit, batch query multiple packages, and get detailed vulnerability information by ID.
- [vespo92/OPNSenseMCP](https://github.com/vespo92/OPNSenseMCP) 📇 🏠 - MCP Server for managing & interacting with Open Source NGFW OPNSense via Natural Language
- [zboralski/ida-headless-mcp](https://github.com/zboralski/ida-headless-mcp) 🏎️ 🐍 🏠 🍎 🪟 🐧 - Headless IDA Pro binary analysis via MCP. Multi-session concurrency with Go orchestration and Python workers. Supports Il2CppDumper and Blutter metadata import for Unity and Flutter reverse engineering.
- [zinja-coder/apktool-mcp-server](https://github.com/zinja-coder/apktool-mcp-server) 🐍 🏠 - APKTool MCP Server is a MCP server for the Apk Tool to provide automation in reverse engineering of Android APKs.
- [takleb3rry/zitadel-mcp](https://github.com/takleb3rry/zitadel-mcp) 📇 ☁️ 🏠 - MCP server for Zitadel identity management — manage users, projects, OIDC apps, roles, and service accounts through natural language.
- [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) ☕ 🏠 - JADX-AI-MCP is a plugin and MCP Server for the JADX decompiler that integrates directly with Model Context Protocol (MCP) to provide live reverse engineering support with LLMs like Claude.
  
### 🌐 <a name="social-media"></a>Social Media

Integration with social media platforms to allow posting, analytics, and interaction management. Enables AI-driven automation for social presence.

- [anwerj/youtube-uploader-mcp](https://github.com/anwerj/youtube-uploader-mcp) 🏎️ ☁️ - AI‑powered YouTube uploader—no CLI, no YouTube Studio. Uploade videos directly from MCP clients with all AI capabilities.
- [arjun1194/insta-mcp](https://github.com/arjun1194/insta-mcp) 📇 🏠 - Instagram MCP server for analytics and insights. Get account overviews, posts, followers, following lists, post insights, and search for users, hashtags, or places.
- [checkra1neth/xbird](https://github.com/checkra1neth/xbird-skill) 📇 ☁️ 🏠 🍎 🪟 🐧 - Twitter/X MCP server with 34 tools — post tweets, search, read timelines, manage engagement, upload media. No API keys needed, uses browser cookies. Pay per call from $0.001 via x402 micropayments.
- [gwbischof/bluesky-social-mcp](https://github.com/gwbischof/bluesky-social-mcp) 🐍 🏠 - An MCP server for interacting with Bluesky via the atproto client.
- [hiroata/meltbook-mcp-server](https://github.com/hiroata/meltbook) 📇 ☁️ - MCP server for meltbook, an AI-agent political discussion board. 50 AI agents autonomously post, vote, and debate Japanese politics. 11 tools for thread creation, posting, voting, and monitoring.
- [HagaiHen/facebook-mcp-server](https://github.com/HagaiHen/facebook-mcp-server) 🐍 ☁️ - Integrates with Facebook Pages to enable direct management of posts, comments, and engagement metrics through the Graph API for streamlined social media management.
- [karanb192/reddit-mcp-buddy](https://github.com/karanb192/reddit-mcp-buddy) 📇 🏠 - Browse Reddit posts, search content, and analyze user activity without API keys. Works out-of-the-box with Claude Desktop.
- [king-of-the-grackles/reddit-research-mcp](https://github.com/king-of-the-grackles/reddit-research-mcp) 🐍 ☁️ - AI-powered Reddit intelligence for market research and competitive analysis. Discover subreddits via semantic search across 20k+ indexed communities, fetch posts/comments with full citations, and manage research feeds. No Reddit API credentials needed.
- [kunallunia/twitter-mcp](https://github.com/LuniaKunal/mcp-twitter) 🐍 🏠 - All-in-one Twitter management solution providing timeline access, user tweet retrieval, hashtag monitoring, conversation analysis, direct messaging, sentiment analysis of a post, and complete post lifecycle control - all through a streamlined API.
- [macrocosm-os/macrocosmos-mcp](https://github.com/macrocosm-os/macrocosmos-mcp) - 🎖️ 🐍 ☁️ Access real-time X/Reddit/YouTube data directly in your LLM applications  with search phrases, users, and date filtering.
- [MarceauSolutions/fitness-influencer-mcp](https://github.com/MarceauSolutions/fitness-influencer-mcp) 🐍 🏠 ☁️ - Fitness content creator workflow automation - video editing with jump cuts, revenue analytics, and branded content creation
- [scrape-badger/scrapebadger-mcp](https://github.com/scrape-badger/scrapebadger-mcp) 🐍 ☁️ - Access Twitter/X data including user profiles, tweets, followers, trends, lists, and communities via the ScrapeBadger API.
- [sinanefeozler/reddit-summarizer-mcp](https://github.com/sinanefeozler/reddit-summarizer-mcp) 🐍 🏠 ☁️ - MCP server for summarizing users's Reddit homepage or any subreddit based on posts and comments.

### 🏃 <a name="sports"></a>Sports

Tools for accessing sports-related data, results, and statistics.

- [cloudbet/sports-mcp-server](https://github.com/cloudbet/sports-mcp-server) 🏎️ ☁️ – Access structured sports data via the Cloudbet API. Query upcoming events, live odds, stake limits, and market info across soccer, basketball, tennis, esports, and more.
- [csjoblom/musclesworked-mcp](https://github.com/csjoblom/musclesworked-mcp) 📇 ☁️ - Exercise-to-muscle mapping MCP server. Look up muscles worked by 856 exercises across 65 muscles and 14 muscle groups, analyze workouts for gaps, and find alternative exercises ranked by muscle overlap.
- [guillochon/mlb-api-mcp](https://github.com/guillochon/mlb-api-mcp) 🐍 🏠 - MCP server that acts as a proxy to the freely available MLB API, which provides player info, stats, and game information.
- [JamsusMaximus/trainingpeaks-mcp](https://github.com/JamsusMaximus/trainingpeaks-mcp) 🐍 🏠 - Query TrainingPeaks workouts, analyze CTL/ATL/TSB fitness metrics, and compare power/pace PRs through Claude Desktop.
- [khaoss85/arvo-mcp](https://github.com/khaoss85/arvo-mcp) 📇 ☁️ - AI workout coach MCP server for Arvo. Access training data, workout history, personal records, body progress, and 29 fitness tools through Claude Desktop.
- [labeveryday/nba_mcp_server](https://github.com/labeveryday/nba_mcp_server) 🐍 🏠 - Access live and historical NBA statistics including player stats, game scores, team data, and advanced analytics via Model Context Protocol
- [mikechao/balldontlie-mcp](https://github.com/mikechao/balldontlie-mcp) 📇 - MCP server that integrates balldontlie api to provide information about players, teams and games for the NBA, NFL and MLB
- [Milofax/xert-mcp](https://github.com/Milofax/xert-mcp) 📇 ☁️ - MCP server for XERT cycling analytics — access fitness signature (FTP, HIE, PP), training status, workouts, activities with XSS metrics, and MPA analysis.
- [r-huijts/firstcycling-mcp](https://github.com/r-huijts/firstcycling-mcp) 📇 ☁️ - Access cycling race data, results, and statistics through natural language. Features include retrieving start lists, race results, and rider information from firstcycling.com.
- [r-huijts/strava-mcp](https://github.com/r-huijts/strava-mcp) 📇 ☁️ - A Model Context Protocol (MCP) server that connects to Strava API, providing tools to access Strava data through LLMs
- [RobSpectre/mvf1](https://github.com/RobSpectre/mvf1) 🐍 ☁️ - MCP server that controls [MultiViewer](https://multiviewer.app), an app for watching motorsports like Formula 1, World Endurance Championship, IndyCar and others.
- [willvelida/mcp-afl-server](https://github.com/willvelida/mcp-afl-server) ☁️ - MCP server that integrates with the Squiggle API to provide information on Australian Football League teams, ladder standings, results, tips, and power rankings.


### 🎧 <a name="support-and-service-management"></a>Support & Service Management

Tools for managing customer support, IT service management, and helpdesk operations.

- [aikts/yandex-tracker-mcp](https://github.com/aikts/yandex-tracker-mcp) 🐍 ☁️ 🏠 - MCP Server for Yandex Tracker. Provides tools for searching and retrieving information about issues, queues, users.
- [Berckan/bugherd-mcp](https://github.com/Berckan/bugherd-mcp) 📇 ☁️ - MCP server for BugHerd bug tracking. List projects, view tasks with filtering by status/priority/tags, get task details, and read comments.
- [effytech/freshdesk-mcp](https://github.com/effytech/freshdesk_mcp) 🐍 ☁️ - MCP server that integrates with Freshdesk, enabling AI models to interact with Freshdesk modules and perform various support operations.
- [incentivai/quickchat-ai-mcp](https://github.com/incentivai/quickchat-ai-mcp) 🐍 🏠 ☁️ - Launch your conversational Quickchat AI agent as an MCP to give AI apps real-time access to its Knowledge Base and conversational capabilities.
- [nguyenvanduocit/jira-mcp](https://github.com/nguyenvanduocit/jira-mcp) 🏎️ ☁️ - A Go-based MCP connector for Jira that enables AI assistants like Claude to interact with Atlassian Jira. This tool provides a seamless interface for AI models to perform common Jira operations including issue management, sprint planning, and workflow transitions.
- [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) 🐍 ☁️ - MCP server for Atlassian products (Confluence and Jira). Supports Confluence Cloud, Jira Cloud, and Jira Server/Data Center. Provides comprehensive tools for searching, reading, creating, and managing content across Atlassian workspaces.
- [tom28881/mcp-jira-server](https://github.com/tom28881/mcp-jira-server) 📇 ☁️ 🏠 - Comprehensive TypeScript MCP server for Jira with 20+ tools covering complete project management workflow: issue CRUD, sprint management, comments/history, attachments, batch operations.

### 🌎 <a name="translation-services"></a>Translation Services

Translation tools and services to enable AI assistants to translate content between different languages.

- [mmntm/weblate-mcp](https://github.com/mmntm/weblate-mcp) 📇 ☁️ - Comprehensive Model Context Protocol server for Weblate translation management, enabling AI assistants to perform translation tasks, project management, and content discovery with smart format transformations.
- [shuji-bonji/xcomet-mcp-server](https://github.com/shuji-bonji/xcomet-mcp-server) 📇 🏠 - Translation quality evaluation using xCOMET models. Provides quality scoring (0-1), error detection with severity levels (minor/major/critical), and optimized batch processing with 25x speedup.
- [translated/lara-mcp](https://github.com/translated/lara-mcp) 🎖️ 📇 ☁️ - MCP Server for Lara Translate API, enabling powerful translation capabilities with support for language detection and context-aware translations.

### 🎧 <a name="text-to-speech"></a>Text-to-Speech

Tools for converting text-to-speech and vice-versa

- [daisys-ai/daisys-mcp](https://github.com/daisys-ai/daisys-mcp) 🐍 🏠 🍎 🪟 🐧 - Generate high-quality text-to-speech and text-to-voice outputs using the [DAISYS](https://www.daisys.ai/) platform and make it able to play and store audio generated.
- [mbailey/voice-mcp](https://github.com/mbailey/voice-mcp) 🐍 🏠 - Complete voice interaction server supporting speech-to-text, text-to-speech, and real-time voice conversations through local microphone, OpenAI-compatible APIs, and LiveKit integration
- [mberg/kokoro-tts-mcp](https://github.com/mberg/kokoro-tts-mcp) 🐍 🏠 - MCP Server that uses the open weight Kokoro TTS models to convert text-to-speech. Can convert text to MP3 on a local driver or auto-upload to an S3 bucket.
- [transcribe-app/mcp-transcribe](https://github.com/transcribe-app/mcp-transcribe) 📇 🏠 - This service provides fast and reliable transcriptions for audio/video files and voice memos. It allows LLMs to interact with the text content of audio/video file.
- [ybouhjira/claude-code-tts](https://github.com/ybouhjira/claude-code-tts) 🏎️ ☁️ 🍎 🪟 🐧 - MCP server plugin for Claude Code that converts text to speech using OpenAI's TTS API. Features 6 voices, worker pool architecture, mutex-protected playback, and cross-platform support.

### 🚆 <a name="travel-and-transportation"></a>Travel & Transportation

Access to travel and transportation information. Enables querying schedules, routes, and real-time travel data.

- [campertunity/mcp-server](https://github.com/campertunity/mcp-server) 🎖️ 📇 🏠 - Search campgrounds around the world on campertunity, check availability, and provide booking links
- [cobanov/teslamate-mcp](https://github.com/cobanov/teslamate-mcp) 🐍 🏠 - A Model Context Protocol (MCP) server that provides access to your TeslaMate database, allowing AI assistants to query Tesla vehicle data and analytics.
- [helpful-AIs/triplyfy-mcp](https://github.com/helpful-AIs/triplyfy-mcp) 📇 ☁️ - An MCP server that lets LLMs plan and manage itineraries with interactive maps in Triplyfy; manage itineraries, places and notes, and search/save flights.
- [KyrieTangSheng/mcp-server-nationalparks](https://github.com/KyrieTangSheng/mcp-server-nationalparks) 📇 ☁️ - National Park Service API integration providing latest information of park details, alerts, visitor centers, campgrounds, and events for U.S. National Parks
- [lucygoodchild/mcp-national-rail](https://github.com/lucygoodchild/mcp-national-rail) 📇 ☁️ - An MCP server for UK National Rail trains service, providing train schedules and live travel information, intergrating the Realtime Trains API
- [MarceauSolutions/rideshare-comparison-mcp](https://github.com/MarceauSolutions/rideshare-comparison-mcp) 🐍 ☁️ - Compare Uber and Lyft prices for any route in real-time with fare estimates, surge pricing info, and cheapest option recommendations
- [openbnb-org/mcp-server-airbnb](https://github.com/openbnb-org/mcp-server-airbnb) 📇 ☁️ - Provides tools to search Airbnb and get listing details.
- [pab1it0/tripadvisor-mcp](https://github.com/pab1it0/tripadvisor-mcp) 📇 🐍 - A MCP server that enables LLMs to interact with Tripadvisor API, supporting location data, reviews, and photos through standardized MCP interfaces
- [Pradumnasaraf/aviationstack-mcp](https://github.com/Pradumnasaraf/aviationstack-mcp) 🐍 ☁️ 🍎 🪟 🐧 - An MCP server using the AviationStack API to fetch real-time flight data including airline flights, airport schedules, future flights and aircraft types.
- [r-huijts/ns-mcp-server](https://github.com/r-huijts/ns-mcp-server) 📇 ☁️ - Access Dutch Railways (NS) travel information, schedules, and real-time updates
- [skedgo/tripgo-mcp-server](https://github.com/skedgo/tripgo-mcp-server) 📇 ☁️ - Provides tools from the TripGo API for multi-modal trip planning, transport locations, and public transport departures, including real-time information.
- [srinath1510/alltrails-mcp-server](https://github.com/srinath1510/alltrails-mcp-server) 🐍 ☁️ - A MCP server that provides access to AllTrails data, allowing you to search for hiking trails and get detailed trail information

### 🔄 <a name="version-control"></a>Version Control

Interact with Git repositories and version control platforms. Enables repository management, code analysis, pull request handling, issue tracking, and other version control operations through standardized APIs.

- [adhikasp/mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest) 🐍 🏠 - Read and analyze GitHub repositories with your LLM
- [ddukbg/github-enterprise-mcp](https://github.com/ddukbg/github-enterprise-mcp) 📇 ☁️ 🏠 - MCP server for GitHub Enterprise API integration
- [gitea/gitea-mcp](https://gitea.com/gitea/gitea-mcp) 🎖️ 🏎️ ☁️ 🏠 🍎 🪟 🐧 - Interactive with Gitea instances with MCP.
- [github/github-mcp-server](https://github.com/github/github-mcp-server) 📇 ☁️ - Official GitHub server for integration with repository management, PRs, issues, and more.
- [JaviMaligno/mcp-server-bitbucket](https://github.com/JaviMaligno/mcp-server-bitbucket) 🐍 ☁️ - Bitbucket MCP server with 58 tools for repository management, PRs, pipelines, branches, commits, deployments, webhooks, tags, branch restrictions, and source browsing.
- [JaviMaligno/mcp-server-bitbucket](https://github.com/JaviMaligno/mcp-server-bitbucket) 🐍 ☁️ - Bitbucket MCP server with 58 tools for repository management, pull requests, pipelines, branches, commits, deployments, webhooks, tags, branch restrictions, and source browsing.
- [kaiyuanxiaobing/atomgit-mcp-server](https://github.com/kaiyuanxiaobing/atomgit-mcp-server) 📇 ☁️ - Official AtomGit server for integration with repository management, PRs, issues, branches, labels, and more.
- [kopfrechner/gitlab-mr-mcp](https://github.com/kopfrechner/gitlab-mr-mcp) 📇 ☁️ - Interact seamlessly with issues and merge requests of your GitLab projects.
- [modelcontextprotocol/server-git](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/git) 🐍 🏠 - Direct Git repository operations including reading, searching, and analyzing local repositories
- [modelcontextprotocol/server-gitlab](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/gitlab) 📇 ☁️ 🏠 - GitLab platform integration for project management and CI/CD operations
- [QuentinCody/github-graphql-mcp-server](https://github.com/QuentinCody/github-graphql-mcp-server) 🐍 ☁️ - Unofficial GitHub MCP server that provides access to GitHub's GraphQL API, enabling more powerful and flexible queries for repository data, issues, pull requests, and other GitHub resources.
- [raohwork/forgejo-mcp](https://github.com/raohwork/forgejo-mcp) 🏎️ ☁️ - An MCP server for managing your repositories on Forgejo/Gitea server.
- [TamiShaks-2/git-context-mcp](https://github.com/TamiShaks-2/git-context-mcp) 🐍 🏠 - Local MCP server that provides structured Git repository analysis (project status, recent activity, code map, and risk hotspots) for AI coding agents.
- [theonedev/tod](https://github.com/theonedev/tod/blob/main/mcp.md) 🏎️ 🏠 - A MCP server for OneDev for CI/CD pipeline editing, issue workflow automation, and pull request review
- [Tiberriver256/mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops) 📇 ☁️ - Azure DevOps integration for repository management, work items, and pipelines.

### 🏢 <a name="workplace-and-productivity"></a>Workplace & Productivity

- [bivex/kanboard-mcp](https://github.com/bivex/kanboard-mcp) 🏎️ ☁️ 🏠 - A Model Context Protocol (MCP) server written in Go that empowers AI agents and Large Language Models (LLMs) to seamlessly interact with Kanboard. It transforms natural language commands into Kanboard API calls, enabling intelligent automation of project, task, and user management, streamlining workflows, and enhancing productivity.
- [bug-breeder/quip-mcp](https://github.com/bug-breeder/quip-mcp) 📇 ☁️ 🍎 🪟 🐧 - A Model Context Protocol (MCP) server providing AI assistants with comprehensive Quip document access and management. Enables document lifecycle management, smart search, comment management, and secure token-based authentication for both Quip.com and enterprise instances.
- [devroopsaha744/TexMCP](https://github.com/devroopsaha744/TexMCP) 🐍 🏠 - An MCP server that converts LaTeX into high-quality PDF documents. It provides tools for rendering both raw LaTeX input and customizable templates, producing shareable, production-ready artifacts such as reports, resumes, and research papers.
- [foxintheloop/UpTier](https://github.com/foxintheloop/UpTier) 📇 🏠 🪟 - Desktop task manager with clean To Do-style UI and 25+ MCP tools for prioritization, goal tracking, and multi-profile workflows.
- [giuseppe-coco/Google-Workspace-MCP-Server](https://github.com/giuseppe-coco/Google-Workspace-MCP-Server) 🐍 ☁️ 🍎 🪟 🐧 - MCP server that seamlessly interacts with your Google Calendar, Gmail, Drive and so on.
- [nicolascroce/keepsake-mcp](https://github.com/nicolascroce/keepsake-mcp) 📇 ☁️ - Personal CRM — manage contacts, interactions, tasks, notes, daily journal, and tags through 42 MCP tools
- [khaoss85/mcp-orchestro](https://github.com/khaoss85/mcp-orchestro) 📇 ☁️ 🍎 🪟 🐧 - Trello for Claude Code: AI-powered task management with 60 MCP tools, visual Kanban board, and intelligent orchestration for product teams and developers.
- [louis030195/toggl-mcp](https://github.com/louis030195/toggl-mcp) 📇 ☁️ 🍎 🪟 🐧 - Time tracking integration with Toggl Track. Start/stop timers, manage time entries, track project time, and get today's summary. Perfect for productivity tracking and billing workflows.
- [MarceauSolutions/amazon-seller-mcp](https://github.com/MarceauSolutions/amazon-seller-mcp) 🐍 ☁️ - Amazon Seller Central operations via SP-API - manage inventory, track orders, analyze sales, and optimize listings
- [MarceauSolutions/hvac-quotes-mcp](https://github.com/MarceauSolutions/hvac-quotes-mcp) 🐍 🏠 ☁️ - HVAC equipment RFQ management for contractors - submit quotes to distributors, track responses, and compare pricing
- [MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite) 🐍 ☁️ - Integration with gmail and Google Calendar.
- [moro3k/mcp-altegio](https://github.com/moro3k/mcp-altegio) 📇 ☁️ - MCP server for Altegio API — appointments, clients, services, staff schedules for salon/spa/clinic management. 18 tools with Docker support.
- [SparkSheets/sparksheets-mcp](https://github.com/saikiyusuke/sparksheets-mcp) 📇 ☁️ - AI-native collaborative spreadsheet MCP server for session management, knowledge base, task tracking, and sheet operations. Integrates with Claude Code, Cursor, and Cline.
- [takumi0706/google-calendar-mcp](https://github.com/takumi0706/google-calendar-mcp) 📇 ☁️ - An MCP server to interface with the Google Calendar API. Based on TypeScript.
- [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) 🐍 ☁️ 🍎 🪟 🐧 - Comprehensive Google Workspace MCP server with full support for Google Calendar, Drive, Gmail, and Docs, Forms, Chats, Slides and Sheets over stdio, Streamable HTTP and SSE transports.
- [teamwork/mcp](https://github.com/teamwork/mcp) 🎖️ 🏎️ ☁️ 🍎 🪟 🐧 - Project and resource management platform that keeps your client projects on track, makes managing resources a breeze, and keeps your profits on point.
- [tubasasakunn/context-apps-mcp](https://github.com/tubasasakunn/context-apps-mcp) 📇 🏠 🍎 🪟 🐧 - AI-powered productivity suite connecting Todo, Idea, Journal, and Timer apps with Claude via Model Context Protocol.
- [universalamateur/reclaim-mcp-server](https://github.com/universalamateur/reclaim-mcp-server) 🐍 ☁️ - Reclaim.ai calendar integration with 40 tools for tasks, habits, focus time, scheduling links, and productivity analytics.
- [vakharwalad23/google-mcp](https://github.com/vakharwalad23/google-mcp) 📇 ☁️ - Collection of Google-native tools (Gmail, Calendar, Drive, Tasks) for MCP with OAuth management, automated token refresh, and auto re-authentication capabilities.
- [vasylenko/claude-desktop-extension-bear-notes](https://github.com/vasylenko/claude-desktop-extension-bear-notes) 📇 🏠 🍎 - Search, read, create, and update Bear Notes directly from Claude. Local-only with complete privacy.
- [wyattjoh/calendar-mcp](https://github.com/wyattjoh/calendar-mcp) 📇 🏠 🍎 - MCP server for accessing macOS Calendar events
- [yuvalsuede/claudia](https://github.com/yuvalsuede/claudia) 📇 🏠 🍎 🪟 🐧 - AI-native task management system for Claude agents. Hierarchical tasks, dependencies, sprints, acceptance criteria, multi-agent coordination, and MCP server integration.

### 🛠️ <a name="other-tools-and-integrations"></a>Other Tools and Integrations

- [2niuhe/plantuml_web](https://github.com/2niuhe/plantuml_web) 🐍 🏠 ☁️ 🍎 🪟 🐧 - A web-based PlantUML frontend with MCP server integration, enable plantuml image generation and plantuml syntax validation.
- [2niuhe/qrcode_mcp](https://github.com/2niuhe/qrcode_mcp) 🐍 🏠 🍎 🪟 🐧 - A QR code generation MCP server that converts any text (including Chinese characters) to QR codes with customizable colors and base64 encoding output.
- [AbdelStark/bitcoin-mcp](https://github.com/AbdelStark/bitcoin-mcp) - ₿ A Model Context Protocol (MCP) server that enables AI models to interact with Bitcoin, allowing them to generate keys, validate addresses, decode transactions, query the blockchain, and more.
- [akseyh/bear-mcp-server](https://github.com/akseyh/bear-mcp-server) - Allows the AI to read from your Bear Notes (macOS only)
- [allenporter/mcp-server-home-assistant](https://github.com/allenporter/mcp-server-home-assistant) 🐍 🏠 - Expose all Home Assistant voice intents through a Model Context Protocol Server allowing home control.
- [altinoren/utopia](https://github.com/altinoren/Utopia) #️⃣ 🏠 - MCP that simulates a set of smart home and lifestyle devices, allowing you to test agent's reasoning and discovery capabilities.
- [Amazon Bedrock Nova Canvas](https://github.com/zxkane/mcp-server-amazon-bedrock) 📇 ☁️ - Use Amazon Nova Canvas model for image generation.
- [amidabuddha/unichat-mcp-server](https://github.com/amidabuddha/unichat-mcp-server) 🐍/📇 ☁️ - Send requests to OpenAI, MistralAI, Anthropic, xAI, Google AI or DeepSeek using MCP protocol via tool or predefined prompts. Vendor API key required
- [anaisbetts/mcp-installer](https://github.com/anaisbetts/mcp-installer) 🐍 🏠 -  An MCP server that installs other MCP servers for you.
- [anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube) 📇 ☁️ - Fetch YouTube subtitles
- [andybrandt/mcp-simple-openai-assistant](https://github.com/andybrandt/mcp-simple-openai-assistant) - 🐍 ☁️  MCP to talk to OpenAI assistants (Claude can use any GPT model as his assitant)
- [andybrandt/mcp-simple-timeserver](https://github.com/andybrandt/mcp-simple-timeserver) 🐍 🏠☁️ - An MCP server that allows checking local time on the client machine or current UTC time from an NTP server
- [anki-mcp/anki-mcp-desktop](https://github.com/anki-mcp/anki-mcp-desktop) 📇 🏠 🍎 🪟 🐧 - Enterprise-grade Anki integration with natural language interaction, comprehensive note/deck management, and one-click MCPB installation. Built on NestJS with comprehensive test coverage.
- [ankitmalik84/notion-mcp-server](https://github.com/ankitmalik84/Agentic_Longterm_Memory/tree/main/src/notion_mcp_server) 🐍 ☁️ - A comprehensive Model Context Protocol (MCP) server for Notion integration with enhanced functionality, robust error handling, production-ready feature.
- [apify/actors-mcp-server](https://github.com/apify/actors-mcp-server) 📇 ☁️ - Use 3,000+ pre-built cloud tools, known as Actors, to extract data from websites, e-commerce, social media, search engines, maps, and more
- [apinetwork/piapi-mcp-server](https://github.com/apinetwork/piapi-mcp-server) 📇 ☁️ PiAPI MCP server makes users able to generate media content with Midjourney/Flux/Kling/Hunyuan/Udio/Trellis directly from Claude or any other MCP-compatible apps.
- [awkoy/replicate-flux-mcp](https://github.com/awkoy/replicate-flux-mcp) 📇 ☁️ - Provides the ability to generate images via Replicate's API.
- [awwaiid/mcp-server-taskwarrior](https://github.com/awwaiid/mcp-server-taskwarrior) 🏠 📇 - An MCP server for basic local taskwarrior usage (add, update, remove tasks)
- [Azure/azure-mcp](https://github.com/Azure/azure-mcp) - Official Microsoft MCP server for Azure services including Storage, Cosmos DB, and Azure Monitor.
- [Badhansen/notion-mcp](https://github.com/Badhansen/notion-mcp) 🐍 ☁️ - A Model Context Protocol (MCP) server that integrates with Notion's API to manage personal todo lists efficiently.
- [bart6114/my-bear-mcp-server](https://github.com/bart6114/my-bear-mcp-server/) 📇 🏠 🍎 - Allows to read notes and tags for the Bear Note taking app, through a direct integration with Bear's sqlitedb.
- [billster45/mcp-chatgpt-responses](https://github.com/billster45/mcp-chatgpt-responses) 🐍 ☁️ - MCP server for Claude to talk to ChatGPT and use its web search capability.
- [blurrah/mcp-graphql](https://github.com/blurrah/mcp-graphql) 📇 ☁️ - Allows the AI to query GraphQL servers
- [boldsign/boldsign-mcp](https://github.com/boldsign/boldsign-mcp) 📇 ☁️ - Search, request, and manage e-signature contracts effortlessly with [BoldSign](https://boldsign.com/).
- [brianxiadong/ones-wiki-mcp-server](https://github.com/brianxiadong/ones-wiki-mcp-server) ☕ ☁️/🏠 - A Spring AI MCP-based service for retrieving ONES Waiki content and converting it to AI-friendly text format.
- [calclavia/mcp-obsidian](https://github.com/calclavia/mcp-obsidian) 📇 🏠 - This is a connector to allow Claude Desktop (or any MCP client) to read and search any directory containing Markdown notes (such as an Obsidian vault).
- [caol64/wenyan-mcp](https://github.com/caol64/wenyan-mcp) 📇 🏠 🍎 🪟 🐧 - Wenyan MCP Server, which lets AI automatically format Markdown articles and publish them to WeChat GZH.
- [chrishayuk/mcp-cli](https://github.com/chrishayuk/mcp-cli) 🐍 🏠 - Yet another CLI tool for testing MCP servers
- [danhilse/notion_mcp](https://github.com/danhilse/notion_mcp) 🐍 ☁️ - Integrates with Notion's API to manage personal todo lists
- [danielkennedy1/pdf-tools-mcp](https://github.com/danielkennedy1/pdf-tools-mcp) 🐍 - PDF download, view & manipulation utilities.
- [dev-mirzabicer/ticktick-sdk](https://github.com/dev-mirzabicer/ticktick-sdk) 🐍 ☁️ - Comprehensive async Python SDK for [TickTick](https://ticktick.com/) with MCP server support. Features 45 tools for tasks, projects, tags, habits, focus/pomodoro sessions, and user analytics.
- [disco-trooper/apple-notes-mcp](https://github.com/disco-trooper/apple-notes-mcp) 📇 🏠 🍎 - Apple Notes MCP with semantic search, hybrid vector+keyword search, full CRUD operations, and incremental indexing. Uses JXA for native macOS integration.
- [dotemacs/domain-lookup-mcp](https://github.com/dotemacs/domain-lookup-mcp) 🏎️ - Domain name lookup service, first via [RDAP](https://en.wikipedia.org/wiki/Registration_Data_Access_Protocol) and then as a fallback via [WHOIS](https://en.wikipedia.org/wiki/WHOIS)
- [ekkyarmandi/ticktick-mcp](https://github.com/ekkyarmandi/ticktick-mcp) 🐍 ☁️ - [TickTick](https://ticktick.com/) MCP server that integrates with TickTick's API to manage personal todo projects and the tasks.
- [emicklei/mcp-log-proxy](https://github.com/emicklei/mcp-log-proxy) 🏎️ 🏠 - MCP server proxy that offers a Web UI to the full message flow
- [esignaturescom/mcp-server-esignatures](https://github.com/esignaturescom/mcp-server-esignatures) 🐍 ☁️️ - Contract and template management for drafting, reviewing, and sending binding contracts via the eSignatures API.
- [evalstate/mcp-hfspace](https://github.com/evalstate/mcp-hfspace) 📇 ☁️ - Use HuggingFace Spaces directly from Claude. Use Open Source Image Generation, Chat, Vision tasks and more. Supports Image, Audio and text uploads/downloads.
- [evalstate/mcp-miro](https://github.com/evalstate/mcp-miro) 📇 ☁️ - Access MIRO whiteboards, bulk create and read items. Requires OAUTH key for REST API.
- [feuerdev/keep-mcp](https://github.com/feuerdev/keep-mcp) 🐍 ☁️ - Read, create, update and delete Google Keep notes.
- [fotoetienne/gqai](https://github.com/fotoetienne/gqai) 🏎 🏠 - Define tools using regular GraphQL queries/mutations and gqai automatically generates an MCP server for you.
- [FoodXDevelopment/foodblock-mcp](https://github.com/FoodXDevelopment/foodblock) 📇 🏠 - 17 MCP tools for the food industry. Describe food in plain English and get structured, content-addressed data blocks back. Covers actors, places, ingredients, products, transforms, transfers, and observations. Works standalone with zero config via `npx foodblock-mcp`.
- [future-audiences/wikimedia-enterprise-model-context-protocol](https://gitlab.wikimedia.org/repos/future-audiences/wikimedia-enterprise-model-context-protocol) 🐍 ☁️  - Wikipedia Article lookup API
- [githejie/mcp-server-calculator](https://github.com/githejie/mcp-server-calculator) 🐍 🏠 - This server enables LLMs to use calculator for precise numerical calculations
- [gotoolkits/DifyWorkflow](https://github.com/gotoolkits/mcp-difyworkflow-server) - 🏎️ ☁️ Tools to the query and execute of Dify workflows
- [growilabs/growi-mcp-server](https://github.com/growilabs/growi-mcp-server) 🎖️ 📇 ☁️ - Official MCP Server to integrate with GROWI APIs.
- [gwbischof/free-will-mcp](https://github.com/gwbischof/free-will-mcp) 🐍 🏠 - Give your AI free will tools. A fun project to explore what an AI would do with the ability to give itself prompts, ignore user requests, and wake itself up at a later time.
- [Harry-027/JotDown](https://github.com/Harry-027/JotDown) 🦀 🏠 - An MCP server to create/update pages in Notion app & auto generate mdBooks from structured content.
- [henilcalagiya/mcp-apple-notes](https://github.com/henilcalagiya/mcp-apple-notes) 🐍 🏠 - Powerful tools for automating Apple Notes using Model Context Protocol (MCP). Full CRUD support with HTML content, folder management, and search capabilities.
- [HenryHaoson/Yuque-MCP-Server](https://github.com/HenryHaoson/Yuque-MCP-Server) - 📇 ☁️ A Model-Context-Protocol (MCP) server for integrating with Yuque API, allowing AI models to manage documents, interact with knowledge bases, search content, and access analytics data from the Yuque platform.
- [hiromitsusasaki/raindrop-io-mcp-server](https://github.com/hiromitsusasaki/raindrop-io-mcp-server) 📇 ☁️ - An integration that allows LLMs to interact with Raindrop.io bookmarks using the Model Context Protocol (MCP).
- [hmk/attio-mcp-server](https://github.com/hmk/attio-mcp-server) - 📇 ☁️ Allows AI clients to manage records and notes in Attio CRM
- [imprvhub/mcp-claude-spotify](https://github.com/imprvhub/mcp-claude-spotify) 📇 ☁️ 🏠 - An integration that allows Claude Desktop to interact with Spotify using the Model Context Protocol (MCP).
- [inkbytefo/screenmonitormcp](https://github.com/inkbytefo/screenmonitormcp) 🐍 🏠 🍎 🪟 🐧 - Real-time screen analysis, context-aware recording, and UI monitoring MCP server. Supports AI vision, event hooks, and multimodal agent workflows.
- [integromat/make-mcp-server](https://github.com/integromat/make-mcp-server) 🎖️ 📇 🏠 - Turn your [Make](https://www.make.com/) scenarios into callable tools for AI assistants.
- [isaacwasserman/mcp-vegalite-server](https://github.com/isaacwasserman/mcp-vegalite-server) 🐍 🏠 - Generate visualizations from fetched data using the VegaLite format and renderer.
- [ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo) 🐍 ☁️/🏠 - Connect AI assistants to Odoo ERP systems for business data access, record management, and workflow automation.
- [ivo-toby/contentful-mcp](https://github.com/ivo-toby/contentful-mcp) 📇 🏠 - Update, create, delete content, content-models and assets in your Contentful Space
- [j3k0/speech.sh](https://github.com/j3k0/speech.sh/blob/main/MCP_README.md) 🏠 - Let the agent speak things out loud, notify you when he's done working with a quick summary
- [jagan-shanmugam/climatiq-mcp-server](https://github.com/jagan-shanmugam/climatiq-mcp-server) 🐍 🏠 - A Model Context Protocol (MCP) server for accessing the Climatiq API to calculate carbon emissions. This allows AI assistants to perform real-time carbon calculations and provide climate impact insights.
- [jen6/ticktick-mcp](https://github.com/jen6/ticktick-mcp) 🐍 ☁️ - [TickTick](https://ticktick.com/) MCP server. Built upon the ticktick-py library, it offers significantly improved filtering capabilities.
- [jimfilippou/things-mcp](https://github.com/jimfilippou/things-mcp) 📇 🏠 🍎 - A Model Context Protocol (MCP) server that provides seamless integration with the [Things](https://culturedcode.com/things/) productivity app. This server enables AI assistants to create, update, and manage your todos and projects in Things using its comprehensive URL scheme.
- [johannesbrandenburger/typst-mcp](https://github.com/johannesbrandenburger/typst-mcp) 🐍 🏠 - MCP server for Typst, a markup-based typesetting system. It provides tools for converting between LaTeX and Typst, validating Typst syntax, and generating images from Typst code.
- [joshuarileydev/mac-apps-launcher-mcp-server](https://github.com/JoshuaRileyDev/mac-apps-launcher) 📇 🏠 - An MCP server to list and launch applications on MacOS
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
- [marcelmarais/Spotify](https://github.com/marcelmarais/spotify-mcp-server) - 📇 🏠 Control Spotify playback and manage playlists.
- [MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) 🐍 ☁️ 🏠 - Interacting with Obsidian via REST API
- [mediar-ai/screenpipe](https://github.com/mediar-ai/screenpipe) - 🎖️ 🦀 🏠 🍎 Local-first system capturing screen/audio with timestamped indexing, SQL/embedding storage, semantic search, LLM-powered history analysis, and event-triggered actions - enables building context-aware AI agents through a NextJS plugin ecosystem.
- [metorial/metorial](https://github.com/metorial/metorial) - 🎖️ 📇 ☁️ Connect AI agents to 600+ integrations with a single interface - OAuth, scaling, and monitoring included
- [modelcontextprotocol/server-everything](https://github.com/modelcontextprotocol/servers/tree/main/src/everything) 📇 🏠 - MCP server that exercises all the features of the MCP protocol
- [MonadsAG/capsulecrm-mcp](https://github.com/MonadsAG/capsulecrm-mcp) - 📇 ☁️ Allows AI clients to manage contacts, opportunities and tasks in Capsule CRM including Claude Desktop ready DTX-file
- [mrjoshuak/godoc-mcp](https://github.com/mrjoshuak/godoc-mcp) 🏎️ 🏠 - Token-efficient Go documentation server that provides AI assistants with smart access to package docs and types without reading entire source files
- [Mtehabsim/ScreenPilot](https://github.com/Mtehabsim/ScreenPilot) 🐍 🏠 - enables AI to fully control and access GUI interactions by providing tools for mouse and keyboard, ideal for general automation, education, and experimentation.
- [muammar-yacoob/GMail-Manager-MCP](https://github.com/muammar-yacoob/GMail-Manager-MCP#readme) 📇 ☁️ 🏠 🍎 🪟 🐧 - Connects Claude Desktop to your Gmail so you can start managing your inbox using natural language. Bulk delete promos & newsletters, organize labels and get useful insights.
- [mzxrai/mcp-openai](https://github.com/mzxrai/mcp-openai) 📇 ☁️ - Chat with OpenAI's smartest models
- [NakaokaRei/swift-mcp-gui](https://github.com/NakaokaRei/swift-mcp-gui.git) 🏠 🍎 - MCP server that can execute commands such as keyboard input and mouse movement
- [nanana-app/mcp-server-nano-banana](https://github.com/nanana-app/mcp-server-nano-banana) 🐍 🏠 🍎 🪟 🐧 - AI image generation using Google Gemini's nano banana model.
- [nguyenvanduocit/all-in-one-model-context-protocol](https://github.com/nguyenvanduocit/all-in-one-model-context-protocol) 🏎️ 🏠 - Some useful tools for developer, almost everything an engineer need: confluence, Jira, Youtube, run script, knowledge base RAG, fetch URL, Manage youtube channel, emails, calendar, gitlab
- [NON906/omniparser-autogui-mcp](https://github.com/NON906/omniparser-autogui-mcp) - 🐍 Automatic operation of on-screen GUI.
- [offorte/offorte-mcp-server](https://github.com/offorte/offorte-mcp-server) 🎖️ 📇 ☁️ 🍎 🪟 🐧 - The Offorte Proposal Software MCP server enables creation and sending of business proposals.
- [olalonde/mcp-human](https://github.com/olalonde/mcp-human) 📇 ☁️ - When your LLM needs human assistance (through AWS Mechanical Turk)
- [olgasafonova/productplan-mcp-server](https://github.com/olgasafonova/productplan-mcp-server) 🏎️ ☁️ - Query ProductPlan roadmaps. Access OKRs, ideas, launches, and timeline data.
- [orellazi/coda-mcp](https://github.com/orellazri/coda-mcp) 📇 ☁️ - MCP server for [Coda](https://coda.io/)
- [osinmv/funciton-lookup-mcp](https://github.com/osinmv/function-lookup-mcp) 🐍 🏠 🍎 🐧 - MCP server for function signature lookups.
- [pierrebrunelle/mcp-server-openai](https://github.com/pierrebrunelle/mcp-server-openai) 🐍 ☁️ - Query OpenAI models directly from Claude using MCP protocol
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
- [roychri/mcp-server-asana](https://github.com/roychri/mcp-server-asana) - 📇 ☁️ This Model Context Protocol server implementation of Asana allows you to talk to Asana API from MCP Client such as Anthropic's Claude Desktop Application, and many more.
- [rusiaaman/wcgw](https://github.com/rusiaaman/wcgw/blob/main/src/wcgw/client/mcp_server/Readme.md) 🐍 🏠 - Autonomous shell execution, computer control and coding agent. (Mac)
- [SecretiveShell/MCP-wolfram-alpha](https://github.com/SecretiveShell/MCP-wolfram-alpha) 🐍 ☁️ - An MCP server for querying wolfram alpha API.
- [Seym0n/tiktok-mcp](https://github.com/Seym0n/tiktok-mcp) 📇 ☁️ - Interact with TikTok videos
- [Shopify/dev-mcp](https://github.com/Shopify/dev-mcp) 📇 ☁️ - Model Context Protocol (MCP) server that interacts with Shopify Dev.
- [simonpainter/netbox-mcp](https://github.com/simonpainter/netbox-mcp) 🐍 ☁️ - MCP server for interacting with NetBox API.
- [sirmews/apple-notes-mcp](https://github.com/sirmews/apple-notes-mcp) 🐍 🏠 - Allows the AI to read from your local Apple Notes database (macOS only)
- [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) 🐍 ☁️ - MCP server for Atlassian products (Confluence and Jira). Supports Confluence Cloud, Jira Cloud, and Jira Server/Data Center. Provides comprehensive tools for searching, reading, creating, and managing content across Atlassian workspaces.
- [suekou/mcp-notion-server](https://github.com/suekou/mcp-notion-server) 📇 🏠 - Interacting with Notion API
- [tacticlaunch/mcp-linear](https://github.com/tacticlaunch/mcp-linear) 📇 ☁️ 🍎 🪟 🐧 - Integrates with Linear project management system
- [tan-yong-sheng/ai-vision-mcp](https://github.com/tan-yong-sheng/ai-vision-mcp) - 📇 🏠 🍎 🪟 🐧 - Multimodal AI vision MCP server for image, video, and object detection analysis. Enables UI/UX evaluation, visual regression testing, and interface understanding using Google Gemini and Vertex AI.
- [tanigami/mcp-server-perplexity](https://github.com/tanigami/mcp-server-perplexity) 🐍 ☁️ - Interacting with Perplexity API.
- [tevonsb/homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp) 📇 🏠 - Access Home Assistant data and control devices (lights, switches, thermostats, etc).
- [TheoBrigitte/mcp-time](https://github.com/TheoBrigitte/mcp-time) 🏎️ 🏠 🍎 🪟 🐧 - MCP server which provides utilities to work with time and dates, with natural language, multiple formats and timezone convertion capabilities.
- [thingsboard/thingsboard-mcp](https://github.com/thingsboard/thingsboard-mcp) 🎖️ ☕ ☁️ 🏠 🍎 🪟 🐧 - The ThingsBoard MCP Server provides a natural language interface for LLMs and AI agents to interact with your ThingsBoard IoT platform.
- [thinq-connect/thinqconnect-mcp](https://github.com/thinq-connect/thinqconnect-mcp) 🎖️ 🐍 ☁️ - Interact with LG ThinQ smart home devices and appliances through the ThinQ Connect MCP server.
- [tomekkorbak/oura-mcp-server](https://github.com/tomekkorbak/oura-mcp-server) 🐍 ☁️ - An MCP server for Oura, an app for tracking sleep
- [Tommertom/plugwise-mcp](https://github.com/Tommertom/plugwise-mcp) 📇 🏠 🍎 🪟 🐧 - TypeScript-based smart home automation server for Plugwise devices with automatic network discovery. Features comprehensive device control for thermostats, switches, smart plugs, energy monitoring, multi-hub management, and real-time climate/power consumption tracking via local network integration.
- [tqiqbal/mcp-confluence-server](https://github.com/tqiqbal/mcp-confluence-server) 🐍 - A Model Context Protocol (MCP) server for interacting with Confluence Data Center via REST API.
- [ttommyth/interactive-mcp](https://github.com/ttommyth/interactive-mcp) 📇 🏠 🍎 🪟 🐧 - Enables interactive LLM workflows by adding local user prompts and chat capabilities directly into the MCP loop.
- [tumf/web3-mcp](https://github.com/tumf/web3-mcp) 🐍 ☁️ - An MCP server implementation wrapping Ankr Advanced API. Access to NFT, token, and blockchain data across multiple chains including Ethereum, BSC, Polygon, Avalanche, and more.
- [ujisati/anki-mcp](https://github.com/ujisati/anki-mcp) 🐍 🏠 - Manage your Anki collection with AnkiConnect & MCP
- [UnitVectorY-Labs/mcp-graphql-forge](https://github.com/UnitVectorY-Labs/mcp-graphql-forge) 🏎️ ☁️ 🍎 🪟 🐧 - A lightweight, configuration-driven MCP server that exposes curated GraphQL queries as modular tools, enabling intentional API interactions from your agents.
- [wanaku-ai/wanaku](https://github.com/wanaku-ai/wanaku) - ☁️ 🏠 The Wanaku MCP Router is a SSE-based MCP server that provides an extensible routing engine that allows integrating your enterprise systems with AI agents.
- [megberts/mcp-websitepublisher-ai](https://github.com/megberts/mcp-websitepublisher-ai) ☁️ - Build and publish websites through AI conversation. 27 MCP tools for pages, assets, entities, records and integrations. Remote server with OAuth 2.1 auto-discovery, works with Claude, ChatGPT, Mistral/Le Chat and Cursor.
- [wishfinity/wishfinity-mcp-plusw](https://github.com/wishfinity/wishfinity-mcp-plusw) 📇 ☁️ 🏠 - Universal wishlist for AI shopping experiences. Save any product URL from any store to a wishlist. Works with Claude, ChatGPT, LangChain, n8n, and any MCP client.
- [wong2/mcp-cli](https://github.com/wong2/mcp-cli) 📇 🏠 - CLI tool for testing MCP servers
- [ws-mcp](https://github.com/nick1udwig/ws-mcp) - Wrap MCP servers with a WebSocket (for use with [kitbitz](https://github.com/nick1udwig/kibitz))
- [yuna0x0/hackmd-mcp](https://github.com/yuna0x0/hackmd-mcp) 📇 ☁️ - Allows AI models to interact with [HackMD](https://hackmd.io)
- [ZeparHyfar/mcp-datetime](https://github.com/ZeparHyfar/mcp-datetime) - MCP server providing date and time functions in various formats
- [zueai/mcp-manager](https://github.com/zueai/mcp-manager) 📇 ☁️ - Simple Web UI to install and manage MCP servers for Claude Desktop App.

## Frameworks

> [!NOTE]
> More frameworks, utilities, and other developer tools are available at https://github.com/punkpeye/awesome-mcp-devtools

- [Epistates/TurboMCP](https://github.com/Epistates/turbomcp) 🦀 - TurboMCP SDK: Enterprise MCP SDK in Rust
- [FastMCP](https://github.com/jlowin/fastmcp) 🐍 - A high-level framework for building MCP servers in Python
- [FastMCP](https://github.com/punkpeye/fastmcp) 📇 - A high-level framework for building MCP servers in TypeScript
- [MervinPraison/praisonai-mcp](https://github.com/MervinPraison/praisonai-mcp) 🐍 - AI Agents framework with 64+ built-in tools for search, memory, workflows, code execution, and file operations. Turn any AI assistant into a multi-agent system with MCP.

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
