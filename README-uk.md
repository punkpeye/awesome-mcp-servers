# Дивовижні MCP сервери [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![ไทย](https://img.shields.io/badge/Thai-Click-blue)](README-th.md)
[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![繁體中文](https://img.shields.io/badge/繁體中文-點擊查看-orange)](README-zh_TW.md)
[![简体中文](https://img.shields.io/badge/简体中文-点击查看-orange)](README-zh.md)
[![日本語](https://img.shields.io/badge/日本語-クリック-青)](README-ja.md)
[![한국어](https://img.shields.io/badge/한국어-클릭-yellow)](README-ko.md)
[![Português Brasileiro](https://img.shields.io/badge/Português_Brasileiro-Clique-green)](README-pt_BR.md)
[![Українська](https://img.shields.io/badge/Українська-Натисніть-blue)](README-uk.md)
[![Discord](https://img.shields.io/discord/1312302100125843476?logo=discord&label=discord)](https://glama.ai/mcp/discord)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/mcp?style=flat&logo=reddit&label=subreddit)](https://www.reddit.com/r/mcp/)

Добірний список чудових серверів Model Context Protocol (MCP).

* [Що таке MCP?](#o-que-e-mcp)
* [Клієнти](#clientes)
* [Туторіали](#tutoriais)
* [Спільнота](#comunidade)
* [Легенда](#legenda)
* [Реалізації серверів](#implementacoes-de-servidores)
* [Фреймворки](#frameworks)
* [Утиліти](#utilitarios)
* [Поради та хитрощі](#dicas-e-truques)

## <a name="o-que-e-mcp"></a>Що таке MCP?

[MCP](https://modelcontextprotocol.io/) — це відкритий протокол, який дозволяє ШІ-моделям безпечно взаємодіяти з локальними та віддаленими ресурсами через стандартизовані серверні реалізації. Цей список зосереджений на production-ready та експериментальних MCP-серверах, що розширюють можливості ШІ завдяки доступу до файлів, з'єднанням із базами даних, API-інтеграціям та іншим контекстним сервісам.

## <a name="clientes"></a>Клієнти

Перегляньте [awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients/) і [glama.ai/mcp/clients](https://glama.ai/mcp/clients).

> [!TIP]
> [Glama Chat](https://glama.ai/chat) — мультимодальний ШІ-клієнт із підтримкою MCP та [AI gateway](https://glama.ai/gateway).

## <a name="tutoriais"></a>Туторіали

* [Швидкий старт із Model Context Protocol (MCP)](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
* [Налаштування настільного застосунку Claude для роботи з базою даних SQLite](https://youtu.be/wxCCzo9dGj0)

## <a name="comunidade"></a>Спільнота

* [Reddit r/mcp](https://www.reddit.com/r/mcp)
* [Discord сервер](https://glama.ai/mcp/discord)

## <a name="legenda"></a>Легенда

* 🎖️ – офіційна реалізація
* мова програмування
  * 🐍 – кодова база Python
  * 📇 – кодова база TypeScript
  * 🏎️ – кодова база Go
  * 🦀 – кодова база Rust
  * #️⃣ - кодова база C#
  * ☕ - кодова база Java
* область застосування
  * ☁️ - Хмарний сервіс
  * 🏠 - Локальний сервіс
  * 📟 - Вбудовані системи
* операційна система
  * 🍎 – Для macOS
  * 🪟 – Для Windows
  * 🐧 - Для Linux

> [!NOTE]
> Неясно, чим відрізняється локальний 🏠 від хмарного ☁️?
> * Використовуйте локальний варіант, коли MCP-сервер взаємодіє з локально встановленим ПЗ, наприклад керує браузером Chrome.
> * Використовуйте хмарний варіант, коли MCP-сервер взаємодіє з віддаленими API, наприклад із погодним API.

## <a name="implementacoes-de-servidores"></a>Реалізації серверів

> [!NOTE]
> Тепер у нас є [вебкаталог](https://glama.ai/mcp/servers), синхронізований із репозиторієм.

* 🔗 - [Агрегатори](#agregadores)
* 🎨 - [Мистецтво та культура](#arte-e-cultura)
* 🧬 - [Біологія, медицина та біоінформатика](#biologia-medicina-bioinformatica)
* 📂 - [Автоматизація браузера](#automação-de-navegadores)
* ☁️ - [Хмарні платформи](#plataformas-em-nuvem)
* 👨‍💻 - [Виконання коду](#execução-de-código)
* 🤖 - [Агенти кодування](#agentes-de-codificação)
* 🖥️ - [Командний рядок](#linha-de-comando)
* 💬 - [Комунікація](#comunicação)
* 👤 - [Платформи клієнтських даних](#plataformas-de-dados-do-cliente)
* 🗄️ - [Бази даних](#bancos-de-dados)
* 📊 - [Платформи даних](#plataformas-de-dados)
* 🛠️ - [Інструменти розробки](#ferramentas-de-desenvolvimento)
* 🧮 - [Інструменти data science](#ferramentas-de-ciência-de-dados)
* 📟 - [Вбудовані системи](#sistema-embarcado)
* 📂 - [Файлові системи](#sistemas-de-arquivos)
* 💰 - [Фінанси та FinTech](#finanças--fintech)
* 🎮 - [Ігри](#jogos)
* 🧠 - [Знання та пам'ять](#conhecimento--memória)
* ⚖️ - [Право](#legal)
* 🗺️ - [Геолокаційні сервіси](#serviços-de-localização)
* 🎯 - [Маркетинг](#marketing)
* 📊 - [Моніторинг](#monitoramento)
* 🔎 - [Пошук та видобування даних](#pesquisa--extração-de-dados)
* 🔒 - [Безпека](#segurança)
* 🏃 - [Спорт](#esportes)
* 🎧 - [Підтримка та сервіс-менеджмент](#suporte--gestão-de-serviços)
* 🌎 - [Сервіси перекладу](#serviços-de-tradução)
* 🚆 - [Подорожі та транспорт](#viagens--transporte)
* 🔄 - [Контроль версій](#controle-de-versão)
* 🛠️ - [Інші інструменти та інтеграції](#outras-ferramentas-e-integrações)

### 🔗 <a name="agregadores"></a>Агрегатори

Сервери для доступу до багатьох застосунків та інструментів через один MCP-сервер.

- [1mcp/agent](https://github.com/1mcp-app/agent) 📇 ☁️ 🏠 🍎 🪟 🐧 - Уніфікована реалізація MCP-сервера, яка об'єднує кілька MCP-серверів в один.
- [julien040/anyquery](https://github.com/julien040/anyquery) 🏎️ 🏠 ☁️ - Запитуйте понад 40 додатків за допомогою одного бінарного файлу, використовуючи SQL. Також може підключатися до вашої бази даних, сумісної з PostgreSQL, MySQL або SQLite. Local-first і приватний за дизайном.
- [PipedreamHQ/pipedream](https://github.com/PipedreamHQ/pipedream/tree/master/modelcontextprotocol) ☁️ 🏠 - Підключайтеся до 2 500 API з понад 8 000 попередньо створеними інструментами та керуйте серверами для ваших користувачів у власному додатку.
- [OpenMCP](https://github.com/wegotdocs/open-mcp) 📇 🏠 🍎 🪟 🐧 - Перетворіть веб-API на MCP-сервер за 10 секунд і додайте його до реєстру відкритого коду: https://open-mcp.org
- [VeriTeknik/pluggedin-mcp-proxy](https://github.com/VeriTeknik/pluggedin-mcp-proxy)  📇 🏠 - Комплексний проксі-сервер, який об'єднує кілька MCP-серверів в один інтерфейс з розширеними можливостями видимості. Надає відкриття та керування інструментами, промптами, ресурсами та моделями на всіх серверах, а також майданчик для налагодження при створенні MCP-серверів.
- [MetaMCP](https://github.com/metatool-ai/metatool-app) 📇 ☁️ 🏠 🍎 🪟 🐧 - MetaMCP — це уніфікований проміжний MCP-сервер, що керує вашими MCP-з'єднаннями з GUI.
- [MCP Access Point](https://github.com/sxhxliang/mcp-access-point)  📇 ☁️ 🏠 🍎 🪟 🐧 - Перетворіть веб-API на MCP-сервер за один клік, не вносячи жодних змін у код.
- [hamflx/imagen3-mcp](https://github.com/hamflx/imagen3-mcp) 📇 🏠 🪟 🍎 🐧 - Потужний інструмент генерації зображень за допомогою API Imagen 3.0 від Google через MCP. Генеруйте високоякісні зображення з текстових промптів з розширеними фотографічними, художніми та фотореалістичними контролами.
- [YangLiangwei/PersonalizationMCP](https://github.com/YangLiangwei/PersonalizationMCP) 🐍 ☁️ 🏠 🍎 🪟 🐧 - Комплексний MCP-сервер агрегації персональних даних з інтеграціями Steam, YouTube, Bilibili, Spotify, Reddit та інших платформ. Має OAuth2 автентифікацію, автоматичне керування токенами та 90+ інструментів для доступу до даних ігор, музики, відео та соціальних платформ.

### 🎨 <a name="arte-e-cultura"></a>Мистецтво та культура

Отримуйте доступ до та досліджуйте колекції мистецтва, культурну спадщину та бази даних музеїв. Дозволяє ШІ-моделям шукати та аналізувати художній та культурний контент.

- [abhiemj/manim-mcp-server](https://github.com/abhiemj/manim-mcp-server) 🐍 🏠 🪟 🐧 - Локальний MCP-сервер, що генерує анімації за допомогою Manim.
- [burningion/video-editing-mcp](https://github.com/burningion/video-editing-mcp) 🐍 - Додавайте, Аналізуйте, Шукайте та Генеруйте Монтаж Відео з вашої Колекції Відео
- [djalal/quran-mcp-server](https://github.com/djalal/quran-mcp-server) 📇 ☁️ - MCP-сервер для взаємодії з корпусом Quran.com через офіційний REST API v4.
- [gavxm/ani-mcp](https://github.com/gavxm/ani-mcp) [glama](https://glama.ai/mcp/servers/gavxm/ani-mcp) 📇 🏠 - MCP-сервер для AniList з рекомендаціями на основі смаку, аналізом переглядів, соціальними інструментами та повним керуванням списками.
- [r-huijts/rijksmuseum-mcp](https://github.com/r-huijts/rijksmuseum-mcp) 📇 ☁️ - Інтеграція API Rijksmuseum для пошуку, деталей та колекцій творів мистецтва
- [r-huijts/oorlogsbronnen-mcp](https://github.com/r-huijts/oorlogsbronnen-mcp) 📇 ☁️ - Інтеграція API Oorlogsbronnen (Джерела Війн) для доступу до історичних записів, фотографій та документів другої світової війни в Нідерландах (1940-1945)
- [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) 🐍 - Інтеграція MCP-сервера для DaVinci Resolve, що надає потужні інструменти для монтажу відео, колірної корекції, керування медіа та контролю проекту
- [tasopen/mcp-alphabanana](https://github.com/tasopen/mcp-alphabanana) [glama](https://glama.ai/mcp/servers/@tasopen/mcp-alphabanana) 📇 🏠 🍎 🪟 🐧 - Локальний MCP-сервер для генерації зображень з Google Gemini (Nano Banana 2 / Pro). Підтримує прозорий вихід PNG/WebP, точне зміщення розміру/обрізку, до 14 референсних зображень та грунтування за допомогою Google Search.
- [yuna0x0/anilist-mcp](https://github.com/yuna0x0/anilist-mcp) 📇 ☁️ - MCP-сервер, що інтегрує API AniList для інформації про аніме та мангу
- [diivi/aseprite-mcp](https://github.com/diivi/aseprite-mcp) 🐍 🏠 - MCP-сервер з використанням API Aseprite для створення піксель-арту
- [cantian-ai/bazi-mcp](https://github.com/cantian-ai/bazi-mcp) 📇 🏠 ☁️ 🍎 🪟 - Надає комплексні та точні аналізи Бацзи (Чотири Стовпи Долі)

### 🧬 <a name="biologia-medicina-bioinformatica"></a>Біологія, медицина та біоінформатика

- [genomoncology/biomcp](https://github.com/genomoncology/biomcp) 🐍 ☁️ - MCP-сервер біомедичного пошуку, що надає доступ до PubMed, ClinicalTrials.gov та MyVariant.info.
- [longevity-genie/biothings-mcp](https://github.com/longevity-genie/biothings-mcp) 🐍 🏠 ☁️ - MCP-сервер для взаємодії з API BioThings, включаючи генетичні варіанти, ліки та таксономічну інформацію.
- [longevity-genie/gget-mcp](https://github.com/longevity-genie/gget-mcp) 🐍 🏠 ☁️ - MCP-сервер, що надає потужний біоінформатичний набір інструментів для геномних запитів та аналізів, що обгортає популярну бібліотеку `gget`.
- [longevity-genie/opengenes-mcp](https://github.com/longevity-genie/opengenes-mcp) 🎖️ 🐍 🏠 ☁️ - MCP-сервер для консультуваної бази даних пошуку старісті та довголіття проекту OpenGenes.
- [longevity-genie/synergy-age-mcp](https://github.com/longevity-genie/synergy-age-mcp) 🎖️ 🐍 🏠 ☁️ - MCP-сервер для бази даних SynergyAge синергетичних та антагоністичних генетичних взаємодій у довголітті.
- [wso2/fhir-mcp-server](https://github.com/wso2/fhir-mcp-server) 🐍 🏠 ☁️ - Сервер Model Context Protocol для API FHIR (Fast Healthcare Interoperability Resources). Надає безперебійну інтеграцію з FHIR-серверами, дозволяючи ШІ-асистентам шукати, отримувати, створювати, оновлювати та аналізувати клінічні дані охорони здоров'я з підтримкою автентифікації SMART-on-FHIR.

### 📂 <a name="automação-de-navegadores"></a>Автоматизація браузера

Доступ до та ресурси автоматизації веб-контенту. Дозволяє шукати, витягувати та обробляти веб-контент у форматах, зручних для ШІ.

- [BB-fat/browser-use-rs](https://github.com/BB-fat/browser-use-rs) 🦀 - Легкий MCP-сервер автоматизації браузера на Rust, без зовнішніх залежностей.
- [34892002/bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js) 📇 🏠 - MCP-сервер, що підтримує пошук контенту Bilibili. Надає приклади інтеграції з LangChain та тестові скрипти.
- [automatalabs/mcp-server-playwright](https://github.com/Automata-Labs-team/MCP-Server-Playwright) 🐍 - MCP-сервер для автоматизації браузера за допомогою Playwright
- [blackwhite084/playwright-plus-python-mcp](https://github.com/blackwhite084/playwright-plus-python-mcp) 🐍 - MCP-сервер на Python з використанням Playwright для автоматизації браузера, більш придатний для LLM
- [browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) 🎖️ 📇 - Автоматизуйте взаємодії браузера в хмарі (наприклад, веб-навігація, вилучення даних, заповнення форм тощо)
- [browsermcp/mcp](https://github.com/browsermcp/mcp) 📇 🏠 - Автоматизуйте ваш локальний браузер Chrome
- [brutalzinn/simple-mcp-selenium](https://github.com/brutalzinn/simple-mcp-selenium) 📇 🏠 - MCP-сервер Selenium для керування браузерами за допомогою природної мови в Cursor IDE. Ідеально для тестування, автоматизації та сценаріїв багатьох користувачів.
- [co-browser/browser-use-mcp-server](https://github.com/co-browser/browser-use-mcp-server) 🐍 - browser-use, упакований як MCP-сервер з транспортом SSE. Включає Dockerfile для запуску Chromium в Docker + VNC-сервер.
- [executeautomation/playwright-mcp-server](https://github.com/executeautomation/mcp-playwright) 📇 - MCP-сервер з використанням Playwright для автоматизації браузера та веб-скрапінгу
- [eyalzh/browser-control-mcp](https://github.com/eyalzh/browser-control-mcp) 📇 🏠 - MCP-сервер, спарений з розширенням браузера, що дозволяє клієнтам LLM керувати браузером користувача (Firefox).
- [freema/firefox-devtools-mcp](https://github.com/freema/firefox-devtools-mcp) 📇 🏠 - Автоматизація браузера Firefox через WebDriver BiDi для тестування, скрапінгу та керування браузером. Підтримує інтеракції на основі снпшотів/UID, моніторинг мережі, захват консолі та скріншотів.
- [fradser/mcp-server-apple-reminders](https://github.com/FradSer/mcp-server-apple-reminders) 📇 🏠 🍎 - MCP-сервер для взаємодії з Нагадуваннями Apple на macOS
- [getrupt/ashra-mcp](https://github.com/getrupt/ashra-mcp) 📇 🏠 - Витягуйте структуровані дані з будь-якого сайту. Просто запитайте і отримайте JSON.
- [kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) 📇 ☁️ - Отримуйте субтитри та транскрипції YouTube для ШІ-аналізу
- [kimtth/mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing) 🐍 🏠 - `Мінімальна` реалізація MCP-сервера/клієнта з використанням Azure OpenAI та Playwright.
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) - Офіційний MCP-сервер Microsoft для Playwright, що дозволяє LLM взаємодіяти з веб-сторінками через структуровані снпшоти доступності
- [modelcontextprotocol/server-puppeteer](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/puppeteer) 📇 🏠 - Автоматизація браузера для веб-скрапінгу та взаємодії
- [ndthanhdev/mcp-browser-kit](https://github.com/ndthanhdev/mcp-browser-kit) 📇 🏠 - MCP-сервер для взаємодії з браузерами, сумісними з manifest v2.
- [pskill9/web-search](https://github.com/pskill9/web-search) 📇 🏠 - MCP-сервер, що дозволяє безкоштовний веб-пошук за допомогою результатів Google, без необхідності API-ключів.
- [recursechat/mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts) 📇 🏠 🍎 - Інтеграція MCP-сервера з Скороченнями Apple

### ☁️ <a name="plataformas-em-nuvem"></a>Хмарні платформи

Інтеграція хмарних сервісів платформи. Дозволяє керування та взаємодію з хмарною інфраструктурою та сервісами.

- [mctlhq/mctl-mcp](https://github.com/mctlhq/mctl-mcp) [![mctl-mcp MCP server](https://glama.ai/mcp/servers/mctlhq/mctl-mcp/badges/score.svg)](https://glama.ai/mcp/servers/mctlhq/mctl-mcp) ☁️ - AI-нативна платформа для керування Kubernetes та автоматизованого GitOps (понад 30 інструментів).
- [mrostamii/rancher-mcp-server](https://github.com/mrostamii/rancher-mcp-server) [glama](https://glama.ai/mcp/servers/mrostamii/rancher-mcp-server) 🏎️ ☁️/🏠 - MCP-сервер для екосистеми Rancher з багатоспектровими Kubernetes-операціями, керуванням Harvester HCI (ВМ, сховища, мережі) та інструментами Fleet GitOps.
- [Nebula-Block-Data/nebulablock-mcp-server](https://github.com/Nebula-Block-Data/nebulablock-mcp-server) 📇 🏠 - інтегрується з бібліотекою fastmcp для експозиції всього спектру функціональності API NebulaBlock як доступних інструментів.
- [4everland/4everland-hosting-mcp](https://github.com/4everland/4everland-hosting-mcp) 🎖️ 📇 🏠 🍎 🐧 - Реалізація MCP-сервера для 4EVERLAND Hosting, що дозволяє миттєве розгортання коду, згенерованого ШІ, у децентралізованих мережах зберігання, таких як Greenfield, IPFS та Arweave.
- [qiniu/qiniu-mcp-server](https://github.com/qiniu/qiniu-mcp-server) 🐍 ☁️ - MCP, побудований на продуктах Qiniu Cloud, що підтримує доступ до Qiniu Cloud Storage, медіа-сервісів обробки тощо.
- [alexbakers/mcp-ipfs](https://github.com/alexbakers/mcp-ipfs) 📇 ☁️ - Завантаження та маніпуляція сховищем IPFS
- [VmLia/books-mcp-server](https://github.com/VmLia/books-mcp-server) 📇 ☁️ - Це MCP-сервер, що використовується для запиту книг, і може бути застосовано в поширених клієнтах MCP, таких як Cherry Studio.
- [alexei-led/aws-mcp-server](https://github.com/alexei-led/aws-mcp-server) 🐍 ☁️ - Легкий, але потужний сервер, що дозволяє ШІ-асистентам виконувати команди AWS CLI, використовувати Unix-пайпи та застосовувати шаблони промптів для поширених AWS-завдань у безпечному Docker-середовищі з підтримкою мульти-архітектури
- [alexei-led/k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server) 🐍 - Надійний та легкий сервер, що дає змогу ШІ-асистентам безпечно виконувати CLI-команди Kubernetes (`kubectl`, `helm`, `istioctl` та `argocd`) з використанням Unix-пайпів у безпечному Docker-середовищі з підтримкою мульти-архітектури.
- [aliyun/alibaba-cloud-ops-mcp-server](https://github.com/aliyun/alibaba-cloud-ops-mcp-server) 🎖️ 🐍 ☁️ - MCP-сервер, що дозволяє ШІ-асистентам керувати та експлуатувати ресурси в Alibaba Cloud, з підтримкою ECS, хмарного моніторингу, OOS та інших широко використовуваних хмарних продуктів.
- [bright8192/esxi-mcp-server](https://github.com/bright8192/esxi-mcp-server) 🐍 ☁️ - Сервер для керування VMware ESXi/vCenter на основі MCP (Model Control Protocol), що надає прості REST API інтерфейси для керування віртуальними машинами.
- [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) 🎖️ 📇 ☁️ - Інтеграція з сервісами Cloudflare, включаючи Workers, KV, R2 та D1
- [flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) 📇 ☁️/🏠 - TypeScript-реалізація операцій кластера Kubernetes для подів, деплойментів, сервісів.
- [hardik-id/azure-resource-graph-mcp-server](https://github.com/hardik-id/azure-resource-graph-mcp-server) 📇 ☁️/🏠 - Сервер Model Context Protocol для запиту та аналізу ресурсів Azure у масштабі за допомогою Azure Resource Graph, що дозволяє ШІ-асистентам досліджувати та моніторити інфраструктуру Azure.
- [jdubois/azure-cli-mcp](https://github.com/jdubois/azure-cli-mcp) - Обгортка навколо командного рядка Azure CLI, що дозволяє спілкуватися з Azure безпосередньо
- [johnneerdael/netskope-mcp](https://github.com/johnneerdael/netskope-mcp) 🔒 ☁️ - MCP для надання доступу до всіх компонентів Netskope Private Access всередині середовищ Netskope Private Access, включаючи детальної інформацію про конфігурацію та приклади використання LLM.
- [portainer/portainer-mcp](https://github.com/portainer/portainer-mcp) 🏎️ ☁️/🏠 - Потужний MCP-сервер, що дозволяє ШІ-асистентам безперешкодно взаємодіяти з екземплярами Portainer, надаючи доступ мовою природного стилю до керування контейнерами, операціями розгортання та ресурсів моніторингу інфраструктури.
- [rrmistry/tilt-mcp](https://github.com/rrmistry/tilt-mcp) 🐍 🏠 🍎 🪟 🐧 - Сервер Model Context Protocol, що інтегрується з Tilt для надання програмного доступу до ресурсів, логів та операцій керування Tilt для середовищ розробки Kubernetes.
- [trilogy-group/aws-pricing-mcp](https://github.com/trilogy-group/aws-pricing-mcp) 🏎️ ☁️/🏠 - Отримайте актуальну інформацію про ціни EC2 за один виклик. Швидко. Передбачається попередньо проаналізованим каталогом цін AWS.

### 👨‍💻 <a name="execução-de-código"></a>Виконання коду

Сервери для виконання коду. Дозволяють LLM запускати код у безпечному середовищі, наприклад для агентів кодування.

- [pydantic/pydantic-ai/mcp-run-python](https://github.com/pydantic/pydantic-ai/tree/main/mcp-run-python) 🐍🏠 - Виконує код Python у безпечному пісочниці через виклики інструментів MCP
- [yepcode/mcp-server-js](https://github.com/yepcode/mcp-server-js) 🎖️ 📇 ☁️ - Виконує будь-який код, згенерований LLM, у безпечному та масштабованому середовищі пісочниці та створює власні інструменти MCP за допомогою JavaScript або Python, з повною підтримкою пакетів NPM та PyPI

### 🤖 <a name="agentes-de-codificação"></a>Агенти кодування

Повні агенти кодування, які дозволяють LLM читати, редагувати та виконувати код та вирішувати загальні задачі програмування повністю автономно.

- [oraios/serena](https://github.com/oraios/serena)🐍🏠 - Повний агент кодування, який покладається на операції символічного коду за допомогою серверів мов.
- [ezyang/codemcp](https://github.com/ezyang/codemcp) 🐍🏠 - Агент кодування з базовими інструментами читання, написання та командного рядка.

### 🖥️ <a name="linha-de-comando"></a>Командний рядок

Виконує команди, захоплює вивід та взаємодіє іншими способами з оболонками та інструментами командного рядка.

- [freema/openclaw-mcp](https://github.com/freema/openclaw-mcp) [glama](https://glama.ai/mcp/servers/@freema/openclaw-mcp) 📇 ☁️ 🏠 - MCP-сервер для інтеграції з помічником ШІ [OpenClaw](https://github.com/openclaw/openclaw). Дозволяє Claude делегувати задачі агентам OpenClaw з синхронними/асинхронними інструментами, автентифікацією OAuth 2.1 та транспортом SSE для Claude.ai.
- [ferrislucas/iterm-mcp](https://github.com/ferrislucas/iterm-mcp) 🖥️ 🛠️ 💬 - Сервер для Model Context Protocol, що надає доступ до iTerm. Ви можете виконувати команди та ставити питання про те, що ви бачите в терміналі iTerm.
- [g0t4/mcp-server-commands](https://github.com/g0t4/mcp-server-commands) 📇 🏠 - Виконує будь-яку команду з інструментами `run_command` та `run_script`.
- [maxim-saplin/mcp_safe_local_python_executor](https://github.com/maxim-saplin/mcp_safe_local_python_executor) - Безпечний інтерпретатор Python на основі `LocalPythonExecutor` з HF Smolagents
- [MladenSU/cli-mcp-server](https://github.com/MladenSU/cli-mcp-server) 🐍 🏠 - Інтерфейс командного рядка з безпечним виконанням та налаштовуваними політиками безпеки
- [OthmaneBlial/term_mcp_deepseek](https://github.com/OthmaneBlial/term_mcp_deepseek) 🐍 🏠 - Сервер, схожий на MCP DeepSeek для терміналу
- [tumf/mcp-shell-server](https://github.com/tumf/mcp-shell-server) - Сервер для безпечного виконання команд shell, що реалізує Model Context Protocol (MCP)
- [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) 📇 🏠 🍎 🪟 🐧 - Швейцарський ніж, який може керувати/виконувати програми та читати/писати/шукати/редагувати файли коду та тексту.

### 💬 <a name="comunicação"></a>Комунікація

Інтеграція з платформами комунікації для керування повідомленнями та операціями каналів. Дозволяє ШІ-моделям взаємодіяти з інструментами командної комунікації.

- [AbdelStark/nostr-mcp](https://github.com/AbdelStark/nostr-mcp) ☁️ - MCP-сервер Nostr, що дозволяє взаємодіяти з Nostr, публікувати нотатки та багато іншого.
- [adhikasp/mcp-twikit](https://github.com/adhikasp/mcp-twikit) 🐍 ☁️ - Взаємодіяйте з пошуком та стрічкою Twitter
- [agentmail-toolkit/mcp](https://github.com/agentmail-to/agentmail-toolkit/tree/main/mcp) 🐍 💬 - MCP-сервер для миттєвого створення вхідних скриньок для надсилання, отримання та виконання дій з емейлами. Ми не агенти ШІ для емейлу, а емейл для Агентів ШІ.
- [arpitbatra123/mcp-googletasks](https://github.com/arpitbatra123/mcp-googletasks) 📇 ☁️ - MCP-сервер для інтерфейсу з API Google Tasks
- [carterlasalle/mac_messages_mcp](https://github.com/carterlasalle/mac_messages_mcp) 🏠 🍎 🚀 - MCP-сервер, що безпечно підключається до вашої бази даних iMessage через Model Context Protocol (MCP), дозволяючи LLM запитувати та аналізувати розмови iMessage. Включає надійну валідацію номерів телефонів, обробку вкладень, керування контактами, обробку групових чатів та повну підтримку надсилання та отримання повідомлень.
- [chaindead/telegram-mcp](https://github.com/chaindead/telegram-mcp) 🏎️ 🏠 - Інтеграція з API Telegram для доступу до даних користувача, керування діалогами (чати, канали, групи), отримання повідомлень та обробки статусу прочитання
- [elie222/inbox-zero](https://github.com/elie222/inbox-zero/tree/main/apps/mcp-server) 🐍 ☁️ - MCP-сервер для Inbox Zero. Додає функціональність до Gmail, наприклад, виявлення яких емейлів ви повинні відповісти або відстежувати.
- [FastAlertNow/mcp-server](https://github.com/FastAlertNow/mcp-server) 🎖️ 📇 ☁️ - Офіційний сервер Model Context Protocol (MCP) для FastAlert. Цей сервер дозволяє агентам ШІ (таким як Claude, ChatGPT та Cursor) перелічувати ваші канали та надсилати сповіщення безпосередньо через API FastAlert.
- [gotoolkits/wecombot](https://github.com/gotoolkits/mcp-wecombot-server.git) 🚀 ☁️ - MCP-додаток-сервер, який надсилає різні типи повідомлень для бота групи WeCom.
- [hannesrudolph/imessage-query-fastmcp-mcp-server](https://github.com/hannesrudolph/imessage-query-fastmcp-mcp-server) 🐍 🏠 🍎 - MCP-сервер, що надає безпечний доступ до вашої бази даних iMessage через Model Context Protocol (MCP), дозволяючи LLM запитувати та аналізувати розмови iMessage з належною валідацією номерів телефонів та обробкою вкладень
- [jagan-shanmugam/mattermost-mcp-host](https://github.com/jagan-shanmugam/mattermost-mcp-host) 🐍 🏠 - MCP-сервер разом з хостом MCP, що надає доступ до команд, каналів та повідомлень Mattermost. Хост MCP інтегрований як бот у Mattermost з доступом до серверів MCP, які можна налаштувати.
- [lharries/whatsapp-mcp](https://github.com/lharries/whatsapp-mcp) 🐍 🏎️ - MCP-сервер для пошуку ваших особистих повідомлень WhatsApp, контактів та надсилання повідомлень окремим особам або групам
- [line/line-bot-mcp-server](https://github.com/line/line-bot-mcp-server) 🎖 📇 ☁️ - MCP-сервер для інтеграції офіційних акаунтів LINE
- [ztxtxwd/open-feishu-mcp-server](https://github.com/ztxtxwd/open-feishu-mcp-server) 📇 ☁️ 🏠 - Сервер Model Context Protocol (MCP) з інтегрованою автентифікацією Feishu OAuth, що підтримує віддалені підключення та надає комплексні інструменти керування документами Feishu, включаючи створення блоків, оновлення контенту та розширені функції.
- [MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite) 🐍 ☁️ - Інтеграція з Gmail та Google Calendar.
- [jaipandya/producthunt-mcp-server](https://github.com/jaipandya/producthunt-mcp-server) 🐍 🏠 - MCP-сервер для Product Hunt. Взаємодіяйте з популярними публікаціями, коментарями, колекціями, користувачами та багато іншим.
- [Danielpeter-99/calcom-mcp](https://github.com/Danielpeter-99/calcom-mcp) 🐍 🏠 - MCP-сервер для Cal.com. Керуйте типами подій, створюйте розклади та отримуйте доступ до даних планування Cal.com через LLM.
- [areweai/tsgram-mcp](https://github.com/areweai/tsgram-mcp) - TSgram: Telegram + Claude з доступом до локального робочого простору на вашому телефоні на TypeScript. Читайте, пишіть та vibe-кодьте в дорозі!

### 👤 <a name="plataformas-de-dados-do-cliente"></a>Платформи клієнтських даних

Надає доступ до профілів клієнтів у платформах даних клієнтів

- [iaptic/mcp-server-iaptic](https://github.com/iaptic/mcp-server-iaptic) 🎖️ 📇 ☁️ - Підключіться до [iaptic](https://www.iaptic.com) для запитів про Покупки Клієнтів, дані Транзакцій та статистику Доходу Додатків.
- [OpenDataMCP/OpenDataMCP](https://github.com/OpenDataMCP/OpenDataMCP) 🐍 ☁️ - Підключіть будь-які Відкриті Дані до будь-якого LLM за допомогою Model Context Protocol.
- [sergehuber/inoyu-mcp-unomi-server](https://github.com/sergehuber/inoyu-mcp-unomi-server) 📇 ☁️ - MCP-сервер для доступу та оновлення профілів на сервері CDP Apache Unomi.
- [tinybirdco/mcp-tinybird](https://github.com/tinybirdco/mcp-tinybird) 🐍 ☁️ - MCP-сервер для взаємодії з робочим простором Tinybird з будь-якого клієнта MCP.
- [@antv/mcp-server-chart](https://github.com/antvis/mcp-server-chart) 🎖️ 📇 ☁️ - Плагін MCP-сервера на основі [AntV](https://github.com/antvis) для генерації графіків візуалізації даних.
- [hustcc/mcp-echarts](https://github.com/hustcc/mcp-echarts) 📇 🏠 - MCP-інструмент динамічно генерує візуальні графіки з синтаксисом [Apache ECharts](https://echarts.apache.org) за допомогою ШІ.
- [hustcc/mcp-mermaid](https://github.com/hustcc/mcp-mermaid) 📇 🏠 - ШІ динамічно генерує візуальні графіки за допомогою синтаксису [Mermaid](https://mermaid.js.org/) MCP.

### 🗄️ <a name="bancos-de-dados"></a>Бази даних

Безпечний доступ до баз даних з функціями інспекції схеми. Дозволяє запитувати та аналізувати дані з налаштовуваними контролями безпеки, включаючи доступ лише для читання.

- [Aiven-Open/mcp-aiven](https://github.com/Aiven-Open/mcp-aiven) - 🐍 ☁️ 🎖️ - Переглядайте ваші [проекти Aiven](https://go.aiven.io/mcp-server) та взаємодіяйте з сервісами PostgreSQL®, Apache Kafka®, ClickHouse® та OpenSearch®
- [alexanderzuev/supabase-mcp-server](https://github.com/alexander-zuev/supabase-mcp-server) - MCP-сервер Supabase з підтримкою виконання SQL-запитів та інструментів дослідження баз даних
- [aliyun/alibabacloud-tablestore-mcp-server](https://github.com/aliyun/alibabacloud-tablestore-mcp-server) ☕ 🐍 ☁️ - MCP-сервіс для Tablestore, функції включають додавання документів, семантичний пошук документів на основі векторів і скалярів, сумісний з RAG та serverless.
- [benborla29/mcp-server-mysql](https://github.com/benborla/mcp-server-mysql) ☁️ 🏠 - Інтеграція з базою даних MySQL на NodeJS з налаштовуваними контролями доступу та інспекцією схеми
- [bytebase/dbhub](https://github.com/bytebase/dbhub) 📇 🏠 – Універсальний MCP-сервер баз даних, що підтримує основні бази даних.
- [c4pt0r/mcp-server-tidb](https://github.com/c4pt0r/mcp-server-tidb) 🐍 ☁️ - Інтеграція з базою даних TiDB з інспекцією схеми та функціями запиту
- [Canner/wren-engine](https://github.com/Canner/wren-engine) 🐍 🦀 🏠 - Семантичний Двигун для Клієнтів Model Context Protocol (MCP) та Агентів ШІ
- [centralmind/gateway](https://github.com/centralmind/gateway) 🏎️ 🏠 🍎 🪟 - MCP-сервер та SSE MCP, що автоматично генерує API на основі схеми та даних бази даних. Підтримує PostgreSQL, Clickhouse, MySQL, Snowflake, BigQuery, Supabase
- [chroma-core/chroma-mcp](https://github.com/chroma-core/chroma-mcp) 🎖️ 🐍 ☁️ 🏠 - MCP-сервер Chroma для доступу до локальних та хмарних екземплярів Chroma для функцій пошуку
- [ClickHouse/mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse) 🐍 ☁️ - Інтеграція бази даних ClickHouse з інспекцією схеми та функціями запиту
- [confluentinc/mcp-confluent](https://github.com/confluentinc/mcp-confluent) 🐍 ☁️ - Інтеграція Confluent для взаємодії з REST API Confluent Kafka та Confluent Cloud.
- [prisma/mcp](https://github.com/prisma/mcp) 📇 ☁️ 🏠 - Дозволяє LLM керувати базами даних Prisma Postgres (наприклад, створювати нові бази даних та виконувати міграції або запити).
- [subnetmarco/pgmcp](https://github.com/subnetmarco/pgmcp) 🏎️ 🏠 - PostgreSQL-запити природною мовою з автоматичним стрімінгом, безпекою лише для читання та універсальною сумісністю з базами даних.
- [pgtuner_mcp](https://github.com/isdaniel/pgtuner_mcp) 🐍🗄️ - надає функції налаштування продуктивності PostgreSQL за допомогою ШІ.
- [ydb/ydb-mcp](https://github.com/ydb-platform/ydb-mcp) 🎖️ 🐍 ☁️ – MCP-сервер для взаємодії з базами даних [YDB](https://ydb.tech)

### 📊 <a name="plataformas-de-dados"></a>Платформи даних

Платформи даних для інтеграції, трансформації та оркестрації конвеєрів даних.

- [flowcore/mcp-flowcore-platform](https://github.com/flowcore-io/mcp-flowcore-platform) 🎖️📇☁️🏠 - Взаємодійте з Flowcore для виконання дій, інгастування даних, та аналізу, перехресної перевірки та використання будь-яких даних у ваших ядрах даних або публічних ядрах даних; все людською мовою.
- [JordiNei/mcp-databricks-server](https://github.com/JordiNeil/mcp-databricks-server) - Підключіться до API Databricks, дозволяючи LLM виконувати SQL-запити, перелічувати роботи та отримувати статус робіт.
- [jwaxman19/qlik-mcp](https://github.com/jwaxman19/qlik-mcp) 📇 ☁️ - MCP-сервер для Qlik Cloud API, що дозволяє запитувати додатки, аркуші та витягувати дані з візуалізацій з комплексним підтримкою автентифікації та обмеження частоти.
- [keboola/keboola-mcp-server](https://github.com/keboola/keboola-mcp-server) - взаємодійте з Платформою Даних Keboola Connection. Цей сервер надає інструменти для перелічення та доступу до даних API Зберігання Keboola.

### 💻 <a name="ferramentas-de-desenvolvimento"></a>Інструменти розробки

Інструменти та інтеграції, що покращують робочий процес розробки та керування середовищем.

- [JamesANZ/system-prompts-mcp-server](https://github.com/JamesANZ/system-prompts-mcp-server) 📇 🏠 🍎 🪟 🐧 - Публікує розширений каталог промптів помічників коду як інструменти MCP, з рекомендаціями, чутливими до моделі, та активацією персона для імітації агентів як Cursor або Devin.
- [Kapeli/dash-mcp-server](https://github.com/Kapeli/dash-mcp-server) [![Kapeli/dash-mcp-server MCP server](https://glama.ai/mcp/servers/@Kapeli/dash-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/@Kapeli/dash-mcp-server) 🐍 🏠 🍎 - MCP-сервер для [Dash](https://kapeli.com/dash), браузера документації API для macOS. Миттєвий пошук у більш ніж 200 наборах документації.
- [21st-dev/Magic-MCP](https://github.com/21st-dev/magic-mcp) - Створюйте вишуканий UI-компоненти, натхненні найкращими інженерами дизайну 21st.dev.
- [a-25/ios-mcp-code-quality-server](https://github.com/a-25/ios-mcp-code-quality-server) 📇 🏠 🍎 - Сервер аналізу якості коду iOS та автоматизації тестів. Надає комплексне виконання тестів Xcode, інтеграцію SwiftLint та детальний аналіз збоїв. Працює в режимах CLI та MCP-сервер для прямого використання розробниками та інтеграції з помічниками ШІ.
- [Hypersequent/qasphere-mcp](https://github.com/Hypersequent/qasphere-mcp) 🎖️ 📇 ☁️ - Інтеграція з системою керування тестами [QA Sphere](https://qasphere.com/), що дозволяє LLM виявляти, резюмувати та взаємодіяти з тест-кейсами безпосередньо з IDE з ШІ
- [admica/FileScopeMCP](https://github.com/admica/FileScopeMCP) 🐍 📇 🦀 - Аналізує вашу кодову базу, виявляючи важливі файли на основі залежностей. Генерує діаграми та оцінки важливості, допомагаючи помічникам ШІ зрозуміти кодову базу.
- [ambar/simctl-mcp](https://github.com/ambar/simctl-mcp) 📇 🏠 🍎 Реалізація MCP-сервера для керування симулятором iOS.
- [api7/apisix-mcp](https://github.com/api7/apisix-mcp) 🎖️ 📇 🏠 MCP-сервер, що надає підтримку запиту та керування всіма ресурсами в [Apache APISIX](https://github.com/apache/apisix).
- [davidan90/time-node-mcp](https://github.com/davidan90/time-node-mcp) 📇 🏠 - Операції дати та часу з підтримкою часових поясів, включаючи часові пояси IANA, конвертацію часових поясів та обробку летнього часу.
- [endorhq/cli](https://github.com/endorhq/cli) 📇 ☁️ 🏠 🪟 🐧 🍎 - Endor дозволяє вашим агентам ШІ запускати сервіси як MariaDB, Postgres, Redis, Memcached, Alpine або Valkey в ізольованих пісочницях. Отримайте попередньо налаштовані додатки, що ініціалізуються менш ніж за 5 секунд. [Перевірте нашу документацію](https://docs.endor.dev/mcp/overview/).
- [mhmzdev/Figma-Flutter-MCP](https://github.com/mhmzdev/Figma-Flutter-MCP) 📇 🏠 - Надає агентам кодування прямий доступ до даних Figma, щоб допомогти їм писати код Flutter для створення додатків, включаючи експорт ресурсів, підтримку віджетів та реалізації повноекранних екранів.
- [yiwenlu66/PiloTY](https://github.com/yiwenlu66/PiloTY) 🐍 🏠 - ШІ-пілот для PTY-операцій, що дозволяє агентам керувати інтерактивними терміналами зі станами сесій, SSH-з'єднаннями та керуванням фоновими процесами
- [lpigeon/ros-mcp-server](https://github.com/lpigeon/ros-mcp-server) 🐍 🏠 🍎 🪟 🐧 - MCP-сервер ROS допомагає керувати роботами, перетворюючи команди природної мови користувача на команди керування для ROS або ROS2.
- [freema/mcp-design-system-extractor](https://github.com/freema/mcp-design-system-extractor) 📇 🏠 - Витягує інформацію компонентів систем дизайну Storybook. Надає HTML, стилі, властивості, залежності, токени теми та метадані компонентів для аналізу систем дизайну за допомогою ШІ.
- [HainanZhao/mcp-gitlab-jira](https://github.com/HainanZhao/mcp-gitlab-jira) 📇 ☁️ 🏠 - Уніфікований MCP-сервер для GitLab та Jira: керуйте проектами, merge requests, файлами, релізами та тикетами з агентами ШІ.
- [gitkraken/gk-cli](https://github.com/gitkraken/gk-cli) 🎖️ 🏎️ 🏠 ☁️ 🍎 🪟 🐧 - CLI для взаємодії з API GitKraken. Включає MCP-сервер через gk mcp, який охоплює не лише API GitKraken, а також Jira, GitHub, GitLab та інші. Працює з локальними інструментами та віддаленими сервісами.
- [public-ui/kolibri](https://github.com/public-ui/kolibri) 📇 ☁️ 🏠 - MCP-сервер KoliBri зі стрімінгом (NPM: `@public-ui/mcp`), що надає понад 200 прикладів, специфікацій, документів та сценаріїв веб-компонентів з гарантованою доступністю через розгорнутий HTTP-ендпоінт або локальний CLI `kolibri-mcp`.
- [lpigeon/unitree-go2-mcp-server](https://github.com/lpigeon/unitree-go2-mcp-server) 🐍 🏠 🐧 - MCP-сервер Unitree Go2 — це сервер, побудований на основі MCP, що дозволяє користувачам керувати роботом Unitree Go2 за допомогою команд природної мови, інтерпретованих великою мовною моделлю (LLM).
- [veelenga/claude-mermaid](https://github.com/veelenga/claude-mermaid/) 📇 🏠 🍎 🪟 🐧 - MCP-сервер рендерингу діаграм Mermaid для Claude Code з функціональністю живої перезавантаження, що підтримує кілька форматів експорту (SVG, PNG, PDF) та тем.
- [selvage-lab/selvage](https://github.com/selvage-lab/selvage) 🐍 🏠 - MCP-сервер перевірки коду на основі LLM з інтелектуальним витягуванням контексту на основі AST. Підтримує Claude, GPT, Gemini та понад 20 моделей через OpenRouter.

### 🧮 <a name="ferramentas-de-ciência-de-dados"></a>Інструменти data science

Інтеграції та інструменти, розроблені для спрощення дослідження даних, аналізу та покращення робочих процесів науки про дані.

- [ChronulusAI/chronulus-mcp](https://github.com/ChronulusAI/chronulus-mcp) 🐍 ☁️ - Передбачайте будь-що з агентами передбачення та проєкції Chronulus AI.
- [reading-plus-ai/mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration) 🐍 ☁️ - Дозволяє автономне дослідження даних у наборах даних на основі .csv, надаючи інтелектуальні інсайти з мінімальними зусиллями.
- [zcaceres/markdownify-mcp](https://github.com/zcaceres/markdownify-mcp) 📇 🏠 - MCP-сервер для конвертації майже будь-якого файлу або веб-контенту у Markdown
- [jjsantos01/jupyter-notebook-mcp](https://github.com/jjsantos01/jupyter-notebook-mcp) 🐍 🏠 - підключає Jupyter Notebook до Claude AI, дозволяючи Claude безпосередньо взаємодіяти та керувати Jupyter Notebooks.
- [abhiphile/fermat-mcp](https://github.com/abhiphile/fermat-mcp) 🐍 🏠 🍎 🪟 🐧 - Остаточний математичний двигун, що об'єднує SymPy, NumPy та Matplotlib у один потужний сервер. Ідеально для розробників та дослідників, які потребують символьної алгебри, чисельних обчислень та візуалізації даних.

### 📟 <a name="sistema-embarcado"></a>Вбудовані системи

Надає доступ до документації та скорочень для роботи на вбудованих пристроях.

- [adancurusul/embedded-debugger-mcp](https://github.com/adancurusul/embedded-debugger-mcp) 🦀 📟 - Сервер для протоколу контексту моделі для вбудованої відладки з probe-rs - підтримує відладку ARM Cortex-M, RISC-V через J-Link, ST-Link та інше
- [adancurusul/serial-mcp-server](https://github.com/adancurusul/serial-mcp-server) 🦀 📟 - Комплексний MCP-сервер для комунікації через послідовний порт
- [horw/esp-mcp](https://github.com/horw/esp-mcp) 📟 - Робочий процес для виправлення проблем компіляції в чипах серії ESP32 за допомогою ESP-IDF.
- [stack-chan/stack-chan](https://github.com/stack-chan/stack-chan) 📇 📟 - Супер kawaii робот, вбудований в M5Stack з JavaScript та функціональністю MCP-сервера для ШІ-керованих взаємодій та емоцій.

### 📂 <a name="sistemas-de-arquivos"></a>Файлові системи

Надає прямий доступ до локальних файлових систем із налаштовуваними дозволами. Дозволяє ШІ-моделям читати, писати та керувати файлами всередині вказаних директорій.

- [8b-is/smart-tree](https://github.com/8b-is/smart-tree) 🦀 🏠 🍎 🪟 🐧 - Нативна візуалізація директорії для ШІ з семантичним аналізом, ультра-стислі формати для споживання ШІ та скорочення токенів у 10 разів. Підтримує квантово-семантичний режим з інтелектуальною категоризацією файлів.
- [cyberchitta/llm-context.py](https://github.com/cyberchitta/llm-context.py) 🐍 🏠 - Поділіться контекстом коду з LLM через MCP або буфер обміну
- [exoticknight/mcp-file-merger](https://github.com/exoticknight/mcp-file-merger) 🏎️ 🏠 - Інструмент об'єднання файлів, придатний для обмежень довжини чату ШІ.
- [FI-Mihej/text_file_read_and_refactor_mcp](https://github.com/FI-Mihej/text_file_read_and_refactor_mcp) [![text_file_read_and_refactor_mcp MCP server](https://glama.ai/mcp/servers/FI-Mihej/text_file_read_and_refactor_mcp/badges/score.svg)](https://glama.ai/mcp/servers/FI-Mihej/text_file_read_and_refactor_mcp) 🐍 🏠 🍎 🪟 🐧 - Python MCP-сервер через stdio з високою ефективністю використання токенів, що надає безпечні інструменти для пошуку, читання та рефакторингу текстових файлів. Інструменти автоматично вирішують BOM (Byte Order Mark) та кодування файлу. Інструменти редагування зберігають файли, зберігаючи оригінальне кодування та BOM. `uvx text-file-read-and-refactor-mcp`
- [filesystem@quarkiverse/quarkus-mcp-servers](https://github.com/quarkiverse/quarkus-mcp-servers/tree/main/filesystem) ☕ 🏠 - Файлова система, що дозволяє переглядати та редагувати файли, реалізована на Java з використанням Quarkus. Доступна як jar або нативний образ.
- [hmk/box-mcp-server](https://github.com/hmk/box-mcp-server) 📇 ☁️ - Інтеграція з Box для переліку, читання та пошуку файлів
- [mamertofabian/mcp-everything-search](https://github.com/mamertofabian/mcp-everything-search) 🐍 🏠 🪟 - Швидкий пошук файлів у Windows за допомогою Everything SDK
- [mark3labs/mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server) 🏎️ 🏠 - Реалізація на Golang для доступу до локальної файлової системи.
- [microsoft/markitdown](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp) 🎖️ 🐍 🏠 - Доступ до MCP-інструменту MarkItDown — бібліотеки, що конвертує різні формати файлів (локальних або віддалених) у Markdown для споживання LLM.
- [modelcontextprotocol/server-filesystem](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/filesystem) 📇 🏠 - Прямий доступ до локальної файлової системи.
- [modelcontextprotocol/server-google-drive](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive) 📇 ☁️ - Інтеграція з Google Drive для переліку, читання та пошуку файлів
- [Xuanwo/mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal) 🐍 🏠 ☁️ - Отримуйте доступ до будь-якого сховища з Apache OpenDAL™

### 💰 <a name="finanças--fintech"></a>Фінанси та FinTech

Доступ до фінансових даних та інструментів аналізу. Дозволяє ШІ-моделям працювати з ринковими даними, торговельними платформами та фінансовою інформацією.

- [OctagonAI/octagon-mcp-server](https://github.com/OctagonAI/octagon-mcp-server) 🐍 ☁️ - Агенти Octagon AI для інтеграції даних приватних та публічних ринків
- [anjor/coinmarket-mcp-server](https://github.com/anjor/coinmarket-mcp-server) 🐍 ☁️ - Інтеграція з API CoinMarket для отримання лістингів та котирувань криптовалют
- [bankless/onchain-mcp](https://github.com/Bankless/onchain-mcp/) 📇 ☁️ - API Bankless Onchain для взаємодії з розумними контрактами, запиту інформації про транзакції та токени
- [base/base-mcp](https://github.com/base/base-mcp) 🎖️ 📇 ☁️ - Інтеграція з мережею Base для onchain-інструментів, що дозволяє взаємодію з мережею Base та API Coinbase для управління гаманцями, переказування коштів, розумними контрактами та DeFi-операціями
- [berlinbra/alpha-vantage-mcp](https://github.com/berlinbra/alpha-vantage-mcp) 🐍 ☁️ - Інтеграція з API Alpha Vantage для отримання інформації як про акції, так і про криптовалюти
- [hoqqun/stooq-mcp](https://github.com/hoqqun/stooq-mcp) 🦀 ☁️ - Отримуйте ціни на акції в реальному часі від Stooq без ключів API. Підтримує глобальні ринки (США, Японія, Велика Британія, Німеччина).
- [ahnlabio/bicscan-mcp](https://github.com/ahnlabio/bicscan-mcp) 🎖️ 🐍 ☁️ - Оцінка ризику / активів адреси блокчейну EVM (EOA, CA, ENS) та навіть доменних імен.
- [bitteprotocol/mcp](https://github.com/BitteProtocol/mcp) 📇 - Інтеграція з протоколом Bitte для виконання агентів ШІ в різних блокчейнах.
- [chargebee/mcp](https://github.com/chargebee/agentkit/tree/main/modelcontextprotocol) 🎖️ 📇 ☁️ - MCP-сервер, що підключає агентів ШІ до [платформи Chargebee](https://www.chargebee.com/).
- [debridge-finance/debridge-mcp](https://github.com/debridge-finance/debridge-mcp) [glama](https://glama.ai/mcp/servers/@debridge-finance/de-bridge) 📇 🏠 ☁️ - Cross-chain свапи та мостування між EVM-блокчейнами та Solana через протокол deBridge. Дозволяє агентам ШІ знаходити оптимізовані маршрути, оцінювати комісії та ініціювати необідманні угоди.
- [Wuye-AI/mcp-server-wuye-ai](https://github.com/wuye-ai/mcp-server-wuye-ai) 🎖️ 📇 ☁️ - MCP-сервер, підключений до платформи CRIC Wuye AI. CRIC Wuye AI — це інтелектуальний помічник, розроблений CRIC спеціально для сектору управління нерухомістю.
- [JamesANZ/evm-mcp](https://github.com/JamesANZ/evm-mcp) 📇 ☁️ - MCP-сервер, що надає повний доступ до методів JSON-RPC машини віртуальної Ethereum (EVM). Працює з будь-яким провайдером вузла, сумісним з EVM, включаючи Infura, Alchemy, QuickNode, локальні вузли та багато інших.
- [JamesANZ/prediction-market-mcp](https://github.com/JamesANZ/prediction-market-mcp) 📇 ☁️ - MCP-сервер, що надає дані ринку прогнозування в реальному часі з декількох платформ, включаючи Polymarket, PredictIt та Kalshi. Дозволяє помічникам ШІ запитувати поточні ймовірності, ціни та інформацію про ринок через уніфікований інтерфейс.
- [JamesANZ/bitcoin-mcp](https://github.com/JamesANZ/bitcoin-mcp) 📇 🏠 - MCP-сервер, що дозволяє моделям ШІ запитувати блокчейн Bitcoin.

### 🎮 <a name="jogos"></a>Ігри

Інтеграція з даними, пов'язаними з іграми, ігровими движками та сервісами

- [CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity) 📇 #️⃣ 🏠 - MCP-сервер для інтеграції з ігровим движком Unity3d для розробки ігор
- [Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp) 📇 🏠 - MCP-сервер для взаємодії з ігровим движком Godot, що надає інструменти для редагування, запуску, налагодження та керування сценами в проєктах Godot.
- [pab1ito/chess-mcp](https://github.com/pab1it0/chess-mcp) 🐍 ☁️ - Отримуйте доступ до даних гравців Chess.com, записів ігор та іншої публічної інформації через стандартизовані інтерфейси MCP, що дозволяє помічникам ШІ досліджувати та аналізувати шахову інформацію.
- [rishijatia/fantasy-pl-mcp](https://github.com/rishijatia/fantasy-pl-mcp/) 🐍 ☁️ - MCP-сервер для даних та інструментів аналізу в реальному часі Fantasy Premier League.
- [opgginc/opgg-mcp](https://github.com/opgginc/opgg-mcp) 📇 ☁️ - Отримуйте доступ до ігрових даних в реальному часі у популярних назвах, таких як League of Legends, TFT та Valorant, що пропонує аналіз чемпіонів, календарі кіберспорту, мета-склади та статистику персонажів.

### 🧠 <a name="conhecimento--memória"></a>Знання та пам'ять

Постійне зберігання пам'яті з використанням структур графів знань. Дозволяє ШІ-моделям зберігати та запитувати структуровану інформацію між сесіями.

- [apecloud/ApeRAG](https://github.com/apecloud/ApeRAG) 🐍 ☁️ 🏠 - Production-ready RAG-платформа, що поєднує Graph RAG, векторний пошук та повнотекстовий пошук. Найкращий вибір для створення власного Графу Знань та для Інженерії Контексту
- [CheMiguel23/MemoryMesh](https://github.com/CheMiguel23/MemoryMesh) 📇 🏠 - Покращена на основі графів пам'ять із фокусом на рольову гру ШІ та генерацію історій
- [graphlit-mcp-server](https://github.com/graphlit/graphlit-mcp-server) 📇 ☁️ - Завантажте будь-що з Slack, Discord, веб-сайтів, Google Drive, Linear або GitHub у проєкт Graphlit — а потім шукайте та отримуйте відповідні знання всередині MCP-клієнта, такого як Cursor, Windsurf або Cline.
- [hannesrudolph/mcp-ragdocs](https://github.com/hannesrudolph/mcp-ragdocs) 🐍 🏠 - Реалізація MCP-сервера, що надає інструменти для отримання та обробки документації через векторний пошук, дозволяючи помічникам ШІ розширювати свої відповіді контекстом відповідної документації
- [jinzcdev/markmap-mcp-server](https://github.com/jinzcdev/markmap-mcp-server) 📇 🏠 - MCP-сервер, створений за допомогою [markmap](https://github.com/markmap/markmap), що конвертує **Markdown** у **інтерактивні ментальні карти**. Підтримує експорт у кілька форматів (PNG/JPG/SVG), перегляд в реальному часі в браузері, копіювання Markdown одним кліком та функції динамічного перегляду.
- [kaliaboi/mcp-zotero](https://github.com/kaliaboi/mcp-zotero) 📇 ☁️ - Конектор для LLM для роботи з колекціями та джерелами у вашому Zotero Cloud
- [mcp-summarizer](https://github.com/0xshellming/mcp-summarizer) 📕 ☁️ - MCP-сервер резюмування ШІ, Підтримка кількох типів контенту: Простий текст, Веб-сторінки, PDF-документи, EPUB-книги, HTML-контент
- [mem0ai/mem0-mcp](https://github.com/mem0ai/mem0-mcp) 🐍 🏠 - Сервер для Model Context Protocol для Mem0, що допомагає керувати перевагами та шаблонами кодування, надаючи інструменти для зберігання, отримання та семантичної обробки реалізацій коду, найкращих практик та технічної документації в IDE, таких як Cursor та Windsurf
- [modelcontextprotocol/server-memory](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/memory) 📇 🏠 - Система постійної пам'яті на основі графу знань для збереження контексту
- [nonatofabio/local-faiss-mcp](https://github.com/nonatofabio/local_faiss_mcp) 🐍 🏠 🍎 🐧 - Локальна векторна база даних FAISS для RAG з інжекцією документів (PDF/TXT/MD/DOCX), семантичним пошуком, ре-рейкінгом та CLI-інструментами
- [pinecone-io/assistant-mcp](https://github.com/pinecone-io/assistant-mcp) 🎖️ 🦀 ☁️ - Підключається до вашого Pinecone Assistant і надає агенту контекст з вашого движка знань.
- [@ragieai/mcp-server](https://github.com/ragieai/ragie-mcp-server) 📇 ☁️ - Отримуйте контекст з вашої бази знань [Ragie](https://www.ragie.ai) (RAG), підключеної до інтеграцій, таких як Google Drive, Notion, JIRA та багато інших.
- [JamesANZ/memory-mcp](https://github.com/JamesANZ/memory-mcp) 📇 🏠 - MCP-сервер, що зберігає та отримує спогади кількох LLM за допомогою MongoDB. Надає інструменти для збереження, отримання, додавання та очищення спогадів розмови з позначками часу та ідентифікацією LLM.
- [JamesANZ/cross-llm-mcp](https://github.com/JamesANZ/cross-llm-mcp) 📇 🏠 - MCP-сервер, що дозволяє комунікацію між LLM та спільне використання пам'яті, дозволяючи різним моделям ШІ співпрацювати та спільно використовувати контекст між розмовами.
- [topoteretes/cognee](https://github.com/topoteretes/cognee/tree/dev/cognee-mcp) 📇 🏠 - Менеджер пам'яті для додатків ШІ та Агентів з використанням декількох сховищ графів та векторів, що дозволяє інжекцію понад 30 джерел даних
- [unibaseio/membase-mcp](https://github.com/unibaseio/membase-mcp) 📇 ☁️ - Зберігайте та запитуйте пам'ять вашого агента розподілено через Membase
- [entanglr/zettelkasten-mcp](https://github.com/entanglr/zettelkasten-mcp) 🐍 🏠 - Сервер для Model Context Protocol (MCP), що реалізує методологію управління знаннями Zettelkasten, дозволяючи створювати, пов'язувати та шукати атомічні нотатки через Claude та інші MCP-сумісні клієнти.

### ⚖️ <a name="legal"></a>Право

Доступ до юридичної інформації, законодавства та юридичних баз даних. Дозволяє ШІ-моделям досліджувати та аналізувати юридичні документи та регуляторну інформацію.

- [JamesANZ/us-legal-mcp](https://github.com/JamesANZ/us-legal-mcp) 📇 ☁️ - MCP-сервер, що надає комплексне законодавство США.

### 🗺️ <a name="serviços-de-localização"></a>Геолокаційні сервіси

Сервіси на основі локації та інструменти мапінгу. Дозволяє ШІ-моделям працювати з географічними даними, метеорологічною інформацією та аналітикою на основі локації.

- [briandconnelly/mcp-server-ipinfo](https://github.com/briandconnelly/mcp-server-ipinfo) 🐍 ☁️ - Геолокація IP-адреси та мережева інформація з використанням API IPInfo
- [isdaniel/mcp_weather_server](https://github.com/isdaniel/mcp_weather_server) 🐍 ☁️ - Отримання метеорологічної інформації з API https://api.open-meteo.com.
- [jagan-shanmugam/open-streetmap-mcp](https://github.com/jagan-shanmugam/open-streetmap-mcp) 🐍 🏠 - MCP-сервер OpenStreetMap з сервісами на основі локації та геопросторовими даними.
- [kukapay/nearby-search-mcp](https://github.com/kukapay/nearby-search-mcp) 🐍 ☁️ - MCP-сервер для пошуку місцевих місць з виявленням локації на основі IP.
- [modelcontextprotocol/server-google-maps](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/google-maps) 📇 ☁️ - Інтеграція з Google Maps для сервісів локації, маршрутів та деталей місць
- [QGIS MCP](https://github.com/jjsantos01/qgis_mcp) - підключає QGIS Desktop до Claude AI через MCP. Ця інтеграція дозволяє створення проєктів, підготовлене промптами, завантаження шарів, виконання коду та багато іншого.
- [SaintDoresh/Weather-MCP-ClaudeDesktop](https://github.com/SaintDoresh/Weather-MCP-ClaudeDesktop.git) 🐍 ☁️ - Інструмент MCP, що надає метеорологічні дані в реальному часі, прогнози та історичну метеорологічну інформацію з використанням API OpenWeatherMap.
- [rossshannon/Weekly-Weather-mcp](https://github.com/rossshannon/weekly-weather-mcp.git) 🐍 ☁️ - MCP-сервер для тижневого прогнозу погоди, що повертає 7 повних днів детальних прогнозів погоди в будь-якій точці світу.
- [SecretiveShell/MCP-timeserver](https://github.com/SecretiveShell/MCP-timeserver) 🐍 🏠 - Отримуйте доступ до часу в будь-якому часовому поясі та отримуйте поточний локальний час
- [webcoderz/MCP-Geo](https://github.com/webcoderz/MCP-Geo) 🐍 🏠 - MCP-сервер геокодування для nominatim, ArcGIS, Bing

### 🎯 <a name="marketing"></a>Маркетинг

Інструменти для створення та редагування маркетингового контенту, роботи з веб-метаданими, позиціонування продукту та редагувальних посібників.

- [AdsMCP/tiktok-ads-mcp-server](https://github.com/AdsMCP/tiktok-ads-mcp-server) 🐍 ☁️ - Сервер Model Context Protocol для інтеграції з API TikTok Ads, що дозволяє помічникам ШІ керувати кампаніями, аналізувати показники ефективності, працювати з аудиторіями та креативними матеріалами через OAuth-автентифікацію.
- [Open Strategy Partners Marketing Tools](https://github.com/open-strategy-partners/osp_marketing_tools) 🐍 🏠 - Набір маркетингових інструментів від Open Strategy Partners, включаючи стиль написання, коди редагування та створення карти цінності маркетингу продукту.

### 📊 <a name="monitoramento"></a>Моніторинг

Отримайте доступ до та проаналізуйте дані моніторингу додатків. Дозволяє ШІ-моделям переглядати звіти про помилки та показники продуктивності.

- [tumf/grafana-loki-mcp](https://github.com/tumf/grafana-loki-mcp) 🐍 🏠 - MCP-сервер, що дозволяє запитувати логи Loki через API Grafana.
- [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) 🎖️ 🐍 🏠 ☁️ - Пошукайте панелі, розслідуйте інциденти та запитуйте джерела даних у вашій інстанції Grafana
- [hyperb1iss/lucidity-mcp](https://github.com/hyperb1iss/lucidity-mcp) 🐍 🏠 - Покращте якість коду, згенерованого ШІ, через інтелектуальний аналіз на основі промптів у 10 критичних вимірах, від складності до вразливостей безпеки
- [inventer-dev/mcp-internet-speed-test](https://github.com/inventer-dev/mcp-internet-speed-test) 🐍 ☁️ - Тест швидкості інтернету з метриками продуктивності мережі, включаючи швидкість завантаження/вивантаження, латентність, аналіз джиттера та виявлення CDN-сервера з географічним мапінгом
- [last9/last9-mcp-server](https://github.com/last9/last9-mcp-server) - Легко прив'яжіть контекст production в реальному часі — логи, метрики та траси — до вашого локального середовища для швидшого автоматичного виправлення коду
- [metoro-io/metoro-mcp-server](https://github.com/metoro-io/metoro-mcp-server) 🎖️ 🏎️ ☁️ - Запитуйте та взаємодіюйте з Kubernetes-середовищами, що моніторяться Metoro
- [MindscapeHQ/server-raygun](https://github.com/MindscapeHQ/mcp-server-raygun) 📇 ☁️ - Інтеграція з API V3 Raygun для звітів про збої та моніторингу реальних користувачів
- [modelcontextprotocol/server-sentry](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry) 🐍 ☁️ - Інтеграція з Sentry.io для відстеження помилок та моніторингу продуктивності
- [pydantic/logfire-mcp](https://github.com/pydantic/logfire-mcp) 🎖️ 🐍 ☁️ - Надає доступ до трас та метрик OpenTelemetry через Logfire
- [seekrays/mcp-monitor](https://github.com/seekrays/mcp-monitor) 🏎️ 🏠 - Інструмент моніторингу системи, що виставляє системні метрики через Model Context Protocol (MCP). Цей інструмент дозволяє LLM отримувати інформацію про систему в реальному часі через MCP-сумісний інтерфейс (підтримує CPU, Пам'ять, Диск, Мережу, Хост, Процес)

### 🔎 <a name="pesquisa--extração-de-dados"></a>Пошук та видобування даних

- [0xdaef0f/job-searchoor](https://github.com/0xDAEF0F/job-searchoor) 📇 🏠 - MCP-сервер для пошуку вакансій з фільтрами за датою, ключовими словами, варіантами віддаленої роботи тощо.
- [ac3xx/mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi) 📇 ☁️ - Інтеграція з API пошуку Kagi
- [andybrandt/mcp-simple-arxiv](https://github.com/andybrandt/mcp-simple-arxiv) - 🐍 ☁️ MCP для LLM пошуку та читання статей arXiv
- [andybrandt/mcp-simple-pubmed](https://github.com/andybrandt/mcp-simple-pubmed) - 🐍 ☁️ MCP для пошуку та читання медичних / наукових статей PubMed.
- [angheljf/nyt](https://github.com/angheljf/nyt) 📇 ☁️ - Пошук статей за допомогою API NYTimes
- [apify/mcp-server-rag-web-browser](https://github.com/apify/mcp-server-rag-web-browser) 📇 ☁️ - MCP-сервер для Актору RAG Web Browser з відкритим кодом від Apify для виконання веб-пошуків, скрейпінгу URL та повернення контенту у Markdown.
- [Bigsy/Clojars-MCP-Server](https://github.com/Bigsy/Clojars-MCP-Server) 📇 ☁️ - MCP-сервер Clojars для актуальної інформації про залежності бібліотек Clojure
- [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) ☁️ 🐍 - Пошук статей пошуку ArXiv
- [chanmeng/google-news-mcp-server](https://github.com/ChanMeng666/server-google-news) 📇 ☁️ - Інтеграція з Google News з автоматичною категоризацією тем, багатомовною підтримкою та комплексними можливостями пошуку, включаючи заголовки, історії та пов'язані теми через [SerpAPI](https://serpapi.com/).
- [DappierAI/dappier-mcp](https://github.com/DappierAI/dappier-mcp) 🐍 ☁️ - MCP-сервер Dappier дозволяє швидкий та безкоштовний веб-пошук в реальному часі, а також доступ до преміальних даних від надійних медіа-брендів — новини, фінансові ринки, спорт, розваги, погода та багато іншого — для створення потужних агентів ШІ.
- [Pearch-ai/mcp_pearch](https://github.com/Pearch-ai/mcp_pearch) 🎖️ 🐍 ☁️ - Найкращий пошукова машина для людей, що скорочує час, витрачений на пошук талантів

### 🔒 <a name="segurança"></a>Безпека

- [AIM-Intelligence/AIM-Guard-MCP](https://github.com/AIM-Intelligence/AIM-MCP) 📇 🏠 🍎 🪟 🐧 - MCP-сервер, зосереджений на безпеці, що надає напрямки з безпеки та аналіз контенту для агентів ШІ.
- [bx33661/Wireshark-MCP](https://github.com/bx33661/Wireshark-MCP) [glama](https://glama.ai/mcp/servers/bx33661/Wireshark-MCP) 🐍 🏠 - MCP-сервер для аналізу мережевих пакетів Wireshark з функціями захоплення, статистики протоколів, вилучення полів та аналізу безпеки.
- [firstorderai/authenticator_mcp](https://github.com/firstorderai/authenticator_mcp) 📇 🏠 🍎 🪟 🐧 – Безпечний MCP-сервер (Model Context Protocol), що дозволяє агентам ШІ взаємодіяти з додатком автентифікатора.
- [13bm/GhidraMCP](https://github.com/13bm/GhidraMCP) 🐍 ☕ 🏠 - MCP-сервер для інтеграції Ghidra з помічницями ШІ. Цей плагін дозволяє бінарний аналіз, надаючи інструменти для інспекції функцій, декомпіляції, дослідження пам'яті та аналізу імпорту/експорту через Model Context Protocol.
- [atomicchonk/roadrecon_mcp_server](https://github.com/atomicchonk/roadrecon_mcp_server) 🐍 🪟 🏠 MCP-сервер для аналізу результатів, зібраних з ROADrecon при переліку клієнтів Azure
- [BurtTheCoder/mcp-dnstwist](https://github.com/BurtTheCoder/mcp-dnstwist) 📇 🪟 ☁️ - MCP-сервер для dnstwist, потужного інструменту fuzzing DNS, що допомагає виявляти 타이посквотінг, фішинг та корпоративний шпигунство.
- [BurtTheCoder/mcp-maigret](https://github.com/BurtTheCoder/mcp-maigret) 📇 🪟 ☁️ - MCP-сервер для maigret, потужного інструменту OSINT, що збирає інформацію про облікові записи користувачів з різних публічних джерел. Цей сервер надає інструменти для пошуку імен користувачів у соціальних мережах та аналізу URL.
- [intruder-io/intruder-mcp](https://github.com/intruder-io/intruder-mcp) 🐍 ☁️ - MCP-сервер для доступу до [Intruder](https://www.intruder.io/), допомагає ідентифікувати, розуміти та виправляти вразливості безпеки в вашій інфраструктурі.
- [joergmichno/clawguard-mcp](https://github.com/joergmichno/clawguard-mcp) ([glama](https://glama.ai/mcp/servers/joergmichno/clawguard-mcp)) 🐍 🏠 - Сканер безпеки для агентів ШІ, що виявляє ін'єкції промптів за допомогою 42+ regex-шаблонів
- [jtang613/GhidrAssistMCP](https://github.com/jtang613/GhidrAssistMCP) ☕ 🏠 - Нативний сервер Model Context Protocol для Ghidra. Включає конфігурацію через графічний інтерфейс, реєстрацію логів, 31 потужний інструмент та відсутність зовнішніх залежностей.
- [quantakrypto/pqc-tools](https://github.com/quantakrypto/pqc-tools) [![quantakrypto/pqc-tools MCP server](https://glama.ai/mcp/servers/quantakrypto/pqc-tools/badges/score.svg)](https://glama.ai/mcp/servers/quantakrypto/pqc-tools) 📇 🏠 ☁️ - Готовність до постквантового періоду для агентів кодування з ШІ: перевіряє в коді криптографію, вразливу до квантових атак (RSA/ECDH/ECDSA/DH), пояснює ризик harvest-now-decrypt-later, надає рекомендації щодо міграції на NIST ML-KEM/ML-DSA/SLH-DSA (та гібридні), перевіряє виправлення та перевіряє залежності. Тільки консультативні інструменти на основі контенту. Запускаємо локально (`npx @quantakrypto/mcp`) або використовуємо хостований OAuth ендпоінт на [mcp.quantakrypto.com](https://mcp.quantakrypto.com).

### 🏃 <a name="esportes"></a>Спорт

Інструменти для доступу до даних, результатів та статистики, пов'язаних із спортом.

- [mikechao/balldontlie-mcp](https://github.com/mikechao/balldontlie-mcp) 📇 - MCP-сервер, що інтегрує API balldontlie для надання інформації про гравців, команди та ігри NBA, NFL та MLB
- [r-huijts/firstcycling-mcp](https://github.com/r-huijts/firstcycling-mcp) 📇 ☁️ - Отримуйте доступ до даних велогонок, результатів та статистики через природну мову. Функції включають отримання списків учасників, результатів гонок та інформації про велосипедистів з firstcycling.com.
- [r-huijts/strava-mcp](https://github.com/r-huijts/strava-mcp) 📇 ☁️ - Сервер для Model Context Protocol (MCP), що підключається до API Strava, надаючи інструменти для доступу до даних Strava через LLM

### 🎧 <a name="suporte--gestão-de-serviços"></a>Підтримка та сервіс-менеджмент

Інструменти для керування підтримкою клієнтів, управлінням IT-сервісами та операціями/helpdesk.

- [effytech/freshdesk-mcp](https://github.com/effytech/freshdesk_mcp) 🐍 ☁️ - MCP-сервер, що інтегрується з Freshdesk, дозволяючи моделям ШІ взаємодіяти з модулями Freshdesk та виконувати різні операції підтримки.
- [nguyenvanduocit/jira-mcp](https://github.com/nguyenvanduocit/jira-mcp) 🏎️ ☁️ - MCP-конектор на базі Go для Jira, що дозволяє помічникам ШІ, таким як Claude, взаємодіяти з Atlassian Jira. Цей інструмент надає зручний інтерфейс для моделей ШІ для виконання поширених операцій Jira, включаючи управління завданнями, планування спринтів та переходи робочих процесів.

### 🌎 <a name="serviços-de-tradução"></a>Сервіси перекладу

Інструменти та сервіси перекладу для забезпечення можливості помічників ШІ перекладати контент між різними мовами.

- [translated/lara-mcp](https://github.com/translated/lara-mcp) 🎖️ 📇 ☁️ - MCP-сервер для API Lara Translate, що увімкнює потужні можливості перекладу з підтримкою виявлення мови та контекстно-чутливих перекладів.

### 🚆 <a name="viagens--transporte"></a>Подорожі та транспорт

Доступ до інформації про подорожі та транспорт. Дозволяє запитувати розклади, маршрути та дані про подорожі в реальному часі.

- [Airbnb MCP Server](https://github.com/openbnb-org/mcp-server-airbnb) 📇 ☁️ - Надає інструменти для пошуку на Airbnb та отримання деталей оголошень.
- [KyrieTangSheng/mcp-server-nationalparks](https://github.com/KyrieTangSheng/mcp-server-nationalparks) 📇 ☁️ - Інтеграція з API Національної паркової служби, що надає найновішу інформацію про деталі парків, попередження, центри відвідувачів, 캠пінги та події для Національних парків США
- [NS Travel Information MCP Server](https://github.com/r-huijts/ns-mcp-server) 📇 ☁️ - Отримуйте доступ до інформації про подорожі, розкладів та оновлень у реальному часі від Нідерландських залізниць (NS)
- [pab1it0/tripadvisor-mcp](https://github.com/pab1it0/tripadvisor-mcp) 📇 🐍 - MCP-сервер, що дозволяє LLM взаємодіяти з API Tripadvisor, підтримуючи дані розташування, відгуки та фото через стандартизовані інтерфейси MCP

### 🔄 <a name="controle-de-versão"></a>Контроль версій

Взаємодія з Git-репозиторіями та платформами контролю версій. Дозволяє управління репозиторіями, аналіз коду, обробку pull request, відстеження проблем та інші операції контролю версій через стандартизовані API.

- [adhikasp/mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest) 🐍 🏠 - Читайте та аналізуйте GitHub-репозиторії з вашим LLM
- [ddukbg/github-enterprise-mcp](https://github.com/ddukbg/github-enterprise-mcp) 📇 ☁️ 🏠 - MCP-сервер для інтеграції з API GitHub Enterprise
- [gitea/gitea-mcp](https://gitea.com/gitea/gitea-mcp) 🎖️ 🏎️ ☁️ 🏠 🍎 🪟 🐧 - Взаємодіяйте з екземплярами Gitea через MCP.
- [kopfrechner/gitlab-mr-mcp](https://github.com/kopfrechner/gitlab-mr-mcp) 📇 ☁️ - Безперешкодно взаємодійте з проблемами та запитами на злиття ваших проєктів GitLab.
- [modelcontextprotocol/server-git](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/git) 🐍 🏠 - Прямі операції з Git-репозиторіями, включаючи читання, пошук та аналіз локальних репозиторіїв
- [modelcontextprotocol/server-github](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/github) 📇 ☁️ - Інтеграція з API GitHub для управління репозиторіями, PR, проблемами та іншим
- [modelcontextprotocol/server-gitlab](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/gitlab) 📇 ☁️ 🏠 - Інтеграція з платформою GitLab для управління проєктами та операцій CI/CD
- [Tiberriver256/mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops) 📇 ☁️ - Інтеграція з Azure DevOps для управління репозиторіями, робочими елементами та конвеєрами.

### 🛠️ <a name="outras-ferramentas-e-integrações"></a>Інші інструменти та інтеграції

- [2niuhe/plantuml_web](https://github.com/2niuhe/plantuml_web) 🐍 🏠 ☁️ 🍎 🪟 🐧 - Веб-фронтенд PlantUML з інтеграцією MCP-сервера, що дозволяє генерувати зображення PlantUML та валідувати синтаксис.
- [2niuhe/qrcode_mcp](https://github.com/2niuhe/qrcode_mcp) 🐍 🏠 🍎 🪟 🐧 - MCP-сервер генерації QR-кодів, що перетворює будь-який текст (включаючи китайські ієрогліфи) на QR-коди з налаштовуваними кольорами та виводом у кодуванні base64.
- [AbdelStark/bitcoin-mcp](https://github.com/AbdelStark/bitcoin-mcp) - ₿ Сервер для Model Context Protocol (MCP), що дозволяє моделям ШІ взаємодіяти з Bitcoin, дозволяючи генерувати ключі, валідувати адреси, декодувати транзакції, запитувати блокчейн та багато іншого.
- [akseyh/bear-mcp-server](https://github.com/akseyh/bear-mcp-server) - Дозволяє ШІ читати ваші Нотатки Bear (тільки macOS)
- [allenporter/mcp-server-home-assistant](https://github.com/allenporter/mcp-server-home-assistant) 🐍 🏠 - Експонуйте всі голосові наміри Home Assistant через сервер для Model Context Protocol, дозволяючи керування будинком.
- [Amazon Bedrock Nova Canvas](https://github.com/zxkane/mcp-server-amazon-bedrock) 📇 ☁️ - Використовуйте модель Amazon Nova Canvas для генерації зображень.
- [amidabuddha/unichat-mcp-server](https://github.com/amidabuddha/unichat-mcp-server) 🐍/📇 ☁️ - Надсилайте запити до OpenAI, MistralAI, Anthropic, xAI, Google AI або DeepSeek за допомогою протоколу MCP через інструмент або попередньо визначені промпти. Потрібен API-ключ провайдера
- [fotoetienne/gqai](https://github.com/fotoetienne/gqai) 🏎 🏠 - Використовуйте звичайні інструменти визначення мутацій/запитів GraphQL, а gqai автоматично згенерує для вас MCP-сервер.
- [ttommyth/interactive-mcp](https://github.com/ttommyth/interactive-mcp) 📇 🏠 🍎 🪟 🐧 - Увімкнює інтерактивні робочі процеси LLM, додаючи локальні промпти користувача та функції чату безпосередньо в цикл MCP.
- [growilabs/growi-mcp-server](https://github.com/growilabs/growi-mcp-server) 🎖️ 📇 ☁️ - Офіційний MCP-сервер для інтеграції з API GROWI.
- [JamesANZ/medical-mcp](https://github.com/JamesANZ/medical-mcp) 📇 🏠 - MCP-сервер, що надає доступ до медичної інформації, баз даних ліків та ресурсів охорони здоров'я. Дозволяє помічникам ШІ консультуватися з медичними даними, взаємодією ліків та клінічними рекомендаціями.

## <a name="frameworks"></a>Фреймворки

- [FastMCP](https://github.com/jlowin/fastmcp) 🐍 - Фреймворк високого рівня для створення MCP-серверів на Python
- [FastMCP](https://github.com/punkpeye/fastmcp) 📇 - Фреймворк високого рівня для створення MCP-серверів на TypeScript
- [Foxy Contexts](https://github.com/strowk/foxy-contexts) 🏎️ - Бібліотека Golang для написання MCP-серверів декларативним способом з включеним функціональним тестуванням
- [gabfr/waha-api-mcp-server](https://github.com/gabfr/waha-api-mcp-server) 📇 - MCP-сервер зі специфікаціями openAPI для використання неофіційного API WhatsApp (https://waha.devlike.pro/ - також з відкритим кодом: https://github.com/devlikeapro/waha
- [Genkit MCP](https://github.com/firebase/genkit/tree/main/js/plugins/mcp) 📇 – Надає інтеграцію між [Genkit](https://github.com/firebase/genkit/tree/main) та Model Context Protocol (MCP).
- [http4k MCP SDK](https://mcp.http4k.org) 🐍 - Функціональний та тестований Kotlin SDK на базі популярного веб-набору інструментів [http4k](https://http4k.org). Підтримує новий протокол HTTP-стримінгу.
- [lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent) 🤖 🔌 - Створюйте ефективних агентів з MCP-серверами, використовуючи прості та композиційні патерни.
- [LiteMCP](https://github.com/wong2/litemcp) 📇 - Фреймворк високого рівня для створення MCP-серверів на JavaScript/TypeScript
- [marimo-team/codemirror-mcp](https://github.com/marimo-team/codemirror-mcp) - Розширення CodeMirror, що реалізує Model Context Protocol (MCP) для згадок ресурсів та команд промптів.
- [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go) 🏎️ - Golang SDK для створення MCP-серверів та клієнтів.
- [mcp-framework](https://github.com/QuantGeekDev/mcp-framework) 📇 - Швидкий та елегантний TypeScript фреймворк для створення MCP-серверів
- [mcp-proxy](https://github.com/punkpeye/mcp-proxy) - 📇 Проксі SSE для MCP-серверів, що використовують транспорт `stdio`.
- [mcp-rs-template](https://github.com/linux-china/mcp-rs-template) 🦀 - Шаблон CLI MCP-сервера для Rust
- [metoro-io/mcp-golang](https://github.com/metoro-io/mcp-golang) 🏎️ - Фреймворк Golang для створення MCP-серверів, зосереджений на типобезпеці
- [mullerhai/sakura-mcp](https://github.com/mullerhai/sakura-mcp) 🦀 ☕ - MCP-фреймворк Scala для створення ефективних агентів з MCP-серверами та MCP-клієнтами, похідними від modelcontextprotocol.io.
- [paulotaylor/voyp-mcp](https://github.com/paulotaylor/voyp-mcp) 📇 - VOYP - MCP-сервер Voice Over Your Phone для здійснення дзвінків.
- [poem-web/poem-mcpserver](https://github.com/poem-web/poem/tree/master/poem-mcpserver) 🦀 - Реалізація MCP-сервера для Poem.
- [quarkiverse/quarkus-mcp-server](https://github.com/quarkiverse/quarkus-mcp-server) ☕ - Java SDK для створення MCP-серверів за допомогою Quarkus.
- [rectalogic/langchain-mcp](https://github.com/rectalogic/langchain-mcp) 🐍 - Надає підтримку викликів MCP-інструментів у LangChain, дозволяючи інтеграцію MCP-інструментів у робочі процеси LangChain.
- [ribeirogab/simple-mcp](https://github.com/ribeirogab/simple-mcp) 📇 - Проста бібліотека TypeScript для створення MCP-серверів.
- [salty-flower/ModelContextProtocol.NET](https://github.com/salty-flower/ModelContextProtocol.NET) #️⃣ 🏠 - C# SDK для створення MCP-серверів на .NET 9 з сумісністю NativeAOT ⚡ 🔌
- [spring-ai-mcp](https://github.com/spring-projects-experimental/spring-ai-mcp) ☕ 🌱 - Java SDK та інтеграція з Spring Framework для створення MCP-клієнтів та MCP-серверів з різними варіантами транспорту.
- [spring-projects-experimental/spring-ai-mcp](https://github.com/spring-projects-experimental/spring-ai-mcp) ☕ 🌱 - Java SDK та інтеграція з Spring Framework для створення MCP-клієнтів та MCP-серверів з різними варіантами транспорту.
- [Template MCP Server](https://github.com/mcpdotdirect/template-mcp-server) 📇 - Інструмент командного рядка для створення нового проєкту сервера для Model Context Protocol з підтримкою TypeScript, подвійними варіантами транспорту та розширюваною структурою
- [sendaifun/solana-mcp-kit](https://github.com/sendaifun/solana-agent-kit/tree/main/examples/agent-kit-mcp-server) - Solana MCP SDK
- [tumf/web3-mcp](https://github.com/tumf/web3-mcp) 🐍 ☁️ - Реалізація MCP-сервера, що обгортає Ankr Advanced API. Доступ до NFT, токенів та даних блокчейну у декількох мережах, включаючи Ethereum, BSC, Polygon, Avalanche та інші.

## <a name="utilitarios"></a>Утиліти

- [boilingdata/mcp-server-and-gw](https://github.com/boilingdata/mcp-server-and-gw) 📇 - Шлюз транспорту MCP stdio до HTTP SSE з прикладом сервера та MCP-клієнтом.
- [f/MCPTools](https://github.com/f/mcptools) 🔨 - Інструмент розробки командного рядка для інспектування та взаємодії з MCP-серверами з додатковими функціями, такими як моки та проксі.
- [flux159/mcp-chat](https://github.com/flux159/mcp-chat) 📇🖥️ - CLI-клієнт для спілкування та підключення до будь-якого MCP-сервера. Корисний під час розробки та тестування MCP-серверів.
- [isaacwasserman/mcp-langchain-ts-client](https://github.com/isaacwasserman/mcp-langchain-ts-client) 📇 – Використовуйте інструменти, надані MCP, у LangChain.js
- [kukapay/whattimeisit-mcp](https://github.com/kukapay/whattimeisit-mcp) 🐍 ☁️ - Легкий MCP-сервер, що повідомляє точний час.
- [kukapay/whereami-mcp](https://github.com/kukapay/whereami-mcp) 🐍 ☁️ - Легкий MCP-сервер, що повідомляє, де ви знаходитеся, на основі вашої поточної IP-адреси.
- [kukapay/whoami-mcp](https://github.com/kukapay/whoami-mcp) 🐍 🏠 - Легкий MCP-сервер, що повідомляє, хто ви є.
- [lightconetech/mcp-gateway](https://github.com/lightconetech/mcp-gateway) 📇 - Демонстрація шлюзу для MCP-сервера SSE.
- [mark3labs/mcphost](https://github.com/mark3labs/mcphost) 🏎️ - CLI-додаток-хост, що дозволяє Великим Мовним Моделям (LLM) взаємодіяти з зовнішніми інструментами через Model Context Protocol (MCP).
- [MCP-Connect](https://github.com/EvalsOne/MCP-Connect) 📇 - Невеликий інструмент, що дозволяє хмарним AI-сервісам отримувати доступ до локальних MCP-серверів на базі Stdio через HTTP/HTTPS-запити.
- [SecretiveShell/MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge) 🐍 – проксі-мідлвер openAI для використання mcp у будь-якому клієнті, сумісному з openAI
- [sparfenyuk/mcp-proxy](https://github.com/sparfenyuk/mcp-proxy) 🐍 – Шлюз транспорту MCP stdio до SSE.
- [TBXark/mcp-proxy](https://github.com/TBXark/mcp-proxy) 🏎️ - MCP-проксі-сервер, що агрегує та обслуговує кілька MCP-серверів ресурсів через один HTTP-сервер.
- [upsonic/gpt-computer-assistant](https://github.com/Upsonic/gpt-computer-assistant) 🐍 – фреймворк для створення вертикального AI-агента
- [JoshuaSiraj/mcp_auto_register](https://github.com/JoshuaSiraj/mcp_auto_register) 🐍 – інструмент для автоматизації реєстрації функцій та класів пакета python в екземплярі FastMCP.

## <a name="dicas-e-truques"></a>Поради та хитрощі

### Офіційний промпт, щоб пояснити LLM, як використовувати MCP

Хочете поставити Claude запитання про Model Context Protocol?

Створіть Project і додайте до нього цей файл:

https://modelcontextprotocol.io/llms-full.txt

Тепер Claude може відповідати на запитання про те, як писати MCP-сервери та як вони працюють

- https://www.reddit.com/r/ClaudeAI/comments/1h3g01r/want_to_ask_claude_about_model_context_protocol/

## Історія зірок

<a href="https://star-history.com/#punkpeye/awesome-mcp-servers&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date" />
 </picture>
</a>
