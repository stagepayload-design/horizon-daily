---
layout: default
title: "Horizon Summary: 2026-09-03 (ZH)"
date: 2026-09-03
lang: zh
---

> From 43 items, 15 important content pieces were selected

---

1. [SonicWall SMA1000 关键漏洞遭积极利用实现远程代码执行](#item-1) ⭐️ 9.0/10
2. [Claude Fable/Mythos 5.1：新 SOTA 模型，缓存价格降低 75%，输出令牌增加 70%](#item-2) ⭐️ 9.0/10
3. [Meta 的 Muse Spark 1.3 在 DeepSWE 上夺冠，且价格低廉](#item-3) ⭐️ 8.0/10
4. [谷歌发布 Gemini 3.8 Flash 和 Flash Cyber](#item-4) ⭐️ 8.0/10
5. [谷歌击败美国强制出售广告技术业务的诉讼](#item-5) ⭐️ 8.0/10
6. [报告：AI 搜索工具引用批量生成的“最佳软件”页面](#item-6) ⭐️ 8.0/10
7. [全球最大暗物质探测器记录到单个异常事件](#item-7) ⭐️ 8.0/10
8. [Cisco Nexus 9000 Silicon One 交换机存在严重远程代码执行漏洞](#item-8) ⭐️ 8.0/10
9. [Paint.NET 借助 AI 重写 Direct2D 以支持 Wine](#item-9) ⭐️ 8.0/10
10. [Fable 5.1 世界建模演示引发赞誉与质疑](#item-10) ⭐️ 7.0/10
11. [Mistral 团队版默认开启数据训练，引发隐私担忧](#item-11) ⭐️ 7.0/10
12. [LWN 宣布订阅价格调整，社区反响积极](#item-12) ⭐️ 7.0/10
13. [CISA 将七个已利用漏洞加入 KEV 目录](#item-13) ⭐️ 7.0/10
14. [Cisco Secure Email S/MIME 解密漏洞可导致明文泄露](#item-14) ⭐️ 7.0/10
15. [Anthropic 更新 Claude 系统提示，限制歌词复制](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [SonicWall SMA1000 关键漏洞遭积极利用实现远程代码执行](https://www.rapid7.com/blog/post/etr-critical-sonicwall-sma1000-vulnerabilities-cve-2026-83548-cve-2026-83549-exploited-in-the-wild) ⭐️ 9.0/10

2026 年 9 月 1 日，SonicWall 披露了两个影响 SMA1000 设备且已被积极利用的漏洞（CVE-2026-83548 和 CVE-2026-83549）。这两个漏洞可被链式利用，实现未认证的远程代码执行（RCE）。 这些漏洞影响广泛部署的企业安全远程访问网关，积极利用对组织构成严重风险。成功利用可能使攻击者完全控制设备，可能导致数据泄露或网络受损。 CVE-2026-83548 是一个预认证 SSRF 漏洞，CVSS 评分为 10.0；CVE-2026-83549 是 Appliance Management Console 中的高危 OS 命令注入漏洞（CVSS 7.8）。受影响型号包括 SMA1000 6210、7210 和 8200v；修复版本为 12.4.3-03526 和 12.5.0-02952。

rss · Rapid7 Emergent Threat Response · Sep 2, 16:58

**背景**: SonicWall SMA1000 设备是企业安全远程访问网关，为员工提供对内部应用程序的访问。Work Place 接口可能暴露于互联网，使这些漏洞尤为危险。SSRF 允许攻击者从服务器发起请求，而命令注入则能执行任意操作系统命令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sonicwall.com/support/notices/product-notice-sma-1000-series-affected-by-multiple-vulnerabilities-snwlid-2026-0016/kA1VN000002AXmQ0AW">Product Notice: SMA 1000 Series affected by Multiple Vulnerabilities ...</a></li>
<li><a href="https://www.infosecurity-magazine.com/news/hackers-chain-sonicwall-zeroday/">Hackers Chain Two New SonicWall Zero-Day... - Infosecurity Magazine</a></li>
<li><a href="https://cybersecuritynews.com/sonicwall-remote-code-execution-vulnerabilities/">Critical SonicWall Remote Code Execution Vulnerabilities Actively...</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#CVE`, `#SonicWall`, `#RCE`

---

<a id="item-2"></a>
## [Claude Fable/Mythos 5.1：新 SOTA 模型，缓存价格降低 75%，输出令牌增加 70%](https://www.latent.space/p/ainews-claude-fablemythos-51-new) ⭐️ 9.0/10

Anthropic 发布了 Claude Fable 5.1 和 Claude Mythos 5.1，这是一个新的最先进模型系列，提示缓存读取价格降低了 75%，输出令牌增加了 70%。 此次发布树立了新的性能基准，并大幅降低了缓存密集型工作负载的成本，可能加速智能体和长期运行 AI 应用的采用。价格降低和更高的输出能力可能改变 AI 模型提供商之间的竞争格局。 Claude Fable 5.1 和 Mythos 5.1 是同一个底层模型，仅在安全干预上有所不同。基础价格仍为每百万令牌$10/$50，但缓存读取从每百万令牌$1 降至$0.25，输出令牌相比 Fable 5 增加了 70%。

rss · Latent Space · Sep 2, 07:46

**背景**: Claude 模型是 Anthropic 的大型语言模型系列。提示缓存允许开发者存储常用上下文，从而降低成本和延迟。'Fable'和'Mythos'名称指同一模型的不同安全调优变体，其中 Mythos 在某些任务上具有较少的限制性安全措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-fable-and-mythos-5-1">Introducing Claude Fable 5 . 1 and Claude Mythos 5 . 1 \ Anthropic</a></li>
<li><a href="https://cursor.com/docs/models/claude-fable-5-1">Claude Fable 5 . 1 | Cursor Docs</a></li>
<li><a href="https://ofox.ai/blog/claude-fable-5-1-vs-fable-5-vs-opus-5-2026/">Fable 5.1 vs Fable 5 vs Opus 5: It's All in the Cache</a></li>

</ul>
</details>

**标签**: `#AI`, `#Claude`, `#Model Release`, `#Pricing`, `#SOTA`

---

<a id="item-3"></a>
## [Meta 的 Muse Spark 1.3 在 DeepSWE 上夺冠，且价格低廉](https://developer.meta.com/ai/models/muse-spark/) ⭐️ 8.0/10

Meta 发布了 Muse Spark 1.3，这是一款多模态推理模型，在 DeepSWE 基准测试中取得了 75.4 的最高分，超越了此前的领先者。其定价为每百万输入 token 1.25 美元，每百万输出 token 4.25 美元，上下文窗口为 1,048,576 个 token。 此次发布标志着 Meta 在 AI 领域的快速进步，其模型以极低的成本媲美前沿系统，可能推动整个行业价格下降。开发者将受益于一个价格实惠且性能出色的选择，用于智能体（agentic）和编码工作流。 Muse Spark 1.3 是五个月内的第四次发布，在长时程协作、多任务处理和指令遵循方面相比 1.2 版本有所改进。它可通过 Meta 的 API 以及 OpenRouter 等平台使用，并提供“贡献者”（contributor）定价层级，允许 Meta 使用用户数据进行训练，从而降低费用。

hackernews · bvaldivielso · Sep 2, 19:35 · [社区讨论](https://news.ycombinator.com/item?id=49541256)

**背景**: DeepSWE 是一个无污染（contamination-free）的基准测试，旨在测试真实的仓库级工程行为，其任务从零开始编写，涵盖 91 个代码仓库和 5 种语言。Muse Spark 是 Meta 专有的多模态推理模型系列，面向长时间运行的智能体、多智能体和编码工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepswe.net/">DeepSWE Benchmark : GPT vs Claude for Agentic Coding</a></li>
<li><a href="https://openrouter.ai/meta/muse-spark-1.3">Muse Spark 1 . 3 - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://artificialanalysis.ai/articles/muse-spark-1-3">Muse Spark 1 . 3 : Meta reaches the frontier | Artificial Analysis</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体积极，用户称赞该模型的质量和低成本。一些人分享了实际示例，如生成 SVG，并指出相比 1.2 版本的改进。其他人强调了有竞争力的定价以及对训练数据使用的明确区分，不过也有评论者开玩笑地提到了 Meta 的诉讼。

**标签**: `#Meta`, `#AI model`, `#Muse Spark`, `#benchmarks`, `#machine learning`

---

<a id="item-4"></a>
## [谷歌发布 Gemini 3.8 Flash 和 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) ⭐️ 8.0/10

谷歌发布了 Gemini 3.8 Flash 和 Gemini 3.8 Flash Cyber，这是一款快速且能力强大的模型，在基准测试中名列前茅，并以低成本 HTML 生成著称。Cyber 版本通过 Fairwind 计划向受信任的防御者开放，用于漏洞发现和自动修补。 此次发布延续了谷歌在 Flash 模型上的快速迭代，以低成本提供高性能，可能颠覆 AI 模型市场，并惠及需要高效编码和多模态分析的开发者。Cyber 版本针对关键的网络安全需求，可能增强自动化防御能力。 Gemini 3.8 Flash 在 Artificial Analysis 上的智能得分为 59，与 Opus 5 medium 相当，并在 DeepSwe 上排名第一。它支持音频和视频输入，而 OpenAI 和 Anthropic 的旗舰模型仅支持图像，且成本低至 1.8 美分即可在 13 秒内完成 HTML 生成任务。

hackernews · bratao · Sep 2, 15:12 · [社区讨论](https://news.ycombinator.com/item?id=49537553)

**背景**: Gemini 3.8 Flash 是谷歌 Gemini 模型家族的一员，旨在提供速度和效率，同时在基准测试中保持强劲性能。Flash 系列面向需要经济高效 AI 进行编码、多模态分析和智能体任务的开发者。Cyber 版本专为网络安全设计，内部测试显示在 20 种编程语言的漏洞任务中成功率超过 70%。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-8-flash/">Gemini 3 . 8 Flash - Model Card — Google DeepMind</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/">Introducing Gemini 3 . 8 Flash and 3 . 8 Flash Cyber</a></li>
<li><a href="https://www.datacamp.com/blog/gemini-3-8-flash-cyber">Gemini 3 . 8 Flash : Features, Benchmarks, and Pricing | DataCamp</a></li>

</ul>
</details>

**社区讨论**: simonw 等社区成员称赞该模型的速度和 HTML/JavaScript 生成能力，并分享了低成本输出的示例。其他人指出其在基准测试中的强劲表现，有些人将其与 Opus 5 进行有利比较，但也有少数人对低设置下的思考水平回归表示担忧。

**标签**: `#AI`, `#Google`, `#Gemini`, `#model release`, `#benchmarks`

---

<a id="item-5"></a>
## [谷歌击败美国强制出售广告技术业务的诉讼](https://www.nytimes.com/2026/09/02/technology/google-ad-tech-remedies.html) ⭐️ 8.0/10

2026 年 9 月 2 日，美国法院裁定政府试图强制谷歌剥离部分广告技术业务的行为败诉，这对谷歌来说是一次重大的法律胜利。该裁决意味着谷歌不会因其广告技术业务而被拆分。 这一决定对科技行业的反垄断执法具有重要意义，为未来针对主导平台的拆分尝试树立了先例。它也对广告技术市场产生影响，尽管该业务收入下滑，谷歌仍是关键参与者。 谷歌的广告技术业务去年创造了 300 亿美元的收入，约占 Alphabet 总收入的 8%，但其利润贡献估计不到 1%。该业务收入已连续 16 个季度下滑，导致一些人质疑此案的重要性。

hackernews · donohoe · Sep 2, 14:46 · [社区讨论](https://news.ycombinator.com/item?id=49537131)

**背景**: 美国司法部于 2023 年 1 月提起诉讼，指控谷歌通过将其广告交易平台与发布商广告服务器捆绑等方式非法垄断广告技术市场。政府试图迫使谷歌出售其广告管理套件。此案与早先的搜索垄断案不同，后者也做出了对谷歌不利的裁决。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/c3674nl7g74o">Google has illegal advertising monopoly, judge rules</a></li>
<li><a href="https://www.straitstimes.com/world/united-states/us-targets-googles-online-ad-business-monopoly-in-latest-big-tech-lawsuit">US targets Google 's online ad business monopoly in latest Big Tech ...</a></li>
<li><a href="https://www.adexchanger.com/platforms/its-happening-the-doj-is-suing-google-for-alleged-monopolistic-ad-tech-practices/">The DOJ Is Suing Google For Alleged Monopolistic Ad Tech Practices</a></li>

</ul>
</details>

**社区讨论**: 评论者对拆分公司比合并更难表示不满，有人建议对垄断企业征收累进税。其他人质疑此案的相关性，因为广告技术业务利润占比很小，还有人指出谷歌受益于有利的法律环境。

**标签**: `#antitrust`, `#Google`, `#ad tech`, `#regulation`, `#tech policy`

---

<a id="item-6"></a>
## [报告：AI 搜索工具引用批量生成的“最佳软件”页面](https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/) ⭐️ 8.0/10

Trellner 的一份报告揭示，三个网站生成了 215,128 个“最佳软件”页面，这些页面现被 Perplexity 等 AI 工具引用。这凸显了 AI 生成推荐中的系统性问题。 这很重要，因为 AI 搜索引擎越来越多地被用于决策，而引用低质量、程序化生成的内容会削弱对 AI 推荐的信任。它影响了依赖这些工具获取准确信息的用户，并引发了对 AI 驱动搜索完整性的担忧。 报告特别指出了三个网站，它们可能使用 AI 或模板批量生成这些页面。Perplexity 作为一个 AI 驱动的答案引擎，将这些页面作为来源引用，这可能会误导寻求真实软件推荐的用户。

hackernews · jakobgreenfeld · Sep 2, 13:59 · [社区讨论](https://news.ycombinator.com/item?id=49536375)

**背景**: AI 内容农场已成为一个日益严重的问题，这些低质量、AI 生成的文章旨在赚取广告收入。这些农场利用可能未充分审查来源的搜索引擎和 AI 工具。Perplexity 是一个 AI 答案引擎，提供带引用的实时答案，但其对此类内容的依赖引发了对来源质量的质疑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://futurism.com/content-farms-ai">People Are Spinning Up Content Farms Using AI</a></li>
<li><a href="https://www.perplexity.ai/">Perplexity</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了个人经历，指出 AI 工具偏爱 AI 生成的内容并编造信息，例如推荐不存在的地方。有人指出模型缺乏来源怀疑精神，引用了由被比较公司托管的比较页面。总体情绪对当前 AI 引用做法持批评态度，但乐观认为问题将得到解决。

**标签**: `#AI`, `#Search`, `#SEO`, `#Content Quality`, `#LLM`

---

<a id="item-7"></a>
## [全球最大暗物质探测器记录到单个异常事件](https://www.science.org/content/article/world-s-biggest-dark-matter-detector-spots-single-weird-particle) ⭐️ 8.0/10

全球最大的暗物质探测器 LUX-ZEPLIN（LZ）记录到了一个不寻常的单个粒子事件，物理学家们正在对此进行调查。研究团队发表了他们的发现，但警告说现在断言这是发现还为时过早。 这一异常现象可能暗示着超越标准模型的新物理，包括暗物质相互作用，并在粒子物理学界引起了极大关注。虽然尚未得到证实，但它可能为未来的研究和数据收集工作提供指导。 该事件是在南达科他州一个前金矿中的桑福德地下研究设施深处探测到的。LZ 探测器使用液态氙时间投影室，周围有多层屏蔽层，以识别和减少虚假信号。

hackernews · randycupertino · Sep 2, 13:40 · [社区讨论](https://news.ycombinator.com/item?id=49536079)

**背景**: 暗物质是一种不可见的物质形式，约占宇宙质量的 85%，但它不发光也不吸收光，只能通过引力效应被探测到。LZ 实验旨在寻找弱相互作用大质量粒子（WIMP），这是暗物质的主要候选者，通过寻找氙核上的稀有散射事件来实现。探测器位于地下 1480 米处，以屏蔽宇宙射线和其他背景干扰。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LZ_experiment">LZ experiment - Wikipedia</a></li>
<li><a href="https://lz.lbl.gov/detector/">Detector | The LZ Dark Matter Experiment</a></li>
<li><a href="https://lz.lbl.gov/">The LZ Dark Matter Experiment | The status and science of the LZ ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论反映了谨慎的兴趣。一位评论者称赞了预印本中分析的彻底性，指出粒子物理学史上充满了 3 西格玛的“发现”，但随着更多数据的出现而消失。另一位强调了单个事件解释的挑战，还有一位对暗物质的存在表示怀疑，认为当前物理模型可能存在缺陷。

**标签**: `#dark matter`, `#particle physics`, `#LZ detector`, `#physics research`, `#anomaly detection`

---

<a id="item-8"></a>
## [Cisco Nexus 9000 Silicon One 交换机存在严重远程代码执行漏洞](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-n9k-s1-rce-EH8dEtr?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Cisco%20Nexus%209000%20Series%20Switches%20Silicon%20One%20Remote%20Code%20Execution%20Vulnerability%26vs_k=1) ⭐️ 8.0/10

Cisco 披露了 Nexus 9000 系列交换机 Silicon One 集成中的一个严重未认证远程代码执行漏洞（CVE-2026-20212）。该漏洞允许攻击者通过默认 L3 VRF 中暴露的 TCP 端口 43210 和 43211 以 root 权限执行代码。 该漏洞影响广泛部署的数据中心交换机，且无需认证即可利用，可能导致网络基础设施完全沦陷，因此十分严重。成功利用可能中断业务运营并导致数据泄露，受影响组织必须立即修补。 该漏洞源于默认 Layer 3 VRF 中可访问的 TCP 端口 43210 和 43211，使精心构造的输入能够以 root 权限执行。利用该漏洞还可能导致 S1HAL 进程崩溃，从而引发设备重载；Cisco 已发布软件更新和缓解措施。

rss · Cisco Security Advisories · Sep 2, 16:00

**背景**: Cisco Nexus 9000 系列交换机广泛用于数据中心，Silicon One 集成提供高性能转发能力。S1HAL 进程是管理 Silicon One 硬件的硬件抽象层组件，其崩溃可能导致交换机重载。默认 VRF 是所有 Layer 3 接口所在的路由上下文，除非分配到其他 VRF，默认 VRF 中的服务可能暴露于网络。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://feedly.com/cve/CVE-2026-20212">CVE-2026-20212 - Exploits & Severity - Feedly</a></li>
<li><a href="https://www.ajsnetworking.com/cisco-nexus-management-and-default-vrfs/">Cisco Nexus Management and Default VRFs - Anthony...</a></li>

</ul>
</details>

**标签**: `#Cisco`, `#security`, `#RCE`, `#network infrastructure`, `#vulnerability`

---

<a id="item-9"></a>
## [Paint.NET 借助 AI 重写 Direct2D 以支持 Wine](https://simonwillison.net/2026/Sep/2/rick-brewster/) ⭐️ 8.0/10

Paint.NET 开发者 Rick Brewster 宣布，他们内部从头开始、以洁净室逆向工程方式重写了 Direct2D，并在使用 /wine 参数时供 Paint.NET 在 Wine 上使用。这次重写总计 18 万行代码，主要由 AI 助手 Claude 编写。 这标志着 Windows 兼容性的一个重要里程碑，可能使 Paint.NET 能够通过 Wine 在 Linux 等平台上运行。同时，它也展示了 AI 在复杂逆向工程任务中的潜力，可能对兼容层和软件开发产生更广泛的影响。 这次重写包含在 PaintDotNet.Windows.Direct2D1.Managed.dll 中，并被描述为“氛围编码”（vibe coded），意味着它尚未经过彻底审查。Brewster 提到，他需要监督 Claude 以确保正确的资源管理，因为 Claude 最初遗漏了 COM 的 AddRef() 调用，他还纠正了一些糟糕的设计决策。

rss · Simon Willison · Sep 2, 05:50

**背景**: Direct2D 是一个基于 Direct3D 的硬件加速 2D 图形 API，许多 Windows 应用程序都使用它。Wine 是一个兼容层，通过转换 Windows 系统调用，使 Windows 应用程序能在 Linux 和其他 POSIX 系统上运行。洁净室逆向工程是一种在不侵犯版权的情况下重新创建设计的方法，通常由独立团队根据规格说明而非原始代码进行工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/D2D">D 2 D - Wikipedia</a></li>
<li><a href="https://www.winehq.org/">WineHQ - Run Windows applications on Linux, BSD, Solaris and macOS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Clean-room_design">Clean - room design - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Direct2D`, `#Wine`, `#AI-assisted development`, `#reverse engineering`, `#Paint.NET`

---

<a id="item-10"></a>
## [Fable 5.1 世界建模演示引发赞誉与质疑](https://github.com/PhiloLabs/fable51-worlds) ⭐️ 7.0/10

PhiloLabs 发布了 Fable 5.1 世界建模的演示，展示了 AI 生成的 3D 世界。该演示突出了模型创建详细环境的能力，但社区反馈指出了拓扑和纹理方面的局限性。 该演示展示了 AI 驱动的 3D 内容生成的快速进展，这可能对游戏开发和虚拟世界创建产生重大影响。然而，社区对实际可用性的担忧凸显了令人印象深刻的演示与生产就绪资产之间的差距。 社区成员指出，生成的模型对于简单几何体具有高多边形数量，且缺乏针对游戏引擎的优化。一些人建议使用该模型生成低多边形轮廓，并烘焙包含窗户、门等细节的纹理，而不是直接使用原始输出。

hackernews · surreal_ · Sep 2, 19:49 · [社区讨论](https://news.ycombinator.com/item?id=49541458)

**背景**: AI 世界建模是指使用机器学习模型从文本或其他输入生成 3D 环境。该领域正在快速发展，像 Roblox AI 和 Rosebud AI 这样的工具使用户能够从描述创建可玩的游戏。然而，生成干净的拓扑和可用的纹理仍然是 AI 生成资产的挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.animaticsassetstore.com/2024/02/02/5-easy-steps-to-resolve-topology-issues-in-3d-modeling/">5 Easy Steps to Resolve Topology Issues in... - Animatics Asset Store</a></li>
<li><a href="https://robloxai.net/">Roblox AI – AI Game Maker, Thumbnails & Icons</a></li>
<li><a href="https://rosebud.ai/ai-game-creator">Free AI Game Maker — Create Games Online | Rosebud AI</a></li>

</ul>
</details>

**社区讨论**: 社区情绪复杂：一些人觉得演示令人印象深刻，但质疑其在简单演示之外的实用价值，指出拓扑和纹理问题。其他人建议采用替代方法，如使用模型生成轮廓并烘焙纹理，并要求提供更多关于时间、成本和可靠性的细节。一位用户指出，Opus 5 效果相当且更便宜。

**标签**: `#AI`, `#3D modeling`, `#game development`, `#world generation`

---

<a id="item-11"></a>
## [Mistral 团队版默认开启数据训练，引发隐私担忧](https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training) ⭐️ 7.0/10

Mistral AI 已将其团队版默认设置为选择加入数据训练，这意味着除非用户手动关闭该设置，否则用户的输入和输出数据可能被用于模型改进。这一变化发生在一些组织为了获得更好的隐私控制而升级到团队版之后。 这一变化削弱了企业对 AI 服务的信任，因为组织通常根据隐私保证来选择供应商。它凸显了 AI 公司默认收集数据的行业趋势，这可能导致更严格的监管和注重隐私的客户的更多审查。 团队版此前提供带有中央隐私控制功能的组织仪表板，但更改后，中央禁用训练的功能可能已丢失或默认选择加入。用户仍可通过转到“设置”→“隐私”并关闭“允许 Mistral 使用您的数据进行模型改进”来选择退出，但这必须手动完成。

hackernews · teekert · Sep 2, 12:30 · [社区讨论](https://news.ycombinator.com/item?id=49535284)

**背景**: Mistral AI 是一家欧洲 AI 公司，提供多种服务层级，包括免费版、专业版和团队版。数据训练政策决定用户提示和输出是否用于改进 AI 模型。选择加入意味着默认使用数据，除非用户明确禁用；选择退出意味着默认不使用数据，除非用户明确启用。企业通常要求默认选择退出，以遵守数据保护法规并维护客户机密。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://freellm.net/providers/mistral-ai">Free Mistral AI API Key & Free Tier : Base URL, Rate... — freellm.net</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了对 AI 公司数据实践的普遍不信任，一些用户认为无论选择退出政策如何，公司都会对数据进行训练。其他人指出监控供应商变化的困难，以及通过“知识探测”检测未经授权数据使用并采取法律行动的潜力。一些用户还批评了新闻标题的编辑化，指出实际页面标题是一个问题。

**标签**: `#AI`, `#privacy`, `#data governance`, `#Mistral`, `#enterprise`

---

<a id="item-12"></a>
## [LWN 宣布订阅价格调整，社区反响积极](https://lwn.net/Articles/1090585/) ⭐️ 7.0/10

LWN.net 在一份致社区的说明中宣布了订阅价格的调整。这一公告引发了讨论，读者们纷纷表示支持其用户资助的模式。 LWN 是 Linux 社区中备受尊敬的技术出版物，其订阅模式对其独立性和质量至关重要。社区的积极回应凸显了读者对无广告、高质量技术新闻的重视。 公告未明确具体的新价格，但读者表示即使是最便宜的档位也愿意支付。一位读者指出，文章的 EPUB 格式是他们保持订阅的关键原因。

hackernews · rwky · Sep 2, 13:17 · [社区讨论](https://news.ycombinator.com/item?id=49535752)

**背景**: LWN.net 是一家长期报道 Linux 和自由软件的出版物，依靠读者订阅而非广告资助。这种模式使其能够保持编辑独立性和高质量内容。该网站自 1998 年运营以来，拥有忠实的读者群。

**社区讨论**: 评论者称赞 LWN 是信号质量最高的科技出版物之一，并将其质量归功于用户资助和不受广告商影响。一位读者将 LWN 视为其成功职业的基础，另一位建议使用更具描述性的标题以避免引起读者恐慌。还有读者表示希望其他领域也有类似出版物。

**标签**: `#LWN`, `#subscription`, `#community`, `#technical writing`, `#Linux`

---

<a id="item-13"></a>
## [CISA 将七个已利用漏洞加入 KEV 目录](https://www.cisa.gov/news-events/alerts/2026/09/02/cisa-adds-seven-known-exploited-vulnerabilities-catalog) ⭐️ 7.0/10

2026 年 9 月 2 日，CISA 将七个新被利用的漏洞添加到其已知被利用漏洞（KEV）目录中，包括 SQL 注入、HTTP 请求走私、操作系统命令注入和不当认证漏洞。这些漏洞影响 Sangoma Switchvox、Starlette、Kestra OSS、LiteLLM、JFrog Artifactory 和 SonicWall SMA1000 等产品。 此次更新对安全团队至关重要，因为它表明这些漏洞正被积极利用，需要立即修补以防止入侵。KEV 目录是优先修复的关键资源，尤其对 BOD 26-04 下的联邦机构而言，但所有组织都应重视这些新增项。 这七个 CVE 包括 CVE-2026-9586（Sangoma Switchvox SQL 注入，CVSS 9.3）、CVE-2026-48710（Starlette HTTP 请求走私）、CVE-2026-49869（Kestra OSS 操作系统命令注入）、CVE-2026-59822（LiteLLM 不当认证）、CVE-2026-82329（JFrog Artifactory 不当认证）以及 CVE-2026-83548/CVE-2026-83549（SonicWall SMA1000 SSRF 和操作系统命令注入）。CISA 鼓励各组织优先修复这些漏洞，并通过其 KEV 提名表提交其他被利用的漏洞。

rss · CISA Cybersecurity Advisories · Sep 2, 12:00

**背景**: KEV 目录是由 CISA 维护的已确认被积极利用的漏洞列表，旨在帮助组织优先修补。约束操作指令（BOD）26-04 要求联邦民事行政部门机构迅速修复 KEV 目录中列出的高风险漏洞，尤其是那些位于公开暴露资产上且可能授予完全控制权的漏洞。虽然 BOD 26-04 仅适用于联邦机构，但 CISA 建议所有组织采用基于风险的漏洞管理，并优先处理 KEV 漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://horizon3.ai/attack-research/disclosures/cve-2026-9586-sangoma-switchvox-rce/">CVE-2026-9586: Sangoma Switchvox RCE | Horizon3</a></li>
<li><a href="https://thehackernews.com/2026/09/attackers-exploit-critical-switchvox.html">Attackers Exploit Critical Switchvox Flaw to Deploy Reverse Shells...</a></li>
<li><a href="https://security.snyk.io/vuln/SNYK-PYTHON-STARLETTE-16881242">HTTP Request Smuggling in starlette | CVE-2026-48710 | Snyk</a></li>

</ul>
</details>

**标签**: `#CISA`, `#vulnerabilities`, `#security`, `#KEV`, `#exploits`

---

<a id="item-14"></a>
## [Cisco Secure Email S/MIME 解密漏洞可导致明文泄露](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-smime-disc-dzw4rEdY?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Cisco%20Secure%20Email%20Secure/Multipurpose%20Internet%20Mail%20Extensions%20Ciphertext%20Decryption%20Vulnerabilities%26vs_k=1) ⭐️ 7.0/10

Cisco 披露了 Cisco Secure Email 的 S/MIME 解密功能中的多个漏洞，编号为 CVE-2026-20354 和 CVE-2026-20355，这些漏洞可能允许未经认证的远程攻击者通过中间人攻击恢复加密邮件中的明文。该公告的安全影响评级为中等，且没有可用的变通方案。 这很重要，因为 Cisco Secure Email 在企业环境中广泛用于保护敏感通信，而这些漏洞破坏了 S/MIME 加密的机密性保证。依赖该产品满足合规要求或进行安全数据交换的组织需要评估其风险，并及时应用可用的补丁。 这些漏洞源于对消息完整性验证不足，攻击者可以拦截并修改邮件网关之间的流量。目前没有变通方案，该公告的 CVSS 评分为 7.0（满分 10 分），表明风险较高。

rss · Cisco Security Advisories · Sep 2, 16:00

**背景**: S/MIME（安全/多用途互联网邮件扩展）是一种用于加密和数字签名电子邮件以确保机密性和真实性的标准。中间人（MITM）攻击是指攻击者将自己置于两个通信方之间，从而能够在不被发现的情况下拦截、修改或转发数据。在此案例中，攻击者利用完整性检查的缺失来篡改加密消息，导致解密过程泄露明文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cvefeed.io/vuln/detail/CVE-2026-20354">CVE-2026-20354 - Cisco Secure Email S / MIME Decryption Plaintext...</a></li>
<li><a href="https://www.cy5.io/blog/man-in-the-middle-attack-explained/">What Is a Man- in - the - Middle (MITM) Attack ? Technical Guide</a></li>

</ul>
</details>

**标签**: `#Cisco`, `#S/MIME`, `#security vulnerability`, `#email encryption`, `#CVE`

---

<a id="item-15"></a>
## [Anthropic 更新 Claude 系统提示，限制歌词复制](https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/) ⭐️ 7.0/10

Anthropic 已为其 Claude 消费级应用发布了更新的系统提示，特别新增了一个部分，明确禁止整体或部分复制歌词、诗歌或书籍段落。该变更出现在 2026 年 1 月 18 日更新的 Fable 5.1 提示中。 此次更新凸显了 AI 行业持续存在的版权问题，因为模型越来越多地被用于生成或复制创意内容。Anthropic 在发布和版本化管理系统提示方面的透明度，为问责制树立了宝贵先例，并让研究人员和开发者能够追踪政策随时间的变化。 新部分规定，Claude 将拒绝复制歌词、诗歌或段落（包括副歌或逐音符旋律等部分复制）的请求，并在同一对话中继续拒绝改写版本。1929 年前发表的作品除外，但 Claude 依据自身对作品日期的了解而非用户的说法。

rss · Simon Willison · Sep 2, 14:16

**背景**: 系统提示是指导 AI 模型行为的隐藏指令，Anthropic 出于透明度考虑将其公开。该公司最近将系统提示文档重组为索引页和按模型分页，并支持 Markdown 输出，使得对比变更更加容易。此次更新顺应了行业解决 AI 输出版权问题的更广泛趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2025/May/25/claude-4-system-prompt/">Highlights from the Claude 4 system prompt | Simon Willison ’s Weblog</a></li>
<li><a href="https://github.com/asgeirtj/system_prompts_leaks">GitHub - asgeirtj/ system _ prompts _leaks: Extracted system prompts ...</a></li>
<li><a href="https://medium.com/@ThinkingLoop/claudes-system-prompts-de-risked-e91524ac1868">Claude ’s System Prompts , De-Risked | by Thinking Loop | Medium</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#Claude`, `#system prompts`, `#AI safety`, `#copyright`

---