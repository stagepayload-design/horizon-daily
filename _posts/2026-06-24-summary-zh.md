---
layout: default
title: "Horizon Summary: 2026-06-24 (ZH)"
date: 2026-06-24
lang: zh
---

> From 50 items, 18 important content pieces were selected

---

1. [Swift 包索引被苹果收购](#item-1) ⭐️ 8.0/10
2. [开源所见即所得 TikZ 编辑器发布](#item-2) ⭐️ 8.0/10
3. [AI 编码代理需要人类规范，而非循环](#item-3) ⭐️ 8.0/10
4. [Unlimited OCR：一次性长视野解析](#item-4) ⭐️ 8.0/10
5. [不要通过发送垃圾邮件来验证电子邮件地址](#item-5) ⭐️ 8.0/10
6. [谷歌因非官方 CLI 工具解雇员工](#item-6) ⭐️ 8.0/10
7. [GPT-5 助力解决三年免疫学谜题](#item-7) ⭐️ 8.0/10
8. [FUTO Swipe：安卓新滑行输入模型](#item-8) ⭐️ 7.0/10
9. [维生素 D：对缺乏者有益，对其他人则被过度吹捧](#item-9) ⭐️ 7.0/10
10. [德国列车因 GSMR 无线电系统故障停运](#item-10) ⭐️ 7.0/10
11. [《艾尔登法环》的低技术 AI：基于栈的设计](#item-11) ⭐️ 7.0/10
12. [加州 AB 2047 法案禁止学生和教育工作者使用 3D 打印机](#item-12) ⭐️ 7.0/10
13. [PatentBrief.org：用通俗英语解释 821 项美国专利](#item-13) ⭐️ 7.0/10
14. [CISA 将四个正在被利用的漏洞加入 KEV 目录](#item-14) ⭐️ 7.0/10
15. [Scattered Spider 黑客在伦敦交通局网络攻击案中认罪](#item-15) ⭐️ 7.0/10
16. [OpenAI 支持 Appia 基金会制定 AI 标准](#item-16) ⭐️ 7.0/10
17. [Datasette 1.0a35 测试版新增创建/修改表功能及 JSON API](#item-17) ⭐️ 7.0/10
18. [Spacex 280 亿美元营收使其成为主要 Neocloud](#item-18) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Swift 包索引被苹果收购](https://swiftpackageindex.com/blog/swift-package-index-joins-apple) ⭐️ 8.0/10

苹果已收购 Swift 包索引（SPI），这是一个社区运营的 Swift 包搜索引擎，相关消息已在 SPI 博客上公布。 此次收购表明苹果对 Swift 生态系统的战略投入，可能改善开发者的包管理体验，但也引发了对开源治理和开发者身份集成未来走向的担忧。 Swift 包索引是一个社区运营的包搜索引擎，支持按平台和语言筛选，此前由英国公司 SPI Operations Limited 运营。

hackernews · JDevlieghere · Jun 23, 18:00 · [社区讨论](https://news.ycombinator.com/item?id=48648779)

**背景**: Swift 包索引（SPI）是一个社区驱动的工具，帮助开发者发现可用于 Swift 包管理器（SPM）的 Swift 包。SPM 是苹果官方的 Swift 项目依赖管理器，但缺乏内置的包注册中心，因此 SPI 成为重要资源。此次收购正值苹果寻求加强其开发者工具和生态系统之际。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.swift.org/packages/">Packages | Swift .org</a></li>
<li><a href="https://swiftpackageindex.cn/faq">常见问题解答 – Swift Package Index - Swift 包索引</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：有人为 SPI 团队的成功感到高兴，也有人担心苹果在开源方面的过往记录以及未来方向中提到的开发者身份。甚至有用户计划因 SPI 仅支持 GitHub 的限制而构建一个竞争对手。

**标签**: `#Swift`, `#Apple`, `#Package Management`, `#Open Source`, `#Developer Tools`

---

<a id="item-2"></a>
## [开源所见即所得 TikZ 编辑器发布](https://tikz.dev/editor/) ⭐️ 8.0/10

一款新的开源所见即所得 TikZ 编辑器已发布，用户可以通过拖拽和调整元素大小来可视化编辑 TikZ 代码，同时保持源代码与渲染图形同步。 该工具解决了学术界和 LaTeX 用户手动编写 TikZ 图形的主要痛点，减少了繁琐的坐标调整和重新编译。它可能显著加快科学论文中的图形创建速度。 该编辑器几乎完全使用 Codex（一种 AI 编码代理）构建，开发过程中消耗了约 7 亿个 token。它重新实现了 TikZ 的大部分功能，以跟踪对象的精确源代码位置，从而在不更改其他代码的情况下精确覆盖坐标。

hackernews · DominikPeters · Jun 23, 14:24 · [社区讨论](https://news.ycombinator.com/item?id=48645437)

**背景**: TikZ 是一个强大的 LaTeX 包，用于创建矢量图形，广泛用于学术论文中的图表、图形和插图。传统上，用户手动编写 TikZ 代码并重新编译以查看更改，这非常耗时。由于解析和渲染 TikZ 命令的复杂性，所见即所得的 TikZ 编辑器非常罕见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.overleaf.com/learn/latex/TikZ_package">TikZ package - Overleaf, Online LaTeX Editor</a></li>
<li><a href="https://github.com/topics/tikz?l=tex&o=desc&s=updated">tikz · GitHub Topics · GitHub</a></li>

</ul>
</details>

**社区讨论**: 社区称赞该项目解决了实际需求，一些人指出它对学生的潜力。然而，也有人担心生成的 TikZ 代码不必要地使用了绝对坐标，并提出了支持 Typst 的 CeTZ 等替代系统的建议。

**标签**: `#LaTeX`, `#TikZ`, `#editor`, `#academic`, `#open-source`

---

<a id="item-3"></a>
## [AI 编码代理需要人类规范，而非循环](https://lucumr.pocoo.org/2026/6/23/the-coming-loop/) ⭐️ 8.0/10

一篇博客文章指出，AI 编码代理在人类仔细规范和迭代之后最为有效，而非作为自主循环的驱动者。作者强调，清晰度和前期设计是成功使用代理的前提。 这挑战了围绕自主 AI 编码代理的主流炒作，强调人类思考和规范仍然至关重要。它影响开发者和团队将 AI 工具整合到工作流程中的方式，可能节省时间并减少挫败感。 文章指出，LLM 在美学和品味方面存在困难，过度空值检查和错误处理是 AI 生成代码中的常见问题。作者建议，规范驱动开发（人类在代理实施前编写详细规范）能产生更好的结果。

hackernews · ingve · Jun 23, 11:06 · [社区讨论](https://news.ycombinator.com/item?id=48643180)

**背景**: 像 Cursor 和 Zencoder 这样的 AI 编码代理使用大型语言模型（LLM）来辅助代码生成和调试。然而，LLM 存在已知的局限性，例如缺乏实际经验和难以进行复杂推理，这可能导致次优代码。这篇博客文章是关于如何在软件工程中最好地利用 AI 的更广泛讨论的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zencoder.ai/">Zencoder | The AI Coding Agent</a></li>
<li><a href="https://cursor.com/">Cursor: AI coding agent</a></li>
<li><a href="https://research.chalmers.se/publication/550397/file/550397_Fulltext.pdf">Emotional Strain and Frustration in LLM Interactions in Software ...</a></li>

</ul>
</details>

**社区讨论**: 评论者大多同意这篇文章，分享经验认为规范编写是瓶颈，没有清晰的规范，代理循环就不太有用。一些人指出，LLM 擅长完成任务但不擅长美学，人类对规范的迭代是不可避免的。

**标签**: `#AI coding agents`, `#software engineering`, `#LLM limitations`, `#development workflow`

---

<a id="item-4"></a>
## [Unlimited OCR：一次性长视野解析](https://github.com/baidu/Unlimited-OCR) ⭐️ 8.0/10

百度研究人员推出了 Unlimited OCR，这是一种巧妙的架构技巧，通过避免 KV 缓存的线性增长来防止 AI 内存囤积，从而无需逐页分块即可一次性对长文档进行 OCR。 这一突破显著降低了内存使用并简化了长文档 OCR 的流程，使得无需自定义分块代码即可一次性处理整个 PDF 或书籍，这对文档分析工具的开发者与用户都有利。 该方法基于 arXiv 上的论文（2606.23050），并构建在 Deepseek-OCR 和 PaddleOCR 等模型之上。该方案专门解决了基于 Transformer 的 OCR 模型中 KV 缓存的内存瓶颈问题。

hackernews · ingve · Jun 23, 11:35 · [社区讨论](https://news.ycombinator.com/item?id=48643426)

**背景**: OCR（光学字符识别）将文本图像转换为机器可读文本。在处理长文档时，AI 模型通常维护一个随输入长度线性增长的 KV 缓存，导致内存不足错误。开发者常常不得不将文档拆分成单页，这增加了复杂性并可能丢失上下文。

**社区讨论**: 社区称赞了这一巧妙的技巧以及对 Deepseek-OCR 和 PaddleOCR 的致谢。一些用户注意到对 Fate/stay night 中“无限剑制”的引用，还有用户分享了他们在本地 OCR 用于 RAG 的经验，证实了流式处理的价值。

**标签**: `#OCR`, `#AI`, `#memory optimization`, `#deep learning`, `#open source`

---

<a id="item-5"></a>
## [不要通过发送垃圾邮件来验证电子邮件地址](https://milek7.pl/mailverifyspam/) ⭐️ 8.0/10

milek7.pl 的一篇博客文章揭露，包括 Pangram 在内的一些服务可能通过发送垃圾邮件来验证电子邮件地址，这促使 Pangram 的创始人展开调查并承诺修复该问题。 这种做法损害了用户的信任和隐私，因为电子邮件验证不应涉及发送未经请求的邮件。它揭示了电子邮件验证生态系统中一个更广泛的问题，即第三方服务可能滥用提交的地址。 作者在用一个全新的电子邮件地址注册后收到了垃圾邮件，垃圾邮件内容包含关于磁畴的填充文本。Pangram 使用 Zerobounce 和 CustomerIO 进行电子邮件验证，创始人尚不确定是哪个服务导致了垃圾邮件。

hackernews · garaetjjte · Jun 23, 20:23 · [社区讨论](https://news.ycombinator.com/item?id=48650837)

**背景**: 电子邮件验证是一种常见做法，用于确保电子邮件地址有效且属于用户。通常，服务会发送一个验证链接或代码，用户需要点击或输入。然而，一些第三方验证服务可能会发送类似垃圾邮件的测试邮件，这是不道德的，甚至可能违法。

**社区讨论**: 评论意见不一：一些用户无法复现该问题，怀疑是巧合，而另一些用户则认为这种做法难以置信，并建议使用一次性代码等替代验证方法。创始人的直接回应增加了可信度，并显示出解决问题的意愿。

**标签**: `#email verification`, `#spam`, `#privacy`, `#web development`, `#security`

---

<a id="item-6"></a>
## [谷歌因非官方 CLI 工具解雇员工](https://twitter.com/JPoehnelt/status/2069482265953087602) ⭐️ 8.0/10

谷歌解雇了员工 Justin Poehnelt，原因是他创建并发布了一个名为 gogcli 的非官方 Google Workspace CLI 工具，该工具可能被误认为是谷歌的官方产品。 这一事件凸显了员工创新与企业政策之间的紧张关系，尤其是在可能被视为官方的开源贡献方面。它引发了关于公司如何平衡鼓励副业项目与保护品牌的问题。 该工具 gogcli 是一个面向 Google Workspace 服务（如 Gmail 和 Drive）的 JSON 优先 CLI，并获得了其他谷歌员工的贡献。尽管该项目在 GitHub 上大受欢迎，Poehnelt 仍被解雇，这表明可能缺乏事先批准或曾收到直接警告。

hackernews · justinwp · Jun 23, 18:13 · [社区讨论](https://news.ycombinator.com/item?id=48649011)

**背景**: 谷歌历来通过“20%时间”和开源贡献鼓励员工副业项目，但也有严格政策防止与官方产品混淆。Google Workspace CLI (gws) 是官方工具，而 gogcli 是一个独立的非官方项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/atomic-skills-role-based-recipes-architecture-google-cli-hawksey-46ine">Atomic Skills and Role-Based Recipes: The Architecture of the Google ...</a></li>
<li><a href="https://termo.ai/skills/gogcli">gogcli - Google Workspace CLI — AI Skill — Termo</a></li>
<li><a href="https://akillness.github.io/posts/gogcli-google-workspace-cli/">gogcli: The Google Workspace CLI I Wish Every Agent Had</a></li>

</ul>
</details>

**社区讨论**: 社区评论存在分歧：一些人批评 Poehnelt 判断失误，发布了可能被误认为官方的工具；另一些人则表示同情，指责谷歌的官僚主义和“官僚铁律”。几位评论者指出，在谷歌工作会加剧混淆，如果曾被警告，解雇似乎是意料之中的。

**标签**: `#Google`, `#employment`, `#open source`, `#corporate policy`, `#CLI`

---

<a id="item-7"></a>
## [GPT-5 助力解决三年免疫学谜题](https://openai.com/index/gpt-5-immunology-mystery) ⭐️ 8.0/10

OpenAI 的 GPT-5 Pro 模型帮助免疫学家 Derya Unutmaz 解决了一个长达三年之久的 T 细胞行为谜题。 这一突破展示了 GPT-5 在科学研究中的具体影响力，可能推动癌症免疫疗法和自身免疫疾病治疗的进步。 该谜题涉及理解多年来一直困扰研究人员的特定 T 细胞行为，GPT-5 Pro 的高级推理能力提供了新的见解，从而找到了解决方案。

rss · OpenAI Blog · Jun 23, 17:00

**背景**: T 细胞是一种对免疫系统至关重要的白细胞，在抵抗感染和癌症中发挥关键作用。理解其行为是开发免疫疗法的基础。GPT-5 是 OpenAI 最新的大型语言模型，在包括科学推理在内的多个领域具有最先进的性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-5/">Introducing GPT - 5 | OpenAI</a></li>

</ul>
</details>

**标签**: `#GPT-5`, `#immunology`, `#AI in science`, `#cancer research`, `#autoimmune disease`

---

<a id="item-8"></a>
## [FUTO Swipe：安卓新滑行输入模型](https://swipe.futo.tech/) ⭐️ 7.0/10

FUTO 发布了名为 FUTO Swipe 的新滑行输入系统，现已集成到安卓版 FUTO 键盘中，声称具有领先的准确性和更少的词重叠。 这解决了移动输入中长期存在的痛点——滑行准确性，并提供了一个注重隐私的 Gboard 替代方案，可能改善数百万安卓用户的体验。 滑行库采用 GPLv3 许可，而安卓键盘使用 FUTO 许可。早期用户报告称其感觉与 Gboard 一样好，但仍存在随机大写和缺乏上下文感知等问题。

hackernews · futohq · Jun 23, 17:50 · [社区讨论](https://news.ycombinator.com/item?id=48648619)

**背景**: 滑行输入允许用户通过在键盘上滑动手指来输入单词，比点击更快，但经常出现词重叠错误。FUTO 键盘是一款面向安卓的开源、注重隐私的键盘应用。FUTO Swipe 使用在用户滑行数据上训练的机器学习模型来提高准确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://swipe.futo.tech/">FUTO Swipe</a></li>
<li><a href="https://github.com/futo-org/android-keyboard/releases">Releases · futo -org/android-keyboard</a></li>

</ul>
</details>

**社区讨论**: 社区评论总体积极，用户指出 FUTO Swipe 现已可与 Gboard 媲美。一些用户报告了随机大写和缺乏上下文感知等小问题，但总体情绪认为这是一项重大改进。

**标签**: `#mobile keyboard`, `#swipe typing`, `#machine learning`, `#privacy`, `#Android`

---

<a id="item-9"></a>
## [维生素 D：对缺乏者有益，对其他人则被过度吹捧](https://dynomight.net/vitamin-d/) ⭐️ 7.0/10

一项对维生素 D 研究的批判性分析认为，补充剂对严重缺乏者确实有益，但对普通人群广泛有益的证据薄弱且常被夸大。 这很重要，因为维生素 D 补充剂被健康博主广泛推广，该分析有助于澄清证据强与弱之处，指导更明智的个人和临床决策。 该分析指出，许多研究未能测量基线维生素 D 水平或考虑季节和纬度等因素，且建议可能基于有缺陷的统计方法。

hackernews · surprisetalk · Jun 23, 16:30 · [社区讨论](https://news.ycombinator.com/item?id=48647486)

**背景**: 维生素 D 是一种帮助身体吸收钙质、对骨骼健康重要的营养素。皮肤在阳光照射下会产生维生素 D，也可从食物或补充剂中获取。严重缺乏可导致儿童佝偻病和成人骨软化症。

**社区讨论**: 评论者称赞了这种平衡的分析，一些人指出健康博主常转而声称广泛缺乏以解释弱结果。其他人则提出维生素 K2 在吸收中的作用，以及需要测量血液水平和考虑阳光照射的研究。

**标签**: `#nutrition`, `#vitamin D`, `#evidence-based medicine`, `#health research`

---

<a id="item-10"></a>
## [德国列车因 GSMR 无线电系统故障停运](https://apnews.com/article/germany-trains-halted-communications-radio-problem-deutsche-bahn-e8fd970b2d889f3ae7ce03322d5c726b) ⭐️ 7.0/10

2026 年 6 月 23 日，德国 GSMR 数字铁路无线电系统发生全国性故障，迫使德国铁路公司在全国范围内停运所有列车。此次故障疑似由有缺陷的软件更新导致。 这一事件凸显了关键基础设施在软件故障面前的脆弱性，影响了数百万乘客并扰乱了全国铁路运营。它强调了在关键通信系统中需要强大的测试和故障安全机制。 GSMR（铁路全球移动通信系统）数字无线电系统用于列车控制以及司机与调度员之间的通信。德国铁路公司的技术人员昼夜不停地解决问题，系统恢复后服务得以重启。

hackernews · sva_ · Jun 23, 21:19 · [社区讨论](https://news.ycombinator.com/item?id=48651613)

**背景**: GSMR 是一种基于 GSM 技术的标准化铁路数字通信系统，专为高速铁路和安全关键操作而设计。它支持列车控制和信号所需的语音和数据通信。该系统一旦故障，列车将无法接收信号或与控制中心通信，从而导致所有列车停运。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-06-23/german-rail-halted-nationwide-services-after-radio-system-outage">German Rail Halted Nationwide Services After Radio System Outage</a></li>

</ul>
</details>

**社区讨论**: 社区评论推测有缺陷的软件更新是可能的原因，一些人指出德国铁路公司有 IT 问题的历史。其他人将其与英国最近的一起火车事故相提并论，质疑是否有人为破坏，但大多数人认为软件故障是最合理的解释。

**标签**: `#software failure`, `#critical infrastructure`, `#railway`, `#GSMR`, `#IT outage`

---

<a id="item-11"></a>
## [《艾尔登法环》的低技术 AI：基于栈的设计](https://nega.tv/posts/low-tech-ai-of-elden-ring.html) ⭐️ 7.0/10

一项分析揭示，《艾尔登法环》的敌人 AI 采用基于栈的决策系统，而非更常见的行为树，以优先考虑性能和简洁性。 这一设计选择挑战了行业惯例，凸显了 AI 复杂度与运行时性能之间的权衡，可能影响未来游戏 AI 的开发。 基于栈的系统通过简单的压栈/出栈机制避免了行为树的开销，但与更模块化的方法相比，可能限制了行为的多样性。

hackernews · g0xA52A2A · Jun 23, 11:40 · [社区讨论](https://news.ycombinator.com/item?id=48643489)

**背景**: 行为树是游戏中流行的 AI 架构，使用节点表示任务和条件，支持模块化和可复用的行为。然而，由于树遍历和内存分配，它们可能带来性能开销。相比之下，基于栈的 AI 使用更简单的控制流，效率更高但灵活性较低。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Behavior_tree_(artificial_intelligence,_robotics_and_control)">Behavior tree (artificial intelligence, robotics and control) - Wikipedia</a></li>
<li><a href="https://gamedev.stackexchange.com/questions/51693/difference-between-decision-trees-behavior-trees-for-game-ai">Difference between Decision Trees & Behavior Trees for Game AI</a></li>
<li><a href="https://www.gamedeveloper.com/programming/behavior-trees-for-ai-how-they-work">Behavior trees for AI : How they work</a></li>

</ul>
</details>

**社区讨论**: 评论者就所描述的系统是否真的不同于行为树展开了辩论，一些人认为许多行为树实现使用了类似的栈机制。其他人则注意到任务设计中的权衡以及由于术语过载而讨论 AI 的挑战。

**标签**: `#game AI`, `#behavior trees`, `#Elden Ring`, `#software architecture`, `#performance`

---

<a id="item-12"></a>
## [加州 AB 2047 法案禁止学生和教育工作者使用 3D 打印机](https://www.the3dprintingnerd.com/ab2047) ⭐️ 7.0/10

加州议会法案 AB 2047 提议限制学生、教育工作者和企业使用 3D 打印机，旨在防止打印武器。 该法案可能为美国 3D 打印技术的监管开创先例，影响创新、教育和小型企业，同时引发技术和宪法方面的担忧。 该法案已通过议会投票（投票链接可见），批评者认为检测武器意图所需的技术不可行，因为 3D 打印机读取的是代码而非意图。

hackernews · Buildstarted · Jun 23, 22:12 · [社区讨论](https://news.ycombinator.com/item?id=48652184)

**背景**: 3D 打印（增材制造）通过数字模型逐层创建物体。对无法检测的 3D 打印枪支的担忧导致了监管努力，但技术限制使执法变得困难。

**社区讨论**: 评论者就该法案的可行性展开辩论，有人指出打印机无法推断意图，且动机强烈的人可以绕过限制，如复印美元钞票的故事所示。还有人提到布隆伯格的政治游说，并将美国监管与欧洲进行不利比较。

**标签**: `#3D printing`, `#regulation`, `#technology policy`, `#California law`

---

<a id="item-13"></a>
## [PatentBrief.org：用通俗英语解释 821 项美国专利](https://patentbrief.org/) ⭐️ 7.0/10

PatentBrief.org 上线，提供 821 项美国专利的通俗英语解释，并通过 JSON 和 Markdown 端点提供结构化数据访问。 该项目使开发者、研究人员和公众能够理解复杂的专利，通过降低理解专利内容的门槛，可能加速创新和教育。 数据集涵盖知名专利，如滑动解锁、CRISPR、尼龙和 RSA 加密。每个专利页面提供 /json 和 /md 端点，完整数据可在 patentbrief.org/data 获取。

rss · Hacker News Show HN · Jun 23, 20:07

**背景**: 美国专利是授予发明人独占权的法律文件，但通常用晦涩的法律术语写成。PatentBrief.org 旨在通过提供清晰、简洁的通俗英语解释，以及便于集成到应用程序中的机器可读格式，来揭开这些文件的神秘面纱。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2l2aExiekRSR0g5RUN0Mk02OW95Z0FQAQ?hl=en-GB&gl=GB&ceid=GB:en">Google News - Federal court rules on CRISPR patent dispute - Overview</a></li>
<li><a href="https://cs.stanford.edu/people/eroberts/cs201/projects/software-patents/rsa.html">cs.stanford.edu/people/eroberts/cs201/projects/software- patents / rsa ....</a></li>

</ul>
</details>

**标签**: `#patents`, `#open-data`, `#API`, `#education`, `#technology`

---

<a id="item-14"></a>
## [CISA 将四个正在被利用的漏洞加入 KEV 目录](https://www.cisa.gov/news-events/alerts/2026/06/23/cisa-adds-four-known-exploited-vulnerabilities-catalog) ⭐️ 7.0/10

CISA 已将四个新漏洞加入其已知被利用漏洞（KEV）目录，包括影响 Lantronix EDS5000 的 CVE-2025-67038 以及三个 Ubiquiti UniFi OS 漏洞（CVE-2026-34908、CVE-2026-34909、CVE-2026-34910），这些漏洞均有被积极利用的证据。 这些漏洞正在被积极利用，对联邦企业及网络基础设施构成重大风险。CISA 的 KEV 新增条目作为权威警告，敦促所有组织优先修补这些高风险漏洞。 Lantronix 漏洞（CVE-2025-67038）是 EDS5000 设备中的代码注入漏洞，而三个 Ubiquiti 漏洞包括 UniFi OS 中的不当访问控制、路径遍历和不当输入验证。联邦机构必须根据 BOD 26-04 修复这些漏洞，该指令要求对公开暴露资产上的 KEV 列表漏洞进行快速修补。

rss · CISA Cybersecurity Advisories · Jun 23, 12:00

**背景**: CISA 的已知被利用漏洞（KEV）目录是一个精选列表，收录了已被确认在野外被积极利用的漏洞。约束性操作指令（BOD）26-04 要求联邦民事行政部门（FCEB）机构优先修复 KEV 列表中那些在利用后可完全控制资产的公开暴露资产上的漏洞。虽然该指令仅适用于联邦机构，但 CISA 强烈建议所有组织采用类似的风险导向型漏洞管理实践。

**标签**: `#CISA`, `#vulnerability`, `#exploitation`, `#network security`, `#KEV`

---

<a id="item-15"></a>
## [Scattered Spider 黑客在伦敦交通局网络攻击案中认罪](https://krebsonsecurity.com/2026/06/scattered-spider-hackers-plead-guilty-on-day-1-of-trial/) ⭐️ 7.0/10

Scattered Spider 网络犯罪团伙的两名核心成员 Owen Flowers 和 Thalha Jubair，在审判第一天就 2024 年 8 月对伦敦交通局（TfL）的网络攻击认罪。 此次认罪标志着针对一个活跃黑客团伙的重大法律胜利，该团伙曾对多家大型组织发动高调攻击，展示了执法部门将网络犯罪分子绳之以法的能力。 此次攻击给 TfL 造成约 3900 万英镑的损失，并导致数月的中断，泄露了包括银行账号和家庭地址在内的敏感数据。

rss · Krebs on Security · Jun 23, 16:12

**背景**: Scattered Spider 是一个以英语为主的网络犯罪团伙，部分成员年仅 16 岁，源自被称为“The Com”的地下黑客社区。该团伙曾与对凯撒娱乐、米高梅国际酒店集团等公司的攻击有关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/czx5yp9qy0do">Two men plead guilty over £39m Transport for London cyber attack</a></li>
<li><a href="https://www.aol.com/inside-scattered-spider-notorious-teen-142611588.html">Inside Scattered Spider : The notorious teen hacking group causing...</a></li>
<li><a href="https://www.bitdefender.com/en-au/blog/hotforsecurity/transport-for-london-cyberattack-bank-account-numbers-names-teen-arrested/">Transport for London Cyberattack Compromises Bank Account...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#cybercrime`, `#Scattered Spider`, `#hacking`, `#legal`

---

<a id="item-16"></a>
## [OpenAI 支持 Appia 基金会制定 AI 标准](https://openai.com/index/helping-build-shared-standards-for-advanced-ai) ⭐️ 7.0/10

OpenAI 宣布支持 Appia 基金会，该基金会是 Linux 基金会的一项倡议，旨在为先进 AI 制定共享标准、评估框架和安全实践。 此次合作意义重大，因为它汇集了 Google、Microsoft 和 OpenAI 等主要 AI 参与者，共同制定全球标准，这对 AI 安全和负责任部署至关重要。 Appia 基金会基于国际标准和现有框架，制定公开可用的全球规范，弥合标准与实际实施之间的差距。

rss · OpenAI Blog · Jun 23, 13:00

**背景**: 先进 AI 系统缺乏普遍接受的安全和评估标准，难以评估其可靠性。Appia 基金会旨在提供一个开放的连接层，将现有标准付诸实践，实现 AI 供应链中的一致评估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://appiafoundation.org/">Appia Foundation</a></li>
<li><a href="https://finance.yahoo.com/technology/ai/articles/linux-foundation-launches-appia-foundation-153500083.html">Linux Foundation Launches Appia Foundation to Establish...</a></li>
<li><a href="https://nerds.xyz/2026/06/google-microsoft-openai-appia-linux-foundation-ai-project/">Google, Microsoft, and OpenAI unite behind new Linux Foundation AI...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#standards`, `#OpenAI`, `#global cooperation`

---

<a id="item-17"></a>
## [Datasette 1.0a35 测试版新增创建/修改表功能及 JSON API](https://simonwillison.net/2026/Jun/23/datasette/#atom-everything) ⭐️ 7.0/10

Datasette 1.0a35 测试版引入了新的“创建表”和“修改表”界面，均通过 JSON API 支持，用户可以通过网页界面或 API 定义列、主键、约束等。 此版本通过直接在界面中支持模式管理，大幅提升了 Datasette 的易用性，使其对非开发者更友好，并扩展了其作为数据探索和发布工具的应用范围。 “创建表”API 支持自定义列类型、NOT NULL 约束、字面量和表达式默认值以及单列外键。“修改表”API 允许添加、重命名、重新排序和删除列，以及更改类型、默认值、约束、主键、外键和表名。

rss · Simon Willison · Jun 23, 21:34

**背景**: Datasette 是一个基于 SQLite 的开源数据探索和发布工具，提供网页界面和 JSON API 用于查询数据库。在此版本之前，创建或修改表需要外部工具或直接使用 SQL 命令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.datasette.io/en/latest/json_api.html?highlight=pagination">JSON API - Datasette documentation</a></li>

</ul>
</details>

**标签**: `#datasette`, `#release`, `#data tools`, `#JSON API`

---

<a id="item-18"></a>
## [Spacex 280 亿美元营收使其成为主要 Neocloud](https://www.latent.space/p/ainews-spacex-is-already-a-28byr) ⭐️ 7.0/10

Jamin Ball 的分析显示，SpaceX 的年营收达到 280 亿美元，使其成为 AI 基础设施领域的重要 Neocloud 参与者。 这重新定义了 SpaceX，不仅是一家太空公司，更是一个主要的云基础设施提供商，可能颠覆传统的超大规模云市场，并为 AI 工作负载提供新选择。 280 亿美元的数字来自 Jamin Ball 的分析，而 Neocloud 是以 AI 为先的云提供商，其 GPU 访问成本比超大规模云低 70-80%。

rss · Latent Space · Jun 23, 06:19

**背景**: Neocloud 是一类新兴的云基础设施提供商，源于 GPU 稀缺和高成本，专注于 AI 工作负载。与传统超大规模云（如 AWS、Azure 和 GCP）相比，它们提供更便宜的 GPU 访问。SpaceX 的 Starlink 卫星网络提供低延迟连接，可用于云服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vast.ai/article/what-is-a-neocloud-business-model-explained">What Is a Neocloud ? The Business Model Explained</a></li>
<li><a href="https://cloudedjudgement.substack.com/">Clouded Judgement | Jamin Ball | Substack</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#neocloud`, `#cloud computing`, `#AI infrastructure`, `#finance`

---