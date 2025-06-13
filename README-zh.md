# 精选的 MCP 服务器 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![繁體中文](https://img.shields.io/badge/繁體中文-點擊查看-orange)](README-zh_TW.md)
[![简体中文](https://img.shields.io/badge/简体中文-点击查看-orange)](README-zh.md)
[![日本語](https://img.shields.io/badge/日本語-クリック-青)](README-ja.md)
[![한국어](https://img.shields.io/badge/한국어-클릭-yellow)](README-ko.md)
[![Português Brasileiro](https://img.shields.io/badge/Português_Brasileiro-Clique-green)](README-pt_BR.md)
[![Discord](https://img.shields.io/discord/1312302100125843476?logo=discord&label=discord)](https://glama.ai/mcp/discord)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/mcp?style=flat&logo=reddit&label=subreddit)](https://www.reddit.com/r/mcp/)

精选的优秀模型上下文协议 (MCP) 服务器列表。

* [什么是MCP？](#什么是MCP？)
* [客户端](#客户端)
* [教程](#教程)
* [社区](#社区)
* [说明](#说明)
* [Server 实现](#服务器实现)
* [框架](#框架)
* [实用工具](#实用工具)
* [提示和技巧](#提示和技巧)

## 什么是MCP？

[MCP](https://modelcontextprotocol.io/) 是一种开放协议，通过标准化的服务器实现，使 AI 模型能够安全地与本地和远程资源进行交互。此列表重点关注可用于生产和实验性的 MCP 服务器，这些服务器通过文件访问、数据库连接、API 集成和其他上下文服务来扩展 AI 功能。

## 客户端

查看 [awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients/) 和 [glama.ai/mcp/clients](https://glama.ai/mcp/clients)。

> [!TIP]
> [Glama Chat](https://glama.ai/chat)是一款支持MCP的多模态AI客户端，并集成[AI网关](https://glama.ai/gateway)功能。

## 教程

* [Model Context Protocol (MCP) 快速开始](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
* [设置 Claude 桌面应用程序以使用 SQLite 数据库](https://youtu.be/wxCCzo9dGj0)

## 社区

* [r/mcp Reddit](https://www.reddit.com/r/mcp)
* [Discord 服务](https://glama.ai/mcp/discord)

## 说明

* 🎖️ – 官方实现
* 编程语言
  * 🐍 – Python 代码库
  * 📇 – TypeScript 代码库
  * 🏎️ – Go 代码库
  * 🦀 – Rust 代码库
  * #️⃣ - C# 代码库
  * ☕ - Java 代码库
* 范围
  * ☁️ - 云服务
  * 🏠 - 本地服务
* 操作系统
  * 🍎 – For macOS
  * 🪟 – For Windows
  * 🐧 - For Linux


> [!NOTE]
> 关于本地 🏠 和云 ☁️ 的区别：
> * 当 MCP 服务器与本地安装的软件通信时使用本地服务，例如控制 Chrome 浏览器。
> * 当 MCP 服务器与远程 API 通信时使用网络服务，例如天气 API。
## 服务器实现

> [!NOTE]
> 我们现在有一个与存储库同步的[基于 Web 的目录](https://glama.ai/mcp/servers)。

* 🔗 - [Aggregators](#aggregators)
* 📂 - [浏览器自动化](#browser-automation)
* 🎨 - [艺术与文化](#art-and-culture)
* ☁️ - [云平台](#cloud-platforms)
* 🤖 - [编程智能体](#coding-agents)
* 🖥️ - [命令行](#command-line)
* 💬 - [社交](#communication)
* 👤 - [客户数据平台](#customer-data-platforms)
* 🗄️ - [数据库](#databases)
* 📊 - [数据平台](#data-platforms)
* 🛠️ - [开发者工具](#developer-tools)
* 🧮 - [数据科学工具](#data-science-tools)
* 📂 - [文件系统](#file-systems)
* 💰 - [金融与金融科技](#finance--fintech)
* 🎮 - [游戏](#gaming)
* 🧠 - [知识与记忆](#knowledge--memory)
* 🗺️ - [位置服务](#location-services)
* 🎯 - [营销](#marketing)
* 📊 - [监测](#monitoring)
* 🔎 - [搜索](#search)
* 🔒 - [安全](#security)
* 🏃 - [体育](#sports)
* 🌎 - [翻译服务](#translation-services)
* 🚆 - [旅行与交通](#travel-and-transportation)
* 🔄 - [版本控制](#version-control)
* 🛠️ - [其他工具和集成](#other-tools-and-integrations)

### 🔗 <a name="aggregators"></a>聚合器

通过单个MCP服务器访问多个应用程序和工具的服务器。

- [OpenMCP](https://github.com/wegotdocs/open-mcp) 📇 🏠 🍎 🪟 🐧 - 10秒内将Web API转换为MCP服务器并将其添加到开源注册表中: https://open-mcp.org
- [tigranbs/mcgravity](https://github.com/tigranbs/mcgravity) 📇 🏠 - 一个代理工具，用于将多个MCP服务器组合成一个统一的端点。通过跨多个MCP服务器负载均衡请求来扩展您的AI工具，类似于Nginx对Web服务器的工作方式。
- [MetaMCP](https://github.com/metatool-ai/metatool-app) 📇 ☁️ 🏠 🍎 🪟 🐧 - MetaMCP是一个统一的中间件MCP服务器，通过GUI管理您的MCP连接。
- [MCP Access Point](https://github.com/sxhxliang/mcp-access-point)  📇 ☁️ 🏠 🍎 🪟 🐧  - 一键将Web API转成为MCP服务器，而无需对服务器端代码进行任何修改。
- [hamflx/imagen3-mcp](https://github.com/hamflx/imagen3-mcp) 📇 🏠 🪟 🍎 🐧 - 一个通过 MCP 使用 Google Imagen 3.0 API 的强大图像生成工具。使用文本提示生成具有高级摄影、艺术和逼真控制的高质量图像。

### 📂 <a name="browser-automation"></a>浏览器自动化

Web 内容访问和自动化功能。支持以 AI 友好格式搜索、抓取和处理 Web 内容。
- [@blackwhite084/playwright-plus-python-mcp](https://github.com/blackwhite084/playwright-plus-python-mcp) 🌐 - 使用 Playwright 进行浏览器自动化的 MCP 服务器，更适合llm
- [@executeautomation/playwright-mcp-server](https://github.com/executeautomation/mcp-playwright) 🌐⚡️ - 使用 Playwright 进行浏览器自动化和网页抓取的 MCP 服务器
- [@automatalabs/mcp-server-playwright](https://github.com/Automata-Labs-team/MCP-Server-Playwright) 🌐🖱️ - 使用 Playwright 实现浏览器自动化的 MCP 服务器
- [@modelcontextprotocol/server-puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) 📇 🏠 - 用于网页抓取和交互的浏览器自动化
- [@kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) 📇 ☁️ - 获取 YouTube 字幕和文字记录以供 AI 分析
- [@recursechat/mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts) 📇 🏠 🍎 - MCP 服务器与 Apple Shortcuts 的集成
- [@fradser/mcp-server-apple-reminders](https://github.com/FradSer/mcp-server-apple-reminders) 📇 🏠 🍎 - macOS 上与 Apple Reminders 集成的 MCP 服务器
- [kimtth/mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing) 🐍 🏠 - 使用 Azure OpenAI 和 Playwright 的“最小”服务器/客户端 MCP 实现。
- [@pskill9/web-search](https://github.com/pskill9/web-search) 📇 🏠 - 一个支持使用 Google 搜索结果进行免费网页搜索的 MCP 服务器，无需 API 密钥
- [@co-browser/browser-use-mcp-server](https://github.com/co-browser/browser-use-mcp-server) 🌐🔮 - browser-use是一个封装了SSE传输协议的MCP服务器。包含一个dockerfile用于在docker中运行chromium浏览器+VNC服务器。
- [@34892002/bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js) 📇 🏠 - 一个支持搜索 B站 内容的 MCP 服务器。提供LangChain调用示例、测试脚本。
- [@getrupt/ashra-mcp](https://github.com/getrupt/ashra-mcp) 🐍 🏠 - 从任何网站提取结构化数据。只需输入提示即可获取JSON。
- [aircodelabs/grasp](https://github.com/aircodelabs/grasp) 📇 🏠 - 可本地部署或自托管的浏览器自动化操作，原生支持 MCP 和 A2A。

### 🎨 <a name="art-and-culture"></a>艺术与文化

提供艺术收藏、文化遗产和博物馆数据库的访问与探索。让 AI 模型能够搜索和分析艺术文化内容。

- [cantian-ai/bazi-mcp](https://github.com/cantian-ai/bazi-mcp) 📇 🏠 ☁️ 🍎 🪟 - 提供全面精准的八字排盘和测算信息
- [burningion/video-editing-mcp](https://github.com/burningion/video-editing-mcp) 📹🎬 - 从您的视频集合中添加、分析、搜索和生成视频剪辑
- [r-huijts/rijksmuseum-mcp](https://github.com/r-huijts/rijksmuseum-mcp) 📇 ☁️ - 荷兰国立博物馆 API 集成，支持艺术品搜索、详情查询和收藏品浏览
- [yuna0x0/anilist-mcp](https://github.com/yuna0x0/anilist-mcp) 📇 ☁️ - 集成 AniList API 获取动画和漫画信息的 MCP 服务器

### ☁️ <a name="cloud-platforms"></a>云平台

云平台服务集成。实现与云基础设施和服务的管理和交互。

- [qiniu/qiniu-mcp-server](https://github.com/qiniu/qiniu-mcp-server) 🐍 ☁️ - 基于七牛云产品构建的 MCP，支持访问七牛云存储、智能多媒体服务等。
- [Cloudflare MCP Server](https://github.com/cloudflare/mcp-server-cloudflare) 🎖️ 📇 ☁️ - 与 Cloudflare 服务集成，包括 Workers、KV、R2 和 D1
- [alexbakers/mcp-ipfs](https://github.com/alexbakers/mcp-ipfs) 📇 ☁️ - 上传和操作 IPFS 存储
- [alexei-led/aws-mcp-server](https://github.com/alexei-led/aws-mcp-server) 🐍 ☁️ - 一款轻量但功能强大的服务器，使AI助手能够在支持多架构的安全Docker环境中执行AWS CLI命令、使用Unix管道，并为常见AWS任务应用提示模板。
- [aliyun/alibaba-cloud-ops-mcp-server](https://github.com/aliyun/alibaba-cloud-ops-mcp-server) 🎖️ 🐍 ☁️ - 一款MCP服务器，使AI助手能够运维管理阿里云上的资源，支持ECS、云监控、OOS和其他各种广泛使用的云产品。
- [Kubernetes MCP Server](https://github.com/strowk/mcp-k8s-go) - 🏎️ ☁️ 通过 MCP 操作 Kubernetes 集群
- [@flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) - 📇 ☁️/🏠 使用 Typescript 实现 Kubernetes 集群中针对 pod、部署、服务的操作。
- [@manusa/Kubernetes MCP Server](https://github.com/manusa/kubernetes-mcp-server) - 🏎️ 🏠 一个功能强大的Kubernetes MCP服务器，额外支持OpenShift。除了为**任何**Kubernetes资源提供CRUD操作外，该服务器还提供专用工具与您的集群进行交互。
- [wenhuwang/mcp-k8s-eye](https://github.com/wenhuwang/mcp-k8s-eye) 🏎️ ☁️/🏠 提供 Kubernetes 集群资源管理, 深度分析集群和应用的健康状态
- [johnneerdael/netskope-mcp](https://github.com/johnneerdael/netskope-mcp) 🔒 ☁️ - 提供对 Netskope Private Access 环境中所有组件的访问权限，包含详细的设置信息和 LLM 使用示例。
- [nwiizo/tfmcp](https://github.com/nwiizo/tfmcp) - 🦀 🏠 - 一个Terraform MCP服务器，允许AI助手管理和操作Terraform环境，实现读取配置、分析计划、应用配置以及管理Terraform状态的功能。
- [johnneerdael/netskope-mcp](https://github.com/johnneerdael/netskope-mcp) ☁️ - 提供对 Netskope Private Access 环境中所有组件的访问权限，包含详细的设置信息和 LLM 使用示例。
- [bright8192/esxi-mcp-server](https://github.com/bright8192/esxi-mcp-server) 🐍 ☁️ - 提供对 VMware ESXi/vCenter 管理服务器，提供简单的 REST API 接口来管理虚拟机。
- [wenhuwang/mcp-k8s-eye](https://github.com/wenhuwang/mcp-k8s-eye) 🏎️ ☁️/🏠 提供 Kubernetes 集群资源管理, 深度分析集群和应用的健康状态
- [johnneerdael/netskope-mcp](https://github.com/johnneerdael/netskope-mcp) 🔒 ☁️ - 提供对 Netskope Private Access 环境中所有组件的访问权限，包含详细的设置信息和 LLM 使用示例。
- [weibaohui/k8m](https://github.com/weibaohui/k8m) - 🏎️ ☁️/🏠 提供MCP多集群k8s管理操作，提供管理界面、日志，内置近50种工具，覆盖常见运维开发场景，支持常规资源、CRD资源。
- [silenceper/mcp-k8s](https://github.com/silenceper/mcp-k8s) 🏎️ ☁️/🏠 MCP-K8S 是一个 AI 驱动的 Kubernetes 资源管理工具，通过自然语言交互方式，让用户能够轻松操作 Kubernetes 集群中的任意资源，包括原生资源（如 Deployment、Service）和自定义资源（CRD）。无需记忆复杂命令，只需描述需求，AI 就能准确执行对应的集群操作，大大提升了 Kubernetes 的易用性。
- [portainer/portainer-mcp](https://github.com/portainer/mcp-server) 🏎️ ☁️/🏠 - 一个用于管理 Portainer 容器管理平台的 MCP 服务器，支持通过自然语言交互来管理容器、镜像、网络和卷等资源。

### 🤖 <a name="coding-agents"></a>编程智能体

使大语言模型能够读取、编辑和执行代码，并自主解决各种编程任务。

- [jinzcdev/leetcode-mcp-server](https://github.com/jinzcdev/leetcode-mcp-server) 📇 ☁️ - 一个专为 LeetCode(力扣) 设计的 MCP 服务，实现自动化获取编程题目、题解文章、提交记录等公开数据，并支持用户认证（用于笔记、解题进度等私有数据），同时支持 `leetcode.com`（国际版）和 `leetcode.cn`（中国版）双站点。

### 🖥️ <a name="command-line"></a>命令行

运行命令、捕获输出以及以其他方式与 shell 和命令行工具交互。

- [ferrislucas/iterm-mcp](https://github.com/ferrislucas/iterm-mcp) 🖥️ 🛠️ 💬 - 一个为 iTerm 终端提供访问能力的 MCP 服务器。您可以执行命令，并就终端中看到的内容进行提问交互。
- [g0t4/mcp-server-commands](https://github.com/g0t4/mcp-server-commands) 📇 🏠 - 使用`run_command`和`run_script`工具运行任何命令。
- [MladenSU/cli-mcp-server](https://github.com/MladenSU/cli-mcp-server) 🐍 🏠 - 具有安全执行和可定制安全策略的命令行界面
- [tumf/mcp-shell-server](https://github.com/tumf/mcp-shell-server) 实现模型上下文协议 (MCP) 的安全 shell 命令执行服务器

### 💬 <a name="communication"></a>社交

与通讯平台集成，实现消息管理和渠道运营。使AI模型能够与团队沟通工具进行交互。

- [zcaceres/gtasks-mcp](https://github.com/zcaceres/gtasks-mcp) - 📇 ☁️ - 用于管理 Google Tasks 的 MCP 服务器
- [hannesrudolph/imessage-query-fastmcp-mcp-server](https://github.com/hannesrudolph/imessage-query-fastmcp-mcp-server) 🐍 🏠 🍎 - MCP 服务器通过模型上下文协议 (MCP) 提供对 iMessage 数据库的安全访问，使 LLM 能够通过适当的电话号码验证和附件处理来查询和分析 iMessage 对话
- [@modelcontextprotocol/server-slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack) 📇 ☁️ - 用于频道管理和消息传递的 Slack 工作区集成
- [@keturiosakys/bluesky-context-server](https://github.com/keturiosakys/bluesky-context-server) 📇 ☁️ - Bluesky 实例集成，用于查询和交互
- [MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite) - 🐍 ☁️ - 与 Gmail 和 Google 日历集成。
- [adhikasp/mcp-twikit](https://github.com/adhikasp/mcp-twikit) 🐍 ☁️ - 与 Twitter 搜索和时间线进行交互
- [gotoolkits/wecombot](https://github.com/gotoolkits/mcp-wecombot-server.git) - 🚀 ☁️  - MCP服务器 Tools 应用程序，用于向企业微信群机器人发送各种类型的消息。
- [AbdelStark/nostr-mcp](https://github.com/AbdelStark/nostr-mcp) - 🌐 ☁️ - Nostr MCP 服务器，支持与 Nostr 交互，可发布笔记等功能。
- [elie222/inbox-zero](https://github.com/elie222/inbox-zero/tree/main/apps/mcp-server) - 🐍 ☁️ - 一款专为 Inbox Zero 设计的MCP服务器。在Gmail基础上新增功能，例如识别需要回复或跟进处理的邮件。
- [carterlasalle/mac_messages_mcp](https://github.com/carterlasalle/mac_messages_mcp) 🏠 🍎 🚀 - 一款通过模型上下文协议（MCP）安全连接iMessage数据库的MCP服务器，支持大语言模型查询与分析iMessage对话。该系统具备完善的电话号码验证、附件处理、联系人管理、群聊操作功能，并全面支持消息收发。
- [sawa-zen/vrchat-mcp](https://github.com/sawa-zen/vrchat-mcp) - 📇 🏠 这是一个与VRChat API交互的MCP服务器。您可以获取VRChat的好友、世界、化身等信息。
- [line/line-bot-mcp-server](https://github.com/line/line-bot-mcp-server) 🎖 📇 ☁️ - 整合 LINE 官方账号的 MCP 服务器
- [arpitbatra123/mcp-googletasks](https://github.com/arpitbatra123/mcp-googletasks) - 📇 ☁️ - 一个用于连接Google Tasks API的MCP服务器
- [teddyzxcv/ntfy-mcp](https://github.com/teddyzxcv/ntfy-mcp) 通过使用 ntfy 向手机发送通知，实时更新信息的 MCP 服务器。
- [YCloud-Developers/ycloud-whatsapp-mcp-server](https://github.com/YCloud-Developers/ycloud-whatsapp-mcp-server) 📇 🏠 - 一个通过 YCloud 平台发送 WhatsApp Business 消息的 MCP 服务器。
- [jaipandya/producthunt-mcp-server](https://github.com/jaipandya/producthunt-mcp-server) 🐍 🏠 - Product Hunt 的 MCP 服务器。与热门帖子、评论、收藏集、用户等进行交互。

### 👤 <a name="customer-data-platforms"></a>客户数据平台

提供对客户数据平台内客户资料的访问

- [sergehuber/inoyu-mcp-unomi-server](https://github.com/sergehuber/inoyu-mcp-unomi-server) 📇 ☁️ - MCP 服务器用于访问和更新 Apache Unomi CDP 服务器上的配置文件。
- [OpenDataMCP/OpenDataMCP](https://github.com/OpenDataMCP/OpenDataMCP) 🐍☁️ - 使用模型上下文协议将任何开放数据连接到任何 LLM。
- [tinybirdco/mcp-tinybird](https://github.com/tinybirdco/mcp-tinybird) 🐍☁️ - MCP 服务器可从任何 MCP 客户端与 Tinybird Workspace 进行交互。
- [@iaptic/mcp-server-iaptic](https://github.com/iaptic/mcp-server-iaptic) 🎖️ 📇 ☁️ - 连接 [iaptic](https://www.iaptic.com) 平台，让您轻松查询客户购买记录、交易数据以及应用营收统计信息。
- [@antv/mcp-server-chart](https://github.com/antvis/mcp-server-chart) 🎖️ 📇 ☁️ - 一个基于 [AntV](https://github.com/antvis) 生成数据可视化图表的 MCP Server 插件。

### 🗄️ <a name="databases"></a>数据库

具有模式检查功能的安全数据库访问。支持使用可配置的安全控制（包括只读访问）查询和分析数据。

- [aliyun/alibabacloud-tablestore-mcp-server](https://github.com/aliyun/alibabacloud-tablestore-mcp-server) ☕ 🐍 ☁️ - 阿里云表格存储(Tablestore)的 MCP 服务器实现，特性包括添加文档、基于向量和标量进行语义搜索、RAG友好。
- [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) 🐍 🏠 - 集成 Elasticsearch 的 MCP 服务器实现
- [domdomegg/airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server) 📇 🏠 - Airtable 数据库集成，具有架构检查、读写功能
- [rashidazarang/airtable-mcp](https://github.com/rashidazarang/airtable-mcp) 🐍 ☁️ - 将AI工具直接连接至Airtable。通过自然语言查询、创建、更新及删除记录。通过标准化MCP接口实现的功能包括：基库管理、表格操作、结构修改、记录筛选以及数据迁移。
- [LucasHild/mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery) 🐍 ☁️ - BigQuery 数据库集成了架构检查和查询功能
- [c4pt0r/mcp-server-tidb](https://github.com/c4pt0r/mcp-server-tidb) 🐍 ☁️ - TiDB 数据库集成，包括表结构的建立 DDL 和 SQL 的执行
- [crystaldba/postgres-mcp](https://github.com/crystaldba/postgres-mcp) 🐍 🏠 - 全能型 MCP 服务器，用于 Postgres 开发和运维，提供性能分析、调优和健康检查等工具
- [tradercjz/dolphindb-mcp-server](https://github.com/tradercjz/dolphindb-mcp-server) 🐍 ☁️ - TDolphinDB数据库集成，具备模式检查与查询功能
- [ergut/mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server) 📇 ☁️ - Google BigQuery 集成的服务器实现，可实现直接 BigQuery 数据库访问和查询功能
- [ClickHouse/mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse) 🐍 ☁️ - 集成 Apache Kafka 和 Timeplus。可以获取Kafka中的最新数据，并通过 Timeplus 来 SQL 查询。
- [get-convex/convex-backend](https://stack.convex.dev/convex-mcp-server) 📇 ☁️ - 集成 Convex 数据库，用于查看表结构、函数及执行一次性查询([Source](https://github.com/get-convex/convex-backend/blob/main/npm-packages/convex/src/cli/mcp.ts))
- [@gannonh/firebase-mcp](https://github.com/gannonh/firebase-mcp) 🔥 ⛅️ - 包括认证、Firestore和存储在内的Firebase服务。
- [jovezhong/mcp-timeplus](https://github.com/jovezhong/mcp-timeplus) 🐍 ☁️ - 用于Apache Kafka和Timeplus的MCP服务器。能够列出Kafka主题、轮询Kafka消息、将Kafka数据本地保存，并通过Timeplus使用SQL查询流数据。
- [@fireproof-storage/mcp-database-server](https://github.com/fireproof-storage/mcp-database-server) 📇 ☁️ - Fireproof 分布式账本数据库，支持多用户数据同步
- [designcomputer/mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server) 🐍 🏠 - MySQL 数据库集成可配置的访问控制、模式检查和全面的安全指南
- [wenb1n-dev/mysql_mcp_server_pro](https://github.com/wenb1n-dev/mysql_mcp_server_pro)  🐍 🏠 - 支持SSE，STDIO；不仅止于mysql的增删改查功能；还包含了数据库异常分析能力；根据角色控制数据库权限；且便于开发者们进行个性化的工具扩展
- [f4ww4z/mcp-mysql-server](https://github.com/f4ww4z/mcp-mysql-server) 📇 🏠 - 基于 Node.js 的 MySQL 数据库集成，提供安全的 MySQL 数据库操作
- [FreePeak/db-mcp-server](https://github.com/FreePeak/db-mcp-server) 🏎️ 🏠 – 一款基于Golang构建的高性能多数据库MCP服务器，支持MySQL和PostgreSQL（即将支持NoSQL）。内置查询执行、事务管理、模式探索、查询构建以及性能分析工具，与Cursor无缝集成优化数据库工作流程。
- [@modelcontextprotocol/server-postgres](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) 📇 🏠 - PostgreSQL 数据库集成了模式检查和查询功能
- [@modelcontextprotocol/server-sqlite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) 🐍 🏠 - 具有内置分析功能的 SQLite 数据库操作
- [@joshuarileydev/supabase-mcp-server](https://github.com/joshuarileydev/supabase) - Supabase MCP 服务器用于管理和创建 Supabase 中的项目和组织
- [ktanaka101/mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb) 🐍 🏠 - DuckDB 数据库集成了模式检查和查询功能
- [Dataring-engineering/mcp-server-trino](https://github.com/Dataring-engineering/mcp-server-trino) 🐍 ☁️ - 用于查询和访问Trino集群数据的Trino MCP服务器。
- [tuannvm/mcp-trino](https://github.com/tuannvm/mcp-trino) 🏎️ ☁️ - 用于 Trino 的 Model Context Protocol (MCP) 服务器的 Go 实现.
- [memgraph/mcp-memgraph](https://github.com/memgraph/mcp-memgraph) 🐍 🏠 - Memgraph MCP 서버 - 包含一个对Memgraph执行查询的工具以及一个模式资源。
- [furey/mongodb-lens](https://github.com/furey/mongodb-lens) 📇 🏠 - MongoDB Lens：功能全面的MongoDB数据库MCP服务器
- [QuantGeekDev/mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp) 📇 🏠 - MongoDB 集成使 LLM 能够直接与数据库交互。
- [kiliczsh/mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server) 📇 🏠 - MongoDB 的模型上下文协议服务器
- [tinybirdco/mcp-tinybird](https://github.com/tinybirdco/mcp-tinybird) 🐍 ☁️ - Tinybird 集成查询和 API 功能
- [KashiwaByte/vikingdb-mcp-server](https://github.com/KashiwaByte/vikingdb-mcp-server) 🐍 ☁️ - VikingDB 数据库集成了collection和index的基本信息介绍，并提供向量存储和查询的功能.
- [neo4j-contrib/mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j) 🐍 🏠 - Neo4j 的模型上下文协议
- [niledatabase/nile-mcp-server](https://github.com/niledatabase/nile-mcp-server) 🐍 ☁️ - Nile 的 Postgres 平台 MCP 服务器 - 使用 LLM 管理和查询 Postgres 数据库、租户、用户和认证
- [isaacwasserman/mcp-snowflake-server](https://github.com/isaacwasserman/mcp-snowflake-server) 🐍 ☁️ - Snowflake 集成实现，支持读取和（可选）写入操作，并具备洞察跟踪功能
- [hannesrudolph/sqlite-explorer-fastmcp-mcp-server](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server) 🐍 🏠 - 一个 MCP 服务器，通过模型上下文协议 （MCP） 提供对 SQLite 数据库的安全只读访问。该服务器是使用 FastMCP 框架构建的，它使 LLM 能够探索和查询具有内置安全功能和查询验证的 SQLite 数据库。
- [sirmews/mcp-pinecone](https://github.com/sirmews/mcp-pinecone) 🐍 ☁️ - Pinecone 与矢量搜索功能的集成
- [runekaagaard/mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy) 🐍 🏠 - 基于SQLAlchemy的通用数据库集成，支持PostgreSQL、MySQL、MariaDB、SQLite、Oracle、MS SQL Server等众多数据库。具有架构和关系检查以及大型数据集分析功能。
- [Zhwt/go-mcp-mysql](https://github.com/Zhwt/go-mcp-mysql) 🏎️ 🏠 – 基于 Go 的开箱即用的 MySQL MCP 服务器，支持只读模式和自动 Schema 检查。
- [mcp-server-jdbc](https://github.com/quarkiverse/quarkus-mcp-servers/tree/main/jdbc) ☕ 🏠 - 连接到任何兼容JDBC的数据库，执行查询、插入、更新、删除等操作。
- [pab1it0/adx-mcp-server](https://github.com/pab1it0/adx-mcp-server) 🐍 ☁️ - 查询和分析Azure Data Explorer数据库
- [pab1it0/prometheus-mcp-server](https://github.com/pab1it0/prometheus-mcp-server) 🐍 ☁️ -  查询并分析开源监控系统Prometheus。
- [neondatabase/mcp-server-neon](https://github.com/neondatabase/mcp-server-neon) 📇 ☁️ — 用于通过 Neon Serverless Postgres 创建和管理 Postgres 数据库的MCP服务器
- [XGenerationLab/xiyan_mcp_server](https://github.com/XGenerationLab/xiyan_mcp_server) 📇 ☁️ — 一个支持通过自然语言查询从数据库获取数据的MCP服务器，由XiyanSQL作为文本转SQL的大语言模型提供支持。
- [bytebase/dbhub](https://github.com/bytebase/dbhub) 📇 🏠 – 支持主流数据库的通用数据库MCP服务器。
- [GreptimeTeam/greptimedb-mcp-server](https://github.com/GreptimeTeam/greptimedb-mcp-server) 🐍 🏠 - 查询 GreptimeDB 的 MCP 服务。
- [idoru/influxdb-mcp-server](https://github.com/idoru/influxdb-mcp-server) 📇 ☁️ 🏠 - 针对 InfluxDB OSS API v2 运行查询
- [xing5/mcp-google-sheets](https://github.com/xing5/mcp-google-sheets) 🐍 ☁️ - 一个用于与 Google Sheets 交互的模型上下文协议服务器。该服务器通过 Google Sheets API 提供创建、读取、更新和管理电子表格的工具。
- [freema/mcp-gsheets](https://github.com/freema/mcp-gsheets) 📇 ☁️ - 具有全面读取、写入、格式化和工作表管理功能的 Google Sheets API 集成 MCP 服务器。
- [qdrant/mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant) 🐍 🏠 - 一个Qdrant MCP服务器
- [ydb/ydb-mcp](https://github.com/ydb-platform/ydb-mcp) 🎖️ 🐍 ☁️ – MCP 服务器：用于与 [YDB](https://ydb.tech) 数据库交互。
- [yincongcyincong/VictoriaMetrics-mcp-server](https://github.com/yincongcyincong/VictoriaMetrics-mcp-server) 🐍 🏠 - VictoriaMetrics 数据库 MCP 服务器.

### 📊 <a name="data-platforms"></a>数据平台

用于数据集成、转换和管道编排的数据平台。

- [flowcore/mcp-flowcore-platform](https://github.com/flowcore-io/mcp-flowcore-platform) 🎖️📇☁️🏠 - 与 Flowcore 交互以执行操作、提取数据以及分析、交叉引用和利用数据核心或公共数据核心中的任何数据；全部通过人类语言完成。

### 💻 <a name="developer-tools"></a>开发者工具

增强开发工作流程和环境管理的工具和集成。

- [21st-dev/Magic-MCP](https://github.com/21st-dev/magic-mcp) - 打造受21世纪顶尖设计工程师启发的精致UI组件。
- [Hypersequent/qasphere-mcp](https://github.com/Hypersequent/qasphere-mcp) 🎖️ 📇 ☁️ - 与[QA Sphere](https://qasphere.com/)测试管理系统集成，使LLM能够发现、总结和操作测试用例，并可直接从AI驱动的IDE访问
- [Coment-ML/Opik-MCP](https://github.com/comet-ml/opik-mcp) 🎖️ 📇 ☁️ 🏠 - 使用自然语言与您的LLM可观测性、Opik捕获的追踪和监控数据进行对话。
- [GLips/Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) 📇 🏠 - 为编码代理提供直接访问Figma数据的权限，助力其一次性完成设计实现。
- [QuantGeekDev/docker-mcp](https://github.com/QuantGeekDev/docker-mcp) 🏎️ 🏠 - 通过 MCP 进行 Docker 容器管理和操作
- [zcaceres/fetch-mcp](https://github.com/zcaceres/fetch-mcp) 📇 🏠 - 一个灵活获取 JSON、文本和 HTML 数据的 MCP 服务器
- [kealuya/mcp-jina-ai](https://github.com/kealuya/mcp-jina-ai) 🏎️ 🏠 - 集成 Jina.ai 将目标网页进行总结，转换成对LLM友好的Markdown格式返回
- [r-huijts/xcode-mcp-server](https://github.com/r-huijts/xcode-mcp-server) 📇 🏠 🍎 - Xcode 集成，支持项目管理、文件操作和构建自动化
- [snaggle-ai/openapi-mcp-server](https://github.com/snaggle-ai/openapi-mcp-server) 🏎️ 🏠 - 使用开放 API 规范 (v3) 连接任何 HTTP/REST API 服务器
- [jetbrains/mcpProxy](https://github.com/JetBrains/mcpProxy) 🎖️ 📇 🏠 - 连接到 JetBrains IDE
- [tumf/mcp-text-editor](https://github.com/tumf/mcp-text-editor) 🐍 🏠 - 面向行的文本文件编辑器。针对 LLM 工具进行了优化，具有高效的部分文件访问功能，可最大限度地减少令牌使用量。
- [@joshuarileydev/simulator-mcp-server](https://github.com/JoshuaRileyDev/simulator-mcp-server) 📇 🏠 - 用于控制 iOS 模拟器的 MCP 服务器
- [@joshuarileydev/app-store-connect-mcp-server](https://github.com/JoshuaRileyDev/app-store-connect-mcp-server) 📇 🏠 - 一个 MCP 服务器，用于与 iOS 开发者的 App Store Connect API 进行通信
- [@sammcj/mcp-package-version](https://github.com/sammcj/mcp-package-version) 📇 🏠 - MCP 服务器可帮助 LLM 在编写代码时建议最新的稳定软件包版本。
- [delano/postman-mcp-server](https://github.com/delano/postman-mcp-server) 📇 ☁️ - 与 [Postman API](https://www.postman.com/postman/postman-public-workspace/) 进行交互
- [vivekVells/mcp-pandoc](https://github.com/vivekVells/mcp-pandoc) 🗄️ 🚀 - 基于 Pandoc 的 MCP 服务器，支持 Markdown、HTML、PDF、DOCX（.docx）、csv 等格式之间的无缝转换
- [pskill9/website-downloader](https://github.com/pskill9/website-downloader) 🗄️ 🚀 - 这个 MCP 服务器提供了使用 wget 下载完整网站的工具，可保留网站结构并转换链接以支持本地访问
- [@lamemind/mcp-server-multiverse](https://github.com/lamemind/mcp-server-multiverse) 📇 🏠 🛠️ - 一种中间件服务器，允许多个相同MCP服务器的隔离实例以独立的命名空间和配置共存。
- [j4c0bs/mcp-server-sql-analyzer](https://github.com/j4c0bs/mcp-server-sql-analyzer) 🐍 - 基于 [SQLGlot](https://github.com/tobymao/sqlglot) 的 MCP 服务器，提供 SQL 分析、代码检查和方言转换功能
- [@haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server) 🐍 🏠 - 一个Excel操作服务器，提供工作簿创建、数据操作、格式设置及高级功能（图表、数据透视表、公式）。
- [xcodebuild](https://github.com/ShenghaiWang/xcodebuild) 🍎 构建iOS Xcode工作区/项目并将错误反馈给LLM。
- [@jasonjmcghee/claude-debugs-for-you](https://github.com/jasonjmcghee/claude-debugs-for-you) 📇 🏠 - 一个MCP服务器及VS Code扩展，支持通过断点和表达式评估实现（语言无关的）自动调试。
- [@Jktfe/serveMyAPI](https://github.com/Jktfe/serveMyAPI) 📇 🏠 🍎 - 一个个人MCP（模型上下文协议）服务器，用于通过macOS钥匙串安全存储和跨项目访问API密钥。
- [@xzq.xu/jvm-mcp-server](https://github.com/xzq-xu/jvm-mcp-server) 📇 🏠  - 一个基于JVM的MCP（模型上下文协议）服务器的实现项目。
- [@yangkyeongmo@/mcp-server-apache-airflow](https://github.com/yangkyeongmo/mcp-server-apache-airflow) 🐍 🏠 - 使用官方客户端连接至[Apache Airflow](https://airflow.apache.org/)的MCP服务器。
- [hyperb1iss/droidmind](https://github.com/hyperb1iss/droidmind) 🐍 🏠 - 通过MCP利用AI控制安卓设备，实现设备操控、调试、系统分析及UI自动化，并配备全面的安全框架。
- [XixianLiang/HarmonyOS-mcp-server](https://github.com/XixianLiang/HarmonyOS-mcp-server) 🐍 🏠 - 通过MCP利用AI控制鸿蒙(next)设备，实现设备操控及UI自动化
- [Rootly-AI-Labs/Rootly-MCP-server](https://github.com/Rootly-AI-Labs/Rootly-MCP-server) 🎖️🐍☁️🍎 - 用于事件管理平台 Rootly](https://rootly.com/) 的 MCP 服务器
- [YuChenSSR/mindmap-mcp-server](https://github.com/YuChenSSR/mindmap-mcp-server) 🐍 🏠 - 用于生成漂亮交互式思维导图mindmap的模型上下文协议（MCP）服务器。
- [InhiblabCore/mcp-image-compression](https://github.com/InhiblabCore/mcp-image-compression) 🐍 🏠 - 用于本地压缩各种图片格式的 MCP 服务器。
- [SDGLBL/mcp-claude-code](https://github.com/SDGLBL/mcp-claude-code) 🐍 🏠 - 使用 MCP 实现的 Claude Code 功能，支持 AI 代码理解、修改和项目分析，并提供全面的工具支持。
- [IlyaGulya/gradle-mcp-server](https://github.com/IlyaGulya/gradle-mcp-server) 🏠 - 使用 Gradle Tooling API 来检查项目、执行任务并在每个测试的级别进行测试结果报告的 Gradle 集成
- [gofireflyio/firefly-mcp](https://github.com/gofireflyio/firefly-mcp) 🎖️ 📇 ☁️ - 集成、发现、管理并通过[Firefly](https://firefly.ai)规范化云资源。
- [api7/apisix-mcp](https://github.com/api7/apisix-mcp) 🎖️ 📇 🏠 支持对 [Apache APISIX](https://github.com/apache/apisix) 网关中所有资源进行查询和管理的 MCP 服务。
- [ios-simulator-mcp](https://github.com/joshuayoes/ios-simulator-mcp) 📇 🏠 🍎 - 用于与 iOS 模拟器交互的模型上下文协议 (MCP) 服务器。此服务器允许您通过获取有关 iOS 模拟器的信息、控制 UI 交互和检查 UI 元素来与 iOS 模拟器交互。
- [higress-group/higress-ops-mcp-server](https://github.com/higress-group/higress-ops-mcp-server) 🐍 🏠 - 支持对 [Higress](https://github.com/alibaba/higress/blob/main/README_ZH.md) 网关进行全面的配置和管理。
- [ReAPI-com/mcp-openapi](https://github.com/ReAPI-com/mcp-openapi) 📇 🏠 - MCP服务器让LLM能够了解您的OpenAPI规范的所有信息，以发现、解释和生成代码/模拟数据
- [automation-ai-labs/mcp-link](https://github.com/automation-ai-labs/mcp-link) 🏎️ 🏠 - 无缝集成任何 API 与 AI 代理（通过 OpenAPI 架构）
- [cjo4m06/mcp-shrimp-task-manager](https://github.com/cjo4m06/mcp-shrimp-task-manager) 📇 ☁️ 🏠 – 一款专为编程开发设计的任务管理系统，通过先进的任务记忆、自我反思和依赖管理，增强如 Cursor AI 等编码代理的能力。 [ShrimpTaskManager](https://cjo4m06.github.io/mcp-shrimp-task-manager)
- [axliupore/mcp-code-runner](https://github.com/axliupore/mcp-code-runner) 📇 🏠 - 一个MCP服务器，用于在本地通过docker运行代码，并支持多种编程语言。
- [TencentEdgeOne/edgeone-pages-mcp](https://github.com/TencentEdgeOne/edgeone-pages-mcp) 📇 ☁️ - 基于 EdgeOne Pages 的 MCP 服务器，支持代码部署为在线页面。
- [yikakia/godoc-mcp-server](https://github.com/yikakia/godoc-mcp-server) 🏎️ ☁️ 🪟 🐧 🍎 - 查询 pkg.go.dev 上的 golang 包信息
- [lpigeon/ros-mcp-server](https://github.com/lpigeon/ros-mcp-server) 🐍 🏠 🍎 🪟 🐧 - ROS MCP服务器通过将用户的自然语言指令转换为ROS或ROS2控制指令，以支持机器人的控制。

### 🧮 <a name="data-science-tools"></a>数据科学工具

旨在简化数据探索、分析和增强数据科学工作流程的集成和工具。

- [@reading-plus-ai/mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration) 🐍 ☁️ - 支持对基于 .csv 的数据集进行自主数据探索，以最小的成本提供智能见解。
- [zcaceres/markdownify-mcp](https://github.com/zcaceres/markdownify-mcp) 📇 🏠 - 一个 MCP 服务器，可将几乎任何文件或网络内容转换为 Markdown
- [@reading-plus-ai/mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration) 🐍 ☁️ - 实现基于.csv数据集的自动数据探索，提供最少工作量的智能化洞察。

### 📂 <a name="file-systems"></a>文件系统

提供对本地文件系统的直接访问，并具有可配置的权限。使 AI 模型能够读取、写入和管理指定目录中的文件。

- [@modelcontextprotocol/server-filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) 📇 🏠 - 直接访问本地文件系统。
- [@modelcontextprotocol/server-google-drive](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive) 📇 ☁️ - Google Drive 集成，用于列出、阅读和搜索文件
- [hmk/box-mcp-server](https://github.com/hmk/box-mcp-server) 📇 ☁️ - Box 集成，支持文件列表、阅读和搜索功能
- [mark3labs/mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server) 🏎️ 🏠 - 用于本地文件系统访问的 Golang 实现。
- [mamertofabian/mcp-everything-search](https://github.com/mamertofabian/mcp-everything-search) 🐍 🏠 🪟 - 使用 Everything SDK 实现的快速 Windows 文件搜索
- [cyberchitta/llm-context.py](https://github.com/cyberchitta/llm-context.py) 🐍 🏠 - 通过 MCP 或剪贴板与 LLM 共享代码上下文
- [filesystem@quarkiverse/quarkus-mcp-servers](https://github.com/quarkiverse/quarkus-mcp-servers/tree/main/filesystem) ☕ 🏠 - 一个基于Java和Quarkus实现的文件系统，支持浏览和编辑文件。提供jar包或原生镜像两种形式。
- [Xuanwo/mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal) 🐍 🏠 ☁️ - 使用 Apache OpenDAL™ 访问任何存储
- [exoticknight/mcp-file-merger](https://github.com/exoticknight/mcp-file-merger) 📇 🏠 - 文件合并工具，适配AI Chat长度限制

### 💰 <a name="finance--fintech"></a>金融与金融科技

金融数据访问和加密货币市场信息。支持查询实时市场数据、加密货币价格和财务分析。

- [heurist-network/heurist-mesh-mcp-server](https://github.com/heurist-network/heurist-mesh-mcp-server) 🎖️ ⛅️ 🏠 🐍 - 通过Heurist Mesh网络访问专业化的web3 AI代理，用于区块链分析、智能合约安全审计、代币指标评估及链上交互。提供全面的DeFi分析工具、NFT估值及跨多链交易监控功能
- [@base/base-mcp](https://github.com/base/base-mcp) 🎖️ 📇 ☁️ - 集成Base网络的链上工具，支持与Base网络及Coinbase API交互，实现钱包管理、资金转账、智能合约和DeFi操作
- [QuantGeekDev/coincap-mcp](https://github.com/QuantGeekDev/coincap-mcp) 📇 ☁️ - 使用 CoinCap 的公共 API 集成实时加密货币市场数据，无需 API 密钥即可访问加密货币价格和市场信息
- [anjor/coinmarket-mcp-server](https://github.com/anjor/coinmarket-mcp-server) 🐍 ☁️ - Coinmarket API 集成以获取加密货币列表和报价
- [berlinbra/alpha-vantage-mcp](https://github.com/berlinbra/alpha-vantage-mcp) 🐍 ☁️ - Alpha Vantage API 集成，用于获取股票和加密货币信息
- [ferdousbhai/tasty-agent](https://github.com/ferdousbhai/tasty-agent) 🐍 ☁️ - Tastyworks API 集成，用于管理 Tastytrade 平台的交易活动
- [ferdousbhai/investor-agent](https://github.com/ferdousbhai/investor-agent) 🐍 ☁️ - 整合雅虎财经以获取股市数据，包括期权推荐
- [mcpdotdirect/evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server) 📇 ☁️ - 全面支持30多种EVM网络的区块链服务，涵盖原生代币、ERC20、NFT、智能合约、交易及ENS解析。
- [bankless/onchain-mcp](https://github.com/Bankless/onchain-mcp/) 📇 ☁️ - Bankless链上API，用于与智能合约交互、查询交易及代币信息
- [kukapay/cryptopanic-mcp-server](https://github.com/kukapay/cryptopanic-mcp-server) 🐍 ☁️ - 为AI代理提供由CryptoPanic驱动的最新加密货币新闻。
- [kukapay/whale-tracker-mcp](https://github.com/kukapay/whale-tracker-mcp) 🐍 ☁️ -  一个用于追踪加密货币大额交易的MCP服务器。
- [kukapay/crypto-feargreed-mcp](https://github.com/kukapay/crypto-feargreed-mcp) 🐍 ☁️ -  提供实时和历史加密恐惧与贪婪指数数据。
- [kukapay/dune-analytics-mcp](https://github.com/kukapay/dune-analytics-mcp) 🐍 ☁️ -  一个将Dune Analytics数据桥接到AI代理的mcp服务器。
- [kukapay/pancakeswap-poolspy-mcp](https://github.com/kukapay/pancakeswap-poolspy-mcp) 🐍 ☁️ -  一个追踪Pancake Swap上新创建资金池的MCP服务器。
- [kukapay/uniswap-poolspy-mcp](https://github.com/kukapay/uniswap-poolspy-mcp) 🐍 ☁️ -  一个MCP服务器，用于追踪Uniswap在多个区块链上新创建的流动性池。
- [kukapay/uniswap-trader-mcp](https://github.com/kukapay/uniswap-trader-mcp) 🐍 ☁️ -  一个MCP服务器，用于AI代理在多个区块链上的Uniswap去中心化交易所自动执行代币交换。
- [kukapay/token-minter-mcp](https://github.com/kukapay/token-minter-mcp) 🐍 ☁️ -  一个MCP服务器，为AI代理提供工具以跨多个区块链铸造ERC-20代币。
- [kukapay/thegraph-mcp](https://github.com/kukapay/thegraph-mcp) 🐍 ☁️ -  一个MCP服务器，通过The Graph提供的索引区块链数据为AI代理提供支持。
- [longportapp/openapi](https://github.com/longportapp/openapi/tree/main/mcp) - 🐍 ☁️ - LongPort OpenAPI 提供港美股等市场的股票实时行情数据，通过 MCP 提供 AI 接入分析、交易能力。
- [pwh-pwh/coin-mcp-server](https://github.com/pwh-pwh/coin-mcp-server) 🐍 ☁️ -  使用 Bitget 公共 API 去获取加密货币最新价格
- [HuggingAGI/mcp-baostock-server](https://github.com/HuggingAGI/mcp-baostock-server) 🐍 ☁️ - 基于 baostock 的 MCP 服务器,提供对中国股票市场数据的访问和分析功能。
- [Wuye-AI/mcp-server-wuye-ai](https://github.com/wuye-ai/mcp-server-wuye-ai) 🎖️ 📇 ☁️ - 接入 CRIC物业AI 平台的 MCP 服务器。CRIC物业AI 是克而瑞专为物业行业打造的智能 AI 助理。
- [zlinzzzz/finData-mcp-server](https://github.com/zlinzzzz/finData-mcp-server) 🐍 ☁️ -  一个获取专业级金融数据的MCP服务器，支持Tushare等多种数据供应商。

### 🎮 <a name="gaming"></a>游戏

游戏相关数据和服务集成

- [Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp) 📇 🏠 - 一个用于与Godot游戏引擎交互的MCP服务器，提供编辑、运行、调试和管理Godot项目中场景的工具。
- [rishijatia/fantasy-pl-mcp](https://github.com/rishijatia/fantasy-pl-mcp/) 🐍 ☁️ - 用于实时 Fantasy Premier League 数据和分析工具的 MCP 服务器。
- [CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity) 📇 #️⃣ 🏠 - Unity3d 游戏引擎集成 MCP 服务器
- [opgginc/opgg-mcp](https://github.com/opgginc/opgg-mcp) 📇 ☁️ - 访问英雄联盟、云顶之弈、无界英雄等热门游戏的实时游戏数据，提供英雄分析、电竞赛程、元组合和角色统计。

### 🧠 <a name="knowledge--memory"></a>知识与记忆

使用知识图谱结构的持久内存存储。使 AI 模型能够跨会话维护和查询结构化信息。

- [jinzcdev/markmap-mcp-server](https://github.com/jinzcdev/markmap-mcp-server) 📇 🏠 - 基于 [markmap](https://github.com/markmap/markmap) 构建的 MCP 服务器，可将 **Markdown** 转换为交互式的 **思维导图**。支持多格式导出（PNG/JPG/SVG）、浏览器在线预览、一键复制 Markdown 和动态可视化功能。
- [@modelcontextprotocol/server-memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) 📇 🏠 - 基于知识图谱的长期记忆系统用于维护上下文
- [/CheMiguel23/MemoryMesh](https://github.com/CheMiguel23/MemoryMesh) 📇 🏠 - 增强基于图形的记忆，重点关注 AI 角色扮演和故事生成
- [/topoteretes/cognee](https://github.com/topoteretes/cognee/tree/dev/cognee-mcp) 📇 🏠 - AI应用程序和Agent的内存管理器使用各种图存储和向量存储，并允许从 30 多个数据源提取数据
- [@hannesrudolph/mcp-ragdocs](https://github.com/hannesrudolph/mcp-ragdocs) 🐍 🏠 - MCP 服务器实现提供了通过矢量搜索检索和处理文档的工具，使 AI 助手能够利用相关文档上下文来增强其响应能力
- [@kaliaboi/mcp-zotero](https://github.com/kaliaboi/mcp-zotero) 📇 ☁️ - 为 LLM 提供的连接器，用于操作 Zotero Cloud 上的文献集合和资源
- [mcp-summarizer](https://github.com/0xshellming/mcp-summarizer) 📕 ☁️ - AI摘要生成MCP服务器，支持多种内容类型：纯文本、网页、PDF文档、EPUB电子书、HTML内容
- [graphlit-mcp-server](https://github.com/graphlit/graphlit-mcp-server) 📇 ☁️ - 将来自Slack、Discord、网站、Google Drive、Linear或GitHub的任何内容摄取到Graphlit项目中，然后在诸如Cursor、Windsurf或Cline等MCP客户端中搜索并检索相关知识。
- [@mem0ai/mem0-mcp](https://github.com/mem0ai/mem0-mcp) 🐍 🏠 - 用于 Mem0 的模型上下文协议服务器，帮助管理编码偏好和模式，提供工具用于存储、检索和语义处理代码实现、最佳实践和技术文档，适用于 Cursor 和 Windsurf 等 IDE
- [@ragieai/mcp-server](https://github.com/ragieai/ragie-mcp-server) 📇 ☁️ - 从您的 [Ragie](https://www.ragie.ai) (RAG) 知识库中检索上下文，该知识库连接到 Google Drive、Notion、JIRA 等多种集成。

### 🗺️ <a name="location-services"></a>位置服务

地理和基于位置的服务集成。支持访问地图数据、方向和位置信息。

- [@modelcontextprotocol/server-google-maps](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps) 📇 ☁️ - Google 地图集成，提供位置服务、路线规划和地点详细信息
- [SecretiveShell/MCP-timeserver](https://github.com/SecretiveShell/MCP-timeserver) 🐍 🏠 - 访问任意时区的时间并获取当前本地时间
- [webcoderz/MCP-Geo](https://github.com/webcoderz/MCP-Geo) 🐍 🏠 - 支持 nominatim、ArcGIS、Bing 的地理编码 MCP 服务器
- [@briandconnelly/mcp-server-ipinfo](https://github.com/briandconnelly/mcp-server-ipinfo) 🐍 ☁️ - 使用 IPInfo API 获取 IP 地址的地理位置和网络信息
- [QGIS MCP](https://github.com/jjsantos01/qgis_mcp) - 通过MCP将QGIS桌面端与Claude AI连接。该集成支持提示辅助的项目创建、图层加载、代码执行等功能。
-  [kukapay/nearby-search-mcp](https://github.com/kukapay/nearby-search-mcp) 🐍 ☁️ - 一个基于IP定位检测的附近地点搜索MCP服务器。

### 🎯 <a name="marketing"></a>营销

用于创建和编辑营销内容、处理网页元数据、产品定位和编辑指南的工具。

- [Open Strategy Partners Marketing Tools](https://github.com/open-strategy-partners/osp_marketing_tools) 🐍 🏠 - Open Strategy Partners 提供的营销工具套件，包含写作风格指南、编辑规范和产品营销价值图谱创建工具

### 📊 <a name="monitoring"></a>监测

访问和分析应用程序监控数据。使 AI 模型能够审查错误报告和性能指标。

- [@modelcontextprotocol/server-sentry](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry) 🐍 ☁️ - Sentry.io 集成用于错误跟踪和性能监控
- [@MindscapeHQ/server-raygun](https://github.com/MindscapeHQ/mcp-server-raygun) 📇 ☁️ - Raygun API V3 集成用于崩溃报告和真实用户监控
- [metoro-io/metoro-mcp-server](https://github.com/metoro-io/metoro-mcp-server) 🎖️ 🏎️ ☁️ - 查询并与 Metoro 监控的 kubernetes 环境交互
- [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) 🎖️ 🐍 🏠 ☁️ - 在 Grafana 实例中搜索仪表盘、调查事件并查询数据源
- [tumf/grafana-loki-mcp](https://github.com/tumf/grafana-loki-mcp) 🐍 🏠 - 一个 MCP 服务器，允许通过 Grafana API 查询 Loki 日志。
- [pydantic/logfire-mcp](https://github.com/pydantic/logfire-mcp) 🎖️ 🐍 ☁️ - 通过Logfire提供对OpenTelemetry追踪和指标的访问
- [seekrays/mcp-monitor](https://github.com/seekrays/mcp-monitor) 🏎️ 🏠 - 一款通过模型上下文协议（MCP）暴露系统指标的监控工具。该工具允许大型语言模型通过兼容MCP的接口实时获取系统信息（支持CPU、内存、磁盘、网络、主机、进程）。
- [hyperb1iss/lucidity-mcp](https://github.com/hyperb1iss/lucidity-mcp) 🐍 🏠 - 通过基于提示的智能分析，从代码复杂度到安全漏洞等10个关键维度，提升AI生成代码的质量
- [VictoriaMetrics-Community/mcp-victoriametrics](https://github.com/VictoriaMetrics-Community/mcp-victoriametrics) 🎖️ 🏎️ 🏠 - 与 [VictoriaMetrics API](https://docs.victoriametrics.com/victoriametrics/url-examples/) 和[文档](https://docs.victoriametrics.com/) 完整集成，监控你的 VictoriaMetrics 实例及排查问题。

### 🔎 <a name="search"></a>搜索

- [scrapeless-ai/scrapeless-mcp-server](https://github.com/scrapeless-ai/scrapeless-mcp-server) 🐍 ☁️ - Scrapeless模型上下文协议服务作为MCP服务器连接器，连接到Google SERP API，使得在MCP生态系统内无需离开即可进行网页搜索。
- [@modelcontextprotocol/server-brave-search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) 📇 ☁️ - 使用 Brave 的搜索 API 实现网页搜索功能
- [Dumpling-AI/mcp-server-dumplingai](https://github.com/Dumpling-AI/mcp-server-dumplingai) 🎖️ 📇 ☁️ - 通过 [Dumpling AI](https://www.dumplingai.com/) 提供的数据访问、网页抓取与文档转换 API
- [@angheljf/nyt](https://github.com/angheljf/nyt) 📇 ☁️ - 使用 NYTimes API 搜索文章
- [@modelcontextprotocol/server-fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) 🐍 🏠 ☁️ - 高效获取和处理网页内容，供 AI 使用
- [ac3xx/mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi) 📇 ☁️ - Kagi 搜索 API 集成
- [exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) 🎖️ 📇 ☁️ – 模型上下文协议 (MCP) 服务器让 Claude 等 AI 助手可以使用 Exa AI Search API 进行网络搜索。此设置允许 AI 模型以安全且可控的方式获取实时网络信息。
- [fatwang2/search1api-mcp](https://github.com/fatwang2/search1api-mcp) 📇 ☁️ - 通过 search1api 搜索（需要付费 API 密钥）
- [Tomatio13/mcp-server-tavily](https://github.com/Tomatio13/mcp-server-tavily) ☁️ 🐍 – Tavily AI 搜索 API
- [kshern/mcp-tavily](https://github.com/kshern/mcp-tavily.git) ☁️ 📇 – Tavily AI 搜索 API
- [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) ☁️ 🐍 - 搜索 ArXiv 研究论文
- [mzxrai/mcp-webresearch](https://github.com/mzxrai/mcp-webresearch) 🔍📚 - 在 Google 上搜索并对任何主题进行深度研究
- [andybrandt/mcp-simple-arxiv](https://github.com/andybrandt/mcp-simple-arxiv) - 🐍 ☁️  MCP for LLM 用于搜索和阅读 arXiv 上的论文)
- [andybrandt/mcp-simple-pubmed](https://github.com/andybrandt/mcp-simple-pubmed) - 🐍 ☁️  MCP 用于搜索和阅读 PubMed 中的医学/生命科学论文。
- [apify/mcp-server-rag-web-browser](https://github.com/apify/mcp-server-rag-web-browser) 📇 ☁️ - 一个用于 Apify 的 RAG Web 浏览器 Actor 的 MCP 服务器，可以执行网页搜索、抓取 URL，并以 Markdown 格式返回内容。
- [SecretiveShell/MCP-searxng](https://github.com/SecretiveShell/MCP-searxng) 🐍 🏠 - 用于连接到 searXNG 实例的 MCP 服务器
- [Bigsy/Clojars-MCP-Server](https://github.com/Bigsy/Clojars-MCP-Server) 📇 ☁️ - Clojars MCP 服务器，提供 Clojure 库的最新依赖信息
- [Ihor-Sokoliuk/MCP-SearXNG](https://github.com/ihor-sokoliuk/mcp-searxng) 📇 🏠/☁️ - [SearXNG](https://docs.searxng.org) 的模型上下文协议服务器
- [erithwik/mcp-hn](https://github.com/erithwik/mcp-hn) 🐍 ☁️ - 一个用于搜索 Hacker News、获取热门故事等的 MCP 服务器。
- [chanmeng/google-news-mcp-server](https://github.com/ChanMeng666/server-google-news) 📇 ☁️ - Google News 集成，具有自动主题分类、多语言支持，以及通过 [SerpAPI](https://serpapi.com/) 提供的标题、故事和相关主题的综合搜索功能。
- [hellokaton/unsplash-mcp-server](https://github.com/hellokaton/unsplash-mcp-server)) 🐍 ☁️ - 用于集成 Unsplash 图片搜索功能
- [devflowinc/trieve](https://github.com/devflowinc/trieve/tree/main/clients/mcp-server) 🎖️📇☁️🏠 - 通过 [Trieve](https://trieve.ai) 爬取、嵌入、分块、搜索和检索数据集中的信息
- [nickclyde/duckduckgo-mcp-server](https://github.com/nickclyde/duckduckgo-mcp-server) 🐍 ☁️ - 使用DuckDuckGo进行网络搜索
- [zhsama/duckduckgo-mcp-server](https://github.com/zhsama/duckduckgo-mpc-server/) 📇 🏠 ☁️ - 这是一个基于TypeScript的MCP服务器，提供DuckDuckGo搜索功能。
- [vectorize-io/vectorize-mcp-server](https://github.com/vectorize-io/vectorize-mcp-server/) ☁️ 📇 - [Vectorize](https://vectorize.io) 用于高级检索的MCP服务器，私有Deep Research，任意文件转Markdown提取及文本分块处理。
- [jae-jae/fetcher-mcp](https://github.com/jae-jae/fetcher-mcp) 📇 🏠 - 用于通过Playwright无头浏览器获取网页内容的MCP服务器，支持JavaScript渲染与智能内容提取，并输出Markdown或HTML格式。
- [yamanoku/baseline-mcp-server](https://github.com/yamanoku/baseline-mcp-server) 📇 🏠 - 使用Web平台API查询Baseline状态的MCP服务器

### 🔒 <a name="security"></a>安全

- [firstorderai/authenticator_mcp](https://github.com/firstorderai/authenticator_mcp) 📇 🏠 🍎 🪟 🐧 – 一个安全的 MCP（Model Context Protocol）服务器，使 AI 代理能够与认证器应用程序交互。
- [dnstwist MCP Server](https://github.com/BurtTheCoder/mcp-dnstwist) 📇 🪟 ☁️ - dnstwist 的 MCP 服务器，这是一个强大的 DNS 模糊测试工具，可帮助检测域名抢注、钓鱼和企业窃密行为
- [fosdickio/binary_ninja_mcp](https://github.com/Vector35/binaryninja-mcp) 🐍 🏠 🍎 🪟 🐧 - Binary Ninja 的 MCP 服务器和桥接器。提供二进制分析和逆向工程工具。
- [Maigret MCP Server](https://github.com/BurtTheCoder/mcp-maigret) 📇 🪟 ☁️ - maigret 的 MCP 服务器，maigret 是一款强大的 OSINT 工具，可从各种公共来源收集用户帐户信息。此服务器提供用于在社交网络中搜索用户名和分析 URL 的工具。
- [Shodan MCP Server](https://github.com/BurtTheCoder/mcp-shodan) 📇 🪟 ☁️ - MCP 服务器用于查询 Shodan API 和 Shodan CVEDB。此服务器提供 IP 查找、设备搜索、DNS 查找、漏洞查询、CPE 查找等工具。
- [VirusTotal MCP Server](https://github.com/BurtTheCoder/mcp-virustotal) 📇 🪟 ☁️ - 用于查询 VirusTotal API 的 MCP 服务器。此服务器提供用于扫描 URL、分析文件哈希和检索 IP 地址报告的工具。
- [ORKL MCP Server](https://github.com/fr0gger/MCP_Security) 📇 🛡️ ☁️ - 用于查询 ORKL API 的 MCP 服务器。此服务器提供获取威胁报告、分析威胁行为者和检索威胁情报来源的工具。
- [Security Audit MCP Server](https://github.com/qianniuspace/mcp-security-audit) 📇 🛡️ ☁️ 一个强大的 MCP (模型上下文协议) 服务器，审计 npm 包依赖项的安全漏洞。内置远程 npm 注册表集成，以进行实时安全检查。
- [zoomeye-ai/mcp_zoomeye](https://github.com/zoomeye-ai/mcp_zoomeye) 📇 ☁️ - 使用 ZoomEye API 搜索全球网络空间资产
- [ConechoAI/openai-websearch-mcp](https://github.com/ConechoAI/openai-websearch-mcp/) 🐍 🏠 ☁️ - 将OpenAI内置的`web_search`工具封转成MCP服务器使用.
- [roadwy/cve-search_mcp](https://github.com/roadwy/cve-search_mcp) 🐍 🏠 - CVE-Search MCP服务器， 提供CVE漏洞信息查询、漏洞产品信息查询等功能。

### 🎧 <a name="support-and-service-management"></a>客户支持与服务管理

用于管理客户支持、IT服务管理和服务台操作的工具。

- [effytech/freshdesk-mcp](https://github.com/effytech/freshdesk_mcp) 🐍 ☁️ - 与Freshdesk集成的MCP服务器，使AI模型能够与Freshdesk模块交互并执行各种支持操作。
- [nguyenvanduocit/jira-mcp](https://github.com/nguyenvanduocit/jira-mcp) 🏎️ ☁️ - 一款基于Go语言的Jira MCP连接器，使Claude等AI助手能够与Atlassian Jira交互。该工具为AI模型提供了一个无缝接口，可执行包括问题管理、Sprint计划和工作流转换在内的常见Jira操作。

### 🏃 <a name="sports"></a>体育

体育相关数据、结果和统计信息的访问工具。

- [r-huijts/firstcycling-mcp](https://github.com/r-huijts/firstcycling-mcp) 📇 ☁️ - 通过自然语言访问自行车比赛数据、结果和统计信息。功能包括从 firstcycling.com 获取参赛名单、比赛结果和车手信息。
- [willvelida/mcp-afl-server](https://github.com/willvelida/mcp-afl-server) ☁️ - MMCP 服务器集成了 Squiggle API，提供有关澳大利亚橄榄球联盟球队、排名、比赛结果、预测和实力排名的信息。

### 🌎 <a name="translation-services"></a>翻译服务

AI助手可以通过翻译工具和服务在不同语言之间翻译内容。

- [translated/lara-mcp](https://github.com/translated/lara-mcp) 🎖️ 📇 ☁️ - Lara翻译API的MCP服务器，提供强大的翻译功能，支持语言检测和上下文感知翻译。

### 🚆 <a name="travel-and-transportation"></a>旅行与交通

访问旅行和交通信息。可以查询时刻表、路线和实时旅行数据。

- [Airbnb MCP Server](https://github.com/openbnb-org/mcp-server-airbnb) 📇 ☁️ - 提供搜索Airbnb房源及获取详细信息的工具。
- [NS Travel Information MCP Server](https://github.com/r-huijts/ns-mcp-server) 📇 ☁️ - 了解荷兰铁路 (NS) 的旅行信息、时刻表和实时更新
- [KyrieTangSheng/mcp-server-nationalparks](https://github.com/KyrieTangSheng/mcp-server-nationalparks) 📇 ☁️ - 美国国家公园管理局 API 集成，提供美国国家公园的详细信息、警报、游客中心、露营地和活动的最新信息
- [pab1it0/tripadvisor-mcp](https://github.com/pab1it0/tripadvisor-mcp) 📇 🐍 - 一个MCP服务器，使LLM能够通过标准化的MCP接口与Tripadvisor API交互，支持位置数据、评论和照片

### 🔄 <a name="version-control"></a>版本控制

与 Git 存储库和版本控制平台交互。通过标准化 API 实现存储库管理、代码分析、拉取请求处理、问题跟踪和其他版本控制操作。

- [@modelcontextprotocol/server-github](https://github.com/modelcontextprotocol/servers/tree/main/src/github) 📇 ☁️ - GitHub API集成用于仓库管理、PR、问题等
- [@modelcontextprotocol/server-gitlab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab) 📇 ☁️ 🏠 - GitLab平台集成用于项目管理和CI/CD操作
- [@oschina/mcp-gitee](https://github.com/oschina/gitee) 🏎️ ☁️ 🏠 - Gitee API集成、仓库、问题及拉取请求管理等功能。
- [@modelcontextprotocol/server-git](https://github.com/modelcontextprotocol/servers/tree/main/src/git) 🐍 🏠 - 直接的Git仓库操作，包括读取、搜索和分析本地仓库
- [Tiberriver256/mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops) 📇 ☁️ - Azure DevOps 集成，用于管理存储库、工作项目和管道
- [adhikasp/mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest) 🐍 🏠 - 使用 LLM 阅读和分析 GitHub 存储库
- [kopfrechner/gitlab-mr-mcp](https://github.com/kopfrechner/gitlab-mr-mcp) 📇 ☁️ - 与 GitLab 项目问题和合并请求无缝互动。
- [kaiyuanxiaobing/atomgit-mcp-server](https://github.com/kaiyuanxiaobing/atomgit-mcp-server) 📇 ☁️ - AtomGit API 集成用于仓库管理、问题、拉取请求等功能。

### 🛠️ <a name="other-tools-and-integrations"></a>其他工具和集成

- [apify/actors-mcp-server](https://github.com/apify/actors-mcp-server) 📇 ☁️ - 使用超过 3,000 个预构建的云工具（称为 Actors）从网站、电商、社交媒体、搜索引擎、地图等提取数据。
- [githejie/mcp-server-calculator](https://github.com/githejie/mcp-server-calculator) 🐍 🏠 - 使LLM能够使用计算器进行精确的数值计算
- [ivo-toby/contentful-mcp](https://github.com/ivo-toby/contentful-mcp) 📇 🏠 - 更新、创建、删除 Contentful Space 中的内容、内容模型和资产
- [mzxrai/mcp-openai](https://github.com/mzxrai/mcp-openai) 📇 ☁️ - 与 OpenAI 最智能的模型聊天
- [mrjoshuak/godoc-mcp](https://github.com/mrjoshuak/godoc-mcp) 🏎️ 🏠 - 高效的 Go 文档服务器，让 AI 助手可以智能访问包文档和类型，而无需阅读整个源文件
- [pierrebrunelle/mcp-server-openai](https://github.com/pierrebrunelle/mcp-server-openai) 🐍 ☁️ - 直接从Claude查询OpenAI模型，使用MCP协议
- [@modelcontextprotocol/server-everything](https://github.com/modelcontextprotocol/servers/tree/main/src/everything) 📇 🏠 - MCP服务器，涵盖MCP协议的所有功能
- [baba786/phabricator-mcp-server](https://github.com/baba786/phabricator-mcp-server) 🐍 ☁️ - 与Phabricator API交互
- [MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) 🐍 ☁️ 🏠 - 通过REST API与Obsidian交互
- [calclavia/mcp-obsidian](https://github.com/calclavia/mcp-obsidian) 📇 🏠 - 这是一个连接器，允许Claude Desktop（或任何MCP兼容应用程序）读取和搜索包含Markdown笔记的目录（如Obsidian库）。
- [anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube) 📇 ☁️ - 获取YouTube字幕
- [danhilse/notion_mcp](https://github.com/danhilse/notion_mcp) 🐍 ☁️ - 与Notion API集成，管理个人待办事项列表
- [rusiaaman/wcgw](https://github.com/rusiaaman/wcgw/blob/main/src/wcgw/client/mcp_server/Readme.md) 🐍 🏠 - 自动化shell执行、计算机控制和编码代理。（Mac）
- [reeeeemo/ancestry-mcp](https://github.com/reeeeemo/ancestry-mcp) 🐍 🏠 - 允许AI读取.ged文件和基因数据
- [sirmews/apple-notes-mcp](https://github.com/sirmews/apple-notes-mcp) 🐍 🏠 - 允许AI读取本地Apple Notes数据库（仅限macOS）
- [anjor/coinmarket-mcp-server](https://github.com/anjor/coinmarket-mcp-server) 🐍 🏠 - Coinmarket API集成，用于获取加密货币列表和报价
- [suekou/mcp-notion-server](https://github.com/suekou/mcp-notion-server) 📇 🏠 - 与Notion API交互
- [amidabuddha/unichat-mcp-server](https://github.com/amidabuddha/unichat-mcp-server) 🐍/📇 ☁️ - 使用MCP协议通过工具或预定义的提示发送请求给OpenAI、MistralAI、Anthropic、xAI或Google AI。需要供应商API密钥
- [evalstate/mcp-miro](https://github.com/evalstate/mcp-miro) 📇 ☁️ - 访问 MIRO 白板，批量创建和读取项目。需要 REST API 的 OAUTH 密钥。
- [@tacticlaunch/mcp-linear](https://github.com/tacticlaunch/mcp-linear) 📇 ☁️ 🍎 🪟 🐧 - 与Linear项目管理系统集成
- [KS-GEN-AI/jira-mcp-server](https://github.com/KS-GEN-AI/jira-mcp-server) 📇 ☁️ 🍎 🪟 - 通过 JQL 和 API 读取 Jira 数据，并执行创建和编辑工单的请求
- [KS-GEN-AI/confluence-mcp-server](https://github.com/KS-GEN-AI/confluence-mcp-server) 📇 ☁️ 🍎 🪟 - 通过 CQL 获取 Confluence 数据并阅读页面
- [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) 🐍 ☁️ - Confluence工作区的自然语言搜索和内容访问
- [pyroprompts/any-chat-completions-mcp](https://github.com/pyroprompts/any-chat-completions-mcp) - 与任何其他OpenAI SDK兼容的聊天完成API对话，例如Perplexity、Groq、xAI等
- [anaisbetts/mcp-installer](https://github.com/anaisbetts/mcp-installer) 🐍 🏠 -  一个MCP服务器，可以为您安装其他MCP服务器
- [tanigami/mcp-server-perplexity](https://github.com/tanigami/mcp-server-perplexity) 🐍 ☁️ - 与 Perplexity API 交互。
- [future-audiences/wikimedia-enterprise-model-context-protocol](https://gitlab.wikimedia.org/repos/future-audiences/wikimedia-enterprise-model-context-protocol) 🐍 ☁️  - 维基百科文章查找 API
- [andybrandt/mcp-simple-timeserver](https://github.com/andybrandt/mcp-simple-timeserver) 🐍 🏠☁️ - MCP 服务器允许检查客户端计算机上的本地时间或 NTP 服务器上的当前 UTC 时间
- [andybrandt/mcp-simple-openai-assistant](https://github.com/andybrandt/mcp-simple-openai-assistant) - 🐍 ☁️  MCP 与 OpenAI 助手对话（Claude 可以使用任何 GPT 模型作为他的助手）
- [@evalstate/mcp-hfspace](https://github.com/evalstate/mcp-hfspace) 📇 ☁️ - 直接从 Claude 使用 HuggingFace Spaces。使用开源图像生成、聊天、视觉任务等。支持图像、音频和文本上传/下载。
- [zueai/mcp-manager](https://github.com/zueai/mcp-manager) 📇 ☁️ - 简单的 Web UI 用于安装和管理 Claude 桌面应用程序的 MCP 服务器。
- [wong2/mcp-cli](https://github.com/wong2/mcp-cli) 📇 🏠 - 用于测试 MCP 服务器的 CLI 工具
- [isaacwasserman/mcp-vegalite-server](https://github.com/isaacwasserman/mcp-vegalite-server) 🐍 🏠 - 使用 VegaLite 格式和渲染器从获取的数据生成可视化效果。
- [tevonsb/homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp) 📇 🏠 - 访问家庭助理数据和控制设备（灯、开关、恒温器等）。
- [allenporter/mcp-server-home-assistant](https://github.com/allenporter/mcp-server-home-assistant) 🐍 🏠 - 通过模型上下文协议服务器暴露所有 Home Assistant 语音意图，实现智能家居控制
- [@magarcia/mcp-server-giphy](https://github.com/magarcia/mcp-server-giphy) 📇 ☁️ - 通过Giphy API从庞大的Giphy图库中搜索并获取GIF动图。
- [nguyenvanduocit/all-in-one-model-context-protocol](https://github.com/nguyenvanduocit/all-in-one-model-context-protocol) 🏎️ 🏠 - 一些对开发者有用的工具，几乎涵盖工程师所需的一切：Confluence、Jira、YouTube、运行脚本、知识库RAG、抓取URL、管理YouTube频道、电子邮件、日历、GitLab
- [@joshuarileydev/mac-apps-launcher-mcp-server](https://github.com/JoshuaRileyDev/mac-apps-launcher) 📇 🏠 - 用于列出和启动 MacOS 上的应用程序的 MCP 服务器
- [ZeparHyfar/mcp-datetime](https://github.com/ZeparHyfar/mcp-datetime) - MCP 服务器提供多种格式的日期和时间函数
- [SecretiveShell/MCP-wolfram-alpha](https://github.com/SecretiveShell/MCP-wolfram-alpha) 🐍 ☁️ - 用于查询Wolfram Alpha API的MCP服务器。
- [apinetwork/piapi-mcp-server](https://github.com/apinetwork/piapi-mcp-server) 📇 ☁️ PiAPI MCP服务器使用户能够直接从Claude或其他MCP兼容应用程序中使用Midjourney/Flux/Kling/Hunyuan/Udio/Trellis生成媒体内容。
- [gotoolkits/DifyWorkflow](https://github.com/gotoolkits/mcp-difyworkflow-server) - 🏎️ ☁️ MCP 服务器 Tools 实现查询与执行 Dify AI 平台上自定义的工作流
- [@pskill9/hn-server](https://github.com/pskill9/hn-server) - 📇 ☁️ 解析 news.ycombinator.com（Hacker News）的 HTML 内容，为不同类型的故事（热门、最新、问答、展示、工作）提供结构化数据
- [@mediar-ai/screenpipe](https://github.com/mediar-ai/screenpipe) - 🎖️ 🦀 🏠 🍎 本地优先的系统，支持屏幕/音频捕获并带有时间戳索引、SQL/嵌入存储、语义搜索、LLM 驱动的历史分析和事件触发动作 - 通过 NextJS 插件生态系统实现构建上下文感知的 AI 代理
- [akseyh/bear-mcp-server](https://github.com/akseyh/bear-mcp-server) - 允许 AI 读取您的 Bear Notes（仅支持 macOS）
- [mcp-server-jfx](https://github.com/quarkiverse/quarkus-mcp-servers/tree/main/jfx) ☕ 🏠 - 在JavaFX画布上绘制。
- [hmk/attio-mcp-server](https://github.com/hmk/attio-mcp-server) - 📇 ☁️ 允许AI客户端在Attio CRM中管理记录和笔记
- [roychri/mcp-server-asana](https://github.com/roychri/mcp-server-asana) - 📇 ☁️ 这个Asana的模型上下文协议（MCP）服务器实现允许你通过MCP客户端（如Anthropic的Claude桌面应用等）与Asana API进行交互。
- [ws-mcp](https://github.com/nick1udwig/ws-mcp) - 使用 WebSocket 包装 MCP 服务器（用于 [kitbitz](https://github.com/nick1udwig/kibitz)）
- [AbdelStark/bitcoin-mcp](https://github.com/AbdelStark/bitcoin-mcp) - ₿ 一个模型上下文协议（MCP）服务器，使 AI 模型能够与比特币交互，允许它们生成密钥、验证地址、解码交易、查询区块链等
- [louiscklaw/hko-mcp](https://github.com/louiscklaw/hko-mcp) 📇 🏠 - 一个 MCP 服务器，演示如何从香港天文台获取天气数据
- [tomekkorbak/strava-mcp-server](https://github.com/tomekkorbak/strava-mcp-server) 🐍 ☁️ - An MCP server for Strava, an app for tracking physical exercise
- [tomekkorbak/oura-mcp-server](https://github.com/tomekkorbak/oura-mcp-server) 🐍 ☁️ - An MCP server for Oura, an app for tracking sleep
- [rember/rember-mcp](https://github.com/rember/rember-mcp) 📇 🏠 - Create spaced repetition flashcards in [Rember](https://rember.com) to remember anything you learn in your chats.
- [hiromitsusasaki/raindrop-io-mcp-server](https://github.com/hiromitsusasaki/raindrop-io-mcp-server) 📇 ☁️ - An integration that allows LLMs to interact with Raindrop.io bookmarks using the Model Context Protocol (MCP).
- [@integromat/make-mcp-server](https://github.com/integromat/make-mcp-server) 🎖️ 📇 🏠 - Turn your [Make](https://www.make.com/) scenarios into callable tools for AI assistants.
- [NON906/omniparser-autogui-mcp](https://github.com/NON906/omniparser-autogui-mcp) - 🐍 Automatic operation of on-screen GUI.
- [kj455/mcp-kibela](https://github.com/kj455/mcp-kibela) - 📇 ☁️ [Kibela](https://kibe.la/) 与 MCP 的集成
- [blurrah/mcp-graphql](https://github.com/blurrah/mcp-graphql) 📇 ☁️ - Allows the AI to query GraphQL servers
- [fotoetienne/gqai](https://github.com/fotoetienne/gqai) 🏎 🏠 - 使用常规 GraphQL 查询/变异定义工具，gqai 会自动为您生成 MCP 服务器。
- [@awkoy/replicate-flux-mcp](https://github.com/awkoy/replicate-flux-mcp) 📇 ☁️ - 通过Replicate API提供图像生成功能。
- [kenliao94/mcp-server-rabbitmq](https://github.com/kenliao94/mcp-server-rabbitmq) 🐍 🏠 - Enable interaction (admin operation, message enqueue/dequeue) with RabbitMQ
- [marcelmarais/Spotify](https://github.com/marcelmarais/spotify-mcp-server) - 📇 🏠 Control Spotify playback and manage playlists.
- [NakaokaRei/swift-mcp-gui](https://github.com/NakaokaRei/swift-mcp-gui.git) 🏠 🍎 - MCP服务器，可以执行键盘输入、鼠标移动等命令
- [awwaiid/mcp-server-taskwarrior](https://github.com/awwaiid/mcp-server-taskwarrior) 🏠 📇 - An MCP server for basic local taskwarrior usage (add, update, remove tasks)
- [kelvin6365/plane-mcp-server](https://github.com/kelvin6365/plane-mcp-server) - 🏎️ 🏠 此 MCP 伺服器將協助您透過 [Plane 的](https://plane.so) API 管理專案和問題
- [yuna0x0/hackmd-mcp](https://github.com/yuna0x0/hackmd-mcp) 📇 ☁️ - 允许 AI 模型与 [HackMD](https://hackmd.io) 交互
- [pwh-pwh/cal-mcp](https://github.com/pwh-pwh/cal-mcp) - MCP服务器，可以计算数学表达式
- [HenryHaoson/Yuque-MCP-Server](https://github.com/HenryHaoson/Yuque-MCP-Server) - 📇 ☁️ 用于与语雀API集成的Model-Context-Protocol (MCP)服务器，允许AI模型管理文档、与知识库交互、搜索内容以及访问语雀平台的统计数据。
- [tumf/web3-mcp](https://github.com/tumf/web3-mcp) 🐍 ☁️ - 包装Ankr Advanced API的MCP服务器实现。可以访问以太坊、BSC、Polygon、Avalanche等多条区块链上的NFT、代币和区块链数据。
- [ttommyth/interactive-mcp](https://github.com/ttommyth/interactive-mcp) 📇 🏠 🍎 🪟 🐧 - 通过在 MCP 循环中直接添加本地用户提示和聊天功能，启用交互式 LLM 工作流程。
- [caol64/wenyan-mcp](https://github.com/caol64/wenyan-mcp) 📇 🏠 🍎 🪟 🐧 - 文颜 MCP Server， 让 AI 将 Markdown 文章自动排版后发布至微信公众号。

## 框架

- [FastMCP](https://github.com/jlowin/fastmcp) 🐍 - 用于在 Python 中构建 MCP 服务器的高级框架
- [FastMCP](https://github.com/punkpeye/fastmcp) 📇 - 用于在 TypeScript 中构建 MCP 服务器的高级框架
- [Foxy Contexts](https://github.com/strowk/foxy-contexts) 🏎️ - 用于以声明方式编写 MCP 服务器的 Golang 库，包含功能测试
- [Genkit MCP](https://github.com/firebase/genkit/tree/main/js/plugins/mcp) 📇 – 提供[Genkit](https://github.com/firebase/genkit/tree/main)与模型上下文协议（MCP）之间的集成。
- [LiteMCP](https://github.com/wong2/litemcp) 📇 - 用于在 JavaScript/TypeScript 中构建 MCP 服务器的高级框架
- [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go) 🏎️ - 用于构建MCP服务器和客户端的Golang SDK。
- [mcp-framework](https://github.com/QuantGeekDev/mcp-framework) - 📇 用于构建 MCP 服务器的快速而优雅的 TypeScript 框架
- [mcp-proxy](https://github.com/punkpeye/mcp-proxy) 📇 - 用于使用 `stdio` 传输的 MCP 服务器的 TypeScript SSE 代理
- [mcp-rs-template](https://github.com/linux-china/mcp-rs-template) 🦀 - Rust的MCP CLI服务器模板
- [metoro-io/mcp-golang](https://github.com/metoro-io/mcp-golang) 🏎️ - 用于构建 MCP 服务器的 Golang 框架，专注于类型安全。
- [rectalogic/langchain-mcp](https://github.com/rectalogic/langchain-mcp) 🐍 - 提供LangChain中MCP工具调用支持，允许将MCP工具集成到LangChain工作流中。
- [salty-flower/ModelContextProtocol.NET](https://github.com/salty-flower/ModelContextProtocol.NET) #️⃣🏠 - 基于 .NET 9 的 C# MCP 服务器 SDK ，支持 NativeAOT ⚡ 🔌
- [spring-ai-mcp](https://github.com/spring-projects-experimental/spring-ai-mcp) ☕ 🌱 - 用于构建 MCP 客户端和服务器的 Java SDK 和 Spring Framework 集成，支持多种可插拔的传输选项
- [@marimo-team/codemirror-mcp](https://github.com/marimo-team/codemirror-mcp) - CodeMirror 扩展，实现了用于资源提及和提示命令的模型上下文协议 (MCP)
- [quarkiverse/quarkus-mcp-server](https://github.com/quarkiverse/quarkus-mcp-server) ☕ - 用于基于Quarkus构建MCP服务器的Java SDK。
- [lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent) 🤖 🔌 - 使用简单、可组合的模式，通过MCP服务器构建高效的代理。
- [mullerhai/sakura-mcp](https://github.com/mullerhai/sakura-mcp) 🦀 ☕ - Scala MCP 框架 构建企业级MCP客户端和服务端 shade from modelcontextprotocol.io.

## 实用工具

- [boilingdata/mcp-server-and-gw](https://github.com/boilingdata/mcp-server-and-gw) 📇 - 带有示例服务器和 MCP 客户端的 MCP stdio 到 HTTP SSE 传输网关
- [isaacwasserman/mcp-langchain-ts-client](https://github.com/isaacwasserman/mcp-langchain-ts-client) 📇 - 在 LangChain.js 中使用 MCP 提供的工具
- [lightconetech/mcp-gateway](https://github.com/lightconetech/mcp-gateway) 📇 - MCP SSE 服务器的网关演示
- [mark3labs/mcphost](https://github.com/mark3labs/mcphost) 🏎️ - 一个 CLI 主机应用程序，使大型语言模型 (LLM) 能够通过模型上下文协议 (MCP) 与外部工具交互
- [MCP-Connect](https://github.com/EvalsOne/MCP-Connect) 📇 - 一个小工具，使基于云的 AI 服务能够通过 HTTP/HTTPS 请求访问本地的基于 Stdio 的 MCP 服务器
- [SecretiveShell/MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge) 🐍 - OpenAI 中间件代理，用于在任何现有的 OpenAI 兼容客户端中使用 MCP
- [sparfenyuk/mcp-proxy](https://github.com/sparfenyuk/mcp-proxy) 🐍 - MCP stdio 到 SSE 的传输网关
- [upsonic/gpt-computer-assistant](https://github.com/Upsonic/gpt-computer-assistant) 🐍 - 用于构建垂直 AI 代理的框架
- [kukapay/whereami-mcp](https://github.com/kukapay/whereami-mcp) 🐍 ☁️ -  一款轻量级MCP服务器，能根据您当前的IP准确定位您所在的位置。
- [kukapay/whattimeisit-mcp](https://github.com/kukapay/whattimeisit-mcp) 🐍 ☁️ - 一款轻量级的MCP服务器，能准确告诉你当前时间。
- [kukapay/whoami-mcp](https://github.com/kukapay/whoami-mcp) 🐍 🏠 - 一款轻量级MCP服务器，能准确告诉你你的身份。
- [flux159/mcp-chat](https://github.com/flux159/mcp-chat) 📇🖥️ - 基于命令行的客户端，用于与任何MCP服务器进行聊天和连接。在MCP服务器的开发与测试阶段非常实用。
- [TBXark/mcp-proxy](https://github.com/TBXark/mcp-proxy) 🏎️ - 一个通过单个HTTP服务器聚合并服务多个MCP资源服务器的MCP代理服务器。

## 提示和技巧

### 官方提示关于 LLM 如何使用 MCP

想让 Claude 回答有关模型上下文协议的问题？

创建一个项目，然后将此文件添加到其中：

https://modelcontextprotocol.io/llms-full.txt

这样 Claude 就能回答关于编写 MCP 服务器及其工作原理的问题了

- https://www.reddit.com/r/ClaudeAI/comments/1h3g01r/want_to_ask_claude_about_model_context_protocol/

## 收藏历史

<a href="https://star-history.com/#punkpeye/awesome-mcp-servers&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date" />
 </picture>
</a>
