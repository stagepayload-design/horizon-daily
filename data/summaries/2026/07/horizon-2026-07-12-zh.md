# Horizon 每日速递 - 2026-07-12

> From 21 items, 6 important content pieces were selected

---

1. [vLLM v0.25.0：Model Runner V2 成为默认，PagedAttention 被移除](#item-1) ⭐️ 8.0/10
2. [llama.cpp b9963 为 DeepSeek OCR v1 添加多图块动态分辨率支持](#item-2) ⭐️ 7.0/10
3. [GPU 热潮中的循环融资：Nvidia、CoreWeave 与 Nebius](#item-3) ⭐️ 7.0/10
4. [ClickHouse 将 PgBouncer 吞吐量提升 4 倍](#item-4) ⭐️ 7.0/10
5. [在 SQLite 中优先使用严格表](#item-5) ⭐️ 7.0/10
6. [别再让我去问大语言模型了](#item-6) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [vLLM v0.25.0：Model Runner V2 成为默认，PagedAttention 被移除](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 8.0/10

vLLM v0.25.0 将 Model Runner V2 设为所有稠密模型的默认执行路径，移除了旧的 PagedAttention 实现，并引入了新的 Streaming Parser Engine 用于工具调用和推理解析。该版本还新增了对 LLaVA-OneVision-2、GLM-5 和 MiniMax-M3（支持流水线并行）等模型的支持。 此版本标志着 vLLM 架构的重大转变，将推理引擎统一到 Model Runner V2 并移除旧的 PagedAttention，从而简化了代码库并提升了性能。新的 Streaming Parser Engine 和扩展的模型支持使 vLLM 在生产级 LLM 服务中更加通用。 Model Runner V2 现在支持 EVS（高效视觉缩放）、实时嵌入、Mamba 混合模型的前缀缓存，以及带有完整 CUDA 图的动态推测解码。Transformers 建模后端已优化至与原生 vLLM 性能相当，并新增了 FP8 MoE 支持以及 GPTBigCode 和 RoBERTa 的迁移。

github · khluu · Jul 11, 20:06

**背景**: vLLM 是一个开源的高性能大语言模型（LLM）推理引擎，以其高效管理 GPU 内存的 PagedAttention 机制而闻名。Model Runner V2 是一个重新设计的执行路径，旨在提升性能和灵活性，逐步取代旧的 V1 后端。移除 PagedAttention 表明 V1 后端已完全废弃。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm/releases">Releases · vllm -project/ vllm</a></li>
<li><a href="https://vllm.com.cn/blog/mrv2">Model Runner V 2 ： vLLM ... - vLLM 推理引擎</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/paged_attention/">Paged Attention - vLLM</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#release`, `#performance`, `#open source`

---

<a id="item-2"></a>
## [llama.cpp b9963 为 DeepSeek OCR v1 添加多图块动态分辨率支持](https://github.com/ggml-org/llama.cpp/releases/tag/b9963) ⭐️ 7.0/10

llama.cpp 版本 b9963 为 DeepSeek OCR v1 引入了多图块动态分辨率支持，并为 v1 和 v2 提供了统一的图像预处理器，同时包含多项修复和改进。 此次更新显著增强了 llama.cpp 的 OCR 能力，使其能够更准确、灵活地处理复杂文档布局。它使依赖本地开源 LLM 推理进行文档理解任务的用户受益。 多图块动态分辨率功能允许 DeepSeek OCR v1 将图像分割成图块并动态调整每个图块的分辨率。该版本还修复了多行/列图像中的图块丢失问题，并放宽了 v1 单视图测试的容差。

github · github-actions[bot] · Jul 11, 08:38

**背景**: llama.cpp 是一个流行的开源项目，用于在消费级硬件上本地运行大型语言模型 (LLM)。DeepSeek OCR 是一种压缩引导的 OCR 模型，专为文档、表格和复杂布局设计。多图块处理通过将高分辨率图像分解为可管理的块来提高 OCR 准确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-OCR">deepseek -ai/ DeepSeek - OCR · Hugging Face</a></li>
<li><a href="https://github.com/deepseek-ai/DeepSeek-OCR">GitHub - deepseek -ai/ DeepSeek - OCR : Contexts Optical Compression</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#DeepSeek OCR`, `#multi-tile`, `#release`, `#machine learning`

---

<a id="item-3"></a>
## [GPU 热潮中的循环融资：Nvidia、CoreWeave 与 Nebius](https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom) ⭐️ 7.0/10

一项分析揭示了 Nvidia、CoreWeave 和 Nebius 之间的循环融资动态：Nvidia 投资于 GPU 云提供商，而这些提供商又大量采购 Nvidia 硬件，引发了对 AI 基础设施繁荣可持续性的质疑。 这种模式之所以重要，是因为如果 AI 计算需求未能如期实现，可能预示着不可持续的泡沫，进而给投资者和整个科技生态系统带来金融不稳定。 Nvidia 向 CoreWeave 投资 20 亿美元获得 9%股权，而 CoreWeave 计划 2026 年资本支出 350 亿美元，Nvidia 的投资仅覆盖该年支出的 5.7%。剩余资金来自其他渠道，挑战了纯粹循环融资的说法。

hackernews · adletbalzhanov · Jul 11, 17:21 · [社区讨论](https://news.ycombinator.com/item?id=48873836)

**背景**: 循环融资是指一家公司投资于客户，客户再用这些资金购买投资方的产品，从而形成自我强化的循环。在 GPU 热潮中，Nvidia 投资于 CoreWeave 和 Nebius 等“新云”提供商，这些提供商购买 Nvidia GPU 来提供云端 AI 服务。这引发了需求是真实还是被人为夸大的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/nvidia-coreweave-nebius-inside-circular-financing-gpu-beth-kindig-nponc">Nvidia, CoreWeave, and Nebius: Inside the Circular Financing of the...</a></li>
<li><a href="https://factually.co/fact-checks/finance/ai-circular-financing-bubble-c5b370">Is AI's circular financing inflating a bubble?</a></li>
<li><a href="https://heatmap.news/ideas/data-center-bubble">A Backup Plan for the AI Boom - Heatmap News</a></li>

</ul>
</details>

**社区讨论**: 社区评论观点不一：有人认为循环融资被夸大，指出 Nvidia 的投资仅占 CoreWeave 总资本支出的一小部分。另一些人则关注经济可行性，质疑这些建设在代币投资回报率和开源模型竞争下能否盈利。少数人警告，如果 AI 热潮消退，可能形成一触即溃的纸牌屋。

**标签**: `#Nvidia`, `#GPU`, `#financing`, `#cloud computing`, `#AI infrastructure`

---

<a id="item-4"></a>
## [ClickHouse 将 PgBouncer 吞吐量提升 4 倍](https://clickhouse.com/blog/pgbouncer-clickhouse-managed-postgres) ⭐️ 7.0/10

ClickHouse 发布了一篇博客文章，详细介绍了他们如何通过使用 SO_REUSEPORT 套接字选项以及在 PgBouncer 进程之间实现 peering 来高效处理查询取消，从而将 PgBouncer 的吞吐量提升了 4 倍。 这一优化对于依赖 PgBouncer 进行连接池管理的 PostgreSQL 用户意义重大，因为它能够在多进程设置中实现更高的吞吐量和更好的查询取消处理，这对于大规模部署至关重要。 关键技术包括 SO_REUSEPORT（允许多个进程绑定到同一端口以实现负载均衡）和 peering（将取消请求转发到正确的进程）。博客称在他们的测试中吞吐量提升了 4 倍。

hackernews · saisrirampur · Jul 11, 15:28 · [社区讨论](https://news.ycombinator.com/item?id=48872874)

**背景**: PgBouncer 是 PostgreSQL 的轻量级连接池工具，用于减少建立新连接的开销。在多进程设置中，查询取消请求可能落在不拥有该会话的进程上，导致取消失败。SO_REUSEPORT 是一个 Linux 套接字选项，允许多个进程共享同一端口，从而提高可扩展性。Peering 允许 PgBouncer 进程之间通信，将取消请求转发给正确的所有者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pgstef.github.io/talks/en/20250912_PGDayLowlands_PgBouncer-at-scale.pdf">PgBouncer at scale</a></li>
<li><a href="https://github.com/pgbouncer/pgbouncer/blob/master/doc/usage.md">pgbouncer /doc/usage.md at master · pgbouncer / pgbouncer · GitHub</a></li>
<li><a href="https://postgrespro.com/docs/postgrespro/current/pgbouncer">Postgres Pro Standard : Documentation: 18: pgbouncer</a></li>

</ul>
</details>

**社区讨论**: 社区讨论活跃，用户分享了 Odyssey 和 pgdog 等替代方案，并询问 peering 设置的简便性。一些用户指出 Kubernetes 使得运行多个 PgBouncer 进程变得容易，并且对 SO_REUSEPORT 技术表现出兴趣。

**标签**: `#PostgreSQL`, `#PgBouncer`, `#connection pooling`, `#scalability`, `#ClickHouse`

---

<a id="item-5"></a>
## [在 SQLite 中优先使用严格表](https://evanhahn.com/prefer-strict-tables-in-sqlite/) ⭐️ 7.0/10

一篇指南推荐使用 SQLite 的 STRICT 表来强制列类型安全，社区成员讨论了使用 sqlite-utils transform 等迁移工具将非严格表转换为严格表。 这很重要，因为 SQLite 默认的灵活类型可能静默存储错误的数据类型，导致难以发现的错误；采用严格表可以提高使用 SQLite 的应用程序的数据完整性和可靠性。 STRICT 表在 SQLite 3.37.0（2021-11-27）中引入，需要为每个表单独启用；没有 ALTER TABLE 语句可以将现有表变为严格表，需要通过 sqlite-utils 等工具复制数据。

hackernews · ingve · Jul 11, 17:33 · [社区讨论](https://news.ycombinator.com/item?id=48873940)

**背景**: SQLite 传统上使用灵活类型，列类型声明只是提示而非强制约束。这允许将字符串插入 INTEGER 列，可能导致数据损坏。STRICT 表强制执行精确类型匹配，拒绝不匹配的值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sqlite.org/stricttables.html">STRICT Tables</a></li>
<li><a href="https://antonz.org/sqlite-strict-tables/">STRICT tables in SQLite</a></li>
<li><a href="https://sqlite-utils.datasette.io/en/latest/cli.html">sqlite -utils command-line tool - sqlite -utils</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍支持严格表，有些人认为它应该成为默认设置。Simon Willison 分享了一个转换表的工具，而其他人则讨论了 SQLite 的设计哲学，引用了官方 'flextypegood' 文档，该文档解释了为什么严格模式不是默认选项。

**标签**: `#SQLite`, `#database`, `#type safety`, `#software engineering`

---

<a id="item-6"></a>
## [别再让我去问大语言模型了](https://blog.yaelwrites.com/stop-telling-me-to-ask-an-llm/) ⭐️ 7.0/10

作者反对在未承认对方已有研究努力的情况下，习惯性地建议“去问大语言模型”，并指出了技术文化中的沟通鸿沟。 这一讨论对软件工程师和知识工作者意义重大，他们在寻求专家建议时经常遇到敷衍的回应，这可能损害协作和知识共享。 作者强调，他们在向人类提问之前已经咨询过大语言模型，而“去问大语言模型”的建议忽视了他们的努力以及大语言模型在处理细微问题上的局限性。

hackernews · theorchid · Jul 11, 22:28 · [社区讨论](https://news.ycombinator.com/item?id=48876441)

**背景**: 在技术社区中，人们常被引导去使用搜索引擎或大语言模型，而不是直接回答问题。这种做法被称为“LMGTFY”（让我帮你谷歌一下），现已扩展到大语言模型。作者认为，当提问者已经做过功课，这种回应可能显得敷衍。

**社区讨论**: 评论者大多同意作者的观点，指出提供“工作证明”（例如你已经尝试过的方法）可以避免敷衍的回应。一些人认为，在某些情况下大语言模型确实能提供更好的答案，但关键在于清晰沟通已有的努力。

**标签**: `#LLM`, `#communication`, `#tech culture`, `#knowledge work`, `#AI`

---

