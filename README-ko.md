# Awesome MCP Servers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![繁體中文](https://img.shields.io/badge/繁體中文-點擊查看-orange)](README-zh_TW.md)
[![简体中文](https://img.shields.io/badge/简体中文-点击查看-orange)](README-zh.md)
[![日本語](https://img.shields.io/badge/日本語-クリック-青)](README-ja.md)
[![한국어](https://img.shields.io/badge/한국어-클릭-yellow)](README-ko.md)
[![Português Brasileiro](https://img.shields.io/badge/Português_Brasileiro-Clique-green)](README-pt_BR.md)
[![Discord](https://img.shields.io/discord/1312302100125843476?logo=discord&label=discord)](https://glama.ai/mcp/discord)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/mcp?style=flat&logo=reddit&label=subreddit)](https://www.reddit.com/r/mcp/)

# 모델 컨텍스트 프로토콜 (MCP) 서버 엄선 목록

* [MCP란 무엇인가?](#mcp란-무엇인가)
* [클라이언트](#클라이언트)
* [튜토리얼](#튜토리얼)
* [서버 구현](#서버-구현)
* [프레임워크](#프레임워크)
* [유틸리티](#유틸리티)
* [팁과 요령](#팁과-요령)
* [스타 히스토리](#스타-히스토리)

## MCP란 무엇인가?

[MCP](https://modelcontextprotocol.io/)는 AI 모델이 표준화된 서버 구현을 통해 로컬 및 원격 리소스와 안전하게 상호 작용할 수 있도록 하는 개방형 프로토콜입니다. 이 목록은 파일 접근, 데이터베이스 연결, API 통합 및 기타 컨텍스트 서비스를 통해 AI 기능을 확장하는 프로덕션 준비 및 실험적 MCP 서버에 중점을 둡니다.

## 클라이언트

[awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients/) 및 [glama.ai/mcp/clients](https://glama.ai/mcp/clients)를 확인하세요.

> [!팁]
> [Glama Chat](https://glama.ai/chat)은 MCP 지원 및 [AI 게이트웨이](https://glama.ai/gateway)를 갖춘 멀티모달 AI 클라이언트입니다.

## 튜토리얼

* [모델 컨텍스트 프로토콜 (MCP) 빠른 시작](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
* [SQLite 데이터베이스를 사용하도록 Claude 데스크톱 앱 설정하기](https://youtu.be/wxCCzo9dGj0)

## 커뮤니티

* [r/mcp 레딧](https://www.reddit.com/r/mcp)
* [디스코드 서버](https://glama.ai/mcp/discord)

## 범례

* 🎖️ – 공식 구현
* 프로그래밍 언어
  * 🐍 – 파이썬 코드베이스
  * 📇 – 타입스크립트 코드베이스
  * 🏎️ – Go 코드베이스
  * 🦀 – Rust 코드베이스
  * #️⃣ - C# 코드베이스
  * ☕ - Java 코드베이스
* 범위
  * ☁️ - 클라우드 서비스
  * 🏠 - 로컬 서비스
* 운영체제
  * 🍎 – macOS용
  * 🪟 – Windows용
  * 🐧 - Linux용

> [!참고]
> 로컬 🏠 vs 클라우드 ☁️ 가 헷갈리시나요?
> * MCP 서버가 로컬에 설치된 소프트웨어와 통신할 때 로컬을 사용하세요 (예: Chrome 브라우저 제어).
> * MCP 서버가 원격 API와 통신할 때 네트워크(클라우드)를 사용하세요 (예: 날씨 API).

## 서버 구현

> [!참고]
> 이제 리포지토리와 동기화되는 [웹 기반 디렉토리](https://glama.ai/mcp/servers)가 있습니다.

* 🔗 - [Aggregators](#aggregators)
* 📂 - [브라우저 자동화](#browser-automation)
* 🎨 - [예술 및 문화](#art-and-culture)
* ☁️ - [클라우드 플랫폼](#cloud-platforms)
* 🖥️ - [커맨드 라인](#command-line)
* 💬 - [커뮤니케이션](#communication)
* 👤 - [고객 데이터 플랫폼](#customer-data-platforms)
* 🗄️ - [데이터베이스](#databases)
* 📊 - [데이터 플랫폼](#data-platforms)
* 🛠️ - [개발자 도구](#developer-tools)
* 📂 - [파일 시스템](#file-systems)
* 💰 - [금융 및 핀테크](#finance--fintech)
* 🎮 - [게임](#gaming)
* 🧠 - [지식 및 메모리](#knowledge--memory)
* 🗺️ - [위치 서비스](#location-services)
* 🎯 - [마케팅](#marketing)
* 📊 - [모니터링](#monitoring)
* 🔎 - [검색](#search)
* 🔒 - [보안](#security)
* 🏃 - [스포츠](#sports)
* 🌎 - [번역 서비스](#translation-services)
* 🚆 - [여행 및 교통](#travel-and-transportation)
* 🔄 - [버전 관리](#version-control)
* 🛠️ - [기타 도구 및 통합](#other-tools-and-integrations)

### 🔗 <a name="aggregators"></a>애그리게이터

단일 MCP 서버를 통해 많은 앱과 도구에 접근하기 위한 서버입니다.

- [OpenMCP](https://github.com/wegotdocs/open-mcp) 📇 🏠 🍎 🪟 🐧 - 웹 API를 10초 만에 MCP 서버로 전환하고 오픈 소스 레지스트리에 추가하세요: https://open-mcp.org
- [tigranbs/mcgravity](https://github.com/krayniok/mcgravity) 📇 🏠 🪟 🐧 - 여러 MCP 서버를 단일 연결 포인트로 통합하여 프록시하는 도구로, 요청 부하를 분산하여 AI 도구를 확장합니다.
- [MetaMCP](https://github.com/metatool-ai/metatool-app) 📇 ☁️ 🏠 🍎 🪟 🐧 - MetaMCP는 GUI를 통해 MCP 연결을 관리하는 통합 미들웨어 MCP 서버입니다.
- [MCP Access Point](https://github.com/sxhxliang/mcp-access-point)  📇 ☁️ 🏠 🍎 🪟 🐧 - 서버 측 코드를 변경하지 않고 한 번의 클릭으로 웹 API를 MCP 서버로 변환합니다.
- [hamflx/imagen3-mcp](https://github.com/hamflx/imagen3-mcp) 📇 🏠 🪟 🍎 🐧 - MCP를 통해 Google의 Imagen 3.0 API를 사용하는 강력한 이미지 생성 도구. 고급 사진, 예술 및 사실적인 컨트롤로 텍스트 프롬프트에서 고품질 이미지를 생성합니다.

### 📂 <a name="browser-automation"></a>브라우저 자동화

웹 콘텐츠 접근 및 자동화 기능. AI 친화적인 형식으로 웹 콘텐츠 검색, 스크래핑 및 처리를 가능하게 합니다.
- [@blackwhite084/playwright-plus-python-mcp](https://github.com/blackwhite084/playwright-plus-python-mcp) 🌐 - Playwright를 사용한 브라우저 자동화를 위한 MCP 파이썬 서버, llm에 더 적합
- [@executeautomation/playwright-mcp-server](https://github.com/executeautomation/mcp-playwright) 🌐⚡️ - 브라우저 자동화 및 웹 스크래핑을 위해 Playwright를 사용하는 MCP 서버
- [@automatalabs/mcp-server-playwright](https://github.com/Automata-Labs-team/MCP-Server-Playwright) 🌐 🖱️ - Playwright를 사용한 브라우저 자동화를 위한 MCP 서버
- [@modelcontextprotocol/server-puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) 📇 🏠 - 웹 스크래핑 및 상호 작용을 위한 브라우저 자동화
- [@kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) 📇 ☁️ - AI 분석을 위해 YouTube 자막 및 스크립트 가져오기
- [@recursechat/mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts) 📇 🏠 🍎 - Apple Shortcuts와의 MCP 서버 통합
- [@kimtth/mcp-aoai-web-Browse](https://github.com/kimtth/mcp-aoai-web-Browse) 🐍 🏠 - Azure OpenAI 및 Playwright를 사용하는 `최소한의` 서버/클라이언트 MCP 구현
- [@pskill9/web-search](https://github.com/pskill9/web-search) 📇 🏠 - API 키 없이 Google 검색 결과를 사용하여 무료 웹 검색을 가능하게 하는 MCP 서버
- [@co-browser/browser-use-mcp-server](https://github.com/co-browser/browser-use-mcp-server) 🌐🔮 - SSE 전송을 지원하는 MCP 서버로 패키징된 browser-use. Docker에서 Chromium을 실행하기 위한 Dockerfile + VNC 서버 포함.
- [@34892002/bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js) 📇 🏠 - Bilibili 콘텐츠 검색을 지원하는 MCP 서버. LangChain 통합 예제 및 테스트 스크립트 제공.
- [@getrupt/ashra-mcp](https://github.com/getrupt/ashra-mcp) 🐍 🏠 - 모든 웹사이트에서 구조화된 데이터 추출. 프롬프트만 입력하면 JSON 획득.
- [aircodelabs/grasp](https://github.com/aircodelabs/grasp) 📇 🏠 - MCP 및 A2A를 기본 지원하는 에이전트 기반의 자체 호스팅 브라우저

### 🎨 <a name="art-and-culture"></a>예술 및 문화

예술 컬렉션, 문화 유산 및 박물관 데이터베이스에 접근하고 탐색합니다. AI 모델이 예술 및 문화 콘텐츠를 검색하고 분석할 수 있게 합니다.

- [cantian-ai/bazi-mcp](https://github.com/cantian-ai/bazi-mcp) 📇 🏠 ☁️ 🍎 🪟 - 포괄적이고 정확한 사주팔자(八字) 분석과 해석 제공
- [burningion/video-editing-mcp](https://github.com/burningion/video-editing-mcp) 📹🎬 - Video Jungle 컬렉션에서 비디오 편집 추가, 분석, 검색 및 생성
- [r-huijts/rijksmuseum-mcp](https://github.com/r-huijts/rijksmuseum-mcp) 📇 ☁️ - 작품 검색, 세부 정보 및 컬렉션을 위한 Rijksmuseum API 통합
- [yuna0x0/anilist-mcp](https://github.com/yuna0x0/anilist-mcp) 📇 ☁️ - 애니메이션 및 만화 정보를 위한 AniList API를 통합하는 MCP 서버

### ☁️ <a name="cloud-platforms"></a>클라우드 플랫폼

클라우드 플랫폼 서비스 통합. 클라우드 인프라 및 서비스의 관리 및 상호 작용을 가능하게 합니다.

- [qiniu/qiniu-mcp-server](https://github.com/qiniu/qiniu-mcp-server) 🐍 ☁️ - 치니우안(七牛云) 제품으로 구축된 MCP는 치니우안 스토리지, 지능형 멀티미디어 서비스 등에 접근할 수 있습니다.
- [Cloudflare MCP 서버](https://github.com/cloudflare/mcp-server-cloudflare) 🎖️ 📇 ☁️ - Workers, KV, R2 및 D1을 포함한 Cloudflare 서비스와의 통합
- [alexbakers/mcp-ipfs](https://github.com/alexbakers/mcp-ipfs) 📇 ☁️ - IPFS 스토리지 업로드 및 조작
- [alexei-led/aws-mcp-server](https://github.com/alexei-led/aws-mcp-server) 🐍 ☁️ - AI 어시스턴트가 AWS CLI 명령을 실행하고, 유닉스 파이프를 사용하며, 안전한 Docker 환경에서 일반적인 AWS 작업을 위한 프롬프트 템플릿을 멀티 아키텍처 지원으로 적용할 수 있게 하는 가볍지만 강력한 서버
- [aliyun/alibaba-cloud-ops-mcp-server](https://github.com/aliyun/alibaba-cloud-ops-mcp-server) 🎖️ 🐍 ☁️ - 알리바바 클라우드에서 AI 어시스턴트가 리소스를 운영하고 관리할 수 있게 해주는 MCP 서버로, ECS, 클라우드 모니터링, OOS 및 기타 널리 사용되는 클라우드 제품들을 지원합니다.
- [Kubernetes MCP 서버](https://github.com/strowk/mcp-k8s-go) - 🏎️ ☁️/🏠 MCP를 통한 쿠버네티스 클러스터 운영
- [@flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) - 📇 ☁️/🏠 파드, 디플로이먼트, 서비스를 위한 쿠버네티스 클러스터 운영의 타입스크립트 구현
- [@manusa/Kubernetes MCP 서버](https://github.com/manusa/kubernetes-mcp-server) - 🏎️ 🏠 OpenShift를 추가로 지원하는 강력한 쿠버네티스 MCP 서버. **모든** 쿠버네티스 리소스에 대한 CRUD 작업을 제공하는 것 외에도, 이 서버는 클러스터와 상호 작용하기 위한 전문 도구를 제공합니다.
- [wenhuwang/mcp-k8s-eye](https://github.com/wenhuwang/mcp-k8s-eye) 🏎️ ☁️/🏠 쿠버네티스 관리 및 클러스터, 애플리케이션 상태 분석을 위한 MCP 서버
- [johnneerdael/netskope-mcp](https://github.com/johnneerdael/netskope-mcp) 🔒 ☁️ - Netskope Private Access 환경 내의 모든 Netskope Private Access 구성 요소에 대한 접근을 제공하는 MCP. 자세한 설정 정보와 사용법에 대한 LLM 예제 포함.
- [nwiizo/tfmcp](https://github.com/nwiizo/tfmcp) - 🦀 🏠 - AI 어시스턴트가 Terraform 환경을 관리하고 운영할 수 있게 하는 Terraform MCP 서버. 구성 읽기, 계획 분석, 구성 적용 및 Terraform 상태 관리를 가능하게 합니다.
- [silenceper/mcp-k8s](https://github.com/silenceper/mcp-k8s) 🏎️ ☁️/🏠 MCP-K8S는 AI 기반 Kubernetes 리소스 관리 도구로, 자연어 상호작용을 통해 사용자가 Kubernetes 클러스터의 모든 리소스(네이티브 리소스(예: Deployment, Service) 및 사용자 정의 리소스(CRD) 포함)를 운영할 수 있게 합니다. 복잡한 명령어를 외울 필요 없이 요구사항만 설명하면 AI가 해당 클러스터 작업을 정확하게 실행하여 Kubernetes의 사용성을 크게 향상시킵니다.

### 🖥️ <a name="command-line"></a>커맨드 라인

명령을 실행하고, 출력을 캡처하며, 셸 및 커맨드 라인 도구와 상호 작용합니다.

- [ferrislucas/iterm-mcp](https://github.com/ferrislucas/iterm-mcp) 🖥️ 🛠️ 💬 - iTerm에 대한 접근을 제공하는 모델 컨텍스트 프로토콜 서버. 명령을 실행하고 iTerm 터미널에서 보이는 내용에 대해 질문할 수 있습니다.
- [g0t4/mcp-server-commands](https://github.com/g0t4/mcp-server-commands) 📇 🏠 - `run_command` 및 `run_script` 도구를 사용하여 모든 명령 실행.
- [MladenSU/cli-mcp-server](https://github.com/MladenSU/cli-mcp-server) 🐍 🏠 - 안전한 실행 및 사용자 정의 가능한 보안 정책을 갖춘 커맨드 라인 인터페이스
- [tumf/mcp-shell-server](https://github.com/tumf/mcp-shell-server) 모델 컨텍스트 프로토콜(MCP)을 구현하는 안전한 셸 명령 실행 서버

### 💬 <a name="communication"></a>커뮤니케이션

메시지 관리 및 채널 운영을 위한 커뮤니케이션 플랫폼과의 통합. AI 모델이 팀 커뮤니케이션 도구와 상호 작용할 수 있게 합니다.

- [zcaceres/gtasks-mcp](https://github.com/zcaceres/gtasks-mcp) - 📇 ☁️ - Google Tasks를 관리하기 위한 MCP 서버
- [hannesrudolph/imessage-query-fastmcp-mcp-server](https://github.com/hannesrudolph/imessage-query-fastmcp-mcp-server) 🐍 🏠 🍎 - 모델 컨텍스트 프로토콜(MCP)을 통해 iMessage 데이터베이스에 안전하게 접근할 수 있게 하는 MCP 서버. LLM이 적절한 전화번호 유효성 검사 및 첨부 파일 처리로 iMessage 대화를 쿼리하고 분석할 수 있도록 지원합니다.
- [@modelcontextprotocol/server-slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack) 📇 ☁️ - 채널 관리 및 메시징을 위한 Slack 워크스페이스 통합
- [@keturiosakys/bluesky-context-server](https://github.com/keturiosakys/bluesky-context-server) 📇 ☁️ - 쿼리 및 상호 작용을 위한 Bluesky 인스턴스 통합
- [MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite) - 🐍 ☁️ - Gmail 및 Google Calendar와의 통합.
- [adhikasp/mcp-twikit](https://github.com/adhikasp/mcp-twikit) 🐍 ☁️ - 트위터 검색 및 타임라인과 상호 작용
- [gotoolkits/wecombot](https://github.com/gotoolkits/mcp-wecombot-server.git) - 🚀 ☁️ - WeCom 그룹 로봇에게 다양한 유형의 메시지를 보내는 MCP 서버 애플리케이션.
- [AbdelStark/nostr-mcp](https://github.com/AbdelStark/nostr-mcp) - 🌐 ☁️ - Nostr과 상호 작용하여 노트 게시 등을 할 수 있는 Nostr MCP 서버.
- [elie222/inbox-zero](https://github.com/elie222/inbox-zero/tree/main/apps/mcp-server) - 🐍 ☁️ - Inbox Zero를 위한 MCP 서버. 답장해야 할 이메일이나 후속 조치가 필요한 이메일을 찾는 등 Gmail 위에 기능을 추가합니다.
- [carterlasalle/mac_messages_mcp](https://github.com/carterlasalle/mac_messages_mcp) 🏠 🍎 🚀 - 모델 컨텍스트 프로토콜(MCP)을 통해 iMessage 데이터베이스와 안전하게 인터페이스하는 MCP 서버로, LLM이 iMessage 대화를 쿼리하고 분석할 수 있게 합니다. 강력한 전화번호 유효성 검사, 첨부 파일 처리, 연락처 관리, 그룹 채팅 처리 및 메시지 송수신 전체 지원을 포함합니다.
- [line/line-bot-mcp-server](https://github.com/line/line-bot-mcp-server) 🎖 📇 ☁️ - LINE 공식 계정을 통합하는 MCP 서버
- [sawa-zen/vrchat-mcp](https://github.com/sawa-zen/vrchat-mcp) - 📇 🏠 VRChat API와 상호 작용하기 위한 MCP 서버입니다. VRChat에서 친구, 월드, 아바타 등에 대한 정보를 검색할 수 있습니다.
- [arpitbatra123/mcp-googletasks](https://github.com/arpitbatra123/mcp-googletasks) - 📇 ☁️ - Google Tasks API와 인터페이스하기 위한 MCP 서버
- [YCloud-Developers/ycloud-whatsapp-mcp-server](https://github.com/YCloud-Developers/ycloud-whatsapp-mcp-server) 📇 🏠 - YCloud 플랫폼을 통해 WhatsApp 비즈니스 메시지를 발송하는 MCP 서버입니다. 
- [jaipandya/producthunt-mcp-server](https://github.com/jaipandya/producthunt-mcp-server) 🐍 🏠 - Product Hunt을 위한 MCP 서버. 트렌딩 게시물, 댓글, 컬렉션, 사용자 등과 상호 작용할 수 있습니다.

### 👤 <a name="customer-data-platforms"></a>고객 데이터 플랫폼

고객 데이터 플랫폼 내의 고객 프로필에 대한 접근을 제공합니다.

- [sergehuber/inoyu-mcp-unomi-server](https://github.com/sergehuber/inoyu-mcp-unomi-server) 📇 ☁️ - Apache Unomi CDP 서버의 프로필에 접근하고 업데이트하는 MCP 서버.
- [OpenDataMCP/OpenDataMCP](https://github.com/OpenDataMCP/OpenDataMCP) 🐍 ☁️ - 모델 컨텍스트 프로토콜을 사용하여 모든 개방형 데이터를 모든 LLM에 연결합니다.
- [tinybirdco/mcp-tinybird](https://github.com/tinybirdco/mcp-tinybird) 🐍 ☁️ - 모든 MCP 클라이언트에서 Tinybird 워크스페이스와 상호 작용하기 위한 MCP 서버.
- [@iaptic/mcp-server-iaptic](https://github.com/iaptic/mcp-server-iaptic) 🎖️ 📇 ☁️ - [iaptic](https://www.iaptic.com)과 연결하여 고객 구매, 거래 데이터 및 앱 수익 통계에 대해 질문합니다.
- [@antv/mcp-server-chart](https://github.com/antvis/mcp-server-chart) 🎖️ 📇 ☁️ - [AntV](https://github.com/antvis) 를 기반으로 데이터 시각화 차트를 생성하는 MCP Server 플러그인.

### 📊 <a name="data-platforms"></a>데이터 플랫폼

데이터 통합, 변환 및 파이프라인 오케스트레이션을 위한 데이터 플랫폼.

- [flowcore/mcp-flowcore-platform](https://github.com/flowcore-io/mcp-flowcore-platform) 🎖️📇☁️🏠 - Flowcore와 상호 작용하여 작업을 수행하고, 데이터를 수집하고, 데이터 코어나 공개 데이터 코어에 있는 모든 데이터를 분석, 교차 참조하고 활용할 수 있습니다. 이 모든 작업은 인간 언어를 사용합니다.


### 🗄️ <a name="databases"></a>데이터베이스

스키마 검사 기능을 갖춘 안전한 데이터베이스 접근. 읽기 전용 접근을 포함한 구성 가능한 보안 제어로 데이터 쿼리 및 분석을 가능하게 합니다.

- [aliyun/alibabacloud-tablestore-mcp-server](https://github.com/aliyun/alibabacloud-tablestore-mcp-server) ☕ 🐍 ☁️ - Tablestore용 MCP 서비스, 문서 추가, 벡터 및 스칼라 기반 문서의 시맨틱 검색, RAG 친화적, 서버리스 기능 포함.
- [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) 🐍 🏠 - Elasticsearch 상호 작용을 제공하는 MCP 서버 구현
- [crystaldba/postgres-mcp](https://github.com/crystaldba/postgres-mcp) 🐍 🏠 - Postgres 개발 및 운영을 위한 올인원 MCP 서버로, 성능 분석, 튜닝 및 상태 점검을 위한 도구 제공
- [domdomegg/airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server) 📇 🏠 - 스키마 검사, 읽기 및 쓰기 기능을 갖춘 Airtable 데이터베이스 통합
- [rashidazarang/airtable-mcp](https://github.com/rashidazarang/airtable-mcp) 🐍 ☁️ - AI 도구를 Airtable에 직접 연결합니다. 자연어를 사용하여 레코드를 쿼리, 생성, 업데이트 및 삭제합니다. 베이스 관리, 테이블 작업, 스키마 조작, 레코드 필터링 및 표준화된 MCP 인터페이스를 통한 데이터 마이그레이션 기능 포함.
- [LucasHild/mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery) 🐍 ☁️ - 스키마 검사 및 쿼리 기능을 갖춘 BigQuery 데이터베이스 통합
- [c4pt0r/mcp-server-tidb](https://github.com/c4pt0r/mcp-server-tidb) 🐍 ☁️ - 스키마 검사 및 쿼리 기능을 갖춘 TiDB 데이터베이스 통합
- [tradercjz/dolphindb-mcp-server](https://github.com/tradercjz/dolphindb-mcp-server) 🐍 ☁️ - 스키마 검사 및 쿼리 기능을 갖춘 TDolphinDB 데이터베이스 통합
- [ergut/mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server) 📇 ☁️ - 직접적인 BigQuery 데이터베이스 접근 및 쿼리 기능을 가능하게 하는 Google BigQuery 통합을 위한 서버 구현
- [ClickHouse/mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse) 🐍 ☁️ - 스키마 검사 및 쿼리 기능을 갖춘 ClickHouse 데이터베이스 통합
- [get-convex/convex-backend](https://stack.convex.dev/convex-mcp-server) 📇 ☁️ - 테이블, 함수를 검사하고 일회성 쿼리를 실행하기 위한 Convex 데이터베이스 통합 ([소스](https://github.com/get-convex/convex-backend/blob/main/npm-packages/convex/src/cli/mcp.ts))
- [@gannonh/firebase-mcp](https://github.com/gannonh/firebase-mcp) 🔥 ⛅️ - Auth, Firestore 및 Storage를 포함한 Firebase 서비스.
- [jovezhong/mcp-timeplus](https://github.com/jovezhong/mcp-timeplus) 🐍 ☁️ - Apache Kafka 및 Timeplus용 MCP 서버. Kafka 토픽 나열, Kafka 메시지 폴링, Kafka 데이터 로컬 저장 및 Timeplus를 통한 SQL로 스트리밍 데이터 쿼리 가능
- [@fireproof-storage/mcp-database-server](https://github.com/fireproof-storage/mcp-database-server) 📇 ☁️ - 다중 사용자 동기화를 지원하는 Fireproof 원장 데이터베이스
- [designcomputer/mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server) 🐍 🏠 - 구성 가능한 접근 제어, 스키마 검사 및 포괄적인 보안 지침을 갖춘 MySQL 데이터베이스 통합
- [f4ww4z/mcp-mysql-server](https://github.com/f4ww4z/mcp-mysql-server) 📇 🏠 - 안전한 MySQL 데이터베이스 운영을 제공하는 Node.js 기반 MySQL 데이터베이스 통합
- [FreePeak/db-mcp-server](https://github.com/FreePeak/db-mcp-server) 🏎️ 🏠 – Golang으로 구축된 고성능 다중 데이터베이스 MCP 서버, MySQL & PostgreSQL 지원 (NoSQL 곧 지원 예정). 쿼리 실행, 트랜잭션 관리, 스키마 탐색, 쿼리 빌딩 및 성능 분석을 위한 내장 도구 포함, 향상된 데이터베이스 워크플로우를 위한 원활한 Cursor 통합.
- [@modelcontextprotocol/server-postgres](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) 📇 🏠 - 스키마 검사 및 쿼리 기능을 갖춘 PostgreSQL 데이터베이스 통합
- [@modelcontextprotocol/server-sqlite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite) 🐍 🏠 - 내장 분석 기능을 갖춘 SQLite 데이터베이스 운영
- [@joshuarileydev/supabase-mcp-server](https://github.com/joshuarileydev/supabase) - Supabase에서 프로젝트 및 조직을 관리하고 생성하기 위한 Supabase MCP 서버
- [@alexanderzuev/supabase-mcp-server](https://github.com/alexander-zuev/supabase-mcp-server) - SQL 쿼리 실행 및 데이터베이스 탐색 도구를 지원하는 Supabase MCP 서버
- [ktanaka101/mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb) 🐍 🏠 - 스키마 검사 및 쿼리 기능을 갖춘 DuckDB 데이터베이스 통합
- [Dataring-engineering/mcp-server-trino](https://github.com/Dataring-engineering/mcp-server-trino) 🐍 ☁️ - Trino 클러스터에서 데이터를 쿼리하고 접근하기 위한 Trino MCP 서버.
- [tuannvm/mcp-trino](https://github.com/tuannvm/mcp-trino) 🏎️ ☁️ - Trino를 위한 Model Context Protocol (MCP) 서버의 Go 구현.
- [memgraph/mcp-memgraph](https://github.com/memgraph/mcp-memgraph) 🐍 🏠 - Memgraph MCP 서버 - Memgraph에 대한 쿼리 실행 도구 및 스키마 리소스 포함.
- [furey/mongodb-lens](https://github.com/furey/mongodb-lens) 📇 🏠 - MongoDB Lens: MongoDB 데이터베이스를 위한 모든 기능을 갖춘 MCP 서버
- [QuantGeekDev/mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp) 📇 🏠 - LLM이 데이터베이스와 직접 상호 작용할 수 있게 하는 MongoDB 통합.
- [kiliczsh/mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server) 📇 🏠 - MongoDB를 위한 모델 컨텍스트 프로토콜 서버
- [tinybirdco/mcp-tinybird](https://github.com/tinybirdco/mcp-tinybird) 🐍 ☁️ - 쿼리 및 API 기능을 갖춘 Tinybird 통합
- [KashiwaByte/vikingdb-mcp-server](https://github.com/KashiwaByte/vikingdb-mcp-server) 🐍 ☁️ - 컬렉션 및 인덱스 소개, 벡터 저장소 및 검색 기능을 갖춘 VikingDB 통합.
- [neo4j-contrib/mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j) 🐍 🏠 - Neo4j와 함께하는 모델 컨텍스트 프로토콜
- [niledatabase/nile-mcp-server](https://github.com/niledatabase/nile-mcp-server) Nile의 Postgres 플랫폼용 MCP 서버 - LLM을 사용하여 Postgres 데이터베이스, 테넌트, 사용자, 인증 관리 및 쿼리
- [isaacwasserman/mcp-snowflake-server](https://github.com/isaacwasserman/mcp-snowflake-server) 🐍 ☁️ - 읽기 및 (선택적) 쓰기 작업뿐만 아니라 인사이트 추적을 구현하는 Snowflake 통합
- [hannesrudolph/sqlite-explorer-fastmcp-mcp-server](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server) 🐍 🏠 - 모델 컨텍스트 프로토콜(MCP)을 통해 SQLite 데이터베이스에 안전한 읽기 전용 접근을 제공하는 MCP 서버. 이 서버는 FastMCP 프레임워크로 구축되어 LLM이 내장된 안전 기능과 쿼리 유효성 검사로 SQLite 데이터베이스를 탐색하고 쿼리할 수 있도록 지원합니다.
- [sirmews/mcp-pinecone](https://github.com/sirmews/mcp-pinecone) 🐍 ☁️ - 벡터 검색 기능을 갖춘 Pinecone 통합
- [runekaagaard/mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy) 🐍 🏠 - PostgreSQL, MySQL, MariaDB, SQLite, Oracle, MS SQL Server 등 다양한 데이터베이스를 지원하는 범용 SQLAlchemy 기반 데이터베이스 통합. 스키마 및 관계 검사, 대규모 데이터셋 분석 기능 제공.
- [mcp-server-jdbc](https://github.com/quarkiverse/quarkus-mcp-servers/tree/main/jdbc) ☕ 🏠 - 모든 JDBC 호환 데이터베이스에 연결하여 쿼리, 삽입, 업데이트, 삭제 등을 수행합니다.
- [pab1it0/adx-mcp-server](https://github.com/pab1it0/adx-mcp-server) 🐍 ☁️ - Azure Data Explorer 데이터베이스 쿼리 및 분석
- [pab1it0/prometheus-mcp-server](https://github.com/pab1it0/prometheus-mcp-server) 🐍 ☁️ - Prometheus 오픈 소스 모니터링 시스템 쿼리 및 분석.
- [neondatabase/mcp-server-neon](https://github.com/neondatabase/mcp-server-neon) 📇 ☁️ — Neon Serverless Postgres를 사용하여 Postgres 데이터베이스를 생성하고 관리하기 위한 MCP 서버
- [XGenerationLab/xiyan_mcp_server](https://github.com/XGenerationLab/xiyan_mcp_server) 📇 ☁️ — 텍스트-SQL LLM으로 XiyanSQL을 사용하여 자연어 쿼리로 데이터베이스에서 데이터를 가져오는 것을 지원하는 MCP 서버.
- [bytebase/dbhub](https://github.com/bytebase/dbhub) 📇 🏠 – 주요 데이터베이스를 지원하는 범용 데이터베이스 MCP 서버.
- [GreptimeTeam/greptimedb-mcp-server](https://github.com/GreptimeTeam/greptimedb-mcp-server) 🐍 🏠 - GreptimeDB 쿼리를 위한 MCP 서버.
- [idoru/influxdb-mcp-server](https://github.com/idoru/influxdb-mcp-server) 📇 ☁️ 🏠 - InfluxDB OSS API v2에 대한 쿼리 실행.
- [xing5/mcp-google-sheets](https://github.com/xing5/mcp-google-sheets) 🐍 ☁️ - Google Sheets와 상호 작용하기 위한 모델 컨텍스트 프로토콜 서버. 이 서버는 Google Sheets API를 통해 스프레드시트를 생성, 읽기, 업데이트 및 관리하는 도구를 제공합니다.
- [freema/mcp-gsheets](https://github.com/freema/mcp-gsheets) 📇 ☁️ - 포괄적인 읽기, 쓰기, 서식 지정 및 시트 관리 기능을 갖춘 Google Sheets API 통합 MCP 서버.
- [qdrant/mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant) 🐍 🏠 - Qdrant MCP 서버
- [ydb/ydb-mcp](https://github.com/ydb-platform/ydb-mcp) 🎖️ 🐍 ☁️ – MCP 서버: [YDB](https://ydb.tech) 데이터베이스와 상호 작용하기 위한

### 💻 <a name="developer-tools"></a>개발자 도구

개발 워크플로우 및 환경 관리를 향상시키는 도구 및 통합.

- [21st-dev/Magic-MCP](https://github.com/21st-dev/magic-mcp) - 최고의 21st.dev 디자인 엔지니어에게서 영감을 받은 맞춤형 UI 컴포넌트 생성.
- [Hypersequent/qasphere-mcp](https://github.com/Hypersequent/qasphere-mcp) 🎖️ 📇 ☁️ - [QA Sphere](https://qasphere.com/) 테스트 관리 시스템과의 통합. LLM이 테스트 케이스를 발견, 요약, 상호작용할 수 있도록 하며 AI 기반 IDE에서 직접 접근 가능
- [Coment-ML/Opik-MCP](https://github.com/comet-ml/opik-mcp) 🎖️ 📇 ☁️ 🏠 - Opik이 캡처한 LLM 관찰 가능성, 추적 및 모니터링 데이터와 자연어로 대화합니다.
- [GLips/Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) 📇 🏠 - 코딩 에이전트가 Figma 데이터에 직접 접근하여 디자인 구현을 한 번에 완료하도록 돕습니다.
- [QuantGeekDev/docker-mcp](https://github.com/QuantGeekDev/docker-mcp) 🏎️ 🏠 - MCP를 통한 Docker 컨테이너 관리 및 운영
- [zcaceres/fetch-mcp](https://github.com/zcaceres/fetch-mcp) 📇 🏠 - JSON, 텍스트, HTML 데이터를 유연하게 가져오는 MCP 서버
- [r-huijts/xcode-mcp-server](https://github.com/r-huijts/xcode-mcp-server) 📇 🏠 🍎 - 프로젝트 관리, 파일 작업 및 빌드 자동화를 위한 Xcode 통합
- [snaggle-ai/openapi-mcp-server](https://github.com/snaggle-ai/openapi-mcp-server) 🏎️ 🏠 - Open API 사양(v3)을 사용하여 모든 HTTP/REST API 서버 연결
- [jetbrains/mcpProxy](https://github.com/JetBrains/mcpProxy) 🎖️ 📇 🏠 - JetBrains IDE에 연결
- [tumf/mcp-text-editor](https://github.com/tumf/mcp-text-editor) 🐍 🏠 - 라인 지향 텍스트 파일 편집기. 토큰 사용량을 최소화하기 위해 효율적인 부분 파일 접근으로 LLM 도구에 최적화됨.
- [@joshuarileydev/simulator-mcp-server](https://github.com/JoshuaRileyDev/simulator-mcp-server) 📇 🏠 - iOS 시뮬레이터를 제어하는 MCP 서버
- [@joshuarileydev/app-store-connect-mcp-server](https://github.com/JoshuaRileyDev/app-store-connect-mcp-server) 📇 🏠 - iOS 개발자를 위한 App Store Connect API와 통신하는 MCP 서버
- [@sammcj/mcp-package-version](https://github.com/sammcj/mcp-package-version) 📇 🏠 - LLM이 코드를 작성할 때 최신 안정 패키지 버전을 제안하도록 돕는 MCP 서버.
- [@delano/postman-mcp-server](https://github.com/delano/postman-mcp-server) 📇 ☁️ - [Postman API](https://www.postman.com/postman/postman-public-workspace/)와 상호 작용
- [@vivekvells/mcp-pandoc](https://github.com/vivekVells/mcp-pandoc) 🗄️ 🚀 - Pandoc을 사용하여 Markdown, HTML, PDF, DOCX(.docx), csv 등 원활한 문서 형식 변환을 위한 MCP 서버.
- [@pskill9/website-downloader](https://github.com/pskill9/website-downloader) 🗄️ 🚀 - 이 MCP 서버는 wget을 사용하여 전체 웹사이트를 다운로드하는 도구를 제공합니다. 웹사이트 구조를 보존하고 로컬에서 작동하도록 링크를 변환합니다.
- [@lamemind/mcp-server-multiverse](https://github.com/lamemind/mcp-server-multiverse) 📇 🏠 🛠️ - 동일한 MCP 서버의 여러 격리된 인스턴스가 고유한 네임스페이스와 구성으로 독립적으로 공존할 수 있도록 하는 미들웨어 서버.
- [@j4c0bs/mcp-server-sql-analyzer](https://github.com/j4c0bs/mcp-server-sql-analyzer) 🐍 - [SQLGlot](https://github.com/tobymao/sqlglot)을 사용하여 SQL 분석, 린팅 및 방언 변환을 제공하는 MCP 서버
- [@haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server) 🐍 🏠 - 워크북 생성, 데이터 작업, 서식 지정 및 고급 기능(차트, 피벗 테이블, 수식)을 제공하는 Excel 조작 서버.
- [xcodebuild](https://github.com/ShenghaiWang/xcodebuild) 🍎 iOS Xcode 워크스페이스/프로젝트를 빌드하고 오류를 llm에 피드백합니다.
- [@jasonjmcghee/claude-debugs-for-you](https://github.com/jasonjmcghee/claude-debugs-for-you) 📇 🏠 - 중단점 및 표현식 평가를 통해 (언어에 구애받지 않는) 자동 디버깅을 가능하게 하는 MCP 서버 및 VS Code 확장 프로그램.
- [@Jktfe/serveMyAPI](https://github.com/Jktfe/serveMyAPI) 📇 🏠 🍎 - macOS 키체인을 사용하여 프로젝트 간에 API 키를 안전하게 저장하고 접근하기 위한 개인 MCP(모델 컨텍스트 프로토콜) 서버.
- [@xzq.xu/jvm-mcp-server](https://github.com/xzq-xu/jvm-mcp-server) 📇 🏠  - JVM 기반 MCP(모델 컨텍스트 프로토콜) 서버의 구현 프로젝트.
- [@yangkyeongmo@/mcp-server-apache-airflow](https://github.com/yangkyeongmo/mcp-server-apache-airflow) 🐍 🏠 - 공식 클라이언트를 사용하여 [Apache Airflow](https://airflow.apache.org/)에 연결하는 MCP 서버.
- [hyperb1iss/droidmind](https://github.com/hyperb1iss/droidmind) 🐍 🏠 - MCP를 통해 AI로 안드로이드 장치를 제어하여 장치 제어, 디버깅, 시스템 분석 및 포괄적인 보안 프레임워크를 통한 UI 자동화 가능.
- [Rootly-AI-Labs/Rootly-MCP-server](https://github.com/Rootly-AI-Labs/Rootly-MCP-server) 🎖️🐍☁️🍎 - 인시던트 관리 플랫폼 [Rootly](https://rootly.com/)를 위한 MCP 서버.
- [YuChenSSR/mindmap-mcp-server](https://github.com/YuChenSSR/mindmap-mcp-server) 🐍 🏠 - 아름다운 대화형 마인드맵 생성을 위한 모델 컨텍스트 프로토콜(MCP) 서버.
- [SDGLBL/mcp-claude-code](https://github.com/SDGLBL/mcp-claude-code) 🐍 🏠 - MCP를 사용한 Claude Code 기능 구현으로, 포괄적인 도구 지원을 통해 AI 코드 이해, 수정 및 프로젝트 분석 가능.
- [gofireflyio/firefly-mcp](https://github.com/gofireflyio/firefly-mcp) 🎖️ 📇 ☁️ - [Firefly](https://firefly.ai)를 사용하여 클라우드 리소스를 통합, 검색, 관리 및 코드화합니다.
- [yWorks/mcp-typescribe](https://github.com/yWorks/mcp-typescribe) 📇 🏠 - 에이전트가 학습되지 않은 API로 작업할 수 있도록 타입스크립트 API 정보를 효율적으로 제공하는 MCP 서버
- [cjo4m06/mcp-shrimp-task-manager](https://github.com/cjo4m06/mcp-shrimp-task-manager) 📇 ☁️ 🏠 – Cursor AI 같은 코딩 에이전트를 강화하기 위해 설계된 프로그래밍 전용 작업 관리 시스템으로, 고급 작업 메모리, 자기 성찰, 의존성 관리 기능을 갖추고 있습니다. [ShrimpTaskManager](https://cjo4m06.github.io/mcp-shrimp-task-manager)
- [axliupore/mcp-code-runner](https://github.com/axliupore/mcp-code-runner) 📇 🏠 - Docker를 통해 로컬로 코드를 실행하고 여러 프로그래밍 언어를 지원하는 MCP 서버입니다
- [TencentEdgeOne/edgeone-pages-mcp](https://github.com/TencentEdgeOne/edgeone-pages-mcp) 📇 ☁️ - EdgeOne Pages에 HTML 콘텐츠를 배포하고 공개적으로 접근 가능한 URL을 얻기 위한 MCP 서비스입니다.
- [lpigeon/ros-mcp-server](https://github.com/lpigeon/ros-mcp-server) 🐍 🏠 🍎 🪟 🐧 - ROS MCP 서버는 사용자의 자연어 명령을 ROS 또는 ROS2 제어 명령으로 변환함으로써 로봇의 제어를 지원합니다.


### 🧮 데이터 과학 도구

데이터 탐색, 분석을 단순화하고 데이터 과학 워크플로우를 향상시키기 위해 설계된 통합 및 도구.
- [ChronulusAI/chronulus-mcp](https://github.com/ChronulusAI/chronulus-mcp) 🐍 ☁️ - Chronulus AI 예측 및 예측 에이전트로 무엇이든 예측하세요.
- [zcaceres/markdownify-mcp](https://github.com/zcaceres/markdownify-mcp) 📇 🏠 - 거의 모든 파일이나 웹 콘텐츠를 마크다운으로 변환하는 MCP 서버
- [@reading-plus-ai/mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration) 🐍 ☁️ - .csv 기반 데이터셋에 대한 자율적인 데이터 탐색을 가능하게 하여 최소한의 노력으로 지능적인 통찰력 제공.

### 📂 <a name="file-systems"></a>파일 시스템

구성 가능한 권한으로 로컬 파일 시스템에 직접 접근을 제공합니다. AI 모델이 지정된 디렉토리 내에서 파일을 읽고, 쓰고, 관리할 수 있게 합니다.

- [@modelcontextprotocol/server-filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) 📇 🏠 - 로컬 파일 시스템 직접 접근.
- [@modelcontextprotocol/server-google-drive](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive) 📇 ☁️ - 파일 목록 조회, 읽기 및 검색을 위한 Google Drive 통합
- [hmk/box-mcp-server](https://github.com/hmk/box-mcp-server) 📇 ☁️ - 파일 목록 조회, 읽기 및 검색을 위한 Box 통합
- [mark3labs/mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server) 🏎️ 🏠 - 로컬 파일 시스템 접근을 위한 Golang 구현.
- [mamertofabian/mcp-everything-search](https://github.com/mamertofabian/mcp-everything-search) 🐍 🏠 🪟 - Everything SDK를 사용한 빠른 Windows 파일 검색
- [cyberchitta/llm-context.py](https://github.com/cyberchitta/llm-context.py) 🐍 🏠 - MCP 또는 클립보드를 통해 LLM과 코드 컨텍스트 공유
- [filesystem@quarkiverse/quarkus-mcp-servers](https://github.com/quarkiverse/quarkus-mcp-servers/tree/main/filesystem) ☕ 🏠 - Quarkus를 사용하여 Java로 구현된 파일 탐색 및 편집을 허용하는 파일 시스템. jar 또는 네이티브 이미지로 사용 가능.
- [Xuanwo/mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal) 🐍 🏠 ☁️ - Apache OpenDAL™을 사용하여 모든 스토리지에 접근

### 💰 <a name="finance--fintech"></a>금융 및 핀테크

금융 데이터 접근 및 암호화폐 시장 정보. 실시간 시장 데이터, 암호화폐 가격 및 금융 분석 쿼리를 가능하게 합니다.

- [heurist-network/heurist-mesh-mcp-server](https://github.com/heurist-network/heurist-mesh-mcp-server) 🎖️ ⛅️ 🏠 🐍 - Heurist Mesh 네트워크를 통해 블록체인 분석, 스마트 계약 보안 감사, 토큰 메트릭 평가 및 온체인 상호 작용을 위한 특화된 웹3 AI 에이전트에 접근합니다. 여러 블록체인에 걸쳐 DeFi 분석, NFT 가치 평가 및 트랜잭션 모니터링을 위한 포괄적인 도구를 제공합니다.
- [@base/base-mcp](https://github.com/base/base-mcp) 🎖️ 📇 ☁️ - 온체인 도구를 위한 Base 네트워크 통합으로, Base 네트워크 및 Coinbase API와 상호 작용하여 지갑 관리, 자금 이체, 스마트 계약 및 DeFi 운영 가능
- [QuantGeekDev/coincap-mcp](https://github.com/QuantGeekDev/coincap-mcp) 📇 ☁️ - CoinCap의 공개 API를 사용한 실시간 암호화폐 시장 데이터 통합으로, API 키 없이 암호화폐 가격 및 시장 정보 접근 제공
- [anjor/coinmarket-mcp-server](https://github.com/anjor/coinmarket-mcp-server) 🐍 ☁️ - 암호화폐 목록 및 시세를 가져오기 위한 Coinmarket API 통합
- [berlinbra/alpha-vantage-mcp](https://github.com/berlinbra/alpha-vantage-mcp) 🐍 ☁️ - 주식 및 암호화폐 정보를 모두 가져오기 위한 Alpha Vantage API 통합
- [ferdousbhai/tasty-agent](https://github.com/ferdousbhai/tasty-agent) 🐍 ☁️ - Tastytrade에서의 거래 활동을 처리하기 위한 Tastyworks API 통합
- [ferdousbhai/investor-agent](https://github.com/ferdousbhai/investor-agent) 🐍 ☁️ - 옵션 추천을 포함한 주식 시장 데이터를 가져오기 위한 Yahoo Finance 통합
- [mcpdotdirect/evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server) 📇 ☁️ - 30개 이상의 EVM 네트워크를 위한 포괄적인 블록체인 서비스, 네이티브 토큰, ERC20, NFT, 스마트 계약, 트랜잭션 및 ENS 확인 지원.
- [bankless/onchain-mcp](https://github.com/Bankless/onchain-mcp/) 📇 ☁️ - 스마트 계약과 상호 작용하고 트랜잭션 및 토큰 정보를 쿼리하는 Bankless Onchain API
- [kukapay/cryptopanic-mcp-server](https://github.com/kukapay/cryptopanic-mcp-server) 🐍 ☁️ - CryptoPanic 기반의 최신 암호화폐 뉴스를 AI 에이전트에게 제공.
- [kukapay/whale-tracker-mcp](https://github.com/kukapay/whale-tracker-mcp) 🐍 ☁️ - 암호화폐 고래 거래 추적을 위한 mcp 서버.
- [kukapay/crypto-feargreed-mcp](https://github.com/kukapay/crypto-feargreed-mcp) 🐍 ☁️ - 실시간 및 과거의 암호화폐 공포 및 탐욕 지수 데이터 제공.
- [kukapay/dune-analytics-mcp](https://github.com/kukapay/dune-analytics-mcp) 🐍 ☁️ - Dune Analytics 데이터를 AI 에이전트에게 연결하는 mcp 서버.
- [kukapay/pancakeswap-poolspy-mcp](https://github.com/kukapay/pancakeswap-poolspy-mcp) 🐍 ☁️ - Pancake Swap에서 새로 생성된 풀을 추적하는 MCP 서버.
- [kukapay/uniswap-poolspy-mcp](https://github.com/kukapay/uniswap-poolspy-mcp) 🐍 ☁️ - 여러 블록체인에서 Uniswap에 새로 생성된 유동성 풀을 추적하는 MCP 서버.
- [kukapay/uniswap-trader-mcp](https://github.com/kukapay/uniswap-trader-mcp) 🐍 ☁️ - 여러 블록체인에서 Uniswap DEX의 토큰 스왑을 자동화하는 AI 에이전트를 위한 MCP 서버.
- [kukapay/token-minter-mcp](https://github.com/kukapay/token-minter-mcp) 🐍 ☁️ - 여러 블록체인에서 ERC-20 토큰을 발행하는 도구를 AI 에이전트에게 제공하는 MCP 서버.
- [kukapay/thegraph-mcp](https://github.com/kukapay/thegraph-mcp) 🐍 ☁️ - The Graph의 인덱싱된 블록체인 데이터로 AI 에이전트를 강화하는 MCP 서버.
- [pwh-pwh/coin-mcp-server](https://github.com/pwh-pwh/coin-mcp-server) 🐍 ☁️ - 암호화폐 가격을 가져오기 위한 Bitget API.
- [HuggingAGI/mcp-baostock-server](https://github.com/HuggingAGI/mcp-baostock-server) 🐍 ☁️ - baostock 기반 MCP 서버로 중국 주식 시장 데이터에 대한 액세스 및 분석 기능을 제공합니다.
- [Wuye-AI/mcp-server-wuye-ai](https://github.com/wuye-ai/mcp-server-wuye-ai) 🎖️ 📇 ☁️ - CRIC부동산AI 플랫폼에 접속하는 MCP 서버입니다. CRIC부동산AI는 커얼루이가 부동산 업계를 위해 특별히 개발한 지능형 AI 어시스턴트입니다.

### 🎮 <a name="gaming"></a>게임

게임 관련 데이터, 게임 엔진 및 서비스와의 통합

- [Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp) 📇 🏠 - Godot 게임 엔진과 상호 작용하기 위한 MCP 서버, Godot 프로젝트에서 장면 편집, 실행, 디버깅 및 관리 도구 제공.
- [rishijatia/fantasy-pl-mcp](https://github.com/rishijatia/fantasy-pl-mcp/) 🐍 ☁️ - 실시간 판타지 프리미어 리그 데이터 및 분석 도구를 위한 MCP 서버.
- [CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity) 📇 #️⃣ 🏠 - 게임 개발을 위한 Unity3d 게임 엔진 통합용 MCP 서버
- [opgginc/opgg-mcp](https://github.com/opgginc/opgg-mcp) 📇 ☁️ - 리그 오브 레전드, TFT, 발로란트와 같은 인기 게임의 실시간 게임 데이터에 접근하여 챔피언 분석, e스포츠 일정, 메타 구성 및 캐릭터 통계를 제공합니다.

### 🧠 <a name="knowledge--memory"></a>지식 및 메모리

지식 그래프 구조를 사용한 영구 메모리 저장. AI 모델이 세션 간에 구조화된 정보를 유지하고 쿼리할 수 있게 합니다.
- [@modelcontextprotocol/server-memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) 📇 🏠 - 컨텍스트 유지를 위한 지식 그래프 기반 영구 메모리 시스템
- [/CheMiguel23/MemoryMesh](https://github.com/CheMiguel23/MemoryMesh) 📇 🏠 - AI 역할극 및 스토리 생성에 중점을 둔 향상된 그래프 기반 메모리
- [/topoteretes/cognee](https://github.com/topoteretes/cognee/tree/dev/cognee-mcp) 📇 🏠 - 다양한 그래프 및 벡터 저장소를 사용하고 30개 이상의 데이터 소스에서 수집을 허용하는 AI 앱 및 에이전트용 메모리 관리자
- [@hannesrudolph/mcp-ragdocs](https://github.com/hannesrudolph/mcp-ragdocs) 🐍 🏠 - 벡터 검색을 통해 문서를 검색하고 처리하는 도구를 제공하는 MCP 서버 구현으로, AI 어시스턴트가 관련 문서 컨텍스트로 응답을 보강할 수 있도록 지원합니다.
- [jinzcdev/markmap-mcp-server](https://github.com/jinzcdev/markmap-mcp-server) 📇 🏠 - [markmap](https://github.com/markmap/markmap)을 기반으로 구축된 MCP 서버로, **Markdown**을 대화형 **마인드맵**으로 변환합니다. 다양한 형식(PNG/JPG/SVG) 내보내기, 브라우저 실시간 미리보기, 원클릭 Markdown 복사 및 동적 시각화 기능을 지원합니다.
- [@kaliaboi/mcp-zotero](https://github.com/kaliaboi/mcp-zotero) 📇 ☁️ - LLM이 Zotero 클라우드의 컬렉션 및 소스와 함께 작업할 수 있도록 하는 커넥터
- [mcp-summarizer](https://github.com/0xshellming/mcp-summarizer) 📕 ☁️ - AI 요약 MCP 서버, 여러 콘텐츠 유형 지원: 일반 텍스트, 웹 페이지, PDF 문서, EPUB 책, HTML 콘텐츠
- [graphlit-mcp-server](https://github.com/graphlit/graphlit-mcp-server) 📇 ☁️ - Slack, Discord, 웹사이트, Google Drive, Linear 또는 GitHub에서 무엇이든 Graphlit 프로젝트로 수집한 다음 Cursor, Windsurf 또는 Cline과 같은 MCP 클라이언트 내에서 관련 지식을 검색하고 검색합니다.
- [@mem0ai/mem0-mcp](https://github.com/mem0ai/mem0-mcp) 🐍 🏠 - 코딩 선호도 및 패턴 관리를 돕는 Mem0용 모델 컨텍스트 프로토콜 서버로, Cursor 및 Windsurf와 같은 IDE에서 코드 구현, 모범 사례 및 기술 문서를 저장, 검색 및 의미론적으로 처리하는 도구를 제공합니다.
- [@ragieai/mcp-server](https://github.com/ragieai/ragie-mcp-server) 📇 ☁️ - Google Drive, Notion, JIRA 등과 같은 통합 서비스에 연결된 [Ragie](https://www.ragie.ai) (RAG) 지식 베이스에서 컨텍스트를 검색합니다.

### 🗺️ <a name="location-services"></a>위치 서비스

지리 및 위치 기반 서비스 통합. 지도 데이터, 길찾기 및 장소 정보에 대한 접근을 가능하게 합니다.

- [@modelcontextprotocol/server-google-maps](https://github.com/modelcontextprotocol/servers/tree/main/src/google-maps) 📇 ☁️ - 위치 서비스, 경로 안내 및 장소 세부 정보를 위한 Google 지도 통합
- [SecretiveShell/MCP-timeserver](https://github.com/SecretiveShell/MCP-timeserver) 🐍 🏠 - 모든 시간대의 시간에 접근하고 현재 현지 시간 확인
- [webcoderz/MCP-Geo](https://github.com/webcoderz/MCP-Geo) 🐍 🏠 - nominatim, ArcGIS, Bing을 위한 지오코딩 MCP 서버
- [@briandconnelly/mcp-server-ipinfo](https://github.com/briandconnelly/mcp-server-ipinfo) 🐍 ☁️  - IPInfo API를 사용한 IP 주소 지리 위치 및 네트워크 정보
- [QGIS MCP](https://github.com/jjsantos01/qgis_mcp) - QGIS 데스크톱을 MCP를 통해 Claude AI에 연결합니다. 이 통합은 프롬프트 지원 프로젝트 생성, 레이어 로딩, 코드 실행 등을 가능하게 합니다.
- [kukapay/nearby-search-mcp](https://github.com/kukapay/nearby-search-mcp) 🐍 ☁️ - IP 기반 위치 감지를 통한 주변 장소 검색을 위한 MCP 서버.

### 🎯 <a name="marketing"></a>마케팅

마케팅 콘텐츠 생성 및 편집, 웹 메타 데이터 작업, 제품 포지셔닝 및 편집 가이드 작업을 위한 도구.

- [Open Strategy Partners 마케팅 도구](https://github.com/open-strategy-partners/osp_marketing_tools) 🐍 🏠 - 글쓰기 스타일, 편집 코드, 제품 마케팅 가치 맵 생성을 포함한 Open Strategy Partners의 마케팅 도구 모음.

### 📊 <a name="monitoring"></a>모니터링

애플리케이션 모니터링 데이터 접근 및 분석. AI 모델이 오류 보고서 및 성능 지표를 검토할 수 있게 합니다.

- [tumf/grafana-loki-mcp](https://github.com/tumf/grafana-loki-mcp) 🐍 🏠 - Grafana API를 통해 Loki 로그를 쿼리할 수 있는 MCP 서버입니다.
- [@modelcontextprotocol/server-sentry](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry) 🐍 ☁️ - 오류 추적 및 성능 모니터링을 위한 Sentry.io 통합
- [@MindscapeHQ/server-raygun](https://github.com/MindscapeHQ/mcp-server-raygun) 📇 ☁️ - 충돌 보고 및 실제 사용자 모니터링을 위한 Raygun API V3 통합
- [metoro-io/metoro-mcp-server](https://github.com/metoro-io/metoro-mcp-server) 🎖️ 🏎️ ☁️ - Metoro로 모니터링되는 쿠버네티스 환경 쿼리 및 상호 작용
- [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) 🎖️ 🐍 🏠 ☁️ - Grafana 인스턴스에서 대시보드 검색, 인시던트 조사 및 데이터 소스 쿼리
- [pydantic/logfire-mcp](https://github.com/pydantic/logfire-mcp) 🎖️ 🐍 ☁️ - Logfire를 통해 OpenTelemetry 추적 및 메트릭에 대한 접근 제공
- [seekrays/mcp-monitor](https://github.com/seekrays/mcp-monitor) 🏎️ 🏠 - 모델 컨텍스트 프로토콜(MCP)을 통해 시스템 메트릭을 노출하는 시스템 모니터링 도구. 이 도구를 사용하면 LLM이 MCP 호환 인터페이스를 통해 실시간 시스템 정보를 검색할 수 있습니다. (CPU, 메모리, 디스크, 네트워크, 호스트, 프로세스 지원)
- [hyperb1iss/lucidity-mcp](https://github.com/hyperb1iss/lucidity-mcp) 🐍 🏠 - 복잡성에서 보안 취약점에 이르기까지 10가지 중요한 차원에 걸쳐 지능적이고 프롬프트 기반 분석을 통해 AI 생성 코드 품질 향상

### 🔎 <a name="search"></a>검색

- [scrapeless-ai/scrapeless-mcp-server](https://github.com/scrapeless-ai/scrapeless-mcp-server) 🐍 ☁️ - Scrapeless Model Context Protocol 서비스는 MCP 생태계 내에서 떠나지 않고 웹 검색을 가능하게 하는 Google SERP API에 대한 MCP 서버 커넥터 역할을 합니다.
- [@modelcontextprotocol/server-brave-search](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search) 📇 ☁️ - Brave의 검색 API를 사용한 웹 검색 기능
- [@angheljf/nyt](https://github.com/angheljf/nyt) 📇 ☁️ - NYTimes API를 사용하여 기사 검색
- [@modelcontextprotocol/server-fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) 🐍 🏠 ☁️ - AI 소비를 위한 효율적인 웹 콘텐츠 가져오기 및 처리
- [ac3xx/mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi) 📇 ☁️ - Kagi 검색 API 통합
- [exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) 🎖️ 📇 ☁️ – 모델 컨텍스트 프로토콜(MCP) 서버는 Claude와 같은 AI 어시스턴트가 웹 검색을 위해 Exa AI 검색 API를 사용할 수 있게 합니다. 이 설정은 AI 모델이 안전하고 통제된 방식으로 실시간 웹 정보를 얻을 수 있도록 합니다.
- [fatwang2/search1api-mcp](https://github.com/fatwang2/search1api-mcp) 📇 ☁️ - search1api를 통한 검색 (유료 API 키 필요)
- [Tomatio13/mcp-server-tavily](https://github.com/Tomatio13/mcp-server-tavily) ☁️ 🐍 – Tavily AI 검색 API
- [kshern/mcp-tavily](https://github.com/kshern/mcp-tavily.git) ☁️ 📇 – Tavily AI 검색 API
- [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) ☁️ 🐍 - ArXiv 연구 논문 검색
- [mzxrai/mcp-webresearch](https://github.com/mzxrai/mcp-webresearch) 🔍📚 - Google 검색 및 모든 주제에 대한 심층 웹 리서치 수행
- [andybrandt/mcp-simple-arxiv](https://github.com/andybrandt/mcp-simple-arxiv) - 🐍 ☁️  arXiv에서 논문을 검색하고 읽기 위한 LLM용 MCP
- [andybrandt/mcp-simple-pubmed](https://github.com/andybrandt/mcp-simple-pubmed) - 🐍 ☁️  PubMed에서 의료/생명 과학 논문을 검색하고 읽기 위한 MCP.
- [apify/mcp-server-rag-web-browser](https://github.com/apify/mcp-server-rag-web-browser) 📇 ☁️ - Apify의 오픈 소스 RAG 웹 브라우저 액터를 위한 MCP 서버로 웹 검색, URL 스크래핑 및 마크다운 형식으로 콘텐츠 반환 수행.
- [SecretiveShell/MCP-searxng](https://github.com/SecretiveShell/MCP-searxng) 🐍 🏠 - searXNG 인스턴스에 연결하기 위한 MCP 서버
- [Bigsy/Clojars-MCP-Server](https://github.com/Bigsy/Clojars-MCP-Server) 📇 ☁️ - Clojure 라이브러리의 최신 의존성 정보를 위한 Clojars MCP 서버
- [Ihor-Sokoliuk/MCP-SearXNG](https://github.com/ihor-sokoliuk/mcp-searxng) 📇 🏠/☁️ - [SearXNG](https://docs.searxng.org)를 위한 모델 컨텍스트 프로토콜 서버
- [erithwik/mcp-hn](https://github.com/erithwik/mcp-hn) 🐍 ☁️ - 해커 뉴스 검색, 인기 기사 가져오기 등을 위한 MCP 서버.
- [chanmeng/google-news-mcp-server](https://github.com/ChanMeng666/server-google-news) 📇 ☁️ - 자동 주제 분류, 다국어 지원 및 [SerpAPI](https://serpapi.com/)를 통한 헤드라인, 기사 및 관련 주제를 포함한 포괄적인 검색 기능을 갖춘 Google 뉴스 통합.
- [devflowinc/trieve](https://github.com/devflowinc/trieve/tree/main/clients/mcp-server) 🎖️ 📇 ☁️ 🏠 - [Trieve](https://trieve.ai)를 통해 데이터셋에서 정보를 크롤링, 임베딩, 청킹, 검색 및 검색합니다.
- [nickclyde/duckduckgo-mcp-server](https://github.com/nickclyde/duckduckgo-mcp-server) 🐍 ☁️ - DuckDuckGo를 사용한 웹 검색
- [zhsama/duckduckgo-mcp-server](https://github.com/zhsama/duckduckgo-mpc-server/) 📇 🏠 ☁️ - DuckDuckGo 검색 기능을 제공하는 TypeScript 기반 MCP 서버입니다.
- [vectorize-io/vectorize-mcp-server](https://github.com/vectorize-io/vectorize-mcp-server/) ☁️ 📇 - 고급 검색, 비공개 심층 연구, 모든 것을 마크다운으로 변환하는 파일 추출 및 텍스트 청킹을 위한 [Vectorize](https://vectorize.io) MCP 서버.
- [jae-jae/fetcher-mcp](https://github.com/jae-jae/fetcher-mcp) 📇 🏠 - Playwright 헤드리스 브라우저를 사용하여 웹 페이지 콘텐츠를 가져오는 MCP 서버, Javascript 렌더링 및 지능형 콘텐츠 추출 지원, 마크다운 또는 HTML 형식 출력.
- [isnow890/naver-search-mcp](https://github.com/isnow890/naver-search-mcp) 📇 ☁️ - 네이버 검색 API를 통합한 MCP 서버로, 블로그, 뉴스, 쇼핑 검색 및 데이터랩 분석 기능을 제공합니다.
- [yamanoku/baseline-mcp-server](https://github.com/yamanoku/baseline-mcp-server) 📇 🏠 - 웹 플랫폼 API를 사용하여 Baseline 상태를 검색하는 MCP 서버

### 🔒 <a name="security"></a>보안

- [firstorderai/authenticator_mcp](https://github.com/firstorderai/authenticator_mcp) 📇 🏠 🍎 🪟 🐧 – AI 에이전트가 인증 앱과 상호 작용할 수 있도록 하는 보안 MCP(Model Context Protocol) 서버입니다.
- [dnstwist MCP 서버](https://github.com/BurtTheCoder/mcp-dnstwist) 📇 🪟 ☁️ - 타이포스쿼팅, 피싱 및 기업 스파이 활동 탐지를 돕는 강력한 DNS 퍼징 도구인 dnstwist용 MCP 서버.
- [fosdickio/binary_ninja_mcp](https://github.com/Vector35/binaryninja-mcp) 🐍 🏠 🍎 🪟 🐧 - Binary Ninja를 위한 MCP 서버 및 브릿지. 바이너리 분석 및 리버스 엔지니어링을 위한 도구를 제공합니다.
- [Maigret MCP 서버](https://github.com/BurtTheCoder/mcp-maigret) 📇 🪟 ☁️ - 다양한 공개 소스에서 사용자 계정 정보를 수집하는 강력한 OSINT 도구인 maigret용 MCP 서버. 이 서버는 소셜 네트워크에서 사용자 이름 검색 및 URL 분석 도구를 제공합니다.
- [Shodan MCP 서버](https://github.com/BurtTheCoder/mcp-shodan) 📇 🪟 ☁️ - Shodan API 및 Shodan CVEDB 쿼리를 위한 MCP 서버. 이 서버는 IP 조회, 장치 검색, DNS 조회, 취약점 쿼리, CPE 조회 등을 위한 도구를 제공합니다.
- [VirusTotal MCP 서버](https://github.com/BurtTheCoder/mcp-virustotal) 📇 🪟 ☁️ - VirusTotal API 쿼리를 위한 MCP 서버. 이 서버는 URL 스캔, 파일 해시 분석 및 IP 주소 보고서 검색 도구를 제공합니다.
- [ORKL MCP 서버](https://github.com/fr0gger/MCP_Security) 📇 🛡️ ☁️ - ORKL API 쿼리를 위한 MCP 서버. 이 서버는 위협 보고서 가져오기, 위협 행위자 분석 및 인텔리전스 소스 검색 도구를 제공합니다.
- [Security Audit MCP 서버](https://github.com/qianniuspace/mcp-security-audit) 📇 🛡️ ☁️ 보안 취약점에 대해 npm 패키지 의존성을 감사하는 강력한 MCP(모델 컨텍스트 프로토콜) 서버. 실시간 보안 검사를 위한 원격 npm 레지스트리 통합으로 구축됨.
- [ROADRecon MCP 서버](https://github.com/atomicchonk/roadrecon_mcp_server) 🐍 🪟 🏠 Azure 테넌트 열거에서 ROADrecon 수집 결과 분석을 위한 MCP 서버
- [VMS MCP 서버](https://github.com/jyjune/mcp_vms) 🐍 🏠 🪟 VMS MCP 서버는 CCTV 녹화 프로그램(VMS)에 연결하여 녹화된 영상과 실시간 영상을 가져오며, 특정 채널의 특정 시간에 실시간 영상이나 재생 화면을 표시하는 등의 VMS 소프트웨어 제어 도구도 제공합니다.
- 
### 🏃 <a name="sports"></a>스포츠

스포츠 관련 데이터, 결과 및 통계에 접근하기 위한 도구.

- [r-huijts/firstcycling-mcp](https://github.com/r-huijts/firstcycling-mcp) 📇 ☁️ - 자연어를 통해 사이클링 경주 데이터, 결과 및 통계에 접근합니다. firstcycling.com에서 출발 목록, 경주 결과 및 라이더 정보 검색 기능 포함.
- [willvelida/mcp-afl-server](https://github.com/willvelida/mcp-afl-server) ☁️ - MCP 서버는 Squiggle API와 통합되어 호주 풋볼 리그 팀, 순위표, 경기 결과, 예측, 그리고 파워 랭킹에 대한 정보를 제공합니다.

### 🌎 <a name="translation-services"></a>번역 서비스

AI 어시스턴트가 다양한 언어 간에 콘텐츠를 번역할 수 있게 해주는 번역 도구 및 서비스.

- [translated/lara-mcp](https://github.com/translated/lara-mcp) 🎖️ 📇 ☁️ - Lara 번역 API를 위한 MCP 서버로, 언어 감지 및 컨텍스트 인식 번역을 지원하는 강력한 번역 기능을 제공합니다.

### 🚆 <a name="travel-and-transportation"></a>여행 및 교통

여행 및 교통 정보 접근. 일정, 경로 및 실시간 여행 데이터 쿼리를 가능하게 합니다.

- [Airbnb MCP 서버](https://github.com/openbnb-org/mcp-server-airbnb) 📇 ☁️ - Airbnb 검색 및 숙소 세부 정보 가져오기 도구 제공.
- [NS 여행 정보 MCP 서버](https://github.com/r-huijts/ns-mcp-server) 📇 ☁️ - 네덜란드 철도(NS) 여행 정보, 일정 및 실시간 업데이트 접근
- [KyrieTangSheng/mcp-server-nationalparks](https://github.com/KyrieTangSheng/mcp-server-nationalparks) 📇 ☁️ - 미국 국립 공원의 공원 세부 정보, 경고, 방문자 센터, 캠프장 및 이벤트에 대한 최신 정보를 제공하는 국립 공원 서비스 API 통합
- [pab1it0/tripadvisor-mcp](https://github.com/pab1it0/tripadvisor-mcp) 📇 🐍 - LLM이 Tripadvisor API와 상호 작용할 수 있게 하는 MCP 서버로, 표준화된 MCP 인터페이스를 통해 위치 데이터, 리뷰 및 사진 지원

### 🔄 <a name="version-control"></a>버전 관리

Git 리포지토리 및 버전 관리 플랫폼과 상호 작용합니다. 표준화된 API를 통해 리포지토리 관리, 코드 분석, 풀 리퀘스트 처리, 이슈 추적 및 기타 버전 관리 작업을 가능하게 합니다.

- [@modelcontextprotocol/server-github](https://github.com/modelcontextprotocol/servers/tree/main/src/github) 📇 ☁️ - 리포지토리 관리, PR, 이슈 등을 위한 GitHub API 통합
- [@modelcontextprotocol/server-gitlab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab) 📇 ☁️ 🏠 - 프로젝트 관리 및 CI/CD 운영을 위한 GitLab 플랫폼 통합
- [Tiberriver256/mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops) 📇 ☁️ - Azure DevOps 통합, 리포지토리, 작업 항목 및 파이프라인 관리용
- [@oschina/mcp-gitee](https://github.com/oschina/gitee) 🏎️ ☁️ 🏠 - Gitee API 통합, 리포지토리, 이슈 및 풀 리퀘스트 관리 등.
- [@modelcontextprotocol/server-git](https://github.com/modelcontextprotocol/servers/tree/main/src/git) 🐍 🏠 - 로컬 리포지토리 읽기, 검색 및 분석을 포함한 직접적인 Git 리포지토리 운영
- [adhikasp/mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest) 🐍 🏠 - LLM으로 GitHub 리포지토리 읽기 및 분석

### 🛠️ <a name="other-tools-and-integrations"></a>기타 도구 및 통합

- [apify/actors-mcp-server](https://github.com/apify/actors-mcp-server) 📇 ☁️ - 액터라고 알려진 3,000개 이상의 사전 구축된 클라우드 도구를 사용하여 웹사이트, 전자 상거래, 소셜 미디어, 검색 엔진, 지도 등에서 데이터 추출
- [ivo-toby/contentful-mcp](https://github.com/ivo-toby/contentful-mcp) 📇 🏠 - Contentful Space에서 콘텐츠, 콘텐츠 모델 및 에셋 업데이트, 생성, 삭제
- [mzxrai/mcp-openai](https://github.com/mzxrai/mcp-openai) 📇 ☁️ - OpenAI의 가장 똑똑한 모델과 채팅
- [mrjoshuak/godoc-mcp](https://github.com/mrjoshuak/godoc-mcp) 🏎️ 🏠 - 전체 소스 파일을 읽지 않고 AI 어시스턴트에게 패키지 문서 및 유형에 대한 스마트한 접근을 제공하는 토큰 효율적인 Go 문서 서버
- [pierrebrunelle/mcp-server-openai](https://github.com/pierrebrunelle/mcp-server-openai) 🐍 ☁️ - MCP 프로토콜을 사용하여 Claude에서 직접 OpenAI 모델 쿼리
- [@modelcontextprotocol/server-everything](https://github.com/modelcontextprotocol/servers/tree/main/src/everything) 📇 🏠 - MCP 프로토콜의 모든 기능을 실행하는 MCP 서버
- [baba786/phabricator-mcp-server](https://github.com/baba786/phabricator-mcp-server) 🐍 ☁️ - Phabricator API와 상호 작용
- [MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) 🐍 ☁️ 🏠 - REST API를 통해 Obsidian과 상호 작용
- [calclavia/mcp-obsidian](https://github.com/calclavia/mcp-obsidian) 📇 🏠 - Claude 데스크톱(또는 모든 MCP 클라이언트)이 마크다운 노트(예: Obsidian 보관소)를 포함하는 모든 디렉토리를 읽고 검색할 수 있도록 하는 커넥터입니다.
- [anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube) 📇 ☁️ - YouTube 자막 가져오기
- [Seym0n/tiktok-mcp](https://github.com/Seym0n/tiktok-mcp) 📇 ☁️ - TikTok 동영상과 상호 작용
- [danhilse/notion_mcp](https://github.com/danhilse/notion_mcp) 🐍 ☁️ - 개인 할 일 목록 관리를 위해 Notion의 API와 통합
- [rusiaaman/wcgw](https://github.com/rusiaaman/wcgw/blob/main/src/wcgw/client/mcp_server/Readme.md) 🐍 🏠 - 자율 셸 실행, 컴퓨터 제어 및 코딩 에이전트. (Mac)
- [reeeeemo/ancestry-mcp](https://github.com/reeeeemo/ancestry-mcp) 🐍 🏠 - AI가 .ged 파일 및 유전 데이터 읽기 가능
- [sirmews/apple-notes-mcp](https://github.com/sirmews/apple-notes-mcp) 🐍 🏠 - AI가 로컬 Apple Notes 데이터베이스에서 읽기 가능 (macOS 전용)
- [anjor/coinmarket-mcp-server](https://github.com/anjor/coinmarket-mcp-server) 🐍 🏠 - 암호화폐 목록 및 시세를 가져오기 위한 Coinmarket API 통합
- [suekou/mcp-notion-server](https://github.com/suekou/mcp-notion-server) 📇 🏠 - Notion API와 상호 작용
- [amidabuddha/unichat-mcp-server](https://github.com/amidabuddha/unichat-mcp-server) 🐍/📇 ☁️ - 도구 또는 사전 정의된 프롬프트를 통해 MCP 프로토콜을 사용하여 OpenAI, MistralAI, Anthropic, xAI, Google AI 또는 DeepSeek에 요청 보내기. 공급업체 API 키 필요
- [evalstate/mcp-miro](https://github.com/evalstate/mcp-miro) 📇 ☁️ - MIRO 화이트보드 접근, 항목 대량 생성 및 읽기. REST API용 OAUTH 키 필요.
- [@tacticlaunch/mcp-linear](https://github.com/tacticlaunch/mcp-linear) 📇 ☁️ 🍎 🪟 🐧 - Linear 프로젝트 관리 시스템과 통합
- [KS-GEN-AI/jira-mcp-server](https://github.com/KS-GEN-AI/jira-mcp-server) 📇 ☁️ 🍎 🪟 - JQL 및 API를 통해 Jira 데이터 읽기 및 티켓 생성 및 편집 요청 실행.
- [KS-GEN-AI/confluence-mcp-server](https://github.com/KS-GEN-AI/confluence-mcp-server) 📇 ☁️ 🍎 🪟 - CQL을 통해 Confluence 데이터 가져오기 및 페이지 읽기.
- [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) 🐍 ☁️ - Atlassian 제품(Confluence 및 Jira)용 MCP 서버. Confluence Cloud, Jira Cloud 및 Jira Server/Data Center 지원. Atlassian 작업 공간 전반에 걸쳐 콘텐츠 검색, 읽기, 생성 및 관리를 위한 포괄적인 도구 제공.
- [pyroprompts/any-chat-completions-mcp](https://github.com/pyroprompts/any-chat-completions-mcp) - Perplexity, Groq, xAI 등과 같은 다른 OpenAI SDK 호환 채팅 완료 API와 채팅
- [anaisbetts/mcp-installer](https://github.com/anaisbetts/mcp-installer) 🐍 🏠 -  다른 MCP 서버를 설치해주는 MCP 서버.
- [tanigami/mcp-server-perplexity](https://github.com/tanigami/mcp-server-perplexity) 🐍 ☁️ - Perplexity API와 상호 작용.
- [future-audiences/wikimedia-enterprise-model-context-protocol](https://gitlab.wikimedia.org/repos/future-audiences/wikimedia-enterprise-model-context-protocol) 🐍 ☁️  - 위키백과 기사 조회 API
- [andybrandt/mcp-simple-timeserver](https://github.com/andybrandt/mcp-simple-timeserver) 🐍 🏠☁️ - 클라이언트 머신의 현지 시간 또는 NTP 서버의 현재 UTC 시간을 확인할 수 있는 MCP 서버
- [andybrandt/mcp-simple-openai-assistant](https://github.com/andybrandt/mcp-simple-openai-assistant) - 🐍 ☁️  OpenAI 어시스턴트와 대화하기 위한 MCP (Claude는 모든 GPT 모델을 어시스턴트로 사용할 수 있음)
- [@evalstate/mcp-hfspace](https://github.com/evalstate/mcp-hfspace) 📇 ☁️ - Claude에서 직접 HuggingFace Spaces 사용. 오픈 소스 이미지 생성, 채팅, 비전 작업 등 사용. 이미지, 오디오 및 텍스트 업로드/다운로드 지원.
- [zueai/mcp-manager](https://github.com/zueai/mcp-manager) 📇 ☁️ - Claude 데스크톱 앱용 MCP 서버를 설치하고 관리하는 간단한 웹 UI.
- [wong2/mcp-cli](https://github.com/wong2/mcp-cli) 📇 🏠 - MCP 서버 테스트용 CLI 도구
- [chrishayuk/mcp-cli](https://github.com/chrishayuk/mcp-cli) 🐍 🏠 - MCP 서버 테스트를 위한 또 다른 CLI 도구
- [isaacwasserman/mcp-vegalite-server](https://github.com/isaacwasserman/mcp-vegalite-server) 🐍 🏠 - VegaLite 형식 및 렌더러를 사용하여 가져온 데이터에서 시각화 생성.
- [tevonsb/homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp) 📇 🏠 - Home Assistant 데이터 접근 및 장치(조명, 스위치, 온도 조절기 등) 제어.
- [allenporter/mcp-server-home-assistant](https://github.com/allenporter/mcp-server-home-assistant) 🐍 🏠 - 모델 컨텍스트 프로토콜 서버를 통해 모든 Home Assistant 음성 인텐트를 노출하여 홈 제어 가능.
- [@magarcia/mcp-server-giphy](https://github.com/magarcia/mcp-server-giphy) 📇 ☁️ - Giphy API를 통해 Giphy의 방대한 라이브러리에서 GIF 검색 및 검색.
- [nguyenvanduocit/all-in-one-model-context-protocol](https://github.com/nguyenvanduocit/all-in-one-model-context-protocol) 🏎️ 🏠 - 개발자를 위한 유용한 도구 모음, 엔지니어가 필요로 하는 거의 모든 것: confluence, Jira, Youtube, 스크립트 실행, 지식 기반 RAG, URL 가져오기, Youtube 채널 관리, 이메일, 캘린더, gitlab
- [@joshuarileydev/mac-apps-launcher-mcp-server](https://github.com/JoshuaRileyDev/mac-apps-launcher) 📇 🏠 - MacOS에서 애플리케이션을 나열하고 실행하는 MCP 서버
- [ZeparHyfar/mcp-datetime](https://github.com/ZeparHyfar/mcp-datetime) - 다양한 형식의 날짜 및 시간 함수를 제공하는 MCP 서버
- [SecretiveShell/MCP-wolfram-alpha](https://github.com/SecretiveShell/MCP-wolfram-alpha) 🐍 ☁️ - Wolfram Alpha API 쿼리를 위한 MCP 서버.
- [Amazon Bedrock Nova Canvas](https://github.com/zxkane/mcp-server-amazon-bedrock) 📇 ☁️ - 이미지 생성을 위해 Amazon Nova Canvas 모델 사용.
- [apinetwork/piapi-mcp-server](https://github.com/apinetwork/piapi-mcp-server) 📇 ☁️ PiAPI MCP 서버는 사용자가 Claude 또는 다른 MCP 호환 앱에서 직접 Midjourney/Flux/Kling/Hunyuan/Udio/Trellis로 미디어 콘텐츠를 생성할 수 있게 합니다.
- [gotoolkits/DifyWorkflow](https://github.com/gotoolkits/mcp-difyworkflow-server) - 🏎️ ☁️ Dify 워크플로우 쿼리 및 실행 도구
- [@pskill9/hn-server](https://github.com/pskill9/hn-server) - 📇 ☁️ news.ycombinator.com(해커 뉴스)의 HTML 콘텐츠를 파싱하고 다양한 유형의 스토리(인기, 신규, 질문, 쇼, 채용)에 대한 구조화된 데이터 제공.
- [@mediar-ai/screenpipe](https://github.com/mediar-ai/screenpipe) - 🎖️ 🦀 🏠 🍎 타임스탬프 인덱싱, SQL/임베딩 저장소, 시맨틱 검색, LLM 기반 기록 분석 및 이벤트 트리거 작업을 통해 화면/오디오를 캡처하는 로컬 우선 시스템 - NextJS 플러그인 생태계를 통해 컨텍스트 인식 AI 에이전트 구축 가능.
- [akseyh/bear-mcp-server](https://github.com/akseyh/bear-mcp-server) - AI가 Bear Notes에서 읽을 수 있도록 허용 (macOS 전용)
- [mcp-server-jfx](https://github.com/quarkiverse/quarkus-mcp-servers/tree/main/jfx) ☕ 🏠 - JavaFX 캔버스에 그리기.
- [hmk/attio-mcp-server](https://github.com/hmk/attio-mcp-server) - 📇 ☁️ AI 클라이언트가 Attio CRM에서 레코드 및 노트를 관리할 수 있도록 허용
- [roychri/mcp-server-asana](https://github.com/roychri/mcp-server-asana) - 📇 ☁️ 이 모델 컨텍스트 프로토콜 서버의 Asana 구현은 Anthropic의 Claude 데스크톱 애플리케이션과 같은 MCP 클라이언트에서 Asana API와 통신할 수 있게 합니다.
- [ws-mcp](https://github.com/nick1udwig/ws-mcp) - WebSocket으로 MCP 서버 래핑 ([kitbitz](https://github.com/nick1udwig/kibitz)와 함께 사용하기 위해)
- [AbdelStark/bitcoin-mcp](https://github.com/AbdelStark/bitcoin-mcp) - ₿ AI 모델이 비트코인과 상호 작용하여 키 생성, 주소 유효성 검사, 트랜잭션 디코딩, 블록체인 쿼리 등을 할 수 있도록 하는 모델 컨텍스트 프로토콜(MCP) 서버.
- [tomekkorbak/strava-mcp-server](https://github.com/tomekkorbak/strava-mcp-server) 🐍 ☁️ - 신체 운동 추적 앱인 Strava용 MCP 서버
- [tomekkorbak/oura-mcp-server](https://github.com/tomekkorbak/oura-mcp-server) 🐍 ☁️ - 수면 추적 앱인 Oura용 MCP 서버
- [rember/rember-mcp](https://github.com/rember/rember-mcp) 📇 🏠 - 채팅에서 배운 내용을 기억하기 위해 [Rember](https://rember.com)에 간격 반복 플래시 카드 만들기.
- [hiromitsusasaki/raindrop-io-mcp-server](https://github.com/hiromitsusasaki/raindrop-io-mcp-server) 📇 ☁️ - LLM이 모델 컨텍스트 프로토콜(MCP)을 사용하여 Raindrop.io 북마크와 상호 작용할 수 있도록 하는 통합.
- [@integromat/make-mcp-server](https://github.com/integromat/make-mcp-server) 🎖️ 📇 🏠 - [Make](https://www.make.com/) 시나리오를 AI 어시스턴트가 호출할 수 있는 도구로 변환합니다.
- [NON906/omniparser-autogui-mcp](https://github.com/NON906/omniparser-autogui-mcp) - 🐍 화면 GUI 자동 조작.
- [kj455/mcp-kibela](https://github.com/kj455/mcp-kibela) - 📇 ☁️ AI 모델이 [Kibela](https://kibe.la/)와 상호 작용할 수 있도록 허용
- [blurrah/mcp-graphql](https://github.com/blurrah/mcp-graphql) 📇 ☁️ - AI가 GraphQL 서버를 쿼리할 수 있도록 허용
- [fotoetienne/gqai](https://github.com/fotoetienne/gqai) 🏎 🏠 - 일반 GraphQL 쿼리/변이 정의 도구를 사용하면 gqai가 자동으로 MCP 서버를 생성합니다.
- [@awkoy/replicate-flux-mcp](https://github.com/awkoy/replicate-flux-mcp) 📇 ☁️ - Replicate의 API를 통해 이미지 생성 기능 제공.
- [kenliao94/mcp-server-rabbitmq](https://github.com/kenliao94/mcp-server-rabbitmq) 🐍 🏠 - RabbitMQ와의 상호 작용(관리 작업, 메시지 인큐/디큐) 가능
- [marcelmarais/Spotify](https://github.com/marcelmarais/spotify-mcp-server) - 📇 🏠 Spotify 재생 제어 및 재생 목록 관리.
- [NakaokaRei/swift-mcp-gui](https://github.com/NakaokaRei/swift-mcp-gui.git) 🏠 🍎 - 키보드 입력, 마우스 이동과 같은 명령을 실행할 수 있는 MCP 서버
- [awwaiid/mcp-server-taskwarrior](https://github.com/awwaiid/mcp-server-taskwarrior) 🏠 📇 - 기본적인 로컬 taskwarrior 사용(작업 추가, 업데이트, 제거)을 위한 MCP 서버
- [tumf/web3-mcp](https://github.com/tumf/web3-mcp) 🐍 ☁️ - Ankr Advanced API를 래핑하는 MCP 서버 구현. 이더리움, BSC, 폴리곤, 아발란체 등 여러 체인에서 NFT, 토큰 및 블록체인 데이터에 접근할 수 있습니다.
- [Alfex4936/kogrammar](https://github.com/Alfex4936/Hangul-MCP) 📇 - 한국어 맞춤법/글자 수 세기 MCP 서버
- [ttommyth/interactive-mcp](https://github.com/ttommyth/interactive-mcp) 📇 🏠 🍎 🪟 🐧 - 로컬 사용자 프롬프트 및 채팅 기능을 MCP 루프에 직접 추가하여 대화형 LLM 워크플로를 활성화합니다.


## 프레임워크

- [FastMCP](https://github.com/jlowin/fastmcp) 🐍 - 파이썬으로 MCP 서버를 구축하기 위한 고수준 프레임워크
- [FastMCP](https://github.com/punkpeye/fastmcp) 📇 - 타입스크립트로 MCP 서버를 구축하기 위한 고수준 프레임워크
- [Foxy Contexts](https://github.com/strowk/foxy-contexts) 🏎️ - 함수형 테스트를 포함하여 선언적으로 MCP 서버를 작성하기 위한 Golang 라이브러리
- [Genkit MCP](https://github.com/firebase/genkit/tree/main/js/plugins/mcp) 📇 – [Genkit](https://github.com/firebase/genkit/tree/main)과 모델 컨텍스트 프로토콜(MCP) 간의 통합 제공.
- [LiteMCP](https://github.com/wong2/litemcp) 📇 - JavaScript/TypeScript로 MCP 서버를 구축하기 위한 고수준 프레임워크
- [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go) 🏎️ - MCP 서버 및 클라이언트 구축을 위한 Golang SDK.
- [mcp-framework](https://github.com/QuantGeekDev/mcp-framework) 📇 - MCP 서버 구축을 위한 빠르고 우아한 타입스크립트 프레임워크
- [mcp-proxy](https://github.com/punkpeye/mcp-proxy) - 📇 `stdio` 전송을 사용하는 MCP 서버를 위한 타입스크립트 SSE 프록시.
- [mcp-rs-template](https://github.com/linux-china/mcp-rs-template) 🦀 - Rust용 MCP CLI 서버 템플릿
- [metoro-io/mcp-golang](https://github.com/metoro-io/mcp-golang) 🏎️ - 타입 안전성에 중점을 둔 MCP 서버 구축을 위한 Golang 프레임워크
- [rectalogic/langchain-mcp](https://github.com/rectalogic/langchain-mcp) 🐍 - LangChain에서 MCP 도구 호출 지원을 제공하여 MCP 도구를 LangChain 워크플로우에 통합 가능.
- [salty-flower/ModelContextProtocol.NET](https://github.com/salty-flower/ModelContextProtocol.NET) #️⃣ 🏠 - NativeAOT 호환성으로 .NET 9에서 MCP 서버를 구축하기 위한 C# SDK ⚡ 🔌
- [spring-projects-experimental/spring-ai-mcp](https://github.com/spring-projects-experimental/spring-ai-mcp) ☕ 🌱 - 다양한 플러그형 전송 옵션으로 MCP 클라이언트 및 MCP 서버 구축을 위한 Java SDK 및 Spring 프레임워크 통합.
- [@marimo-team/codemirror-mcp](https://github.com/marimo-team/codemirror-mcp) - 리소스 언급 및 프롬프트 명령을 위한 모델 컨텍스트 프로토콜(MCP)을 구현하는 CodeMirror 확장 프로그램.
- [quarkiverse/quarkus-mcp-server](https://github.com/quarkiverse/quarkus-mcp-server) ☕ - Quarkus를 사용하여 MCP 서버를 구축하기 위한 Java SDK.
- [lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent) 🤖 🔌 - 간단하고 구성 가능한 패턴을 사용하여 MCP 서버로 효과적인 에이전트 구축.
- [mullerhai/sakura-mcp](https://github.com/mullerhai/sakura-mcp) 🦀 ☕ - modelcontextprotocol.io에서 가져온 MCP 서버 및 MCP 클라이언트로 효과적인 에이전트를 구축하기 위한 Scala MCP 프레임워크.

## 유틸리티

- [boilingdata/mcp-server-and-gw](https://github.com/boilingdata/mcp-server-and-gw) 📇 - 예제 서버 및 MCP 클라이언트가 포함된 MCP stdio에서 HTTP SSE 전송 게이트웨이.
- [isaacwasserman/mcp-langchain-ts-client](https://github.com/isaacwasserman/mcp-langchain-ts-client) 📇 – LangChain.js에서 MCP 제공 도구 사용
- [lightconetech/mcp-gateway](https://github.com/lightconetech/mcp-gateway) 📇 - MCP SSE 서버용 게이트웨이 데모.
- [mark3labs/mcphost](https://github.com/mark3labs/mcphost) 🏎️ -  대규모 언어 모델(LLM)이 모델 컨텍스트 프로토콜(MCP)을 통해 외부 도구와 상호 작용할 수 있도록 하는 CLI 호스트 애플리케이션.
- [MCP-Connect](https://github.com/EvalsOne/MCP-Connect) 📇 - 클라우드 기반 AI 서비스가 HTTP/HTTPS 요청을 통해 로컬 Stdio 기반 MCP 서버에 접근할 수 있도록 하는 작은 도구.
- [SecretiveShell/MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge) 🐍 – 기존의 모든 openAI 호환 클라이언트에서 mcp를 사용하기 위한 openAI 미들웨어 프록시
- [sparfenyuk/mcp-proxy](https://github.com/sparfenyuk/mcp-proxy) 🐍 – MCP stdio에서 SSE 전송 게이트웨이.
- [upsonic/gpt-computer-assistant](https://github.com/Upsonic/gpt-computer-assistant) 🐍 – 수직 AI 에이전트 구축 프레임워크
- [kukapay/whereami-mcp](https://github.com/kukapay/whereami-mcp) 🐍 ☁️ -  현재 IP를 기반으로 현재 위치를 정확히 알려주는 경량 mcp 서버.
- [kukapay/whattimeisit-mcp](https://github.com/kukapay/whattimeisit-mcp) 🐍 ☁️ - 현재 시간을 정확히 알려주는 경량 mcp 서버.
- [kukapay/whoami-mcp](https://github.com/kukapay/whoami-mcp) 🐍 🏠 - 현재 사용자가 누구인지 정확히 알려주는 경량 MCP 서버.
- [flux159/mcp-chat](https://github.com/flux159/mcp-chat) 📇🖥️ - 모든 MCP 서버와 채팅하고 연결하는 CLI 기반 클라이언트. MCP 서버 개발 및 테스트 중에 유용합니다.
- [TBXark/mcp-proxy](https://github.com/TBXark/mcp-proxy) 🏎️ - 여러 MCP 리소스 서버를 단일 http 서버를 통해 집계하고 제공하는 MCP 프록시 서버.

## 팁과 요령

### LLM에게 MCP 사용 방법을 알리는 공식 프롬프트

Claude에게 모델 컨텍스트 프로토콜에 대해 물어보고 싶으신가요?

프로젝트를 생성한 다음 이 파일을 추가하세요:

https://modelcontextprotocol.io/llms-full.txt

Claude에게 MCP 서버 작성 및 작동 방식에 대한 질문해보세요!

- https://www.reddit.com/r/ClaudeAI/comments/1h3g01r/want_to_ask_claude_about_model_context_protocol/

## 스타 히스토리

<a href="https://star-history.com/#punkpeye/awesome-mcp-servers&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date" />
 </picture>
</a>
