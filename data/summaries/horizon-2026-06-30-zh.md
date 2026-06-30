# Horizon 每日速递 - 2026-06-30

> From 45 items, 14 important content pieces were selected

---

1. [llama.cpp b9840 版本新增 DeepSeek V4 支持](#item-1) ⭐️ 9.0/10
2. [最高法院裁定地理围栏搜查令需遵循宪法保护](#item-2) ⭐️ 9.0/10
3. [vLLM v0.24.0 新增 MiniMax-M3 支持与 DeepSeek-V4 优化](#item-3) ⭐️ 8.0/10
4. [火箭实验室收购铱星公司达成历史性交易](#item-4) ⭐️ 8.0/10
5. [WATaBoy 将 Game Boy 指令 JIT 编译为 WASM，性能超越原生解释器](#item-5) ⭐️ 8.0/10
6. [深度解析：CUDA 内核从 CPU 到 GPU 的启动路径](#item-6) ⭐️ 8.0/10
7. [OpenSfM v1.0 以 GPU 加速重振无人维护的 SfM 工具](#item-7) ⭐️ 8.0/10
8. [Ornith-1.0：开源编程大模型发布](#item-8) ⭐️ 8.0/10
9. [open-webui v0.10.0：文件夹共享与上下文压缩](#item-9) ⭐️ 7.0/10
10. [Qwen 3.6 27B：本地开发的甜蜜点？](#item-10) ⭐️ 7.0/10
11. [桑迪亚国家实验室 SA3000：抗辐射 8085 处理器](#item-11) ⭐️ 7.0/10
12. [欧洲 ISP 要求版权方为过度屏蔽承担责任](#item-12) ⭐️ 7.0/10
13. [CISA 将 SimpleHelp 认证绕过漏洞加入 KEV 目录](#item-13) ⭐️ 7.0/10
14. [OpenAI 报告绘制 AI 对欧盟就业影响图谱](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [llama.cpp b9840 版本新增 DeepSeek V4 支持](https://github.com/ggml-org/llama.cpp/releases/tag/b9840) ⭐️ 9.0/10

llama.cpp 的 b9840 版本新增了对 DeepSeek V4 架构的支持，包括模型转换、图输入、状态保存和 flash attention。 此次更新使广泛使用的 llama.cpp 推理引擎能够运行 DeepSeek V4（一个 1 万亿参数的 MoE 模型），使其可在本地硬件上运行，并扩展了开放权重模型的生态系统。 该版本包含 DeepSeek V4 的转换脚本，支持基础版和 Pro 版模型，启用了 flash attention 以加速推理，并实现了图复用以提高效率。它还确保与社区现有的 GGUF 文件兼容。

github · github-actions[bot] · Jun 29, 10:25

**背景**: llama.cpp 是一个开源 C++ 库，用于在消费级硬件上本地运行大型语言模型，使用 GGUF 格式存储量化模型。DeepSeek V4 是一个混合专家模型，总参数量 1 万亿，激活参数 320 亿，采用 Engram 记忆架构和动态稀疏注意力。Flash attention 是一种优化的注意力机制，可减少内存使用并加速推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepseek.ai/deepseek-v4">DeepSeek V 4 (2026) — 1T Params, Benchmarks & Pricing</a></li>
<li><a href="https://spoonai.me/posts/2026-03-19-deepseek-v4-open-weight-en">DeepSeek V 4 — 1 Trillion Parameters, Open-Weight, and... | spoonai</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#DeepSeek V4`, `#machine learning`, `#open source`, `#release`

---

<a id="item-2"></a>
## [最高法院裁定地理围栏搜查令需遵循宪法保护](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

美国最高法院裁定，要求科技公司提供虚拟边界内所有设备位置数据的地理围栏搜查令，必须遵循第四修正案保护并具备可能原因。该裁决限制了执法部门未经授权获取批量位置数据的行为。 这项里程碑式的裁决要求执法部门在获取地理围栏数据前必须基于可能原因获得搜查令，从而显著加强了数字隐私权。它为其他形式的批量数据收集树立了先例，影响数百万智能手机用户和谷歌等科技公司。 该案涉及一起银行抢劫案，谷歌提供了银行周围 150 米内 19 个账户的位置数据。法院裁定，政府获取此类数据构成第四修正案下的搜查，需要基于可能原因获得搜查令。

hackernews · cdrnsf · Jun 29, 15:54 · [社区讨论](https://news.ycombinator.com/item?id=48720924)

**背景**: 地理围栏搜查令（又称反向位置搜查令）允许警方要求科技公司提供特定地理区域和时间段内所有设备的位置数据。第四修正案保护公民免受不合理搜查和扣押，但其对数字数据的适用自 2018 年 Carpenter 诉美国案以来一直在演变。

**社区讨论**: 评论者对裁决表示强烈支持，一些人指出其对 Flock 车牌识别器等监控技术的影响。一位用户用酒店住客名单识别无手机人员的案例进行历史类比，凸显了更广泛的隐私担忧。其他人批评持异议的 Alito 和 Thomas 大法官反对该裁决。

**标签**: `#privacy`, `#supreme court`, `#geofence warrants`, `#fourth amendment`, `#digital rights`

---

<a id="item-3"></a>
## [vLLM v0.24.0 新增 MiniMax-M3 支持与 DeepSeek-V4 优化](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 8.0/10

vLLM v0.24.0 由 256 位贡献者提交了 571 次提交，新增了对 MiniMax-M3 模型的支持，并对 DeepSeek-V4 进行了重大优化，包括 FlashInfer 稀疏索引缓存和预填充分块规划改进。 此版本显著扩展了 vLLM 的模型覆盖范围和推理性能，通过支持高效部署 MiniMax-M3 和 DeepSeek-V4 等前沿模型，惠及开源大语言模型生态系统。 MiniMax-M3 支持包括通过 MSA 实现的 BF16/FP8 索引器、MXFP4 和 FP8 稀疏 GQA，而 DeepSeek-V4 获得了 FlashInfer 稀疏索引缓存（TTFT 提升 2–4%）和预填充分块规划优化带来的 4% 端到端吞吐量提升。

github · khluu · Jun 29, 19:41

**背景**: vLLM 是一个高性能的开源大语言模型推理和服务库，以其高效的内存管理和快速解码而广泛使用。MiniMax-M3 是一个前沿的开源权重模型，具有 1M 上下文窗口和原生多模态理解能力，而 DeepSeek-V4 是一个需要高级优化才能在生产环境中部署的大型语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/models/text/m3">MiniMax M 3 - Coding & Agentic Frontier, 1M Context, Multimodal</a></li>
<li><a href="https://docs.flashinfer.ai/api/sparse.html">flashinfer . sparse - FlashInfer 0.6.13 documentation</a></li>
<li><a href="https://rocm.blogs.amd.com/artificial-intelligence/w4a6-quant-mm/README.html">MXFP6 and MXFP 4 Mixed Precision for Accelerating... — ROCm Blogs</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#open-source`, `#performance optimization`, `#model support`

---

<a id="item-4"></a>
## [火箭实验室收购铱星公司达成历史性交易](https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-acquire-iridium-historic-deal-creating-fully) ⭐️ 8.0/10

火箭实验室宣布收购铱星通信公司，这是一项历史性交易，将打造一家完全整合的太空公司，确保基础发射任务并增加卫星制造能力。 此次收购使火箭实验室能够效仿 SpaceX 的策略，利用卫星星座保证稳定的发射节奏，同时获得铱星公司成熟的卫星网络和制造专长。 铱星公司运营着由 66 颗活跃低地球轨道卫星和 9 颗在轨备用卫星组成的星座，而火箭实验室目前的电子号火箭无法到达铱星的轨道，不过其即将推出的中子号火箭可能具备此能力。

hackernews · everfrustrated · Jun 29, 14:09 · [社区讨论](https://news.ycombinator.com/item?id=48719485)

**背景**: 火箭实验室是一家端到端的太空公司，提供发射服务、卫星制造和在轨管理。铱星是一家卫星通信公司，以其全球低地球轨道星座闻名，为地球任何地方提供语音和数据覆盖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Iridium_satellite_constellation">Iridium satellite constellation - Wikipedia</a></li>
<li><a href="https://rocketlabcorp.com/">Rocket Lab | The Space Company | Rocket Lab</a></li>
<li><a href="https://www.space.com/rocket-lab.html">Rocket Lab : Private Spaceflight for Tiny Satellites | Space</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调了与 SpaceX 星链策略的相似之处，一些人表达了对太空垃圾和卫星发射增加对环境影响的担忧。其他人则质疑技术适配性，指出电子号火箭目前无法到达铱星的轨道。

**标签**: `#space industry`, `#acquisition`, `#Rocket Lab`, `#Iridium`, `#satellites`

---

<a id="item-5"></a>
## [WATaBoy 将 Game Boy 指令 JIT 编译为 WASM，性能超越原生解释器](https://humphri.es/blog/WATaBoy/) ⭐️ 8.0/10

一个名为 WATaBoy 的学生项目展示了一款 Game Boy 模拟器，它使用即时（JIT）编译技术在运行时将 SM83 指令翻译为 WebAssembly，其性能超越了原生解释器。 该方法巧妙地利用浏览器内置的 WASM JIT 编译器绕过了 iOS 的 JIT 限制，可能使得在禁止原生 JIT 的平台上实现高性能模拟成为可能，并且挑战了 WASM 开销使其不适合模拟的假设。 该模拟器在 Web 浏览器中运行，利用浏览器的 WebAssembly 引擎将 Game Boy 指令 JIT 编译为原生代码，执行速度比用 C 或 Rust 编写的传统解释器更快。在此场景下，Firefox 比 Chrome 和 Safari 慢约 25%。

hackernews · energeticbark · Jun 29, 15:02 · [社区讨论](https://news.ycombinator.com/item?id=48720190)

**背景**: JIT 编译在运行时动态翻译代码以提升性能，但苹果出于安全原因在 iOS 上限制原生 JIT。然而，Web 浏览器被允许对 JavaScript 和 WebAssembly 使用 JIT。WATaBoy 利用这一漏洞，将模拟的指令编译为 WASM，然后由浏览器 JIT 编译为原生代码，从而有效绕过了限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://asktechnicians.com/the-browser-loophole-that-could-sneak-emulators-onto-iphone">JIT -to-Wasm: The Browser Loophole for iPhone Emulators · Ask...</a></li>
<li><a href="https://github.com/EnergeticBark/WATaBoy">GitHub - EnergeticBark/ WATaBoy : A Game Boy emulator with an...</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该项目作为本科生作品令人印象深刻，并指出 WASM 开销（约 20%）远小于解释器开销（约 1000%），解释了性能优势。一些人讨论了其他 JIT 技术（如 JavaScript eval()）以及 NES 代码静态重编译的挑战，凸显了基于 JIT 的模拟的广泛兴趣。

**标签**: `#JIT compilation`, `#WebAssembly`, `#emulation`, `#Game Boy`, `#performance`

---

<a id="item-6"></a>
## [深度解析：CUDA 内核从 CPU 到 GPU 的启动路径](https://fergusfinn.com/blog/what-happens-when-you-run-a-gpu-kernel/) ⭐️ 8.0/10

Fergus Finn 发表了一篇博客文章，详细介绍了从 CUDA 内核启动到 GPU 执行的完整路径，涵盖了驱动程序交互、通过 GPU 门铃机制提交命令，以及使用 GPU 的 GigaThread 引擎进行硬件调度。 这一解释弥合了高级 CUDA 编程与底层硬件执行之间的鸿沟，帮助开发者理解简单内核启动背后的性能影响和复杂性。 文章描述了 CUDA 运行时如何与 NVIDIA 驱动程序通信，分配内存，将命令推送到环形缓冲区，并通过门铃寄存器通知 GPU，GPU 随后通过 GigaThread 引擎获取并执行内核。

hackernews · mezark · Jun 29, 13:11 · [社区讨论](https://news.ycombinator.com/item?id=48718863)

**背景**: CUDA 是 NVIDIA 的并行计算平台，允许开发者在 GPU 上运行代码。启动 CUDA 内核不仅涉及 GPU 硬件，还涉及 CPU、驱动程序和运行时软件层。理解这一路径对于优化 GPU 工作负载和调试性能问题至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/news/MTIxOTQ">Handling Command Submission For The Intel DRM Driver - Phoronix</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该文章清晰明了，尤其是对门铃和队列管理描述符（QMD）的解释。有人指出 NVIDIA 的开源 GPU 文档提供了更多底层细节，还有人讨论了开源内核优化工具挑战专有解决方案的潜力。

**标签**: `#CUDA`, `#GPU programming`, `#systems programming`, `#NVIDIA`

---

<a id="item-7"></a>
## [OpenSfM v1.0 以 GPU 加速重振无人维护的 SfM 工具](https://github.com/OpenSfM/OpenSfM) ⭐️ 8.0/10

OpenSfM v1.0 作为重大更新发布，引入了 C++ SfM 循环、GPU 加速的 OpenCL 匹配、基于 PatchMatch 和 TSDF-on-SVO 的全新密集重建管线，以及包括 GeoTIFF DSM/正射影像和 LAS/LAZ 点云在内的 GIS 导出功能。 此次发布重振了 OpenDroneMap 和 WebODM 所使用的关键开源运动恢复结构引擎，提供了显著的性能提升和从原始照片到 GIS 成果的完整管线，惠及摄影测量、无人机测绘和 GIS 社区。 新的密集重建管线使用 GPU 加速的 PatchMatch 进行深度估计，并使用 TSDF-on-SVO 进行体素融合，生成干净的点云，但网格输出目前质量较差且正在开发中。该软件支持 Linux 和 macOS，Windows 支持需等待 conda-lock 更新。

rss · Hacker News Show HN · Jun 29, 22:32

**背景**: 运动恢复结构（SfM）是一种从重叠的二维图像重建三维结构的摄影测量技术。OpenSfM 最初由 Mapillary 开发，作为 OpenDroneMap 和 WebODM 的 SfM 引擎，但已有一段时间无人维护。此次 v1.0 版本由前维护者发布，通过 OpenCL 引入现代 GPU 计算，使其重回活跃开发状态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.academia.edu/56386521/Structure_from_Motion_a_high_resolution_low_cost_photogrammetric_tool_for_geoscience_applications">(PDF) Structure - from - Motion ': a high resolution, low-cost...</a></li>
<li><a href="https://developer.nvidia.com/opencl">Open Computing Language OpenCL | NVIDIA Developer</a></li>

</ul>
</details>

**标签**: `#Structure-from-Motion`, `#Photogrammetry`, `#Open Source`, `#GIS`, `#GPU Computing`

---

<a id="item-8"></a>
## [Ornith-1.0：开源编程大模型发布](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce 发布了 Ornith-1.0，这是一个用于智能体编程的开源权重大模型系列，参数规模从 9B 到 397B 不等，基于 Gemma 4 和 Qwen 3.5 构建，在编程基准测试中取得了最先进的结果。 此次发布提供了一个高性能、采用宽松 MIT 许可的编程模型，可在本地运行，使开发者能够构建智能体编程工具，而无需依赖专有 API。 该模型采用自脚手架训练框架来解决奖励作弊问题，35B MoE 变体以 20GB GGUF 文件形式提供，可通过 LM Studio 进行本地推理。

rss · Simon Willison · Jun 29, 16:17

**背景**: 智能体编程指的是大模型能够通过多次工具调用自主编写、调试和执行代码。自脚手架是一种让模型生成自身推理结构以提升性能的技术。Gemma 4 和 Qwen 3.5 是基于 Apache 2.0 许可的开源权重基础模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deep-reinforce.com/ornith_1_0.html">Ornith-1.0: Self - Scaffolding LLMs for Agentic Coding</a></li>
<li><a href="https://news.ycombinator.com/item?id=48709744">Ornith-1.0: Self - Scaffolding LLMs for Agentic Coding | Hacker News</a></li>
<li><a href="https://modernorange.io/item/48675882">Ornith-1.0: Self - Scaffolding LLMs for Agentic Coding | Modern Orange</a></li>

</ul>
</details>

**社区讨论**: Hacker News 和 Simon Willison 博客上的早期用户反馈积极，该模型能够处理复杂的智能体任务，如浏览代码库和绘制图像。一些用户注意到关于 DeepReinforce 公司的信息较少。

**标签**: `#LLM`, `#open-source`, `#coding`, `#agentic`, `#model release`

---

<a id="item-9"></a>
## [open-webui v0.10.0：文件夹共享与上下文压缩](https://github.com/open-webui/open-webui/releases/tag/v0.10.0) ⭐️ 7.0/10

open-webui v0.10.0 引入了团队文件夹共享（支持细粒度的读写权限）、长对话的自动上下文压缩，以及对 Open WebUI Computer 代理的支持。此外，还包含大型知识库的更快混合搜索、外部知识库连接以及重构的内存系统。 此版本显著增强了多用户环境下的协作能力，使 open-webui 更适合团队工作流程。上下文压缩和内存改进也解决了长时间 AI 对话中的关键限制，提升了用户体验。 文件夹共享默认关闭，需要管理员通过新的“文件夹共享”权限启用。上下文压缩通过摘要使对话保持在模型上下文窗口内，可为每个模型配置阈值。混合搜索优化仅适用于 pgvector 设置。

github · github-actions[bot] · Jun 29, 19:17

**背景**: open-webui 是一个开源、自托管的 Web 界面，用于与大型语言模型（LLM）交互。它支持多种后端，如 Ollama 和兼容 OpenAI 的 API，在希望获得可定制、注重隐私的聊天界面的用户中很受欢迎。文件夹共享允许用户与特定用户或群组共享聊天文件夹，从而实现团队协作。

**标签**: `#open-webui`, `#collaboration`, `#release`, `#team`, `#permissions`

---

<a id="item-10"></a>
## [Qwen 3.6 27B：本地开发的甜蜜点？](https://quesma.com/blog/qwen-36-is-awesome/) ⭐️ 7.0/10

这一讨论很重要，因为它突出了本地 LLM 部署与云端替代方案之间的权衡，影响开发者在硬件投资和工作流程效率上的决策。 在 128GB MacBook Pro 上运行 Qwen 3.6 27B 成本为 6,699 美元，而通过 OpenRouter 使用云积分则便宜得多。社区成员指出，零样本演示并不能反映在现有代码库上进行现实编码的情况。

hackernews · stared · Jun 29, 17:05 · [社区讨论](https://news.ycombinator.com/item?id=48721903)

**背景**: 本地 LLM 部署允许开发者在自己的硬件上运行模型，以保护隐私和离线使用，但需要大量 RAM 和 GPU 算力。Qwen 3.6 27B 是一个 270 亿参数的模型，在性能和资源需求之间取得平衡。

**社区讨论**: 社区评论表达了复杂的情绪：一些人称赞模型的能力，但警告硬件噪音和成本；另一些人则认为云 API 更经济，且零样本演示不能代表真实的编码任务。

**标签**: `#LLM`, `#local development`, `#hardware`, `#Qwen`, `#AI coding`

---

<a id="item-11"></a>
## [桑迪亚国家实验室 SA3000：抗辐射 8085 处理器](https://www.cpushack.com/2026/06/03/sandia-national-labs-sa3000-8085-cpu/) ⭐️ 7.0/10

CPU Shack 上的一篇文章详细介绍了桑迪亚国家实验室的 SA3000，这是英特尔 8085 CPU 的抗辐射版本，于 1970 年代末至 1980 年代初开发。 这凸显了政府实验室内部制造抗辐射芯片的历史重要性，这种能力如今已罕见，与当前依赖承包商的做法形成对比。 SA3000 能承受 1×10^6 rad 的辐射，性能仅下降 25%；承受 3×10^6 rad 时性能下降 40%，采用了外延衬底和保护环等技术。

hackernews · rbanffy · Jun 29, 10:20 · [社区讨论](https://news.ycombinator.com/item?id=48717287)

**背景**: 英特尔 8085 是 1977 年推出的 8 位微处理器。抗辐射 CPU 对于航空航天和国防应用至关重要，因为电子设备必须在高辐射环境中生存。桑迪亚国家实验室为此类特殊需求建立了自己的 IC 设计和制造能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48717287">Sandia National Labs SA 3000 8085 CPU | Hacker News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Intel_8085">Intel 8085 - Wikipedia</a></li>
<li><a href="https://www.cpu-world.com/CPUs/8085/index.html">Intel 8085 microprocessor family</a></li>

</ul>
</details>

**社区讨论**: 评论者提到了现代抗辐射 CPU，如 MOOG BRE440 和 BAE RAD5500，它们都采用 IBM POWER 架构。一些人赞扬政府内部的技术能力，另一些人则调侃核武器系统的计算能力。少数人批评了文章科学记数法的格式。

**标签**: `#radiation-hardened`, `#CPU`, `#Sandia National Labs`, `#8085`, `#historical computing`

---

<a id="item-12"></a>
## [欧洲 ISP 要求版权方为过度屏蔽承担责任](https://torrentfreak.com/european-isps-want-rightsholders-held-accountable-for-overblocking-damage/) ⭐️ 7.0/10

欧洲互联网服务提供商（ISP）正在推动让版权方对因过度屏蔽合法内容所造成的损害承担法律责任，此举可能改变版权执法的权力平衡。 这可能会阻止版权方发出过于宽泛的下架请求，减少网络审查并保护在线言论自由。同时，这也为欧盟的 ISP 责任改革树立了先例。 该提议正值欧盟《数字服务法》的持续辩论中，并与美国对 DMCA 滥用的担忧相呼应。ISP 认为，版权方目前不会因过度屏蔽而受到惩罚，导致大量合法内容被审查。

hackernews · Brajeshwar · Jun 29, 16:07 · [社区讨论](https://news.ycombinator.com/item?id=48721072)

**背景**: 过度屏蔽是指因过于激进的版权执法而导致合法内容被移除或限制。在欧盟，版权方可以要求 ISP 屏蔽侵权材料，但这些请求往往也会导致合法内容被屏蔽。《数字服务法》旨在更新在线平台的责任规则。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.euractiv.com/news/dsa-rightsholders-make-final-push-for-takedown-obligations-on-search-engines/">DSA: rightsholders make final push for takedown... | Euractiv</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍支持这一举措，并提到西班牙西甲联赛在比赛期间干扰互联网的滥用行为。一些人对其执行表示怀疑，指出版权垄断者往往能逃避责任。另一些人则将时机与 AI 训练公司寻求更便捷数据访问联系起来。

**标签**: `#copyright`, `#internet governance`, `#ISP`, `#censorship`, `#EU policy`

---

<a id="item-13"></a>
## [CISA 将 SimpleHelp 认证绕过漏洞加入 KEV 目录](https://www.cisa.gov/news-events/alerts/2026/06/29/cisa-adds-one-known-exploited-vulnerability-catalog) ⭐️ 7.0/10

此次添加表明该漏洞正在被积极利用，需要紧急修补，特别是受 BOD 26-04 约束的联邦机构。使用 SimpleHelp 进行远程支持的组织应优先修复，以防止未经授权的访问。 该漏洞影响使用 OpenID Connect (OIDC) 认证的 SimpleHelp 部署。CISA 的 KEV 目录要求在添加 CVE 之前提供活跃利用证据和明确的缓解指南。

rss · CISA Cybersecurity Advisories · Jun 29, 12:00

**背景**: CISA 的已知被利用漏洞（KEV）目录跟踪已确认在野外被积极利用的漏洞。约束性操作指令（BOD）26-04 要求联邦民事行政部门（FCEB）机构优先修复 KEV 目录中列出的、存在于公开暴露资产上的漏洞。SimpleHelp 是一种自托管的远程支持和监控软件，被 IT 团队和 MSP 使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://horizon3.ai/attack-research/disclosures/cve-2026-48558-simplehelp-authentication-bypass-iocs/">CVE-2026-48558: SimpleHelp Auth Bypass IOCs | Horizon3.ai</a></li>
<li><a href="https://linuxsecurity.com/news/security-vulnerabilities/simplehelp-authentication-bypass-vulnerability">SimpleHelp OIDC Important Remote Access Risk CVE-2026-48558</a></li>

</ul>
</details>

**标签**: `#CISA`, `#vulnerability`, `#exploitation`, `#security`, `#CVE`

---

<a id="item-14"></a>
## [OpenAI 报告绘制 AI 对欧盟就业影响图谱](https://openai.com/index/mapping-ai-jobs-transition-eu) ⭐️ 7.0/10

OpenAI 发布了一份报告，分析了 AI 如何自动化、增强或改变欧盟各职业，提供了数据驱动的劳动力机会与风险图谱。 该报告为规划 AI 驱动的劳动力转型的政策制定者和企业提供了关键见解，指出了可能面临颠覆或增长的行业。 该报告按自动化、增强或转型的潜力对职业进行分类，但摘要中未详细说明具体数字或方法。

rss · OpenAI Blog · Jun 29, 07:00

**背景**: 像大型语言模型这样的 AI 技术越来越能够执行以前由人类完成的任务。了解哪些工作最受 AI 影响对于劳动力再培训和政策制定至关重要。该报告通过聚焦欧盟背景，为这一理解做出了贡献。

**标签**: `#AI`, `#workforce`, `#Europe`, `#automation`, `#policy`

---

