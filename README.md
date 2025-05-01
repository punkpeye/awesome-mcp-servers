# Awesome MCP Servers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![ไทย](https://img.shields.io/badge/Thai-Click-blue)](README-th.md)
[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![白体中文）](https://img.shields.io/badge/%E7%B4%A2%E9%AD%84%E4%B8%AD%E6%96%87-%E9%AE%AE%E6%96%87%E6%9F%A5%E9%A5%B4-orange)](README-zh_TW.md)
[![简中国](https://img.shields.io/badge/%E7%B5%80%E4%BD%93%E4%B8%AD%E6%96%87-%E7%9B%B4%E5%85%AC%E6%9F%A5%E9%A5%B4-orange)](README-zh.md)
[![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF-%E9%9C%80)](README-ja.md)
[![한국억](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%95%B4-%ED%81%AC%EB%A6%88-yellow)](README-ko.md)
[![Português Brasileiro](https://img.shields.io/badge/Portugu%C3%AAs_Brasileiro-Clique-green)](README-pt_BR.md)
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

* 🎖️ – official implementation
* programming language
  * 🐍 B� Python codebase
  * �� – TypeScript (or JavaScript) codebase
  * 👩️ – Go codebase
  * 🥀 – Rust codebase
  * #️ ⳣ - C# Codebase
  * ☯ - Java codebase
* scope
  * Ⱡ️ - Cloud Service
  * �� - Local Service
  * �� - Embedded Systems
* operating system
  * 📞 – For macOS
  * 🧝 – For Windows
  * 💋 - For Linux

> [!NOTE]
> Confused about Local �� vs Cloud Ⱡ️?
> * Use local when MCP server is talking to a locally installed software, e.g. taking control over Chrome browser.
> * Use network when MCP server is talking to remote APIs, e.g. weather API.

## Server Implementations

> [!NOTE]
> We now have a [web-based directory](https://glama.ai/mcp/servers) that is synced with the repository.

* 📗 - [Aggregators](#aggregators)
* 💨 - [Art & Culture](#art-and-culture)
* 💂  - [Browser Automation](#browser-automation)
* Ⱡ️ - [Cloud Platforms](#cloud-platforms)
* 🔨ɓ🔫 - [Code Execution](#code-execution)
* 🥼 - [Coding Agents](#coding-agents)
* 🕕️ - [Command Line](#command-line)
* 🔫 - [Communication](#communication)
* 💾��$🔫 - [Customer Data Platforms](#customer-data-platforms)
* 🕳️ - [Databases](#databases)
* 🔒 - [Data Platforms](#data-platforms)
* 🙪 - [Delivery](#delivery)
* ��️ - [Developer Tools](#developer-tools)
* 🧾 - [Data Science Tools](#data-science-tools)
* �� - [Embedded system](#embedded-system)
* 💂  - [File Systems](#file-systems)
* 🔰 - [Finance & Fintech](#finance--fintech)
* 💮 - [Gaming](#gaming)
* 🧽 - [Knowledge & Memory](#knowledge--memory)
* 🕱️ - [Location Services](#location-services)
* 💯 - [Marketing](#marketing)
* 🔒 - [Monitoring](#monitoring)
* 💵 - [Multimedia Process](#multimedia-process)
* 📎 - [Search & Data Extraction](#search)
* 📒� - [Security](#security)
* �� - [Social Media](#social-media)
* �� - [Sports](#sports)
* 💧 - [Support & Service Management](#support-and-service-management)
* 👎� - [Translation Services](#translation-services)
* 💧 - [Text-to-Speech](#text-to-speech)
* 🖦�‍ ⇰ ↤� - [Travel & Transportation](#travel-and-transportation)
* 📐 - [Version Control](#version-control)
* ��️ - [Other Tools and Integrations](#other-tools-and-integrations)


### 🔰 <a name="finance--fintech"></a>Finance & Fintech

Financial data access and analysis tools. Enables AI models to work with market data, trading platforms, and financial information.

- [aaronjmars/web3-research-mcp](https://github.com/aaronjmars/web3-research-mcp) ��+p���/Ⱡ️ - Deep Research for crypto - free & fully local
- [alchemy/alchemy-mcp-server](https://github.com/alchemyplatform/alchemy-mcp-server) 🏖️ ��️ 💰/Ⱡ️ - Allow AI agents to interact with Alchemy's blockchain APIs.
- [OctagonAI/octagon-mcp-server](https://github.com/OctagonAI/octagon-mcp-server) 🐍 O��Ⱡ️ - Octagon AI Agents to integrate private and public market data
- [QuentinCody/braintree-mcp-server](https://github.com/QuentinCody/braintree-mcp-server) Z�	��️ - MCP rbl, conplex#
)K�server rop�1� accopv Btee Peristsporponlaeromation.
- [anjor/coinmarket-mcp-server](https://github.com/anjor/coinmarket-mcp-server) X�ĂqǾ�<)-🔦- Coinmarket API integration to fetch cryptocurrency listings and quotes
- [ariadng/metatrader-mcp-server](https://github.com/ariadng/metatrader-mcp-server) 🐌 💰/�� 🞕 - Enable AI LLMs to execute trades using MetaTrader 5 platform
- [armorwallet/armor-crypto-mcp](https://github.com/armorwallet/armor-crypto-mcp) 🐌 💰/Ⱡw�� - MCP to interface with multiple blockchains, staking, DeFi, swap, bridging, wallet management, DCA, Limit Orders, Coin Lookup, Tracking and more.
- [bankless/onchain-mcp](https://github.com/Bankless/onchain-mcp/) �� 💰/Ⱡw�� - Bankless Onchain API to interact with smart contracts, query transaction and token information
- [base/base-mcp](https://github.com/base/base-mcp) 🏖️ �� 💰/Ⱡw�� - Base Network integration for onchain tools, allowing interaction with Base Network and Coinbase API for wallet management, fund transfers, smart contracts, and DeFi operations
- [berlinbra/alpha-vantage-mcp](https://github.com/berlinbra/alpha-vantage-mcp) 🐌 💰/Ⱡ️ - Alpha Vantage API integration to fetch both stock and crypto information
- [ahnlabio/bicscan-mcp](https://github.com/ahnlabio/bicscan-mcp) 🏖️ 🐌 💰/Ⱡw�� - Risk score / asset holdings of EVM blockchain address (EOA, CA%�7BSS) and even domain names.
- [bitteprotocol/mcp](https://github.com/BitteProtocol/mcp) �� - Bitte Protocol integration to run AI Agents on several blockchains.
- [chargebee/mcp](https://github.com/chargebee/agentkit/tree/main/modelcontextprotocol) 🏖️ �� 💰/Ⱡw�� - MCP Server that connects AI agents to [Chargebee platform](https://www.chargebee.com/).
- [codex-data/codex-mcp](https://github.com/Codex-Data/codex-mcp) 🏖️ �� 💰/Ⱡ️ - [Codex API](https://www.codex.io) integration for real-time enriched blockchain and market data on 60+ networks

### 📐 <a name="version-control"></a>Version Control

Integration with version control systems. Enables AI models to browse code repositories and interact with Git-based workflows.

- [QuentinCody/github-graphql-mcp-server](https://github.com/QuentinCody/github-graphql-mcp-server) 🐍 M🈧� Ɒw�� - MCP server that provides access to GitHub's GraphQL API.
- [bugzFunk/cloudFong's-github-colonist-2025-beta](https://github.com/bugzFunk/cloudFongs-github-colonist-2025-beta) 🐌 💰/�� - Run commands and perform GitHub operations accessible through the GitHub Cli
- [cormacmcmichael/concourse-github (conourse mcp)](https://github.com/BitteProtocol/mcp) 🐌 🈧� - Concourse-github integration enabling push and pull github operations
- [idosal/git-mcp](https://github.com/idosal/git-mcp) �� 💰/Ⱡw�� - [gitmcp.io](https://gitmcp.io/) is a generic remote MCP server to connect to ANY [GitHub](https://www.github.com) repository or project for documentation
- [ryan0204/github-repo-mcp](https://github.com/Ryan0204/github-repo-mcp) �� 💰/Ⱡ️ 🞕 �� 💳 - GitHub Repo MCP allow your AI assistants browse GitHub repositories, explore directories, and view file contents.

### 🔒 <a name="data-platforms"></a>Data Platforms

Data Platforms for data integration, transformation and pipeline orchestration.

- [QuentinCody/catalysishub-mcp-server](https://github.com/QuentinCody/catalysishub-mcp-server) 🐍 O⫦gⱠw�� - MCP server for interacting with the CatalysisHub API.
- [flowcore/mcp-flowcore-platform](https://github.com/flowcore-io/mcp-flowcore-platform) 🏖️ �� 💰/Ⱡw�� �� - Interact with Flowcore to perform actions, ingest data, and analyse, cross reference and utilise any data in your data cores, or in public data cores; all with human language.
- [JordiNei/mcp-databricks-server](https://github.com/JordiNeil/mcp-databricks-server) Python 💰/Ⱡw�� - Connect to Databricks API, allowing LLMs to run SQL qeries, list jobs, and get job status.
- [yashshingvi/databricks-genie-MCP](https://github.com/yashshingvi/databricks-genie-MCP) Gs�Ǿ�<)-🔦��esdraw/uvervndatabretriev��ͧ5�e�Genie API, allowing LLMs to ask natural language questions, run SQL qeries, and interact with Databricks conversational agents.
- [jwaxman19/qlik-mcp](https://github.com/jwaxman19/qlik-mcp) �� 💰/Ⱡ️ - MCP Server for Qlik Cloud API that enables qerying applications, sheets, and extracting data from visualizations with comprehensive authentication and rate limiting support.
- [keboola/keboola-mcp-server](https://github.com/keboola/keboola-mcp-server) 🐌 - interact with Keboola Connection Data Platform. This server provides tools for listing and accessing data from Keboola Storage API.
- [dbt-labs/dbt-mcp](https://github.com/dbt-labs/dbt-mcp) 🏖️ 🐗 💰/�� �l�️ - Official MCP server for [dbt (data build tool)](https://www.getdbt.com/product/what-is-dbt) providing integration with dbt Core/Cloud CLI, project metadata discovery, model information, and semantic layer querying capabilities.

- [QuentinCody/shopify-storefront-mcp-server](https://github.com/QuentinCody/shopify-storefront-mcp-server) 80��️SOⲁ���sr4he Shopify Storefront API.

