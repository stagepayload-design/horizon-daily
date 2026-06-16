# Horizon 每日速递 - 2026-06-16

> From 61 items, 15 important content pieces were selected

---

1. [LinkedIn 工作邀请中的后门利用 npm prepare 脚本](#item-1) ⭐️ 9.0/10
2. [vLLM v0.23.0：DeepSeek-V4 加固，MRv2 扩展](#item-2) ⭐️ 8.0/10
3. [将禁书藏入 Wi-Fi 智能灯泡](#item-3) ⭐️ 8.0/10
4. [Iroh 1.0：点对点网络库发布](#item-4) ⭐️ 8.0/10
5. [福克斯以 220 亿美元收购 Roku](#item-5) ⭐️ 8.0/10
6. [Salesforce 以 36 亿美元收购 Fin（前身为 Intercom）](#item-6) ⭐️ 8.0/10
7. [Rust 与 C/C++内存安全 CVE 差异分析](#item-7) ⭐️ 8.0/10
8. [Typst 0.15.0：新增路径类型与改进脚注](#item-8) ⭐️ 8.0/10
9. [开发者分享本地 LLM 编程设置](#item-9) ⭐️ 7.0/10
10. [Hetzner 云服务器价格最高上涨 3 倍](#item-10) ⭐️ 7.0/10
11. [TimescaleDB Hypercore 压缩详解](#item-11) ⭐️ 7.0/10
12. [深入解析《指挥官基恩》的平滑滚动引擎](#item-12) ⭐️ 7.0/10
13. [为 Visual Studio 带来 Claude Code 原生差异接受/拒绝功能](#item-13) ⭐️ 7.0/10
14. [CISA 将两个正在被利用的漏洞加入 KEV 目录](#item-14) ⭐️ 7.0/10
15. [性格冲突导致 Anthropic 模型被暂停](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [LinkedIn 工作邀请中的后门利用 npm prepare 脚本](https://roman.pt/posts/linkedin-backdoor/) ⭐️ 9.0/10

一名求职者发现招聘人员为虚假面试发送的 GitHub 仓库中隐藏了后门，该后门利用 npm 的 prepare 脚本在运行 npm install 时执行任意代码。 此次攻击揭示了一种针对求职面试中开发者的新型供应链攻击向量，利用信任和常见工作流程，并凸显了当前网络犯罪报告机制的不足。 后门隐藏在注释掉的测试代码之间，利用 npm 的 prepare 生命周期脚本（在 npm install 后自动运行）执行负载，该负载可从远程服务器运行任意命令。

hackernews · lwhsiao · Jun 15, 20:00 · [社区讨论](https://news.ycombinator.com/item?id=48546294)

**背景**: npm（Node Package Manager）是 JavaScript 广泛使用的包管理器，其 prepare 脚本是一个生命周期钩子，会在 npm install 后自动运行。通过恶意 npm 包进行的供应链攻击日益令人担忧，最近的 Axios npm 包事件就是例证。此次攻击通过虚假面试诱骗开发者运行恶意代码，扩展了这一概念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/works-on-my-machine/the-axios-npm-supply-chain-attack-what-happened-how-to-check-if-you-were-hit-and-what-to-do-now-2bcc10ba2460">The Axios npm Supply Chain Attack What Happened, How... | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了对这种攻击与正常面试任务非常相似的担忧，许多开发者可能会毫无怀疑地运行 npm install。用户还批评 GitHub 和 LinkedIn 在移除恶意仓库和账户方面反应迟缓，呼吁建立更好的网络犯罪报告基础设施。

**标签**: `#supply chain attack`, `#npm`, `#backdoor`, `#job scam`, `#cybersecurity`

---

<a id="item-2"></a>
## [vLLM v0.23.0：DeepSeek-V4 加固，MRv2 扩展](https://github.com/vllm-project/vllm/releases/tag/v0.23.0) ⭐️ 8.0/10

vLLM v0.23.0 发布，包含来自 200 位贡献者的 408 次提交，主要对 DeepSeek-V4 进行了大幅加固和优化，将 Model Runner V2 默认扩展到 Llama 和 Mistral 密集模型，并完善了 Rust 前端。 此版本显著提升了 DeepSeek-V4 及其他流行密集模型在生产部署中的性能和稳定性，使 vLLM 成为 LLM 服务中更关键的基础设施组件。 DeepSeek-V4 获得了稀疏 MLA 元数据解耦、TRTLLM-gen 注意力内核、Mega-MoE 的 EPLB 支持以及选择性前缀缓存保留。Model Runner V2 现在默认用于 Llama 和 Mistral 密集模型，并支持 FlashInfer 采样器和可中断 CUDA 图。

github · khluu · Jun 15, 05:27

**背景**: vLLM 是一个开源的高吞吐量 LLM 推理引擎。Model Runner V2 是重新设计的执行流水线，可减少 Python 开销并提高 GPU 利用率。DeepSeek-V4 是一个具有混合专家架构的大型语言模型，需要专门的优化才能实现高效推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/design/model_runner_v2/">Model Runner V 2 Design Document - vLLM</a></li>
<li><a href="https://charlestar.github.io/2026/05/25/vllm-model-runner-v2-architecture-refactoring-gpu-native-and-zero-sync-design-analysis/">vLLM Model Runner V 2 架构重构：GPU-native...</a></li>
<li><a href="https://www.spheron.network/blog/vllm-model-runner-v2-mrv2-deployment-guide/">vLLM Model Runner V 2 on GPU Cloud: Deploy... | Spheron Blog</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#DeepSeek-V4`, `#open source`, `#AI infrastructure`

---

<a id="item-3"></a>
## [将禁书藏入 Wi-Fi 智能灯泡](https://www.richardosgood.com/posts/banned-book-library/) ⭐️ 8.0/10

一位开发者创建了一个项目，将禁书存储在 Wi-Fi 智能灯泡中，使其成为可通过网页浏览器访问的便携式图书馆，以规避审查。 该项目展示了物联网设备在数字权利和规避审查方面的创造性用途，可能为在压制性环境中分发受限信息提供一种隐蔽的方式。 该灯泡作为 Wi-Fi 接入点，托管一个包含书籍的网页服务器；其设计使其看起来像普通灯泡，难以被察觉。作者指出了存储限制，并建议未来通过网状网络进行改进。

hackernews · sohkamyung · Jun 15, 22:37 · [社区讨论](https://news.ycombinator.com/item?id=48547985)

**背景**: VPN 和 Tor 等规避审查的工具很常见，但物联网设备为隐藏信息提供了新途径。智能灯泡无处不在且常被忽视，使其成为隐蔽数据存储的理想选择。该项目借鉴了 PirateBox 和 LibraryBox 等早期项目的思路。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ssd.eff.org/module/understanding-and-circumventing-network-censorship">How to: Understand and Circumvent Network Censorship</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该项目的创意及其与数字权利的相关性，一些人指出与 PirateBox 和 Meshtastic 的相似之处。一位评论者质疑检测此类设备的难度，认为它可能并不比其他公共 Wi-Fi 设备更难被关闭。

**标签**: `#censorship`, `#IoT`, `#digital rights`, `#hacking`, `#privacy`

---

<a id="item-4"></a>
## [Iroh 1.0：点对点网络库发布](https://www.iroh.computer/blog/v1) ⭐️ 8.0/10

Iroh 1.0 已发布，这是一个用于 Rust 的点对点网络库，支持应用实例之间的直接连接，其思维模型类似于“应用层的 Tailscale”。 该版本为应用开发者提供了一种新方法，可以轻松嵌入点对点网络功能，无需用户管理账户或复杂的基础设施，可能简化去中心化应用的开发。 Iroh 1.0 目前开箱即支持 IPv4、IPv6 和中继传输，并允许实现自定义传输以支持 WebRTC 或 BLE 等其他协议。

hackernews · chadfowler · Jun 15, 15:13 · [社区讨论](https://news.ycombinator.com/item?id=48542480)

**背景**: 点对点网络允许设备之间直接通信，无需中央服务器。Tailscale 是一种流行的工具，它在网络层创建安全的网络覆盖，但需要用户账户，并且不适合嵌入到应用程序中。Iroh 旨在在应用层提供类似的功能，使应用开发者更容易在应用实例之间添加直接连接。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tailscale.com/kb/1456/osi">Learn how Tailscale relates to the OSI model layers .</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调了与应用层 Tailscale 的类比，开发者询问对 WebRTC 和 BLE 等额外传输的支持。一些用户对 Iroh 解决的问题表示困惑，而另一些用户则赞扬了去中心化的愿景。

**标签**: `#networking`, `#peer-to-peer`, `#rust`, `#open-source`, `#release`

---

<a id="item-5"></a>
## [福克斯以 220 亿美元收购 Roku](https://www.wsj.com/business/deals/fox-roku-deal-f6e564f9) ⭐️ 8.0/10

福克斯公司已同意以约 220 亿美元收购 Roku，这是近年来流媒体行业最大的收购案之一。 此次收购将一家大型内容公司与领先的流媒体分发平台结合，引发了重大的反垄断担忧，并可能终结 Roku 作为中立平台的声誉。 为获得反垄断批准，福克斯已承诺保持 Roku 平台对 Netflix、Disney+和 Max 等竞争对手开放。消息公布后，福克斯股价下跌 15%。

hackernews · thm · Jun 15, 12:50 · [社区讨论](https://news.ycombinator.com/item?id=48540499)

**背景**: Roku 是一家流媒体设备和平台公司，以其简单、以应用为先的用户体验和平台中立性而闻名，这使其对 OTT 服务具有吸引力。福克斯是一家大型内容提供商，拥有福克斯新闻和福克斯体育等资产。该交易引发了对福克斯服务获得优待以及媒体整合的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://easternherald.com/2026/06/15/fox-corporation-roku-22-billion-acquisition-antitrust-open-platform/">Fox Buys Roku for $22 Billion — and Its Biggest Problem Is Its Own...</a></li>
<li><a href="https://artikls.com/article/fox-acquires-roku-22-billion-streaming-deal">Fox Acquires Roku in Landmark $22 Billion Streaming Deal | Artikls</a></li>
<li><a href="https://tech-oracle.com/5-biggest-concerns-after-foxs-22-billion-roku-acquisition/">5 Biggest Concerns After Fox ’s $22 Billion Roku Acquisition – Top...</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍悲观，用户对 Roku 平台中立性的丧失以及福克斯可能优先推广自家内容表示担忧。一些用户建议改用 Nvidia Shield 等替代方案并搭配自定义启动器，以避免广告和偏见。

**标签**: `#acquisition`, `#streaming`, `#media`, `#antitrust`, `#Roku`

---

<a id="item-6"></a>
## [Salesforce 以 36 亿美元收购 Fin（前身为 Intercom）](https://www.salesforce.com/news/press-releases/2026/06/15/salesforce-signs-definitive-agreement-to-acquire-fin/?bc=HL) ⭐️ 8.0/10

Salesforce 已签署最终协议，以 36 亿美元收购 Fin（前身为 Intercom）这一 AI 驱动的客户支持平台。该收购于 2026 年 6 月 15 日宣布，距离 Intercom 更名为 Fin 仅一个月。 此次收购加剧了 AI 驱动客户服务领域的竞争，尤其是针对由 Salesforce 前联席 CEO Bret Taylor 创立的竞争对手 Sierra。这也表明 Salesforce 的战略意图是防止独立的 AI 支持代理成为其 CRM 生态系统之外的控制点。 Fin 的 AI 代理由专为客户支持构建的专有模型 Apex 提供支持。这笔交易发生在 AI 客户支持领域估值高涨的背景下，Sierra 估值 158 亿美元，Decagon 估值 45 亿美元。

hackernews · colesantiago · Jun 15, 12:08 · [社区讨论](https://news.ycombinator.com/item?id=48540126)

**背景**: Intercom 成立于 2011 年，最初是一个客户消息平台，于 2026 年 5 月更名为 Fin 以突出其 AI 重点。Salesforce 是领先的 CRM 提供商，一直在积极收购 AI 公司以增强其 Service Cloud 产品。此次收购反映了将 AI 代理直接嵌入企业软件堆栈的日益增长的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fin_(company)">Fin (company) - Wikipedia</a></li>
<li><a href="https://martech.org/salesforce-acquires-fin-formerly-known-as-intercom/">Salesforce acquires Fin , formerly known as Intercom</a></li>

</ul>
</details>

**社区讨论**: 社区评论显示出复杂的情绪：一些用户称赞执行良好的 AI 客户支持，以 Starlink 为例，而另一些用户则担心 AI 代理会编造借口。还有关于传统帮助台公司对非企业客户是否可行的讨论，一些用户已转向 Hermes 等替代方案。

**标签**: `#acquisition`, `#AI`, `#customer support`, `#Salesforce`, `#SaaS`

---

<a id="item-7"></a>
## [Rust 与 C/C++内存安全 CVE 差异分析](https://kobzol.github.io/rust/2026/06/15/how-memory-safety-cves-differ-between-rust-and-c-cpp.html) ⭐️ 8.0/10

一项详细分析表明，虽然 Rust 的类型系统消除了 C/C++中常见的许多内存安全漏洞，但它引入了不同的 CVE 模式，例如因意外不变量或 unsafe 代码故障导致的 panic。 这一区别对开发者和安全研究人员至关重要，因为它表明内存安全并不等同于无缺陷软件，并且直接比较不同语言的 CVE 数量可能具有误导性。 该分析以 curl 网络库（用 C 编写）为例，说明 Rust 的所有权模型如何防止缓冲区溢出和释放后使用，但仍可能导致漏洞，例如通过 panic 或 unsafe 块中的逻辑错误引发拒绝服务。

hackernews · nicoburns · Jun 15, 16:11 · [社区讨论](https://news.ycombinator.com/item?id=48543392)

**背景**: 内存安全漏洞（如缓冲区溢出和释放后使用）历史上约占 C/C++软件所有 CVE 的三分之二。Rust 的所有权和类型系统在编译时保证内存安全，消除了这些类型的错误。然而，Rust 代码仍然可能存在漏洞，特别是在 unsafe 代码中或通过违反不变量的 panic。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kobzol.github.io/rust/2026/06/15/how-memory-safety-cves-differ-between-rust-and-c-cpp.html">How memory safety CVEs differ between Rust and... | Kobzol’s blog</a></li>
<li><a href="https://cyberarmy.ai/blog/memory-safe-doesnt-mean-bug-free">Memory -safe doesn't mean bug-free: what Mythos finds in Rust</a></li>
<li><a href="https://v100.ai/blog/rust-vs-cpp-video-server">Rust vs C++ for Video Server Performance: Why V100 Chose ..</a></li>

</ul>
</details>

**社区讨论**: 评论者就 CVE 数量作为指标的实用性进行了辩论，一些人认为由于代码库规模和使用情况的差异，直接比较原始数字毫无意义。其他人指出，Rust 的 Option<T>显式处理空值，不同于 C 的隐式空指针处理，并且 Rust 中的任何类型安全故障都可能被视为漏洞，给开发者带来挑战。

**标签**: `#memory safety`, `#Rust`, `#C/C++`, `#CVEs`, `#systems programming`

---

<a id="item-8"></a>
## [Typst 0.15.0：新增路径类型与改进脚注](https://typst.app/docs/changelog/0.15.0/) ⭐️ 8.0/10

Typst 0.15.0 引入了专门的路径类型用于文件引用，并显著改进了脚注处理，包括支持在单个文档中使用多个参考文献列表。 此版本解决了用户长期以来的痛点，使 Typst 更适合复杂的学术和出版工作流程，并巩固了其作为 LaTeX 可行替代方案的地位。 新的路径类型简化了相对于文档根目录的文件引用，特别是对于本地自定义包。此外，数学方程现在会自动导出为 MathML，以获得更好的 HTML 输出。

hackernews · schu · Jun 15, 17:24 · [社区讨论](https://news.ycombinator.com/item?id=48544396)

**背景**: Typst 是一个基于标记的开源排版系统，旨在作为 LaTeX 的现代替代品。它使用更简单的语法，并能快速编译为 PDF。路径处理和脚注一直是用户反馈的常见领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://typst.app/docs/reference/foundations/path/">Path - Typst Documentation</a></li>
<li><a href="https://github.com/typst/typst">GitHub - typst / typst : A markup-based typesetting system that is...</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍积极，用户对路径类型和改进的脚注表示兴奋。一些用户分享了具体用例，例如撰写带有论述性脚注的学位论文以及制作包含多个参考文献列表的书籍。

**标签**: `#typesetting`, `#open-source`, `#release`, `#typst`

---

<a id="item-9"></a>
## [开发者分享本地 LLM 编程设置](https://news.ycombinator.com/item?id=48542100) ⭐️ 7.0/10

Hacker News 用户报告称，他们已用 Qwen 3.6 和 Gemma 等本地模型取代了 Claude 和 GPT 等云端编程助手，并使用 Pi harness 和 llama.cpp 等工具。在双 RTX 3090 等消费级硬件上，他们实现了每秒 150 个 token 以上的速度。 这一转变表明，本地模型在日常编程中正变得可行，在不过多牺牲性能的情况下提供了隐私保护和成本节约。这可能会减少对昂贵云 API 的依赖，并加速本地 AI 工具的采用。 用户报告称，Qwen 3.6 35B（3B 活跃参数）和 Gemma 4 26B 等本地模型在高 RAM Mac Studio 或双 RTX 3090 配置上运行良好。虽然不如 Claude 或 GPT 智能，但足以完成大多数编程任务，偶尔会回退到云端模型。

hackernews · cloudking · Jun 15, 14:46

**背景**: 本地 LLM 在用户自己的硬件上运行，保护数据隐私并避免重复的 API 费用。llama.cpp 和 Ollama 等工具可在消费级 GPU 上实现高效推理。Qwen 3.6 和 Gemma 是近期针对编程任务优化的开源权重模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/data-science-collective/how-to-build-your-own-llm-coding-assistant-with-qwen2-5-coder-b26aaadf071d">How to Build Your Own LLM Coding Assistant With... | Medium</a></li>
<li><a href="https://vasilkoff.com/blog/vscodium-and-ollama">VSCodium + Ollama: Local LLM Coding Setup Guide</a></li>
<li><a href="https://dev.to/chung_duy_51a346946b27a3d/use-opencode-with-local-llm-not-bad-all-at-5cdm">Use OpenCode with local LLM , not bad all at - DEV Community</a></li>

</ul>
</details>

**社区讨论**: 评论者对本地设置充满热情，分享了具体的硬件和模型组合。一些人指出，本地模型在质量上落后于前沿模型，但对大多数工作来说已经足够。少数用户仍依赖云端模型处理复杂任务。

**标签**: `#local-llm`, `#coding-assistant`, `#privacy`, `#qwen`, `#llm-performance`

---

<a id="item-10"></a>
## [Hetzner 云服务器价格最高上涨 3 倍](https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/#cloud-servers) ⭐️ 7.0/10

Hetzner 宣布其云服务器价格大幅上涨，部分配置涨幅高达 3 倍，自 2026 年 4 月 1 日起生效，原因是硬件成本上升。 此次涨价反映了更广泛的行业趋势：AI 对 RAM 和 GPU 等硬件的需求推高了成本，影响云用户和可能难以消化如此涨幅的小型提供商。 根据社区对比，云服务器价格上涨 30-43%，专用服务器上涨 3-21%，对象存储上涨 30%，内存附加组件涨幅高达 575%。

hackernews · tuhtah · Jun 15, 13:19 · [社区讨论](https://news.ycombinator.com/item?id=48540844)

**背景**: Hetzner 是一家知名的德国托管服务商，以价格实惠的云和专用服务器著称。此次价格调整归因于全球硬件成本上升，尤其是 RAM 和 SSD，由 AI 基础设施需求驱动。类似趋势已在全行业出现，AWS 和 GCP 等超大规模云服务商利用供应链优势保持价格相对稳定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://netcupvoucher.com/blog/netcup-vs-hetzner-after-rampocalypse-2026">Netcup vs Hetzner After the RAMpocalypse - Updated 2026 Price ...</a></li>
<li><a href="https://xthe.com/news/gartner-warns-of-rising-ai-hardware-costs/">Rising RAM Prices Drive AI Hardware Costs Higher</a></li>

</ul>
</details>

**社区讨论**: 社区对涨幅之大表示震惊，有用户称 3 倍涨幅“疯狂”。一些人争论 AI 是否应归咎于不平等加剧，而另一些人指出硬件稀缺是影响所有提供商的真实问题。

**标签**: `#cloud computing`, `#pricing`, `#hardware costs`, `#AI infrastructure`, `#Hetzner`

---

<a id="item-11"></a>
## [TimescaleDB Hypercore 压缩详解](https://roszigit.com/en/blog/timescaledb-compression-hypercore) ⭐️ 7.0/10

TimescaleDB 的 hypercore 压缩通过列式存储和类型感知技术（如增量编码、增量之增量、simple-8b、游程编码、基于 XOR 的压缩和字典压缩），对时序数据实现了高达 98%的压缩率。 这种压缩显著降低了时序工作负载的存储成本，并能加速某些查询，使 PostgreSQL 在与专用时序数据库的竞争中更具优势。社区讨论强调了查询性能的权衡以及 deltax 等替代方案。 压缩是列式和类型感知的，针对不同数据类型应用不同算法（例如，时间戳使用增量之增量，浮点数使用 XOR）。然而，“高达 98%”的说法被批评可能具有误导性，实际压缩率取决于数据模式。

hackernews · lkanwoqwp · Jun 15, 17:29 · [社区讨论](https://news.ycombinator.com/item?id=48544451)

**背景**: 时序数据库通常使用列式存储，通过只读取相关列来提高分析性能。压缩减少了 I/O 和存储，但可能增加解压时的 CPU 使用。TimescaleDB 是一个为 PostgreSQL 添加时序功能的扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.tigerdata.com/use-timescale/latest/hypercore/compression-methods/">Tiger Data Documentation | About compression methods</a></li>
<li><a href="https://docs.timescale.com/use-timescale/latest/compression/">Timescale Documentation | Compression</a></li>
<li><a href="https://tiger-data-docs.vercel.app/docs/learn/columnar-storage/understand-hypercore">Understand hypercore | Tiger Data Docs</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了压缩与查询性能之间的权衡，有人指出字典编码读取速度可能较慢。提到了 deltax 等替代方案，标题中的“高达”说法被批评为标题党。

**标签**: `#TimescaleDB`, `#compression`, `#time-series`, `#PostgreSQL`, `#database`

---

<a id="item-12"></a>
## [深入解析《指挥官基恩》的平滑滚动引擎](https://forgottenbytes.net/commander_keen.html) ⭐️ 7.0/10

一份关于《指挥官基恩》游戏引擎的技术白皮书已发布，详细介绍了约翰·卡马克和约翰·罗梅罗开创的平滑滚动技术。 这项分析揭示了 PC 游戏开发中的一项基础性突破，展示了卡马克的自适应瓦片刷新引擎如何克服硬件限制实现平滑滚动，影响了后来无数游戏。 白皮书涵盖了 ATR 引擎的技术细节，该引擎采用基于瓦片的方法来最小化重绘，并在当时有限的 VGA 硬件上实现了平滑滚动。

hackernews · mfiguiere · Jun 15, 17:52 · [社区讨论](https://news.ycombinator.com/item?id=48544781)

**背景**: 在 1990 年代初期，PC 游戏常常因硬件缺乏像 SNES 等主机那样的专用精灵和滚动支持而出现卡顿滚动。1990 年发布的《指挥官基恩》是首批实现平滑滚动的 MS-DOS 游戏之一，这得益于卡马克创新的软件解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.generationamiga.com/2023/07/30/how-commander-keen-changed-the-face-of-ms-dos-gaming-forever/">How Commander Keen changed the face of MS-DOS gaming forever</a></li>
<li><a href="https://gamicus.fandom.com/wiki/Commander_Keen">Commander Keen - Codex Gamicus - Humanity's collective gaming ...</a></li>
<li><a href="https://www.wikiwand.com/en/articles/Commander_Keen_(video_game)">Commander Keen (video game ) - Wikiwand</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞了这份白皮书，并推荐了《毁灭战士大师》一书以了解历史背景。一些人指出了当时 PC 与主机硬件的差异，还有用户提到了类似的分析网站如 Cosmodoc。

**标签**: `#game development`, `#retro computing`, `#software history`, `#game engines`

---

<a id="item-13"></a>
## [为 Visual Studio 带来 Claude Code 原生差异接受/拒绝功能](https://github.com/firish/claude_code_vs) ⭐️ 7.0/10

一款新的 Visual Studio 扩展将 Claude Code 与 IDE 的原生差异查看器集成，允许开发者直接接受或拒绝 AI 生成的编辑，并自动将编译器错误和当前选择内容共享给 Claude CLI。 这填补了 Visual Studio 用户此前缺乏官方 Claude Code 集成的重大空白，通过提供类似 VS Code 和 JetBrains 的无缝差异审查体验，改进了 AI 辅助编码工作流。 该扩展实现了与官方插件相同的协议，因此 Claude CLI 无需配置即可自动连接。它还包含一个可停靠面板，显示连接状态和令牌/成本统计，以及一个自动接受编辑的“run wild”开关。

rss · Hacker News Show HN · Jun 15, 23:15

**背景**: Claude Code 是 Anthropic 的 AI 编码助手，通过 CLI 工具运行。虽然 VS Code 和 JetBrains 有官方扩展，但 Visual Studio 缺乏支持，用户需要手动复制粘贴上下文或接受终端提示。此扩展通过利用 Visual Studio 的原生差异查看器来弥合这一差距，提供更集成的体验。

**社区讨论**: Hacker News 上的一条评论对该扩展表示赞赏，指出它解决了 Visual Studio 用户希望集成 Claude Code 的实际痛点。

**标签**: `#Claude Code`, `#Visual Studio`, `#IDE integration`, `#developer tools`, `#AI-assisted coding`

---

<a id="item-14"></a>
## [CISA 将两个正在被利用的漏洞加入 KEV 目录](https://www.cisa.gov/news-events/alerts/2026/06/15/cisa-adds-two-known-exploited-vulnerabilities-catalog) ⭐️ 7.0/10

CISA 已将 CVE-2026-20262（Cisco Catalyst SD-WAN Manager 路径遍历漏洞）和 CVE-2026-54420（LiteSpeed cPanel 符号链接跟随漏洞）加入其已知被利用漏洞（KEV）目录，原因是存在活跃利用证据。 这些新增漏洞要求联邦机构根据 BOD 26-04 优先修补，同时所有组织都被敦促尽快修复这些漏洞，因为它们对企业安全构成重大风险。 Cisco 漏洞允许经过身份验证的远程攻击者通过精心构造的 HTTP 请求创建或覆盖文件，可能导致权限提升至 root；LiteSpeed cPanel 漏洞则允许在共享主机环境中通过符号链接跟随实现权限提升。

rss · CISA Cybersecurity Advisories · Jun 15, 12:00

**背景**: CISA 的已知被利用漏洞（KEV）目录是一个已知在野外被积极利用的漏洞列表。具有约束力的操作指令（BOD）26-04 要求联邦民事行政部门（FCEB）机构在规定时间内修复公开暴露资产上的 KEV 列出的漏洞。虽然该指令仅适用于联邦机构，但 CISA 鼓励所有组织采用基于风险的漏洞管理，并优先处理 KEV 漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cvefeed.io/vuln/detail/CVE-2026-54420">CVE-2026-54420 - LiteSpeed cPanel Plugin Symlink Privilege...</a></li>
<li><a href="https://threat-modeling.com/cve-2026-54420-litespeed-cpanel-symlink-mishandling/">CVE-2026-54420: LiteSpeed cPanel Plugin Symlink Mishandling...</a></li>

</ul>
</details>

**标签**: `#CISA`, `#vulnerability`, `#exploitation`, `#security`, `#KEV`

---

<a id="item-15"></a>
## [性格冲突导致 Anthropic 模型被暂停](https://simonwillison.net/2026/Jun/15/axios-clashes-anthropics/#atom-everything) ⭐️ 7.0/10

Axios 的一篇报道揭示了 Anthropic 与美国政府之间的性格冲突和幕后动态，导致 Anthropic 的前沿模型 Mythos 和 Fable 被暂停访问。关键人物 Logan Graham、Dave Orr 和 Nicholas Carlini 正在与商务部会面以解决这一问题。 这一事件凸显了 AI 实验室与政府监管机构在出口管制和模型安全方面日益紧张的关系，可能为前沿 AI 模型的治理开创先例。其结果可能影响全球对尖端 AI 能力的获取，并塑造未来的 AI 政策。 暂停是由一次越狱攻击引发的，美国政府认为这构成了国家安全风险，而 Anthropic 将其归类为“潜在的非普遍性越狱”。最终结论表明，完美的越狱防御可能是不可能的，可能需要“态度调整”才能恢复访问。

rss · Simon Willison · Jun 15, 14:57

**背景**: Anthropic 最近发布了两个前沿模型：面向普通用户的 Fable 5 和作为可信版本、具有额外安全措施的 Mythos 5。美国政府出于国家安全考虑，发布指令暂停外国用户访问这些模型，理由是可能在网络和生物领域被滥用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://digg.com/tech/fpdiy0g6">Anthropic silently restricts Fable 5 from assisting with frontier LLM...</a></li>
<li><a href="https://cloudnews.tech/claude-fable-5-brings-frontier-models-into-general-use-but-with-limitations/">Claude Fable 5 brings frontier models into general use... | Cloud News</a></li>
<li><a href="https://www.zerohedge.com/ai/anthropic-blocks-foreign-access-fable-5-mythos-5-after-us-national-security-order">Anthropic Blocks Foreign Access To Fable 5, Mythos ... | ZeroHedge</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#Anthropic`, `#export controls`, `#government`, `#frontier models`

---

