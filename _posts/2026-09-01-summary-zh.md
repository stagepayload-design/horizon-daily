---
layout: default
title: "Horizon Summary: 2026-09-01 (ZH)"
date: 2026-09-01
lang: zh
---

> From 59 items, 12 important content pieces were selected

---

1. [谷歌从 Chrome 网上应用店移除 MV2 扩展，包括 uBlock Origin](#item-1) ⭐️ 8.0/10
2. [NAT：互联网中心化的原罪](#item-2) ⭐️ 8.0/10
3. [httpx v1.11.0 新增 TLS 模拟与页面类型分类功能](#item-3) ⭐️ 7.0/10
4. [llama.cpp b10726 加速 AVX2 CPU 上的 IQ 模型](#item-4) ⭐️ 7.0/10
5. [将安防摄像头改造成自动鸟类识别系统](#item-5) ⭐️ 7.0/10
6. [RavynOS：基于 FreeBSD 和 Darwin 的预 alpha 类 macOS 开源操作系统](#item-6) ⭐️ 7.0/10
7. [ChatGPT Work 工具参考网站重点介绍 Playwright 浏览器控制技能](#item-7) ⭐️ 7.0/10
8. [军事超市冰柜故障引发 ICS 安全争论](#item-8) ⭐️ 7.0/10
9. [将《毁灭战士》编译进大语言模型：一次新颖的 AI 演示](#item-9) ⭐️ 7.0/10
10. [CISA 将两个正在被利用的 PaperCut 漏洞加入 KEV 目录](#item-10) ⭐️ 7.0/10
11. [OpenAI 的 ChatGPT 广告年化收入达 10 亿美元，全球扩展](#item-11) ⭐️ 7.0/10
12. [Wrapture：用于追踪和测试的新 Python 库](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [谷歌从 Chrome 网上应用店移除 MV2 扩展，包括 uBlock Origin](https://webiterate.dev/google-removed-extensions-ublock-origin-108/) ⭐️ 8.0/10

谷歌已开始从 Chrome 网上应用店移除 Manifest V2（MV2）扩展，包括流行的广告拦截器 uBlock Origin。这一变化迫使用户要么改用 Firefox 等替代浏览器，要么依赖功能较弱的 uBlock Origin Lite。 这标志着浏览器生态系统的重大转变，影响了数百万依赖广告拦截器保障安全和隐私的用户。这引发了对谷歌对网络控制的担忧，并可能加速用户迁移到 Firefox，后者继续支持功能完整的 MV2 扩展。 此次移除是谷歌向 Manifest V3 过渡的一部分，该版本限制了广告拦截功能。uBlock Origin 在 Firefox 和 Brave 上仍然可用，而 Chrome 用户只能使用 uBlock Origin Lite，其过滤列表更少，功能也较弱。

hackernews · twapi · Aug 31, 21:10 · [社区讨论](https://news.ycombinator.com/item?id=49514878)

**背景**: Manifest V2 是 Chrome 之前的扩展框架，而 Manifest V3 是新的框架，谷歌声称其更安全，但对广告拦截器施加了限制。uBlock Origin 是一款广泛使用的开源广告拦截器，依赖 MV2 的 webRequest API 来有效拦截广告。谷歌从 2024 年开始分阶段移除 MV2 扩展，预计到 2025 年 6 月完成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techzine.eu/news/security/126153/chrome-extensions-remain-a-threat-even-after-googles-manifest-v3/">Chrome extensions remain a threat even after Google's Manifest V 3</a></li>
<li><a href="https://medium.com/@pthapa1/google-chromes-monopoly-on-the-browser-market-is-scary-1267454b5aa6">Google Chrome ’s Monopoly on the Browser Market Is Scary. | Medium</a></li>
<li><a href="https://factually.co/fact-checks/technology/manifest-v3-ad-blockers-ublock-origin-brave-firefox-2026-16ed91">How Manifest V3 Changed Ad Blockers: uBlock Origin , Br...</a></li>

</ul>
</details>

**社区讨论**: 社区情绪普遍负面，用户表示沮丧并推荐 Firefox 作为更好的替代品。一些人强调广告拦截是安全问题，尤其是对技术不熟悉的用户，并批评谷歌在浏览器市场的垄断地位。

**标签**: `#Chrome`, `#Manifest V2`, `#ad-blocking`, `#Firefox`, `#browser monopoly`

---

<a id="item-2"></a>
## [NAT：互联网中心化的原罪](https://dreamstation.systems/personal/ntppost.html) ⭐️ 8.0/10

一篇评论文章认为网络地址转换（NAT）是互联网中心化的根本原因，引发了与 Linux NAT 实现者 Rusty Russell 的历史见解的讨论。讨论强调 NAT 削弱了托管服务器的能力，并塑造了客户端-服务器的思维模式。 这一观点挑战了将 NAT 视为良性地址节省工具的常见看法，暗示它促成了从去中心化、对等互联网向集中化、云主导互联网的转变。这对网络工程师、政策制定者以及任何关心互联网开放性和用户自主权的人都很重要。 文章引用了 RFC 1631（1994 年）作为 NAT 的正式提案，旨在解决 IP 地址枯竭和路由扩展问题。社区评论指出，NAT 还充当“穷人的防火墙”，而运营商级 NAT（CGNAT）被认为比普通 NAT 更有害。

hackernews · robinpie · Aug 31, 02:23 · [社区讨论](https://news.ycombinator.com/item?id=49504905)

**背景**: 网络地址转换（NAT）是路由器使用的一种方法，允许专用网络上的多个设备共享一个公共 IP 地址访问互联网。它于 20 世纪 90 年代中期引入，以缓解 IPv4 地址枯竭问题，但它也破坏了原始互联网设计的端到端连接原则，使设备更难接受传入连接。这对托管服务和点对点通信有影响，可能促进了互联网服务的中心化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/network-address-translation-nat-unsung-hero-your-bhaskar-jyoti-mudoi-nygsf">Network Address Translation ( NAT ): The Unsung Hero of Your...</a></li>
<li><a href="https://maneesh29s.github.io/digital-garden-publish/ComputerNetworking/NAT">Network Address Translationby Maneesh Sutar</a></li>
<li><a href="https://www.exam-labs.com/blog/decoding-the-invisible-bridge-how-nat-quietly-shapes-internet-communication">Decoding the Invisible Bridge — How NAT Quietly Shapes Internet ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论情绪复杂。Linux NAT 实现者 Rusty Russell 对自己的角色表示遗憾，承认 NAT 削弱了拥有公共端点的能力。其他人则认为 NAT 不是“原罪”，而是一种务实的解决方案，真正的问题是 CGNAT，并且 NAT 保护了不安全的设备免受暴露。还有人指责互联网的设计将“现实世界规范”应用于网络空间，导致安全问题。

**标签**: `#NAT`, `#internet architecture`, `#networking`, `#centralization`, `#history`

---

<a id="item-3"></a>
## [httpx v1.11.0 新增 TLS 模拟与页面类型分类功能](https://github.com/projectdiscovery/httpx/releases/tag/v1.11.0) ⭐️ 7.0/10

httpx v1.11.0 已发布，通过新的 -kb 标志引入了可选的页面类型分类功能，并为 -tls-impersonate 选项添加了 Chrome 和 JA3 策略。该版本还包含多项错误修复和其他改进。 此版本增强了 httpx 在安全侦察方面的能力，尤其是 TLS 模拟策略有助于在扫描过程中规避检测。可选的页面类型分类功能为用户提供了更多灵活性，使其能够在不需要性能开销的情况下识别网页类型。 -kb 标志使页面类型分类变为可选，默认关闭以避免性能影响。新的 TLS 模拟策略包括 Chrome 和 JA3，允许用户模仿不同的 TLS 指纹。错误修复解决了 pdcp 数据丢失、管道连接泄漏、Close() 竞态条件以及 FilterCustom 错误吞没等问题。

github · dogancanbakir · Aug 31, 05:18

**背景**: httpx 是由 ProjectDiscovery 开发的快速多用途 HTTP 工具包，安全专业人员广泛使用它来探测基于 HTTP 的目标并提取状态码、标题、重定向和 Web 技术等信息。TLS 模拟允许工具模仿真实浏览器的 TLS 指纹，使服务器更难检测到自动化扫描。页面类型分类有助于识别响应是否为登录页面、错误页面或其他类型，这对侦察非常有用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://scansearch.net/en/articles/httpx-web-toolkit-guide/">httpx : Fast HTTP Toolkit for Security Reconnaissance | ScanSearch</a></li>
<li><a href="https://lipsonthomas.com/httpx/">Mastering HTTPX : Installation, Usage, and Best Practices</a></li>

</ul>
</details>

**标签**: `#security`, `#httpx`, `#release`, `#TLS`, `#bugfix`

---

<a id="item-4"></a>
## [llama.cpp b10726 加速 AVX2 CPU 上的 IQ 模型](https://github.com/ggml-org/llama.cpp/releases/tag/b10726) ⭐️ 7.0/10

llama.cpp 版本 b10726 为 IQ 量化模型引入了批量 GEMM 内核，显著加快了 AVX2 CPU 上大批量提示词处理的速度。该更新包括新的内核（如 ggml_gemm_iqp_8x8_q8_K_p4）以及对 IQ 面板解码的多项优化。 此优化提升了 AVX2 CPU（常见于消费级硬件）上 IQ 量化模型的推理性能。它加快了大批量提示词的处理速度，有利于批量推理和服务器端部署等应用。 该版本为 IQ 量化添加了批量 GEMM 内核，包括新内核 ggml_gemm_iqp_8x8_q8_K_p4，并移除了临时缓冲区。它还包含 NUMA 回退，并为所有网格 IQ 类型添加了 IQP 覆盖测试。

github · github-actions[bot] · Aug 31, 19:41

**背景**: IQ（整数量化）是 llama.cpp 中的一系列量化方法，利用查找表压缩模型权重，以速度换取内存节省。AVX2 是 x86 CPU 的指令集扩展，支持更快的 SIMD 操作，常见于现代 Intel 和 AMD 处理器。批量 GEMM（通用矩阵乘法）内核针对同时处理多个输入进行了优化，这对于大批量提示词处理至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/eightynine01/arm-quant-gemm">GitHub - eightynine01/arm-quant- gemm : int8 GEMM kernels for...</a></li>
<li><a href="https://stackoverflow.com/questions/78356777/what-does-i-in-the-section-iq-and-m-mean-in-this-name-meta-llama-3-8b-i">artificial intelligence - What does "I" in the section "_ IQ "...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Skylake_(microarchitecture)">Skylake (microarchitecture) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#performance`, `#AVX2`, `#quantization`, `#inference`

---

<a id="item-5"></a>
## [将安防摄像头改造成自动鸟类识别系统](https://jasontucker.blog/how-i-turned-my-security-cameras-into-an-automatic-bird-identification-system-with-birdnet-go/) ⭐️ 7.0/10

一位爱好者详细介绍了如何利用 BirdNET-Go 将安防摄像头改造成自动鸟类识别系统，并分享了设置过程，引发了社区讨论。该帖子展示了 BirdNET-Go 与 RTSP 摄像头流的实用且新颖的应用。 该项目展示了现有硬件的创造性 DIY 用途，使鸟类识别对爱好者更加普及，并可能激发类似的家居自动化项目。它还展示了 BirdNET-Go 的多功能性，可能促进其在公民科学和家庭监控中的更广泛应用。 该设置利用安防摄像头的 RTSP 流，BirdNET-Go 可对其进行分析以识别鸟声。社区成员指出了诸如音频采样率要求（BirdNET 期望 48kHz）和风噪等挑战，有些人选择使用外部麦克风或专用硬件（如 Raspberry Pi）。

hackernews · speckx · Aug 31, 16:47 · [社区讨论](https://news.ycombinator.com/item?id=49511856)

**背景**: BirdNET 是由康奈尔鸟类学实验室开发的 AI 鸟类声音识别工具，能够从音频录音中识别数千种鸟类。BirdNET-Go 是一种自托管、实时的实现，可以处理来自麦克风或网络流的音频，因此非常适合此类 DIY 项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepwiki.com/tphakala/birdnet-go">tphakala/ birdnet - go | DeepWiki</a></li>
<li><a href="https://birdnet.cornell.edu/">BirdNET – AI-Powered Sound ID</a></li>
<li><a href="https://github.com/tphakala/birdnet-go">GitHub - tphakala/ birdnet - go : Self-hosted realtime soundscape...</a></li>

</ul>
</details>

**社区讨论**: 社区反应积极且参与度高，用户分享了他们自己的类似设置和改进。一些人讨论了音频质量和采样率等技术挑战，而另一些人则建议使用 Merlin Bird ID 应用或便携式 BirdNET-Pi 构建等替代工具。

**标签**: `#BirdNET`, `#DIY`, `#Computer Vision`, `#Audio Processing`, `#Home Automation`

---

<a id="item-6"></a>
## [RavynOS：基于 FreeBSD 和 Darwin 的预 alpha 类 macOS 开源操作系统](https://ravynos.com/) ⭐️ 7.0/10

RavynOS 是一个预 alpha 阶段的开源操作系统，旨在将类似 macOS 的易用性与 FreeBSD 的自由相结合，并引发了大量社区讨论（101 条评论，得分 160）。该项目基于 Darwin、FreeBSD 和 Apple 的开源组件，目标是 x86-64 架构，未来计划支持 arm64。 该项目在技术上很有趣，因为它探索了一种开源的、可能更灵活的 macOS 替代方案，这可能会吸引那些希望获得类似 macOS 体验但不想受限于 Apple 硬件的用户。它也为 ReactOS 和 Darling 等旨在兼容专有系统的开源 OS 项目生态系统做出了贡献。 RavynOS 处于预 alpha 阶段，仅有 5 年历史，团队规模小，因此尚不能作为 macOS 的即用替代品。项目 FAQ 通过引用 ReactOS 和 GNUstep 等先例来回应法律问题，并旨在通过克隆库和 API 来实现与 macOS 应用的兼容性。

hackernews · Bluestein · Aug 31, 16:19 · [社区讨论](https://news.ycombinator.com/item?id=49511534)

**背景**: Darwin 是 macOS 的开源核心，由 XNU 内核（基于 Mach 和 BSD）和各种 Unix 工具组成，但缺少图形用户界面和专有框架。FreeBSD 是一个成熟的开源类 Unix 操作系统，以其稳定性和宽松许可证而闻名。RavynOS 基于这些基础，提供类似 macOS 的桌面环境，同时保持完全开源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ravynos.com/">ravynOS - Finesse of macOS. Freedom of Open Source.</a></li>
<li><a href="https://github.com/ravynsoft/ravynos">GitHub - ravynsoft/ ravynos : An open-source OS project that aims to...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Darwin_(operating_system)">Darwin ( operating system ) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区情绪复杂：一些人质疑 Darwin 相对于其他 BSD 的价值，而另一些人则鉴于项目规模小且处于早期阶段，为其雄心辩护。关于缺少截图和法律方面也存在争论，FAQ 通过引用类似项目来回应这些担忧。

**标签**: `#operating systems`, `#open source`, `#FreeBSD`, `#macOS compatibility`, `#Darwin`

---

<a id="item-7"></a>
## [ChatGPT Work 工具参考网站重点介绍 Playwright 浏览器控制技能](https://codex-tool-reference.simonw.chatgpt.site/) ⭐️ 7.0/10

一个新的参考网站 codex-tool-reference.simonw.chatgpt.site 记录了 ChatGPT Work 的工具和技能，其中重点介绍了一个使用 Playwright 通过 Node.js REPL 控制浏览器的技能。该技能指示模型运行 `nodeRepl.write(await browser.documentation());` 以获取详细的使用说明。 该参考为扩展 ChatGPT Work 的功能提供了实用且可复用的模式，尤其是浏览器自动化方面，这可能使开发者和 AI 代理受益。它还引发了关于 AI 生成工具的设计及其与 Codex 等现有框架关系的讨论。 浏览器控制技能利用了跨浏览器自动化框架 Playwright，并通过 Node.js REPL 与浏览器交互。该网站还包含创建提示和背景信息，如社区评论中所述。

hackernews · ijidak · Aug 31, 14:07 · [社区讨论](https://news.ycombinator.com/item?id=49510000)

**背景**: ChatGPT Work 是 ChatGPT 的一项功能，允许其使用外部工具和技能来执行任务。Playwright 是一个开源浏览器自动化库，支持 Chromium、Firefox 和 WebKit，常用于测试和脚本编写。该参考网站似乎是此类工具和技能的精选集合，其中浏览器控制技能是一个突出的例子。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://playwright.dev/">Fast and reliable end-to-end testing for modern web apps | Playwright</a></li>
<li><a href="https://github.com/microsoft/playwright">GitHub - microsoft/ playwright : Playwright is a framework for Web...</a></li>

</ul>
</details>

**社区讨论**: 社区评论显示了对浏览器控制技能的兴趣，simonw 提供了技术细节和背景。一些用户质疑它与 Codex 的区别，而另一些用户则建议改进 UI，并指出 AI 生成的网站具有常见的美学风格。

**标签**: `#ChatGPT`, `#AI tools`, `#browser automation`, `#Playwright`, `#reference`

---

<a id="item-8"></a>
## [军事超市冰柜故障引发 ICS 安全争论](https://signalandsilence.substack.com/p/i-think-someone-hacked-the-commissary) ⭐️ 7.0/10

一篇推测性博客文章认为，美国军事超市的冰柜可能遭到黑客攻击，此前有报道称从 8 月 26 日起，14 个以上基地出现大范围制冷中断。五角大楼已确认发生“制冷中断”，但未说明原因。 这一事件凸显了关键基础设施中工业控制系统（ICS）的脆弱性，尤其是在军事环境中。如果确认为网络攻击，可能预示着一种针对食品供应链和偏远基地的新型战略威胁，并对当地经济产生连锁影响。 这篇博客文章是推测性的，没有提供黑客攻击的具体证据。来自 IT 和军事专业人士的社区评论提出了其他解释，如配置错误或更新故障，并指出许多 PLC（如西门子 S7-1500）通常缺乏 TLS 加密等基本安全措施。

hackernews · jcurbo · Aug 31, 11:45 · [社区讨论](https://news.ycombinator.com/item?id=49508506)

**背景**: 工业控制系统（ICS）管理着电网、水处理和制冷等关键基础设施。这些系统通常依赖可编程逻辑控制器（PLC），而这些控制器可能具有弱安全性，例如默认凭据或未加密通信。军事超市是基地内的杂货店，为军人及其家属提供折扣食品；中断可能影响士气和战备状态，尤其是在偏远的海外地点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://genztech.blog/p/military-commissary-freezers-hack-theory/">Military Commissary Freezers Failed at 14+ Bases. Was It a Hack ?</a></li>
<li><a href="https://www.militarytimes.com/news/your-military/2026/08/28/dod-confirms-refrigeration-disruption-at-military-commissaries/">DoD confirms ‘refrigeration disruption’ at military commissaries</a></li>

</ul>
</details>

**社区讨论**: 社区评论大多对黑客攻击理论持怀疑态度。一位有 20 多年服役经验的退役 IT/安全专业人士认为，这更可能是配置错误或更新故障，但指出时机令人担忧。另一位评论者指出，作者并未明确声称是黑客攻击，并质疑故障基线率，而其他人则分享了工业环境中 PLC 不安全的轶事，支持此类漏洞存在的可能性。

**标签**: `#security`, `#industrial-control-systems`, `#military`, `#infrastructure`, `#hacking`

---

<a id="item-9"></a>
## [将《毁灭战士》编译进大语言模型：一次新颖的 AI 演示](https://github.com/physicsrob/torchwright_doom/) ⭐️ 7.0/10

一个名为 torchwright_doom 的项目将经典游戏《毁灭战士》编译进了大语言模型（LLM），展示了 LLM 在文本生成之外的非常规用途。该项目托管在 GitHub 上，并以“Show HN”的形式发布在 Hacker News 上。 该项目拓展了 LLM 的能力边界，可能激发关于将 LLM 用于交互式应用或游戏引擎的新研究。它也可能引发关于 LLM 在处理复杂实时任务时的通用性和局限性的讨论。 该项目可在 GitHub 上获取，地址为 https://github.com/physicsrob/torchwright_doom/。截至 Hacker News 发布时，它只有 2 个积分和 0 条评论，表明即时参与度较低。提供的内容中未完整描述技术实现细节，但该概念涉及将《毁灭战士》的源代码编译成 LLM 可以执行或模拟的格式。

rss · Hacker News Show HN · Aug 31, 20:22

**背景**: 大语言模型（LLM）通常用于自然语言处理任务，如文本生成、翻译和摘要。将《毁灭战士》这样的游戏编译进 LLM 是一种非常规的方法，可能涉及将游戏的逻辑和状态编码到模型参数中，或使用 LLM 根据输入生成游戏帧。该项目是探索 LLM 创造性及意外应用的更广泛趋势的一部分，例如将其用于代码生成甚至作为计算引擎。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49514445">Show HN: Doom Compiled into an LLM | Hacker News</a></li>

</ul>
</details>

**社区讨论**: 分析时 Hacker News 帖子上没有可用评论，因此没有社区讨论可总结。

**标签**: `#LLM`, `#Doom`, `#AI`, `#compilation`, `#novelty`

---

<a id="item-10"></a>
## [CISA 将两个正在被利用的 PaperCut 漏洞加入 KEV 目录](https://www.cisa.gov/news-events/alerts/2026/08/31/cisa-adds-two-known-exploited-vulnerabilities-catalog) ⭐️ 7.0/10

CISA 已将 PaperCut NG/MF 中两个正在被积极利用的漏洞 CVE-2026-81578 和 CVE-2026-82078 添加到其已知被利用漏洞（KEV）目录中。这两个漏洞分别涉及关键功能缺少身份验证和不安全的反射问题，均构成重大风险。 加入 KEV 目录意味着联邦机构及所有组织应立即优先修补这些漏洞，因为它们正在野外被积极利用。这凸显了基于风险的漏洞管理和快速修复的重要性，以防止潜在的安全入侵。 CVE-2026-81578 是 PaperCut NG/MF 中关键功能缺少身份验证的漏洞，而 CVE-2026-82078 是不安全的反射漏洞。约束操作指令（BOD）26-04 要求 FCEB 机构优先修复 KEV 列表中列出的、在利用后可完全控制资产的公开暴露资产上的漏洞。

rss · CISA Cybersecurity Advisories · Aug 31, 12:00

**背景**: PaperCut NG/MF 是一款广泛使用的打印管理软件，帮助组织管理打印成本和用量。KEV 目录是 CISA 维护的已知被利用漏洞列表，旨在帮助组织优先修补工作。BOD 26-04 为联邦机构制定了漏洞管理要求，强调快速修复高风险漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rapid7.com/db/vulnerabilities/cve-2026-81578/">CVE - 2026 - 81578 : PaperCut... | Rapid7 Vulnerability Database</a></li>
<li><a href="https://www.rapid7.com/db/vulnerabilities/cve-2026-82078/">CVE - 2026 - 82078 : PaperCut... | Rapid7 Vulnerability Database</a></li>
<li><a href="https://www.ihonker.com/thread-35918-1-1.html">CVE - 2026 - 81578 PaperCut...</a></li>

</ul>
</details>

**社区讨论**: 在 iHonker 等论坛的社区讨论中，这些漏洞被认为非常严重，有评论指出未认证即可执行任意代码，且已在野外被利用。大家普遍认为修补工作十分紧迫。

**标签**: `#CISA`, `#vulnerability`, `#exploited`, `#PaperCut`, `#security`

---

<a id="item-11"></a>
## [OpenAI 的 ChatGPT 广告年化收入达 10 亿美元，全球扩展](https://openai.com/index/expanding-access-to-ai-with-chatgpt-ads) ⭐️ 7.0/10

OpenAI 宣布 ChatGPT 广告的年化收入运行率已达到 10 亿美元，并正在全球扩展，以支持免费和负担得起的 AI 访问。 这一里程碑证明了 ChatGPT 广告的强大市场接受度和财务可行性，有助于维持数亿用户的免费和低成本 AI 服务。它标志着通过广告实现 AI 变现的趋势日益增长，影响更广泛的 AI 生态系统。 广告放置在 ChatGPT 的有机回复之后，以保持编辑内容与商业内容之间的分离。OpenAI 强调，广告不会影响 ChatGPT 提供的答案。

rss · OpenAI Blog · Aug 31, 04:00

**背景**: ChatGPT 拥有数亿用户，维持免费和快速的服务需要大量的基础设施投资。广告提供了收入来源以抵消这些成本，使 OpenAI 能够继续提供免费和负担得起的访问。年化收入运行率将近期销售速度推算至全年，表明强劲的增长势头。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://help.openai.com/en/articles/20001047-ads-in-chatgpt">Ads in ChatGPT | OpenAI Help Center</a></li>
<li><a href="https://www.linkedin.com/posts/iamarjungr_chatgpt-is-getting-ads-and-people-have-feelings-activity-7461086989765791745-2mJx">ChatGPT Ads Beta: A New Revenue Model for OpenAI | LinkedIn</a></li>
<li><a href="https://ppc.land/openai-finally-pulls-trigger-on-chatgpt-ads-after-monthslong-delay/">OpenAI finally pulls trigger on ChatGPT ads after monthslong delay</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些用户感到恼火，感叹失去了无广告空间，而另一些人则认为鉴于高昂的计算成本，这是不可避免的。还有人担心广告可能影响答案，但 OpenAI 已表示不会。

**标签**: `#OpenAI`, `#ChatGPT Ads`, `#AI monetization`, `#business milestone`, `#AI access`

---

<a id="item-12"></a>
## [Wrapture：用于追踪和测试的新 Python 库](https://simonwillison.net/2026/Aug/31/introducing-wrapture/) ⭐️ 7.0/10

wrapt 的创建者 Graham Dumpleton 发布了 wrapture，这是一个新的 Python 库，将猴子补丁扩展到追踪和函数覆盖，用于测试和可观测性。它支持 OpenTelemetry，并提供基于配置的机制来为现有项目添加追踪。 Wrapture 为测试和可观测性提供了一种新颖的方法，可能成为 unittest.mock 的替代品，并简化追踪集成。其基于配置的追踪可以降低为现有 Python 项目添加可观测性的门槛，影响开发者和运维团队。 该项目非常年轻，只有几周历史，是 Graham 第一个完全由 AI 代理驱动的大型项目，所有代码和文档都由 AI 助手在他的指导下编写。它提供了基于 TOML 的追踪配置，如示例中的 capture 和 observe 部分所示。

rss · Simon Willison · Aug 31, 23:59

**背景**: 猴子补丁是一种在运行时动态修改代码的技术，常用于测试中替换函数或方法。wrapt 是一个知名的 Python 库，用于包装函数和方法，而 Graham Dumpleton 还以 mod_wsgi 和 New Relic 的 Python 代理而闻名。Wrapture 基于这些思想，结合了测试和追踪功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/GrahamDumpleton/wrapture-instrumentation">GitHub - GrahamDumpleton/ wrapture -instrumentation: Instrumentation...</a></li>

</ul>
</details>

**标签**: `#Python`, `#testing`, `#monkeypatching`, `#tracing`, `#open source`

---