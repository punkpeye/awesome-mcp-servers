# รายชื่อ MCP Servers ที่น่าสนใจ [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![繁體中文](https://img.shields.io/badge/中文文件-點擊查看-orange)](README-zh_TW.md)
[![简体中文](https://img.shields.io/badge/中文文档-点击查看-orange)](README-zh.md)
[![日本語](https://img.shields.io/badge/日本語-クリック-青)](README-ja.md)
[![한국어](https://img.shields.io/badge/한국어-클릭-yellow)](README-ko.md)
[![Português Brasileiro](https://img.shields.io/badge/Português_Brasileiro-Clique-green)](README-pt_BR.md)
[![Discord](https://img.shields.io/discord/1312302100125843476?logo=discord&label=discord)](https://glama.ai/mcp/discord)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/mcp?style=flat&logo=reddit&label=subreddit)](https://www.reddit.com/r/mcp/)

รายการรวบรวม Model Context Protocol (MCP) servers ที่น่าสนใจ

* [MCP คืออะไร?](#what-is-mcp)
* [ไคลเอนต์](#clients)
* [บทแนะนำ](#tutorials)
* [การนำไปใช้งานเซิร์ฟเวอร์](#server-implementations)
* [เฟรมเวิร์ค](#frameworks)
* [ยูทิลิตี้](#utilities)
* [เคล็ดลับและเทคนิค](#tips-and-tricks)

## MCP คืออะไร?

[MCP](https://modelcontextprotocol.io/) คือโปรโตคอลเปิดที่ช่วยให้โมเดล AI สามารถโต้ตอบกับทรัพยากรทั้งในระบบและระยะไกลได้อย่างปลอดภัย ผ่านการใช้งานเซิร์ฟเวอร์มาตรฐาน รายการนี้มุ่งเน้นไปที่ MCP เซิร์ฟเวอร์ที่พร้อมใช้งานและอยู่ในช่วงทดลอง ซึ่งช่วยขยายความสามารถของ AI ผ่านการเข้าถึงไฟล์ การเชื่อมต่อฐานข้อมูล การผสานรวม API และบริการอื่นๆ ที่เกี่ยวข้องกับบริบท

## ไคลเอนต์

ดูเพิ่มเติมได้ที่ [awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients/) และ [glama.ai/mcp/clients](https://glama.ai/mcp/clients)

> [!TIP]
> [Glama Chat](https://glama.ai/chat) คือไคลเอนต์ AI แบบ multi-modal ที่รองรับ MCP และมี [AI gateway](https://glama.ai/gateway)

## บทแนะนำ

* [Model Context Protocol (MCP) เริ่มต้นอย่างรวดเร็ว](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
* [การตั้งค่า Claude Desktop App เพื่อใช้งานกับฐานข้อมูล SQLite](https://youtu.be/wxCCzo9dGj0)

## ชุมชน

* [r/mcp Reddit](https://www.reddit.com/r/mcp)
* [เซิร์ฟเวอร์ Discord](https://glama.ai/mcp/discord)

## คำอธิบายสัญลักษณ์

* 🎖️ – การนำไปใช้งานอย่างเป็นทางการ
* ภาษาโปรแกรมมิ่ง
  * 🐍 – โค้ดเบส Python
  * 📇 – โค้ดเบส TypeScript
  * 🏎️ – โค้ดเบส Go
  * 🦀 – โค้ดเบส Rust
  * #️⃣ - โค้ดเบส C#
  * ☕ - โค้ดเบส Java
* ขอบเขต
  * ☁️ - บริการคลาวด์
  * 🏠 - บริการในเครื่อง
  * 📟 - ระบบฝังตัว
* ระบบปฏิบัติการ
  * 🍎 – สำหรับ macOS
  * 🪟 – สำหรับ Windows
  * 🐧 - สำหรับ Linux

> [!NOTE]
> สับสนระหว่าง Local 🏠 กับ Cloud ☁️ ?
> * ใช้ local เมื่อ MCP เซิร์ฟเวอร์สื่อสารกับซอฟต์แวร์ที่ติดตั้งในเครื่อง เช่น การควบคุมเบราว์เซอร์ Chrome
> * ใช้ network เมื่อ MCP เซิร์ฟเวอร์สื่อสารกับ API ระยะไกล เช่น API สภาพอากาศ

## การนำไปใช้งานเซิร์ฟเวอร์

> [!NOTE]
> ตอนนี้เรามี[ไดเร็กทอรี web-based](https://glama.ai/mcp/servers) ที่ซิงค์กับ repository นี้

* 🔗 - [รวบรวม](#aggregators)
* 🎨 - [ศิลปะและวัฒนธรรม](#art-and-culture)
* 🧬 - [ชีววิทยา การแพทย์ และไบโออินฟอร์เมติกส์](#bio)
* 📂 - [การทำงานอัตโนมัติของเบราว์เซอร์](#browser-automation)
* ☁️ - [แพลตฟอร์มคลาวด์](#cloud-platforms)
* 👨‍💻 - [การเรียกใช้โค้ด](#code-execution)
* 🖥️ - [คำสั่งในเทอร์มินัล](#command-line)
* 💬 - [การสื่อสาร](#communication)
* 👤 - [แพลตฟอร์มข้อมูลลูกค้า](#customer-data-platforms)
* 🗄️ - [ฐานข้อมูล](#databases)
* 📊 - [แพลตฟอร์มข้อมูล](#data-platforms)
* 🛠️ - [เครื่องมือสำหรับนักพัฒนา](#developer-tools)
* 📟 - [ระบบฝังตัว](#embedded-system)
* 📂 - [ระบบไฟล์](#file-systems)
* 💰 - [การเงินและฟินเทค](#finance--fintech)
* 🎮 - [เกม](#gaming)
* 🧠 - [ความรู้และความจำ](#knowledge--memory)
* ⚖️ - [กฎหมาย](#legal)
* 🗺️ - [บริการตำแหน่ง](#location-services)
* 🎯 - [การตลาด](#marketing)
* 📊 - [การตรวจสอบ](#monitoring)
* 🔎 - [ค้นหาและสกัดข้อมูล](#search)
* 🔒 - [ความปลอดภัย](#security)
* 🏃 - [กีฬา](#sports)
* 🎧 - [การสนับสนุนและจัดการบริการ](#support-and-service-management)
* 🌎 - [บริการแปลภาษา](#translation-services)
* 🚆 - [การเดินทางและการขนส่ง](#travel-and-transportation)
* 🔄 - [ระบบควบคุมเวอร์ชัน](#version-control)
* 🛠️ - [เครื่องมือและการผสานรวมอื่นๆ](#other-tools-and-integrations)

### 🔗 รวบรวม

เซิร์ฟเวอร์สำหรับเข้าถึงแอปและเครื่องมือจำนวนมากผ่าน MCP เซิร์ฟเวอร์เดียว

- [1mcp/agent](https://github.com/1mcp-app/agent) 📇 ☁️ 🏠 🍎 🪟 🐧 - เซิร์ฟเวอร์ MCP ที่รวมกันหลายเซิร์ฟเวอร์ MCP เป็นเซิร์ฟเวอร์เดียว
- [PipedreamHQ/pipedream](https://github.com/PipedreamHQ/pipedream/tree/master/modelcontextprotocol) ☁️ 🏠 - เชื่อมต่อกับ API 2,500 รายการ พร้อมเครื่องมือสำเร็จรูป 8,000+ รายการ และจัดการเซิร์ฟเวอร์สำหรับผู้ใช้งานของคุณในแอปของคุณเอง
- [tigranbs/mcgravity](https://github.com/tigranbs/mcgravity) 📇 🏠 - เครื่องมือพร็อกซี่สำหรับรวมเซิร์ฟเวอร์ MCP หลายตัวเข้าด้วยกันเป็นจุดเชื่อมต่อเดียว ปรับขนาดเครื่องมือ AI ของคุณด้วยการกระจายโหลดคำขอระหว่างเซิร์ฟเวอร์ MCP หลายตัว คล้ายกับวิธีที่ Nginx ทำงานสำหรับเว็บเซิร์ฟเวอร์
- [YangLiangwei/PersonalizationMCP](https://github.com/YangLiangwei/PersonalizationMCP) 🐍 ☁️ 🏠 🍎 🪟 🐧 - เซิร์ฟเวอร์ MCP รวมข้อมูลส่วนตัวที่ครอบคลุมด้วยการรวม Steam, YouTube, Bilibili, Spotify, Reddit และแพลตฟอร์มอื่นๆ พร้อมการรับรองความถูกต้อง OAuth2 การจัดการโทเค็นอัตโนมัติ และเครื่องมือ 90+ สำหรับเข้าถึงข้อมูลเกม เพลง วิดีโอ และแพลตฟอร์มโซเชียล

### 🎨 ศิลปะและวัฒนธรรม

เข้าถึงและสำรวจคอลเลกชันงานศิลปะ มรดกทางวัฒนธรรม และฐานข้อมูลพิพิธภัณฑ์ ช่วยให้โมเดล AI สามารถค้นหาและวิเคราะห์เนื้อหาด้านศิลปะและวัฒนธรรม

- [abhiemj/manim-mcp-server](https://github.com/abhiemj/manim-mcp-server) 🐍 🏠 🪟 🐧 - เซิร์ฟเวอร์ MCP ในเครื่องที่สร้างภาพเคลื่อนไหวด้วย Manim
- [burningion/video-editing-mcp](https://github.com/burningion/video-editing-mcp) 🐍 - เพิ่ม วิเคราะห์ ค้นหา และสร้างการตัดต่อวิดีโอจากคอลเลกชันวิดีโอของคุณ
- [djalal/quran-mcp-server](https://github.com/djalal/quran-mcp-server) 📇 🏠 - เซิร์ฟเวอร์ MCP เพื่อโต้ตอบกับคลังข้อมูลอัลกุรอาน ผ่าน REST API v4 อย่างเป็นทางการ
- [r-huijts/rijksmuseum-mcp](https://github.com/r-huijts/rijksmuseum-mcp) 📇 ☁️ - การผสานรวม API พิพิธภัณฑ์ Rijksmuseum สำหรับค้นหางานศิลปะ รายละเอียด และคอลเลกชัน
- [r-huijts/oorlogsbronnen-mcp](https://github.com/r-huijts/oorlogsbronnen-mcp) 📇 ☁️ - การผสานรวม API Oorlogsbronnen (แหล่งข้อมูลสงคราม) สำหรับเข้าถึงบันทึกทางประวัติศาสตร์ ภาพถ่าย และเอกสารจากเนเธอร์แลนด์ในช่วงสงครามโลกครั้งที่ 2 (1940-1945)
- [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) 🐍 - การผสานรวมเซิร์ฟเวอร์ MCP สำหรับ DaVinci Resolve ที่ให้เครื่องมือทรงพลังสำหรับการตัดต่อวิดีโอ ปรับสี จัดการสื่อ และควบคุมโปรเจ็กต์
- [yuna0x0/anilist-mcp](https://github.com/yuna0x0/anilist-mcp) 📇 ☁️ - เซิร์ฟเวอร์ MCP ที่ผสานรวม AniList API สำหรับข้อมูลอนิเมะและมังงะ
- [cantian-ai/bazi-mcp](https://github.com/cantian-ai/bazi-mcp) 📇 🏠 ☁️ 🍎 🪟 - ให้บริการจัดทำแผนภูมิปาจื้อ (八字) และการวิเคราะห์ที่ครอบคลุมและแม่นยำ

### 🧬 ชีววิทยา การแพทย์ และไบโออินฟอร์เมติกส์

- [genomoncology/biomcp](https://github.com/genomoncology/biomcp) 🐍 ☁️ - เซิร์ฟเวอร์ MCP สำหรับการวิจัยทางชีวการแพทย์ที่ให้การเข้าถึง PubMed, ClinicalTrials.gov และ MyVariant.info
- [longevity-genie/biothings-mcp](https://github.com/longevity-genie/biothings-mcp) 🐍 🏠 ☁️ - เซิร์ฟเวอร์ MCP เพื่อโต้ตอบกับ BioThings API รวมถึงยีน ความแปรปรวนทางพันธุกรรม ยา และข้อมูลอนุกรมวิธาน
- [longevity-genie/gget-mcp](https://github.com/longevity-genie/gget-mcp) 🐍 🏠 ☁️ - เซิร์ฟเวอร์ MCP ที่ให้เครื่องมือไบโออินฟอร์เมติกส์ที่ทรงพลังสำหรับการสืบค้นและวิเคราะห์ทางพันธุกรรม ห่อหุ้มไลบรารี `gget` ยอดนิยม
- [longevity-genie/opengenes-mcp](https://github.com/longevity-genie/opengenes-mcp) 🎖️ 🐍 🏠 ☁️ - เซิร์ฟเวอร์ MCP สำหรับฐานข้อมูลที่สามารถสืบค้นได้สำหรับการวิจัยเรื่องความชราและอายุยืนจากโครงการ OpenGenes
- [longevity-genie/synergy-age-mcp](https://github.com/longevity-genie/synergy-age-mcp) 🎖️ 🐍 🏠 ☁️ - เซิร์ฟเวอร์ MCP สำหรับฐานข้อมูล SynergyAge ของปฏิสัมพันธ์ทางพันธุกรรมที่เสริมกันและต่อต้านกันในด้านอายุยืน
- [wso2/fhir-mcp-server](https://github.com/wso2/fhir-mcp-server) 🐍 🏠 ☁️ - เซิร์ฟเวอร์โปรโตคอลบริบทโมเดลสำหรับ Fast Healthcare Interoperability Resources (FHIR) APIs ให้การผสานรวมที่ราบรื่นกับเซิร์ฟเวอร์ FHIR ทำให้ผู้ช่วย AI สามารถค้นหา ดึงข้อมูล สร้าง อัปเดต และวิเคราะห์ข้อมูลสุขภาพทางคลินิกด้วยการสนับสนุนการรับรองความถูกต้อง SMART-on-FHIR

### 📂 การทำงานอัตโนมัติของเบราว์เซอร์

ความสามารถในการเข้าถึงและทำงานอัตโนมัติกับเว็บ ช่วยให้สามารถค้นหา ดึงข้อมูล และประมวลผลเนื้อหาเว็บในรูปแบบที่เป็นมิตรกับ AI

- [BB-fat/browser-use-rs](https://github.com/BB-fat/browser-use-rs) 🦀 - เซิร์ฟเวอร์ MCP สำหรับการทำงานอัตโนมัติของเบราว์เซอร์ที่มีน้ำหนักเบา เขียนด้วย Rust และไม่มีการพึ่งพาภายนอก.
- [34892002/bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js) 📇 🏠 - เซิร์ฟเวอร์ MCP ที่สนับสนุนการค้นหาเนื้อหา Bilibili พร้อมตัวอย่างการผสานรวม LangChain และสคริปต์ทดสอบ
- [automatalabs/mcp-server-playwright](https://github.com/Automata-Labs-team/MCP-Server-Playwright) 🐍 - เซิร์ฟเวอร์ MCP สำหรับการทำงานอัตโนมัติของเบราว์เซอร์โดยใช้ Playwright
- [blackwhite084/playwright-plus-python-mcp](https://github.com/blackwhite084/playwright-plus-python-mcp) 🐍 - เซิร์ฟเวอร์ MCP Python ที่ใช้ Playwright สำหรับการทำงานอัตโนมัติของเบราว์เซอร์ เหมาะสำหรับ llm มากขึ้น
- [browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) 🎖️ 📇 - ทำงานอัตโนมัติกับเบราว์เซอร์บนคลาวด์ (เช่น การนำทางเว็บ การดึงข้อมูล การกรอกแบบฟอร์ม และอื่นๆ)
- [brutalzinn/simple-mcp-selenium](https://github.com/brutalzinn/simple-mcp-selenium) 📇 🏠 - เซิร์ฟเวอร์ MCP Selenium สำหรับควบคุมเบราว์เซอร์ด้วยภาษาธรรมชาติใน Cursor IDE เหมาะอย่างยิ่งสำหรับการทดสอบ การทำงานอัตโนมัติ และสถานการณ์การใช้งานหลายผู้ใช้
- [freema/firefox-devtools-mcp](https://github.com/freema/firefox-devtools-mcp) 📇 🏠 - การทำงานอัตโนมัติของเบราว์เซอร์ Firefox ผ่าน WebDriver BiDi สำหรับการทดสอบ การดึงข้อมูล และการควบคุมเบราว์เซอร์ รองรับการโต้ตอบแบบ snapshot/UID การตรวจสอบเครือข่าย การจับภาพคอนโซล และการจับภาพหน้าจอ

และอื่นๆ อีกมากมาย...

### ☁️ แพลตฟอร์มคลาวด์

การผสานรวมบริการแพลตฟอร์มคลาวด์ ช่วยให้สามารถจัดการและโต้ตอบกับโครงสร้างพื้นฐานและบริการคลาวด์

- [mrostamii/rancher-mcp-server](https://github.com/mrostamii/rancher-mcp-server) [glama](https://glama.ai/mcp/servers/mrostamii/rancher-mcp-server) 🏎️ ☁️/🏠 - MCP server สำหรับระบบนิเวศ Rancher รองรับการดำเนินงาน Kubernetes แบบหลายคลัสเตอร์ การจัดการ Harvester HCI (VM, storage, network) และเครื่องมือ Fleet GitOps
- [Nebula-Block-Data/nebulablock-mcp-server](https://github.com/Nebula-Block-Data/nebulablock-mcp-server) 📇 🏠 - ผสานการทำงานกับไลบรารี fastmcp เพื่อให้สามารถเข้าถึงฟังก์ชัน API ทั้งหมดของ NebulaBlock ได้ผ่านเครื่องมือ。

- [4everland/4everland-hosting-mcp](https://github.com/4everland/4everland-hosting-mcp) 🎖️ 📇 🏠 🍎 🐧 - การใช้งานเซิร์ฟเวอร์ MCP สำหรับ 4EVERLAND Hosting ที่ช่วยให้สามารถปรับใช้โค้ดที่สร้างด้วย AI บนเครือข่ายการจัดเก็บแบบกระจายศูนย์ เช่น Greenfield, IPFS และ Arweave ได้ทันที
- [alexei-led/aws-mcp-server](https://github.com/alexei-led/aws-mcp-server) 🐍 ☁️ - เซิร์ฟเวอร์ที่มีน้ำหนักเบาแต่ทรงพลังที่ช่วยให้ผู้ช่วย AI สามารถเรียกใช้คำสั่ง AWS CLI ใช้ท่อ Unix และใช้เทมเพลตพรอมต์สำหรับงาน AWS ทั่วไปในสภาพแวดล้อม Docker ที่ปลอดภัยพร้อมการสนับสนุนหลายสถาปัตยกรรม
- [alexei-led/k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server) 🐍 - เซิร์ฟเวอร์ที่มีน้ำหนักเบาแต่แข็งแกร่งที่ช่วยให้ผู้ช่วย AI สามารถเรียกใช้คำสั่ง CLI ของ Kubernetes (`kubectl`, `helm`, `istioctl` และ `argocd`) โดยใช้ท่อ Unix ในสภาพแวดล้อม Docker ที่ปลอดภัยพร้อมการสนับสนุนหลายสถาปัตยกรรม
- [aliyun/alibaba-cloud-ops-mcp-server](https://github.com/aliyun/alibaba-cloud-ops-mcp-server) 🎖️ 🐍 ☁️ - เซิร์ฟเวอร์ MCP ที่ช่วยให้ผู้ช่วย AI สามารถจัดการและดูแลทรัพยากรบน Alibaba Cloud ได้ โดยรองรับ ECS, การตรวจสอบคลาวด์, OOS และผลิตภัณฑ์คลาวด์อื่นๆ ที่มีการใช้งานอย่างแพร่หลาย
- [silenceper/mcp-k8s](https://github.com/silenceper/mcp-k8s) 🏎️ ☁️/🏠 - MCP-K8S เป็นเครื่องมือจัดการทรัพยากร Kubernetes ขับเคลื่อนด้วย AI ที่ช่วยให้ผู้ใช้สามารถดำเนินการกับทรัพยากรใดๆ ในคลัสเตอร์ Kubernetes ผ่านการโต้ตอบด้วยภาษาธรรมชาติ รวมถึงทรัพยากรดั้งเดิม (เช่น Deployment, Service) และทรัพยากรที่กำหนดเอง (CRD) ไม่จำเป็นต้องจำคำสั่งที่ซับซ้อน เพียงอธิบายความต้องการ และ AI จะดำเนินการในคลัสเตอร์ที่เกี่ยวข้องได้อย่างแม่นยำ ช่วยเพิ่มความสะดวกในการใช้งาน Kubernetes อย่างมาก
- [rrmistry/tilt-mcp](https://github.com/rrmistry/tilt-mcp) 🐍 🏠 🍎 🪟 🐧 - เซิร์ฟเวอร์ Model Context Protocol ที่ผสานการทำงานกับ Tilt เพื่อให้สามารถเข้าถึงทรัพยากร, ล็อก และการดำเนินการจัดการของ Tilt สำหรับสภาพแวดล้อมการพัฒนา Kubernetes ผ่านโปรแกรม
- [trilogy-group/aws-pricing-mcp](https://github.com/trilogy-group/aws-pricing-mcp) 🏎️ ☁️/🏠 - รับข้อมูลราคา EC2 ล่าสุดด้วยการเรียกเพียงครั้งเดียว รวดเร็ว ขับเคลื่อนโดยแคตตาล็อกราคา AWS ที่แยกวิเคราะห์ไว้ล่วงหน้า

### 👨‍💻 การเรียกใช้โค้ด

เซิร์ฟเวอร์สำหรับการเรียกใช้โค้ด ช่วยให้ LLMs สามารถเรียกใช้โค้ดในสภาพแวดล้อมที่ปลอดภัย เช่น สำหรับตัวแทน coding

- [pydantic/pydantic-ai/mcp-run-python](https://github.com/pydantic/pydantic-ai/tree/main/mcp-run-python) 🐍🏠- เรียกใช้โค้ด Python ในแซนด์บ็อกซ์ที่ปลอดภัยผ่านการเรียกเครื่องมือ MCP

### 🖥️ คำสั่งในเทอร์มินัล

เรียกใช้คำสั่ง จับการแสดงผล และโต้ตอบกับเชลล์และเครื่องมือบรรทัดคำสั่ง

- [freema/openclaw-mcp](https://github.com/freema/openclaw-mcp) [glama](https://glama.ai/mcp/servers/@freema/openclaw-mcp) 📇 ☁️ 🏠 - เซิร์ฟเวอร์ MCP สำหรับการรวม AI assistant กับ [OpenClaw](https://github.com/openclaw/openclaw) ช่วยให้ Claude มอบหมายงานให้กับ OpenClaw agents ด้วยเครื่องมือแบบ sync/async, การยืนยันตัวตน OAuth 2.1 และ SSE transport สำหรับ Claude.ai
- [ferrislucas/iterm-mcp](https://github.com/ferrislucas/iterm-mcp) 🖥️ 🛠️ 💬 - เซิร์ฟเวอร์ Model Context Protocol ที่ให้การเข้าถึง iTerm คุณสามารถรันคำสั่งและถามคำถามเกี่ยวกับสิ่งที่คุณเห็นในเทอร์มินัล iTerm
- [g0t4/mcp-server-commands](https://github.com/g0t4/mcp-server-commands) 📇 🏠 - รันคำสั่งใดๆ ด้วยเครื่องมือ `run_command` และ `run_script`
- [maxim-saplin/mcp_safe_local_python_executor](https://github.com/maxim-saplin/mcp_safe_local_python_executor) - ตัวแปลภาษา Python ที่ปลอดภัยบนพื้นฐานของ HF Smolagents `LocalPythonExecutor`

### 💬 การสื่อสาร

การผสานรวมกับแพลตฟอร์มการสื่อสารสำหรับการจัดการข้อความและการดำเนินการช่อง ช่วยให้โมเดล AI สามารถโต้ตอบกับเครื่องมือการสื่อสารทีม

- [AbdelStark/nostr-mcp](https://github.com/AbdelStark/nostr-mcp) - 🌐 ☁️ - เซิร์ฟเวอร์ Nostr MCP ที่ช่วยให้สามารถโต้ตอบกับ Nostr เปิดใช้งานการโพสต์บันทึก และอื่นๆ
- [adhikasp/mcp-twikit](https://github.com/adhikasp/mcp-twikit) 🐍 ☁️ - โต้ตอบกับการค้นหาและไทม์ไลน์ Twitter
- [agentmail-toolkit/mcp](https://github.com/agentmail-to/agentmail-toolkit/tree/main/mcp) - 🐍 💬 - เซิร์ฟเวอร์ MCP เพื่อสร้างกล่องจดหมายแบบทันทีสำหรับส่ง รับ และดำเนินการกับอีเมล เราไม่ใช่ตัวแทน AI สำหรับอีเมล แต่เป็นอีเมลสำหรับตัวแทน AI
- [line/line-bot-mcp-server](https://github.com/line/line-bot-mcp-server) 🎖 📇 ☁️ - เซิร์ฟเวอร์ MCP สำหรับการรวมบัญชี LINE ทางการ
- [ztxtxwd/open-feishu-mcp-server](https://github.com/ztxtxwd/open-feishu-mcp-server) 📇 ☁️ 🏠 - เซิร์ฟเวอร์ Model Context Protocol (MCP) ที่มีการรับรองความถูกต้อง Feishu OAuth ในตัว รองรับการเชื่อมต่อระยะไกลและให้เครื่องมือจัดการเอกสาร Feishu ที่ครอบคลุม รวมถึงการสร้างบล็อค การอัปเดตเนื้อหา และคุณสมบัติขั้นสูง
- [YCloud-Developers/ycloud-whatsapp-mcp-server](https://github.com/YCloud-Developers/ycloud-whatsapp-mcp-server) 📇 🏠 - เซิร์ฟเวอร์ MCP สำหรับส่งข้อความ WhatsApp Business ผ่านแพลตฟอร์ม YCloud
- [jaipandya/producthunt-mcp-server](https://github.com/jaipandya/producthunt-mcp-server) 🐍 🏠 - เซิร์ฟเวอร์ MCP สำหรับ Product Hunt โต้ตอบกับโพสต์ที่กำลังเป็นที่นิยม ความคิดเห็น คอลเลกชัน ผู้ใช้ และอื่นๆ อีกมากมาย
- [Danielpeter-99/calcom-mcp](https://github.com/Danielpeter-99/calcom-mcp) 🐍 🏠 - เซิร์ฟเวอร์ MCP สำหรับ Cal.com จัดการประเภทกิจกรรม สร้างการนัดหมาย และเข้าถึงข้อมูลตารางนัดของ Cal.com ผ่าน LLMs ได้
- [areweai/tsgram-mcp](https://github.com/areweai/tsgram-mcp) - TSgram: Telegram + Claude พร้อมการเข้าถึงพื้นที่ทำงานในเครื่องบนโทรศัพท์ของคุณใน TypeScript อ่าน เขียน และ vibe code ระหว่างเดินทาง!

### 👤 แพลตฟอร์มข้อมูลลูกค้า

ให้การเข้าถึงโปรไฟล์ลูกค้าภายในแพลตฟอร์มข้อมูลลูกค้า

- [iaptic/mcp-server-iaptic](https://github.com/iaptic/mcp-server-iaptic) 🎖️ 📇 ☁️ - เชื่อมต่อกับ [iaptic](https://www.iaptic.com) เพื่อถามเกี่ยวกับการซื้อของลูกค้า ข้อมูลธุรกรรม และสถิติรายได้ของแอป
- [OpenDataMCP/OpenDataMCP](https://github.com/OpenDataMCP/OpenDataMCP) 🐍 ☁️ - เชื่อมต่อข้อมูลเปิดใดๆ กับ LLM ใดๆ ด้วย Model Context Protocol
- [@antv/mcp-server-chart](https://github.com/antvis/mcp-server-chart) 🎖️ 📇 ☁️ - ปลั๊กอินสำหรับ MCP Server ที่สร้างขึ้นเพื่อสร้างแผนภูมิการมองเห็นข้อมูลโดยใช้ [AntV](https://github.com/antvis)
- [hustcc/mcp-echarts](https://github.com/hustcc/mcp-echarts) 📇 🏠 - AI สร้างแผนภูมิการมองเห็นที่เขียนด้วยไวยากรณ์ของ [Apache ECharts](https://echarts.apache.org) แบบไดนามิก MCP
- [hustcc/mcp-mermaid](https://github.com/hustcc/mcp-mermaid) 📇 🏠 - AI สร้างแผนภูมิที่มองเห็นได้แบบไดนามิกโดยใช้ไวยากรณ์ของ [Mermaid](ttps://mermaid.js.org/) MCP

### 🗄️ ฐานข้อมูล

การเข้าถึงฐานข้อมูลอย่างปลอดภัยพร้อมความสามารถในการตรวจสอบสคีมา ช่วยให้สามารถสืบค้นและวิเคราะห์ข้อมูลด้วยการควบคุมความปลอดภัยที่กำหนดค่าได้ รวมถึงการเข้าถึงแบบอ่านอย่างเดียว

- [Aiven-Open/mcp-aiven](https://github.com/Aiven-Open/mcp-aiven) - 🐍 ☁️ 🎖️ - นำทางโปรเจ็กต์ [Aiven](https://go.aiven.io/mcp-server) ของคุณและโต้ตอบกับบริการ PostgreSQL®, Apache Kafka®, ClickHouse® และ OpenSearch®
- [alexanderzuev/supabase-mcp-server](https://github.com/alexander-zuev/supabase-mcp-server) - เซิร์ฟเวอร์ Supabase MCP พร้อมการสนับสนุนการเรียกใช้คำสั่ง SQL และเครื่องมือสำรวจฐานข้อมูล
- [aliyun/alibabacloud-tablestore-mcp-server](https://github.com/aliyun/alibabacloud-tablestore-mcp-server) ☕ 🐍 ☁️ - บริการ MCP สำหรับ Tablestore คุณสมบัติรวมถึงการเพิ่มเอกสาร การค้นหาเชิงความหมายสำหรับเอกสารตามเวกเตอร์และสเกลาร์ เป็นมิตรกับ RAG และไร้เซิร์ฟเวอร์
- [benborla29/mcp-server-mysql](https://github.com/benborla/mcp-server-mysql) ☁️ 🏠 - การผสานรวมฐานข้อมูล MySQL ใน NodeJS พร้อมการควบคุมการเข้าถึงที่กำหนดค่าได้และการตรวจสอบสคีมา
- [bytebase/dbhub](https://github.com/bytebase/dbhub) 📇 🏠 – เซิร์ฟเวอร์ MCP ฐานข้อมูลสากลที่รองรับฐานข้อมูลกระแสหลัก
- [c4pt0r/mcp-server-tidb](https://github.com/c4pt0r/mcp-server-tidb) 🐍 ☁️ - การผสานรวมฐานข้อมูล TiDB พร้อมความสามารถในการตรวจสอบสคีมาและการสืบค้น
- [Canner/wren-engine](https://github.com/Canner/wren-engine) 🐍 🦀 🏠 - Semantic Engine สำหรับไคลเอนต์ Model Context Protocol (MCP) และตัวแทน AI
- [centralmind/gateway](https://github.com/centralmind/gateway) 🏎️ 🏠 🍎 🪟 - เซิร์ฟเวอร์ MCP และ MCP SSE ที่สร้าง API โดยอัตโนมัติตามสคีมาและข้อมูลของฐานข้อมูล รองรับ PostgreSQL, Clickhouse, MySQL, Snowflake, BigQuery, Supabase
- [ClickHouse/mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse) 🐍 ☁️ - การผสานรวมฐานข้อมูล ClickHouse พร้อมความสามารถในการตรวจสอบสคีมาและการสืบค้น
- [cr7258/elasticsearch-mcp-server](https://github.com/cr7258/elasticsearch-mcp-server) 🐍 🏠 - การใช้งานเซิร์ฟเวอร์ MCP ที่ให้การโต้ตอบกับ Elasticsearch
- [crystaldba/postgres-mcp](https://github.com/crystaldba/postgres-mcp) 🐍 🏠 - เซิร์ฟเวอร์ MCP แบบครบวงจรสำหรับการพัฒนาและการดำเนินการ Postgres พร้อมเครื่องมือสำหรับการวิเคราะห์ประสิทธิภาพ การปรับแต่ง และการตรวจสอบสถานะ
- [Dataring-engineering/mcp-server-trino](https://github.com/Dataring-engineering/mcp-server-trino) 🐍 ☁️ - เซิร์ฟเวอร์ Trino MCP เพื่อสืบค้นและเข้าถึงข้อมูลจากคลัสเตอร์ Trino
- [tuannvm/mcp-trino](https://github.com/tuannvm/mcp-trino) 🏎️ ☁️ - การใช้งานเซิร์ฟเวอร์ Model Context Protocol (MCP) สำหรับ Trino ด้วยภาษา Go.
- [designcomputer/mysql_mcp_server](https://github.com/designcomputer/mysql_mcp_server) 🐍 🏠 - การผสานรวมฐานข้อมูล MySQL พร้อมการควบคุมการเข้าถึงที่กำหนดค่าได้ การตรวจสอบสคีมา และแนวทางความปลอดภัยที่ครอบคลุม
- [domdomegg/airtable-mcp-server](https://github.com/domdomegg/airtable-mcp-server) 📇 🏠 - การผสานรวมฐานข้อมูล Airtable พร้อมความสามารถในการตรวจสอบสคีมา การอ่าน และการเขียน
- [ergut/mcp-bigquery-server](https://github.com/ergut/mcp-bigquery-server) 📇 ☁️ - การใช้งานเซิร์ฟเวอร์สำหรับการผสานรวม Google BigQuery ที่ช่วยให้สามารถเข้าถึงและสืบค้นฐานข้อมูล BigQuery ได้โดยตรง
- [f4ww4z/mcp-mysql-server](https://github.com/f4ww4z/mcp-mysql-server) 📇 🏠 - การผสานรวมฐานข้อมูล MySQL บน Node.js ที่ให้การดำเนินการฐานข้อมูล MySQL ที่ปลอดภัย
- [fireproof-storage/mcp-database-server](https://github.com/fireproof-storage/mcp-database-server) 📇 ☁️ - ฐานข้อมูลบัญชีแยกประเภท Fireproof พร้อมการซิงค์ผู้ใช้หลายคน
- [FreePeak/db-mcp-server](https://github.com/FreePeak/db-mcp-server) 🏎️ 🏠 – เซิร์ฟเวอร์ MCP ฐานข้อมูลหลายตัวประสิทธิภาพสูงที่สร้างด้วย Golang รองรับ MySQL & PostgreSQL (NoSQL กำลังจะมาเร็วๆ นี้) รวมถึงเครื่องมือในตัวสำหรับการเรียกใช้คำสั่ง การจัดการธุรกรรม การสำรวจสคีมา การสร้างคำสั่ง และการวิเคราะห์ประสิทธิภาพ พร้อมการผสานรวม Cursor อย่างราบรื่นสำหรับเวิร์กโฟลว์ฐานข้อมูลที่ปรับปรุงแล้ว
- [furey/mongodb-lens](https://github.com/furey/mongodb-lens) 📇 🏠 - MongoDB Lens: เซิร์ฟเวอร์ MCP ที่มีคุณสมบัติครบถ้วนสำหรับฐานข้อมูล MongoDB
- [gannonh/firebase-mcp](https://github.com/gannonh/firebase-mcp) 🔥 ⛅️ - บริการ Firebase รวมถึง Auth, Firestore และ Storage
- [get-convex/convex-backend](https://stack.convex.dev/convex-mcp-server) 📇 ☁️ - การผสานรวมฐานข้อมูล Convex เพื่อตรวจสอบตาราง ฟังก์ชัน และเรียกใช้คำสั่งแบบครั้งเดียว ([Source](https://github.com/get-convex/convex-backend/blob/main/npm-packages/convex/src/cli/mcp.ts))
- [GreptimeTeam/greptimedb-mcp-server](https://github.com/GreptimeTeam/greptimedb-mcp-server) 🐍 🏠 - เซิร์ฟเวอร์ MCP สำหรับการสืบค้น GreptimeDB
- [hannesrudolph/sqlite-explorer-fastmcp-mcp-server](https://github.com/hannesrudolph/sqlite-explorer-fastmcp-mcp-server) 🐍 🏠 - เซิร์ฟเวอร์ MCP ที่ให้การเข้าถึงฐานข้อมูล SQLite แบบอ่านอย่างเดียวที่ปลอดภัยผ่าน Model Context Protocol (MCP) เซิร์ฟเวอร์นี้สร้างขึ้นด้วยเฟรมเวิร์ก FastMCP ซึ่งช่วยให้ LLMs สามารถสำรวจและสืบค้นฐานข้อมูล SQLite ด้วยคุณสมบัติความปลอดภัยในตัวและการตรวจสอบความถูกต้องของคำสั่ง
- [idoru/influxdb-mcp-server](https://github.com/idoru/influxdb-mcp-server) 📇 ☁️ 🏠 - เรียกใช้คำสั่งกับ InfluxDB OSS API v2
- [isaacwasserman/mcp-snowflake-server](https://github.com/isaacwasserman/mcp-snowflake-server) 🐍 ☁️ - การผสานรวม Snowflake ที่ใช้การดำเนินการอ่านและ (ทางเลือก) เขียน รวมถึงการติดตามข้อมูลเชิงลึก
- [joshuarileydev/supabase-mcp-server](https://github.com/joshuarileydev/supabase) - เซิร์ฟเวอร์ Supabase MCP สำหรับการจัดการและสร้างโปรเจ็กต์และองค์กรใน Supabase
- [jovezhong/mcp-timeplus](https://github.com/jovezhong/mcp-timeplus) 🐍 ☁️ - เซิร์ฟเวอร์ MCP สำหรับ Apache Kafka และ Timeplus สามารถแสดงรายการหัวข้อ Kafka, ดึงข้อความ Kafka, บันทึกข้อมูล Kafka ในเครื่อง และสืบค้นข้อมูลสตรีมมิ่งด้วย SQL ผ่าน Timeplus
- [KashiwaByte/vikingdb-mcp-server](https://github.com/KashiwaByte/vikingdb-mcp-server) 🐍 ☁️ - การผสานรวม VikingDB พร้อมการแนะนำคอลเลกชันและดัชนี ที่เก็บเวกเตอร์ และความสามารถในการค้นหา
- [kiliczsh/mcp-mongo-server](https://github.com/kiliczsh/mcp-mongo-server) 📇 🏠 - เซิร์ฟเวอร์ Model Context Protocol สำหรับ MongoDB
- [ktanaka101/mcp-server-duckdb](https://github.com/ktanaka101/mcp-server-duckdb) 🐍 🏠 - การผสานรวมฐานข้อมูล DuckDB พร้อมความสามารถในการตรวจสอบสคีมาและการสืบค้น
- [LucasHild/mcp-server-bigquery](https://github.com/LucasHild/mcp-server-bigquery) 🐍 ☁️ - การผสานรวมฐานข้อมูล BigQuery พร้อมความสามารถในการตรวจสอบสคีมาและการสืบค้น
- [mcp-server-jdbc](https://github.com/quarkiverse/quarkus-mcp-servers/tree/main/jdbc) ☕ 🏠 - เชื่อมต่อกับฐานข้อมูลที่เข้ากันได้กับ JDBC และสืบค้น แทรก อัปเดต ลบ และอื่นๆ
- [memgraph/mcp-memgraph](https://github.com/memgraph/ai-toolkit/tree/main/integrations/mcp-memgraph) 🐍 🏠 - เซิร์ฟเวอร์ Memgraph MCP - รวมถึงเครื่องมือสำหรับเรียกใช้คำสั่งกับ Memgraph และทรัพยากรสคีมา
- [modelcontextprotocol/server-postgres](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/postgres) 📇 🏠 - การผสานรวมฐานข้อมูล PostgreSQL พร้อมความสามารถในการตรวจสอบสคีมาและการสืบค้น
- [modelcontextprotocol/server-sqlite](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/sqlite) 🐍 🏠 - การดำเนินการฐานข้อมูล SQLite พร้อมคุณสมบัติการวิเคราะห์ในตัว
- [neo4j-contrib/mcp-neo4j](https://github.com/neo4j-contrib/mcp-neo4j) 🐍 🏠 - Model Context Protocol กับ Neo4j
- [neondatabase/mcp-server-neon](https://github.com/neondatabase/mcp-server-neon) 📇 ☁️ — เซิร์ฟเวอร์ MCP สำหรับสร้างและจัดการฐานข้อมูล Postgres โดยใช้ Neon Serverless Postgres
- [niledatabase/nile-mcp-server](https://github.com/niledatabase/nile-mcp-server) เซิร์ฟเวอร์ MCP สำหรับแพลตฟอร์ม Postgres ของ Nile - จัดการและสืบค้นฐานข้อมูล Postgres ผู้เช่า ผู้ใช้ การรับรองความถูกต้องโดยใช้ LLMs
- [openlink/mcp-server-odbc](https://github.com/OpenLinkSoftware/mcp-odbc-server) 🐍 🏠 - เซิร์ฟเวอร์ MCP สำหรับการเชื่อมต่อระบบจัดการฐานข้อมูล (DBMS) ทั่วไปผ่านโปรโตคอล Open Database Connectivity (ODBC)
- [openlink/mcp-server-sqlalchemy](https://github.com/OpenLinkSoftware/mcp-sqlalchemy-server) 🐍 🏠 - เซิร์ฟเวอร์ MCP สำหรับการเชื่อมต่อระบบจัดการฐานข้อมูล (DBMS) ทั่วไปผ่าน SQLAlchemy โดยใช้ Python ODBC (pyodbc)
- [pab1it0/adx-mcp-server](https://github.com/pab1it0/adx-mcp-server) 🐍 ☁️ - สืบค้นและวิเคราะห์ฐานข้อมูล Azure Data Explorer
- [pab1it0/prometheus-mcp-server](https://github.com/pab1it0/prometheus-mcp-server) 🐍 ☁️ - สืบค้นและวิเคราะห์ Prometheus ระบบตรวจสอบโอเพ่นซอร์ส
- [prisma/mcp](https://github.com/prisma/mcp) 📇 ☁️ 🏠 - ช่วยให้ LLM จัดการฐานข้อมูล Prisma Postgres ได้ (เช่น สร้างฐานข้อมูลใหม่และรันการ migration หรือ query).
- [qdrant/mcp-server-qdrant](https://github.com/qdrant/mcp-server-qdrant) 🐍 🏠 - เซิร์ฟเวอร์ Qdrant MCP
- [QuantGeekDev/mongo-mcp](https://github.com/QuantGeekDev/mongo-mcp) 📇 🏠 - การผสานรวม MongoDB ที่ช่วยให้ LLMs สามารถโต้ตอบกับฐานข้อมูลได้โดยตรง
- [rashidazarang/airtable-mcp](https://github.com/rashidazarang/airtable-mcp) 🐍 ☁️ - เชื่อมต่อเครื่องมือ AI โดยตรงกับ Airtable สืบค้น สร้าง อัปเดต และลบบันทึกโดยใช้ภาษาธรรมชาติ คุณสมบัติรวมถึงการจัดการฐาน การดำเนินการตาราง การจัดการสคีมา การกรองบันทึก และการย้ายข้อมูลผ่านอินเทอร์เฟซ MCP มาตรฐาน
- [runekaagaard/mcp-alchemy](https://github.com/runekaagaard/mcp-alchemy) 🐍 🏠 - การผสานรวมฐานข้อมูลสากลบน SQLAlchemy ที่รองรับ PostgreSQL, MySQL, MariaDB, SQLite, Oracle, MS SQL Server และฐานข้อมูลอื่นๆ อีกมากมาย คุณสมบัติการตรวจสอบสคีมาและความสัมพันธ์ และความสามารถในการวิเคราะห์ชุดข้อมูลขนาดใหญ่
- [subnetmarco/pgmcp](https://github.com/subnetmarco/pgmcp) 🏎️ 🏠 - การสืบค้น PostgreSQL ด้วยภาษาธรรมชาติที่มีการสตรีมอัตโนมัติ ความปลอดภัยแบบอ่านอย่างเดียว และความเข้ากันได้กับฐานข้อมูลสากล
- [pgtuner_mcp](https://github.com/isdaniel/pgtuner_mcp) 🐍🗄️ - มอบความสามารถในการปรับแต่งประสิทธิภาพ PostgreSQL ด้วย AI
- [sirmews/mcp-pinecone](https://github.com/sirmews/mcp-pinecone) 🐍 ☁️ - การผสานรวม Pinecone พร้อมความสามารถในการค้นหาเวกเตอร์
- [TheRaLabs/legion-mcp](https://github.com/TheRaLabs/legion-mcp) 🐍 🏠 เซิร์ฟเวอร์ MCP ฐานข้อมูลสากลที่รองรับฐานข้อมูลหลายประเภท รวมถึง PostgreSQL, Redshift, CockroachDB, MySQL, RDS MySQL, Microsoft SQL Server, BigQuery, Oracle DB และ SQLite
- [tinybirdco/mcp-tinybird](https://github.com/tinybirdco/mcp-tinybird) 🐍 ☁️ - การผสานรวม Tinybird พร้อมความสามารถในการสืบค้นและ API
- [tradercjz/dolphindb-mcp-server](https://github.com/tradercjz/dolphindb-mcp-server) 🐍 ☁️ - การผสานรวมฐานข้อมูล TDolphinDB พร้อมความสามารถในการตรวจสอบสคีมาและการสืบค้น
- [weaviate/mcp-server-weaviate](https://github.com/weaviate/mcp-server-weaviate) 🐍 📇 ☁️ - เซิร์ฟเวอร์ MCP เพื่อเชื่อมต่อกับคอลเลกชัน Weaviate ของคุณเป็นฐานความรู้ รวมถึงการใช้ Weaviate เป็นที่เก็บหน่วยความจำแชท
- [XGenerationLab/xiyan_mcp_server](https://github.com/XGenerationLab/xiyan_mcp_server) 📇 ☁️ — เซิร์ฟเวอร์ MCP ที่รองรับการดึงข้อมูลจากฐานข้อมูลโดยใช้คำสั่งภาษาธรรมชาติ ขับเคลื่อนโดย XiyanSQL เป็น LLM แบบ text-to-SQL
- [xing5/mcp-google-sheets](https://github.com/xing5/mcp-google-sheets) 🐍 ☁️ - เซิร์ฟเวอร์ Model Context Protocol สำหรับโต้ตอบกับ Google Sheets เซิร์ฟเวอร์นี้มีเครื่องมือสำหรับสร้าง อ่าน อัปเดต และจัดการสเปรดชีตผ่าน Google Sheets API
- [freema/mcp-gsheets](https://github.com/freema/mcp-gsheets) 📇 ☁️ - เซิร์ฟเวอร์ MCP สำหรับการผสานรวม Google Sheets API พร้อมความสามารถในการอ่าน เขียน จัดรูปแบบ และจัดการแผ่นงานอย่างครอบคลุม
- [ydb/ydb-mcp](https://github.com/ydb-platform/ydb-mcp) 🎖️ 🐍 ☁️ – เซิร์ฟเวอร์ MCP สำหรับโต้ตอบกับฐานข้อมูล [YDB](https://ydb.tech)
- [zilliztech/mcp-server-milvus](https://github.com/zilliztech/mcp-server-milvus) 🐍 🏠 ☁️ - เซิร์ฟเวอร์ MCP สำหรับ Milvus / Zilliz ทำให้สามารถโต้ตอบกับฐานข้อมูลของคุณได้

### 📊 แพลตฟอร์มข้อมูล

แพลตฟอร์มข้อมูลสำหรับการผสานรวมข้อมูล การแปลง และการประสานงานไปป์ไลน์

- [JordiNei/mcp-databricks-server](https://github.com/JordiNeil/mcp-databricks-server) - เชื่อมต่อกับ Databricks API ช่วยให้ LLMs สามารถเรียกใช้คำสั่ง SQL แสดงรายการงาน และรับสถานะงาน
- [keboola/keboola-mcp-server](https://github.com/keboola/keboola-mcp-server) - โต้ตอบกับ Keboola Connection Data Platform เซิร์ฟเวอร์นี้มีเครื่องมือสำหรับแสดงรายการและเข้าถึงข้อมูลจาก Keboola Storage API

### 💻 เครื่องมือสำหรับนักพัฒนา

เครื่องมือและการผสานรวมที่ปรับปรุงเวิร์กโฟลว์การพัฒนาและการจัดการสภาพแวดล้อม

- [JamesANZ/system-prompts-mcp-server](https://github.com/JamesANZ/system-prompts-mcp-server) 📇 🏠 🍎 🪟 🐧 - เปิดคลังพรอมต์ผู้ช่วยเขียนโค้ดจำนวนมากเป็นเครื่องมือ MCP พร้อมการแนะนำตามโมเดลและการสลับบุคลิก เพื่อจำลองเอเจนต์อย่าง Cursor หรือ Devin ได้ทันที
- [21st-dev/Magic-MCP](https://github.com/21st-dev/magic-mcp) - สร้างส่วนประกอบ UI ที่สร้างขึ้นอย่างประณีตซึ่งได้รับแรงบันดาลใจจากวิศวกรออกแบบที่ดีที่สุดของ 21st.dev
- [a-25/ios-mcp-code-quality-server](https://github.com/a-25/ios-mcp-code-quality-server) 📇 🏠 🍎 - เซิร์ฟเวอร์สำหรับการวิเคราะห์คุณภาพโค้ด iOS และการทดสอบอัตโนมัติ ให้การดำเนินการทดสอบ Xcode อย่างครอบคลุม การผสานรวม SwiftLint และการวิเคราะห์ข้อผิดพลาดโดยละเอียด ทำงานในโหมด CLI และ MCP เซิร์ฟเวอร์ สำหรับการใช้งานโดยตรงของนักพัฒนาและการผสานรวมผู้ช่วย AI
- [Hypersequent/qasphere-mcp](https://github.com/Hypersequent/qasphere-mcp) 🎖️ 📇 ☁️ - การรวมกับระบบจัดการทดสอบ [QA Sphere](https://qasphere.com/) ช่วยให้ LLM สามารถค้นพบ สรุป และโต้ตอบกับกรณีทดสอบได้โดยตรงจาก IDE ที่ขับเคลื่อนด้วย AI
- [admica/FileScopeMCP](https://github.com/admica/FileScopeMCP) 🐍 📇 🦀 - วิเคราะห์โค้ดเบสของคุณโดยระบุไฟล์สำคัญตามความสัมพันธ์ของการพึ่งพา สร้างไดอะแกรมและคะแนนความสำคัญ ช่วยให้ผู้ช่วย AI เข้าใจโค้ดเบส
- [api7/apisix-mcp](https://github.com/api7/apisix-mcp) 🎖️ 📇 🏠 เซิร์ฟเวอร์ MCP ที่รองรับการสืบค้นและจัดการทรัพยากรทั้งหมดใน [Apache APISIX](https://github.com/apache/apisix)
- [automation-ai-labs/mcp-link](https://github.com/automation-ai-labs/mcp-link) 🏎️ 🏠 - ผสานรวม API ใดๆ กับตัวแทน AI ได้อย่างราบรื่น (ด้วย OpenAPI Schema)
- [Coment-ML/Opik-MCP](https://github.com/comet-ml/opik-mcp) 🎖️ 📇 ☁️ 🏠 - พูดคุยกับการสังเกตการณ์ LLM การติดตาม และการตรวจสอบที่บันทึกโดย Opik โดยใช้ภาษาธรรมชาติ
- [davidan90/time-node-mcp](https://github.com/davidan90/time-node-mcp) 📇 🏠 - การดำเนินการเกี่ยวกับวันที่และเวลาที่รองรับเขตเวลา พร้อมรองรับ IANA timezones การแปลงเขตเวลา และการจัดการ Daylight Saving Time
- [davidlin2k/pox-mcp-server](https://github.com/davidlin2k/pox-mcp-server) 🐍 🏠 - เซิร์ฟเวอร์ MCP สำหรับตัวควบคุม POX SDN เพื่อให้ความสามารถในการควบคุมและจัดการเครือข่าย
- [delano/postman-mcp-server](https://github.com/delano/postman-mcp-server) 📇 ☁️ - โต้ตอบกับ [Postman API](https://www.postman.com/postman/postman-public-workspace/)
- [endorhq/cli](https://github.com/endorhq/cli) 📇 ☁️ 🏠 🪟 🐧 🍎 - Endor ช่วยให้เอเจนต์ AI ของคุณรันบริการต่างๆ เช่น MariaDB, Postgres, Redis, Memcached, Alpine หรือ Valkey ในแซนด์บ็อกซ์ที่แยกจากกัน รับแอปพลิเคชันที่กำหนดค่าไว้ล่วงหน้าซึ่งบูตได้ภายในเวลาไม่ถึง 5 วินาที. [ตรวจสอบเอกสารของเรา](https://docs.endor.dev/mcp/overview/).
- [flipt-io/mcp-server-flipt](https://github.com/flipt-io/mcp-server-flipt) 📇 🏠 - ช่วยให้ผู้ช่วย AI สามารถโต้ตอบกับแฟล็กคุณสมบัติของคุณใน [Flipt](https://flipt.io)
- [GLips/Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) 📇 🏠 - ให้ตัวแทน coding เข้าถึงข้อมูล Figma โดยตรงเพื่อช่วยในการใช้งานการออกแบบแบบ one-shot
- [mhmzdev/Figma-Flutter-MCP](https://github.com/mhmzdev/Figma-Flutter-MCP) 📇 🏠 - ให้ตัวแทนการเขียนโค้ดเข้าถึงข้อมูล Figma โดยตรงเพื่อช่วยในการเขียนโค้ด Flutter สำหรับการสร้างแอปรวมถึงการส่งออกทรัพยากร การบำรุงรักษาวิดเจ็ต และการใช้งานหน้าจอแบบเต็ม
- [gofireflyio/firefly-mcp](https://github.com/gofireflyio/firefly-mcp) 🎖️ 📇 ☁️ - ผสานรวม ค้นพบ จัดการ และเข้ารหัสทรัพยากรคลาวด์ด้วย [Firefly](https://firefly.ai)
- [Govcraft/rust-docs-mcp-server](https://github.com/Govcraft/rust-docs-mcp-server) 🦀 🏠 - ให้บริบทเอกสารล่าสุดสำหรับ crate Rust เฉพาะแก่ LLMs ผ่านเครื่องมือ MCP โดยใช้การค้นหาเชิงความหมาย (embeddings) และการสรุป LLM
- [haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server) 🐍 🏠 - เซิร์ฟเวอร์จัดการ Excel ที่ให้การสร้างเวิร์กบุ๊ก การดำเนินการข้อมูล การจัดรูปแบบ และคุณสมบัติขั้นสูง (แผนภูมิ ตาราง Pivot สูตร)
- [higress-group/higress-ops-mcp-server](https://github.com/higress-group/higress-ops-mcp-server) 🐍 🏠 - เซิร์ฟเวอร์ MCP ที่มีเครื่องมือที่ครอบคลุมสำหรับการจัดการการกำหนดค่าและการดำเนินการเกตเวย์ [Higress](https://github.com/alibaba/higress)
- [hungthai1401/bruno-mcp](https://github.com/hungthai1401/bruno-mcp) 📇 🏠 - เซิร์ฟเวอร์ MCP สำหรับโต้ตอบกับ [Bruno API Client](https://www.usebruno.com/)
- [hyperb1iss/droidmind](https://github.com/hyperb1iss/droidmind) 🐍 🏠 - ควบคุมอุปกรณ์ Android ด้วย AI ผ่าน MCP เปิดใช้งานการควบคุมอุปกรณ์ การดีบัก การวิเคราะห์ระบบ และการทำงานอัตโนมัติของ UI ด้วยกรอบความปลอดภัยที่ครอบคลุม
- [IlyaGulya/gradle-mcp-server](https://github.com/IlyaGulya/gradle-mcp-server) 🏠 - การผสานรวม Gradle โดยใช้ Gradle Tooling API เพื่อตรวจสอบโปรเจ็กต์ เรียกใช้งาน และรันการทดสอบพร้อมการรายงานผลการทดสอบแต่ละรายการ
- [InhiblabCore/mcp-image-compression](https://github.com/InhiblabCore/mcp-image-compression) 🐍 🏠 - เซิร์ฟเวอร์ MCP สำหรับการบีบอัดรูปภาพรูปแบบต่างๆ ในเครื่อง
- [ios-simulator-mcp](https://github.com/joshuayoes/ios-simulator-mcp) 📇 🏠 🍎 - เซิร์ฟเวอร์ Model Context Protocol (MCP) สำหรับโต้ตอบกับ iOS simulators เซิร์ฟเวอร์นี้ช่วยให้คุณสามารถโต้ตอบกับ iOS simulators โดยรับข้อมูลเกี่ยวกับพวกมัน ควบคุมการโต้ตอบ UI และตรวจสอบองค์ประกอบ UI
- [j4c0bs/mcp-server-sql-analyzer](https://github.com/j4c0bs/mcp-server-sql-analyzer) 🐍 - เซิร์ฟเวอร์ MCP ที่ให้การวิเคราะห์ SQL การตรวจสอบโค้ด และการแปลงภาษาโดยใช้ [SQLGlot](https://github.com/tobymao/sqlglot)
- [jasonjmcghee/claude-debugs-for-you](https://github.com/jasonjmcghee/claude-debugs-for-you) 📇 🏠 - เซิร์ฟเวอร์ MCP และส่วนขยาย VS Code ซึ่งเปิดใช้งานการดีบักอัตโนมัติ (ไม่จำกัดภาษา) ผ่านเบรกพอยต์และการประเมินนิพจน์
- [jetbrains/mcpProxy](https://github.com/JetBrains/mcpProxy) 🎖️ 📇 🏠 - เชื่อมต่อกับ JetBrains IDE
- [Jktfe/serveMyAPI](https://github.com/Jktfe/serveMyAPI) 📇 🏠 🍎 - เซิร์ฟเวอร์ MCP (Model Context Protocol) ส่วนบุคคลสำหรับจัดเก็บและเข้าถึงคีย์ API อย่างปลอดภัยในโปรเจ็กต์ต่างๆ โดยใช้ macOS Keychain
- [joshuarileydev/app-store-connect-mcp-server](https://github.com/JoshuaRileyDev/app-store-connect-mcp-server) 📇 🏠 - เซิร์ฟเวอร์ MCP เพื่อสื่อสารกับ App Store Connect API สำหรับนักพัฒนา iOS
- [joshuarileydev/simulator-mcp-server](https://github.com/JoshuaRileyDev/simulator-mcp-server) 📇 🏠 - เซิร์ฟเวอร์ MCP เพื่อควบคุม iOS Simulators
- [lamemind/mcp-server-multiverse](https://github.com/lamemind/mcp-server-multiverse) 📇 🏠 🛠️ - เซิร์ฟเวอร์มิดเดิลแวร์ที่ช่วยให้อินสแตนซ์ที่แยกจากกันหลายอินสแตนซ์ของเซิร์ฟเวอร์ MCP เดียวกันสามารถอยู่ร่วมกันได้อย่างอิสระด้วยเนมสเปซและการกำหนดค่าที่ไม่ซ้ำกัน
- [langfuse/mcp-server-langfuse](https://github.com/langfuse/mcp-server-langfuse) 🐍 🏠 - เซิร์ฟเวอร์ MCP เพื่อเข้าถึงและจัดการพรอมต์แอปพลิเคชัน LLM ที่สร้างด้วย [Langfuse]([https://langfuse.com/](https://langfuse.com/docs/prompts/get-started)) Prompt Management
- [mrexodia/user-feedback-mcp](https://github.com/mrexodia/user-feedback-mcp) 🐍 🏠 - เซิร์ฟเวอร์ MCP อย่างง่ายเพื่อเปิดใช้งานเวิร์กโฟลว์ human-in-the-loop ในเครื่องมือเช่น Cline และ Cursor
- [OctoMind-dev/octomind-mcp](https://github.com/OctoMind-dev/octomind-mcp) - 📇 ☁️ ให้ตัวแทน AI ที่คุณต้องการสร้างและรันการทดสอบ end-to-end ของ [Octomind](https://www.octomind.dev/) ที่จัดการเต็มรูปแบบจากโค้ดเบสของคุณหรือแหล่งข้อมูลอื่นๆ เช่น Jira, Slack หรือ TestRail
- [pskill9/website-downloader](https://github.com/pskill9/website-downloader) 🗄️ 🚀 - เซิร์ฟเวอร์ MCP นี้มีเครื่องมือสำหรับดาวน์โหลดเว็บไซต์ทั้งหมดโดยใช้ wget มันรักษาโครงสร้างเว็บไซต์และแปลงลิงก์ให้ทำงานในเครื่อง
- [public-ui/kolibri](https://github.com/public-ui/kolibri) 📇 ☁️ 🏠 - เซิร์ฟเวอร์ KoliBri MCP แบบสตรีมมิง (NPM: `@public-ui/mcp`) ให้ตัวอย่าง สเปก เอกสาร และสถานการณ์คอมโพเนนต์เว็บมากกว่า 200 รายการที่การันตีความเข้าถึงได้ ผ่านปลายทาง HTTP ที่โฮสต์หรือ CLI `kolibri-mcp` ภายในเครื่อง
- [yiwenlu66/PiloTY](https://github.com/yiwenlu66/PiloTY) 🐍 🏠 - นักบิน AI สำหรับการดำเนินงาน PTY ที่ช่วยให้เอเจนต์สามารถควบคุมเทอร์มินัลแบบโต้ตอบด้วยเซสชันที่มีสถานะ การเชื่อมต่อ SSH และการจัดการกระบวนการพื้นหลัง
- [QuantGeekDev/docker-mcp](https://github.com/QuantGeekDev/docker-mcp) 🏎️ 🏠 - การจัดการและการดำเนินการคอนเทนเนอร์ Docker ผ่าน MCP
- [r-huijts/xcode-mcp-server](https://github.com/r-huijts/xcode-mcp-server) 📇 🏠 🍎 - การผสานรวม Xcode สำหรับการจัดการโปรเจ็กต์ การดำเนินการไฟล์ และการทำงานอัตโนมัติของการสร้าง
- [FastAlertNow/mcp-server](https://github.com/FastAlertNow/mcp-server) 💬 ☁️ - เซิร์ฟเวอร์ FastAlert MCP - เซิร์ฟเวอร์ Model Context Protocol (MCP) อย่างเป็นทางการของ FastAlert เซิร์ฟเวอร์นี้ช่วยให้ AI เอเจนต์ (เช่น Claude, ChatGPT และ Cursor) สามารถแสดงรายการช่องของคุณ และส่งการแจ้งเตือนโดยตรงผ่าน FastAlert API ได้ ![ไอคอน FastAlert](https://fastalert.now/icons/favicon-32x32.png)
- [ReAPI-com/mcp-openapi](https://github.com/ReAPI-com/mcp-openapi) 📇 🏠 - เซิร์ฟเวอร์ MCP ที่ช่วยให้ LLMs รู้ทุกอย่างเกี่ยวกับข้อกำหนด OpenAPI ของคุณเพื่อค้นหา อธิบาย และสร้างโค้ด/ข้อมูลจำลอง
- [Rootly-AI-Labs/Rootly-MCP-server](https://github.com/Rootly-AI-Labs/Rootly-MCP-server) 🎖️🐍☁️🍎 - เซิร์ฟเวอร์ MCP สำหรับแพลตฟอร์มการจัดการเหตุการณ์ [Rootly](https://rootly.com/)
- [sammcj/mcp-package-version](https://github.com/sammcj/mcp-package-version) 📇 🏠 - เซิร์ฟเวอร์ MCP เพื่อช่วย LLMs แนะนำเวอร์ชันแพ็คเกจที่เสถียรล่าสุดเมื่อเขียนโค้ด
- [sapientpants/sonarqube-mcp-server](https://github.com/sapientpants/sonarqube-mcp-server) 🦀 ☁️ 🏠 - เซิร์ฟเวอร์ Model Context Protocol (MCP) ที่ผสานรวมกับ SonarQube เพื่อให้ผู้ช่วย AI เข้าถึงเมตริกคุณภาพโค้ด ปัญหา และสถานะเกตคุณภาพ
- [SDGLBL/mcp-claude-code](https://github.com/SDGLBL/mcp-claude-code) 🐍 🏠 - การใช้งานความสามารถของ Claude Code โดยใช้ MCP เปิดใช้งานความเข้าใจโค้ด AI การแก้ไข และการวิเคราะห์โปรเจ็กต์ด้วยการสนับสนุนเครื่องมือที่ครอบคลุม
- [selvage-lab/selvage](https://github.com/selvage-lab/selvage) 🐍 🏠 - เซิร์ฟเวอร์ MCP สำหรับการรีวิวโค้ดด้วย LLM พร้อมระบบดึงบริบทอัจฉริยะด้วย AST รองรับ Claude, GPT, Gemini และโมเดลมากกว่า 20 รายการผ่าน OpenRouter
- [snaggle-ai/openapi-mcp-server](https://github.com/snaggle-ai/openapi-mcp-server) 🏎️ 🏠 - เชื่อมต่อเซิร์ฟเวอร์ HTTP/REST API ใดๆ โดยใช้ข้อกำหนด Open API (v3)
- [stass/lldb-mcp](https://github.com/stass/lldb-mcp) 🐍 🏠 🐧 🍎 - เซิร์ฟเวอร์ MCP สำหรับ LLDB เปิดใช้งานการวิเคราะห์ไบนารีและไฟล์คอร์ของ AI การดีบัก การแยกส่วนประกอบ
- [TencentEdgeOne/edgeone-pages-mcp](https://github.com/TencentEdgeOne/edgeone-pages-mcp) 📇 ☁️ - บริการ MCP สำหรับการปรับใช้เนื้อหา HTML บน EdgeOne Pages และรับ URL ที่สามารถเข้าถึงได้จากสาธารณะ
- [tumf/mcp-text-editor](https://github.com/tumf/mcp-text-editor) 🐍 🏠 - โปรแกรมแก้ไขไฟล์ข้อความแบบบรรทัดต่อบรรทัด ปรับให้เหมาะสมสำหรับเครื่องมือ LLM ด้วยการเข้าถึงไฟล์บางส่วนที่มีประสิทธิภาพเพื่อลดการใช้โทเค็น
- [vivekvells/mcp-pandoc](https://github.com/vivekVells/mcp-pandoc) 🗄️ 🚀 - เซิร์ฟเวอร์ MCP สำหรับการแปลงรูปแบบเอกสารอย่างราบรื่นโดยใช้ Pandoc รองรับ Markdown, HTML, PDF, DOCX (.docx), csv และอื่นๆ
- [VSCode Devtools](https://github.com/biegehydra/BifrostMCP) 📇 - เชื่อมต่อกับ VSCode ide และใช้เครื่องมือเชิงความหมายเช่น `find_usages`
- [xcodebuild](https://github.com/ShenghaiWang/xcodebuild) 🍎 สร้าง iOS Xcode workspace/project และส่งข้อผิดพลาดกลับไปยัง llm
- [xzq.xu/jvm-mcp-server](https://github.com/xzq-xu/jvm-mcp-server) 📇 🏠 - โครงการใช้งานเซิร์ฟเวอร์ MCP (Model Context Protocol) บน JVM
- [yangkyeongmo@/mcp-server-apache-airflow](https://github.com/yangkyeongmo/mcp-server-apache-airflow) 🐍 🏠 - เซิร์ฟเวอร์ MCP ที่เชื่อมต่อกับ [Apache Airflow](https://airflow.apache.org/) โดยใช้ไคลเอนต์อย่างเป็นทางการ
- [YuChenSSR/mindmap-mcp-server](https://github.com/YuChenSSR/mindmap-mcp-server) 🐍 🏠 - เซิร์ฟเวอร์ Model Context Protocol (MCP) สำหรับสร้างแผนผังความคิดแบบโต้ตอบที่สวยงาม
- [YuChenSSR/multi-ai-advisor](https://github.com/YuChenSSR/multi-ai-advisor-mcp) 📇 🏠 - เซิร์ฟเวอร์ Model Context Protocol (MCP) ที่สืบค้นโมเดล Ollama หลายตัวและรวมการตอบสนองของพวกมัน ให้มุมมอง AI ที่หลากหลายในคำถามเดียว
- [yWorks/mcp-typescribe](https://github.com/yWorks/mcp-typescribe) 📇 🏠 - เซิร์ฟเวอร์ MCP ที่ให้ข้อมูล Typescript API อย่างมีประสิทธิภาพแก่ตัวแทนเพื่อให้สามารถทำงานกับ API ที่ไม่ได้รับการฝึกฝน
- [zcaceres/fetch-mcp](https://github.com/zcaceres/fetch-mcp) 📇 🏠 - เซิร์ฟเวอร์ MCP เพื่อดึงข้อมูล JSON, ข้อความ และ HTML ได้อย่างยืดหยุ่น
- [zenml-io/mcp-zenml](https://github.com/zenml-io/mcp-zenml) 🐍 🏠 ☁️ - เซิร์ฟเวอร์ MCP เพื่อเชื่อมต่อกับไปป์ไลน์ MLOps และ LLMOps ของ [ZenML](https://www.zenml.io)
- [cjo4m06/mcp-shrimp-task-manager](https://github.com/cjo4m06/mcp-shrimp-task-manager) 📇 ☁️ 🏠 – ระบบจัดการงานที่ออกแบบมาสำหรับการเขียนโปรแกรมโดยเฉพาะ ช่วยเพิ่มประสิทธิภาพให้กับโค้ดดิ้งเอเจนต์อย่าง Cursor AI ด้วยหน่วยความจำงานขั้นสูง การสะท้อนตนเอง และการจัดการลำดับงาน [ShrimpTaskManager](https://cjo4m06.github.io/mcp-shrimp-task-manager)
- [axliupore/mcp-code-runner](https://github.com/axliupore/mcp-code-runner) 📇 🏠 - เซิร์ฟเวอร์ MCP สำหรับการรันโค้ดในเครื่องผ่าน Docker และรองรับภาษาการเขียนโปรแกรมหลายภาษา
- [lpigeon/ros-mcp-server](https://github.com/lpigeon/ros-mcp-server) 🐍 🏠 🍎 🪟 🐧 - เซิร์ฟเวอร์ ROS MCP ช่วยควบคุมหุ่นยนต์โดยแปลงคำสั่งภาษาธรรมชาติของผู้ใช้ให้เป็นคำสั่งควบคุม ROS หรือ ROS2
- [freema/mcp-design-system-extractor](https://github.com/freema/mcp-design-system-extractor) 📇 🏠 - ดึงข้อมูลคอมโพเนนต์จากระบบการออกแบบ Storybook ให้ HTML, สไตล์, props, การพึ่งพา, โทเค็นธีม และเมตาดาต้าของคอมโพเนนต์สำหรับการวิเคราะห์ระบบการออกแบบด้วย AI
- [HainanZhao/mcp-gitlab-jira](https://github.com/HainanZhao/mcp-gitlab-jira) 📇 ☁️ 🏠 - เซิร์ฟเวอร์ MCP แบบรวมสำหรับ GitLab และ Jira: จัดการโปรเจกต์, merge request, ไฟล์, รีลีส และตั๋วด้วยเอเจนต์ AI
- [gitkraken/gk-cli](https://github.com/gitkraken/gk-cli) 🎖️ 🏎️ 🏠 ☁️ 🍎 🪟 🐧 - CLI สำหรับโต้ตอบกับ GitKraken API โดยมีเซิร์ฟเวอร์ MCP ผ่าน gk mcp ซึ่งไม่เพียงแต่ครอบคลุม GitKraken API เท่านั้น แต่ยังรวมถึง Jira, GitHub, GitLab และอื่น ๆ อีกมากมาย รองรับการทำงานร่วมกับเครื่องมือในเครื่องและบริการระยะไกล.
- [lpigeon/unitree-go2-mcp-server](https://github.com/lpigeon/unitree-go2-mcp-server) 🐍 🏠 🐧 - เซิร์ฟเวอร์ Unitree Go2 MCP เป็นเซิร์ฟเวอร์ที่พัฒนาขึ้นบน MCP ซึ่งช่วยให้ผู้ใช้สามารถควบคุมหุ่นยนต์ Unitree Go2 ได้โดยใช้คำสั่งภาษาธรรมชาติที่แปลโดยโมเดลภาษาขนาดใหญ่ (LLM)
- [veelenga/claude-mermaid](https://github.com/veelenga/claude-mermaid/) 📇 🏠 🍎 🪟 🐧 - เซิร์ฟเวอร์ MCP สำหรับการเรนเดอร์ไดอะแกรม Mermaid สำหรับ Claude Code พร้อมฟังก์ชันการโหลดสดและรองรับรูปแบบการส่งออกหลายแบบ (SVG, PNG, PDF) และธีม

### 🧮 เครื่องมือวิทยาศาสตร์ข้อมูล

การผสานรวมและเครื่องมือที่ออกแบบมาเพื่อลดความซับซ้อนในการสำรวจข้อมูล การวิเคราะห์ และปรับปรุงเวิร์กโฟลว์วิทยาศาสตร์ข้อมูล

- [abhiphile/fermat-mcp](https://github.com/abhiphile/fermat-mcp) 🐍 🏠 🍎 🪟 🐧 - เครื่องมือคณิตศาสตร์ที่ทรงพลังที่รวม SymPy, NumPy และ Matplotlib ไว้ในเซิร์ฟเวอร์เดียว เหมาะสำหรับนักพัฒนาและนักวิจัยที่ต้องการพีชคณิตเชิงสัญลักษณ์ การคำนวณเชิงตัวเลข และการแสดงภาพข้อมูล
- [ChronulusAI/chronulus-mcp](https://github.com/ChronulusAI/chronulus-mcp) 🐍 ☁️ - ทำนายอะไรก็ได้ด้วยตัวแทนการพยากรณ์และการทำนายของ Chronulus AI
- [reading-plus-ai/mcp-server-data-exploration](https://github.com/reading-plus-ai/mcp-server-data-exploration) 🐍 ☁️ - เปิดใช้งานการสำรวจข้อมูลอัตโนมัติบนชุดข้อมูลที่ใช้ .csv ให้ข้อมูลเชิงลึกอัจฉริยะด้วยความพยายามน้อยที่สุด
- [zcaceres/markdownify-mcp](https://github.com/zcaceres/markdownify-mcp) 📇 🏠 - เซิร์ฟเวอร์ MCP เพื่อแปลงไฟล์หรือเนื้อหาเว็บเกือบทุกชนิดเป็น Markdown
- [jjsantos01/jupyter-notebook-mcp](https://github.com/jjsantos01/jupyter-notebook-mcp) 🐍 🏠 - เชื่อมต่อ Jupyter Notebook กับ Claude AI ช่วยให้ Claude สามารถโต้ตอบและควบคุม Jupyter Notebooks ได้โดยตรง

### 📟 ระบบฝังตัว

ให้การเข้าถึงเอกสารและทางลัดสำหรับการทำงานบนอุปกรณ์ฝังตัว

- [adancurusul/embedded-debugger-mcp](https://github.com/adancurusul/embedded-debugger-mcp) 🦀 📟 - เซิร์ฟเวอร์โปรโตคอลบริบทโมเดลสำหรับการดีบักระบบฝังตัวด้วย probe-rs - รองรับการดีบัก ARM Cortex-M, RISC-V ผ่าน J-Link, ST-Link และอื่นๆ
- [adancurusul/serial-mcp-server](https://github.com/adancurusul/serial-mcp-server) 🦀 📟 - เซิร์ฟเวอร์ MCP ที่ครอบคลุมสำหรับการสื่อสารพอร์ตอนุกรม
- [horw/esp-mcp](https://github.com/horw/esp-mcp) 📟 - เวิร์กโฟลว์สำหรับการแก้ไขปัญหาการสร้างในชิปซีรีส์ ESP32 โดยใช้ ESP-IDF
- [stack-chan/stack-chan](https://github.com/stack-chan/stack-chan) 📇 📟 - หุ่นยนต์น่ารักที่ขับเคลื่อนด้วย JavaScript บน M5Stack พร้อมฟังก์ชัน MCP server สำหรับการโต้ตอบและอารมณ์ที่ควบคุมด้วย AI

### 📂 ระบบไฟล์

ให้การเข้าถึงระบบไฟล์ในเครื่องโดยตรงพร้อมสิทธิ์ที่กำหนดค่าได้ ช่วยให้โมเดล AI สามารถอ่าน เขียน และจัดการไฟล์ภายในไดเร็กทอรีที่ระบุ

- [8b-is/smart-tree](https://github.com/8b-is/smart-tree) 🦀 🏠 🍎 🪟 🐧 - การแสดงผลไดเร็กทอรีแบบ AI-native พร้อมการวิเคราะห์เชิงความหมาย รูปแบบบีบอัดขั้นสูงสำหรับการใช้งาน AI และลดโทเค็น 10 เท่า รองรับโหมด quantum-semantic พร้อมการจัดหมวดหมู่ไฟล์อัจฉริยะ
- [cyberchitta/llm-context.py](https://github.com/cyberchitta/llm-context.py) 🐍 🏠 - แบ่งปันบริบทโค้ดกับ LLMs ผ่าน MCP หรือคลิปบอร์ด
- [exoticknight/mcp-file-merger](https://github.com/exoticknight/mcp-file-merger) 🏎️ 🏠 - เครื่องมือรวมไฟล์ เหมาะสำหรับขีดจำกัดความยาวของการแชท AI
- [filesystem@quarkiverse/quarkus-mcp-servers](https://github.com/quarkiverse/quarkus-mcp-servers/tree/main/filesystem) ☕ 🏠 - ระบบไฟล์ที่อนุญาตให้เรียกดูและแก้ไขไฟล์ที่ใช้งานใน Java โดยใช้ Quarkus มีให้ใช้งานเป็น jar หรือ native image
- [hmk/box-mcp-server](https://github.com/hmk/box-mcp-server) 📇 ☁️ - การผสานรวม Box สำหรับการแสดงรายการ อ่าน และค้นหาไฟล์
- [mamertofabian/mcp-everything-search](https://github.com/mamertofabian/mcp-everything-search) 🐍 🏠 🪟 - ค้นหาไฟล์ Windows อย่างรวดเร็วโดยใช้ Everything SDK
- [mark3labs/mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server) 🏎️ 🏠 - การใช้งาน Golang สำหรับการเข้าถึงระบบไฟล์ในเครื่อง
- [modelcontextprotocol/server-filesystem](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/filesystem) 📇 🏠 - การเข้าถึงระบบไฟล์ในเครื่องโดยตรง
- [modelcontextprotocol/server-google-drive](https://github.com/modelcontextprotocol/servers/tree/main/src/gdrive) 📇 ☁️ - การผสานรวม Google Drive สำหรับการแสดงรายการ อ่าน และค้นหาไฟล์
- [Xuanwo/mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal) 🐍 🏠 ☁️ - เข้าถึงที่เก็บข้อมูลใดๆ ด้วย Apache OpenDAL™

### 💰 การเงินและฟินเทค

เครื่องมือเข้าถึงและวิเคราะห์ข้อมูลทางการเงิน ช่วยให้โมเดล AI สามารถทำงานกับข้อมูลตลาด แพลตฟอร์มการซื้อขาย และข้อมูลทางการเงิน

- [qiniu/qiniu-mcp-server](https://github.com/qiniu/qiniu-mcp-server) 🐍 ☁️ - MCP ที่สร้างจากผลิตภัณฑ์ของ Qiniu Cloud รองรับการเข้าถึงบริการจัดเก็บข้อมูล Qiniu Cloud, บริการมัลติมีเดียอัจฉริยะ และอื่นๆ
- [anjor/coinmarket-mcp-server](https://github.com/anjor/coinmarket-mcp-server) 🐍 ☁️ - การผสานรวม Coinmarket API เพื่อดึงรายการและราคา cryptocurrency
- [bankless/onchain-mcp](https://github.com/Bankless/onchain-mcp/) 📇 ☁️ - Bankless Onchain API เพื่อโต้ตอบกับสัญญาอัจฉริยะ สืบค้นข้อมูลธุรกรรมและโทเค็น
- [base/base-mcp](https://github.com/base/base-mcp) 🎖️ 📇 ☁️ - การผสานรวม Base Network สำหรับเครื่องมือ onchain ช่วยให้สามารถโต้ตอบกับ Base Network และ Coinbase API สำหรับการจัดการกระเป๋าเงิน การโอนเงิน สัญญาอัจฉริยะ และการดำเนินการ DeFi
- [berlinbra/alpha-vantage-mcp](https://github.com/berlinbra/alpha-vantage-mcp) 🐍 ☁️ - การผสานรวม Alpha Vantage API เพื่อดึงข้อมูลทั้งหุ้นและ crypto
- [bitteprotocol/mcp](https://github.com/BitteProtocol/mcp) 📇 - การผสานรวม Bitte Protocol เพื่อรันตัวแทน AI บนบล็อกเชนหลายตัว
- [chargebee/mcp](https://github.com/chargebee/agentkit/tree/main/modelcontextprotocol) 🎖️ 📇 ☁️ - เซิร์ฟเวอร์ MCP ที่เชื่อมต่อตัวแทน AI กับแพลตฟอร์ม [Chargebee](https://www.chargebee.com/)
- [debridge-finance/debridge-mcp](https://github.com/debridge-finance/debridge-mcp) [glama](https://glama.ai/mcp/servers/@debridge-finance/de-bridge) 📇 🏠 ☁️ - การสลับข้ามเชนและการเชื่อมต่อระหว่างบล็อกเชน EVM และ Solana ผ่านโปรโตคอล deBridge ช่วยให้ตัวแทน AI ค้นหาเส้นทางที่เหมาะสมที่สุด ประเมินค่าธรรมเนียม และเริ่มต้นการซื้อขายแบบไม่ต้องฝากเงิน
- [ferdousbhai/investor-agent](https://github.com/ferdousbhai/investor-agent) 🐍 ☁️ - การผสานรวม Yahoo Finance เพื่อดึงข้อมูลตลาดหุ้น รวมถึงคำแนะนำออปชัน
- [ferdousbhai/tasty-agent](https://github.com/ferdousbhai/tasty-agent) 🐍 ☁️ - การผสานรวม Tastyworks API เพื่อจัดการกิจกรรมการซื้อขายบน Tastytrade
- [getalby/nwc-mcp-server](https://github.com/getalby/nwc-mcp-server) 📇 🏠 - การผสานรวมกระเป๋าเงิน Bitcoin Lightning ขับเคลื่อนโดย Nostr Wallet Connect
- [heurist-network/heurist-mesh-mcp-server](https://github.com/heurist-network/heurist-mesh-mcp-server) 🎖️ ⛅️ 🏠 🐍 - เข้าถึงตัวแทน AI web3 เฉพาะทางสำหรับการวิเคราะห์บล็อกเชน การตรวจสอบความปลอดภัยของสัญญาอัจฉริยะ การประเมินเมตริกโทเค็น และการโต้ตอบบนเชนผ่านเครือข่าย Heurist Mesh ให้เครื่องมือที่ครอบคลุมสำหรับการวิเคราะห์ DeFi การประเมินมูลค่า NFT และการตรวจสอบธุรกรรมในบล็อกเชนหลายตัว
- [hoqqun/stooq-mcp](https://github.com/hoqqun/stooq-mcp) 🦀 ☁️ - ดึงราคาหุ้นแบบเรียลไทม์จาก Stooq โดยไม่ต้องใช้ API key รองรับตลาดทั่วโลก (สหรัฐอเมริกา, ญี่ปุ่น, สหราชอาณาจักร, เยอรมนี)
- [@iiatlas/hledger-mcp](https://github.com/iiAtlas/hledger-mcp) 📇 🏠 🍎 🪟 - การบันทึกบัญชีแบบ double entry ในรูปแบบข้อความล้วน ภายใน LLM ของคุณ! MCP นี้รองรับการเข้าถึงไฟล์ journal ของ [HLedger](https://hledger.org/) บนเครื่องในโหมดอ่านอย่างครบถ้วน และ (เลือกได้) การเขียนด้วย
- [kukapay/crypto-feargreed-mcp](https://github.com/kukapay/crypto-feargreed-mcp) 🐍 ☁️ - ให้ข้อมูลดัชนี Crypto Fear & Greed แบบเรียลไทม์และย้อนหลัง
- [kukapay/crypto-indicators-mcp](https://github.com/kukapay/crypto-indicators-mcp) 🐍 ☁️ - เซิร์ฟเวอร์ MCP ที่ให้ตัวบ่งชี้และกลยุทธ์การวิเคราะห์ทางเทคนิคของ cryptocurrency ที่หลากหลาย
- [kukapay/crypto-sentiment-mcp](https://github.com/kukapay/crypto-sentiment-mcp) 🐍 ☁️ - เซิร์ฟเวอร์ MCP ที่ส่งการวิเคราะห์ความเชื่อมั่นของ cryptocurrency ให้กับตัวแทน AI
- [kukapay/cryptopanic-mcp-server](https://github.com/kukapay/cryptopanic-mcp-server) 🐍 ☁️ - ให้ข่าวสาร cryptocurrency ล่าสุดแก่ตัวแทน AI ขับเคลื่อนโดย CryptoPanic
- [kukapay/dune-analytics-mcp](https://github.com/kukapay/dune-analytics-mcp) 🐍 ☁️ - เซิร์ฟเวอร์ mcp ที่เชื่อมโยงข้อมูล Dune Analytics กับตัวแทน AI
- [kukapay/freqtrade-mcp](https://github.com/kukapay/freqtrade-mcp) 🐍 ☁️ - เซิร์ฟเวอร์ MCP ที่ผสานรวมกับบอทซื้อขาย cryptocurrency Freqtrade
- [kukapay/jupiter-mcp](https://github.com/kukapay/jupiter-mcp) 🐍 ☁️ - เซิร์ฟเวอร์ MCP สำหรับดำเนินการแลกเปลี่ยนโทเค็นบนบล็อกเชน Solana โดยใช้ Ultra API ใหม่ของ Jupiter
- [kukapay/pancakeswap-poolspy-mcp](https://github.com/kukapay/pancakeswap-poolspy-mcp) 🐍 ☁️ - เซิร์ฟเวอร์ MCP ที่ติดตามพูลที่สร้างขึ้นใหม่บน Pancake Swap
- [kukapay/rug-check-mcp](https://github.com/kukapay/rug-check-mcp) 🐍 ☁️ - เซิร์ฟเวอร์ MCP ที่ตรวจจับความเสี่ยงที่อาจเกิดขึ้นในโทเค็นมีม Solana
- [kukapay/thegraph-mcp](https://github.com/kukapay/thegraph-mcp) 🐍 ☁️ - เซิร์ฟเวอร์ MCP ที่ขับเคลื่อนตัวแทน AI ด้วยข้อมูลบล็อกเชนที่จัดทำดัชนีจาก The Graph
- [kukapay/token-minter-mcp](https://github.com/kukapay/token-minter-mcp) 🐍 ☁️ - เซิร์ฟเวอร์ MCP ที่มีเครื่องมือสำหรับตัวแทน AI เพื่อสร้างโทเค็น ERC-20 ในบล็อกเชนหลายตัว
- [kukapay/token-revoke-mcp](https://github.com/kukapay/token-revoke-mcp) 🐍 ☁️ - เซิร์ฟเวอร์ MCP สำหรับตรวจสอบและเพิกถอนการอนุญาตโทเค็น ERC-20 ในบล็อกเชนหลายตัว
- [kukapay/uniswap-poolspy-mcp](https://github.com/kukapay/uniswap-poolspy-mcp) 🐍 ☁️ - เซิร์ฟเวอร์ MCP ที่ติดตามพูลสภาพคล่องที่สร้างขึ้นใหม่บน Uniswap ในบล็อกเชนหลายตัว
- [kukapay/uniswap-trader-mcp](https://github.com/kukapay/uniswap-trader-mcp) 🐍 ☁️ - เซิร์ฟเวอร์ MCP สำหรับตัวแทน AI เพื่อทำการแลกเปลี่ยนโทเค็นอัตโนมัติบน Uniswap DEX ในบล็อกเชนหลายตัว
- [kukapay/whale-tracker-mcp](https://github.com/kukapay/whale-tracker-mcp) 🐍 ☁️ - เซิร์ฟเวอร์ mcp สำหรับติดตามธุรกรรมวาฬ cryptocurrency
- [longportapp/openapi](https://github.com/longportapp/openapi/tree/main/mcp) - 🐍 ☁️ - LongPort OpenAPI ให้ข้อมูลตลาดหุ้นแบบเรียลไทม์ ให้การเข้าถึงการวิเคราะห์และความสามารถในการซื้อขายของ AI ผ่าน MCP
- [mcpdotdirect/evm-mcp-server](https://github.com/mcpdotdirect/evm-mcp-server) 📇 ☁️ - บริการบล็อกเชนที่ครอบคลุมสำหรับเครือข่าย EVM มากกว่า 30 เครือข่าย รองรับโทเค็นเนทีฟ, ERC20, NFTs, สัญญาอัจฉริยะ, ธุรกรรม และการแก้ไข ENS
- [mcpdotdirect/starknet-mcp-server](https://github.com/mcpdotdirect/starknet-mcp-server) 📇 ☁️ - การผสานรวมบล็อกเชน Starknet ที่ครอบคลุมพร้อมการสนับสนุนโทเค็นเนทีฟ (ETH, STRK), สัญญาอัจฉริยะ, การแก้ไข StarknetID และการโอนโทเค็น
- [minhyeoky/mcp-server-ledger](https://github.com/minhyeoky/mcp-server-ledger) 🐍 🏠 - การผสานรวม ledger-cli สำหรับการจัดการธุรกรรมทางการเงินและการสร้างรายงาน
- [openMF/mcp-mifosx](https://github.com/openMF/mcp-mifosx) ☁️ 🏠 - การผสานรวม core banking สำหรับการจัดการลูกค้า สินเชื่อ เงินฝาก หุ้น ธุรกรรมทางการเงิน และการสร้างรายงานทางการเงิน
- [narumiruna/yfinance-mcp](https://github.com/narumiruna/yfinance-mcp) 🐍 ☁️ - เซิร์ฟเวอร์ MCP ที่ใช้ yfinance เพื่อรับข้อมูลจาก Yahoo Finance
- [pwh-pwh/coin-mcp-server](https://github.com/pwh-pwh/coin-mcp-server) 🐍 ☁️ - Bitget API เพื่อดึงราคา cryptocurrency
- [QuantGeekDev/coincap-mcp](https://github.com/QuantGeekDev/coincap-mcp) 📇 ☁️ - การผสานรวมข้อมูลตลาด cryptocurrency แบบเรียลไทม์โดยใช้ API สาธารณะของ CoinCap ให้การเข้าถึงราคา crypto และข้อมูลตลาดโดยไม่ต้องใช้คีย์ API
- [SaintDoresh/Crypto-Trader-MCP-ClaudeDesktop](https://github.com/SaintDoresh/Crypto-Trader-MCP-ClaudeDesktop.git) 🐍 ☁️ - เครื่องมือ MCP ที่ให้ข้อมูลตลาด cryptocurrency โดยใช้ CoinGecko API
- [SaintDoresh/YFinance-Trader-MCP-ClaudeDesktop](https://github.com/SaintDoresh/YFinance-Trader-MCP-ClaudeDesktop.git) 🐍 ☁️ - เครื่องมือ MCP ที่ให้ข้อมูลตลาดหุ้นและการวิเคราะห์โดยใช้ Yahoo Finance API
- [HuggingAGI/mcp-baostock-server](https://github.com/HuggingAGI/mcp-baostock-server) 🐍 ☁️ - เซิร์ฟเวอร์ MCP ที่ใช้ baostock เป็นฐาน ให้การเข้าถึงและวิเคราะห์ข้อมูลตลาดหุ้นจีน
- [Wuye-AI/mcp-server-wuye-ai](https://github.com/wuye-ai/mcp-server-wuye-ai) 🎖️ 📇 ☁️ - เซิร์ฟเวอร์ MCP ที่เชื่อมต่อกับแพลตฟอร์ม CRIC Wuye AI โดย CRIC Wuye AI เป็นผู้ช่วย AI อัจฉริยะที่บริษัท CRIC พัฒนาขึ้นสำหรับอุตสาหกรรมการบริหารอสังหาริมทรัพย์
- [JamesANZ/evm-mcp](https://github.com/JamesANZ/evm-mcp) 📇 ☁️ - เซิร์ฟเวอร์ MCP ที่ให้การเข้าถึงแบบสมบูรณ์ไปยังเมธอด JSON-RPC ของ Ethereum Virtual Machine (EVM) ทำงานร่วมกับผู้ให้บริการโหนดที่เข้ากันได้กับ EVM ใดๆ รวมถึง Infura, Alchemy, QuickNode, โหนดท้องถิ่น และอื่นๆ
- [JamesANZ/prediction-market-mcp](https://github.com/JamesANZ/prediction-market-mcp) 📇 ☁️ - เซิร์ฟเวอร์ MCP ที่ให้ข้อมูลตลาดการพยากรณ์แบบเรียลไทม์จากหลายแพลตฟอร์มรวมถึง Polymarket, PredictIt และ Kalshi ช่วยให้ผู้ช่วย AI สามารถสืบค้นอัตราต่อรองปัจจุบัน ราคา และข้อมูลตลาดผ่านอินเทอร์เฟซที่รวมเป็นหนึ่งเดียว
- [JamesANZ/bitcoin-mcp](https://github.com/JamesANZ/bitcoin-mcp) 📇 🏠 - เซิร์ฟเวอร์ MCP ที่ช่วยให้โมเดล AI สามารถสืบค้นบล็อกเชน Bitcoin ได้

### 🎮 เกม

การผสานรวมกับข้อมูลที่เกี่ยวข้องกับเกม เอนจิ้นเกม และบริการ

- [CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity) 📇 #️⃣ 🏠 - เซิร์ฟเวอร์ MCP สำหรับการผสานรวม Unity3d Game Engine สำหรับการพัฒนาเกม
- [Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp) 📇 🏠 - เซิร์ฟเวอร์ MCP สำหรับโต้ตอบกับเอนจิ้นเกม Godot ให้เครื่องมือสำหรับการแก้ไข รัน ดีบัก และจัดการฉากในโปรเจ็กต์ Godot
- [pab1ito/chess-mcp](https://github.com/pab1it0/chess-mcp) 🐍 ☁️ - เข้าถึงข้อมูลผู้เล่น Chess.com บันทึกเกม และข้อมูลสาธารณะอื่นๆ ผ่านอินเทอร์เฟซ MCP มาตรฐาน ช่วยให้ผู้ช่วย AI สามารถค้นหาและวิเคราะห์ข้อมูลหมากรุก
- [rishijatia/fantasy-pl-mcp](https://github.com/rishijatia/fantasy-pl-mcp/) 🐍 ☁️ - เซิร์ฟเวอร์ MCP สำหรับข้อมูล Fantasy Premier League แบบเรียลไทม์และเครื่องมือวิเคราะห์
- [opgginc/opgg-mcp](https://github.com/opgginc/opgg-mcp) 📇 ☁️ - เข้าถึงข้อมูลเกมแบบเรียลไทม์จากเกมยอดนิยมเช่น League of Legends, TFT และ Valorant นำเสนอการวิเคราะห์แชมเปี้ยน ตารางการแข่งขันอีสปอร์ต องค์ประกอบเมต้า และสถิติตัวละคร

### 🧠 ความรู้และความจำ

การจัดเก็บหน่วยความจำถาวรโดยใช้โครงสร้างกราฟความรู้ ช่วยให้โมเดล AI สามารถรักษาและสืบค้นข้อมูลที่มีโครงสร้างข้ามเซสชัน

- [apecloud/ApeRAG](https://github.com/apecloud/ApeRAG) 🐍 ☁️ 🏠 - แพลตฟอร์ม RAG ระดับโปรดักชันที่รวม Graph RAG การค้นหาเวกเตอร์ และการค้นหาข้อความแบบเต็ม ตัวเลือกที่ดีที่สุดสำหรับสร้างกราฟความรู้ของคุณเองและสำหรับวิศวกรรมบริบท
- [CheMiguel23/MemoryMesh](https://github.com/CheMiguel23/MemoryMesh) 📇 🏠 - หน่วยความจำแบบกราฟที่ปรับปรุงแล้วโดยเน้นที่การเล่นบทบาท AI และการสร้างเรื่องราว
- [graphlit-mcp-server](https://github.com/graphlit/graphlit-mcp-server) 📇 ☁️ - นำเข้าอะไรก็ได้จาก Slack, Discord, เว็บไซต์, Google Drive, Linear หรือ GitHub ลงในโปรเจ็กต์ Graphlit - จากนั้นค้นหาและดึงความรู้ที่เกี่ยวข้องภายในไคลเอนต์ MCP เช่น Cursor, Windsurf หรือ Cline
- [hannesrudolph/mcp-ragdocs](https://github.com/hannesrudolph/mcp-ragdocs) 🐍 🏠 - การใช้งานเซิร์ฟเวอร์ MCP ที่มีเครื่องมือสำหรับดึงและประมวลผลเอกสารผ่านการค้นหาเวกเตอร์ ช่วยให้ผู้ช่วย AI สามารถเสริมการตอบสนองด้วยบริบทเอกสารที่เกี่ยวข้อง
- [jinzcdev/markmap-mcp-server](https://github.com/jinzcdev/markmap-mcp-server) 📇 🏠 - เซิร์ฟเวอร์ MCP ที่สร้างขึ้นบน [markmap](https://github.com/markmap/markmap) ซึ่งแปลง **Markdown** เป็น**แผนผังความคิด**แบบโต้ตอบได้ รองรับการส่งออกหลายรูปแบบ (PNG/JPG/SVG) การแสดงตัวอย่างในเบราว์เซอร์แบบเรียลไทม์ การคัดลอก Markdown ด้วยคลิกเดียว และคุณสมบัติการแสดงผลแบบไดนามิก
- [kaliaboi/mcp-zotero](https://github.com/kaliaboi/mcp-zotero) 📇 ☁️ - ตัวเชื่อมต่อสำหรับ LLMs เพื่อทำงานกับคอลเลกชันและแหล่งข้อมูลบน Zotero Cloud ของคุณ
- [mcp-summarizer](https://github.com/0xshellming/mcp-summarizer) 📕 ☁️ - เซิร์ฟเวอร์ MCP สรุป AI รองรับเนื้อหาหลายประเภท: ข้อความธรรมดา, หน้าเว็บ, เอกสาร PDF, หนังสือ EPUB, เนื้อหา HTML
- [mem0ai/mem0-mcp](https://github.com/mem0ai/mem0-mcp) 🐍 🏠 - เซิร์ฟเวอร์ Model Context Protocol สำหรับ Mem0 ที่ช่วยจัดการการตั้งค่าและรูปแบบการเขียนโค้ด ให้เครื่องมือสำหรับจัดเก็บ ดึงข้อมูล และจัดการการใช้งานโค้ด แนวทางปฏิบัติที่ดีที่สุด และเอกสารทางเทคนิคใน IDE เช่น Cursor และ Windsurf
- [modelcontextprotocol/server-memory](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/memory) 📇 🏠 - ระบบหน่วยความจำถาวรแบบกราฟความรู้สำหรับรักษาบริบท
- [@ragieai/mcp-server](https://github.com/ragieai/ragie-mcp-server) 📇 ☁️ - ดึงบริบทจากฐานความรู้ [Ragie](https://www.ragie.ai) (RAG) ของคุณที่เชื่อมต่อกับการผสานรวมต่างๆ เช่น Google Drive, Notion, JIRA และอื่นๆ
- [JamesANZ/memory-mcp](https://github.com/JamesANZ/memory-mcp) 📇 🏠 - เซิร์ฟเวอร์ MCP ที่จัดเก็บและดึงข้อมูลความจำจากหลาย LLMs โดยใช้ MongoDB ให้เครื่องมือสำหรับการบันทึก ดึงข้อมูล เพิ่ม และล้างความจำการสนทนาพร้อมกับไทม์สแตมป์และการระบุ LLM
- [JamesANZ/cross-llm-mcp](https://github.com/JamesANZ/cross-llm-mcp) 📇 🏠 - เซิร์ฟเวอร์ MCP ที่ช่วยให้การสื่อสารข้าม LLM และการแบ่งปันความจำ ช่วยให้โมเดล AI ที่แตกต่างกันสามารถทำงานร่วมกันและแบ่งปันบริบทระหว่างการสนทนา
- [topoteretes/cognee](https://github.com/topoteretes/cognee/tree/dev/cognee-mcp) 📇 🏠 - ตัวจัดการหน่วยความจำสำหรับแอป AI และตัวแทนโดยใช้กราฟและที่เก็บเวกเตอร์ต่างๆ และอนุญาตการนำเข้าจากแหล่งข้อมูลมากกว่า 30 แหล่ง

### ⚖️ กฎหมาย

การเข้าถึงข้อมูลทางกฎหมาย กฎหมาย และฐานข้อมูลกฎหมาย ช่วยให้โมเดล AI สามารถค้นหาและวิเคราะห์เอกสารทางกฎหมายและข้อมูลด้านกฎระเบียบ

- [JamesANZ/us-legal-mcp](https://github.com/JamesANZ/us-legal-mcp) 📇 ☁️ - เซิร์ฟเวอร์ MCP ที่ให้กฎหมายของสหรัฐอเมริกาอย่างครอบคลุม

### 🗺️ บริการตำแหน่ง

บริการตามตำแหน่งและเครื่องมือแผนที่ ช่วยให้โมเดล AI สามารถทำงานกับข้อมูลทางภูมิศาสตร์ ข้อมูลสภาพอากาศ และการวิเคราะห์ตามตำแหน่ง

- [briandconnelly/mcp-server-ipinfo](https://github.com/briandconnelly/mcp-server-ipinfo) 🐍 ☁️ - ตำแหน่งทางภูมิศาสตร์ของที่อยู่ IP และข้อมูลเครือข่ายโดยใช้ IPInfo API
- [isdaniel/mcp_weather_server](https://github.com/isdaniel/mcp_weather_server) 🐍 ☁️ - รับข้อมูลสภาพอากาศจาก https://api.open-meteo.com API
- [kukapay/nearby-search-mcp](https://github.com/kukapay/nearby-search-mcp) 🐍 ☁️ - เซิร์ฟเวอร์ MCP สำหรับการค้นหาสถานที่ใกล้เคียงพร้อมการตรวจจับตำแหน่งตาม IP
- [modelcontextprotocol/server-google-maps](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/google-maps) 📇 ☁️ - การผสานรวม Google Maps สำหรับบริการตำแหน่ง การกำหนดเส้นทาง และรายละเอียดสถานที่
- [QGIS MCP](https://github.com/jjsantos01/qgis_mcp) - เชื่อมต่อ QGIS Desktop กับ Claude AI ผ่าน MCP การผสานรวมนี้ช่วยให้สามารถสร้างโปรเจ็กต์ โหลดเลเยอร์ เรียกใช้โค้ด และอื่นๆ โดยใช้พรอมต์ช่วย
- [SaintDoresh/Weather-MCP-ClaudeDesktop](https://github.com/SaintDoresh/Weather-MCP-ClaudeDesktop.git) 🐍 ☁️ - เครื่องมือ MCP ที่ให้ข้อมูลสภาพอากาศแบบเรียลไทม์ การพยากรณ์ และข้อมูลสภาพอากาศย้อนหลังโดยใช้ OpenWeatherMap API
- [SecretiveShell/MCP-timeserver](https://github.com/SecretiveShell/MCP-timeserver) 🐍 🏠 - เข้าถึงเวลาในเขตเวลาใดก็ได้และรับเวลาท้องถิ่นปัจจุบัน
- [webcoderz/MCP-Geo](https://github.com/webcoderz/MCP-Geo) 🐍 🏠 - เซิร์ฟเวอร์ MCP การเข้ารหัสทางภูมิศาสตร์สำหรับ nominatim, ArcGIS, Bing

### 🎯 การตลาด

เครื่องมือสำหรับสร้างและแก้ไขเนื้อหาทางการตลาด ทำงานกับข้อมูลเมตาเว็บ การวางตำแหน่งผลิตภัณฑ์ และคู่มือการแก้ไข

- [AdsMCP/tiktok-ads-mcp-server](https://github.com/AdsMCP/tiktok-ads-mcp-server) 🐍 ☁️ - เซิร์ฟเวอร์ Model Context Protocol สำหรับการผสานรวม TikTok Ads API ช่วยให้ผู้ช่วย AI สามารถจัดการแคมเปญ วิเคราะห์เมตริกประสิทธิภาพ จัดการกลุ่มเป้าหมายและสร้างสรรค์ผ่านการรับรองตัวตน OAuth
- [Open Strategy Partners Marketing Tools](https://github.com/open-strategy-partners/osp_marketing_tools) 🐍 🏠 - ชุดเครื่องมือทางการตลาดจาก Open Strategy Partners รวมถึงรูปแบบการเขียน รหัสการแก้ไข และการสร้างแผนที่มูลค่าการตลาดผลิตภัณฑ์

### 📊 การตรวจสอบ

เข้าถึงและวิเคราะห์ข้อมูลการตรวจสอบแอปพลิเคชัน ช่วยให้โมเดล AI สามารถตรวจสอบรายงานข้อผิดพลาดและเมตริกประสิทธิภาพ

- [grafana-loki-mcp](https://github.com/tumf/grafana-loki-mcp) 🐍 🏠 - เซิร์ฟเวอร์ MCP ที่อนุญาตให้สืบค้นบันทึก Loki ผ่าน Grafana API
- [grafana/mcp-grafana](https://github.com/grafana/mcp-grafana) 🎖️ 🐍 🏠 ☁️ - ค้นหาแดชบอร์ด ตรวจสอบเหตุการณ์ และสืบค้นแหล่งข้อมูลในอินสแตนซ์ Grafana ของคุณ
- [hyperb1iss/lucidity-mcp](https://github.com/hyperb1iss/lucidity-mcp) 🐍 🏠 - ปรับปรุงคุณภาพโค้ดที่สร้างโดย AI ผ่านการวิเคราะห์อัจฉริยะตามพรอมต์ใน 10 มิติที่สำคัญตั้งแต่ความซับซ้อนไปจนถึงช่องโหว่ด้านความปลอดภัย
- [inventer-dev/mcp-internet-speed-test](https://github.com/inventer-dev/mcp-internet-speed-test) 🐍 ☁️ - การทดสอบความเร็วอินเตอร์เน็ตด้วยเมตริกประสิทธิภาพเครือข่ายรวมถึงความเร็วดาวน์โหลด/อัพโหลด ความล่าช้า การวิเคราะห์จิตเตอร์ และการตรวจจับเซิร์ฟเวอร์ CDN ด้วยการแมพภูมิศาสตร์
- [last9/last9-mcp-server](https://github.com/last9/last9-mcp-server) - นำบริบทการผลิตแบบเรียลไทม์—บันทึก เมตริก และการติดตาม—เข้าสู่สภาพแวดล้อมในเครื่องของคุณเพื่อแก้ไขโค้ดอัตโนมัติได้เร็วขึ้น
- [metoro-io/metoro-mcp-server](https://github.com/metoro-io/metoro-mcp-server) 🎖️ 🏎️ ☁️ - สืบค้นและโต้ตอบกับสภาพแวดล้อม kubernetes ที่ตรวจสอบโดย Metoro
- [modelcontextprotocol/server-raygun](https://github.com/MindscapeHQ/mcp-server-raygun) 📇 ☁️ - การผสานรวม Raygun API V3 สำหรับการรายงานข้อขัดข้องและการตรวจสอบผู้ใช้จริง
- [modelcontextprotocol/server-sentry](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry) 🐍 ☁️ - การผสานรวม Sentry.io สำหรับการติดตามข้อผิดพลาดและการตรวจสอบประสิทธิภาพ
- [pydantic/logfire-mcp](https://github.com/pydantic/logfire-mcp) 🎖️ 🐍 ☁️ - ให้การเข้าถึงการติดตามและเมตริก OpenTelemetry ผ่าน Logfire
- [seekrays/mcp-monitor](https://github.com/seekrays/mcp-monitor) 🏎️ 🏠 - เครื่องมือตรวจสอบระบบที่เปิดเผยเมตริกระบบผ่าน Model Context Protocol (MCP) เครื่องมือนี้ช่วยให้ LLMs สามารถดึงข้อมูลระบบแบบเรียลไทม์ผ่านอินเทอร์เฟซที่เข้ากันได้กับ MCP (รองรับ CPU, หน่วยความจำ, ดิสก์, เครือข่าย, โฮสต์, กระบวนการ)

### 🔎 <a name="search"></a>การค้นหาและการดึงข้อมูล

- [scrapeless-ai/scrapeless-mcp-server](https://github.com/scrapeless-ai/scrapeless-mcp-server) 🐍 ☁️ - บริการ Scrapeless Model Context Protocol ทำหน้าที่เป็นตัวเชื่อมเซิร์ฟเวอร์ MCP กับ Google SERP API ช่วยให้สามารถค้นหาเว็บภายในระบบนิเวศ MCP โดยไม่ต้องออกจากมัน
- [ac3xx/mcp-servers-kagi](https://github.com/ac3xx/mcp-servers-kagi) 📇 ☁️ - การรวม API การค้นหาของ Kagi
- [andybrandt/mcp-simple-arxiv](https://github.com/andybrandt/mcp-simple-arxiv) - 🐍 ☁️ MCP สำหรับ LLM เพื่อค้นหาและอ่านเอกสารจาก arXiv
- [andybrandt/mcp-simple-pubmed](https://github.com/andybrandt/mcp-simple-pubmed) - 🐍 ☁️ MCP เพื่อค้นหาและอ่านเอกสารทางการแพทย์/วิทยาศาสตร์ชีวภาพจาก PubMed
- [angheljf/nyt](https://github.com/angheljf/nyt) 📇 ☁️ - ค้นหาบทความโดยใช้ API ของ NYTimes
- [apify/mcp-server-rag-web-browser](https://github.com/apify/mcp-server-rag-web-browser) 📇 ☁️ - เซิร์ฟเวอร์ MCP สำหรับ RAG Web Browser Actor แบบโอเพ่นซอร์สของ Apify เพื่อทำการค้นหาเว็บ สแครป URL และส่งคืนเนื้อหาในรูปแบบ Markdown
- [Bigsy/Clojars-MCP-Server](https://github.com/Bigsy/Clojars-MCP-Server) 📇 ☁️ - เซิร์ฟเวอร์ MCP ของ Clojars เพื่อข้อมูลการพึ่งพาล่าสุดของไลบรารี Clojure
- [blazickjp/arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) ☁️ 🐍 - ค้นหาเอกสารวิจัยจาก ArXiv
- [chanmeng/google-news-mcp-server](https://github.com/ChanMeng666/server-google-news) 📇 ☁️ - การรวม Google News พร้อมการจัดหมวดหมู่หัวข้ออัตโนมัติ รองรับหลายภาษา และความสามารถในการค้นหาที่ครอบคลุม รวมถึงพาดหัว เรื่องราว และหัวข้อที่เกี่ยวข้องผ่าน [SerpAPI](https://serpapi.com/)
- [ConechoAI/openai-websearch-mcp](https://github.com/ConechoAI/openai-websearch-mcp/) 🐍 🏠 ☁️ - เซิร์ฟเวอร์ MCP ที่ใช้ Python ซึ่งให้เครื่องมือ `web_search` ในตัวของ OpenAI
- [devflowinc/trieve](https://github.com/devflowinc/trieve/tree/main/clients/mcp-server) 🎖️ 📇 ☁️ 🏠 - คลานฝังตัว แบ่งส่วน ค้นหา และดึงข้อมูลจากชุดข้อมูลผ่าน [Trieve](https://trieve.ai)
- [DappierAI/dappier-mcp](https://github.com/DappierAI/dappier-mcp) 🐍 ☁️ - เซิร์ฟเวอร์ MCP ของ Dappier ช่วยให้ค้นหาเว็บแบบเรียลไทม์ได้อย่างรวดเร็วและฟรี พร้อมเข้าถึงข้อมูลระดับพรีเมียมจากแบรนด์สื่อที่เชื่อถือได้ เช่น ข่าว ตลาดการเงิน กีฬา บันเทิง สภาพอากาศ และอื่นๆ เพื่อสร้างเอเจนต์ AI อันทรงพลัง
- [Dumpling-AI/mcp-server-dumplingai](https://github.com/Dumpling-AI/mcp-server-dumplingai) 🎖️ 📇 ☁️ - เข้าถึงข้อมูล การสแครปเว็บ และ API การแปลงเอกสารโดย [Dumpling AI](https://www.dumplingai.com/)
- [erithwik/mcp-hn](https://github.com/erithwik/mcp-hn) 🐍 ☁️ - เซิร์ฟเวอร์ MCP เพื่อค้นหา Hacker News รับเรื่องเด่น และอื่นๆ
- [exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) 🎖️ 📇 ☁️ – เซิร์ฟเวอร์ Model Context Protocol (MCP) ที่ช่วยให้ผู้ช่วย AI เช่น Claude ใช้ Exa AI Search API ในการค้นหาเว็บ การตั้งค่านี้ช่วยให้โมเดล AI รับข้อมูลเว็บแบบเรียลไทม์ได้อย่างปลอดภัยและควบคุมได้
- [fatwang2/search1api-mcp](https://github.com/fatwang2/search1api-mcp) 📇 ☁️ - ค้นหาผ่าน search1api (ต้องใช้คีย์ API แบบชำระเงิน)
- [hellokaton/unsplash-mcp-server](https://github.com/hellokaton/unsplash-mcp-server) 🐍 ☁️ - เซิร์ฟเวอร์ MCP สำหรับการค้นหารูปภาพจาก Unsplash
- [Ihor-Sokoliuk/MCP-SearXNG](https://github.com/ihor-sokoliuk/mcp-searxng) 📇 🏠/☁️ - เซิร์ฟเวอร์ Model Context Protocol สำหรับ [SearXNG](https://docs.searxng.org)
- [jae-jae/fetcher-mcp](https://github.com/jae-jae/fetcher-mcp) 📇 🏠 - เซิร์ฟเวอร์ MCP สำหรับดึงเนื้อหาเว็บเพจโดยใช้เบราว์เซอร์ headless Playwright รองรับการเรนเดอร์ Javascript และการดึงเนื้อหาอย่างชาญฉลาด และส่งออกในรูปแบบ Markdown หรือ HTML
- [jae-jae/g-search-mcp](https://github.com/jae-jae/g-search-mcp) 📇 🏠 - เซิร์ฟเวอร์ MCP อันทรงพลังสำหรับการค้นหา Google ที่ช่วยให้ค้นหาคำหลักหลายคำพร้อมกันแบบขนาน
- [Crawleo/Crawleo-MCP](https://github.com/Crawleo/Crawleo-MCP) ☁️ 🐍 – Crawleo Search & Crawl API
- [kshern/mcp-tavily](https://github.com/kshern/mcp-tavily.git) ☁️ 📇 – API การค้นหา AI ของ Tavily
- [brave/brave-search-mcp-server](https://github.com/brave/brave-search-mcp-server) 📇 ☁️ - ความสามารถในการค้นหาเว็บโดยใช้ API การค้นหาของ Brave
- [modelcontextprotocol/server-fetch](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/fetch) 🐍 🏠 ☁️ - การดึงและประมวลผลเนื้อหาเว็บอย่างมีประสิทธิภาพสำหรับการบริโภคของ AI
- [mzxrai/mcp-webresearch](https://github.com/mzxrai/mcp-webresearch) 🔍📚 - ค้นหา Google และทำการวิจัยเชิงลึกบนเว็บในหัวข้อใดก็ได้
- [nickclyde/duckduckgo-mcp-server](https://github.com/nickclyde/duckduckgo-mcp-server) 🐍 ☁️ - การค้นหาเว็บโดยใช้ DuckDuckGo
- [reading-plus-ai/mcp-server-deep-research](https://github.com/reading-plus-ai/mcp-server-deep-research) 📇 ☁️ - เซิร์ฟเวอร์ MCP ที่ให้การวิจัยเชิงลึกแบบอัตโนมัติคล้าย OpenAI/Perplexity การขยายคำถามที่มีโครงสร้าง และการรายงานที่กระชับ
- [SecretiveShell/MCP-searxng](https://github.com/SecretiveShell/MCP-searxng) 🐍 🏠 - เซิร์ฟเวอร์ MCP เพื่อเชื่อมต่อกับอินสแตนซ์ searXNG
- [tinyfish-io/agentql-mcp](https://github.com/tinyfish-io/agentql-mcp) 🎖️ 📇 ☁️ - เซิร์ฟเวอร์ MCP ที่ให้ความสามารถในการดึงข้อมูลของ [AgentQL](https://agentql.com)
- [Tomatio13/mcp-server-tavily](https://github.com/Tomatio13/mcp-server-tavily) ☁️ 🐍 – API การค้นหา AI ของ Tavily
- [vectorize-io/vectorize-mcp-server](https://github.com/vectorize-io/vectorize-mcp-server/) ☁️ 📇 - เซิร์ฟเวอร์ MCP ของ [Vectorize](https://vectorize.io) สำหรับการดึงข้อมูลขั้นสูง การวิจัยเชิงลึกส่วนตัว การดึงไฟล์ Anything-to-Markdown และการแบ่งส่วนข้อความ
- [zhsama/duckduckgo-mcp-server](https://github.com/zhsama/duckduckgo-mcp-server/) 📇 🏠 ☁️ - เซิร์ฟเวอร์ MCP ที่ใช้ TypeScript ซึ่งให้ฟังก์ชันการค้นหาของ DuckDuckGo
- [zoomeye-ai/mcp_zoomeye](https://github.com/zoomeye-ai/mcp_zoomeye) 📇 ☁️ - การสอบถามข้อมูลสินทรัพย์เครือข่ายโดยเซิร์ฟเวอร์ MCP ของ ZoomEye
- [yamanoku/baseline-mcp-server](https://github.com/yamanoku/baseline-mcp-server) 📇 🏠 - เซิร์ฟเวอร์ MCP ที่ค้นหาสถานะ Baseline โดยใช้ Web Platform API
- [Pearch-ai/mcp_pearch](https://github.com/Pearch-ai/mcp_pearch) 🎖️ 🐍 ☁️ - เครื่องมือค้นหาบุคลากรที่ดีที่สุด ช่วยลดเวลาการค้นหาผู้มีความสามารถ

### 🔒 <a name="security"></a>ความปลอดภัย

- [AIM-Intelligence/AIM-Guard-MCP](https://github.com/AIM-Intelligence/AIM-MCP) 📇 🏠 🍎 🪟 🐧 - เซิร์ฟเวอร์ MCP ที่มุ่งเน้นความปลอดภัย ให้แนวทางความปลอดภัยและการวิเคราะห์เนื้อหาสำหรับตัวแทน AI
- [13bm/GhidraMCP](https://github.com/13bm/GhidraMCP) 🐍 ☕ 🏠 - เซิร์ฟเวอร์ MCP สำหรับการรวม Ghidra กับผู้ช่วย AI ปลั๊กอินนี้ช่วยให้สามารถวิเคราะห์ไบนารีได้ โดยมีเครื่องมือสำหรับการตรวจสอบฟังก์ชัน การดีคอมไพล์ การสำรวจหน่วยความจำ และการวิเคราะห์การนำเข้า/ส่งออกผ่าน Model Context Protocol
- [atomicchonk/roadrecon_mcp_server](https://github.com/atomicchonk/roadrecon_mcp_server) 🐍 🪟 🏠 – เซิร์ฟเวอร์ MCP สำหรับวิเคราะห์ผลการรวบรวม ROADrecon จากการแจงนับผู้เช่า Azure
- [firstorderai/authenticator_mcp](https://github.com/firstorderai/authenticator_mcp) 📇 🏠 🍎 🪟 🐧 – เซิร์ฟเวอร์ MCP (Model Context Protocol) ที่ปลอดภัย ช่วยให้ตัวแทน AI สามารถโต้ตอบกับแอปยืนยันตัวตนได้
- [BurtTheCoder/mcp-dnstwist](https://github.com/BurtTheCoder/mcp-dnstwist) 📇 🪟 ☁️ - เซิร์ฟเวอร์ MCP สำหรับ dnstwist เครื่องมือ fuzzing DNS อันทรงพลังที่ช่วยตรวจจับการพิมพ์ผิด การฟิชชิ่ง และการจารกรรมองค์กร
- [BurtTheCoder/mcp-maigret](https://github.com/BurtTheCoder/mcp-maigret) 📇 🪟 ☁️ - เซิร์ฟเวอร์ MCP สำหรับ maigret เครื่องมือ OSINT อันทรงพลังที่รวบรวมข้อมูลบัญชีผู้ใช้จากแหล่งสาธารณะต่างๆ เซิร์ฟเวอร์นี้มีเครื่องมือสำหรับค้นหาชื่อผู้ใช้ในโซเชียลเน็ตเวิร์กและวิเคราะห์ URL
- [BurtTheCoder/mcp-shodan](https://github.com/BurtTheCoder/mcp-shodan) 📇 🪟 ☁️ - เซิร์ฟเวอร์ MCP สำหรับสอบถาม API ของ Shodan และ Shodan CVEDB เซิร์ฟเวอร์นี้มีเครื่องมือสำหรับการค้นหา IP การค้นหาอุปกรณ์ การค้นหา DNS การสอบถามช่องโหว่ การค้นหา CPE และอื่นๆ
- [BurtTheCoder/mcp-virustotal](https://github.com/BurtTheCoder/mcp-virustotal) 📇 🪟 ☁️ - เซิร์ฟเวอร์ MCP สำหรับสอบถาม API ของ VirusTotal เซิร์ฟเวอร์นี้มีเครื่องมือสำหรับสแกน URL วิเคราะห์แฮชไฟล์ และดึงรายงานที่อยู่ IP
- [fr0gger/MCP_Security](https://github.com/fr0gger/MCP_Security) 📇 ☁️ - เซิร์ฟเวอร์ MCP สำหรับสอบถาม API ของ ORKL เซิร์ฟเวอร์นี้มีเครื่องมือสำหรับดึงรายงานภัยคุกคาม วิเคราะห์ตัวแสดงภัยคุกคาม และดึงแหล่งข่าวกรอง
- [qianniuspace/mcp-security-audit](https://github.com/qianniuspace/mcp-security-audit) 📇 ☁️ เซิร์ฟเวอร์ MCP อันทรงพลังที่ตรวจสอบการพึ่งพาแพ็คเกจ npm เพื่อหาช่องโหว่ด้านความปลอดภัย สร้างด้วยการรวมรีจิสทรี npm ระยะไกลสำหรับการตรวจสอบความปลอดภัยแบบเรียลไทม์
i- [jtang613/GhidrAssistMCP](https://github.com/jtang613/GhidrAssistMCP) ☕ 🏠 - เซิร์ฟเวอร์ Model Context Protocol แบบเนทีฟสำหรับ Ghidra มาพร้อมกับการตั้งค่าผ่าน GUI และระบบบันทึก มีเครื่องมือทรงพลัง 31 รายการ และไม่ต้องใช้ไลบรารีภายนอก
- [semgrep/mcp-security-audit](https://github.com/semgrep/mcp-security-audit) 📇 ☁️ อนุญาตให้ตัวแทน AI สแกนโค้ดเพื่อหาช่องโหว่ด้านความปลอดภัยโดยใช้ [Semgrep](https://semgrep.dev)
- [mrexodia/ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp) 🐍 🏠 - เซิร์ฟเวอร์ MCP สำหรับ IDA Pro ช่วยให้คุณทำการวิเคราะห์ไบนารีด้วยผู้ช่วย AI ปลั๊กอินนี้ใช้การดีคอมไพล์ การแยกส่วน และช่วยให้คุณสร้างรายงานการวิเคราะห์มัลแวร์โดยอัตโนมัติ
- [intruder-io/intruder-mcp](https://github.com/intruder-io/intruder-mcp) 🐍 ☁️ - เซิร์ฟเวอร์ MCP สำหรับเข้าถึง [Intruder](https://www.intruder.io/) ช่วยให้คุณระบุ ทำความเข้าใจ และแก้ไขช่องโหว่ด้านความปลอดภัยในโครงสร้างพื้นฐานของคุณ
- [joergmichno/clawguard-mcp](https://github.com/joergmichno/clawguard-mcp) ([glama](https://glama.ai/mcp/servers/joergmichno/clawguard-mcp)) 🐍 🏠 - Security scanner for AI agents that detects prompt injections using 42+ regex patterns

### 🏃 <a name="sports"></a>กีฬา

เครื่องมือสำหรับการเข้าถึงข้อมูลที่เกี่ยวข้องกับกีฬา ผลการแข่งขัน และสถิติ

- [r-huijts/firstcycling-mcp](https://github.com/r-huijts/firstcycling-mcp) 📇 ☁️ - เข้าถึงข้อมูลการแข่งขันจักรยาน ผลการแข่งขัน และสถิติผ่านภาษาธรรมชาติ คุณสมบัติรวมถึงการดึงรายชื่อผู้เริ่มต้น ผลการแข่งขัน และข้อมูลนักปั่นจาก firstcycling.com
- [willvelida/mcp-afl-server](https://github.com/willvelida/mcp-afl-server) ☁️ - เซิร์ฟเวอร์ MCP ที่ผสานรวมกับ Squiggle API เพื่อให้ข้อมูลเกี่ยวกับทีมในลีกออสเตรเลียนฟุตบอล, ตารางอันดับ, ผลการแข่งขัน, การทำนายผล, และการจัดอันดับพลัง.

### 🎧 <a name="support-and-service-management"></a>การสนับสนุนและการจัดการบริการ

เครื่องมือสำหรับการจัดการการสนับสนุนลูกค้า การจัดการบริการไอที และการดำเนินการช่วยเหลือ

- [effytech/freshdesk-mcp](https://github.com/effytech/freshdesk_mcp) 🐍 ☁️ - เซิร์ฟเวอร์ MCP ที่รวมเข้ากับ Freshdesk ช่วยให้โมเดล AI สามารถโต้ตอบกับโมดูล Freshdesk และดำเนินการสนับสนุนต่างๆ

### 🌎 <a name="translation-services"></a>บริการแปลภาษา

เครื่องมือและบริการแปลภาษาเพื่อช่วยให้ผู้ช่วย AI สามารถแปลเนื้อหาระหว่างภาษาต่างๆ ได้

- [translated/lara-mcp](https://github.com/translated/lara-mcp) 📇 🏠 - เซิร์ฟเวอร์ MCP สำหรับ Lara Translate API ช่วยให้มีความสามารถในการแปลที่ทรงพลัง รองรับการตรวจจับภาษาและการแปลที่คำนึงถึงบริบท

### 🚆 <a name="travel-and-transportation"></a>การเดินทางและการขนส่ง

การเข้าถึงข้อมูลการเดินทางและการขนส่ง ช่วยให้สามารถสอบถามตารางเวลา เส้นทาง และข้อมูลการเดินทางแบบเรียลไทม์

- [Airbnb MCP Server](https://github.com/openbnb-org/mcp-server-airbnb) 📇 ☁️ - ให้เครื่องมือในการค้นหา Airbnb และรับรายละเอียดรายการ
- [KyrieTangSheng/mcp-server-nationalparks](https://github.com/KyrieTangSheng/mcp-server-nationalparks) 📇 ☁️ - การรวม API ของ National Park Service ที่ให้ข้อมูลล่าสุดเกี่ยวกับรายละเอียดของอุทยาน การแจ้งเตือน ศูนย์บริการนักท่องเที่ยว ที่ตั้งแคมป์ และเหตุการณ์สำหรับอุทยานแห่งชาติในสหรัฐอเมริกา
- [NS Travel Information MCP Server](https://github.com/r-huijts/ns-mcp-server) 📇 ☁️ - เข้าถึงข้อมูลการเดินทางของ Dutch Railways (NS) ตารางเวลา และการอัปเดตแบบเรียลไทม์
- [pab1it0/tripadvisor-mcp](https://github.com/pab1it0/tripadvisor-mcp) 📇 🐍 - เซิร์ฟเวอร์ MCP ที่ช่วยให้ LLM สามารถโต้ตอบกับ API ของ Tripadvisor รองรับข้อมูลสถานที่ รีวิว และรูปภาพผ่านอินเทอร์เฟซ MCP ที่ได้มาตรฐาน

### 🔄 <a name="version-control"></a>การควบคุมเวอร์ชัน

โต้ตอบกับที่เก็บ Git และแพลตฟอร์มควบคุมเวอร์ชัน ช่วยให้สามารถจัดการที่เก็บ วิเคราะห์โค้ด จัดการคำขอผสาน (pull request) ติดตามปัญหา และดำเนินการควบคุมเวอร์ชันอื่นๆ ผ่าน API ที่ได้มาตรฐาน

- [adhikasp/mcp-git-ingest](https://github.com/adhikasp/mcp-git-ingest) 🐍 🏠 - อ่านและวิเคราะห์ที่เก็บ GitHub ด้วย LLM ของคุณ
- [ddukbg/github-enterprise-mcp](https://github.com/ddukbg/github-enterprise-mcp) 📇 ☁️ 🏠 - เซิร์ฟเวอร์ MCP สำหรับการรวม API ของ GitHub Enterprise
- [kopfrechner/gitlab-mr-mcp](https://github.com/kopfrechner/gitlab-mr-mcp) 📇 ☁️ - โต้ตอบกับปัญหาและคำขอผสานของโปรเจกต์ GitLab ได้อย่างราบรื่น
- [modelcontextprotocol/server-git](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/git) 🐍 🏠 - การดำเนินการกับที่เก็บ Git โดยตรง รวมถึงการอ่าน ค้นหา และวิเคราะห์ที่เก็บในเครื่อง
- [modelcontextprotocol/server-github](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/github) 📇 ☁️ - การรวม API ของ GitHub สำหรับการจัดการที่เก็บ คำขอผสาน ปัญหา และอื่นๆ
- [modelcontextprotocol/server-gitlab](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/gitlab) 📇 ☁️ 🏠 - การรวมแพลตฟอร์ม GitLab สำหรับการจัดการโปรเจกต์และการดำเนินการ CI/CD
- [Tiberriver256/mcp-server-azure-devops](https://github.com/Tiberriver256/mcp-server-azure-devops) 📇 ☁️ - การรวม Azure DevOps สำหรับการจัดการที่เก็บ รายการงาน และไปป์ไลน์

### 🛠️ <a name="other-tools-and-integrations"></a>เครื่องมือและการรวมอื่นๆ

- [2niuhe/plantuml_web](https://github.com/2niuhe/plantuml_web) 🐍 🏠 ☁️ 🍎 🪟 🐧 - ส่วนหน้าเว็บ PlantUML ที่รวมกับเซิร์ฟเวอร์ MCP เพื่อให้สามารถสร้างภาพ PlantUML และตรวจสอบไวยากรณ์ได้
- [2niuhe/qrcode_mcp](https://github.com/2niuhe/qrcode_mcp) 🐍 🏠 🍎 🪟 🐧 - เซิร์ฟเวอร์ MCP สำหรับสร้าง QR code ที่สามารถแปลงข้อความใดก็ได้ (รวมถึงตัวอักษรจีน) เป็น QR code พร้อมสีที่ปรับแต่งได้และเอาต์พุต base64 encoding
- [AbdelStark/bitcoin-mcp](https://github.com/AbdelStark/bitcoin-mcp) - ₿ เซิร์ฟเวอร์ Model Context Protocol (MCP) ที่ช่วยให้โมเดล AI โต้ตอบกับ Bitcoin สามารถสร้างคีย์ ตรวจสอบที่อยู่ ถอดรหัสธุรกรรม สอบถามบล็อกเชน และอื่นๆ
- [akseyh/bear-mcp-server](https://github.com/akseyh/bear-mcp-server) - ช่วยให้ AI อ่านจาก Bear Notes ของคุณ (เฉพาะ macOS)
- [allenporter/mcp-server-home-assistant](https://github.com/allenporter/mcp-server-home-assistant) 🐍 🏠 - เปิดเผยเจตนาคำสั่งเสียงทั้งหมดของ Home Assistant ผ่านเซิร์ฟเวอร์ Model Context Protocol เพื่อควบคุมบ้าน
- [Amazon Bedrock Nova Canvas](https://github.com/zxkane/mcp-server-amazon-bedrock) 📇 ☁️ - ใช้โมเดล Amazon Nova Canvas เพื่อสร้างภาพ
- [amidabuddha/unichat-mcp-server](https://github.com/amidabuddha/unichat-mcp-server) 🐍/📇 ☁️ - ส่งคำขอไปยัง OpenAI, MistralAI, Anthropic, xAI, Google AI หรือ DeepSeek โดยใช้โปรโตคอล MCP ผ่านเครื่องมือหรือคำสั่งที่กำหนดไว้ล่วงหน้า ต้องใช้คีย์ API ของผู้ให้บริการ
- [anaisbetts/mcp-installer](https://github.com/anaisbetts/mcp-installer) 🐍 🏠 - เซิร์ฟเวอร์ MCP ที่ติดตั้งเซิร์ฟเวอร์ MCP อื่นๆ ให้คุณ
- [anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube) 📇 ☁️ - ดึงคำบรรยายของ YouTube
- [andybrandt/mcp-simple-openai-assistant](https://github.com/andybrandt/mcp-simple-openai-assistant) - 🐍 ☁️ MCP เพื่อพูดคุยกับผู้ช่วย OpenAI (Claude สามารถใช้โมเดล GPT ใดๆ เป็นผู้ช่วยได้)
- [andybrandt/mcp-simple-timeserver](https://github.com/andybrandt/mcp-simple-timeserver) 🐍 🏠☁️ - เซิร์ฟเวอร์ MCP ที่ช่วยให้ตรวจสอบเวลาท้องถิ่นบนเครื่องลูกข่ายหรือเวลา UTC ปัจจุบันจากเซิร์ฟเวอร์ NTP
- [anjor/coinmarket-mcp-server](https://github.com/anjor/coinmarket-mcp-server) 🐍 🏠 - การรวม API ของ Coinmarket เพื่อดึงรายการและราคาสกุลเงินดิจิทัล
- [apify/actors-mcp-server](https://github.com/apify/actors-mcp-server) 📇 ☁️ - ใช้เครื่องมือที่สร้างไว้ล่วงหน้ากว่า 3,000 รายการที่เรียกว่า Actors เพื่อดึงข้อมูลจากเว็บไซต์ อีคอมเมิร์ซ โซเชียลมีเดีย เครื่องมือค้นหา แผนที่ และอื่นๆ
- [apinetwork/piapi-mcp-server](https://github.com/apinetwork/piapi-mcp-server) 📇 ☁️ เซิร์ฟเวอร์ MCP ของ PiAPI ช่วยให้ผู้ใช้สามารถสร้างเนื้อหาสื่อด้วย Midjourney/Flux/Kling/Hunyuan/Udio/Trellis ได้โดยตรงจาก Claude หรือแอปที่เข้ากันได้กับ MCP
- [awkoy/replicate-flux-mcp](https://github.com/awkoy/replicate-flux-mcp) 📇 ☁️ - ให้ความสามารถในการสร้างภาพผ่าน API ของ Replicate
- [awwaiid/mcp-server-taskwarrior](https://github.com/awwaiid/mcp-server-taskwarrior) 🏠 📇 - เซิร์ฟเวอร์ MCP สำหรับการใช้งาน taskwarrior ในเครื่องพื้นฐาน (เพิ่ม อัปเดต ลบงาน)
- [Badhansen/notion-mcp](https://github.com/Badhansen/notion-mcp) 🐍 ☁️ - เซิร์ฟเวอร์ Model Context Protocol (MCP) ที่รวมเข้ากับ API ของ Notion เพื่อจัดการรายการสิ่งที่ต้องทำส่วนตัวอย่างมีประสิทธิภาพ
- [bart6114/my-bear-mcp-server](https://github.com/bart6114/my-bear-mcp-server/) 📇 🏠 🍎 - ช่วยให้อ่านโน้ตและแท็กสำหรับแอปจดโน้ต Bear ผ่านการรวมโดยตรงกับฐานข้อมูล sqlite ของ Bear
- [billster45/mcp-chatgpt-responses](https://github.com/billster45/mcp-chatgpt-responses) 🐍 ☁️ - เซิร์ฟเวอร์ MCP สำหรับ Claude เพื่อพูดคุยกับ ChatGPT และใช้ความสามารถในการค้นหาเว็บของมัน
- [blurrah/mcp-graphql](https://github.com/blurrah/mcp-graphql) 📇 ☁️ - ช่วยให้ AI สามารถสอบถามเซิร์ฟเวอร์ GraphQL
- [fotoetienne/gqai](https://github.com/fotoetienne/gqai) 🏎 🏠 - ใช้เครื่องมือการกำหนดแบบสอบถาม/การกลายพันธุ์ GraphQL ทั่วไป และ gqai จะสร้างเซิร์ฟเวอร์ MCP ให้กับคุณโดยอัตโนมัติ
- [calclavia/mcp-obsidian](https://github.com/calclavia/mcp-obsidian) 📇 🏠 - ตัวเชื่อมต่อนี้ช่วยให้ Claude Desktop (หรือไคลเอนต์ MCP ใดๆ) อ่านและค้นหาไดเรกทอรีที่มีโน้ต Markdown (เช่น vault ของ Obsidian)
- [chrishayuk/mcp-cli](https://github.com/chrishayuk/mcp-cli) 🐍 🏠 - เครื่องมือ CLI อีกตัวสำหรับทดสอบเซิร์ฟเวอร์ MCP
- [danhilse/notion_mcp](https://github.com/danhilse/notion_mcp) 🐍 ☁️ - รวมเข้ากับ API ของ Notion เพื่อจัดการรายการสิ่งที่ต้องทำส่วนตัว
- [evalstate/mcp-miro](https://github.com/evalstate/mcp-miro) 📇 ☁️ - เข้าถึงไวท์บอร์ด MIRO สร้างและอ่านรายการจำนวนมาก ต้องใช้คีย์ OAUTH สำหรับ REST API
- [future-audiences/wikimedia-enterprise-model-context-protocol](https://gitlab.wikimedia.org/repos/future-audiences/wikimedia-enterprise-model-context-protocol) 🐍 ☁️ - API ค้นหาบทความ Wikipedia
- [githejie/mcp-server-calculator](https://github.com/githejie/mcp-server-calculator) 🐍 🏠 - เซิร์ฟเวอร์นี้ช่วยให้ LLM ใช้เครื่องคิดเลขสำหรับการคำนวณตัวเลขที่แม่นยำ
- [gotoolkits/DifyWorkflow](https://github.com/gotoolkits/mcp-difyworkflow-server) - 🏎️ ☁️ เครื่องมือสำหรับสอบถามและดำเนินการเวิร์กโฟลว์ของ Dify
- [hiromitsusasaki/raindrop-io-mcp-server](https://github.com/hiromitsusasaki/raindrop-io-mcp-server) 📇 ☁️ - การรวมที่ช่วยให้ LLM โต้ตอบกับบุ๊กมาร์ก Raindrop.io โดยใช้ Model Context Protocol (MCP)
- [hmk/attio-mcp-server](https://github.com/hmk/attio-mcp-server) - 📇 ☁️ ช่วยให้ไคลเอนต์ AI จัดการบันทึกและโน้ตใน Attio CRM
- [isaacwasserman/mcp-vegalite-server](https://github.com/isaacwasserman/mcp-vegalite-server) 🐍 🏠 - สร้างการแสดงผลข้อมูลจากข้อมูลที่ดึงมาโดยใช้รูปแบบและตัวเรนเดอร์ VegaLite
- [ivo-toby/contentful-mcp](https://github.com/ivo-toby/contentful-mcp) 📇 🏠 - อัปเดต สร้าง ลบเนื้อหา โมเดลเนื้อหา และสินทรัพย์ใน Contentful Space ของคุณ
- [j3k0/speech.sh](https://github.com/j3k0/speech.sh/blob/main/MCP_README.md) 🏠 - ให้ตัวแทนพูดสิ่งต่างๆ ออกมาดังๆ แจ้งเตือนคุณเมื่อเขาทำงานเสร็จพร้อมสรุปสั้นๆ
- [joshuarileydev/mac-apps-launcher-mcp-server](https://github.com/JoshuaRileyDev/mac-apps-launcher) 📇 🏠 - เซิร์ฟเวอร์ MCP เพื่อแสดงรายการและเปิดแอปพลิเคชันบน MacOS
- [kelvin6365/plane-mcp-server](https://github.com/kelvin6365/plane-mcp-server) - 🏎️ 🏠 เซิร์ฟเวอร์ MCP นี้จะช่วยคุณจัดการโปรเจกต์และปัญหาผ่าน API ของ [Plane](https://plane.so)
- [kenliao94/mcp-server-rabbitmq](https://github.com/kenliao94/mcp-server-rabbitmq) 🐍 🏠 - เปิดใช้งานการโต้ตอบ (การดำเนินการจัดการ การส่ง/รับข้อความ) กับ RabbitMQ
- [kj455/mcp-kibela](https://github.com/kj455/mcp-kibela) - 📇 ☁️ ช่วยให้โมเดล AI โต้ตอบกับ [Kibela](https://kibe.la/)
- [KS-GEN-AI/confluence-mcp-server](https://github.com/KS-GEN-AI/confluence-mcp-server) 📇 ☁️ 🍎 🪟 - ดึงข้อมูล Confluence ผ่าน CQL และอ่านหน้า
- [KS-GEN-AI/jira-mcp-server](https://github.com/KS-GEN-AI/jira-mcp-server) 📇 ☁️ 🍎 🪟 - อ่านข้อมูล Jira ผ่าน JQL และ API และดำเนินการคำขอเพื่อสร้างและแก้ไขตั๋ว
- [lciesielski/mcp-salesforce](https://github.com/lciesielski/mcp-salesforce-example) 🏠 ☁️ - เซิร์ฟเวอร์ MCP พร้อมการสาธิตพื้นฐานของการโต้ตอบกับอินสแตนซ์ Salesforce
- [llmindset/mcp-hfspace](https://github.com/evalstate/mcp-hfspace) 📇 ☁️ - ใช้ HuggingFace Spaces โดยตรงจาก Claude ใช้การสร้างภาพแบบโอเพ่นซอร์ส การแชท งานด้านการมองเห็น และอื่นๆ รองรับการอัปโหลด/ดาวน์โหลดภาพ เสียง และข้อความ
- [magarcia/mcp-server-giphy](https://github.com/magarcia/mcp-server-giphy) 📇 ☁️ - ค้นหาและดึง GIF จากคลังขนาดใหญ่ของ Giphy ผ่าน API ของ Giphy
- [makehq/mcp-server](https://github.com/integromat/make-mcp-server) 🎖️ 📇 🏠 - เปลี่ยนสถานการณ์ [Make](https://www.make.com/) ของคุณให้เป็นเครื่องมือที่เรียกใช้ได้สำหรับผู้ช่วย AI
- [marcelmarais/Spotify](https://github.com/marcelmarais/spotify-mcp-server) - 📇 🏠 ควบคุมการเล่น Spotify และจัดการเพลย์ลิสต์
- [MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) 🐍 ☁️ 🏠 - โต้ตอบกับ Obsidian ผ่าน REST API
- [mcp-server-jfx](https://github.com/quarkiverse/quarkus-mcp-servers/tree/main/jfx) ☕ 🏠 - วาดบนผ้าใบ JavaFX
- [mediar-ai/screenpipe](https://github.com/mediar-ai/screenpipe) - 🎖️ 🦀 🏠 🍎 ระบบท้องถิ่นเป็นอันดับแรกที่จับภาพหน้าจอ/เสียงพร้อมการจัดทำดัชนีตามเวลา การจัดเก็บ SQL/embedding การค้นหาเชิงความหมาย การวิเคราะห์ประวัติที่ขับเคลื่อนด้วย LLM และการกระทำที่เกิดจากเหตุการณ์ - ช่วยให้สามารถสร้างตัวแทน AI ที่ตระหนักถึงบริบทผ่านระบบปลั๊กอิน NextJS
- [modelcontextprotocol/server-everything](https://github.com/modelcontextprotocol/servers/tree/main/src/everything) 📇 🏠 - เซิร์ฟเวอร์ MCP ที่ใช้คุณสมบัติทั้งหมดของโปรโตคอล MCP
- [mrjoshuak/godoc-mcp](https://github.com/mrjoshuak/godoc-mcp) 🏎️ 🏠 - เซิร์ฟเวอร์เอกสาร Go ที่มีประสิทธิภาพด้านโทเค็น ซึ่งให้ผู้ช่วย AI เข้าถึงเอกสารแพ็คเกจและประเภทอย่างชาญฉลาดโดยไม่ต้องอ่านไฟล์ต้นฉบับทั้งหมด
- [mzxrai/mcp-openai](https://github.com/mzxrai/mcp-openai) 📇 ☁️ - แชทกับโมเดลที่ฉลาดที่สุดของ OpenAI
- [NakaokaRei/swift-mcp-gui](https://github.com/NakaokaRei/swift-mcp-gui.git) 🏠 🍎 - เซิร์ฟเวอร์ MCP ที่สามารถดำเนินการคำสั่ง เช่น การป้อนข้อมูลจากคีย์บอร์ดและการเคลื่อนไหวของเมาส์
- [nguyenvanduocit/all-in-one-model-context-protocol](https://github.com/nguyenvanduocit/all-in-one-model-context-protocol) 🏎️ 🏠 - เครื่องมือที่มีประโยชน์สำหรับนักพัฒนา เกือบทุกอย่างที่วิศวกรต้องการ: Confluence, Jira, Youtube, รันสคริปต์, ฐานความรู้ RAG, ดึง URL, จัดการช่อง Youtube, อีเมล, ปฏิทิน, Gitlab
- [NON906/omniparser-autogui-mcp](https://github.com/NON906/omniparser-autogui-mcp) - 🐍 การดำเนินการอัตโนมัติของ GUI บนหน้าจอ
- [pierrebrunelle/mcp-server-openai](https://github.com/pierrebrunelle/mcp-server-openai) 🐍 ☁️ - สอบถามโมเดล OpenAI โดยตรงจาก Claude โดยใช้โปรโตคอล MCP
- [pskill9/hn-server](https://github.com/pskill9/hn-server) - 📇 ☁️ แยกวิเคราะห์เนื้อหา HTML จาก news.ycombinator.com (Hacker News) และให้ข้อมูลที่มีโครงสร้างสำหรับเรื่องราวประเภทต่างๆ (ยอดนิยม ใหม่ ถาม แสดง งาน)
- [PV-Bhat/vibe-check-mcp-server](https://github.com/PV-Bhat/vibe-check-mcp-server) 📇 ☁️ - เซิร์ฟเวอร์ MCP ที่ป้องกันข้อผิดพลาดแบบต่อเนื่องและการขยายขอบเขตโดยเรียกตัวแทน "Vibe-check" เพื่อให้แน่ใจว่าสอดคล้องกับผู้ใช้
- [pwh-pwh/cal-mcp](https://github.com/pwh-pwh/cal-mcp) - เซิร์ฟเวอร์ MCP สำหรับการคำนวณนิพจน์ทางคณิตศาสตร์
- [pyroprompts/any-chat-completions-mcp](https://github.com/pyroprompts/any-chat-completions-mcp) - แชทกับ API Chat Completions ที่เข้ากันได้กับ OpenAI SDK อื่นๆ เช่น Perplexity, Groq, xAI และอื่นๆ
- [reeeeemo/ancestry-mcp](https://github.com/reeeeemo/ancestry-mcp) 🐍 🏠 - ช่วยให้ AI อ่านไฟล์ .ged และข้อมูลพันธุกรรม
- [rember/rember-mcp](https://github.com/rember/rember-mcp) 📇 🏠 - สร้างบัตรคำทบทวนแบบเว้นระยะใน [Rember](https://rember.com) เพื่อจดจำสิ่งที่คุณเรียนรู้ในการแชทของคุณ
- [roychri/mcp-server-asana](https://github.com/roychri/mcp-server-asana) - 📇 ☁️ การใช้งานเซิร์ฟเวอร์ Model Context Protocol ของ Asana นี้ช่วยให้คุณพูดคุยกับ API ของ Asana จากไคลเอนต์ MCP เช่นแอปพลิเคชันเดสก์ท็อปของ Anthropic Claude และอื่นๆ อีกมากมาย
- [rusiaaman/wcgw](https://github.com/rusiaaman/wcgw/blob/main/src/wcgw/client/mcp_server/Readme.md) 🐍 🏠 - การดำเนินการเชลล์อัตโนมัติ การควบคุมคอมพิวเตอร์ และตัวแทนเขียนโค้ด (Mac)
- [SecretiveShell/MCP-wolfram-alpha](https://github.com/SecretiveShell/MCP-wolfram-alpha) 🐍 ☁️ - เซิร์ฟเวอร์ MCP สำหรับสอบถาม API ของ Wolfram Alpha
- [Seym0n/tiktok-mcp](https://github.com/Seym0n/tiktok-mcp) 📇 ☁️ - โต้ตอบกับวิดีโอ TikTok
- [sirmews/apple-notes-mcp](https://github.com/sirmews/apple-notes-mcp) 🐍 🏠 - ช่วยให้ AI อ่านจากฐานข้อมูล Apple Notes ในเครื่องของคุณ (เฉพาะ macOS)
- [henilcalagiya/mcp-apple-notes](https://github.com/henilcalagiya/mcp-apple-notes) 🐍 🏠 - เครื่องมือที่ทรงพลังสำหรับการทำงานอัตโนมัติของ Apple Notes โดยใช้ Model Context Protocol (MCP) รองรับการทำงาน CRUD เต็มรูปแบบพร้อมเนื้อหา HTML การจัดการโฟลเดอร์ และความสามารถในการค้นหา
- [sooperset/mcp-atlassian](https://github.com/sooperset/mcp-atlassian) 🐍 ☁️ - เซิร์ฟเวอร์ MCP สำหรับผลิตภัณฑ์ Atlassian (Confluence และ Jira) รองรับ Confluence Cloud, Jira Cloud และ Jira Server/Data Center ให้เครื่องมือที่ครอบคลุมสำหรับการค้นหา อ่าน สร้าง และจัดการเนื้อหาทั่วทั้งพื้นที่ทำงาน Atlassian
- [suekou/mcp-notion-server](https://github.com/suekou/mcp-notion-server) 📇 🏠 - โต้ตอบกับ API ของ Notion
- [tacticlaunch/mcp-linear](https://github.com/tacticlaunch/mcp-linear) 📇 ☁️ 🍎 🪟 🐧 - รวมเข้ากับระบบการจัดการโปรเจกต์ Linear
- [tanigami/mcp-server-perplexity](https://github.com/tanigami/mcp-server-perplexity) 🐍 ☁️ - โต้ตอบกับ API ของ Perplexity
- [tevonsb/homeassistant-mcp](https://github.com/tevonsb/homeassistant-mcp) 📇 🏠 - เข้าถึงข้อมูล Home Assistant และควบคุมอุปกรณ์ (ไฟ สวิตช์ เทอร์โมสตัท ฯลฯ)
- [tomekkorbak/oura-mcp-server](https://github.com/tomekkorbak/oura-mcp-server) 🐍 ☁️ - เซิร์ฟเวอร์ MCP สำหรับ Oura แอปสำหรับติดตามการนอนหลับ
- [tomekkorbak/strava-mcp-server](https://github.com/tomekkorbak/strava-mcp-server) 🐍 ☁️ - เซิร์ฟเวอร์ MCP สำหรับ Strava แอปสำหรับติดตามการออกกำลังกาย
- [wanaku-ai/wanaku](https://github.com/wanaku-ai/wanaku) - ☁️ 🏠 Wanaku MCP Router เป็นเซิร์ฟเวอร์ MCP ที่ใช้ SSE ซึ่งให้เครื่องมือกำหนดเส้นทางที่ขยายได้ ช่วยให้รวมระบบองค์กรของคุณเข้ากับตัวแทน AI
- [wong2/mcp-cli](https://github.com/wong2/mcp-cli) 📇 🏠 - เครื่องมือ CLI สำหรับทดสอบเซิร์ฟเวอร์ MCP
- [ws-mcp](https://github.com/nick1udwig/ws-mcp) - ห่อหุ้มเซิร์ฟเวอร์ MCP ด้วย WebSocket (สำหรับใช้กับ [kitbitz](https://github.com/nick1udwig/kibitz))
- [yuna0x0/hackmd-mcp](https://github.com/yuna0x0/hackmd-mcp) 📇 ☁️ - ช่วยให้โมเดล AI โต้ตอบกับ [HackMD](https://hackmd.io)
- [ZeparHyfar/mcp-datetime](https://github.com/ZeparHyfar/mcp-datetime) - เซิร์ฟเวอร์ MCP ที่ให้ฟังก์ชันวันที่และเวลาในรูปแบบต่างๆ
- [zueai/mcp-manager](https://github.com/zueai/mcp-manager) 📇 ☁️ - อินเทอร์เฟซเว็บ UI ง่ายๆ เพื่อติดตั้งและจัดการเซิร์ฟเวอร์ MCP สำหรับแอป Claude Desktop
- [HenryHaoson/Yuque-MCP-Server](https://github.com/HenryHaoson/Yuque-MCP-Server) - 📇 ☁️ เซิร์ฟเวอร์ Model-Context-Protocol (MCP) สำหรับการรวมเข้ากับ API ของ Yuque ช่วยให้โมเดล AI จัดการเอกสาร โต้ตอบกับฐานความรู้ ค้นหาเนื้อหา และเข้าถึงข้อมูลการวิเคราะห์จากแพลตฟอร์ม Yuque
- [tumf/web3-mcp](https://github.com/tumf/web3-mcp) 🐍 ☁️ - การใช้งาน MCP เซิร์ฟเวอร์ที่ห่อหุ้ม Ankr Advanced API สามารถเข้าถึงข้อมูล NFT, โทเค็น และบล็อกเชนในหลายเครือข่ายรวมถึง Ethereum, BSC, Polygon, Avalanche และอื่นๆ
- [growilabs/growi-mcp-server](https://github.com/growilabs/growi-mcp-server) 🎖️ 📇 ☁️ - เซิร์ฟเวอร์ MCP อย่างเป็นทางการสำหรับการผสานรวมกับ GROWI API
- [JamesANZ/medical-mcp](https://github.com/JamesANZ/medical-mcp) 📇 🏠 - เซิร์ฟเวอร์ MCP ที่ให้การเข้าถึงข้อมูลทางการแพทย์ ฐานข้อมูลยา และทรัพยากรด้านสุขภาพ ช่วยให้ผู้ช่วย AI สามารถสืบค้นข้อมูลทางการแพทย์ การโต้ตอบของยา และแนวทางทางคลินิก

## กรอบการทำงาน (Frameworks)

- [FastMCP (Python)](https://github.com/jlowin/fastmcp) 🐍 - กรอบการทำงานระดับสูงสำหรับการสร้างเซิร์ฟเวอร์ MCP ใน Python
- [FastMCP (TypeScript)](https://github.com/punkpeye/fastmcp) 📇 - กรอบการทำงานระดับสูงสำหรับการสร้างเซิร์ฟเวอร์ MCP ใน TypeScript
- [Foxy Contexts](https://github.com/strowk/foxy-contexts) 🏎️ - ไลบรารี Golang เพื่อเขียนเซิร์ฟเวอร์ MCP แบบกำหนดเองพร้อมการทดสอบฟังก์ชันรวมอยู่ด้วย
- [gabfr/waha-api-mcp-server](https://github.com/gabfr/waha-api-mcp-server) 📇 - เซิร์ฟเวอร์ MCP พร้อมสเปค openAPI สำหรับการใช้ API WhatsApp ที่ไม่เป็นทางการ (https://waha.devlike.pro/ - และยังเป็นโอเพ่นซอร์ส: https://github.com/devlikeapro/waha)
- [Genkit MCP](https://github.com/firebase/genkit/tree/main/js/plugins/mcp) 📇 – ให้การรวมระหว่าง [Genkit](https://github.com/firebase/genkit/tree/main) และ Model Context Protocol (MCP)
- [http4k MCP SDK](https://mcp.http4k.org) 🐍 - SDK Kotlin ที่ใช้งานได้ดีและทดสอบได้ โดยอิงจากชุดเครื่องมือเว็บ [http4k](https://http4k.org) ยอดนิยม รองรับโปรโตคอลสตรีมมิ่ง HTTP ใหม่
- [lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent) 🤖 🔌 - สร้างตัวแทนที่มีประสิทธิภาพด้วยเซิร์ฟเวอร์ MCP โดยใช้รูปแบบที่เรียบง่ายและประกอบได้
- [LiteMCP](https://github.com/wong2/litemcp) 📇 - กรอบการทำงานระดับสูงสำหรับการสร้างเซิร์ฟเวอร์ MCP ใน JavaScript/TypeScript
- [marimo-team/codemirror-mcp](https://github.com/marimo-team/codemirror-mcp) - ส่วนขยาย CodeMirror ที่ใช้ Model Context Protocol (MCP) สำหรับการกล่าวถึงทรัพยากรและคำสั่งพรอมต์
- [mark3labs/mcp-go](https://github.com/mark3labs/mcp-go) 🏎️ - SDK Golang สำหรับการสร้างเซิร์ฟเวอร์และไคลเอนต์ MCP
- [mcp-framework](https://github.com/QuantGeekDev/mcp-framework) 📇 - กรอบการทำงาน TypeScript ที่รวดเร็วและสง่างามสำหรับการสร้างเซิร์ฟเวอร์ MCP
- [mcp-proxy](https://github.com/punkpeye/mcp-proxy) - 📇 พร็อกซี่ SSE TypeScript สำหรับเซิร์ฟเวอร์ MCP ที่ใช้การขนส่ง `stdio`
- [mcp-rs-template](https://github.com/linux-china/mcp-rs-template) 🦀 - เทมเพลตเซิร์ฟเวอร์ MCP CLI สำหรับ Rust
- [metoro-io/mcp-golang](https://github.com/metoro-io/mcp-golang) 🏎️ - กรอบการทำงาน Golang สำหรับการสร้างเซิร์ฟเวอร์ MCP โดยเน้นที่ความปลอดภัยของประเภท
- [mullerhai/sakura-mcp](https://github.com/mullerhai/sakura-mcp) 🦀 ☕ - กรอบการทำงาน Scala MCP สำหรับสร้างตัวแทนที่มีประสิทธิภาพด้วยเซิร์ฟเวอร์และไคลเอนต์ MCP ที่แรเงาจาก modelcontextprotocol.io
- [paulotaylor/voyp-mcp](https://github.com/paulotaylor/voyp-mcp) 📇 - VOYP - เซิร์ฟเวอร์ MCP Voice Over Your Phone สำหรับการโทร
- [poem-web/poem-mcpserver](https://github.com/poem-web/poem/tree/master/poem-mcpserver) 🦀 - การใช้งานเซิร์ฟเวอร์ MCP สำหรับ Poem
- [quarkiverse/quarkus-mcp-server](https://github.com/quarkiverse/quarkus-mcp-server) ☕ - SDK Java สำหรับการสร้างเซิร์ฟเวอร์ MCP โดยใช้ Quarkus
- [rectalogic/langchain-mcp](https://github.com/rectalogic/langchain-mcp) 🐍 - ให้การสนับสนุนการเรียกเครื่องมือ MCP ใน LangChain ช่วยให้สามารถรวมเครื่องมือ MCP เข้ากับเวิร์กโฟลว์ LangChain
- [ribeirogab/simple-mcp](https://github.com/ribeirogab/simple-mcp) 📇 - ไลบรารี TypeScript ง่ายๆ สำหรับการสร้างเซิร์ฟเวอร์ MCP
- [salty-flower/ModelContextProtocol.NET](https://github.com/salty-flower/ModelContextProtocol.NET) #️⃣ 🏠 - SDK C# สำหรับการสร้างเซิร์ฟเวอร์ MCP บน .NET 9 ที่เข้ากันได้กับ NativeAOT ⚡ 🔌
- [spring-ai-mcp](https://github.com/spring-projects-experimental/spring-ai-mcp) ☕ 🌱 - SDK Java และการรวม Spring Framework สำหรับการสร้างไคลเอนต์และเซิร์ฟเวอร์ MCP ด้วยตัวเลือกการขนส่งที่หลากหลายและเสียบได้
- [spring-projects-experimental/spring-ai-mcp](https://github.com/spring-projects-experimental/spring-ai-mcp) ☕ 🌱 - SDK Java และการรวม Spring Framework สำหรับการสร้างไคลเอนต์และเซิร์ฟเวอร์ MCP ด้วยตัวเลือกการขนส่งที่หลากหลายและเสียบได้
- [Template MCP Server](https://github.com/mcpdotdirect/template-mcp-server) 📇 - เครื่องมือ CLI เพื่อสร้างโปรเจกต์เซิร์ฟเวอร์ Model Context Protocol ใหม่ด้วยการสนับสนุน TypeScript ตัวเลือกการขนส่งคู่ และโครงสร้างที่ขยายได้
- [sendaifun/solana-mcp-kit](https://github.com/sendaifun/solana-agent-kit/tree/main/examples/agent-kit-mcp-server) - SDK MCP Solana

## ยูทิลิตี้ (Utilities)

- [boilingdata/mcp-server-and-gw](https://github.com/boilingdata/mcp-server-and-gw) 📇 - เกตเวย์การขนส่ง MCP stdio ไปยัง HTTP SSE พร้อมเซิร์ฟเวอร์ตัวอย่างและไคลเอนต์ MCP
- [f/MCPTools](https://github.com/f/mcptools) 🔨 - เครื่องมือพัฒนาแบบ command-line สำหรับการตรวจสอบและโต้ตอบกับเซิร์ฟเวอร์ MCP พร้อมฟีเจอร์พิเศษ เช่น การจำลองและพร็อกซี่
- [flux159/mcp-chat](https://github.com/flux159/mcp-chat) 📇🖥️ - ไคลเอนต์แบบ CLI เพื่อแชทและเชื่อมต่อกับเซิร์ฟเวอร์ MCP ใดๆ มีประโยชน์ในระหว่างการพัฒนาและทดสอบเซิร์ฟเวอร์ MCP
- [isaacwasserman/mcp-langchain-ts-client](https://github.com/isaacwasserman/mcp-langchain-ts-client) 📇 – ใช้เครื่องมือที่จัดหาโดย MCP ใน LangChain.js
- [kukapay/whattimeisit-mcp](https://github.com/kukapay/whattimeisit-mcp) 🐍 ☁️ - เซิร์ฟเวอร์ MCP น้ำหนักเบาที่บอกเวลาที่แน่นอนให้คุณทราบ
- [kukapay/whereami-mcp](https://github.com/kukapay/whereami-mcp) 🐍 ☁️ - เซิร์ฟเวอร์ MCP น้ำหนักเบาที่บอกตำแหน่งที่แน่นอนของคุณตาม IP ปัจจุบัน
- [kukapay/whoami-mcp](https://github.com/kukapay/whoami-mcp) 🐍 🏠 - เซิร์ฟเวอร์ MCP น้ำหนักเบาที่บอกว่าคุณเป็นใครอย่างแน่นอน
- [lightconetech/mcp-gateway](https://github.com/lightconetech/mcp-gateway) 📇 - การสาธิตเกตเวย์สำหรับเซิร์ฟเวอร์ MCP SSE
- [mark3labs/mcphost](https://github.com/mark3labs/mcphost) 🏎️ - แอปพลิเคชันโฮสต์ CLI ที่ช่วยให้ Large Language Models (LLMs) โต้ตอบกับเครื่องมือภายนอกผ่าน Model Context Protocol (MCP)
- [MCP-Connect](https://github.com/EvalsOne/MCP-Connect) 📇 - เครื่องมือขนาดเล็กที่ช่วยให้บริการ AI บนคลาวด์เข้าถึงเซิร์ฟเวอร์ MCP ที่ใช้ Stdio ในเครื่องผ่านคำขอ HTTP/HTTPS
- [SecretiveShell/MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge) 🐍 – พร็อกซี่ middleware OpenAI เพื่อใช้ MCP ในไคลเอนต์ที่เข้ากันได้กับ OpenAI ใดๆ
- [sparfenyuk/mcp-proxy](https://github.com/sparfenyuk/mcp-proxy) 🐍 – เกตเวย์การขนส่ง MCP stdio ไปยัง SSE
- [TBXark/mcp-proxy](https://github.com/TBXark/mcp-proxy) 🏎️ - เซิร์ฟเวอร์พร็อกซี่ MCP ที่รวบรวมและให้บริการเซิร์ฟเวอร์ทรัพยากร MCP หลายตัวผ่านเซิร์ฟเวอร์ http เดียว
- [upsonic/gpt-computer-assistant](https://github.com/Upsonic/gpt-computer-assistant) 🐍 – กรอบการทำงานเพื่อสร้างตัวแทน AI แนวตั้ง

## เคล็ดลับและเทคนิค (Tips and Tricks)

### พรอมต์อย่างเป็นทางการเพื่อแจ้ง LLM เกี่ยวกับวิธีใช้ MCP

ต้องการถาม Claude เกี่ยวกับ Model Context Protocol หรือไม่?

สร้างโปรเจกต์ จากนั้นเพิ่มไฟล์นี้เข้าไป:

https://modelcontextprotocol.io/llms-full.txt

ตอนนี้ Claude สามารถตอบคำถามเกี่ยวกับการเขียนเซิร์ฟเวอร์ MCP และวิธีการทำงานของมันได้

- https://www.reddit.com/r/ClaudeAI/comments/1h3g01r/want_to_ask_claude_about_model_context_protocol/

## Star History

<a href="https://star-history.com/#punkpeye/awesome-mcp-servers&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date" />
 </picture>
</a>
