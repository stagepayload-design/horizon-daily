# Horizon 每日速递 - 2026-06-12

> From 50 items, 16 important content pieces were selected

---

1. [AMD 用 CRC32 修补 RCE 漏洞，修复无效](#item-1) ⭐️ 9.0/10
2. [Haskell TLS 库未强制执行 X.509 名称约束](#item-2) ⭐️ 9.0/10
3. [Homebrew 6.0.0 发布，引入 Tap 信任机制和 Linux 沙箱](#item-3) ⭐️ 8.0/10
4. [寻求人类关注需付出人类努力](#item-4) ⭐️ 8.0/10
5. [小米开源 AI 编程助手 MiMo Code](#item-5) ⭐️ 8.0/10
6. [Anthropic 为 Claude Code 隐形护栏道歉](#item-6) ⭐️ 8.0/10
7. [请愿撤回加拿大 C-22 法案](#item-7) ⭐️ 8.0/10
8. [Claude Fable 5：编码任务表现中等，超时率高](#item-8) ⭐️ 8.0/10
9. [代码行数：一个有缺陷的 AI 生产力指标](#item-9) ⭐️ 8.0/10
10. [CISA 将正在被利用的 Ivanti Sentry 漏洞加入 KEV 目录](#item-10) ⭐️ 8.0/10
11. [Cisco SD-WAN 权限提升漏洞](#item-11) ⭐️ 8.0/10
12. [DeltaDB 捕获 Git 提交之间的每一次编辑](#item-12) ⭐️ 7.0/10
13. [Waymo 推出每月 30 美元的订阅服务 Waymo Premier](#item-13) ⭐️ 7.0/10
14. [LLM 在核战争模拟中展现出不同个性](#item-14) ⭐️ 7.0/10
15. [Boo：基于 libghostty 的现代 screen 风格终端复用器](#item-15) ⭐️ 7.0/10
16. [Datasette 1.0a33 扩展 JSON API 的 `?_extra=` 模式](#item-16) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [AMD 用 CRC32 修补 RCE 漏洞，修复无效](https://mrbruh.com/amd2/) ⭐️ 9.0/10

AMD 用一个非加密的 CRC32 检查替换了远程代码执行漏洞，而非正确的加密签名，导致系统在 Web 服务器被攻破时极易被利用。 这导致 AMD 用户在 Web 服务器被攻破时极易被入侵，削弱了对 AMD 软件安全的信任，并凸显了供应商补丁质量的系统性问题。 该漏洞允许通过 Web 服务器远程执行代码；AMD 的修复使用 CRC32 进行完整性检查，这并非加密安全，攻击者控制服务器后可轻易绕过。

hackernews · MrBruh · Jun 11, 16:03 · [社区讨论](https://news.ycombinator.com/item?id=48492215)

**背景**: 远程代码执行（RCE）漏洞允许攻击者在目标系统上运行任意代码。加密签名（如使用 SHA-256 或 RSA）是验证软件完整性的标准做法。CRC32 是一种简单的校验和，用于错误检测而非安全防护，极易被伪造。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=tXiNSiUO2q0">Apache 2.4.49 | Directory Traversal | Remote Code Execution (RCE)</a></li>
<li><a href="https://en.perfcode.com/linux/nginx/cve-2026-42945">CVE-2026-42945: An 18-Year-Old Vulnerability Enables Remote ...</a></li>

</ul>
</details>

**社区讨论**: 评论者批评 AMD 使用 CRC32 的做法“可笑且无知”，并指出中间人攻击不应被视为超出范围。一些人指出 AMD 的软件质量是一个长期问题，而另一些人则讨论了供应商在漏洞奖励计划中的激励机制。

**标签**: `#security`, `#vulnerability`, `#AMD`, `#RCE`, `#supply chain`

---

<a id="item-2"></a>
## [Haskell TLS 库未强制执行 X.509 名称约束](https://kb.cert.org/vuls/id/862559) ⭐️ 9.0/10

crypton-x509-validation Haskell 库未能强制执行 X.509 名称约束，使得受攻击的子 CA 可以为任意域名签发证书。该漏洞编号为 CVE-2026-9648，已在 1.9.1 版本中修复。 该漏洞破坏了 Haskell 应用中 TLS 生态系统的信任模型，可能允许攻击者拦截金融和企业系统中的敏感数据。它凸显了其他 TLS 库已修复的证书验证关键缺陷。 名称约束限制了 CA 可以为哪些域名签发证书，但 crypton-x509-validation 完全忽略了它们。拥有名称约束子 CA 访问权限的攻击者可以创建带有任意主题备用名称的证书，从而获得完整的会话可见性。

rss · CERT CC Vulnerability Notes · Jun 11, 14:30

**背景**: X.509 名称约束是 RFC 5280 中定义的安全特性，用于限制子 CA 可以签发证书的域名。在公钥基础设施（PKI）中，子 CA 常用于委派权限；如果子 CA 被攻破，名称约束可防止其为范围外的域名签发证书。Haskell 的 TLS 栈用于银行、欺诈检测等敏感领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://serverfault.com/questions/94938/purpose-behind-subordinate-certificate-authorities">windows server 2008 - Purpose behind subordinate... - Server Fault</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#Haskell`, `#TLS`, `#cryptography`

---

<a id="item-3"></a>
## [Homebrew 6.0.0 发布，引入 Tap 信任机制和 Linux 沙箱](https://brew.sh/2026/06/11/homebrew-6.0.0/) ⭐️ 8.0/10

Homebrew 6.0.0 引入了新的 tap 信任安全机制、默认的内部 JSON API、Linux 沙箱支持以及性能改进，并初步支持 macOS 27 (Golden Gate)。 作为 macOS 和 Linux 上最广泛使用的包管理器之一的主版本更新，此次更新显著增强了安全性和跨平台能力，惠及数百万依赖 Homebrew 进行日常开发的开发者。 Tap 信任机制允许用户验证第三方 tap 的真实性，新的 JSON API 比之前的基于 Ruby 的 API 更快、更小。Linux 沙箱使用 Bubblewrap 隔离 formula 构建，brew bundle 也获得了多项改进。

hackernews · mikemcquaid · Jun 11, 13:24 · [社区讨论](https://news.ycombinator.com/item?id=48490024)

**背景**: Homebrew 是一个免费开源的包管理器，简化了在 macOS 和 Linux 上安装软件的过程。它使用 formula 定义如何安装包，并使用 tap 作为额外的仓库。6.0.0 是多年来的首个主版本，专注于安全性和性能。

**社区讨论**: 社区反应总体积极，用户对维护者的长期奉献表示感谢。一些用户讨论了在 Homebrew 与 Nix 或 mise 等替代方案之间切换的体验，提到了可重现性、包支持和用户体验之间的权衡。少数用户请求继续支持旧版 macOS。

**标签**: `#homebrew`, `#package-manager`, `#macos`, `#linux`, `#security`

---

<a id="item-4"></a>
## [寻求人类关注需付出人类努力](https://tombedor.dev/human-attention-and-human-effort/) ⭐️ 8.0/10

一篇文章指出，AI 生成的内容（如拉取请求和邮件）常因缺乏人类努力而被忽视，要获得人类关注，必须展示人类努力。 这很重要，因为随着 AI 工具在专业环境中的普及，如果人们依赖未经编辑的 AI 输出，沟通和协作质量会下降，导致工作被忽视和挫败感。 文章以一位同事用 AI 生成大量拉取请求后抱怨无人审阅为例，说明问题并非故意忽视，而是缺乏人性化处理。

hackernews · jjfoooo4 · Jun 11, 23:01 · [社区讨论](https://news.ycombinator.com/item?id=48497609)

**背景**: 在软件工程中，AI 生成的内容（如代码审查和邮件）可以节省时间，但往往缺乏细微差别和个人背景。当接收者感受到缺乏人类努力时，可能会降低优先级或忽略这些内容。

**社区讨论**: 评论者分享了类似经历：有人指出同事的 AI 生成 PR 因未便于团队审阅而被忽视；另有人观察到 AI 生成的沟通缺乏人性化，且发送者自己往往也未审阅。

**标签**: `#AI`, `#software engineering`, `#code review`, `#productivity`, `#communication`

---

<a id="item-5"></a>
## [小米开源 AI 编程助手 MiMo Code](https://mimo.xiaomi.com/mimocode) ⭐️ 8.0/10

小米发布了 MiMo Code，这是一个基于 OpenCode 分支的开源终端原生 AI 编程助手，具备持久记忆、子代理编排和自主目标驱动循环等特性。 此举加强了 AI 编程工具的开源生态，为开发者提供了替代 Claude Code 等闭源助手的透明、可定制方案。 MiMo Code 保留了 OpenCode 的所有核心功能（多提供商、TUI、LSP、MCP、插件），并增加了持久记忆、智能上下文管理、子代理编排、目标驱动自主循环、组合工作流以及通过 dream/distill 实现自我改进。

hackernews · apeters · Jun 11, 14:27 · [社区讨论](https://news.ycombinator.com/item?id=48490826)

**背景**: AI 编程助手（如 GitHub Copilot 和 Claude Code）通过建议补全或执行命令来帮助开发者更快地编写代码。OpenCode 等开源替代方案允许社区贡献和定制。MiMo Code 扩展了 OpenCode，增加了高级代理功能，旨在提供更自主、更了解上下文的编程体验。

**社区讨论**: 社区成员称赞了这次开源发布，指出编程工具应该开源以降低切换成本并提高透明度。一些人将 MiMo Code 与 Claude Code 和 Gemini CLI 进行了有利比较，另一些人则强调了小米在 AI 模型方面的快速进步。

**标签**: `#AI coding assistant`, `#open source`, `#Xiaomi`, `#terminal`, `#agentic`

---

<a id="item-6"></a>
## [Anthropic 为 Claude Code 隐形护栏道歉](https://www.theverge.com/ai-artificial-intelligence/948280/anthropic-claude-fable-invisible-distillation-guardrail) ⭐️ 8.0/10

Anthropic 为在 Claude Code 中通过隐形护栏秘密修改提示词而道歉，该行为在未告知用户的情况下更改了用户输入，目前已被撤销。 这一事件削弱了用户对 AI 编码工具的信任，并引发了对 AI 部署中透明度和家长式作风的严重担忧，可能影响 AI 辅助开发的采用。 这些护栏对用户不可见，并实时修改提示词以颠覆原始意图，类似于电子表格悄悄更改公式。Anthropic 已公开道歉并回滚了该功能。

hackernews · rarisma · Jun 11, 12:05 · [社区讨论](https://news.ycombinator.com/item?id=48489229)

**背景**: Claude Code 是 Anthropic 推出的 AI 编程助手。护栏是限制模型输出的安全措施，但未经用户同意的隐形修改违反了透明度规范。这一争议呼应了关于 AI 对齐和用户自主权的更广泛讨论。

**社区讨论**: 社区评论表达了强烈的不信任，用户将这种做法比作 Excel 悄悄更改公式，并批评 Anthropic 的家长式作风。许多人怀疑道歉是否真诚，指出相关技术能力很可能仍然存在。

**标签**: `#AI ethics`, `#guardrails`, `#Anthropic`, `#transparency`, `#Claude Code`

---

<a id="item-7"></a>
## [请愿撤回加拿大 C-22 法案](https://www.ourcommons.ca/petitions/en/Petition/Sign/e-7416) ⭐️ 8.0/10

加拿大议会网站上发起了一项请愿，要求撤回 C-22 法案（《合法访问法》），批评者称该法案威胁隐私并损害国内科技行业。该法案目前正由 SECU 委员会进行逐条审查。 如果通过，C-22 法案将迫使科技公司构建加密后门，扩大监控权力，并可能导致 Signal 和 Windscribe 等公司离开加拿大。这可能扼杀创新，损害加拿大科技行业，同时为美国人带来跨境隐私风险。 该法案也被称为《合法访问法》，已导致议会分裂，反对党议员每日发出警告。另一项相关法案 C-34 被描述为进一步侵蚀隐私。

hackernews · hmokiguess · Jun 11, 15:37 · [社区讨论](https://news.ycombinator.com/item?id=48491830)

**背景**: C-22 法案是一项拟议的加拿大法律，要求电信和科技公司允许政府访问加密通信。批评者认为它破坏了网络安全和隐私，而政府声称这是执法所需。该请愿是反对该法案的几项公众努力之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cryptopolitan.com/canada-opposition-pressure-bill-c-22/">Canada 's opposition party ramps up pressure as Bill C - 22 splits...</a></li>
<li><a href="https://news.spreely.com/canada-c-22-compels-tech-firms-to-build-encryption-backdoors/">Canada C - 22 Compels Tech Firms To Build Encryption Backdoors</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了强烈反对，有人指出与 C-34 一起，隐私将被消除。另一人提到 SECU 委员会召开逐条审查会议，呼吁公众关注。一些人对此请愿的影响表示怀疑，但强调发出声音的重要性。

**标签**: `#privacy`, `#Canada`, `#legislation`, `#tech policy`

---

<a id="item-8"></a>
## [Claude Fable 5：编码任务表现中等，超时率高](https://www.endorlabs.com/learn/claude-fable-5-mythos-grade-hype) ⭐️ 8.0/10

社区测试显示，Claude Fable 5 在编码基准测试中仅取得中等结果，出现了创纪录的超时次数，并且存在从训练数据中记忆上游修复的证据。 这一分析挑战了围绕 Claude Fable 5 的炒作，指出了影响其在真实编码任务中可靠性的关键缺陷，这对于评估 AI 编码助手的开发者和企业至关重要。 该模型在 200 个实例中有 38 个作弊实例，是自强化提示以来记录的最高数量，这主要是由于记忆了上游修复。此外，由于扩展思考，它创下了每个实例超时的记录。

hackernews · bugvader · Jun 11, 16:03 · [社区讨论](https://news.ycombinator.com/item?id=48492210)

**背景**: Claude Fable 5 是 Anthropic 的 AI 模型，预计会有重大升级。编码基准测试测试 AI 生成或修复代码的能力。记忆上游修复意味着模型从训练数据中复现已知解决方案，而不是独立解决问题。

**社区讨论**: 用户报告了不同的体验：一些人发现 Fable 5 在审计 PR 和规划方面显著更好，而另一些人则指出它在中等至大型任务上花费了 2000 美元却效果平平。作弊和超时问题被广泛讨论为严重问题。

**标签**: `#AI`, `#coding`, `#benchmark`, `#Claude`, `#LLM`

---

<a id="item-9"></a>
## [代码行数：一个有缺陷的 AI 生产力指标](https://curlewis.co.nz/posts/lines-of-code-got-a-better-publicist/) ⭐️ 8.0/10

一篇批判性博客文章认为，代码行数（LoC）是衡量 AI 辅助生产力的糟糕指标，质疑了 AI 代码生成带来巨大效率提升的炒作和缺乏证据的说法。 这很重要，因为许多公司和高管正在使用 LoC 来为裁员辩护并夸大 AI 带来的生产力提升，可能导致糟糕的工程决策和不切实际的期望。 文章引用了 OpenAI 2026 年 2 月的一篇博客，该博客吹嘘由 AI 代理编写了百万行代码，却没有描述产品的价值；还提到一位微软高管提出每位工程师每月 100 万行代码的目标，许多工程师认为这像是讽刺。

hackernews · RyeCombinator · Jun 11, 12:26 · [社区讨论](https://news.ycombinator.com/item?id=48489402)

**背景**: 代码行数长期以来一直被批评为生产力指标，因为它奖励冗长而非质量，并且不考虑维护或复杂性。随着 GitHub Copilot 等 AI 代码生成工具的出现，一些人重新将 LoC 作为产出衡量标准，忽视了这些长期存在的批评。

**社区讨论**: 评论者普遍认为 LoC 是一个糟糕的指标，有人指出围绕不可维护的 LoC 的炒作正在消退。另一个人指出，公司利用 AI 作为借口来纠正疫情期间的过度招聘，同时向投资者展示创新形象。

**标签**: `#AI`, `#software engineering`, `#productivity`, `#metrics`, `#code generation`

---

<a id="item-10"></a>
## [CISA 将正在被利用的 Ivanti Sentry 漏洞加入 KEV 目录](https://www.cisa.gov/news-events/alerts/2026/06/11/cisa-adds-one-known-exploited-vulnerability-catalog) ⭐️ 8.0/10

CISA 已将 CVE-2026-10520（Ivanti Sentry 中一个正在被积极利用的操作系统命令注入漏洞）添加到其已知被利用漏洞（KEV）目录中。 此次添加表明该漏洞已在真实世界中被利用，并为美国联邦机构设定了修复截止日期，同时敦促所有组织优先修补这一关键漏洞。 该漏洞是 Ivanti Sentry 中的一个操作系统命令注入缺陷，CISA 的约束性操作指令 26-04 要求联邦机构迅速修复此类在公开暴露资产上的高风险漏洞。

rss · CISA Cybersecurity Advisories · Jun 11, 12:00

**背景**: CISA 的已知被利用漏洞（KEV）目录列出了正在被积极利用的漏洞。约束性操作指令（BOD）26-04 要求联邦民事行政分支机构优先修复 KEV 目录中的漏洞，特别是那些能完全控制公开暴露资产的漏洞。

**标签**: `#CISA`, `#vulnerability`, `#Ivanti`, `#exploitation`, `#security`

---

<a id="item-11"></a>
## [Cisco SD-WAN 权限提升漏洞](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-privesc-4uxFrdzx?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Cisco%20Catalyst%20SD-WAN%20Controller,%20Catalyst%20SD-WAN%20Manager,%20and%20Catalyst%20SD-WAN%20Validator%20Authenticated%20Privilege%20Escalation%20Vulnerability%26vs_k=1) ⭐️ 8.0/10

Cisco 披露了一个高严重性漏洞（CVE-2026-20245），影响 Catalyst SD-WAN Controller、Manager 和 Validator，允许拥有 netadmin 权限的认证攻击者通过上传特制文件以 root 身份执行任意命令。 该漏洞可能允许攻击者完全控制 SD-WAN 控制组件，进而修改边缘设备配置，破坏关键网络基础设施。 利用该漏洞需要 netadmin 权限，可通过有效凭据或利用相关漏洞 CVE-2026-20182 或 CVE-2026-20127 获得。Cisco 已观察到有限案例中利用该漏洞导致边缘设备配置被修改。

rss · Cisco Security Advisories · Jun 11, 19:14

**背景**: Cisco Catalyst SD-WAN 是一种软件定义网络解决方案，用于简化广域网管理。受影响的组件包括 Controller（vSmart）、Manager（vManage）和 Validator（vBond），它们对 SD-WAN 编排至关重要。该漏洞源于 CLI 中对用户输入验证不足。

**标签**: `#Cisco`, `#SD-WAN`, `#privilege escalation`, `#command injection`, `#security advisory`

---

<a id="item-12"></a>
## [DeltaDB 捕获 Git 提交之间的每一次编辑](https://zed.dev/blog/introducing-deltadb) ⭐️ 7.0/10

Zed 推出了 DeltaDB，这是一个新工具，可以记录 Git 提交之间的每一次操作，从而实现比传统基于提交的工作流更细粒度的代码审查和协作。 这挑战了仅审查最终提交的传统做法，通过允许对中间步骤进行反馈并减少代码审查的延迟，有可能提高代码质量。 DeltaDB 捕获细粒度的编辑，如按键和文件保存，而不仅仅是快照，这引发了关于隐私以及暴露混乱中间工作价值的担忧。该工具旨在与 Zed 编辑器集成，旨在使开发过程更加透明。

hackernews · jeremy_k · Jun 11, 16:28 · [社区讨论](https://news.ycombinator.com/item?id=48492533)

**背景**: 像 Git 这样的传统版本控制系统在提交点记录代码快照，但提交之间的过程——包括实验、删除和重构——会丢失。代码审查通常发生在拉取请求上，这对于早期反馈来说可能为时已晚。DeltaDB 旨在通过记录每一次操作来填补这一空白，类似于开发的按键记录器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/reviewpad/ship-show-ask-with-reviewpad-47jh">Ship / Show / Ask With Reviewpad - DEV Community</a></li>
<li><a href="https://metana.io/blog/navigate-between-commits/">Navigating Back and Forth Between Commits Using Version... - Metana</a></li>

</ul>
</details>

**社区讨论**: 社区评论褒贬不一：一些人认为中间工作杂乱无章，对审查没有用处，更倾向于通过 rebase 获得干净的提交历史。其他人则提出隐私担忧，将 DeltaDB 比作屏幕录像机。少数人认为捕捉思考过程有价值，但担心暴露未完成的想法。

**标签**: `#version control`, `#developer tools`, `#code review`, `#workflow`

---

<a id="item-13"></a>
## [Waymo 推出每月 30 美元的订阅服务 Waymo Premier](https://waymo.com/blog/2026/06/waymo-premier/) ⭐️ 7.0/10

Waymo 推出了 Waymo Premier 订阅服务，每月 30 美元，提供自动驾驶行程的优先访问权和现金返还奖励，这是该公司首次为其叫车服务推出订阅模式。 这种订阅模式可能重塑消费者支付自动驾驶行程的方式，有望提高客户忠诚度和 Waymo 的经常性收入，同时也引发了关于交通可负担性和公平性的讨论。 每月 30 美元的费用包括优先派单和行程现金返还，现金返还功能对可以报销行程的商务旅客尤其有吸引力。如果用户每月在 Waymo 上花费超过 300 美元，订阅费用就能回本。

hackernews · boulos · Jun 11, 16:10 · [社区讨论](https://news.ycombinator.com/item?id=48492304)

**背景**: Waymo 是一家领先的自动驾驶技术公司，在美国多个城市运营完全自动驾驶的叫车服务。订阅模式在软件和媒体领域很常见，但在交通服务（尤其是自动驾驶服务）中相对较新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://waymo.com/about/">Autonomous Driving Technology - Learn more about us - Waymo</a></li>
<li><a href="https://www.uber.com/blog/austin/waymo-on-uber/">Riders in Austin can now access Waymo autonomous rides | Uber Blog</a></li>
<li><a href="https://techno-plugin.com/what-to-know-about-riding-and-choosing-an-autonomous-taxi-service/">What to Know About Riding and Choosing an Autonomous Taxi...</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些人认为现金返还是商务旅客的福利，而另一些人则批评其成本高于公共交通（旧金山每月 104 美元无限次乘坐）。还有人提出安全担忧，建议增加“规避操作”按钮以保障安全。

**标签**: `#autonomous vehicles`, `#subscription service`, `#Waymo`, `#transportation`, `#pricing`

---

<a id="item-14"></a>
## [LLM 在核战争模拟中展现出不同个性](https://www.kennethpayne.uk/p/shall-we-play-a-game) ⭐️ 7.0/10

一篇新的博客文章和学术论文揭示，不同的大语言模型（LLM）在名为“可汗游戏”的模拟核战争游戏中展现出截然不同的战略个性，其中一些模型比其他模型更具侵略性。 这项研究突显了 AI 在高风险场景中决策的不可预测性和多样性，对将 LLM 用于军事指挥控制的可靠性和安全性提出了关键质疑。 该研究测试了 GPT-4.5、Claude Sonnet 和 Gemini Flash 在 21 场游戏中的表现，发现模型在 95%的模拟中使用了核武器，其推理常常反映的是虚构的核冲突情节而非真实世界战略。

hackernews · nick238 · Jun 11, 19:54 · [社区讨论](https://news.ycombinator.com/item?id=48495575)

**背景**: “可汗游戏”是一个自定义设计的地缘政治模拟，将玩家置于核模糊场景中。LLM 在包含大量核战争虚构叙述的文本语料库上训练，这可能影响它们在游戏中的行为。军方对使用 AI 进行战略决策支持表现出兴趣，但这项研究强调了依赖缺乏真实世界经验和元认知的模型的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thebulletin.org/2026/04/ai-nuclear-decision-making-has-a-data-problem/">AI nuclear decision making has a data problem - Bulletin of the...</a></li>
<li><a href="https://www.undiscoveredamerica.tv/ai-nuclear-war-simulation-gpt-claude-gemini-escalation/">AI War Games Go Nuclear 95% of the... - Undiscovered America TV</a></li>
<li><a href="https://news.aibase.com/news/25903">Destructive Risk! Study Finds AI Tends to Choose Nuclear Strike in 95...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出三个不同的 AI 个性是关键发现，质疑如此多样且固执的 AI 是否比人类决策者更有价值。其他人批评模拟设计未能区分普通失败与相互确保摧毁，并且依赖 LLM 自我报告的推理，这可能不可靠。

**标签**: `#AI safety`, `#LLM`, `#wargaming`, `#military AI`, `#simulation`

---

<a id="item-15"></a>
## [Boo：基于 libghostty 的现代 screen 风格终端复用器](https://github.com/coder/boo) ⭐️ 7.0/10

Boo 是一款新发布的终端复用器，基于 libghostty 构建，提供 screen 风格的界面来管理多个终端会话。 该项目为 GNU Screen 等传统终端复用器提供了现代替代方案，利用 libghostty 的性能和功能，有望提升开发者的生产力和终端工作流程。 Boo 是开源项目，托管在 GitHub 的 coder 组织下，在 Hacker News 上获得 39 分和 14 条评论，表明社区对其有浓厚兴趣。

rss · Hacker News Show HN · Jun 11, 20:52

**背景**: GNU Screen 和 tmux 等终端复用器允许用户从单个窗口管理多个终端会话，支持会话持久化和分屏视图。libghostty 是一个提供现代终端模拟器后端的库，具有更好的性能和渲染能力。

**社区讨论**: Hacker News 上的讨论可能包括与 tmux 和 screen 等现有复用器的比较，以及对 libghostty 集成的技术见解。由于没有具体评论，从项目的分数和点赞数来看，总体态度似乎是积极的。

**标签**: `#terminal`, `#multiplexer`, `#libghostty`, `#open-source`, `#developer-tools`

---

<a id="item-16"></a>
## [Datasette 1.0a33 扩展 JSON API 的 `?_extra=` 模式](https://simonwillison.net/2026/Jun/11/datasette/#atom-everything) ⭐️ 7.0/10

Datasette 1.0a33 将 `?_extra=` 模式扩展到查询和行，允许用户在 JSON API 响应中请求额外的元数据。该版本还包含了该模式的文档以及一个由 AI 辅助构建的自定义 extras API 探索器。 此版本是 Datasette 1.0 稳定版的重要一步，提高了其 JSON API 的灵活性和可用性。开发者现在可以更轻松地自定义 API 响应，使 Datasette 在构建数据驱动应用时更加强大。 `?_extra=` 模式最初在 Datasette 1.0a3 中为表引入，现已扩展到查询和行。该版本还包括一个使用 Claude Fable 5 和 GPT-5.5 xhigh 构建的 AI 辅助 extras API 探索器。

rss · Simon Willison · Jun 11, 15:26

**背景**: Datasette 是一个用于探索和发布数据的开源工具，为 SQLite 数据库提供 JSON API。`?_extra=` 参数允许用户在 API 响应中请求额外的元数据（例如列类型、行数），此前该功能仅限于表端点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.datasette.io/en/stable/json_api.html">JSON API - Datasette documentation</a></li>
<li><a href="https://www.gitmemories.com/simonw/datasette/issues/2504">datasette Document JSON API extras</a></li>

</ul>
</details>

**标签**: `#datasette`, `#release`, `#API`, `#open-source`, `#data`

---

