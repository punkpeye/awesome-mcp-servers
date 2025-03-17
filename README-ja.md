# 素晴らしいMCPサーバー [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![中文文档](https://img.shields.io/badge/中文文档-点击查看-orange)](README-zh.md)
[![日本語](https://img.shields.io/badge/日本語-クリック-青)](README-ja.md)
[![Discord](https://img.shields.io/discord/1312302100125843476?logo=discord&label=discord)](https://glama.ai/mcp/discord)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/mcp?style=flat&logo=reddit&label=subreddit)](https://www.reddit.com/r/mcp/)

素晴らしいモデルコンテキストプロトコル（MCP）サーバーの厳選リスト。

* [MCPとは何ですか？](#MCPとは何ですか？)
* [チュートリアル](#チュートリアル)
* [コミュニティ](#コミュニティ)
* [凡例](#凡例)
* [サーバー実装](#サーバー実装)
* [フレームワーク](#フレームワーク)
* [ヒントとコツ](#ヒントとコツ)

## MCPとは何ですか？

[MCP](https://modelcontextprotocol.io/) は、標準化されたサーバー実装を通じて、AIモデルがローカルおよびリモートリソースと安全に対話できるようにするオープンプロトコルです。このリストは、ファイルアクセス、データベース接続、API統合、その他のコンテキストサービスを通じてAIの機能を拡張する、実運用および実験的なMCPサーバーに焦点を当てています。

## チュートリアル

* [モデルコンテキストプロトコル (MCP) クイックスタート](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
* [SQLiteデータベースを使用するためのClaudeデスクトップアプリのセットアップ](https://youtu.be/wxCCzo9dGj0)

## コミュニティ

* [r/mcp Reddit](https://www.reddit.com/r/mcp)
* [Discordサーバー](https://glama.ai/mcp/discord)

## 凡例

* 🎖️ – 公式実装
* 🐍 – Pythonコードベース
* 📇 – TypeScriptコードベース
* 🏎️ – Goコードベース
* #️⃣ – C#コードベース
* ☁️ - クラウドサービス
* 🏠 - ローカルサービス

## サーバー実装

* 📂 - [ブラウザ自動化](#browser-automation)
* ☁️ - [クラウドプラットフォーム](#cloud-platforms)
* 💬 - [コミュニケーション](#communication)
* 👤 - [顧客データプラットフォーム](#customer-data-platforms)
* 🗄️ - [データベース](#databases)
* 🛠️ - [開発者ツール](#developer-tools)
* 📂 - [ファイルシステム](#file-systems)
* 🧠 - [知識と記憶](#knowledge--memory)
* 🗺️ - [位置情報サービス](#location-services)
* 📊 - [監視](#monitoring)
* 🔎 - [検索](#search)
* 🔄 - [旅行と交通](#travel-and-transportation)
* 🔄 - [バージョン管理](#version-control)
* 🛠️ - [その他のツールと統合](#other-tools-and-integrations)

### 📂 <a name="browser-automation"></a>ブラウザ自動化

Webコンテンツのアクセスと自動化機能。AIに優しい形式でWebコンテンツを検索、スクレイピング、処理することができます。

- [@executeautomation/playwright-mcp-server](https://github.com/executeautomation/mcp-playwright) 🌐⚡️ - Playwrightを使用したブラウザ自動化とWebスクレイピングのためのMCPサーバー
- [@automatalabs/mcp-server-playwright](https://github.com/Automata-Labs-team/MCP-Server-Playwright) 🌐🖱️ - Playwrightを使用したブラウザ自動化のためのMCPサーバー
- [@modelcontextprotocol/server-puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) 📇 🏠 - Webスクレイピングとインタラクションのためのブラウザ自動化
- [@kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) 📇 ☁️ - AI分析のためのYouTube字幕とトランスクリプトの取得
- [@kimtth/mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing) 🐍 🏠 - Azure OpenAIとPlaywrightを使用した「最小限の」サーバー/クライアントMCP実装。

### ☁️ <a name="cloud-platforms"></a>クラウドプラットフォーム

クラウドプラットフォームサービスの統合。クラウドインフラストラクチャとサービスの管理と対話を可能にします。

- [Cloudflare MCP Server](https://github.com/cloudflare/mcp-server-cloudflare) 🎖️ 📇 ☁️ - Workers、KV、R2、D1を含むCloudflareサービスとの統合
- [Kubernetes MCP Server](https://github.com/strowk/mcp-k8s-go) - 🏎️ ☁️ MCPを通じたKubernetesクラスター操作

### 💬 <a name="communication"></a>コミュニケーション

メッセージ管理とチャネル操作のためのコミュニケーションプラットフォームとの統合。AIモデルがチームコミュニケーションツールと対話できるようにします。

- [@modelcontextprotocol/server-slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack) 📇 ☁️ - チャネル管理とメッセージングのためのSlackワークスペース統合
- [@modelcontextprotocol/server-bluesky](https://github.com/keturiosakys/bluesky-context-server) 📇 ☁️ - クエリとインタラクションのためのBlueskyインスタンス統合
- [MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite) - 🐍 ☁️ - GmailとGoogleカレンダーとの統合。
- [gotoolkits/wecombot](https://github.com/gotoolkits/mcp-wecombot-server.git) - 🚀 ☁️  - MCPサーバーアプリケーションは、WeComグループロボットにさまざまなタイプのメッセージを送信します。
- [sawa-zen/vrchat-mcp](https://github.com/sawa-zen/vrchat-mcp) - 📇 🏠 VRChat APIと対話するためのMCPサーバーです。VRChatのフレンドやワールド、アバターなどの情報を取得することができます。

### 👤 <a name="customer-data-platforms"></a>顧客データプラットフォーム

顧客データプラットフォーム内の顧客プロファイルへのアクセスを提供します。

- [sergehuber/inoyu-mcp-unomi-server](https://github.com/sergehuber/inoyu-mcp-unomi-server) 📇 ☁️ - Apache Unomi CDPサーバー上のプロファイルにアクセスし、更新するためのMCPサーバー。

### 🗄️ <a name="databases"></a>データベース

スキーマ検査機能を備えた安全なデータベースアクセス。読み取り専用アクセスを含む構成可能なセキュリティ制御を使用してデータをクエリおよび分析することができます。

- [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) 🐍 🏠 - MCPサーバーの実装で、Elasticsearchとのインタラクションを提供します
- [domdomegg/airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server) 📇 🏠 - スキーマ検査、読み取り/書き込み機能を備えた Airtable データベース統合
- [LucasHild/mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery) 🐍 ☁️ - スキーマ検査とクエリ機能を備えたBigQueryデータベース統合
- [ergut/mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server) 📇 ☁️ - Google BigQuery統合のためのサーバー実装で、直接的なBigQueryデータベースアクセスとクエリ機能を提供
- [designcomputer/mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server) 🐍 🏠 - 構成可能なアクセス制御、スキーマ検査、包括的なセキュリティガイドラインを備えたMySQLデータベース統合
- [@modelcontextprotocol/server-postgres](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) 📇 🏠 - スキーマ検査とクエリ機能を備えたPostgreSQLデータベース統合
- [@modelcontextprotocol/server-sqlite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) 🐍 🏠 - 組み込みの分析機能を備えたSQLiteデータベース操作
- [@joshuarileydev/supabase-mcp-server](https://github.com/joshuarileydev/supabase) - Supabaseでプロジェクトと組織を管理および作成するためのSupabase MCPサーバー
- [ktanaka101/mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb) 🐍 🏠 - スキーマ検査とクエリ機能を備えたDuckDBデータベース統合
- [QuantGeekDev/mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp) 📇 🏠 - LLMがデータベースと直接対話できるようにするMongoDB統合。
- [tinybirdco/mcp-tinybird](https://github.com/tinybirdco/mcp-tinybird) 🐍 ☁️ - クエリとAPI機能を備えたTinybird統合
- [kiliczsh/mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server) 📇 🏠 - MongoDBのためのモデルコンテキストプロトコルサーバー
- [KashiwaByte/vikingdb-mcp-server](https://github.com/KashiwaByte/vikingdb-mcp-server) 🐍 ☁️ - コレクションとインデックスの紹介、ベクトルストアと検索機能を備えたVikingDB統合。
- [runekaagaard/mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy) 🐍 🏠 - PostgreSQL、MySQL、MariaDB、SQLite、Oracle、MS SQL Serverなど多数のデータベースをサポートするSQLAlchemyベースの汎用データベース統合。スキーマと関係の検査、大規模データセット分析機能を備えています。

### 💻 <a name="developer-tools"></a>開発者ツール

開発ワークフローと環境管理を強化するツールと統合。

- [QuantGeekDev/docker-mcp](https://github.com/QuantGeekDev/docker-mcp) 🏎️ 🏠 - MCPを通じたDockerコンテナの管理と操作
- [zcaceres/fetch-mcp](https://github.com/zcaceres/fetch-mcp) 📇 🏠 - JSON、テキスト、HTMLデータを柔軟に取得するためのMCPサーバー
- [zcaceres/gtasks-mcp](https://github.com/zcaceres/gtasks-mcp) - 📇 ☁️ - Google タスクを管理するための MCP サーバー
- [snaggle-ai/openapi-mcp-server](https://github.com/snaggle-ai/openapi-mcp-server) 🏎️ 🏠 - Open API spec (v3) を使用して任意のHTTP/REST APIサーバーに接続
- [@joshuarileydev/terminal-mcp-server](https://www.npmjs.com/package/@joshuarileydev/terminal-mcp-server) 📇 🏠 - 任意のシェルターミナルコマンドを実行するためのMCPサーバー
- [tumf/mcp-text-editor](https://github.com/tumf/mcp-text-editor) - ラインエディタ 行単位の取得と編集ができるので、特に大きなファイルの一部書き換えを効率的に行う
- [ferrislucas/iterm-mcp](https://github.com/ferrislucas/iterm-mcp) 🖥️ 🛠️ 💬 - iTermへのアクセスを提供するモデルコンテキストプロトコルサーバー。コマンドを実行し、iTermターミナルで見た内容について質問することができます。

### 📂 <a name="file-systems"></a>ファイルシステム

構成可能な権限を備えたローカルファイルシステムへの直接アクセスを提供します。指定されたディレクトリ内のファイルを読み取り、書き込み、管理することができます。

- [@modelcontextprotocol/server-filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) 📇 🏠 - ローカルファイルシステムへの直接アクセス。
- [@modelcontextprotocol/server-google-drive](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive) 📇 ☁️ - ファイルのリスト、読み取り、検索のためのGoogle Drive統合
- [mark3labs/mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server) 🏎️ 🏠 - ローカルファイルシステムアクセスのためのGolang実装。
- [Xuanwo/mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal) 🐍 🏠 ☁️ - Apache OpenDAL™ でどのストレージにもアクセスできます

### 🧠 <a name="knowledge--memory"></a>知識と記憶

知識グラフ構造を使用した永続的なメモリストレージ。セッション間で構造化情報を維持およびクエリすることができます。

- [@modelcontextprotocol/server-memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) 📇 🏠 - コンテキストを維持するための知識グラフベースの長期記憶システム
- [/CheMiguel23/MemoryMesh](https://github.com/CheMiguel23/MemoryMesh) 📇 🏠 - AIロールプレイとストーリー生成に焦点を当てた強化されたグラフベースのメモリ

### 🗺️ <a name="location-services"></a>位置情報サービス

地理および位置ベースのサービス統合。地図データ、方向、および場所情報へのアクセスを提供します。

- [@modelcontextprotocol/server-google-maps](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps) 📇 ☁️ - 位置情報サービス、ルート計画、および場所の詳細のためのGoogle Maps統合

### 📊 <a name="monitoring"></a>監視

アプリケーション監視データへのアクセスと分析。エラーレポートとパフォーマンスメトリクスをレビューすることができます。

- [@modelcontextprotocol/server-sentry](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry) 🐍 ☁️ - エラートラッキングとパフォーマンス監視のためのSentry.io統合
- [@modelcontextprotocol/server-raygun](https://github.com/MindscapeHQ/mcp-server-raygun) 📇 ☁️ - クラッシュレポートとリアルユーザーモニタリングのためのRaygun API V3統合

### 🔎 <a name="search"></a>検索

- [@modelcontextprotocol/server-brave-search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) 📇 ☁️ - Braveの検索APIを使用したWeb検索機能
- [@angheljf/nyt](https://github.com/angheljf/nyt) 📇 ☁️ - NYTimes APIを使用して記事を検索
- [@modelcontextprotocol/server-fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) 🐍 🏠 ☁️ - AI消費のための効率的なWebコンテンツの取得と処理
- [ac3xx/mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi) 📇 ☁️ - Kagi検索API統合
- [theishangoswami/exa-mcp-server](https://github.com/theishangoswami/exa-mcp-server) 📇 ☁️ - Exa AI検索API
- [exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) 🎖️ 📇 ☁️ – モデルコンテキストプロトコル（MCP）サーバーは、ClaudeなどのAIアシスタントがExa AI検索APIを使用してWeb検索を行うことを可能にします。この設定により、AIモデルは安全かつ制御された方法でリアルタイムのWeb情報を取得できます。
- [fatwang2/search1api-mcp](https://github.com/fatwang2/search1api-mcp) 📇 ☁️ - search1apiを介した検索（有料APIキーが必要）
- [Tomatio13/mcp-server-tavily](https://github.com/Tomatio13/mcp-server-tavily) ☁️ 🐍 – Tavily AI検索API
- [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) ☁️ 🐍 - ArXiv研究論文を検索
- [mzxrai/mcp-webresearch](https://github.com/mzxrai/mcp-webresearch) 🔍📚 - Googleを検索し、任意のトピックに関する深いWebリサーチを行う
- [andybrandt/mcp-simple-arxiv](https://github.com/andybrandt/mcp-simple-arxiv) - 🐍 ☁️  MCPを使用してLLMがArXivの論文を検索および読む
- [apify/mcp-server-rag-web-browser](https://github.com/apify/mcp-server-rag-web-browser) 📇 ☁️ - Apify の RAG Web Browser Actor 用の MCP サーバーで、ウェブ検索を実行し、URL をスクレイピングし、Markdown 形式でコンテンツを返します。
- [Ihor-Sokoliuk/MCP-SearXNG](https://github.com/ihor-sokoliuk/mcp-searxng) 📇 🏠/☁️ - [SearXNG](https://docs.searxng.org)のモデルコンテキストプロトコルサーバー
- [erithwik/mcp-hn](https://github.com/erithwik/mcp-hn) 🐍 ☁️ - Hacker Newsの検索、トップストーリーの取得などを行うMCPサーバー。
- [chanmeng/google-news-mcp-server](https://github.com/ChanMeng666/server-google-news) 📇 ☁️ - 自動トピック分類、多言語サポート、[SerpAPI](https://serpapi.com/)を通じたヘッドライン、ストーリー、関連トピックの包括的な検索機能を備えたGoogle News統合。

### 🔒 <a name="security"></a>セキュリティ

- [Security Audit MCP Server](https://github.com/qianniuspace/mcp-security-audit) 📇🛡️☁️ 強力なモデルコンテキストプロトコル（MCP）サーバーで、npmパッケージ依存関係のセキュリティ脆弱性を監査します。リモートnpmレジストリ統合を備えたリアルタイムセキュリティチェックを使用して構築されています。

### 🚆 <a name="travel-and-transportation"></a>旅行と交通

旅行および交通情報へのアクセス。スケジュール、ルート、およびリアルタイムの旅行データをクエリすることができます。

- [NS Travel Information MCP Server](https://github.com/r-huijts/ns-mcp-server) 📇 ☁️ - オランダ鉄道（NS）の旅行情報、スケジュール、およびリアルタイムの更新にアクセス

### 🔄 <a name="version-control"></a>バージョン管理

Gitリポジトリおよびバージョン管理プラットフォームとの対話。標準化されたAPIを通じて、リポジトリ管理、コード分析、プルリクエスト処理、問題追跡、およびその他のバージョン管理操作を実行できます。

- [@modelcontextprotocol/server-github](https://github.com/modelcontextprotocol/servers/tree/main/src/github) 📇 ☁️ - リポジトリ管理、PR、問題などのためのGitHub API統合
- [@modelcontextprotocol/server-gitlab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab) 📇 ☁️ 🏠 - プロジェクト管理およびCI/CD操作のためのGitLabプラットフォーム統合
- [@modelcontextprotocol/server-git](https://github.com/modelcontextprotocol/servers/tree/main/src/git) 🐍 🏠 - ローカルリポジトリの読み取り、検索、および分析を含む直接的なGitリポジトリ操作

### 🛠️ <a name="other-tools-and-integrations"></a>その他のツールと統合

- [apify/actors-mcp-server](https://github.com/apify/actors-mcp-server) 📇 ☁️ - 3,000以上の事前構築されたクラウドツール（Actors として知られる）を使用して、ウェブサイト、eコマース、ソーシャルメディア、検索エンジン、地図などからデータを抽出できます。
- [zcaceres/markdownify-mcp](https://github.com/zcaceres/markdownify-mcp) 📇 🏠 - ほぼすべてのファイルやウェブコンテンツをMarkdownに変換するMCPサーバー
- [mzxrai/mcp-openai](https://github.com/mzxrai/mcp-openai) 📇 ☁️ - OpenAIの最も賢いモデルとチャット
- [mrjoshuak/godoc-mcp](https://github.com/mrjoshuak/godoc-mcp) 🏎️ 🏠 - Goドキュメントサーバーで、AIアシスタントがパッケージドキュメントとタイプにスマートにアクセスできるようにします。
- [pierrebrunelle/mcp-server-openai](https://github.com/pierrebrunelle/mcp-server-openai) 🐍 ☁️ - MCPプロトコルを使用してClaudeから直接OpenAIモデルにクエリを送信
- [@modelcontextprotocol/server-everything](https://github.com/modelcontextprotocol/servers/tree/main/src/everything) 📇 🏠 - MCPプロトコルのすべての機能を実行するMCPサーバー
- [baba786/phabricator-mcp-server](https://github.com/baba786/phabricator-mcp-server) 🐍 ☁️ - Phabricator APIとの対話
- [MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) 🐍 ☁️ 🏠 - REST APIを介してObsidianと対話
- [calclavia/mcp-obsidian](https://github.com/calclavia/mcp-obsidian) 📇 🏠 - これは、Claude Desktop（または任意のMCPクライアント）がMarkdownノートを含むディレクトリ（Obsidianボールトなど）を読み取り、検索できるようにするコネクタです。
- [anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube) 📇 ☁️ - YouTube字幕の取得
- [danhilse/notion_mcp](https://github.com/danhilse/notion_mcp) 🐍 ☁️ - NotionのAPIと統合して個人のToDoリストを管理
- [rusiaaman/wcgw](https://github.com/rusiaaman/wcgw/blob/main/src/wcgw/client/mcp_server/Readme.md) 🐍 🏠 - 自律的なシェル実行、コンピュータ制御、およびコーディングエージェント。（Mac）
- [reeeeemo/ancestry-mcp](https://github.com/reeeeemo/ancestry-mcp) 🐍 🏠 - AIが.gedファイルと遺伝データを読み取ることができるようにします。
- [sirmews/apple-notes-mcp](https://github.com/sirmews/apple-notes-mcp) 🐍 🏠 - AIがローカルのApple Notesデータベースから読み取ることができるようにします（macOSのみ）
- [anjor/coinmarket-mcp-server](https://github.com/anjor/coinmarket-mcp-server) 🐍 🏠 - 暗号通貨のリストと見積もりを取得するためのCoinmarket API統合
- [suekou/mcp-notion-server](https://github.com/suekou/mcp-notion-server) 📇 🏠 - Notion APIとの対話
- [amidabuddha/unichat-mcp-server](https://github.com/amidabuddha/unichat-mcp-server) 🐍/📇 ☁️ - MCPプロトコルを使用してOpenAI、MistralAI、Anthropic、xAI、またはGoogle AIにリクエストを送信するためのツールまたは事前定義されたプロンプト。ベンダーAPIキーが必要
- [g0t4/mcp-server-commands](https://github.com/g0t4/mcp-server-commands) 📇 🏠 - コマンドを実行し、その出力を含める。ツールとプロンプト。
- [evalstate/mcp-miro](https://github.com/evalstate/mcp-miro) 📇 ☁️ - MIROホワイトボードにアクセスし、アイテムを一括作成および読み取り。REST APIのOAUTHキーが必要。
- [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) 🐍 ☁️ - Confluenceワークスペースの自然言語検索とコンテンツアクセス
- [pyroprompts/any-chat-completions-mcp](https://github.com/pyroprompts/any-chat-completions-mcp) - Perplexity、Groq、xAIなどの他のOpenAI SDK互換のチャット完了APIとチャット
- [anaisbetts/mcp-installer](https://github.com/anaisbetts/mcp-installer) 🐍 🏠 - 他のMCPサーバーをインストールするMCPサーバー。
- [tanigami/mcp-server-perplexity](https://github.com/tanigami/mcp-server-perplexity) 🐍 ☁️ - Perplexity APIとの対話。
- [future-audiences/wikimedia-enterprise-model-context-protocol](https://gitlab.wikimedia.org/repos/future-audiences/wikimedia-enterprise-model-context-protocol) 🐍 ☁️  - Wikipedia記事検索API
- [andybrandt/mcp-simple-timeserver](https://github.com/andybrandt/mcp-simple-timeserver) 🐍 🏠☁️ - クライアントマシンのローカル時間またはNTPサーバーからの現在のUTC時間を確認するためのMCPサーバー
- [andybrandt/mcp-simple-openai-assistant](https://github.com/andybrandt/mcp-simple-openai-assistant) - 🐍 ☁️  MCPを使用してOpenAIアシスタントと対話（Claudeは任意のGPTモデルをアシスタントとして使用できます）
- [@joshuarileydev/simulator-mcp-server](https://www.npmjs.com/package/@joshuarileydev/simulator-mcp-server) - 📇 🏠 iOSシミュレータを制御し、シミュレータを起動し、アプリをインストール/起動するためのMCPサーバー。
- [tumf/mcp-shell-server](https://github.com/tumf/mcp-shell-server) シェルからホワイトリストにあるコマンドを実行して結果を返すMCPサーバ
- [apinetwork/piapi-mcp-server](https://github.com/apinetwork/piapi-mcp-server) 📇 ☁️ PiAPI MCPサーバーは、ユーザーがClaudeや他のMCP互換アプリから直接Midjourney/Flux/Kling/Hunyuan/Udio/Trellisでメディアコンテンツを生成することを可能にします。
- [gotoolkits/DifyWorkflow](https://github.com/gotoolkits/mcp-difyworkflow-server) - 🚀 ☁️ MCP サーバーの Tools を使用して、Dify AI プラットフォーム上でカスタムされたワークフローを検索および実行する
- [boilingdata/mcp-server-and-gw](https://github.com/boilingdata/mcp-server-and-gw) サンプルサーバーとMCPクライアントを備えたMCP stdioからHTTP SSEへのトランスポートゲートウェイ。
- [lightconetech/mcp-gateway](https://github.com/lightconetech/mcp-gateway) MCP SSEサーバーのゲートウェイデモ。
- [sparfenyuk/mcp-proxy](https://github.com/sparfenyuk/mcp-proxy) 🐍 MCP stdioからSSEへのトランスポートゲートウェイ。
- [NON906/omniparser-autogui-mcp](https://github.com/NON906/omniparser-autogui-mcp) 🐍 - 画面上のGUIの自動操作
- [kj455/mcp-kibela](https://github.com/kj455/mcp-kibela) - 📇 ☁️ [Kibela](https://kibe.la/)との連携

## フレームワーク

- [Genkit MCP](https://github.com/firebase/genkit/tree/main/js/plugins/mcp) 📇 – [Genkit](https://github.com/firebase/genkit/tree/main) とモデルコンテキストプロトコル（MCP）との統合を提供します。
- [@modelcontextprotocol/server-langchain](https://github.com/rectalogic/langchain-mcp) 🐍 - LangChainでのMCPツール呼び出しサポートを提供し、LangChainワークフローにMCPツールを統合できるようにします。
- [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go) 🏎️ - MCPサーバーとクライアントを構築するためのGolang SDK。
- [FastMCP](https://github.com/jlowin/fastmcp) 🐍 - PythonでMCPサーバーを構築するための高レベルフレームワーク
- [mcp-rs-template](https://github.com/linux-china/mcp-rs-template) 🦀 - RustのためのMCP CLIサーバーテンプレート
- [Foxy Contexts](https://github.com/strowk/foxy-contexts) 🏎️ - 機能テストを含む宣言的にMCPサーバーを記述するためのGolangライブラリ
- [salty-flower/ModelContextProtocol.NET](https://github.com/salty-flower/ModelContextProtocol.NET) #️⃣🏠 - .NET 9上でNativeAOT対応のMCPサーバーを構築するためのC# SDK ⚡ 🔌
- [@marimo-team/codemirror-mcp](https://github.com/marimo-team/codemirror-mcp) - リソースメンションとプロンプトコマンドのためのModel Context Protocol (MCP)を実装するCodeMirror拡張

## クライアント

- [SecretiveShell/MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge) 🐍 既存のOpenAI互換クライアントでMCPを使用するためのOpenAIミドルウェアプロキシ
- [3choff/MCP-Chatbot](https://github.com/3choff/mcp-chatbot) シンプルでありながら強力な⭐CLIチャットボットで、ツールサーバーを任意のOpenAI互換のLLM APIと統合します。
- [zed-industries/zed](https://github.com/zed-industries/zed) Atomの作成者によるマルチプレイヤーコードエディタ
- [firebase/genkit](https://github.com/firebase/genkit) エージェントおよびデータ変換フレームワーク
- [continuedev/continue](https://github.com/continuedev/continue) VSCodeの自動補完およびチャットツール（フル機能サポート）
- [MCP-Connect](https://github.com/EvalsOne/MCP-Connect) クラウドベースのAIサービスがローカルのStdioベースのMCPサーバーにHTTP/HTTPSリクエストでアクセスできるようにするツール

## ヒントとコツ

### LLMがMCPを使用する方法を通知するための公式プロンプト

モデルコンテキストプロトコルについてClaudeに質問したいですか？

プロジェクトを作成し、このファイルを追加します：

https://modelcontextprotocol.io/llms-full.txt

これで、ClaudeはMCPサーバーの作成方法やその動作について質問に答えることができます。

- https://www.reddit.com/r/ClaudeAI/comments/1h3g01r/want_to_ask_claude_about_model_context_protocol/

## スター履歴

<a href="https://star-history.com/#punkpeye/awesome-mcp-servers&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date" />
 </picture>
</a>
