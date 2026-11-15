# Horizon 每日速递 - 2026-11-15

> From 62 items, 13 important content pieces were selected

---

1. [SpaceX 在第 15 次飞行中首次成功捕获星舰助推器](#item-1) ⭐️ 9.0/10
2. [Lovable 应用因 Supabase 配置错误泄露护照数据和 20 万条消息](#item-2) ⭐️ 8.0/10
3. [Google Project Zero 将在报告后 90 天披露漏洞](#item-3) ⭐️ 8.0/10
4. [ggml 张量库迎来 v1.0.0 里程碑](#item-4) ⭐️ 8.0/10
5. [PyPI 重新设计的项目页面现已上线，安全信号更清晰](#item-5) ⭐️ 7.0/10
6. [约 200 行纯 JAX 实现 DeepSeek V3 的极简项目](#item-6) ⭐️ 7.0/10
7. [EFF 警告科技公司再次重新定义隐私概念](#item-7) ⭐️ 7.0/10
8. [手机解锁工具技术概述引发取证泄露讨论](#item-8) ⭐️ 7.0/10
9. [单人开发者构建乱序执行 RISC-V 核心，成功启动 Linux 6.6](#item-9) ⭐️ 7.0/10
10. [美国国税局在 GitHub 上开源 Direct File 报税代码](#item-10) ⭐️ 7.0/10
11. [NVIDIA 使用 vLLM 在两台 DGX 工作站上以 607.8 tok/s 服务 GLM-5.3](#item-11) ⭐️ 7.0/10
12. [用 Lean 形式化美国税法以寻找漏洞](#item-12) ⭐️ 7.0/10
13. [llama.cpp 与 ggml 库版本升至 1.0.0，支持超 150 种模型架构](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [SpaceX 在第 15 次飞行中首次成功捕获星舰助推器](https://www.spacex.com/launches/starship-flight-15) ⭐️ 9.0/10

SpaceX 在星舰第 15 次飞行结束时，首次使用发射塔的“筷子”机械臂成功捕获了超重型助推器，同时 Ship 42 上级在成功上升和级间分离后进入了轨道。 这一里程碑表明整个超重型助推器可以被回收和重复使用，这是 SpaceX 实现完全且快速可重复使用的超重型运载火箭目标的关键一步，有望大幅降低进入太空的成本。 此次捕获由发射塔的机械臂完成，该任务标志着星舰的第 15 次试飞，也是星舰 V3 构型的第 4 次飞行；此前部分飞行中助推器未能回收，而飞船热防护罩的性能仍是实现完全可重复使用的关键因素。

hackernews · ls612 · Nov 14, 21:22 · [社区讨论](https://news.ycombinator.com/item?id=50500963)

**背景**: 星舰是有史以来最大、推力最强的火箭，由配备 33 台发动机的超重型助推器和同样称为星舰（或 Ship）的上级航天器组成。与使用固体火箭助推器和侧挂轨道器的航天飞机不同，星舰设计为完全可重复使用，两级均返回发射场。SpaceX 通过试飞快速迭代，而用发射塔捕获助推器是一种避免着陆腿并实现快速重复使用的新颖方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnn.com/2026/11/13/science/live-news/spacex-starship-flight-15-ship-catch">Live updates: SpaceX Starship nails historic ship catch in... | CNN</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_Starship_launches">List of Starship launches - Wikipedia</a></li>
<li><a href="https://www.spacelaunchschedule.com/launch/starship-starlink-group-31-2-starship-flight-15/">SpaceX Starlink Group 31-2 (Starship Flight 15) Starship Rocket Launch</a></li>

</ul>
</details>

**社区讨论**: 评论者庆祝这一成就为历史性里程碑，许多人将星舰与航天飞机进行有利比较，称其为“正确完成的航天飞机”，并强调避免固体助推器和侧挂轨道器是安全性的改进。一些人指出，完全可重复使用取决于热防护罩能否保持完好，而重复使用同一批飞船将是下一个关键步骤，其他人则讨论了工程挑战以及有效载荷进入轨道成本大幅降低的潜力。

**标签**: `#spacex`, `#starship`, `#reusable-rockets`, `#spaceflight`, `#engineering`

---

<a id="item-2"></a>
## [Lovable 应用因 Supabase 配置错误泄露护照数据和 20 万条消息](https://www.crissyfield.de/research/lovable-en/) ⭐️ 8.0/10

Crissy Field 的安全研究人员发现，使用 Lovable 和 Supabase 构建的应用因行级安全（RLS）不足而泄露了护照详细信息和超过 20 万条私人消息。这些发现发表在博客文章中，并在 Hacker News 上引发了讨论，Lovable 的安全负责人也参与其中。 这一事件凸显了 AI 生成应用中的系统性安全风险，非专家用户可以快速部署具有不安全默认配置的应用，可能导致大规模敏感数据泄露。它引发了关于平台责任以及 AI 辅助开发工具中默认安全设置必要性的质疑。 根本原因是 Supabase 中的行级安全不足，这允许在没有适当授权检查的情况下访问数据库行。Lovable 的安全负责人表示，他们在发布前自动扫描每个应用，并提供更深入的 SAST 扫描，两者都是免费的，并提供修复或自动修复发现问题的选项。

hackernews · armcat · Nov 14, 17:43 · [社区讨论](https://news.ycombinator.com/item?id=50499017)

**背景**: Lovable 是一个 AI 驱动的应用构建器，允许用户通过自然语言描述来创建全栈应用。Supabase 是一个开源的 Firebase 替代品，提供带有行级安全的 Postgres 数据库，该功能根据用户角色限制数据访问。当 RLS 配置不当时，敏感数据可能通过 API 调用暴露，而这些调用可以在浏览器中检查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lovable.dev/">App & Website Builder | Build Software in Minutes | Lovable</a></li>
<li><a href="https://www.minimum-code.com/blog/ai-generated-code-vulnerabilities-security">AI Generated Code Vulnerabilities : Security Risks in 2026</a></li>

</ul>
</details>

**社区讨论**: 讨论中包括了 Lovable 安全负责人的发言，他强调了他们的扫描工具，以及博客文章的作者。评论者就 Supabase 的责任进行了辩论，一些人指出 GitHub 上关于默认设置的讨论，另一些人则认为 AI 生成的应用由于数量多且不需要复杂的黑客技术而容易成为目标。大家一致认为需要更好的默认设置，例如默认拒绝的数据库和最小权限 API。

**标签**: `#security`, `#AI-generated code`, `#Supabase`, `#data exposure`, `#vulnerability`

---

<a id="item-3"></a>
## [Google Project Zero 将在报告后 90 天披露漏洞](https://projectzero.google/2026/11/disclosure-policy.html) ⭐️ 8.0/10

Google Project Zero 宣布了一项新的“Full 90”披露政策，立即生效，即在向供应商报告漏洞后 90 天进行披露。该政策将于 2027 年 2 月 2 日缩短至 60 天，并于 2028 年 1 月 3 日缩短至 30 天。 这一政策转变显著缩短了漏洞披露时间线，迫使供应商更快地发布补丁，并可能影响像 Ubuntu 这样依赖上游修复的下游项目。它设定了新的行业规范，可能影响其他安全研究团队和协同披露实践。 从 90 天到 60 天再到 30 天的分阶段缩减为供应商提供了过渡期，但最终的 30 天窗口非常激进，对于复杂漏洞或进展缓慢的开源项目可能具有挑战性。该政策适用于 Project Zero 报告的所有漏洞，无论供应商是谁。

hackernews · hacb · Nov 14, 11:13 · [社区讨论](https://news.ycombinator.com/item?id=50496051)

**背景**: Google Project Zero 是一支安全研究员团队，负责在广泛使用的软件中寻找零日漏洞。协同漏洞披露是指私下向供应商报告漏洞并给予其时间在公开披露前进行修复的实践，通常为 90 天。Project Zero 历史上一直遵循 90 天的披露截止日期，但这项新政策使其更严格且更可预测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wired.com/2014/07/google-project-zero/">Meet ' Project Zero ,' Google 's Secret Team of Bug-Hunting... | WIR...</a></li>
<li><a href="https://www.first.org/global/sigs/vulnerability-coordination/multiparty/guidelines-v1.1">Guidelines and Practices for Multi-Party Vulnerability Coordination ...</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了不同观点：一些人主张立即披露以向供应商施压，而另一些人指出像 Ubuntu 这样的下游项目需要更多时间来修补。一位评论者担心公司可能利用漏洞发现作为杠杆来推广自己的大语言模型。

**标签**: `#vulnerability-disclosure`, `#project-zero`, `#security-policy`, `#google`, `#coordinated-disclosure`

---

<a id="item-4"></a>
## [ggml 张量库迎来 v1.0.0 里程碑](https://github.com/ggml-org/ggml/releases/tag/v1.0.0) ⭐️ 8.0/10

ggml 张量库——llama.cpp 及众多本地 AI 工具的基础——发布了 1.0.0 版本。这是首个主要版本，标志着项目承诺遵循语义化版本控制，未来主要版本号的提升将表示 API 和 ABI 的不兼容变更。 这一里程碑为基于 ggml 的开发者提供了稳定性和可预测性，因为 1.0.0 版本正式确立了版本管理并标志着长期维护。它巩固了 ggml 作为开源本地推理基石的地位，影响着广泛的 AI 应用生态。 该版本包含性能改进和新特性，例如 MoE 内存卸载，当模型略微超出 GPU 内存时，可将不常用的专家缓存到主机内存中。社区基准测试显示每次升级可获得 5-10% 的运行时间改进，并且广泛支持包括 AMD GPU 上的 Vulkan 在内的硬件。

hackernews · cobychapple · Nov 14, 02:28 · [社区讨论](https://news.ycombinator.com/item?id=50493062)

**背景**: ggml 是一个为机器学习设计的 C 语言张量库，旨在在消费级硬件上实现高效推理。它驱动着 llama.cpp——一个在本地运行大型语言模型的流行项目，并使用 GGUF 文件格式存储模型权重。该库以其跨多样硬件的可移植性和性能优化而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/ggml-org/llama-cpp-v1">A Blog post by ggml -org on Hugging Face</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/ llama . cpp : LLM inference in C/C++ · GitHub</a></li>
<li><a href="https://news.ycombinator.com/item?id=50493062">Ggml v 1 . 0 . 0 | Hacker News</a></li>

</ul>
</details>

**社区讨论**: 评论者赞扬了持续的性能提升，有人指出每月升级可获得 5-10% 的速度提升，并举例说明一个 50K token 提示的运行时间从 4:22 提升到 3:59。其他人强调了 ggml 作为“AI 世界的 Linux”的角色，以及通过 Vulkan 在较旧 AMD GPU 上的可用性，同时还提到了新的 MoE 内存卸载功能。

**标签**: `#ggml`, `#llama.cpp`, `#local-inference`, `#AI-infrastructure`, `#open-source`

---

<a id="item-5"></a>
## [PyPI 重新设计的项目页面现已上线，安全信号更清晰](https://blog.pypi.org/posts/2026-11-06-ui-updates-complete/) ⭐️ 7.0/10

PyPI 已完成界面更新，重新设计了项目页面，突出显示来源证明（provenance attestations）和可信发布（trusted publishing）状态等安全信号。新界面让用户更容易查看某个软件包版本是否通过可信发布者发布，以及是否带有可验证的来源证明。 这一变化通过让开发者在安装前更容易评估软件包的可信度，提升了 Python 生态系统的供应链安全。它可能鼓励更多维护者采用可信发布和来源证明，从而提高整个软件包索引的安全基线。 PyPI 使用 in-toto 证明框架，目前接受 SLSA Provenance 谓词，而可信发布依赖 OpenID Connect (OIDC) 与 GitHub Actions 等 CI/CD 提供商交换短期身份令牌。然而，来源证明只能证明软件包是如何构建和发布的，并不能证明软件包本身没有恶意代码。

hackernews · rbanffy · Nov 14, 15:40 · [社区讨论](https://news.ycombinator.com/item?id=50497892)

**背景**: PyPI 是 Python 的官方软件包索引，托管着数十万个项目，开发者通过 pip 安装这些包。来源证明是 PEP 740 提案的一部分，是记录软件包构建方式和位置的加密签名声明，通常使用 Sigstore 的无密钥签名基础设施。可信发布允许维护者直接从 CI/CD 系统发布软件包，而无需存储长期有效的 API 令牌，从而降低令牌被盗的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.pypi.org/attestations/">Introduction - PyPI Docs</a></li>
<li><a href="https://docs.pypi.org/trusted-publishers/">Getting Started - PyPI User Documentation</a></li>
<li><a href="https://github.com/sigstore/cosign">GitHub - sigstore /cosign: Code signing and transparency for...</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍欢迎来源信息可见性的提升，一些人赞赏向 Sigstore 风格无密钥签名的推进。然而，也有人担心集中化以及对大型云 CI 提供商的锁定，请求可信发布支持可复用工作流，并指出来源证明无法检测恶意项目，只能检测原本良性的项目是否被篡改。

**标签**: `#supply-chain-security`, `#PyPI`, `#provenance`, `#sigstore`, `#package-management`

---

<a id="item-6"></a>
## [约 200 行纯 JAX 实现 DeepSeek V3 的极简项目](https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax) ⭐️ 7.0/10

一位开发者发布了用约 200 行纯 JAX 代码从零实现 DeepSeek V3 语言模型的项目，并托管在 GitHub 上。该项目旨在帮助动手学习和本地实验，社区成员已报告通过 ROCm 在 AMD GPU 上成功运行。 这一极简实现降低了理解 DeepSeek V3 这类先进开源大模型内部工作原理的门槛，对学习者和研究者很有价值。社区报告的 ROCm 成功案例还表明 JAX 是在非 NVIDIA 硬件上进行深度学习的可行途径，可能为 AMD GPU 用户拓宽使用渠道。 该实现刻意保持极简，约 200 行代码，优先考虑可读性和从第一性原理理解，而非性能或生产可用性。一位社区成员指出，在 RX 7600 XT 16GB 上运行需要设置环境变量 HSA_OVERRIDE_GFX_VERSION=11.0.0，因为 JAX 的 ROCm 插件默认无法识别该 GPU。

hackernews · VaibhaavTiwari · Nov 14, 15:04 · [社区讨论](https://news.ycombinator.com/item?id=50497589)

**背景**: DeepSeek V3 是一款开源大语言模型，以强劲性能和高效架构著称，也是 DeepSeek R1 背后的基础模型。JAX 是一个用于高性能数值计算的 Python 库，结合了自动微分和 XLA 编译器，为面向加速器的机器学习提供类似 NumPy 的 API。ROCm 是 AMD 面向 GPU 计算的开放软件栈，为 AI 和 HPC 工作负载提供 CUDA 之外的替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/DeepSeek-V3">GitHub - deepseek -ai/ DeepSeek - V 3 · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/JAX_(software)">JAX (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/ROCm">ROCm - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者反应积极，有人称赞从第一性原理重建模型的价值，还有人询问构建 LLM 推理直觉的学习路线图。一个值得注意的实践报告来自一位用户，他在 Fedora 上通过 ROCm 在 RX 7600 XT 16GB 上端到端跑通了本地训练，称这是第一个在其显卡上成功运行的项目，并分享了所需的环境变量变通方法。

**标签**: `#JAX`, `#DeepSeek`, `#LLM inference`, `#ROCm`, `#open-source`

---

<a id="item-7"></a>
## [EFF 警告科技公司再次重新定义隐私概念](https://www.eff.org/deeplinks/2026/11/tech-companies-are-trying-shift-entire-concept-privacy-again) ⭐️ 7.0/10

电子前沿基金会（EFF）发表分析文章，指出科技公司再次试图重新定义隐私概念，这次是在 AI 会议记录器及相关技术的背景下。该文章在 Hacker News 上引发了 451 分、170 条评论的热烈讨论。 这一点很重要，因为科技公司对隐私的重新定义可能会使日常职业和个人场景中的普遍录音和数据收集正常化，从而侵蚀法律保护和个人对信息的控制权。这场辩论影响到所有使用或受制于 AI 工具的人，以及政策制定者和数字权利倡导者。 EFF 的分析强调了 AI 会议记录器（通常以可见或不可见的机器人身份加入通话）如何捕获音频并传输到云服务器进行转录，从而引发同意和监控方面的担忧。社区评论还指出这对失聪和听障用户的无障碍益处，但也提到这类系统“离保留数据只差一个 if 语句”的风险。

hackernews · gslin · Nov 14, 12:45 · [社区讨论](https://news.ycombinator.com/item?id=50496602)

**背景**: 电子前沿基金会（EFF）是一家领先的非营利数字权利组织，成立于 1990 年，旨在捍卫数字世界的公民自由。AI 会议记录器是一种自动加入视频通话、录制音频并生成转录文本的工具，通常将数据存储在云端。隐私倡导者担心，在未获得所有参与者明确同意的情况下广泛采用此类工具，可能会导致持续监控的新常态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Electronic_Frontier_Foundation">Electronic Frontier Foundation - Wikipedia</a></li>
<li><a href="https://modelpiper.com/blog/ai-meeting-recorder-privacy">AI Meeting Recorders and the Consent Problem... — ModelPiper</a></li>

</ul>
</details>

**社区讨论**: 评论者担心 AI 记录器在职业环境中变得不可避免，使得选择退出可能危及就业。其他人强调了这对失聪和听障人士的潜在无障碍益处，同时一些人引用联合国《世界人权宣言》指出任意干涉隐私是基本权利侵犯。少数人建议采取实用措施，如使用一次性身份和气隙隔离，并支持 EFF 等组织。

**标签**: `#privacy`, `#AI-surveillance`, `#EFF`, `#policy`, `#human-rights`

---

<a id="item-8"></a>
## [手机解锁工具技术概述引发取证泄露讨论](https://osservatorionessuno.org/blog/2026/05/demystifying-phone-unlocking-tools-a-technical-overview/) ⭐️ 7.0/10

Osservatorio Nessuno 发布了一份新的技术概述，揭秘手机解锁工具，解释 Cellebrite 和 MSAB 等取证供应商如何从锁定的设备中提取数据。随附的 Hacker News 讨论重点提到了最近泄露的 Cellebrite 和 MSAB 文档，这些文档揭示了这些工具可以解锁哪些手机和操作系统版本。 这份分析帮助隐私倡导者、安全研究人员和普通用户了解商业手机解锁工具的真实能力和局限性，这些工具正越来越多地被执法部门使用。它还强调了锁屏安全的重要性以及取证供应商囤积零日漏洞所带来的风险。 该概述可能详细介绍了暴力破解 PIN 码、利用引导加载程序漏洞以及使用专用硬件等方法，并指出其有效性因设备型号和操作系统版本而异。社区成员还质疑三星的 Knox 平台是否在标准 Android 锁屏行为之外引入了额外的延迟或保护。

hackernews · iloveyoutwo · Nov 14, 14:44 · [社区讨论](https://news.ycombinator.com/item?id=50497416)

**背景**: 手机解锁工具用于移动取证，通过绕过锁屏从智能手机中提取数据以进行调查。Cellebrite 和 MSAB 等公司向执法部门出售这些工具，其能力通常秘而不宣。泄露的文档（如 404 Media 最近报道的那些）为了解哪些设备和软件版本存在漏洞提供了难得的信息。Android 的锁屏是关键的安全屏障，而三星等制造商增加了 Knox 等层来增强保护。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.404media.co/leaked-docs-show-what-phones-cellebrite-can-and-cant-unlock/">Leaked Docs Show What Phones Cellebrite Can (and Can’t) Unlock</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cellebrite">Cellebrite - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者链接了 GrapheneOS 论坛上泄露的 Cellebrite 和 MSAB 文档，提供了取证能力的具体例子。一位用户质疑三星的 Knox 是否影响“锁屏只是 UI”的概念，并指出输入 PIN 后会有延迟。另一位批评情报机构没有帮助修补零日漏洞，认为供应商和政府正在联手对付普通用户。

**标签**: `#mobile-forensics`, `#phone-unlocking`, `#privacy`, `#Cellebrite`, `#Android-security`

---

<a id="item-9"></a>
## [单人开发者构建乱序执行 RISC-V 核心，成功启动 Linux 6.6](https://github.com/FURSOY/fursoy-cpu) ⭐️ 7.0/10

一位独立开发者发布了 Fursoy Slice-1，这是一个用 SystemVerilog 编写的 64 位乱序执行超标量 RISC-V 核心，实现了 RV64IMAFDV 以及 Zba/Zbb/Zicsr/Zifencei 扩展。该核心集成在一个最小 SoC 中，包含 5 主设备交叉开关、CLINT、PLIC、16550 UART 和自定义 SBI v2.0 固件，并能够启动 Linux 6.6.50 与 BusyBox。 对于单人开发者而言，构建一个能运行现代 Linux 内核的功能性乱序执行超标量核心是一项重大的技术成就，表明复杂的 CPU 微架构可以在开源硬件项目中实现。这可能激励更多个人为 RISC-V 和开源处理器设计做出贡献。 该核心具有 2 宽度的取指/解码/重命名/退休流水线、128 项重排序缓冲区、160 项整数物理寄存器堆、8 个分支检查点用于单周期推测性 RAT 回滚，以及独立的整数、内存、浮点和向量发射队列。完整的 Linux 启动收尾大约需要 1.5–2 小时实际时间。

hackernews · fursoy · Nov 14, 14:06 · [社区讨论](https://news.ycombinator.com/item?id=50497137)

**背景**: RISC-V 是一个开放的指令集架构（ISA），允许任何人设计和构建处理器而无需支付许可费。RV64IMAFDV 的命名表示一个 64 位 RISC-V 核心，包含整数、乘除法、原子、单/双精度浮点和向量扩展。乱序执行是一种 CPU 动态重排指令以利用空闲执行单元来提高性能的技术，常见于英特尔和 AMD 等高性能处理器中。SystemVerilog 是一种用于设计数字电路的硬件描述和验证语言。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/FURSOY/fursoy-cpu">FURSOY/fursoy-cpu: 64-bit out-of-order superscalar RISC - V processor...</a></li>
<li><a href="https://riscv.atlassian.net/wiki/spaces/HOME/pages/16154665/Language+Runtimes">Language Runtimes - Home - RISC - V Tech Hub</a></li>

</ul>
</details>

**社区讨论**: 社区反应积极，评论者称该项目“非常酷”，并承认在单人项目中实现乱序设计的难度。一位评论者建议发布到 Reddit 的 r/RISCV 以获得更多关注，另一位询问是否可以通过 tiny tap 或类似服务制作物理副本。

**标签**: `#risc-v`, `#computer-architecture`, `#systemverilog`, `#out-of-order-execution`, `#open-source-hardware`

---

<a id="item-10"></a>
## [美国国税局在 GitHub 上开源 Direct File 报税代码](https://github.com/IRS-Public/direct-file) ⭐️ 7.0/10

美国国税局（IRS）已在 GitHub 上发布了其 Direct File 在线报税系统的开源代码库，使代码可供公众审查和重用。 此次发布标志着政府透明度和公民科技的重要进步，可能使第三方开发者能够构建替代性报税工具，并减少对 TurboTax 等商业软件的依赖。 该代码库包含 Direct File 系统的代码，该系统在 2024 年和 2025 年报税季面向 25 个州的简单申报纳税人开放；然而，IRS 此后已终止该计划，代码可能不再积极维护。

hackernews · accountinhn · Nov 14, 17:48 · [社区讨论](https://news.ycombinator.com/item?id=50499083)

**背景**: Direct File 是 IRS 于 2024 年试点推出的免费在线报税系统，旨在让纳税人直接向该机构提交联邦税表，而无需通过商业软件。它支持简单申报，例如有 W-2 收入和采用标准扣除的纳税人。开源代码使公众能够检查并可能调整政府的实现用于其他用途。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnet.com/tech/services-and-software/irs-ends-free-direct-file-tax-program-best-alternatives/">IRS Ended Its Direct File Tax Program . Here Are the Best... - CNET</a></li>
<li><a href="https://money.usnews.com/money/personal-finance/taxes/articles/how-to-file-taxes-for-free">How to File Taxes for Free | Taxes | U.S. News</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了美国税制的复杂性，一些人指出免费报税服务往往不支持更复杂的表格，而另一些人则称赞那些由税务机关预先计算税款的国家。几位评论者表示有兴趣构建开源或 AI 辅助的报税工具，并质疑为何此类解决方案没有更早出现。

**标签**: `#open-source`, `#government-tech`, `#tax-filing`, `#civic-tech`, `#IRS`

---

<a id="item-11"></a>
## [NVIDIA 使用 vLLM 在两台 DGX 工作站上以 607.8 tok/s 服务 GLM-5.3](https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/) ⭐️ 7.0/10

NVIDIA 发布了一篇开发者博客，详细介绍了如何使用 vLLM 在两台 NVIDIA DGX 工作站上以每秒 607.8 个 token 的速度服务 GLM-5.3 语言模型。该设置展示了大型模型的多节点推理，利用 NVIDIA 的专用 AI 硬件实现了高吞吐量。 这证明了在多节点 DGX 系统上服务 GLM-5.3 等大型模型的可行性，这对于需要高吞吐量推理的企业很重要。然而，DGX 硬件的高成本引发了与替代 GPU 配置相比经济可行性的质疑。 博客报告了 607.8 token/秒的吞吐量，但未披露延迟、批处理大小或成本细节。社区成员指出，使用 8 块 B6000 GPU 的类似设置可以以一半的价格实现约 60% 更高的吞吐量，表明 DGX 可能不是最具成本效益的解决方案。

hackernews · wondersky · Nov 14, 14:09 · [社区讨论](https://news.ycombinator.com/item?id=50497155)

**背景**: vLLM 是一个开源的高吞吐量 LLM 推理和服务引擎，最初由加州大学伯克利分校开发。NVIDIA DGX 工作站是专为 demanding AI 工作负载设计的集成 AI 工作站，配备多个高端 GPU 和高速互连。GLM-5.3 是一个大型语言模型，服务它需要大量的 GPU 内存和计算资源，通常需要多个 GPU 或节点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm">vllm -project/ vllm : A high-throughput and memory-efficient inference ...</a></li>
<li><a href="https://blogs.nvidia.cn/blog/dgx-station-keya-medical/">NVIDIA DGX Station 加速AI... | NVIDIA 英伟达博客</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者质疑其经济性：hkalbasi 估计在最大利用率下投资回报期约为 7 年，且忽略电费，除非需要隐私，否则不合理。jbellis 指出，8 块 B6000 的设置可以以一半的价格提供 60% 更高的吞吐量，并链接到一个 GitHub 实现。其他人询问了网络选项以及高速 RAM 是否被充分利用。

**标签**: `#vLLM`, `#LLM inference`, `#NVIDIA DGX`, `#GLM-5.3`, `#AI infrastructure`

---

<a id="item-12"></a>
## [用 Lean 形式化美国税法以寻找漏洞](https://lexifina.com/blog/formalizing-the-us-tax-code) ⭐️ 7.0/10

Lexifina 的一篇博客文章描述了一项工作：使用 Lean 证明助手对整个美国国内税收法典进行形式化，以检测不一致和歧义，并将漏洞视为 bug。该项目旨在利用 Lean 的类型检查器来验证税收规则是否从法规中逻辑推导出来。 这是形式化验证在一个大规模现实法律系统上的新颖应用，可能揭示税法中隐藏的冲突，并启发其他立法领域的类似工作。它可能带来更透明和一致的法律，影响政策制定者、法律科技开发者和纳税人。 该项目使用 Lean——一种具有依赖类型系统的编程语言和证明助手——来编码税收法规。社区讨论强调了一个具体发现：“大美丽法案”可能在大多数州对高收入夫妇造成高达 1.5 万美元的婚姻惩罚，并指出漏洞往往是有意为之，从而对该项目的前提提出了质疑。

hackernews · dnw · Nov 14, 15:41 · [社区讨论](https://news.ycombinator.com/item?id=50497900)

**背景**: Lean 是一个交互式定理证明器和编程语言，允许数学家形式化证明并用类型检查器进行验证。形式化验证已用于软件和硬件以证明正确性，但将其应用于法律法典却很罕见。美国国内税收法典是一套管理税收的复杂法律，其中的歧义或不一致可能导致意外的漏洞或争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lexifina.com/blog/formalizing-the-us-tax-code">Formalizing the US tax code | Lexifina</a></li>
<li><a href="https://arxiv.org/pdf/2103.03198">Catala : A Programming Language for the Law</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了法律中不一致的不可避免性，一些人分享了在法律分析公司的工作经验。其他人提到了 Catala——一种由法国政府使用的法律形式化领域特定语言，并争论将漏洞标记为 bug 是否是一种政治声明，指出许多漏洞是有意为之的。

**标签**: `#formal-verification`, `#Lean`, `#tax-code`, `#legal-tech`, `#programming-languages`

---

<a id="item-13"></a>
## [llama.cpp 与 ggml 库版本升至 1.0.0，支持超 150 种模型架构](https://www.ithome.com/0/1027/019.htm) ⭐️ 7.0/10

llama.cpp 和 ggml 库均已升级至 1.0.0 版本，这是它们的首个主要稳定版发布。此次更新带来了对超过 150 种模型架构的支持，大幅扩展了可在本地运行的模型范围。 这一里程碑表明 llama.cpp 和 ggml 已经足够成熟，可用于生产环境，这可能会促进开发者在构建本地大语言模型应用时的采用。广泛的架构支持使得无需切换工具即可轻松运行多种模型。 来源未提供发布说明或技术细节，因此性能改进或重大变更等具体情况尚不清楚。150 多种架构可能包括 Llama、Mistral 等流行系列，但确切列表尚未确认。

rss · BALA AI News · Nov 14, 03:31

**背景**: llama.cpp 是一个开源项目，它使用 ggml 张量库作为计算后端，能够在消费级硬件上以最少的配置本地运行大语言模型。ggml 是一个为在通用硬件上高效进行机器学习而设计的 C/C++ 张量库，它也支持 whisper.cpp 等其他项目。达到 1.0.0 版本通常意味着 API 稳定性以及为更广泛采用做好了准备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ggml-org/ggml">GitHub - ggml -org/ ggml : Tensor library for machine learning · GitHub</a></li>
<li><a href="https://ggml.ai/">ggml .ai</a></li>
<li><a href="https://llama.app/docs/introduction">Introduction — llama .app</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#ggml`, `#LLM inference`, `#open-source`, `#model architectures`

---

