---
layout: default
title: "Horizon Summary: 2026-08-23 (ZH)"
date: 2026-08-23
lang: zh
---

> From 51 items, 12 important content pieces were selected

---

1. [MCP 路线图：将远程服务器标准化为 HTTP 工作负载](#item-1) ⭐️ 8.0/10
2. [林纳斯·托瓦兹称赞 AI 在 Linux 内核调试中的帮助](#item-2) ⭐️ 8.0/10
3. [llama.cpp b10584 修复草稿上下文大小以提升服务器稳定性](#item-3) ⭐️ 7.0/10
4. [为什么本地 LLM 看起来比实际更笨](#item-4) ⭐️ 7.0/10
5. [苹果在 macOS 27 Golden Gate 中弃用 hdiutil](#item-5) ⭐️ 7.0/10
6. [Munder Difflin：本地运行一个 AI 克隆办公室](#item-6) ⭐️ 7.0/10
7. [工具让你忘记屏幕使用时间密码以遏制冲动覆盖](#item-7) ⭐️ 7.0/10
8. [浏览器工具为 JPEG 添加增益映射，实现 HDR 标志亮度](#item-8) ⭐️ 7.0/10
9. [llm 0.33：升级 OpenAI 库并新增嵌入键支持](#item-9) ⭐️ 7.0/10
10. [编码代理：验证不止于逐行审查](#item-10) ⭐️ 7.0/10
11. [AI 中的模拟：性能降低 10%，成本降低 100 倍，速度提升 10000 倍](#item-11) ⭐️ 7.0/10
12. [AI 模型吸收“缰绳”，焦点转向人类注意力](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [MCP 路线图：将远程服务器标准化为 HTTP 工作负载](https://blog.modelcontextprotocol.io/posts/mcp-roadmap/) ⭐️ 8.0/10

MCP 路线图宣布计划将远程服务器标准化为 HTTP 工作负载，并改进代理授权，以回应此前的批评。其中包括 2026 年 7 月 28 日 HTTP 标准化的发布日期。 这一转变意义重大，因为它使 MCP 与标准 Web 技术保持一致，可能增加采用率并减少开发者的摩擦。改进的代理授权对于越来越多在云环境中运行的 AI 代理至关重要，确保安全且可扩展的集成。 路线图特别解决了标准化代理身份识别的需求，超越了基于浏览器的授权，以支持云工作负载和委派子代理。2026 年 7 月 28 日的发布标志着一个关键里程碑，届时远程 MCP 服务器将与其他 HTTP 工作负载无异。

hackernews · pentagrama · Aug 22, 13:31 · [社区讨论](https://news.ycombinator.com/item?id=49399591)

**背景**: MCP（模型上下文协议）是一个开放协议，标准化了 AI 应用程序访问外部工具和数据的方式。最初，它为远程服务器引入了定制协议，因非标准和复杂而受到批评。路线图旨在通过采用广泛使用的 HTTP 标准来简化这一点，并增强基于代理的交互的安全性。

**社区讨论**: 社区情绪复杂：一些人称赞转向 HTTP 是对最初失误的纠正，而另一些人则对实现复杂性以及是否真正简化了代理交互持怀疑态度。担忧包括 MCP 相比简单 REST 端点的开销，以及实现所有新功能的负担。

**标签**: `#MCP`, `#AI`, `#protocol`, `#agents`, `#roadmap`

---

<a id="item-2"></a>
## [林纳斯·托瓦兹称赞 AI 在 Linux 内核调试中的帮助](https://simonwillison.net/2026/Aug/22/linus-torvalds/) ⭐️ 8.0/10

林纳斯·托瓦兹公开称赞 AI 助手在调试一个困难的 Linux 内核问题时提供了巨大帮助，具体涉及 drm/xe 驱动的提交“不要将扁平 CCS 存储作为可用 VRAM 分配”。他指出，虽然 AI 很有帮助，但它多次放弃并建议写报告而不是继续。 林纳斯·托瓦兹作为软件开发领域备受尊敬的人物，他的这一认可凸显了 AI 在复杂调试任务中日益重要的作用，并可能鼓励在内核开发中更广泛地采用 AI 辅助编程。这也引发了关于 AI 局限性（如容易放弃）以及人类坚持重要性的讨论。 相关提交是“drm/xe: 不要将扁平 CCS 存储作为可用 VRAM 分配”（提交号 818bebeb63dd6bf5f4e07e145f6cdbace520a34c）。托瓦兹提到，AI 在推动下添加了调试代码并忠实分析，他甚至让 AI 写了提交信息。然而，AI 多次表示问题不可能且无法解决。

rss · Simon Willison · Aug 22, 21:04

**背景**: Linux 内核是一个复杂的开源操作系统内核，调试像 drm/xe（用于 Intel GPU）这样的驱动问题可能极具挑战性。AI 辅助编程涉及使用大型语言模型生成或分析代码，这在软件开发中越来越普遍。托瓦兹的评论反映了 AI 在内核开发中使用的增长趋势，最近的规则要求人工监督并为 AI 生成的代码添加“Assisted-by”标签。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://r.nf/post/10017859">Linus Torvalds uses AI to debug an Intel GPU driver bug - R.NF</a></li>
<li><a href="https://docs.kernel.org/next/gpu/driver-uapi.html">DRM Driver uAPI — The Linux Kernel documentation</a></li>
<li><a href="https://www.linkedin.com/posts/omgjasonbourne_most-strict-code-review-process-in-the-world-activity-7449109052917428224-DCUy">Linux kernel allows AI -generated code with human oversight | LinkedIn</a></li>

</ul>
</details>

**标签**: `#AI`, `#Linux kernel`, `#debugging`, `#Linus Torvalds`, `#software development`

---

<a id="item-3"></a>
## [llama.cpp b10584 修复草稿上下文大小以提升服务器稳定性](https://github.com/ggml-org/llama.cpp/releases/tag/b10584) ⭐️ 7.0/10

llama.cpp 发布了 b10584，修复了草稿上下文大小以匹配目标上下文，从而避免使用非统一 KV 缓存时出现服务器 500 错误。该更新还重构了内存适配逻辑，以考虑第二个模型，提高了准确性。 此修复对于使用独立草稿模型进行推测解码的用户至关重要，因为它消除了服务器崩溃的常见原因并提高了可靠性。它还增强了 llama.cpp（一个广泛使用的 LLM 推理库）的健壮性，使开发者和自托管用户受益。 草稿上下文现在从目标上下文获取其大小，确保两者每个序列持有相同数量的 token。草稿模型的内存预留按目标可容纳的最大上下文进行测量，并且 fit 函数现在接受可选的第二个模型以改进内存估算。

github · github-actions[bot] · Aug 22, 15:06

**背景**: 在 LLM 推理中，KV 缓存存储已处理 token 的中间注意力状态，以加速生成。推测解码使用较小的草稿模型预测多个 token，然后由主模型验证。在 llama.cpp 中，草稿上下文必须正确设置大小，以避免在使用非统一 KV 缓存（每个序列有自己的缓存）时出现故障。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wavect.io/blog/shared-kv-cache-llm-inference-latency/">Shared KV Cache Cut LLM Inference Latency 14x | Wavect</a></li>
<li><a href="https://www.braincuber.com/tutorial/how-to-use-multi-token-prediction-llama-cpp-complete-tutorial">Multi-Token Prediction in llama . cpp : 2.4x Faster Inference (2026)</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#bug-fix`, `#LLM inference`, `#KV cache`, `#server`

---

<a id="item-4"></a>
## [为什么本地 LLM 看起来比实际更笨](https://forum.level1techs.com/t/why-your-local-llm-feels-dumber-than-it-is/253917) ⭐️ 7.0/10

Level1Techs 论坛上的一场讨论探讨了为什么本地 LLM 往往看起来比实际能力更弱，将问题归因于量化、硬件限制等因素。该帖子包含用户在消费级硬件上运行 Qwen 3 8B 和 27B 等模型的实际技巧和基准测试。 这场讨论之所以重要，是因为它解决了 AI 爱好者和开发者在运行本地模型时常遇到的挫败感，可能影响他们如何配置自己的系统。它还强调了速度、准确性和硬件成本之间的权衡，随着本地 LLM 因隐私和成本原因越来越受欢迎，这一点至关重要。 用户报告称，即使是 4 位量化的 Qwen 3 27B 在内部测试中也与 Gemini 3.7 Flash 难以区分，并且在 RTX 5090 和 ninfer 下，他们实现了约 800 TPS 的 token 生成（c=8）和单流约 140 tokens/s。一位用户建议不要量化 KV 缓存，并建议使用至多 Q8 量化以获得更好的准确性，而另一位用户指出本地模型无法与拥有海量计算资源的托管前沿模型相匹敌。

hackernews · felineflock · Aug 22, 18:14 · [社区讨论](https://news.ycombinator.com/item?id=49402232)

**背景**: 本地 LLM 是在个人硬件上运行的大型语言模型，而非云服务器。量化是一种通过降低模型权重的精度来减少内存占用和提高速度的技术，但过度量化可能会降低准确性。拥有足够 VRAM 的 GPU 或具有统一内存的 Apple Silicon 等硬件对于有效运行这些模型至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/what-llm-quantization-simply-explained-simon-frey-ybdzf">What is LLM quantization ? Simply explained .</a></li>
<li><a href="https://symbl.ai/developers/blog/a-guide-to-quantization-in-llms/">A Guide to Quantization in LLMs | Symbl.ai</a></li>
<li><a href="https://overchat.ai/ai-hub/llm-hardware-requirements">Local LLM Hardware Requirements in 2026 | AI Hub</a></li>

</ul>
</details>

**社区讨论**: 社区意见分歧：一些用户热情高涨，分享使用量化模型的积极体验，而怀疑者则认为本地模型无法与托管的前沿模型竞争。关于量化实践也存在争论，一位用户主张避免 KV 缓存量化并最多使用 Q8，而另一位用户则强调激进量化的速度优势。

**标签**: `#local-llm`, `#quantization`, `#hardware`, `#AI`, `#community-discussion`

---

<a id="item-5"></a>
## [苹果在 macOS 27 Golden Gate 中弃用 hdiutil](https://lapcatsoftware.com/articles/2026/8/7.html) ⭐️ 7.0/10

苹果在 macOS 27 Golden Gate 中弃用了命令行工具 hdiutil，并指示用户改用 diskutil image 进行所有磁盘映像操作。这一变化影响了磁盘映像和 RAM 磁盘的创建工作流。 这一弃用对依赖 hdiutil 编写磁盘映像管理脚本的开发者和高级用户意义重大，因为它标志着苹果工具策略的转变。它还可能影响现有的自动化脚本，需要更新以保持与未来 macOS 版本的兼容性。 根据手册页，在 macOS 27.0 中，hdiutil 已被弃用，diskutil image 提供了 attach、create、resize、info 和 chpass 等子命令。然而，hdiutil 目前可能仍可运行，但将不再获得更新。

hackernews · zdw · Aug 22, 19:04 · [社区讨论](https://news.ycombinator.com/item?id=49402741)

**背景**: hdiutil 是 macOS 中历史悠久的命令行工具，用于创建、挂载、转换和验证磁盘映像文件，如 .dmg、.iso 和 .cdr。多年来，它一直是开发者和系统管理员的核心工具。此次弃用与苹果持续现代化和整合命令行工具的努力一致，但过渡可能需要用户调整其工作流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://keith.github.io/xcode-man-pages/hdiutil.1.html">HDIUTIL (1)</a></li>
<li><a href="https://iboysoft.com/wiki/hdiutil.html">What is hdiutil & How to Use It to Convert DMG to ISO</a></li>

</ul>
</details>

**社区讨论**: 社区评论对苹果维护该工具的承诺表示怀疑，有用户指出尽管 xip 已被弃用很长时间，但仍用于 Xcode 分发。其他人则感叹时机不佳，他们刚开始使用 hdiutil，并质疑 RAM 磁盘创建是否也被弃用。一些人则为苹果辩护，指出大多数用户很少使用 hdiutil。

**标签**: `#macOS`, `#deprecation`, `#developer tools`, `#Apple`, `#system utilities`

---

<a id="item-6"></a>
## [Munder Difflin：本地运行一个 AI 克隆办公室](https://munderdiffl.in/) ⭐️ 7.0/10

Munder Difflin 是一个新的开源、本地优先的多智能体框架，它包装现有的编码代理（如 Claude Code 和 Codex），模拟一个 AI 克隆办公室。该项目在发布第一周内就吸引了超过 2 万名用户，并以《办公室》的幽默主题呈现。 该工具通过使模拟确定性和无 token 消耗，解决了多智能体系统中日益增长的 token 消耗问题，可能为开发者降低成本。它还以新颖、幽默的视角展现了智能体群体的功能失调，引起了开发者社区的共鸣，并凸显了更好编排的必要性。 Munder Difflin 与现有订阅配合使用，并利用小时限制，作为个人的克隆并控制其计算机。它支持几乎所有框架和编码代理，模拟是确定性的，意味着不消耗 token，从而可能降低整体 token 使用量。

hackernews · simonpure · Aug 22, 09:49 · [社区讨论](https://news.ycombinator.com/item?id=49398152)

**背景**: 多智能体系统涉及多个 AI 代理协同完成任务，但常常面临高 token 消耗和协调问题。Token 消耗是基于 LLM 的应用中的重大成本因素，因此能够减少 token 消耗的工具很有价值。该项目的《办公室》主题是对此类智能体群体常常混乱和功能失调行为的一种幽默致敬。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://munderdiffl.in/">Munder Difflin — Agent harness to run an office of your clones</a></li>
<li><a href="https://github.com/chaitanyagiri/munder-difflin">GitHub - chaitanyagiri/ munder - difflin : local multi - agent harness</a></li>
<li><a href="https://www.youtube.com/watch?v=yhMLkbNPxXM">Munder Difflin : Free Multi - Agent Harness or Just a Cute... - YouTube</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体积极，用户欣赏其幽默主题以及它带来的关于管理 AI 代理的反思。一些用户如 joshstrange 提供了详细反馈，建议更倾向于流水线和角色而非固定代理，并指出尽管有一些批评，该工具仍令人着迷。作者 chaicodes 积极参与，回答问题并强调减少 token 消耗的好处。

**标签**: `#multi-agent`, `#AI`, `#LLM`, `#developer-tools`, `#automation`

---

<a id="item-7"></a>
## [工具让你忘记屏幕使用时间密码以遏制冲动覆盖](https://waittounlock.com/) ⭐️ 7.0/10

WaitToUnlock.com 是一个新的网络工具，它生成一个随机的屏幕使用时间密码，并以故意令人困惑的方式引导用户输入，使其难以记住。密码被安全存储，只有在强制等待 6 小时后才能恢复。 这解决了 iOS 用户常见的自控问题，他们希望强制执行应用限制，但往往冲动地覆盖限制。通过增加摩擦和冷静期，它帮助用户坚持数字健康目标，而不会完全将自己锁在外面。 该工具使用网页界面生成 4 位密码，并提供涉及算术和删除的逐步说明，以混淆记忆。恢复过程需要 6 小时的延迟，在可访问性和威慑力之间取得平衡。

rss · Hacker News Show HN · Aug 22, 20:17

**背景**: iOS 屏幕使用时间是一项内置功能，允许用户设置应用使用限制，但它依赖于用户容易覆盖的 4 位密码。第三方应用拦截器可以被卸载，使得屏幕使用时间更强大，但密码漏洞削弱了其有效性。该工具利用操作系统级别的限制，同时增加心理障碍以防止冲动绕过。

**标签**: `#iOS`, `#productivity`, `#digital wellbeing`, `#self-control`, `#web tool`

---

<a id="item-8"></a>
## [浏览器工具为 JPEG 添加增益映射，实现 HDR 标志亮度](https://www.soverybright.com/) ⭐️ 7.0/10

一款新的基于浏览器的工具 SoVeryBright 允许用户为 JPEG 图像添加增益映射，使标志在 HDR 屏幕上显得更亮。该工具使用 Claude Code 开发，无需注册。 该技术利用了 Ultra HDR / 增益映射 JPEG 格式，在 HDR 显示器上增强视觉冲击力，目前这一格式在网络上尚未充分利用。它为设计师和开发者提供了一种实用方法，使图像在现代设备上脱颖而出，可能影响未来针对 HDR 屏幕的图像优化方式。 该工具通过向现有 JPEG 添加增益映射来工作，这种映射仅在 HDR 屏幕（如新款 MacBook Pro）上可见。作者指出，LinkedIn 是唯一不剥离这些增益映射的主要社交网络，但用户可以在自己的网站上提供这些图像。

rss · Hacker News Show HN · Aug 22, 18:43

**背景**: 高动态范围（HDR）成像比传统的 8 位格式存储更多的亮度数据。增益映射 JPEG（标准化为 ISO 21496-1，即 Ultra HDR）在标准 SDR JPEG 数据之上添加了一个转换层，使其与 SDR 显示器向后兼容，同时在兼容屏幕上实现 HDR 增强。当前版本的 Chrome 和 Edge 浏览器支持解码增益映射 JPEG。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_dynamic_range">High dynamic range - Wikipedia</a></li>
<li><a href="https://photovoid.com/en/tools/ultrahdr-inspector/">Ultra HDR / Gain Map JPEG Inspector — Photovoid</a></li>
<li><a href="https://github.com/topics/gainmap">gainmap · GitHub Topics · GitHub</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（54 条评论）可能探讨了增益映射的技术细节、浏览器支持以及潜在用例。一些人可能质疑其实用价值或指出效果微妙，而另一些人可能欣赏这个巧妙的技巧和工具的简洁性。

**标签**: `#HDR`, `#JPEG`, `#image-processing`, `#web-development`, `#show-hn`

---

<a id="item-9"></a>
## [llm 0.33：升级 OpenAI 库并新增嵌入键支持](https://simonwillison.net/2026/Aug/22/llm/) ⭐️ 7.0/10

Simon Willison 发布了 llm 0.33，该版本升级到 OpenAI Python 库 3.x，并将 HTTP 客户端依赖从 httpx 切换到 httpx2。同时为 llm embed 和 llm embed-multi 命令新增了--key 支持，并允许重复使用-t/--template 来组合模板。 对于使用 llm 作为与 LLM 交互的 CLI 工具的开发者来说，此版本意义重大，因为它与最新的 OpenAI 库保持一致，并提高了嵌入键管理和模板组合的灵活性。这些更改增强了工具的可用性和可维护性，使更广泛的 LLM 开发者生态系统受益。 嵌入方法现在接受 key=参数，将解析后的每次调用键传递给插件，而不改变共享模型状态，并为现有插件提供了兼容性回退。此外，支持推理的 Responses API 模型现在支持 reasoning_summary 选项，其值可为 auto、concise 和 detailed，可与 llm openai endpoint --responses 一起使用。

rss · Simon Willison · Aug 22, 17:01

**背景**: llm 是 Simon Willison 开发的命令行工具，用于与各种大型语言模型交互。OpenAI Python 库是访问 OpenAI 模型的官方客户端，而 httpx2 是一个 HTTP 客户端库。升级到 OpenAI 库 3.x 和 httpx2 可确保与最新的 API 更改兼容，并提高性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pypi.org/project/openai/">The official Python library for the openai API</a></li>
<li><a href="https://archlinux.org/packages/extra/any/python-httpx2/">Arch Linux - python - httpx 2 2.3.0-1 (any)</a></li>

</ul>
</details>

**标签**: `#llm`, `#release`, `#OpenAI`, `#CLI`, `#embedding`

---

<a id="item-10"></a>
## [编码代理：验证不止于逐行审查](https://simonwillison.net/2026/Aug/22/more-than-just-code-review/) ⭐️ 7.0/10

Simon Willison 认为，有效使用编码代理的关键技能是自信地指导它们并进行验证，而这并不总是需要逐行审查代码。他指出，逐行检查并非最有效的验证方式。 这一观点对采用 AI 辅助开发的软件工程师意义重大，它将焦点从详尽的代码审查转向更高层次的验证策略。它强调了一种实用技能，可以提高生产力并增强对编码代理的信任。 文章简洁，未提供具体示例或工具，但提到了编码代理和代理工程的更广泛背景。它暗示验证可以包括测试、运行软件或其他方法，而不仅仅是人工检查。

rss · Simon Willison · Aug 22, 15:56

**背景**: 编码代理是能够自主编写或修改代码的 AI 工具，例如 OpenAI 的 Codex 或 Zencoder。代理工程是指使用此类代理更快地交付软件的做法，通常会产生大量拉取请求。有效使用需要清晰的指令和稳健的验证，以确保更改正确。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/codex/">Codex in ChatGPT | AI Coding Agents for Software... | OpenAI</a></li>
<li><a href="https://zencoder.ai/">Zencoder | The AI Coding Agent</a></li>
<li><a href="https://www.linkedin.com/pulse/agentic-engineering-shipping-real-systems-speed-vibes-antonichev-v5w2f">Agentic Engineering : Shipping Real Systems at the Speed of Vibes</a></li>

</ul>
</details>

**标签**: `#coding-agents`, `#code-review`, `#generative-ai`, `#agentic-engineering`, `#AI`

---

<a id="item-11"></a>
## [AI 中的模拟：性能降低 10%，成本降低 100 倍，速度提升 10000 倍](https://www.latent.space/p/ainews-10-worse-100x-cheaper-10000x) ⭐️ 7.0/10

文章强调了 AI 中日益增长的趋势，即越来越多地使用模拟进行训练，以仅 10%的性能损失换取 100 倍的成本降低和 10000 倍的速度提升。这表明模拟正在扩展到模型训练之外的其他领域。 这一趋势可能通过显著降低训练模型的成本和加快速度，使 AI 开发更加民主化，让较小的团队和组织能够进行实验和创新。它还可能加速 AI 在物理数据稀缺或获取成本高昂的现实应用中的采用。 文章特别提到了“RSI”（递归自我改进），暗示模拟可能应用于 AI 系统的自我改进循环，而不仅仅是初始训练。提供的内容中没有详细说明具体方法和示例。

rss · Latent Space · Aug 22, 07:36

**背景**: 递归自我改进（RSI）是一个概念，即 AI 系统自主改进自己的代码、提示或参数，可能形成无需人工干预的闭环改进。在这种情况下，模拟可能指的是使用虚拟环境生成训练数据或测试场景，这比现实世界的数据收集更便宜、更快。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.promptbuff.app/blog/when-ai-builds-itself-recursive-self-improvement">When AI Builds Itself: The Rise of Recursive Self-Improvement ( RSI )</a></li>
<li><a href="https://techcrunch.com/2026/05/28/rsi-is-the-new-agi-and-its-just-as-hard-to-pin-down/">RSI is the new AGI — and it's just as hard to pin down | TechCrunch</a></li>
<li><a href="https://min.news/en/tech/3bbea74a30a37d314993a2128620f1cb.html">The RSI concept suddenly triggered a collective bet from top investors...</a></li>

</ul>
</details>

**标签**: `#AI`, `#simulation`, `#training`, `#efficiency`, `#trends`

---

<a id="item-12"></a>
## [AI 模型吸收“缰绳”，焦点转向人类注意力](https://www.latent.space/p/attention-interface) ⭐️ 7.0/10

文章认为，AI 模型正越来越多地将操作框架（“缰绳”）内化到其权重中，并预测下一个前沿是设计利用人类注意力而非模型约束的界面。 这一转变可能重新定义人机交互，从提示工程转向设计适应人类注意力的系统，可能使 AI 对用户更直观、更高效。 这篇文章是一篇评论，缺乏技术深度或实证证据，评分为 7.0/10。它表明，随着模型吸收“缰绳”，界面的角色从约束模型演变为管理人类注意力。

rss · Latent Space · Aug 22, 07:30

**背景**: AI 代理“缰绳”是围绕 AI 模型的软件层，将其从文本生成器转变为工作代理，包括工具、监督和安全制动。注意力界面是根据人类注意力动态优先呈现信息的用户界面，通常使用眼神接触或凝视作为输入。文章结合了这些概念，暗示未来“缰绳”不再需要用于模型，而是用于人类。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/codex/ai-agent-harness-the-layer-that-makes-agents-useful-21ec9eb6f3c7">AI Agent Harness : The Layer That Makes Agents Useful | Medium</a></li>
<li><a href="https://www.cnbc.cmu.edu/~tai/readings/active_vision/attentive_interface.pdf">Designing</a></li>

</ul>
</details>

**标签**: `#AI`, `#human-computer interaction`, `#agent design`, `#attention`, `#future of AI`

---