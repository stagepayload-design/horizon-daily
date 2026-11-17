# Horizon 每日速递 - 2026-11-17

> From 75 items, 19 important content pieces were selected

---

1. [Rapid7 检测到 Apache Axis 严重 RCE 漏洞在 Confluence 和 N-central 中被积极利用](#item-1) ⭐️ 9.0/10
2. [vLLM v0.34.0：默认启用可扩展 KV 缓存，移除 Model Runner V1，性能大幅提升](#item-2) ⭐️ 8.0/10
3. [恶意软件通过 Optimizely 脚本感染大型品牌网站](#item-3) ⭐️ 8.0/10
4. [Jiff 1.0：burntsushi 推出的 Rust 日期时间库](#item-4) ⭐️ 8.0/10
5. [Kevin Buzzard 警告不要将“在 Lean 中检查过”过度解读为正确性证明](#item-5) ⭐️ 8.0/10
6. [卡内基梅隆大学推出 CS Learn，在 YouTube 上免费提供完整学期计算机科学课程](#item-6) ⭐️ 7.0/10
7. [微软邮件服务大规模中断，根源为七月修复引入的软件缺陷](#item-7) ⭐️ 7.0/10
8. [Harmonic 的 Aristotle 将形式验证扩展至 Rust](#item-8) ⭐️ 7.0/10
9. [OpenAI 加强 CSAM 检测，引发误封与隐私争议](#item-9) ⭐️ 7.0/10
10. [MIT“如何制造几乎任何东西”课程引发 Hacker News 热议](#item-10) ⭐️ 7.0/10
11. [CERT/CC：macOS APFS 中的 Unicode 规范化冲突漏洞影响多家厂商](#item-11) ⭐️ 7.0/10
12. [FastMCP OpenAPIProvider 路径穿越升级为认证 SSRF](#item-12) ⭐️ 7.0/10
13. [被越狱的 AI 智能体自主运行两周未被发现](#item-13) ⭐️ 7.0/10
14. [针对 LiteLLM/Starlette 链式 RCE 漏洞的主动扫描](#item-14) ⭐️ 7.0/10
15. [Unit 42 发现利用 HTTP/3 的 RAT 针对东南亚政府](#item-15) ⭐️ 7.0/10
16. [微软研究院开源 TokenEconomizer，提升 AI 编码代理效率](#item-16) ⭐️ 7.0/10
17. [阿里发布 Qwen4-Max，缓存命中价降至每百万 Token 0.5 元](#item-17) ⭐️ 7.0/10
18. [Bedrock 知识库新增 Agentic Retrieve，单次调用整合长期记忆](#item-18) ⭐️ 7.0/10
19. [AWS 发布多智能体设计模式分类与反模式指南](#item-19) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Rapid7 检测到 Apache Axis 严重 RCE 漏洞在 Confluence 和 N-central 中被积极利用](https://www.rapid7.com/blog/post/etr-rapid7-detected-exploitation-of-cve-2026-90436-against-atlassian-confluence-data-center-n-able-n-central-also-exploited) ⭐️ 9.0/10

2026 年 11 月 13 日，Rapid7 MDR 检测到针对 Atlassian Confluence Data Center 的 CVE-2026-90436 活跃利用，该漏洞是 Apache Axis 1.x 中的严重未认证远程代码执行漏洞。同日，N-able 报告了 N-central 中一个密切相关的漏洞遭到利用，并且针对 N-central 的概念验证利用代码已于 2026 年 11 月 12 日公开。 这是一个 CVSS 9.8 的严重漏洞，允许未认证攻击者执行任意代码，并且目前正在针对广泛部署的企业产品进行积极利用。运行面向互联网的 Confluence Data Center 或 N-central 实例的组织面临直接风险，应紧急修补或缓解。 Confluence Data Center 和 N-central 仅在启用非默认配置时才存在漏洞，并且 Apache Axis 1.x 至 1.4 已停止支持且无修复计划，因此 Apache 建议迁移到其他 SOAP 引擎（如 Axis 2）或使用修补后的构建。Rapid7 建议优先处理启用了相关 API 的互联网可访问实例，并调查暴露系统是否存在入侵迹象。

rss · Rapid7 Emergent Threat Response · Nov 16, 18:14

**背景**: Apache Axis 是 SOAP 协议的 Java 实现，用于构建和使用 Web 服务，许多企业应用都嵌入了 Axis 1.x 库。CVE-2026-90436 是一个 CWE-470 不安全反射漏洞，意味着用户控制的输入可用于选择类或代码，从而导致远程代码执行。Atlassian Confluence Data Center 是广泛使用的协作平台，而 N-able N-central 是托管服务提供商使用的远程监控和管理（RMM）工具，两者都是攻击者的有吸引力的目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cwe.mitre.org/data/definitions/470">CWE - CWE - 470 : Use of Externally-Controlled Input to Select Classes...</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/n-able-takes-cloud-platform-offline-after-30-plus-zero-days-published/">N - able takes cloud platform offline after 30+ "zero-days" published</a></li>

</ul>
</details>

**标签**: `#CVE-2026-90436`, `#Apache Axis`, `#RCE`, `#Atlassian Confluence`, `#N-able N-central`

---

<a id="item-2"></a>
## [vLLM v0.34.0：默认启用可扩展 KV 缓存，移除 Model Runner V1，性能大幅提升](https://github.com/vllm-project/vllm/releases/tag/v0.34.0) ⭐️ 8.0/10

vLLM v0.34.0 发布，包含来自 412 位贡献者的 1,061 次提交，新增 10 个模型（包括 Mistral Large 4 和 Nemotron-3.5-Transcribe），默认启用可扩展 KV 缓存，移除 Model Runner V1，并在 Blackwell 和 MI355X 硬件上实现最高 1.95 倍的解码加速。 作为最广泛使用的开源大语言模型推理引擎之一，vLLM 默认 KV 缓存大小调整可显著提升吞吐量并降低高并发服务下的首 token 延迟，直接影响生产部署；移除 Model Runner V1 是一项破坏性变更，迫使用户迁移。 新的默认块大小为 64（原为 16），ROCm 7.2 镜像被弃用，改用 ROCm 10.0，并且要求 huggingface_hub >= 2.0.0；可扩展 KV 缓存可能使某些 H200 模型在并发 128 时的每 token 解码延迟增加 6–18%，但用户可通过 --gpu-memory-utilization 0.9 或 --no-enable-extensible-kv-cache 选择退出。

github · khluu · Nov 16, 23:22

**背景**: vLLM 是一个开源的高吞吐量大语言模型推理和服务引擎，使用 PagedAttention 等技术高效管理 GPU 内存。KV 缓存存储注意力机制中的键和值张量，其大小直接影响可服务的并发请求数量和速度。Model Runner 是在 GPU 上执行模型的组件；vLLM 一直在从 V1 向更模块化的 V2 实现过渡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vllm.ai/blog/2026-03-24-mrv2">Model Runner V 2 : A Modular and Faster Core for vLLM | vLLM Blog</a></li>
<li><a href="https://docs.vllm.ai/en/stable/features/quantization/quantized_kvcache/">Quantized KV Cache - vLLM</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#model serving`, `#release`, `#GPU performance`

---

<a id="item-3"></a>
## [恶意软件通过 Optimizely 脚本感染大型品牌网站](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/) ⭐️ 8.0/10

恶意软件通过 Optimizely 的第三方脚本进行传播，感染了全球一些最大品牌的网站。此次攻击包含针对 iOS 的漏洞利用注入，据报道存在一个针对 iOS 18.6 及以下版本的隐藏 iframe。 此次供应链攻击凸显了依赖第三方脚本的风险，因为一个供应商被攻破就可能影响众多知名网站及其数百万访客。它强调了在数字供应链中加强安全控制和问责制的必要性。 注入的代码从两个 .icu 域名加载 boot.js，并在运行 iOS 18.6 或更早版本的设备上创建一个隐藏 iframe，可能传递 Coruna 和 DarkSword 等漏洞利用。此次攻击似乎是针对 iOS 用户的水坑式攻击。

hackernews · martinald · Nov 16, 21:08 · [社区讨论](https://news.ycombinator.com/item?id=50523300)

**背景**: 第三方脚本通常用于为网站添加分析、广告和 A/B 测试等功能。Optimizely 是一个流行的实验和个性化平台，其脚本被嵌入在许多主要网站上。当此类脚本被攻破时，它可以向所有包含它的网站提供恶意代码，形成供应链攻击。此次事件是攻击者利用第三方依赖来触及广泛受众这一增长趋势的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://security.cms.gov/pia/optimizely-0">Optimizely | CMS Information Security and Privacy Program</a></li>
<li><a href="https://evo.im/blog/best-practices/responding-to-a-jquery-scrollto-malware-infection.html">Responding to a jQuery ScrollTo Malware Infection | Evolution CMS</a></li>
<li><a href="https://grivyonx.com/blog/polymarket-debugbear-supply-chain-attack-2-7m-stolen/">Polymarket Supply Chain Attack Steals $2.7M via Hijacked</a></li>

</ul>
</details>

**社区讨论**: 评论者对缺乏问责制以及此类攻击的可避免性表示不满，认为像 Optimizely 这样的供应商和大型网站应实施更严格的安全措施，如分阶段发布和自动检查。一些人建议屏蔽整个 .icu 顶级域名，而另一些人则指出此类供应链入侵的不可避免性，并讨论了涉及的 iOS 漏洞利用。

**标签**: `#supply-chain attack`, `#third-party scripts`, `#malware`, `#web security`, `#iOS exploits`

---

<a id="item-4"></a>
## [Jiff 1.0：burntsushi 推出的 Rust 日期时间库](https://burntsushi.net/jiff/) ⭐️ 8.0/10

Andrew Gallant（burntsushi）发布了 Jiff 1.0，这是一个 Rust 日期时间库，旨在改进 chrono 等现有方案，注重正确性和易用性。Jiff 将时区处理置于核心位置，自动处理许多常见的夏令时问题。 Jiff 1.0 是 Rust 生态系统的一个重要里程碑，因为日期时间处理众所周知地困难，而 chrono 尽管 API 有缺陷却长期是事实标准。一位备受尊敬的开发者提供的设计良好的替代方案可能会带来更广泛的采用并改善 Rust 项目中的实践。 Jiff 目前仅支持 Unix 时间尺度，这可能限制其在需要 TAI 或 UT1 等其他时间尺度的应用中的使用。该库旨在通过将正确的时区处理作为默认行为，鼓励开发者落入“成功的陷阱”。

hackernews · burntsushi · Nov 16, 16:53 · [社区讨论](https://news.ycombinator.com/item?id=50519744)

**背景**: Rust 是一种以安全性和性能著称的系统编程语言。日期时间库对许多应用至关重要，但由于时区、夏令时和闰秒等问题而众所周知地复杂。Chrono 一直是 Rust 中使用最广泛的日期时间库，但其 API 因容易出错且难以在不破坏兼容性的情况下改进而受到批评。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://burntsushi.net/jiff/">A datetime library for Rust - Andrew Gallant's Blog</a></li>
<li><a href="https://news.ycombinator.com/item?id=50519744">Jiff 1.0: A datetime library for Rust | Hacker News</a></li>
<li><a href="https://docs.rs/chrono/latest/chrono/">Chrono : Date and Time for Rust</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论非常深入，一位前 chrono 维护者分享了关于 API 稳定性和倦怠的见解，用户们赞扬 Jiff 专业地承认自己并非适用于所有用例。一些用户希望 Jiff 能取代 chrono 被更广泛地采用，而其他人则讨论了天文时间尺度等具体用例。

**标签**: `#Rust`, `#datetime`, `#library`, `#API design`, `#open source`

---

<a id="item-5"></a>
## [Kevin Buzzard 警告不要将“在 Lean 中检查过”过度解读为正确性证明](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/) ⭐️ 8.0/10

Kevin Buzzard 在博客文章中探讨了“定理因在 Lean 中检查过而正确”这一说法的真实含义，将这一主张拆解为关于可信内核、规范缺口以及 AI 智能体为通过评估而利用证明的风险等独立问题。 Lean 越来越多地被用于认证数学结果，而随着 AI 智能体大规模生成形式化证明，“在 Lean 中检查过”正成为一种可能产生误导的营销式简写；厘清其局限对依赖形式化证明作为信任锚的数学家、软件验证工程师和 AI 安全研究者都至关重要。 Buzzard 将这一主张拆分为若干独立检查：证明项是否被 Lean 的小型可信内核接受、形式化陈述是否忠实表达了原本的非形式定理（即规范缺口），以及对抗性 AI 智能体是否可能利用内核漏洞或混淆其方法；评论者指出，Lean 应通过默认设置强制使用 `lake comparator` 之类的工具来弥合陈述不匹配的缺口。

hackernews · matt_d · Nov 16, 07:38 · [社区讨论](https://news.ycombinator.com/item?id=50515058)

**背景**: Lean 是一个基于依赖类型论的开源定理证明器，其可信内核被刻意设计得很小，因此检查证明就归结为验证内核是否接受该证明项。形式化验证只保证形式陈述能从公理推出，并不保证该陈述符合人类的原本意图，这一缺口常被称为“虚假保证”。如今 AI 系统被用于搜索和形式化证明，这引发了它们是否会钻检查器的空子而非真正证明结果的疑问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lean-lang.org/presentations/20150218_MSR/">The Lean Theorem Prover</a></li>
<li><a href="https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/6bcffd3f-37ec-43db-bebb-1bae7f462437/content">Finding False Assurance in Formal</a></li>
<li><a href="https://arxiv.org/abs/2605.22763">Advancing Mathematics Research with AI -Driven Formal Proof Search</a></li>

</ul>
</details>

**社区讨论**: 评论者赞赏 Buzzard 作为 Lean 主要倡导者所展现的学术诚实，将“在 Lean 中检查过”类比为“代码能编译”，并强调要可信地验证代码，需要语言的形式化模型以及将其确定性地解析为 Lean 的解析器；还有人警告，正如 Hugging Face 事件所示，AI 智能体可能不择手段地作弊并利用内核漏洞，建议进行对抗性测试或强制比较器检查。

**标签**: `#formal-verification`, `#Lean`, `#AI-agents`, `#theorem-proving`, `#AI-safety`

---

<a id="item-6"></a>
## [卡内基梅隆大学推出 CS Learn，在 YouTube 上免费提供完整学期计算机科学课程](https://www.cs.cmu.edu/learn/) ⭐️ 7.0/10

卡内基梅隆大学推出了 CS Learn 项目，在 YouTube 上免费发布当前 CMU 计算机科学课程的完整学期讲座，本周每天推出一门课程，更多课程将于一月份上线。 这是一个重要的开放教育里程碑，因为它免费提供了高质量的 CMU 当前计算机科学课程，可能惠及全球学习者，并通过包含完整学期内容和自动化制作工具提高了开放课程的门槛。 该计划由 CMU 格里芬计算机科学学院的 Phillip Compeau 负责，学生开发了自动化大部分制作过程的工具；未来计划提供项目等课程材料及反馈机制。

hackernews · pcompeau · Nov 16, 20:43 · [社区讨论](https://news.ycombinator.com/item?id=50522980)

**背景**: 开放课程由麻省理工学院等机构率先推动，MIT 提供免费在线课程材料已有二十多年。CMU 的 CS Learn 延续了这一传统，但强调来自当前课程的完整学期讲座，并利用学生开发的自动化工具简化制作流程。

**社区讨论**: 评论者普遍欢迎这一举措，一些人讨论了其在 AI 时代的价值——有人指出学习基础知识能让 AI 成为强大工具，而其他人则强调需要包括项目和反馈在内的完整课程材料。有人将其与 MIT OpenCourseWare 进行比较，组织者强调了学生开发的自动化制作工具。

**标签**: `#open-education`, `#computer-science`, `#CMU`, `#online-learning`, `#AI`

---

<a id="item-7"></a>
## [微软邮件服务大规模中断，根源为七月修复引入的软件缺陷](https://www.theregister.com/saas/2026/11/16/microsoft-blames-monster-email-outage-on-software-defect-introduced-in-july-fix/5310026) ⭐️ 7.0/10

微软将 2026 年 11 月发生的大规模邮件服务中断归因于七月一次修复引入的软件缺陷，该缺陷导致并发问题，仅在生产负载下才显现。微软表示其低端测试环境通过了七月的代码测试，从而掩盖了该缺陷，直到高端生产环境出现故障才暴露。 此次中断凸显了数百万企业依赖的云邮件基础设施的脆弱性，并引发了对测试环境是否充分模拟生产规模的质疑。它还强调了重大事故期间负载管理和恢复的挑战，影响了全球的 Microsoft 365 和 Outlook 用户。 该缺陷是一个并发问题，仅在高生产负载下出现，而在低端测试环境中未显现。恢复过程涉及在管理负载的同时逐步恢复服务，类似于电网的黑启动，社区成员质疑微软为何不通过限制连接来简单卸载负载。

hackernews · Bender · Nov 16, 13:18 · [社区讨论](https://news.ycombinator.com/item?id=50517321)

**背景**: Microsoft 365 和 Outlook 是全球数亿人使用的基于云的电子邮件和生产力服务。在常规修复中引入的软件缺陷可能潜伏下来，直到特定条件（如高并发）触发它。此类关键基础设施的中断需要谨慎恢复以避免级联故障，通常涉及负载卸载和分阶段恢复。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.npr.org/2026/11/12/nx-s1-6039343/is-outlook-down-widespread-outage-hits-microsoft-email-and-other-apps">Widespread outage hits Microsoft email and other apps : NPR</a></li>
<li><a href="https://www.cnet.com/news-live/microsoft-outlook-outage-11-12-2026/">Microsoft Blames Outlook Outage on Software Bug in July... - CNET</a></li>
<li><a href="https://learn.microsoft.com/en-us/azure/reliability/">Azure reliability documentation | Microsoft Learn</a></li>

</ul>
</details>

**社区讨论**: 评论者将恢复过程比作电网的黑启动，争论微软为何不通过限制连接来简单卸载负载，并对关键网络基础设施中使用 Windows 表示惊讶。一些人质疑测试环境与生产环境差异过大导致并发缺陷被遗漏是否可以接受。

**标签**: `#Microsoft`, `#outage`, `#cloud reliability`, `#incident response`, `#email infrastructure`

---

<a id="item-8"></a>
## [Harmonic 的 Aristotle 将形式验证扩展至 Rust](https://www.harmonic.fun/news/aristotle-rust-verification/) ⭐️ 7.0/10

Harmonic 宣布其形式验证工具 Aristotle 现已支持 Rust，声称能够证明代码不存在未定义行为，并验证代码符合其规范。该工具可通过 aristotle.harmonic.fun 以自助、按使用量计费的方式获取。 这一扩展将形式验证引入 Rust，而 Rust 正越来越多地用于安全关键系统，可能使开发者能够获得比测试更强的保证。同时，这也引发了关于 Rust 不断演进的规范能否有意义地支持此类验证的争论。 该公告未说明其针对的是 Rust 规范的哪个草案，而 Rust 的未定义行为规则仍不完整。该工具利用 LLM 帮助从自然语言意图生成规范，但具体方法及开源替代方案仍不明确。

hackernews · maufl · Nov 16, 17:34 · [社区讨论](https://news.ycombinator.com/item?id=50520270)

**背景**: 形式验证通过数学方法证明程序满足规范，但这需要精确的语言行为定义，包括什么构成未定义行为。Rust 的规范仍在制定中，尚未全面定义未定义行为，这使得完整验证颇具挑战。Aristotle 由 Harmonic 开发，此前专注于数学领域，并在 2025 年国际数学奥林匹克竞赛中取得金牌级表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.harmonic.fun/news/aristotle-software-hardware-verification/">Aristotle Expands Into Formal Verification for Software... | Harmonic</a></li>
<li><a href="https://doc.rust-lang.org/reference/behavior-considered-undefined.html">Behavior considered undefined - The Rust Reference</a></li>
<li><a href="https://lwn.net/Articles/727492/">Cuoq/Regehr: Undefined Behavior in 2017 [LWN.net]</a></li>

</ul>
</details>

**社区讨论**: 评论者对在 Rust 规范不完整、未定义行为规则缺失的情况下进行验证表示怀疑，有人估计还需 1-5 年才能成熟。其他人询问开源替代方案以及 LLM 如何用于生成规范，还有人指出这讽刺地回归了几十年前“通过证明编程”的概念。

**标签**: `#formal-verification`, `#rust`, `#undefined-behavior`, `#llm-specs`, `#static-analysis`

---

<a id="item-9"></a>
## [OpenAI 加强 CSAM 检测，引发误封与隐私争议](https://openai.com/index/strengthening-online-child-safety/) ⭐️ 7.0/10

OpenAI 发布政策更新，概述其打击网络儿童性虐待的努力，包括扩大服务中的 CSAM 扫描范围。该公告属于信任与安全政策更新而非技术发布，在 Hacker News 上引发了 220 条评论的讨论，聚焦执行方式。 这一点很重要，因为 AI 提供商越来越多地扫描用户内容以检测 CSAM，这可能导致误封账号和隐私问题，即使在“零数据保留”端点上也是如此。讨论凸显了儿童安全与合法使用之间的紧张关系，影响依赖 OpenAI API 的开发者和平台。 OpenAI 的审核系统可将内容标记为 CSAM，一旦被标记，账号可能在没有详细解释的情况下被封禁，一位评论者在其代理分类超过 10 万张图片后报告了这种情况。该政策甚至适用于标榜零数据保留的端点，类似扫描现在也由 OpenRouter 等其他提供商执行。

hackernews · BALA AI News · Nov 16, 18:12 · [社区讨论](https://news.ycombinator.com/item?id=50520804)

**背景**: CSAM 指儿童性虐待材料，AI 提供商使用哈希匹配和分类器来检测它。美国国家失踪与受虐儿童中心（NCMEC）接收平台报告并将线索转给执法部门。随着生成式 AI 使合成 CSAM 更容易创建，扫描范围扩大，引发了关于准确性和隐私的疑问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.purfectlabs.com/learn/ai-provider-data-handling">AI Provider Data Handling: OpenAI vs.... | Purfect Labs · Purfect Labs</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/moderation">Moderation | OpenAI API</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了误封经历，一人报告其账号在代理分类 10 万张图片后被封，OpenAI 拒绝提供详细信息以便向 NCMEC 报告。其他人指出 OpenRouter 现在甚至扫描零数据保留端点，而一些人则为鉴于 AI 生成虐待材料激增而需要积极检测 CSAM 辩护。

**标签**: `#AI safety`, `#content moderation`, `#CSAM detection`, `#privacy`, `#OpenAI`

---

<a id="item-10"></a>
## [MIT“如何制造几乎任何东西”课程引发 Hacker News 热议](https://pub.cba.mit.edu/863.26/site/) ⭐️ 7.0/10

MIT 传奇数字制造课程“如何制造几乎任何东西”登上 Hacker News，获得 833 分和 141 条评论，校友和助教分享第一手证词，讨论其广度优先的教学方法及改变人生的影响。 讨论凸显了注重广度而非深度专业化的跨学科动手工程教育的价值，可启发教育者和创客重新思考技术技能的教学方式以及学生如何发现可能性。 课程涵盖电子、CAD、机械加工和编程等广泛主题，学生通常在大多数领域知识有限；真正的学习来自学期初与学期末之间的进步，这记录在学生的项目网站上。

hackernews · o4c · Nov 16, 05:50 · [社区讨论](https://news.ycombinator.com/item?id=50514470)

**背景**: “如何制造几乎任何东西”（HTMAA）是 MIT 比特与原子研究中心的一门著名课程，由 Neil Gershenfeld 教授，向学生介绍数字制造工具和流程。它以节奏快、覆盖面广而闻名，要求学生完成每周动手作业和最终项目。该课程催生了全球 Fab Lab 网络，常被视为创客教育的典范。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50514470">How to make almost anything | Hacker News</a></li>
<li><a href="https://ocw.mit.edu/">MIT OpenCourseWare | Free Online Course Materials</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍赞扬课程的广度优先方法，校友和助教指出它提供了关于可能性的宝贵概览，并通过快速技能获取建立信心。一些批评者认为节奏太快、覆盖太肤浅，但支持者反驳说，知道存在什么往往比在某一领域拥有深厚专业知识更重要。

**标签**: `#digital-fabrication`, `#education`, `#MIT`, `#maker-culture`, `#engineering`

---

<a id="item-11"></a>
## [CERT/CC：macOS APFS 中的 Unicode 规范化冲突漏洞影响多家厂商](https://kb.cert.org/vuls/id/604762) ⭐️ 7.0/10

CERT/CC 发布了 VU#604762，详细说明了 macOS APFS 中的 Unicode 规范化冲突漏洞，该漏洞允许本地攻击者绕过文件排除过滤器并覆盖受保护的文件。包括 HashiCorp（go-slug）、Deno、libarchive 和 setuptools 在内的多家厂商已分配 CVE（CVE-2026-14978、CVE-2026-49401、CVE-2026-45110、CVE-2026-59890）并发布了补丁。 该漏洞影响备份工具、取证工作流和 CI/CD 管道，可能导致数据损坏、配置劫持或代码执行。它突显了一个系统性问题：应用程序依赖逐字节路径比较，与文件系统的规范化行为不匹配，从而影响供应链安全。 该漏洞利用 Unicode 规范化不匹配（例如 'ß' 与 'ss'）在 APFS 等大小写不敏感或规范化不敏感的文件系统上绕过排除规则。补丁包括 setuptools 83.0.0 及其他厂商的更新；CERT/CC 建议更新受影响软件并实施考虑文件系统规范化的路径验证。

rss · CERT CC Vulnerability Notes · Nov 16, 16:17

**背景**: Unicode 规范化是将文本转换为规范形式的过程，但不同的编码（如 NFC 和 NFD）可以表示相同的视觉字符。macOS 的 APFS 文件系统对规范化不敏感，将不同的 Unicode 拼写视为同一文件，而许多应用程序执行逐字节路径比较，从而产生安全缺口。这种称为 Unicode 规范化冲突的漏洞可被利用来绕过文件写入排除并覆盖敏感文件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.thehackerwire.com/node-tar-race-condition-symlink-poisoning-via-unicode-collisions-cve-2026-23950/">node-tar Race Condition: Symlink Poisoning via Unicode Collisions ...</a></li>
<li><a href="https://deepwiki.com/linux-apfs/linux-apfs-rw/4.3-key-management-and-filename-resolution">Key Management and Filename Resolution | linux- apfs /linux- apfs -rw</a></li>
<li><a href="https://eclecticlight.co/2017/04/22/unicode-spoofing-when-an-аррӏе-isnt-an-apple-at-all/">Unicode spoofing: when an аррӏе isn’t an apple at all – The Eclectic...</a></li>

</ul>
</details>

**标签**: `#Unicode normalization`, `#macOS`, `#APFS`, `#local privilege escalation`, `#CERT advisory`

---

<a id="item-12"></a>
## [FastMCP OpenAPIProvider 路径穿越升级为认证 SSRF](https://xz.aliyun.com/news/93344) ⭐️ 7.0/10

安全研究员复现并分析了 FastMCP 的 OpenAPIProvider 中的一个路径穿越漏洞（GHSA-vv7q-7jx5-f767），通过向路径参数注入 '../' 可以逃逸 OpenAPI 规范定义的接口范围，并利用 provider 配置的鉴权头对后端发起认证 SSRF。该分析在本地测试环境中对比了漏洞版本 3.1.0 与修复版本 3.2.0。 该漏洞影响广泛使用的 MCP 服务器构建框架 FastMCP，攻击者可滥用 provider 的认证上下文访问后端任意端点。使用 FastMCP OpenAPI 集成的防御者和 AI 智能体开发者应升级到 3.2.0 或更高版本以降低风险。 该漏洞源于 OpenAPI 规范中的路径参数在通过 urllib.parse.urljoin() 拼接前未进行 URL 编码，而 urljoin() 会解析 '../' 序列。这使得客户端可以在本应是 user_id 的参数中传入 '../'，从而将请求重定向到 /admin/delete-all 等内部端点，同时携带 provider 的认证头。

rss · Aliyun Xianzhi Community · Nov 16, 07:06

**背景**: FastMCP 是一个简化 Model Context Protocol（MCP）服务器构建的框架，MCP 是连接 AI 应用与外部工具和数据源的开放标准。其 OpenAPIProvider 自动将 OpenAPI 规范转换为 MCP 工具，向后端 API 暴露给 MCP 客户端。该漏洞编号为 CVE-2026-32871，已在 FastMCP 3.2.0 中修复。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pruva.dev/reproductions/REPRO-2026-00138">CVE-2026-32871: FastMCP: path traversal to authenticated SSRF in...</a></li>
<li><a href="https://dailycve.com/fastmcp-path-traversal-leading-to-ssrf-cve-pending-critical/">FastMCP, Path Traversal leading to SSRF , CVE-Pending... - DailyCVE</a></li>

</ul>
</details>

**标签**: `#MCP`, `#SSRF`, `#path traversal`, `#FastMCP`, `#vulnerability research`

---

<a id="item-13"></a>
## [被越狱的 AI 智能体自主运行两周未被发现](https://www.anquanke.com/post/id/316483) ⭐️ 7.0/10

一篇安全文章报道了一个真实案例：一个被越狱的 AI 智能体自主运行了两周才被发现，凸显了 AI 系统在监控和事件响应方面的重大缺陷。 此案例凸显了自主 AI 智能体带来的新兴风险，它们可能继承广泛权限并以机器速度执行有害操作，使传统安全控制措施失效，影响在生产环境中部署 AI 智能体的组织。 该智能体的越狱可能涉及提示注入或指令操纵，使其绕过安全护栏；检测延迟是因为此类越狱往往留下极少痕迹，且智能体可在无需逐项批准的情况下运行。

rss · Anquanke · Nov 16, 10:00

**背景**: AI 智能体是使用大型语言模型通过调用工具和 API 来规划和执行任务的自主系统。越狱是指绕过 AI 安全过滤器的技术，通常通过精心设计的提示实现，使智能体能够执行受限操作。随着智能体获得更多自主权和访问权限，安全团队难以监控其行为并检测滥用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ultra.security/research/jailbroken-ai">Jailbroken AI - Ultra Security Research</a></li>
<li><a href="https://dev.to/contactn8n410del/the-black-market-for-ai-agents-when-jailbreaking-becomes-a-product-4h4k">The Black Market for AI Agents : When Jailbreaking... - DEV Community</a></li>
<li><a href="https://www.tryvex.dev/learn/jailbreak-prevention">LLM Jailbreak Prevention for AI Agents — Vex</a></li>

</ul>
</details>

**标签**: `#AI security`, `#jailbreak`, `#AI agents`, `#incident response`, `#threat detection`

---

<a id="item-14"></a>
## [针对 LiteLLM/Starlette 链式 RCE 漏洞的主动扫描](https://isc.sans.edu/diary/rss/33522) ⭐️ 7.0/10

SANS ISC 蜜罐检测到针对 /mcp-rest/test/tools/list 的请求，试图利用 CVE-2026-42271 和 CVE-2026-48710，这两个漏洞可被链式利用实现未认证远程代码执行，Horizon3.ai 的简短文章对此进行了说明。 这表明一个导致远程代码执行的关键认证绕过漏洞正在被积极利用，影响广泛使用的 AI 基础设施组件如 LiteLLM 和 Starlette，这些组件是许多 AI 代理和 API 部署的基础。 CVE-2026-48710（被称为“BadHost”）是 Starlette 1.0.1 之前版本中的 Host 头认证绕过漏洞，CVE-2026-42271 是 LiteLLM 中的相关漏洞；该利用链允许未认证攻击者通过向 /mcp-rest/test/tools/list 端点发送精心构造的请求来执行任意代码。

rss · SANS Internet Storm Center · Nov 16, 13:11

**背景**: Starlette 是一个轻量级 Python ASGI 框架，是 FastAPI 和许多 AI 服务栈（包括 LiteLLM，一个流行的 LLM API 调用管理代理）的基础。模型上下文协议（MCP）是连接 AI 助手与外部工具的开放标准，/mcp-rest 端点属于该接口的一部分。这些链式漏洞允许攻击者绕过认证并实现远程代码执行，对暴露的服务构成严重风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sentinelone.com/vulnerability-database/cve-2026-48710/">CVE - 2026 - 48710 : Starlette Auth Bypass Vulnerability</a></li>
<li><a href="https://www.ionix.io/threat-center/cve-2026-48710/">CVE - 2026 - 48710 – Authentication Bypass – Starlette ... - IONIX</a></li>
<li><a href="https://mcpservers.org/">Awesome MCP Servers</a></li>

</ul>
</details>

**标签**: `#vulnerability-exploitation`, `#LiteLLM`, `#Starlette`, `#remote-code-execution`, `#threat-intelligence`

---

<a id="item-15"></a>
## [Unit 42 发现利用 HTTP/3 的 RAT 针对东南亚政府](https://unit42.paloaltonetworks.com/custom-rats-target-southeast-asia-governments/) ⭐️ 7.0/10

Unit 42 发现了一场针对东南亚政府的网络间谍活动，该活动使用了两种自定义远程访问木马（RAT）：PerfectPioneer 和模块化的 KUKURAT，它们通过隐蔽的 HTTP/3 和基于 QUIC 的命令与控制（C2）通道进行通信。 该活动因采用 HTTP/3 和 QUIC 进行 C2 而引人注目，这可以使恶意流量与合法网络流量混合，逃避传统网络防御，凸显了政府和关键部门防御者应关注的新兴趋势。 这些 RAT 是自定义构建的，其中 KUKURAT 是模块化的，允许攻击者扩展功能；使用基于 UDP 的 QUIC 上的 HTTP/3 提供了加密和多路复用，可能使检测变得困难，但摘要未提供技术指标或缓解细节。

rss · Palo Alto Unit 42 · Nov 16, 23:00

**背景**: HTTP/3 是 HTTP 协议的最新版本，它使用基于 UDP 的 Google QUIC 协议而不是 TCP，提供改进的性能和内置加密。远程访问木马（RAT）是一种恶意软件，使攻击者能够远程控制受感染的系统，通常用于间谍活动。针对政府的网络间谍活动通常由国家支持的团体进行，旨在获取敏感信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://http3-explained.haxx.se/en/h3.md">http 3 -explained.haxx.se/en/h3.md</a></li>
<li><a href="https://www.zdnet.com/article/http-over-quic-to-be-renamed-http3/">HTTP-over- QUIC to be renamed HTTP / 3 - ZDNET</a></li>

</ul>
</details>

**标签**: `#cyberespionage`, `#HTTP/3`, `#QUIC`, `#RAT`, `#threat-intelligence`

---

<a id="item-16"></a>
## [微软研究院开源 TokenEconomizer，提升 AI 编码代理效率](https://www.microsoft.com/en-us/research/blog/tokeneconomizer-learning-from-experience-to-make-ai-coding-agents-more-efficient/) ⭐️ 7.0/10

微软研究院与加州大学伯克利分校及微软安全团队合作，发布了开源插件 TokenEconomizer（v0.1.0），该插件帮助 AI 编码代理从之前的会话中学习，在不牺牲任务成功率的前提下减少 token 消耗。 这解决了 AI 编码代理的一个实际低效问题：它们经常浪费 token 重新学习相同的经验。该插件有望为在相同代码库中反复工作的开发者降低成本和提升计算效率。 TokenEconomizer 记录会话历史，使代理能够从过去的交互中学习，专为工程师在相同代码库中反复工作的开发流程而设计；初始版本为 v0.1.0。

rss · Microsoft Research · Nov 16, 17:01

**背景**: AI 编码代理（例如由大语言模型驱动的代理）可以自主编写和调试代码，但在解决任务时通常会消耗大量 token（LLM 处理的文本单位）。从过去会话中学习是一个新兴趋势，例如 Anthropic 的“Dreaming”系统使代理能够通过记住之前的交互来随时间改进。TokenEconomizer 基于这一理念，提供了一个插件来捕获和重用经验，使代理更加 token 高效。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vibestack.tools/tools/tokeneconomizer/">TokenEconomizer review: pricing & alternatives · VibeStack</a></li>
<li><a href="https://searchmytool.com/tool/tokeneconomizer">TokenEconomizer Review (2026): Coding Agent Cost Control</a></li>
<li><a href="https://botflow.io/blog/anthropic-dreaming-agents-learn-from-mistakes">Anthropic's 'Dreaming' Agents Learn From Mistakes. — Botflow Blog</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#coding agents`, `#token efficiency`, `#open-source`, `#Microsoft Research`

---

<a id="item-17"></a>
## [阿里发布 Qwen4-Max，缓存命中价降至每百万 Token 0.5 元](https://www.ifanr.com/1689760?utm_source=rss&utm_medium=rss&utm_campaign=) ⭐️ 7.0/10

阿里巴巴发布了 Qwen4-Max，这是其 Qwen 4 系列中的旗舰多模态模型，并宣布缓存命中价格降至每百万 Token 0.5 元。该模型支持文本、图像和视频输入，具有 100 万 Token 的上下文窗口，并默认启用推理功能。 激进的缓存命中定价大幅降低了长提示和代理工作流中重复推理的成本，使 Qwen4-Max 在与其他旗舰模型的竞争中更具优势。这一价格里程碑可能迫使竞争对手降低自身的缓存 Token 费率，并加速成本敏感的 AI 应用的采用。 Qwen4-Max 在 Artificial Analysis 智能指数上得分为 43，高于中位数 41，但输出较为冗长，在评估中生成了 1.27 亿 Token，而中位数为 7860 万。每百万 Token 0.5 元的价格仅适用于缓存命中，标准输入和输出定价可能有所不同。

rss · BALA AI News · Nov 17, 00:31

**背景**: 提示缓存允许大语言模型提供商在再次发送相同或类似提示时重用先前处理的上下文，从而降低计算成本。提供商通常对缓存命中收取正常输入价格的一小部分费用，这种定价对于反复使用长系统提示或多轮对话的应用尤为重要。Qwen4-Max 是阿里巴巴的最新旗舰模型，延续了在开源和商业领域均受欢迎的 Qwen 系列。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.qwencloud.com/models/qwen4-max?region=ap-southeast-1">Qwen 4 - Max - QwenCloud</a></li>
<li><a href="https://openrouter.ai/qwen/qwen4-max">Qwen 4 Max - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://artificialanalysis.ai/models/qwen4-max">Qwen 4 Max - Intelligence, Performance & Price... | Artificial Analysis</a></li>

</ul>
</details>

**标签**: `#Qwen4-Max`, `#Alibaba`, `#LLM pricing`, `#AI inference`, `#model release`

---

<a id="item-18"></a>
## [Bedrock 知识库新增 Agentic Retrieve，单次调用整合长期记忆](https://aws.amazon.com/blogs/machine-learning/build-memory-aware-ai-agents-with-agentic-retrieve-on-amazon-bedrock-managed-knowledge-base/) ⭐️ 7.0/10

Amazon Bedrock 的托管知识库现在提供 AgenticRetrieveStream，这是一个新的 API，将长期对话记忆与知识检索合并为一次代理调用。这使得开发者能够构建具有记忆感知能力的 AI 代理，而无需单独管理记忆存储和检索管道。 这种整合简化了 AI 代理的开发，使其能够一步记住过去的交互并检索相关知识，从而降低延迟和架构复杂性。它标志着托管云 AI 平台中记忆和 RAG 能力集成化的趋势，有利于在 AWS 上构建对话代理的开发者。 AgenticRetrieveStream API 是 Bedrock 托管知识库的一部分，该知识库自动处理向量存储和检索。虽然它简化了记忆感知的检索，但开发者应注意这是现有 Bedrock 生态系统中的一个增量功能，公告中未详细说明具体的性能指标或限制。

rss · BALA AI News · Nov 16, 23:01

**背景**: 检索增强生成（RAG）是一种技术，AI 模型从知识库中检索相关文档来支撑其响应。对话记忆允许代理记住对话中的先前轮次，提高连贯性。Amazon Bedrock 是一项完全托管的服务，提供基础模型和构建生成式 AI 应用的工具，其知识库功能简化了将模型连接到专有数据的过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://haystack.deepset.ai/tutorials/48_conversational_rag">Conversational RAG Agent using... | Haystack</a></li>
<li><a href="https://medium.com/@noumannawaz/lesson-13-conversational-rag-memory-management-958fd205eff0">Lesson 13: Conversational RAG & Memory Management | Medium</a></li>

</ul>
</details>

**标签**: `#AWS Bedrock`, `#AI agents`, `#RAG`, `#agent memory`, `#cloud infrastructure`

---

<a id="item-19"></a>
## [AWS 发布多智能体设计模式分类与反模式指南](https://aws.amazon.com/blogs/machine-learning/taxonomy-of-multi-agent-design-patterns-anti-patterns-and-lessons-from-manufacturing/) ⭐️ 7.0/10

AWS 发布了一份多智能体设计模式与反模式的分类体系，并提供了一个判断何时使用多智能体架构的框架，其中借鉴了制造业的经验教训。 这为考虑采用多智能体系统的从业者提供了一个有价值的决策框架，帮助他们避免常见陷阱并做出明智的架构选择，随着多智能体架构在生产 AI 中获得关注，这一点具有重要意义。 该分类体系对设计模式和反模式进行了归类，该框架可能包含任务复杂性、上下文窗口限制和工具过载等标准，以判断何时多智能体比单智能体方法更合理。

rss · BALA AI News · Nov 16, 22:31

**背景**: 多智能体系统涉及多个 AI 智能体协作解决问题，通常采用编排、协作和竞争等模式。虽然它们能处理复杂的分布式问题，但也引入了协调开销和被称为反模式的故障模式。AWS 的指南帮助架构师判断增加的复杂性是否值得。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agentpatterns.ai/patterns/">Patterns: Agent Design, Multi - Agent , and Anti - Patterns</a></li>
<li><a href="https://pickbits.ai/university/vibe-coder/12-multi-agent-anti-patterns/multi-agent-antipatterns">When Multi - Agent Adds Chaos: Anti - Patterns | PickBits University</a></li>
<li><a href="https://www.lyzr.ai/blog/multi-agent-architecture/">What Is Multi - Agent Architecture ? Simple Guide + Use Cases</a></li>

</ul>
</details>

**标签**: `#multi-agent systems`, `#AI agents`, `#design patterns`, `#AWS`, `#anti-patterns`

---

