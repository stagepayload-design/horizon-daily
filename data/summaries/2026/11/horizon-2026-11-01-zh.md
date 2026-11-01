# Horizon 每日速递 - 2026-11-01

> From 54 items, 12 important content pieces were selected

---

1. [Linux TCP 释放后重用漏洞 CVE-2026-98432（CVSS 9.8）引发补丁担忧](#item-1) ⭐️ 8.0/10
2. [Jepsen 发现 ParticleDB 1.1.4 存在严重事务异常](#item-2) ⭐️ 8.0/10
3. [Parameter Labs 披露通过预览内容操纵接管 ChatGPT 账户](#item-3) ⭐️ 8.0/10
4. [Karpathy 推出 HackerTube：基于 HN 推荐视频的 YouTube 风格界面](#item-4) ⭐️ 7.0/10
5. [开发者将 NES《魂斗罗》移植到 WebAssembly 并加入在线合作](#item-5) ⭐️ 7.0/10
6. [开发者将神经网络推理引擎塞进 512 字节引导扇区](#item-6) ⭐️ 7.0/10
7. [Anthropic 因用户训练更大模型而封禁账号](#item-7) ⭐️ 7.0/10
8. [GCC 的 switch 语句降级策略详解](#item-8) ⭐️ 7.0/10
9. [VOLTA 信息窃取器利用 LLM 按价值对受害者进行排序](#item-9) ⭐️ 7.0/10
10. [微软分析恶意 Claude Code 品牌 Cursor 扩展及其 SSH 后门](#item-10) ⭐️ 7.0/10
11. [五家科技巨头承诺超 3 万亿美元 AI 基建投入](#item-11) ⭐️ 7.0/10
12. [快手可灵 AI 完成约 198 亿元融资，阿里腾讯百度入股](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Linux TCP 释放后重用漏洞 CVE-2026-98432（CVSS 9.8）引发补丁担忧](https://atlasum.net/blog/cve-2026-98432-linux-ipv4-tcp-uaf) ⭐️ 8.0/10

Linux 内核 IPv4 TCP 栈中的一个严重释放后重用漏洞被追踪为 CVE-2026-98432，CVSS 评分为 9.8，已于 2026 年 10 月 15 日在上游修复，但 Ubuntu 和 RHEL 等主要发行版尚未发布修补后的内核。该漏洞由携带 IPv4 选项的传入 SYN 数据包触发，导致内核在请求套接字上保存这些选项的副本，并随后过早释放内存。 该漏洞影响 Linux 的核心网络组件，而 Linux 支撑着大多数互联网服务器，因此对系统管理员来说是一个高优先级的补丁问题。然而，互联网上的利用受到限制，因为大多数 ISP 路由器会丢弃带有 IP 选项的数据包，且成功利用需要多个 CPU 核心，从而限制了其实际影响。 利用该漏洞需要至少两个 CPU 核心来并发处理数据包，因此单核系统或将数据包处理固定在一个核心上的系统不受影响。根据 Red Hat 的说法，丢弃带有 IP 选项的数据包可以降低风险，但并非完整的缓解措施，且 MPTCP 并非该漏洞的前提条件。

hackernews · oger · Oct 31, 19:16 · [社区讨论](https://news.ycombinator.com/item?id=50319143)

**背景**: 释放后重用（UAF）漏洞发生在程序在内存被释放后继续使用指向该内存的指针时，可能允许攻击者执行任意代码或导致崩溃。CVSS（通用漏洞评分系统）评分范围从 0 到 10，9.8 表示严重级别，通常与无需身份验证的远程可利用漏洞相关。Linux 内核的 TCP/IP 栈是操作系统网络功能的基础部分，其中的漏洞可能影响广泛的设备和服务器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://atlasum.net/blog/cve-2026-98432-linux-ipv4-tcp-uaf">Linux 's October 2026 TCP Use-After-Free: CVE - 2026 - 98432 — Atlas</a></li>
<li><a href="https://getrff.com/blog/cve-2026-98432-linux-tcp-ip-options-block/">CVE - 2026 - 98432 : how to block the Linux TCP bug until Ubuntu and...</a></li>
<li><a href="https://github.com/tc4dy/CVE-2026-98432-PoC-Exploit">GitHub - tc4dy/ CVE - 2026 - 98432 -PoC-Exploit: CVE - 2026 - 98432 ...</a></li>

</ul>
</details>

**社区讨论**: 评论者强调该漏洞是 Linux 特有的，不影响 BSD、macOS 或 Windows，并批评 Ubuntu 和 RHEL 鉴于其服务器市场重点却延迟发布补丁。其他人指出了可利用性的实际限制，例如需要多个 CPU 核心以及 ISP 普遍过滤 IP 选项，还有一些人表示对用于 CVE 警报的 RSS 源感兴趣。

**标签**: `#Linux kernel`, `#use-after-free`, `#CVE-2026-98432`, `#vulnerability`, `#TCP/IP`

---

<a id="item-2"></a>
## [Jepsen 发现 ParticleDB 1.1.4 存在严重事务异常](https://jepsen.io/analyses/particledb-1.1.4) ⭐️ 8.0/10

Jepsen 对 ParticleDB 1.1.4 至 1.1.18.11.rc-22 版本的分析发现，尽管厂商声称完全符合 ACID 并兼容 Postgres，但该数据库频繁出现严重的事务异常，包括已提交写入丢失、内部一致性违规、G1a（中止读）、G1b（中间读）和 P4（丢失更新）。报告还指出，在合作期间没有可用的 TLA+ 规范，这与 ParticleDB 宣传的“形式化证明”状态相矛盾。 这份报告是一份高可信度的一手技术分析，它削弱了 ParticleDB 关于 ACID 合规性和形式化验证的核心声明，可能影响依赖其进行 AI 工作负载的用户，并引发对数据库行业厂商声明可信度的质疑。 Jepsen 测试了多个版本，并观察到在追加工作负载中，成功追加的值会经常从后续对给定键的读取中消失。报告建议用户停止进一步部署 ParticleDB，并迁移到更安全的替代方案。

hackernews · aphyr · Oct 31, 13:39 · [社区讨论](https://news.ycombinator.com/item?id=50316100)

**背景**: Jepsen 是一家知名的独立组织，专门对分布式系统进行严格的安全性和活性测试，经常发现细微的缺陷。ParticleDB 是一个为 AI 工作负载设计的多模型数据库，声称兼容 Postgres 并提供完整的 ACID 保证。ACID 是一组属性（原子性、一致性、隔离性、持久性），用于确保可靠的事务处理。TLA+ 是一种形式化规范语言，用于验证系统设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jepsen.io/analyses/particledb-1.1.4">Jepsen: ParticleDB 1.1.4</a></li>
<li><a href="https://news.ycombinator.com/item?id=50316100">Jepsen: ParticleDB 1.1.4 | Hacker News</a></li>
<li><a href="https://particledb.ai/">ParticleDB | The database for AI agents</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（99 条评论）包括一位用户的第一手经历，该用户之前与 Jepsen 合作过并获得了积极体验，与此报告描述的“小丑表演”形成对比。评论者强调了调查结果的严重性，例如缺失的 TLA+ 证明和停止部署的建议，并讨论了“构造正确”与“构造错误”的软件之间的二分法。

**标签**: `#databases`, `#distributed-systems`, `#jepsen`, `#transactional-consistency`, `#formal-verification`

---

<a id="item-3"></a>
## [Parameter Labs 披露通过预览内容操纵接管 ChatGPT 账户](https://www.parameter.ai/labs/we-found-a-gap-at-openai) ⭐️ 8.0/10

Parameter Labs 详细描述了如何通过操纵预览内容并利用 artifacts/Canvas 功能链式接管 ChatGPT 账户。OpenAI 确认两个前端均拒绝了所报告的消息，修复了该问题，并授予了 5000 美元的漏洞赏金。 ChatGPT 前端的这一账户接管漏洞凸显了渲染富内容的 AI 聊天界面中的安全风险，可能影响数百万用户。较低的赏金可能会阻碍研究人员报告类似漏洞，引发了对 OpenAI 漏洞赏金激励是否充足的担忧。 该漏洞利用需要用户点击链接，限制了攻击面，OpenAI 表示两个前端均拒绝了所报告的消息。赏金总额为 5000 美元，社区成员批评称鉴于账户接管的严重性，这一金额过低。

hackernews · armcat · Oct 31, 10:30 · [社区讨论](https://news.ycombinator.com/item?id=50314699)

**背景**: ChatGPT 的 artifacts（原 Canvas）功能允许模型在聊天界面内生成并渲染代码、网页等交互式内容。预览内容操纵涉及构造消息，使其在渲染时能够绕过安全控制并执行恶意操作。OpenAI 的漏洞赏金计划奖励负责任地披露漏洞的研究人员，奖励金额根据严重程度而有所不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/bug-bounty-program/">Announcing OpenAI ’s Bug Bounty Program | OpenAI</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍批评 5000 美元的赏金对于账户接管漏洞来说太低，认为这可能会阻碍未来的报告。一些人还提到了相关的桌面应用文件系统暴露问题，并认为文章写作风格不清晰，尤其是对 JSONP 的解释。

**标签**: `#account-takeover`, `#OpenAI`, `#web-security`, `#bug-bounty`, `#vulnerability-disclosure`

---

<a id="item-4"></a>
## [Karpathy 推出 HackerTube：基于 HN 推荐视频的 YouTube 风格界面](https://karpathy.bearblog.dev/hacker-tube/) ⭐️ 7.0/10

Andrej Karpathy 构建了 HackerTube，一个 YouTube 风格的网页界面，展示了从 2007 年以来 39,834 条 Hacker News 评论中挖掘出的 6,454 个视频。该项目以可复刻的数据集形式发布，并附有面向 AI 代理的文档，允许任何人重用数据并构建自己的界面。 该项目展示了一种新颖的内容策展方法，利用 Hacker News 的社区驱动推荐，提供了不同于 engagement 优化算法的替代方案。它还凸显了发布数据集时附带面向代理的文档这一增长趋势，使 AI 代理能够轻松复刻和定制应用。 该数据集涵盖了自 2007 年以来在 HN 评论中推荐的视频，从 39,834 条评论中总计得到 6,454 个独特视频。发布内容包含专门为 AI 代理编写的 DATA.md 文件，详细说明了文件结构、注意事项和示例记录，以及根据需要获取 YouTube 元数据的说明。

hackernews · karpathy · Oct 31, 19:56 · [社区讨论](https://news.ycombinator.com/item?id=50319510)

**背景**: Hacker News (HN) 是一个流行的科技新闻聚合器，用户在其中分享和讨论链接。Andrej Karpathy 是一位知名的 AI 研究者和教育家，经常分享实验性项目。面向代理的文档是指为 AI 代理（如 Claude Code）设计的文档，以便它们理解和操作代码或数据，通常包括结构化的解释和示例。

**社区讨论**: 评论者称赞了与 YouTube 的参与度驱动信息流相比令人耳目一新的体验，一些人指出他们更看重偶然发现和拓宽视野的内容，而非个性化推荐。其他人赞赏了可复刻、对代理友好的发布方式，还有少数人轻松地调侃了 cookie 横幅和对长期观点的验证。

**标签**: `#data-mining`, `#recommendation-systems`, `#Hacker News`, `#open-source`, `#AI-agents`

---

<a id="item-5"></a>
## [开发者将 NES《魂斗罗》移植到 WebAssembly 并加入在线合作](https://epoyraz.github.io/nes-contra-us/) ⭐️ 7.0/10

一位开发者将 1987 年的 NES 游戏《魂斗罗》从 6502 汇编语言移植到 C 语言，再编译为 WebAssembly，并加入了在线合作多人模式。移植过程使用 Mesen 模拟器与原版逐帧比对验证。 这展示了一条实用的转编译流程，用于保存和现代化经典游戏，使其能在浏览器中运行并添加在线合作等新功能。它表明细致的逆向工程可以让传统软件触达新的受众。 该移植基于 vermiceli 对《魂斗罗》的注释反汇编，源代码已在 GitHub 上公开。游戏逻辑逐例程翻译，逐帧比对确保了准确性，但目前缺少音频。

hackernews · tevlon · Oct 31, 19:18 · [社区讨论](https://news.ycombinator.com/item?id=50319169)

**背景**: NES（任天堂娱乐系统）使用 6502 CPU，像《魂斗罗》这样的游戏是用 6502 汇编语言编写的。转编译是将代码从一种语言转换为另一种语言，这里从汇编转到 C 再转到 WebAssembly，从而能在现代浏览器中运行。Mesen 是一款高精度模拟器，被用作验证移植行为的参考。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://www.mesen.ca/">Mesen is a multi-system emulator for Windows, Linux and macOS.</a></li>
<li><a href="https://skilldrick.github.io/easy6502/">Easy 6502 by skilldrick</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞了技术成就和合作功能，但多人询问缺失的音频以及添加音乐的可能性。其他人讨论了转编译方法以及替换更高分辨率资源的可行性。

**标签**: `#retro-gaming`, `#webassembly`, `#transcompilation`, `#emulation`, `#game-development`

---

<a id="item-6"></a>
## [开发者将神经网络推理引擎塞进 512 字节引导扇区](https://github.com/kerlenton/bootgpt) ⭐️ 7.0/10

开发者创建了 bootgpt，一个完全适配 512 字节 MBR 引导扇区的字符级神经网络推理引擎，可无限生成虚假的 Linux 启动消息。项目包含一个与汇编输出逐位精确匹配的训练脚本，开发者还记录了调试一个隐蔽的 idiv 寄存器覆盖 bug 的过程。 该项目展示了极端的约束工程，通过用神经网络替代传统程序，突破了单个引导扇区所能实现的极限。它突出了创造性的底层黑客技术，并证明在极其微小的环境中进行有意义的机器学习推理是可能的。 推理引擎为 510 字节，权重、词汇表和字符串存储在后续扇区中。网络是一个单隐藏层的 int8 模型，训练脚本精确复现了汇编代码的整数运算，确保与 QEMU 输出逐字符一致。一个值得注意的 bug 涉及 idiv 覆盖 edx，而 edx 存储了偏置指针，导致只有第一个神经元被正确偏置。

hackernews · kerlenton · Oct 31, 12:58 · [社区讨论](https://news.ycombinator.com/item?id=50315782)

**背景**: 引导扇区是磁盘的前 512 字节，计算机启动时由 BIOS 加载并执行。引导扇区演示场景涉及在这个极小限制内编写国际象棋或 BASIC 游戏等程序。dmesg 是一个显示内核启动消息的 Linux 命令，该项目使用神经网络而非实际硬件来模拟这些消息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.d-robotics.cc/rdk_x_doc/Appendix/linux-command-manual/cmd_dmesg">dmesg | RDK X3/X5 DOC</a></li>
<li><a href="https://qastack.cn/unix/35851/whats-the-difference-of-dmesg-output-and-var-log-messages">dmesg 输出和/ var / log / messages有什么区别</a></li>
<li><a href="https://diqi.org/c/dmesg.html">dmesg 命令，Linux dmesg 命令详解：显示Linux系统启动信息 - Linux...</a></li>

</ul>
</details>

**社区讨论**: 社区赞赏该项目为“愚蠢的工程”，展示了人类的创造力以及在没有经济或实用理由的情况下构建事物的乐趣。评论者认为这类项目提醒人们，并非所有事情都需要关乎价值或实用性。

**标签**: `#boot-sector`, `#neural-network`, `#assembly`, `#embedded`, `#creative-coding`

---

<a id="item-7"></a>
## [Anthropic 因用户训练更大模型而封禁账号](https://twitter.com/jiahaoshao1/status/2116475922190922088) ⭐️ 7.0/10

Hacker News 上的一则讨论指出，有报道称 Anthropic 封禁了使用 Claude 训练更大模型的用户，社区成员就这一政策、地理封锁以及开源替代方案的必要性展开了辩论。 这一事件凸显了 AI 公司的服务条款与用户对灵活模型开发的需求之间的紧张关系，可能加速人们对开放权重替代方案以及标准化、可移植 AI 生态的兴趣。 该说法源自一条推文，缺乏一手证据，且未得到 Anthropic 官方确认；评论者指出该用户位于香港，而 Claude 在当地被地理封锁，因此使用 VPN 加上训练行为很可能触发了 Anthropic 的分类器。

hackernews · pretext · Oct 31, 19:39 · [社区讨论](https://news.ycombinator.com/item?id=50319358)

**背景**: Anthropic 开发了 Claude 系列 AI 助手，并执行服务条款，禁止使用其模型训练竞争性或更大的模型。地理封锁限制在某些地区（如香港）访问 Claude，当地用户常依赖 VPN。这场辩论反映了业界对透明度、数据来源以及 AI 生态开放性的更广泛担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.ai/">Sign in to Claude , Anthropic 's AI assistant for problem solvers.</a></li>
<li><a href="https://www.anthropic.com/constitution">Claude ’s Constitution \ Anthropic</a></li>
<li><a href="https://openalternative.co/alternatives/claude">10+ Best Open Source Claude Alternatives in 2026</a></li>

</ul>
</details>

**社区讨论**: 评论者对 Anthropic 固执己见的政策表示担忧，一些人敦促专业人士培养开源替代方案和后备方案。其他人分享了 Claude 以道德为由拒绝任务的轶事，而一位评论者认为使用 VPN 加上训练活动很可能触发了封禁。还有人呼吁对训练数据和方法实行强制性透明，类似于食品成分标签。

**标签**: `#AI policy`, `#Anthropic`, `#model training`, `#terms of service`, `#community discussion`

---

<a id="item-8"></a>
## [GCC 的 switch 语句降级策略详解](https://xoranth.net/gcc-switch/) ⭐️ 7.0/10

一篇技术文章详细介绍了 GCC 如何将 switch 语句降级为跳转表、决策树或混合形式，同时 Hacker News 上的讨论指出了性能权衡以及缺失的完美哈希优化。 理解这些降级策略有助于编译器和系统工程师分析生成代码的性能，并在性能关键代码中对 switch 的使用做出明智选择。 GCC 即使在跳转表看似合适时也可能选择决策树，并且目前没有为大型稀疏 switch 表实现完美哈希，而一些开发者已手动实现了该功能。

hackernews · signa11 · Oct 31, 08:02 · [社区讨论](https://news.ycombinator.com/item?id=50314085)

**背景**: switch 语句是一种多路分支，编译器可以用多种方式实现。跳转表（分支表）通过索引代码地址数组实现常数时间分派，而决策树则使用一系列比较。GCC 和其他编译器根据 case 的密度和其他启发式规则在这些方法中进行选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50314085">Switch Lowering in GCC | Hacker News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Switch_statement">Switch statement - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了实际经验：有人发现 .NET 中决策树比跳转表更快，另一人指出 LLVM 编译大型 switch 很慢，还有几人批评 GCC 和 Clang 缺乏针对稀疏 switch 的完美哈希优化，其中一人提到十年前被拒绝的 LLVM 补丁。

**标签**: `#compilers`, `#GCC`, `#code-generation`, `#optimization`, `#performance`

---

<a id="item-9"></a>
## [VOLTA 信息窃取器利用 LLM 按价值对受害者进行排序](https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer/) ⭐️ 7.0/10

Cisco Talos 报告称，一种名为“VOLTA-AUTODOXER”的新型自删除 Windows 信息窃取器在窃取凭据、会话和加密货币钱包之前，利用 LLM 驱动的阶段对受害者进行画像并对其最有价值的资产进行排序。 这标志着信息窃取器技术的显著演变，攻击者利用 AI 优先攻击高价值目标，可能提高凭据盗窃和金融欺诈的效率与影响。 该恶意软件具有自删除功能，并通过 CAIRN 研究项目被发现；它在盗窃后的工作流程中加入了基于 LLM 的受害者画像，但摘要中未详细说明具体的 LLM 模型或技术。

hackernews · Cisco Talos Intelligence · Oct 31, 14:29 · [社区讨论](https://news.ycombinator.com/item?id=50316531)

**背景**: 信息窃取器是一种恶意软件，旨在从受感染的机器上收集登录凭据、浏览器会话和加密货币钱包等敏感数据。Cisco Talos 是一家知名的威胁情报团队，研究和报告新兴网络威胁。LLM（大语言模型）是在大量文本数据上训练的 AI 系统，正日益被攻击者滥用于自动化画像等任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer/">Appraisal by AI: Model-driven victim prioritization in the VOLTA...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cisco_Talos">Cisco Talos - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对自动下载工具和频繁代码变更带来的供应链风险的担忧，将其比作早期互联网病毒风暴，并认为防御性提示注入可能成为未来的军备竞赛。一些人开玩笑说贫穷反而成了防御手段，另一些人则呼吁出现“罗宾汉”式恶意软件。

**标签**: `#malware`, `#LLM`, `#infostealer`, `#threat-intelligence`, `#supply-chain`

---

<a id="item-10"></a>
## [微软分析恶意 Claude Code 品牌 Cursor 扩展及其 SSH 后门](https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/) ⭐️ 7.0/10

微软安全研究团队发布了一份分析报告，详细剖析了一个伪装成 Claude Code 的恶意 Cursor 扩展，该扩展会在开发者机器上安装持久化 SSH 后门，并提供了检测与修复指南。报告指出，这个被植入木马的扩展通过授权 SSH 密钥和反向 SSH 隧道实现持久化远程访问。 这一事件凸显了通过开发者工具扩展进行供应链攻击的风险日益加剧，直接威胁到人们日益信任 Cursor 和 Claude Code 等工具的 AI 辅助开发环境。使用此类扩展的开发者和组织可能面临对源代码和内部系统的持久化未授权访问。 恶意代码被前置插入正常的扩展包中，并在合法初始化之前执行，其命令与控制基础设施使用 IP 地址 134.209.82.225，通过 SSH 和 HTTP 端口 8099 通信。报告指出，该扩展是通过一个经过验证的 Cursor 账户分发的，但目前尚不清楚攻击者是如何获取该账户访问权限的。

rss · Microsoft Security Blog · Oct 31, 01:02

**背景**: Cursor 是一款基于 VS Code 的 AI 驱动集成开发环境，而 Claude Code 是 Anthropic 推出的 AI 编程助手，可以作为扩展安装在 VS Code、Cursor 及类似编辑器中。通过 IDE 扩展进行的供应链攻击之所以有效，是因为开发者通常带着隐含的信任从市场安装工具，而被攻陷的扩展可以以开发者权限执行任意代码。持久化 SSH 后门使攻击者能够在重启后仍保持访问权限，并逃避常规检测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opensourcemalware.com/blog/trojanized-claude-code-extension-plants-persistent-ssh-backdoor">Trojanized Claude Code Extension Plants an SSH Backdoor</a></li>
<li><a href="https://arstechnica.com/security/2026/10/anthropic-vs-code-extension-on-cursor-backdoored-for-nearly-12-hours/">Anthropic VS code extension on Cursor backdoored... - Ars Technica</a></li>
<li><a href="https://www.webasha.com/blog/what-is-the-real-risk-behind-malicious-vscode-extensions-like-the-cursor-ide-incident">What is the real risk behind malicious VSCode extensions like the...</a></li>

</ul>
</details>

**标签**: `#supply-chain-attack`, `#malicious-extension`, `#SSH-backdoor`, `#AI-coding-tools`, `#threat-intelligence`

---

<a id="item-11"></a>
## [五家科技巨头承诺超 3 万亿美元 AI 基建投入](https://www.ithome.com/0/1020/632.htm) ⭐️ 7.0/10

微软、谷歌、甲骨文等五家科技巨头共同披露了未来数年超过 3 万亿美元的 AI 基础设施投入承诺，其中部分为长期合同。 这一巨额资本支出标志着 AI 算力建设的范式转变，凸显了超大规模云厂商争相锁定 GPU 产能和数据中心资源的竞赛，将深刻影响未来数年的竞争格局和供应链。 这些承诺包含长期合同，但简报未披露各公司的具体分配、时间表或原始文件，因此尚不清楚其中多少具有约束力、多少是意向性的。

rss · BALA AI News · Oct 31, 19:30

**背景**: 超大规模云厂商是指微软、谷歌、甲骨文等运营大型数据中心、在全球范围提供弹性计算服务的企业。随着 AI 工作负载需要庞大的 GPU 集群，这些公司正大举投资基础设施以支持训练和推理，并常通过长期合同锁定供应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hyperscale_computing">Hyperscale computing - Wikipedia</a></li>
<li><a href="https://www.thundercompute.com/blog/what-is-a-hyperscaler">What Is a Hyperscaler ? The Big Clouds Behind AI Infrastructure (2026)</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#capex`, `#hyperscalers`, `#industry news`, `#compute`

---

<a id="item-12"></a>
## [快手可灵 AI 完成约 198 亿元融资，阿里腾讯百度入股](http://www.techweb.com.cn/it/2026-10-31/2980160.shtml) ⭐️ 7.0/10

快手旗下可灵 AI 视频生成业务已完成约 198 亿元人民币的融资交割，投资方包括阿里巴巴、腾讯和百度。该消息在简短公告中得到确认，这是中国生成式 AI 视频领域规模最大的融资之一。 中国三大互联网巨头同时入股，表明对可灵作为国内领先视频生成模型的战略信心，可能加速行业围绕少数主导平台整合。此次融资也为可灵提供算力扩张资源，并为其潜在 IPO 前的国际竞争增添筹码。 据此前报道，本轮融资对可灵的估值约为 180 亿美元，而可灵目前仍占快手总营收不到 3%。此次简短公告未披露技术细节或各投资方的具体持股比例。

rss · BALA AI News · Oct 31, 07:01

**背景**: 可灵是快手推出的生成式 AI 视频模型，可根据文本提示生成富有想象力的图像和视频，已成为中国最受关注的国际视频生成工具的替代品之一。快手此前一直在为这一 AI 分拆业务寻找外部投资者，包括与 General Atlantic 洽谈，并为潜在的香港 IPO 做准备。阿里巴巴、腾讯和百度的入股，反映了中国科技巨头在基础模型和生成式媒体领域争相布局的更大趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-06-17/kuaishou-kling-ai-seeks-2-billion-at-18-billion-value-from-general-atlantic">Kuaishou Kling AI Seeks $2 Billion at $18 Billion Value... - Bloomberg</a></li>
<li><a href="https://cryptobriefing.com/kuaishou-kling-ai-video-model-hong-kong-ipo/">Kuaishou Technology's AI spinoff unveils Kling 4.0 video model...</a></li>

</ul>
</details>

**标签**: `#AI funding`, `#generative video`, `#Kling AI`, `#China tech`, `#industry news`

---

