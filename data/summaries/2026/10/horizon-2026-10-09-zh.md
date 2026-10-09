# Horizon 每日速递 - 2026-10-09

> From 95 items, 19 important content pieces were selected

---

1. [OpenAI 撤回三项数学成果](#item-1) ⭐️ 8.0/10
2. [Cisco NX-OS NX-API 漏洞可致未授权 root 远程代码执行](#item-2) ⭐️ 8.0/10
3. [UAT-11985 利用 AI 辅助活动诱饵进行谷歌 AitM 钓鱼攻击](#item-3) ⭐️ 8.0/10
4. [Cisco Talos 分析恶意软件中的 AI 分析规避技术](#item-4) ⭐️ 8.0/10
5. [Cactus 发布 Whistle：仅 16.9 MB 的本地语音转文字模型](#item-5) ⭐️ 7.0/10
6. [htmx 作者认为在 AI 时代学习计算机科学依然值得](#item-6) ⭐️ 7.0/10
7. [Biohub 以 18 亿美元全球承诺扩展虚拟生物学计划](#item-7) ⭐️ 7.0/10
8. [一个提示词、六小时：Opus 5.5 可视化《看不见的城市》全部 55 座城](#item-8) ⭐️ 7.0/10
9. [ICANN 收到 .lan 通用顶级域名申请，引发局域网 DNS 安全担忧](#item-9) ⭐️ 7.0/10
10. [Meta 的 CRAM 为 Linux 带来缓存行级压缩内存](#item-10) ⭐️ 7.0/10
11. [OpenAI 年化收入比此前信号低 200 亿美元](#item-11) ⭐️ 7.0/10
12. [全球范围内 4 小时电池储能安装成本已低于燃气调峰机组](#item-12) ⭐️ 7.0/10
13. [Periodic Labs 创始人探讨 AI 驱动半导体与超导体研发](#item-13) ⭐️ 7.0/10
14. [微软呼吁尽早测试后量子证书生态系统](#item-14) ⭐️ 7.0/10
15. [JPCERT/CC 警告日本国内组织遭未授权访问事件激增](#item-15) ⭐️ 7.0/10
16. [《麻省理工科技评论》专访 AI 设计病毒的创造者](#item-16) ⭐️ 7.0/10
17. [新论文提出智能体可塑性指标，衡量自我改进效率](#item-17) ⭐️ 7.0/10
18. [RoboJEPA：8B 参数多形态机器人世界模型与算力缩放律](#item-18) ⭐️ 7.0/10
19. [AWS 通过 Bedrock AgentCore 推出 AI 智能体按次付费推理](#item-19) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI 撤回三项数学成果](https://twitter.com/danintheory/status/2108065033070789090) ⭐️ 8.0/10

OpenAI 从其公开的数学仓库中撤回了三项数学成果，这一变动记录在 GitHub 上的项目历史文件中。此次撤回引发了社区对 AI 生成证明可靠性及其验证方式的广泛讨论。 这一事件对 AI 生成数学证明的可信度以及用于验证它们的标准提出了重要质疑。它可能影响研究机构展示和审核 AI 辅助成果的方式，进而波及数学家、AI 研究人员以及更广泛的科学界。 此次撤回记录在 OpenAI 数学仓库的 history.md 文件中，社区成员指出部分成果带有 Lean 证书，而另一些仅以自然语言表述。评论者还指出，即便是经过 Lean 验证的证明，也可能形式化出与原本意图不同的命题。

hackernews · sashank_1509 · Oct 8, 07:05 · [社区讨论](https://news.ycombinator.com/item?id=50002650)

**背景**: Lean 是一个证明助手，主要由亚马逊的 Leonardo de Moura 开发，允许数学家以计算机可检查的形式化语言编写证明；其社区驱动的 mathlib 库旨在构建统一的数学形式化体系。像大语言模型这样的 AI 系统可以生成候选证明，但由于其输出具有概率性，通常会借助 Lean 等形式化验证工具将 AI 草稿转化为机器可检查的证明。OpenAI 此前也开展过 AI 生成数学方面的工作，包括能合成证明的 GPT-f 变换器模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>
<li><a href="https://leanprover-community.github.io/">Lean community</a></li>
<li><a href="https://eonsr.com/en/formal-verification-of-ai-generated-proofs-ensuring-logical-integrity-and-trustworthiness-in-complex-mathematical-problem-solving/">Formal verification of AI generated proofs ensuring logical... - EONSR</a></li>

</ul>
</details>

**社区讨论**: 评论者质疑被撤回的三项证明是否正是缺少 Lean 验证的那些，以及为何将已验证的证明与自然语言证明混在一起。一些人认为许多完全由 AI 生成的证明最终会站不住脚，并指出即便是 Lean 证明也可能在编译通过的同时表述出与预期不同的命题；还有人将这一情况类比为带有撤回和版本修复的软件工程实践。

**标签**: `#AI`, `#mathematics`, `#OpenAI`, `#proof verification`, `#Lean`

---

<a id="item-2"></a>
## [Cisco NX-OS NX-API 漏洞可致未授权 root 远程代码执行](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-napi-rce-r2shwu2j?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Cisco%20NX-OS%20Software%20NX-API%20Remote%20Code%20Execution%20Vulnerability%26vs_k=1) ⭐️ 8.0/10

Cisco 披露了 Cisco NX-OS 软件 NX-API 功能中的一个严重漏洞（CVE-2026-76471），未授权的远程攻击者可利用该漏洞以 root 权限执行任意代码，或导致受影响设备出现拒绝服务。Cisco 已发布修复该漏洞的软件更新，且目前没有可用的临时缓解措施。 由于 NX-API 通过 HTTP/HTTPS 暴露在广泛部署的 Nexus 和 MDS 交换机上，核心数据中心网络设备中出现未授权的 root 级远程代码执行漏洞，对网络基础设施构成严重风险。由于没有临时缓解措施，各组织必须尽快打补丁，以防止设备被完全攻陷或发生中断。 该漏洞源于对发送至 NX-API 的数据输入验证不足，攻击者只需发送特制的 HTTP 请求即可利用，可能导致进程崩溃、设备重启以及拒绝服务。Cisco 将该漏洞的安全影响评级定为“严重”，并指出该公告是其 2026 年 10 月 NX-OS 安全加固版本一同发布的一组公告之一。

rss · Cisco Security Advisories · Oct 8, 14:11

**背景**: Cisco NX-OS 是运行在 Cisco Nexus 系列以太网交换机和 MDS 系列光纤通道 SAN 交换机上的网络操作系统。NX-API 是一种可编程接口，通过 HTTP/HTTPS 暴露交换机的管理功能，使自动化工具和脚本能够配置和查询设备。由于该接口可通过网络访问，其输入处理中的缺陷可被攻击者在无需任何凭据的情况下远程利用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cisco.com/c/en/us/td/docs/switches/datacenter/mds9000/sw/8_x/programmability/cisco_mds9000_programmability_guide_8x/nx_api.html">Cisco MDS 9000 Series Programmability Guide, Release 8.x - NX - API ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cisco_NX-OS">Cisco NX - OS - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Cisco`, `#NX-OS`, `#remote code execution`, `#vulnerability`, `#network security`

---

<a id="item-3"></a>
## [UAT-11985 利用 AI 辅助活动诱饵进行谷歌 AitM 钓鱼攻击](https://blog.talosintelligence.com/uat-11985/) ⭐️ 8.0/10

Cisco Talos 发现了一个被追踪为 UAT-11985 的 APT 鱼叉式钓鱼攻击活动，该活动利用 AI 辅助的活动诱饵和实时的谷歌中间人（AitM）钓鱼技术，针对与台湾研究机构有关联的个人。该行动冒充知名的学术和政策机构，并利用合法的公开活动主题以显得可信。 该攻击活动表明攻击者正在将 AI 生成的诱饵与实时 AitM 钓鱼相结合，以绕过多重身份验证（MFA），使传统防御措施效果降低。它凸显了研究和政策机构（尤其是在台湾）面临的不断演变的威胁，并强调需要先进的钓鱼检测和会话令牌保护。 该钓鱼工具包在展示虚假登录页面之前，会收集设备与浏览器信息，如区域设置、用户代理、屏幕尺寸和移动设备状态。AitM 反向代理位于受害者和谷歌真实登录页面之间，剥离 CSP、HSTS 和 X-Frame-Options 等安全标头，以在 MFA 完成后捕获会话令牌。

rss · Cisco Talos Intelligence · Oct 8, 10:01

**背景**: 中间人（AitM）钓鱼是一种中继攻击，攻击者在用户和合法身份提供商之间插入反向代理，使受害者完成正常登录，而攻击者则捕获生成的会话令牌。这种技术绕过了 MFA，因为攻击者窃取的是已认证的会话而非密码。UAT-11985 是 Cisco Talos 追踪的威胁行为者，该活动专门利用 AI 辅助的活动诱饵冒充学术和政策机构，针对台湾研究组织。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.talosintelligence.com/uat-11985/">UAT - 11985 : AI-assisted event lures delivering real-time Google AitM...</a></li>
<li><a href="https://www.zscaler.com/blogs/security-research/aitm-phishing-attack-targeting-enterprise-users-gmail">AITM phishing attack against Enterprise Users | Zscaler</a></li>
<li><a href="https://ironscales.com/glossary/adversary-in-the-middle">What is Adversary - in - the - Middle (AiTM)?</a></li>

</ul>
</details>

**标签**: `#APT`, `#spear-phishing`, `#AitM`, `#AI-assisted`, `#threat intelligence`

---

<a id="item-4"></a>
## [Cisco Talos 分析恶意软件中的 AI 分析规避技术](https://blog.talosintelligence.com/ignore-all-instructions-and-read-this-blog-the-state-of-ai-analysis-evasion-in-malware/) ⭐️ 8.0/10

Cisco Talos 发布了一篇技术深度分析文章，记录了恶意软件作者为阻碍或击败基于 AI 的自动化恶意软件分析系统而正在开发的新兴技术。该博客的标题本身“忽略所有指令并阅读此博客”就是提示注入式规避策略的一个演示。 这项分析处于 AI/ML 与威胁情报的交汇点，是一个新兴且重要的领域，为对抗 AI 防御的对手战术提供了第一手见解。随着越来越多的安全厂商部署 AI 驱动的恶意软件分诊系统，这些规避技术可能削弱自动化检测流程，并迫使防御者重新思考 AI 代理如何将指令与不可信内容区分开来。 已记录的技术包括将自然语言提示嵌入恶意软件代码中，诱使 AI 驱动的安全工具将样本误分类为无害，以及在纯文本注释中放置提示注入载荷，从而迫使基于 AI 的安全分析器进入拒绝行为。这些攻击利用了 AI 代理的一个根本缺陷：无法可靠地将指令与内容区分开来。

rss · Cisco Talos Intelligence · Oct 8, 10:00

**背景**: 基于 AI 的恶意软件分析系统使用机器学习模型，并且越来越多地使用大型语言模型（LLM），来自动检查文件和代码中的恶意行为。提示注入是一类攻击，通过精心构造对抗性文本（通常将恶意指令伪装成良性内容）来操纵 AI 模型的输出。随着这些 AI 分析工具在安全运营中越来越普遍，恶意软件作者已开始专门针对它们调整其战术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aigovernance.com/news/malware-comments-defeated-ai-security-analysis-via-prompt-injection">Malware Comments Defeated AI Security Analysis via Prompt ...</a></li>
<li><a href="https://pyramidledger.com/blog/prompt-injection-now-cuts-both-ways-ai-browsers-and-ai-malware-triage">Prompt Injection Hits AI Browsers and AI Malware Triage</a></li>
<li><a href="https://www.linkedin.com/top-content/technology/cybersecurity-exploit-techniques/advanced-malware-injection-tactics/">Advanced malware injection tactics</a></li>

</ul>
</details>

**标签**: `#malware`, `#AI evasion`, `#threat intelligence`, `#prompt injection`, `#Talos`

---

<a id="item-5"></a>
## [Cactus 发布 Whistle：仅 16.9 MB 的本地语音转文字模型](https://cactuscompute.com/blog/whistle) ⭐️ 7.0/10

Cactus Compute 发布了 Whistle，这是一个仅 16.9 MB 的开源语音识别模型，完全在本地 CPU 上运行，支持七种语言（英语、德语、法语、西班牙语、意大利语、荷兰语和波兰语），首个 token 延迟仅为 11 毫秒。它与 Cactus 的 Needle 模型共用同一套 CPU 引擎，因此单个二进制文件就能把音频片段直接转换为工具调用。 Whistle 表明可用的语音转文字功能可以完全离线运行在低资源硬件上，这对隐私敏感的应用、嵌入式设备以及不适合将音频上传到云端的边缘 AI 场景意义重大。它也反映出模型压缩技术正把语音识别能力带到以往无法承载此类模型的设备上这一更广泛的趋势。 Whistle 可以一次性转写最长 30 秒的 16 kHz 单声道录音，并返回词级时间戳和概率，但目前尚不支持录音过程中的流式输出。Hugging Face 上已出现一个希伯来语微调版本（whistle-he），拥有 5500 万参数、文件大小 24.7 MB，说明该模型在设计上便于微调。

hackernews · gmays · Oct 8, 16:59 · [社区讨论](https://news.ycombinator.com/item?id=50008427)

**背景**: 语音转文字（STT）模型传统上需要数百 MB 到数 GB 的存储空间，且往往运行在云端，这会带来延迟、成本和隐私问题。量化感知训练等模型压缩技术可以在尽量保持精度的同时大幅缩小模型体积，从而实现端侧推理。Cactus Compute 是一家专注于在 CPU 和边缘硬件上高效运行 AI 模型的初创公司，Whistle 是继 Needle 模型之后其在该方向上的最新发布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cactuscompute.com/blog/whistle">Whistle : Speech to Text in 16.9 MB | Cactus</a></li>
<li><a href="https://runtimewire.com/article/cactus-whistle-16-9mb-local-speech-model">Cactus Compute releases a 16.9MB speech model for local CPUs</a></li>
<li><a href="https://huggingface.co/MaorB/whistle-he">MaorB/ whistle -he · Hugging Face</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者对模型体积感到惊叹，但也提出了实际担忧：一位用户在实际测试中发现 Whistle 的准确率远低于 1.7B 的 Qwen ASR 模型（170 条消息中 Whistle 正确识别 70 条，Qwen 为 168 条）；另一位指出缺少流式输出是实时 STT 应用的关键短板；还有一位报告模型在转写电视节目时会卡住并反复输出“Thank you.”。也有人询问它与 M 系列 Mac 上 Parakeet 的对比，还有评论者认为 STT 的真正挑战不在模型大小，而在于处理非典型语音，例如一位中风后口齿不清的 84 岁老人。

**标签**: `#speech-to-text`, `#edge-ai`, `#local-inference`, `#model-compression`, `#hackernews`

---

<a id="item-6"></a>
## [htmx 作者认为在 AI 时代学习计算机科学依然值得](https://htmx.org/essays/yes-and/) ⭐️ 7.0/10

htmx 的创建者发表了一篇题为《Yes, and》的文章，认为尽管 AI 进步迅速，学习计算机科学依然值得，该文在 Hacker News 上引发了 151 分、63 条评论的讨论。作者提到自己的儿子刚开始攻读计算机科学学位，并观察到最有效的“氛围编程者”（vibe coders）本身已经是优秀的开发者。 这篇文章回应了学生和从业者面临的一个紧迫问题：在 AI 工具重塑软件开发之际，传统编程技能是否仍有价值。这场高质量的讨论反映了业界对软件工程职业未来以及正规计算机科学教育价值的普遍焦虑。 评论者反驳了“提示词之于编程如同高级语言之于汇编”的类比，认为编译器是确定性的，而当前的 AI 工具并非如此，因此开发者无法形式化地预测源代码改动会如何影响程序行为。还有人指出，写代码可能是学会读代码的必要途径；一位从业者报告新功能交付速度提升了约 30%，暗示未来可能需要的开发者会更少。

hackernews · Michelangelo11 · Oct 8, 09:48 · [社区讨论](https://news.ycombinator.com/item?id=50003796)

**背景**: htmx 是一个 JavaScript 库，允许开发者通过 HTML 属性直接使用 AJAX、CSS 过渡、WebSockets 和 Server-Sent Events，作为 React 风格前端框架的更简单替代方案而流行起来。其作者在网上名为 recursivedoubts，撰写软件开发相关文章，是 Web 开发社区中颇具影响力的声音。这场讨论属于关于大语言模型如何改变编程实践的更广泛对话的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://htmx.org/">htmx - high power tools for html</a></li>
<li><a href="https://news.ycombinator.com/?ref=dtf.ru">Hacker News</a></li>

</ul>
</details>

**社区讨论**: 讨论情绪褒贬不一：一些评论者赞同作者，认为编程基础仍然有价值；另一些人则持反对意见，认为随着 LLM 的进步，所需的开发者会减少，瓶颈已经变成产生新的创收想法而非编写代码。一个反复出现的主题是对“汇编到高级语言”类比的质疑，因为 AI 工具缺乏编译器的确定性。

**标签**: `#AI`, `#computer-science-education`, `#software-engineering`, `#career-advice`, `#developer-tools`

---

<a id="item-7"></a>
## [Biohub 以 18 亿美元全球承诺扩展虚拟生物学计划](https://biohub.org/news/virtual-biology-initiative-expansion/) ⭐️ 7.0/10

Biohub 宣布了一项 18 亿美元的全球协调承诺，用于扩展虚拟生物学计划，资助 AI 就绪的生物数据、计算能力和新型测量技术。这是迄今为止规模最大的协调投资，旨在为 AI 加速的生物学构建开放数据基础。 这一承诺通过开放大规模标准化生物数据集，可能显著加速 AI 驱动的生物学研究，并有望改变药物发现、细胞模拟和生物信息学。它表明主要资助方正日益将生物数据基础设施视为共享公共产品，而非专有资产。 这 18 亿美元涵盖多个组织的资金、数据、计算和新型测量技术，并建立在 Biohub 此前 5 亿美元虚拟生物学计划启动的基础上。该计划强调生成由可扩展、可复现的生物信息学流程支持的“AI 就绪”数据，而不仅仅是产生更多原始数据。

hackernews · ray__ · Oct 8, 20:46 · [社区讨论](https://news.ycombinator.com/item?id=50011999)

**背景**: 虚拟生物学计划是由 Biohub 主导的项目，旨在为 AI 加速的生物学创建开放数据基础，包括用 AI 模拟人类细胞。“AI 就绪的生物数据”指的是经过标准化、预处理和结构化，可直接用于训练机器学习模型的数据集。Biohub 是由陈·扎克伯格倡议支持的非营利研究组织，其此前 5 亿美元的承诺为这一扩展的全球努力奠定了基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://biohub.org/news/virtual-biology-initiative-expansion/">AI - ready biological data : $1.8 billion global commitment</a></li>
<li><a href="https://biohub.org/news/virtual-biology-initiative/">Virtual Biology Initiative - $500M for AI-powered biology</a></li>
<li><a href="https://kumdi.com/technology/zuckerberg-ai-biology-cellular-simulation-2026/">Zuckerberg’s $500M AI Biology Bet Explained (2026)</a></li>

</ul>
</details>

**社区讨论**: 评论者建议效仿 SETI@Home 模式，利用剩余的 AI 订阅额度进行集体计算，并呼吁举办难度不断升级的生物 AGI 竞赛。还有人指出这与梅奥诊所的数据资助类似，同时一位评论者担忧当前政府正在将原本公开的研究数据集下线。

**标签**: `#AI`, `#biology`, `#data infrastructure`, `#research funding`, `#bioinformatics`

---

<a id="item-8"></a>
## [一个提示词、六小时：Opus 5.5 可视化《看不见的城市》全部 55 座城](https://quesma.com/blog/invisible-cities-one-shot/) ⭐️ 7.0/10

一位作者只给 Anthropic 的 Opus 5.5 一个提示词，让它自主运行六小时，生成了伊塔洛·卡尔维诺《看不见的城市》中全部 55 座城市的可视化作品。该项目发布在 quesma.com 上，并在 Hacker News 上获得 353 分和 179 条评论。 这是对长时程 AI 智能体能力的一次引人注目的展示，说明单个提示词可以驱动数小时的持续生成工作，而非只产出一张图。由此引发的关于 AI 对文学经典的诠释是增值还是减值的争论，触及创造力、作者身份以及读者如何与文本互动等更广泛的问题。 产出是一整套一次性生成的 55 座城市可视化作品，但有评论者发现了文本与图像之间的具体不符之处，例如书中描述一座拥有许多不同桥梁的城市，生成结果却只有大约五座桥，其中三座根本没有连接任何东西。该项目属于创意应用而非技术突破，讨论也质疑这些可视化是否捕捉到了书中更深层的主题。

hackernews · stared · Oct 8, 12:00 · [社区讨论](https://news.ycombinator.com/item?id=50004790)

**背景**: 《看不见的城市》是伊塔洛·卡尔维诺 1972 年的小说，书中马可·波罗向忽必烈汗描述了 55 座奇幻城市，人们普遍将其视为对符号学、语言、记忆与意义的沉思，而非字面意义上的游记。Opus 5.5 是 Anthropic 的 Claude Opus 系列中的新模型，定位于复杂编程、长时程智能体任务和高要求的专业工作。文本到图像的生成式艺术工具能把文字提示转化为图像，而该项目把这一思路扩展为一个可自主工作数小时的智能体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://9to5mac.com/2026/09/22/anthropic-upgrades-claude-with-new-opus-5-5-model-details-here/">Anthropic upgrades Claude with new Opus 5 . 5 model ... - 9to5Mac</a></li>
<li><a href="https://platform.experientiallabs.ai/models/claude-opus-5.5">Model · Experiential</a></li>
<li><a href="https://www.archdaily.com/906742/intricate-illustrations-of-italo-calvinos-invisible-cities">Intricate Illustrations of Italo Calvino 's ' Invisible Cities ' | A...</a></li>

</ul>
</details>

**社区讨论**: 评论情绪褒贬不一：有人称赞这一技术壮举，也有人认为它损害了这本书，一位评论者还警告新读者不要打开该网站，以便自己想象这些城市。其他人指出这本书真正讲的是符号学和语言的局限，还有评论者说结果更像会前十分钟赶出来的漂亮演示，而非打动人的作品。

**标签**: `#AI agents`, `#generative art`, `#LLM applications`, `#creative AI`, `#Hacker News`

---

<a id="item-9"></a>
## [ICANN 收到 .lan 通用顶级域名申请，引发局域网 DNS 安全担忧](https://newgtldprogram-aps.icann.org/applications/CD2694T-T26351/summary) ⭐️ 7.0/10

ICANN 收到了一份针对 .lan 通用顶级域名的申请，而 .lan 这一字符串被 OpenWRT 及其他路由器广泛用于命名局域网内的设备。如果该申请获批并完成委派，.lan 将可在全球范围内被解析，可能导致依赖其进行内部解析的网络出现 DNS 错误路由或劫持。 这一点很重要，因为数以百万计的家庭和企业网络已将 .lan 用作仅限内部使用的域名，若将其公开委派，外部 DNS 应答可能覆盖本地解析，从而暴露内部主机名或重定向流量。这也凸显了更广泛的治理缺口：ICANN 的 gTLD 流程可能与既有的私有用途命名惯例发生冲突。 该申请列于 ICANN 新 gTLD 计划门户网站上，按照当前流程，在字符串确认日（11 月 17 日）之后，公众大约有 104 天的时间提出异议，前提是政府咨询委员会（GAC）没有先行介入。提出异议需要缴纳申请费，最终结果取决于 ICANN 的评估和争议解决程序。

hackernews · mzajc · Oct 8, 15:51 · [社区讨论](https://news.ycombinator.com/item?id=50007353)

**背景**: 通用顶级域名（gTLD）是指 .com、.org、.info 这类不隶属于特定国家的互联网扩展名。负责协调全球域名系统的组织 ICANN 运行着新 gTLD 计划，实体可通过该计划申请运营新的扩展名。像 .lan 这样的名称并未在全球 DNS 中委派，通常只在私有网络内部使用，因此将其公开委派可能造成本地解析与全球解析之间的冲突。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Generic_top-level_domain">Generic top-level domain - Wikipedia</a></li>
<li><a href="https://newgtlds.icann.org/en/applicants/global-support/faqs/faqs-en">Frequently Asked Questions | ICANN New gTLDs</a></li>
<li><a href="https://newgtlds.icann.org/en/applicants">Applicants | ICANN New gTLDs</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论者担心 OpenWRT 等路由器默认分配 .lan 名称，而 dnsmasq 有时会将此类查询泄漏到上游解析器，一旦 .lan 被委派就可能造成危险。其他人讨论了 ICANN 的异议流程和费用，指出企业网络已因第三方拥有的内部域名而遭到入侵，并建议更新 RFC 6762 附录 G。

**标签**: `#DNS`, `#ICANN`, `#network-security`, `#OpenWRT`, `#gTLD`

---

<a id="item-10"></a>
## [Meta 的 CRAM 为 Linux 带来缓存行级压缩内存](https://www.tomshardware.com/software/linux/new-linux-tech-compresses-memory-in-ram-as-ram-for-452x-speedup-new-cram-method-offers-giant-boost-to-compressed-memory-reads) ⭐️ 7.0/10

Meta 的工程师在 10 月 5 日于布拉格举行的 Linux Plumbers Conference 上介绍了 CRAM（Compressed RAM），这是一种新的 Linux 内存压缩方法，利用硬件卸载压缩，使压缩内存可以按缓存行/字节级访问，而不是按页级的块设备方式访问。Tom's Hardware 报道称，该方法对压缩内存读取可带来最高 452 倍的加速，性能接近原生 DRAM。 CRAM 有望显著提升面临内存价格高企和容量需求不断增长的 Linux 系统的内存效率，可能使从服务器到 Steam Deck 等设备都受益。相比 ZRAM 和 zswap 等按页粒度操作、开销更高的现有方案，它代表了一种更先进的方法。 关键创新在于硬件卸载压缩，同时仍允许对压缩内存进行缓存行/字节访问，这与将压缩内存视为块设备的 ZRAM 和 zswap 不同。452 倍这一数字特指压缩内存读取，该项目仍由 Meta 开发中，尚未进入 Linux 主线。

hackernews · danny00 · Oct 8, 13:11 · [社区讨论](https://news.ycombinator.com/item?id=50005424)

**背景**: Linux 中的内存压缩通过将不常用的页面以压缩形式存储在内存中而非交换到磁盘，从而减少内存占用。现有的 zswap 和 ZRAM 等机制按页粒度进行压缩，访问单个字节需要解压整个页面，因而增加延迟。CRAM 旨在借助硬件辅助实现对压缩内存的细粒度访问，从而消除这一瓶颈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/news/Linux-CRAM-Compressed-RAM">Meta Developing Compressed RAM "CRAM" For Linux... - Phoronix</a></li>
<li><a href="https://www.tomshardware.com/software/linux/new-linux-tech-compresses-memory-in-ram-as-ram-for-452x-speedup-new-cram-method-offers-giant-boost-to-compressed-memory-reads">New Linux tech compresses memory in RAM , as... | Tom's Hardware</a></li>
<li><a href="https://www.notebookcheck.net/Steam-Deck-New-memory-technology-promises-major-benefits-but-there-s-a-catch.1419192.0.html">Steam Deck: New memory technology... - Notebookcheck News</a></li>

</ul>
</details>

**社区讨论**: 评论者指出这与 1996 年 Mac 和 Windows 上的 Ram Doubler 有历史相似之处，开玩笑说终于可以“下载更多内存”了，并指出 Phoronix 的文章是更好的来源。一位评论者（cwillu）批评 Tom's Hardware 的文章误解了该项目，指出它主要描述的是 zswap 已有的功能，而非 CRAM 的硬件卸载缓存行级访问。

**标签**: `#Linux`, `#memory-compression`, `#systems-performance`, `#zswap`, `#hardware-offload`

---

<a id="item-11"></a>
## [OpenAI 年化收入比此前信号低 200 亿美元](https://www.cnbc.com/2026/10/08/open-ai-revenue-nvidia-oracle-coreweave.html) ⭐️ 7.0/10

据 CNBC 报道，OpenAI 的年化收入比公司此前对外释放的信号低约 200 亿美元；这一差异据称源于投资者试图将 OpenAI 的数据与 Anthropic 采用不同计算方式得出的年化收入进行直接比较。 这一差距引发了外界对这家估值约 8520 亿美元、并有望进行 IPO 的公司的透明度和估值的质疑，也可能影响投资者对 OpenAI 及其竞争对手的评估。 据报道，差异源于 OpenAI 与 Anthropic 对年化收入的计算方式不同，而 OpenAI 正面临证明其 8520 亿美元估值合理性的压力；该公司已于 6 月秘密提交招股说明书，高管暗示可能在 2027 年上市，Anthropic 也在筹备大规模 IPO。

hackernews · mfiguiere · Oct 8, 16:45 · [社区讨论](https://news.ycombinator.com/item?id=50008187)

**背景**: 年化收入是一种将较短时期的收入按全年推算的指标，这可能使快速增长的公司看起来比其过去 12 个月的实际业绩更大。OpenAI 是 ChatGPT 和 GPT 系列模型的开发商，目前仍为私有公司，因此与上市公司相比，投资者对其财务状况的直接了解有限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.dualentry.com/blog/arr-vs-revenue">ARR vs Revenue : Differences and Reconciliation</a></li>
<li><a href="https://pod.wave.co/podcast/better-offline/monologue-annualized-revenues-are-bs-1ac4984e">Monologue: Annualized Revenues Are BS - Better Offline</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lmLVBQd0VCSG5Cc1ltQjR4cmp5Z0FQAQ?hl=en-GB&gl=GB&ceid=GB:en">Google News - OpenAI valued at $852 billion following new funding...</a></li>

</ul>
</details>

**社区讨论**: 评论者质疑一家估值约 1 万亿美元的公司为何能在几乎没有公开财务信息的情况下运营，有人认为收入误报是严重问题，也有人指出差异源于试图与 Anthropic 的指标对齐；还有多人将此事与围绕 OpenAI 估值和 IPO 时间的持续争论联系起来。

**标签**: `#OpenAI`, `#revenue`, `#AI industry`, `#IPO`, `#valuation`

---

<a id="item-12"></a>
## [全球范围内 4 小时电池储能安装成本已低于燃气调峰机组](https://www.solarpowerworldonline.com/2026/10/4-hour-battery-storage-is-cheaper-to-install-than-gas-turbines-all-across-globe/) ⭐️ 7.0/10

一份新报告声称，4 小时电网级电池储能在全球所有地区的安装成本都已低于燃气调峰机组，并预测未来十年电池成本还将再下降 33%。该结论由 Pickerel 女士总结，引发了关于其建模假设的批判性讨论。 这一转变可能加速电池储能对开式循环燃气调峰机组的替代，重塑电网可靠性规划和电力行业投资决策。对于必须在间歇性发电与稳定容量之间做出平衡的公用事业公司、监管机构和可再生能源开发商而言，这具有重要意义。 报告假设由于需求旺盛，未来十年电池成本将下降 33%，而燃气轮机成本同期将上升，批评者认为这些假设缺乏充分依据。报告还包含延伸至 2060 年的长期预测，例如陆上风电 LCOE 下降 16%，一些评论者认为这难以置信。

hackernews · 01-_- · Oct 8, 16:03 · [社区讨论](https://news.ycombinator.com/item?id=50007519)

**背景**: 电网级电池储能通常指可按固定小时数放电的公用事业规模系统，其中 4 小时系统是目前电网储能的主力。燃气调峰机组是用于满足短时高电力需求的开式循环电厂，传统上一直是提供稳定容量的更便宜选择。该报告比较了这两种技术在各地区的安装成本，但未涉及更长时间储能需求，例如弥合多日季节性缺口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://greenkeyenergy.ca/2025/10/24/the-big-picture-of-energy-storage-home-utility-long-duration/">The Big Picture of Energy Storage : Home, Utility... - greenkeyenergy.ca</a></li>
<li><a href="https://www.crvscience.com/post/milliseconds-matter-the-physical-limits-of-gas-peakers-on-a-renewable-grid">Milliseconds Matter: The Physical Limits of Gas Peakers on...</a></li>
<li><a href="https://solartechonline.com/blog/disadvantages-renewable-energy-2025-comprehensive-guide/">7 Major Disadvantages Of Renewable Energy In 2025</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞文章写作严谨，但批评其基本假设，尤其是电池成本下降 33%和燃气轮机成本上升，有人称这些是“为了得出想要的结论而必须填入模型的数字”。其他人指出 4 小时储能无法弥合阴天无风的冬季一周，并质疑延伸至 2060 年的预测是否合理。

**标签**: `#energy-storage`, `#batteries`, `#renewables`, `#grid-infrastructure`, `#techno-economics`

---

<a id="item-13"></a>
## [Periodic Labs 创始人探讨 AI 驱动半导体与超导体研发](https://www.latent.space/p/periodic) ⭐️ 7.0/10

在 Latent Space 的一期播客中，Periodic Labs 的 Liam Fedus 和 Ekin Dogus Cubuk 探讨了 AI 如何加速半导体和超导体的发现，并推动通往超级智能的进程。该期节目是 Science 与 Engineering 两档播客的交叉特辑，并带有“Forward Deployed Engineering”环节。 AI 驱动的材料发现有望大幅缩短寻找更优半导体和超导体的周期，而这些材料是先进计算、能源和核聚变技术的基础。Fedus（前 OpenAI/Google Brain）和 Cubuk（Google DeepMind 材料科学家）等知名研究者的参与，表明“AI for science”作为前沿应用正获得越来越多的关注。 Periodic Labs 自称是一家 AI 研究与部署公司，致力于构建模型和自主实验室以加速科学发展，总部位于加州门洛帕克。该播客预告提供的技术细节有限，关于半导体或超导体突破的具体主张仍需在完整节目中进一步展开。

rss · Latent Space · Oct 8, 16:27

**背景**: AI 材料发现利用在 Materials Project、AFLOW 等数据库上训练的机器学习模型，在昂贵的实验室合成之前预测有前景的新化合物。超导体——即电阻为零的导电材料——是重点目标，因为更好的超导体可能变革电网、核磁共振设备和聚变反应堆。Periodic Labs 的目标是将此类 AI 模型与可规模化运行实验的自主实验室相结合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://periodic.com/">Periodic Labs</a></li>
<li><a href="https://www.azom.com/article.aspx?ArticleID=25568">How AI and Automation Are Changing Materials Discovery</a></li>
<li><a href="https://spectrum.ieee.org/high-temperature-superconductor-ai-research">Fusion Dreams Drive High-Temperature Superconductor Quest</a></li>

</ul>
</details>

**标签**: `#AI for Science`, `#Materials Discovery`, `#Superintelligence`, `#Frontier Tech`, `#Podcast`

---

<a id="item-14"></a>
## [微软呼吁尽早测试后量子证书生态系统](https://www.microsoft.com/en-us/security/blog/2026/10/08/post-quantum-authentication-why-organizations-should-start-testing-certificate-ecosystems-now/) ⭐️ 7.0/10

微软于 2026 年 10 月 8 日发布安全博客文章，呼吁各组织尽早测试其证书生态系统的后量子认证就绪情况，并重点介绍了其 PQC TLS 试点计划作为具体准备途径。该试点由微软受信任根计划（Trusted Root Program）运营，允许获批的证书颁发机构在封闭测试环境中运行一个 ML-DSA-87 试点根证书。 后量子迁移不仅仅是更换算法，还需要验证证书链、平台和运营流程如何协同工作，因此拖延测试的组织可能在量子威胁成熟时措手不及。微软的试点为证书颁发机构和企业提供了进入根存储、获取后量子 TLS 证书的首个入口，可能影响整个 PKI 生态采用 PQC 的方式。 该试点严格限定在封闭测试环境中：证书不受公开信任，也不用于生产环境，获批的 CA 只能运行一个 ML-DSA-87 试点根证书。DigiCert 也已发布 TLS PQC 试点证书策略与实践声明（v1.0，2026 年 9 月 18 日生效），表明更广泛的 CA 参与。

rss · Microsoft Security Blog · Oct 8, 20:44

**背景**: 后量子密码学（PQC）是指旨在抵御未来量子计算机攻击的密码算法，因为量子计算机预计将破解 RSA 和 ECC 等广泛使用的方案。公钥基础设施（PKI）和 TLS 依赖数字证书来认证服务器并加密流量，因此迁移到 PQC 需要新的证书层级、根计划和运营工具。微软受信任根计划决定哪些根证书被 Windows 和微软服务信任，因此它是任何新证书类型的关键把关者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/TrustedRootProgram/Program-Requirements/blob/main/PQC+Pilot+Program.md">Program -Requirements/ PQC Pilot Program .md at main...</a></li>
<li><a href="https://fixmycert.com/news">PKI News — Certificate Authority, TLS & SSL Certificate... | FixMyCert</a></li>
<li><a href="https://www.microsoft.com/en-us/security/blog/2026/10/08/post-quantum-authentication-why-organizations-should-start-testing-certificate-ecosystems-now/">Post - quantum authentication: Why... | Microsoft Security Blog</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#PKI`, `#TLS`, `#Microsoft`, `#security readiness`

---

<a id="item-15"></a>
## [JPCERT/CC 警告日本国内组织遭未授权访问事件激增](https://www.jpcert.or.jp/at/2026/at260030.html) ⭐️ 7.0/10

JPCERT/CC 发布了编号为 at260030 的官方警告，指出近期日本国内组织接连发生未授权访问事件。该公告面向公众，呼吁国内防御方对显然仍在持续的攻击活动提高警惕。 由于该警告来自日本国家级计算机应急响应团队，对日本企业和公共机构的安全团队具有权威参考价值。它表明这是一波仍在持续的攻击活动，而非例行的单一厂商公告，因此各组织应立即检查自身的检测与响应能力。 所提供的摘要中没有具体的 CVE 编号或入侵指标（IOC），因此防御方应查阅 JPCERT/CC 的完整页面以获取技术细节。该警告被归类为事件响应、威胁情报和未授权访问，说明这是活动层面的警告，而非单一漏洞披露。

rss · JPCERT Alerts · Oct 8, 01:19

**背景**: JPCERT/CC 是日本的国家级计算机安全事件响应团队，负责协调漏洞处理与事件响应，并发布以“at”编号的公开警告。未授权访问指攻击者在未获许可的情况下进入系统或账户，通常是数据窃取或勒索软件攻击的第一步。近期日本的事件印证了这一模式：Nichirei 自 2026 年 7 月 13 日起因系统故障导致冷藏仓库和冷冻食品配送中断，Temairazu 则在 2026 年 9 月确认遭到未授权访问，随后其客户收到与预订相关的可疑信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://smartscope.blog/en/blog/jpcert-domestic-unauthorized-access-alert-api-2026/">Data leaks keep hitting Japan: the 3 attack methods JPCERT / CC ...</a></li>
<li><a href="https://www.linkedin.com/posts/ruby-comm_in-mid-july-2026-japanese-frozen-food-and-activity-7487495781432745984-B3C-">In mid-July 2026 , Japanese frozen-food and logistics giant Nichirei...</a></li>
<li><a href="https://en.traicy.com/posts/2026092940592/">Japan ’s TEMAIRAZU Investigates Unauthorized Access Following...</a></li>

</ul>
</details>

**标签**: `#incident-response`, `#threat-intelligence`, `#unauthorized-access`, `#JPCERT`, `#cybersecurity-advisory`

---

<a id="item-16"></a>
## [《麻省理工科技评论》专访 AI 设计病毒的创造者](https://www.technologyreview.com/2026/10/08/1146224/roundtables-a-conversation-with-the-creator-of-ai-designed-viruses/) ⭐️ 7.0/10

《麻省理工科技评论》发布了一篇圆桌访谈，采访对象是斯坦福大学博士生 Samuel King，他于 2025 年使用生成式 AI 模型提出了微观病毒的基因蓝图。该访谈定于 2026 年 10 月 16 日发布，探讨了 AI 设计生命形式的影响与未来。 这项工作处于生成式 AI 与合成生物学的交叉点，引发了重大的两用和生物安全担忧，因为同样的技术可能被滥用来设计有害病原体。它表明 AI 设计的生物学正从猜测走向实验室现实，对生物防御、研究治理以及更广泛的生命科学生态系统都有影响。 King 的 AI 生成设计尚不属于完全由 AI 生成的生命，但这可能是下一步；针对更大基因组的 AI 设计进行测试仍然困难，因为与某些可以从单条 DNA 链启动的病毒不同，细菌和更复杂的生物无法做到这一点。在实验室测试中，一种 AI 设计病毒的混合物杀死了对天然噬菌体具有抗性的大肠杆菌。

rss · MIT Technology Review AI · Oct 9, 00:08

**背景**: 两用研究关切（DURC）是指生命科学研究中，根据当前认知可以合理预期会提供可被直接滥用于对公共卫生、农业、动物或环境构成威胁的知识或产品。生成式 AI 模型现在能够提出基因序列，而合成生物学的进步使这些序列可以在实验室中合成和测试。这种融合引发了关于如何在保留有益研究的同时治理 AI 设计生物制剂的日益激烈的争论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.technologyreview.com/2025/09/17/1123801/ai-virus-bacteriophage-life/">AI - designed viruses are here and already... | MIT Technology Review</a></li>
<li><a href="https://www.theguardian.com/science/2026/aug/06/safety-fears-as-scientists-make-first-viruses-designed-by-ai">Safety fears as scientists make first viruses designed by AI | Science</a></li>
<li><a href="https://research.louisville.edu/department-environmental-health-and-safety/research-laboratory-safety/biosafety/dual-use-research-concern">Dual Use of Research of Concern | Research & Innovation</a></li>

</ul>
</details>

**标签**: `#AI`, `#biosecurity`, `#generative AI`, `#synthetic biology`, `#dual-use research`

---

<a id="item-17"></a>
## [新论文提出智能体可塑性指标，衡量自我改进效率](https://huggingface.co/papers/2610.08902) ⭐️ 7.0/10

一篇新研究论文（arXiv 2610.08902，发布于 Hugging Face Papers）提出了名为“智能体可塑性”（Agent Plasticity）的指标，旨在量化 AI 智能体将积累的经验转化为未来性能提升的效率。该工作聚焦于如何衡量智能体的自我改进，而不仅仅是展示这种能力。 随着自我改进智能体成为重要研究方向，业界一直缺乏统一标准来比较不同智能体从经验中学习的效率，因此该指标对基准测试和智能体架构设计具有潜在价值。它可能影响研究人员和工程团队在生产环境中评估持续学习智能体的方式。 目前可获取的摘要较为简短，未包含论文的方法论、实验设置或结果，因此该指标的精确定义、跨任务的稳健性，以及是否能避免智能体对自身评估信号过拟合等问题仍待验证。读者应查阅完整论文以了解正式定义与实证结果。

rss · BALA AI News · Oct 8, 21:31

**背景**: 自我改进的 AI 智能体旨在利用自身经验（如生产环境中的执行轨迹或任务反馈）随时间不断提升，这一目标与持续学习密切相关——持续学习要求模型在获得新技能的同时不出现灾难性遗忘。近期相关研究包括基于正则化的 RRSI 方法，以及将智能体外部组件视为可演化状态的 Harness Continual Learning 等框架。衡量改进效率之所以困难，是因为性能提升可能来自提示词、记忆或工具使用等多个方面，而不一定源于底层模型本身。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://enapragma.co/field-notes/self-improving-agents-overfit-their-own-tests-two-september-papers-show-two-brakes">Self - improving AI agents overfit their own tests. Two September...</a></li>
<li><a href="https://www.alphaxiv.org/abs/2608.19013">Harness Continual Learning : Continual Adaptation Beyond... | alphaXiv</a></li>
<li><a href="https://www.taskade.com/wiki/ai/continual-learning">Continual Learning : Why AI Forgets What It Knew (2026) | Taskade AI</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#self-improvement`, `#metrics`, `#continual learning`, `#research paper`

---

<a id="item-18"></a>
## [RoboJEPA：8B 参数多形态机器人世界模型与算力缩放律](https://huggingface.co/papers/2610.10515) ⭐️ 7.0/10

RoboJEPA 是一个拥有 8B 参数的多形态机器人世界模型，提出了算力与想象误差之间的二阶幂律缩放关系，使得模型质量可以在拟合该规律的规模之外进行外推预测。 这是对世界模型与机器人领域的一项实质性技术贡献，因为可预测的想象误差算力缩放律能够在训练大规模系统之前指导资源分配与模型设计决策。 该缩放律具体描述的是模型潜在推演（latent rollouts）的误差，即想象误差，并随算力呈二阶幂律变化；不过目前提供的内容仅为简要摘要，缺少详细的实验验证或代码。

rss · BALA AI News · Oct 8, 21:01

**背景**: JEPA（联合嵌入预测架构）是一种学习预测性表征的方法，可作为世界模型使用，其中 I-JEPA 等变体主要学习观测的有用表征。世界模型让机器人和智能体能够在内部模拟结果，而缩放律则描述模型性能如何随算力提升而改善。RoboJEPA 将这一范式扩展到多形态机器人领域，把想象误差建模为算力的函数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.alphaxiv.org/abs/2610.10515">RoboJEPA: Scaling Robotic Latent World Models | alphaXiv</a></li>
<li><a href="https://www.turingpost.com/p/jepa">JEPA : Joint Embedding Predictive Architecture Explained</a></li>

</ul>
</details>

**标签**: `#world models`, `#robotics`, `#scaling laws`, `#multimodal AI`, `#JEPA`

---

<a id="item-19"></a>
## [AWS 通过 Bedrock AgentCore 推出 AI 智能体按次付费推理](https://aws.amazon.com/blogs/machine-learning/pay-per-inference-for-ai-agents-how-blockrun-and-incarna-use-amazon-bedrock-agentcore-payments/) ⭐️ 7.0/10

AWS 通过 Amazon Bedrock AgentCore 正式推出面向 AI 智能体的按次付费推理功能，BlockRun 与 Incarna 成为首批采用者。Incarna 使用 x402 协议按每次推理调用向 BlockRun 付费，而 AgentCore 在基础设施层面而非模型层面强制执行支出限额。 这为 AI 智能体提供了一种受管理的自主付费方式，可用于支付 API、MCP 和付费内容，免去了为每个客户单独构建支付逻辑的麻烦。它标志着智能体之间货币化的转变，并可能加速整个生态系统对按使用量付费推理的采用。 AgentCore Payments 已于 8 月 18 日正式全面可用，并支持 Coinbase 和 Stripe Privy 钱包进行自主交易。x402 协议将 HTTP 402 Payment Required 状态转化为真实的支付流程，而 BlockRun 作为按使用量付费的路由器通过 x402 提供模型推理服务。

rss · BALA AI News · Oct 8, 19:01

**背景**: Amazon Bedrock AgentCore 是一项用于构建和运行 AI 智能体的托管服务，其支付功能让智能体能够安全、自主地大规模进行交易。x402 协议重新启用了长期闲置的 HTTP 402 状态码，将支付要求直接嵌入 HTTP 响应中，使付费端点无需单独的结账系统即可请求付款。BlockRun 是一个按使用量付费的推理路由器，提供 113 个模型和 100 个工具 API，并兼容 OpenAI 接口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/blogs/machine-learning/pay-per-inference-for-ai-agents-how-blockrun-and-incarna-use-amazon-bedrock-agentcore-payments/">Pay-per- inference for AI agents: How BlockRun and Incarna use...</a></li>
<li><a href="https://docs.useanima.sh/blog/x402-payments">x 402 Payments : How AI Agents Pay for Things on the Internet - Anima</a></li>
<li><a href="https://blockrun.ai/">BlockRun — The routing & payment layer for AI</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#AWS Bedrock`, `#Agent Payments`, `#x402`, `#Inference Infrastructure`

---

