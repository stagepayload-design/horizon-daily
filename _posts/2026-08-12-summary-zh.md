---
layout: default
title: "Horizon Summary: 2026-08-12 (ZH)"
date: 2026-08-12
lang: zh
---

> From 69 items, 21 important content pieces were selected

---

1. [TPM 2.0 参考代码存在侧信道攻击漏洞](#item-1) ⭐️ 9.0/10
2. [关键 SharePoint 远程代码执行链已披露并修复](#item-2) ⭐️ 9.0/10
3. [压缩即预测：统一信息论与机器学习](#item-3) ⭐️ 8.0/10
4. [Mojo 1.0 发布：高性能 Python 超集的重要里程碑](#item-4) ⭐️ 8.0/10
5. [Go：AI 辅助软件工程的理想语言](#item-5) ⭐️ 8.0/10
6. [Grok Bot：自主 AI 代理引发安全与隐私担忧](#item-6) ⭐️ 8.0/10
7. [英伟达的战略风险：估值过高与 CUDA 生态挑战](#item-7) ⭐️ 8.0/10
8. [开发者通过中间人代理截获 GitHub Copilot 流量](#item-8) ⭐️ 8.0/10
9. [CISA 将三个正在被利用的漏洞加入 KEV 目录](#item-9) ⭐️ 8.0/10
10. [微软修复近 400 个漏洞，其中一个已被积极利用](#item-10) ⭐️ 8.0/10
11. [Chai Discovery 引领 BioAI 浪潮，达成四项制药合作](#item-11) ⭐️ 8.0/10
12. [llama.cpp b10361 修复 EXAONE 4.5 的 SWA 错误](#item-12) ⭐️ 7.0/10
13. [NVIDIA 发布 Nemotron 3.5 Lightning 和 NeMo Switchyard](#item-13) ⭐️ 7.0/10
14. [OpenAI 伦理主管上任不到一年即离职](#item-14) ⭐️ 7.0/10
15. [用笔式绘图机制作全息图，巧妙类比橄榄油](#item-15) ⭐️ 7.0/10
16. [伦敦地铁启动实时面部识别试验](#item-16) ⭐️ 7.0/10
17. [Apple Silicon macOS 虚拟机修复显著提升 llama.cpp 推理速度](#item-17) ⭐️ 7.0/10
18. [OpenAI 测试在 ChatGPT 中投放广告以维持免费服务](#item-18) ⭐️ 7.0/10
19. [OpenAI Daybreak 模型现已在 AWS Bedrock 上可用](#item-19) ⭐️ 7.0/10
20. [无无损文本转换：Sophie Alpert 的 AI 写作政策](#item-20) ⭐️ 7.0/10
21. [开源权重模型 Glimmer 和 Spark 承诺在单张 RTX 3090 上实现个人 AI](#item-21) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [TPM 2.0 参考代码存在侧信道攻击漏洞](https://kb.cert.org/vuls/id/431093) ⭐️ 9.0/10

在 TPM 2.0 参考实现中发现了两个严重漏洞（CVE-2026-6726 和 CVE-2026-6727），可导致信息泄露和时序侧信道攻击，从而危及 RSA 密钥并可能伪造证明。 这些漏洞影响了现代计算平台的基础安全性，因为 TPM 广泛用于硬件支持的加密操作和证明。成功利用可能破坏对安全启动、磁盘加密和远程证明的信任，影响企业、云服务提供商和个人用户。 CVE-2026-6727 是 RSA OAEP 解密中的时序侧信道漏洞，可能允许解密使用 TPM 管理的 RSA 密钥（包括背书密钥 EK）加密的密文。CVE-2026-6726 是一个信息泄露漏洞，可能让攻击者从支持 TPM 的 CA 获取伪造 TPM 密钥的凭证，从而伪造证明。两者都需要对 TPM 命令接口具有特权本地访问权限。

rss · CERT CC Vulnerability Notes · Aug 11, 15:12

**背景**: 可信平台模块（TPM）是一种安全密码处理器，提供硬件支持的加密服务，如安全启动、磁盘加密和远程证明。可信计算组织（TCG）维护 TPM 规范并提供参考实现，供供应商构建符合 TPM 标准的产品。侧信道攻击利用时序或功耗等物理特性来提取秘密信息，而 RSA OAEP 解密是时序攻击的常见目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kb.cert.org/vuls/id/431093">VU#431093 - TCG TPM 2 . 0 reference code found vulnerable to...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Trusted_Platform_Module">Trusted Platform Module - Wikipedia</a></li>
<li><a href="https://blog.quarkslab.com/vulnerabilities-in-the-tpm-20-reference-implementation-code.html">Vulnerabilities in the TPM 2 . 0 reference implementation code</a></li>

</ul>
</details>

**社区讨论**: 提供的评论与 TPM 漏洞无直接关联，它们讨论了无关的话题，如 AI 模型训练和推理。因此，无法总结相关的社区观点。

**标签**: `#security`, `#TPM`, `#vulnerability`, `#side-channel`, `#cryptography`

---

<a id="item-2"></a>
## [关键 SharePoint 远程代码执行链已披露并修复](https://www.rapid7.com/blog/post/etr-cve-2026-63520-microsoft-sharepoint-remote-code-execution-fixed) ⭐️ 9.0/10

Rapid7 Labs 披露了 CVE-2026-63520，这是 Microsoft SharePoint 中的一个远程代码执行漏洞，当与先前披露的身份验证绕过漏洞 CVE-2026-55040 链接时，允许未经身份验证的攻击者在易受攻击的服务器上执行任意代码。微软已发布此漏洞的修复程序。 此漏洞链至关重要，因为它允许在广泛使用的企业平台 SharePoint 上执行未经身份验证的远程代码，可能导致服务器完全受损和数据泄露。协调披露凸显了及时修补的重要性以及 AI 在漏洞研究中日益增长的作用。 CVE-2026-63520 的 CVSSv3.1 评分为 8.1（高危），归类为 CWE-20（输入验证不当）。该漏洞源于 SharePoint 的 Business Connectivity Services 中的不安全.NET 类型实例化问题，影响所有受支持的 SharePoint 版本，以及 Microsoft Project Server 和 Office Web Apps Server 的某些版本。

rss · Rapid7 Emergent Threat Response · Aug 11, 13:00

**背景**: CVE-2026-63520 是 Rapid7 Labs 发现的两个漏洞链的一部分。第一个漏洞 CVE-2026-55040 是一个 JWT 令牌身份验证绕过漏洞，允许未经身份验证的攻击者以 SharePoint 用户或管理员身份进行身份验证。将这些漏洞链接起来可以实现未经身份验证的远程代码执行。该漏洞链是为 2026 年柏林 Pwn2Own 竞赛开发的，Rapid7 的研究还探讨了 AI 模型如何加速漏洞发现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rapid7.com/blog/post/etr-cve-2026-63520-microsoft-sharepoint-remote-code-execution-fixed/">Rapid7 and Microsoft disclose CVE - 2026 - 63520 , a new SharePoint ...</a></li>
<li><a href="https://windowsforum.com/security-alerts.84/cve-2026-63520-patch-sharepoint-server-rce-now.442485/">CVE - 2026 - 63520 : Patch SharePoint Server RCE Now | Windows Forum</a></li>
<li><a href="https://dbugs.ptsecurity.com/vulnerability/PT-2026-70612">CVE - 2026 - 63520 — Remote Code Execution in Microsoft Sharepoint ...</a></li>

</ul>
</details>

**标签**: `#CVE`, `#Microsoft SharePoint`, `#Remote Code Execution`, `#Security`, `#Vulnerability Disclosure`

---

<a id="item-3"></a>
## [压缩即预测：统一信息论与机器学习](https://ngrok.com/blog/compression-is-prediction) ⭐️ 8.0/10

文章《压缩即预测》认为压缩与预测在根本上是等价的，这一论点对理解智能和机器学习具有深远意义。它引发了高质量的社区讨论，引用了学术课程和视频。 这一观点可能重塑研究人员处理 AI 的方式，表明改进压缩算法可能直接增强预测能力。它架起了信息论与机器学习之间的桥梁，可能带来更统一的理论框架和实际进展。 讨论强调了细微差别，例如当数据分布完全代表未来问题时等价性成立，但在分布偏移下则不成立。社区成员还指出了相关概念，如 Kolmogorov 复杂度和归一化压缩距离，以及 Grant Sanderson 的视频系列。

hackernews · nikolay · Aug 11, 19:49 · [社区讨论](https://news.ycombinator.com/item?id=49263497)

**背景**: 压缩涉及用更少的比特表示数据，而预测涉及预测未来数据。这种等价性表明，这两个任务都依赖于捕捉数据中的潜在模式和规律。这一思想源于信息论以及 Solomonoff 和 Kolmogorov 等人的工作，并且是剑桥大学“信息论、推理与学习算法”课程的核心。

**社区讨论**: 社区评论表现出强烈的参与度，一位用户指出该论点与剑桥大学的一门课程一致，另一位引用了 Grant Sanderson 的视频系列。关于“压缩即预测”是否准确存在争论，有人建议“压缩即抽象，解压即外推”，并针对分布偏移下的泛化提出了细致的反驳。

**标签**: `#compression`, `#prediction`, `#machine learning`, `#information theory`, `#AI`

---

<a id="item-4"></a>
## [Mojo 1.0 发布：高性能 Python 超集的重要里程碑](https://www.modular.com/blog/modular-26-5-mojo-1-0-is-here) ⭐️ 8.0/10

Modular 发布了 Mojo 1.0，标志着这个面向高性能 AI/ML 工作负载的 Python 超集语言迈出了重要一步。该版本包含 Mojo 编译器和工具链，并计划逐步开源更多组件，到 2026 年完全开源编译器。 Mojo 1.0 意义重大，因为它旨在将 Python 的易用性与 C 级性能相结合，面向 AI/ML 工作负载。此次发布可能会吸引寻求高性能 Python 替代品的开发者，从而影响 AI/ML 生态系统和更广泛的编程语言格局。 Mojo 最初旨在成为 Python 的超集，但截至 2026 年 3 月，这一目标已被无限期推迟或放弃。编译器目前是闭源的，计划于 2026 年开源，该语言支持 Linux 和 macOS。

hackernews · dayanruben · Aug 11, 16:56 · [社区讨论](https://news.ycombinator.com/item?id=49261128)

**背景**: Mojo 是由 Modular 开发的编程语言，旨在结合 Python 的易用性与 C 和 Rust 等系统语言的性能。它面向高性能计算，特别是 AI/ML 工作负载，采用类似 Python 的语法，但具有静态类型和其他系统级特性。该语言已开发多年，测试版于 2026 年达到 1.0。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_(programming_language)">Mojo (programming language) - Wikipedia</a></li>
<li><a href="https://mojolang.org/">Mojo</a></li>
<li><a href="https://www.modular.com/blog/the-next-big-step-in-mojo-open-source">Modular: The Next Big Step in Mojo Open Source</a></li>

</ul>
</details>

**社区讨论**: 社区评论情绪复杂：一些用户对 Mojo 的价值主张和缺乏清晰概述表示困惑，另一些则批评闭源编译器并质疑开源延迟。还有人担心放弃 Python 超集目标以及公告中使用 AI 生成内容的问题。

**标签**: `#Mojo`, `#programming-languages`, `#AI/ML`, `#compiler`, `#Python`

---

<a id="item-5"></a>
## [Go：AI 辅助软件工程的理想语言](https://developers.googleblog.com/why-go-is-an-ideal-language-for-ai-assisted-software-engineering/) ⭐️ 8.0/10

谷歌发布了一篇博客文章，认为 Go 语言的简洁性、工具链和可读性使其特别适合 AI 辅助软件工程，引发了关于 AI 编程语言选择的激烈讨论。 这很重要，因为随着 AI 辅助开发成为主流，编程语言的选择会显著影响 AI 工具的效果。讨论凸显了关于哪种语言最适合 AI 编码的日益激烈的争论，对开发者、团队和行业都有影响。 博客文章强调 Go 的简洁性、强大的工具链和可读性是 AI 辅助工程的关键优势。社区评论包括 Netflix Go 公会负责人的见解和批评性观点，表明存在实质性的辩论。

hackernews · 0xedb · Aug 11, 16:57 · [社区讨论](https://news.ycombinator.com/item?id=49261133)

**背景**: AI 辅助软件工程涉及使用 AI 工具，如聊天机器人、代码助手和自主代理，帮助工程师编写、审查、测试和交付代码。根据 Stack Overflow 2025 年开发者调查，到 2026 年，84%的开发者在工作中使用这些工具。Go，也称为 Golang，是由谷歌设计的开源、编译型、静态类型编程语言，旨在简单、高性能、可读且高效。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://reliasoftware.com/blog/ai-assisted-software-development">AI - Assisted Software Development: Workflow, Risks, Best Practices</a></li>
<li><a href="https://www.freecodecamp.org/news/what-is-go-programming-language/">What is Go ? Golang Programming Language Meaning Explained</a></li>

</ul>
</details>

**社区讨论**: 社区讨论热烈且观点不一。一些人，如 Netflix Go 公会负责人，同意文章观点，指出 AI 代理能写出更好的 Go 代码，且 Go 有很好的资源。其他人则持批评态度，一位评论者称该文章是“障眼法”，另一位建议具有形式验证的语言（如 Dafny）或 Rust 的严格编译器可能更适合 AI 编码。

**标签**: `#Go`, `#AI-assisted software engineering`, `#programming languages`, `#developer tools`, `#Google`

---

<a id="item-6"></a>
## [Grok Bot：自主 AI 代理引发安全与隐私担忧](https://x.ai/bot) ⭐️ 8.0/10

xAI 推出了 Grok Bot，这是一种能够自主与用户账户交互的新型 AI 代理，其官方页面展示了这一功能。该机器人可以接管浏览器凭据并代表用户执行操作，标志着 AI 代理演进的重要一步。 Grok Bot 代表了 AI 代理领域的重要进展，可能重塑用户与在线服务的交互方式。然而，它也加剧了安全和隐私风险，因为拥有账户访问权限的代理可能通过提示注入或漏洞被利用，影响个人和企业。 该机器人可以自主管理例程、上下文和领域，并与其他代理通信，类似于 OpenClaw 等框架。社区成员对凭据窃取和数据画像表示担忧，强调需要强有力的安全措施和明确政策。

hackernews · rvz · Aug 11, 17:23 · [社区讨论](https://news.ycombinator.com/item?id=49261514)

**背景**: AI 代理是能够自主感知、决策并采取行动以实现目标的系统，无需人工干预。与传统聊天机器人不同，它们可以访问和操作内部系统，增加了数据泄露风险。代理式 AI 的兴起引发了关于安全、治理和法律影响的讨论，尤其是当像 xAI 这样的公司推广此类机器人同时也在使用反机器人措施时。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.openhermit.com/blog/how-agents-interact">How AI Agents Actually Interact with Websites... — OpenHermit Blog</a></li>
<li><a href="https://www.hulkapps.com/blogs/ecommerce-hub/are-we-ready-for-autonomous-ai-agents-5">Are We Ready for Autonomous AI Agents ?</a></li>
<li><a href="https://www.lunagen.ai/post/ai-entanglement-podcast-1">The Hidden Danger of AI Agents | Data Leaks & Security Risks</a></li>

</ul>
</details>

**社区讨论**: 社区评论反应不一：一些用户觉得交互自然，视其为 AI 演进的下一个步骤，而另一些用户则对安全感到焦虑，担心数据泄露、删除或通过提示注入被劫持。还有人担心机器人与系统交互的合法性以及政府进行数据画像的可能性。

**标签**: `#AI agents`, `#security`, `#privacy`, `#automation`, `#X`

---

<a id="item-7"></a>
## [英伟达的战略风险：估值过高与 CUDA 生态挑战](https://stratechery.com/2026/nvidias-risky-business/) ⭐️ 8.0/10

Stratechery 发布了一篇题为《英伟达的冒险生意》的分析文章，审视英伟达在 AI 硬件市场中的战略风险，重点关注潜在的估值过高和软件生态挑战。文章强调了对 AI 计算需求可持续性以及 CUDA 开发者体验的担忧。 这一分析意义重大，因为英伟达是 AI 硬件领域的主导者，任何战略失误都可能影响整个科技行业和投资者情绪。关于 CUDA 开发者体验和需求增长的讨论可能影响未来 AI 基础设施的投资和竞争。 文章指出，虽然英伟达关于计算需求增长的一阶假设可能是正确的，但关于需求增长的二阶假设可能被夸大。文章还提到，尽管 CUDA 是护城河，但其开发者体验相比替代方案较差，并且英伟达正在拓展机器人领域作为另一条路径。

hackernews · jonbaer · Aug 11, 10:02 · [社区讨论](https://news.ycombinator.com/item?id=49255710)

**背景**: 英伟达在 AI 硬件领域的主导地位得益于其 CUDA 软件生态系统，该系统已建设 20 多年，并深度融入机器学习研究。然而，AMD 和英特尔等竞争对手正在取得进展，美国对华芯片销售限制等地缘政治因素也增加了不确定性。AI 市场的快速增长也引发了潜在泡沫的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rownix.dev/en/articles/nvidia-cuda-ai-infrastructure-moat">Is Nvidia's Moat The Chip, Or The CUDA Ecosystem ? | Rownix's Blog</a></li>
<li><a href="https://www.htx.com/news/the-cuda-moat-that-huang-built-over-20-years-was-chiseled-op-ArnmnLMF/">The CUDA Moat That Huang Built Over 20 Years Was... | HTX Insights</a></li>
<li><a href="https://www.hitpaw.com/top-trending-tips/deepseek-is-bad-for-nvidia.html">How DeepSeek Disrupts NVIDIA ’s AI Chip Dominance</a></li>

</ul>
</details>

**社区讨论**: 社区评论反映了赞同与批评的混合观点。一位评论者指出，尽管 CUDA 根深蒂固，但其开发者体验较差；另一位则强调需求增长预期被夸大的风险。其他人则指出英伟达在机器人领域的布局及其在西方与中国之间的地位。

**标签**: `#Nvidia`, `#AI hardware`, `#CUDA`, `#business strategy`, `#semiconductors`

---

<a id="item-8"></a>
## [开发者通过中间人代理截获 GitHub Copilot 流量](https://www.lighthousenewsletter.com/p/i-put-github-copilot-behind-a-mitm) ⭐️ 8.0/10

一位开发者使用 mitmproxy 截获了 GitHub Copilot 的网络流量，揭示了其如何管理上下文、路由和数据收集。调查发现，最近的编辑可以从其他文件拉取上下文，并且没有规则将环境文件排除在上下文之外。 这很重要，因为它提供了对 Copilot 内部行为的实际洞察，对隐私和使用有影响。了解上下文如何注入以及收集了哪些数据，可以帮助开发者在是否使用 AI 编程助手方面做出明智的决定。 开发者实时观察了模型/能力发现和路由，并看到了在幽灵补全中注入到上下文的内容。他们还发现，最近的编辑可以从当前编辑文件之外的其他文件拉取上下文，并指出缺乏排除 env 文件的规则。

hackernews · j0selit0 · Aug 11, 10:40 · [社区讨论](https://news.ycombinator.com/item?id=49256057)

**背景**: GitHub Copilot 是一个 AI 编程助手，使用大型语言模型来建议代码。mitmproxy 是一个交互式的、支持 TLS 的拦截代理，可以捕获和修改 HTTP/HTTPS 流量。通过将 Copilot 置于中间人代理之后，开发者可以检查发送到服务以及从服务接收的数据，从而揭示其如何处理上下文和数据收集。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.github.com/en/copilot/concepts/network-settings">Network settings for GitHub Copilot - GitHub Docs</a></li>
<li><a href="https://github.com/mitmproxy/mitmproxy">GitHub - mitmproxy / mitmproxy : An interactive TLS-capable...</a></li>
<li><a href="https://github.blog/changelog/2024-07-31-copilot-network-requests-are-now-routed-based-on-subscription/">Copilot network requests are now routed based... - GitHub Changelog</a></li>

</ul>
</details>

**社区讨论**: 社区成员分享了技术修正和替代方法。一位用户指出 Codex 客户端是开源的，另一位建议使用 eBPF 来捕获明文数据，而无需对抗证书固定。一些人对缺乏 env 文件排除表示惊讶，还有一位不同意结论，认为高端 LLM 在没有精心策划上下文的情况下也能表现良好。

**标签**: `#GitHub Copilot`, `#AI coding assistants`, `#network interception`, `#privacy`, `#reverse engineering`

---

<a id="item-9"></a>
## [CISA 将三个正在被利用的漏洞加入 KEV 目录](https://www.cisa.gov/news-events/alerts/2026/08/11/cisa-adds-three-known-exploited-vulnerabilities-catalog) ⭐️ 8.0/10

2026 年 8 月 11 日，CISA 将三个漏洞加入其已知被利用漏洞（KEV）目录：CVE-2026-20349（Cisco ASA/FTD 堆检查）、CVE-2026-68820（Microsoft Windows AFD 释放后使用）和 CVE-2026-72898（Metabase SQL 注入）。这些添加基于积极利用的证据。 这些漏洞正被恶意行为者积极利用，对联邦企业及更广泛的公众构成重大风险。KEV 目录是确定修补优先级的关键资源，BOD 26-04 要求联邦机构及时修复这些高风险漏洞。 CVE-2026-20349 是 Cisco ASA/FTD 中的堆检查漏洞，可能与其他 FMC 漏洞结合导致权限提升。CVE-2026-68820 是 Windows WinSock 辅助功能驱动程序中的释放后使用漏洞，可实现本地权限提升。CVE-2026-72898 是 Metabase SQL 注入漏洞，CVSS 评分为 10.0，可导致完全管理员访问。

rss · CISA Cybersecurity Advisories · Aug 11, 12:00

**背景**: KEV 目录是 CISA 维护的已知被利用漏洞列表，旨在帮助组织确定修复优先级。BOD 26-04 要求联邦机构快速修补目录中列出的高风险漏洞，尤其是那些在公开暴露资产上的漏洞。这些漏洞是网络行为者常用的攻击向量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vuldb.com/?id.331995">CVE-2025-62213 Microsoft Windows Ancillary Function Driver for ...</a></li>
<li><a href="https://www.sentinelone.com/vulnerability-database/cve-2026-42911/">CVE-2026-42911: Windows WinSock Privilege Escalation Flaw</a></li>
<li><a href="https://wz-it.com/en/blog/metabase-sql-injection-cvss-10-emergency-patch/">Metabase emergency patch: SQL injection rated CVSS 10.0 is being...</a></li>

</ul>
</details>

**标签**: `#CISA`, `#vulnerabilities`, `#security`, `#KEV catalog`, `#exploits`

---

<a id="item-10"></a>
## [微软修复近 400 个漏洞，其中一个已被积极利用](https://krebsonsecurity.com/2026/08/microsoft-plugs-nearly-400-security-holes/) ⭐️ 8.0/10

微软发布了最新的安全更新，修复了 Windows 及受支持软件中的 398 个漏洞，其中包括一个已被积极利用的漏洞和两个在补丁发布前已被公开披露的漏洞。 这次大规模补丁至关重要，因为它包含一个已被积极利用的漏洞，对用户和组织构成直接威胁。及时修补对于减轻潜在攻击和保护敏感数据至关重要。 此次更新涵盖多种产品，被积极利用的漏洞很可能是一个零日漏洞。微软的补丁星期二发布通常包含大量 CVE，但此次数量明显偏高，强调了立即部署的必要性。

rss · Krebs on Security · Aug 11, 21:28

**背景**: 微软通常在每月的第二个星期二发布安全更新，称为“补丁星期二”，以修复其软件中的漏洞。被积极利用的漏洞是指在现实攻击中已被观察到的漏洞，通常在补丁可用之前就被利用，因此特别危险。美国网络安全和基础设施安全局（CISA）维护着一个已知被利用漏洞的列表，以帮助组织确定修复的优先级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cert.be/en/advisory/warning-microsoft-patch-tuesday-addressed-38-microsoft-vulnerabilities-including-2-actively">Warning: Microsoft Patch Tuesday addressed 38 Microsoft ... | Cert</a></li>
<li><a href="https://www.bleepingcomputer.com/news/microsoft/windows-10-kb5025221-and-kb5025229-updates-released/">Windows 10 KB5025221 and KB5025229 updates released</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#security`, `#patch`, `#vulnerabilities`, `#Windows`

---

<a id="item-11"></a>
## [Chai Discovery 引领 BioAI 浪潮，达成四项制药合作](https://www.latent.space/p/chai-discovery) ⭐️ 8.0/10

Chai Discovery 的联合创始人 Matthew McPartlon 和 Neil Patil 宣布，公司今年夏天达成了四项制药合作，标志着制药行业对 BioAI 工具的采用激增。这标志着 AI 驱动的药物发现平台获得了重要的商业验证。 这一进展凸显了更广泛的行业趋势：制药公司越来越愿意为 AI 驱动的药物发现工具付费，可能加速 AI 在生物技术领域的整合。Chai Discovery 的成功可能鼓励更多投资和采用 BioAI，重塑药物开发管线。 今年夏天达成的四项合作的具体合作伙伴未在新闻中披露。Chai Discovery 的平台，包括 Chai-2 模型，在从头抗体设计中实现了接近 20% 的命中率，公司最近以 38 亿美元估值完成了 4 亿美元的 C 轮融资，礼来、辉瑞和诺华已在运行其模型。

rss · Latent Space · Aug 11, 21:03

**背景**: BioAI 是指人工智能在生物学研究和药物发现中的应用，旨在加速治疗分子的识别和设计。传统的生物药发现可能需要 12 到 24 个月的反复湿实验测试，而像 Chai Discovery 这样的 AI 平台将早期发现压缩为自动化冲刺，减少了时间和成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/beyond-generative-code-why-chai-discovery-exposes-big-alex-hong-dndyc">Beyond the Generative Code: Why Chai Discovery Exposes Big...</a></li>
<li><a href="https://spoonai.me/posts/2026-07-17-chai-discovery-400m-series-c-ai-drug-discovery-jul2026-en">AI Doesn't Just Find Drugs Anymore — It Designs Them. Chai ...</a></li>
<li><a href="https://trial.medpath.com/news/chai-discovery-raises-70m-series-a-to-revolutionize-antibody-design-with-ai-platform-achieving-20-hit-rate">Chai Discovery Raises $70M Series A to... - MedPath Trial</a></li>

</ul>
</details>

**标签**: `#BioAI`, `#AI in Pharma`, `#Chai Discovery`, `#Biotech`, `#Commercialization`

---

<a id="item-12"></a>
## [llama.cpp b10361 修复 EXAONE 4.5 的 SWA 错误](https://github.com/ggml-org/llama.cpp/releases/tag/b10361) ⭐️ 7.0/10

llama.cpp 版本 b10361 修复了一个错误：由于层数检查发生在元数据加载之前，EXAONE 4.5 模型的滑动窗口注意力（SWA）未被启用。该修复确保了 EXAONE 4.5 的 SWA 行为正确，并添加了一个测试来覆盖 hparams 的顺序。 此错误修复意义重大，因为 EXAONE 4.5 是一个广泛使用的开源视觉语言模型，错误的 SWA 会降低模型性能和输出质量。该修复确保 llama.cpp 用户能够以正确的注意力机制运行 EXAONE 4.5，从而提高 LLM 推理的可靠性。 该错误发生在 load_arch_hparams 在读取 LLM_KV_NEXTN_PREDICT_LAYERS 之前检查 hparams.n_layer() == 64。对于带有 MTP 头的 EXAONE 4.5（block_count=65，nextn=1），n_layer() 返回 65，导致 SWA 块被跳过。修复还解决了 TENSOR_SKIP 张量在仅元数据模型构建中导致失败的相关问题，但该更改后来被还原。

github · github-actions[bot] · Aug 11, 17:12

**背景**: 滑动窗口注意力（SWA）是一种用于 Transformer 模型的技术，将注意力限制在局部窗口内，以减少计算成本和内存使用。EXAONE 4.5 是 LG AI Research 推出的 33B 参数视觉语言模型，采用 SWA 以提高效率。llama.cpp 是一个流行的开源库，用于在消费级硬件上运行 LLM，支持包括 EXAONE 在内的多种模型架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/docs/transformers/main/en/model_doc/exaone4_5.md">huggingface.co/docs/transformers/main/en/ model _doc/ exaone 4 _ 5 .md</a></li>
<li><a href="https://arxiv.org/html/2604.08644v1">EXAONE 4 . 5 Technical Report LG’s First Open-Weight...</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#bug fix`, `#SWA`, `#EXAONE`, `#LLM inference`

---

<a id="item-13"></a>
## [NVIDIA 发布 Nemotron 3.5 Lightning 和 NeMo Switchyard](https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/) ⭐️ 7.0/10

NVIDIA 发布了 Nemotron 3.5 Lightning，这是一个 30B 参数的混合专家（MoE）模型，具有 3B 激活参数，针对高吞吐、低延迟的智能体工作流进行了优化。此外，他们还推出了 NeMo Switchyard，一个用于智能模型路由的开源库，可动态为每个请求选择最佳模型。 此次发布标志着 NVIDIA 在面向智能体 AI 的高效专用模型领域发力，可能降低实时应用的推理成本和延迟。开源路由库可使开发者在多个模型之间平衡性能和成本，从而促进 AI 智能体在生产环境中的更广泛应用。 Nemotron 3.5 Lightning 是全精度版本，主要用于定制和后训练，而非直接用于生产推理。NeMo Switchyard 是一个 Apache-2.0 许可的预 alpha 控制平面，可在模型之间路由单个编码智能体的轮次，同时转换 OpenAI 和 Anthropic API 格式。

hackernews · droidjj · Aug 11, 19:35 · [社区讨论](https://news.ycombinator.com/item?id=49263340)

**背景**: 混合专家（MoE）是一种 LLM 架构，每个 token 仅激活部分参数，与相同规模的稠密模型相比，可实现更快的推理和更低的计算成本。模型路由是一种根据能力、成本和延迟等因素为每个请求动态选择最合适模型的技术，对于优化涉及多个模型的智能体工作流至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16">nvidia / NVIDIA - Nemotron - 3 . 5 - Lightning -30B-A3B-BF16 · Hugging Face</a></li>
<li><a href="https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/">NVIDIA Nemotron 3 . 5 Lightning Delivers Fast, Accurate Specialized...</a></li>
<li><a href="https://developer.nvidia.com/blog/route-ai-agent-workloads-across-models-with-nvidia-nemo-switchyard/">Route AI Agents Across Models with NVIDIA NeMo Switchyard</a></li>

</ul>
</details>

**社区讨论**: 社区评论情绪复杂：一些用户报告称，像 Nemotron 3.5 Lightning 这样的 MoE 模型在复杂编码任务上表现不如稠密模型，而另一些用户则称赞其速度。还有人担心路由如何处理提示缓存和粘性会话，并有人指责 NVIDIA 在基准比较中排除 Qwen 模型以偏概全。

**标签**: `#NVIDIA`, `#LLM`, `#MoE`, `#model routing`, `#open source`

---

<a id="item-14"></a>
## [OpenAI 伦理主管上任不到一年即离职](https://www.ft.com/content/e49dfb75-f841-4466-a577-f7aaff8779a0) ⭐️ 7.0/10

OpenAI 的伦理主管 Chloe Bakalar 在加入不到一年后离职。她的离开发生在 OpenAI AI 安全动荡时期之后，包括最近的黑客事件。 此次离职凸显了 AI 开发中伦理与商业优先事项之间的持续紧张关系，可能影响 OpenAI 对负责任 AI 的态度。这也引发了对大型科技公司 AI 治理角色稳定性的担忧。 Bakalar 此前在 Meta 担任首席伦理学家六年。在 OpenAI，她的工作重点包括道德模型开发、人机交互以及关于机器意识的辩论。

hackernews · ilamont · Aug 11, 12:23 · [社区讨论](https://news.ycombinator.com/item?id=49257160)

**背景**: AI 伦理是一个确保人工智能系统以公平、透明和负责任的方式开发和使用的领域。像 OpenAI 这样的公司因如何平衡伦理考量与商业利益而受到审查，伦理负责人的离职可能表明内部冲突。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aimagazine.com/news/why-did-openai-head-of-ethics-chloe-bakalar-leave">Why Did OpenAI ’s Head of Ethics Chloé Bakalar Leave? | AI Magazine</a></li>
<li><a href="https://finance.yahoo.com/technology/ai/articles/openai-head-ethics-leaves-start-223518680.html">OpenAI ’s head of ethics leaves start-up less than one year after joining</a></li>
<li><a href="https://www.tomsguide.com/ai/openais-head-of-ethics-just-quit-heres-why-chatgpt-users-should-pay-attention">OpenAI ’s head of ethics just quit — here’s why... | Tom's Guide</a></li>

</ul>
</details>

**社区讨论**: 社区评论对 AI 伦理工作的诚意表示怀疑，一些人认为伦理部门常被视为公关噱头。其他人推测 Bakalar 的离职可能不仅仅是伦理与利润的简单对立，并预测未来会有关于大型 AI 公司的揭秘书籍。

**标签**: `#AI ethics`, `#OpenAI`, `#AI governance`, `#industry news`

---

<a id="item-15"></a>
## [用笔式绘图机制作全息图，巧妙类比橄榄油](https://blog.jordan.matelsky.com/Penplotter-holography/) ⭐️ 7.0/10

一篇博客文章演示了如何使用笔式绘图机制作全息图，介绍了一种新颖的 DIY 方法。作者用橄榄油和指纹的类比来解释其背后的原理。 该项目使全息摄影对爱好者和创意编程者更加平易近人，融合了艺术与科学。它可能激发更多在低成本全息制作和教育演示方面的实验。 该技术可能涉及在表面上绘制精细线条以产生衍射图案，类似于磨损全息术。绘图机的精度至关重要，作者建议可能的改进，例如用针代替笔。

hackernews · DemiGuru · Aug 11, 18:51 · [社区讨论](https://news.ycombinator.com/item?id=49262811)

**背景**: 全息摄影是一种记录和重建光场以创建三维图像的技术。传统全息图需要激光干涉，但像磨损全息术这样的简单方法可以通过在表面划出细线来产生可见的全息效果。笔式绘图机是计算机控制的设备，可以绘制精确的图案，因此适合此用途。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=V7z7BAZdt2M">PHOTOGRAPHY BASICS in 10 MINUTES - YouTube</a></li>
<li><a href="https://www.domestika.org/">Online courses for creative professionals | Domestika</a></li>
<li><a href="https://id.pinterest.com/ideas/photography-basics-for-beginners-pdf/896968556385/">Photography Basics for Beginners Pdf</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该项目为“老式互联网”风格的乐趣，并欣赏橄榄油类比的清晰性。他们还分享了相关资源，如磨损全息术和 Steve Mould 的视频，并提出了技术改进建议，如使用压电扫描仪实现更精细的运动。

**标签**: `#holography`, `#pen plotter`, `#DIY`, `#optics`, `#creative coding`

---

<a id="item-16"></a>
## [伦敦地铁启动实时面部识别试验](https://www.btp.police.uk/news/btp/news/england/btp-expands-live-facial-recognition-lfr-trial-into-london-underground-stations/) ⭐️ 7.0/10

英国交通警察已将实时面部识别（LFR）试验扩展到伦敦地铁站，摄像头于 2026 年 8 月 11 日在维多利亚站启用，此前已在伦敦桥站进行了初步试点。这项为期六个月的试验旨在识别被通缉的严重犯罪者。 这项试验引发了重大的隐私和公民自由担忧，因为它能够在公共交通系统中对通勤者进行持续监控。其结果可能影响面部识别技术在英国未来的部署，并为其他国家树立先例。 该试验由英国交通警察进行，并包含严格的保障措施，官员称其“具有针对性且相称”。这是英国政府就面部识别法律框架进行更广泛咨询的一部分，目前该领域缺乏具体立法。

hackernews · BlueBerry2001 · Aug 11, 09:40 · [社区讨论](https://news.ycombinator.com/item?id=49255496)

**背景**: 实时面部识别（LFR）利用摄像头实时扫描人脸，并与通缉名单进行比对。在英国，此类技术的法律基础仍在发展中，信息专员办公室（ICO）为合法部署设定了条件。此次试验之前，警方已在公共活动中使用 LFR，但在伦敦地铁中的应用标志着日常监控达到了新的水平。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.co.uk/news/articles/c07r0gvgjxyo">Facial recognition cameras to be trialled at London Tube stations</a></li>
<li><a href="https://metro.co.uk/2026/08/11/live-facial-recognition-cameras-deployed-london-tube-stations-today-29348878/">Live facial recognition cameras deployed at London ... | Metro News</a></li>
<li><a href="https://shuftipro.com/blog/facial-recognition-uk/">Facial Recognition in UK : Legal Framework & Compliance | Shufti</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了强烈反对，用户指出隐私侵犯，并将英国比作“奥威尔式社会”。一些人认为，非接触式支付已经破坏了匿名出行，而另一些人则质疑试验的目的，指出它很可能导致进一步的监控，而不是对公民自由权衡进行真正的评估。

**标签**: `#surveillance`, `#privacy`, `#facial recognition`, `#civil liberties`, `#UK`

---

<a id="item-17"></a>
## [Apple Silicon macOS 虚拟机修复显著提升 llama.cpp 推理速度](https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md) ⭐️ 7.0/10

trycua 的一篇博客文章详细说明了如何通过修复 Apple Silicon 上 macOS 虚拟机中的内核选择，大幅提升 llama.cpp 的推理速度，与标准虚拟机相比，处理速度提升 11.08 倍，令牌生成速度提升 16.36 倍。 这一优化对于在 macOS 虚拟机中运行 LLM 工作负载的开发者具有重要意义，表明正确的内核选择可以带来显著的性能提升。同时，它也凸显了理解 Virtualization.framework 等虚拟化框架对于在 Apple Silicon 上进行 AI 推理的重要性。 该修复专门针对 Virtualization.framework 虚拟机中的内核选择问题，并非通用的 llama.cpp 加速。性能提升源于虚拟机报告了保守的 Metal 能力配置文件，导致 llama.cpp 选择了次优内核；修复后，llama.cpp 能够使用更好的内核。

hackernews · frabonacci · Aug 11, 14:50 · [社区讨论](https://news.ycombinator.com/item?id=49259339)

**背景**: Apple 的 Virtualization.framework 允许 macOS 虚拟机在 Apple Silicon 上运行，并使用由主机 Apple GPU 支持的虚拟 GPU。然而，虚拟 GPU 报告了保守的 Metal 能力配置文件，这可能导致 llama.cpp 等框架选择次优内核。这篇博客文章展示了一种通过修正内核选择来提升性能的解决方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/trycua/cua/blob/main/blog/gpu-passthrough-macos-vms.md">cua/blog/ gpu - passthrough - macos -vms.md at main · trycua/cua</a></li>
<li><a href="https://techxplainator.com/docker-mac-gpu-guide/">Why Docker Can’t Use macOS GPUs —And What to Do Instead...</a></li>

</ul>
</details>

**社区讨论**: 社区评论澄清了该加速仅适用于 Virtualization.framework 虚拟机，并非通用的 llama.cpp 改进。用户还质疑为什么 Virtualization.framework 会暴露较低的 Metal 配置文件，并对 M5 Pro+ 神经加速器等未来硬件进行了推测。

**标签**: `#llama.cpp`, `#Apple Silicon`, `#macOS VMs`, `#GPU passthrough`, `#LLM inference`

---

<a id="item-18"></a>
## [OpenAI 测试在 ChatGPT 中投放广告以维持免费服务](https://openai.com/index/testing-ads-in-chatgpt) ⭐️ 7.0/10

OpenAI 宣布开始在 ChatGPT 中测试广告，旨在支持免费版服务。广告将明确标注，OpenAI 强调广告不会影响回答的独立性，同时实施严格的隐私保护和用户控制。 此举意义重大，因为它标志着 OpenAI 在旗舰产品变现方式上的重大转变，可能影响用户体验，并为 AI 聊天机器人广告树立先例。它可能影响整个 AI 行业的商业模式，并引发关于隐私以及免费访问与商业化之间平衡的讨论。 该公告未明确时间表或广告的具体形式，但强调了明确标注、答案独立性、严格的隐私保护和用户控制。OpenAI 尚未透露哪些用户会看到广告以及广告如何定向，细节有待进一步公布。

rss · OpenAI Blog · Aug 11, 10:00

**背景**: ChatGPT 是 OpenAI 开发的广泛使用的 AI 聊天机器人，免费版是其受欢迎的关键因素。通过广告变现是免费服务的常见策略，但引发了关于用户体验和数据隐私的担忧。OpenAI 的做法旨在通过确保透明度和用户控制来解决这些问题。

**标签**: `#OpenAI`, `#ChatGPT`, `#advertising`, `#monetization`, `#privacy`

---

<a id="item-19"></a>
## [OpenAI Daybreak 模型现已在 AWS Bedrock 上可用](https://openai.com/index/daybreak-models-are-now-available-on-aws) ⭐️ 7.0/10

OpenAI 的 Daybreak 网络安全模型现已在 AWS 上通过 Amazon Bedrock 提供，支持企业安全工作流。此次集成将先进的 AI 驱动安全能力带给 AWS 客户。 OpenAI 与 AWS 的合作标志着向企业提供专业网络安全 AI 的重要一步，可能增强威胁检测与响应能力。这凸显了将 AI 嵌入云原生安全运营的日益增长的趋势。 Daybreak 模型包括用于防御工作流的 Daybreak Blue 和用于进攻性安全测试的 Daybreak Red，其中 GPT-5.6-Cyber 通过 Daybreak Red 提供。在 Amazon Bedrock 上的可用性允许与 AWS 原生安全服务和企业工作流集成。

rss · OpenAI Blog · Aug 11, 10:00

**背景**: Amazon Bedrock 是一项托管服务，使组织能够使用基础模型构建生成式 AI 应用。OpenAI 的 Daybreak 计划于 2026 年 5 月启动，推出了专门应对防御和进攻性安全挑战的网络安全模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/">Expanding Daybreak as the Cyber Defense Window Narrows | OpenAI</a></li>
<li><a href="https://aws.amazon.com/bedrock/">Amazon Bedrock – Build genAI applications and agents at production...</a></li>
<li><a href="https://cryptobriefing.com/openai-daybreak-cybersecurity-models/">OpenAI unveils Daybreak Blue and Daybreak Red cybersecurity ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Cybersecurity`, `#AWS`, `#OpenAI`, `#Enterprise`

---

<a id="item-20"></a>
## [无无损文本转换：Sophie Alpert 的 AI 写作政策](https://simonwillison.net/2026/Aug/11/there-are-no-lossless-transformations-of-natural-language-text/#atom-everything) ⭐️ 7.0/10

Clay 公司的工程师 Sophie Alpert 发布了一份关于 AI 写作可接受使用的内部政策，指出自然语言文本不存在无损转换。该政策强调工程师必须对自己文档中的每一句话和每一个观点负责，并且 AI 辅助的改写不可避免地会改变原意。 该政策为使用 LLM 的工程师和技术作家提供了一个清晰的伦理和实践框架，解决了 AI 辅助写作中的责任问题和信息丢失问题。它可能会影响组织处理 AI 生成内容的方式，促进透明度和人工监督。 该政策简洁明了，支持其自身的建议，并于 2026 年 6 月 25 日在 Sophie 的博客上分享。它也在 Hacker News 上引发了讨论，表明社区对此感兴趣。核心规则是作者必须能够解释他们发布的每一行内容，并且 AI 重写应被视为有损转换。

rss · Simon Willison · Aug 11, 23:48

**背景**: 大型语言模型（LLM）越来越多地被用于辅助写作，但在改写文本时可能会微妙地改变原意。Sophie Alpert 是一位知名工程师，曾在 Meta 工作并为 React 做出贡献，这为她的政策增添了可信度。该政策回应了专业环境中对 AI 生成内容日益增长的担忧，强调作者必须保持对工作的所有权和理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sophiebits.com/2026/06/25/there-are-no-lossless-transformations-of-natural-language-text">There are no lossless transformations of natural - language text</a></li>
<li><a href="https://news.ycombinator.com/item?id=48980425">There are no lossless transformations of natural - language text</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论可能包含赞同和争论，一些人称赞政策的清晰性，而另一些人则质疑在所有情况下避免 AI 辅助的可行性。有些人可能会争辩说，如果谨慎使用，AI 可以在不丢失意义的情况下帮助提高清晰度，而另一些人则强调人类责任的重要性。

**标签**: `#AI writing`, `#LLM`, `#engineering culture`, `#documentation`, `#ethics`

---

<a id="item-21"></a>
## [开源权重模型 Glimmer 和 Spark 承诺在单张 RTX 3090 上实现个人 AI](https://www.latent.space/p/ainews-muse-glimmer-and-spark-open) ⭐️ 7.0/10

该新闻介绍了两个开源权重 AI 模型 Glimmer 和 Spark，其中 Glimmer 能够在单个 RTX 3090 GPU 上运行。这标志着向可访问的个人 AI 迈出了一步。 该新闻简短且缺乏技术细节，但关键点是 Glimmer 适合在单个 RTX 3090 上运行，该显卡具有 24GB 显存。这表明该模型针对内存效率进行了优化。

rss · Latent Space · Aug 11, 05:16

**背景**: 开源权重 AI 模型提供对模型权重的访问，允许用户托管和调整它们，但并非完全开源，因为训练数据和代码可能被保留。RTX 3090 是基于 NVIDIA Ampere 架构的高端消费级 GPU，以其 24GB 显存而闻名，适合本地运行大型模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/open-weight-ai-what-we-finally-opened-bonnet-nicolas-pistorio-n3ulf">Open - weight AI : what if we finally opened the bonnet ?</a></li>
<li><a href="https://wccftechas.pages.dev/posts/elsa-unveils-its-geforce-rtx-3090-lc-graphics-card-features-aio-360mm-cooling-with-custom-alphacool-waterblock-for-2275-us/">Elsa Unveils Its Geforce Rtx 3090 Lc Graphics Card Features Aio...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Open Source`, `#Models`, `#Hardware`

---