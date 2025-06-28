# 素晴らしいMCPサーバー [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![繁體中文](https://img.shields.io/badge/繁體中文-點擊查看-orange)](README-zh_TW.md)
[![简体中文](https://img.shields.io/badge/简体中文-点击查看-orange)](README-zh.md)
[![日本語](https://img.shields.io/badge/日本語-クリック-青)](README-ja.md)
[![한국어](https://img.shields.io/badge/한국어-클릭-yellow)](README-ko.md)
[![Português Brasileiro](https://img.shields.io/badge/Português_Brasileiro-Clique-green)](README-pt_BR.md)
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

## クライアント

[awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients/)と[glama.ai/mcp/clients](https://glama.ai/mcp/clients)をチェックしてください。
MCPをサポートするクライアントのリストです。

> [!TIP]
> [Glama Chat](https://glama.ai/chat)はMCPサポートと[AI gateway](https://glama.ai/gateway)を備えたマルチモーダルAIクライアントです。

## チュートリアル

* [モデルコンテキストプロトコル (MCP) クイックスタート](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
* [SQLiteデータベースを使用するためのClaudeデスクトップアプリのセットアップ](https://youtu.be/wxCCzo9dGj0)

## コミュニティ

* [r/mcp Reddit](https://www.reddit.com/r/mcp)
* [Discordサーバー](https://glama.ai/mcp/discord)

## 凡例

* 🎖️ – 公式実装	
* プログラミング言語 
  * 🐍 – Pythonコードベース 
  * 📇 – TypeScriptコードベース 
  * 🏎️ – Goコードベース 
  * 🦀 – Rustコードベース 
  * #️⃣ – C#コードベース 
  * ☕ – Javaコードベース 
* スコープ 
  * ☁️ – クラウドサービス 
  * 🏠 – ローカルサービス 
  * 📟 – 組み込みシステム 
* 対応OS 
  * 🍎 – macOS用 
  * 🪟 – Windows用 
  * 🐧 – Linux用

> [!NOTE]
> ローカル 🏠 とクラウド ☁️ の違いに迷っていますか？ 
> * MCPサーバーがローカルにインストールされたソフトウェアと通信する場合（例：Chromeブラウザの制御）には「ローカル 🏠」を使用してください。 
> * MCPサーバーがリモートAPIと通信する場合（例：天気API）には「とクラウド ☁️」を使用してください。

## サーバー実装

> [!NOTE]
> 現在、リポジトリと同期されている[ウェブのディレクトリ](https://glama.ai/mcp/servers)があります。

* 🔗 - [Aggregators](#aggregators)
* 📂 - [ブラウザ自動化](#browser-automation)
* 🎨 - [芸術と文化](#art-and-culture)
* ☁️ - [クラウドプラットフォーム](#cloud-platforms)
* 💬 - [コミュニケーション](#communication)
* 👤 - [顧客データプラットフォーム](#customer-data-platforms)
* 🗄️ - [データベース](#databases)
* 📊 - [データプラットフォーム](#data-platforms)
* 🛠️ - [開発者ツール](#developer-tools)
* 📂 - [ファイルシステム](#file-systems)
* 🎮 - [ ゲーミング](#gaming)
* 🧠 - [知識と記憶](#knowledge--memory)
* 🗺️ - [位置情報サービス](#location-services)
* 📊 - [監視](#monitoring)
* 🔎 - [検索](#search)
* 🌎 - [翻訳サービス](#translation-services)
* 🔄 - [旅行と交通](#travel-and-transportation)
* 🔄 - [バージョン管理](#version-control)
* 🛠️ - [その他のツールと統合](#other-tools-and-integrations)

### 🔗 <a name="aggregators"></a>アグリゲーター

単一のMCPサーバーを通じて多くのアプリやツールにアクセスするためのサーバー。

- [OpenMCP](https://github.com/wegotdocs/open-mcp) 📇 🏠 🍎 🪟 🐧 - Web APIを10秒でMCPサーバーに変換し、オープンソースレジストリに追加する: https://open-mcp.org
- [tigranbs/mcgravity](https://github.com/tigranbs/mcgravity) 📇 🏠 - 複数のMCPサーバーを1つの統一エンドポイントに構成するためのプロキシツール。Nginxがウェブサーバーのために機能するのと同様に、複数のMCPサーバー間でリクエストの負荷分散を行うことで、AIツールをスケーリングします。
- [MetaMCP](https://github.com/metatool-ai/metatool-app) 📇 ☁️ 🏠 🍎 🪟 🐧 - MetaMCPは、GUIでMCP接続を管理する統合ミドルウェアMCPサーバーです。
- [MCP Access Point](https://github.com/sxhxliang/mcp-access-point)  📇 ☁️ 🏠 🍎 🪟 🐧 - サーバー側のコードに変更を加えることなく、Web API を 1 回のクリックで MCP サーバーに変換します。。
- [hamflx/imagen3-mcp](https://github.com/hamflx/imagen3-mcp) 📇 🏠 🪟 🍎 🐧 - MCPを通じてGoogleのImagen 3.0 APIを使用する強力な画像生成ツール。高度な写真、芸術的、写実的なコントロールでテキストプロンプトから高品質な画像を生成します。

### 📂 <a name="browser-automation"></a>ブラウザ自動化

Webコンテンツのアクセスと自動化機能。AIに優しい形式でWebコンテンツを検索、スクレイピング、処理することができます。

- [@executeautomation/playwright-mcp-server](https://github.com/executeautomation/mcp-playwright) 🌐⚡️ - Playwrightを使用したブラウザ自動化とWebスクレイピングのためのMCPサーバー
- [@automatalabs/mcp-server-playwright](https://github.com/Automata-Labs-team/MCP-Server-Playwright) 🌐🖱️ - Playwrightを使用したブラウザ自動化のためのMCPサーバー
- [@modelcontextprotocol/server-puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) 📇 🏠 - Webスクレイピングとインタラクションのためのブラウザ自動化
- [@kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) 📇 ☁️ - AI分析のためのYouTube字幕とトランスクリプトの取得
- [@kimtth/mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing) 🐍 🏠 - Azure OpenAIとPlaywrightを使用した「最小限の」サーバー/クライアントMCP実装。
- [@fradser/mcp-server-apple-reminders](https://github.com/FradSer/mcp-server-apple-reminders) 📇 🏠 🍎 - macOS 用の Apple Reminders と統合された MCP サーバーです。
- [@34892002/bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js) 📇 🏠  - Bilibiliコンテンツの検索をサポートするMCPサーバー。LangChain連携のサンプルとテストスクリプトを提供。
- [aircodelabs/grasp](https://github.com/aircodelabs/grasp) 📇 🏠 - MCPとA2Aをネイティブにサポートする、エージェント駆動のセルフホスト型ブラウザ。

### 🎨 <a name="art-and-culture"></a>芸術と文化

美術コレクション、文化遺産、博物館データベースにアクセスして探索できます。AIモデルは、芸術的および文化的なコンテンツを検索および分析できます。

- [cantian-ai/bazi-mcp](https://github.com/cantian-ai/bazi-mcp) 📇 🏠 ☁️ 🍎 🪟 - 包括的で正確な八字（四柱推命）の命式作成と占い情報を提供
- [yuna0x0/anilist-mcp](https://github.com/yuna0x0/anilist-mcp) 📇 ☁️ - アニメとマンガの情報をAniList APIと連携するMCPサーバー

### ☁️ <a name="cloud-platforms"></a>クラウドプラットフォーム

クラウドプラットフォームサービスの統合。クラウドインフラストラクチャとサービスの管理と対話を可能にします。

- [Cloudflare MCP Server](https://github.com/cloudflare/mcp-server-cloudflare) 🎖️ 📇 ☁️ - Workers、KV、R2、D1を含むCloudflareサービスとの統合
- [Kubernetes MCP Server](https://github.com/strowk/mcp-k8s-go) - 🏎️ ☁️ MCPを通じたKubernetesクラスター操作
- [alexbakers/mcp-ipfs](https://github.com/alexbakers/mcp-ipfs) 📇 ☁️ - IPFSストレージのアップロードと操作
- [aliyun/alibaba-cloud-ops-mcp-server](https://github.com/aliyun/alibaba-cloud-ops-mcp-server) 🎖️ 🐍 ☁️ - MCPサーバーは、AIアシスタントがAlibaba Cloud上のリソースを運用・管理できるようにし、ECS、クラウドモニタリング、OOS、およびその他の広く使用されているクラウド製品をサポートします。
- [wenhuwang/mcp-k8s-eye](https://github.com/wenhuwang/mcp-k8s-eye) 🏎️ ☁️/🏠 Kubernetes クラスターのリソース管理と、クラスターとアプリケーションの健全性ステータスの詳細な分析を提供します。
- [weibaohui/k8m](https://github.com/weibaohui/k8m) - 🏎️ ☁️/🏠 MCPマルチクラスターKubernetesの管理と運用を提供し、管理インターフェース、ログ機能を備え、一般的な運用・開発シナリオをカバーする約50種類のツールを内蔵。標準リソースおよびCRDリソースをサポート。  
- [weibaohui/kom](https://github.com/weibaohui/kom) - 🏎️ ☁️/🏠 MCPマルチクラスターKubernetesの管理と運用を提供。SDKとして自身のプロジェクトに統合可能で、一般的な運用・開発シナリオをカバーする約50種類のツールを内蔵。標準リソースおよびCRDリソースをサポート。
- [silenceper/mcp-k8s](https://github.com/silenceper/mcp-k8s) 🏎️ ☁️/🏠 MCP-K8Sは、AI駆動のKubernetesリソース管理ツールで、自然言語インタラクションを通じて、ユーザーがKubernetesクラスター内の任意のリソース（ネイティブリソース（DeploymentやServiceなど）やカスタムリソース（CRD）を含む）を操作できるようにします。複雑なコマンドを覚える必要はなく、要件を説明するだけで、AIが対応するクラスター操作を正確に実行し、Kubernetesの使いやすさを大幅に向上させます。
- [portainer/portainer-mcp](https://github.com/portainer/portainer-mcp) - 🏎️ ☁️/🏠 強力なMCPサーバーで、AIアシスタントがPortainerインスタンスとシームレスに連携し、コンテナ管理、デプロイメント操作、インフラストラクチャ監視機能に自然言語でアクセスできるようにします。

### 💬 <a name="communication"></a>コミュニケーション

メッセージ管理とチャネル操作のためのコミュニケーションプラットフォームとの統合。AIモデルがチームコミュニケーションツールと対話できるようにします。

- [@modelcontextprotocol/server-slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack) 📇 ☁️ - チャネル管理とメッセージングのためのSlackワークスペース統合
- [@keturiosakys/bluesky-context-server](https://github.com/keturiosakys/bluesky-context-server) 📇 ☁️ - クエリとインタラクションのためのBlueskyインスタンス統合
- [MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite) - 🐍 ☁️ - GmailとGoogleカレンダーとの統合。
- [gotoolkits/wecombot](https://github.com/gotoolkits/mcp-wecombot-server.git) - 🚀 ☁️  - MCPサーバーアプリケーションは、WeComグループロボットにさまざまなタイプのメッセージを送信します。
- [line/line-bot-mcp-server](https://github.com/line/line-bot-mcp-server) 🎖 📇 ☁️ - Messaging APIを利用したLINE公式アカウントとの統合
- [sawa-zen/vrchat-mcp](https://github.com/sawa-zen/vrchat-mcp) - 📇 🏠 VRChat APIと対話するためのMCPサーバーです。VRChatのフレンドやワールド、アバターなどの情報を取得することができます。
- [takumi0706/google-calendar-mcp](https://github.com/takumi0706/google-calendar-mcp) 📇 ☁️ - GoogleカレンダーAPIと連携するためのMCPサーバーです。GoogleCalendar APIの作成、更新、取得、削除ができます。また、TypeScriptベースです。
- [teddyzxcv/ntfy-mcp](https://github.com/teddyzxcv/ntfy-mcp) ntfy を使用してスマートフォンに通知を送信し、情報を確実に伝達する MCP サーバーです。
- [YCloud-Developers/ycloud-whatsapp-mcp-server](https://github.com/YCloud-Developers/ycloud-whatsapp-mcp-server) 📇 🏠 - YCloudプラットフォーム経由でWhatsAppビジネスメッセージを送信するためのMCPサーバー。
- [jaipandya/producthunt-mcp-server](https://github.com/jaipandya/producthunt-mcp-server) 🐍 🏠 - Product Huntのための MCP サーバー。トレンド投稿、コメント、コレクション、ユーザーなどと対話できます。

### 👤 <a name="customer-data-platforms"></a>顧客データプラットフォーム

顧客データプラットフォーム内の顧客プロファイルへのアクセスを提供します。

- [sergehuber/inoyu-mcp-unomi-server](https://github.com/sergehuber/inoyu-mcp-unomi-server) 📇 ☁️ - Apache Unomi CDPサーバー上のプロファイルにアクセスし、更新するためのMCPサーバー。
- [@antv/mcp-server-chart](https://github.com/antvis/mcp-server-chart) 🎖️ 📇 ☁️ - [AntV](https://github.com/antvis) をベースにしたデータ可視化チャートを生成する MCP Server プラグイン。

### 🗄️ <a name="databases"></a>データベース

スキーマ検査機能を備えた安全なデータベースアクセス。読み取り専用アクセスを含む構成可能なセキュリティ制御を使用してデータをクエリおよび分析することができます。

- [qiniu/qiniu-mcp-server](https://github.com/qiniu/qiniu-mcp-server) 🐍 ☁️ - 七牛クラウド製品に基づいて構築されたMCP、七牛クラウドストレージやインテリジェントマルチメディアサービスなどへのアクセスをサポートします。
- [aliyun/alibabacloud-tablestore-mcp-server](https://github.com/aliyun/alibabacloud-tablestore-mcp-server) ☕ 🐍 ☁️ - テーブル ストア用の MC P サービスには、ドキュメントの追加、ドキュメント ベースのセマンティック検索、ドン ベクトル サンド スカラーがラグ フレンドリーでサーバー レスなどの機能があります。
aliyun/alibabacloud-tablestore-mcp-server ☕ 🐍 ☁️ - 阿里云表格存储(Tablestore)的 MCP 服务器实现，特性包括添加文档、基于向量和标量进行语义搜索、RAG友好。
- [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) 🐍 🏠 - MCPサーバーの実装で、Elasticsearchとのインタラクションを提供します
- [crystaldba/postgres-mcp](https://github.com/crystaldba/postgres-mcp) 🐍 🏠 - パフォーマンス分析、チューニング、ヘルスチェックのためのツールを備えた、Postgres開発と運用のためのオールインワンMCPサーバー
- [domdomegg/airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server) 📇 🏠 - スキーマ検査、読み取り/書き込み機能を備えた Airtable データベース統合
- [LucasHild/mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery) 🐍 ☁️ - スキーマ検査とクエリ機能を備えたBigQueryデータベース統合
- [c4pt0r/mcp-server-tidb](https://github.com/c4pt0r/mcp-server-tidb) 🐍 ☁️ - TiDB データベースの統合、テーブル構造の作成（DDL）および SQL の実行
- [ergut/mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server) 📇 ☁️ - Google BigQuery統合のためのサーバー実装で、直接的なBigQueryデータベースアクセスとクエリ機能を提供
- [designcomputer/mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server) 🐍 🏠 - 構成可能なアクセス制御、スキーマ検査、包括的なセキュリティガイドラインを備えたMySQLデータベース統合
- [@modelcontextprotocol/server-postgres](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) 📇 🏠 - スキーマ検査とクエリ機能を備えたPostgreSQLデータベース統合
- [@modelcontextprotocol/server-sqlite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) 🐍 🏠 - 組み込みの分析機能を備えたSQLiteデータベース操作
- [@joshuarileydev/supabase-mcp-server](https://github.com/joshuarileydev/supabase) - Supabaseでプロジェクトと組織を管理および作成するためのSupabase MCPサーバー
- [ktanaka101/mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb) 🐍 🏠 - スキーマ検査とクエリ機能を備えたDuckDBデータベース統合
- [QuantGeekDev/mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp) 📇 🏠 - LLMがデータベースと直接対話できるようにするMongoDB統合。
- [tinybirdco/mcp-tinybird](https://github.com/tinybirdco/mcp-tinybird) 🐍 ☁️ - クエリとAPI機能を備えたTinybird統合
- [kiliczsh/mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server) 📇 🏠 - MongoDBのためのモデルコンテキストプロトコルサーバー
- [tuannvm/mcp-trino](https://github.com/tuannvm/mcp-trino) 🏎️ ☁️ - Trino用のModel Context Protocol (MCP)サーバーのGo実装。
- [KashiwaByte/vikingdb-mcp-server](https://github.com/KashiwaByte/vikingdb-mcp-server) 🐍 ☁️ - コレクションとインデックスの紹介、ベクトルストアと検索機能を備えたVikingDB統合。
- [runekaagaard/mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy) 🐍 🏠 - PostgreSQL、MySQL、MariaDB、SQLite、Oracle、MS SQL Serverなど多数のデータベースをサポートするSQLAlchemyベースの汎用データベース統合。スキーマと関係の検査、大規模データセット分析機能を備えています。
- [GreptimeTeam/greptimedb-mcp-server](https://github.com/GreptimeTeam/greptimedb-mcp-server) 🐍 🏠 - GreptimeDBのMCPサービスにクエリを実行する。
- [xing5/mcp-google-sheets](https://github.com/xing5/mcp-google-sheets) 🐍 ☁️ - Google Sheetsと対話するためのモデルコンテキストプロトコルサーバー。このサーバーはGoogle Sheets APIを通じてスプレッドシートの作成、読み取り、更新、管理のためのツールを提供します。
- [freema/mcp-gsheets](https://github.com/freema/mcp-gsheets) 📇 ☁️ - 包括的な読み取り、書き込み、フォーマット、シート管理機能を備えたGoogle Sheets API統合のMCPサーバー。
- [ydb/ydb-mcp](https://github.com/ydb-platform/ydb-mcp) 🎖️ 🐍 ☁️ – MCPサーバー：[YDB](https://ydb.tech)データベースと対話するための。

### 📊 <a name="data-platforms"></a>データプラットフォーム

データ統合、変換、パイプライン オーケストレーションのためのデータ プラットフォーム。

- [flowcore/mcp-flowcore-platform](https://github.com/flowcore-io/mcp-flowcore-platform) 🎖️📇☁️🏠 - Flowcore と対話してアクションを実行し、データを取り込み、データ コア内またはパブリック データ コア内のあらゆるデータを分析、相互参照、活用します。これらはすべて人間の言語で実行できます。

### 💻 <a name="developer-tools"></a>開発者ツール

開発ワークフローと環境管理を強化するツールと統合。

- [Hypersequent/qasphere-mcp](https://github.com/Hypersequent/qasphere-mcp) 🎖️ 📇 ☁️ - [QA Sphere](https://qasphere.com/)テスト管理システムとの統合。LLMがテストケースを発見、要約、操作できるようにし、AI搭載IDEから直接アクセス可能
- [QuantGeekDev/docker-mcp](https://github.com/QuantGeekDev/docker-mcp) 🏎️ 🏠 - MCPを通じたDockerコンテナの管理と操作
- [zcaceres/fetch-mcp](https://github.com/zcaceres/fetch-mcp) 📇 🏠 - JSON、テキスト、HTMLデータを柔軟に取得するためのMCPサーバー
- [zcaceres/gtasks-mcp](https://github.com/zcaceres/gtasks-mcp) - 📇 ☁️ - Google タスクを管理するための MCP サーバー
- [snaggle-ai/openapi-mcp-server](https://github.com/snaggle-ai/openapi-mcp-server) 🏎️ 🏠 - Open API spec (v3) を使用して任意のHTTP/REST APIサーバーに接続
- [@joshuarileydev/terminal-mcp-server](https://www.npmjs.com/package/@joshuarileydev/terminal-mcp-server) 📇 🏠 - 任意のシェルターミナルコマンドを実行するためのMCPサーバー
- [tumf/mcp-text-editor](https://github.com/tumf/mcp-text-editor) - ラインエディタ 行単位の取得と編集ができるので、特に大きなファイルの一部書き換えを効率的に行う
- [ferrislucas/iterm-mcp](https://github.com/ferrislucas/iterm-mcp) 🖥️ 🛠️ 💬 - iTermへのアクセスを提供するモデルコンテキストプロトコルサーバー。コマンドを実行し、iTermターミナルで見た内容について質問することができます。
- [freema/mcp-design-system-extractor](https://github.com/freema/mcp-design-system-extractor) 📇 🏠 - Storybookデザインシステムからコンポーネント情報を抽出します。AI搭載デザインシステム分析のためのHTML、スタイル、プロパティ、依存関係、テーマトークン、コンポーネントメタデータを提供します。
- [Rootly-AI-Labs/Rootly-MCP-server](https://github.com/Rootly-AI-Labs/Rootly-MCP-server) 🎖️🐍☁️🍎 - インシデント管理プラットフォーム[Rootly](https://rootly.com/)向けのMCPサーバー
- [YuChenSSR/mindmap-mcp-server](https://github.com/YuChenSSR/mindmap-mcp-server) 🐍 🏠 - きれいなインタラクティブなマインドマップを生成するためのモデルコンテキストプロトコル（MCP）サーバ。
- [InhiblabCore/mcp-image-compression](https://github.com/InhiblabCore/mcp-image-compression) 🐍 🏠 - 様々な画像フォーマットのローカル圧縮のためのMCPサーバー。
- [SDGLBL/mcp-claude-code](https://github.com/SDGLBL/mcp-claude-code) 🐍 🏠 - MCPを使用したClaude Code機能の実装で、AIによるコード理解、修正、プロジェクト分析を包括的なツールサポートで実現します。
- [api7/apisix-mcp](https://github.com/api7/apisix-mcp) 🎖️ 📇 🏠 [Apache APISIX](https://github.com/apache/apisix) のすべてのリソースの照会と管理をサポートするMCPサービス。
- [ios-simulator-mcp](https://github.com/joshuayoes/ios-simulator-mcp) 📇 🏠 🍎 - iOS シミュレータと対話するためのモデル コンテキスト プロトコル (MCP) サーバー。このサーバーを使用すると、iOS シミュレータに関する情報を取得したり、UI の対話を制御したり、UI 要素を検査したりして、iOS シミュレータと対話できます。
- [higress-group/higress-ops-mcp-server](https://github.com/higress-group/higress-ops-mcp-server) 🐍 🏠 - MCP サーバーが [Higress](https://github.com/alibaba/higress/blob/main/README_JP.md) ゲートウェイの構成と操作を管理するための全面的なツールを提供します。
- [yiwenlu66/PiloTY](https://github.com/yiwenlu66/PiloTY) 🐍 🏠 - AIエージェントが状態保持セッション、SSH接続、バックグラウンドプロセス管理を使ってインタラクティブターミナルを制御できるPTY操作のAIパイロット
- [ReAPI-com/mcp-openapi](https://github.com/ReAPI-com/mcp-openapi) 📇 🏠 - LLMがOpenAPI仕様のすべてを理解し、コードの発見、説明、生成、モックデータの作成を可能にするMCPサーバー
- [automation-ai-labs/mcp-link](https://github.com/automation-ai-labs/mcp-link) 🏎️ 🏠 - OpenAPIスキーマを使用してAIエージェントと任意のAPIをシームレスに統合
- [cjo4m06/mcp-shrimp-task-manager](https://github.com/cjo4m06/mcp-shrimp-task-manager) 📇 ☁️ 🏠 – Cursor AI のようなコーディングエージェントを強化するために設計された、プログラミング特化型のタスク管理システム。高度なタスク記憶、自省、依存関係の管理機能を備えています。[ShrimpTaskManager](https://cjo4m06.github.io/mcp-shrimp-task-manager)
- [axliupore/mcp-code-runner](https://github.com/axliupore/mcp-code-runner) 📇 🏠 - Docker 経由でローカルにコードを実行し、複数のプログラミング言語をサポートする MCP サーバー
- [TencentEdgeOne/edgeone-pages-mcp](https://github.com/TencentEdgeOne/edgeone-pages-mcp) 📇 ☁️ - EdgeOne Pagesに HTMLコンテンツをデプロイし、公開アクセス可能なURLを取得するためのMCPサービスです。
- [lpigeon/ros-mcp-server](https://github.com/lpigeon/ros-mcp-server) 🐍 🏠 🍎 🪟 🐧 - ROS MCPサーバーは、ユーザーの自然言語コマンドをROSまたはROS2の制御コマンドに変換することで、ロボットの制御を支援します。


### 📂 <a name="file-systems"></a>ファイルシステム

構成可能な権限を備えたローカルファイルシステムへの直接アクセスを提供します。指定されたディレクトリ内のファイルを読み取り、書き込み、管理することができます。

- [@modelcontextprotocol/server-filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) 📇 🏠 - ローカルファイルシステムへの直接アクセス。
- [@modelcontextprotocol/server-google-drive](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive) 📇 ☁️ - ファイルのリスト、読み取り、検索のためのGoogle Drive統合
- [mark3labs/mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server) 🏎️ 🏠 - ローカルファイルシステムアクセスのためのGolang実装。
- [Xuanwo/mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal) 🐍 🏠 ☁️ - Apache OpenDAL™ でどのストレージにもアクセスできます
- [exoticknight/mcp-file-merger](https://github.com/exoticknight/mcp-file-merger) 📇 🏠 - AI Chatの長さ制限に適応するファイルマージツール

### 🎮 <a name="gaming"></a> ゲーミング

ゲーミングに関連するデータとサービスとの統合

- [rishijatia/fantasy-pl-mcp](https://github.com/rishijatia/fantasy-pl-mcp/) 🐍 ☁️ - 実際のFantasy Premier Leagueデータと分析ツールのためのMCPサーバー
- [CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity) 📇 #️⃣ 🏠 - Unity3dゲームエンジン統合によるゲーム開発用MCPサーバー
- [opgginc/opgg-mcp](https://github.com/opgginc/opgg-mcp) 📇 ☁️ - League of Legends、TFT、Valorantなどの人気ゲームのリアルタイムゲームデータにアクセスし、チャンピオン分析、eスポーツスケジュール、メタ構成、キャラクター統計を提供します。

### 🧠 <a name="knowledge--memory"></a>知識と記憶

知識グラフ構造を使用した永続的なメモリストレージ。セッション間で構造化情報を維持およびクエリすることができます。

- [jinzcdev/markmap-mcp-server](https://github.com/jinzcdev/markmap-mcp-server) 📇 🏠 - [markmap](https://github.com/markmap/markmap) を基にしたMCPサーバーで、**Markdown**をインタラクティブな**マインドマップ**に変換します。複数のフォーマット（PNG/JPG/SVG）でのエクスポート、ブラウザでのリアルタイムプレビュー、ワンクリックでのMarkdownコピー、ダイナミックな視覚化機能をサポートしています。
- [@modelcontextprotocol/server-memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) 📇 🏠 - コンテキストを維持するための知識グラフベースの長期記憶システム
- [/CheMiguel23/MemoryMesh](https://github.com/CheMiguel23/MemoryMesh) 📇 🏠 - AIロールプレイとストーリー生成に焦点を当てた強化されたグラフベースのメモリ
- [@mem0ai/mem0-mcp](https://github.com/mem0ai/mem0-mcp) 🐍 🏠 - CursorやWindsurfなどのIDEでコーディングの好みやパターンを管理するためのMem0用モデルコンテキストプロトコルサーバー。コード実装、ベストプラクティス、技術文書の保存、取得、意味的な処理のためのツールを提供します
- [@ragieai/mcp-server](https://github.com/ragieai/ragie-mcp-server) 📇 ☁️ - あなたの [Ragie](https://www.ragie.ai) (RAG) ナレッジベースから、Google Drive、Notion、JIRAなどの連携サービスに接続されたコンテキストを取得します。

### 🗺️ <a name="location-services"></a>位置情報サービス

地理および位置ベースのサービス統合。地図データ、方向、および場所情報へのアクセスを提供します。

- [@modelcontextprotocol/server-google-maps](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps) 📇 ☁️ - 位置情報サービス、ルート計画、および場所の詳細のためのGoogle Maps統合

### 📊 <a name="monitoring"></a>監視

アプリケーション監視データへのアクセスと分析。エラーレポートとパフォーマンスメトリクスをレビューすることができます。

- [tumf/grafana-loki-mcp](https://github.com/tumf/grafana-loki-mcp) 🐍 🏠 - Grafana API を通じて Loki ログをクエリできる MCP サーバー。
- [@modelcontextprotocol/server-sentry](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry) 🐍 ☁️ - エラートラッキングとパフォーマンス監視のためのSentry.io統合
- [@MindscapeHQ/server-raygun](https://github.com/MindscapeHQ/mcp-server-raygun) 📇 ☁️ - クラッシュレポートとリアルユーザーモニタリングのためのRaygun API V3統合

### 🔎 <a name="search"></a>検索

- [scrapeless-ai/scrapeless-mcp-server](https://github.com/scrapeless-ai/scrapeless-mcp-server) 🐍 ☁️ - Scrapeless Model Context Protocolサービスは、MCPエコシステム内で離れることなくWeb検索を可能にするGoogle SERP APIへのMCPサーバコネクタとして機能します。
- [@modelcontextprotocol/server-brave-search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) 📇 ☁️ - Braveの検索APIを使用したWeb検索機能
- [Dumpling-AI/mcp-server-dumplingai](https://github.com/Dumpling-AI/mcp-server-dumplingai) 🎖️ 📇 ☁️ - [Dumpling AI](https://www.dumplingai.com/) によるデータ取得、Webスクレイピング、ドキュメント変換API
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
- [hellokaton/unsplash-mcp-server](https://github.com/hellokaton/unsplash-mcp-server)) 🐍 ☁️ - Unsplash 画像検索機能の統合用
- [ConechoAI/openai-websearch-mcp](https://github.com/ConechoAI/openai-websearch-mcp/) 🐍 🏠 ☁️ - OpenAI の組み込み `web_search` ツールを MCP サーバーに変換して使用します。
- [yamanoku/baseline-mcp-server](https://github.com/yamanoku/baseline-mcp-server) 📇 🏠 - Web Platform APIを使ってBaselineの状態を検索してくれるMCPサーバー
- [Wuye-AI/mcp-server-wuye-ai](https://github.com/wuye-ai/mcp-server-wuye-ai) 🎖️ 📇 ☁️ - CRICプロパティAIプラットフォームに接続するMCPサーバーです。CRICプロパティAIは、克而瑞がプロパティ業界向けに開発したインテリジェントAIアシスタントです。

### 🔒 <a name="security"></a>セキュリティ

- [firstorderai/authenticator_mcp](https://github.com/firstorderai/authenticator_mcp) 📇 🏠 🍎 🪟 🐧 – AIエージェントが認証アプリと連携できるようにする安全なMCP（Model Context Protocol）サーバー。
- [fosdickio/binary_ninja_mcp](https://github.com/Vector35/binaryninja-mcp) 🐍 🏠 🍎 🪟 🐧 - Binary NinjaのためのMCPサーバーとブリッジ。バイナリ分析とリバースエンジニアリングのためのツールを提供します。
- [Security Audit MCP Server](https://github.com/qianniuspace/mcp-security-audit) 📇 ☁️ 強力なモデルコンテキストプロトコル（MCP）サーバーで、npmパッケージ依存関係のセキュリティ脆弱性を監査します。リモートnpmレジストリ統合を備えたリアルタイムセキュリティチェックを使用して構築されています。
- [GhidraMCP](https://github.com/13bm/GhidraMCP) 🐍 ☕ 🏠 - GhidraをAIアシスタントと統合するためのMCPサーバー。このプラグインはバイナリ分析を可能にし、モデルコンテキストプロトコルを通じて関数検査、逆コンパイル、メモリ探索、インポート/エクスポート分析などのツールを提供します。
- [intruder-io/intruder-mcp](https://github.com/intruder-io/intruder-mcp) 🐍 ☁️ - [Intruder](https://www.intruder.io/) にアクセスするためのMCPサーバー。インフラストラクチャのセキュリティ脆弱性の特定、理解、修正を支援します。

### 📟 <a name="embedded-system"></a>組み込みシステム

組み込みデバイスでの作業のためのドキュメントとショートカットへのアクセスを提供します。

- [stack-chan/stack-chan](https://github.com/stack-chan/stack-chan) 📇 📟 - JavaScriptで動作するM5Stack組み込みｽｰﾊﾟｰｶﾜｲｲロボット。AI制御による対話と感情表現のためのMCPサーバー機能を搭載。

### 🌎 <a name="translation-services"></a>翻訳サービス

AIアシスタントが異なる言語間でコンテンツを翻訳できるようにする翻訳ツールとサービス。

- [translated/lara-mcp](https://github.com/translated/lara-mcp) 🎖️ 📇 ☁️ - Lara Translate APIのためのMCPサーバー。言語検出とコンテキスト対応の翻訳機能を備えた強力な翻訳機能を提供します。

### 🚆 <a name="travel-and-transportation"></a>旅行と交通

旅行および交通情報へのアクセス。スケジュール、ルート、およびリアルタイムの旅行データをクエリすることができます。

- [NS Travel Information MCP Server](https://github.com/r-huijts/ns-mcp-server) 📇 ☁️ - オランダ鉄道（NS）の旅行情報、スケジュール、およびリアルタイムの更新にアクセス
- [KyrieTangSheng/mcp-server-nationalparks](https://github.com/KyrieTangSheng/mcp-server-nationalparks) 📇 ☁️ - 米国国立公園局APIの統合で、米国国立公園の詳細情報、警報、ビジターセンター、キャンプ場、イベントの最新情報を提供

### 🔄 <a name="version-control"></a>バージョン管理

Gitリポジトリおよびバージョン管理プラットフォームとの対話。標準化されたAPIを通じて、リポジトリ管理、コード分析、プルリクエスト処理、問題追跡、およびその他のバージョン管理操作を実行できます。

- [@modelcontextprotocol/server-github](https://github.com/modelcontextprotocol/servers/tree/main/src/github) 📇 ☁️ - リポジトリ管理、PR、問題などのためのGitHub API統合
- [@modelcontextprotocol/server-gitlab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab) 📇 ☁️ 🏠 - プロジェクト管理およびCI/CD操作のためのGitLabプラットフォーム統合
- [@modelcontextprotocol/server-git](https://github.com/modelcontextprotocol/servers/tree/main/src/git) 🐍 🏠 - ローカルリポジトリの読み取り、検索、および分析を含む直接的なGitリポジトリ操作
- [Tiberriver256/mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops) 📇 ☁️ - リポジトリ管理、作業項目、パイプラインのためのAzure DevOps統合
- [kopfrechner/gitlab-mr-mcp](https://github.com/kopfrechner/gitlab-mr-mcp) 📇 ☁️ - GitLabプロジェクトの課題やマージリクエストとシームレスにやり取りできます。

### 🛠️ <a name="other-tools-and-integrations"></a>その他のツールと統合

- [apify/actors-mcp-server](https://github.com/apify/actors-mcp-server) 📇 ☁️ - 3,000以上の事前構築されたクラウドツール（Actors として知られる）を使用して、ウェブサイト、eコマース、ソーシャルメディア、検索エンジン、地図などからデータを抽出できます。
- [githejie/mcp-server-calculator](https://github.com/githejie/mcp-server-calculator) 🐍 🏠 - このサーバーは、LLMが計算機を使用して正確な数値計算を行えるようにします
- [zcaceres/markdownify-mcp](https://github.com/zcaceres/markdownify-mcp) 📇 🏠 - ほぼすべてのファイルやウェブコンテンツをMarkdownに変換するMCPサーバー
- [mzxrai/mcp-openai](https://github.com/mzxrai/mcp-openai) 📇 ☁️ - OpenAIの最も賢いモデルとチャット
- [mrjoshuak/godoc-mcp](https://github.com/mrjoshuak/godoc-mcp) 🏎️ 🏠 - Goドキュメントサーバーで、AIアシスタントがパッケージドキュメントとタイプにスマートにアクセスできるようにします。
- [fotoetienne/gqai](https://github.com/fotoetienne/gqai) 🏎 🏠 - 通常の GraphQL クエリ/ミューテーション定義ツールを使用すると、gqai によって MCP サーバーが自動的に生成されます。
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
- [kiwamizamurai/mcp-kibela-server](https://github.com/kiwamizamurai/mcp-kibela-server) - 📇 ☁️ より強力な[Kibela](https://kibe.la/)との連携
- [@awkoy/replicate-flux-mcp](https://github.com/awkoy/replicate-flux-mcp) 📇 ☁️ - Replicate APIを通じて画像を生成する機能を提供します。
- [NakaokaRei/swift-mcp-gui](https://github.com/NakaokaRei/swift-mcp-gui.git) 🏠 🍏 - キーボード入力やマウス移動などのコマンドが実行できるMCPサーバー
- [IlyaGulya/gradle-mcp-server](https://github.com/IlyaGulya/gradle-mcp-server) 🏠 - Gradle Tooling API を使用してプロジェクトを検査し、タスクを実行し、テスト結果をテストごとに報告するGradle連携
- [kelvin6365/plane-mcp-server](https://github.com/kelvin6365/plane-mcp-server) - 🏎️ 🏠 この MCP サーバーは、[Plane](https://plane.so) API を通じてプロジェクトや課題を管理するのに役立ちます
- [yuna0x0/hackmd-mcp](https://github.com/yuna0x0/hackmd-mcp) 📇 ☁️ - AIモデルが [HackMD](https://hackmd.io) と連携できるようにします。
- [HenryHaoson/Yuque-MCP-Server](https://github.com/HenryHaoson/Yuque-MCP-Server) - 📇 ☁️ 語雀APIと統合するためのModel-Context-Protocol (MCP)サーバー。AIモデルがドキュメントを管理し、ナレッジベースと対話し、コンテンツを検索し、語雀プラットフォームの分析データにアクセスできるようにします。
- [tumf/web3-mcp](https://github.com/tumf/web3-mcp) 🐍 ☁️ - Ankr Advanced APIをラップするMCPサーバー実装。イーサリアム、BSC、ポリゴン、アバランチなど複数のブロックチェーンにわたるNFT、トークン、ブロックチェーンデータにアクセスできます。
- [ttommyth/interactive-mcp](https://github.com/ttommyth/interactive-mcp) 📇 🏠 🍎 🪟 🐧 - ローカルユーザープロンプトとチャット機能を MCP ループに直接追加することで、インタラクティブな LLM ワークフローを有効にします。

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
- [TBXark/mcp-proxy](https://github.com/TBXark/mcp-proxy) 🏎️ - 複数のMCPリソースサーバーを、単一のHTTPサーバーを通して集約し、提供するMCPプロキシサーバー。


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
