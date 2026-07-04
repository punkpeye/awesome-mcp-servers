# خوادم MCP الرائعة [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![Arabic](https://img.shields.io/badge/Arabic-Click-brightgreen)](README-ar.md)
[![ไทย](https://img.shields.io/badge/Thai-Click-blue)](README-th.md)
[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![繁體中文](https://img.shields.io/badge/繁體中文-點擊查看-orange)](README-zh_TW.md)
[![简体中文](https://img.shields.io/badge/简体中文-点击查看-orange)](README-zh.md)
[![日本語](https://img.shields.io/badge/日本語-クリック-青)](README-ja.md)
[![한국어](https://img.shields.io/badge/한국어-클릭-yellow)](README-ko.md)
[![Português Brasileiro](https://img.shields.io/badge/Português_Brasileiro-Clique-green)](README-pt_BR.md)
[![Discord](https://img.shields.io/discord/1312302100125843476?logo=discord&label=discord)](https://glama.ai/mcp/discord)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/mcp?style=flat&logo=reddit&label=subreddit)](https://www.reddit.com/r/mcp/)

> [!IMPORTANT]
> دليل الويب لـ [خوادم MCP الرائعة](https://glama.ai/mcp/servers).

قائمة منتقاة لأفضل خوادم بروتوكول سياق النموذج (Model Context Protocol – MCP).

* [ما هو MCP؟](#what-is-mcp)
* [العملاء (Clients)](#clients)
* [الدروس التعليمية](#tutorials)
* [المجتمع](#community)
* [مفتاح الرموز](#legend)
* [تطبيقات الخوادم](#server-implementations)
* [أطر العمل (Frameworks)](#frameworks)
* [نصائح وحيل](#tips-and-tricks)

## <a name="what-is-mcp"></a>ما هو MCP؟

[MCP](https://modelcontextprotocol.io/) بروتوكول مفتوح يُمكّن نماذج الذكاء الاصطناعي من التفاعل الآمن مع الموارد المحلية والبعيدة عبر تطبيقات خوادم موحّدة. تركّز هذه القائمة على خوادم MCP الجاهزة للإنتاج والتجريبية التي توسّع قدرات الذكاء الاصطناعي عبر الوصول إلى الملفات، والاتصال بقواعد البيانات، وتكامل واجهات البرمجة (APIs)، وغيرها من خدمات السياق.

## <a name="clients"></a>العملاء (Clients)

اطّلع على [awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients/) و [glama.ai/mcp/clients](https://glama.ai/mcp/clients).

## <a name="tutorials"></a>الدروس التعليمية

* [مقياس جودة تعريف الأدوات (TDQS)](https://github.com/glama-ai/tool-definition-quality-score)
* [بداية سريعة مع بروتوكول سياق النموذج (MCP)](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
* [إعداد تطبيق Claude Desktop لاستخدام قاعدة بيانات SQLite](https://youtu.be/wxCCzo9dGj0)

## <a name="community"></a>المجتمع

* [مجتمع r/mcp على Reddit](https://www.reddit.com/r/mcp)
* [خادم Discord](https://glama.ai/mcp/discord)

## <a name="legend"></a>مفتاح الرموز

* 🎖️ – تطبيق رسمي
* لغة البرمجة
  * 🐍 – شيفرة بلغة Python
  * 📇 – شيفرة بلغة TypeScript (أو JavaScript)
  * 🏎️ – شيفرة بلغة Go
  * 🦀 – شيفرة بلغة Rust
  * #️⃣ – شيفرة بلغة C#
  * ☕ – شيفرة بلغة Java
  * 🌊 – شيفرة بلغة C/C++
  * 💎 – شيفرة بلغة Ruby

* النطاق
  * ☁️ – خدمة سحابية
  * 🏠 – خدمة محلية
  * 📟 – أنظمة مدمجة
* نظام التشغيل
  * 🍎 – لنظام macOS
  * 🪟 – لنظام Windows
  * 🐧 – لنظام Linux

> [!NOTE]
> محتار بين المحلي 🏠 والسحابي ☁️؟
> * استخدم **المحلي** عندما يتخاطب خادم MCP مع برنامج مثبَّت محلياً، مثل التحكم في متصفح Chrome.
> * استخدم **السحابي** عندما يتخاطب خادم MCP مع واجهات برمجة بعيدة، مثل واجهة بيانات الطقس.

## <a name="server-implementations"></a>تطبيقات الخوادم

> [!NOTE]
> لدينا الآن [دليل ويب](https://glama.ai/mcp/servers) متزامن مع هذا المستودع.

> 📋 **ملاحظة:** لتفادي التكرار وصعوبة الصيانة، تُترجم هذه الصفحة **التصنيفات وأوصافها** فقط. أما **القائمة الكاملة للخوادم (أكثر من 1400 خادم)** فتجدها في [النسخة الإنجليزية](README.md) وفي [دليل الويب](https://glama.ai/mcp/servers).

* 🔗 - [المُجمِّعات](#aggregators)
* 🎨 - [الفن والثقافة](#art-and-culture)
* 📐 - [العمارة والتصميم](#architecture-and-design)
* 📂 - [أتمتة المتصفح](#browser-automation)
* 🧬 - [الأحياء والطب والمعلوماتية الحيوية](#bio)
* ☁️ - [المنصّات السحابية](#cloud-platforms)
* 👨‍💻 - [تنفيذ الشيفرة](#code-execution)
* 🤖 - [وكلاء البرمجة](#coding-agents)
* 🖥️ - [سطر الأوامر](#command-line)
* 💬 - [التواصل](#communication)
* 🗣️ - [الذكاء الاصطناعي الحواري](#conversational-ai)
* 🔑 - [التشفير](#cryptography)
* 👤 - [منصّات بيانات العملاء](#customer-data-platforms)
* 🗄️ - [قواعد البيانات](#databases)
* 📊 - [منصّات البيانات](#data-platforms)
* 🚚 - [التوصيل](#delivery)
* 🛠️ - [أدوات المطوّرين](#developer-tools)
* 🧮 - [أدوات علم البيانات](#data-science-tools)
* 📊 - [تمثيل البيانات المرئي](#data-visualization)
* 📟 - [الأنظمة المدمجة](#embedded-system)
* 🎓 - [التعليم](#education)
* 🛒 - [التجارة الإلكترونية](#e-commerce)
* 🌳 - [البيئة والطبيعة](#environment-and-nature)
* 📂 - [أنظمة الملفات](#file-systems)
* 💰 - [المال والتقنية المالية](#finance--fintech)
* 🎮 - [الألعاب](#gaming)
* 🏠 - [أتمتة المنزل](#home-automation)
* 🧠 - [المعرفة والذاكرة](#knowledge--memory)
* ⚖️ - [القانون](#legal)
* 🗺️ - [خدمات الموقع](#location-services)
* 🎯 - [التسويق](#marketing)
* 📊 - [المراقبة](#monitoring)
* 🎥 - [معالجة الوسائط المتعددة](#multimedia-process)
* 🖥️ - [أتمتة نظام التشغيل](#os-automation)
* 📋 - [إدارة المنتجات](#product-management)
* 🏠 - [العقارات](#real-estate)
* 🔬 - [البحث العلمي](#research)
* 🔎 - [البحث واستخراج البيانات](#search)
* 🔒 - [الأمن](#security)
* 🌐 - [وسائل التواصل الاجتماعي](#social-media)
* 🔮 - [الروحانيات والعلوم الباطنية](#spirituality-and-esoterica)
* 🏃 - [الرياضة](#sports)
* 🎧 - [الدعم وإدارة الخدمات](#support-and-service-management)
* 🌎 - [خدمات الترجمة](#translation-services)
* 🎧 - [تحويل النص إلى كلام](#text-to-speech)
* 🎙️ - [تحويل الكلام إلى نص](#speech-to-text)
* 🚆 - [السفر والنقل](#travel-and-transportation)
* 🔄 - [إدارة الإصدارات](#version-control)
* 🏢 - [بيئة العمل والإنتاجية](#workplace-and-productivity)
* 🛠️ - [أدوات وتكاملات أخرى](#other-tools-and-integrations)

### 🔗 <a name="aggregators"></a>المُجمِّعات

خوادم للوصول إلى العديد من التطبيقات والأدوات عبر خادم MCP واحد.

### 🚀 <a name="aerospace-and-astrodynamics"></a>الفضاء الجوي وديناميكا الأجرام

### 🎨 <a name="art-and-culture"></a>الفن والثقافة

الوصول إلى مجموعات الفنون والتراث الثقافي وقواعد بيانات المتاحف واستكشافها. تُمكّن نماذج الذكاء الاصطناعي من البحث في المحتوى الفني والثقافي وتحليله.

### 📐 <a name="architecture-and-design"></a>العمارة والتصميم

تصميم بنية البرمجيات ومخططات الأنظمة والتوثيق التقني وتصوّرها بصرياً. تُمكّن نماذج الذكاء الاصطناعي من توليد مخططات ووثائق معمارية احترافية.

### <a name="bio"></a>الأحياء والطب والمعلوماتية الحيوية

### 📂 <a name="browser-automation"></a>أتمتة المتصفح

الوصول إلى محتوى الويب وأتمتته. تُمكّن من البحث والاستخلاص (Scraping) ومعالجة محتوى الويب بصيغ ملائمة للذكاء الاصطناعي.

### ☁️ <a name="cloud-platforms"></a>المنصّات السحابية

تكامل مع خدمات المنصّات السحابية. تُمكّن من إدارة البنية التحتية والخدمات السحابية والتفاعل معها.

### 👨‍💻 <a name="code-execution"></a>تنفيذ الشيفرة

خوادم لتنفيذ الشيفرة. تتيح للنماذج اللغوية تنفيذ الشيفرة في بيئة آمنة، مثل وكلاء البرمجة.

### 🤖 <a name="coding-agents"></a>وكلاء البرمجة

وكلاء برمجة متكاملون يتيحون للنماذج اللغوية قراءة الشيفرة وتعديلها وتنفيذها وحلّ مهام البرمجة العامة بشكل مستقل تماماً.

### 🖥️ <a name="command-line"></a>سطر الأوامر

تنفيذ الأوامر والتقاط مخرجاتها والتفاعل مع الأصداف (Shells) وأدوات سطر الأوامر.

### 💬 <a name="communication"></a>التواصل

تكامل مع منصّات التواصل لإدارة الرسائل وعمليات القنوات. تُمكّن نماذج الذكاء الاصطناعي من التفاعل مع أدوات تواصل الفرق.

### 🗣️ <a name="conversational-ai"></a>الذكاء الاصطناعي الحواري

أدوات لبناء وتشغيل وكلاء محادثة يجرون حوارات منظّمة مع المستخدمين.

### 🔑 <a name="cryptography"></a>التشفير

أدوات لتشفير البيانات وفكّ تشفيرها.

### 👤 <a name="customer-data-platforms"></a>منصّات بيانات العملاء

توفّر الوصول إلى ملفات تعريف العملاء داخل منصّات بيانات العملاء.

### 🗄️ <a name="databases"></a>قواعد البيانات

وصول آمن إلى قواعد البيانات مع إمكانات فحص المخطط (Schema). تُمكّن من الاستعلام عن البيانات وتحليلها مع ضوابط أمان قابلة للتهيئة تشمل الوصول للقراءة فقط.

### 📊 <a name="data-platforms"></a>منصّات البيانات

منصّات بيانات لتكامل البيانات وتحويلها وتنظيم مسارات المعالجة (Pipelines).

### 🛠️ <a name="developer-tools"></a>أدوات المطوّرين

أدوات وتكاملات تُحسّن سير عمل التطوير وإدارة البيئة.

### 🔒 <a name="delivery"></a>التوصيل

### 🧮 <a name="data-science-tools"></a>أدوات علم البيانات

تكاملات وأدوات مصمّمة لتبسيط استكشاف البيانات وتحليلها وتحسين سير عمل علم البيانات.

### 📊 <a name="data-visualization"></a>تمثيل البيانات المرئي

مخططات ولوحات تفاعلية وأدوات بيانات مرئية تُعرض داخل محادثات الذكاء الاصطناعي.

### 📟 <a name="embedded-system"></a>الأنظمة المدمجة

توفّر الوصول إلى التوثيق والاختصارات للعمل على الأجهزة المدمجة.

### 🎓 <a name="education"></a>التعليم

خوادم MCP لأنظمة إدارة التعلّم (LMS) والأدوات التعليمية.

### 🛒 <a name="e-commerce"></a>التجارة الإلكترونية

خوادم MCP لمنصّات التجارة الإلكترونية وإدارة المتاجر الإلكترونية.

### 🌳 <a name="environment-and-nature"></a>البيئة والطبيعة

توفّر الوصول إلى البيانات البيئية والأدوات والخدمات والمعلومات المتعلقة بالطبيعة.

### 📂 <a name="file-systems"></a>أنظمة الملفات

توفّر وصولاً مباشراً إلى أنظمة الملفات المحلية مع أذونات قابلة للتهيئة. تُمكّن نماذج الذكاء الاصطناعي من قراءة الملفات وكتابتها وإدارتها ضمن مجلدات محدّدة.

### 💰 <a name="finance--fintech"></a>المال والتقنية المالية

أدوات للبيانات المالية والأسواق والمدفوعات والتقنية المالية.

### 🎮 <a name="gaming"></a>الألعاب

تكامل مع البيانات المتعلقة بالألعاب ومحرّكات الألعاب وخدماتها.

### 🏠 <a name="home-automation"></a>أتمتة المنزل

التحكم في أجهزة المنزل الذكي ومعدات الشبكة المنزلية وأنظمة الأتمتة.

### 🧠 <a name="knowledge--memory"></a>المعرفة والذاكرة

تخزين دائم للذاكرة باستخدام بنى الرسوم البيانية المعرفية (Knowledge Graphs). تُمكّن نماذج الذكاء الاصطناعي من الاحتفاظ بالمعلومات المنظّمة والاستعلام عنها عبر الجلسات المختلفة.

### ⚖️ <a name="legal"></a>القانون

الوصول إلى المعلومات القانونية والتشريعات وقواعد البيانات القانونية. تُمكّن نماذج الذكاء الاصطناعي من البحث في الوثائق القانونية والمعلومات التنظيمية وتحليلها.

### 🗺️ <a name="location-services"></a>خدمات الموقع

خدمات قائمة على الموقع وأدوات الخرائط. تُمكّن نماذج الذكاء الاصطناعي من التعامل مع البيانات الجغرافية ومعلومات الطقس والتحليلات المعتمدة على الموقع.

### 🎯 <a name="marketing"></a>التسويق

أدوات لإنشاء وتحرير محتوى التسويق، والتعامل مع بيانات الويب الوصفية، وتموضع المنتجات، وأدلة التحرير.

### 📊 <a name="monitoring"></a>المراقبة

الوصول إلى بيانات مراقبة التطبيقات وتحليلها. تُمكّن نماذج الذكاء الاصطناعي من مراجعة تقارير الأخطاء ومقاييس الأداء.

### 🎥 <a name="multimedia-process"></a>معالجة الوسائط المتعددة

توفّر القدرة على التعامل مع الوسائط المتعددة، مثل تحرير الصوت والفيديو والتشغيل وتحويل الصيغ، وتشمل أيضاً مرشّحات الفيديو وتحسيناته وما إلى ذلك.

### 🖥️ <a name="os-automation"></a>أتمتة نظام التشغيل

خوادم للتحكم في نظام تشغيل سطح المكتب: لقطات الشاشة، وإدارة النوافذ، وحقن إدخال الفأرة/لوحة المفاتيح، والأتمتة على مستوى النظام.

### 📋 <a name="product-management"></a>إدارة المنتجات

أدوات لتخطيط المنتجات وتحليل ملاحظات العملاء وترتيب الأولويات.

### 🏠 <a name="real-estate"></a>العقارات

خوادم MCP لإدارة علاقات عملاء العقارات وإدارة الممتلكات وسير عمل الوكلاء.

### 🔬 <a name="research"></a>البحث العلمي

أدوات لإجراء البحوث والاستبيانات والمقابلات وجمع البيانات.

### 🔎 <a name="RAG"></a>منصّات RAG الشاملة (End-to-End)

### 🔎 <a name="search"></a>البحث واستخراج البيانات

### 🔒 <a name="security"></a>الأمن

### 🌐 <a name="social-media"></a>وسائل التواصل الاجتماعي

تكامل مع منصّات التواصل الاجتماعي لإتاحة النشر والتحليلات وإدارة التفاعل. تُمكّن الأتمتة المدفوعة بالذكاء الاصطناعي للحضور الاجتماعي.

### 🔮 <a name="spirituality-and-esoterica"></a>الروحانيات والعلوم الباطنية

أدوات للتنجيم والتاروت وعلم الأعداد والأنظمة الفيدية وتصميم الإنسان (Human Design) وغيرها من الأدوات الباطنية — لوكلاء الذكاء الاصطناعي الذين يحسبون الخرائط أو يسحبون البطاقات أو يولّدون الأبراج.

### 🏃 <a name="sports"></a>الرياضة

أدوات للوصول إلى البيانات والنتائج والإحصاءات المتعلقة بالرياضة.

### 🎧 <a name="support-and-service-management"></a>الدعم وإدارة الخدمات

أدوات لإدارة دعم العملاء وإدارة خدمات تقنية المعلومات وعمليات مكتب المساعدة.

### 🌎 <a name="translation-services"></a>خدمات الترجمة

أدوات وخدمات ترجمة تُمكّن مساعدي الذكاء الاصطناعي من ترجمة المحتوى بين اللغات المختلفة.

### 🎙️ <a name="speech-to-text"></a>تحويل الكلام إلى نص

### 🎧 <a name="text-to-speech"></a>تحويل النص إلى كلام

أدوات لتحويل النص إلى كلام والعكس.

### 🚆 <a name="travel-and-transportation"></a>السفر والنقل

الوصول إلى معلومات السفر والنقل. تُمكّن من الاستعلام عن الجداول والمسارات وبيانات السفر الفورية.

### 🔄 <a name="version-control"></a>إدارة الإصدارات

التفاعل مع مستودعات Git ومنصّات إدارة الإصدارات. تُمكّن من إدارة المستودعات وتحليل الشيفرة والتعامل مع طلبات الدمج وتتبّع المشكلات وغيرها من عمليات إدارة الإصدارات عبر واجهات موحّدة.

### 🏢 <a name="workplace-and-productivity"></a>بيئة العمل والإنتاجية

### 🛠️ <a name="other-tools-and-integrations"></a>أدوات وتكاملات أخرى

## <a name="frameworks"></a>أطر العمل (Frameworks)

> [!NOTE]
> يتوفّر المزيد من أطر العمل والأدوات المساعدة وأدوات المطوّرين على [awesome-mcp-devtools](https://github.com/punkpeye/awesome-mcp-devtools).
> القائمة الكاملة لأطر العمل متوفّرة في [النسخة الإنجليزية](README.md#frameworks).

## <a name="tips-and-tricks"></a>نصائح وحيل

### موجّه (Prompt) رسمي لتعريف النماذج اللغوية بكيفية استخدام MCP

هل تريد أن تسأل Claude عن بروتوكول سياق النموذج (MCP)؟

أنشئ مشروعاً (Project)، ثم أضف إليه هذا الملف:

https://modelcontextprotocol.io/llms-full.txt

الآن يستطيع Claude الإجابة عن أسئلة كتابة خوادم MCP وكيفية عملها.

- https://www.reddit.com/r/ClaudeAI/comments/1h3g01r/want_to_ask_claude_about_model_context_protocol/

## سجل النجوم (Star History)

<a href="https://star-history.com/#punkpeye/awesome-mcp-servers&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=punkpeye/awesome-mcp-servers&type=Date" />
 </picture>
</a>
