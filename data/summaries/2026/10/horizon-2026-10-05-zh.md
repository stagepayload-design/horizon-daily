# Horizon 每日速递 - 2026-10-05

> From 46 items, 7 important content pieces were selected

---

1. [CISA 将已被利用的 Citrix NetScaler 漏洞加入 KEV 目录](#item-1) ⭐️ 8.0/10
2. [Strata 声称在 RTX 4090 上以 124 tokens/秒运行 125B Qwen 模型](#item-2) ⭐️ 7.0/10
3. [浏览器原生的经典 Visual Basic 6 IDE](#item-3) ⭐️ 7.0/10
4. [Homa：旨在取代 AI 集群中 TCP 的新型传输协议](#item-4) ⭐️ 7.0/10
5. [Xray-core 隐瞒证书验证绕过漏洞](#item-5) ⭐️ 7.0/10
6. [提前生成元数据使 Rust 构建与检查速度翻倍](#item-6) ⭐️ 7.0/10
7. [何恺明团队 VISTA 让 Claude 在 ARC-AGI-3 拿到满分](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [CISA 将已被利用的 Citrix NetScaler 漏洞加入 KEV 目录](https://www.cisa.gov/news-events/alerts/2026/10/04/cisa-adds-one-known-exploited-vulnerability-catalog) ⭐️ 8.0/10

2026 年 10 月 4 日，CISA 基于存在主动利用的证据，将 Citrix NetScaler 中一个内存缓冲区操作边界限制不当的漏洞 CVE-2026-88779 加入其已知被利用漏洞（KEV）目录。 Citrix NetScaler ADC 和 Gateway 是广泛部署的企业级设备，通常位于网络边缘，因此一个被主动利用的内存缓冲区漏洞对联邦机构和私营组织都构成重大风险；被列入 KEV 目录后，美国联邦文职机构须依据第 26-04 号约束性操作指令迅速完成修复。 CISA 的公告提供的技术细节极少——没有 CVSS 评分、受影响版本或利用细节——不过第三方来源报告该漏洞 CVSS 评分为 8.5，并将其归类为 NetScaler ADC 和 NetScaler Gateway 中可导致拒绝服务的缓冲区溢出。

rss · CISA Cybersecurity Advisories · Oct 4, 12:00

**背景**: CISA 的已知被利用漏洞（KEV）目录是由网络安全和基础设施安全局维护的权威列表，收录了有可靠证据表明已在野外被主动利用的 CVE；它记录的是攻击者确实在利用某个漏洞，而非该漏洞在理论上的危险程度。第 26-04 号约束性操作指令为联邦文职行政机构制定了基于风险的漏洞管理要求，规定对公开暴露资产上、利用后可获得完全控制权的 KEV 漏洞须迅速修复。Citrix NetScaler ADC 和 NetScaler Gateway 是常见的应用交付和远程访问产品，通常暴露在互联网上，因此经常成为攻击目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog">cisa .gov/ known - exploited - vulnerabilities - catalog</a></li>
<li><a href="https://www.dsecured.com/en/cyber-security-glossary/cisa-kev-catalog">What is the CISA KEV Catalog ? | Cybersecurity Glossary | DSecured</a></li>
<li><a href="https://feedly.com/cve/CVE-2026-88779">CVE - 2026 - 88779 - Exploits & Severity - Feedly</a></li>

</ul>
</details>

**标签**: `#CISA KEV`, `#Citrix NetScaler`, `#actively exploited`, `#vulnerability management`, `#CVE-2026-88779`

---

<a id="item-2"></a>
## [Strata 声称在 RTX 4090 上以 124 tokens/秒运行 125B Qwen 模型](https://github.com/Niko1221/Strata) ⭐️ 7.0/10

一个名为 Strata 的 GitHub 项目声称能在单张消费级 RTX 4090 上以每秒超过 100 个 token 的速度运行 125B 参数模型（Qwen 3.8 Flash Next），有用户在配备 128GB DDR5 和 Ryzen 7950X3D 的 4090 上实测达到 124 tokens/秒。该帖子在 Hacker News 上获得 597 分和 279 条评论，既有热情的复现尝试，也有对量化质量的质疑。 如果该说法成立，就意味着前沿规模的 125B 模型可以在仅需几千美元的硬件上运行，而无需数据中心级 GPU，从而大幅降低本地部署大语言模型的门槛。这也加剧了当前关于为将大模型塞进消费级显存而把量化压到 4-bit 以下会损失多少质量的争论。 该模型名称似乎是虚构或标注错误的，且相关说法没有官方发布或论文支持，因此可信度存疑；一位评论者的独立测试发现，Strata 在视觉任务上的中位误差为 154.8 像素，而相同 GGUF 权重在 llama.cpp 上仅为 46.5 像素，暗示可能存在质量下降。其他用户则报告在租用的 RTX Pro 6000 和 RTX 6000 Pro 硬件上使用 4-bit 量化取得了不错的结果，多并发流下达到每秒数百个 token。

hackernews · snehesht · Oct 4, 12:51 · [社区讨论](https://news.ycombinator.com/item?id=49953495)

**背景**: 量化是一种模型压缩技术，将大语言模型的权重和激活值从高精度格式（如 FP16）转换为低位表示，例如把 70B 模型从约 140GB 压缩到 4-bit 下的约 35GB，从而能装进单张 GPU。要在 24GB 显存的 RTX 4090 上运行 125B 模型，需要非常激进的量化，很可能低于 4-bit，这正是质量担忧的来源。Strata 被定位为 llama.cpp 和 vLLM 等成熟推理栈的替代方案，而 Qwen 3.8 Flash Next 的权重托管在 Hugging Face 和 Ollama 上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen / Qwen 3 . 8 - Flash - Next · Hugging Face</a></li>
<li><a href="https://ollama.com/frob/qwen3.8-flash-next">frob/ qwen 3 . 8 - flash - next</a></li>
<li><a href="https://symbl.ai/developers/blog/a-guide-to-quantization-in-llms/">A Guide to Quantization in LLMs | Symbl.ai</a></li>

</ul>
</details>

**社区讨论**: 社区情绪分化：一些用户复现了速度声明（4090 上 124 tokens/秒），并称赞 4-bit 量化在范围明确的编码任务上表现良好；另一些人则对低于 4-bit 的量化持怀疑态度，并报告视觉任务准确率明显差于 llama.cpp。一位评论者警告说，各大 LLM 讨论区正被 Strata 链接刷屏，这种热度可能熬不过蜜月期。

**标签**: `#LLM inference`, `#quantization`, `#consumer hardware`, `#Qwen`, `#performance benchmarking`

---

<a id="item-3"></a>
## [浏览器原生的经典 Visual Basic 6 IDE](https://wieslawsoltes.github.io/VB6/) ⭐️ 7.0/10

一位开发者发布了一个完全在浏览器中运行的经典 Visual Basic 6 IDE，托管在 wieslawsoltes.github.io/VB6/。它凭借出色的速度和怀旧价值获得了社区的高度关注（68 分，23 条评论）。 该项目展示了浏览器端工具链的巨大进步，让一个备受喜爱的复古开发环境无需本地安装即可复活。它可能重新激发人们对高效轻量级 IDE 以及保存遗留编程平台的兴趣。 该 IDE 完全在浏览器中运行，很可能借助 WebAssembly 实现高性能，用户反馈其启动速度非常快。但它目前尚不支持 Win32 API 层，因此依赖 BitBlt 等调用的程序无法运行。

hackernews · wiso · Oct 4, 18:49 · [社区讨论](https://news.ycombinator.com/item?id=49956681)

**背景**: Visual Basic 6 是微软于 1998 年发布的流行 IDE，在让位于 .NET 之前被广泛用于构建 Windows 桌面应用。WebAssembly 是一种二进制指令格式，可让高性能代码在现代浏览器中运行，从而使此类 IDE 等复杂应用完全在客户端工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.openreplay.com/unlock-high-performance-with-webassembly/">Unlock high performance with WebAssembly</a></li>
<li><a href="https://www.testmuai.com/learning-hub/webassembly-compatible-browsers/">WebAssembly : Browser Support, Features, Use Cases</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该项目唤起了美好回忆，并对其惊人的启动速度印象深刻，有人指出这应让现代 IDE 开发者感到羞愧。其他人建议增加部分 Win32 API 支持以及将程序发布为 PWA 的能力，还有用户分享说一个使用 BitBlt 的旧 VB6 地图编辑器无法运行。

**标签**: `#Visual Basic`, `#IDE`, `#WebAssembly`, `#Browser`, `#Retro Computing`

---

<a id="item-4"></a>
## [Homa：旨在取代 AI 集群中 TCP 的新型传输协议](https://www.youtube.com/watch?v=eZ8WWZzoaR0) ⭐️ 7.0/10

Hacker News 上的一场讨论聚焦于 Homa——斯坦福大学开发、发表于 USENIX ATC 2021 的接收端驱动传输协议，它被提议用于取代 AI 集群中的 TCP。John Ousterhout 的演讲指出，Homa 能将数据中心工作负载的尾延迟降低一个数量级甚至更多。 随着 AI 训练集群规模扩大，TCP 的字节流抽象和拥塞控制越来越被视为分布式训练中短小突发消息的瓶颈。如果 Homa 或类似协议获得采用，可能重塑数据中心网络栈，并影响 AI 基础设施的构建方式。 Homa 将消息分为立即发送的未调度部分和仅在收到接收方 GRANT 包后才发送的调度部分，但批评者指出它缺乏整个 RPC 的丢失检测和内置加密。该协议面向消息且基于 UDP，并与 Meta 的努力及九家厂商组成的以太网联盟等替代方案竞争。

hackernews · signa11 · Oct 4, 19:42 · [社区讨论](https://news.ycombinator.com/item?id=49957117)

**背景**: TCP 是互联网的主导传输协议，但其设计假设字节流和通用流量，这会给数据中心工作负载增加延迟。Homa 是为现代数据中心从头设计的，那里常见大量短消息和严格的尾延迟要求。它采用接收端驱动的调度来优先处理消息并避免队头阻塞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49957117">Homa: The end of TCP for AI clusters [video] | Hacker News</a></li>
<li><a href="https://ai.engineer/talks/eZ8WWZzoaR0-homa-end-tcp-ai-clusters">Homa: The End of TCP for AI Clusters — John... | AI Engineer</a></li>

</ul>
</details>

**社区讨论**: 评论者大多持批评态度：Veserv 认为 Homa 无法检测整个 RPC 的丢失且缺乏内置加密，而 Animats 指出该协议至少自 2018 年就已存在。其他人讨论了电路交换与分组交换的历史类比，并询问以太网/RoCE 是否已提供链路级流控。

**标签**: `#networking`, `#AI clusters`, `#transport protocol`, `#Homa`, `#TCP`

---

<a id="item-5"></a>
## [Xray-core 隐瞒证书验证绕过漏洞](https://github.com/net4people/bbs/issues/672) ⭐️ 7.0/10

net4people/bbs 的一个 GitHub issue 指出，广泛使用的代理工具 Xray-core 隐瞒了一个证书验证绕过漏洞长达约半年，首个包含该漏洞的版本于 2026 年 1 月 13 日发布。由于旧的非漏洞选项已被移除，用户别无选择，只能迁移到存在漏洞的新选项。 这是一个重大的安全问题，因为 Xray-core 被广泛用于安全与私密通信，而证书验证绕过会破坏用户所依赖的传输层安全。隐瞒行为还引发了人们对项目漏洞披露处理方式的信任担忧，可能影响大量使用该工具进行翻墙和规避审查的用户。 该漏洞存在于 2026 年 1 月 13 日发布的第一个版本中，由于旧选项被移除，用户别无选择只能迁移到存在漏洞的配置。据报道，该问题在被披露前已被隐瞒约半年。

hackernews · timbill · Oct 4, 17:38 · [社区讨论](https://news.ycombinator.com/item?id=49956003)

**背景**: Xray-core 是一款常用于规避网络审查和保护隐私的开源代理工具，它依赖 TLS 证书验证来确保用户连接到合法服务器。证书验证绕过意味着攻击者可以冒充服务器并拦截流量，从而破坏核心安全保证。net4people/bbs 论坛专门跟踪翻墙工具及其安全问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/net4people/bbs/issues/672">Popular proxy software Xray - core covered up a certification ...</a></li>
<li><a href="https://news.ycombinator.com/item?id=49956003">Xray - core concealed a certificate verification bypass vulnerability</a></li>

</ul>
</details>

**社区讨论**: 社区反应批评声较多，有评论者对 Xray-core 的处理方式表示失望，反映出对该项目透明度和可信度的更广泛担忧。

**标签**: `#security`, `#vulnerability`, `#Xray-core`, `#certificate-verification`, `#proxy`

---

<a id="item-6"></a>
## [提前生成元数据使 Rust 构建与检查速度翻倍](https://github.com/PowderworksCode/headstart) ⭐️ 7.0/10

一个名为 headstart 的 GitHub 项目展示了一种技术：在编译流程早期就生成编译器元数据，可使 Rust 的构建和检查速度提升至多两倍。该技术通过 rustc 的 -Zearly-metadata 标志启用，编译器还需要学会在真正的元数据生成后，用它替换掉早期的占位元数据。 如果被主线编译器采纳，这一优化可以显著缩短 Rust 开发者的迭代时间，而编译速度慢一直是 Rust 开发者抱怨的主要痛点之一。它还引发了关于构建系统中缓存策略和泛型实例化的讨论，可能影响 Rust 工具链的演进方向。 该方法依赖提前生成元数据，并在之后替换为真正的元数据，通过 -Zearly-metadata 标志启用。社区成员指出，类似思路此前可能已在更晚的阶段尝试过，同时有人推测不同构建之间泛型实例化存在多少重复。

hackernews · knuckleheads · Oct 4, 06:26 · [社区讨论](https://news.ycombinator.com/item?id=49951218)

**背景**: Rust 的编译器 rustc 会生成元数据文件（lib.rmeta），其中包含符号表以及链接和增量编译所需的其他信息。构建速度长期以来一直是 Rust 生态的关注点，因此出现了增量编译、缓存工具等多种优化努力。该项目探索将元数据生成提前到编译流程的更早阶段，以便下游工作能更早开始。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49951218">Emitting metadata early makes building/checking Rust ... | Hacker News</a></li>
<li><a href="https://rustc-dev-guide.rust-lang.org/backend/libs-and-metadata.html">Libraries and metadata - Rust Compiler Development Guide</a></li>

</ul>
</details>

**社区讨论**: 评论者对这一技术被主线采纳的可能性表示兴奋，有人提到原以为类似做法已在更晚阶段实现。其他人将其与 TypeScript 的 Turborepo 等缓存工具类比，并推测能否避免不同构建间泛型实例化的重复，同时有人分享了关于加速 Rust 编译器的相关讨论链接。

**标签**: `#Rust`, `#compiler-optimization`, `#build-systems`, `#caching`, `#developer-tools`

---

<a id="item-7"></a>
## [何恺明团队 VISTA 让 Claude 在 ARC-AGI-3 拿到满分](https://www.36kr.com/p/4011070893871238) ⭐️ 7.0/10

何恺明团队提出了 VISTA，一种视觉外壳（visual harness），它让通用多模态模型直接以原始视觉观测来感知环境，并以无损方式保存过去的视觉记忆；据报道，这一方法使 Claude（以及 GPT-5.6 Sol 等模型）在公开的 ARC-AGI-3 游戏上取得了 100/100 的满分。 ARC-AGI-3 是一个交互式推理基准，旨在考察智能体的探索能力、即时目标获取能力和世界模型构建能力，因此满分成绩对智能体与推理研究是一个强烈信号；但这也凸显出基准成绩在很大程度上取决于套在模型外面的“外壳”，而不只是模型本身。 VISTA 的核心思路是用直接的视觉观测取代文本化的输入喂给方式，并维护一个无损的视觉记忆，把过去的观测以原始形式保留下来，从而赋予模型长时程视觉能力；不过所提供的报道内容仅有一句话摘要，没有给出论文链接，也没有独立验证。

rss · BALA AI News · Oct 4, 12:31

**背景**: ARC-AGI 是 ARC Prize 推出的一系列基准，用来测试模型在新任务上的抽象推理与泛化能力，而不是记忆已有模式；ARC-AGI-3 进一步把它扩展到交互式环境，智能体必须探索环境、即时推断目标并构建可适应的世界模型。“外壳”（harness）指的是模型外围的脚手架——观测如何呈现、记忆如何保存、动作如何选择——此前的报道显示，同一个模型在 ARC-AGI-3 上的得分会因外壳不同而相差数十分。VISTA 就是这样一个外壳，其重点在于视觉输入与视觉记忆，而非把环境文本化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2610.02200">VISTA : A Visual Harness for Reasoning in an Interactive World</a></li>
<li><a href="https://arcprize.org/arc-agi/3">ARC - AGI - 3</a></li>
<li><a href="https://www.mindstudio.ai/blog/gpt6-astra-benchmarks-agi-claims">GPT-6 Astra Benchmarks : Do the Numbers Actually Mean AGI ?</a></li>

</ul>
</details>

**标签**: `#AI research`, `#ARC-AGI`, `#Claude`, `#visual memory`, `#reasoning benchmarks`

---

