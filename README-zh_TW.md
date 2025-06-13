# 精選的 MCP 伺服器 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![繁體中文](https://img.shields.io/badge/繁體中文-點擊查看-orange)](README-zh_TW.md)
[![简体中文](https://img.shields.io/badge/简体中文-点击查看-orange)](README-zh.md)
[![日本語](https://img.shields.io/badge/日本語-クリック-青)](README-ja.md)
[![한국어](https://img.shields.io/badge/한국어-클릭-yellow)](README-ko.md)
[![Português Brasileiro](https://img.shields.io/badge/Português_Brasileiro-Clique-green)](README-pt_BR.md)
[![Discord](https://img.shields.io/discord/1312302100125843476?logo=discord&label=discord)](https://glama.ai/mcp/discord)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/mcp?style=flat&logo=reddit&label=subreddit)](https://www.reddit.com/r/mcp/)

精選的優秀模型上下文協議 (MCP) 伺服器列表。

* [什麼是 MCP？](#什麼是MCP？)
* [教學](#教學)
* [社群](#社群)
* [說明](#說明)
* [Server 實現](#伺服器實現)
* [框架](#框架)
* [實用工具](#實用工具)
* [用戶端](#用戶端)
* [提示和技巧](#提示和技巧)

## 什麼是MCP？

[MCP](https://modelcontextprotocol.io/) 是一種開放協議，通過標準化的伺服器實現，使 AI 模型能夠安全地與本地和遠端資源進行交互。此列表重點關注可用於生產和實驗性的 MCP 伺服器，這些伺服器通過文件訪問、資料庫連接、API 整合和其他上下文服務來擴展 AI 功能。

## 教學

* [Model Context Protocol (MCP) 快速開始](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
* [設置 Claude 桌面應用程式以使用 SQLite 資料庫](https://youtu.be/wxCCzo9dGj0)

## 社群

* [r/mcp Reddit](https://www.reddit.com/r/mcp)
* [Discord 服務](https://glama.ai/mcp/discord)

## 說明

* 🎖️ – 官方實現
* 程式語言
  * 🐍 – Python 代碼庫
  * 📇 – TypeScript 代碼庫
  * 🏎️ – Go 代碼庫
  * 🦀 – Rust 代碼庫
  * #️⃣ - C# 代碼庫
  * ☕ - Java 代碼庫
* 範圍
  * ☁️ - 雲服務
  * 🏠 - 本地服務
* 操作系統
  * 🍎 – For macOS
  * 🪟 – For Windows


> [!NOTE]
> 關於本地 🏠 和雲 ☁️ 的區別：
> * 當 MCP 伺服器與本地安裝的軟體通信時使用本地服務，例如控制 Chrome 瀏覽器。
> * 當 MCP 伺服器與遠端 API 通信時使用網路服務，例如天氣 API。
## 伺服器實現

> [!NOTE]
> 我們現在有一個與儲存庫同步的[基於 Web 的目錄](https://glama.ai/mcp/servers)。

* 🔗 - [Aggregators](#aggregators)
* 📂 - [瀏覽器自動化](#browser-automation)
* 🎨 - [藝術與文化](#art-and-culture)
* ☁️ - [雲端平台](#cloud-platforms)
* 🖥️ - [命令行](#command-line)
* 💬 - [社交](#communication)
* 👤 - [數據平台](#customer-data-platforms)
* 🗄️ - [資料庫](#databases)
* 📊 - [數據平台](#data-platforms)
* 🛠️ - [開發者工具](#developer-tools)
* 📂 - [文件系統](#file-systems)
* 💰 - [Finance & Fintech](#finance--fintech)
* 🎮 - [遊戲](#gaming)
* 🧠 - [知識與記憶](#knowledge--memory)
* 🗺️ - [位置服務](#location-services)
* 🎯 - [行銷](#marketing)
* 📊 - [監測](#monitoring)
* 🔎 - [搜尋](#search)
* 🔒 - [安全](#security)
* 🌎 - [翻譯服務](#translation-services)
* 🚆 - [旅行與交通](#travel-and-transportation)
* 🔄 - [版本控制](#version-control)
* 🛠️ - [其他工具和整合](#other-tools-and-integrations)

### 🔗 <a name="aggregators"></a>聚合器

通過單個MCP伺服器訪問多個應用程式和工具的伺服器。

- [OpenMCP](https://github.com/wegotdocs/open-mcp) 📇 🏠 🍎 🪟 🐧 - 10秒內將Web API轉換為MCP伺服器並將其添加到開源註冊表中: https://open-mcp.org
- [tigranbs/mcgravity](https://github.com/tigranbs/mcgravity) 📇 🏠 - 一個用於將多個MCP伺服器組合成一個統一端點的代理工具。通過在多個MCP伺服器之間進行負載平衡請求來擴展您的AI工具，類似於Nginx對Web伺服器的工作方式。
- [MetaMCP](https://github.com/metatool-ai/metatool-app) 📇 ☁️ 🏠 🍎 🪟 🐧 - MetaMCP是一個統一的中間件MCP伺服器，通過GUI管理您的MCP連接。
- [MCP Access Point](https://github.com/sxhxliang/mcp-access-point)  📇 ☁️ 🏠 🍎 🪟 🐧  - 一鍵將Web API轉入MCP伺服器，而無需對程式碼進行任何修改。
- [hamflx/imagen3-mcp](https://github.com/hamflx/imagen3-mcp) 📇 🏠 🪟 🍎 🐧 - 一個通過 MCP 使用 Google Imagen 3.0 API 的強大圖像生成工具。使用文本提示生成具有高級攝影、藝術和逼真控制的高質量圖像。

### 📂 <a name="browser-automation"></a>瀏覽器自動化

Web 內容訪問和自動化功能。支援以 AI 友好格式搜尋、抓取和處理 Web 內容。
- [@blackwhite084/playwright-plus-python-mcp](https://github.com/blackwhite084/playwright-plus-python-mcp) 🌐 - 使用 Playwright 進行瀏覽器自動化的 MCP 伺服器，更適合llm
- [@executeautomation/playwright-mcp-server](https://github.com/executeautomation/mcp-playwright) 🌐⚡️ - 使用 Playwright 進行瀏覽器自動化和網頁抓取的 MCP 伺服器
- [@automatalabs/mcp-server-playwright](https://github.com/Automata-Labs-team/MCP-Server-Playwright) 🌐🖱️ - 使用 Playwright 實現瀏覽器自動化的 MCP 伺服器
- [@modelcontextprotocol/server-puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) 📇 🏠 - 用於網頁抓取和交互的瀏覽器自動化
- [@kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) 📇 ☁️ - 獲取 YouTube 字幕和文字記錄以供 AI 分析
- [@recursechat/mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts) 📇 🏠 🍎 - MCP 伺服器與 Apple Shortcuts 的整合
- [@fradser/mcp-server-apple-reminders](https://github.com/FradSer/mcp-server-apple-reminders) 📇 🏠 🍎 - macOS 上與 Apple Reminders 整合的 MCP 伺服器
- [kimtth/mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing) 🐍 🏠 - 使用 Azure OpenAI 和 Playwright 的“最小”伺服器/用戶端 MCP 實現。
- [@pskill9/web-search](https://github.com/pskill9/web-search) 📇 🏠 - 一個支援使用 Google 搜尋結果進行免費網頁搜尋的 MCP 伺服器，無需 API 金鑰
- [@34892002/bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js) 📇 🏠 - 一個支援搜尋 B站 內容的 MCP 伺服器。提供LangChain呼叫範例、測試腳本。
- [aircodelabs/grasp](https://github.com/aircodelabs/grasp) 📇 🏠 - 可本地部署或自托管的瀏覽器自動化操作，原生支持 MCP 和 A2A。

### 🎨 <a name="art-and-culture"></a>藝術與文化

提供藝術收藏、文化遺產和博物館資料庫的訪問與探索。讓 AI 模型能夠搜尋和分析藝術文化內容。

- [cantian-ai/bazi-mcp](https://github.com/cantian-ai/bazi-mcp) 📇 🏠 ☁️ 🍎 🪟 - 提供全面精準的八字排盤和測算信息
- [burningion/video-editing-mcp](https://github.com/burningion/video-editing-mcp) 📹🎬 - 從您的影片集合中添加、分析、搜尋和生成影片剪輯
- [r-huijts/rijksmuseum-mcp](https://github.com/r-huijts/rijksmuseum-mcp) 📇 ☁️ - 荷蘭國立博物館 API 整合，支援藝術品搜尋、詳情查詢和收藏品瀏覽
- [yuna0x0/anilist-mcp](https://github.com/yuna0x0/anilist-mcp) 📇 ☁️ - 整合 AniList API 獲取動畫和漫畫資訊的 MCP 伺服器

### ☁️ <a name="cloud-platforms"></a>雲平台

雲平台服務整合。實現與雲基礎設施和服務的管理和交互。

- [qiniu/qiniu-mcp-server](https://github.com/qiniu/qiniu-mcp-server) 🐍 ☁️ - 基於七牛雲產品構建的 MCP，支援存取七牛雲儲存、智能多媒體服務等。
- [Cloudflare MCP Server](https://github.com/cloudflare/mcp-server-cloudflare) 🎖️ 📇 ☁️ - 與 Cloudflare 服務整合，包括 Workers、KV、R2 和 D1
- [Kubernetes MCP Server](https://github.com/strowk/mcp-k8s-go) - 🏎️ ☁️ 通過 MCP 操作 Kubernetes 集群
- [alexbakers/mcp-ipfs](https://github.com/alexbakers/mcp-ipfs) 📇 ☁️ - 上傳和操作 IPFS 儲存
- [aliyun/alibaba-cloud-ops-mcp-server](https://github.com/aliyun/alibaba-cloud-ops-mcp-server) 🎖️ 🐍 ☁️ - 一款MCP伺服器，使AI助手能夠運維管理阿里雲上的資源，支援ECS、雲監控、OOS以及其他各種廣泛使用的雲產品。
- [@flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) - 📇 ☁️/🏠 使用 Typescript 實現 Kubernetes 集群中針對 pod、部署、服務的操作。
- [johnneerdael/netskope-mcp](https://github.com/johnneerdael/netskope-mcp) ☁️ - 提供對 Netskope Private Access 環境中所有組件的訪問權限，包含詳細的設置資訊和 LLM 使用範例。
- [bright8192/esxi-mcp-server](https://github.com/bright8192/esxi-mcp-server) 🐍 ☁️ - 提供對 VMware ESXi/vCenter 管理伺服器，提供簡單的 REST API 介面來管理虛擬機。
- [wenhuwang/mcp-k8s-eye](https://github.com/wenhuwang/mcp-k8s-eye) 🏎️ ☁️/🏠 提供 Kubernetes 集群資源管理, 深度分析集群和應用的健康狀態
- [johnneerdael/netskope-mcp](https://github.com/johnneerdael/netskope-mcp) 🔒 ☁️ - 提供對 Netskope Private Access 環境中所有組件的訪問權限，包含詳細的設置資訊和 LLM 使用範例。
- [weibaohui/k8m](https://github.com/weibaohui/k8m) - 🏎️ ☁️/🏠 提供MCP多集群k8s管理操作，提供管理界面、日誌，內建近50種工具，覆蓋常見運維開發場景，支援常規資源、CRD資源。
- [weibaohui/kom](https://github.com/weibaohui/kom) - 🏎️ ☁️/🏠 提供MCP多集群k8s管理操作，可作為SDK集成到您自己的項目中，內建近50種工具，覆蓋常見運維開發場景，支援常規資源、CRD資源。
- [silenceper/mcp-k8s](https://github.com/silenceper/mcp-k8s) 🏎️ ☁️/🏠 MCP-K8S 是一個 AI 驅動的 Kubernetes 資源管理工具，通過自然語言交互方式，讓用戶能夠輕鬆操作 Kubernetes 集群中的任意資源，包括原生資源（如 Deployment、Service）和自定義資源（CRD）。無需記憶複雜命令，只需描述需求，AI 就能準確執行對應的集群操作，大大提升了 Kubernetes 的易用性。

### 🖥️ <a name="command-line"></a>Command Line

運行命令、捕獲輸出以及以其他方式與 shell 和命令行工具交互。

- [ferrislucas/iterm-mcp](https://github.com/ferrislucas/iterm-mcp) 🖥️ 🛠️ 💬 - 一個為 iTerm 終端提供訪問能力的 MCP 伺服器。您可以執行命令，並就終端中看到的內容進行提問交互。
- [g0t4/mcp-server-commands](https://github.com/g0t4/mcp-server-commands) 📇 🏠 - 使用“run_command”和“run_script”工具運行任何命令。
- [MladenSU/cli-mcp-server](https://github.com/MladenSU/cli-mcp-server) 🐍 🏠 - 具有安全執行和可訂製安全策略的命令行界面
- [tumf/mcp-shell-server](https://github.com/tumf/mcp-shell-server) 實現模型上下文協議 (MCP) 的安全 shell 命令執行伺服器

### 💬 <a name="communication"></a>社交

與通訊平台集成，實現消息管理和渠道運營。使AI模型能夠與團隊溝通工具進行交互。

- [zcaceres/gtasks-mcp](https://github.com/zcaceres/gtasks-mcp) - 📇 ☁️ - 用於管理 Google Tasks 的 MCP 伺服器
- [hannesrudolph/imessage-query-fastmcp-mcp-server](https://github.com/hannesrudolph/imessage-query-fastmcp-mcp-server) 🐍 🏠 🍎 - MCP 伺服器通過模型上下文協議 (MCP) 提供對 iMessage 資料庫的安全訪問，使 LLM 能夠透過適當的電話號碼驗證和附件處理來查詢和分析 iMessage 對話
- [@modelcontextprotocol/server-slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack) 📇 ☁️ - 用於頻道管理和消息傳遞的 Slack 工作區集成
- [@keturiosakys/bluesky-context-server](https://github.com/keturiosakys/bluesky-context-server) 📇 ☁️ - Bluesky 實例集成，用於查詢和交互
- [MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite) - 🐍 ☁️ - 與 Gmail 和 Google 日曆集成。
- [adhikasp/mcp-twikit](https://github.com/adhikasp/mcp-twikit) 🐍 ☁️ - 與 Twitter 搜尋和時間線進行交互
- [gotoolkits/wecombot](https://github.com/gotoolkits/mcp-wecombot-server.git) - 🚀 ☁️  - MCP伺服器 Tools 應用程式，用於向企業微信群機器人發送各種類型的消息。
- [AbdelStark/nostr-mcp](https://github.com/AbdelStark/nostr-mcp) - 🌐 ☁️ - Nostr MCP 伺服器，支援與 Nostr 交互，可發布筆記等功能。
- [line/line-bot-mcp-server](https://github.com/line/line-bot-mcp-server) 🎖 📇 ☁️ - 整合 LINE 官方帳號的 MCP 伺服器
- [sawa-zen/vrchat-mcp](https://github.com/sawa-zen/vrchat-mcp) - 📇 🏠 這是一個與VRChat API交互的MCP伺服器。您可以獲取VRChat的好友、世界、化身等資訊。
- [YCloud-Developers/ycloud-whatsapp-mcp-server](https://github.com/YCloud-Developers/ycloud-whatsapp-mcp-server) 📇 🏠 - 透過 YCloud 平台發送 WhatsApp Business 訊息的 MCP 伺服器。  
- [jaipandya/producthunt-mcp-server](https://github.com/jaipandya/producthunt-mcp-server) 🐍 🏠 - Product Hunt 的 MCP 伺服器。可與熱門貼文、評論、收藏集、用戶等進行互動。

### 👤 <a name="customer-data-platforms"></a>數據平台

提供對客戶數據平台內客戶資料的訪問

- [sergehuber/inoyu-mcp-unomi-server](https://github.com/sergehuber/inoyu-mcp-unomi-server) 📇 ☁️ - MCP 伺服器用於訪問和更新 Apache Unomi CDP 伺服器上的設定檔。
- [OpenDataMCP/OpenDataMCP](https://github.com/OpenDataMCP/OpenDataMCP) 🐍☁️ - 使用模型上下文協議將任何開放數據連接到任何 LLM。
- [tinybirdco/mcp-tinybird](https://github.com/tinybirdco/mcp-tinybird) 🐍☁️ - MCP 伺服器可從任何 MCP 用戶端與 Tinybird Workspace 進行交互。
- [@iaptic/mcp-server-iaptic](https://github.com/iaptic/mcp-server-iaptic) 🎖️ 📇 ☁️ - 連接 [iaptic](https://www.iaptic.com) 平台，讓您輕鬆查詢客戶購買記錄、交易數據以及應用營收統計資訊。
- [@antv/mcp-server-chart](https://github.com/antvis/mcp-server-chart) 🎖️ 📇 ☁️ - 一個基於 [AntV](https://github.com/antvis) 生成資料視覺化圖表的 MCP Server 插件。

### 🗄️ <a name="databases"></a>資料庫

具有模式檢查功能的安全資料庫訪問。支援使用可配置的安全控制（包括只讀訪問）查詢和分析數據。

- [aliyun/alibabacloud-tablestore-mcp-server](https://github.com/aliyun/alibabacloud-tablestore-mcp-server) ☕ 🐍 ☁️ - 阿里雲表格儲存(Tablestore)的 MCP 伺服器實現，特性包括添加文件、基於向量和標量進行語義搜尋、RAG友好。
- [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) 🐍 🏠 - 集成 Elasticsearch 的 MCP 伺服器實現
- [domdomegg/airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server) 📇 🏠 - Airtable 資料庫集成，具有架構檢查、讀寫功能
- [LucasHild/mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery) 🐍 ☁️ - BigQuery 資料庫集成了架構檢查和查詢功能
- [c4pt0r/mcp-server-tidb](https://github.com/c4pt0r/mcp-server-tidb) 🐍 ☁️ - TiDB 資料庫集成，包括表結構的建立 DDL 和 SQL 的執行
- [crystaldba/postgres-mcp](https://github.com/crystaldba/postgres-mcp) 🐍 🏠 - 用於 Postgres 開發和運維的多功能 MCP 伺服器，提供性能分析、調優和健康檢查工具
- [ergut/mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server) 📇 ☁️ - Google BigQuery 集成的伺服器實現，可實現直接 BigQuery 資料庫訪問和查詢功能
- [ClickHouse/mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse) 🐍 ☁️ - 集成 Apache Kafka 和 Timeplus。可以獲取Kafka中的最新數據，並通過 Timeplus 來 SQL 查詢。
- [jovezhong/mcp-timeplus](https://github.com/jovezhong/mcp-timeplus) 🐍 ☁️ - MCP server for Apache Kafka and Timeplus. Able to list Kafka topics, poll Kafka messages, save Kafka data locally and query streaming data with SQL via Timeplus
- [@fireproof-storage/mcp-database-server](https://github.com/fireproof-storage/mcp-database-server) 📇 ☁️ - Fireproof 分布式帳本資料庫，支援多用戶數據同步
- [designcomputer/mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server) 🐍 🏠 - MySQL 資料庫集成可配置的訪問控制、模式檢查和全面的安全指南
- [f4ww4z/mcp-mysql-server](https://github.com/f4ww4z/mcp-mysql-server) 📇 🏠 - 基於 Node.js 的 MySQL 資料庫集成，提供安全的 MySQL 資料庫操作
- [@modelcontextprotocol/server-postgres](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) 📇 🏠 - PostgreSQL 資料庫集成了模式檢查和查詢功能
- [@modelcontextprotocol/server-sqlite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) 🐍 🏠 - 具有內建分析功能的 SQLite 資料庫操作
- [@joshuarileydev/supabase-mcp-server](https://github.com/joshuarileydev/supabase) - Supabase MCP 伺服器用於管理和創建 Supabase 中的項目和組織
- [ktanaka101/mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb) 🐍 🏠 - DuckDB 資料庫集成了模式檢查和查詢功能
- [QuantGeekDev/mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp) 📇 🏠 - MongoDB 集成使 LLM 能夠直接與資料庫交互。
- [tinybirdco/mcp-tinybird](https://github.com/tinybirdco/mcp-tinybird) 🐍 ☁️ - Tinybird 集成查詢和 API 功能
- [kiliczsh/mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server) 📇 🏠 - MongoDB 的模型上下文協議伺服器
- [tuannvm/mcp-trino](https://github.com/tuannvm/mcp-trino) 🏎️ ☁️ - 一個使用 Go 語言實現的 Trino 專用 Model Context Protocol (MCP) 伺服器。
- [KashiwaByte/vikingdb-mcp-server](https://github.com/KashiwaByte/vikingdb-mcp-server) 🐍 ☁️ - VikingDB 資料庫集成了collection和index的基本資訊介紹，並提供向量儲存和查詢的功能.
- [neo4j-contrib/mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j) 🐍 🏠 - Neo4j 的模型上下文協議
- [isaacwasserman/mcp-snowflake-server](https://github.com/isaacwasserman/mcp-snowflake-server) 🐍 ☁️ - Snowflake 集成實現，支援讀取和（可選）寫入操作，並具備洞察跟蹤功能
- [hannesrudolph/sqlite-explorer-fastmcp-mcp-server](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server) 🐍 🏠 - 一個 MCP 伺服器，通過模型上下文協議 （MCP） 提供對 SQLite 資料庫的安全只讀訪問。該伺服器是使用 FastMCP 框架構建的，它使 LLM 能夠探索和查詢具有內建安全功能和查詢驗證的 SQLite 資料庫。
- [sirmews/mcp-pinecone](https://github.com/sirmews/mcp-pinecone) 🐍 ☁️ - Pinecone 與向量搜尋功能的集成
- [runekaagaard/mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy) 🐍 🏠 - 基於SQLAlchemy的通用資料庫集成，支援PostgreSQL、MySQL、MariaDB、SQLite、Oracle、MS SQL Server等眾多資料庫。具有架構和關係檢查以及大型數據集分析功能。
- [GreptimeTeam/greptimedb-mcp-server](https://github.com/GreptimeTeam/greptimedb-mcp-server) 🐍 🏠 - 查詢 GreptimeDB 的 MCP 服務。
- [xing5/mcp-google-sheets](https://github.com/xing5/mcp-google-sheets) 🐍 ☁️ - 一個用於與 Google Sheets 交互的模型上下文協議伺服器。該伺服器通過 Google Sheets API 提供創建、讀取、更新和管理電子表格的工具。
- [freema/mcp-gsheets](https://github.com/freema/mcp-gsheets) 📇 ☁️ - 具有全面讀取、寫入、格式化和工作表管理功能的 Google Sheets API 整合 MCP 伺服器。
- [ydb/ydb-mcp](https://github.com/ydb-platform/ydb-mcp) 🎖️ 🐍 ☁️ – MCP 伺服器：用於與 [YDB](https://ydb.tech) 資料庫互動。

### 📊 <a name="data-platforms"></a>數據平台

用於資料整合、轉換和管道編排的資料平台。

- [flowcore/mcp-flowcore-platform](https://github.com/flowcore-io/mcp-flowcore-platform) 🎖️📇☁️🏠 - 與 Flowcore 互動以執行操作、提取資料並分析、交叉引用和利用您的資料核心或公共資料核心中的任何資料；全部用人類語言。

### 💻 <a name="developer-tools"></a>開發者工具

增強開發工作流程和環境管理的工具和集成。

- [Hypersequent/qasphere-mcp](https://github.com/Hypersequent/qasphere-mcp) 🎖️ 📇 ☁️ - 與[QA Sphere](https://qasphere.com/)測試管理系統整合，使LLM能夠發現、總結和操作測試用例，並可直接從AI驅動的IDE訪問
- [QuantGeekDev/docker-mcp](https://github.com/QuantGeekDev/docker-mcp) 🏎️ 🏠 - 通過 MCP 進行 Docker 容器管理和操作
- [zcaceres/fetch-mcp](https://github.com/zcaceres/fetch-mcp) 📇 🏠 - 一個靈活獲取 JSON、文本和 HTML 數據的 MCP 伺服器
- [r-huijts/xcode-mcp-server](https://github.com/r-huijts/xcode-mcp-server) 📇 🏠 🍎 - Xcode 集成，支援項目管理、文件操作和構建自動化
- [snaggle-ai/openapi-mcp-server](https://github.com/snaggle-ai/openapi-mcp-server) 🏎️ 🏠 - 使用開放 API 規範 (v3) 連接任何 HTTP/REST API 伺服器
- [jetbrains/mcpProxy](https://github.com/JetBrains/mcpProxy) 🎖️ 📇 🏠 - 連接到 JetBrains IDE
- [tumf/mcp-text-editor](https://github.com/tumf/mcp-text-editor) 🐍 🏠 - 面向行的文本文件編輯器。針對 LLM 工具進行了最佳化，具有高效的部分文件訪問功能，可最大限度地減少令牌使用量。
- [@joshuarileydev/simulator-mcp-server](https://github.com/JoshuaRileyDev/simulator-mcp-server) 📇 🏠 - 用於控制 iOS 模擬器的 MCP 伺服器
- [@joshuarileydev/app-store-connect-mcp-server](https://github.com/JoshuaRileyDev/app-store-connect-mcp-server) 📇 🏠 - 一個 MCP 伺服器，用於與 iOS 開發者的 App Store Connect API 進行通信
- [@sammcj/mcp-package-version](https://github.com/sammcj/mcp-package-version) 📦 🏠 - MCP 伺服器可幫助 LLM 在編寫程式碼時建議最新的穩定套裝軟體版本。
- [delano/postman-mcp-server](https://github.com/delano/postman-mcp-server) 📇 ☁️ - 與 [Postman API](https://www.postman.com/postman/postman-public-workspace/) 進行交互
- [vivekVells/mcp-pandoc](https://github.com/vivekVells/mcp-pandoc) 🗄️ 🚀 - 基於 Pandoc 的 MCP 伺服器，支援 Markdown、HTML、PDF、DOCX（.docx）、csv 等格式之間的無縫轉換
- [pskill9/website-downloader](https://github.com/pskill9/website-downloader) 🗄️ 🚀 - 這個 MCP 伺服器提供了使用 wget 下載完整網站的工具，可保留網站結構並轉換連結以支援本地訪問
- [j4c0bs/mcp-server-sql-analyzer](https://github.com/j4c0bs/mcp-server-sql-analyzer) 🐍 - 基於 [SQLGlot](https://github.com/tobymao/sqlglot) 的 MCP 伺服器，提供 SQL 分析、代碼檢查和方言轉換功能
- [Rootly-AI-Labs/Rootly-MCP-server](https://github.com/Rootly-AI-Labs/Rootly-MCP-server) 🎖️🐍☁️🍎 - 用於事件管理平台 Rootly](https://rootly.com/) 的 MCP 伺服器
- [YuChenSSR/mindmap-mcp-server](https://github.com/YuChenSSR/mindmap-mcp-server) 🐍 🏠 - 用於生成漂亮互動式心智圖mindmap的模型上下文協議（MCP）伺服器。
- [InhiblabCore/mcp-image-compression](https://github.com/InhiblabCore/mcp-image-compression) 🐍 🏠 - 用於本地壓縮各種圖片格式的 MCP 伺服器。
- [SDGLBL/mcp-claude-code](https://github.com/SDGLBL/mcp-claude-code) 🐍 🏠 - 使用 MCP 實現的 Claude Code 功能，支援 AI 代碼理解、修改和項目分析，並提供全面的工具支援。
- [ios-simulator-mcp](https://github.com/joshuayoes/ios-simulator-mcp) 📇 🏠 🍎 - 用於與 iOS 模擬器交互的模型上下文協議 (MCP) 伺服器。此伺服器允許您通過獲取有關 iOS 模擬器的資訊、控制 UI 交互和檢查 UI 元素來與 iOS 模擬器交互。
- [higress-group/higress-ops-mcp-server](https://github.com/higress-group/higress-ops-mcp-server) 🐍 🏠 - 支援對 [Higress](https://github.com/alibaba/higress/blob/main/README_ZH.md) 閘道器進行全面的配置和管理。
- [ReAPI-com/mcp-openapi](https://github.com/ReAPI-com/mcp-openapi) 📇 🏠 - MCP伺服器讓LLM能夠了解您的OpenAPI規範的所有資訊，以發現、解釋和生成代碼/模擬數據
- [automation-ai-labs/mcp-link](https://github.com/automation-ai-labs/mcp-link) 🏎️ 🏠 - 無縫集成任何 API 與 AI 代理（通過 OpenAPI 架構）
- [cjo4m06/mcp-shrimp-task-manager](https://github.com/cjo4m06/mcp-shrimp-task-manager) 📇 ☁️ 🏠 – 一個專為程式開發設計的任務管理系統，透過先進的任務記憶、自我反思與依賴管理，強化如 Cursor AI 等編碼代理的能力。[ShrimpTaskManager](https://cjo4m06.github.io/mcp-shrimp-task-manager)
- [axliupore/mcp-code-runner](https://github.com/axliupore/mcp-code-runner) 📇 🏠 - 一個MCP伺服器，用於在本地透過docker運行程式碼，並支援多種程式語言。
- [TencentEdgeOne/edgeone-pages-mcp](https://github.com/TencentEdgeOne/edgeone-pages-mcp) 📇 ☁️ - 基於 EdgeOne Pages 的 MCP 伺服器，支援代碼部署為在線頁面。
- [lpigeon/ros-mcp-server](https://github.com/lpigeon/ros-mcp-server) 🐍 🏠 🍎 🪟 🐧 - ROS MCP伺服器透過將使用者的自然語言指令轉換為ROS或ROS2控制指令，以支援機器人的控制。

### 🧮 數據科學工具

旨在簡化數據探索、分析和增強數據科學工作流程的集成和工具。

- [@reading-plus-ai/mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration) 🐍 ☁️ - 支援對基於 .csv 的數據集進行自主數據探索，以最小的成本提供智慧見解。
- [zcaceres/markdownify-mcp](https://github.com/zcaceres/markdownify-mcp) 📇 🏠 - 一個 MCP 伺服器，可將幾乎任何文件或網路內容轉換為 Markdown

### 📂 <a name="file-systems"></a>文件系統

提供對本地文件系統的直接訪問，並具有可配置的權限。使 AI 模型能夠讀取、寫入和管理指定目錄中的文件。

- [@modelcontextprotocol/server-filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) 📇 🏠 - 直接訪問本地文件系統。
- [@modelcontextprotocol/server-google-drive](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive) 📇 ☁️ - Google Drive 集成，用於列出、閱讀和搜尋文件
- [hmk/box-mcp-server](https://github.com/hmk/box-mcp-server) 📇 ☁️ - Box 集成，支援文件列表、閱讀和搜尋功能
- [mark3labs/mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server) 🏎️ 🏠 - 用於本地文件系統訪問的 Golang 實現。
- [mamertofabian/mcp-everything-search](https://github.com/mamertofabian/mcp-everything-search) 🐍 🏠 🪟 - 使用 Everything SDK 實現的快速 Windows 文件搜尋
- [cyberchitta/llm-context.py](https://github.com/cyberchitta/llm-context.py) 🐍 🏠 - 通過 MCP 或剪貼簿與 LLM 共享代碼上下文
- [Xuanwo/mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal) 🐍 🏠 ☁️ - 使用 Apache OpenDAL™ 訪問任何儲存
- [exoticknight/mcp-file-merger](https://github.com/exoticknight/mcp-file-merger) 📇 🏠 - 文件合併工具，適配AI Chat長度限制

### 💰 <a name="finance--fintech"></a>金融 & 金融科技

金融數據訪問和加密貨幣市場資訊。支援查詢即時市場數據、加密貨幣價格和財務分析。

- [QuantGeekDev/coincap-mcp](https://github.com/QuantGeekDev/coincap-mcp) 📇 ☁️ - 使用 CoinCap 的公共 API 集成即時加密貨幣市場數據，無需 API 金鑰即可訪問加密貨幣價格和市場資訊
- [anjor/coinmarket-mcp-server](https://github.com/anjor/coinmarket-mcp-server) 🐍 ☁️ - Coinmarket API 集成以獲取加密貨幣列表和報價
- [berlinbra/alpha-vantage-mcp](https://github.com/berlinbra/alpha-vantage-mcp) 🐍 ☁️ - Alpha Vantage API 集成，用於獲取股票和加密貨幣資訊
- [ferdousbhai/tasty-agent](https://github.com/ferdousbhai/tasty-agent) 🐍 ☁️ - Tastyworks API 集成，用於管理 Tastytrade 平台的交易活動
- [longportapp/openapi](https://github.com/longportapp/openapi/tree/main/mcp) - 🐍 ☁️ - LongPort OpenAPI 提供港美股等市場的股票即時行情數據，通過 MCP 提供 AI 接入分析、交易能力。
- [pwh-pwh/coin-mcp-server](https://github.com/pwh-pwh/coin-mcp-server) 🐍 ☁️ -  使用 Bitget 公共 API 去獲取加密貨幣最新價格
- [HuggingAGI/mcp-baostock-server](https://github.com/HuggingAGI/mcp-baostock-server) 🐍 ☁️ - 基於 baostock 的 MCP 伺服器,提供對中國股票市場數據的訪問和分析功能。
- [Wuye-AI/mcp-server-wuye-ai](https://github.com/wuye-ai/mcp-server-wuye-ai) 🎖️ 📇 ☁️ - 接入 CRIC物業AI 平台的 MCP 伺服器。CRIC物業AI 是克而瑞專為物業行業打造的智慧型 AI 助理。

### 🎮 <a name="gaming"></a>遊戲

遊戲相關數據和服務集成

- [rishijatia/fantasy-pl-mcp](https://github.com/rishijatia/fantasy-pl-mcp/) 🐍 ☁️ - 用於即時 Fantasy Premier League 數據和分析工具的 MCP 伺服器。
- [CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity) 📇 #️⃣ 🏠 - Unity3d 遊戲引擎集成 MCP 伺服器
- [opgginc/opgg-mcp](https://github.com/opgginc/opgg-mcp) 📇 ☁️ - 訪問英雄聯盟、雲頂之弈、無界英雄等熱門遊戲的即時遊戲數據，提供英雄分析、電競賽程、元組合和角色統計。

### 🧠 <a name="knowledge--memory"></a>知識與記憶

使用知識圖譜結構的持久記憶體儲存。使 AI 模型能夠跨會話維護和查詢結構化資訊。

- [@modelcontextprotocol/server-memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) 📇 🏠 - 基於知識圖譜的長期記憶系統用於維護上下文
- [/CheMiguel23/MemoryMesh](https://github.com/CheMiguel23/MemoryMesh) 📇 🏠 - 增強基於圖形的記憶，重點關注 AI 角色扮演和故事生成
- [/topoteretes/cognee](https://github.com/topoteretes/cognee/tree/dev/cognee-mcp) 📇 🏠 - AI應用程式和Agent的記憶體管理器使用各種圖儲存和向量儲存，並允許從 30 多個數據源提取數據
- [@hannesrudolph/mcp-ragdocs](https://github.com/hannesrudolph/mcp-ragdocs) 🐍 🏠 - MCP 伺服器實現提供了通過向量搜尋檢索和處理文件的工具，使 AI 助手能夠利用相關文件上下文來增強其響應能力
- [jinzcdev/markmap-mcp-server](https://github.com/jinzcdev/markmap-mcp-server) 📇 🏠 - 基於 [markmap](https://github.com/markmap/markmap) 構建的 MCP 伺服器，可將 **Markdown** 轉換為互動式的 **思維導圖**。支援多格式匯出（PNG/JPG/SVG）、瀏覽器即時預覽、一鍵複製 Markdown 和動態視覺化功能。
- [@kaliaboi/mcp-zotero](https://github.com/kaliaboi/mcp-zotero) 📇 ☁️ - 為 LLM 提供的連接器，用於操作 Zotero Cloud 上的文獻集合和資源
- [@mem0ai/mem0-mcp](https://github.com/mem0ai/mem0-mcp) 🐍 🏠 - 用於 Mem0 的模型上下文協議伺服器，幫助管理編碼偏好和模式，提供工具用於儲存、檢索和語義處理代碼實現、最佳實踐和技術文件，適用於 Cursor 和 Windsurf 等 IDE
- [@ragieai/mcp-server](https://github.com/ragieai/ragie-mcp-server) 📇 ☁️ - 從您的 [Ragie](https://www.ragie.ai) (RAG) 知識庫中檢索上下文，可連接至 Google Drive、Notion、JIRA 等多種整合服務。

### 🗺️ <a name="location-services"></a>位置服務

地理和基於位置的服務集成。支援訪問地圖數據、方向和位置資訊。

- [@modelcontextprotocol/server-google-maps](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps) 📇 ☁️ - Google 地圖集成，提供位置服務、路線規劃和地點詳細資訊
- [SecretiveShell/MCP-timeserver](https://github.com/SecretiveShell/MCP-timeserver) 🐍 🏠 - 訪問任意時區的時間並獲取當前本地時間
- [webcoderz/MCP-Geo](https://github.com/webcoderz/MCP-Geo) 🐍 🏠 - 支援 nominatim、ArcGIS、Bing 的地理編碼 MCP 伺服器
- [@briandconnelly/mcp-server-ipinfo](https://github.com/briandconnelly/mcp-server-ipinfo) 🐍 ☁️ - 使用 IPInfo API 獲取 IP 地址的地理位置和網路資訊

### 🎯 <a name="marketing"></a>行銷

用於創建和編輯行銷內容、處理網頁元數據、產品定位和編輯指南的工具。

- [Open Strategy Partners Marketing Tools](https://github.com/open-strategy-partners/osp_marketing_tools) 🐍 🏠 - Open Strategy Partners 提供的行銷工具套件，包含寫作風格指南、編輯規範和產品行銷價值圖譜創建工具

### 📊 <a name="monitoring"></a>監測

訪問和分析應用程式監控數據。使 AI 模型能夠審查錯誤報告和性能指標。

- [@modelcontextprotocol/server-sentry](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry) 🐍 ☁️ - Sentry.io 集成用於錯誤跟蹤和性能監控
- [@MindscapeHQ/server-raygun](https://github.com/MindscapeHQ/mcp-server-raygun) 📇 ☁️ - Raygun API V3 集成用於崩潰報告和真實用戶監控
- [metoro-io/metoro-mcp-server](https://github.com/metoro-io/metoro-mcp-server) 🎖️ 🏎️ ☁️ - 查詢並與 Metoro 監控的 kubernetes 環境交互
- [tumf/grafana-loki-mcp](https://github.com/tumf/grafana-loki-mcp) 🐍 🏠 - 一個 MCP 伺服器，允許透過 Grafana API 查詢 Loki 日誌。
- [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) 🎖️ 🐍 🏠 ☁️ - 在 Grafana 實例中搜尋儀錶板、調查事件並查詢數據源
- [seekrays/mcp-monitor](https://github.com/seekrays/mcp-monitor) 🏎️ 🏠 - 監控系統 CPU、Memory、Disk、Network、Host、Process 等資訊，並與 LLM 進行交互
- [VictoriaMetrics-Community/mcp-victoriametrics](https://github.com/VictoriaMetrics-Community/mcp-victoriametrics) 🎖️ 🏎️ 🏠 - 與 [VictoriaMetrics API](https://docs.victoriametrics.com/victoriametrics/url-examples/) 及[文檔](https://docs.victoriametrics.com/) 完整集成，監控你的 VictoriaMetrics 實例及排查問題。

### 🔎 <a name="search"></a>搜尋

- [scrapeless-ai/scrapeless-mcp-server](https://github.com/scrapeless-ai/scrapeless-mcp-server) 🐍 ☁️ - Scrapeless模型上下文協議服務作為MCP伺服器連接器，連接到Google SERP API，使得在MCP生態系統內無需離開即可進行網頁搜索。
- [@modelcontextprotocol/server-brave-search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) 📇 ☁️ - 使用 Brave 的搜尋 API 實現網頁搜尋功能
- [Dumpling-AI/mcp-server-dumplingai](https://github.com/Dumpling-AI/mcp-server-dumplingai) 🎖️ 📇 ☁️ - 通過 [Dumpling AI](https://www.dumplingai.com/) 提供的數據訪問、網頁抓取與文件轉換 API
- [@angheljf/nyt](https://github.com/angheljf/nyt) 📇 ☁️ - 使用 NYTimes API 搜尋文章
- [@modelcontextprotocol/server-fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) 🐍 🏠 ☁️ - 高效獲取和處理網頁內容，供 AI 使用
- [ac3xx/mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi) 📇 ☁️ - Kagi 搜尋 API 集成
- [exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) 🎖️ 📇 ☁️ – 模型上下文協議 (MCP) 伺服器讓 Claude 等 AI 助手可以使用 Exa AI Search API 進行網路搜尋。此設置允許 AI 模型以安全且可控的方式獲取即時網路資訊。
- [fatwang2/search1api-mcp](https://github.com/fatwang2/search1api-mcp) 📇 ☁️ - 通過 search1api 搜尋（需要付費 API 金鑰）
- [Tomatio13/mcp-server-tavily](https://github.com/Tomatio13/mcp-server-tavily) ☁️ 🐍 – Tavily AI 搜尋 API
- [kshern/mcp-tavily](https://github.com/kshern/mcp-tavily.git) ☁️ 📇 – Tavily AI 搜尋 API
- [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) ☁️ 🐍 - 搜尋 ArXiv 研究論文
- [mzxrai/mcp-webresearch](https://github.com/mzxrai/mcp-webresearch) 🔍📚 - 在 Google 上搜尋並對任何主題進行深度研究
- [andybrandt/mcp-simple-arxiv](https://github.com/andybrandt/mcp-simple-arxiv) - 🐍 ☁️  MCP for LLM 用於搜尋和閱讀 arXiv 上的論文)
- [andybrandt/mcp-simple-pubmed](https://github.com/andybrandt/mcp-simple-pubmed) - 🐍 ☁️  MCP 用於搜尋和閱讀 PubMed 中的醫學/生命科學論文。
- [apify/mcp-server-rag-web-browser](https://github.com/apify/mcp-server-rag-web-browser) 📇 ☁️ - 一個用於 Apify 的 RAG Web 瀏覽器 Actor 的 MCP 伺服器，可以執行網頁搜尋、抓取 URL，並以 Markdown 格式返回內容。
- [SecretiveShell/MCP-searxng](https://github.com/SecretiveShell/MCP-searxng) 🐍 🏠 - 用於連接到 searXNG 實例的 MCP 伺服器
- [Bigsy/Clojars-MCP-Server](https://github.com/Bigsy/Clojars-MCP-Server) 📇 ☁️ - Clojars MCP 伺服器，提供 Clojure 庫的最新依賴資訊
- [Ihor-Sokoliuk/MCP-SearXNG](https://github.com/ihor-sokoliuk/mcp-searxng) 📇 🏠/☁️ - [SearXNG](https://docs.searxng.org) 的模型上下文協議伺服器
- [erithwik/mcp-hn](https://github.com/erithwik/mcp-hn) 🐍 ☁️ - 一個用於搜尋 Hacker News、獲取熱門故事等的 MCP 伺服器。
- [chanmeng/google-news-mcp-server](https://github.com/ChanMeng666/server-google-news) 📇 ☁️ - Google News 集成，具有自動主題分類、多語言支援，以及通過 [SerpAPI](https://serpapi.com/) 提供的標題、故事和相關主題的綜合搜尋功能。
- [devflowinc/trieve](https://github.com/devflowinc/trieve/tree/main/clients/mcp-server) 🎖️📇☁️🏠 - 通過 [Trieve](https://trieve.ai) 爬取、嵌入、分塊、搜尋和檢索數據集中的資訊
- [zoomeye-ai/mcp_zoomeye](https://github.com/zoomeye-ai/mcp_zoomeye) 📇 ☁️ - 使用 ZoomEye API 搜尋全球網路空間資產
- [ConechoAI/openai-websearch-mcp](https://github.com/ConechoAI/openai-websearch-mcp/) 🐍 🏠 ☁️ - 將OpenAI內建的`web_search`工具封轉成MCP伺服器使用.
- [yamanoku/baseline-mcp-server](https://github.com/yamanoku/baseline-mcp-server) 📇 🏠 - 使用 Web Platform API 搜尋 Baseline 狀態的 MCP 伺服器

### 🔒 <a name="security"></a>安全

- [firstorderai/authenticator_mcp](https://github.com/firstorderai/authenticator_mcp) 📇 🏠 🍎 🪟 🐧 – 個安全的 MCP（Model Context Protocol）伺服器，使 AI 代理能與驗證器應用程式互動。
- [dnstwist MCP Server](https://github.com/BurtTheCoder/mcp-dnstwist) 📇🪟☁️ - dnstwist 的 MCP 伺服器，這是一個強大的 DNS 模糊測試工具，可幫助檢測域名搶註、釣魚和企業竊密行為
- [fosdickio/binary_ninja_mcp](https://github.com/Vector35/binaryninja-mcp) 🐍 🏠 🍎 🪟 🐧 - Binary Ninja 的 MCP 伺服器和橋接器。提供二進制分析和逆向工程工具。
- [Maigret MCP Server](https://github.com/BurtTheCoder/mcp-maigret) 📇 ☁️ - maigret 的 MCP 伺服器，maigret 是一款強大的 OSINT 工具，可從各種公共來源收集用戶帳戶資訊。此伺服器提供用於在社交網路中搜尋使用者名稱和分析 URL 的工具。
- [Shodan MCP Server](https://github.com/BurtTheCoder/mcp-shodan) 📇 ☁️ - MCP 伺服器用於查詢 Shodan API 和 Shodan CVEDB。此伺服器提供 IP 尋找、設備搜尋、DNS 尋找、漏洞查詢、CPE 尋找等工具。
- [VirusTotal MCP Server](https://github.com/BurtTheCoder/mcp-virustotal) 📇 ☁️ - 用於查詢 VirusTotal API 的 MCP 伺服器。此伺服器提供用於掃描 URL、分析文件哈希和檢索 IP 地址報告的工具。
- [ORKL MCP Server](https://github.com/fr0gger/MCP_Security) 📇🛡️☁️ - 用於查詢 ORKL API 的 MCP 伺服器。此伺服器提供獲取威脅報告、分析威脅行為者和檢索威脅情報來源的工具。
- [Security Audit MCP Server](https://github.com/qianniuspace/mcp-security-audit) 📇🛡️☁️ – 一個強大的 MCP (模型上下文協議) 伺服器，審計 npm 包依賴項的安全漏洞。內建遠端 npm 註冊表集成，以進行即時安全檢查。

### 🌎 <a name="translation-services"></a>翻譯服務

AI助手可以通過翻譯工具和服務在不同語言之間翻譯內容。

- [translated/lara-mcp](https://github.com/translated/lara-mcp) 🎖️ 📇 ☁️ - Lara翻譯API的MCP伺服器，提供強大的翻譯功能，支援語言檢測和上下文感知翻譯。

### 🚆 <a name="travel-and-transportation"></a>旅行與交通

訪問旅行和交通資訊。可以查詢時刻表、路線和即時旅行數據。

- [NS Travel Information MCP Server](https://github.com/r-huijts/ns-mcp-server) 📇 ☁️ - 了解荷蘭鐵路 (NS) 的旅行資訊、時刻表和即時更新
- [KyrieTangSheng/mcp-server-nationalparks](https://github.com/KyrieTangSheng/mcp-server-nationalparks) 📇 ☁️ - 美國國家公園管理局 API 集成，提供美國國家公園的詳細資訊、警報、遊客中心、露營地和活動的最新資訊

### 🔄 <a name="version-control"></a>版本控制

與 Git 儲存庫和版本控制平台交互。通過標準化 API 實現儲存庫管理、代碼分析、拉取請求處理、問題跟蹤和其他版本控制操作。

- [@modelcontextprotocol/server-github](https://github.com/modelcontextprotocol/servers/tree/main/src/github) 📇 ☁️ - GitHub API集成用於倉庫管理、PR、問題等
- [@modelcontextprotocol/server-gitlab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab) 📇 ☁️ 🏠 - GitLab平台集成用於項目管理和CI/CD操作
- [@modelcontextprotocol/server-git](https://github.com/modelcontextprotocol/servers/tree/main/src/git) 🐍 🏠 - 直接的Git倉庫操作，包括讀取、搜尋和分析本地倉庫
- [adhikasp/mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest) 🐍 🏠 - 使用 LLM 閱讀和分析 GitHub 儲存庫
- [kopfrechner/gitlab-mr-mcp](https://github.com/kopfrechner/gitlab-mr-mcp) 📇 ☁️ - 與 GitLab 項目問題和合併請求無縫互動。
- [Tiberriver256/mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops) 📇 ☁️ - Azure DevOps 集成，用於管理儲存庫、工作項目和管道。

### 🛠️ <a name="other-tools-and-integrations"></a>其他工具和集成

- [apify/actors-mcp-server](https://github.com/apify/actors-mcp-server) 📇 ☁️ - 使用超過 3,000 個預構建的雲工具（稱為 Actors）從網站、電商、社交媒體、搜尋引擎、地圖等提取數據。
- [githejie/mcp-server-calculator](https://github.com/githejie/mcp-server-calculator) 🐍 🏠 - 使LLM能夠使用計算機進行精確的數值計算
- [ivo-toby/contentful-mcp](https://github.com/ivo-toby/contentful-mcp) 📇 🏠 - 更新、創建、刪除 Contentful Space 中的內容、內容模型和資產
- [mzxrai/mcp-openai](https://github.com/mzxrai/mcp-openai) 📇 ☁️ - 與 OpenAI 最智慧的模型聊天
- [mrjoshuak/godoc-mcp](https://github.com/mrjoshuak/godoc-mcp) 🏎️ 🏠 - 高效的 Go 文件伺服器，讓 AI 助手可以智慧訪問包文件和類型，而無需閱讀整個源文件
- [pierrebrunelle/mcp-server-openai](https://github.com/pierrebrunelle/mcp-server-openai) 🐍 ☁️ - 直接從Claude查詢OpenAI模型，使用MCP協議
- [@modelcontextprotocol/server-everything](https://github.com/modelcontextprotocol/servers/tree/main/src/everything) 📇 🏠 - MCP伺服器，涵蓋MCP協議的所有功能
- [baba786/phabricator-mcp-server](https://github.com/baba786/phabricator-mcp-server) 🐍 ☁️ - 與Phabricator API交互
- [MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) 🐍 ☁️ 🏠 - 通過REST API與Obsidian交互
- [calclavia/mcp-obsidian](https://github.com/calclavia/mcp-obsidian) 📇 🏠 - 這是一個連接器，允許Claude Desktop（或任何MCP相容應用程式）讀取和搜尋包含Markdown筆記的目錄（如Obsidian庫）。
- [anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube) 📇 ☁️ - 獲取YouTube字幕
- [danhilse/notion_mcp](https://github.com/danhilse/notion_mcp) 🐍 ☁️ - 與Notion API集成，管理個人待辦事項列表
- [rusiaaman/wcgw](https://github.com/rusiaaman/wcgw/blob/main/src/wcgw/client/mcp_server/Readme.md) 🐍 🏠 - 自動化shell執行、電腦控制和編碼代理。（Mac）
- [reeeeemo/ancestry-mcp](https://github.com/reeeeemo/ancestry-mcp) 🐍 🏠 - 允許AI讀取.ged文件和基因數據
- [sirmews/apple-notes-mcp](https://github.com/sirmews/apple-notes-mcp) 🐍 🏠 - 允許AI讀取本地Apple Notes資料庫（僅限macOS）
- [anjor/coinmarket-mcp-server](https://github.com/anjor/coinmarket-mcp-server) 🐍 🏠 - Coinmarket API集成，用於獲取加密貨幣列表和報價
- [suekou/mcp-notion-server](https://github.com/suekou/mcp-notion-server) 📇 🏠 - 與Notion API交互
- [amidabuddha/unichat-mcp-server](https://github.com/amidabuddha/unichat-mcp-server) 🐍/📇 ☁️ - 使用MCP協議通過工具或預定義的提示發送請求給OpenAI、MistralAI、Anthropic、xAI或Google AI。需要供應商API金鑰
- [evalstate/mcp-miro](https://github.com/evalstate/mcp-miro) 📇 ☁️ - 訪問 MIRO 白板，批次創建和讀取項目。需要 REST API 的 OAUTH 金鑰。
- [fotoetienne/gqai](https://github.com/fotoetienne/gqai) 🏎 🏠 - 使用常規的 GraphQL 查詢/變異定義工具，gqai 將自動為您產生 MCP 伺服器。
- [KS-GEN-AI/jira-mcp-server](https://github.com/KS-GEN-AI/jira-mcp-server) 📇 ☁️ 🍎 🪟 - 通過 JQL 和 API 讀取 Jira 數據，並執行創建和編輯工單的請求
- [KS-GEN-AI/confluence-mcp-server](https://github.com/KS-GEN-AI/confluence-mcp-server) 📇 ☁️ 🍎 🪟 - 通過 CQL 獲取 Confluence 數據並閱讀頁面
- [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) 🐍 ☁️ - Confluence工作區的自然語言搜尋和內容訪問
- [pyroprompts/any-chat-completions-mcp](https://github.com/pyroprompts/any-chat-completions-mcp) - 與任何其他OpenAI SDK相容的聊天完成API對話，例如Perplexity、Groq、xAI等
- [anaisbetts/mcp-installer](https://github.com/anaisbetts/mcp-installer) 🐍 🏠 -  一個MCP伺服器，可以為您安裝其他MCP伺服器
- [tanigami/mcp-server-perplexity](https://github.com/tanigami/mcp-server-perplexity) 🐍 ☁️ - 與 Perplexity API 交互。
- [future-audiences/wikimedia-enterprise-model-context-protocol](https://gitlab.wikimedia.org/repos/future-audiences/wikimedia-enterprise-model-context-protocol) 🐍 ☁️  - 維基百科文章尋找 API
- [andybrandt/mcp-simple-timeserver](https://github.com/andybrandt/mcp-simple-timeserver) 🐍 🏠☁️ - MCP 伺服器允許檢查用戶端計算機上的本地時間或 NTP 伺服器上的當前 UTC 時間
- [andybrandt/mcp-simple-openai-assistant](https://github.com/andybrandt/mcp-simple-openai-assistant) - 🐍 ☁️  MCP 與 OpenAI 助手對話（Claude 可以使用任何 GPT 模型作為他的助手）
- [@evalstate/mcp-hfspace](https://github.com/evalstate/mcp-hfspace) 📇 ☁️ - 直接從 Claude 使用 HuggingFace Spaces。使用開源圖像生成、聊天、視覺任務等。支援圖像、音訊和文本上傳/下載。
- [zueai/mcp-manager](https://github.com/zueai/mcp-manager) 📇 ☁️ - 簡單的 Web UI 用於安裝和管理 Claude 桌面應用程式的 MCP 伺服器。
- [wong2/mcp-cli](https://github.com/wong2/mcp-cli) 📇 🏠 - 用於測試 MCP 伺服器的 CLI 工具
- [isaacwasserman/mcp-vegalite-server](https://github.com/isaacwasserman/mcp-vegalite-server) 🐍 🏠 - 使用 VegaLite 格式和渲染器從獲取的數據生成可視化效果。
- [tevonsb/homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp) 📇 🏠 - 訪問家庭助理數據和控制設備（燈、開關、恆溫器等）。
- [allenporter/mcp-server-home-assistant](https://github.com/allenporter/mcp-server-home-assistant) 🐍 🏠 - 通過模型上下文協議伺服器暴露所有 Home Assistant 語音意圖，實現智慧家居控制
- [nguyenvanduocit/all-in-one-model-context-protocol](https://github.com/nguyenvanduocit/all-in-one-model-context-protocol) 🏎️ 🏠 - 一些對開發人員有用的工具。
- [@joshuarileydev/mac-apps-launcher-mcp-server](https://github.com/JoshuaRileyDev/mac-apps-launcher) 📇 🏠 - 用於列出和啟動 MacOS 上的應用程式的 MCP 伺服器
- [ZeparHyfar/mcp-datetime](https://github.com/ZeparHyfar/mcp-datetime) - MCP 伺服器提供多種格式的日期和時間函數
- [apinetwork/piapi-mcp-server](https://github.com/apinetwork/piapi-mcp-server) 📇 ☁️ PiAPI MCP伺服器使用戶能夠直接從Claude或其他MCP相容應用程式中使用Midjourney/Flux/Kling/Hunyuan/Udio/Trellis生成媒體內容。
- [gotoolkits/DifyWorkflow](https://github.com/gotoolkits/mcp-difyworkflow-server) - 🚀 ☁️ MCP 伺服器 Tools 實現查詢與執行 Dify AI 平台上自訂的工作流
- [@pskill9/hn-server](https://github.com/pskill9/hn-server) - 📇 ☁️ 解析 news.ycombinator.com（Hacker News）的 HTML 內容，為不同類型的故事（熱門、最新、問答、展示、工作）提供結構化數據
- [@mediar-ai/screenpipe](https://github.com/mediar-ai/screenpipe) - 🎖️ 🦀 🏠 🍎 本地優先的系統，支援螢幕/音訊捕獲並帶有時間戳索引、SQL/嵌入儲存、語義搜尋、LLM 驅動的歷史分析和事件觸發動作 - 通過 NextJS 插件生態系統實現構建上下文感知的 AI 代理
- [akseyh/bear-mcp-server](https://github.com/akseyh/bear-mcp-server) - 允許 AI 讀取您的 Bear Notes（僅支援 macOS）
- [ws-mcp](https://github.com/nick1udwig/ws-mcp) - 使用 WebSocket 包裝 MCP 伺服器（用於 [kitbitz](https://github.com/nick1udwig/kibitz)）
- [AbdelStark/bitcoin-mcp](https://github.com/AbdelStark/bitcoin-mcp) - ₿ 一個模型上下文協議（MCP）伺服器，使 AI 模型能夠與比特幣交互，允許它們生成金鑰、驗證地址、解碼交易、查詢區塊鏈等
- [kj455/mcp-kibela](https://github.com/kj455/mcp-kibela) - 📇 ☁️ [Kibela](https://kibe.la/) 與 MCP 的集成
- [@awkoy/replicate-flux-mcp](https://github.com/awkoy/replicate-flux-mcp) 📇 ☁️ - 通過Replicate API提供圖像生成功能。
- [NakaokaRei/swift-mcp-gui](https://github.com/NakaokaRei/swift-mcp-gui.git) 🏠 🍏 - MCP伺服器，可以執行鍵盤輸入、滑鼠移動等命令
- [louiscklaw/hko-mcp](https://github.com/louiscklaw/hko-mcp) 📇 🏠 - MCP 伺服器，示範如何從香港天文台獲取天氣數據
- [kelvin6365/plane-mcp-server](https://github.com/kelvin6365/plane-mcp-server) - 🏎️ 🏠 此 MCP 伺服器將協助您透過 [Plane 的](https://plane.so) API 管理專案和問題
- [yuna0x0/hackmd-mcp](https://github.com/yuna0x0/hackmd-mcp) 📇 ☁️ - 允許 AI 模型與 [HackMD](https://hackmd.io) 交互
- [pwh-pwh/cal-mcp](https://github.com/pwh-pwh/cal-mcp) - MCP伺服器，可以計算數學表達式
- [tumf/web3-mcp](https://github.com/tumf/web3-mcp) 🐍 ☁️ - 包裝Ankr Advanced API的MCP伺服器實現。可以訪問以太坊、BSC、Polygon、Avalanche等多條區塊鏈上的NFT、代幣和區塊鏈數據。
- [ttommyth/interactive-mcp](https://github.com/ttommyth/interactive-mcp) 📇 🏠 🍎 🪟 🐧 - 透過在 MCP 循環中直接加入本機使用者提示和聊天功能，啟用互動式 LLM 工作流程。
- [caol64/wenyan-mcp](https://github.com/caol64/wenyan-mcp) 📇 🏠 🍎 🪟 🐧 - 文顏 MCP Server，讓 AI 將 Markdown 文章自動排版後發佈至微信公眾號。

## 框架
- [FastMCP](https://github.com/jlowin/fastmcp) 🐍 - 用於在 Python 中構建 MCP 伺服器的高級框架
- [FastMCP](https://github.com/punkpeye/fastmcp) 📇 - 用於在 TypeScript 中構建 MCP 伺服器的高級框架
- [Foxy Contexts](https://github.com/strowk/foxy-contexts) 🏎️ - 用於以聲明方式編寫 MCP 伺服器的 Golang 庫，包含功能測試
- [Genkit MCP](https://github.com/firebase/genkit/tree/main/js/plugins/mcp) 📇 – 提供[Genkit](https://github.com/firebase/genkit/tree/main)與模型上下文協議（MCP）之間的集成。
- [LiteMCP](https://github.com/wong2/litemcp) ⚡️ - 用於在 JavaScript/TypeScript 中構建 MCP 伺服器的高級框架
- [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go) 🏎️ - 用於構建MCP伺服器和用戶端的Golang SDK。
- [mcp-framework](https://github.com/QuantGeekDev/mcp-framework) - ⚡️ 用於構建 MCP 伺服器的快速而優雅的 TypeScript 框架
- [mcp-proxy](https://github.com/punkpeye/mcp-proxy) 📇 - 用於使用 `stdio` 傳輸的 MCP 伺服器的 TypeScript SSE 代理
- [mcp-rs-template](https://github.com/linux-china/mcp-rs-template) 🦀 - Rust的MCP CLI伺服器模板
- [metoro-io/mcp-golang](https://github.com/metoro-io/mcp-golang) 🏎️ - 用於構建 MCP 伺服器的 Golang 框架，專注於類型安全。
- [rectalogic/langchain-mcp](https://github.com/rectalogic/langchain-mcp) 🐍 - 提供LangChain中MCP工具呼叫支援，允許將MCP工具集成到LangChain工作流中。
- [salty-flower/ModelContextProtocol.NET](https://github.com/salty-flower/ModelContextProtocol.NET) #️⃣🏠 - 基於 .NET 9 的 C# MCP 伺服器 SDK ，支援 NativeAOT ⚡ 🔌
- [spring-ai-mcp](https://github.com/spring-projects-experimental/spring-ai-mcp) ☕ 🌱 - 用於構建 MCP 用戶端和伺服器的 Java SDK 和 Spring Framework 集成，支援多種可插拔的傳輸選項
- [@marimo-team/codemirror-mcp](https://github.com/marimo-team/codemirror-mcp) - CodeMirror 擴展，實現了用於資源提及和提示命令的模型上下文協議 (MCP)
- [mullerhai/sakura-mcp](https://github.com/mullerhai/sakura-mcp) 🦀 ☕ 🔌 - Scala MCP 框架 構建企業級MCP用戶端和服務端 shade from modelcontextprotocol.io.
  
## 實用工具

- [boilingdata/mcp-server-and-gw](https://github.com/boilingdata/mcp-server-and-gw) 📇 - 帶有範例伺服器和 MCP 用戶端的 MCP stdio 到 HTTP SSE 傳輸閘道器
- [isaacwasserman/mcp-langchain-ts-client](https://github.com/isaacwasserman/mcp-langchain-ts-client) 📇 - 在 LangChain.js 中使用 MCP 提供的工具
- [lightconetech/mcp-gateway](https://github.com/lightconetech/mcp-gateway) 📇 - MCP SSE 伺服器的閘道器示範
- [mark3labs/mcphost](https://github.com/mark3labs/mcphost) 🏎️ - 一個 CLI 主機應用程式，使大型語言模型 (LLM) 能夠通過模型上下文協議 (MCP) 與外部工具交互
- [MCP-Connect](https://github.com/EvalsOne/MCP-Connect) 📇 - 一個小工具，使基於雲的 AI 服務能夠通過 HTTP/HTTPS 請求訪問本地的基於 Stdio 的 MCP 伺服器
- [SecretiveShell/MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge) 🐍 - OpenAI 中間件代理，用於在任何現有的 OpenAI 相容用戶端中使用 MCP
- [sparfenyuk/mcp-proxy](https://github.com/sparfenyuk/mcp-proxy) 🐍 - MCP stdio 到 SSE 的傳輸閘道器
- [upsonic/gpt-computer-assistant](https://github.com/Upsonic/gpt-computer-assistant) 🐍 - 用於構建垂直 AI 代理的框架
- [TBXark/mcp-proxy](https://github.com/TBXark/mcp-proxy) 🏎️ - 一個通過單個HTTP伺服器聚合併服務多個MCP資源伺服器的MCP代理伺服器。
- [yikakia/godoc-mcp-server](https://github.com/yikakia/godoc-mcp-server) 🏎️ ☁️ 🪟 🐧 🍎 - 查詢 pkg.go.dev 上的 golang 包資訊


## 用戶端

> [!NOTE]
> 尋找 MCP 用戶端？請查看 [awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients/) 倉庫。


## 提示和技巧

### 官方提示關於 LLM 如何使用 MCP

想讓 Claude 回答有關模型上下文協議的問題？

創建一個項目，然後將此文件添加到其中：

https://modelcontextprotocol.io/llms-full.txt

這樣 Claude 就能回答關於編寫 MCP 伺服器及其工作原理的問題了

- https://www.reddit.com/r/ClaudeAI/comments/1h3g01r/want_to_ask_claude_about_model_context_protocol/

## 收藏歷史

<a href="https://star-history.com/#punkpeye/awesome-mcp-servers&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date" />
 </picture>
</a>
