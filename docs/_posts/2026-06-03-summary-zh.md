---
layout: default
title: "Horizon Summary: 2026-06-03 (ZH)"
date: 2026-06-03
lang: zh
---

> From 71 items, 22 important content pieces were selected

---

1. [Verizon VoLTE 缺少 IPsec 完整性保护](#item-1) ⭐️ 9.0/10
2. [特朗普签署缩减版人工智能行政令，要求自愿审查](#item-2) ⭐️ 8.0/10
3. [Anthropic 将 Project Glasswing 扩展至 15 个国家](#item-3) ⭐️ 8.0/10
4. [KDE Plasma 最后一个 X11 版本标志 Wayland 里程碑](#item-4) ⭐️ 8.0/10
5. [Scholar Sidekick：验证真实 DOI 是否对应错误论文](#item-5) ⭐️ 8.0/10
6. [Collibra Agent 认证绕过与路径遍历致远程代码执行](#item-6) ⭐️ 8.0/10
7. [OpenAI Codex 扩展至通用知识工作](#item-7) ⭐️ 8.0/10
8. [微软发布 MAI-Thinking-1 和 MAI-Code-1-Flash 大语言模型](#item-8) ⭐️ 8.0/10
9. [GitHub 应对 AI 代理激增的计划](#item-9) ⭐️ 8.0/10
10. [NVIDIA 发布 Cosmos 3、Nemotron 3 Ultra 和 RTX Spark](#item-10) ⭐️ 8.0/10
11. [llama.cpp b9470 优化 Hexagon DSP 性能](#item-11) ⭐️ 7.0/10
12. [llama.cpp b9468 新增实时推理中断功能](#item-12) ⭐️ 7.0/10
13. [CT 扫描揭示比亚迪垂直整合工程细节](#item-13) ⭐️ 7.0/10
14. [徒步之旅揭示西雅图监控基础设施](#item-14) ⭐️ 7.0/10
15. [Adafruit 收到 Flux.ai 律师函](#item-15) ⭐️ 7.0/10
16. [即将进入你浏览器的广告卡特尔](#item-16) ⭐️ 7.0/10
17. [为什么你应该爱上 systemd 定时器](#item-17) ⭐️ 7.0/10
18. [AI 从单条提示构建出《英雄联盟》克隆版](#item-18) ⭐️ 7.0/10
19. [CISA 将两个已遭利用的漏洞加入 KEV 目录](#item-19) ⭐️ 7.0/10
20. [Appsmith SQL 自动补全 XSS 漏洞已在 v2.1 中修复](#item-20) ⭐️ 7.0/10
21. [Travelers 携手 OpenAI 部署 AI 理赔助手](#item-21) ⭐️ 7.0/10
22. [Datasette Agent MicroPython Alpha 实现安全代码执行](#item-22) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Verizon VoLTE 缺少 IPsec 完整性保护](https://kb.cert.org/vuls/id/615987) ⭐️ 9.0/10

CERT/CC 披露，Verizon 的 VoLTE 部署缺少对 SIP 信令的 IPsec 完整性保护，允许路径上的攻击者拦截和修改通话及消息。该漏洞编号为 CVE-2026-10629。 该漏洞破坏了 VoLTE 的核心安全假设，影响数百万 Verizon 用户，可实现通话劫持、伪造和紧急呼叫错误路由。它凸显了移动网络安全中的关键缺陷，需要立即修复。 观察到 SIP 信令（包括注册和呼叫建立）缺少 Security-Client、Security-Server 或 Security-Verify 头部，且未检测到 ESP 封装流量。Verizon 最初承认了该问题，但后来停止了协调，修复情况未得到确认。

rss · CERT CC Vulnerability Notes · Jun 2, 14:27

**背景**: VoLTE（长期演进语音承载）依赖 IP 多媒体子系统（IMS）在 LTE 网络上传输语音通话。根据 3GPP 标准，用户设备与网络之间的 SIP 信令必须在 IMS AKA 认证后使用 IPsec ESP 进行保护。缺少此保护，攻击者可以不被察觉地操纵信令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/List_of_SIP_response_codes">List of SIP response codes - Wikipedia</a></li>
<li><a href="https://datatracker.ietf.org/doc/html/rfc3329">RFC 3329 - Security Mechanism Agreement for the Session ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/IP_Multimedia_Subsystem">IP Multimedia Subsystem - Wikipedia</a></li>

</ul>
</details>

**标签**: `#security`, `#VoLTE`, `#vulnerability`, `#CERT`, `#Verizon`

---

<a id="item-2"></a>
## [特朗普签署缩减版人工智能行政令，要求自愿审查](https://www.politico.com/news/2026/06/02/trump-signs-downsized-ai-order-00946389) ⭐️ 8.0/10

2026 年 6 月 2 日，特朗普总统签署了一项行政令，要求人工智能公司在公开发布强大新模型前，自愿提交给政府进行 30 天审查；此前的草案曾提议 90 天，最终版本有所缩减。 该行政令标志着美国从之前对 AI 监管的不干预态度转向，可能为未来的监管树立先例，同时平衡创新与国家安全关切。 该行政令明确声明不授权强制许可或预先批准，并指示司法部对滥用 AI 的个人提起刑事诉讼。

hackernews · _alternator_ · Jun 2, 16:40 · [社区讨论](https://news.ycombinator.com/item?id=48372628)

**背景**: AI 监管一直是一个有争议的问题，争论焦点在于如何在不扼杀创新的前提下确保安全。该行政令的早期草案遭到行业官员反对，他们认为 90 天审查过于繁重。最终版本强调自愿合作，避免强制要求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deadline.com/2026/06/trump-ai-executive-order-1236938859/">Trump Signs AI Executive Order That Includes Review Period For...</a></li>
<li><a href="https://www.nytimes.com/2026/06/02/technology/trump-executive-order-ai.html">Trump Signs Executive Order Seeking Oversight of A . I . Models</a></li>
<li><a href="https://www.theguardian.com/us-news/2026/jun/02/trump-executive-order-ai-voluntary-review">Trump signs executive order seeking early access to new AI releases</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了怀疑态度：一些人认为该行政令缺乏实质内容，而另一些人担心这是迈向强制限制的一步，可能损害开源开发。评论者还质疑自愿审查在实践中如何运作。

**标签**: `#AI regulation`, `#executive order`, `#AI safety`, `#policy`, `#open-source`

---

<a id="item-3"></a>
## [Anthropic 将 Project Glasswing 扩展至 15 个国家](https://www.anthropic.com/news/expanding-project-glasswing) ⭐️ 8.0/10

Anthropic 正在通过 Project Glasswing 将其 Claude Mythos 模型扩展到 15 个国家的关键基础设施，为选定的技术提供商提供早期访问权限以加强网络安全防御。 此次扩展是将先进 AI 部署到现实世界安全领域的重要一步，但也引发了对误报、计算能力限制以及大规模监控伦理影响的担忧。 Claude Mythos 模型被认为过于强大，因此 Anthropic 决定不公开发布，而是以“道德部署”的名义私下提供。社区报告显示，该系统可能产生大量误报，给安全团队带来噪音。

hackernews · surprisetalk · Jun 2, 13:15 · [社区讨论](https://news.ycombinator.com/item?id=48369863)

**背景**: Project Glasswing 是 Anthropic 的一项计划，旨在利用其前沿 AI 模型（特别是 Claude Mythos）保护关键软件。Claude Mythos 是 Anthropic 最先进也最具争议的模型，经过训练可识别代码中的漏洞。该项目为选定的提供商提供早期访问权限，以测试和部署该模型用于网络安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing : Securing critical software for the AI era \ Anthropic</a></li>
<li><a href="https://www.bbc.com/news/articles/crk1py1jgzko">What is Anthopic's Claude Mythos and what risks does it pose?</a></li>
<li><a href="https://www.linkedin.com/pulse/anthropic-launches-project-glasswing-after-claude-mythos-alvaro-cuba-ie40e">Anthropic launches Project Glasswing after Claude Mythos finds...</a></li>

</ul>
</details>

**社区讨论**: 社区评论褒贬不一：一些用户报告该模型产生过多误报，带来噪音而非价值。其他人怀疑 Anthropic 正利用安全担忧来掩盖计算能力限制，同时也有关于大规模监控和企业访问关键基础设施的伦理担忧被提出。

**标签**: `#AI safety`, `#critical infrastructure`, `#Anthropic`, `#Claude`, `#security`

---

<a id="item-4"></a>
## [KDE Plasma 最后一个 X11 版本标志 Wayland 里程碑](https://blog.davidedmundson.co.uk/blog/596/) ⭐️ 8.0/10

KDE Plasma 正在准备其最后一个支持 X11 显示服务器的版本，预计在 2027 年初完全过渡到仅使用 Wayland。 这标志着 Linux 桌面向 Wayland 迁移的一个重要里程碑，提升了性能和安全性，但也引发了对依赖 X11 功能的辅助工具的担忧。 KDE 应用程序在其他桌面环境下仍可在 X11 上运行，但 Plasma 本身将放弃 X11 支持。已知问题包括缺少窗口位置保存和按应用设置键盘布局。

hackernews · jandeboevrie · Jun 2, 14:16 · [社区讨论](https://news.ycombinator.com/item?id=48370588)

**背景**: X11 是 Linux 的旧版显示服务器协议，而 Wayland 是其现代替代品，旨在提供更好的安全性和性能。KDE Plasma 是一个流行的桌面环境，多年来一直在逐步过渡到 Wayland。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.davidedmundson.co.uk/blog/596/">EX-11: Prepping for Plasma ’s Last X 11 -Supported Release – David...</a></li>
<li><a href="https://www.phoronix.com/news/KDE-Plasma-2025-Wayland-Success">KDE Plasma 's Wayland Transition "Nears Completion" In... - Phoron...</a></li>
<li><a href="https://biggo.com/news/202509140722_Wayland_Accessibility_Crisis">Wayland 's Accessibility Crisis: Voice Control Tools Still... - BigGo News</a></li>

</ul>
</details>

**社区讨论**: 社区评论既肯定了进展，也指出了未解决的问题：一些用户称赞 KDE 在 Wayland 上的流畅体验和功能增加，而另一些用户则对缺失的辅助功能支持（如 Talon 等语音控制工具）以及窗口置顶等功能表示不满。

**标签**: `#KDE`, `#Wayland`, `#X11`, `#Linux Desktop`, `#Accessibility`

---

<a id="item-5"></a>
## [Scholar Sidekick：验证真实 DOI 是否对应错误论文](https://scholar-sidekick.com/tools/citation-verifier) ⭐️ 8.0/10

Scholar Sidekick 是一款免费网络工具，新增了引文验证功能，可检查 DOI、PMID 或 arXiv ID 是否确实指向参考文献中声称的论文标题，解决了 AI 幻觉中标识符真实但引文伪造的常见问题。 该工具直接应对学术出版中日益严重的问题：AI 生成的引文具有真实标识符但标题错误，最近《柳叶刀》研究发现每 277 篇 PubMed Central 文章中就有 1 篇存在此问题。通过提供简单的自动检查，它帮助研究人员和编辑维护引文完整性，而不必仅依赖容易出错的人工验证。 在对 350 条引文的测试中，该工具正确识别了所有 37 条伪造参考文献，但错误标记了 285 条真实引文中的 5 条（误报率 1.8%）。该工具解析标识符，将参考文献中的标题与返回的元数据进行比较，但不评估被引论文是否支持论点——这仍需人工判断。

rss · Hacker News Show HN · Jun 2, 22:29

**背景**: 数字对象标识符（DOI）是一种持久标识符，用于唯一标识学术文章、书籍等对象。点击 DOI 时，它应解析到正确的文章。然而，AI 语言模型有时会生成包含真实 DOI 但标题伪造的引文，这种模式被称为“真实 DOI，错误论文”幻觉。2025 年 5 月 Topaz 等人在《柳叶刀》上发表的研究分析了 250 万篇 PubMed Central 文章，估计每 277 篇中就有 1 篇包含伪造引文，其中许多表现出这种模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_object_identifier">Digital object identifier - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/posts/salimhayek_more-disclaimers-will-not-stop-ai-from-fabricating-activity-7458712981137399808-k1KZ">AI-generated citations in scientific papers on the rise | LinkedIn</a></li>
<li><a href="https://timesofindia.indiatimes.com/india/new-study-detected-at-least-1-4l-in-2025-alone-2nd-paper-in-lancet-flags-issue-in-biomed-journals/articleshow/131321024.cms">New study detected at least 1.4L in 2025 alone; 2nd paper in Lancet ...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的唯一评论在提供的数据中不可见，因此无法总结社区讨论。

**标签**: `#citation verification`, `#AI hallucination`, `#academic integrity`, `#research tools`

---

<a id="item-6"></a>
## [Collibra Agent 认证绕过与路径遍历致远程代码执行](https://kb.cert.org/vuls/id/873170) ⭐️ 8.0/10

CERT/CC 披露了 Collibra Agent 中的两个漏洞（CVE-2026-10622 和 CVE-2026-10621），未认证攻击者可通过上传特制 ZIP 压缩包，将认证绕过与 Zip Slip 路径遍历漏洞串联，实现远程代码执行。 Collibra 是广泛使用的企业数据治理平台，这些漏洞可被远程未认证攻击者利用，可能导致安装 Web Shell、访问敏感数据或在网络内横向移动。 认证绕过（CVE-2026-10622）暴露了 /rest/* 下的特权 REST 端点，而路径遍历（CVE-2026-10621）发生在通过 POST /rest/restore 解压 ZIP 时，允许将任意文件写入 Web 可访问目录，实现基于 JSP 的远程代码执行。

rss · CERT CC Vulnerability Notes · Jun 2, 13:54

**背景**: Collibra Agent 是 Collibra Platform（SaaS）和 Collibra Platform Self-Hosted（本地部署）的一个组件，作为独立服务运行。Zip Slip 是一种常见漏洞，解压时未验证文件路径，允许使用 ../ 等遍历序列将文件写入预期目录之外。认证绕过发生在 REST 端点未正确实施访问控制时。

**标签**: `#Collibra`, `#RCE`, `#authentication bypass`, `#path traversal`, `#CERT`

---

<a id="item-7"></a>
## [OpenAI Codex 扩展至通用知识工作](https://openai.com/index/codex-for-knowledge-work) ⭐️ 8.0/10

OpenAI 宣布 Codex 正从编程助手演变为面向知识工作的通用生产力工具，支持 AI 驱动的研究、数据分析、工作流自动化和内容创作。 这标志着 AI 生产力工具的重大转变，可能改变各行业知识工作者利用 AI 处理编程之外复杂任务的方式。 该公告基于一份名为《知识工作的下一个时代》的报告，强调了 Codex 在研究、数据分析、自动化和内容创作方面的能力。Codex 于 2025 年 10 月全面可用，并最近增加了为单一任务生成多个解决方案的功能。

rss · OpenAI Blog · Jun 2, 02:00

**背景**: Codex 最初是作为基于 OpenAI GPT 模型的 AI 编程助手推出的，旨在帮助开发者编写代码。其向知识工作的扩展反映了 AI 工具从专业领域向通用生产力应用发展的更广泛趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.sina.com.cn/tech/roll/2025-06-17/doc-infaismr6882515.shtml">OpenAI Codex 人工智能编程工具推出新功能：可一次生成多个方案</a></li>
<li><a href="https://docs.zyhorg.cn/docs/Command-List/OpenAI/OpenAI-Codex/">OpenAI Codex 现已全面可用 | UNHub DOCS</a></li>

</ul>
</details>

**标签**: `#AI`, `#productivity`, `#OpenAI`, `#Codex`, `#knowledge work`

---

<a id="item-8"></a>
## [微软发布 MAI-Thinking-1 和 MAI-Code-1-Flash 大语言模型](https://simonwillison.net/2026/Jun/2/microsofts-new-models/#atom-everything) ⭐️ 8.0/10

微软宣布推出两款新的文本大语言模型：MAI-Thinking-1（350 亿参数推理模型）和 MAI-Code-1-Flash（50 亿参数代码模型，专为 GitHub Copilot 和 VS Code 构建）。 这些模型以远少于典型大模型的参数数量实现了有竞争力的性能，有望降低 AI 推理成本并提高可及性。 MAI-Thinking-1 从头开始使用干净、商业许可的数据进行训练，未从第三方模型进行蒸馏，在盲测中优于 Sonnet 4.6。

rss · Simon Willison · Jun 2, 22:21

**背景**: 大语言模型通常需要数十亿参数和昂贵的硬件才能运行。具有竞争性能的小型模型可以降低使用门槛和运营成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://microsoft.ai/news/introducing-mai-thinking-1/">Introducing MAI - Thinking - 1 | Microsoft AI</a></li>
<li><a href="https://microsoft.ai/news/introducingmai-code-1-flash/">Introducing MAI - Code - 1 - Flash | Microsoft AI</a></li>
<li><a href="https://www.baseten.co/library/mai-thinking-1/">MAI - Thinking - 1 | Model library</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#LLM`, `#AI models`, `#reasoning`, `#code generation`

---

<a id="item-9"></a>
## [GitHub 应对 AI 代理激增的计划](https://www.latent.space/p/github) ⭐️ 8.0/10

GitHub 正在制定一项策略，以应对其平台上 AI 代理使用量的快速增长，解决基础设施压力，并规划代理式编码的未来方向。 这很重要，因为 AI 代理正在改变开发者工作流程，GitHub 的做法将影响数百万开发者与 AI 工具的交互方式，并可能为代理式编码平台设定行业标准。 该计划应对了代理式编码激增带来的压力，代理式编码指的是 AI 代理自主编写和管理代码，与简单的“氛围编码”方法不同。

rss · Latent Space · Jun 2, 16:48

**背景**: GitHub Copilot 开创了 AI 辅助编程的先河，但能够自主规划、构建和交付软件的 AI 代理的兴起，给平台的可扩展性和可靠性带来了新的挑战。代理式编码涉及代理通过对话与开发者协作完成复杂任务，超越了简单的代码补全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/agentic-coding-real-heres-mental-model-every-leader-engineer-arbab-engsc">Agentic Coding Is Real. Here's the Mental Model Every Leader...</a></li>
<li><a href="https://mohewedy.medium.com/agentic-coding-is-not-vibe-coding-88a98a0e76c3">Agentic Coding is not Vibe Coding | by Mohammed Hewedy | Medium</a></li>

</ul>
</details>

**标签**: `#GitHub`, `#AI agents`, `#Copilot`, `#developer tools`, `#platform evolution`

---

<a id="item-10"></a>
## [NVIDIA 发布 Cosmos 3、Nemotron 3 Ultra 和 RTX Spark](https://www.latent.space/p/ainews-nvidia-cosmos-3-nemotron-3) ⭐️ 8.0/10

NVIDIA 宣布了三项重大 AI 发布：面向物理 AI 的开放全模态模型 Cosmos 3；包含 Ultra、Super 和 Nano 三种规模的 Nemotron 3 开放模型系列；以及用于 AI 驱动 Windows PC 的新芯片 RTX Spark。 这些发布巩固了 NVIDIA 在 AI 硬件和模型领域的地位，使开发者能够构建更强大的机器人、代理式 AI 和个人 AI 助手，有望加速 AI 在机器人和边缘计算领域的应用。 Cosmos 3 以 Cosmos 3 Super 和 Cosmos 3 Nano 的形式在 Hugging Face 上提供，并集成了 Diffusers。Nemotron 3 Ultra 具有强大的代理、推理和对话能力。RTX Spark 专为轻薄笔记本电脑和小型台式机设计，可全天候运行个人 AI 代理。

rss · Latent Space · Jun 2, 03:28

**背景**: 物理 AI 指与物理世界交互的 AI 系统，如机器人和自动驾驶汽车。像 Cosmos 3 这样的基础模型是大型预训练模型，可针对特定任务进行微调。Nemotron 是 NVIDIA 的开放语言模型系列。RTX Spark 是面向 AI PC 的新芯片类别，结合了 NVIDIA 的 GPU 技术与 MediaTek 的低功耗设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/cosmos-3-physical-ai-open-world-foundation-model/">How Cosmos 3 Helps Physical AI Think Before It Acts | NVIDIA Blog</a></li>
<li><a href="https://research.nvidia.com/labs/nemotron/Nemotron-3/">NVIDIA Nemotron 3 Family of Models - NVIDIA Nemotron</a></li>
<li><a href="https://www.nvidia.com/en-us/products/rtx-spark/">Slim Laptops & Small Desktops | NVIDIA RTX Spark</a></li>

</ul>
</details>

**社区讨论**: 源材料中未提供社区评论。

**标签**: `#NVIDIA`, `#AI`, `#hardware`, `#models`, `#announcement`

---

<a id="item-11"></a>
## [llama.cpp b9470 优化 Hexagon DSP 性能](https://github.com/ggml-org/llama.cpp/releases/tag/b9470) ⭐️ 7.0/10

llama.cpp 版本 b9470 引入了针对 Hexagon DSP 的矩阵乘法（MUL_MAT、MUL_MAT_ID）、flash attention 和 RMS 归一化的优化，并对 Qualcomm 设备进行了常规清理和改进。 这些优化显著提升了 Qualcomm 设备上的推理性能，使大型语言模型在移动和边缘平台上更加高效。这扩大了本地 AI 推理的硬件覆盖范围。 更新包括 Hexagon 上对 F32 * F32 矩阵乘法的支持、流水线与非流水线模式以提升性能，以及为 GATED_DELTA_NET 添加的 DMA 预取/双缓冲。还修复了融合逻辑中的一个 bug，该 bug 在某些源为空时影响了张量顺序。

github · github-actions[bot] · Jun 2, 09:35

**背景**: Hexagon DSP 是集成在 Qualcomm Snapdragon SoC 中的数字信号处理器，专为高效的设备端 AI 处理而设计。Flash attention 是一种减少内存使用并加速 Transformer 中注意力计算的技术。RMS 归一化是 LLaMA 等现代 LLM 中常用的归一化方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pcworld.com/article/423191/qualcomm-announces-snapdragon-820s-new-hexagon-dsp-for-always-on-sensors-image-processing.html">Qualcomm announces Snapdragon 820's new Hexagon DSP for...</a></li>
<li><a href="https://gordicaleksa.medium.com/eli5-flash-attention-5c44017022ad">ELI5: FlashAttention. Step by step explanation of how one of | Medium</a></li>
<li><a href="https://dev.to/yagyaraj_sharma_6cd410179/title-understanding-layernorm-and-rms-norm-in-transformer-models-3ahl">Title: Understanding LayerNorm and RMS Norm in... - DEV Community</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#Hexagon DSP`, `#performance optimization`, `#machine learning`, `#inference`

---

<a id="item-12"></a>
## [llama.cpp b9468 新增实时推理中断功能](https://github.com/ggml-org/llama.cpp/releases/tag/b9468) ⭐️ 7.0/10

llama.cpp 版本 b9468 新增了一个控制端点，通过向 /v1/chat/completions/control 发送包含 reasoning_end 等操作的 POST 请求，可以在生成过程中实时中断 LLM 的推理过程。 该功能使交互式应用能够动态管理推理预算，提升了实时 LLM 交互中的用户控制能力和响应速度。 控制端点使用完成 ID（而非槽 ID）以避免 TOCTOU 竞态条件，WebUI 现在基于新的 isReasoning 状态仅在推理阶段显示跳过按钮。

github · github-actions[bot] · Jun 2, 05:53

**背景**: llama.cpp 是一个流行的开源 LLM 推理引擎，能在消费级硬件上高效运行。推理预算允许模型在生成最终答案前分配有限数量的 token 用于“思考”。此版本基于早期手动触发预算强制的工作构建。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.runlocalai.co/pulse/gh-ggml-org-llama-cpp-b9468">llama.cpp ships b9468 · Pulse | RunLocalAI</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#LLM`, `#inference`, `#reasoning`, `#control`

---

<a id="item-13"></a>
## [CT 扫描揭示比亚迪垂直整合工程细节](https://www.lumafield.com/scan-of-the-month/byd) ⭐️ 7.0/10

Lumafield 发布了比亚迪汽车零部件的高分辨率 CT 扫描图像，包括钥匙、电驱动单元和电池包，展示了该公司垂直整合的制造方式。 这些扫描提供了罕见的工程视角，展示了比亚迪如何通过自产关键零部件获得成本和性能优势，对特斯拉和福特等竞争对手构成挑战。 CT 扫描揭示了复杂的内部结构，例如钥匙中的机械备用钥匙机构和电驱动单元的紧凑设计，凸显了比亚迪的制造设计理念。

hackernews · viasfo · Jun 2, 20:30 · [社区讨论](https://news.ycombinator.com/item?id=48375824)

**背景**: 垂直整合意味着公司控制从原材料到成品的多个生产阶段。比亚迪最初是电池制造商，现在约 75%的汽车零部件为自产，而福特仅为 25%。CT 扫描是一种无损检测技术，用于检查制造零件的内部特征。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://evboosters.com/ev-charging-news/the-blueprint-of-an-ev-empire-how-byd-built-global-dominance-through-vertical-integration/">The blueprint of an EV empire: how BYD built global... | EVBoosters</a></li>
<li><a href="https://www.automotivemanufacturingsolutions.com/electrification/from-battery-maker-to-ev-leader-byds-strategic-rise/46813.article">BYD ’s strategy to overtake Tesla in EV production globally | Automotive...</a></li>
<li><a href="https://www.or3d.co.uk/knowledge-base/the-basics-ct-scanning/">The Basics: CT Scanning - OR3D</a></li>

</ul>
</details>

**社区讨论**: 评论者提供了修正和额外背景：一位比亚迪车主指出钥匙的机械备用钥匙并非铰接，而是通过卡扣拉出。另一人对比了比亚迪（年产 460 万辆）、特斯拉（160 万辆）和福特（440 万辆）的生产规模。还分享了相关电动汽车拆解视频链接。

**标签**: `#EV`, `#manufacturing`, `#engineering`, `#BYD`, `#CT scanning`

---

<a id="item-14"></a>
## [徒步之旅揭示西雅图监控基础设施](https://coveillance.org/a-walking-tour-of-surveillance-infrastructure-in-seattle/) ⭐️ 7.0/10

一次详细的徒步之旅记录了西雅图无处不在的监控基础设施，包括摄像头和传感器，并讨论了它们的社会影响。 这项工作凸显了城市监控日益常态化及其对隐私和公民自由的影响，引发了关于安全与自由之间权衡的讨论。 这次徒步之旅涵盖了各种类型的监控技术，例如具有不同“观看方式”的摄像头，这些方式强制执行社会规范，并指出检察官通常需要视频证据才能定罪。

hackernews · eustoria · Jun 2, 13:24 · [社区讨论](https://news.ycombinator.com/item?id=48369980)

**背景**: 城市监控系统已从简单的闭路电视演变为具有实时视频分析的多传感器平台。“反向监控”（从公众视角记录）的概念作为自上而下监控的对立面也具有相关性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sousveillance">Sousveillance - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/pulse/edition-18-urban-surveillance-age-dissent-modern-peter-nmdoe">Edition 18 - Urban Surveillance in the Age of Dissent: Navigating...</a></li>

</ul>
</details>

**社区讨论**: 评论表达了不同的观点：一些人认为监控是保障安全的必要手段，而另一些人则批评自由的侵蚀以及描述监控系统时使用的晦涩语言。少数人分享了个人经历，说明法庭上需要视频证据。

**标签**: `#surveillance`, `#privacy`, `#civil liberties`, `#urban technology`, `#Seattle`

---

<a id="item-15"></a>
## [Adafruit 收到 Flux.ai 律师函](https://blog.adafruit.com/) ⭐️ 7.0/10

开源硬件巨头 Adafruit 收到了由 Fenwick 律师事务所代表 Flux.ai 发出的律师函，Flux.ai 是一家提供 AI 驱动的 PCB 设计工具的初创公司。该函件很可能与 Adafruit 计划发布的关于 Flux.ai 产品及商业实践的评测或讨论有关。 这一事件凸显了成熟的开源社区与获得融资的初创公司之间的紧张关系，尤其是在知识产权和公平批评方面。它可能为企业在面对负面评价时的应对方式树立先例，并影响社区关于言论自由的规范。 Adafruit 的创始人'ladyada'表示愿意公开解决此事，可能通过播客形式。社区评论显示用户对 Flux.ai 产品普遍不满，指出其代币成本高、性能差，并暗示律师函可能是为了压制批评。

hackernews · semanser · Jun 2, 10:00 · [社区讨论](https://news.ycombinator.com/item?id=48368121)

**背景**: 律师函是一种正式的法律通知，要求收件人采取或停止特定行为，通常是诉讼的前奏。Adafruit 是开源硬件社区中知名的公司，而 Flux.ai 是一家最近获得 Bain Capital 等投资的初创公司。社区怀疑 Adafruit 正在准备一篇关于 Flux.ai 的 AI PCB 设计工具的批评性评测。

**社区讨论**: 社区一边倒地支持 Adafruit，许多用户分享了使用 Flux.ai 产品的负面体验，称其昂贵且效果不佳。一些人认为 Flux.ai 的法律行动是为了掩盖产品质量问题和用户投诉。还有用户呼吁通过公开讨论透明地解决此事。

**标签**: `#open-source`, `#legal`, `#hardware`, `#startup`, `#community`

---

<a id="item-16"></a>
## [即将进入你浏览器的广告卡特尔](https://blog.zgp.org/the-advertising-cartel-coming-to-your-web-browser/) ⭐️ 7.0/10

一篇批判性分析指出，谷歌、Meta 和苹果等科技巨头提出的浏览器广告标准可能会巩固基于监控的广告模式，同时削弱独立广告网络。 如果实施，这些标准可能会集中控制在线广告，减少竞争，并迫使用户进入一个双层隐私系统，其中浏览器内置的跟踪功能不受严格同意要求的约束。 该提案缺少关于权限或同意的部分，并创建了一个双轨系统，其中第三方广告功能必须遵守隐私法规，而浏览器自身的跟踪仅需用户选择退出。

hackernews · speckx · Jun 2, 19:39 · [社区讨论](https://news.ycombinator.com/item?id=48375175)

**背景**: 监控资本主义指的是企业将个人数据商品化以获取利润。基于浏览器的广告标准旨在用新的 API 取代第三方 Cookie，但批评者认为它们可能会巩固大型科技公司的统治地位并限制用户隐私。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Surveillance_capitalism">Surveillance capitalism - Wikipedia</a></li>
<li><a href="https://acceptableads.com/">Acceptable Ads | Light and nonintrusive advertising</a></li>

</ul>
</details>

**社区讨论**: 评论意见分歧：一些人认为该提案是大型科技公司的权力争夺，而另一些人则视其为隐私改进。一位评论者暗示作者是假装关心隐私的广告商，另一位则指出谷歌、Meta 和苹果在“隐私”功能上达成一致是一个积极信号。

**标签**: `#privacy`, `#advertising`, `#web browsers`, `#big tech`, `#surveillance capitalism`

---

<a id="item-17"></a>
## [为什么你应该爱上 systemd 定时器](https://blog.tjll.net/you-dont-love-systemd-timers-enough/) ⭐️ 7.0/10

一篇博客文章认为，在 Linux 上调度任务时，systemd 定时器优于 cron，强调了其应对系统启动时间的弹性和可预测执行等优势。 这很重要，因为许多 Linux 用户和管理员仍依赖 cron，而 systemd 定时器与现代基于 systemd 的系统集成更好，提高了可靠性和可调试性。 systemd 定时器可以在系统启动后运行错过的任务，支持日历事件和单调定时器，并与 journalctl 集成进行日志记录。文章指出 cron 模糊的 PATH 设置可能导致问题。

hackernews · yacin · Jun 2, 09:34 · [社区讨论](https://news.ycombinator.com/item?id=48367904)

**背景**: Cron 是类 Unix 系统上传统的任务调度器，在指定时间运行命令。systemd 定时器是较新的替代方案，随 systemd 一起提供，systemd 是大多数现代 Linux 发行版使用的初始化系统。定时器提供更多功能，如依赖处理和日志记录。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wiki.archlinux.org/title/Systemd/Timers">systemd / Timers - ArchWiki</a></li>
<li><a href="https://medium.com/@zaturdayapril/systemd-timer-in-linux-0ac6f6cd60a2">Systemd timer in linux. Systemd Timer | by Voravit... | Medium</a></li>
<li><a href="https://www.linode.com/docs/guides/what-is-systemd/">What is systemd ? | Linode Docs</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了使用 systemd 定时器的积极体验，例如应对启动时间的弹性和通过 journalctl 更易调试。一些人讨论了 cron 的 PATH 处理，另一些人提供了实际用例，如自动备份和打印机维护。

**标签**: `#systemd`, `#cron`, `#Linux`, `#scheduling`, `#devops`

---

<a id="item-18"></a>
## [AI 从单条提示构建出《英雄联盟》克隆版](https://lmaomoba.com/) ⭐️ 7.0/10

一位开发者使用 Anthropic 的 Claude Opus 4.8 模型，通过单条提示词生成了一个名为 LMAO 的、功能完整的网页版《英雄联盟》克隆游戏，随后利用子代理和 Ultracode Workflows 进行了迭代改进。 这展示了前沿 AI 模型从极简输入生成复杂、多组件软件的卓越能力，可能降低游戏原型设计和快速开发的门槛。 该游戏使用 React/TypeScript 作为 Web 前端，Canvas 进行渲染，PartyKit 提供多人服务器支持，并采用 Claude Code 与 Opus 4.8 作为 AI 工具链。开发者还利用 Ultracode Workflows 编排子代理进行性能优化和平衡性调整。

rss · Hacker News Show HN · Jun 2, 21:10

**背景**: Claude Opus 4.8 是 Anthropic 于 2026 年 5 月发布的最新旗舰 AI 模型，在 Artificial Analysis Intelligence Index 中以 61.4 分位居榜首，超越了 GPT-5.5。Ultracode Workflows 是 Claude Code 中的一项功能，允许通过脚本编排数十到数百个子代理，从而实现复杂的多步骤任务。《英雄联盟》是一款流行的多人在线战斗竞技场（MOBA）游戏，该项目在网页浏览器中复现了其核心机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.atlascloud.ai/models/anthropic/claude-opus-4.8">Claude Opus 4 . 8 API by ANTHROPIC - Competitive... | Atlas Cloud</a></li>
<li><a href="https://lushbinary.com/blog/claude-opus-4-8-developer-guide-benchmarks-pricing-dynamic-workflows/">Claude Opus 4 . 8 Developer Guide: Benchmarks & Pricing | Lushbinary</a></li>
<li><a href="https://code.claude.com/docs/en/workflows">Orchestrate subagents at scale with dynamic workflows</a></li>

</ul>
</details>

**标签**: `#AI`, `#game development`, `#LLM`, `#Opus 4.8`, `#show HN`

---

<a id="item-19"></a>
## [CISA 将两个已遭利用的漏洞加入 KEV 目录](https://www.cisa.gov/news-events/alerts/2026/06/02/cisa-adds-two-known-exploited-vulnerabilities-catalog) ⭐️ 7.0/10

CISA 已将 CVE-2022-0492（Linux 内核身份验证不当）和 CVE-2025-48595（Android 框架整数溢出）加入其已知被利用漏洞（KEV）目录，原因是存在活跃利用证据。 这些漏洞对联邦企业构成重大风险，是常见的攻击途径；KEV 目录要求联邦机构进行修复，并为所有组织提供关键的优先级指导。 CVE-2022-0492 是 Linux 内核的身份验证不当漏洞，而 CVE-2025-48595 是 Android 框架中的整数溢出漏洞，影响版本 14、15、16 和 16-qpr2，可导致本地权限提升。

rss · CISA Cybersecurity Advisories · Jun 2, 12:00

**背景**: KEV 目录由 CISA 的《约束性操作指令 22-01》建立，列出了已知被利用且风险重大的漏洞。联邦民事行政分支机构必须在规定期限内修复所列漏洞。虽然该指令仅适用于联邦机构，但 CISA 敦促所有组织在补丁管理中优先处理这些漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog">Known Exploited Vulnerabilities Catalog | CISA</a></li>
<li><a href="https://nvd.nist.gov/vuln/detail/CVE-2025-48595">NVD - CVE - 2025 - 48595</a></li>
<li><a href="https://www.helpnetsecurity.com/2026/06/02/android-vulnerability-exploited-cve-2025-48595/">Google fixes actively exploited Android vulnerability ( CVE - 2025 - 48595 )</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#CISA`, `#vulnerability`, `#KEV`, `#exploitation`

---

<a id="item-20"></a>
## [Appsmith SQL 自动补全 XSS 漏洞已在 v2.1 中修复](https://kb.cert.org/vuls/id/265691) ⭐️ 7.0/10

在 Appsmith 基于 CodeMirror 的 SQL 查询编辑器自动补全渲染器中发现了一个存储型跨站脚本（XSS）漏洞（CVE-2026-7299），可导致任意 JavaScript 执行。该漏洞已在 Appsmith 2.1 版本中修复。 该漏洞允许具有开发者权限的攻击者通过恶意数据库对象名称注入持久性 XSS，导致任何使用同一数据源的工作区成员遭受会话劫持、权限提升或凭据窃取。Appsmith 是一个广泛使用的开源低代码平台，因此这是一个高影响力的安全问题。 该漏洞需要经过身份验证的开发者账户才能利用，并且影响的是自动补全渲染器——它在通过 innerHTML 渲染数据库对象名称之前未能进行清理。修复程序已包含在 Appsmith 2.1 版本中，用户应立即更新。

rss · CERT CC Vulnerability Notes · Jun 2, 14:06

**背景**: Appsmith 是一个开源低代码平台，允许开发者通过 UI 构建器和数据库集成来创建内部工具、仪表盘和应用程序。存储型 XSS 是一种跨站脚本攻击，恶意脚本被永久存储在服务器上，当用户访问受影响内容时执行。SQL 编辑器中的自动补全功能使用 CodeMirror（一个流行的代码编辑器组件）来建议表和列名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kb.cert.org/vuls/id/265691">VU#265691 - Appsmiths SQL Query autocomplete renderer contains...</a></li>
<li><a href="https://juejin.cn/post/7347911052174393383">AppSmith 它到底好用吗? 目前来看 AppSmith ...</a></li>
<li><a href="https://www.huluohu.com/posts/950/">Appsmith ...</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#XSS`, `#Appsmith`, `#CVE`

---

<a id="item-21"></a>
## [Travelers 携手 OpenAI 部署 AI 理赔助手](https://openai.com/index/travelers) ⭐️ 7.0/10

Travelers 部署了基于 OpenAI 构建的 AI 理赔助手，用于引导客户完成理赔流程、提供全天候支持，并在高峰期扩展运营能力。 这标志着大型语言模型在保险行业的重要实际应用，展示了 AI 如何提升客户服务效率和运营可扩展性，同时也验证了 OpenAI 技术在企业级关键任务部署中的可行性。 该理赔助手旨在处理理赔指导并提供全天候支持，帮助 Travelers 在不按比例增加人员的情况下应对需求高峰。该系统已在美国全国范围内部署。

rss · OpenAI Blog · Jun 2, 12:00

**背景**: Travelers 是美国领先的财产和意外伤害保险公司。理赔是关键的客户接触点，但通常给客户带来压力，传统上需要人工代理。通过利用 OpenAI 的大型语言模型，Travelers 旨在简化流程并改善客户体验。

**标签**: `#AI`, `#Insurance`, `#Customer Service`, `#OpenAI`, `#LLM`

---

<a id="item-22"></a>
## [Datasette Agent MicroPython Alpha 实现安全代码执行](https://simonwillison.net/2026/Jun/2/datasette-agent-micropython/#atom-everything) ⭐️ 7.0/10

Simon Willison 发布了 datasette-agent-micropython 0.1a0，这是一个 alpha 包，将 MicroPython 的 WebAssembly 构建与 wasmtime 封装器捆绑在一起，以安全执行 Datasette Agent 生成的 Python 代码。该版本旨在让 GPT-5.5 生成并运行 Python 代码，而不会突破沙箱。 这种方法提供了一种轻量级且安全的方式来执行 LLM 生成的 Python 代码，这对代理式 AI 工作流至关重要。通过使用 WebAssembly 沙箱，它在保持性能的同时降低了恶意代码执行的风险。 该包使用 MicroPython 的定制 WASM 构建，并通过 WebAssembly 运行时 wasmtime 执行代码。当前版本为 0.1a0，表示早期 alpha 阶段，作者报告称 GPT-5.5 迄今未能逃逸沙箱。

rss · Simon Willison · Jun 2, 19:28

**背景**: WebAssembly (WASM) 是一种在沙箱环境中运行的二进制指令格式，非常适合安全代码执行。MicroPython 是 Python 3 的精简实现，专为微控制器和受限系统设计。将两者结合可以在受限环境中运行 Python 代码，这对于安全执行由 GPT-5.5 等大型语言模型 (LLM) 生成的代码非常有用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/collaborne-engineering/building-a-secure-code-sandbox-for-llms-with-webassembly-bdd91a835f23">Building a Secure Code Sandbox for LLMs with WebAssembly | Medium</a></li>
<li><a href="https://developer.nvidia.com/blog/sandboxing-agentic-ai-workflows-with-webassembly/">Sandboxing Agentic AI Workflows with WebAssembly</a></li>
<li><a href="https://til.simonwillison.net/webassembly/python-in-a-wasm-sandbox">Run Python code in a WebAssembly sandbox | Simon Willison’s TILs</a></li>

</ul>
</details>

**标签**: `#datasette`, `#python`, `#sandboxing`, `#webassembly`

---