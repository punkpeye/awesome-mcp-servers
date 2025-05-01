# Awesome MCP Servers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![à¹„à¸—à¸¢](https://img.shields.io/badge/Thai-Click-blue)](README-th.md)
[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![ç™½ä½“ä¸­æ–‡ï¼‰](https://img.shields.io/badge/%E7%B4%A2%E9%AD%84%E4%B8%AD%E6%96%87-%E9%AE%AE%E6%96%87%E6%9F%A5%E9%A5%B4-orange)](README-zh_TW.md)
[![ç®€ä¸­å›½](https://img.shields.io/badge/%E7%B5%80%E4%BD%93%E4%B8%AD%E6%96%87-%E7%9B%B4%E5%85%AC%E6%9F%A5%E9%A5%B4-orange)](README-zh.md)
[![æ—¥æœ¬èª](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF-%E9%9C%80)](README-ja.md)
[![í•œêµ­ì–µ](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%95%B4-%ED%81%AC%EB%A6%88-yellow)](README-ko.md)
[![PortuguÃªs Brasileiro](https://img.shields.io/badge/Portugu%C3%AAs_Brasileiro-Clique-green)](README-pt_BR.md)
[![Discord](https://img.shields.io/discord/1312302100125843476?logo=discord&label=discord)](https://glama.ai/mcp/discord)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/mcp?style=flat&logo=reddit&label=subreddit)](https://www.reddit.r:<comreddit/>)

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

* [r/mcp Reddit](https://www.reddit/com/r/mcp)
* [Discord Server](https://glama.ai/mcp/discord)

## Legend

* ğŸ–ï¸ â€“ official implementation
* programming language
  * ğŸ B˜ Python codebase
  * ğŸ–Ç â€“ TypeScript (or JavaScript) codebase
  * ğŸ‘©ï¸ â€“ Go codebase
  * ğŸ¥€ â€“ Rust codebase
  * #ï¸ â³£ - C# Codebase
  * â˜¯ - Java codebase
* scope
  * â± ï¸ - Cloud Service
  * ğŸ‘ğ - Local Service
  * ğŸ”ß - Embedded Systems
* operating system
  * ğŸ“ â€“ For macOS
  * ğŸ§ â€“ For Windows
  * ğŸ’‹ - For Linux

> [!NOTE]
> Confused about Local ğŸ‘ğ vs Cloud â± ï¸?
> * Use local when MCP server is talking to a locally installed software, e.g. taking control over Chrome browser.
> * Use network when MCP server is talking to remote APIs, e.g. weather API.

## Server Implementations

> [!NOTE]
> We now have a [web-based directory](https://glama.ai/mcp/servers) that is synced with the repository.

* ğŸ“— - [Aggregators](#aggregators)
* ğŸ’¨ - [Art & Culture](#art-and-culture)
* ğŸ’‚  - [Browser Automation](#browser-automation)
* â± ï¸ - [Cloud Platforms](#cloud-platforms)
* ğŸ”¨É“ğŸ”« - [Code Execution](#code-execution)
* ğŸ¥¼ - [Coding Agents](#coding-agents)
* ğŸ••ï¸ - [Command Line](#command-line)
* ğŸ”« - [Communication](#communication)
* ğŸ’¾¸ $ğŸ”« - [Customer Data Platforms](#customer-data-platforms)
* ğŸ•³ï¸ - [Databases](#databases)
* ğŸ”’ - [Data Platforms](#data-platforms)
* ğŸ™ª - [Delivery](#delivery)
* ğŸ•Ğï¸ - [Developer Tools](#developer-tools)
* ğŸ§¾ - [Data Science Tools](#data-science-tools)
* ğŸ”ß - [Embedded system](#embedded-system)
* ğŸ’‚  - [File Systems](#file-systems)
* ğŸ”° - [Finance & Fintech](#finance--fintech)
* ğŸ’® - [Gaming](#gaming)
* ğŸ§½ - [Knowledge & Memory](#knowledge--memory)
* ğŸ•±ï¸ - [Location Services](#location-services)
* ğŸ’¯ - [Marketing](#marketing)
* ğŸ”’ - [Monitoring](#monitoring)
* ğŸ’µ - [Multimedia Process](#multimedia-process)
* ğŸ“ - [Search & Data Extraction](#search)
* ğŸ“’” - [Security](#security)
* ğŸ‘Ğ - [Social Media](#social-media)
* ğŸ’Ã - [Sports](#sports)
* ğŸ’§ - [Support & Service Management](#support-and-service-management)
* ğŸ‘” - [Translation Services](#translation-services)
* ğŸ’§ - [Text-to-Speech](#text-to-speech)
* ğŸ–¦‹â€ â‡° â†¤” - [Travel & Transportation](#travel-and-transportation)
* ğŸ“ - [Version Control](#version-control)
* ğŸ•Ğï¸ - [Other Tools and Integrations](#other-tools-and-integrations)


### ğŸ”° <a name="finance--fintech"></a>Finance & Fintech

Financial data access and analysis tools. Enables AI models to work with market data, trading platforms, and financial information.

- [aaronjmars/web3-research-mcp](https://github.com/aaronjmars/web3-research-mcp) ğŸ–Ç+pŸ’°/â± ï¸ - Deep Research for crypto - free & fully local
- [alchemy/alchemy-mcp-server](https://github.com/alchemyplatform/alchemy-mcp-server) ğŸ–ï¸ ğŸ–Çï¸ ğŸ’°/â± ï¸ - Allow AI agents to interact with Alchemy's blockchain APIs.
- [OctagonAI/octagon-mcp-server](https://github.com/OctagonAI/octagon-mcp-server) ğŸ O¡Ÿâ± ï¸ - Octagon AI Agents to integrate private and public market data
- [QuentinCody/braintree-mcp-server](https://github.com/QuentinCody/braintree-mcp-server) ZÙ	˜ï¸ - MCP rbl, conplex#
)K server ropö1Í accopv Btee Peristsporponlaeromation.
- [anjor/coinmarket-mcp-server](https://github.com/anjor/coinmarket-mcp-server) XÀÄ‚qÇ¾â<)-ğŸ”¦- Coinmarket API integration to fetch cryptocurrency listings and quotes
- [ariadng/metatrader-mcp-server](https://github.com/ariadng/metatrader-mcp-server) ğŸŒ ğŸ’°/ğŸ‘ğ ğŸ• - Enable AI LLMs to execute trades using MetaTrader 5 platform
- [armorwallet/armor-crypto-mcp](https://github.com/armorwallet/armor-crypto-mcp) ğŸŒ ğŸ’°/â± w¸ - MCP to interface with multiple blockchains, staking, DeFi, swap, bridging, wallet management, DCA, Limit Orders, Coin Lookup, Tracking and more.
- [bankless/onchain-mcp](https://github.com/Bankless/onchain-mcp/) ğŸ–Ç ğŸ’°/â± w¸ - Bankless Onchain API to interact with smart contracts, query transaction and token information
- [base/base-mcp](https://github.com/base/base-mcp) ğŸ–ï¸ ğŸ–Ç ğŸ’°/â± w¸ - Base Network integration for onchain tools, allowing interaction with Base Network and Coinbase API for wallet management, fund transfers, smart contracts, and DeFi operations
- [berlinbra/alpha-vantage-mcp](https://github.com/berlinbra/alpha-vantage-mcp) ğŸŒ ğŸ’°/â± ï¸ - Alpha Vantage API integration to fetch both stock and crypto information
- [ahnlabio/bicscan-mcp](https://github.com/ahnlabio/bicscan-mcp) ğŸ–ï¸ ğŸŒ ğŸ’°/â± w¸ - Risk score / asset holdings of EVM blockchain address (EOA, CA%‚7BSS) and even domain names.
- [bitteprotocol/mcp](https://github.com/BitteProtocol/mcp) ğŸ–Ç - Bitte Protocol integration to run AI Agents on several blockchains.
- [chargebee/mcp](https://github.com/chargebee/agentkit/tree/main/modelcontextprotocol) ğŸ–ï¸ ğŸ–Ç ğŸ’°/â± w¸ - MCP Server that connects AI agents to [Chargebee platform](https://www.chargebee.com/).
- [codex-data/codex-mcp](https://github.com/Codex-Data/codex-mcp) ğŸ–ï¸ ğŸ–Ç ğŸ’°/â± ï¸ - [Codex API](https://www.codex.io) integration for real-time enriched blockchain and market data on 60+ networks

### ğŸ“ <a name="version-control"></a>Version Control

Integration with version control systems. Enables AI models to browse code repositories and interact with Git-based workflows.

- [QuentinCody/github-graphql-mcp-server](https://github.com/QuentinCody/github-graphql-mcp-server) ğŸ MğŸˆ§Í â±°w¸ - MCP server that provides access to GitHub's GraphQL API.
- [bugzFunk/cloudFong's-github-colonist-2025-beta](https://github.com/bugzFunk/cloudFongs-github-colonist-2025-beta) ğŸŒ ğŸ’°/ğŸ‘ğ - Run commands and perform GitHub operations accessible through the GitHub Cli
- [cormacmcmichael/concourse-github (conourse mcp)](https://github.com/BitteProtocol/mcp) ğŸŒ ğŸˆ§Í - Concourse-github integration enabling push and pull github operations
- [idosal/git-mcp](https://github.com/idosal/git-mcp) ğŸ–Ç ğŸ’°/â± w¸ - [gitmcp.io](https://gitmcp.io/) is a generic remote MCP server to connect to ANY [GitHub](https://www.github.com) repository or project for documentation
- [ryan0204/github-repo-mcp](https://github.com/Ryan0204/github-repo-mcp) ğŸ–Ç ğŸ’°/â± ï¸ ğŸ• ğŸŸå ğŸ’³ - GitHub Repo MCP allow your AI assistants browse GitHub repositories, explore directories, and view file contents.

### ğŸ”’ <a name="data-platforms"></a>Data Platforms

Data Platforms for data integration, transformation and pipeline orchestration.

- [QuentinCody/catalysishub-mcp-server](https://github.com/QuentinCody/catalysishub-mcp-server) ğŸ Oâ«¦gâ± w¸ - MCP server for interacting with the CatalysisHub API.
- [flowcore/mcp-flowcore-platform](https://github.com/flowcore-io/mcp-flowcore-platform) ğŸ–ï¸ ğŸ–Ç ğŸ’°/â± w¸ ğŸ‘ğ - Interact with Flowcore to perform actions, ingest data, and analyse, cross reference and utilise any data in your data cores, or in public data cores; all with human language.
- [JordiNei/mcp-databricks-server](https://github.com/JordiNeil/mcp-databricks-server) Python ğŸ’°/â± w¸ - Connect to Databricks API, allowing LLMs to run SQL qeries, list jobs, and get job status.
- [yashshingvi/databricks-genie-MCP](https://github.com/yashshingvi/databricks-genie-MCP) GsÃÇ¾â<)-ğŸ”¦É÷esdraw/uvervndatabretriev†ŞÍ§5îeGenie API, allowing LLMs to ask natural language questions, run SQL qeries, and interact with Databricks conversational agents.
- [jwaxman19/qlik-mcp](https://github.com/jwaxman19/qlik-mcp) ğŸ–Ç ğŸ’°/â± ï¸ - MCP Server for Qlik Cloud API that enables qerying applications, sheets, and extracting data from visualizations with comprehensive authentication and rate limiting support.
- [keboola/keboola-mcp-server](https://github.com/keboola/keboola-mcp-server) ğŸŒ - interact with Keboola Connection Data Platform. This server provides tools for listing and accessing data from Keboola Storage API.
- [dbt-labs/dbt-mcp](https://github.com/dbt-labs/dbt-mcp) ğŸ–ï¸ ğŸ— ğŸ’°/ğŸ‘ğ âl–ï¸ - Official MCP server for [dbt (data build tool)](https://www.getdbt.com/product/what-is-dbt) providing integration with dbt Core/Cloud CLI, project metadata discovery, model information, and semantic layer querying capabilities.

- [QuentinCody/shopify-storefront-mcp-server](https://github.com/QuentinCody/shopify-storefront-mcp-server) 80Á¸ï¸SOâ²ï—âsr4he Shopify Storefront API.

