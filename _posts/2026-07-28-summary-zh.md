---
layout: default
title: "Horizon Summary: 2026-07-28 (ZH)"
date: 2026-07-28
lang: zh
---

> From 50 items, 15 important content pieces were selected

---

1. [Moonshot AI 发布 2.8 万亿参数 Kimi K3 模型](#item-1) ⭐️ 9.0/10
2. [vLLM v0.26.0：支持 Inkling 模型家族、DeepSeek-V4 优化等](#item-2) ⭐️ 8.0/10
3. [Anthropic 主张对开放权重模型进行强制安全测试](#item-3) ⭐️ 8.0/10
4. [Python-build-standalone：便携式 Python 发行版](#item-4) ⭐️ 8.0/10
5. [缺失的下划线导致无辜者被错判入狱 18 个月](#item-5) ⭐️ 8.0/10
6. [法官驳回谷歌用 DMCA 抗辩数据抓取](#item-6) ⭐️ 8.0/10
7. [研究人员完全控制沃尔沃/埃契尔车队平台](#item-7) ⭐️ 8.0/10
8. [llama.cpp b10155 新增 MiMo-V2.5 音频输入支持](#item-8) ⭐️ 7.0/10
9. [Open WebUI v0.11.0：全面视觉重构发布](#item-9) ⭐️ 7.0/10
10. [案例研究：用 HTMX 替换 React 的论坛平台迁移](#item-10) ⭐️ 7.0/10
11. [Paged Out #9：免费黑客杂志发布](#item-11) ⭐️ 7.0/10
12. [Libsm64：将《超级马力欧 64》作为可复用库用于游戏引擎](#item-12) ⭐️ 7.0/10
13. [Ami：开源本地优先的图记忆智能代理](#item-13) ⭐️ 7.0/10
14. [CISA 将两个正在被利用的漏洞加入 KEV 目录](#item-14) ⭐️ 7.0/10
15. [Ethan Mollick 更新 AI 指南：转向智能体系统](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Moonshot AI 发布 2.8 万亿参数 Kimi K3 模型](https://simonwillison.net/2026/Jul/27/kimi-k3/#atom-everything) ⭐️ 9.0/10

Moonshot AI 在 Hugging Face 上发布了其 2.8 万亿参数的 Kimi K3 模型权重，采用修改版许可证，要求大型模型即服务（MaaS）企业另行签订协议。 此次发布标志着可获取的最大开放权重模型之一的重要里程碑，推动了可访问大型语言模型的前沿，同时引入了可能影响行业实践的许可条款。 模型权重大小为 1.56 TB，许可证不再自称“修改版 MIT”，而是要求年收入超过 2000 万美元的 MaaS 企业另行签订协议。OpenRouter 已从 7 家提供商处提供 K3，定价具有竞争力。

rss · Simon Willison · Jul 27, 23:39

**背景**: 像 Kimi K3 这样的大型语言模型是在海量文本数据上训练的人工智能系统，能够生成类似人类的文本。Moonshot AI 此前在修改版 MIT 许可证下发布了 Kimi K2，要求大型商业实体进行署名。K3 许可证更进一步，要求大型 MaaS 提供商另行签订协议，这反映了关于开源定义和商业使用限制的持续争论。

**标签**: `#AI`, `#open-source`, `#large language model`, `#Moonshot AI`, `#Kimi K3`

---

<a id="item-2"></a>
## [vLLM v0.26.0：支持 Inkling 模型家族、DeepSeek-V4 优化等](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 全面支持 Inkling 模型家族，包括基础建模、CUDA 图、Hopper FA4 注意力、推测解码、LoRA 和 ModelOpt NVFP4 量化。同时为 DeepSeek-V4 带来显著性能优化，支持 fp32 lm_head、灵活注意力后端，并完善了 KV 卸载系统。 此版本通过支持 Inkling 和 DeepSeek-V4 等前沿模型，并在 NVIDIA、AMD 和 Intel 硬件上进行跨厂商优化，巩固了 vLLM 作为领先开源 LLM 推理引擎的地位。灵活注意力后端和 KV 卸载改进使大型模型在生产环境中部署更高效。 此版本包含来自 212 位贡献者的 411 次提交，其中 61 位是新贡献者。关键技术亮点包括 DeepSeek-V4 专用路由内核（端到端 TPOT 提升 2.94%）、fused_topk_bias 内核（1.5-2 倍加速），以及通过 head_dtype 为生成模型提供 fp32 lm_head 支持。现在可以为每个 KV 缓存组选择注意力后端，滑动窗口支持成为显式后端能力。

github · khluu · Jul 27, 01:06

**背景**: vLLM 是一个开源高吞吐量 LLM 推理引擎，支持多种模型架构和硬件后端。Inkling 模型家族是 Thinking Machines Lab 推出的通用多模态模型，可接受文本、图像和音频输入。Hopper FA4 指针对 NVIDIA Hopper 架构优化的 FlashAttention-4，而 ModelOpt NVFP4 是 NVIDIA 的一种量化方法，使用 4 位浮点权重。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/thinkingmachines/Inkling">thinkingmachines/ Inkling · Hugging Face</a></li>
<li><a href="https://nvidia.github.io/TensorRT-LLM/latest/features/quantization.html">Quantization — TensorRT LLM</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#performance optimization`, `#GPU kernels`, `#open source`

---

<a id="item-3"></a>
## [Anthropic 主张对开放权重模型进行强制安全测试](https://www.anthropic.com/news/position-open-weights-models) ⭐️ 8.0/10

Anthropic 发布了一份立场声明，主张对所有足够强大的 AI 模型（包括开放权重模型）进行强制安全测试，批评者认为这实际上是在禁止开放权重模型。 这家领先 AI 公司的政策立场可能影响监管并塑造开放权重 AI 开发的未来，可能限制对强大模型的访问，并引发安全与开放之间的辩论。 Anthropic CEO Dario Amodei 还支持禁止向中国销售芯片并打击走私，一些评论者认为这与他声称反对禁令的立场相矛盾。该公司未明确说明由谁负责安全测试或如何管理成本。

hackernews · surprisetalk · Jul 27, 22:03 · [社区讨论](https://news.ycombinator.com/item?id=49076057)

**背景**: 开放权重模型是指其训练参数公开发布的 AI 模型，允许任何人下载、运行和微调，这与 GPT-4 等完全封闭的模型不同。它们促进了广泛的访问和创新，但也引发了安全担忧，因为它们可以不受限制地使用。Anthropic 提出的强制安全测试要求所有强大模型在发布前通过政府管理的测试，批评者认为这对开放权重模型不切实际，实际上等于禁止。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/open-weights-llms-in-depth-analysis-adoption-usage-performance-jha-kymhc">Open - Weights LLMs: In-Depth Analysis of Adoption, Usage, and...</a></li>
<li><a href="https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss">OpenAI open - weight models (gpt-oss) | OpenAI Help Center</a></li>
<li><a href="https://medium.com/@aruna.kolluru/exploring-the-world-of-open-source-and-open-weights-ai-aa09707b69fc">Exploring the World of Open Source and Open Weights AI | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区评论高度怀疑，用户认为强制测试因成本和行政障碍实际上会禁止开放权重模型。一些人指出 Anthropic 立场中的矛盾，例如支持芯片禁令却声称不赞成禁令。其他人指责该公司利用安全言论保护其商业利益。

**标签**: `#AI safety`, `#open-weights`, `#regulation`, `#Anthropic`, `#policy`

---

<a id="item-4"></a>
## [Python-build-standalone：便携式 Python 发行版](https://gregoryszorc.com/docs/python-build-standalone/main/) ⭐️ 8.0/10

Python-build-standalone 提供自包含、高度便携的 Python 发行版，现由 Astral（uv 的创建者）维护，并被 uv、pipx、Hatch 和 Poetry 等主要工具用于将 Python 捆绑到应用程序中。 这些发行版简化了开发者的 Python 分发流程，使工具无需用户管理系统 Python 安装即可安装 Python，是现代 Python 打包和部署的关键基础设施。 这些发行版基于上游 CPython 构建并进行了可移植性修改，Astral 已接管维护，并计划将更改上游化。它们被 uv、pipx、Hatch、Poetry、Bazel 等工具使用。

hackernews · jcbhmr · Jul 27, 18:43 · [社区讨论](https://news.ycombinator.com/item?id=49073942)

**背景**: Python 打包通常需要将 Python 解释器与应用程序捆绑在一起，但由于平台差异，这可能很复杂。Python-build-standalone 通过提供预构建的、可移植的 Python 二进制文件来解决这个问题，这些文件可以轻松嵌入。相关项目如 PyOxidizer 和 Cosmopolitan 提供了创建单文件可执行文件或跨平台二进制文件的替代方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/astral-sh/python-build-standalone">GitHub - astral-sh/ python - build - standalone : Produce redistributable...</a></li>
<li><a href="https://docs.astral.sh/uv/">uv is an extremely fast Python package and project manager, written...</a></li>

</ul>
</details>

**社区讨论**: 社区成员对这些发行版表示赞赏，charliermarsh（uv 创建者）确认它们在 uv 和其他工具中的使用。Simonw 指出 Astral 的维护，并推荐将它们用于将 Python 捆绑到桌面应用中。其他人提到了相关项目如 PyOxidizer 和 Cosmopolitan 作为替代方案。

**标签**: `#Python`, `#packaging`, `#portability`, `#build-tools`, `#infrastructure`

---

<a id="item-5"></a>
## [缺失的下划线导致无辜者被错判入狱 18 个月](https://arstechnica.com/tech-policy/2026/07/police-missed-one-underscore-and-sent-the-wrong-man-to-prison/) ⭐️ 8.0/10

Kik 用户名中缺失的一个下划线导致警方逮捕并定罪了错误的人，该无辜者在监狱服刑 18 个月后，错误才被发现，定罪被撤销。 此案暴露了执法和司法系统在处理数字证据方面的严重缺陷，表明一个简单的打字错误就能毁掉一个无辜者的生活。它强调了严格验证数字标识符的必要性，以及对法医调查人员进行更好培训的需求。 受害者 Klayme 与犯罪毫无关联：没有不雅照片，也没有证据表明他在相关期间使用过 Kik，但他在审判中被判有罪。错误在于用户名中缺失了一个下划线，导致与真正嫌疑人的用户名不同。

hackernews · quantified · Jul 27, 22:10 · [社区讨论](https://news.ycombinator.com/item?id=49076116)

**背景**: 数字取证通常依赖用户名和在线标识符将嫌疑人与犯罪联系起来。然而，用户名可能区分大小写并包含下划线等特殊字符，容易导致人为错误。此案与经典的计算机科学警示故事（如《Computers Don't Argue》）类似，警示盲目信任自动化系统的危险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/368900790_Wrongful_Conviction_in_England_and_Wales_An_Assessment_of_Successful_Appeals_and_Key_Contributors">(PDF) Wrongful Conviction in England and Wales: An Assessment of...</a></li>
<li><a href="https://www.nacdl.org/Landing/Postconviction">NACDL - Postconviction</a></li>

</ul>
</details>

**社区讨论**: 评论者对受害者未获赔偿表示愤慨，并质疑在证据如此不足的情况下审判如何能定罪。一些人将其与经典故事《Computers Don't Argue》相提并论，强调了在没有适当验证的情况下过度依赖数字证据的危险。

**标签**: `#digital forensics`, `#wrongful conviction`, `#legal tech`, `#privacy`, `#systemic failure`

---

<a id="item-6"></a>
## [法官驳回谷歌用 DMCA 抗辩数据抓取](https://www.techdirt.com/2026/07/27/judge-rejects-googles-attempt-to-dmca-its-way-out-of-being-scraped/) ⭐️ 8.0/10

一名法官裁定，谷歌不能利用《数字千年版权法》（DMCA）阻止第三方抓取其搜索结果，驳回了谷歌试图对搜索引擎结果页面主张版权保护的做法。 这一裁决确立了搜索结果可能不受 DMCA 版权保护的法律先例，可能影响企业控制数据访问和网络抓取行为的方式。同时，它也凸显了谷歌自身抓取网络的历史与其限制他人抓取之间的紧张关系。 该案涉及谷歌起诉 SerpAPI（一家为客户抓取谷歌搜索结果的服務）。谷歌主张抓取行为侵犯其版权，但法官认为搜索结果页面缺乏版权保护所需的原创性，且 DMCA 安全港条款不适用于谷歌自身的防抓取措施。

hackernews · cdrnsf · Jul 27, 18:15 · [社区讨论](https://news.ycombinator.com/item?id=49073513)

**背景**: DMCA 是美国版权法，包含保护在线服务提供商免于因用户生成内容承担责任的安全港条款，以及反规避规则。网络抓取的合法性通常取决于被抓取数据是否受版权或服务条款保护。谷歌已弃用其官方搜索 API，导致获取搜索数据的合法途径极少，从而推动了对第三方抓取服务的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eff.org/issues/dmca">DMCA | Electronic Frontier Foundation</a></li>
<li><a href="https://blog.apify.com/is-web-scraping-legal/">Is web scraping legal ? Yes, if you know the rules.</a></li>
<li><a href="https://www.scrapeless.com/en/blog/google-search-api-alternatives">Top Google Search API Alternatives : 2025 List</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍支持该裁决，批评谷歌在缺乏良好 API 的同时起诉填补空白的第三方。有人指出，谷歌建立在抓取开放网络的基础上，如今却试图阻止抓取，颇具讽刺意味。其他人则讨论了数据库保护的法律细微差别以及抓取在揭露诈骗中的重要性。

**标签**: `#legal`, `#web scraping`, `#Google`, `#DMCA`, `#data access`

---

<a id="item-7"></a>
## [研究人员完全控制沃尔沃/埃契尔车队平台](https://eaton-works.com/2026/07/27/my-eicher-hack/) ⭐️ 8.0/10

安全研究员 Eaton Works 披露了 VE Commercial Vehicles 的 My Eicher 车队管理平台中的一个严重漏洞，攻击者可接管任何用户账户并控制所有连接的车辆。 该漏洞凸显了依赖云端的车辆管理系统的风险，一个缺陷就可能危及整个车队。它强调了汽车远程信息处理中强安全性的必要性，并引发了对维修权和用户控制的担忧。 研究人员于 2025 年 11 月 3 日报告了该漏洞，在未收到回复后多次跟进。主要漏洞于 2025 年 11 月 20 日修复，但披露于 2026 年 7 月 27 日发布，相隔近八个月。

hackernews · EatonZ · Jul 27, 15:08 · [社区讨论](https://news.ycombinator.com/item?id=49070756)

**背景**: 像 My Eicher 这样的车队管理平台允许公司通过云 API 远程监控和控制车辆。这些系统处理跟踪、锁定和启动车辆等敏感功能，使其成为攻击者的诱人目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eaton-works.com/2026/07/27/my-eicher-hack/">Exploiting Volvo / Eicher ’s fleet management platform to gain control...</a></li>
<li><a href="https://thepixelspulse.com/posts/exploiting-volvoeichers-fleet-platform-to-gain-control-over-all-usersvehicles/">Exploiting VolvoEicher's fleet platform to gain control over all...</a></li>

</ul>
</details>

**社区讨论**: 评论者赞扬了研究人员的耐心，指出其披露时间线非常宽厚。一些人表达了对现代汽车依赖云服务的更广泛担忧，举例说明车辆因连接问题无法启动，并将讨论与维修权倡导联系起来。

**标签**: `#security`, `#automotive`, `#vulnerability`, `#fleet management`, `#responsible disclosure`

---

<a id="item-8"></a>
## [llama.cpp b10155 新增 MiMo-V2.5 音频输入支持](https://github.com/ggml-org/llama.cpp/releases/tag/b10155) ⭐️ 7.0/10

llama.cpp 版本 b10155 新增了对基于 RVQ 的 MiMo-V2.5 音频输入的支持，使得这一开源大模型推理引擎能够处理多模态音频。 此次更新扩展了 llama.cpp 的多模态能力，允许用户本地运行基于音频的模型，对边缘 AI 和隐私敏感应用具有重要意义。 该版本包含 MiMo 音频的 GGUF 转换器、C++ 实现，以及针对 macOS、Linux、Windows、Android 和 iOS 等多个平台的预编译二进制文件。

github · github-actions[bot] · Jul 27, 21:59

**背景**: MiMo-V2.5 是小米推出的原生全模态模型，支持文本、图像、视频和音频理解。RVQ（残差向量量化）是一种音频编解码技术，用于将音频压缩为离散 token，供语言模型处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mimo.mi.com/">Xiaomi MiMo Home</a></li>
<li><a href="https://deepinfra.com/XiaomiMiMo/MiMo-V2.5">XiaomiMiMo/ MiMo - V 2 . 5 - Demo - DeepInfra</a></li>
<li><a href="https://arxiv.org/pdf/2502.20067">UniCodec: Unified Audio Codec with Single Domain-Adaptive Codebook</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#multimodal`, `#audio`, `#machine learning`, `#open source`

---

<a id="item-9"></a>
## [Open WebUI v0.11.0：全面视觉重构发布](https://github.com/open-webui/open-webui/releases/tag/v0.11.0) ⭐️ 7.0/10

Open WebUI v0.11.0 对其界面进行了全面的视觉重构，包括聊天视图、管理面板、字体和间距，采用了更窄的对话列并重新排列了设置项。 这一重构显著提升了这一最受欢迎的开源 LLM UI 平台的用户体验，使其对普通用户和管理员都更加现代和直观。 此次更新涉及超过 30 个提交和一个拉取请求 (#27178)，专注于视觉一致性，包括更轻的字体、更整洁的间距和清晰的文本框轮廓。

github · github-actions[bot] · Jul 27, 09:30

**背景**: Open WebUI 是一个开源、自托管的 Web 界面，用于与大型语言模型（LLM）交互。它提供类似 ChatGPT 的体验，同时允许用户本地运行模型或连接远程 API。此次发布纯粹专注于 UI/UX 改进，而非新的后端功能。

**标签**: `#open-webui`, `#UI/UX`, `#release`, `#LLM`, `#open-source`

---

<a id="item-10"></a>
## [案例研究：用 HTMX 替换 React 的论坛平台迁移](https://misago-project.org/t/removing-reactjs-from-the-codebase-and-adapting-htmx-for-ui-interactivity/1267/) ⭐️ 7.0/10

Misago 论坛项目从代码库中移除了 React.js，并采用 HTMX 实现 UI 交互，在 2023 年的一篇详细案例研究中分享了他们的经验。 这一迁移表明，对于论坛等服务器渲染的应用，HTMX 能以更低的复杂度提供足够的交互性，挑战了重型客户端框架的主导地位。 HTMX 允许开发者直接在 HTML 中使用属性添加 AJAX、CSS 过渡、WebSocket 和服务器推送事件，无需编写 JavaScript 即可实现动态更新。该案例研究强调了代码更简单、与服务器端渲染更契合等优势。

hackernews · Ralfp · Jul 27, 09:58 · [社区讨论](https://news.ycombinator.com/item?id=49067301)

**背景**: React 是一个流行的用于构建交互式用户界面的 JavaScript 库，但它需要大量客户端 JavaScript，并且可能为内容型网站增加复杂性。HTMX 是一个轻量级库，通过超媒体驱动的交互性扩展 HTML，允许开发者通过从服务器返回 HTML 片段来构建现代 UI。这种方法特别适用于论坛等应用，其中大部分内容是文本和图像，无需完整的客户端渲染。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://htmx.org/">htmx - high power tools for html</a></li>
<li><a href="https://juejin.cn/post/7272523490498134071">htmx -使HTML更强大 htmx 让我们可以在html中使用属性直接访问AJAX...</a></li>
<li><a href="https://htmx.uk/">htmx</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍称赞这一举措，许多人分享了自己在服务器渲染应用中使用 HTMX 的积极经验。一些人指出 HTMX 非常适合论坛和类似的内容密集型网站，而另一些人则建议将 HTMX 与小型客户端框架（如 Vue 或 React）结合用于高度交互的组件。

**标签**: `#HTMX`, `#React`, `#web development`, `#server-side rendering`, `#case study`

---

<a id="item-11"></a>
## [Paged Out #9：免费黑客杂志发布](https://pagedout.institute/download/PagedOut_009.pdf) ⭐️ 7.0/10

Paged Out #9，一本面向黑客的免费 PDF 杂志，已发布，包含深入的技术文章，涵盖 C 语言编程和亚像素渲染等主题。 这本杂志填补了对好奇心驱动、底层技术内容的需求，让人想起 2600 和 Phrack 等经典杂志，并受到黑客社区的高度赞赏。 该杂志可从 Paged Out 网站免费下载 PDF 版本，印刷版预计将通过 Lulu 销售。社区称赞其精美的设计和多样化的主题。

hackernews · laurensr · Jul 27, 14:22 · [社区讨论](https://news.ycombinator.com/item?id=49070138)

**背景**: Paged Out 是一本免费的、由社区驱动的黑客杂志，专注于技术深度和好奇心驱动的内容，类似于历史上的 2600 和 Phrack 等杂志。它涵盖底层编程、安全和其他黑客相关主题。

**社区讨论**: 评论者对发布表示兴奋，有人注意到像《Baby Steps in C》这样的文章中的幽默，并将该杂志与经典黑客出版物进行了有利比较。一位用户询问了印刷版的可用性。

**标签**: `#hacker zine`, `#technical publication`, `#programming`, `#low-level`, `#community`

---

<a id="item-12"></a>
## [Libsm64：将《超级马力欧 64》作为可复用库用于游戏引擎](https://github.com/libsm64/libsm64) ⭐️ 7.0/10

Libsm64 是一个开源库，提取了《超级马力欧 64》的角色和机制，允许开发者将马力欧集成到 Unity 或 Source 等其他游戏引擎中。它提供了用于控制马力欧移动、碰撞和动画的 C 语言 API。 该库实现了创造性的跨游戏集成，例如将马力欧放入《半条命 2》中，而无需依赖区块链或专有元宇宙平台。它展示了逆向工程经典游戏以创造新体验的潜力。 该库基于原始《超级马力欧 64》ROM 的反编译构建，并提供了渲染、物理和输入处理的函数。它采用 GPL-2.0 许可证，已被用于 Unity 集成和 VR 模组等项目。

hackernews · klaussilveira · Jul 27, 10:04 · [社区讨论](https://news.ycombinator.com/item?id=49067352)

**背景**: 《超级马力欧 64》是 1996 年具有里程碑意义的平台游戏，以其 3D 移动和摄像机系统而闻名。像 libsm64 这样的逆向工程项目通过反编译游戏代码来理解并合法地复用其机制，用于非商业目的。

**社区讨论**: 评论者热情高涨，称其为最喜爱的库，并指出它实现了可互换游戏角色的承诺，没有炒作。有人分享了演示视频和使用 libsm64 的项目精选列表，还有人开玩笑说任天堂可能不会批准。

**标签**: `#game development`, `#reverse engineering`, `#open source`, `#library`, `#retro gaming`

---

<a id="item-13"></a>
## [Ami：开源本地优先的图记忆智能代理](https://github.com/NanoNets/ami) ⭐️ 7.0/10

Ami 是一个开源、本地优先的 AI 代理，能通过学习用户风格并维护图记忆，跨应用自主执行琐碎工作。它可以获取错误报告、创建修复 PR、调试问题，并根据活动自动更新工单。 Ami 通过将本地优先架构与图记忆相结合，代表了个人 AI 助手的新方法，增强了隐私和自主性。它能够学习用户风格并跨应用执行任务，有望显著提高开发者和知识工作者的生产力。 Ami 使用上下文图记忆，存储实体、关系、反馈、决策和写作风格，使其随着使用变得更加自主。它需要个人令牌来连接应用，并在执行风险操作前请求批准。

rss · Hacker News Show HN · Jul 27, 22:55

**背景**: 本地优先的 AI 代理在本地运行编排和记忆，仅将模型请求发送到云端 API，从而提升隐私并降低延迟。图记忆将信息存储为实体和关系的连接网络，与传统向量存储相比，能实现更具上下文且高效的检索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.getzep.com/">Agent memory at enterprise scale — Zep</a></li>
<li><a href="https://munderdiffl.in/blog/why-local-first-matters-for-ai-agents/">Why Local - First Matters for Your AI Agents — Munder Difflin Blog</a></li>
<li><a href="https://ai.plainenglish.io/beyond-the-context-how-memory-and-promise-graphs-make-powerful-agents-da8caa74703e">Beyond the Context: How Memory and Promise Graphs Make...</a></li>

</ul>
</details>

**社区讨论**: HN 上唯一的评论询问技术栈以及是否使用本地 LLM。作者回复说目前使用 OpenAI，但计划通过 Ollama 支持本地模型。

**标签**: `#AI agent`, `#open-source`, `#local-first`, `#graph memory`, `#productivity`

---

<a id="item-14"></a>
## [CISA 将两个正在被利用的漏洞加入 KEV 目录](https://www.cisa.gov/news-events/alerts/2026/07/27/cisa-adds-two-known-exploited-vulnerabilities-catalog) ⭐️ 7.0/10

CISA 于 2026 年 7 月 27 日将 CVE-2025-68686（Fortinet FortiOS 信息泄露）和 CVE-2026-16812（Arista VeloCloud Orchestrator OS 命令注入）加入其已知被利用漏洞（KEV）目录，原因是存在活跃利用的证据。 这些漏洞在广泛使用的企业产品中被积极利用，对联邦机构和私营组织构成重大风险。CISA 的 KEV 新增条目是安全团队优先修补漏洞、防范潜在入侵的关键警报。 CVE-2025-68686 是 Fortinet FortiOS SSL-VPN 中的信息泄露漏洞，而 CVE-2026-16812 是 Arista VeloCloud Orchestrator 本地部署版中 CVSS 10.0 的 OS 命令注入漏洞。两者均被积极利用，并有明确的缓解指南。

rss · CISA Cybersecurity Advisories · Jul 27, 12:00

**背景**: CISA 的已知被利用漏洞（KEV）目录列出了在野外被积极利用的漏洞，要求联邦机构根据约束性操作指令（BOD）26-04 及时修复。Fortinet FortiOS 是广泛使用的网络安全平台，Arista VeloCloud 是流行的 SD-WAN 编排器。信息泄露和命令注入是常见的攻击向量，可能导致数据泄露或系统完全沦陷。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://suriq.io/blog/velocloud-orchestrator-cve-2026-16812-onprem-command-injection">VeloCloud Orchestrator RCE (CVE-2026-16812) exploited</a></li>
<li><a href="https://www.sentinelone.com/vulnerability-database/cve-2025-25250/">CVE-2025-25250: Fortinet FortiOS Info Disclosure Flaw</a></li>

</ul>
</details>

**标签**: `#CISA`, `#vulnerability`, `#exploitation`, `#Fortinet`, `#Arista`

---

<a id="item-15"></a>
## [Ethan Mollick 更新 AI 指南：转向智能体系统](https://simonwillison.net/2026/Jul/27/an-opinionated-guide-to-which-ai-to-use-to-do-stuff/#atom-everything) ⭐️ 7.0/10

Ethan Mollick 发布了一份更新的观点性 AI 使用指南，反映了从聊天式模型向智能体系统的转变。他现在推荐 ChatGPT 和 Claude 而非 Gemini，并指出 Google 的 Gemini Spark 尚未在 Codex/ChatGPT Work/Cowork 类别中证明自己。 该指南帮助用户驾驭快速演变的 AI 格局，其中智能体系统可以自主完成相当于数小时的人类工作。它凸显了智能体能力日益增长的重要性以及主要 AI 提供商之间的竞争动态。 Mollick 解释说，ChatGPT Work 和 Claude Cowork 是让 AI 访问计算机的模式，而 Codex 和 Code 是独立的编码智能体。他指出命名约定令人困惑，并且移动端的 ChatGPT Work 与桌面应用不同，后者作为 Codex 之上的界面层，具有互联网访问权限。

rss · Simon Willison · Jul 27, 21:55

**背景**: 智能体系统是能够自主执行复杂任务的 AI 系统，通常通过使用工具或访问计算机来实现。它们代表了从简单的聊天式交互向更强大、面向行动的 AI 的转变。主要 AI 公司如 OpenAI 和 Anthropic 提供智能体模式，如 ChatGPT Work 和 Claude Cowork，而 Google 的 Gemini Spark 是较新的入局者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.prestoncardwell.com/p/039-chatgpt-work-gpt-5-6-and-claude-cowork-on-mobile">#039: ChatGPT Work , GPT -5.6, and Claude Cowork on Mobile</a></li>
<li><a href="https://ai-bot.cn/gemini-spark/">Gemini Spark - 谷歌推出的个人 AI Agent | AI工具集</a></li>

</ul>
</details>

**标签**: `#AI`, `#agentic systems`, `#LLMs`, `#productivity`, `#opinionated guide`

---