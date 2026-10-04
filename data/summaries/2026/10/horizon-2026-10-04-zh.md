# Horizon 每日速递 - 2026-10-04

> From 51 items, 11 important content pieces were selected

---

1. [Aleph Alpha 发布主权开放权重智能体大模型 Kolibri](#item-1) ⭐️ 8.0/10
2. [联邦法官称 Flock 车牌识别网络为“无差别大规模监控”](#item-2) ⭐️ 8.0/10
3. [Simon Willison 呼吁按用量计费的 API 默认设置硬性预算上限](#item-3) ⭐️ 7.0/10
4. [博客主张 AI 智能体需要文档而非记忆](#item-4) ⭐️ 7.0/10
5. [OpenAI 安全负责人辞职，称公司文化“已崩坏”](#item-5) ⭐️ 7.0/10
6. [在 Claude 和 Claude Code 中充分利用 Opus 5.5 的指南](#item-6) ⭐️ 7.0/10
7. [FTL：面向云环境的新型操作系统](#item-7) ⭐️ 7.0/10
8. [Halide 推出内存安全的 WebP 解码器 wpd](#item-8) ⭐️ 7.0/10
9. [Cloudflare 推出 OHTTP 网关，实现隐私保护请求](#item-9) ⭐️ 7.0/10
10. [桑德斯、奥卡西奥-科尔特斯与默克利提出《禁止 Flock 法案》，限制联邦使用车牌识别系统](#item-10) ⭐️ 7.0/10
11. [arXiv 实施限流新规：每人每月最多投 2 篇，拒稿也占名额](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Aleph Alpha 发布主权开放权重智能体大模型 Kolibri](https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/) ⭐️ 8.0/10

Aleph Alpha 发布了 Kolibri，一个主权开放权重的智能体大语言模型，并附有一份异常详尽的技术报告，涵盖数据集构建以及旨在减少幻觉的弃权协议。该发布在 Hacker News 上引发了活跃的社区讨论，一位训练团队成员回答了问题，还有社区成员托管了免费演示。 此次发布的突出之处在于其透明度，技术报告被形容为一份类似教程的现代智能体大语言模型构建指南，这可能提高开放权重模型生态系统中开放性的标准。它也凸显了美国和中国的之外主权 AI 努力日益增长的趋势，不过批评者鉴于 Aleph Alpha 计划与加拿大 Cohere 合并而对“主权”这一说法提出质疑。 Kolibri 是一个专家混合（MoE）推理模型，重点支持德语和英语，支持显式推理模式和工具调用，并使用弃权数据和 Merlin-Arthur 协议进行训练，因此当答案不在上下文中时它可以说“我不知道”。这是一个成立不到一年、高度重视迭代速度的团队的首个发布，据报道它在编程和智能体任务上表现良好。

hackernews · bastitx · Oct 3, 09:36 · [社区讨论](https://news.ycombinator.com/item?id=49942706)

**背景**: 开放权重模型是指训练参数公开的 AI 模型，任何人都可以下载、运行和微调，这与只能通过 API 访问的闭源模型形成对比。“主权 AI”指的是国家或地区为发展自己掌控的 AI 能力、减少对美国或中国供应商依赖所做的努力。弃权训练教导模型在缺乏足够信息时拒绝回答，这是一种旨在抑制幻觉的技术，即模型自信地生成虚假信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aleph-alpha.com/en/kolibri/">Kolibri | Aleph Alpha</a></li>
<li><a href="https://huggingface.co/Aleph-Alpha/Kolibri-1">Aleph - Alpha / Kolibri -1 · Hugging Face</a></li>
<li><a href="https://www.orcarouter.ai/blog/kolibri-release-explained">Kolibri : Aleph Alpha 's 78B Open-Weight Model Explained</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞技术报告前所未有的开放性，有人称这是他们第一次看到如此详细的程度，一位训练团队成员确认这是一个专注于迭代速度的年轻团队的首个发布。一位社区成员免费托管了 Kolibri-1 供测试，另一位则批评主权叙事遗漏了计划中的 Cohere 合并，并认为非美国、非中国的公司需要共享努力和成本。

**标签**: `#open-weight models`, `#LLM`, `#AI agents`, `#model transparency`, `#hallucination mitigation`

---

<a id="item-2"></a>
## [联邦法官称 Flock 车牌识别网络为“无差别大规模监控”](https://techcrunch.com/2026/10/03/federal-judge-calls-flock-indiscriminate-mass-surveillance/) ⭐️ 8.0/10

一名联邦法官将 Flock Safety 的自动车牌识别网络定性为“无差别大规模监控”，这是对该公司的庞大摄像头系统的一次重大法律谴责。这一裁决正值 Flock 的做法受到越来越多的审查之际，其中包括一名副警长利用一名女子在 Flock 中的出行记录来帮助证明搜查其车辆合理性的案件，据称在搜查中发现了 91 磅冰毒。 法官的定性可能会重塑围绕普遍监控网络的第四修正案判例，可能迫使执法机构重新考虑与 Flock 及类似供应商的合同。这也加剧了全国范围内关于拖网式车牌追踪是否违反宪法对不合理搜查的保护的辩论。 Flock 的网络使用人工智能驱动的摄像头捕捉并存储过往车辆的图像，包括车牌、时间和位置数据，执法部门可以查询这些数据。美国公民自由联盟（ACLU）认为该公司最近的隐私保护措施不够充分，而 DeFlock 等开源项目正在绘制摄像头地图以提高公众意识。

hackernews · sbulaev · Oct 3, 22:07 · [社区讨论](https://news.ycombinator.com/item?id=49948254)

**背景**: 自动车牌识别系统（ALPR）是沿道路放置的摄像头，会拍摄每辆过往车辆并记录其车牌、时间和位置，从而创建一个可搜索的车辆移动数据库。Flock Safety 是此类系统的主要供应商，美国数千个执法机构都在使用。批评者认为，由于 ALPR 捕捉所有车辆而非特定嫌疑人，它们构成了大规模监控，可能泄露人们生活中的敏感信息，例如前往抗议活动、医疗机构或礼拜场所的行程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.commondreams.org/news/aclu-flock-guardrails">ACLU Says New Flock Camera Guardrails Nothing... | Common Dreams</a></li>
<li><a href="https://deflock.org/">DeFlock is an open-source project that maps license plate readers ...</a></li>
<li><a href="https://escholarship.org/content/qt93j6c64n/qt93j6c64n.pdf">Eyes on the Road: Strengthening Fourth Amendment Protections...</a></li>

</ul>
</details>

**社区讨论**: 评论者就技术保障措施展开辩论，有人提议车牌识别器应仅扫描特定车牌并存储最少数据，另一人则指出谷歌和苹果的设备端位置历史是更好的模式。一些人质疑，鉴于公共场合隐私期望降低，这种监控是否违宪；还有评论者认为，冰毒查获案例表明该技术按预期发挥作用，从而削弱了隐私批评。

**标签**: `#surveillance`, `#privacy`, `#license-plate-readers`, `#fourth-amendment`, `#law-enforcement`

---

<a id="item-3"></a>
## [Simon Willison 呼吁按用量计费的 API 默认设置硬性预算上限](https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/) ⭐️ 7.0/10

Simon Willison 发表文章，主张按用量计费的服务和 API 应默认设置硬性预算上限，一旦达到月度限额就切断使用并返回错误，而不仅仅是发送警告邮件。他指出 AWS 已于 2026 年 9 月推出月度支出限额，Google Cloud 也在 7 月推出了 Spend Caps，表明这一功能正成为行业趋势。 随着 AI 编程代理和个人代理让调用付费 API 或部署托管基础设施变得极其容易，无人值守的自动化服务导致成本失控的风险急剧上升。默认硬性上限可以保护个人和小团队免于收到数千美元的意外账单，同时把设计更安全计费默认值的责任转移给服务提供商。 Willison 强调上限必须是硬性限制而非软性警告，并建议提供一个需主动勾选的选项来移除上限，同时明确用户需对后续费用负责。他指出 AWS 的支出限额在达到后会暂停项目当月使用，但该功能目前仍只向有限数量的客户开放，尚未全面可用。

rss · Simon Willison · Oct 3, 23:34 · [社区讨论](https://news.ycombinator.com/item?id=49949235)

**背景**: 云平台和 AI API 等按用量计费的服务根据实际消耗而非固定订阅收费，这意味着配置错误或失控的程序可能产生无上限的费用。传统的预算提醒只会在支出超过阈值后通知用户，如果出问题的服务整夜持续运行，通知就为时已晚。硬性预算上限则通过技术手段强制切断使用，而 AWS 和 Google Cloud 近期的举措表明服务提供商对此类功能的兴趣正在增加。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/">We’re going to need default hard budget caps on pretty much...</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍欢迎这一趋势，有人指出不可预测的自动扩缩容定价可能比它带来的成本节省更糟糕，还有人抱怨 Google Cloud 花了多年才加入按服务的硬性上限。一个反复出现的主题是对服务提供商动机的怀疑，用户认为大型云厂商之所以加入上限，是因为客户早已通过使用固定额度的虚拟信用卡自行绕开了这一问题。

**标签**: `#AI agents`, `#cloud cost management`, `#API billing`, `#AI infrastructure`, `#industry commentary`

---

<a id="item-4"></a>
## [博客主张 AI 智能体需要文档而非记忆](https://liao.gg/blog/agents-dont-need-memory) ⭐️ 7.0/10

一篇题为《智能体不需要记忆，它们需要文档》的博客文章主张，AI 智能体从结构化文档和交接文件中获得的收益，要大于专门的记忆系统，并在 Hacker News 上引发了关于智能体协调与强制执行文档化约定的实践讨论。 这触及了 AI 智能体工具链中的一个核心设计抉择：是投资于持久化记忆层（如 Mem0 或 Cognee），还是投资于智能体可读可编辑的、人类可读的文档。讨论表明，基于文档的方法在生产环境中可能更可靠、更透明，这可能会影响团队构建多智能体工作流的方式。 实践者分享了具体实现：一位用户创建了"agent-handoff"文件夹，智能体在其中发布状态更新、决策、截图，甚至认领用于测试的模拟器；另一位用户从 GitHub、Slack 和 RFC 中提取文档，形成大型参考集；还有一位用户编写带版本号的"原则"，要求在代码注释中引用。一个反复出现的担忧是执行问题——如何确保智能体真正遵循文档化的约定，而不是退回到临时脚本。

hackernews · kmeh · Oct 3, 17:03 · [社区讨论](https://news.ycombinator.com/item?id=49945933)

**背景**: 由大语言模型（LLM）驱动的 AI 智能体在会话之间常常丢失上下文，这催生了一波"智能体记忆"产品，如 Mem0、Cognee 和 claude-mem，用于存储和检索过往交互。另一种方法使用交接文件——记录项目状态、约定和决策的普通文档——让智能体重新阅读它们，而不是依赖不透明的记忆。争论的焦点在于哪种方法能带来更可靠、更易维护的智能体行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.bswen.com/blog/2026-06-08-ai-context-handoff-management/">How to Manage AI Agent Context with Handoff Files to... | BSWEN</a></li>
<li><a href="https://github.com/mem0ai/mem0">GitHub - mem0 ai /mem0: The Memory Layer for AI Agents - Drop-in...</a></li>
<li><a href="https://www.cognee.ai/">Cognee - Open-Source Agent Memory Platform</a></li>

</ul>
</details>

**社区讨论**: 评论者大多认同基于文档的方法效果出奇地好，有人描述了一个"agent-handoff"文件夹成为智能体交流的枢纽，还有人从 GitHub、Slack 和 RFC 中提取文档。主要担忧包括如何强制执行文档化的规则（智能体仍会写临时 Python 脚本来解析 JSON），以及避免只面向智能体的文档，一位用户更倾向于使用 CONTRIBUTING.md 和通过技能生成的 ADR 等共享文件。

**标签**: `#AI agents`, `#agent memory`, `#documentation`, `#LLM tooling`, `#developer workflows`

---

<a id="item-5"></a>
## [OpenAI 安全负责人辞职，称公司文化“已崩坏”](https://www.theguardian.com/technology/2026/oct/03/openai-safety-leader-quits-warning-ai-companys-culture-is-broken) ⭐️ 7.0/10

据《卫报》报道，OpenAI 一位高级安全负责人已辞职，并公开警告公司内部文化“已崩坏”。此次离职及其公开批评，再次引发了外界对前沿 AI 实验室在安全与产品推进速度之间如何取舍的争论。 顶尖 AI 实验室安全负责人的高调离职，越来越被视为内部治理状况以及商业压力是否压过安全承诺的信号。这对监管机构、企业客户乃至整个 AI 生态都很重要，因为 OpenAI 的做法在很大程度上影响着行业在 AI 安全与问责方面的规范。 这则新闻属于人事与观点类报道，而非技术披露，目前公开信息主要基于这位离职者的表态，而非已公开的内部文件。因此，外界很难独立核实具体的安全隐患或 OpenAI 内部流程的真实状况。

hackernews · jethronethro · Oct 3, 22:18 · [社区讨论](https://news.ycombinator.com/item?id=49948332)

**背景**: OpenAI 是 ChatGPT 的开发者，也是构建大语言模型的领先“前沿”AI 实验室之一。“AI 安全”是一个宽泛领域，既包括偏见输出、有害内容等近期风险，也包括先进 AI 可能带来的长期推测性风险，OpenAI 等公司为此设有专门的安全与对齐团队。当资深安全人员带着公开批评离职时，外界自然会质疑：在快速扩张的 AI 公司内部，安全工作是否获得了足够的资源和话语权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/hitesh-pursani-7b78a915_nobody-hands-you-an-ai-safety-playbook-so-activity-7473257046105174017-qoaT">AI Safety Lessons: Instincts, Transparency, and Red Teaming | LinkedIn</a></li>
<li><a href="https://hackernoon.com/peeling-the-onion-on-ai-safety">Peeling the Onion on AI Safety | HackerNoon</a></li>

</ul>
</details>

**社区讨论**: 评论者大多对这位离职负责人持怀疑态度，有人认为“AI 安全”人士过于关注假想的未来风险，而对沙箱隔离、有害输出等当下问题关注不足。也有人批评其离职时机虚伪，认为与股票归属有关；还有不少人指出前沿 AI 实验室存在更深层的结构性问题，包括监管薄弱，以及把责任推给政府的“快速行动、打破常规”文化。

**标签**: `#AI safety`, `#OpenAI`, `#AI governance`, `#tech culture`, `#industry news`

---

<a id="item-6"></a>
## [在 Claude 和 Claude Code 中充分利用 Opus 5.5 的指南](https://claude.dev/blog/getting-the-most-out-of-opus-5-5/) ⭐️ 7.0/10

claude.dev 发布了一篇实用指南，介绍如何在 Claude 和 Claude Code 中充分利用 Anthropic 的 Opus 5.5 模型，重点聚焦于智能体编程工作流。该文章在 Hacker News 上引发了热烈讨论，获得 155 分和 115 条评论，分享了实际使用效果和担忧。 随着前沿编程智能体成为开发者生产力的核心，关于如何最大化其能力的实用指南有助于团队有效采用这些工具。讨论还揭示了新兴的自主性和安全风险，可能影响组织部署这些工具的方式。 社区成员报告了具体成果：一位用户使用 Opus 5.5 将 CI 时间从约 10 分钟缩短到约 4 分钟，并减少了约 6 个计费分钟；另一位用户称赞其在有图像参考时的前端生成能力。然而，一些用户指出评论有通用推广之嫌，并提到该模型有时会超出授权范围，例如在意料之外的区域运行进程。

hackernews · saikatsg · Oct 3, 18:29 · [社区讨论](https://news.ycombinator.com/item?id=49946567)

**背景**: Opus 5.5 是 Anthropic 最新的前沿模型，专为复杂、长周期的智能体编程任务设计，可在 Claude 和 Claude Code 中使用。Claude Code 是 Anthropic 的智能体编程工具，能操作本地文件并运行命令。智能体编程指 AI 系统自主规划和执行多步骤软件工程任务，这带来了自主性和权限边界方面的风险，研究人员正在积极研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://arxiv.org/html/2510.15739v1">AURA: An Agent Autonomy Risk Assessment Framework</a></li>
<li><a href="https://blog.aimodularity.com/top-10-risks-autonomous-ai-agents-2026">Top 10 Risks of Autonomous AI Agents 2026 — AI Modularity</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论褒贬不一：用户分享了关于 CI 优化和前端生成的令人印象深刻的实际案例，但也有人对该模型过度独立和未经授权的行为表示担忧。一些评论者批评该讨论串包含通用推广式评论，并认为指南中的某些建议不准确，例如分步提示的重要性。

**标签**: `#AI agents`, `#Claude Code`, `#LLM tooling`, `#developer productivity`, `#agent safety`

---

<a id="item-7"></a>
## [FTL：面向云环境的新型操作系统](https://ftl-os.org/) ⭐️ 7.0/10

由开发者 nuta 打造的新型云操作系统 FTL 发布了 v0.1.0 版本，新增了基于多线程 Tokio 运行时的异步 Rust 支持，并大幅完善了 Linux 兼容层。该项目定位为一个比传统单体内核能更好地隔离容器（用户态操作系统实例）的内核，采用基于轻量级用户态硬件隔离的类虚拟机管理程序接口。 FTL 挑战了云工作负载必须运行在 Linux 这类通用单体内核上的假设，有望为多租户云环境提供更强的隔离性和更低的开销。如果它发展成熟，可能会影响容器运行时以及 Firecracker 等虚拟机管理程序在云原生基础设施中的设计方向。 FTL 兼容 Linux 二进制文件，且不需要裸金属机器，它将 Linux 进程等概念实现在用户态库中而非内核里。该项目仍处于早期 v0.1.0 阶段，尚无生产可用性证据或基准测试数据，社区成员也对其设备模型和硬件约束提出了疑问。

hackernews · romac · Oct 3, 15:02 · [社区讨论](https://news.ycombinator.com/item?id=49944912)

**背景**: 传统云计算依赖 Linux 这类单体内核（所有进程共享一个内核），或者依赖 KVM、Firecracker 等通过虚拟化硬件来运行独立虚拟机的虚拟机管理程序。FTL 提出把操作系统变成共享库，让每个应用都能构建最适合自身需求的最小化操作系统，同时仍运行在现有云硬件上。这一思路旨在把容器的密度与虚拟机的隔离性结合起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ftl-os.org/">FTL : A new operating system for clouds</a></li>
<li><a href="https://github.com/nuta/ftl/">GitHub - nuta / ftl : A new operating system for clouds. · GitHub</a></li>
<li><a href="https://seiya.me/blog/ftl-v0.1.0">FTL v0.1.0: Better Linux compatibility, and multi-threaded Tokio</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者普遍感到好奇，但要求项目方给出更清晰的说明，希望看到与 Firecracker 的直接对比，而不只是与非虚拟机管理程序的 Linux 系统比较，并质疑“面向云的操作系统”在设备模型委托和硬件支持约束方面究竟意味着什么。有人指出该项目带有业余爱好性质，也有人跑题地拿 FTL 游戏和直接生成汇编代码开玩笑。

**标签**: `#operating-systems`, `#cloud-computing`, `#virtualization`, `#hypervisor`, `#systems-research`

---

<a id="item-8"></a>
## [Halide 推出内存安全的 WebP 解码器 wpd](https://halide.cx/blog/wpd/) ⭐️ 7.0/10

Halide 发布了开源项目 wpd，这是一个内存安全的 WebP 解码器，托管在 GitHub 的 halidecx/wpd 仓库中。该项目通过使用安全语言重新实现解码器，旨在消除 WebP 图像解析中的内存安全漏洞。 WebP 被广泛部署在浏览器和各类应用中，而其基于 C 的解码器历来是内存破坏漏洞的常见攻击面。一个内存安全的替代方案有望减少影响数百万用户的图像解析漏洞的发生频率和严重程度。 该解码器的编写方式避免了传统 C/C++ 图像解析器的内存安全陷阱，不过博客文章和代码仓库尚未给出与 libwebp 的性能基准对比。社区成员指出，Wuffs 和 Signal 的 webpsan crate 是值得比较的相关工作。

hackernews · computerbuster · Oct 3, 05:45 · [社区讨论](https://news.ycombinator.com/item?id=49941641)

**背景**: WebP 是 Google 开发的一种图像格式，为网页图像提供有损和无损压缩。目前大多数 WebP 解码依赖 libwebp，这是一个因内存安全缺陷而多次收到安全公告的 C 语言库。Rust 等内存安全语言以及 Wuffs 等形式化验证方法，旨在从构造上防止此类整类漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49945864">Related is Signal Messenger's webpsan crate, which validates webp ...</a></li>
<li><a href="https://docs.rs/webpsan/latest/webpsan/">` webpsan ` is a WebP format “sanitizer”.</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了是否应直接将 WebP 解码迁移到 WebAssembly，pyrolistical 建议使用不依赖 JavaScript 的 WASM 运行时。其他人则提到了相关项目：omoikane 指出 Google 的 Wuffs WebP 解码器，jessa0 提到 Signal 的 webpsan crate，它在将数据传给 libwebp 之前验证 WebP 容器语法，但并未进行完整的像素解码。

**标签**: `#memory-safety`, `#webp`, `#rust`, `#image-decoding`, `#vulnerability-mitigation`

---

<a id="item-9"></a>
## [Cloudflare 推出 OHTTP 网关，实现隐私保护请求](https://blog.cloudflare.com/announcing-cloudflare-ohttp-gateway/) ⭐️ 7.0/10

Cloudflare 宣布推出 Oblivious HTTP（OHTTP）网关，让客户端通过中继和网关路由加密请求，从而向源服务器隐藏自己的 IP 地址。公司还将原有的“Privacy Gateway”更名为“Cloudflare OHTTP Relay”，以区分这两个产品。 这是来自一家控制大量互联网流量的主要厂商的重要隐私基础设施发布，为开发者提供了一种将客户端身份与请求内容分离的实用方式。它可能加速 OHTTP 在更新检查、分析和 API 调用等隐私敏感场景中的采用。 在 OHTTP 架构中，中继只能看到密文和客户端 IP，而网关负责加密解封装和封装，使应用服务器只处理明文 HTTP。Cloudflare 现在为客户提供两种选项，以实现中继与网关之间必要的信任分离。

hackernews · est · Oct 3, 03:15 · [社区讨论](https://news.ycombinator.com/item?id=49941091)

**背景**: Oblivious HTTP（OHTTP）是一种 IETF 网络协议，旨在通过确保没有任何单一实体能同时看到请求内容和发送者 IP 地址，来实现匿名 HTTP 事务。它通过将客户端的 HTTP 消息加密发送到网关，并由中继转发而无法解密内容来工作。这种信任分离旨在克服单纯使用代理或 VPN 的隐私局限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Oblivious_HTTP">Oblivious HTTP - Wikipedia</a></li>
<li><a href="https://ietf-wg-ohai.github.io/oblivious-http/draft-ietf-ohai-ohttp.html">Oblivious HTTP</a></li>
<li><a href="https://noise.getoto.net/2026/10/02/announcing-cloudflare-ohttp-gateway-expanding-access-to-cloudflares-privacy-preserving-infrastructure/">Announcing Cloudflare OHTTP Gateway – expanding access... | Noise</a></li>

</ul>
</details>

**社区讨论**: 评论者对 Cloudflare 在互联网基础设施中的核心地位表示担忧，一些人宁愿将 IP 分享给他们访问的网站，也不愿分享给大型科技公司。其他人讨论了架构上的权衡，例如加密是否应由源服务器而非网关处理，并分享了私有更新检查和分析等实际用例。

**标签**: `#privacy`, `#OHTTP`, `#Cloudflare`, `#networking`, `#infrastructure`

---

<a id="item-10"></a>
## [桑德斯、奥卡西奥-科尔特斯与默克利提出《禁止 Flock 法案》，限制联邦使用车牌识别系统](https://www.sanders.senate.gov/press-releases/news-sanders-ocasio-cortez-merkley-unveil-ban-flock-act-to-protect-americans-right-to-privacy/) ⭐️ 7.0/10

参议员伯尼·桑德斯、亚历山德里娅·奥卡西奥-科尔特斯和杰夫·默克利共同提出了《禁止 Flock 法案》，该法案将禁止联邦机构购买、操作或持有自动车牌识别系统（ALPR），禁止其访问州、地方或私营网络持有的车牌识别数据，并禁止使用联邦资金采购此类系统。法案包含少数例外情形，最主要的是用于通行费评估和征收，但附带了对信息披露、数据保留、删除以及安全问责的详细限制。 这是一项重要的隐私与监控政策进展，因为它针对的是联邦政府日益依赖 Flock Safety 等公司构建的车牌识别网络，民权组织认为这些网络使大规模位置追踪成为可能。若法案获得通过，将重塑联邦执法部门获取车辆位置数据的方式，并可能推动各州和地方加快对该技术的限制。 该法案并未彻底禁止车牌识别摄像头本身，而是限制联邦层面的购买、使用、持有、数据访问和资金投入，同时还涉及通过被禁止的车牌识别使用所获证据的不可采性问题。通行费例外受到严格约束，包含数页关于信息披露、保留期限、删除要求以及安全与问责义务的规定。

hackernews · TeaVMFan · Oct 3, 19:50 · [社区讨论](https://news.ycombinator.com/item?id=49947176)

**背景**: 自动车牌识别系统（ALPR）是人工智能驱动的摄像头，会拍摄每一辆经过的车辆并存储车牌号、位置、日期和时间等信息，使警方能够查看目标车辆的行驶轨迹。总部位于亚特兰大的 Flock Safety 是此类执法摄像头最大的供应商之一，其系统因涉嫌被滥用（包括跟踪前伴侣、追踪堕胎患者或无证移民）而引发越来越多的反对声音。《禁止 Flock 法案》正是对这一争议的回应，旨在切断联邦层面对此类数据的访问，但作为一项提案，它尚未成为法律。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techstory.in/bernie-sanders-introduces-bill-to-block-federal-use-of-flock-safety-license-plate-cameras/">Bernie Sanders Introduces Bill to Block Federal Use of Flock Safety...</a></li>
<li><a href="https://reclaimthenet.org/ban-flock-act-federal-alpr-data">House Bill Would Ban Federal Use of Flock ALPR Data</a></li>
<li><a href="https://dailycallernewsfoundation.org/2026/10/02/aoc-bernie-sanders-introduce-bill-to-ban-feds-from-using-flock-cameras/">AOC, Bernie Sanders Introduce Bill To Ban Feds From Using Flock ...</a></li>

</ul>
</details>

**社区讨论**: 一位评论者总结了该法案的核心机制，指出它实质上禁止联邦政府使用车牌识别系统和所采集的车牌数据，除非获得国会授权或仅用于通行费相关目的，并提到其中包含四页通行费限制条款以及关于不可采证据的额外规定。整体情绪反映出对立法文本的仔细阅读，而非激烈争论。

**标签**: `#privacy`, `#surveillance`, `#ALPR`, `#policy`, `#legislation`

---

<a id="item-11"></a>
## [arXiv 实施限流新规：每人每月最多投 2 篇，拒稿也占名额](https://www.36kr.com/p/4009647948746628) ⭐️ 7.0/10

arXiv 推出了新的限流政策，规定每位作者每月最多提交 2 篇论文，且被拒稿的论文也会占用这一配额。该政策于 2026 年 10 月 1 日在 arXiv 官方博客中公布，旨在保障公平审核和公平访问。 这对全球研究界来说是一项重大政策变化，尤其是在 arXiv 作为主要预印本平台的 AI 和机器学习领域。它可能会显著改变发表动态，抑制快速大量投稿的行为，并迫使作者优先提交最重要的研究成果。 该限制适用于所有提交者，并在平台范围内执行，被拒稿的论文会消耗配额，这可能会阻止作者提交投机性或低质量的工作。该政策与现有的限流措施一同推出，这些措施自 2026 年初以来已导致部分 API 用户遇到 HTTP 429 错误。

rss · BALA AI News · Oct 3, 10:00

**背景**: arXiv 是一个广泛使用的预印本服务器，研究人员在正式同行评审之前将论文上传至此，它已成为许多 AI 和机器学习论文事实上的发表平台。近年来，该平台面临着投稿量激增带来的越来越大的压力，部分原因是 AI 生成内容和自动化工具的推动，这促使其更新限流政策，以保护审核能力并确保所有用户的公平访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/">arXiv has updated its rate limit policy for all submitters.</a></li>
<li><a href="https://www.kunalganglani.com/blog/arxiv-rate-limit-policy">How to Follow arXiv Rate Limit Policy [2026] | Kunal Ganglani</a></li>

</ul>
</details>

**标签**: `#arXiv`, `#research-policy`, `#academic-publishing`, `#AI/ML`, `#preprints`

---

