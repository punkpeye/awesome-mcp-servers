# Servidores MCP Incríveis [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![ไทย](https://img.shields.io/badge/Thai-Click-blue)](README-th.md)
[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![繁體中文](https://img.shields.io/badge/繁體中文-點擊查看-orange)](README-zh_TW.md)
[![简体中文](https://img.shields.io/badge/简体中文-点击查看-orange)](README-zh.md)
[![日本語](https://img.shields.io/badge/日本語-クリック-青)](README-ja.md)
[![한국어](https://img.shields.io/badge/한국어-클릭-yellow)](README-ko.md)
[![Português Brasileiro](https://img.shields.io/badge/Português_Brasileiro-Clique-green)](README-pt_BR.md)
[![Discord](https://img.shields.io/discord/1312302100125843476?logo=discord&label=discord)](https://glama.ai/mcp/discord)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/mcp?style=flat&logo=reddit&label=subreddit)](https://www.reddit.com/r/mcp/)

Uma lista curada de servidores incríveis do Model Context Protocol (MCP).

* [O que é MCP?](#o-que-é-mcp)
* [Clientes](#clientes)
* [Tutoriais](#tutoriais)
* [Comunidade](#comunidade)
* [Legenda](#legenda)
* [Implementações de Servidores](#implementações-de-servidores)
* [Frameworks](#frameworks)
* [Utilitários](#utilitários)
* [Dicas & Truques](#dicas-e-truques)

## O que é MCP?

[MCP](https://modelcontextprotocol.io/) é um protocolo aberto que permite que modelos de IA interajam de forma segura com recursos locais e remotos através de implementações padronizadas de servidores. Esta lista foca em servidores MCP prontos para produção e experimentais que ampliam os recursos de IA por meio de acesso a arquivos, conexões de banco de dados, integrações de API e outros serviços contextuais.

## Clientes

Confira [awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients/) e [glama.ai/mcp/clients](https://glama.ai/mcp/clients).

> [!TIP]
> [Glama Chat](https://glama.ai/chat) é um cliente de IA multimodal com suporte a MCP & [gateway de IA](https://glama.ai/gateway).

## Tutoriais

* [Introdução Rápida ao Model Context Protocol (MCP)](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
* [Configurar o Aplicativo Desktop Claude para usar um banco de dados SQLite](https://youtu.be/wxCCzo9dGj0)

## Comunidade

* [Reddit r/mcp](https://www.reddit.com/r/mcp)
* [Servidor Discord](https://glama.ai/mcp/discord)

## Legenda

* 🎖️ – implementação oficial
* linguagem de programação
  * 🐍 – código Python
  * 📇 – código TypeScript
  * 🏎️ – código Go
  * 🦀 – código Rust
  * #️⃣ - código C#
  * ☕ - código Java
* escopo
  * ☁️ - Serviço em Nuvem
  * 🏠 - Serviço Local
  * 📟 - Sistemas Embarcados
* sistema operacional
  * 🍎 – Para macOS
  * 🪟 – Para Windows
  * 🐧 - Para Linux

> [!NOTE]
> Confuso sobre Local 🏠 vs Nuvem ☁️?
> * Use local quando o servidor MCP está se comunicando com um software instalado localmente, por exemplo, assumindo o controle do navegador Chrome.
> * Use rede quando o servidor MCP está se comunicando com APIs remotas, por exemplo, API de clima.

## Implementações de Servidores

> [!NOTE]
> Agora temos um [diretório baseado na web](https://glama.ai/mcp/servers) que é sincronizado com o repositório.

* 🔗 - [Agregadores](#agregadores)
* 🎨 - [Arte e Cultura](#arte-e-cultura)
* 🧬 - [Biologia, Medicina e Bioinformática](#biologia-medicina-bioinformatica)
* 📂 - [Automação de Navegadores](#automação-de-navegadores)
* ☁️ - [Plataformas em Nuvem](#plataformas-em-nuvem)
* 👨‍💻 - [Execução de Código](#execução-de-código)
* 🤖 - [Agentes de Codificação](#agentes-de-codificação)
* 🖥️ - [Linha de Comando](#linha-de-comando)
* 💬 - [Comunicação](#comunicação)
* 👤 - [Plataformas de Dados do Cliente](#plataformas-de-dados-do-cliente)
* 🗄️ - [Bancos de Dados](#bancos-de-dados)
* 📊 - [Plataformas de Dados](#plataformas-de-dados)
* 🛠️ - [Ferramentas de Desenvolvimento](#ferramentas-de-desenvolvimento)
* 🧮 - [Ferramentas de Ciência de Dados](#ferramentas-de-ciência-de-dados)
* 📟 - [Sistema Embarcado](#sistema-embarcado)
* 📂 - [Sistemas de Arquivos](#sistemas-de-arquivos)
* 💰 - [Finanças & Fintech](#finanças--fintech)
* 🎮 - [Jogos](#jogos)
* 🧠 - [Conhecimento & Memória](#conhecimento--memória)
* ⚖️ - [Legal](#legal)
* 🗺️ - [Serviços de Localização](#serviços-de-localização)
* 🎯 - [Marketing](#marketing)
* 📊 - [Monitoramento](#monitoramento)
* 🔎 - [Pesquisa & Extração de Dados](#pesquisa--extração-de-dados)
* 🔒 - [Segurança](#segurança)
* 🏃 - [Esportes](#esportes)
* 🎧 - [Suporte & Gestão de Serviços](#suporte--gestão-de-serviços)
* 🌎 - [Serviços de Tradução](#serviços-de-tradução)
* 🚆 - [Viagens & Transporte](#viagens--transporte)
* 🔄 - [Controle de Versão](#controle-de-versão)
* 🛠️ - [Outras Ferramentas e Integrações](#outras-ferramentas-e-integrações)


### 🔗 <a name="agregadores"></a>Agregadores

Servidores para acessar muitos aplicativos e ferramentas por meio de um único servidor MCP.

- [1mcp/agent](https://github.com/1mcp-app/agent) 📇 ☁️ 🏠 🍎 🪟 🐧 - Uma implementação de servidor MCP unificado que agrega vários servidores MCP em um único servidor.
- [julien040/anyquery](https://github.com/julien040/anyquery) 🏎️ 🏠 ☁️ - Consulte mais de 40 aplicativos com um único binário usando SQL. Também pode se conectar ao seu banco de dados compatível com PostgreSQL, MySQL ou SQLite. Local primeiro e privado por design.
- [PipedreamHQ/pipedream](https://github.com/PipedreamHQ/pipedream/tree/master/modelcontextprotocol) ☁️ 🏠 - Conecte-se a 2.500 APIs com mais de 8.000 ferramentas pré-construídas e gerencie servidores para seus usuários, em seu próprio aplicativo.
- [OpenMCP](https://github.com/wegotdocs/open-mcp) 📇 🏠 🍎 🪟 🐧 - Transforme uma API web em um servidor MCP em 10 segundos e adicione-o ao registro de código aberto: https://open-mcp.org
- [VeriTeknik/pluggedin-mcp-proxy](https://github.com/VeriTeknik/pluggedin-mcp-proxy)  📇 🏠 - Um servidor proxy abrangente que combina vários servidores MCP em uma única interface com extensos recursos de visibilidade. Fornece descoberta e gerenciamento de ferramentas, prompts, recursos e modelos em todos os servidores, além de um playground para depuração ao construir servidores MCP.
- [MetaMCP](https://github.com/metatool-ai/metatool-app) 📇 ☁️ 🏠 🍎 🪟 🐧 - MetaMCP é o servidor middleware MCP unificado que gerencia suas conexões MCP com GUI.
- [MCP Access Point](https://github.com/sxhxliang/mcp-access-point)  📇 ☁️ 🏠 🍎 🪟 🐧 - Transforme um API web em um servidor MCP com um clique, sem fazer nenhuma alteração no código.
- [hamflx/imagen3-mcp](https://github.com/hamflx/imagen3-mcp) 📇 🏠 🪟 🍎 🐧 - Uma poderosa ferramenta de geração de imagens usando a API Imagen 3.0 do Google através do MCP. Gere imagens de alta qualidade a partir de prompts de texto com controles avançados de fotografia, artísticos e fotorrealistas.
- [YangLiangwei/PersonalizationMCP](https://github.com/YangLiangwei/PersonalizationMCP) 🐍 ☁️ 🏠 🍎 🪟 🐧 - Servidor MCP abrangente de agregação de dados pessoais com integrações Steam, YouTube, Bilibili, Spotify, Reddit e outras plataformas. Possui autenticação OAuth2, gerenciamento automático de tokens e 90+ ferramentas para acesso a dados de jogos, música, vídeo e plataformas sociais.

### 🎨 <a name="arte-e-cultura"></a>Arte e Cultura

Acesse e explore coleções de arte, patrimônio cultural e bancos de dados de museus. Permite que modelos de IA pesquisem e analisem conteúdo artístico e cultural.

- [abhiemj/manim-mcp-server](https://github.com/abhiemj/manim-mcp-server) 🐍 🏠 🪟 🐧 - Um servidor MCP local que gera animações usando Manim.
- [burningion/video-editing-mcp](https://github.com/burningion/video-editing-mcp) 🐍 - Adicione, Analise, Pesquise e Gere Edições de Vídeo da sua Coleção de Vídeos
- [djalal/quran-mcp-server](https://github.com/djalal/quran-mcp-server) 📇 ☁️ Servidor MCP para interagir com o corpus do Quran.com através da API REST oficial v4.
- [r-huijts/rijksmuseum-mcp](https://github.com/r-huijts/rijksmuseum-mcp) 📇 ☁️ - Integração da API do Rijksmuseum para pesquisa, detalhes e coleções de obras de arte
- [r-huijts/oorlogsbronnen-mcp](https://github.com/r-huijts/oorlogsbronnen-mcp) 📇 ☁️ - Integração da API de Oorlogsbronnen (Fontes de Guerra) para acessar registros históricos, fotografias e documentos da Segunda Guerra Mundial da Holanda (1940-1945)
- [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) 🐍 - Integração de servidor MCP para DaVinci Resolve, fornecendo ferramentas poderosas para edição de vídeo, correção de cores, gerenciamento de mídia e controle de projeto
- [yuna0x0/anilist-mcp](https://github.com/yuna0x0/anilist-mcp) 📇 ☁️ - Um servidor MCP integrando a API do AniList para informações sobre anime e mangá
- [diivi/aseprite-mcp](https://github.com/diivi/aseprite-mcp) 🐍 🏠 - Servidor MCP usando a API do Aseprite para criar pixel art
- [cantian-ai/bazi-mcp](https://github.com/cantian-ai/bazi-mcp) 📇 🏠 ☁️ 🍎 🪟 - Fornece análises abrangentes e precisas de Bazi (Quatro Pilares do Destino)

### 🧬 <a name="biologia-medicina-bioinformatica"></a>Biologia, Medicina e Bioinformática

- [genomoncology/biomcp](https://github.com/genomoncology/biomcp) 🐍 ☁️ - Servidor MCP de pesquisa biomédica fornecendo acesso ao PubMed, ClinicalTrials.gov e MyVariant.info.
- [longevity-genie/biothings-mcp](https://github.com/longevity-genie/biothings-mcp) 🐍 🏠 ☁️ - Servidor MCP para interagir com a API BioThings, incluindo genes, variantes genéticas, medicamentos e informações taxonômicas.
- [longevity-genie/gget-mcp](https://github.com/longevity-genie/gget-mcp) 🐍 🏠 ☁️ - Servidor MCP fornecendo um toolkit poderoso de bioinformática para consultas e análises genômicas, envolvendo a popular biblioteca `gget`.
- [longevity-genie/opengenes-mcp](https://github.com/longevity-genie/opengenes-mcp) 🎖️ 🐍 🏠 ☁️ - Servidor MCP para um banco de dados consultável para pesquisa de envelhecimento e longevidade do projeto OpenGenes.
- [longevity-genie/synergy-age-mcp](https://github.com/longevity-genie/synergy-age-mcp) 🎖️ 🐍 🏠 ☁️ - Servidor MCP para o banco de dados SynergyAge de interações genéticas sinérgicas e antagônicas na longevidade.
- [wso2/fhir-mcp-server](https://github.com/wso2/fhir-mcp-server) 🐍 🏠 ☁️ - Servidor de Protocolo de Contexto de Modelo para APIs de Recursos de Interoperabilidade de Saúde Rápida (FHIR). Fornece integração perfeita com servidores FHIR, permitindo que assistentes de IA pesquisem, recuperem, criem, atualizem e analisem dados clínicos de saúde com suporte de autenticação SMART-on-FHIR.

### 📂 <a name="automação-de-navegadores"></a>Automação de Navegadores

Acesso e recursos de automação de conteúdo web. Permite pesquisar, extrair e processar conteúdo web em formatos amigáveis para IA.

- [BB-fat/browser-use-rs](https://github.com/BB-fat/browser-use-rs) 🦀 - Servidor MCP leve de automação de navegador em Rust, sem dependências externas.
- [34892002/bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js) 📇 🏠 - Um servidor MCP que suporta a pesquisa de conteúdo do Bilibili. Fornece exemplos de integração com LangChain e scripts de teste.
- [automatalabs/mcp-server-playwright](https://github.com/Automata-Labs-team/MCP-Server-Playwright) 🐍 - Um servidor MCP para automação de navegador usando Playwright
- [blackwhite084/playwright-plus-python-mcp](https://github.com/blackwhite084/playwright-plus-python-mcp) 🐍 - Um servidor MCP em python usando Playwright para automação de navegador, mais adequado para LLM
- [browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) 🎖️ 📇 - Automatize interações do navegador na nuvem (por exemplo, navegação web, extração de dados, preenchimento de formulários e mais)
- [browsermcp/mcp](https://github.com/browsermcp/mcp) 📇 🏠 - Automatize seu navegador Chrome local
- [brutalzinn/simple-mcp-selenium](https://github.com/brutalzinn/simple-mcp-selenium) 📇 🏠 - Um servidor MCP Selenium para controlar navegadores usando linguagem natural no Cursor IDE. Perfeito para testes, automação e cenários multiusuário.
- [co-browser/browser-use-mcp-server](https://github.com/co-browser/browser-use-mcp-server) 🐍 - browser-use empacotado como um servidor MCP com transporte SSE. Inclui um dockerfile para executar o chromium em docker + um servidor vnc.
- [executeautomation/playwright-mcp-server](https://github.com/executeautomation/mcp-playwright) 📇 - Um servidor MCP usando Playwright para automação de navegador e raspagem web
- [eyalzh/browser-control-mcp](https://github.com/eyalzh/browser-control-mcp) 📇 🏠 - Um servidor MCP pareado com uma extensão de navegador que permite clientes LLM controlar o navegador do usuário (Firefox).
- [freema/firefox-devtools-mcp](https://github.com/freema/firefox-devtools-mcp) 📇 🏠 - Automação do navegador Firefox via WebDriver BiDi para testes, raspagem e controle do navegador. Suporta interações baseadas em snapshot/UID, monitoramento de rede, captura de console e screenshots.
- [fradser/mcp-server-apple-reminders](https://github.com/FradSer/mcp-server-apple-reminders) 📇 🏠 🍎 - Um servidor MCP para interagir com Lembretes da Apple no macOS
- [getrupt/ashra-mcp](https://github.com/getrupt/ashra-mcp) 📇 🏠 - Extraia dados estruturados de qualquer site. Basta solicitar e obter JSON.
- [kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) 📇 ☁️ - Busque legendas e transcrições do YouTube para análise de IA
- [kimtth/mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing) 🐍 🏠 - Uma implementação `mínima` de servidor/cliente MCP usando Azure OpenAI e Playwright.
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) - Servidor MCP oficial da Microsoft para Playwright, permitindo que LLMs interajam com páginas web através de snapshots de acessibilidade estruturados
- [modelcontextprotocol/server-puppeteer](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/puppeteer) 📇 🏠 - Automação de navegador para raspagem web e interação
- [ndthanhdev/mcp-browser-kit](https://github.com/ndthanhdev/mcp-browser-kit) 📇 🏠 - Um servidor MCP para interagir com navegadores compatíveis com manifest v2.
- [pskill9/web-search](https://github.com/pskill9/web-search) 📇 🏠 - Um servidor MCP que permite pesquisas web gratuitas usando resultados do Google, sem necessidade de chaves de API.
- [recursechat/mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts) 📇 🏠 🍎 - Uma integração de servidor MCP com os Atalhos da Apple

### ☁️ <a name="plataformas-em-nuvem"></a>Plataformas em Nuvem

Integração de serviços de plataforma em nuvem. Permite o gerenciamento e interação com infraestrutura e serviços em nuvem.

- [mrostamii/rancher-mcp-server](https://github.com/mrostamii/rancher-mcp-server) [glama](https://glama.ai/mcp/servers/mrostamii/rancher-mcp-server) 🏎️ ☁️/🏠 - Servidor MCP para o ecossistema Rancher com operações Kubernetes multi-cluster, gestão do Harvester HCI (VMs, armazenamento e redes) e ferramentas de Fleet GitOps.
- [Nebula-Block-Data/nebulablock-mcp-server](https://github.com/Nebula-Block-Data/nebulablock-mcp-server) 📇 🏠 - integra-se com a biblioteca fastmcp para expor toda a gama de funcionalidades da API NebulaBlock como ferramentas acessíveis。
- [4everland/4everland-hosting-mcp](https://github.com/4everland/4everland-hosting-mcp) 🎖️ 📇 🏠 🍎 🐧 - Uma implementação de servidor MCP para 4EVERLAND Hosting permitindo implantação instantânea de código gerado por IA em redes de armazenamento descentralizadas como Greenfield, IPFS e Arweave.
- [qiniu/qiniu-mcp-server](https://github.com/qiniu/qiniu-mcp-server) 🐍 ☁️ - Um MCP construído com produtos Qiniu Cloud, suportando acesso ao Armazenamento Qiniu Cloud, serviços de processamento de mídia, etc.
- [alexbakers/mcp-ipfs](https://github.com/alexbakers/mcp-ipfs) 📇 ☁️ - Upload e manipulação de armazenamento IPFS
- [VmLia/books-mcp-server](https://github.com/VmLia/books-mcp-server) 📇 ☁️ - Este é um servidor MCP usado para consultar livros, e pode ser aplicado em clientes MCP comuns, como Cherry Studio.
- [alexei-led/aws-mcp-server](https://github.com/alexei-led/aws-mcp-server) 🐍 ☁️ - Um servidor leve mas poderoso que permite assistentes de IA executarem comandos AWS CLI, usarem pipes Unix e aplicarem templates de prompt para tarefas comuns da AWS em um ambiente Docker seguro com suporte multi-arquitetura
- [alexei-led/k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server) 🐍 - Um servidor robusto e leve que capacita assistentes de IA para executar com segurança comandos CLI do Kubernetes (`kubectl`, `helm`, `istioctl` e `argocd`) usando pipes Unix em um ambiente Docker seguro com suporte multi-arquitetura.
- [aliyun/alibaba-cloud-ops-mcp-server](https://github.com/aliyun/alibaba-cloud-ops-mcp-server) 🎖️ 🐍 ☁️ - Um servidor MCP que permite que assistentes de IA gerenciem e operem recursos na Alibaba Cloud, com suporte para ECS, monitoramento de nuvem, OOS e outros diversos produtos em nuvem amplamente utilizados.
- [bright8192/esxi-mcp-server](https://github.com/bright8192/esxi-mcp-server) 🐍 ☁️ - Um servidor de gerenciamento VMware ESXi/vCenter baseado em MCP (Model Control Protocol), fornecendo interfaces de API REST simples para gerenciamento de máquinas virtuais.
- [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) 🎖️ 📇 ☁️ - Integração com serviços Cloudflare incluindo Workers, KV, R2 e D1
- [flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) 📇 ☁️/🏠 - Implementação em TypeScript de operações de cluster Kubernetes para pods, deployments, serviços.
- [hardik-id/azure-resource-graph-mcp-server](https://github.com/hardik-id/azure-resource-graph-mcp-server) 📇 ☁️/🏠 - Um servidor de Protocolo de Contexto de Modelo para consultar e analisar recursos do Azure em escala usando o Azure Resource Graph, permitindo que assistentes de IA explorem e monitorem a infraestrutura do Azure.
- [jdubois/azure-cli-mcp](https://github.com/jdubois/azure-cli-mcp) - Um wrapper em torno da linha de comando Azure CLI que permite conversar diretamente com o Azure
- [johnneerdael/netskope-mcp](https://github.com/johnneerdael/netskope-mcp) 🔒 ☁️ - Um MCP para dar acesso a todos os componentes do Netskope Private Access dentro de ambientes Netskope Private Access, incluindo informações detalhadas de configuração e exemplos de LLM sobre uso.
- [portainer/portainer-mcp](https://github.com/portainer/portainer-mcp) 🏎️ ☁️/🏠 - Um poderoso servidor MCP que permite que assistentes de IA interajam de forma integrada com instâncias do Portainer, fornecendo acesso em linguagem natural ao gerenciamento de contêineres, operações de implantação e recursos de monitoramento de infraestrutura.
- [rrmistry/tilt-mcp](https://github.com/rrmistry/tilt-mcp) 🐍 🏠 🍎 🪟 🐧 - Um servidor de Protocolo de Contexto de Modelo que se integra com o Tilt para fornecer acesso programático a recursos, logs e operações de gerenciamento do Tilt para ambientes de desenvolvimento Kubernetes.
- [trilogy-group/aws-pricing-mcp](https://github.com/trilogy-group/aws-pricing-mcp) 🏎️ ☁️/🏠 - Obtenha informações de preços atualizadas do EC2 com uma única chamada. Rápido. Alimentado por um catálogo de preços da AWS pré-analisado.

### 👨‍💻 <a name="execução-de-código"></a>Execução de Código

Servidores de execução de código. Permitem que LLMs executem código em um ambiente seguro, por exemplo, para agentes de codificação.

- [pydantic/pydantic-ai/mcp-run-python](https://github.com/pydantic/pydantic-ai/tree/main/mcp-run-python) 🐍🏠 - Execute código Python em uma sandbox segura via chamadas de ferramentas MCP
- [yepcode/mcp-server-js](https://github.com/yepcode/mcp-server-js) 🎖️ 📇 ☁️ - Execute qualquer código gerado por LLM em um ambiente sandbox seguro e escalável e crie suas próprias ferramentas MCP usando JavaScript ou Python, com suporte completo para pacotes NPM e PyPI

### 🤖 <a name="agentes-de-codificação"></a>Agentes de Codificação

Agentes de codificação completos que permitem LLMs ler, editar e executar código e resolver tarefas gerais de programação de forma completamente autônoma.

- [oraios/serena](https://github.com/oraios/serena)🐍🏠 - Um agente de codificação completo que depende de operações de código simbólico usando servidores de linguagem.
- [ezyang/codemcp](https://github.com/ezyang/codemcp) 🐍🏠 - Agente de codificação com ferramentas básicas de leitura, escrita e linha de comando.

### 🖥️ <a name="linha-de-comando"></a>Linha de Comando

Execute comandos, capture saída e interaja de outras formas com shells e ferramentas de linha de comando.

- [freema/openclaw-mcp](https://github.com/freema/openclaw-mcp) [glama](https://glama.ai/mcp/servers/@freema/openclaw-mcp) 📇 ☁️ 🏠 - Servidor MCP para integração com o assistente de IA [OpenClaw](https://github.com/openclaw/openclaw). Permite que o Claude delegue tarefas a agentes OpenClaw com ferramentas síncronas/assíncronas, autenticação OAuth 2.1 e transporte SSE para Claude.ai.
- [ferrislucas/iterm-mcp](https://github.com/ferrislucas/iterm-mcp) 🖥️ 🛠️ 💬 - Um servidor de Protocolo de Contexto de Modelo que fornece acesso ao iTerm. Você pode executar comandos e fazer perguntas sobre o que você vê no terminal iTerm.
- [g0t4/mcp-server-commands](https://github.com/g0t4/mcp-server-commands) 📇 🏠 - Execute qualquer comando com as ferramentas `run_command` e `run_script`.
- [maxim-saplin/mcp_safe_local_python_executor](https://github.com/maxim-saplin/mcp_safe_local_python_executor) - Interpretador Python seguro baseado no `LocalPythonExecutor` do HF Smolagents
- [MladenSU/cli-mcp-server](https://github.com/MladenSU/cli-mcp-server) 🐍 🏠 - Interface de linha de comando com execução segura e políticas de segurança personalizáveis
- [OthmaneBlial/term_mcp_deepseek](https://github.com/OthmaneBlial/term_mcp_deepseek) 🐍 🏠 - Um Servidor semelhante ao MCP do DeepSeek para Terminal
- [tumf/mcp-shell-server](https://github.com/tumf/mcp-shell-server) - Um servidor de execução segura de comandos shell implementando o Protocolo de Contexto de Modelo (MCP)
- [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) 📇 🏠 🍎 🪟 🐧 - Um canivete suíço que pode gerenciar/executar programas e ler/escrever/pesquisar/editar arquivos de código e texto.

### 💬 <a name="comunicação"></a>Comunicação

Integração com plataformas de comunicação para gerenciamento de mensagens e operações de canais. Permite que modelos de IA interajam com ferramentas de comunicação em equipe.

- [AbdelStark/nostr-mcp](https://github.com/AbdelStark/nostr-mcp) ☁️ - Um servidor MCP Nostr que permite interagir com Nostr, possibilitando a publicação de notas e muito mais.
- [adhikasp/mcp-twikit](https://github.com/adhikasp/mcp-twikit) 🐍 ☁️ - Interaja com pesquisa e timeline do Twitter
- [agentmail-toolkit/mcp](https://github.com/agentmail-to/agentmail-toolkit/tree/main/mcp) 🐍 💬 - Um servidor MCP para criar caixas de entrada instantaneamente para enviar, receber e realizar ações em e-mails. Não somos agentes de IA para e-mail, mas e-mail para Agentes de IA.
- [arpitbatra123/mcp-googletasks](https://github.com/arpitbatra123/mcp-googletasks) 📇 ☁️ - Um servidor MCP para interface com a API do Google Tasks
- [carterlasalle/mac_messages_mcp](https://github.com/carterlasalle/mac_messages_mcp) 🏠 🍎 🚀 - Um servidor MCP que se conecta de forma segura ao seu banco de dados iMessage via Protocolo de Contexto de Modelo (MCP), permitindo que LLMs consultem e analisem conversas do iMessage. Inclui validação robusta de números de telefone, processamento de anexos, gerenciamento de contatos, manipulação de bate-papo em grupo e suporte completo para envio e recebimento de mensagens.
- [chaindead/telegram-mcp](https://github.com/chaindead/telegram-mcp) 🏎️ 🏠 - Integração com a API do Telegram para acessar dados do usuário, gerenciar diálogos (chats, canais, grupos), recuperar mensagens e lidar com status de leitura
- [elie222/inbox-zero](https://github.com/elie222/inbox-zero/tree/main/apps/mcp-server) 🐍 ☁️ - Um servidor MCP para Inbox Zero. Adiciona funcionalidades ao Gmail, como descobrir quais e-mails você precisa responder ou acompanhar.
- [FastAlertNow/mcp-server](https://github.com/FastAlertNow/mcp-server) 🎖️ 📇 ☁️ - Servidor oficial Model Context Protocol (MCP) para FastAlert. Este servidor permite que agentes de IA (como Claude, ChatGPT e Cursor) listem seus canais e enviem notificações diretamente através da API FastAlert.
- [gotoolkits/wecombot](https://github.com/gotoolkits/mcp-wecombot-server.git) 🚀 ☁️ - Uma aplicação servidora MCP que envia vários tipos de mensagens para o robô de grupo WeCom.
- [hannesrudolph/imessage-query-fastmcp-mcp-server](https://github.com/hannesrudolph/imessage-query-fastmcp-mcp-server) 🐍 🏠 🍎 - Um servidor MCP que fornece acesso seguro ao seu banco de dados iMessage através do Protocolo de Contexto de Modelo (MCP), permitindo que LLMs consultem e analisem conversas iMessage com validação adequada de números de telefone e tratamento de anexos
- [jagan-shanmugam/mattermost-mcp-host](https://github.com/jagan-shanmugam/mattermost-mcp-host) 🐍 🏠 - Um servidor MCP junto com um host MCP que fornece acesso a equipes, canais e mensagens do Mattermost. O host MCP é integrado como um bot no Mattermost com acesso a servidores MCP que podem ser configurados.
- [lharries/whatsapp-mcp](https://github.com/lharries/whatsapp-mcp) 🐍 🏎️ - Um servidor MCP para pesquisar suas mensagens pessoais do WhatsApp, contatos e enviar mensagens para indivíduos ou grupos
- [line/line-bot-mcp-server](https://github.com/line/line-bot-mcp-server) 🎖 📇 ☁️ - Servidor MCP para Integrar Contas Oficiais do LINE
- [ztxtxwd/open-feishu-mcp-server](https://github.com/ztxtxwd/open-feishu-mcp-server) 📇 ☁️ 🏠 - Um servidor Model Context Protocol (MCP) com autenticação Feishu OAuth integrada, suportando conexões remotas e fornecendo ferramentas abrangentes de gerenciamento de documentos Feishu incluindo criação de blocos, atualizações de conteúdo e recursos avançados.
- [MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite) 🐍 ☁️ - Integração com Gmail e Google Calendar.
- [jaipandya/producthunt-mcp-server](https://github.com/jaipandya/producthunt-mcp-server) 🐍 🏠 - Servidor MCP para o Product Hunt. Interaja com postagens em tendência, comentários, coleções, usuários e muito mais.
- [Danielpeter-99/calcom-mcp](https://github.com/Danielpeter-99/calcom-mcp) 🐍 🏠 - Servidor MCP para o Cal.com. Gerencie tipos de eventos, crie agendamentos e acesse dados de agendamento do Cal.com por meio de LLMs.
- [areweai/tsgram-mcp](https://github.com/areweai/tsgram-mcp) - TSgram: Telegram + Claude com acesso ao workspace local no seu telefone em TypeScript. Leia, escreva e vibe code em movimento!

### 👤 <a name="plataformas-de-dados-do-cliente"></a>Plataformas de Dados do Cliente

Fornece acesso a perfis de clientes dentro de plataformas de dados de clientes

- [iaptic/mcp-server-iaptic](https://github.com/iaptic/mcp-server-iaptic) 🎖️ 📇 ☁️ - Conecte-se com [iaptic](https://www.iaptic.com) para perguntar sobre Compras de Clientes, dados de Transações e estatísticas de Receita de Aplicativos.
- [OpenDataMCP/OpenDataMCP](https://github.com/OpenDataMCP/OpenDataMCP) 🐍 ☁️ - Conecte qualquer Dado Aberto a qualquer LLM com o Protocolo de Contexto de Modelo.
- [sergehuber/inoyu-mcp-unomi-server](https://github.com/sergehuber/inoyu-mcp-unomi-server) 📇 ☁️ - Um servidor MCP para acessar e atualizar perfis em um servidor CDP Apache Unomi.
- [tinybirdco/mcp-tinybird](https://github.com/tinybirdco/mcp-tinybird) 🐍 ☁️ - Um servidor MCP para interagir com um Workspace Tinybird a partir de qualquer cliente MCP.
- [@antv/mcp-server-chart](https://github.com/antvis/mcp-server-chart) 🎖️ 📇 ☁️ - Um plugin do MCP Server baseado no [AntV](https://github.com/antvis) para gerar gráficos de visualização de dados.
- [hustcc/mcp-echarts](https://github.com/hustcc/mcp-echarts) 📇 🏠 - A ferramenta MCP gera dinamicamente gráficos visuais com sintaxe do [Apache ECharts](https://echarts.apache.org) usando IA.
- [hustcc/mcp-mermaid](https://github.com/hustcc/mcp-mermaid) 📇 🏠 - AI gera dinamicamente gráficos visuais usando a sintaxe [Mermaid](https://mermaid.js.org/) MCP.

### 🗄️ <a name="bancos-de-dados"></a>Bancos de Dados

Acesso seguro a banco de dados com recursos de inspeção de esquema. Permite consultar e analisar dados com controles de segurança configuráveis, incluindo acesso somente leitura.

- [Aiven-Open/mcp-aiven](https://github.com/Aiven-Open/mcp-aiven) - 🐍 ☁️ 🎖️ - Navegue pelos seus [projetos Aiven](https://go.aiven.io/mcp-server) e interaja com os serviços PostgreSQL®, Apache Kafka®, ClickHouse® e OpenSearch®
- [alexanderzuev/supabase-mcp-server](https://github.com/alexander-zuev/supabase-mcp-server) - Servidor MCP Supabase com suporte para execução de consultas SQL e ferramentas de exploração de banco de dados
- [aliyun/alibabacloud-tablestore-mcp-server](https://github.com/aliyun/alibabacloud-tablestore-mcp-server) ☕ 🐍 ☁️ - Serviço MCP para Tablestore, funcionalidades incluem adicionar documentos, busca semântica para documentos com base em vetores e escalares, compatível com RAG e serverless.
- [benborla29/mcp-server-mysql](https://github.com/benborla/mcp-server-mysql) ☁️ 🏠 - Integração com banco de dados MySQL em NodeJS com controles de acesso configuráveis e inspeção de esquema
- [bytebase/dbhub](https://github.com/bytebase/dbhub) 📇 🏠 – Servidor MCP de banco de dados universal que suporta os principais bancos de dados.
- [c4pt0r/mcp-server-tidb](https://github.com/c4pt0r/mcp-server-tidb) 🐍 ☁️ - Integração com banco de dados TiDB com inspeção de esquema e recursos de consulta
- [Canner/wren-engine](https://github.com/Canner/wren-engine) 🐍 🦀 🏠 - O Motor Semântico para Clientes do Protocolo de Contexto de Modelo (MCP) e Agentes de IA
- [centralmind/gateway](https://github.com/centralmind/gateway) 🏎️ 🏠 🍎 🪟 - Servidor MCP e SSE MCP que gera automaticamente API com base no esquema e dados do banco de dados. Suporta PostgreSQL, Clickhouse, MySQL, Snowflake, BigQuery, Supabase
- [chroma-core/chroma-mcp](https://github.com/chroma-core/chroma-mcp) 🎖️ 🐍 ☁️ 🏠 - Servidor MCP do Chroma para acessar instâncias Chroma locais e em nuvem para recursos de recuperação
- [ClickHouse/mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse) 🐍 ☁️ - Integração do banco de dados ClickHouse com inspeção de esquema e recursos de consulta
- [confluentinc/mcp-confluent](https://github.com/confluentinc/mcp-confluent) 🐍 ☁️ - Integração Confluent para interagir com as APIs REST do Confluent Kafka e Confluent Cloud.
- [prisma/mcp](https://github.com/prisma/mcp) 📇 ☁️ 🏠 - Permite que LLMs gerenciem bancos de dados Prisma Postgres (ex.: criar novos bancos de dados e executar migrações ou consultas).
- [subnetmarco/pgmcp](https://github.com/subnetmarco/pgmcp) 🏎️ 🏠 - Consultas PostgreSQL em linguagem natural com streaming automático, segurança somente leitura e compatibilidade universal com bancos de dados.
- [pgtuner_mcp](https://github.com/isdaniel/pgtuner_mcp) 🐍🗄️ - fornece recursos de ajuste de desempenho do PostgreSQL com IA.
- [ydb/ydb-mcp](https://github.com/ydb-platform/ydb-mcp) 🎖️ 🐍 ☁️ – servidor MCP para interagir com bancos de dados [YDB](https://ydb.tech)

### 📊 <a name="plataformas-de-dados"></a>Plataformas de Dados

Plataformas de dados para integração, transformação e orquestração de pipelines de dados.

- [flowcore/mcp-flowcore-platform](https://github.com/flowcore-io/mcp-flowcore-platform) 🎖️📇☁️🏠 - Interaja com Flowcore para realizar ações, ingerir dados, e analisar, fazer referência cruzada e utilizar qualquer dado em seus núcleos de dados ou em núcleos de dados públicos; tudo com linguagem humana.
- [JordiNei/mcp-databricks-server](https://github.com/JordiNeil/mcp-databricks-server) - Conecte-se à API do Databricks, permitindo que LLMs executem consultas SQL, listem trabalhos e obtenham status de trabalho.
- [jwaxman19/qlik-mcp](https://github.com/jwaxman19/qlik-mcp) 📇 ☁️ - Servidor MCP para Qlik Cloud API que permite consultar aplicativos, planilhas e extrair dados de visualizações com suporte abrangente de autenticação e limite de taxa.
- [keboola/keboola-mcp-server](https://github.com/keboola/keboola-mcp-server) - interaja com a Plataforma de Dados Keboola Connection. Este servidor fornece ferramentas para listar e acessar dados da API de Armazenamento Keboola.

### 💻 <a name="ferramentas-de-desenvolvimento"></a>Ferramentas de Desenvolvimento

Ferramentas e integrações que aprimoram o fluxo de trabalho de desenvolvimento e o gerenciamento de ambiente.

- [JamesANZ/system-prompts-mcp-server](https://github.com/JamesANZ/system-prompts-mcp-server) 📇 🏠 🍎 🪟 🐧 - Publica um amplo catálogo de prompts de assistentes de código como ferramentas MCP, com recomendações sensíveis ao modelo e ativação de persona para simular agentes como Cursor ou Devin.
- [21st-dev/Magic-MCP](https://github.com/21st-dev/magic-mcp) - Crie componentes UI refinados inspirados pelos melhores engenheiros de design da 21st.dev.
- [a-25/ios-mcp-code-quality-server](https://github.com/a-25/ios-mcp-code-quality-server) 📇 🏠 🍎 - Servidor de análise de qualidade de código iOS e automação de testes. Fornece execução abrangente de testes Xcode, integração SwiftLint e análise detalhada de falhas. Opera nos modos CLI e servidor MCP para uso direto por desenvolvedores e integração com assistentes de IA.
- [Hypersequent/qasphere-mcp](https://github.com/Hypersequent/qasphere-mcp) 🎖️ 📇 ☁️ - Integração com o sistema de gerenciamento de testes [QA Sphere](https://qasphere.com/), permitindo que LLMs descubram, resumam e interajam com casos de teste diretamente de IDEs com IA
- [admica/FileScopeMCP](https://github.com/admica/FileScopeMCP) 🐍 📇 🦀 - Analisa sua base de código identificando arquivos importantes com base em relacionamentos de dependência. Gera diagramas e pontuações de importância, ajudando assistentes de IA a entender a base de código.
- [ambar/simctl-mcp](https://github.com/ambar/simctl-mcp) 📇 🏠 🍎 Uma implementação de servidor MCP para controle de Simulador iOS.
- [api7/apisix-mcp](https://github.com/api7/apisix-mcp) 🎖️ 📇 🏠 Servidor MCP que oferece suporte à consulta e gerenciamento de todos os recursos no [Apache APISIX](https://github.com/apache/apisix).
- [davidan90/time-node-mcp](https://github.com/davidan90/time-node-mcp) 📇 🏠 - Operações de data e hora com suporte a fuso horário, incluindo fusos horários IANA, conversão de fuso horário e tratamento de horário de verão.
- [endorhq/cli](https://github.com/endorhq/cli) 📇 ☁️ 🏠 🪟 🐧 🍎 - O Endor permite que seus agentes de IA executem serviços como MariaDB, Postgres, Redis, Memcached, Alpine ou Valkey em sandboxes isoladas. Obtenha aplicativos pré-configurados que inicializam em menos de 5 segundos. [Confira nossa documentação](https://docs.endor.dev/mcp/overview/).
- [mhmzdev/Figma-Flutter-MCP](https://github.com/mhmzdev/Figma-Flutter-MCP) 📇 🏠 - Fornece aos agentes de codificação acesso direto aos dados do Figma para ajudá-los a escrever código Flutter para construção de aplicativos, incluindo exportação de recursos, manutenção de widgets e implementações de tela completa.
- [yiwenlu66/PiloTY](https://github.com/yiwenlu66/PiloTY) 🐍 🏠 - Piloto de IA para operações PTY que permite aos agentes controlar terminais interativos com sessões com estado, conexões SSH e gerenciamento de processos em segundo plano
- [lpigeon/ros-mcp-server](https://github.com/lpigeon/ros-mcp-server) 🐍 🏠 🍎 🪟 🐧 - O servidor ROS MCP auxilia no controle de robôs convertendo comandos em linguagem natural do usuário em comandos de controle para ROS ou ROS2.
- [freema/mcp-design-system-extractor](https://github.com/freema/mcp-design-system-extractor) 📇 🏠 - Extrai informações de componentes de sistemas de design Storybook. Fornece HTML, estilos, propriedades, dependências, tokens de tema e metadados de componentes para análise de sistemas de design com IA.
- [HainanZhao/mcp-gitlab-jira](https://github.com/HainanZhao/mcp-gitlab-jira) 📇 ☁️ 🏠 - Servidor MCP unificado para GitLab e Jira: gerencie projetos, merge requests, arquivos, releases e tickets com agentes de IA.
- [gitkraken/gk-cli](https://github.com/gitkraken/gk-cli) 🎖️ 🏎️ 🏠 ☁️ 🍎 🪟 🐧 - Uma CLI para interagir com as APIs do GitKraken. Inclui um servidor MCP via gk mcp que envolve não apenas as APIs do GitKraken, mas também Jira, GitHub, GitLab e outros. Funciona com ferramentas locais e serviços remotos.
- [public-ui/kolibri](https://github.com/public-ui/kolibri) 📇 ☁️ 🏠 - Servidor MCP KoliBri com streaming (NPM: `@public-ui/mcp`) que entrega mais de 200 exemplos, especificações, docs e cenários de componentes web com acessibilidade garantida via endpoint HTTP hospedado ou CLI local `kolibri-mcp`.
- [lpigeon/unitree-go2-mcp-server](https://github.com/lpigeon/unitree-go2-mcp-server) 🐍 🏠 🐧 - O servidor Unitree Go2 MCP é um servidor construído sobre o MCP que permite aos usuários controlar o robô Unitree Go2 usando comandos em linguagem natural interpretados por um modelo de linguagem grande (LLM).
- [veelenga/claude-mermaid](https://github.com/veelenga/claude-mermaid/) 📇 🏠 🍎 🪟 🐧 - Servidor MCP de renderização de diagramas Mermaid para Claude Code com funcionalidade de recarga ao vivo, suportando múltiplos formatos de exportação (SVG, PNG, PDF) e temas.
- [selvage-lab/selvage](https://github.com/selvage-lab/selvage) 🐍 🏠 - Servidor MCP de revisão de código baseado em LLM com extração inteligente de contexto baseada em AST. Suporta Claude, GPT, Gemini e mais de 20 modelos via OpenRouter.

### 🧮 <a name="ferramentas-de-ciência-de-dados"></a>Ferramentas de Ciência de Dados

Integrações e ferramentas desenvolvidas para simplificar a exploração de dados, análise e aprimorar fluxos de trabalho de ciência de dados.

- [ChronulusAI/chronulus-mcp](https://github.com/ChronulusAI/chronulus-mcp) 🐍 ☁️ - Preveja qualquer coisa com agentes de previsão e projeção do Chronulus AI.
- [reading-plus-ai/mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration) 🐍 ☁️ - Permite exploração autônoma de dados em conjuntos de dados baseados em .csv, fornecendo insights inteligentes com esforço mínimo.
- [zcaceres/markdownify-mcp](https://github.com/zcaceres/markdownify-mcp) 📇 🏠 - Um servidor MCP para converter quase qualquer arquivo ou conteúdo web em Markdown
- [jjsantos01/jupyter-notebook-mcp](https://github.com/jjsantos01/jupyter-notebook-mcp) 🐍 🏠 - conecta o Jupyter Notebook ao Claude AI, permitindo que o Claude interaja diretamente e controle Jupyter Notebooks.
- [abhiphile/fermat-mcp](https://github.com/abhiphile/fermat-mcp) 🐍 🏠 🍎 🪟 🐧 - O motor de matemática definitivo que unifica SymPy, NumPy e Matplotlib em um servidor poderoso. Perfeito para desenvolvedores e pesquisadores que precisam de álgebra simbólica, computação numérica e visualização de dados.

### 📟 <a name="sistema-embarcado"></a>Sistema Embarcado

Fornece acesso a documentação e atalhos para trabalhar em dispositivos embarcados.

- [adancurusul/embedded-debugger-mcp](https://github.com/adancurusul/embedded-debugger-mcp) 🦀 📟 - Um servidor de protocolo de contexto de modelo para depuração embarcada com probe-rs - suporta depuração ARM Cortex-M, RISC-V via J-Link, ST-Link e mais
- [adancurusul/serial-mcp-server](https://github.com/adancurusul/serial-mcp-server) 🦀 📟 - Um servidor MCP abrangente para comunicação de porta serial
- [horw/esp-mcp](https://github.com/horw/esp-mcp) 📟 - Fluxo de trabalho para corrigir problemas de compilação em chips da série ESP32 usando ESP-IDF.
- [stack-chan/stack-chan](https://github.com/stack-chan/stack-chan) 📇 📟 - Um robô super kawaii embarcado em M5Stack com JavaScript e funcionalidade de servidor MCP para interações e emoções controladas por IA.

### 📂 <a name="sistemas-de-arquivos"></a>Sistemas de Arquivos

Fornece acesso direto aos sistemas de arquivos locais com permissões configuráveis. Permite que modelos de IA leiam, escrevam e gerenciem arquivos dentro de diretórios especificados.

- [8b-is/smart-tree](https://github.com/8b-is/smart-tree) 🦀 🏠 🍎 🪟 🐧 - Visualização de diretório nativa para IA com análise semântica, formatos ultra-comprimidos para consumo de IA e redução de tokens 10x. Suporta modo quântico-semântico com categorização inteligente de arquivos.
- [cyberchitta/llm-context.py](https://github.com/cyberchitta/llm-context.py) 🐍 🏠 - Compartilhe contexto de código com LLMs via MCP ou área de transferência
- [exoticknight/mcp-file-merger](https://github.com/exoticknight/mcp-file-merger) 🏎️ 🏠 - Ferramenta de mesclagem de arquivos, adequada para limites de comprimento de chat de IA.
- [filesystem@quarkiverse/quarkus-mcp-servers](https://github.com/quarkiverse/quarkus-mcp-servers/tree/main/filesystem) ☕ 🏠 - Um sistema de arquivos que permite navegar e editar arquivos implementado em Java usando Quarkus. Disponível como jar ou imagem nativa.
- [hmk/box-mcp-server](https://github.com/hmk/box-mcp-server) 📇 ☁️ - Integração com Box para listar, ler e pesquisar arquivos
- [mamertofabian/mcp-everything-search](https://github.com/mamertofabian/mcp-everything-search) 🐍 🏠 🪟 - Pesquisa rápida de arquivos no Windows usando o SDK Everything
- [mark3labs/mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server) 🏎️ 🏠 - Implementação em Golang para acesso ao sistema de arquivos local.
- [microsoft/markitdown](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp) 🎖️ 🐍 🏠 - Acesso à ferramenta MCP para MarkItDown -- uma biblioteca que converte vários formatos de arquivo (locais ou remotos) para Markdown para consumo por LLM.
- [modelcontextprotocol/server-filesystem](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/filesystem) 📇 🏠 - Acesso direto ao sistema de arquivos local.
- [modelcontextprotocol/server-google-drive](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive) 📇 ☁️ - Integração com Google Drive para listar, ler e pesquisar arquivos
- [Xuanwo/mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal) 🐍 🏠 ☁️ - Acesse qualquer armazenamento com Apache OpenDAL™

### 💰 <a name="finanças--fintech"></a>Finanças & Fintech

Acesso a dados financeiros e ferramentas de análise. Permite que modelos de IA trabalhem com dados de mercado, plataformas de negociação e informações financeiras.

- [OctagonAI/octagon-mcp-server](https://github.com/OctagonAI/octagon-mcp-server) 🐍 ☁️ - Agentes Octagon AI para integrar dados de mercados privados e públicos
- [anjor/coinmarket-mcp-server](https://github.com/anjor/coinmarket-mcp-server) 🐍 ☁️ - Integração com a API do Coinmarket para buscar listagens e cotações de criptomoedas
- [bankless/onchain-mcp](https://github.com/Bankless/onchain-mcp/) 📇 ☁️ - API Bankless Onchain para interagir com contratos inteligentes, consultar informações de transações e tokens
- [base/base-mcp](https://github.com/base/base-mcp) 🎖️ 📇 ☁️ - Integração com a Rede Base para ferramentas onchain, permitindo interação com a Rede Base e API Coinbase para gerenciamento de carteiras, transferências de fundos, contratos inteligentes e operações DeFi
- [berlinbra/alpha-vantage-mcp](https://github.com/berlinbra/alpha-vantage-mcp) 🐍 ☁️ - Integração com a API Alpha Vantage para buscar informações tanto de ações quanto de criptomoedas
- [hoqqun/stooq-mcp](https://github.com/hoqqun/stooq-mcp) 🦀 ☁️ - Obtenha preços de ações em tempo real do Stooq sem chaves de API. Suporta mercados globais (EUA, Japão, Reino Unido, Alemanha).
- [ahnlabio/bicscan-mcp](https://github.com/ahnlabio/bicscan-mcp) 🎖️ 🐍 ☁️ - Pontuação de risco / participações de ativos de endereço de blockchain EVM (EOA, CA, ENS) e até mesmo nomes de domínio.
- [bitteprotocol/mcp](https://github.com/BitteProtocol/mcp) 📇 - Integração com o Bitte Protocol para executar Agentes de IA em várias blockchains.
- [chargebee/mcp](https://github.com/chargebee/agentkit/tree/main/modelcontextprotocol) 🎖️ 📇 ☁️ - Servidor MCP que conecta agentes de IA à [plataforma Chargebee](https://www.chargebee.com/).
- [debridge-finance/debridge-mcp](https://github.com/debridge-finance/debridge-mcp) [glama](https://glama.ai/mcp/servers/@debridge-finance/de-bridge) 📇 🏠 ☁️ - Swaps cross-chain e bridging entre blockchains EVM e Solana via protocolo deBridge. Permite que agentes de IA descubram rotas otimizadas, avaliem taxas e iniciem negociações sem custódia.
- [Wuye-AI/mcp-server-wuye-ai](https://github.com/wuye-ai/mcp-server-wuye-ai) 🎖️ 📇 ☁️ - Servidor MCP conectado à plataforma CRIC Wuye AI. O CRIC Wuye AI é um assistente inteligente desenvolvido pela CRIC especialmente para o setor de gestão de propriedades.
- [JamesANZ/evm-mcp](https://github.com/JamesANZ/evm-mcp) 📇 ☁️ - Um servidor MCP que fornece acesso completo aos métodos JSON-RPC da Máquina Virtual Ethereum (EVM). Funciona com qualquer provedor de nó compatível com EVM, incluindo Infura, Alchemy, QuickNode, nós locais e muito mais.
- [JamesANZ/prediction-market-mcp](https://github.com/JamesANZ/prediction-market-mcp) 📇 ☁️ - Um servidor MCP que fornece dados de mercado de previsão em tempo real de múltiplas plataformas incluindo Polymarket, PredictIt e Kalshi. Permite que assistentes de IA consultem probabilidades atuais, preços e informações de mercado através de uma interface unificada.
- [JamesANZ/bitcoin-mcp](https://github.com/JamesANZ/bitcoin-mcp) 📇 🏠 - Um servidor MCP que permite que modelos de IA consultem a blockchain Bitcoin.

### 🎮 <a name="jogos"></a>Jogos

Integração com dados relacionados a jogos, motores de jogos e serviços
- [CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity) 📇 #️⃣ 🏠 - Servidor MCP para integração com a Engine de Jogos Unity3d para desenvolvimento de jogos
- [Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp) 📇 🏠 - Um servidor MCP para interagir com o motor de jogos Godot, fornecendo ferramentas para editar, executar, depurar e gerenciar cenas em projetos Godot.
- [pab1ito/chess-mcp](https://github.com/pab1it0/chess-mcp) 🐍 ☁️ - Acesse dados de jogadores do Chess.com, registros de jogos e outras informações públicas através de interfaces MCP padronizadas, permitindo que assistentes de IA pesquisem e analisem informações de xadrez.
- [rishijatia/fantasy-pl-mcp](https://github.com/rishijatia/fantasy-pl-mcp/) 🐍 ☁️ - Um servidor MCP para dados e ferramentas de análise em tempo real do Fantasy Premier League.
- [opgginc/opgg-mcp](https://github.com/opgginc/opgg-mcp) 📇 ☁️ - Acesse dados de jogos em tempo real em títulos populares como League of Legends, TFT e Valorant, oferecendo análises de campeões, calendários de esports, composições meta e estatísticas de personagens.

### 🧠 <a name="conhecimento--memória"></a>Conhecimento & Memória

Armazenamento de memória persistente usando estruturas de grafos de conhecimento. Permite que modelos de IA mantenham e consultem informações estruturadas entre sessões.

- [apecloud/ApeRAG](https://github.com/apecloud/ApeRAG) 🐍 ☁️ 🏠 - Plataforma RAG de nível de produção combinando Graph RAG, busca vetorial e busca de texto completo. A melhor escolha para construir seu próprio Grafo de Conhecimento e para Engenharia de Contexto
- [CheMiguel23/MemoryMesh](https://github.com/CheMiguel23/MemoryMesh) 📇 🏠 - Memória aprimorada baseada em grafos com foco em role-play de IA e geração de histórias
- [graphlit-mcp-server](https://github.com/graphlit/graphlit-mcp-server) 📇 ☁️ - Ingira qualquer coisa do Slack, Discord, sites, Google Drive, Linear ou GitHub em um projeto Graphlit - e então pesquise e recupere conhecimento relevante dentro de um cliente MCP como Cursor, Windsurf ou Cline.
- [hannesrudolph/mcp-ragdocs](https://github.com/hannesrudolph/mcp-ragdocs) 🐍 🏠 - Uma implementação de servidor MCP que fornece ferramentas para recuperar e processar documentação através de pesquisa vetorial, permitindo que assistentes de IA aumentem suas respostas com contexto de documentação relevante
- [jinzcdev/markmap-mcp-server](https://github.com/jinzcdev/markmap-mcp-server) 📇 🏠 - Um servidor MCP construído com [markmap](https://github.com/markmap/markmap) que converte **Markdown** em **mapas mentais** interativos. Suporta exportações em múltiplos formatos (PNG/JPG/SVG), visualização em tempo real no navegador, cópia de Markdown com um clique e recursos de visualização dinâmica.
- [kaliaboi/mcp-zotero](https://github.com/kaliaboi/mcp-zotero) 📇 ☁️ - Um conector para LLMs trabalharem com coleções e fontes no seu Zotero Cloud
- [mcp-summarizer](https://github.com/0xshellming/mcp-summarizer) 📕 ☁️ - Servidor MCP de Resumo IA, Suporte para múltiplos tipos de conteúdo: Texto simples, Páginas web, Documentos PDF, Livros EPUB, Conteúdo HTML
- [mem0ai/mem0-mcp](https://github.com/mem0ai/mem0-mcp) 🐍 🏠 - Um servidor de Protocolo de Contexto de Modelo para Mem0 que ajuda a gerenciar preferências e padrões de codificação, fornecendo ferramentas para armazenar, recuperar e lidar semanticamente com implementações de código, melhores práticas e documentação técnica em IDEs como Cursor e Windsurf
- [modelcontextprotocol/server-memory](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/memory) 📇 🏠 - Sistema de memória persistente baseado em grafo de conhecimento para manter contexto
- [nonatofabio/local-faiss-mcp](https://github.com/nonatofabio/local_faiss_mcp) 🐍 🏠 🍎 🐧 - Database vetorial FAISS local para RAG com ingestão de documentos (PDF/TXT/MD/DOCX), busca semântica, re-ranking e ferramentas CLI
- [pinecone-io/assistant-mcp](https://github.com/pinecone-io/assistant-mcp) 🎖️ 🦀 ☁️ - Conecta-se ao seu Assistente Pinecone e dá ao agente contexto a partir do seu motor de conhecimento.
- [@ragieai/mcp-server](https://github.com/ragieai/ragie-mcp-server) 📇 ☁️ - Recupere contexto da sua base de conhecimento [Ragie](https://www.ragie.ai) (RAG) conectada a integrações como Google Drive, Notion, JIRA e muito mais.
- [JamesANZ/memory-mcp](https://github.com/JamesANZ/memory-mcp) 📇 🏠 - Um servidor MCP que armazena e recupera memórias de múltiplos LLMs usando MongoDB. Fornece ferramentas para salvar, recuperar, adicionar e limpar memórias de conversa com timestamps e identificação de LLM.
- [JamesANZ/cross-llm-mcp](https://github.com/JamesANZ/cross-llm-mcp) 📇 🏠 - Um servidor MCP que permite comunicação entre LLMs e compartilhamento de memória, permitindo que diferentes modelos de IA colaborem e compartilhem contexto entre conversas.
- [topoteretes/cognee](https://github.com/topoteretes/cognee/tree/dev/cognee-mcp) 📇 🏠 - Gerenciador de memória para aplicativos de IA e Agentes usando vários armazenamentos de grafos e vetores e permitindo ingestão de mais de 30 fontes de dados
- [unibaseio/membase-mcp](https://github.com/unibaseio/membase-mcp) 📇 ☁️ - Salve e consulte a memória do seu agente de forma distribuída pelo Membase
- [entanglr/zettelkasten-mcp](https://github.com/entanglr/zettelkasten-mcp) 🐍 🏠 - Um servidor de Protocolo de Contexto de Modelo (MCP) que implementa a metodologia de gestão de conhecimento Zettelkasten, permitindo criar, vincular e pesquisar notas atômicas através de Claude e outros clientes compatíveis com MCP.

### ⚖️ <a name="legal"></a>Legal

Acesso a informações jurídicas, legislação e bancos de dados jurídicos. Permite que modelos de IA pesquisem e analisem documentos jurídicos e informações regulatórias.

- [JamesANZ/us-legal-mcp](https://github.com/JamesANZ/us-legal-mcp) 📇 ☁️ - Um servidor MCP que fornece legislação abrangente dos EUA.

### 🗺️ <a name="serviços-de-localização"></a>Serviços de Localização

Serviços baseados em localização e ferramentas de mapeamento. Permite que modelos de IA trabalhem com dados geográficos, informações meteorológicas e análises baseadas em localização.

- [briandconnelly/mcp-server-ipinfo](https://github.com/briandconnelly/mcp-server-ipinfo) 🐍 ☁️ - Geolocalização de endereço IP e informações de rede usando API IPInfo
- [isdaniel/mcp_weather_server](https://github.com/isdaniel/mcp_weather_server) 🐍 ☁️ - Obter informações meteorológicas da API https://api.open-meteo.com.
- [jagan-shanmugam/open-streetmap-mcp](https://github.com/jagan-shanmugam/open-streetmap-mcp) 🐍 🏠 - Um servidor MCP OpenStreetMap com serviços baseados em localização e dados geoespaciais.
- [kukapay/nearby-search-mcp](https://github.com/kukapay/nearby-search-mcp) 🐍 ☁️ - Um servidor MCP para pesquisas de lugares próximos com detecção de localização baseada em IP.
- [modelcontextprotocol/server-google-maps](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/google-maps) 📇 ☁️ - Integração com Google Maps para serviços de localização, rotas e detalhes de lugares
- [QGIS MCP](https://github.com/jjsantos01/qgis_mcp) - conecta o QGIS Desktop ao Claude AI através do MCP. Esta integração permite criação de projetos assistida por prompt, carregamento de camadas, execução de código e muito mais.
- [SaintDoresh/Weather-MCP-ClaudeDesktop](https://github.com/SaintDoresh/Weather-MCP-ClaudeDesktop.git) 🐍 ☁️ - Uma ferramenta MCP que fornece dados meteorológicos em tempo real, previsões e informações meteorológicas históricas usando a API OpenWeatherMap.
- [rossshannon/Weekly-Weather-mcp](https://github.com/rossshannon/weekly-weather-mcp.git) 🐍 ☁️ - Servidor MCP para previsão meteorológica semanal que retorna 7 dias completos de previsões meteorológicas detalhadas em qualquer lugar do mundo.
- [SecretiveShell/MCP-timeserver](https://github.com/SecretiveShell/MCP-timeserver) 🐍 🏠 - Acesse o horário em qualquer fuso horário e obtenha o horário local atual
- [webcoderz/MCP-Geo](https://github.com/webcoderz/MCP-Geo) 🐍 🏠 - Servidor MCP de geocodificação para nominatim, ArcGIS, Bing

### 🎯 <a name="marketing"></a>Marketing

Ferramentas para criar e editar conteúdo de marketing, trabalhar com meta dados web, posicionamento de produto e guias de edição.

- [AdsMCP/tiktok-ads-mcp-server](https://github.com/AdsMCP/tiktok-ads-mcp-server) 🐍 ☁️ - Um servidor Model Context Protocol para integração com a API do TikTok Ads, permitindo que assistentes de IA gerenciem campanhas, analisem métricas de desempenho, lidem com audiências e criativos através do fluxo de autenticação OAuth.
- [Open Strategy Partners Marketing Tools](https://github.com/open-strategy-partners/osp_marketing_tools) 🐍 🏠 - Um conjunto de ferramentas de marketing da Open Strategy Partners, incluindo estilo de escrita, códigos de edição e criação de mapa de valor de marketing de produto.

### 📊 <a name="monitoramento"></a>Monitoramento

Acesse e analise dados de monitoramento de aplicações. Permite que modelos de IA revisem relatórios de erros e métricas de desempenho.

- [tumf/grafana-loki-mcp](https://github.com/tumf/grafana-loki-mcp) 🐍 🏠 - Um servidor MCP que permite consultar logs do Loki através da API do Grafana.
- [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) 🎖️ 🐍 🏠 ☁️ - Pesquise painéis, investigue incidentes e consulte fontes de dados em sua instância Grafana
- [hyperb1iss/lucidity-mcp](https://github.com/hyperb1iss/lucidity-mcp) 🐍 🏠 - Melhore a qualidade do código gerado por IA através de análise inteligente baseada em prompts em 10 dimensões críticas, de complexidade a vulnerabilidades de segurança
- [inventer-dev/mcp-internet-speed-test](https://github.com/inventer-dev/mcp-internet-speed-test) 🐍 ☁️ - Teste de velocidade de internet com métricas de desempenho de rede incluindo velocidade de download/upload, latência, análise de jitter e detecção de servidor CDN com mapeamento geográfico
- [last9/last9-mcp-server](https://github.com/last9/last9-mcp-server) - Traga facilmente o contexto de produção em tempo real—logs, métricas e traces—para seu ambiente local para corrigir código automaticamente mais rápido
- [metoro-io/metoro-mcp-server](https://github.com/metoro-io/metoro-mcp-server) 🎖️ 🏎️ ☁️ - Consulte e interaja com ambientes kubernetes monitorados por Metoro
- [MindscapeHQ/server-raygun](https://github.com/MindscapeHQ/mcp-server-raygun) 📇 ☁️ - Integração com a API V3 Raygun para relatórios de falhas e monitoramento de usuários reais
- [modelcontextprotocol/server-sentry](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry) 🐍 ☁️ - Integração com Sentry.io para rastreamento de erros e monitoramento de desempenho
- [pydantic/logfire-mcp](https://github.com/pydantic/logfire-mcp) 🎖️ 🐍 ☁️ - Fornece acesso a traces e métricas OpenTelemetry através do Logfire
- [seekrays/mcp-monitor](https://github.com/seekrays/mcp-monitor) 🏎️ 🏠 - Uma ferramenta de monitoramento de sistema que expõe métricas do sistema via Protocolo de Contexto de Modelo (MCP). Esta ferramenta permite que LLMs recuperem informações do sistema em tempo real através de uma interface compatível com MCP (suporta CPU, Memória, Disco, Rede, Host, Processo)

### 🔎 <a name="pesquisa--extração-de-dados"></a>Pesquisa & Extração de Dados

- [0xdaef0f/job-searchoor](https://github.com/0xDAEF0F/job-searchoor) 📇 🏠 - Um servidor MCP para pesquisar vagas de emprego com filtros para data, palavras-chave, opções de trabalho remoto e muito mais.
- [ac3xx/mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi) 📇 ☁️ - Integração com API de pesquisa Kagi
- [andybrandt/mcp-simple-arxiv](https://github.com/andybrandt/mcp-simple-arxiv) - 🐍 ☁️ MCP para LLM pesquisar e ler artigos do arXiv
- [andybrandt/mcp-simple-pubmed](https://github.com/andybrandt/mcp-simple-pubmed) - 🐍 ☁️ MCP para pesquisar e ler artigos médicos / ciências da vida do PubMed.
- [angheljf/nyt](https://github.com/angheljf/nyt) 📇 ☁️ - Pesquise artigos usando a API do NYTimes
- [apify/mcp-server-rag-web-browser](https://github.com/apify/mcp-server-rag-web-browser) 📇 ☁️ - Um servidor MCP para o Ator RAG Web Browser de código aberto da Apify para realizar pesquisas na web, raspar URLs e retornar conteúdo em Markdown.
- [Bigsy/Clojars-MCP-Server](https://github.com/Bigsy/Clojars-MCP-Server) 📇 ☁️ - Servidor MCP Clojars para informações atualizadas de dependências de bibliotecas Clojure
- [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) ☁️ 🐍 - Pesquise artigos de pesquisa do ArXiv
- [chanmeng/google-news-mcp-server](https://github.com/ChanMeng666/server-google-news) 📇 ☁️ - Integração com o Google News com categorização automática de tópicos, suporte multilíngue e recursos abrangentes de pesquisa, incluindo manchetes, histórias e tópicos relacionados através do [SerpAPI](https://serpapi.com/).
- [DappierAI/dappier-mcp](https://github.com/DappierAI/dappier-mcp) 🐍 ☁️ - O servidor MCP da Dappier permite pesquisa web em tempo real rápida e gratuita, além de acesso a dados premium de marcas de mídia confiáveis — notícias, mercados financeiros, esportes, entretenimento, clima e muito mais — para construir agentes de IA poderosos.
- [Pearch-ai/mcp_pearch](https://github.com/Pearch-ai/mcp_pearch) 🎖️ 🐍 ☁️ - O melhor motor de busca de pessoas que reduz o tempo gasto na descoberta de talentos

### 🔒 <a name="segurança"></a>Segurança

- [AIM-Intelligence/AIM-Guard-MCP](https://github.com/AIM-Intelligence/AIM-MCP) 📇 🏠 🍎 🪟 🐧 - Servidor MCP focado em segurança que oferece diretrizes de segurança e análise de conteúdo para agentes de IA.
- [firstorderai/authenticator_mcp](https://github.com/firstorderai/authenticator_mcp) 📇 🏠 🍎 🪟 🐧 – Um servidor MCP (Model Context Protocol) seguro que permite que agentes de IA interajam com o aplicativo autenticador.
- [13bm/GhidraMCP](https://github.com/13bm/GhidraMCP) 🐍 ☕ 🏠 - Servidor MCP para integrar Ghidra com assistentes de IA. Este plugin permite análise binária, fornecendo ferramentas para inspeção de funções, descompilação, exploração de memória e análise de importação/exportação via Protocolo de Contexto de Modelo.
- [atomicchonk/roadrecon_mcp_server](https://github.com/atomicchonk/roadrecon_mcp_server) 🐍 🪟 🏠 Servidor MCP para analisar resultados coletados do ROADrecon na enumeração de inquilino Azure
- [BurtTheCoder/mcp-dnstwist](https://github.com/BurtTheCoder/mcp-dnstwist) 📇 🪟 ☁️ - Servidor MCP para dnstwist, uma poderosa ferramenta de fuzzing DNS que ajuda a detectar typosquatting, phishing e espionagem corporativa.
- [BurtTheCoder/mcp-maigret](https://github.com/BurtTheCoder/mcp-maigret) 📇 🪟 ☁️ - Servidor MCP para maigret, uma poderosa ferramenta OSINT que coleta informações de contas de usuários de várias fontes públicas. Este servidor fornece ferramentas para pesquisar nomes de usuário em redes sociais e analisar URLs.
- [intruder-io/intruder-mcp](https://github.com/intruder-io/intruder-mcp) 🐍 ☁️ - Servidor MCP para acessar o [Intruder](https://www.intruder.io/), ajudando você a identificar, entender e corrigir vulnerabilidades de segurança na sua infraestrutura.
- [joergmichno/clawguard-mcp](https://github.com/joergmichno/clawguard-mcp) ([glama](https://glama.ai/mcp/servers/joergmichno/clawguard-mcp)) 🐍 🏠 - Security scanner for AI agents that detects prompt injections using 42+ regex patterns
- [jtang613/GhidrAssistMCP](https://github.com/jtang613/GhidrAssistMCP) ☕ 🏠 - Um servidor nativo do Model Context Protocol para o Ghidra. Inclui configuração via interface gráfica, registro de logs, 31 ferramentas poderosas e nenhuma dependência externa.

### 🏃 <a name="esportes"></a>Esportes

Ferramentas para acessar dados, resultados e estatísticas relacionados a esportes.

- [mikechao/balldontlie-mcp](https://github.com/mikechao/balldontlie-mcp) 📇 - Servidor MCP que integra a API balldontlie para fornecer informações sobre jogadores, times e jogos da NBA, NFL e MLB
- [r-huijts/firstcycling-mcp](https://github.com/r-huijts/firstcycling-mcp) 📇 ☁️ - Acesse dados de corridas de ciclismo, resultados e estatísticas através de linguagem natural. Os recursos incluem recuperação de listas de partida, resultados de corridas e informações sobre ciclistas de firstcycling.com.
- [r-huijts/strava-mcp](https://github.com/r-huijts/strava-mcp) 📇 ☁️ - Um servidor de Protocolo de Contexto de Modelo (MCP) que se conecta à API Strava, fornecendo ferramentas para acessar dados Strava através de LLMs

### 🎧 <a name="suporte--gestão-de-serviços"></a>Suporte & Gestão de Serviços

Ferramentas para gerenciar suporte ao cliente, gerenciamento de serviços de TI e operações de helpdesk.

- [effytech/freshdesk-mcp](https://github.com/effytech/freshdesk_mcp) 🐍 ☁️ - Servidor MCP que se integra ao Freshdesk, permitindo que modelos de IA interajam com módulos do Freshdesk e realizem várias operações de suporte.
- [nguyenvanduocit/jira-mcp](https://github.com/nguyenvanduocit/jira-mcp) 🏎️ ☁️ - Um conector MCP baseado em Go para Jira que permite assistentes de IA como Claude interagirem com o Atlassian Jira. Esta ferramenta fornece uma interface perfeita para modelos de IA realizarem operações comuns do Jira, incluindo gerenciamento de problemas, planejamento de sprint e transições de fluxo de trabalho.

### 🌎 <a name="serviços-de-tradução"></a>Serviços de Tradução

Ferramentas e serviços de tradução para permitir que assistentes de IA traduzam conteúdo entre diferentes idiomas.

- [translated/lara-mcp](https://github.com/translated/lara-mcp) 🎖️ 📇 ☁️ - Servidor MCP para API Lara Translate, habilitando poderosos recursos de tradução com suporte para detecção de idioma e traduções sensíveis ao contexto.

### 🚆 <a name="viagens--transporte"></a>Viagens & Transporte

Acesso a informações de viagem e transporte. Permite consultar horários, rotas e dados de viagem em tempo real.

- [Airbnb MCP Server](https://github.com/openbnb-org/mcp-server-airbnb) 📇 ☁️ - Fornece ferramentas para pesquisar no Airbnb e obter detalhes de listagens.
- [KyrieTangSheng/mcp-server-nationalparks](https://github.com/KyrieTangSheng/mcp-server-nationalparks) 📇 ☁️ - Integração com a API do Serviço de Parques Nacionais fornecendo as informações mais recentes sobre detalhes de parques, alertas, centros de visitantes, acampamentos e eventos para os Parques Nacionais dos EUA
- [NS Travel Information MCP Server](https://github.com/r-huijts/ns-mcp-server) 📇 ☁️ - Acesse informações de viagem, horários e atualizações em tempo real das Ferrovias Holandesas (NS)
- [pab1it0/tripadvisor-mcp](https://github.com/pab1it0/tripadvisor-mcp) 📇 🐍 - Um servidor MCP que permite que LLMs interajam com a API do Tripadvisor, suportando dados de localização, avaliações e fotos através de interfaces MCP padronizadas

### 🔄 <a name="controle-de-versão"></a>Controle de Versão

Interaja com repositórios Git e plataformas de controle de versão. Permite gerenciamento de repositórios, análise de código, tratamento de pull requests, rastreamento de problemas e outras operações de controle de versão através de APIs padronizadas.

- [adhikasp/mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest) 🐍 🏠 - Leia e analise repositórios GitHub com seu LLM
- [ddukbg/github-enterprise-mcp](https://github.com/ddukbg/github-enterprise-mcp) 📇 ☁️ 🏠 - Servidor MCP para integração com API GitHub Enterprise
- [gitea/gitea-mcp](https://gitea.com/gitea/gitea-mcp) 🎖️ 🏎️ ☁️ 🏠 🍎 🪟 🐧 - Interaja com instâncias Gitea com MCP.
- [kopfrechner/gitlab-mr-mcp](https://github.com/kopfrechner/gitlab-mr-mcp) 📇 ☁️ - Interaja perfeitamente com problemas e solicitações de merge dos seus projetos GitLab.
- [modelcontextprotocol/server-git](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/git) 🐍 🏠 - Operações diretas de repositório Git incluindo leitura, pesquisa e análise de repositórios locais
- [modelcontextprotocol/server-github](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/github) 📇 ☁️ - Integração com a API GitHub para gerenciamento de repositórios, PRs, problemas e mais
- [modelcontextprotocol/server-gitlab](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/gitlab) 📇 ☁️ 🏠 - Integração com a plataforma GitLab para gerenciamento de projetos e operações de CI/CD
- [Tiberriver256/mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops) 📇 ☁️ - Integração com Azure DevOps para gerenciamento de repositórios, itens de trabalho e pipelines.

### 🛠️ <a name="outras-ferramentas-e-integrações"></a>Outras Ferramentas e Integrações

- [2niuhe/plantuml_web](https://github.com/2niuhe/plantuml_web) 🐍 🏠 ☁️ 🍎 🪟 🐧 - Um frontend PlantUML baseado na web com integração de servidor MCP, permitindo geração de imagens PlantUML e validação de sintaxe.
- [2niuhe/qrcode_mcp](https://github.com/2niuhe/qrcode_mcp) 🐍 🏠 🍎 🪟 🐧 - Servidor MCP de geração de código QR que converte qualquer texto (incluindo caracteres chineses) em códigos QR com cores personalizáveis e saída de codificação base64.
- [AbdelStark/bitcoin-mcp](https://github.com/AbdelStark/bitcoin-mcp) - ₿ Um servidor de Protocolo de Contexto de Modelo (MCP) que permite que modelos de IA interajam com Bitcoin, permitindo gerar chaves, validar endereços, decodificar transações, consultar a blockchain e muito mais.
- [akseyh/bear-mcp-server](https://github.com/akseyh/bear-mcp-server) - Permite que a IA leia de suas Notas Bear (somente macOS)
- [allenporter/mcp-server-home-assistant](https://github.com/allenporter/mcp-server-home-assistant) 🐍 🏠 - Exponha todas as intenções de voz do Home Assistant através de um servidor de Protocolo de Contexto de Modelo permitindo controle doméstico.
- [Amazon Bedrock Nova Canvas](https://github.com/zxkane/mcp-server-amazon-bedrock) 📇 ☁️ - Use o modelo Amazon Nova Canvas para geração de imagens.
- [amidabuddha/unichat-mcp-server](https://github.com/amidabuddha/unichat-mcp-server) 🐍/📇 ☁️ - Envie solicitações para OpenAI, MistralAI, Anthropic, xAI, Google AI ou DeepSeek usando o protocolo MCP via ferramenta ou prompts predefinidos. Chave de API do fornecedor necessária
- [fotoetienne/gqai](https://github.com/fotoetienne/gqai) 🏎 🏠 - Use ferramentas regulares de definição de mutação/consulta GraphQL e o gqai gerará automaticamente um servidor MCP para você.
- [ttommyth/interactive-mcp](https://github.com/ttommyth/interactive-mcp) 📇 🏠 🍎 🪟 🐧 - Habilita fluxos de trabalho LLM interativos adicionando prompts de usuário local e recursos de chat diretamente no loop do MCP.
- [growilabs/growi-mcp-server](https://github.com/growilabs/growi-mcp-server) 🎖️ 📇 ☁️ - Servidor MCP oficial para integração com APIs do GROWI.
- [JamesANZ/medical-mcp](https://github.com/JamesANZ/medical-mcp) 📇 🏠 - Um servidor MCP que fornece acesso a informações médicas, bancos de dados de medicamentos e recursos de saúde. Permite que assistentes de IA consultem dados médicos, interações medicamentosas e diretrizes clínicas.

## Frameworks

- [FastMCP](https://github.com/jlowin/fastmcp) 🐍 - Um framework de alto nível para construir servidores MCP em Python
- [FastMCP](https://github.com/punkpeye/fastmcp) 📇 - Um framework de alto nível para construir servidores MCP em TypeScript
- [Foxy Contexts](https://github.com/strowk/foxy-contexts) 🏎️ - Biblioteca Golang para escrever Servidores MCP de forma declarativa com teste funcional incluído
- [gabfr/waha-api-mcp-server](https://github.com/gabfr/waha-api-mcp-server) 📇 - Um servidor MCP com especificações openAPI para usar a API não oficial do WhatsApp (https://waha.devlike.pro/ - também de código aberto: https://github.com/devlikeapro/waha
- [Genkit MCP](https://github.com/firebase/genkit/tree/main/js/plugins/mcp) 📇 – Fornece integração entre [Genkit](https://github.com/firebase/genkit/tree/main) e o Protocolo de Contexto de Modelo (MCP).
- [http4k MCP SDK](https://mcp.http4k.org) 🐍 - SDK Kotlin funcional e testável baseado no popular toolkit Web [http4k](https://http4k.org). Suporta o novo protocolo de streaming HTTP.
- [lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent) 🤖 🔌 - Construa agentes eficazes com servidores MCP usando padrões simples e compostos.
- [LiteMCP](https://github.com/wong2/litemcp) 📇 - Um framework de alto nível para construir servidores MCP em JavaScript/TypeScript
- [marimo-team/codemirror-mcp](https://github.com/marimo-team/codemirror-mcp) - Extensão CodeMirror que implementa o Protocolo de Contexto de Modelo (MCP) para menções de recursos e comandos de prompt.
- [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go) 🏎️ - SDK Golang para construir Servidores e Clientes MCP.
- [mcp-framework](https://github.com/QuantGeekDev/mcp-framework) 📇 - Framework TypeScript rápido e elegante para construir servidores MCP
- [mcp-proxy](https://github.com/punkpeye/mcp-proxy) - 📇 Um proxy SSE para servidores MCP que usam transporte `stdio`.
- [mcp-rs-template](https://github.com/linux-china/mcp-rs-template) 🦀 - Template de servidor MCP CLI para Rust
- [metoro-io/mcp-golang](https://github.com/metoro-io/mcp-golang) 🏎️ - Framework Golang para construir Servidores MCP, focado em segurança de tipos
- [mullerhai/sakura-mcp](https://github.com/mullerhai/sakura-mcp) 🦀 ☕ - Framework MCP Scala para construir agentes eficazes com servidores MCP e clientes MCP derivados do modelcontextprotocol.io.
- [paulotaylor/voyp-mcp](https://github.com/paulotaylor/voyp-mcp) 📇 - VOYP - Servidor MCP de Voz Sobre seu Telefone para fazer chamadas.
- [poem-web/poem-mcpserver](https://github.com/poem-web/poem/tree/master/poem-mcpserver) 🦀 - Implementação de Servidor MCP para Poem.
- [quarkiverse/quarkus-mcp-server](https://github.com/quarkiverse/quarkus-mcp-server) ☕ - SDK Java para construir servidores MCP usando Quarkus.
- [rectalogic/langchain-mcp](https://github.com/rectalogic/langchain-mcp) 🐍 - Fornece suporte a chamadas de ferramentas MCP no LangChain, permitindo a integração de ferramentas MCP em fluxos de trabalho LangChain.
- [ribeirogab/simple-mcp](https://github.com/ribeirogab/simple-mcp) 📇 - Uma biblioteca TypeScript simples para criar servidores MCP.
- [salty-flower/ModelContextProtocol.NET](https://github.com/salty-flower/ModelContextProtocol.NET) #️⃣ 🏠 - Um SDK C# para construir servidores MCP no .NET 9 com compatibilidade NativeAOT ⚡ 🔌
- [spring-ai-mcp](https://github.com/spring-projects-experimental/spring-ai-mcp) ☕ 🌱 - SDK Java e integração com Spring Framework para construir cliente MCP e servidores MCP com várias opções de transporte plugáveis.
- [spring-projects-experimental/spring-ai-mcp](https://github.com/spring-projects-experimental/spring-ai-mcp) ☕ 🌱 - SDK Java e integração com Spring Framework para construir cliente MCP e servidores MCP com várias opções de transporte plugáveis.
- [Template MCP Server](https://github.com/mcpdotdirect/template-mcp-server) 📇 - Uma ferramenta de linha de comando para criar um novo projeto de servidor de Protocolo de Contexto de Modelo com suporte a TypeScript, opções de transporte duplo e uma estrutura extensível
- [sendaifun/solana-mcp-kit](https://github.com/sendaifun/solana-agent-kit/tree/main/examples/agent-kit-mcp-server) - SDK Solana MCP
- [tumf/web3-mcp](https://github.com/tumf/web3-mcp) 🐍 ☁️ - Uma implementação de servidor MCP que envolve a Ankr Advanced API. Acesso a NFT, token e dados de blockchain em várias redes, incluindo Ethereum, BSC, Polygon, Avalanche e mais.

## Utilitários

- [boilingdata/mcp-server-and-gw](https://github.com/boilingdata/mcp-server-and-gw) 📇 - Um gateway de transporte MCP stdio para HTTP SSE com servidor de exemplo e cliente MCP.
- [f/MCPTools](https://github.com/f/mcptools) 🔨 - Uma ferramenta de desenvolvimento em linha de comando para inspecionar e interagir com servidores MCP com recursos extras como mocks e proxies.
- [flux159/mcp-chat](https://github.com/flux159/mcp-chat) 📇🖥️ - Um cliente baseado em CLI para conversar e se conectar com qualquer servidor MCP. Útil durante o desenvolvimento e teste de servidores MCP.
- [isaacwasserman/mcp-langchain-ts-client](https://github.com/isaacwasserman/mcp-langchain-ts-client) 📇 – Use ferramentas fornecidas pelo MCP no LangChain.js
- [kukapay/whattimeisit-mcp](https://github.com/kukapay/whattimeisit-mcp) 🐍 ☁️ - Um servidor mcp leve que diz exatamente que horas são.
- [kukapay/whereami-mcp](https://github.com/kukapay/whereami-mcp) 🐍 ☁️ - Um servidor mcp leve que diz exatamente onde você está com base no seu IP atual.
- [kukapay/whoami-mcp](https://github.com/kukapay/whoami-mcp) 🐍 🏠 - Um servidor MCP leve que diz exatamente quem você é.
- [lightconetech/mcp-gateway](https://github.com/lightconetech/mcp-gateway) 📇 - Uma demonstração de gateway para Servidor MCP SSE.
- [mark3labs/mcphost](https://github.com/mark3labs/mcphost) 🏎️ - Um aplicativo host CLI que permite que Modelos de Linguagem Grande (LLMs) interajam com ferramentas externas através do Protocolo de Contexto de Modelo (MCP).
- [MCP-Connect](https://github.com/EvalsOne/MCP-Connect) 📇 - Uma pequena ferramenta que permite serviços de IA baseados em nuvem acessar servidores MCP locais baseados em Stdio por requisições HTTP/HTTPS.
- [SecretiveShell/MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge) 🐍 – um proxy middleware openAI para usar mcp em qualquer cliente compatível com openAI
- [sparfenyuk/mcp-proxy](https://github.com/sparfenyuk/mcp-proxy) 🐍 – Um gateway de transporte MCP stdio para SSE.
- [TBXark/mcp-proxy](https://github.com/TBXark/mcp-proxy) 🏎️ - Um servidor proxy MCP que agrega e serve vários servidores de recursos MCP através de um único servidor http.
- [upsonic/gpt-computer-assistant](https://github.com/Upsonic/gpt-computer-assistant) 🐍 – framework para construir agente de IA vertical
- [JoshuaSiraj/mcp_auto_register](https://github.com/JoshuaSiraj/mcp_auto_register) 🐍 – ferramenta para automatizar o registro de funções e classes de um pacote python em uma instância FastMCP.

## Dicas e Truques

### Prompt oficial para informar LLMs sobre como usar MCP

Quer perguntar ao Claude sobre o Protocolo de Contexto de Modelo?

Crie um Projeto e adicione este arquivo a ele:

https://modelcontextprotocol.io/llms-full.txt

Agora o Claude pode responder perguntas sobre como escrever servidores MCP e como eles funcionam

- https://www.reddit.com/r/ClaudeAI/comments/1h3g01r/want_to_ask_claude_about_model_context_protocol/

## Histórico de Estrelas

<a href="https://star-history.com/#punkpeye/awesome-mcp-servers&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date" />
 </picture>
</a>
