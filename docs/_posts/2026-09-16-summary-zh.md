---
layout: default
title: "Horizon Summary: 2026-09-16 (ZH)"
date: 2026-09-16
lang: zh
---

> From 53 items, 8 important content pieces were selected

---

1. [谷歌 DeepMind 发布 Gemini 3.8 Live 与扩展思考模型](#item-1) ⭐️ 9.0/10
2. [思科安全邮件网关严重漏洞已被野外利用](#item-2) ⭐️ 8.0/10
3. [思科 IMC 参数注入漏洞可致 root 级远程代码执行](#item-3) ⭐️ 7.0/10
4. [思科披露 UCS 服务器 UEFI 安全启动绕过漏洞](#item-4) ⭐️ 7.0/10
5. [Simon Willison 为 Gemini 3.8 Live 语音到语音模型构建浏览器界面](#item-5) ⭐️ 7.0/10
6. [Good Start Labs 的 AI 将铁路游戏技能迁移到金融研究](#item-6) ⭐️ 7.0/10
7. [Groovy 沙箱绕过分析：以 Apache Syncope 为例的多版本 RCE](#item-7) ⭐️ 7.0/10
8. [《麻省理工科技评论》审视 AI 万亿美元基础设施豪赌](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [谷歌 DeepMind 发布 Gemini 3.8 Live 与扩展思考模型](https://deepmind.google/blog/introducing-gemini-3-8-live-and-3-8-live-extended-thinking/) ⭐️ 9.0/10

谷歌 DeepMind 发布了 Gemini 3.8 Live 和 Gemini 3.8 Live Extended Thinking，称其为目前最出色的对话式人工智能模型，旨在让语音交互更自然、流畅和智能。其中 Extended Thinking 版本是一款高推理能力的音频到音频模型，可在实时语音对话中进行复杂的后台推理。 此次发布将实时多模态 AI 推向更接近人类对话的体验，把实时视觉上下文、后台任务执行和扩展推理结合起来，且不打断用户对话。这也表明谷歌与 OpenAI 等公司在语音优先、能处理复杂多步任务的 AI 助手领域的竞争正在加剧。 Gemini 3.8 Live Extended Thinking 适用于在实时语音交互中需要更高后台推理能力来解决复杂多步问题的场景，并能处理实时视觉上下文和后台任务执行。该模型通过 Gemini API 以音频到音频的形式提供。

rss · Google DeepMind · Sep 15, 17:05

**背景**: Gemini 是谷歌 DeepMind 的旗舰多模态 AI 模型系列，能够处理文本、图像、音频和视频。"Live"模型针对实时对话交互进行了优化，而"Extended Thinking"指的是在回答前投入额外算力进行逐步推理的模型，这一技术因近期以推理为重点的大语言模型而流行。音频到音频意味着模型直接接收语音输入并生成语音输出，而无需经过单独的文本转写步骤。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/">Gemini 3 . 8 Live & Gemini 3 . 8 Live Extended Thinking</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.8-live-extended-thinking">Gemini 3 . 8 Live Extended Thinking | Gemini API | Google AI for...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Google DeepMind`, `#Gemini`, `#LLM`, `#Multimodal`

---

<a id="item-2"></a>
## [思科安全邮件网关严重漏洞已被野外利用](https://www.rapid7.com/blog/post/etr-cve-2026-76461-critical-cisco-secure-email-gateway-vulnerability-exploited-in-the-wild) ⭐️ 8.0/10

2026 年 9 月 14 日，思科披露了 CVE-2026-76461，这是 Cisco Secure Email Gateway 所用 AsyncOS 中的一个严重 SQL 注入漏洞，CVSS v3.1 评分为 9.8，CISA 当天即将其加入已知被利用漏洞（KEV）目录。该漏洞允许未经身份验证的远程攻击者通过向存在漏洞的网关发送特制电子邮件，以 root 权限执行任意命令。 由于该网关在日常运行中会处理外部投递的邮件，利用该漏洞无需身份验证或管理权限，因此任何运行受影响设备的企业都面临紧急打补丁的迫切需求。当天即被列入 KEV 目录表明该漏洞在披露前已作为零日漏洞被利用，防御方应假定存在活跃攻击，而非等待常规补丁周期。 修复版本为：15.5 及更早版本升级至 15.5.5-014，16.0 升级至 16.0.4-302，16.5 升级至 16.5.0-780；在发布时尚无公开的概念验证利用代码，也没有对威胁活动的归因。思科 PSIRT 于 2026 年 9 月获悉存在活跃利用，各组织应在常规补丁周期之外进行升级。

rss · Rapid7 Emergent Threat Response · Sep 15, 12:22

**背景**: Cisco Secure Email Gateway（原 IronPort Email Security Appliance）是一款企业邮件安全产品，用于检查入站和出站邮件中的钓鱼、恶意软件、垃圾邮件和商业电子邮件欺诈。它运行思科的 AsyncOS 操作系统，而 SQL 注入是一类将不可信输入当作数据库命令解析的漏洞，在此可升级为远程 root 命令执行。CVSS 是一套标准化的 0-10 分严重性评分体系，9.8 的基础分反映出在无需权限和用户交互的情况下可造成最大影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator">NVD CVSS v 3 Calculator</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#Cisco`, `#SQL injection`, `#exploit`

---

<a id="item-3"></a>
## [思科 IMC 参数注入漏洞可致 root 级远程代码执行](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cimc-arg-inject-upSHdMfU?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Cisco%20Integrated%20Management%20Controller%20Argument%20Injection%20Vulnerabilities%26vs_k=1) ⭐️ 7.0/10

思科披露了其集成管理控制器（IMC）基于 Web 的管理界面中存在多个参数注入漏洞（CVE-2026-20200 和 CVE-2026-20288），安全影响评级为“高”。具有低权限的已认证远程攻击者可利用这些漏洞在底层操作系统上执行任意命令并提升至 root 权限；思科已发布软件更新，但没有任何临时缓解措施。 思科 IMC 广泛部署于 UCS 及其他思科服务器上，是一种带外管理接口，因此其中的 root 级漏洞可能让攻击者深度控制关键基础设施。由于据称 CVE-2026-20200 已存在公开的概念验证利用代码，未修补系统面临更高的真实攻击风险。 这些漏洞属于 IMC Web 界面中的参数注入问题（CWE-88，即未正确中和参数分隔符），攻击者需通过身份认证但仅需低权限。思科将其影响评为“高”，并明确表示没有临时缓解措施，因此管理员必须安装官方提供的软件更新。

rss · Cisco Security Advisories · Sep 15, 20:36

**背景**: 思科集成管理控制器（IMC）是用于远程管理思科 UCS 及其他服务器的基板管理控制器固件，即使主机操作系统宕机也能通过其 Web 界面进行带外管理。参数注入是命令注入的一种，指未经验证的输入被直接传入命令参数，使攻击者能够改变命令的执行方式。CVE 编号是公开披露安全漏洞的标准标识，思科的公告通常会列出受影响产品、修复版本和严重性评级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/cybersecurityjournal_cisco-imc-cve-2026-20200-public-exploit-activity-7491259853877989377-fNXn">Cisco IMC CVE - 2026 - 20200 Exploit Grants Root Access | LinkedIn</a></li>
<li><a href="https://cwe.mitre.org/data/definitions/88">CWE - CWE-88: Improper Neutralization of Argument Delimiters in...</a></li>
<li><a href="https://cve.akaoma.com/cve-2026-20200">CVE - 2026 - 20200 Security Vulnerability & Exploit Details</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#cisco`, `#remote-code-execution`, `#privilege-escalation`

---

<a id="item-4"></a>
## [思科披露 UCS 服务器 UEFI 安全启动绕过漏洞](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ucs-uefi-sb-bypass-eb6xC5GW?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Cisco%20UCS%20and%20UCS-Based%20Appliances%20UEFI%20Shell%20Secure%20Boot%20Bypass%20Vulnerability%26vs_k=1) ⭐️ 7.0/10

思科披露了一个高危的 UEFI 安全启动绕过漏洞，编号为 CVE-2026-20293，影响 UCS 服务器及基于 UCS 的设备。该漏洞源于在启用安全启动的情况下，UEFI Shell 中仍可使用内存写入命令，攻击者可借此修改 UEFI 内存变量并执行未授权软件；思科已发布软件更新，但不存在任何变通方案。 这对企业环境而言是一个重大问题，因为 UCS 服务器和设备在数据中心中广泛部署，而该漏洞破坏了保护预启动环境的安全启动信任链。具有 user 或 admin 角色的已认证用户以及拥有物理访问权限的未认证攻击者均可利用该漏洞，可能危及整个启动过程。 该漏洞被评为高危级别，需要具备 user 或 admin 账户的有效凭据或对设备的物理访问权限；利用方式包括在启动时选择 UEFI Shell 启动选项，并使用 shell 命令覆盖与安全启动相关的内存值。思科指出不存在变通方案，因此应用已发布的软件更新是唯一的修复措施。

rss · Cisco Security Advisories · Sep 15, 20:34

**背景**: UEFI 安全启动是一种固件标准，通过验证引导加载程序和驱动程序的数字签名，防止未授权代码在操作系统加载前运行。UEFI Shell 是内置于固件中的命令行界面，用于调试和诊断，其中包含 dmem 和 mm 等内存读写命令，可直接访问物理内存。当安全启动处于活动状态时，标准防护措施是删除或抑制 UEFI Shell 启动项，但思科的实现使这些内存写入命令仍可访问，从而导致了绕过。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-ucs-uefi-sb-bypass-eb6xC5GW.html">Cisco UCS and UCS -Based Appliances UEFI Shell Secure... - Cisco</a></li>
<li><a href="https://cybersecurefox.com/en/vu-718077-uefi-shell-spi-flash-secure-boot-bypass/">VU#718077: UEFI Shell In SPI Flash Allows Secure Boot Bypass</a></li>
<li><a href="https://cybernews.com/security/uefi-firmware-vulnerability-secure-boot-bypass/">Secure Boot bypass exposes firmware risk across major... | Cybernews</a></li>

</ul>
</details>

**标签**: `#security`, `#UEFI`, `#Secure Boot`, `#Cisco UCS`, `#vulnerability`

---

<a id="item-5"></a>
## [Simon Willison 为 Gemini 3.8 Live 语音到语音模型构建浏览器界面](https://simonwillison.net/2026/Sep/15/gemini-live/) ⭐️ 7.0/10

Simon Willison 发布了一个基于浏览器的 Web UI，用于测试 Google 新推出的 Gemini 3.8 Live 和 Gemini 3.8 Live Extended Thinking 语音到语音模型，支持选择模型和语音预设、输入可选的系统提示词，以及对话中途打断。该实现不使用任何库，直接连接 Google 的 WebSocket 端点，并使用 Web Audio API 的 AudioContext 同时进行麦克风采集和音频播放。 这为开发者提供了一个立即可用、开放的参考实现，让他们无需从零构建客户端就能探索实时语音 AI，降低了试验 Google 新 Live 模型的门槛。这也表明语音到语音模型正成为各大 AI 厂商的竞争焦点，Google 的 Gemini 3.8 Live 系列与 OpenAI 的 GPT-Live 产品线形成了直接对位。 该工具连接到 wss://generativelanguage.googleapis.com 的 v1alpha GenerativeService BidiGenerateContent API WebSocket 端点；转录界面提示发送文本消息会打断当前语音回复，且转录内容可能包含在播放前就被打断的语音。它是一个演示/测试工具而非生产级应用，并建议用户佩戴耳机以减少回声。

rss · Simon Willison · Sep 15, 22:47

**背景**: 语音到语音模型直接处理音频输入并生成音频输出，而不是串联独立的语音识别和文本转语音系统，从而实现更低的延迟和更自然的对话轮次切换。Google 的 Gemini Live API 通过 WebSocket 暴露这一能力，允许客户端与模型之间双向流式传输音频。OpenAI 的 GPT-Live 系列是类似的产品，两者都代表着向实时、可打断的语音代理方向的转变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/live">Getting started with GPT - Live | OpenAI API</a></li>

</ul>
</details>

**标签**: `#gemini`, `#speech-to-speech`, `#voice-ai`, `#google`, `#developer-tools`

---

<a id="item-6"></a>
## [Good Start Labs 的 AI 将铁路游戏技能迁移到金融研究](https://www.latent.space/p/good-start-labs) ⭐️ 7.0/10

Good Start Labs 训练了一个 300 亿参数模型来玩《1830：铁路与强盗大亨游戏》，其中一个训练版本在 Finance-Agent 基准的 SEC 文件研究任务上表现提升。据称，一个独立 AI 研究代理在公司从未运行过的测试中发现了相同的特征。 这表明精心设计的训练环境可以让技能从游戏迁移到现实职业任务，可能重塑在数据稀缺或昂贵领域训练 AI 模型的方式。它也支持了可验证策略游戏能作为可扩展、高信号训练场，用于培养长期规划等通用能力的观点。 该模型在铁路棋盘游戏中作为多轮终端代理进行训练，性能提升取决于具体的训练设计，而不仅仅是接触游戏本身。Good Start Labs 是从 Every 分拆出来的公司，获得了 General Catalyst 和 Inovia 的 360 万美元融资，专注于利用游戏训练和评估模型。

rss · Latent Space · Sep 15, 20:11

**背景**: 迁移学习是一种机器学习技术，模型先在一个任务上预训练，再适应另一个相关任务，从而学得更快、所需数据更少。Good Start Labs 利用强化学习环境和实时人类反馈，在可验证的策略游戏中训练 AI 模型，目标是培养长期规划、多智能体协调和心理理论等通用技能。《1830》棋盘游戏是一款关于 19 世纪铁路大亨的复杂策略游戏，常被用作多步决策的测试平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://goodstartlabs.com/research/what-a-railroad-game-taught-a-model-about-finance">What a Railroad Game Taught a Model About... | Good Start Labs</a></li>
<li><a href="https://zerohour.day/item/eaf5399d32affe9e679f2fbb8627973ed5611bcb">Can Skills Learned in Games Transfer to Real-World Work? · ZeroHour</a></li>
<li><a href="https://pulkit-khandelwal.medium.com/transfer-learning-fad115392f3a">TRANSFER LEARNING . 1. ABSTRACT | by Pulkit Khandelwal | Medium</a></li>

</ul>
</details>

**标签**: `#AI`, `#transfer learning`, `#game-based learning`, `#training design`, `#machine learning`

---

<a id="item-7"></a>
## [Groovy 沙箱绕过分析：以 Apache Syncope 为例的多版本 RCE](https://xz.aliyun.com/news/92835) ⭐️ 7.0/10

阿里云安全博客（xz.aliyun.com）发布了一篇详细的技术分析文章，以真实的 Apache Syncope RCE 漏洞链为例，系统梳理了 Groovy 黑名单沙箱的三类绕过方式：解释器逃逸、运行时间接调用、反射与黑名单盲区。文章从沙箱的实现原理出发，说明每种绕过的切入点在哪、为什么能绕过，并给出了在真实目标上的利用效果。 Groovy 沙箱被广泛用于 Jenkins 等 CI/CD 平台和 CrafterCMS 等内容管理系统中，以安全执行不受信任的脚本，因此任何绕过技术都直接转化为远程代码执行风险。这项研究为安全研究人员和开发者提供了可操作的知识，用于审计和加固沙箱环境，尤其是依赖黑名单限制的场景。 文章涵盖三类不同的绕过方式：解释器逃逸（滥用 Groovy 解释器本身突破沙箱约束）、运行时间接调用（通过黑名单未覆盖的间接调用路径触达危险方法）、以及反射与黑名单盲区（利用 Java 反射或黑名单中的遗漏访问受限类和方法）。分析以真实的 Apache Syncope 漏洞链为基础，展示了实际利用效果而非理论上的弱点。

rss · Aliyun Xianzhi Community · Sep 15, 08:00

**背景**: Groovy 是一种运行在 JVM 上的动态语言，常用于 Java 应用中的脚本编写，沙箱则用于限制不受信任的 Groovy 脚本能做什么。基于黑名单的沙箱通过拦截已知危险的类和方法来工作，但这种机制本质上很脆弱，因为它必须预判所有危险路径。Apache Syncope 是一个开源身份管理平台，使用 Groovy 实现脚本化逻辑，因此其沙箱成为攻击者的高价值目标。类似的绕过曾影响 Jenkins（通过隐式允许列表的平台 Groovy 文件导致的 CVE）和 CrafterCMS（CVE-2025-6384），表明这是一类反复出现的漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://plugins.jenkins.io/workflow-cps/">Pipeline: Groovy | Jenkins plugin</a></li>
<li><a href="https://www.sentinelone.com/vulnerability-database/cve-2025-6384/">CVE-2025-6384: CrafterCMS Groovy Sandbox Bypass RCE Flaw</a></li>

</ul>
</details>

**标签**: `#Groovy`, `#Sandbox Bypass`, `#RCE`, `#Apache Syncope`, `#Security Research`

---

<a id="item-8"></a>
## [《麻省理工科技评论》审视 AI 万亿美元基础设施豪赌](https://www.technologyreview.com/2026/09/15/1144028/ai-infrastructure-boom-investment-bubble-risk/) ⭐️ 7.0/10

《麻省理工科技评论》发表了一篇分析文章，审视规模达万亿美元的 AI 基础设施投资热潮，在技术变革潜力与经济不确定性和泡沫风险之间进行权衡。文章引用了宾夕法尼亚大学沃顿商学院金融学教授杰西卡·瓦赫特（Jessica Wachter）的观点，她从一项毫无争议的“显著事实”出发来评估 AI 对经济的影响。 少数超大规模云厂商的 AI 资本支出规模已成为股市上涨的重要驱动力，因此基础设施变现的任何延迟都可能波及半导体及更广泛的科技股。判断这一支出周期是持久的建设浪潮还是泡沫，对投资者、政策制定者以及所有关注 AI 真实经济影响的人都至关重要。 文章指出，由于存在大量商业和技术层面的不确定性，评估工作十分复杂，而支出高度集中于少数几家公司是这一周期的显著特征。相关报道中引用的分析师认为，AI 泡沫可能在 2027 年前后开始破裂，而且这轮投资热潮的融资方式仍不为人所知。

rss · MIT Technology Review AI · Sep 15, 10:00

**背景**: AI 热潮引发了对数据中心、芯片和电力基础设施前所未有的资本支出浪潮，仅四家最大的科技公司一年内的投资就高达数千亿美元。这轮建设支撑了创纪录的股市估值，但也引发了典型的泡沫疑问：回报能否支撑支出、投资资金从何而来，以及 AI 硬件折旧速度有多快。《麻省理工科技评论》是麻省理工学院旗下的老牌科技刊物，沃顿商学院则是宾夕法尼亚大学的商学院。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2025/dec/01/ai-bubble-us-economy">The question isn’t whether the AI bubble will burst... | The Guardian</a></li>
<li><a href="https://www.aol.com/articles/ai-bubble-leaking-air-economists-185832000.html">The AI bubble is leaking air, some economists say. Should... - AOL</a></li>
<li><a href="https://intellectia.ai/blog/ai-infrastructure-investment-boom-2026">AI Infrastructure Investment Boom 2026: $700B Hyperscaler...</a></li>

</ul>
</details>

**标签**: `#AI investment`, `#economic analysis`, `#AI infrastructure`, `#technology trends`, `#finance`

---