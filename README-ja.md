# 素晴らしい MCP サーバー [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![中文文档](https://img.shields.io/badge/中文文档-点击查看-orange)](README-zh.md)
[![日本語](https://img.shields.io/badge/日本語-クリック-青)](README-ja.md)
[![Discord](https://img.shields.io/discord/1312302100125843476?logo=discord&label=discord)](https://glama.ai/mcp/discord)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/mcp?style=flat&logo=reddit&label=subreddit)](https://www.reddit.com/r/mcp/)

素晴らしいモデルコンテキストプロトコル（MCP）サーバーの厳選リスト。

- [MCP とは何ですか？](#what-is-mcp)
- [チュートリアル](#tutorials)
- [サーバー実装](#server-implementations)
- [フレームワーク](#frameworks)
- [ヒントとコツ](#tips-and-tricks)

## MCP とは何ですか？

[MCP](https://modelcontextprotocol.io/) は、標準化されたサーバー実装を通じて、AI モデルがローカルおよびリモートリソースと安全に対話できるようにするオープンプロトコルです。このリストは、ファイルアクセス、データベース接続、API 統合、その他のコンテキストサービスを通じて AI の機能を拡張する、実運用および実験的な MCP サーバーに焦点を当てています。

## チュートリアル

- [モデルコンテキストプロトコル (MCP) クイックスタート](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
- [SQLite データベースを使用するための Claude デスクトップアプリのセットアップ](https://youtu.be/wxCCzo9dGj0)

## コミュニティ

- [r/mcp Reddit](https://www.reddit.com/r/mcp)
- [Discord サーバー](https://glama.ai/mcp/discord)

## 凡例

- 🎖️ –  公式実装
- 🐍 – Python コードベース
- 📇 – TypeScript コードベース
- 🏎️ – Go コードベース
- #️⃣ – C#コードベース
- ☁️ - クラウドサービス
- 🏠 - ローカルサービス

## サーバー実装

- 📂 - [ブラウザ自動化](#browser-automation)
- ☁️ - [クラウドプラットフォーム](#cloud-platforms)
- 💬 - [コミュニケーション](#communication)
- 👤 - [顧客データプラットフォーム](#customer-data-platforms)
- 🗄️ - [データベース](#databases)
- 🛠️ - [開発者ツール](#developer-tools)
- 📂 - [ファイルシステム](#file-systems)
- 🧠 - [知識と記憶](#knowledge--memory)
- 🗺️ - [位置情報サービス](#location-services)
- 📊 - [監視](#monitoring)
- 🔎 - [検索](#search)
- 🔄 - [旅行と交通](#travel-and-transportation)
- 🔄 - [バージョン管理](#version-control)
- 🛠️ - [その他のツールと統合](#other-tools-and-integrations)

### 📂 <a name="browser-automation"></a>ブラウザ自動化

Web コンテンツのアクセスと自動化機能。AI に優しい形式で Web コンテンツを検索、スクレイピング、処理することができます。

- [@executeautomation/playwright-mcp-server](https://github.com/executeautomation/mcp-playwright) 🌐⚡️ - Playwright を使用したブラウザ自動化と Web スクレイピングのための MCP サーバー
- [@automatalabs/mcp-server-playwright](https://github.com/Automata-Labs-team/MCP-Server-Playwright) 🌐🖱️ - Playwright を使用したブラウザ自動化のための MCP サーバー
- [@modelcontextprotocol/server-puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) 📇 🏠 - Web スクレイピングとインタラクションのためのブラウザ自動化
- [@recursechat/mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts) 📇 🏠 🍎 - Apple Shortcuts と統合された MCP サーバーです。
- [@fradser/mcp-server-apple-reminders](https://github.com/FradSer/mcp-server-apple-reminders) 📇 🏠 🍎 - macOS 用の Apple Reminders と統合された MCP サーバーです。
- [@kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) 📇 ☁️ - AI 分析のための YouTube 字幕とトランスクリプトの取得
- [@kimtth/mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing) 🐍 🏠 - Azure OpenAI と Playwright を使用した「最小限の」サーバー/クライアント MCP 実装。

### ☁️ <a name="cloud-platforms"></a>クラウドプラットフォーム

クラウドプラットフォームサービスの統合。クラウドインフラストラクチャとサービスの管理と対話を可能にします。

- [Cloudflare MCP Server](https://github.com/cloudflare/mcp-server-cloudflare) 🎖️ 📇 ☁️ - Workers、KV、R2、D1 を含む Cloudflare サービスとの統合
- [Kubernetes MCP Server](https://github.com/strowk/mcp-k8s-go) - 🏎️ ☁️ MCP を通じた Kubernetes クラスター操作

### 💬 <a name="communication"></a>コミュニケーション

メッセージ管理とチャネル操作のためのコミュニケーションプラットフォームとの統合。AI モデルがチームコミュニケーションツールと対話できるようにします。

- [@modelcontextprotocol/server-slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack) 📇 ☁️ - チャネル管理とメッセージングのための Slack ワークスペース統合
- [@modelcontextprotocol/server-bluesky](https://github.com/keturiosakys/bluesky-context-server) 📇 ☁️ - クエリとインタラクションのための Bluesky インスタンス統合
- [MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite) - 🐍 ☁️ - Gmail と Google カレンダーとの統合。
- [gotoolkits/wecombot](https://github.com/gotoolkits/mcp-wecombot-server.git) - 🚀 ☁️ - MCP サーバーアプリケーションは、WeCom グループロボットにさまざまなタイプのメッセージを送信します。

### 👤 <a name="customer-data-platforms"></a>顧客データプラットフォーム

顧客データプラットフォーム内の顧客プロファイルへのアクセスを提供します。

- [sergehuber/inoyu-mcp-unomi-server](https://github.com/sergehuber/inoyu-mcp-unomi-server) 📇 ☁️ - Apache Unomi CDP サーバー上のプロファイルにアクセスし、更新するための MCP サーバー。

### 🗄️ <a name="databases"></a>データベース

スキーマ検査機能を備えた安全なデータベースアクセス。読み取り専用アクセスを含む構成可能なセキュリティ制御を使用してデータをクエリおよび分析することができます。

- [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) 🐍 🏠 - MCP サーバーの実装で、Elasticsearch とのインタラクションを提供します
- [domdomegg/airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server) 📇 🏠 - スキーマ検査、読み取り/書き込み機能を備えた Airtable データベース統合
- [LucasHild/mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery) 🐍 ☁️ - スキーマ検査とクエリ機能を備えた BigQuery データベース統合
- [ergut/mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server) 📇 ☁️ - Google BigQuery 統合のためのサーバー実装で、直接的な BigQuery データベースアクセスとクエリ機能を提供
- [designcomputer/mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server) 🐍 🏠 - 構成可能なアクセス制御、スキーマ検査、包括的なセキュリティガイドラインを備えた MySQL データベース統合
- [@modelcontextprotocol/server-postgres](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) 📇 🏠 - スキーマ検査とクエリ機能を備えた PostgreSQL データベース統合
- [@modelcontextprotocol/server-sqlite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) 🐍 🏠 - 組み込みの分析機能を備えた SQLite データベース操作
- [@joshuarileydev/supabase-mcp-server](https://github.com/joshuarileydev/supabase) - Supabase でプロジェクトと組織を管理および作成するための Supabase MCP サーバー
- [ktanaka101/mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb) 🐍 🏠 - スキーマ検査とクエリ機能を備えた DuckDB データベース統合
- [QuantGeekDev/mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp) 📇 🏠 - LLM がデータベースと直接対話できるようにする MongoDB 統合。
- [tinybirdco/mcp-tinybird](https://github.com/tinybirdco/mcp-tinybird) 🐍 ☁️ - クエリと API 機能を備えた Tinybird 統合
- [kiliczsh/mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server) 📇 🏠 - MongoDB のためのモデルコンテキストプロトコルサーバー
- [KashiwaByte/vikingdb-mcp-server](https://github.com/KashiwaByte/vikingdb-mcp-server) 🐍 ☁️ - コレクションとインデックスの紹介、ベクトルストアと検索機能を備えた VikingDB 統合。
- [runekaagaard/mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy) 🐍 🏠 - PostgreSQL、MySQL、MariaDB、SQLite、Oracle、MS SQL Server など多数のデータベースをサポートする SQLAlchemy ベースの汎用データベース統合。スキーマと関係の検査、大規模データセット分析機能を備えています。

### 💻 <a name="developer-tools"></a>開発者ツール

開発ワークフローと環境管理を強化するツールと統合。

- [QuantGeekDev/docker-mcp](https://github.com/QuantGeekDev/docker-mcp) 🏎️ 🏠 - MCP を通じた Docker コンテナの管理と操作
- [zcaceres/fetch-mcp](https://github.com/zcaceres/fetch-mcp) 📇 🏠 - JSON、テキスト、HTML データを柔軟に取得するための MCP サーバー
- [zcaceres/gtasks-mcp](https://github.com/zcaceres/gtasks-mcp) - 📇 ☁️ - Google タスクを管理するための MCP サーバー
- [snaggle-ai/openapi-mcp-server](https://github.com/snaggle-ai/openapi-mcp-server) 🏎️ 🏠 - Open API spec (v3) を使用して任意の HTTP/REST API サーバーに接続
- [@joshuarileydev/terminal-mcp-server](https://www.npmjs.com/package/@joshuarileydev/terminal-mcp-server) 📇 🏠 - 任意のシェルターミナルコマンドを実行するための MCP サーバー
- [tumf/mcp-text-editor](https://github.com/tumf/mcp-text-editor) - ラインエディタ 行単位の取得と編集ができるので、特に大きなファイルの一部書き換えを効率的に行う
- [ferrislucas/iterm-mcp](https://github.com/ferrislucas/iterm-mcp) 🖥️ 🛠️ 💬 - iTerm へのアクセスを提供するモデルコンテキストプロトコルサーバー。コマンドを実行し、iTerm ターミナルで見た内容について質問することができます。

### 📂 <a name="file-systems"></a>ファイルシステム

構成可能な権限を備えたローカルファイルシステムへの直接アクセスを提供します。指定されたディレクトリ内のファイルを読み取り、書き込み、管理することができます。

- [@modelcontextprotocol/server-filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) 📇 🏠 - ローカルファイルシステムへの直接アクセス。
- [@modelcontextprotocol/server-google-drive](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive) 📇 ☁️ - ファイルのリスト、読み取り、検索のための Google Drive 統合
- [mark3labs/mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server) 🏎️ 🏠 - ローカルファイルシステムアクセスのための Golang 実装。

### 🧠 <a name="knowledge--memory"></a>知識と記憶

知識グラフ構造を使用した永続的なメモリストレージ。セッション間で構造化情報を維持およびクエリすることができます。

- [@modelcontextprotocol/server-memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) 📇 🏠 - コンテキストを維持するための知識グラフベースの長期記憶システム
- [/CheMiguel23/MemoryMesh](https://github.com/CheMiguel23/MemoryMesh) 📇 🏠 - AI ロールプレイとストーリー生成に焦点を当てた強化されたグラフベースのメモリ

### 🗺️ <a name="location-services"></a>位置情報サービス

地理および位置ベースのサービス統合。地図データ、方向、および場所情報へのアクセスを提供します。

- [@modelcontextprotocol/server-google-maps](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps) 📇 ☁️ - 位置情報サービス、ルート計画、および場所の詳細のための Google Maps 統合

### 📊 <a name="monitoring"></a>監視

アプリケーション監視データへのアクセスと分析。エラーレポートとパフォーマンスメトリクスをレビューすることができます。

- [@modelcontextprotocol/server-sentry](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry) 🐍 ☁️ - エラートラッキングとパフォーマンス監視のための Sentry.io 統合
- [@modelcontextprotocol/server-raygun](https://github.com/MindscapeHQ/mcp-server-raygun) 📇 ☁️ - クラッシュレポートとリアルユーザーモニタリングのための Raygun API V3 統合

### 🔎 <a name="search"></a>検索

- [@modelcontextprotocol/server-brave-search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) 📇 ☁️ - Brave の検索 API を使用した Web 検索機能
- [@angheljf/nyt](https://github.com/angheljf/nyt) 📇 ☁️ - NYTimes API を使用して記事を検索
- [@modelcontextprotocol/server-fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) 🐍 🏠 ☁️ - AI 消費のための効率的な Web コンテンツの取得と処理
- [ac3xx/mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi) 📇 ☁️ - Kagi 検索 API 統合
- [theishangoswami/exa-mcp-server](https://github.com/theishangoswami/exa-mcp-server) 📇 ☁️ - Exa AI 検索 API
- [exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) 🎖️ 📇 ☁️ –  モデルコンテキストプロトコル（MCP）サーバーは、Claude などの AI アシスタントが Exa AI 検索 API を使用して Web 検索を行うことを可能にします。この設定により、AI モデルは安全かつ制御された方法でリアルタイムの Web 情報を取得できます。
- [fatwang2/search1api-mcp](https://github.com/fatwang2/search1api-mcp) 📇 ☁️ - search1api を介した検索（有料 API キーが必要）
- [Tomatio13/mcp-server-tavily](https://github.com/Tomatio13/mcp-server-tavily) ☁️ 🐍 – Tavily AI 検索 API
- [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) ☁️ 🐍 - ArXiv 研究論文を検索
- [mzxrai/mcp-webresearch](https://github.com/mzxrai/mcp-webresearch) 🔍📚 - Google を検索し、任意のトピックに関する深い Web リサーチを行う
- [andybrandt/mcp-simple-arxiv](https://github.com/andybrandt/mcp-simple-arxiv) - 🐍 ☁️ MCP を使用して LLM が ArXiv の論文を検索および読む
- [apify/mcp-server-rag-web-browser](https://github.com/apify/mcp-server-rag-web-browser) 📇 ☁️ - Apify の RAG Web Browser Actor 用の MCP サーバーで、ウェブ検索を実行し、URL をスクレイピングし、Markdown 形式でコンテンツを返します。
- [Ihor-Sokoliuk/MCP-SearXNG](https://github.com/ihor-sokoliuk/mcp-searxng) 📇 🏠/☁️ - [SearXNG](https://docs.searxng.org)のモデルコンテキストプロトコルサーバー
- [erithwik/mcp-hn](https://github.com/erithwik/mcp-hn) 🐍 ☁️ - Hacker News の検索、トップストーリーの取得などを行う MCP サーバー。
- [chanmeng/google-news-mcp-server](https://github.com/ChanMeng666/server-google-news) 📇 ☁️ - 自動トピック分類、多言語サポート、[SerpAPI](https://serpapi.com/)を通じたヘッドライン、ストーリー、関連トピックの包括的な検索機能を備えた Google News 統合。

### 🔒 <a name="security"></a>セキュリティ

- [Security Audit MCP Server](https://github.com/qianniuspace/mcp-security-audit) 📇🛡️☁️ 強力なモデルコンテキストプロトコル（MCP）サーバーで、npmパッケージ依存関係のセキュリティ脆弱性を監査します。リモートnpmレジストリ統合を備えたリアルタイムセキュリティチェックを使用して構築されています。

### 🚆 <a name="travel-and-transportation"></a>旅行と交通

旅行および交通情報へのアクセス。スケジュール、ルート、およびリアルタイムの旅行データをクエリすることができます。

- [NS Travel Information MCP Server](https://github.com/r-huijts/ns-mcp-server) 📇 ☁️ - オランダ鉄道（NS）の旅行情報、スケジュール、およびリアルタイムの更新にアクセス

### 🔄 <a name="version-control"></a>バージョン管理

Git リポジトリおよびバージョン管理プラットフォームとの対話。標準化された API を通じて、リポジトリ管理、コード分析、プルリクエスト処理、問題追跡、およびその他のバージョン管理操作を実行できます。

- [@modelcontextprotocol/server-github](https://github.com/modelcontextprotocol/servers/tree/main/src/github) 📇 ☁️ - リポジトリ管理、PR、問題などのための GitHub API 統合
- [@modelcontextprotocol/server-gitlab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab) 📇 ☁️ 🏠 - プロジェクト管理および CI/CD 操作のための GitLab プラットフォーム統合
- [@modelcontextprotocol/server-git](https://github.com/modelcontextprotocol/servers/tree/main/src/git) 🐍 🏠 - ローカルリポジトリの読み取り、検索、および分析を含む直接的な Git リポジトリ操作

### 🛠️ <a name="other-tools-and-integrations"></a>その他のツールと統合

- [apify/actors-mcp-server](https://github.com/apify/actors-mcp-server) 📇 ☁️ - 3,000 以上の事前構築されたクラウドツール（Actors として知られる）を使用して、ウェブサイト、e コマース、ソーシャルメディア、検索エンジン、地図などからデータを抽出できます。
- [zcaceres/markdownify-mcp](https://github.com/zcaceres/markdownify-mcp) 📇 🏠 - ほぼすべてのファイルやウェブコンテンツを Markdown に変換する MCP サーバー
- [mzxrai/mcp-openai](https://github.com/mzxrai/mcp-openai) 📇 ☁️ - OpenAI の最も賢いモデルとチャット
- [mrjoshuak/godoc-mcp](https://github.com/mrjoshuak/godoc-mcp) 🏎️ 🏠 - Go ドキュメントサーバーで、AI アシスタントがパッケージドキュメントとタイプにスマートにアクセスできるようにします。
- [pierrebrunelle/mcp-server-openai](https://github.com/pierrebrunelle/mcp-server-openai) 🐍 ☁️ - MCP プロトコルを使用して Claude から直接 OpenAI モデルにクエリを送信
- [@modelcontextprotocol/server-everything](https://github.com/modelcontextprotocol/servers/tree/main/src/everything) 📇 🏠 - MCP プロトコルのすべての機能を実行する MCP サーバー
- [baba786/phabricator-mcp-server](https://github.com/baba786/phabricator-mcp-server) 🐍 ☁️ - Phabricator API との対話
- [MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) 🐍 ☁️ 🏠 - REST API を介して Obsidian と対話
- [calclavia/mcp-obsidian](https://github.com/calclavia/mcp-obsidian) 📇 🏠 - これは、Claude Desktop（または任意の MCP クライアント）が Markdown ノートを含むディレクトリ（Obsidian ボールトなど）を読み取り、検索できるようにするコネクタです。
- [anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube) 📇 ☁️ - YouTube 字幕の取得
- [danhilse/notion_mcp](https://github.com/danhilse/notion_mcp) 🐍 ☁️ - Notion の API と統合して個人の ToDo リストを管理
- [rusiaaman/wcgw](https://github.com/rusiaaman/wcgw/blob/main/src/wcgw/client/mcp_server/Readme.md) 🐍 🏠 - 自律的なシェル実行、コンピュータ制御、およびコーディングエージェント。（Mac）
- [reeeeemo/ancestry-mcp](https://github.com/reeeeemo/ancestry-mcp) 🐍 🏠 - AI が.ged ファイルと遺伝データを読み取ることができるようにします。
- [sirmews/apple-notes-mcp](https://github.com/sirmews/apple-notes-mcp) 🐍 🏠 - AI がローカルの Apple Notes データベースから読み取ることができるようにします（macOS のみ）
- [anjor/coinmarket-mcp-server](https://github.com/anjor/coinmarket-mcp-server) 🐍 🏠 - 暗号通貨のリストと見積もりを取得するための Coinmarket API 統合
- [suekou/mcp-notion-server](https://github.com/suekou/mcp-notion-server) 📇 🏠 - Notion API との対話
- [amidabuddha/unichat-mcp-server](https://github.com/amidabuddha/unichat-mcp-server) 🐍/📇 ☁️ - MCP プロトコルを使用して OpenAI、MistralAI、Anthropic、xAI、または Google AI にリクエストを送信するためのツールまたは事前定義されたプロンプト。ベンダー API キーが必要
- [g0t4/mcp-server-commands](https://github.com/g0t4/mcp-server-commands) 📇 🏠 - コマンドを実行し、その出力を含める。ツールとプロンプト。
- [evalstate/mcp-miro](https://github.com/evalstate/mcp-miro) 📇 ☁️ - MIRO ホワイトボードにアクセスし、アイテムを一括作成および読み取り。REST API の OAUTH キーが必要。
- [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) 🐍 ☁️ - Confluence ワークスペースの自然言語検索とコンテンツアクセス
- [pyroprompts/any-chat-completions-mcp](https://github.com/pyroprompts/any-chat-completions-mcp) - Perplexity、Groq、xAI などの他の OpenAI SDK 互換のチャット完了 API とチャット
- [anaisbetts/mcp-installer](https://github.com/anaisbetts/mcp-installer) 🐍 🏠 - 他の MCP サーバーをインストールする MCP サーバー。
- [tanigami/mcp-server-perplexity](https://github.com/tanigami/mcp-server-perplexity) 🐍 ☁️ - Perplexity API との対話。
- [future-audiences/wikimedia-enterprise-model-context-protocol](https://gitlab.wikimedia.org/repos/future-audiences/wikimedia-enterprise-model-context-protocol) 🐍 ☁️ - Wikipedia 記事検索 API
- [andybrandt/mcp-simple-timeserver](https://github.com/andybrandt/mcp-simple-timeserver) 🐍 🏠☁️ - クライアントマシンのローカル時間または NTP サーバーからの現在の UTC 時間を確認するための MCP サーバー
- [andybrandt/mcp-simple-openai-assistant](https://github.com/andybrandt/mcp-simple-openai-assistant) - 🐍 ☁️ MCP を使用して OpenAI アシスタントと対話（Claude は任意の GPT モデルをアシスタントとして使用できます）
- [@joshuarileydev/simulator-mcp-server](https://www.npmjs.com/package/@joshuarileydev/simulator-mcp-server) - 📇 🏠 iOS シミュレータを制御し、シミュレータを起動し、アプリをインストール/起動するための MCP サーバー。
- [tumf/mcp-shell-server](https://github.com/tumf/mcp-shell-server) シェルからホワイトリストにあるコマンドを実行して結果を返す MCP サーバ
- [apinetwork/piapi-mcp-server](https://github.com/apinetwork/piapi-mcp-server) 📇 ☁️ PiAPI MCP サーバーは、ユーザーが Claude や他の MCP 互換アプリから直接 Midjourney/Flux/Kling/Hunyuan/Udio/Trellis でメディアコンテンツを生成することを可能にします。
- [gotoolkits/DifyWorkflow](https://github.com/gotoolkits/mcp-difyworkflow-server) - 🚀 ☁️ MCP サーバーの Tools を使用して、Dify AI プラットフォーム上でカスタムされたワークフローを検索および実行する
- [boilingdata/mcp-server-and-gw](https://github.com/boilingdata/mcp-server-and-gw) サンプルサーバーと MCP クライアントを備えた MCP stdio から HTTP SSE へのトランスポートゲートウェイ。
- [lightconetech/mcp-gateway](https://github.com/lightconetech/mcp-gateway) MCP SSE サーバーのゲートウェイデモ。
- [sparfenyuk/mcp-proxy](https://github.com/sparfenyuk/mcp-proxy) 🐍 MCP stdio から SSE へのトランスポートゲートウェイ。

## フレームワーク

- [Genkit MCP](https://github.com/firebase/genkit/tree/main/js/plugins/mcp) 📇 – [Genkit](https://github.com/firebase/genkit/tree/main) とモデルコンテキストプロトコル（MCP）との統合を提供します。
- [@modelcontextprotocol/server-langchain](https://github.com/rectalogic/langchain-mcp) 🐍 - LangChain での MCP ツール呼び出しサポートを提供し、LangChain ワークフローに MCP ツールを統合できるようにします。
- [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go) 🏎️ - MCP サーバーとクライアントを構築するための Golang SDK。
- [FastMCP](https://github.com/jlowin/fastmcp) 🐍 - Python で MCP サーバーを構築するための高レベルフレームワーク
- [mcp-rs-template](https://github.com/linux-china/mcp-rs-template) 🦀 - Rust のための MCP CLI サーバーテンプレート
- [Foxy Contexts](https://github.com/strowk/foxy-contexts) 🏎️ - 機能テストを含む宣言的に MCP サーバーを記述するための Golang ライブラリ
- [salty-flower/ModelContextProtocol.NET](https://github.com/salty-flower/ModelContextProtocol.NET) #️⃣🏠 - .NET 9 上で NativeAOT 対応の MCP サーバーを構築するための C# SDK ⚡ 🔌
- [@marimo-team/codemirror-mcp](https://github.com/marimo-team/codemirror-mcp) - リソースメンションとプロンプトコマンドのための Model Context Protocol (MCP)を実装する CodeMirror 拡張

## クライアント

- [SecretiveShell/MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge) 🐍 既存の OpenAI 互換クライアントで MCP を使用するための OpenAI ミドルウェアプロキシ
- [3choff/MCP-Chatbot](https://github.com/3choff/mcp-chatbot) シンプルでありながら強力な ⭐CLI チャットボットで、ツールサーバーを任意の OpenAI 互換の LLM API と統合します。
- [zed-industries/zed](https://github.com/zed-industries/zed) Atom の作成者によるマルチプレイヤーコードエディタ
- [firebase/genkit](https://github.com/firebase/genkit) エージェントおよびデータ変換フレームワーク
- [continuedev/continue](https://github.com/continuedev/continue) VSCode の自動補完およびチャットツール（フル機能サポート）
- [MCP-Connect](https://github.com/EvalsOne/MCP-Connect) クラウドベースの AI サービスがローカルの Stdio ベースの MCP サーバーに HTTP/HTTPS リクエストでアクセスできるようにするツール

## ヒントとコツ

### LLM が MCP を使用する方法を通知するための公式プロンプト

モデルコンテキストプロトコルについて Claude に質問したいですか？

プロジェクトを作成し、このファイルを追加します：

https://modelcontextprotocol.io/llms-full.txt

これで、Claude は MCP サーバーの作成方法やその動作について質問に答えることができます。

- https://www.reddit.com/r/ClaudeAI/comments/1h3g01r/want_to_ask_claude_about_model_context_protocol/

## スター履歴

<a href="https://star-history.com/#punkpeye/awesome-mcp-servers&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date" />
 </picture>
</a>
