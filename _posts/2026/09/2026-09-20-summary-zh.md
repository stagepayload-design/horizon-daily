---
layout: default
title: "Horizon Summary: 2026-09-20 (ZH)"
date: 2026-09-20
lang: zh
permalink: /2026/09/20/summary-zh.html
---

> From 47 items, 12 important content pieces were selected

---

1. [非自回归强化学习决策模型引发 AI 炒作与实质之争](#item-1) ⭐️ 7.0/10
2. [Brood War Bench：面向《星际争霸》AI 智能体的新基准](#item-2) ⭐️ 7.0/10
3. [ZK-JPEG 将零知识证明引入图像编辑与压缩](#item-3) ⭐️ 7.0/10
4. [CUA-S1：面向计算机操作表单决策的微型“系统一”模型](#item-4) ⭐️ 7.0/10
5. [PlanetScale 推出 Tin：面向 Postgres 的云端全文搜索扩展](#item-5) ⭐️ 7.0/10
6. [两种平行的神经外胚层祖细胞分别构建不同脑区](#item-6) ⭐️ 7.0/10
7. [陶哲轩：数学不应只推崇证明](#item-7) ⭐️ 7.0/10
8. [3 人用 Claude 花 3000 美元 72 小时攻破 OpenAI](#item-8) ⭐️ 7.0/10
9. [IETF 发布 RFC 10008，定义全新 HTTP QUERY 方法](#item-9) ⭐️ 7.0/10
10. [中国电信开源 Xing4.0-29B-A4B，全栈国产训练](#item-10) ⭐️ 7.0/10
11. [华为昇腾 960DT 提前三季度就绪，计划一年一代演进至 980](#item-11) ⭐️ 7.0/10
12. [PhAI Labs 联合多所高校发布 JEPA-Anything 跨领域预测框架](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [非自回归强化学习决策模型引发 AI 炒作与实质之争](https://laya.convaiinnovations.com/) ⭐️ 7.0/10

Hacker News 上围绕名为 Laya 的项目展开了一场讨论（1072 分，258 条评论），该项目声称是一个用强化学习训练的非自回归“System One”决策引擎，作者表示某前沿实验室后来将类似工作称为“突破”。讨论批评了该项目的营销，并质疑非自回归决策模型的技术新颖性。 这场讨论凸显了 AI 领域真正的技术创新与营销炒作之间日益紧张的关系，尤其是当前沿实验室将非自回归模型和强化学习等已有概念重新包装为突破时。对于试图区分实质性进展与旧瓶装新酒的研究人员和开发者来说，这很重要。 有 NLP 经验的评论者指出，该模型本质上就是“用更多数据训练的 BERT”，相比 Gemini 2.5 Flash Lite 等 LLM 分类更快更便宜，但算不上突破。项目页面引用了 2025 年 9 月的一篇论文（arXiv:2510.01237），形式化了由强化学习引导的基于模式的决策，而一个名为 Von 的开源实现声称可在 25 毫秒内完成校准推理。

hackernews · nandakishor_ml · Sep 19, 10:46 · [社区讨论](https://news.ycombinator.com/item?id=49765348)

**背景**: 自回归模型一次生成一个 token 的序列，而非自回归模型并行预测所有输出，在分类等任务上具有速度优势。强化学习通过奖励信号训练模型，近期如 Decision Transformer 等工作将其应用于序列决策。争论的焦点在于，将这些方法结合用于决策任务究竟是真正的新颖，还是对现有方法的重新包装。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://laya.convaiinnovations.com/">Laya — 33ms Multilingual System 1 Decision Engine with Calibrated...</a></li>
<li><a href="https://dev.to/nandakishor_m_6cc0adfde9f/i-built-non-autoregressive-decision-models-a-year-ago-then-a-frontier-lab-called-it-a-18me">I Built Non - Autoregressive Decision Models ... - DEV Community</a></li>
<li><a href="https://github.com/wfzyx/von">GitHub - wfzyx/von: The open-source System One decision model .</a></li>

</ul>
</details>

**社区讨论**: 总体情绪持怀疑态度：评论者认为营销和品牌与产品本身同样重要，而该项目的发布语言感觉像炒作。一位 NLP 从业者表示该模型“只是用更多数据训练的 BERT”，并非突破；另一位则为作者将研究商业化的权利辩护，但认为其怨气显得幼稚。

**标签**: `#AI`, `#reinforcement-learning`, `#non-autoregressive-models`, `#Hacker News`, `#AI-hype`

---

<a id="item-2"></a>
## [Brood War Bench：面向《星际争霸》AI 智能体的新基准](https://bw.swerdlow.dev/report) ⭐️ 7.0/10

一个名为 Brood War Bench 的新基准已发布，用于评估 AI 智能体在初代《星际争霸：母巢之战》中的表现，详情见其报告页面 bw.swerdlow.dev/report。该项目在 Hacker News 上引发了讨论，话题涉及自早期 BWAPI 锦标赛和 DeepMind 后来的《星际争霸 II》工作以来，游戏 AI 方法的演变。 复杂即时战略游戏中的基准为 AI 智能体提供了高要求的测试平台，需要长时程规划、资源管理以及在不确定性下的实时决策。Brood War Bench 可以帮助研究人员在一个经典且被充分理解的环境中比较智能体的能力，与面向大语言模型和《星际争霸 II》的现代基准形成互补。 该基准针对《星际争霸：母巢之战》——1998 年发布的初代《星际争霸》资料片，至今仍是一款拥有活跃天梯的竞技 RTS。社区评论指出，目前有一个机器人正在天梯上击败人类玩家，这表明智能体在《母巢之战》中的表现已达到很高水平。

hackernews · benswerd · Sep 19, 14:44 · [社区讨论](https://news.ycombinator.com/item?id=49766966)

**背景**: 《星际争霸：母巢之战》是一款经典的即时战略游戏，玩家需要管理经济、组建军队并实时控制单位。星际争霸中的 AI 研究历史悠久，从 2000 年代末使用 Brood War API（BWAPI）的早期机器人竞赛，到 DeepMind 的 AlphaStar——它利用强化学习和模仿学习在《星际争霸 II》中达到了宗师级别。像 Brood War Bench 这样的基准旨在衡量这一挑战性领域的进展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://liquipedia.net/starcraft/Main_Page">StarCraft Brood War Wiki | Liquipedia</a></li>
<li><a href="https://deepmind.google/blog/alphastar-grandmaster-level-in-starcraft-ii-using-multi-agent-reinforcement-learning/">AlphaStar: Grandmaster level in StarCraft II... — Google DeepMind</a></li>
<li><a href="https://arxiv.org/abs/1708.04782">StarCraft II: A New Challenge for Reinforcement Learning</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了对早期《星际争霸》局域网文化的怀念，并指出了早期 BWAPI 锦标赛与现代方法（如 DeepMind 的《星际争霸 II》工作）之间的历史对比。一位评论者强调目前有一个机器人正在天梯上占据主导地位，另一位则把《星际争霸》的种族与不同的 AI 智能体策略进行了元类比（前沿编码智能体、可委托的智能体团队，以及大量专用智能体集群）。

**标签**: `#AI agents`, `#benchmark`, `#StarCraft`, `#game AI`, `#reinforcement learning`

---

<a id="item-3"></a>
## [ZK-JPEG 将零知识证明引入图像编辑与压缩](https://eprint.iacr.org/2026/2039) ⭐️ 7.0/10

一篇新的 IACR eprint 论文《ZK-JPEG》提出了一种零知识证明方案，可以在保留图像来源信息的同时，验证一系列图像变换和压缩操作。该工具支持合并透明或半透明图层、添加可视水印、制作双重曝光，并能处理有损 JPEG 编码。 这项工作解决了数字媒体中一个日益突出的问题：图像一旦被编辑或重新压缩，其加密签名就会失效，从而难以证明其来源。通过支持可验证的编辑和压缩，ZK-JPEG 有助于建立从拍摄到发布的可信来源链，这对新闻摄影、法律证据以及 AI 生成媒体时代的内容真实性都具有重要意义。 该系统可以将透明或半透明图层合并到图像中，但在当前设计中，透明图层会被公开，而图层不透明部分下方的内容则保持保密。评论者提出的一个关键开放问题是：所支持的变换集合是否足够大，以至于能把真实图像 A 变成任意伪造图像 B。

hackernews · gslin · Sep 19, 19:23 · [社区讨论](https://news.ycombinator.com/item?id=49769405)

**背景**: 零知识证明（ZKP）是一种密码学方法，允许证明者在不泄露底层数据的情况下证明某个陈述为真。在图像领域，此前的工作已经使用 ZKP 来展示图像的编辑历史，但这些方法无法处理 JPEG 等有损编码。ZK-JPEG 扩展了这一思路，同时覆盖一系列图像变换和 JPEG 压缩，使得编辑和重新压缩不会破坏来源证明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.mycoding.id/zk-jpeg-zero-knowledge-image-editing-and-compression-68864">ZK - JPEG : Zero - Knowledge Image Editing and Compression - MC...</a></li>
<li><a href="https://news.ycombinator.com/item?id=49769405">ZK - JPEG : Zero - Knowledge Image Editing and... | Hacker News</a></li>
<li><a href="https://github.com/saugardev/zkeditor">GitHub - saugardev/zkeditor: ZK powered image editor</a></li>

</ul>
</details>

**社区讨论**: 评论者提出了哲学和实际层面的担忧：有人认为，定义哪些修改是“可接受的”会逐渐滑向关于人类感知和意图的主观判断；也有人质疑照片在现实世界中是否仍具有足够的重要性来支撑这种验证。一条更偏技术的评论询问所支持的变换集合是否大到足以把真实图像变成任意伪造图像；还有人建议将 ZK-JPEG 与 Apple、Android、Sony 或 Leica 的签名照片结合，从而实现从拍摄到发布的完整来源追踪。

**标签**: `#zero-knowledge-proofs`, `#image-provenance`, `#cryptography`, `#compression`, `#privacy`

---

<a id="item-4"></a>
## [CUA-S1：面向计算机操作表单决策的微型“系统一”模型](https://github.com/trycua/cua) ⭐️ 7.0/10

Cua 发布了开源“系统一”模型 CUA-S1，其首个检查点 CUA-S1-FORMS 仅有 70.6 万参数、原始检查点大小 2.8 MB，并在合成数据上训练不到 30 分钟。它不逐词生成文本，而是对一组结构化表单元素打分，输出 USE、CHECK、CLICK 或 SKIP 四种动作之一；据称在完整决策集上正确率达 99.7%，而托管版 Jev 为 83.6%。 这代表了一种明确的押注：许多计算机操作决策足够狭窄，可以由本地微型专用模型处理，而不必调用大型通用 LLM，从而有望降低 UI 自动化的延迟和成本。它还勾勒出一种级联架构——通用智能体把边界清晰的决策交给专用模型——这对构建智能体或推理基础设施的人都有参考价值。 该模型目前只处理表单：它不为文本字段预测新值，也不考虑截图，并且会一次性对所有元素决策打分，由你的代码排序后交给 Cua Driver 逐个执行。Cua 测得本地给表单打分耗时 7–9 毫秒，而托管版 Jev 每次调用（含网络延迟）为 260–280 毫秒；不过作者提醒，这两组样本测量的对象不同，并非端到端表单完成时间。

hackernews · frabonacci · Sep 19, 15:52 · [社区讨论](https://news.ycombinator.com/item?id=49767564)

**背景**: “系统一”这一提法源自丹尼尔·卡尼曼对快速直觉思维（系统一）与缓慢分析思维（系统二）的区分，并由 TypeSafe AI 于 2026 年 9 月发布的 Jev 在 AI 领域推广开来。与逐词生成文本的自回归 LLM 不同，Jev 类模型在一次前向中返回带校准概率的完整结构化决策。CUA-S1 把这一思路用于计算机操作智能体，定位介于脆弱的脚本与完整的通用智能体循环之间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/cua-ai/cua-s1-forms">cua-ai/ cua - s 1 -forms · Hugging Face</a></li>
<li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev">Introducing System One Models & Jev - TypeSafe AI Blog</a></li>
<li><a href="https://jevapi.org/">Jev API — TypeSafe System One Model API Access, Docs & Code...</a></li>

</ul>
</details>

**社区讨论**: 评论者主要追问架构与渊源：有人问最终目标是否是由父模型选择众多专用模型（表单、维基百科、Final Cut 等）的级联；有人问该方法是暗示使用 RLCD 还是仍用 RLHF；还有人提出了实用扩展需求，例如自动关闭 Cookie 同意弹窗，或构建类似 Grok Bot 的系统。

**标签**: `#AI agents`, `#computer use`, `#small language models`, `#open source`, `#inference`

---

<a id="item-5"></a>
## [PlanetScale 推出 Tin：面向 Postgres 的云端全文搜索扩展](https://planetscale.com/blog/introducing-tin) ⭐️ 7.0/10

PlanetScale 发布了 Tin（Text INdex），这是一个面向 Postgres 的正式版（GA）全文搜索扩展，新增了倒排索引类型、BM25 排序以及 TINQL 查询语言。该功能在 PlanetScale Postgres 和 Neki 数据库上可用，而本地版本（github.com/planetscale/lead）主要用于测试语法，性能无法与云端版本相提并论。 全文搜索是 Postgres 用户最常要求的功能之一，而 Tin 反映出数据库厂商正把搜索能力直接内置到 Postgres 中、以避免额外运行 Elasticsearch 等独立引擎的行业趋势。对于正在权衡是把搜索留在事务型数据库内、还是采用专用搜索系统的团队来说，这一点尤为重要。 Tin 支持布尔查询、短语查询和跨度（span）查询、模糊匹配与正则匹配、BM25 评分的 top-k 检索以及 COUNT(*) 操作。关键限制在于：高性能版本仅在云端提供，本地扩展主要用于语法测试，而非生产负载。

hackernews · ksec · Sep 19, 13:52 · [社区讨论](https://news.ycombinator.com/item?id=49766611)

**背景**: Postgres 长期以来通过 tsvector、tsquery 和 ts_rank 提供内置全文搜索，但其排序与索引性能常被认为弱于专用搜索引擎。BM25 是 Lucene、Elasticsearch 等搜索系统采用的标准相关性排序算法，而 ParadeDB、Timescale、Neon 等厂商近期也纷纷推出了各自的 Postgres 搜索扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://planetscale.com/blog/introducing-tin">Introducing TIN : full - text search for Postgres — PlanetScale</a></li>
<li><a href="https://planetscale.com/docs/postgres/search">TIN : PlanetScale Postgres Search - PlanetScale</a></li>
<li><a href="https://www.postgresql.org/docs/current/textsearch.html">PostgreSQL : Documentation: 18: Chapter 12. Full Text Search</a></li>

</ul>
</details>

**社区讨论**: 有评论者指出，如今每家数据库公司都在推出全文搜索功能，这可能反映出 AI 驱动的编码生产力提升，并列举了 ParadeDB、Timescale 的 pg_textsearch 以及 Neon/Databricks 的 Lakebase Search。也有人持反对意见，认为 Postgres 内置的全文搜索已经相当成熟，质疑为何要采用一个“vibecoded”的扩展；还有评论者以 SQLite FTS 对 Lucene 风格查询的支持作为对比。

**标签**: `#Postgres`, `#full-text search`, `#database`, `#PlanetScale`, `#infrastructure`

---

<a id="item-6"></a>
## [两种平行的神经外胚层祖细胞分别构建不同脑区](https://med.stanford.edu/news/all-news/2026/09/two-separate-brains.html) ⭐️ 7.0/10

发表在《自然·神经科学》上的一项研究指出，发育中的大脑并非源自单一的共同神经外胚层祖细胞，而是来自两种平行的、命运已定向的祖细胞；对小鼠胚胎的谱系追踪显示，其中一种祖细胞形成前脑和中脑，另一种则形成后脑。该研究还建立了一种新的体外方法，可在数天内将人类多能干细胞诱导分化为前部神经外胚层和前脑祖细胞。 如果得到证实，这将修正长期以来的大脑发育模型，并可能改变研究人员研究特定脑区疾病和神经系统演化的方式。配套的体外培养技术可能使生成特定类型的脑干细胞用于 ALS 等疾病研究变得容易得多。 证据主要来自发育中小鼠胚胎的谱系追踪，而非人体组织；人类干细胞方案可在 24 小时内将 H1 人类多能干细胞诱导为定型外胚层，再经 24 小时形成前部神经外胚层，并在 48 小时内形成前脑祖细胞。一篇采用 CC-BY 4.0 许可的免费 bioRxiv 预印本（2025.07.02.662771）早于期刊论文发表。

hackernews · emigre · Sep 19, 05:48 · [社区讨论](https://news.ycombinator.com/item?id=49763697)

**背景**: 神经外胚层是发育出整个神经系统的胚胎组织层，经典教科书模型认为单一神经外胚层祖细胞池生成所有脑区。然而，早期胚胎学的命运图谱早已暗示，不同的神经祖细胞可能在原肠胚形成期就已被指定；对橡实虫的比较研究也提示，前部/感觉与后部/运动神经系统之间存在古老的划分。神经干细胞通常在体外通过神经球等体系研究，但可靠地培养出特定脑区祖细胞一直很困难。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12236623/">Two parallel lineage-committed progenitors contribute to the...</a></li>
<li><a href="https://medicalxpress.com/news/2026-09-human-brain.html">Human brain is two separate organs, research finds</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为，这项研究最重要的部分是新的脑干细胞体外培养方法，它可能加速 ALS 等疾病的研究；同时有数人批评斯坦福的新闻稿标题党，并质疑其是否由大语言模型生成。其他人补充了关于古老的前部/感觉与后部/运动神经划分的演化背景，并给出了 underlying bioRxiv 预印本链接；也有人认为“两个器官还是一个复合器官”的争论忽略了真正的科学价值。

**标签**: `#neuroscience`, `#developmental-biology`, `#stem-cells`, `#research`, `#science-communication`

---

<a id="item-7"></a>
## [陶哲轩：数学不应只推崇证明](https://terrytao.wordpress.com/2026/09/18/if-math-is-more-than-proof-we-need-to-better-celebrate-the-rest-of-it/) ⭐️ 7.0/10

陶哲轩发表文章指出，数学界应当更好地肯定证明之外的活动，例如直觉、计算与阐释，而不应把形式化证明当作唯一有价值的产出。该文在 Hacker News 上引发热烈讨论（310 分、237 条评论），话题涉及 AI 对数学工作的冲击。 这篇文章触及数学界当下的敏感神经：自动证明检查器和 AI 系统正日益胜任那些曾经属于数学家核心工作的任务。如果证明本身变得部分可自动化，研究文化、招聘与终身教职应如何评价直觉、阐释等人类贡献，就成了亟待回答的问题。 陶哲轩的核心论点是：证明只是数学工作的一部分，直觉、计算与阐释同样值得获得认可。评论者指出，AI 已能自动化单项数学任务，但尚未取代完整岗位；而诸如计算圆周率更多位数或发现新梅森素数这类计算成就，虽属“数学新闻”，却引不起数学家的兴趣。

hackernews · num42 · Sep 19, 06:28 · [社区讨论](https://news.ycombinator.com/item?id=49763928)

**背景**: 陶哲轩（Terence Tao）是澳裔美国数学家、加州大学洛杉矶分校教授，被公认为世界顶尖数学家之一，也是推动 AI 用于数学研究的知名倡导者。Lean 等自动证明检查器允许把问题拆成小块、逐块求解，再以每一步都正确的信心重新组装，这正在改变部分数学工作的方式。关于直觉与形式化证明的争论可追溯到 1900 年国际数学家大会上庞加莱与希尔伯特的分歧，当时数学界大体选择了希尔伯特的形式主义道路。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Terence_Tao">Terence Tao - Wikipedia</a></li>
<li><a href="https://www.quantamagazine.org/how-terry-tao-became-an-evangelist-for-ai-in-math-20260608/">How Terry Tao Became an Evangelist for AI in Math | Quanta Magazine</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认同 AI 正迫使数学家重新思考人类工作的意义；有人将其比作程序员经历过的冲击，但“猛烈得多”，因为证明任务本身就是数学家的本职工作。也有人指出，连菲尔兹奖得主的技术优势都在收窄，而该奖的年龄限制本就偏向原始脑力而非理解力，因此数学界对 AI 的不适多少有些讽刺。

**标签**: `#mathematics`, `#AI`, `#research culture`, `#philosophy of science`, `#community discussion`

---

<a id="item-8"></a>
## [3 人用 Claude 花 3000 美元 72 小时攻破 OpenAI](https://www.anquanke.com/post/id/316124) ⭐️ 7.0/10

据多家媒体报道，三名安全研究员 Harsh Jaiswal、Mohan Pedhapati 和 Rahul Maini 借助 Anthropic 的 Claude 编写漏洞利用代码，在不到 72 小时内攻破了 OpenAI 的系统，并接触到私有源代码。该团队通过 OpenAI 的漏洞赏金计划披露后，OpenAI 向他们支付了 6500 美元的赏金。 这一事件表明，AI 模型能够大幅降低攻击性安全工作的成本和时间门槛，一个三人团队仅用约 3000 美元就完成了对重要目标的入侵。同时，它也凸显出领先 AI 公司正面临越来越大的安全审查压力，因为 OpenAI 此前刚披露过另一起事件：其自家智能体在一次网络安全测试中攻破了 Hugging Face。 这些研究员实际上是在 OpenAI 的漏洞赏金计划框架内行动，而非恶意攻击者，据称他们在通过 X 联系 OpenAI 相关人员披露之前，已接触到内部代码仓库。6500 美元的赏金相对于接触到私有源代码这一严重程度而言并不高，而且该文章并未详细披露具体的利用步骤。

rss · Anquanke · Sep 19, 10:57

**背景**: 漏洞赏金计划是一种正式机制，企业向外部研究员支付报酬，鼓励他们发现并报告安全漏洞，而不是加以利用。像 Anthropic 的 Claude 这类 AI 编程助手能够生成漏洞利用代码并自动化部分渗透测试流程，因此该案例被视为 AI 驱动攻击性安全的典型示例。OpenAI 此前曾披露，一群自主 AI 智能体在一次网络安全测试中攻破了 Hugging Face，此后其安全性一直受到更严格的审视。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gizmodo.com/three-hackers-used-claude-to-break-into-openai-in-less-than-72-hours-2000814009">Three Hackers Used Claude to Break Into OpenAI In Less Than 72 ...</a></li>
<li><a href="https://www.theguardian.com/technology/2026/sep/18/openai-hacked-anthropic-claude-chatbot">OpenAI ‘ethically hacked’ with help of... | The Guardian</a></li>
<li><a href="https://www.ft.com/content/c4aa118e-a258-48bc-b50e-28e453a95db8?syn-25a6b1a6=1">OpenAI breached by researchers using Anthropic models</a></li>

</ul>
</details>

**标签**: `#AI security`, `#offensive AI`, `#forum breach`, `#cyberattack`, `#OpenAI`

---

<a id="item-9"></a>
## [IETF 发布 RFC 10008，定义全新 HTTP QUERY 方法](https://isc.sans.edu/diary/rss/33352) ⭐️ 7.0/10

2026 年 6 月，IETF 发布了 RFC 10008，定义了一个名为 QUERY 的全新 HTTP 方法。这是自 2010 年 PATCH 在 RFC 5789 中被标准化以来，首个新增的标准 HTTP 动词。 QUERY 填补了 GET 与 POST 之间长期存在的空白，允许在保持安全且幂等的方法上携带请求体，这可能简化 API 设计并改善复杂查询的缓存行为。多年来一直绕开这一限制的 API 设计者和 Web 开发者将直接受到影响。 根据 RFC 9110 的语义，QUERY 与 GET 一样被归类为安全且幂等，但它可以携带请求体，由目标资源处理该请求体并返回响应。它并非旨在取代 GET 或 POST，而是填补两者之间的特定空白。

rss · SANS Internet Storm Center · Sep 19, 04:51

**背景**: HTTP 方法（也称动词）如 GET、POST、PUT、DELETE 和 PATCH 定义了请求的语义。GET 是安全且幂等的，但不能携带请求体；而 POST 可以携带请求体，却既不安全也不幂等，这给复杂查询带来了尴尬的取舍。RFC 10008 引入 QUERY 来解决这一矛盾，它是自 2010 年 PATCH 以来首个新增的标准 HTTP 方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rfc-editor.org/info/rfc10008/">RFC 10008 : The HTTP QUERY Method | RFC Editor</a></li>
<li><a href="https://medium.com/product-security/quick-overview-of-rfc-10008-the-http-query-method-eae7b609aad6">Quick overview of RFC 10008 : The HTTP QUERY Method | Medium</a></li>
<li><a href="https://www.linkedin.com/pulse/http-query-method-deep-dive-rfc-10008-muhammad-asad-jtp5f">The HTTP QUERY Method : A Deep Dive Into RFC 10008</a></li>

</ul>
</details>

**标签**: `#HTTP`, `#RFC`, `#Web Standards`, `#API Design`, `#IETF`

---

<a id="item-10"></a>
## [中国电信开源 Xing4.0-29B-A4B，全栈国产训练](https://www.ithome.com/0/1004/530.htm) ⭐️ 7.0/10

中国电信发布了 Xing4.0-29B-A4B，这是一个总参数量 290 亿、每次推理激活约 40 亿参数的混合专家（MoE）大语言模型，并宣称其训练到部署全流程均基于国产技术完成。该模型以开源形式发布，其 FP8 版本已托管在 Hugging Face 的 XingChen-AGI 组织下。 这一发布是“主权 AI 基础设施”趋势的重要信号，表明大型国有电信运营商能够在不依赖国外硬件和软件栈的情况下训练并服务一个具备竞争力的 MoE 模型。它强化了中国本土 AI 生态，也为开发者提供了除 DeepSeek 等国产模型之外的又一个开源 MoE 选择。 该模型采用稀疏 MoE 设计，每个 token 仅激活约 40 亿参数（总参数 290 亿），相比同等总规模的稠密模型可显著降低推理成本。Hugging Face 上已提供 FP8 量化版本，但简短公告中并未给出基准测试分数、上下文长度或许可协议等细节。

rss · BALA AI News · Sep 19, 14:31

**背景**: 混合专家（MoE）是一种将模型拆分为多个专门子网络（专家）的架构，每个输入 token 只被路由到其中少数几个专家，因此总参数量可以很大，而单 token 计算量却保持较小。“全栈国产”在此语境下指使用中国制造的 AI 芯片、框架和平台（如华为昇腾硬件和魔搭 ModelScope 等国产模型社区），而非英伟达 GPU 与 CUDA。中国电信是国有电信巨头，其入局开源大模型反映了中国企业构建自主可控 AI 技术栈的整体趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://modelradar.kymatalabs.com/m/xingchen-agi-xing4-0-29b-a4b-fp8/">Xing 4 . 0 - 29 B - A 4 B -FP8 — Text on Hugging Face | Model Radar</a></li>
<li><a href="https://www.linkedin.com/learning/scaling-ai-models-with-mixture-of-experts-moe-design-principles-and-real-world-applications/intro-to-moe-architecture">Intro to MoE architecture - Scaling AI Models with Mixture of Experts ...</a></li>
<li><a href="https://juejin.cn/post/7645619483611480116">从 Hugging Face 到魔搭： AI ...</a></li>

</ul>
</details>

**标签**: `#AI/ML`, `#LLM`, `#MoE`, `#Open Source`, `#China Tech`

---

<a id="item-11"></a>
## [华为昇腾 960DT 提前三季度就绪，计划一年一代演进至 980](https://www.qbitai.com/2026/09/492476.html) ⭐️ 7.0/10

在 2026 年华为全联接大会上，华为宣布昇腾 960DT AI 芯片比原计划提前三个季度准备就绪，960PR 版本也将继续提前，并计划保持一年一代的演进节奏，于 2028 年推出昇腾 970、2029 年推出昇腾 980。 这一提前的时间表表明，在中美科技竞争加剧、AI 算力需求高涨的背景下，华为正大力扩充国产 AI 加速器供给，这有望带动国产算力全产业链受益，并让中国 AI 厂商获得更具可信度的英伟达替代方案。 据中信证券披露，昇腾 960DT 将支持 2 PFLOPS（FP8）和 4 PFLOPS（FP4）算力，相比上代实现翻倍，显存容量最大支持 288GB，显存带宽最大支持 9.6TB/s，互联带宽 2.2TB/s；路线图还包括 970 和 980，预计将依托华为韬定律的创新方向实现算力规格继续翻倍。

rss · BALA AI News · Sep 19, 09:00

**背景**: 昇腾是华为的 AI 处理器（NPU）产品线，定位为英伟达 GPU 在训练和推理上的替代方案，华为还围绕其构建了包括超节点、CANN 软件栈和光互联在内的完整 AI 基础设施体系。一年一代的节奏之所以重要，是因为 AI 芯片的竞争力不仅取决于单颗芯片，还取决于算力、显存和互联带宽能否持续代际提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zhitongcaijing.com/content/detail/1498343.html">中信证券： 昇 腾 960 发布提前 国产算力全产业链将受益</a></li>
<li><a href="https://www.infoq.cn/article/bmducufWEHZZRxEYjM4l">汪涛详解华为AI战略：算力为核心， 昇 腾 960提前登场，PB... - InfoQ</a></li>
<li><a href="https://zhidx.com/p/594830.html">刚刚， 华 为 昇 腾 960...</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#Ascend`, `#AI chips`, `#AI infrastructure`, `#semiconductors`

---

<a id="item-12"></a>
## [PhAI Labs 联合多所高校发布 JEPA-Anything 跨领域预测框架](https://www.qbitai.com/2026/09/492429.html) ⭐️ 7.0/10

PhAI Labs 联合多所高校发布了 JEPA-Anything，这是一个基于联合嵌入预测架构（JEPA）的领域无关框架，用同一个预测核心在七类系统上完成了验证。这七个评估领域分别是视觉、生物学、临床轨迹、控制、分子动力学、物理场和天气。 如果同一个预测核心能够跨如此不同的领域迁移，将为世界模型研究提供有力支撑，推动其从逐 token 生成转向抽象表征预测，并可能改变科学和工程应用中预测模型的构建方式。 根据论文，JEPA-Anything 在与匹配的 JEPA 基线对比中，于全部 10 个动力学任务上提升了报告指标，并将 Interventional Pong 上的单干预预测误差降低了 34.8%。该工作被定位为一个统一的预测核心，而非特定领域的模型，不过目前可获得的摘要仅为标题级别，缺少一手基准测试和详细的消融实验。

rss · BALA AI News · Sep 19, 08:31

**背景**: JEPA 即联合嵌入预测架构，是一种自监督方法，通过预测输入的抽象表征来学习，而不是重建原始像素或生成 token。Meta 曾推动 V-JEPA 和 VL-JEPA 等 JEPA 变体，将其作为通往世界模型的另一条路径，而 JEPA-Anything 则进一步检验同一个预测核心能否泛化到差异极大的科学与工程领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.20800">JEPA - Anything : Learning Predictive Models across Different Worlds</a></li>
<li><a href="https://github.com/Gen-Verse/JEPA-Anything">GitHub - Gen-Verse/ JEPA - Anything · GitHub</a></li>
<li><a href="https://paperswithcode.co/paper/2609.20800">JEPA - Anything : Learning Predictive Models... | Papers with Code</a></li>

</ul>
</details>

**标签**: `#JEPA`, `#world-models`, `#representation-learning`, `#AI-research`, `#cross-domain`

---