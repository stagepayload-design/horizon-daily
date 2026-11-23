# Horizon 每日速递 - 2026-11-23

> From 52 items, 9 important content pieces were selected

---

1. [Lean 与 Mathlib 社区确认 Alpöge-Claude 黎曼猜想形式化证明正确](#item-1) ⭐️ 9.0/10
2. [Anthropic 数学家称借助 Claude 证明三维纳维-斯托克斯方程爆破](#item-2) ⭐️ 8.0/10
3. [Masullo 黎曼猜想证明的 Lean 形式化进度图引发争议](#item-3) ⭐️ 7.0/10
4. [OpenAI 探讨困惑度作为模型智能的衡量标准](#item-4) ⭐️ 7.0/10
5. [报告预测 Anthropic 2028 年电力结构为 87%天然气、11%煤炭](#item-5) ⭐️ 7.0/10
6. [C++26 在 2026 年 11 月 ISO C++会议上再次定稿](#item-6) ⭐️ 7.0/10
7. [阿尼尔·塞斯在《Noema》撰文挑战有意识 AI 的神话](#item-7) ⭐️ 7.0/10
8. [Signal 默认屏蔽应用内截图，阻止 AI 智能体读取私聊](#item-8) ⭐️ 7.0/10
9. [群联推出内置 NPU 与 64GB 内存的企业级 SSD，可在盘上运行 AI](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Lean 与 Mathlib 社区确认 Alpöge-Claude 黎曼猜想形式化证明正确](https://www.huxiu.com/article/4907474.html) ⭐️ 9.0/10

Lean 与 Mathlib 社区已独立验证，由 Levent Alpöge 与 AI 系统 Claude 合作产生的黎曼猜想形式化证明是正确的。这一确认超越了作者最初的声明，通过社区审查确立了证明的有效性。 这是 AI 辅助数学和形式化验证的一个重大里程碑，表明 AI 能够为解决数学中最著名的未解决问题之一做出贡献，并且结果可以被社区严格检查。这可能会加速形式化方法在数学研究中的采用，并增强对 AI 生成证明的信心。 形式化证明大约有 1700 万行，并在 Lean 证明助手中进行了检查；麻省理工学院数学家 Andrew Sutherland 的独立检查还涵盖了 Dirichlet L 函数的广义黎曼猜想。原始来源较为简短且缺乏主要链接，因此一些细节仍有待完整记录。

rss · BALA AI News · Nov 22, 05:31

**背景**: 黎曼猜想由 Bernhard Riemann 于 1859 年提出，断言黎曼ζ函数的所有非平凡零点的实部均为 1/2，是克雷数学研究所的千禧年大奖难题之一。Lean 是一种用于形式化验证的函数式编程语言和定理证明器，而 Mathlib 是其社区驱动的形式化数学库，截至 2025 年 5 月已包含超过 21 万个定理。形式化验证涉及以机器可检查的格式编写证明，以确保超越人工审查的正确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper.pdf">The Alpoge-Claude proof of the Riemann hypothesis explained for...</a></li>
<li><a href="https://kingy.ai/blog/levent-alpoge-claude-riemann-hypothesis-proof/">Riemann hypothesis proof verified in Lean</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区讨论强调了独立验证的重要性，一些人指出这提升了 AI 辅助证明的可信度。然而，仍有人担心缺乏原始来源，以及需要更广泛的数学社区进一步审查。

**标签**: `#formal-verification`, `#Lean`, `#Mathlib`, `#AI-for-mathematics`, `#Riemann-Hypothesis`

---

<a id="item-2"></a>
## [Anthropic 数学家称借助 Claude 证明三维纳维-斯托克斯方程爆破](https://www.qbitai.com/2026/11/511870.html) ⭐️ 8.0/10

Anthropic 的一位数学家声称，Claude 协助证明了三维纳维-斯托克斯方程的有限时间爆破，但该结果尚未经过独立核验，也未完成正式整理。陶哲轩评论称策略清楚，但仍需规范整理。 如果三维纳维-斯托克斯方程的爆破证明得到确认，将解决克雷千禧年大奖难题之一，并成为 AI 辅助前沿数学研究的里程碑式示范。即便目前只是未经核验的主张，这也表明 AI 模型正越来越多地被用于针对开放问题的严肃研究。 该主张针对无外力作用的三维不可压缩纳维-斯托克斯方程，其爆破被认为比有外力情形困难得多；据报道，Levent（Anthropic）与 Tristan（NYU）在 AI 辅助和大量人工引导下，已就三维欧拉方程等相关问题取得爆破结果。该消息来自二手报道而非原始论文，独立核验与形式化整理仍待完成。

rss · BALA AI News · Nov 22, 06:30

**背景**: 纳维-斯托克斯方程的存在性与光滑性问题是克雷数学研究所选定的七个千禧年大奖难题之一，完整正确的证明可获得 100 万美元奖金。该问题追问三维不可压缩纳维-斯托克斯方程的光滑解是否对所有时间都存在，还是会在有限时间内失效，即所谓“爆破”。解决该问题必须严格证明这两种情形之一，而无外力情形至今仍未解决。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier–Stokes_existence_and_smoothness">Navier – Stokes existence and smoothness - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/posts/flaviusburca_openai-shared-a-solution-to-the-navier-stokes-activity-7503390571684843520-Z0iL">OpenAI shared a solution to the Navier - Stokes Millennium Prize...</a></li>
<li><a href="https://arte-soft.com/discoveries/openai-3d-navier-stokes-singularity/">3 D Navier - Stokes Finite-Time Singularity Claim (BKM Blow - Up )</a></li>

</ul>
</details>

**标签**: `#AI-for-math`, `#Navier-Stokes`, `#Anthropic`, `#Claude`, `#research-verification`

---

<a id="item-3"></a>
## [Masullo 黎曼猜想证明的 Lean 形式化进度图引发争议](https://claude.ai/artifact/CtQyX8qfYAF822bgHJHHE3) ⭐️ 7.0/10

针对 Alessandro Masullo 声称证明广义黎曼猜想的稿件，一个 Lean 形式化进度图已发布，但评论者和专家对该证明的有效性以及 AI 在数学研究中的作用提出了严重质疑。 这一事件凸显了 AI 和 Lean 等形式化验证工具在数学中日益增长的使用，同时也暴露了过早声明的风险以及在高风险数学突破中进行严格同行评审的重要性。 进度图并不代表证明已被验证；一个漏洞就可能使整个论证失效，Brian Conrad 等专家表示稿件需要重大修订，且已有针对关键一致有界性断言的反例被发表。

hackernews · Qision · Nov 22, 23:12 · [社区讨论](https://news.ycombinator.com/item?id=50605045)

**背景**: Lean 是一个交互式定理证明器，允许数学家以机器可检查的语言编写证明，AI 系统越来越多地被用于将非形式证明自动形式化到 Lean 中。广义黎曼猜想是数论中一个重要的未解决问题，Masullo 的稿件声称证明了它，但该工作尚未经过同行评审或验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.scientificamerican.com/article/dueling-claims-of-riemann-hypothesis-proofs-emerge/">Dueling claims of Riemann hypothesis proofs ... | Scientific American</a></li>
<li><a href="https://philarchive.org/rec/NIEIOM">Jenny Lorraine Nielsen, Invalidity of Masullo 's Proof of... - PhilArchive</a></li>
<li><a href="https://www.nacionale.com/en/articles/who-is-alessandro-masullo-all-human-riemann-hypothesis-proof-grh-ravi-vakil-stanford">Masullo 's GRH draft: Stanford PhD, 'all human, no AI'</a></li>

</ul>
</details>

**社区讨论**: 评论者对该证明的有效性表示怀疑，指出原发布者 Ravi Vakil 甚至没有阅读 Masullo 的文件，而 Brian Conrad 表示需要重大修订。一些人还对 AI 在数学中的作用表示担忧，认为它可能削弱人类数学工作的价值。

**标签**: `#Lean`, `#formal verification`, `#AI for mathematics`, `#proof assistants`, `#mathematical claims`

---

<a id="item-4"></a>
## [OpenAI 探讨困惑度作为模型智能的衡量标准](https://openai.com/index/perplexity-and-intelligence/) ⭐️ 7.0/10

OpenAI 发表了一篇文章，探讨困惑度与模型智能之间的关系，引发了关于在基于强化学习（RL）的训练兴起之际，交叉熵损失是否仍是有意义的基准的辩论。这篇文章在 Hacker News 上引发了 467 分和 321 条评论的实质性讨论。 这很重要，因为困惑度和交叉熵损失几十年来一直是评估语言模型的基本指标，但强化学习微调的日益使用引发了这些指标是否仍与模型能力相关的疑问。讨论强调了随着模型变得更加复杂，需要简单、可解释的基准。 困惑度衡量模型平均预测下一个词元的能力，值越低表示预测越好；其范围从 1（完美预测）到词汇表大小（随机预测）。文章指出尽管有 RL 训练，交叉熵损失的趋势仍然清晰，但社区成员指出文章未正式定义困惑度，并质疑讨论中缺失 GPT-4.5。

hackernews · acossta · Nov 22, 17:06 · [社区讨论](https://news.ycombinator.com/item?id=50601525)

**背景**: 困惑度是自然语言处理中的标准指标，量化语言模型对词元序列的“惊讶”程度；它数学上源自交叉熵损失。交叉熵损失是语言模型的默认训练目标，衡量预测概率分布与真实分布之间的差异。强化学习（RL）已流行用于微调模型以符合人类偏好，可能优化超越下一词元预测的目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mbrenndoerfer.com/writing/perplexity-language-model-evaluation-metric">Perplexity : The Standard Language Model Metric - Interactive</a></li>
<li><a href="https://www.analyticsvidhya.com/blog/2025/04/cross-entropy-loss-in-language-model-evaluation/">Cross Entropy Loss in Language Model Evaluation - Analytics Vidhya</a></li>
<li><a href="https://computationallinguistics.com/Cross_Entropy_Loss">Cross - Entropy Loss — Computational Linguistics Reference</a></li>

</ul>
</details>

**社区讨论**: 社区成员进行了技术辩论：一些人澄清了困惑度的定义（例如 hazrmard 解释为惊讶程度，范围从 1 到词汇表大小），而其他人对尽管有 RL 训练交叉熵损失趋势仍然清晰表示惊讶（jrflo 称其“令人震惊”且是“简单的基准”）。d_burfoot 认为困惑度与智能的对应关系并不意外，将预测与压缩联系起来，并引用了 2008 年的一篇论文。

**标签**: `#AI/ML`, `#language models`, `#perplexity`, `#benchmarking`, `#OpenAI`

---

<a id="item-5"></a>
## [报告预测 Anthropic 2028 年电力结构为 87%天然气、11%煤炭](https://betterdatacenterproject.com/2026/11/16/how-ai-is-powered-a-breakdown-of-byop-and-grid-power/) ⭐️ 7.0/10

Better Data Center Project 的一份报告预测，Anthropic 在 2028 年的电力消耗将 87%来自天然气、11%来自煤炭，这一预测基于其签约电力来源和电网电力。该预测在 Hacker News 上引发了大规模讨论，获得 874 分和 883 条评论，聚焦 AI 数据中心能源外部性和企业责任。 这凸显了 AI 数据中心快速扩张对气候的影响，因为像 Anthropic 这样的主要 AI 公司正锁定多年的化石燃料电力。这引发了关于企业问责制以及是否需要监管来防止外部性转嫁给当地社区的疑问。 这些数据来自单一倡导性来源，尚未经过独立验证；报告将 Anthropic 的预计排放量与谷歌、微软和 Meta 最新可持续发展报告中的基于位置的 Scope 2 排放量进行了比较。分析聚焦于电力来源，包括自带电力（BYOP）和电网电力。

hackernews · happosai · Nov 22, 08:57 · [社区讨论](https://news.ycombinator.com/item?id=50597612)

**背景**: AI 数据中心消耗大量电力，其快速增长引发了对碳排放和当地污染的担忧。谷歌和微软等公司已做出可再生能源承诺，但能源结构差异很大。“Scope 2”排放指购买电力产生的间接排放，“基于位置”意味着使用数据中心运营所在地的电网平均强度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://betterdatacenterproject.com/2026/11/16/how-ai-is-powered-a-breakdown-of-byop-and-grid-power/">How AI is powered : a breakdown of BYOP and grid power</a></li>
<li><a href="https://news.ycombinator.com/item?id=50597612">87% of the Anthropic power will come from gas and 11% from coal in...</a></li>
<li><a href="https://www.technologyreview.com/2025/05/20/1116327/ai-energy-usage-climate-footprint-big-tech/">We did the math on AI ’s energy footprint. | MIT Technology Review</a></li>

</ul>
</details>

**社区讨论**: 评论者批评 Anthropic 租赁天然气数据中心（如孟菲斯的 Colossus 1）且缺乏美国可再生能源承诺，一些人呼吁通过监管将外部性内部化。其他人指出数据中心能源使用规模巨大，并认为 AI 正在加速气候变化，而短期财务激励有利于化石燃料。

**标签**: `#AI energy`, `#data centers`, `#Anthropic`, `#climate`, `#regulation`

---

<a id="item-6"></a>
## [C++26 在 2026 年 11 月 ISO C++会议上再次定稿](https://herbsutter.com/2026/11/21/c26-is-done-again-trip-report-november-2026-iso-c-standards-meeting-buzios-brazil/) ⭐️ 7.0/10

在 2026 年 11 月于巴西布济奥斯举行的 ISO C++会议上，委员会第二次完成了 C++26 的技术工作，并在解决国家机构（NB）意见后保留了契约（contracts）特性。Herb Sutter 的行程报告确认 C++26 现已再次定稿，尽管此前存在争议，契约设计仍被保留。 这一里程碑意味着 C++26 重新回到发布轨道，为开发者提供了包括契约在内的新特性的稳定目标，契约旨在提高代码安全性和自文档化能力。该决定也表明了委员会在 C++与 Rust 在内存安全和打包方面竞争持续辩论中的优先事项。 契约将作为实验性特性在 GCC 16 中提供，而 Clang 实现尚未合并，若干相关部分已推迟到 C++29。来自法国、西班牙和芬兰的国家机构意见曾要求标准化前积累更多实现经验，并建议以技术规范或白皮书作为替代路径。

hackernews · dverlaeckt80 · Nov 22, 15:59 · [社区讨论](https://news.ycombinator.com/item?id=50600838)

**背景**: C++26 是 ISO C++标准的下一个主要修订版，由 WG21 委员会通过包括国家机构意见处理在内的流程开发。契约是一种语言特性，允许程序员在函数签名中直接表达前置条件、后置条件和断言，帮助编译器优化和工具验证代码。此前会议上对契约的拒绝曾引发 C++26 可能延迟的猜测，但委员会最终解决了意见并保留了该特性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://herbsutter.com/2026/11/21/c26-is-done-again-trip-report-november-2026-iso-c-standards-meeting-buzios-brazil/">C++26 is done (again)! — Trip report: November 2026 ISO C++ ...</a></li>
<li><a href="https://train-it.eu/blog/cpp26-contracts-experience-and-process/">Were C+ + 26 contracts tried enough, and how were the... | Train IT</a></li>
<li><a href="https://isocpp.org/blog/category/standardization">Standardization : Standard C++</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分歧：一些人认为应移除契约并推迟到 C++29，指出未解决的问题和仓促的流程；另一些人批评委员会优先考虑小众特性，而非 C++落后于 Rust 的打包和内存安全等紧迫问题。少数人为委员会辩护，称其处理了 NB 意见并使 C++26 重回正轨，还有人指出契约实际上是 WG21 流程中较少出现功能障碍的部分之一。

**标签**: `#C++`, `#ISO standards`, `#programming languages`, `#contracts`, `#software engineering`

---

<a id="item-7"></a>
## [阿尼尔·塞斯在《Noema》撰文挑战有意识 AI 的神话](https://www.noemamag.com/the-mythology-of-conscious-ai/) ⭐️ 7.0/10

阿尼尔·塞斯在《Noema》杂志发表题为《有意识 AI 的神话》的文章，认为意识与生物生命密不可分，并挑战了复杂计算能产生意识的假设。该文荣获伯格鲁恩研究所征文奖，并在 Hacker News 上引发了 470 条评论的热烈讨论。 随着 AI 能力不断提升，AI 系统能否产生意识成为重要伦理与监管议题，塞斯的文章对此进行了深入探讨。他提出的生物自然主义立场促使研究者明确何种证据能证明数字系统具有意识，从而影响 AI 意识研究的未来方向。 塞斯的论证并不要求意识研究者全盘接受生物自然主义，但要求他们明确何种证据能说服自己数字系统具有意识。文章严谨地挑战了仅凭复杂计算就能产生意识的观点。

hackernews · Anon84 · Nov 22, 02:10 · [社区讨论](https://news.ycombinator.com/item?id=50595537)

**背景**: 意识研究横跨心灵哲学与神经科学，主观体验的“难问题”在科学上仍难以解决。阿尼尔·塞斯是著名神经科学家，以预测处理理论和“意识是受控幻觉”的观点闻名。《Noema》杂志是伯格鲁恩研究所旗下的出版物，探讨技术的哲学与文化维度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.noemamag.com/only-what-is-alive-can-be-conscious/?trk=article-ssr-frontend-pulse_x-social-details_comments-action_comment-text">Only What Is Alive Can Be Conscious</a></li>
<li><a href="https://theconsciousness.ai/posts/anil-seth-mythology-conscious-ai-biological-naturalism-noema-2026/">Anil Seth Mythology of Conscious AI ... | The Consciousness AI</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为意识在科学上难以捉摸且可能不可证伪，一些人指出不能排除 AI 具有意识的可能。另一些人则关注赋予 AI 意识所带来的伦理问题，例如使用有意识的智能体集群是否等同于奴役，并对文章“扮演上帝”的表述提出批评。

**标签**: `#AI consciousness`, `#philosophy of mind`, `#AI ethics`, `#frontier technology`, `#Hacker News discussion`

---

<a id="item-8"></a>
## [Signal 默认屏蔽应用内截图，阻止 AI 智能体读取私聊](https://www.ithome.com/0/1030/517.htm) ⭐️ 7.0/10

Signal 现在在 iOS 27 和 Android 上默认屏蔽应用内截图，专门阻止 Siri、Gemini 等系统级 AI 助手捕获并读取屏幕上的私密消息。希望截图的用户可以在 Signal 设置中关闭此保护。 此举使 Signal 成为对抗 AI 监控的隐私捍卫者，因为 AI 智能体日益与操作系统集成并能访问屏幕内容。这可能促使其他通讯应用采取类似保护措施，并引发关于用户控制权与平台级 AI 访问之间平衡的讨论。 该保护在 iOS 27 和 Android 上阻止 AI 助手尝试捕获屏幕数据时对 Signal 应用内截图；这建立在 Signal 此前在 Windows 应用中默认阻止截图的基础上。然而，通过另一台设备进行物理拍摄仍然可行，且 Signal 在 macOS 上尚未实现对 Siri 和 Gemini 的同等保护。

rss · BALA AI News · Nov 22, 06:31

**背景**: Signal 是一款广泛使用的端到端加密通讯应用，以其强大的隐私保护著称。苹果 Siri 和谷歌 Gemini 等系统级 AI 智能体可以访问屏幕内容以提供情境化协助，这引发了私密消息在未经用户明确同意下被读取的担忧。Signal 此前已在其 Windows 应用中默认阻止截图，现在将类似保护扩展到移动平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://signal.org/blog/protecting-your-privacy/">Signal >> Blog >> Signal is Serious About Protecting Your Privacy</a></li>
<li><a href="https://techcrunch.com/2026/11/21/signal-restricts-mobile-screenshots-as-it-confronts-existential-threat-of-ai-surveillance/">Signal restricts mobile screenshots as it confronts... | TechCrunch</a></li>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/1038390/signal-blocking-ai-agent-screenshots-mobile-app">Signal is blocking Gemini and Siri AI from reading your... | The Verge</a></li>

</ul>
</details>

**标签**: `#privacy`, `#Signal`, `#AI agents`, `#messaging security`, `#screenshot protection`

---

<a id="item-9"></a>
## [群联推出内置 NPU 与 64GB 内存的企业级 SSD，可在盘上运行 AI](https://www.ithome.com/0/1030/524.htm) ⭐️ 7.0/10

在 SC26 大会上，群联展示了一款计算存储企业级 SSD，集成了提供 36,800 DMIPS 算力的 NPU 和 64GB 内存（带宽 130 GB/s），可直接在盘上运行 AI 模型。该硬盘支持 PyTorch 和 llama.cpp 框架，使得推理能够在存储设备内部执行。 这代表了一种新颖的计算存储架构，可能将 AI 推理推向更靠近数据的位置，减少数据移动和延迟，适用于边缘或数据密集型工作负载。如果实现商业化，它可能使存储设备参与计算，从而实现更高效、可扩展的 AI 部署，影响企业数据中心和 AI 基础设施设计。 NPU 提供 36,800 DMIPS 的算力，64GB 内存提供 130 GB/s 带宽，是潜在 PCIe 6.0 主机带宽（最高 28 GB/s）的 4 倍以上。群联还在 SC26 上展示了混合介质 pSLC 和 QLC 硬盘，但这款计算存储 SSD 是一项技术演示，尚未宣布产品上市时间或独立基准测试。

rss · BALA AI News · Nov 22, 06:31

**背景**: 计算存储是指包含处理能力的存储设备，可在数据附近或之上执行计算，减少将数据传输到主机 CPU 的需求。NPU 代表神经网络处理单元，是一种用于神经网络工作负载的专用加速器。SC26 是 2026 年超级计算大会，是高性能计算和存储技术的重要活动。群联是 NAND 闪存控制器和企业级 SSD 的领先供应商。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/ssds/phison-details-ssd-with-a-built-in-npu-and-64gb-of-memory-that-supports-pytorch-and-llama-cpp-running-on-the-drive-second-design-merges-fast-pslc-cache-and-qlc-capacity-behind-one-controller">Phison details SSD with a built-in NPU and 64GB of... | Tom's Hardware</a></li>
<li><a href="https://www.phison.com/sc26-phison-unveils-three-next-generation-storage-innovations-for-the-new-compute-era/">SC 26 : Phison Unveils Three Next-Generation Storage Innovations for...</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#storage`, `#NPU`, `#compute-in-storage`, `#enterprise SSD`

---

