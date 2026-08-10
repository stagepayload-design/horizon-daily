---
layout: default
title: "Horizon Summary: 2026-08-10 (ZH)"
date: 2026-08-10
lang: zh
---

> From 37 items, 16 important content pieces were selected

---

1. [汤姆·斯坦顿的重力投石机突破音障](#item-1) ⭐️ 8.0/10
2. [Lumabri：受 Napster 启发的点对点 LLM 推理](#item-2) ⭐️ 8.0/10
3. [Preloop：在隔离微虚拟机中本地运行 GitHub Actions](#item-3) ⭐️ 8.0/10
4. [为 AI 编程代理用 Rust 重建虚幻引擎](#item-4) ⭐️ 8.0/10
5. [Claude Opus 5 系统提示揭示出口管制暂停事件](#item-5) ⭐️ 8.0/10
6. [利用 LLM 学习复杂主题：一种实用工作流程](#item-6) ⭐️ 7.0/10
7. [开发者抄袭应用后的“认错”引发强烈反弹](#item-7) ⭐️ 7.0/10
8. [研究发现出租车司机阿尔茨海默病死亡率较低](#item-8) ⭐️ 7.0/10
9. [蒂姆·伯纳斯-李 1998 年关于酷 URI 的文章至今仍有共鸣](#item-9) ⭐️ 7.0/10
10. [AI 可穿戴设备与无处不在的监控的兴起](#item-10) ⭐️ 7.0/10
11. [Windows 11 天气应用占用超过 1GB 内存](#item-11) ⭐️ 7.0/10
12. [Project Oberon 系统移植到 RISC-V](#item-12) ⭐️ 7.0/10
13. [通过 SSH 和 systemd 复活四年前的 reMarkable 2](#item-13) ⭐️ 7.0/10
14. [Celerp：一个本地优先、模块化的会计与 ERP 系统](#item-14) ⭐️ 7.0/10
15. [Albedo：用 Zig 编写的单文件可监听文档数据库](#item-15) ⭐️ 7.0/10
16. [GitHub Models 退役，破坏 Actions 工作流](#item-16) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [汤姆·斯坦顿的重力投石机突破音障](https://www.techeblog.com/tom-stanton-supersonic-trebuchet/) ⭐️ 8.0/10

汤姆·斯坦顿建造了一台仅靠重力驱动的投石机，将 4 克重的弹丸以 776 英里/小时（1249 公里/小时）的速度发射，超过了音速。这一成就被记录在 YouTube 视频中，已获得超过 160 万次观看。 这表明，无需任何化学推进剂，仅凭简单的机械设计就能达到超音速，突破了传统攻城器械技术的极限。它激发了工程和 DIY 社区的想象力，推动了机械抛射技术的进一步创新。 该投石机利用重力配重和高强度迪尼玛（Dyneema）绳索缠绕在鼓上来加速弹丸。弹丸重约 62 格令，大约是 30 格令高速.22LR 子弹的两倍，是 40 格令亚音速子弹的 1.5 倍。

hackernews · Thorondor · Aug 9, 15:08 · [社区讨论](https://news.ycombinator.com/item?id=49232110)

**背景**: 投石机是一种利用铰接臂和投石索发射弹丸的抛石机，历史上用作攻城武器。传统投石机依靠配重提供抛射力，其弹丸通常以亚音速飞行。用这种装置突破音障是一项非凡的工程壮举，需要优化机械优势并最小化能量损失。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=Co57SfcT-h0">Supersonic Trebuchet - YouTube</a></li>
<li><a href="https://hackaday.com/2021/12/01/supersonic-projectile-exceeds-engineers-dreams-the-supersonic-trebuchet/">Supersonic Projectile Exceeds Engineers Dreams: The... | Hackaday</a></li>
<li><a href="https://en.wikipedia.org/wiki/Trebuchet">Trebuchet - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者对此印象深刻，有人指出弹丸重量与枪弹的对比，还有人指出迪尼玛鼓机制与划船自行车上的类似。多位用户分享了视频和相关内容的直接链接，显示出强烈的兴趣和参与度。

**标签**: `#engineering`, `#physics`, `#mechanical design`, `#DIY`, `#supersonic`

---

<a id="item-2"></a>
## [Lumabri：受 Napster 启发的点对点 LLM 推理](https://github.com/JustVugg/lumabri) ⭐️ 8.0/10

Lumabri 是一个新的开源项目，提出通过点对点网络，利用多台普通计算机的资源池来运行大型语言模型，并利用混合专家（MoE）架构来最小化数据传输。这是一个基于作者先前项目 Colibrì的早期实验。 这种方法可能通过让个人共同运行原本需要昂贵数据中心硬件的大型 LLM，从而民主化对大型模型的访问。如果成功，它可能将 AI 基础设施从集中式转向更去中心化、用户拥有的模式，类似于 Napster 改变音乐分发的方式。 Lumabri 解决了网络延迟、安全性、对等验证、SHA-256 验证、签名模型状态、副本选择、故障转移和确定性执行等挑战。它仍处于早期实验阶段，尚无详细评估或基准测试，作者正在用有限的硬件进行构建。

rss · Hacker News Show HN · Aug 9, 22:24

**背景**: 大型语言模型（LLM）通常需要高端硬件，因为其参数量巨大。混合专家（MoE）模型，如 Mixtral 和 DeepSeek-V3，每个 token 只激活一小部分参数，因此更高效。分布式推理技术将模型分割到多个设备上，以运行原本无法访问的模型。Lumabri 将这些概念应用于点对点环境，其中每个节点贡献磁盘、计算或特定专家等资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://digitalis.io/post/why-and-how-i-use-distributed-inference-to-run-a-large-language-model-llm">Why and How I Use Distributed Inference to Run... | Digitalis Blog</a></li>
<li><a href="https://github.com/vllm-project/vllm">vllm-project/vllm: A high-throughput and memory-efficient inference ...</a></li>
<li><a href="https://arxiv.org/pdf/2312.08361">Distributed Inference and Fine-tuning of</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论有限（4 条评论），但总体积极，用户对该概念表示兴趣，并询问延迟和安全性等技术细节。一些评论者指出网络开销和去中心化系统中信任的挑战，而其他人则欣赏这种受 Napster 启发的创新方法。

**标签**: `#distributed systems`, `#LLM inference`, `#peer-to-peer`, `#Mixture-of-Experts`, `#open source`

---

<a id="item-3"></a>
## [Preloop：在隔离微虚拟机中本地运行 GitHub Actions](https://preloop.dev/) ⭐️ 8.0/10

Preloop 是一款基于 Rust 的 GitHub Actions 重新实现，已在 Hacker News 上发布。它能在本地或自托管服务器上，以硬件隔离的微虚拟机（启动时间低于 400 毫秒）运行现有工作流，并使用官方 runner 协议。 这解决了 GitHub Actions 可靠性差且无法本地测试的常见痛点，为开发者提供了一种在不消耗 GitHub 托管分钟数的情况下运行 CI/CD 的方式。其微虚拟机隔离和快速启动特性可能吸引那些希望在工作流中获得更多控制和速度的开发者。 Preloop 使用基于 libkrun 的 smolvm 项目来提供微虚拟机，支持失败暂停（pause-on-failure）以进行调试，并实现了调试适配器协议（DAP）以支持交互式调试。它还支持将更改提交到服务器进行 CI 并打开草稿 PR，并声称在作业/步骤级别上与官方 runner 协议保持一致。

rss · Hacker News Show HN · Aug 9, 19:55

**背景**: GitHub Actions 是一种流行的 CI/CD 服务，但其托管 runner 可能不可靠且缺乏本地测试能力。虽然存在 Act 和 Forgejo 等替代方案，但它们往往没有完全实现官方 runner 协议，或者以容器方式运行作业。微虚拟机比容器提供更强的隔离性，而 libkrun 则支持快速、轻量级的虚拟化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/smol-machines/smolvm">GitHub - smol -machines/ smolvm : Portable, lightweight, self-contained...</a></li>
<li><a href="https://cylab.be/blog/508/smolvm-portable-microvms-without-the-headaches">SmolVM - Portable MicroVMs Without the Headaches | cylab.be</a></li>
<li><a href="https://github.com/ChristopherHX/github-act-runner/issues/96">Upcoming runner -admin / broker / run / results / launch service support...</a></li>

</ul>
</details>

**社区讨论**: HN 讨论目前只有一条评论，因此社区反馈有限。该评论可能提出技术问题或提供反馈，但总体情绪尚不明确。

**标签**: `#GitHub Actions`, `#CI/CD`, `#microVMs`, `#Rust`, `#self-hosted`

---

<a id="item-4"></a>
## [为 AI 编程代理用 Rust 重建虚幻引擎](https://machinesatplay.com/) ⭐️ 8.0/10

一家名为 Machines at Play 的初创公司正在用 Rust 重建虚幻引擎，作为一个面向 Codex 和 Claude Code 等 AI 编程代理的 CLI 驱动的多人 3D 游戏引擎。该项目是开源的（MIT），允许用户提示 AI 代理创建游戏，然后部署到.machinesatplay.com 链接。 该项目可能通过使 AI 代理能够通过 CLI 构建游戏，显著降低 3D 游戏开发的门槛，这比传统可视化编辑器更符合编码代理的工作方式。它还可能展示 Rust 在高性能游戏引擎中的可行性，并影响未来的游戏开发工作流程。 该引擎基于 Bevy（ECS）、Avian（物理）和 Lightyear（预测/回滚/网络）构建。作者指出，Rust 的编译时间是一个他们仍在解决的挑战。该项目包括可工作的演示，如类似 PUBG 的游戏和类似 Rocket League 的汽车足球游戏。

rss · Hacker News Show HN · Aug 9, 19:28

**背景**: 像 Unreal、Unity 和 Godot 这样的传统游戏引擎依赖庞大的编辑器，使用可视化、基于节点的工具，这并不适合通过命令行操作的 AI 编码代理。Rust 是一种以内存安全和性能著称的系统编程语言，通过 Bevy 等库对游戏开发的支持日益增长。Claude Code 和 Codex 等 AI 编码代理是基于终端的工具，可以编辑代码和运行命令，非常适合 CLI 驱动的开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/trunglqdev/Godot_CLI">GitHub - trunglqdev/Godot_ CLI : Drive a live Godot 4.4 editor from the...</a></li>
<li><a href="https://godotengine.org/">Godot Engine - Free and open source 2D and 3D game engine</a></li>
<li><a href="https://openalternative.co/opencode">OpenCode: Open Source Alternative to Claude Code , Codex and Warp</a></li>

</ul>
</details>

**标签**: `#Rust`, `#Game Engine`, `#AI Coding Agents`, `#Open Source`, `#Multiplayer`

---

<a id="item-5"></a>
## [Claude Opus 5 系统提示揭示出口管制暂停事件](https://simonwillison.net/2026/Aug/9/claude-opus-5-system-prompt/#atom-everything) ⭐️ 8.0/10

西蒙·威利森引用了 Claude Opus 5 的系统提示，其中包含一则通知，称 Anthropic 因美国出口管制于 2026 年 6 月 12 日至 7 月 1 日暂停了 Claude Fable 5 和 Claude Mythos 5 的访问。该提示指示模型准确确认暂停事件，并将其视为当前政治话题。 此事意义重大，因为它揭示了主流 AI 模型如何处理敏感的地缘政治事件，表明系统提示可用于弥补模型的知识空白。同时，它也凸显了 AI 监管与模型部署之间日益紧密的联系，影响依赖这些模型的开发者和用户。 系统提示明确指出这些事件发生在 Claude 的训练数据截止日期之后，因此模型仅通过该通知得知。提示指示 Claude 实事求是地确认暂停，避免发表个人观点，并引导用户查阅 Anthropic 的官方声明以获取更多信息。

rss · Simon Willison · Aug 9, 23:31

**背景**: 出口管制是政府用来限制敏感技术跨境流动的法律机制。在此案例中，美国商务部以可能被对手军方用于情报目的为由，对 Anthropic 的 AI 模型实施了管制。Anthropic 游说解除禁令，最终管制于 2026 年 6 月 30 日解除。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cryptobriefing.com/anthropic-lobbies-lutnick-lift-ai-ban/">Anthropic lobbies Commerce Secretary Lutnick to lift US ban on its AI ...</a></li>
<li><a href="https://www.pymnts.com/news/artificial-intelligence/2026/commerce-department-threatened-anthropic-with-criminal-charges-over-ai-models/">PYMNTS | Commerce Dept . Threatened Anthropic With Criminal...</a></li>
<li><a href="https://github.com/asgeirtj/system_prompts_leaks">GitHub - asgeirtj/ system _ prompts _leaks: Extracted system prompts ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Claude`, `#system prompt`, `#Anthropic`, `#model behavior`

---

<a id="item-6"></a>
## [利用 LLM 学习复杂主题：一种实用工作流程](https://laurentiugabriel.github.io/blog/articles/how-i-use-llms-to-learn/) ⭐️ 7.0/10

作者详细介绍了使用 LLM 学习复杂主题的三步工作流程：构建基础知识、事实核查和创建交互式模拟。该方法强调使用 LLM 生成低多边形、类似过山车大亨风格的动画来可视化概念。 这种方法提供了一种新颖的、实践性的方式来利用 LLM 进行深度学习，可能改变个人处理复杂学科的方式。它凸显了 AI 在教育和自学中日益增长的作用，尽管其对 LLM 生成准确性的依赖引发了担忧。 该工作流程包括使用计划模式（如 CC 或 OpenCode）构建基础知识，然后要求模型自我审查准确性，最后生成模拟。作者声称生成的动画“100%准确且无幻觉”，但这一说法在评论中受到质疑。

hackernews · laurentiurad · Aug 9, 19:16 · [社区讨论](https://news.ycombinator.com/item?id=49234675)

**背景**: LLM（大型语言模型）是在海量文本数据上训练的 AI 系统，能够生成类似人类的文本。它们越来越多地被用于学习和教育，但其“幻觉”（产生虚假信息）的倾向是已知的局限性。作者的工作流程试图通过自我审查和模拟来缓解这一问题，但此类方法的有效性并未得到保证。

**社区讨论**: 评论表达了复杂的情绪：一些人觉得模拟步骤有趣，但质疑准确性保证，指出 AI 的自我审查并不可靠。其他人则分享了对 LLM 生成文本的普遍不满，并担心随着 LLM 能力增强，学习技术技能的未来价值。

**标签**: `#LLM`, `#learning`, `#education`, `#AI`, `#productivity`

---

<a id="item-7"></a>
## [开发者抄袭应用后的“认错”引发强烈反弹](https://blog.terrygodier.com/2026/08/09/mea-culpa-dark-hours.html) ⭐️ 7.0/10

一位开发者发布了一篇关于其应用被苹果拒绝的“认错”博客文章，但社区发现该应用是开源天文应用“Dark Hours”的克隆，且开发者误导了 John Gruber。这篇文章因缺乏真诚道歉而引发广泛批评。 这一争议凸显了开发者社区中的伦理问题，包括抄袭和误导有影响力的人物。它强调了应用开发中透明度和原创性的重要性，以及 AI 辅助编码可能导致无意复制的问题。 开发者最初的应用是一个被苹果拒绝的占星应用，之后他们用开源应用“Dark Hours”的克隆版本替换了它，甚至复制了名称。开发者还误导了 John Gruber，后者随后在 Daring Fireball 上发布了撤回声明。批评者指出，这篇“认错”文章没有提及或道歉于误导 Gruber 一事。

hackernews · satvikpendem · Aug 9, 13:20 · [社区讨论](https://news.ycombinator.com/item?id=49231154)

**背景**: 苹果应用商店的指南禁止某些内容，包括占星应用，这导致了拒绝。开源应用“Dark Hours”是一个合法的天文应用，开发者的克隆版本未经署名就复制了它。事件还涉及使用 AI（Claude）生成克隆版本，引发了对 AI 在抄袭中作用的质疑。

**社区讨论**: 社区评论非常批评，用户指责开发者抄袭和误导行为。一些人称这篇帖子是“有限坦白”的公关策略，许多人对开发者涉及 AI 的借口表示怀疑。对 John Gruber 缺乏道歉是主要争议点。

**标签**: `#plagiarism`, `#app-store`, `#ethics`, `#developer-community`, `#controversy`

---

<a id="item-8"></a>
## [研究发现出租车司机阿尔茨海默病死亡率较低](https://theconversation.com/taxi-drivers-rarely-die-of-alzheimers-how-complex-mental-maps-and-spatial-reasoning-protect-your-brain-286650) ⭐️ 7.0/10

最近一项研究表明，与普通人群相比，依赖空间推理的出租车司机阿尔茨海默病死亡率较低。该发现发表在《The Conversation》的一篇新闻文章中，强调了复杂心理地图的潜在保护作用。 这一发现进一步证明了认知参与，尤其是空间推理，可能有助于预防阿尔茨海默病。它可能影响公共卫生建议，并鼓励刺激海马体的活动，从而在更广泛的人群中降低痴呆风险。 该研究使用逻辑回归调整了死亡年龄、性别、种族、民族和教育程度。然而，社区评论者指出了潜在的混杂因素，例如出租车司机的平均预期寿命（67.8 岁）低于普通人群（74 岁），这可能导致结果偏差。

hackernews · jader201 · Aug 9, 15:21 · [社区讨论](https://news.ycombinator.com/item?id=49232253)

**背景**: 阿尔茨海默病是最常见的痴呆症类型，其特征是记忆丧失和认知能力下降。海马体是大脑中对空间导航至关重要的区域，也是阿尔茨海默病最先影响的区域之一。此前的研究，例如 2000 年对伦敦出租车司机的里程碑式研究，表明这些司机因丰富的导航经验而拥有更大的海马体，暗示空间推理与大脑健康之间存在联系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://theconversation.com/taxi-drivers-rarely-die-of-alzheimers-how-complex-mental-maps-and-spatial-reasoning-protect-your-brain-286650">Taxi drivers rarely die of Alzheimer ’ s – how complex mental maps and...</a></li>
<li><a href="https://news.ycombinator.com/item?id=47560179">What are some possibilities? 1. Those with spatial reasoning are less...</a></li>
<li><a href="https://www.healthknowledge.org.uk/public-health-textbook/research-methods/1a-epidemiology/biases">Biases and Confounding | Health Knowledge</a></li>

</ul>
</details>

**社区讨论**: 社区评论提出了几个关键点。一位评论者指出，出租车司机的平均预期寿命较低，这意味着他们可能在达到阿尔茨海默病典型诊断年龄之前去世，从而混淆了结果。另一位强调了选择偏差，认为只有空间能力强的人才能成为成功的出租车司机，因此这份工作可能不会预防阿尔茨海默病，而是吸引了那些不易患病的人。其他人讨论了教育程度调整的作用，并好奇游戏玩家或棋手是否也有类似效应。

**标签**: `#neuroscience`, `#alzheimers`, `#spatial reasoning`, `#cognitive health`, `#epidemiology`

---

<a id="item-9"></a>
## [蒂姆·伯纳斯-李 1998 年关于酷 URI 的文章至今仍有共鸣](https://www.w3.org/Provider/Style/URI) ⭐️ 7.0/10

蒂姆·伯纳斯-李 1998 年的文章《酷 URI 不会改变》再次在 Hacker News 上引发讨论，凸显了其对现代网络架构和链接失效问题的持久相关性。讨论中包含了当代断链和 SEO 驱动重定向的例子。 这篇文章的原则对于维护稳定可靠的网络至关重要，因为链接失效持续影响着用户和组织。理解这些指导原则有助于开发者和内容管理者设计经得起时间考验的 URL，减少断链并保护数字遗产。 文章建议不要在 URL 中包含易变的细节，如文件扩展名、软件名称或主题分类，并建议对移动内容使用 301 重定向。Hacker News 的讨论指出，像 WordPress 这样的现代 CMS 通常会自动处理重定向，但链接失效仍会因网站关闭或重组而发生。

hackernews · Klaster_1 · Aug 9, 14:32 · [社区讨论](https://news.ycombinator.com/item?id=49231809)

**背景**: 链接失效是指超链接逐渐失效的现象，因为目标内容被移动或删除。万维网发明者蒂姆·伯纳斯-李撰写这篇文章，倡导使用持久且长期稳定的 URL，这对于网络的长期可用性和保存至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Link_rot">Link rot - Wikipedia</a></li>
<li><a href="https://museum.parallel.ai/items/cool-uris-don-t-change">Cool URIs Don't Change | Museum of the Human Web</a></li>
<li><a href="https://www.w3.org/Addressing/">Web Naming and Addressing Overview ( URIs , URLs, ...)</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了个人遇到断链的经历，例如微软支持链接指向通用页面，以及 NSF 出版物的 URL 返回 404 错误。一些人指出 SEO 实践和 CMS 重定向缓解了问题，但另一些人认为“永久网络”的理想正受到“垃圾网络”（低质量、短暂内容）的威胁。

**标签**: `#web architecture`, `#URL design`, `#link rot`, `#information architecture`, `#web standards`

---

<a id="item-10"></a>
## [AI 可穿戴设备与无处不在的监控的兴起](https://www.theatlantic.com/technology/2026/05/ai-wearable-surveillance-countermeasures/687203/) ⭐️ 7.0/10

《大西洋月刊》发表了一篇文章，讨论人工智能驱动的可穿戴设备如何普遍记录个人活动，并探讨针对这种监控的潜在对策。这篇文章引发了关于监控资本主义和个人能动性的实质性社区辩论。 这很重要，因为它凸显了人工智能可穿戴设备在日常生活中的日益普及以及随之而来的隐私侵蚀。这一讨论反映了社会对企业权力和加强监管以保护个人自主权的更广泛担忧。 文章提到了芝加哥大学 Sand 实验室的一个早期研究项目“Jammer”，作为当前对策的先驱。社区评论还提到了“监控资本主义”这一概念，该术语由肖莎娜·祖博夫推广，并指出业内人士自 1999 年以来就已意识到这些问题。

hackernews · ike_usawa · Aug 9, 11:30 · [社区讨论](https://news.ycombinator.com/item?id=49230477)

**背景**: 监控资本主义是政治经济学中的一个概念，描述了企业广泛收集和商品化个人数据的现象。人工智能可穿戴设备，如智能眼镜和健身追踪器，持续收集用户活动数据，这些数据可用于定向广告或行为预测。文章和讨论探讨了这项技术对隐私和个人自由的影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Surveillance_capitalism">Surveillance capitalism - Wikipedia</a></li>
<li><a href="https://medium.com/swlh/what-is-surveillance-capitalism-bd7c24d8ddba">What Is Surveillance Capitalism ?. You may have heard the... | Medium</a></li>
<li><a href="https://www.techtarget.com/whatis/definition/surveillance-capitalism">What is surveillance capitalism ? - Definition from WhatIs.com</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了多种观点：一些人提到像“Jammer”这样的早期研究项目作为潜在对策，而另一些人则呼吁像政教分离那样实现企业与国家的分离。一些用户认为人们自愿使用智能手机和社交媒体参与监控，而另一些人则建议像 EFF 这样的监督组织应开展公众宣传活动，以突出企业监控的令人毛骨悚然之处。

**标签**: `#surveillance`, `#AI wearables`, `#privacy`, `#surveillance capitalism`

---

<a id="item-11"></a>
## [Windows 11 天气应用占用超过 1GB 内存](https://www.notebookcheck.net/Windows-11-s-built-in-Weather-app-wastes-more-than-1-GB-of-RAM.1364205.0.html) ⭐️ 7.0/10

Windows 11 自带的天气应用被发现占用超过 1GB 的内存，主要原因是其底层框架。这一问题引发了社区讨论和变通方案，例如改用网页应用封装。 这凸显了默认操作系统组件中的严重性能臃肿问题，影响用户体验和系统资源，尤其是在内存有限的机器上。它还引发了对现代应用框架效率和操作系统级资源管理的更广泛担忧。 高内存占用归因于应用底层框架，它产生了多个进程，如渲染器和 GPU 进程。实际内存占用可能与其他组件共享，使得准确测量变得困难。

hackernews · akyuu · Aug 9, 15:11 · [社区讨论](https://news.ycombinator.com/item?id=49232138)

**背景**: Windows 11 包含一个基于 Web 框架（可能是 Edge WebView2）的默认天气应用。这类框架通常会加载完整的浏览器引擎，导致高内存占用。用户发现，用网页应用快捷方式替代该应用可以显著降低内存消耗。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://notifire.in/tech/windows-11-weather-app-quietly-eats-system-memory">Windows 11 Memory Leak Found in Default Weather App | Notifire</a></li>
<li><a href="https://tech4gamers.com/windows-11-weather-app-consume-1gb-memory/">Windows 11 Weather App Alone Can Consume Over 1GB of Memory</a></li>

</ul>
</details>

**社区讨论**: 社区评论提出了实用的变通方案，例如使用 uBlock Origin 和网页应用快捷方式将内存占用降至约 130MB。一些用户指出，由于共享组件，测量内存使用情况很复杂，而另一些用户则批评与 macOS 相比的臃肿。还有关于需要操作系统级垃圾回收以更有效管理内存的讨论。

**标签**: `#Windows 11`, `#RAM usage`, `#Performance`, `#Blameware`, `#Tech support`

---

<a id="item-12"></a>
## [Project Oberon 系统移植到 RISC-V](https://github.com/rochus-keller/OberonSystem/tree/op2-rv32) ⭐️ 7.0/10

Project Oberon 系统的一个版本已被开发出来，可在 RISC-V 架构上运行，取代了原有的 RISC-5 架构。该项目在 GitHub 上的 'op2-rv32' 分支中可用。 此次移植将 Wirth 的 Oberon 系统扩展到现代开放指令集架构，使其能被更广泛的硬件和爱好者使用。它保留了 Oberon 的遗产，并展示了在当代架构上运行经典系统的可行性。 该系统运行在低成本开发板（Digilent 的 Xilinx Spartan-3）上，配备 1 MB 静态 RAM。该移植基于原始 Oberon 系统，并使其适应 RISC-V 指令集。

hackernews · Rochus · Aug 9, 12:43 · [社区讨论](https://news.ycombinator.com/item?id=49230891)

**背景**: Project Oberon 是 Niklaus Wirth 和 Jürg Gutknecht 在 1980 年代设计的操作系统和编译器，最初针对 RISC-5 架构。RISC-V 是一种开放标准的指令集架构（ISA），近年来因其灵活性和开放性而广受欢迎。此次移植使 Oberon 能够在 RISC-V 硬件上运行，弥合了经典系统与现代开源硬件之间的鸿沟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lists.inf.ethz.ch/pipermail/oberon/2014/007752.html">[Oberon] RISC 5 versus RISC - V</a></li>
<li><a href="https://www.geeksforgeeks.org/computer-organization-architecture/computer-organization-risc-and-cisc/">RISC vs CISC - GeeksforGeeks</a></li>

</ul>
</details>

**社区讨论**: 社区对该项目表示赞赏，一位评论者称赞其为保持 Wirth 精神所做的努力。另一位评论者指出了更早的 Oberon-on-RISC-V 项目和邮件列表讨论，提供了额外背景。还有关于在 ESP P4 上自托管的实用性问题，以及建议使用 MiSTer FPGA 以获得更广泛可用性的建议。

**标签**: `#Oberon`, `#RISC-V`, `#retrocomputing`, `#systems programming`, `#FPGA`

---

<a id="item-13"></a>
## [通过 SSH 和 systemd 复活四年前的 reMarkable 2](https://oskrim.github.io/hardware/2026/08/09/remarkable-over-ssh.html) ⭐️ 7.0/10

一篇详细的教程展示了如何通过 SSH 和 systemd 复活一台四年前的 reMarkable 2 平板，凸显了其基于 Linux 的可玩性。文章表明，即使固件过时，通过手动配置和服务管理也能让设备重获新生。 这很重要，因为它凸显了 reMarkable 2 在消费级平板中罕见的开放性和开发者友好性。同时，它为遇到类似问题的用户提供了实用资源，可能延长设备寿命并减少电子垃圾。 文章详细介绍了通过 USB 启用 SSH、手动更新配置文件以启用 Web 服务器以及使用 systemd 进行服务控制等步骤。同时指出，某些步骤（如启用 Web 服务器）实际上并非必要，因为可以在设置中直接切换。

hackernews · tremguy · Aug 9, 11:39 · [社区讨论](https://news.ycombinator.com/item?id=49230514)

**背景**: reMarkable 2 是一款专为笔记和阅读设计的电子墨水平板，运行基于 Linux 的操作系统。其开发者友好的特性允许用户通过 SSH 访问、修改系统文件并安装自定义软件，这在消费级设备中并不常见。这种开放性催生了一个开发社区，创建各种修改和工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://awesome.ecosyste.ms/topics/remarkable-tablet">reMarkable tablet | Ecosyste.ms: Awesome</a></li>
<li><a href="https://github.com/topics/ssh-bruteforce">ssh -bruteforce · GitHub Topics · GitHub</a></li>
<li><a href="https://hackertarget.com/ssh-two-factor-google-authenticator/">Two factor ( 2 FA) SSH with Google Authenticator in 8 minutes</a></li>

</ul>
</details>

**社区讨论**: 社区讨论总体积极，用户赞赏该设备的 Linux 可玩性。一些评论者指出文章中的某些步骤并非必要，例如手动启用 Web 服务器，并建议使用 codexctl 等工具进行离线更新。也有评论质疑为什么一台四年前的设备需要“复活”。

**标签**: `#reMarkable`, `#Linux`, `#hardware`, `#SSH`, `#systemd`

---

<a id="item-14"></a>
## [Celerp：一个本地优先、模块化的会计与 ERP 系统](https://github.com/celerp/celerp) ⭐️ 7.0/10

Celerp，一个自托管的会计与 ERP 系统，已作为桌面应用发布，启动本地服务器并内置 Postgres，允许办公室内通过浏览器访问。它采用模块化架构，提供 16 个行业预设，并采用开放核心许可模式。 该项目满足了日益增长的本地优先、自托管商业软件需求，使中小企业（SMEs）能更好地控制其数据和基础设施。其模块化设计和 AI 友好的可扩展性可能降低定制 ERP 系统的门槛，有望颠覆传统企业软件模式。 Celerp 捆绑了 Postgres 并启动本地服务器；开发者可通过'pip install celerp && celerp init'安装。它包含库存、采购、发票、制造、会计、条码标签、CSV 导入/导出、角色权限、AI 操作员和不可变审计追踪等模块。核心采用 BUSL-1.1（可转换为 Apache），默认业务模块为 MIT，官方 UI 源代码可用，单用户免费使用。

rss · Hacker News Show HN · Aug 10, 00:04

**背景**: 本地优先软件，由 Ink & Switch 在 2019 年宣言中推广，将数据主要存储在用户设备上，云同步作为次要考虑。模块化 ERP 系统允许企业仅选择和集成所需模块，相比一体化解决方案更具灵活性。自托管会计软件使组织能够直接控制其财务数据和定制化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://powersync.mintlify.app/resources/local-first-software">Understand the local - first software architecture pattern and how...</a></li>
<li><a href="https://www.tailor.tech/resources/posts/modular-erp-system-advantages-and-disadvantages">Modular ERP System Advantages and Disadvantages | Tailor</a></li>
<li><a href="https://openalternative.co/collections/self-hosted/categories/accounting-software">Best Self - hosted Accounting Software in 2026</a></li>

</ul>
</details>

**标签**: `#ERP`, `#accounting`, `#self-hosted`, `#modular`, `#local-first`

---

<a id="item-15"></a>
## [Albedo：用 Zig 编写的单文件可监听文档数据库](https://github.com/klirix/albedo) ⭐️ 7.0/10

Albedo 是一个用 Zig 编写的新型单文件文档数据库，具有可索引的 BSON 数组、查询监听、复制和基本崩溃恢复功能。它作为 Show HN 在 Hacker News 上发布，作者提到开发了大约一年。 Albedo 满足了轻量级嵌入式存储的需求，避免了 SQLite 的 schema 和迁移带来的开销，为小型项目和微服务提供了更简单的替代方案。它使用 Zig 编写，使其能够在 C/C++、Rust 和 Zig 环境中广泛移植，可能吸引寻求最小但功能强大的数据库的开发者。 Albedo 被描述为“字面上是一个可索引的 BSON 数组，具有查询监听、复制和基本崩溃恢复功能”。作者已通过 Flutter 插件将其集成到移动应用中，并通过 Bun FFI 和 Node 原生模块用于后端，表明其实际可用性。

rss · Hacker News Show HN · Aug 9, 23:03

**背景**: BSON（二进制 JSON）是类似 JSON 文档的二进制编码序列化格式，被 MongoDB 等数据库用于高效存储和遍历。单文件数据库将所有数据存储在一个文件中，简化了部署和管理。Zig 是一种低级系统编程语言，注重性能和安全性，适用于嵌入式及可移植应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://modernorange.io/item/49237132">Show HN: Albedo – single-file listenable document database in Zig</a></li>
<li><a href="https://iq.opengenus.org/binary-json/">Binary JSON ( BSON )</a></li>

</ul>
</details>

**标签**: `#database`, `#zig`, `#embedded`, `#bson`, `#replication`

---

<a id="item-16"></a>
## [GitHub Models 退役，破坏 Actions 工作流](https://simonwillison.net/2026/Aug/9/github-models-is-now-retired/#atom-everything) ⭐️ 7.0/10

GitHub Models 已于 2026 年 7 月底正式退役，其统一 LLM API 不再可用。这一退役破坏了依赖 GitHub Actions 中内置 GitHub API 密钥进行 LLM 调用的工作流，Simon Willison 的仓库 Actions 运行失败就是例证。 此次退役影响了那些在 GitHub Actions 中利用 GitHub Models 便捷、低成本访问 LLM 的开发者，尤其是构建 Continuous AI 工作流的开发者。这标志着随着编码代理增加使用成本，免费或补贴 token 的提供模式正在转变，促使开发者转向其他 API 提供商。 GitHub 未透露关闭原因，但推测指向为编码代理模式补贴 token 的高昂成本。Simon Willison 用带月度消费限额的 OpenAI API 密钥替代了 GitHub Models，现使用 GPT-5.6 Luna 生成文件夹摘要，展示了一条实用的迁移路径。

rss · Simon Willison · Aug 9, 22:48

**背景**: GitHub Models 是一项提供模型游乐场和跨多个 LLM 提供商的统一 API 的服务，其关键优势是 GitHub Actions 中的代码可以使用现有的 GitHub API 密钥来运行提示。这与 GitHub Next 的“Continuous AI”概念一致，该概念侧重于在软件协作中针对性地、可靠地使用 AI，而非完全自主的代理。此次退役遵循了一种模式：随着使用量增长，免费或补贴 token 的提供变得不可持续。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://githubnext.com/projects/continuous-ai/">Continuous AI</a></li>
<li><a href="https://simonwillison.net/2025/Jun/27/continuous-ai/">Continuous AI</a></li>
<li><a href="https://docs.github.com/en/actions">GitHub Actions documentation - GitHub Docs</a></li>

</ul>
</details>

**标签**: `#GitHub`, `#LLM`, `#API`, `#Retirement`, `#Developer Tools`

---