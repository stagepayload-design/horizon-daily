---
layout: default
title: "Horizon Summary: 2026-05-24 (ZH)"
date: 2026-05-24
lang: zh
---

> From 34 items, 6 important content pieces were selected

---

1. [80386 微码被反汇编](#item-1) ⭐️ 9.0/10
2. [从第一性原理理解深度学习性能](#item-2) ⭐️ 8.0/10
3. [各大 AI 实验室转向智能体开发](#item-3) ⭐️ 8.0/10
4. [德州女子因发帖讨论水质被捕](#item-4) ⭐️ 7.0/10
5. [意大利选择空客 A330 MRTT 加油机](#item-5) ⭐️ 7.0/10
6. [西班牙法院拒绝因盗版屏蔽令处罚 NordVPN](#item-6) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [80386 微码被反汇编](https://www.reenigne.org/blog/80386-microcode-disassembled/) ⭐️ 9.0/10

Reenigne 成功反汇编了 Intel 80386 处理器的微码 ROM，揭示了实现其复杂指令集的详细微操作。 这一逆向工程壮举提供了对经典 CPU 内部工作的前所未有的洞察，有助于更好地理解历史计算机架构，并可能促进开源兼容处理器的创建。 80386 微码字宽为 37 位，分为源、目标、ALU 源、ALU 跳转、操作、子操作和总线控制等字段。反汇编工作得益于 Ken Shirriff 提供的高分辨率芯片图像。

hackernews · nand2mario · May 23, 12:11 · [社区讨论](https://news.ycombinator.com/item?id=48247004)

**背景**: 微码是实现 CPU 指令集架构的低层指令层。80386 于 1985 年推出，是英特尔首款 32 位处理器，使用微程序设计来执行复杂的 x86 指令。反汇编其微码揭示了每条机器指令如何被分解为微操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reenigne.org/blog/80386-microcode-disassembled/">80386 microcode disassembled « Reenigne blog</a></li>
<li><a href="https://nand2mario.github.io/posts/2026/z386/">z386: An Open-Source 80386 Built Around Original Microcode - Small...</a></li>
<li><a href="https://cybermediacreations.com/80386-microcode-disassembled/">80386 Microcode Disassembled - Cyber Media Creations</a></li>

</ul>
</details>

**社区讨论**: 社区对逆向工程过程表现出浓厚兴趣，有用户询问如何从芯片图像中提取微码。另一位用户注意到该博客的悠久历史，还提到了一个相关项目（z386），该项目围绕原始微码构建开源 80386。

**标签**: `#reverse engineering`, `#microcode`, `#80386`, `#computer architecture`, `#retrocomputing`

---

<a id="item-2"></a>
## [从第一性原理理解深度学习性能](https://horace.io/brrr_intro.html) ⭐️ 8.0/10

一篇 2022 年发布的综合性指南从第一性原理出发，解释了深度学习性能优化，涵盖硬件、软件和系统设计。 该指南帮助工程师和研究人员理解 GPU 性能背后的基本因素，使他们能够编写更高效的深度学习代码并做出明智的硬件选择。 文章强调了 NVIDIA 在 TFLOPs、带宽和互连方面的持续领先地位，并指出在 Python 执行一个 FLOP 的时间内，单个 A100 GPU 可以完成 975 万次 FLOP。

hackernews · tosh · May 23, 11:50 · [社区讨论](https://news.ycombinator.com/item?id=48246889)

**背景**: 深度学习性能既取决于算法效率，也取决于硬件利用率。GPU，尤其是 NVIDIA 的 CUDA 生态系统，凭借大规模并行性和高内存带宽占据主导地位。优化需要理解内存层次结构、内核融合和通信开销。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/berkan_sesen/backpropagation-demystified-neural-nets-from-first-principles-4303">Backpropagation Demystified: Neural Nets from First Principles</a></li>
<li><a href="https://www.ruder.io/optimizing-gradient-descent/">An overview of gradient descent optimization algorithms</a></li>
<li><a href="https://newji.ai/japan-industry/fundamentals-of-gpu-programming-cuda-speed-up-techniques-using-optimization-techniques-and-debugging-points/">Fundamentals of GPU programming (CUDA), speed-up techniques ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论称赞该文章为经典之作，并指出 NVIDIA 显著的竞争优势。一些评论者强调不同运行时和硬件之间缺乏可移植的建议，并对生产系统的故障模式表示兴趣。

**标签**: `#deep learning`, `#performance optimization`, `#ML systems`, `#NVIDIA`, `#GPU`

---

<a id="item-3"></a>
## [各大 AI 实验室转向智能体开发](https://www.latent.space/p/ainews-all-model-labs-are-now-agent) ⭐️ 8.0/10

包括 OpenAI、Google 和 Anthropic 在内的主要 AI 模型实验室正将重心从纯模型开发转向构建基于智能体的系统，这一趋势在近期行业言论的总结中得到凸显。 这一转向标志着 AI 领域的范式转变，从静态模型转向能与环境交互的自主智能体，可能加速自动化、机器人技术和软件工程等领域的实际应用。 该文章综合了多个实验室的言论，但未提供具体技术细节或时间表；它是一篇趋势分析而非原创报道。

rss · Latent Space · May 23, 04:21

**背景**: AI 智能体是能够感知环境、做出决策并采取行动以实现目标的系统，不同于仅生成输出的传统 AI 模型。主要实验室历来专注于提升模型能力，但近期在推理和工具使用方面的进展使智能体变得更加可行。

**标签**: `#AI`, `#agents`, `#industry trend`, `#machine learning`

---

<a id="item-4"></a>
## [德州女子因发帖讨论水质被捕](https://reclaimthenet.org/texas-woman-arrested-for-facebook-post-about-town-water-quality) ⭐️ 7.0/10

一名德州女子因在 Facebook 上发帖称镇上水质可能受到污染而被捕，警方援引虚假报告法规。帖子称有居民因水中细菌住院，她表示这是转述他人说法。 此事件引发对言论自由以及虚假报告法规可能被滥用以压制公共卫生报道的严重担忧。它可能阻止公民报告疑似环境危害，从而损害公共安全和政府问责。 逮捕依据的是德州一项要求明知虚假仍传播的法规；Combs 辩称她只是转述他人说法。批评者指出，向医院核实此类信息会违反 HIPAA，而应由 TCEQ 等州级机构进行调查。

hackernews · abawany · May 23, 18:02 · [社区讨论](https://news.ycombinator.com/item?id=48249747)

**背景**: 该案涉及德州一个小镇，居民报告水变色和健康问题。虚假报告法规通常用于炸弹威胁等恶作剧，而非公民报道。第一修正案保护关于公共议题的言论，但明知虚假的陈述可能不受保护。

**社区讨论**: 评论者普遍批评逮捕行为越界，许多人预测指控不会成立。有人将其比作易卜生的戏剧《人民公敌》，剧中揭露水污染的医生遭到报复。还有人指出，向医院核实会违反 HIPAA，使得遵守法规变得不可能。

**标签**: `#free speech`, `#government overreach`, `#public health`, `#legal`, `#censorship`

---

<a id="item-5"></a>
## [意大利选择空客 A330 MRTT 加油机](https://www.euronews.com/my-europe/2026/05/21/italy-moves-to-airbus-a330-tankers-in-major-nato-aligned-shift) ⭐️ 7.0/10

意大利正式订购 6 架空客 A330 MRTT 加油机，总价 13.9 亿欧元，取消了此前购买波音 KC-46A“飞马”加油机的计划。 这一转变标志着意大利在国防采购上向北约靠拢、远离美国，背后是 KC-46 的技术问题和更广泛的地缘政治调整。此举巩固了空客在加油机市场的地位，并可能促使其他欧洲国家效仿。 A330 MRTT 是一种多用途加油运输机，已被许多北约及非北约盟国采用，其燃油容量和多功能性优于 KC-46。意大利的决定是在波音加油机多年延误和技术问题之后做出的，该机型在国际竞争中一直处于劣势。

hackernews · embedding-shape · May 23, 16:02 · [社区讨论](https://news.ycombinator.com/item?id=48248775)

**背景**: 空客 A330 MRTT 是基于 A330 客机改装的军用加油机，兼具空中加油和货物运输能力。它与波音 KC-46A“飞马”直接竞争，后者一直面临技术问题和交付延迟。意大利的采购转变反映了欧洲国家在跨大西洋关系紧张背景下，寻求国防供应商多元化的更广泛趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Airbus_A330">Airbus A 330 - Wikipedia</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lVN0tHWEVSRlhwbmNPa3ZTQjV5Z0FQAQ?hl=en-GB&gl=GB&ceid=GB:en">Google News - News about A 330 MRTT • Italy - Overview</a></li>
<li><a href="https://simpleflying.com/what-distinguishes-airbus-a330-mrtt-other-tanker-aircraft/">What Distinguishes The Airbus A 330 MRTT From Other Tanker Aircraft?</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为意大利此举是空客的工业胜利，而非美国的政治失败，并指出 KC-46 的技术问题。有人提到美国股市可能滞后反映这种转变，还有人强调瑞士在美国防务合同上也面临类似困境。

**标签**: `#defense`, `#geopolitics`, `#aviation`, `#NATO`, `#procurement`

---

<a id="item-6"></a>
## [西班牙法院拒绝因盗版屏蔽令处罚 NordVPN](https://torrentfreak.com/spanish-court-declines-to-fine-nordvpn-over-laliga-piracy-blocking-order/) ⭐️ 7.0/10

西班牙一家法院拒绝因 NordVPN 未能按西甲联赛要求屏蔽盗版流媒体而对其处以罚款，理由是无差别 IP 屏蔽可能影响合法服务。 这一裁决为 VPN 在盗版屏蔽中的责任设定了法律先例，强化了欧盟反对无差别互联网审查的规定，并保护了网络中立性。 法院最初命令 NordVPN 和 ProtonVPN 屏蔽 16 个盗版网站，但 NordVPN 辩称 IP 屏蔽也会干扰 GitHub 和 Cloudflare 基础设施等合法服务。

hackernews · gslin · May 23, 06:54 · [社区讨论](https://news.ycombinator.com/item?id=48245362)

**背景**: 西甲联赛积极采取反盗版措施，于 2024 年 12 月获得法院命令，迫使 ISP 和 VPN 屏蔽盗版流媒体。然而，无差别 IP 屏蔽造成了附带损害，影响了西班牙的 Cloudflare 服务和 GitHub 访问，引发了公众反弹和议会审查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/legal/spain-orders-nordvpn-protonvpn-to-block-laliga-piracy-sites/">Spain orders NordVPN, ProtonVPN to block LaLiga piracy sites</a></li>
<li><a href="https://www.technadu.com/spain-faces-internet-chaos-amid-cloudflare-isp-and-laliga-blocking-controversy/575457/">LaLiga Blockings Disrupt Cloudflare Infrastructure in Spain - TechNadu</a></li>
<li><a href="https://www.techtimes.com/articles/316733/20260516/spains-parliament-votes-rein-laligas-mass-ip-blockades-test-case-eu-internet-governance.htm">Spain's Parliament Votes to Rein In LaLiga 's Mass IP Blockades...</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍对法院的裁决表示赞赏，许多人指出屏蔽 GitHub 等合法服务的荒谬性。有人对足球赛季即将结束表示欣慰，而另一些人则警告用户必须积极捍卫隐私权。

**标签**: `#VPN`, `#piracy`, `#internet censorship`, `#EU law`, `#net neutrality`

---