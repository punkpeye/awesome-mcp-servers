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
* [クライアント](#クライアント)
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
  * 🌊 – C/C++コードベース 
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

* 🔗 - [アグリゲーター](#aggregators)
* 🎨 - [芸術と文化](#art-and-culture)
* 🧬 - [生物学、医学、バイオインフォマティクス](#bio)
* 📂 - [ブラウザ自動化](#browser-automation)
* ☁️ - [クラウドプラットフォーム](#cloud-platforms)
* 👨‍💻 - [コード実行](#code-execution)
* 🤖 - [コーディングエージェント](#coding-agents)
* 🖥️ - [コマンドライン](#command-line)
* 💬 - [コミュニケーション](#communication)
* 👤 - [顧客データプラットフォーム](#customer-data-platforms)
* 🗄️ - [データベース](#databases)
* 📊 - [データプラットフォーム](#data-platforms)
* 🚚 - [配送](#delivery)
* 🛠️ - [開発者ツール](#developer-tools)
* 🧮 - [データサイエンスツール](#data-science-tools)
* 📟 - [組み込みシステム](#embedded-system)
* 📂 - [ファイルシステム](#file-systems)
* 💰 - [金融・フィンテック](#finance--fintech)
* 🎮 - [ゲーミング](#gaming)
* 🧠 - [知識と記憶](#knowledge--memory)
* 🗺️ - [位置情報サービス](#location-services)
* 🎯 - [マーケティング](#marketing)
* 📊 - [監視](#monitoring)
* 🎥 - [マルチメディア処理](#multimedia-process)
* 🔎 - [検索・データ抽出](#search)
* 🔒 - [セキュリティ](#security)
* 🌐 - [ソーシャルメディア](#social-media)
* 🏃 - [スポーツ](#sports)
* 🎧 - [サポート・サービス管理](#support-and-service-management)
* 🌎 - [翻訳サービス](#translation-services)
* 🎧 - [テキスト読み上げ](#text-to-speech)
* 🚆 - [旅行と交通](#travel-and-transportation)
* 🔄 - [バージョン管理](#version-control)
* 🛠️ - [その他のツールと統合](#other-tools-and-integrations)

### 🔗 <a name="aggregators"></a>アグリゲーター

単一のMCPサーバーを通じて多くのアプリやツールにアクセスするためのサーバー。

- [1mcp/agent](https://github.com/1mcp-app/agent) 📇 ☁️ 🏠 🍎 🪟 🐧 - 複数のMCPサーバーを1つのMCPサーバーに集約する統一的なモデルコンテキストプロトコルサーバー実装。
- [OpenMCP](https://github.com/wegotdocs/open-mcp) 📇 🏠 🍎 🪟 🐧 - Web APIを10秒でMCPサーバーに変換し、オープンソースレジストリに追加する: https://open-mcp.org
- [mindsdb/mindsdb](https://github.com/mindsdb/mindsdb) - [MindsDBを単一のMCPサーバーとして](https://docs.mindsdb.com/mcp/overview)使用し、様々なプラットフォームとデータベース間でデータを接続・統合
- [glenngillen/mcpmcp-server](https://github.com/glenngillen/mcpmcp-server) ☁️ 📇 🍎 🪟 🐧 - MCPサーバーのリストを提供し、日常のワークフローを改善するために使用できるサーバーをクライアントに問い合わせることができる
- [pipedream/pipedream](https://github.com/PipedreamHQ/pipedream/tree/master/modelcontextprotocol) ☁️ 🏠 - 8,000以上の事前構築ツールで2,500のAPIに接続し、独自のアプリでユーザー向けサーバーを管理
- [VeriTeknik/pluggedin-mcp-proxy](https://github.com/VeriTeknik/pluggedin-mcp-proxy) 📇 🏠 - 複数のMCPサーバーを1つのインターフェースに統合する包括的なプロキシサーバー。サーバー間でツール、プロンプト、リソース、テンプレートの発見と管理を提供し、MCPサーバー構築時のデバッグ用プレイグラウンドも含む
- [tigranbs/mcgravity](https://github.com/tigranbs/mcgravity) 📇 🏠 - 複数のMCPサーバーを1つの統一エンドポイントに構成するためのプロキシツール。Nginxがウェブサーバーのために機能するのと同様に、複数のMCPサーバー間でリクエストの負荷分散を行うことで、AIツールをスケーリングします。
- [MetaMCP](https://github.com/metatool-ai/metatool-app) 📇 ☁️ 🏠 🍎 🪟 🐧 - MetaMCPは、GUIでMCP接続を管理する統合ミドルウェアMCPサーバーです。
- [WayStation-ai/mcp](https://github.com/waystation-ai/mcp) ☁️ 🍎 🪟 - Claude Desktopやその他のMCPホストを、お気に入りのアプリ（Notion、Slack、Monday、Airtableなど）にシームレスかつ安全に接続。90秒以下で完了
- [MCP Access Point](https://github.com/sxhxliang/mcp-access-point)  📇 ☁️ 🏠 🍎 🪟 🐧 - サーバー側のコードに変更を加えることなく、Web API を 1 回のクリックで MCP サーバーに変換します。。
- [hamflx/imagen3-mcp](https://github.com/hamflx/imagen3-mcp) 📇 🏠 🪟 🍎 🐧 - MCPを通じてGoogleのImagen 3.0 APIを使用する強力な画像生成ツール。高度な写真、芸術的、写実的なコントロールでテキストプロンプトから高品質な画像を生成します。
- [SureScaleAI/openai-gpt-image-mcp](https://github.com/SureScaleAI/openai-gpt-image-mcp) 📇 ☁️ - OpenAI GPT画像生成・編集MCPサーバー

### 🎨 <a name="art-and-culture"></a>芸術と文化

美術コレクション、文化遺産、博物館データベースにアクセスして探索できます。AIモデルは、芸術的および文化的なコンテンツを検索および分析できます。

- [abhiemj/manim-mcp-server](https://github.com/abhiemj/manim-mcp-server) 🐍 🏠 🪟 🐧 - Manimを使ってアニメーションを生成するローカルMCPサーバー
- [burningion/video-editing-mcp](https://github.com/burningion/video-editing-mcp) 🐍 - Video Jungle Collectionから動画編集の追加、分析、検索、生成
- [cswkim/discogs-mcp-server](https://github.com/cswkim/discogs-mcp-server) 📇 ☁️ - Discogs APIと連携するMCPサーバー
- [djalal/quran-mcp-server](https://github.com/djalal/quran-mcp-server) 📇 ☁️ 公式REST API v4を通してQuran.comコーパスと連携するMCPサーバー
- [mikechao/metmuseum-mcp](https://github.com/mikechao/metmuseum-mcp) 📇 ☁️ - コレクション内の芸術作品を検索・表示するメトロポリタン美術館コレクションAPI統合
- [r-huijts/rijksmuseum-mcp](https://github.com/r-huijts/rijksmuseum-mcp) 📇 ☁️ - 芸術作品検索、詳細、コレクションのためのライクスミュージアムAPI統合
- [r-huijts/oorlogsbronnen-mcp](https://github.com/r-huijts/oorlogsbronnen-mcp) 📇 ☁️ - オランダの歴史的第二次大戦記録、写真、文書（1940-1945）にアクセスするためのOorlogsbronnen（War Sources）API統合
- [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) 🐍 - 動画編集、カラーグレーディング、メディア管理、プロジェクト制御の強力なツールを提供するDaVinci Resolve用MCPサーバー統合
- [yuna0x0/anilist-mcp](https://github.com/yuna0x0/anilist-mcp) 📇 ☁️ - アニメとマンガの情報をAniList APIと連携するMCPサーバー
- [diivi/aseprite-mcp](https://github.com/diivi/aseprite-mcp) 🐍 🏠 - Aseprite APIを使用してピクセルアートを作成するMCPサーバー
- [omni-mcp/isaac-sim-mcp](https://github.com/omni-mcp/isaac-sim-mcp) 📇 ☁️ - NVIDIA Isaac Sim、Lab、OpenUSDなどの自然言語制御を可能にするMCPサーバーと拡張機能
- [8enSmith/mcp-open-library](https://github.com/8enSmith/mcp-open-library) 📇 ☁️ - AIアシスタントが書籍情報を検索できるOpen Library API用MCPサーバー
- [PatrickPalmer/MayaMCP](https://github.com/PatrickPalmer/MayaMCP) 🐍 🏠 - Autodesk Maya用MCPサーバー
- [cantian-ai/bazi-mcp](https://github.com/cantian-ai/bazi-mcp) 📇 🏠 ☁️ 🍎 🪟 - 包括的で正確な八字（四柱推命）の命式作成と占い情報を提供

### 🧬 <a name="bio"></a>生物学、医学、バイオインフォマティクス

- [genomoncology/biomcp](https://github.com/genomoncology/biomcp) 🐍 ☁️ - PubMed、ClinicalTrials.gov、MyVariant.infoへのアクセスを提供する生物医学研究用MCPサーバー。
- [longevity-genie/biothings-mcp](https://github.com/longevity-genie/biothings-mcp) 🐍 🏠 ☁️ - 遺伝子、遺伝的変異、薬物、分類学情報を含むBioThings APIと相互作用するMCPサーバー。
- [longevity-genie/gget-mcp](https://github.com/longevity-genie/gget-mcp) 🐍 🏠 ☁️ - 人気の`gget`ライブラリをラップした、ゲノムクエリと解析のための強力なバイオインフォマティクスツールキットを提供するMCPサーバー。
- [longevity-genie/opengenes-mcp](https://github.com/longevity-genie/opengenes-mcp) 🎖️ 🐍 🏠 ☁️ - OpenGenesプロジェクトの老化と長寿研究のためのクエリ可能なデータベース用MCPサーバー。
- [longevity-genie/synergy-age-mcp](https://github.com/longevity-genie/synergy-age-mcp) 🎖️ 🐍 🏠 ☁️ - 長寿における相乗的および拮抗的遺伝的相互作用のSynergyAgeデータベース用MCPサーバー。
- [wso2/fhir-mcp-server](https://github.com/wso2/fhir-mcp-server) 🐍 🏠 ☁️ - 高速医療相互運用性リソース（FHIR）API用モデルコンテキストプロトコルサーバー。FHIRサーバーとのシームレスな統合を提供し、AIアシスタントがSMART-on-FHIR認証サポートを使用して臨床医療データの検索、取得、作成、更新、分析を可能にします。

### ☁️ <a name="cloud-platforms"></a>クラウドプラットフォーム

クラウドプラットフォームサービスの統合。クラウドインフラストラクチャとサービスの管理と対話を可能にします。

- [Nebula-Block-Data/nebulablock-mcp-server](https://github.com/Nebula-Block-Data/nebulablock-mcp-server) 📇 🏠 - fastmcp ライブラリと統合し、NebulaBlock のすべての API 機能をツールとして提供します。
- [4everland/4everland-hosting-mcp](https://github.com/4everland/4everland-hosting-mcp) 🎖️ 📇 🏠 🍎 🐧 - Greenfield、IPFS、Arweaveなどの分散型ストレージネットワークにAI生成コードをすぐにデプロイできる4EVERLAND Hosting用MCPサーバー実装。
- [awslabs/mcp](https://github.com/awslabs/mcp) 🎖️ ☁️ - AWSサービスとリソースとのシームレスな統合のためのAWS MCPサーバー。
- [qiniu/qiniu-mcp-server](https://github.com/qiniu/qiniu-mcp-server) 🐍 ☁️ - 七牛クラウド製品に基づいて構築されたMCP、七牛クラウドストレージ、メディア処理サービスなどへのアクセスをサポート。
- [alexbakers/mcp-ipfs](https://github.com/alexbakers/mcp-ipfs) 📇 ☁️ - IPFSストレージのアップロードと操作
- [reza-gholizade/k8s-mcp-server](https://github.com/reza-gholizade/k8s-mcp-server) 🏎️ ☁️🏠 - API リソース検出、リソース管理、Pod ログ、メトリクス、イベントなど、標準化されたインターフェースを通じて Kubernetes クラスターと対話するためのツールを提供する Kubernetes モデルコンテキストプロトコル（MCP）サーバー。
- [VmLia/books-mcp-server](https://github.com/VmLia/books-mcp-server) 📇 ☁️ - 書籍クエリに使用されるMCPサーバーで、Cherry Studioなどの一般的なMCPクライアントに適用できます。
- [alexei-led/aws-mcp-server](https://github.com/alexei-led/aws-mcp-server) 🐍 ☁️ - AIアシスタントがAWS CLIコマンドを実行し、Unixパイプを使用し、マルチアーキテクチャサポート付きの安全なDocker環境で一般的なAWSタスクのプロンプトテンプレートを適用できるようにする軽量で強力なサーバー
- [alexei-led/k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server) 🐍 - AIアシスタントがマルチアーキテクチャサポート付きの安全なDocker環境でKubernetes CLIコマンド（`kubectl`、`helm`、`istioctl`、`argocd`）をUnixパイプを使用して安全に実行できるようにする軽量で堅牢なサーバー。
- [aliyun/alibaba-cloud-ops-mcp-server](https://github.com/aliyun/alibaba-cloud-ops-mcp-server) 🎖️ 🐍 ☁️ - MCPサーバーは、AIアシスタントがAlibaba Cloud上のリソースを運用・管理できるようにし、ECS、クラウドモニタリング、OOS、およびその他の広く使用されているクラウド製品をサポートします。
- [bright8192/esxi-mcp-server](https://github.com/bright8192/esxi-mcp-server) 🐍 ☁️ - MCP（Model Control Protocol）に基づくVMware ESXi/vCenter管理サーバーで、仮想マシン管理のためのシンプルなREST APIインターフェースを提供。
- [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) 🎖️ 📇 ☁️ - Workers、KV、R2、D1を含むCloudflareサービスとの統合
- [cyclops-ui/mcp-cyclops](https://github.com/cyclops-ui/mcp-cyclops) 🎖️ 🏎️ ☁️ - AIエージェントがCyclops抽象化を通じてKubernetesリソースを管理できるようにするMCPサーバー
- [flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) 📇 ☁️🏠 - Pod、デプロイメント、サービスのKubernetesクラスター操作のTypeScript実装。
- [hardik-id/azure-resource-graph-mcp-server](https://github.com/hardik-id/azure-resource-graph-mcp-server) 📇 ☁️🏠 - Azure Resource Graphを使用してAzureリソースを大規模にクエリおよび分析するためのModel Context Protocolサーバー。AIアシスタントがAzureインフラストラクチャを探索および監視できるようにします。
- [jdubois/azure-cli-mcp](https://github.com/jdubois/azure-cli-mcp) - Azureと直接対話できるAzure CLIコマンドラインのラッパー
- [johnneerdael/netskope-mcp](https://github.com/johnneerdael/netskope-mcp) 🔒 ☁️ - 詳細なセットアップ情報とLLMの使用例を含む、Netskope Private Access環境内のすべてのNetskope Private Accessコンポーネントへのアクセスを提供するMCP。
- [manusa/Kubernetes MCP Server](https://github.com/manusa/kubernetes-mcp-server) 🏎️ 🏠 - OpenShiftの追加サポートを備えた強力なKubernetes MCPサーバー。**任意の**Kubernetesリソースに対するCRUD操作の提供に加えて、このサーバーはクラスターと対話するための専用ツールを提供します。
- [nwiizo/tfmcp](https://github.com/nwiizo/tfmcp) 🦀 🏠 - AIアシスタントがTerraform環境を管理および操作できるようにするTerraform MCPサーバー。設定の読み取り、プランの分析、設定の適用、Terraformステートの管理を可能にします。
- [pulumi/mcp-server](https://github.com/pulumi/mcp-server) 🎖️ 📇 🏠 - Pulumi Automation APIとPulumi Cloud APIを使用してPulumiと対話するためのMCPサーバー。MCPクライアントがパッケージ情報の取得、変更のプレビュー、更新のデプロイ、スタック出力の取得などのPulumi操作をプログラムで実行できるようにします。
- [rohitg00/kubectl-mcp-server](https://github.com/rohitg00/kubectl-mcp-server) 🐍 ☁️🏠 - Claude、Cursor、その他のAIアシスタントが自然言語を通じてKubernetesクラスターと対話できるようにするKubernetes用Model Context Protocol（MCP）サーバー。
- [strowk/mcp-k8s-go](https://github.com/strowk/mcp-k8s-go) 🏎️ ☁️🏠 - MCPを通じたKubernetesクラスター操作
- [thunderboltsid/mcp-nutanix](https://github.com/thunderboltsid/mcp-nutanix) 🏎️ 🏠☁️ - Nutanix Prism CentralリソースとインターフェースするためのGoベースのMCPサーバー。
- [trilogy-group/aws-pricing-mcp](https://github.com/trilogy-group/aws-pricing-mcp) 🏎️ ☁️🏠 - 一回の呼び出しで最新のEC2価格情報を取得。高速。事前解析済みのAWS価格カタログを使用。
- [weibaohui/k8m](https://github.com/weibaohui/k8m) 🏎️ ☁️🏠 - MCPマルチクラスターKubernetesの管理と運用を提供し、管理インターフェース、ログ機能を備え、一般的なDevOpsおよび開発シナリオをカバーする約50種類のツールを内蔵。標準リソースおよびCRDリソースをサポート。
- [weibaohui/kom](https://github.com/weibaohui/kom) 🏎️ ☁️🏠 - MCPマルチクラスターKubernetesの管理と運用を提供。SDKとして自身のプロジェクトに統合可能で、一般的なDevOpsおよび開発シナリオをカバーする約50種類のツールを内蔵。標準リソースおよびCRDリソースをサポート。
- [wenhuwang/mcp-k8s-eye](https://github.com/wenhuwang/mcp-k8s-eye) 🏎️ ☁️🏠 - Kubernetesクラスターのリソース管理と、クラスターとアプリケーションの健全性ステータスの詳細な分析を提供します。
- [erikhoward/adls-mcp-server](https://github.com/erikhoward/adls-mcp-server) 🐍 ☁️🏠 - Azure Data Lake Storage用MCPサーバー。コンテナの管理、コンテナファイルの読み取り/書き込み/アップロード/ダウンロード操作、ファイルメタデータの管理が可能。
- [silenceper/mcp-k8s](https://github.com/silenceper/mcp-k8s) 🏎️ ☁️🏠 - MCP-K8Sは、AI駆動のKubernetesリソース管理ツールで、自然言語インタラクションを通じて、ユーザーがKubernetesクラスター内の任意のリソース（ネイティブリソース（DeploymentやServiceなど）やカスタムリソース（CRD）を含む）を操作できるようにします。複雑なコマンドを覚える必要はなく、要件を説明するだけで、AIが対応するクラスター操作を正確に実行し、Kubernetesの使いやすさを大幅に向上させます。
- [redis/mcp-redis-cloud](https://github.com/redis/mcp-redis-cloud) 📇 ☁️ - 自然言語を使用してRedis Cloudリソースを簡単に管理。データベースの作成、サブスクリプションの監視、シンプルなコマンドでクラウドデプロイメントの設定。
- [portainer/portainer-mcp](https://github.com/portainer/portainer-mcp) 🏎️ ☁️🏠 - 強力なMCPサーバーで、AIアシスタントがPortainerインスタンスとシームレスに連携し、コンテナ管理、デプロイメント操作、インフラストラクチャ監視機能に自然言語でアクセスできるようにします。

### 👨‍💻 <a name="code-execution"></a>コード実行

コード実行サーバー。LLMが安全な環境でコードを実行できるようにし、コーディングエージェントなどに使用されます。

- [pydantic/pydantic-ai/mcp-run-python](https://github.com/pydantic/pydantic-ai/tree/main/mcp-run-python) 🐍 🏠- MCPツールコールを介して安全なサンドボックスでPythonコードを実行
- [yepcode/mcp-server-js](https://github.com/yepcode/mcp-server-js) 🎖️ 📇 ☁️ - 安全でスケーラブルなサンドボックス環境でLLM生成コードを実行し、NPMやPyPIパッケージの完全サポートでJavaScriptやPythonを使用してMCPツールを作成
- [ckanthony/openapi-mcp](https://github.com/ckanthony/openapi-mcp) 🏎️ ☁️ - OpenAPI-MCP：既存のAPIドキュメントを持つ任意のAPIへのアクセスを可能にするDockerized MCPサーバー。
- [alfonsograziano/node-code-sandbox-mcp](https://github.com/alfonsograziano/node-code-sandbox-mcp) 📇 🏠 – その場でのnpm依存関係インストールとクリーンな破棄を含む、JavaScriptスニペット実行のための分離されたDockerベースサンドボックスを立ち上げるNode.js MCPサーバー
- [r33drichards/mcp-js](https://github.com/r33drichards/mcp-js) 🦀 🏠 🐧 🍎 - v8を使用してAI生成のJavaScriptをローカルで恐れることなく実行するJavaScriptコード実行サンドボックス。永続セッション用のヒープスナップショットをサポート。

### 🤖 <a name="coding-agents"></a>コーディングエージェント

LLMがコードの読み取り、編集、実行を行い、一般的なプログラミングタスクを完全に自律的に解決できるフル機能のコーディングエージェント。

- [oraios/serena](https://github.com/oraios/serena)🐍🏠 - 言語サーバーを使用したシンボリックコード操作に依存するフル機能のコーディングエージェント。
- [ezyang/codemcp](https://github.com/ezyang/codemcp) 🐍🏠 - 基本的な読み取り、書き込み、コマンドラインツールを備えたコーディングエージェント。
- [doggybee/mcp-server-leetcode](https://github.com/doggybee/mcp-server-leetcode) 📇 ☁️ - AIモデルがLeetCode問題を検索、取得、解決できるMCPサーバー。メタデータフィルタリング、ユーザープロファイル、提出、コンテストデータアクセスをサポート。
- [jinzcdev/leetcode-mcp-server](https://github.com/jinzcdev/leetcode-mcp-server) 📇 ☁️ - **LeetCode**のプログラミング問題、解答、提出、公開データへの自動アクセスを可能にするMCPサーバー。`leetcode.com`（グローバル）と`leetcode.cn`（中国）の両サイトをサポート。
- [juehang/vscode-mcp-server](https://github.com/juehang/vscode-mcp-server) 📇 🏠 - ClaudeなどのAIがVS Codeワークスペースのディレクトリ構造を読み取り、リンター及び言語サーバーによって検出された問題を確認し、コードファイルを読み取り、編集を行うことを可能にするMCPサーバー。
- [micl2e2/code-to-tree](https://github.com/micl2e2/code-to-tree) 🌊 🏠 📟 🐧 🪟 🍎 - 言語に関係なくソースコードをASTに変換する単一バイナリMCPサーバー。

### 🖥️ <a name="command-line"></a>コマンドライン

コマンドの実行、出力の取得、シェルやコマンドラインツールとの対話。

- [ferrislucas/iterm-mcp](https://github.com/ferrislucas/iterm-mcp) 🖥️ 🛠️ 💬 - iTermへのアクセスを提供するモデルコンテキストプロトコルサーバー。コマンドを実行し、iTermターミナルで見た内容について質問することができます。
- [g0t4/mcp-server-commands](https://github.com/g0t4/mcp-server-commands) 📇 🏠 - `run_command`と`run_script`ツールで任意のコマンドを実行。
- [maxim-saplin/mcp_safe_local_python_executor](https://github.com/maxim-saplin/mcp_safe_local_python_executor) - HF SmolagentsのLocalPythonExecutorベースの安全なPythonインタープリター
- [MladenSU/cli-mcp-server](https://github.com/MladenSU/cli-mcp-server) 🐍 🏠 - 安全な実行とカスタマイズ可能なセキュリティポリシーを備えたコマンドラインインターフェース
- [OthmaneBlial/term_mcp_deepseek](https://github.com/OthmaneBlial/term_mcp_deepseek) 🐍 🏠 - ターミナル用のDeepSeek MCPライクサーバー
- [tumf/mcp-shell-server](https://github.com/tumf/mcp-shell-server) - モデルコンテキストプロトコル（MCP）を実装する安全なシェルコマンド実行サーバー
- [automateyournetwork/pyATS_MCP](https://github.com/automateyournetwork/pyATS_MCP) - 構造化されたモデル駆動によるネットワークデバイスとの対話を可能にするCisco pyATSサーバー。
- [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) 📇 🏠 🍎 🪟 🐧 - プログラムの管理/実行、コードやテキストファイルの読み取り/書き込み/検索/編集ができるスイス・アーミー・ナイフ。
- [tufantunc/ssh-mcp](https://github.com/tufantunc/ssh-mcp) 📇 🏠 🐧 🪟 - モデルコンテキストプロトコル経由でLinuxおよびWindowsサーバーのSSH制御を公開するMCPサーバー。パスワードまたはSSHキー認証でリモートシェルコマンドを安全に実行。

### 💬 <a name="communication"></a>コミュニケーション

メッセージ管理とチャネル操作のためのコミュニケーションプラットフォームとの統合。AIモデルがチームコミュニケーションツールと対話できるようにします。

- [@modelcontextprotocol/server-slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack) 📇 ☁️ - チャネル管理とメッセージングのためのSlackワークスペース統合
- [@keturiosakys/bluesky-context-server](https://github.com/keturiosakys/bluesky-context-server) 📇 ☁️ - クエリとインタラクションのためのBlueskyインスタンス統合
- [MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite) - 🐍 ☁️ - GmailとGoogleカレンダーとの統合。
- [gotoolkits/wecombot](https://github.com/gotoolkits/mcp-wecombot-server.git) - 🚀 ☁️  - MCPサーバーアプリケーションは、WeComグループロボットにさまざまなタイプのメッセージを送信します。
- [line/line-bot-mcp-server](https://github.com/line/line-bot-mcp-server) 🎖 📇 ☁️ - Messaging APIを利用したLINE公式アカウントとの統合
- [ztxtxwd/open-feishu-mcp-server](https://github.com/ztxtxwd/open-feishu-mcp-server) 📇 ☁️ 🏠 - 内蔵のFeishu OAuth認証を持つModel Context Protocol（MCP）サーバーで、リモート接続をサポートし、ブロック作成、コンテンツ更新、高度な機能を含む包括的なFeishuドキュメント管理ツールを提供します。
- [sawa-zen/vrchat-mcp](https://github.com/sawa-zen/vrchat-mcp) - 📇 🏠 VRChat APIと対話するためのMCPサーバーです。VRChatのフレンドやワールド、アバターなどの情報を取得することができます。
- [takumi0706/google-calendar-mcp](https://github.com/takumi0706/google-calendar-mcp) 📇 ☁️ - GoogleカレンダーAPIと連携するためのMCPサーバーです。GoogleCalendar APIの作成、更新、取得、削除ができます。また、TypeScriptベースです。
- [teddyzxcv/ntfy-mcp](https://github.com/teddyzxcv/ntfy-mcp) ntfy を使用してスマートフォンに通知を送信し、情報を確実に伝達する MCP サーバーです。
- [YCloud-Developers/ycloud-whatsapp-mcp-server](https://github.com/YCloud-Developers/ycloud-whatsapp-mcp-server) 📇 🏠 - YCloudプラットフォーム経由でWhatsAppビジネスメッセージを送信するためのMCPサーバー。
- [jaipandya/producthunt-mcp-server](https://github.com/jaipandya/producthunt-mcp-server) 🐍 🏠 - Product Huntのための MCP サーバー。トレンド投稿、コメント、コレクション、ユーザーなどと対話できます。
- [areweai/tsgram-mcp](https://github.com/areweai/tsgram-mcp) - TSgram: TypeScriptでスマートフォンからローカルワークスペースへアクセス可能なTelegram + Claude。移動中にコードを読み書きしてvibe code

### 👤 <a name="customer-data-platforms"></a>顧客データプラットフォーム

顧客データプラットフォーム内の顧客プロファイルへのアクセスを提供します。

- [sergehuber/inoyu-mcp-unomi-server](https://github.com/sergehuber/inoyu-mcp-unomi-server) 📇 ☁️ - Apache Unomi CDPサーバー上のプロファイルにアクセスし、更新するためのMCPサーバー。
- [@antv/mcp-server-chart](https://github.com/antvis/mcp-server-chart) 🎖️ 📇 ☁️ - [AntV](https://github.com/antvis) をベースにしたデータ可視化チャートを生成する MCP Server プラグイン。
- [Danielpeter-99/calcom-mcp](https://github.com/Danielpeter-99/calcom-mcp) 🐍 🏠 - Cal.com 用の MCP サーバー。イベントタイプの管理、予約の作成、LLM を通じた Cal.com のスケジューリングデータへのアクセスが可能です。
- [hustcc/mcp-echarts](https://github.com/hustcc/mcp-echarts) 📇 🏠 - AI が動的に生成する [Apache ECharts](https://echarts.apache.org) 構文のビジュアルチャート MCP。
- [hustcc/mcp-mermaid](https://github.com/hustcc/mcp-mermaid) 📇 🏠 - AI が動的に [Mermaid](https://mermaid.js.org/) の構文を使用して可視化チャートMCPを生成します。

### 🗄️ <a name="databases"></a>データベース

スキーマ検査機能を備えた安全なデータベースアクセス。読み取り専用アクセスを含む構成可能なセキュリティ制御を使用してデータをクエリおよび分析することができます。

- [qiniu/qiniu-mcp-server](https://github.com/qiniu/qiniu-mcp-server) 🐍 ☁️ - 七牛クラウド製品に基づいて構築されたMCP、七牛クラウドストレージ、メディア処理サービスなどへのアクセスをサポート。
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
- [prisma/mcp](https://github.com/prisma/mcp) 📇 ☁️ 🏠 - LLMがPrismaのPostgresデータベースを管理できるようにします（例: 新しいデータベースを立ち上げ、マイグレーションやクエリを実行）。
- [ydb/ydb-mcp](https://github.com/ydb-platform/ydb-mcp) 🎖️ 🐍 ☁️ – MCPサーバー：[YDB](https://ydb.tech)データベースと対話するための。

### 📊 <a name="data-platforms"></a>データプラットフォーム

データ統合、変換、パイプライン オーケストレーションのためのデータ プラットフォーム。

- [flowcore/mcp-flowcore-platform](https://github.com/flowcore-io/mcp-flowcore-platform) 🎖️📇☁️🏠 - Flowcore と対話してアクションを実行し、データを取り込み、データ コア内またはパブリック データ コア内のあらゆるデータを分析、相互参照、活用します。これらはすべて人間の言語で実行できます。

### 🚚 <a name="delivery"></a>配送

配送およびロジスティクスサービスの統合。

- [jordandalton/doordash-mcp-server](https://github.com/JordanDalton/DoorDash-MCP-Server) 🐍 – DoorDash配送（非公式）

### 🛠️ <a name="developer-tools"></a>開発者ツール

開発ワークフローと環境管理を強化するツールと統合。

- [Hypersequent/qasphere-mcp](https://github.com/Hypersequent/qasphere-mcp) 🎖️ 📇 ☁️ - [QA Sphere](https://qasphere.com/)テスト管理システムとの統合。LLMがテストケースを発見、要約、操作できるようにし、AI搭載IDEから直接アクセス可能
- [QuantGeekDev/docker-mcp](https://github.com/QuantGeekDev/docker-mcp) 🏎️ 🏠 - MCPを通じたDockerコンテナの管理と操作
- [zcaceres/fetch-mcp](https://github.com/zcaceres/fetch-mcp) 📇 🏠 - JSON、テキスト、HTMLデータを柔軟に取得するためのMCPサーバー
- [zcaceres/gtasks-mcp](https://github.com/zcaceres/gtasks-mcp) - 📇 ☁️ - Google タスクを管理するための MCP サーバー
- [snaggle-ai/openapi-mcp-server](https://github.com/snaggle-ai/openapi-mcp-server) 🏎️ 🏠 - Open API spec (v3) を使用して任意のHTTP/REST APIサーバーに接続
- [@joshuarileydev/terminal-mcp-server](https://www.npmjs.com/package/@joshuarileydev/terminal-mcp-server) 📇 🏠 - 任意のシェルターミナルコマンドを実行するためのMCPサーバー
- [tumf/mcp-text-editor](https://github.com/tumf/mcp-text-editor) - ラインエディタ 行単位の取得と編集ができるので、特に大きなファイルの一部書き換えを効率的に行う
- [ferrislucas/iterm-mcp](https://github.com/ferrislucas/iterm-mcp) 🖥️ 🛠️ 💬 - iTermへのアクセスを提供するモデルコンテキストプロトコルサーバー。コマンドを実行し、iTermターミナルで見た内容について質問することができます。
- [Rootly-AI-Labs/Rootly-MCP-server](https://github.com/Rootly-AI-Labs/Rootly-MCP-server) 🎖️🐍☁️🍎 - インシデント管理プラットフォーム[Rootly](https://rootly.com/)向けのMCPサーバー
- [YuChenSSR/mindmap-mcp-server](https://github.com/YuChenSSR/mindmap-mcp-server) 🐍 🏠 - きれいなインタラクティブなマインドマップを生成するためのモデルコンテキストプロトコル（MCP）サーバ。
- [InhiblabCore/mcp-image-compression](https://github.com/InhiblabCore/mcp-image-compression) 🐍 🏠 - 様々な画像フォーマットのローカル圧縮のためのMCPサーバー。
- [SDGLBL/mcp-claude-code](https://github.com/SDGLBL/mcp-claude-code) 🐍 🏠 - MCPを使用したClaude Code機能の実装で、AIによるコード理解、修正、プロジェクト分析を包括的なツールサポートで実現します。
- [api7/apisix-mcp](https://github.com/api7/apisix-mcp) 🎖️ 📇 🏠 [Apache APISIX](https://github.com/apache/apisix) のすべてのリソースの照会と管理をサポートするMCPサービス。
- [davidan90/time-node-mcp](https://github.com/davidan90/time-node-mcp) 📇 🏠 - IANAタイムゾーン対応の日時操作、タイムゾーン変換、夏時間の処理をサポート。
- [endorhq/cli](https://github.com/endorhq/cli) 📇 ☁️ 🏠 🪟 🐧 🍎 - Endorを使用すると、AIエージェントはMariaDB、Postgres、Redis、Memcached、Alpine、Valkeyなどのサービスを隔離されたサンドボックス内で実行できます。5秒以内に起動する、事前構成済みのアプリケーションを入手できます。.
- [ios-simulator-mcp](https://github.com/joshuayoes/ios-simulator-mcp) 📇 🏠 🍎 - iOS シミュレータと対話するためのモデル コンテキスト プロトコル (MCP) サーバー。このサーバーを使用すると、iOS シミュレータに関する情報を取得したり、UI の対話を制御したり、UI 要素を検査したりして、iOS シミュレータと対話できます。
- [higress-group/higress-ops-mcp-server](https://github.com/higress-group/higress-ops-mcp-server) 🐍 🏠 - MCP サーバーが [Higress](https://github.com/alibaba/higress/blob/main/README_JP.md) ゲートウェイの構成と操作を管理するための全面的なツールを提供します。
- [yiwenlu66/PiloTY](https://github.com/yiwenlu66/PiloTY) 🐍 🏠 - AIエージェントが状態保持セッション、SSH接続、バックグラウンドプロセス管理を使ってインタラクティブターミナルを制御できるPTY操作のAIパイロット
- [ReAPI-com/mcp-openapi](https://github.com/ReAPI-com/mcp-openapi) 📇 🏠 - LLMがOpenAPI仕様のすべてを理解し、コードの発見、説明、生成、モックデータの作成を可能にするMCPサーバー
- [automation-ai-labs/mcp-link](https://github.com/automation-ai-labs/mcp-link) 🏎️ 🏠 - OpenAPIスキーマを使用してAIエージェントと任意のAPIをシームレスに統合
- [cjo4m06/mcp-shrimp-task-manager](https://github.com/cjo4m06/mcp-shrimp-task-manager) 📇 ☁️ 🏠 – Cursor AI のようなコーディングエージェントを強化するために設計された、プログラミング特化型のタスク管理システム。高度なタスク記憶、自省、依存関係の管理機能を備えています。[ShrimpTaskManager](https://cjo4m06.github.io/mcp-shrimp-task-manager)
- [axliupore/mcp-code-runner](https://github.com/axliupore/mcp-code-runner) 📇 🏠 - Docker 経由でローカルにコードを実行し、複数のプログラミング言語をサポートする MCP サーバー
- [TencentEdgeOne/edgeone-pages-mcp](https://github.com/TencentEdgeOne/edgeone-pages-mcp) 📇 ☁️ - EdgeOne Pagesに HTMLコンテンツをデプロイし、公開アクセス可能なURLを取得するためのMCPサービスです。
- [lpigeon/ros-mcp-server](https://github.com/lpigeon/ros-mcp-server) 🐍 🏠 🍎 🪟 🐧 - ROS MCPサーバーは、ユーザーの自然言語コマンドをROSまたはROS2の制御コマンドに変換することで、ロボットの制御を支援します。
- [HainanZhao/mcp-gitlab-jira](https://github.com/HainanZhao/mcp-gitlab-jira) 📇 ☁️ 🏠 - GitLabとJiraの統合MCPサーバー：AIエージェントでプロジェクト、マージリクエスト、ファイル、リリース、チケットを管理します。
- [freema/mcp-design-system-extractor](https://github.com/freema/mcp-design-system-extractor) 📇 🏠 - Storybookデザインシステムからコンポーネント情報を抽出します。HTML、スタイル、props、依存関係、テーマトークン、コンポーネントメタデータを提供し、AIによるデザインシステム分析を可能にします。
- [gitkraken/gk-cli](https://github.com/gitkraken/gk-cli) 🎖️ 🏎️ 🏠 ☁️ 🍎 🪟 🐧 - GitKraken の API とやり取りするための CLI。gk mcp 経由で MCP サーバーも含まれており、GitKraken の API だけでなく、Jira、GitHub、GitLab などもラップします。ローカルツールやリモートサービスとも連携可能です。
- [lpigeon/unitree-go2-mcp-server](https://github.com/lpigeon/unitree-go2-mcp-server) 🐍 🏠 🐧 - Unitree Go2 MCPサーバーは、MCP上に構築されたサーバーで、大規模言語モデル（LLM）によって解釈された自然言語コマンドを使用して、ユーザーがUnitree Go2ロボットを制御できるようにします。

### 🧮 <a name="data-science-tools"></a>データサイエンスツール

データ分析、機械学習、統計計算のためのツールとプラットフォーム。

- [bright8192/esxi-mcp-server](https://github.com/bright8192/esxi-mcp-server) 🐍 ☁️ - MCP（Model Control Protocol）に基づくVMware ESXi/vCenter管理サーバーで、仮想マシン管理のためのシンプルなREST APIインターフェースを提供
- [c4pt0r/mcp-server-tidb](https://github.com/c4pt0r/mcp-server-tidb) 🐍 ☁️ - TiDBデータベースの統合、テーブル構造の作成（DDL）およびSQLの実行
- [ergut/mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server) 📇 ☁️ - Google BigQuery統合のためのサーバー実装で、直接的なBigQueryデータベースアクセスとクエリ機能を提供
- [julien040/anyquery](https://github.com/julien040/anyquery) 🏎️ 🏠 ☁️ - SQLを使用して40以上のアプリを1つのバイナリでクエリ。PostgreSQL、MySQL、またはSQLite互換データベースに接続することも可能。ローカルファーストでプライベート設計。
- [QuantGeekDev/mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp) 📇 🏠 - LLMがデータベースと直接対話できるようにするMongoDB統合
- [runekaagaard/mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy) 🐍 🏠 - PostgreSQL、MySQL、MariaDB、SQLite、Oracle、MS SQL Serverなど多数のデータベースをサポートするSQLAlchemyベースの汎用データベース統合。スキーマと関係の検査、大規模データセット分析機能を備えています
- [tinybirdco/mcp-tinybird](https://github.com/tinybirdco/mcp-tinybird) 🐍 ☁️ - クエリとAPI機能を備えたTinybird統合

### 📟 <a name="embedded-system"></a>組み込みシステム

組み込みデバイスでの作業のためのドキュメントとショートカットへのアクセスを提供。

- [horw/esp-mcp](https://github.com/horw/esp-mcp) 📟 - ESP-IDFを使用したESP32シリーズチップのビルド問題修正ワークフロー。
- [kukapay/modbus-mcp](https://github.com/kukapay/modbus-mcp) 🐍 📟 - 産業用Modbusデータを標準化し、コンテキスト化するMCPサーバー。
- [kukapay/opcua-mcp](https://github.com/kukapay/opcua-mcp) 🐍 📟 - OPC UA対応の産業システムに接続するMCPサーバー。
- [yoelbassin/gnuradioMCP](https://github.com/yoelbassin/gnuradioMCP) 🐍 📟 🏠 - LLMがRF `.grc`フローチャートを自律的に作成・修正できるGNU Radio用MCPサーバー。

### 💰 <a name="finance--fintech"></a>金融・フィンテック

金融市場、取引、暗号通貨、投資プラットフォームとの統合。

- [A1X5H04/binance-mcp-server](https://github.com/A1X5H04/binance-mcp-server) 🐍 ☁️ - Binance APIとの統合で、暗号通貨価格、市場データ、口座情報へのアクセスを提供
- [akdetrick/mcp-teller](https://github.com/akdetrick/mcp-teller) 🐍 🏠 - カナダのフィンテック企業Tellerのアカウント集約APIへのアクセス
- [fatwang2/alpaca-trade-mcp](https://github.com/fatwang2/alpaca-trade-mcp) 📇 ☁️ - Alpaca取引プラットフォームとの統合
- [fatwang2/coinbase-mcp](https://github.com/fatwang2/coinbase-mcp) 📇 ☁️ - Coinbase Advanced Trade APIとの統合
- [fatwang2/robinhood-mcp](https://github.com/fatwang2/robinhood-mcp) 📇 ☁️ - Robinhood取引プラットフォームとの統合
- [HuggingAGI/mcp-baostock-server](https://github.com/HuggingAGI/mcp-baostock-server) 🐍 ☁️ - baostockに基づくMCPサーバーで、中国株式市場データへのアクセスと分析機能を提供
- [jarvis2f/polygon-mcp](https://github.com/jarvis2f/polygon-mcp) 🐍 ☁️ - Polygon.io金融市場データAPIへのアクセス
- [kukapay/dune-analytics-mcp](https://github.com/kukapay/dune-analytics-mcp) 🐍 ☁️ - AIエージェントにDune Analyticsデータを橋渡しするMCPサーバー
- [kukapay/etf-flow-mcp](https://github.com/kukapay/etf-flow-mcp) 🐍 ☁️ - 暗号通貨ETFフローデータを提供してAIエージェントの意思決定を支援
- [kukapay/freqtrade-mcp](https://github.com/kukapay/freqtrade-mcp) 🐍 ☁️ - Freqtrade暗号通貨取引ボットと統合するMCPサーバー
- [kukapay/funding-rates-mcp](https://github.com/kukapay/funding-rates-mcp) 🐍 ☁️ - 主要な暗号通貨取引所のリアルタイム資金調達率データを提供
- [kukapay/jupiter-mcp](https://github.com/kukapay/jupiter-mcp) 🐍 ☁️ - JupiterのUltra APIを使用してSolanaブロックチェーンでトークンスワップを実行するMCPサーバー
- [kukapay/pancakeswap-poolspy-mcp](https://github.com/kukapay/pancakeswap-poolspy-mcp) 🐍 ☁️ - PancakeSwapで新しく作成されたプールを追跡するMCPサーバー
- [kukapay/rug-check-mcp](https://github.com/kukapay/rug-check-mcp) 🐍 ☁️ - Solanaミームトークンの潜在的リスクを検出するMCPサーバー
- [kukapay/thegraph-mcp](https://github.com/kukapay/thegraph-mcp) 🐍 ☁️ - AIエージェントにThe Graphからのインデックス済みブロックチェーンデータを提供するMCPサーバー
- [kukapay/token-minter-mcp](https://github.com/kukapay/token-minter-mcp) 🐍 ☁️ - AIエージェントが複数のブロックチェーンでERC-20トークンをミントするためのツールを提供するMCPサーバー
- [kukapay/token-revoke-mcp](https://github.com/kukapay/token-revoke-mcp) 🐍 ☁️ - 複数のブロックチェーンでERC-20トークンの許可をチェックおよび取り消すためのMCPサーバー
- [kukapay/twitter-username-changes-mcp](https://github.com/kukapay/twitter-username-changes-mcp) 🐍 ☁️ - Twitterユーザー名の履歴変更を追跡するMCPサーバー
- [kukapay/uniswap-poolspy-mcp](https://github.com/kukapay/uniswap-poolspy-mcp) 🐍 ☁️ - 複数のブロックチェーンでUniswapの新しく作成された流動性プールを追跡するMCPサーバー
- [kukapay/uniswap-trader-mcp](https://github.com/kukapay/uniswap-trader-mcp) 🐍 ☁️ - AIエージェントが複数のブロックチェーンでUniswap DEXでのトークンスワップを自動化するMCPサーバー
- [kukapay/whale-tracker-mcp](https://github.com/kukapay/whale-tracker-mcp) 🐍 ☁️ - 暗号通貨クジラ取引を追跡するMCPサーバー
- [laukikk/alpaca-mcp](https://github.com/laukikk/alpaca-mcp) 🐍 ☁️ - 株式と暗号通貨ポートフォリオの管理、取引の実行、市場データへのアクセスを提供するAlpaca取引API用MCPサーバー
- [longportapp/openapi](https://github.com/longportapp/openapi/tree/main/mcp) 🐍 ☁️ - LongPort OpenAPIはリアルタイム株式市場データを提供し、MCPを通じてAIアクセス分析と取引機能を提供
- [mcpdotdirect/evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server) 📇 ☁️ - 30以上のEVMネットワークのための包括的なブロックチェーンサービス、ネイティブトークン、ERC20、NFT、スマートコントラクト、取引、ENS解決をサポート
- [mcpdotdirect/starknet-mcp-server](https://github.com/mcpdotdirect/starknet-mcp-server) 📇 ☁️ - ネイティブトークン（ETH、STRK）、スマートコントラクト、StarknetID解決、トークン転送をサポートする包括的なStarknetブロックチェーン統合
- [minhyeoky/mcp-server-ledger](https://github.com/minhyeoky/mcp-server-ledger) 🐍 🏠 - 金融取引の管理とレポート生成のためのledger-cli統合
- [openMF/mcp-mifosx](https://github.com/openMF/mcp-mifosx) ☁️ 🏠 - クライアント、ローン、貯蓄、株式、金融取引の管理と金融レポート生成のためのコアバンキング統合
- [narumiruna/yfinance-mcp](https://github.com/narumiruna/yfinance-mcp) 🐍 ☁️ - yfinanceを使用してYahoo Financeから情報を取得するMCPサーバー
- [polygon-io/mcp_polygon](https://github.com/polygon-io/mcp_polygon) 🐍 ☁️ - 株式、インデックス、外国為替、オプションなどの[Polygon.io](https://polygon.io/)金融市場データAPIへのアクセスを提供するMCPサーバー
- [pwh-pwh/coin-mcp-server](https://github.com/pwh-pwh/coin-mcp-server) 🐍 ☁️ - 暗号通貨価格を取得するためのBitget API
- [QuantGeekDev/coincap-mcp](https://github.com/QuantGeekDev/coincap-mcp) 📇 ☁️ - CoinCapのパブリックAPIを使用したリアルタイム暗号通貨市場データ統合、APIキー不要で暗号通貨価格と市場情報へのアクセスを提供
- [SaintDoresh/Crypto-Trader-MCP-ClaudeDesktop](https://github.com/SaintDoresh/Crypto-Trader-MCP-ClaudeDesktop.git) 🐍 ☁️ - CoinGecko APIを使用して暗号通貨市場データを提供するMCPツール
- [tooyipjee/yahoofinance-mcp](https://github.com/tooyipjee/yahoofinance-mcp.git) 📇 ☁️ - Yahoo Finance MCP のTypeScript版
- [SaintDoresh/YFinance-Trader-MCP-ClaudeDesktop](https://github.com/SaintDoresh/YFinance-Trader-MCP-ClaudeDesktop.git) 🐍 ☁️ - Yahoo Finance APIを使用して株式市場データと分析を提供するMCPツール
- [RomThpt/xrpl-mcp-server](https://github.com/RomThpt/mcp-xrpl) 📇 ☁️ - アカウント情報、取引履歴、ネットワークデータへのアクセスを提供するXRP Ledger用MCPサーバー。台帳オブジェクトの照会、取引の送信、XRPLネットワークの監視が可能
- [janswist/mcp-dexscreener](https://github.com/janswist/mcp-dexscreener) 📇 ☁️ - オープンで無料のDexscreener APIを使用したリアルタイムオンチェーン市場価格
- [wowinter13/solscan-mcp](https://github.com/wowinter13/solscan-mcp) 🦀 🏠 - Solscan APIを使用してSolana取引を自然言語でクエリするMCPツール
- [zlinzzzz/finData-mcp-server](https://github.com/zlinzzzz/finData-mcp-server) 🐍 ☁️ - Tushareなどの複数のデータプロバイダーをサポートする、プロフェッショナル金融データにアクセスするためのMCPサーバー
- [silenceper/mcp-k8s](https://github.com/silenceper/mcp-k8s) 🏎️ ☁️🏠 - MCP-K8Sは、AI駆動のKubernetesリソース管理ツールで、自然言語インタラクションを通じて、ユーザーがKubernetesクラスター内の任意のリソース（ネイティブリソース（DeploymentやServiceなど）やカスタムリソース（CRD）を含む）を操作できるようにします。複雑なコマンドを覚える必要はなく、要件を説明するだけで、AIが対応するクラスター操作を正確に実行し、Kubernetesの使いやすさを大幅に向上させます。
- [redis/mcp-redis-cloud](https://github.com/redis/mcp-redis-cloud) 📇 ☁️ - 自然言語を使用してRedis Cloudリソースを簡単に管理。データベースの作成、サブスクリプションの監視、シンプルなコマンドでクラウドデプロイメントの設定。
- [portainer/portainer-mcp](https://github.com/portainer/portainer-mcp) 🏎️ ☁️🏠 - 強力なMCPサーバーで、AIアシスタントがPortainerインスタンスとシームレスに連携し、コンテナ管理、デプロイメント操作、インフラストラクチャ監視機能に自然言語でアクセスできるようにします。
- [optuna/optuna-mcp](https://github.com/optuna/optuna-mcp) 🎖️ 🐍 🏠 🐧 🍎 - [Optuna](https://optuna.org/)と連携し、ハイパーパラメータ探索をはじめとする各種最適化タスクのシームレスなオーケストレーションを可能にする公式MCPサーバー。
- [JamesANZ/prediction-market-mcp](https://github.com/JamesANZ/prediction-market-mcp) 📇 ☁️ - Polymarket、PredictIt、Kalshiを含む複数のプラットフォームからのリアルタイム予測市場データを提供するMCPサーバー。AIアシスタントが統一されたインターフェースを通じて現在のオッズ、価格、市場情報をクエリできるようにします。
- [JamesANZ/bitcoin-mcp](https://github.com/JamesANZ/bitcoin-mcp) 📇 🏠 - AIモデルがビットコインブロックチェーンをクエリできるようにするMCPサーバー。

### 📂 <a name="file-systems"></a>ファイルシステム

構成可能な権限を備えたローカルファイルシステムへの直接アクセスを提供します。指定されたディレクトリ内のファイルを読み取り、書き込み、管理することができます。

- [@modelcontextprotocol/server-filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) 📇 🏠 - ローカルファイルシステムへの直接アクセス。
- [@modelcontextprotocol/server-google-drive](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive) 📇 ☁️ - ファイルのリスト、読み取り、検索のためのGoogle Drive統合
- [8b-is/smart-tree](https://github.com/8b-is/smart-tree) 🦀 🏠 🍎 🪟 🐧 - AI ネイティブのディレクトリ可視化。セマンティック分析、AI 消費用の超圧縮フォーマット、10倍のトークン削減をサポート。インテリジェントなファイル分類を備えた量子セマンティックモードをサポート。
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

- [apecloud/ApeRAG](https://github.com/apecloud/ApeRAG) 🐍 ☁️ 🏠 - Graph RAG、ベクトル検索、フルテキスト検索を組み合わせた本格的なRAGプラットフォーム。知識グラフ構築とコンテキストエンジニアリングに最適
- [jinzcdev/markmap-mcp-server](https://github.com/jinzcdev/markmap-mcp-server) 📇 🏠 - [markmap](https://github.com/markmap/markmap) を基にしたMCPサーバーで、**Markdown**をインタラクティブな**マインドマップ**に変換します。複数のフォーマット（PNG/JPG/SVG）でのエクスポート、ブラウザでのリアルタイムプレビュー、ワンクリックでのMarkdownコピー、ダイナミックな視覚化機能をサポートしています。
- [@modelcontextprotocol/server-memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) 📇 🏠 - コンテキストを維持するための知識グラフベースの長期記憶システム
- [/CheMiguel23/MemoryMesh](https://github.com/CheMiguel23/MemoryMesh) 📇 🏠 - AIロールプレイとストーリー生成に焦点を当てた強化されたグラフベースのメモリ
- [@mem0ai/mem0-mcp](https://github.com/mem0ai/mem0-mcp) 🐍 🏠 - CursorやWindsurfなどのIDEでコーディングの好みやパターンを管理するためのMem0用モデルコンテキストプロトコルサーバー。コード実装、ベストプラクティス、技術文書の保存、取得、意味的な処理のためのツールを提供します
- [@ragieai/mcp-server](https://github.com/ragieai/ragie-mcp-server) 📇 ☁️ - あなたの [Ragie](https://www.ragie.ai) (RAG) ナレッジベースから、Google Drive、Notion、JIRAなどの連携サービスに接続されたコンテキストを取得します。
- [JamesANZ/memory-mcp](https://github.com/JamesANZ/memory-mcp) 📇 🏠 - MongoDBを使用して複数のLLMからのメモリを保存・取得するMCPサーバー。タイムスタンプとLLM識別を含む会話メモリの保存、取得、追加、クリアのためのツールを提供します。
- [JamesANZ/cross-llm-mcp](https://github.com/JamesANZ/cross-llm-mcp) 📇 🏠 - 異なるAIモデルが協力し、会話間でコンテキストを共有できるようにするクロスLLM通信とメモリ共有を可能にするMCPサーバー。

### 🗺️ <a name="location-services"></a>位置情報サービス

地理および位置ベースのサービス統合。地図データ、方向、および場所情報へのアクセスを提供します。

- [@modelcontextprotocol/server-google-maps](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/google-maps) 📇 ☁️ - 位置情報サービス、ルート計画、および場所の詳細のためのGoogle Maps統合

### 🎯 <a name="marketing"></a>マーケティング

マーケティングコンテンツの作成と編集、ウェブメタデータの操作、製品ポジショニング、編集ガイドのためのツール。

- [gomarble-ai/facebook-ads-mcp-server](https://github.com/gomarble-ai/facebook-ads-mcp-server) 🐍 ☁️ - Facebook Adsとのインターフェースとして機能するMCPサーバーで、Facebook Adsデータと管理機能への プログラマティックアクセスを可能にします。
- [open-strategy-partners/osp_marketing_tools](https://github.com/open-strategy-partners/osp_marketing_tools) 🐍 🏠 - Open Strategy Partnersからの マーケティングツールスイートで、文章スタイル、編集コード、製品マーケティング価値マップ作成を含む。
- [nictuku/meta-ads-mcp](https://github.com/nictuku/meta-ads-mcp) 🐍 ☁️ 🏠 - AIエージェントがMeta広告のパフォーマンスを監視・最適化し、キャンペーンメトリクスを分析し、オーディエンスターゲティングを調整し、クリエイティブアセットを管理し、シームレスなGraph API統合を通じて広告費とキャンペーン設定についてデータ主導の推奨事項を作成できるようにします。
- [marketplaceadpros/amazon-ads-mcp-server](https://github.com/MarketplaceAdPros/amazon-ads-mcp-server) 📇 ☁️ - Amazon Advertisingと対話し、キャンペーンメトリクスと設定を分析するツールを有効にします。

### 📊 <a name="monitoring"></a>監視

アプリケーション監視データへのアクセスと分析。エラーレポートとパフォーマンスメトリクスをレビューすることができます。

- [netdata/netdata](https://github.com/netdata/netdata/blob/master/src/web/mcp/README.md) 🎖️ 🏠 ☁️ 📟 🍎 🪟 🐧 - メトリクス、ログ、システム、コンテナ、プロセス、ネットワーク接続を含む すべての可観測性データを使用した発見、調査、レポート、根本原因分析
- [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) 🎖️ 🐍 🏠 ☁️ - Grafanaインスタンスでダッシュボードを検索し、インシデントを調査し、データソースをクエリ
- [tumf/grafana-loki-mcp](https://github.com/tumf/grafana-loki-mcp) 🐍 🏠 - Grafana APIを通じてLokiログをクエリできるMCPサーバー。
- [hyperb1iss/lucidity-mcp](https://github.com/hyperb1iss/lucidity-mcp) 🐍 🏠 - 複雑さからセキュリティ脆弱性まで、10の重要な次元でインテリジェントでプロンプトベースの分析によってAI生成コードの品質を向上
- [inventer-dev/mcp-internet-speed-test](https://github.com/inventer-dev/mcp-internet-speed-test) 🐍 ☁️ - ダウンロード/アップロード速度、レイテンシ、ジッター分析、地理的マッピング付きCDNサーバー検出を含むネットワークパフォーマンスメトリクスによるインターネット速度テスト
- [last9/last9-mcp-server](https://github.com/last9/last9-mcp-server) - リアルタイム本番コンテキスト（ログ、メトリクス、トレース）をローカル環境にシームレスに持ち込み、コードをより高速に自動修正
- [metoro-io/metoro-mcp-server](https://github.com/metoro-io/metoro-mcp-server) 🎖️ 🏎️ ☁️ - Metoroによって監視されるKubernetes環境をクエリおよび対話
- [MindscapeHQ/server-raygun](https://github.com/MindscapeHQ/mcp-server-raygun) 📇 ☁️ - クラッシュレポートとリアルユーザーモニタリングのためのRaygun API V3統合
- [modelcontextprotocol/server-sentry](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry) 🐍 ☁️ - エラートラッキングとパフォーマンス監視のためのSentry.io統合
- [pydantic/logfire-mcp](https://github.com/pydantic/logfire-mcp) 🎖️ 🐍 ☁️ - Logfireを通じてOpenTelemetryトレースとメトリクスへのアクセスを提供
- [seekrays/mcp-monitor](https://github.com/seekrays/mcp-monitor) 🏎️ 🏠 - Model Context Protocol（MCP）を介してシステムメトリクスを公開するシステムモニタリングツール。このツールにより、LLMはMCP互換インターフェースを通じてリアルタイムシステム情報を取得できます。（CPU、メモリ、ディスク、ネットワーク、ホスト、プロセスをサポート）
- [VictoriaMetrics-Community/mcp-victoriametrics](https://github.com/VictoriaMetrics-Community/mcp-victoriametrics) 🎖️ 🏎️ 🏠 - VictoriaMetricsインスタンスの監視、可観測性、デバッグタスクに関連した[VictoriaMetricsインスタンスAPI](https://docs.victoriametrics.com/victoriametrics/url-examples/)および[ドキュメント](https://docs.victoriametrics.com/)との包括的な統合を提供

### 🎥 <a name="multimedia-process"></a>マルチメディア処理

音声・動画編集、再生、フォーマット変換、および動画フィルタ、拡張などを含むマルチメディア処理機能を提供。

- [video-creator/ffmpeg-mcp](https://github.com/video-creator/ffmpeg-mcp.git) 🎥 🔊 - ffmpegコマンドラインを使用してMCPサーバーを実現。対話を通じてローカル動画の検索、カット、結合、再生などの機能を非常に便利に実現できます
- [stass/exif-mcp](https://github.com/stass/exif-mcp) 📇 🏠 🐧 🍎 🪟 - EXIF、XMP、JFIF、GPSなどの画像メタデータを調べることができるMCPサーバー。これにより、フォトライブラリや画像コレクションのLLM駆動検索と分析の基盤を提供します。
- [sunriseapps/imagesorcery-mcp](https://github.com/sunriseapps/imagesorcery-mcp) 🐍 🏠 🐧 🍎 🪟 - AIアシスタント向けのコンピュータービジョンベースの🪄画像認識・編集ツールの魔法

### 🔎 <a name="search"></a>検索・データ抽出

- [scrapeless-ai/scrapeless-mcp-server](https://github.com/scrapeless-ai/scrapeless-mcp-server) 🐍 ☁️ - Scrapeless Model Context Protocolサービスは、MCPエコシステム内で離れることなくWeb検索を可能にするGoogle SERP APIへのMCPサーバコネクタとして機能します。
- [@modelcontextprotocol/server-brave-search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) 📇 ☁️ - Braveの検索APIを使用したWeb検索機能
- [DappierAI/dappier-mcp](https://github.com/DappierAI/dappier-mcp) 🐍 ☁️ - DappierのMCPサーバーで、信頼できるメディアブランドからのニュース、金融市場、スポーツ、エンタメ、天気などのプレミアムデータへのリアルタイムアクセスと、高速なWeb検索をAIエージェントに提供します。
- [Dumpling-AI/mcp-server-dumplingai](https://github.com/Dumpling-AI/mcp-server-dumplingai) 🎖️ 📇 ☁️ - [Dumpling AI](https://www.dumplingai.com/) によるデータ取得、Webスクレイピング、ドキュメント変換API
- [@angheljf/nyt](https://github.com/angheljf/nyt) 📇 ☁️ - NYTimes APIを使用して記事を検索
- [@modelcontextprotocol/server-fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) 🐍 🏠 ☁️ - AI消費のための効率的なWebコンテンツの取得と処理
- [ac3xx/mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi) 📇 ☁️ - Kagi検索API統合
- [theishangoswami/exa-mcp-server](https://github.com/theishangoswami/exa-mcp-server) 📇 ☁️ - Exa AI検索API
- [exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) 🎖️ 📇 ☁️ – モデルコンテキストプロトコル（MCP）サーバーは、ClaudeなどのAIアシスタントがExa AI検索APIを使用してWeb検索を行うことを可能にします。この設定により、AIモデルは安全かつ制御された方法でリアルタイムのWeb情報を取得できます。
- [fatwang2/search1api-mcp](https://github.com/fatwang2/search1api-mcp) 📇 ☁️ - search1apiを介した検索（有料APIキーが必要）
- [Tomatio13/mcp-server-tavily](https://github.com/Tomatio13/mcp-server-tavily) ☁️ 🐍 – Tavily AI検索API
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
- [Pearch-ai/mcp_pearch](https://github.com/Pearch-ai/mcp_pearch) 🎖️ 🐍 ☁️ - 人材発掘にかかる時間を短縮する、最高の人物検索エンジン

### 🔒 <a name="security"></a>セキュリティ

セキュリティツール、脆弱性評価、フォレンジクス分析。AIアシスタントがサイバーセキュリティタスクを実行できるようにし、侵入テスト、コード分析、セキュリティ監査を支援します。

- [AIM-Intelligence/AIM-Guard-MCP](https://github.com/AIM-Intelligence/AIM-MCP) 📇 🏠 🍎 🪟 🐧 - セキュリティ重視のMCPサーバーで、AIエージェントに安全ガイドラインとコンテンツ分析を提供
- [firstorderai/authenticator_mcp](https://github.com/firstorderai/authenticator_mcp) 📇 🏠 🍎 🪟 🐧 – AIエージェントが認証アプリと連携できるようにする安全なMCP（Model Context Protocol）サーバー。
- [fosdickio/binary_ninja_mcp](https://github.com/Vector35/binaryninja-mcp) 🐍 🏠 🍎 🪟 🐧 - Binary NinjaのためのMCPサーバーとブリッジ。バイナリ分析とリバースエンジニアリングのためのツールを提供します。
- [Security Audit MCP Server](https://github.com/qianniuspace/mcp-security-audit) 📇 ☁️ 強力なモデルコンテキストプロトコル（MCP）サーバーで、npmパッケージ依存関係のセキュリティ脆弱性を監査します。リモートnpmレジストリ統合を備えたリアルタイムセキュリティチェックを使用して構築されています。
- [GhidraMCP](https://github.com/13bm/GhidraMCP) 🐍 ☕ 🏠 - GhidraをAIアシスタントと統合するためのMCPサーバー。このプラグインはバイナリ分析を可能にし、モデルコンテキストプロトコルを通じて関数検査、逆コンパイル、メモリ探索、インポート/エクスポート分析などのツールを提供します。
- [intruder-io/intruder-mcp](https://github.com/intruder-io/intruder-mcp) 🐍 ☁️ - [Intruder](https://www.intruder.io/) にアクセスするためのMCPサーバー。インフラストラクチャのセキュリティ脆弱性の特定、理解、修正を支援します。
- [Gaffx/volatility-mcp](https://github.com/Gaffx/volatility-mcp) - Volatility 3.x用MCPサーバー。AIアシスタントでメモリフォレンジクス分析を実行可能。pslistやnetscanなどのプラグインをクリーンなREST APIとLLMを通じてアクセス可能にし、メモリフォレンジクスを障壁なく体験
- [jtang613/GhidrAssistMCP](https://github.com/jtang613/GhidrAssistMCP) ☕ 🏠 - Ghidra 用のネイティブな Model Context Protocol サーバー。GUI 設定およびログ機能、31 種類の強力なツール、外部依存なし。
- [co-browser/attestable-mcp-server](https://github.com/co-browser/attestable-mcp-server) 🐍 🏠 ☁️ 🐧 - Gramine経由で信頼実行環境（TEE）内で実行されるMCPサーバー。[RA-TLS](https://gramine.readthedocs.io/en/stable/attestation.html)を使用したリモート証明を紹介。MCPクライアントが接続前にサーバーを検証可能
- [zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp) ☕ 🏠 - Model Context Protocol（MCP）と直接統合し、ClaudeなどのLLMでライブリバースエンジニアリング支援を提供するJADXデコンパイラー用プラグインとMCPサーバー
- [zinja-coder/apktool-mcp-server](https://github.com/zinja-coder/apktool-mcp-server) 🐍 🏠 - APK ToolのMCPサーバー。Android APKのリバースエンジニアリング自動化を提供

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

- [2niuhe/plantuml_web](https://github.com/2niuhe/plantuml_web) 🐍 🏠 ☁️ 🍎 🪟 🐧 - MCPサーバー統合を備えたWebベースのPlantUMLフロントエンド。PlantUML画像生成と構文検証を可能にします。
- [2niuhe/qrcode_mcp](https://github.com/2niuhe/qrcode_mcp) 🐍 🏠 🍎 🪟 🐧 - 任意のテキスト（日本語文字を含む）をQRコードに変換し、カスタマイズ可能な色とbase64エンコード出力をサポートするQRコード生成MCPサーバー。
- [AbdelStark/bitcoin-mcp](https://github.com/AbdelStark/bitcoin-mcp) - ₿ AIモデルがBitcoinと相互作用できるModel Context Protocol（MCP）サーバー。キー生成、アドレス検証、トランザクションデコード、ブロックチェーンクエリなどが可能
- [akseyh/bear-mcp-server](https://github.com/akseyh/bear-mcp-server) - AIがBear Notes（macOSのみ）から読み取り可能にする
- [allenporter/mcp-server-home-assistant](https://github.com/allenporter/mcp-server-home-assistant) 🐍 🏠 - Model Context Protocolサーバーを通じてすべてのHome Assistant音声インテントを公開し、ホーム制御を可能にする
- [Amazon Bedrock Nova Canvas](https://github.com/zxkane/mcp-server-amazon-bedrock) 📇 ☁️ - Amazon Nova Canvasモデルを使用した画像生成
- [amidabuddha/unichat-mcp-server](https://github.com/amidabuddha/unichat-mcp-server) 🐍/📇 ☁️ - MCPプロトコル経由でOpenAI、MistralAI、Anthropic、xAI、Google AI、DeepSeekにリクエストを送信。ツールまたは事前定義プロンプトを使用。ベンダーAPIキーが必要
- [anaisbetts/mcp-installer](https://github.com/anaisbetts/mcp-installer) 🐍 🏠 - 他のMCPサーバーをインストールするMCPサーバー
- [anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube) 📇 ☁️ - YouTube字幕を取得
- [andybrandt/mcp-simple-openai-assistant](https://github.com/andybrandt/mcp-simple-openai-assistant) 🐍 ☁️ - OpenAIアシスタントと通信するMCP（ClaudeがGPTモデルをアシスタントとして使用可能）
- [andybrandt/mcp-simple-timeserver](https://github.com/andybrandt/mcp-simple-timeserver) 🐍 🏠☁️ - クライアントマシンのローカル時間またはNTPサーバーからの現在のUTC時間をチェックできるMCPサーバー
- [apify/actors-mcp-server](https://github.com/apify/actors-mcp-server) 📇 ☁️ - ウェブサイト、Eコマース、ソーシャルメディア、検索エンジン、マップなどからデータを抽出する3,000以上の事前構築クラウドツール（Actors）を使用
- [apinetwork/piapi-mcp-server](https://github.com/apinetwork/piapi-mcp-server) 📇 ☁️ - PiAPI MCPサーバーで、Midjourney/Flux/Kling/Hunyuan/Udio/TrellisでClaudeや他のMCP互換アプリから直接メディアコンテンツを生成可能
- [awkoy/replicate-flux-mcp](https://github.com/awkoy/replicate-flux-mcp) 📇 ☁️ - ReplicateのAPIを通じて画像生成機能を提供
- [awwaiid/mcp-server-taskwarrior](https://github.com/awwaiid/mcp-server-taskwarrior) 🏠 📇 - 基本的なローカルtaskwarrior使用（タスクの追加、更新、削除）のためのMCPサーバー
- [Badhansen/notion-mcp](https://github.com/Badhansen/notion-mcp) 🐍 ☁️ - NotionのAPIと統合してパーソナルToDoリストを効率的に管理するModel Context Protocol（MCP）サーバー
- [bart6114/my-bear-mcp-server](https://github.com/bart6114/my-bear-mcp-server/) 📇 🏠 🍎 - BearのsqliteDBと直接統合してBear Note取得アプリのノートとタグを読み取り可能
- [billster45/mcp-chatgpt-responses](https://github.com/billster45/mcp-chatgpt-responses) 🐍 ☁️ - ClaudeがChatGPTと通信してWeb検索機能を使用するためのMCPサーバー
- [blurrah/mcp-graphql](https://github.com/blurrah/mcp-graphql) 📇 ☁️ - AIがGraphQLサーバーをクエリ可能にする
- [calclavia/mcp-obsidian](https://github.com/calclavia/mcp-obsidian) 📇 🏠 - Claude Desktop（または任意のMCPクライアント）がMarkdownノート（Obsidianボルトなど）を含むディレクトリを読み取り・検索できるコネクター
- [chrishayuk/mcp-cli](https://github.com/chrishayuk/mcp-cli) 🐍 🏠 - MCPサーバーテスト用のもう一つのCLIツール
- [danhilse/notion_mcp](https://github.com/danhilse/notion_mcp) 🐍 ☁️ - NotionのAPIと統合してパーソナルToDoリストを管理
- [ekkyarmandi/ticktick-mcp](https://github.com/ekkyarmandi/ticktick-mcp) 🐍 ☁️ - [TickTick](https://ticktick.com/)のAPIと統合してパーソナルToDoプロジェクトとタスクを管理するTickTick MCPサーバー
- [esignaturescom/mcp-server-esignatures](https://github.com/esignaturescom/mcp-server-esignatures) 🐍 ☁️ - eSignatures API経由で拘束力のある契約の起草、レビュー、送信を行う契約・テンプレート管理
- [evalstate/mcp-miro](https://github.com/evalstate/mcp-miro) 📇 ☁️ - MIROホワイトボードにアクセス、アイテムの一括作成・読み取り。REST API用OAUTHキーが必要
- [feuerdev/keep-mcp](https://github.com/feuerdev/keep-mcp) 🐍 ☁️ - Google Keepノートの読み取り、作成、更新、削除
- [future-audiences/wikimedia-enterprise-model-context-protocol](https://gitlab.wikimedia.org/repos/future-audiences/wikimedia-enterprise-model-context-protocol) 🐍 ☁️ - Wikipedia記事検索API
- [fotoetienne/gqai](https://github.com/fotoetienne/gqai) 🏎 🏠 - 通常のGraphQLクエリ/ミューテーションを使ってツールを定義すると、gqaiが自動的にMCPサーバーを生成
- [githejie/mcp-server-calculator](https://github.com/githejie/mcp-server-calculator) 🐍 🏠 - LLMが正確な数値計算のために電卓を使用できるサーバー
- [gotoolkits/DifyWorkflow](https://github.com/gotoolkits/mcp-difyworkflow-server) 🏎️ ☁️ - Difyワークフローのクエリと実行ツール
- [hiromitsusasaki/raindrop-io-mcp-server](https://github.com/hiromitsusasaki/raindrop-io-mcp-server) 📇 ☁️ - LLMがModel Context Protocol（MCP）を使用してRaindrop.ioブックマークと相互作用できる統合
- [hmk/attio-mcp-server](https://github.com/hmk/attio-mcp-server) 📇 ☁️ - AIクライアントがAttio CRMでレコードとノートを管理可能
- [isaacwasserman/mcp-vegalite-server](https://github.com/isaacwasserman/mcp-vegalite-server) 🐍 🏠 - 取得したデータからVegaLite形式とレンダラーを使用して視覚化を生成
- [ivnvxd/mcp-server-odoo](https://github.com/ivnvxd/mcp-server-odoo) 🐍 ☁️/🏠 - AIアシスタントをOdoo ERPシステムに接続し、ビジネスデータアクセス、レコード管理、ワークフロー自動化を提供
- [ivo-toby/contentful-mcp](https://github.com/ivo-toby/contentful-mcp) 📇 🏠 - Contentful Spaceでコンテンツ、コンテンツモデル、アセットの更新、作成、削除
- [j3k0/speech.sh](https://github.com/j3k0/speech.sh/blob/main/MCP_README.md) 🏠 - エージェントに音声出力させ、作業完了時に簡単な要約で通知
- [jagan-shanmugam/climatiq-mcp-server](https://github.com/jagan-shanmugam/climatiq-mcp-server) 🐍 🏠 - Climatiq APIにアクセスして炭素排出量を計算するModel Context Protocol（MCP）サーバー。AIアシスタントがリアルタイム炭素計算と気候影響洞察を提供可能
- [johannesbrandenburger/typst-mcp](https://github.com/johannesbrandenburger/typst-mcp) 🐍 🏠 - マークアップベースの組版システムTypst用MCPサーバー。LaTeXとTypst間の変換、Typst構文検証、Typstコードからの画像生成ツールを提供
- [joshuarileydev/mac-apps-launcher-mcp-server](https://github.com/JoshuaRileyDev/mac-apps-launcher) 📇 🏠 - macOSでアプリケーションをリスト・起動するMCPサーバー
- [Harry-027/JotDown](https://github.com/Harry-027/JotDown) 🦀 🏠 - Notionアプリでページを作成/更新し、構造化コンテンツからmdBookを自動生成するMCPサーバー
- [kelvin6365/plane-mcp-server](https://github.com/kelvin6365/plane-mcp-server) 🏎️ 🏠 - [Plane](https://plane.so)のAPIを通じてプロジェクトと課題を管理するMCPサーバー
- [yuna0x0/hackmd-mcp](https://github.com/yuna0x0/hackmd-mcp) 📇 ☁️ - AIモデルが [HackMD](https://hackmd.io) と連携できるようにします。
- [HenryHaoson/Yuque-MCP-Server](https://github.com/HenryHaoson/Yuque-MCP-Server) - 📇 ☁️ 語雀APIと統合するためのModel-Context-Protocol (MCP)サーバー。AIモデルがドキュメントを管理し、ナレッジベースと対話し、コンテンツを検索し、語雀プラットフォームの分析データにアクセスできるようにします。
- [tumf/web3-mcp](https://github.com/tumf/web3-mcp) 🐍 ☁️ - Ankr Advanced APIをラップするMCPサーバー実装。イーサリアム、BSC、ポリゴン、アバランチなど複数のブロックチェーンにわたるNFT、トークン、ブロックチェーンデータにアクセスできます。
- [ttommyth/interactive-mcp](https://github.com/ttommyth/interactive-mcp) 📇 🏠 🍎 🪟 🐧 - ローカルユーザープロンプトとチャット機能を MCP ループに直接追加することで、インタラクティブな LLM ワークフローを有効にします。
- [growilabs/growi-mcp-server](https://github.com/growilabs/growi-mcp-server) 🎖️ 📇 ☁️ - GROWI APIと統合するための公式MCPサーバー。
- [JamesANZ/medical-mcp](https://github.com/JamesANZ/medical-mcp) 📇 🏠 - 医療情報、薬物データベース、医療リソースへのアクセスを提供するMCPサーバー。AIアシスタントが医療データ、薬物相互作用、臨床ガイドラインをクエリできるようにします。

### 🌐 <a name="social-media"></a>ソーシャルメディア

ソーシャルメディアプラットフォームとの統合により、投稿、アナリティクス、インタラクション管理を可能にします。ソーシャルプレゼンスのAI駆動自動化を実現します。

- [macrocosm-os/macrocosmos-mcp](https://github.com/macrocosm-os/macrocosmos-mcp) 🎖️ 🐍 ☁️ - 検索フレーズ、ユーザー、日付フィルタリングでリアルタイムX/Reddit/YouTubeデータにLLMアプリケーション内で直接アクセス
- [kunallunia/twitter-mcp](https://github.com/LuniaKunal/mcp-twitter) 🐍 🏠 - タイムラインアクセス、ユーザーツイート取得、ハッシュタグモニタリング、会話分析、ダイレクトメッセージング、投稿の感情分析、完全な投稿ライフサイクル制御を提供するオールインワンTwitter管理ソリューション
- [HagaiHen/facebook-mcp-server](https://github.com/HagaiHen/facebook-mcp-server) 🐍 ☁️ - Facebookページと統合し、Graph APIを通じて投稿、コメント、エンゲージメントメトリクスの直接管理を可能にして、ソーシャルメディア管理を効率化
- [gwbischof/bluesky-social-mcp](https://github.com/gwbischof/bluesky-social-mcp) 🐍 🏠 - atprotoクライアント経由でBlueskyと対話するMCPサーバー

### 🏃 <a name="sports"></a>スポーツ

スポーツ関連データ、結果、統計にアクセスするためのツール。

- [mikechao/balldontlie-mcp](https://github.com/mikechao/balldontlie-mcp) 📇 - balldontlie APIと統合してNBA、NFL、MLBの選手、チーム、試合情報を提供するMCPサーバー
- [r-huijts/firstcycling-mcp](https://github.com/r-huijts/firstcycling-mcp) 📇 ☁️ - 自然言語でサイクリングレースデータ、結果、統計にアクセス。firstcycling.comからスタートリスト、レース結果、ライダー情報を取得する機能を含む
- [r-huijts/strava-mcp](https://github.com/r-huijts/strava-mcp) 📇 ☁️ - Strava APIに接続し、LLMを通じてStravaデータにアクセスするツールを提供するModel Context Protocol（MCP）サーバー
- [willvelida/mcp-afl-server](https://github.com/willvelida/mcp-afl-server) ☁️ - Squiggle APIと統合してオーストラリアンフットボールリーグのチーム、ラダー順位、結果、予想、パワーランキング情報を提供するMCPサーバー
- [guillochon/mlb-api-mcp](https://github.com/guillochon/mlb-api-mcp) 🐍 🏠 - 自由に利用可能なMLB APIのプロキシとして機能し、選手情報、統計、試合情報を提供するMCPサーバー

### 🎧 <a name="text-to-speech"></a>テキスト読み上げ

テキストから音声への変換とその逆のためのツール。

- [mberg/kokoro-tts-mcp](https://github.com/mberg/kokoro-tts-mcp) 🐍 🏠 - オープンウェイトKokoro TTSモデルを使用してテキストから音声に変換するMCPサーバー。ローカルドライブでMP3に変換するか、S3バケットに自動アップロード可能
- [mbailey/voice-mcp](https://github.com/mbailey/voice-mcp) 🐍 🏠 - ローカルマイク、OpenAI互換API、LiveKit統合を通じて音声からテキスト、テキストから音声、リアルタイム音声会話をサポートする完全な音声インタラクションサーバー

## フレームワーク

- [Genkit MCP](https://github.com/firebase/genkit/tree/main/js/plugins/mcp) 📇 – [Genkit](https://github.com/firebase/genkit/tree/main) とモデルコンテキストプロトコル（MCP）との統合を提供します。
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

### 📂 <a name="browser-automation"></a>ブラウザ自動化

Webコンテンツのアクセスと自動化機能。AIに優しい形式でWebコンテンツを検索、スクレイピング、処理することができます。

- [xspadex/bilibili-mcp](https://github.com/xspadex/bilibili-mcp.git) 📇 🏠 - FastMCPベースのツールで、Bilibiliのトレンド動画を取得し、標準MCPインターフェースを通じて公開
- [34892002/bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js) 📇 🏠 - Bilibiliコンテンツの検索をサポートするMCPサーバー。LangChain連携のサンプルとテストスクリプトを提供
- [automatalabs/mcp-server-playwright](https://github.com/Automata-Labs-team/MCP-Server-Playwright) 🐍 - Playwrightを使用したブラウザ自動化のためのMCPサーバー
- [blackwhite084/playwright-plus-python-mcp](https://github.com/blackwhite084/playwright-plus-python-mcp) 🐍 - Playwrightを使用したブラウザ自動化のためのMCP Pythonサーバー、LLMにより適している
- [browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) 🎖️ 📇 - クラウドでのブラウザ相互作用の自動化（ウェブナビゲーション、データ抽出、フォーム入力など）
- [browsermcp/mcp](https://github.com/browsermcp/mcp) 📇 🏠 - ローカルChromeブラウザを自動化
- [co-browser/browser-use-mcp-server](https://github.com/co-browser/browser-use-mcp-server) 🐍 - SSEトランスポートでMCPサーバーとしてパッケージ化されたbrowser-use。dockerでchromiumを実行するdockerファイル + vncサーバーを含む
- [executeautomation/playwright-mcp-server](https://github.com/executeautomation/mcp-playwright) 📇 - Playwrightを使用したブラウザ自動化とWebスクレイピングのためのMCPサーバー
- [eyalzh/browser-control-mcp](https://github.com/eyalzh/browser-control-mcp) 📇 🏠 - LLMクライアントがユーザーのブラウザ（Firefox）を制御できるブラウザ拡張機能と組み合わせたMCPサーバー
- [fradser/mcp-server-apple-reminders](https://github.com/FradSer/mcp-server-apple-reminders) 📇 🏠 🍎 - macOS用Apple Remindersと統合されたMCPサーバー
- [getrupt/ashra-mcp](https://github.com/getrupt/ashra-mcp) 🐍 🏠 - 任意のWebサイトから構造化データを抽出。プロンプトを入力するだけでJSONを取得
- [kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) 📇 ☁️ - AI分析のためのYouTube字幕とトランスクリプトの取得
- [kimtth/mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing) 🐍 🏠 - Azure OpenAIとPlaywrightを使用した「最小限の」サーバー/クライアントMCP実装
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) - MicrosoftのオフィシャルPlaywright MCPサーバー。構造化アクセシビリティスナップショットを通じてLLMがWebページと相互作用可能
- [modelcontextprotocol/server-puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) 📇 🏠 - Webスクレイピングとインタラクションのためのブラウザ自動化
- [ndthanhdev/mcp-browser-kit](https://github.com/ndthanhdev/mcp-browser-kit) 📇 🏠 - manifest v2互換ブラウザとの相互作用のためのMCPサーバー
- [pskill9/web-search](https://github.com/pskill9/web-search) 📇 🏠 - APIキー不要でGoogleの検索結果を使った無料Web検索を可能にするMCPサーバー
- [recursechat/mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts) 📇 🏠 🍎 - Apple ShortcutsとのMCPサーバー統合

## フレームワーク

> [!NOTE]
> その他のフレームワーク、ユーティリティ、開発者ツールについては https://github.com/punkpeye/awesome-mcp-devtools をご覧ください

- [FastMCP](https://github.com/jlowin/fastmcp) 🐍 - PythonでMCPサーバーを構築するための高レベルフレームワーク
- [FastMCP](https://github.com/punkpeye/fastmcp) 📇 - TypeScriptでMCPサーバーを構築するための高レベルフレームワーク

## Tips and Tricks

### LLMにModel Context Protocolの使用方法を教える公式プロンプト

ClaudeにModel Context Protocolについて質問したいですか？

プロジェクトを作成し、以下のファイルを追加してください：

https://modelcontextprotocol.io/llms-full.txt

これで、ClaudeはMCPサーバーの作成方法や動作についての質問に答えられるようになります

- https://www.reddit.com/r/ClaudeAI/comments/1h3g01r/want_to_ask_claude_about_model_context_protocol/
