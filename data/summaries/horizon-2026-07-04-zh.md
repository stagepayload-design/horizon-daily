# Horizon 每日速递 - 2026-07-04

> From 44 items, 9 important content pieces were selected

---

1. [本地运行 SOTA 大模型指南引发成本争论](#item-1) ⭐️ 8.0/10
2. [欧盟议会间谍软件调查员遭飞马间谍软件攻击](#item-2) ⭐️ 8.0/10
3. [Wordgard：ProseMirror 创建者推出的新富文本编辑器](#item-3) ⭐️ 8.0/10
4. [PostgreSQL 与 OOM 杀手：为何使用严格内存过量使用](#item-4) ⭐️ 8.0/10
5. [Current AI 发布开源 AI 差距地图](#item-5) ⭐️ 8.0/10
6. [llama.cpp b9866 支持 288 专家的 topk-MoE 融合](#item-6) ⭐️ 7.0/10
7. [SearXNG：一款免费、注重隐私的元搜索引擎](#item-7) ⭐️ 7.0/10
8. [星链弥合非洲数字鸿沟](#item-8) ⭐️ 7.0/10
9. [课程创作者报告收入因 AI 下降超 50%](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [本地运行 SOTA 大模型指南引发成本争论](https://github.com/jamesob/local-llm) ⭐️ 8.0/10

Jamesob 在 GitHub 上发布了一份实用指南，详细介绍了如何搭建昂贵的本地环境来运行最先进的大语言模型，其中包括一个超过 4 万美元的配置，使用了四块每块 1.2 万美元的 GPU。 该指南凸显了本地 AI 推理与云服务之间的持续矛盾——高昂的硬件成本使得本地部署对大多数用户而言经济上不可行，但对于隐私保护和离线使用仍至关重要。 指南中的旗舰配置实际花费在 5 万到 5.5 万美元之间，而非声称的 4 万美元，并且依赖量化与剪枝技术（如 REAP）来缩小模型体积，这可能在基准测试之外导致性能下降。

hackernews · livestyle · Jul 3, 15:03 · [社区讨论](https://news.ycombinator.com/item?id=48775921)

**背景**: 本地运行大语言模型需要配备大显存的高性能 GPU，例如 NVIDIA H200 或 RTX 3090。像 GLM-5.2 或 Qwen3.6 这样的最先进模型在全精度推理时通常需要数百 GB 的显存，迫使用户采用量化或剪枝技术以适应消费级硬件。云服务（如 Claude Opus）以极低的初始成本提供了相近的智能水平。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rajuhemanth456.medium.com/state-of-the-art-in-large-language-models-llms-a-deep-dive-into-the-cutting-edge-ai-technology-a080283d0729">State-of-the-Art in Large Language Models ( LLMs ): A Deep... | Medium</a></li>
<li><a href="https://huggingface.co/blog/wolfram/llm-comparison-test-2024-12-04">LLM Comparison/Test: 25 SOTA LLMs (including QwQ) through 59...</a></li>
<li><a href="https://www.analyticsvidhya.com/blog/2025/03/top-sota-llms/">Top 6 SOTA LLMs for Code, Web search, Research... - Analytics Vidhya</a></li>

</ul>
</details>

**社区讨论**: 评论者如 Aurornis 和 jacobgold 警告说，本地部署极其昂贵且质量通常低于云服务，jacobgold 指出 4 万美元相当于 16.8 年的 Claude Opus 订阅费用。GTP 等人建议采用 128GB 统一内存等中端方案来运行 DeepSeek V4 flash，而 kgeist 则质疑剪枝模型在实际中的表现。

**标签**: `#LLM`, `#local inference`, `#hardware`, `#cost analysis`, `#open-source AI`

---

<a id="item-2"></a>
## [欧盟议会间谍软件调查员遭飞马间谍软件攻击](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 8.0/10

公民实验室确认，一名参与调查间谍软件的欧洲议会成员在 2022 年和 2023 年多次感染飞马间谍软件，很可能是一个有权在多个欧盟国家进行间谍活动的国家行为体所为。 这一事件凸显了雇佣间谍软件对民主机构的威胁，以及调查监控滥用行为者所面临的风险，可能削弱整个欧盟的监督努力。 首次感染发生在 2022 年 10 月 21 日左右，与针对俄语和白俄罗斯语流亡记者的飞马间谍软件活动重叠，表明客户拥有跨境间谍授权。该设备还包含机密医疗和政府文件，引发数据泄露担忧。

hackernews · ledoge · Jul 3, 20:38 · [社区讨论](https://news.ycombinator.com/item?id=48779683)

**背景**: 飞马间谍软件是由以色列 NSO 集团开发的一款强大间谍软件，能够远程感染智能手机并提取数据、信息和录音。它已被关联到全球记者、活动家和政治人物的监控。欧洲议会一直在调查此类间谍软件在欧盟内部的使用情况。

**社区讨论**: 评论者指出，此次攻击可能与涉及总理办公室的更广泛的希腊间谍软件丑闻有关，一些欧盟国家滥用飞马间谍软件的程度已导致以色列公司切断联系。其他人质疑为何该议员在敏感工作中使用个人设备。

**标签**: `#cybersecurity`, `#spyware`, `#Pegasus`, `#European Parliament`, `#surveillance`

---

<a id="item-3"></a>
## [Wordgard：ProseMirror 创建者推出的新富文本编辑器](https://wordgard.net/) ⭐️ 8.0/10

Wordgard 是 ProseMirror 创建者 Marijn Haverbeke 发布的一款新的浏览器内富文本编辑器，它采用了全新的方法，与 ProseMirror 共享概念，但没有提供从 ProseMirror 升级的路径。 这很重要，因为 ProseMirror 是构建富文本编辑器的广泛使用的库，其创建者的新编辑器可能会影响基于 Web 的编辑的未来，特别是对于寻求现代替代方案的开发者。 Wordgard 与 ProseMirror 共享许多概念，但并非直接替代品；切换需要大量重做。该编辑器注重简洁性和性能，其文档强调了与 ProseMirror 的差异。

hackernews · indy · Jul 3, 08:50 · [社区讨论](https://news.ycombinator.com/item?id=48772573)

**背景**: ProseMirror 是一个流行的开源工具包，用于在浏览器中构建富文本编辑器，以其灵活的模式系统和协作编辑支持而闻名。Wordgard 是同一作者的新项目，旨在解决 ProseMirror 的一些复杂性，同时保留其核心思想。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://prosemirror.net/">ProseMirror</a></li>

</ul>
</details>

**社区讨论**: 社区讨论显示出浓厚兴趣，用户注意到缺乏升级路径，并将其与 ProseMirror 和 TipTap 进行比较。一些用户称赞其设计并认为该方法具有验证性，而另一些用户则对缺乏富文本编辑的 Web 标准表示沮丧。

**标签**: `#rich-text editor`, `#ProseMirror`, `#web development`, `#open source`

---

<a id="item-4"></a>
## [PostgreSQL 与 OOM 杀手：为何使用严格内存过量使用](https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit) ⭐️ 8.0/10

Ubicloud 发布了一篇博客文章，解释了他们为何对 PostgreSQL 使用严格内存过量使用（vm.overcommit_memory=2），以防止 OOM 杀手终止数据库进程。 这种做法提高了 PostgreSQL 在内存压力下的稳定性，这对生产数据库至关重要。同时，它也引发了社区关于权衡的讨论，因为严格过量使用可能导致分配大量虚拟内存的应用程序出现 fork 失败。 文章推荐模式 2（严格过量使用），但警告如果过量使用比例过低，可能会阻止 fork() 调用。用户应在生产部署前在 QA 环境中进行测试。

hackernews · furkansahin · Jul 3, 13:00 · [社区讨论](https://news.ycombinator.com/item?id=48774509)

**背景**: Linux 使用内存过量使用允许进程分配比物理内存更多的虚拟内存。当系统内存不足时，OOM 杀手会被触发，可能杀死像 PostgreSQL 这样的关键进程。严格过量使用禁用过量使用，确保在内存不足时拒绝内存分配请求，从而避免 OOM 杀死，但可能导致 fork 失败。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kernel.org/doc/html/next/mm/overcommit-accounting.html">Overcommit Accounting — The Linux Kernel documentation</a></li>
<li><a href="https://www.baeldung.com/linux/overcommit-modes">Linux Overcommit Modes | Baeldung on Linux</a></li>
<li><a href="https://rakeshjain-devops.medium.com/linux-out-of-memory-killer-31e477a45759">Linux Out-Of-Memory Killer . What is this ? | by Rakesh Jain | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出 Linux 默认内存设置存在问题，严格过量使用如果调整不当可能导致不稳定。一些用户分享了在同一台机器上运行 Go 应用程序和 PostgreSQL 时因虚拟内存分配导致崩溃的经验。

**标签**: `#PostgreSQL`, `#Linux`, `#memory management`, `#database administration`, `#OOM killer`

---

<a id="item-5"></a>
## [Current AI 发布开源 AI 差距地图](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

Current AI 是一家在 2025 年 2 月巴黎 AI 行动峰会上成立的非营利组织，已获得 4 亿美元承诺资金；它发布了开源 AI 差距地图 v0.1，索引了开源 AI 技术栈中的 421 个产品，包括来自 228 个组织的 266 个软件工具、85 个模型、50 个数据集和 20 个硬件项目。 该地图提供了开源 AI 生态系统的结构化、数据驱动概览，有助于识别投资和开发中的空白与机遇，对引导开源 AI 的战略方向至关重要。 底层数据以 MIT 许可证在 GitHub 上发布，包含 1,184 个 YAML 文件以及笔记本、模式和其他脚本，可通过 Datasette Lite 进行探索，其中包含一个包含 16,185 个跟踪 GitHub 仓库的 CSV 文件。

rss · Simon Willison · Jul 3, 22:04

**背景**: 开源 AI 技术栈通常包括三个层次：模型组件（如训练框架）、产品/用户体验（如应用程序）和基础设施（如硬件）。Current AI 是一个全球合作伙伴关系，旨在构建 AI 的公共选项，并获得了大量资金支持。

**标签**: `#open source`, `#AI`, `#ecosystem mapping`, `#non-profit`, `#infrastructure`

---

<a id="item-6"></a>
## [llama.cpp b9866 支持 288 专家的 topk-MoE 融合](https://github.com/ggml-org/llama.cpp/releases/tag/b9866) ⭐️ 7.0/10

llama.cpp 版本 b9866 为拥有 288 个专家的模型（如 Step-3.7-Flash）添加了 CUDA topk-MoE 融合支持，在浅上下文下将 token 生成速度提升了约 2.4%。 此优化减少了非 2 的幂次专家数量的 MoE 模型的每 token 路由开销，使使用稀疏专家架构的日益增多的大型语言模型的推理更加高效。 此前，融合仅接受 2 的幂次专家数量或特殊处理的 576；288 是 warp 大小的倍数，因此现有内核已能处理，只需补充缺失的模板实例化。随着上下文深度增加，注意力成为瓶颈，增益逐渐消失。

github · github-actions[bot] · Jul 3, 14:20

**背景**: 混合专家（MoE）模型使用多个专门的子网络（专家）和路由机制来选择每个 token 激活哪些专家。topk-MoE 融合将多个路由操作合并到一个内核中，减少图节点开销并提高 GPU 利用率。llama.cpp 是一个流行的开源推理引擎，用于本地运行大语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp/releases">Releases · ggml-org/ llama . cpp · GitHub</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#CUDA`, `#MoE`, `#performance`, `#machine learning`

---

<a id="item-7"></a>
## [SearXNG：一款免费、注重隐私的元搜索引擎](https://github.com/searxng/searxng) ⭐️ 7.0/10

SearXNG 是一款免费开源的元搜索引擎，它聚合多个搜索引擎的结果，且不追踪用户。该工具因日常隐私搜索以及与 RAG 应用的集成而受到关注。 SearXNG 提供了一种保护隐私的替代方案，取代了集中式搜索引擎，其 JSON API 支持与 AI 代理和 RAG 管道的无缝集成。这使其成为开发人员构建注重隐私的 AI 应用的关键工具。 SearXNG 支持 JSON 输出，适合在 RAG 系统中以编程方式使用。但用户反映其速度较慢，且偶尔会遇到来自上游搜索引擎（如 DuckDuckGo 和 Brave）的 CAPTCHA 验证挑战。

hackernews · theanonymousone · Jul 3, 20:15 · [社区讨论](https://news.ycombinator.com/item?id=48779454)

**背景**: 元搜索引擎将用户查询发送到多个搜索引擎并合并结果，提供更广的覆盖范围，但依赖第三方服务。RAG（检索增强生成）将大语言模型与外部数据检索相结合，以提高准确性和相关性。SearXNG 的 JSON API 使其能够作为 RAG 管道中的检索组件。

**社区讨论**: 社区成员称赞 SearXNG 适合日常使用和 RAG 应用，有用户表示已将其作为日常搜索工具超过 5 年。但也有人担心速度和 CAPTCHA 拦截问题，同时有人提到 TinySearch 等工具可为代理优化上下文。Searx 的原始创建者已转向新项目 Hister，一个全文索引器。

**标签**: `#search engine`, `#privacy`, `#metasearch`, `#open source`, `#RAG`

---

<a id="item-8"></a>
## [星链弥合非洲数字鸿沟](https://www.economist.com/middle-east-and-africa/2026/07/02/africans-are-turning-to-starlink) ⭐️ 7.0/10

据《经济学人》报道，非洲人越来越多地采用星链卫星互联网，在缺乏传统宽带基础设施的地区获得连接。 这一趋势可能显著缩小非洲的数字鸿沟，在服务不足的地区促进经济增长、教育和医疗接入，类似于手机带来的跨越式发展效应。 星链利用低地球轨道卫星星座提供低延迟互联网，解决了传统地球静止轨道卫星互联网的高延迟问题。

hackernews · bookofjoe · Jul 3, 21:08 · [社区讨论](https://news.ycombinator.com/item?id=48779977)

**背景**: 非洲的数字鸿沟十分显著，许多农村地区缺乏有线基础设施。星链的低地球轨道卫星技术提供了一种可行的替代方案，因为它不需要地面基础设施，可以快速部署。这类似于非洲早期绕过固定电话、直接采用手机的跨越式发展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Starlink">Starlink - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/pulse/guide-how-starlink-internet-works-patrick-mutabazi-rtr2e">A Guide to How Starlink Internet Works</a></li>
<li><a href="https://en.wikipedia.org/wiki/Digital_divide_by_continent,_area_and_country">Digital divide by continent, area and country - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调了在农村地区使用星链的个人体验，指出与蜂窝热点或传统卫星互联网等替代方案相比，其价格合理且性能优越。用户强调其作为均衡器的作用，提供了获取知识和工具的途径。

**标签**: `#Starlink`, `#Internet Access`, `#Digital Divide`, `#Satellite Internet`

---

<a id="item-9"></a>
## [课程创作者报告收入因 AI 下降超 50%](https://simonwillison.net/2026/Jul/3/josh-w-comeau/#atom-everything) ⭐️ 7.0/10

Josh W. Comeau 报告称，他的新课程《Whimsical Animations》预计销量仅为通常水平的三分之一，现有课程的销售额也比去年大幅下降，他将此归因于 AI 引发的开发者就业不确定性以及 LLM 取代付费教育内容。 这提供了来自知名课程创作者的切实数据，展示了 AI 如何颠覆开发者教育市场，对就业保障、学习动机以及付费教育内容的可持续性产生影响。 Comeau 的第三门课程《Whimsical Animations》近期上线，销量约为以往的三分之一；他还指出，多位课程创作者的收入下降了 50%以上，参与人数减少，许多人转向 LLM，而 LLM 未经同意或补偿就重复使用他们的内容。

rss · Simon Willison · Jul 3, 21:25

**背景**: Josh W. Comeau 是一位知名的开发者教育者，创建了关于 CSS、React 和动画的互动课程。像 GPT-4 这样的大型语言模型（LLM）的兴起，使得个性化辅导和内容生成成为可能，可能减少对结构化付费课程的需求。此外，AI 驱动的自动化引发了对软件开发工作未来的担忧，抑制了学习新技能的投资。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://whimsy.joshwcomeau.com/">Whimsical Animations , a new course from Josh W . Comeau</a></li>
<li><a href="https://www.joshwcomeau.com/courses/">Online Courses • Josh W . Comeau</a></li>

</ul>
</details>

**标签**: `#AI impact`, `#developer education`, `#course creation`, `#job market`, `#LLMs`

---

