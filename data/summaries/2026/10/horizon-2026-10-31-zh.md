# Horizon 每日速递 - 2026-10-31

> From 71 items, 14 important content pieces were selected

---

1. [被篡改的 Claude Code VS Code 扩展在 Cursor 市场植入后门](#item-1) ⭐️ 9.0/10
2. [研究员发现 Azure 五个完全跨租户入侵漏洞](#item-2) ⭐️ 9.0/10
3. [Northflank PaaS 遭遇安全漏洞](#item-3) ⭐️ 8.0/10
4. [CISA 将两个已遭利用的 Ivanti Connect Secure 漏洞加入 KEV 目录](#item-4) ⭐️ 8.0/10
5. [Cloudflare 追踪 eMudhra 弱 RSA 密钥的利用情况](#item-5) ⭐️ 8.0/10
6. [开发者用约 1GB 的 Qwen 模型权重模拟 NES 游戏机](#item-6) ⭐️ 7.0/10
7. [Tangled 推出基于 AT Protocol 的联邦代码托管平台](#item-7) ⭐️ 7.0/10
8. [AO3 因检测到安全事件而停机维护](#item-8) ⭐️ 7.0/10
9. [AI 代理正在使 SRE 技能退化，而非取代他们](#item-9) ⭐️ 7.0/10
10. [Bunny CDN 因 Gcore 被入侵隔离节点并重发 TLS 证书](#item-10) ⭐️ 7.0/10
11. [Polymarket 因供应商被入侵暂停交易一小时，承诺全额补偿受影响用户](#item-11) ⭐️ 7.0/10
12. [微软追踪从帮助台冒充到 AD CS ESC1/ESC8 滥用的入侵路径](#item-12) ⭐️ 7.0/10
13. [Nathan Lambert 在“黑色十月”后重新审视开放模型的网络风险](#item-13) ⭐️ 7.0/10
14. [JEPA 可跨模态学到统一表征，文本 JEPA 对齐优于 72B 语言模型](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [被篡改的 Claude Code VS Code 扩展在 Cursor 市场植入后门](https://phorion.io/blog/offical-claude-code-vsx-compromise/) ⭐️ 9.0/10

一个被恶意篡改的 Claude Code VS Code 扩展（版本 2.1.313）被发布到 Cursor 市场，该扩展会将攻击者控制的 SSH 公钥（标记为 'svc-telemetry'）追加到用户的 ~/.ssh/authorized_keys 文件中。Cursor 和 Anthropic 发布了官方安全公告，称该扩展在周四太平洋时间约凌晨 2:27 至下午 1:35 期间上线，最多影响 5,000 名用户。 这是一起影响广泛使用的 AI 编程工具的供应链攻击事件，表明即使官方供应商没有过错，扩展市场也可能被滥用来分发带有后门的软件。它凸显了 SSH 密钥注入作为持久化手段的持续风险，并引发了关于第三方 IDE 市场信任与验证机制的疑问。 该后门会向 authorized_keys 添加一个 SSH 公钥，使攻击者能够持久地远程访问；用户可以在 macOS 上运行 `grep -qs svc-telemetry ~/.ssh/authorized_keys`（Windows 上有对应命令）来检查是否受影响。Anthropic 澄清该恶意版本并非由 Anthropic 构建或发布，官方渠道（如微软 VS Code 市场）上的版本不受影响。

hackernews · _chall · Oct 30, 07:09 · [社区讨论](https://news.ycombinator.com/item?id=50300683)

**背景**: Claude Code VS Code 扩展将 Anthropic 的 Claude Code AI 助手集成到 Visual Studio Code 及兼容 IDE 中。Cursor 市场是 Cursor IDE 使用的第三方扩展注册表，Cursor 基于 VS Code，通常从 Open VSX 而非微软官方市场获取扩展。SSH 的 authorized_keys 文件列出了允许登录某账户的公钥；添加攻击者的密钥是一种常见的后门技术，用于维持持久访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2026/10/official-claude-code-vs-code-extension.html">Official Claude Code VS Code Extension Compromised to Install...</a></li>
<li><a href="https://explainx.ai/blog/claude-code-extension-trojanized-2-1-313-cursor-marketplace-ssh-backdoor-what-is-confirmed-2026">Claude Code Extension 2.1.313 SSH Backdoor: What To... | explainx.ai</a></li>
<li><a href="https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code">Claude Code for VS Code - Visual Studio Marketplace</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了检测命令和官方公告链接，Anthropic 的 Felix Rieseberg 澄清该事件不涉及 Anthropic 系统被入侵，仅影响 Cursor 用户。一些用户争论微软官方市场是否也受影响，另一些人则强调应参考 Phorion 的原始报告以了解技术细节。

**标签**: `#supply-chain-attack`, `#claude-code`, `#cursor-marketplace`, `#ssh-backdoor`, `#vscode-extension-security`

---

<a id="item-2"></a>
## [研究员发现 Azure 五个完全跨租户入侵漏洞](https://www.binarysecurity.no/posts/2026/10/one-root-case) ⭐️ 9.0/10

一位安全研究员发布详细报告，记录了微软 Azure 中的五个不同漏洞，每个漏洞都允许完全的跨租户入侵，即攻击者可以完全控制另一个客户的云资源。该报告强调了 Azure 多租户隔离中的系统性弱点，包括可伪造的管理员同意回调和路径遍历/IDOR 根本原因。 这些发现意义重大，因为 Azure 是全球企业广泛使用的主要云平台，而完全的跨租户入侵破坏了多租户云服务的基本信任模型。如果被利用，此类漏洞可能导致众多组织的大规模数据泄露和服务中断。 这些漏洞涉及 login.microsoftonline.com 管理员同意流程中可伪造的回调，攻击者若知道另一个租户的 ID 就能伪造重定向，以及可能自功能引入以来就存在的路径遍历和 IDOR 问题。研究员建议在资源名称中添加随机性作为缓解措施，但这只是安全通过 obscurity，而非根本性修复。

hackernews · swq115 · Oct 30, 10:06 · [社区讨论](https://news.ycombinator.com/item?id=50301854)

**背景**: 像 Azure 这样的多租户云平台会隔离客户环境（租户），使一个客户无法访问另一个客户的数据或资源。跨租户漏洞打破了这种隔离，通常通过不安全的直接对象引用（IDOR）等缺陷实现，攻击者操纵标识符来访问未授权的资源，或通过路径遍历导航到预期目录之外。管理员同意流程是 Azure 身份平台（Entra ID，前身为 Azure AD）的一部分，用于授予应用程序代表组织访问资源的权限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cyberpress.org/azure-api-connection-vulnerability/">Critical Azure API Connection Vulnerability Exposes Cross - Tenant ...</a></li>
<li><a href="https://tamnoon.io/blog/breaking-the-barriers-exploiting-entra-id-consent-and-groups-challenge-3/">Exploiting Entra ID Consent and Groups | Tamnoon Research</a></li>
<li><a href="https://redbotsecurity.com/insecure-direct-object-reference/">Insecure Direct Object Reference ( IDOR ) Guide | Redbot Security</a></li>

</ul>
</details>

**社区讨论**: 评论者对 Azure 的跨租户泄露记录表示担忧，其中一人指出可伪造的管理员同意回调是一个持续存在的问题，并质疑企业为何仍选择 Azure。其他人赞扬了研究员的工作，并指出路径遍历和 IDOR 缺陷可能追溯到功能引入之初，一人认为在资源名称中添加随机性的建议是一种安全通过 obscurity 的做法。

**标签**: `#azure`, `#cloud-security`, `#cross-tenant`, `#vulnerability-research`, `#idor`

---

<a id="item-3"></a>
## [Northflank PaaS 遭遇安全漏洞](https://status.northflank.com/) ⭐️ 8.0/10

多租户平台即服务提供商 Northflank 遭遇安全漏洞，其状态页面显示了相关信息。该事件在 Hacker News 上引发了大量讨论，共有 272 条评论和 351 个点赞。 此次漏洞是近期针对 SaaS 基础设施供应商的一系列攻击的一部分，引发了对供应链安全和多租户平台信任的担忧。这可能会加速注重安全的企业回归超大规模云服务商的趋势。 漏洞的详细信息仅限于 Northflank 的状态页面，目前尚不清楚客户的代码或二进制文件是否被访问。社区成员指出，自 9 月以来，至少发生了六起针对多租户即服务供应商的类似攻击，包括 PingCAP/TiDB、Fireworks AI、Zeabur、OpenCode Console 和 Railway。

hackernews · js4ever · Oct 30, 15:10 · [社区讨论](https://news.ycombinator.com/item?id=50305025)

**背景**: Northflank 是一家平台即服务（PaaS）提供商，它将传统平台的简单性与 Kubernetes 的强大功能和灵活性相结合，允许开发人员在云中部署和管理应用程序。多租户平台在共享基础设施上托管多个客户，如果其中一个租户被攻破，可能会带来安全风险。近期针对此类供应商的攻击凸显了 SaaS 生态系统中强大安全措施的重要性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://northflank.com/blog/what-is-paas-hosting">What is PaaS hosting? Benefits and how it works | Blog — Northflank</a></li>
<li><a href="https://northflank.com/blog/best-paas-for-enterprises">Best PaaS for enterprises in 2026 | Blog — Northflank</a></li>

</ul>
</details>

**社区讨论**: 评论者对攻击的频率表示震惊，有人统计自 9 月以来针对多租户即服务供应商的六起重大攻击。一些人提出了变通方法，如使用硬编码密钥加密环境变量，而另一些人则预测出于安全考虑将回归超大规模云服务商。还有人推测未来技术安全将变得不可能，行为安全和摩擦将变得必要。

**标签**: `#cloud-security`, `#supply-chain`, `#SaaS`, `#breach`, `#infrastructure`

---

<a id="item-4"></a>
## [CISA 将两个已遭利用的 Ivanti Connect Secure 漏洞加入 KEV 目录](https://www.cisa.gov/news-events/alerts/2026/10/30/cisa-adds-two-known-exploited-vulnerabilities-catalog) ⭐️ 8.0/10

CISA 基于主动利用的证据，将 Ivanti Connect Secure 中的 CVE-2026-111357（关键功能缺失身份验证）和 CVE-2026-118527（可预测数字或标识符生成）加入其已知被利用漏洞（KEV）目录。此次新增触发了联邦文职行政部门（FCEB）机构在《约束性操作指令》（BOD）26-04 下的修复要求。 这些漏洞正被主动利用，且影响广泛部署的远程访问 VPN 设备 Ivanti Connect Secure，因此任何暴露的组织都面临重大风险。KEV 收录使 FCEB 机构在 BOD 26-04 下必须进行修复，并向所有企业发出信号：应立即优先处理这些漏洞。 BOD 26-04 于 2026 年 6 月 10 日发布，以基于风险的分级系统取代 BOD 22-01 的固定截止日期，对公开暴露资产上利用后可获得完全控制权的最严重漏洞设定了 3 天的修复期限。该指令还要求机构检查在打补丁前威胁行为者是否已入侵系统，同时 CISA 鼓励所有组织采用基于风险的漏洞管理。

rss · CISA Cybersecurity Advisories · Oct 30, 12:00

**背景**: KEV 目录是 CISA 维护的权威列表，收录有证据表明正被主动利用的漏洞，用于推动优先修补。Ivanti Connect Secure 是一种常用于远程访问的 SSL VPN 设备，因此经常成为攻击者的目标。约束性操作指令是面向联邦行政部门机构的强制性指令，用于保护联邦信息系统，而 BOD 26-04 特别将修复紧迫性与 KEV 收录及资产暴露情况挂钩。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog">cisa .gov/ known - exploited - vulnerabilities - catalog</a></li>
<li><a href="https://shattered.io/cisa-kev-bod-26-04-deadline-2026/">CISA KEV Adds 12 CVEs as BOD 26 - 04 Cuts Deadline [2026]</a></li>
<li><a href="https://community.opentextcybersecurity.com/vulnerability-vault-228/binding-operational-directives-bod-26-04-prioritizing-security-updates-based-on-risk-june-10-2026-364598">Binding Operational Directives BOD 26 - 04 : Prioritizing Security...</a></li>

</ul>
</details>

**标签**: `#CISA KEV`, `#Ivanti Connect Secure`, `#actively exploited vulnerabilities`, `#vulnerability management`, `#federal cybersecurity`

---

<a id="item-5"></a>
## [Cloudflare 追踪 eMudhra 弱 RSA 密钥的利用情况](https://blog.cloudflare.com/emudhra-patching/) ⭐️ 8.0/10

Cloudflare 发布了对使用弱 RSA 密钥的 eMudhra 证书的分析，这些密钥仅需四次尝试即可被分解，并详细说明了其如何修补自身系统以及追踪互联网上的利用尝试。 该漏洞影响互联网范围内使用的 TLS 证书，可能允许攻击者冒充受信任的服务并拦截加密流量，因此未修补系统的暴露对依赖 eMudhra 颁发证书的组织来说是一个关键的安全问题。 这些弱密钥与 eMudhra 运营的八个中间证书颁发机构证书相关，并且由于私钥可以从公开证书中恢复，任何使用这些证书的未修补连接都面临风险；Cloudflare 还观察到了野外利用尝试的证据。

rss · Cloudflare Blog · Oct 30, 17:38

**背景**: eMudhra 是一家印度数字信任提供商，作为证书颁发机构（CA）运营，颁发用于保护 TLS 连接的数字证书。在典型的 RSA 设置中，公钥由两个大质数生成，其安全性依赖于将公钥分解回这两个质数的难度。如果质数生成得较弱，密钥可以被快速分解，从而允许攻击者推导出私钥并冒充证书持有者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Black_October_(information_security)">Black October (information security) - Wikipedia</a></li>
<li><a href="https://socradar.io/blog/emudhra-ca-key-compromise-weak-keys-risks-and-fixes/">eMudhra CA Key Compromise: Weak Keys , Risks and Fixes</a></li>
<li><a href="https://bitcoinfoundation.org/news/ethereum/consensys-flags-web3signer-risk-from-8-compromised-emudhra-certificates/">Web3Signer Security Warning: 8 Compromised Certificates</a></li>

</ul>
</details>

**标签**: `#TLS`, `#RSA`, `#weak keys`, `#certificate vulnerability`, `#exploitation`

---

<a id="item-6"></a>
## [开发者用约 1GB 的 Qwen 模型权重模拟 NES 游戏机](https://github.com/dbreunig/nesformer) ⭐️ 7.0/10

开发者 dbreunig 创建了名为“nesformer”的项目，利用约 1GB 的 Qwen 语言模型来模拟任天堂娱乐系统（NES），包括 CPU 和 RAM，其权重和代码主要由 LLM（Opus 5.5）通过两个提示生成。 这一概念验证表明，虚拟机和解释器有可能直接嵌入到 LLM 权重中，为在模型内部仅使用矩阵乘法来运行工具和执行代码开辟了可能性，而无需依赖缓慢的外部工具调用。 该模拟运行速度比真实 NES 慢 150–290 倍，凸显了 LLM 与确定性程序之间的巨大效率差距；模型使用门控 deltanet 架构同时模拟 CPU 和 RAM，且项目仅通过少量提示构建。

hackernews · dbreunig · Oct 30, 16:40 · [社区讨论](https://news.ycombinator.com/item?id=50306442)

**背景**: NES 是 20 世纪 80 年代的经典 8 位游戏机，模拟它通常需要编写复现其硬件行为的软件。像 Qwen 这样的大语言模型（LLM）是逐词生成文本的神经网络，通常不用于确定性计算。本项目探索了一种非常规方法：将整个模拟器编码到 LLM 的权重中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.6-27B">Qwen / Qwen 3.6-27B · Hugging Face</a></li>
<li><a href="https://www.retroreversing.com/nes-emulation">The History of NES Emulation - Retro Reversing (Reverse Engineering)</a></li>

</ul>
</details>

**社区讨论**: 评论者认为这一黑客行为非常有趣，一些人提出可以将小型虚拟机（如 Python 解释器）直接编译到 LLM 权重中以实现更快的执行。其他人则强调了效率上的鲜明对比，指出虽然技术上可行，但这种基于 LLM 的模拟比传统程序慢几个数量级且计算密集得多。

**标签**: `#LLM`, `#emulation`, `#Qwen`, `#AI agents`, `#Show HN`

---

<a id="item-7"></a>
## [Tangled 推出基于 AT Protocol 的联邦代码托管平台](https://tangled.org/blog/forge/) ⭐️ 7.0/10

Tangled 是一个基于 AT Protocol 的联邦代码托管平台，现已推出，具有稳定的词法定义、全面重构的架构和界面、易于自托管整个技术栈以及对组织的支持。私有仓库计划在未来几周内推出。 这为 GitHub 等中心化代码托管平台提供了一种替代方案，利用联邦协议进行代码协作，可能让开发者对自己的数据和身份拥有更多控制权。这也表明人们对去中心化开发工具和平台间互操作性的兴趣日益增长。 Tangled 已稳定其 AT Protocol 词法定义（用于定义互操作性的数据模式），并允许自托管整个技术栈或部分组件。团队还致力于将问题、PR 和评论记录移至仓库作用域下，以改善与其他平台的互操作性。

hackernews · zlliang · Oct 30, 15:44 · [社区讨论](https://news.ycombinator.com/item?id=50305573)

**背景**: AT Protocol 是由 Bluesky 开发的联邦社交网络协议，支持账户可移植性和独立服务间的互操作性。代码托管平台是用于托管和协作开发软件仓库的平台，传统上是中心化的，如 GitHub。Tangled 旨在将联邦原则应用于代码协作，类似于 Radicle 等其他去中心化平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://atproto.com/guides/faq">Frequently Asked Questions about AT Protocol .</a></li>
<li><a href="https://bsky.social/about/blog/10-18-2022-the-at-protocol">The AT Protocol - Bluesky</a></li>
<li><a href="https://radicle.dev/">The Radicle forge is an open source, peer-to-peer code collaboration...</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对 Tangled 的热情，一位开发者计划从自托管的 Gitea 迁移，另一位正在构建可互操作的平台。联合创始人回答了问题，并强调了稳定的词法定义和即将推出的私有仓库，其他人则提供了界面反馈，并提到了一轮 380 万欧元的融资。

**标签**: `#federated-code-forge`, `#AT-Protocol`, `#decentralized-git`, `#code-collaboration`, `#self-hosting`

---

<a id="item-8"></a>
## [AO3 因检测到安全事件而停机维护](https://www.otwstatus.org/) ⭐️ 7.0/10

Archive of Our Own（AO3）在检测到安全事件证据后停机维护，该组织表示没有数据被删除，目前认为用户数据库未被窃取。调查仍在进行中，以确定事件范围。 AO3 是一个拥有大量用户的大型同人小说平台，安全事件可能泄露用户名、电子邮件、IP 地址和哈希密码等敏感用户信息。此事件凸显了事件响应中透明度的重要性，并提高了对密码安全实践的认识。 AO3 数据库可能包含账户信息，包括用户名、电子邮件地址、IP 地址和哈希密码。虽然该组织目前认为用户数据库未被窃取，但调查仍处于早期阶段，范围正在确定中。

hackernews · idlewords · Oct 30, 21:17 · [社区讨论](https://news.ycombinator.com/item?id=50310258)

**背景**: AO3 是一个由粉丝创建的热门平台，用于托管同人小说和其他衍生作品，由 Organization for Transformative Works（OTW）运营。密码哈希是一种安全措施，将密码转换为固定长度的字符串，使得攻击者即使获取数据库也难以恢复原始密码。然而，弱哈希算法或不良实现仍可能使密码容易被破解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wired.com/2016/06/hacker-lexicon-password-hashing/">Hacker Lexicon: What Is Password Hashing ? | WIRED</a></li>
<li><a href="https://haveibeenpwned.com/Passwords">Have I Been Pwned: Pwned Passwords</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对未被检测到的泄露和安全事件频繁发生的担忧，一些人指出当前时期似乎充斥着泄露披露。一位评论者强调了更好的密码哈希实践以保护用户的重要性。

**标签**: `#security-incident`, `#data-breach`, `#AO3`, `#password-hashing`, `#incident-response`

---

<a id="item-9"></a>
## [AI 代理正在使 SRE 技能退化，而非取代他们](https://newsletter.signoz.io/p/ai-isnt-replacing-sres-its-deskilling) ⭐️ 7.0/10

SigNoz 通讯的一篇文章认为，AI 代理并未取代站点可靠性工程师（SRE），而是通过移除构建运维理解所需的动手故障排查工作，使他们技能退化。该文章在 Hacker News 上引发了大规模辩论，获得 498 分和 376 条评论。 这很重要，因为随着 AI 代理在云运维中能力越来越强，SRE 可能失去对系统的深入理解，而这种理解对于处理新型故障和维持可靠性至关重要。讨论凸显了自动化效率与保留人类专业知识之间的更广泛行业矛盾。 文章建议 SRE 团队可以指定某些事件为人工练习机会，类似于美国联邦航空管理局规定飞行员即使自动驾驶仪可用也必须进行手动飞行时间。评论者指出，像 Claude 这样的 AI 代理在使用 AWS CLI 等任务上可以超越人类，解决问题快 10 倍。

hackernews · dorianniemiec · Oct 30, 15:52 · [社区讨论](https://news.ycombinator.com/item?id=50305693)

**背景**: 站点可靠性工程（SRE）是一门将软件工程原则应用于 IT 运维的学科，以确保系统可靠且可扩展。技能退化是指技术淘汰熟练劳动力，使工人降级为低技能角色的过程。辩论将其与航空业相提并论，航空业长期以来一直管理自动化以保持飞行员的参与。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Site_reliability_engineering">Site reliability engineering - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Deskilling">Deskilling - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者观点不一：一些人同意航空业为保持人类技能提供了模型，而另一些人则认为 AI 在云运维中已超越人类，技能退化是进步的自然结果，类似于 Terraform 使基础设施管理技能退化。一个关键担忧是 AI 生成的系统缺乏真正的理解，而这对于 SRE 工作至关重要。

**标签**: `#AI agents`, `#SRE`, `#deskilling`, `#automation`, `#DevOps`

---

<a id="item-10"></a>
## [Bunny CDN 因 Gcore 被入侵隔离节点并重发 TLS 证书](https://status.bunny.net/incidents/p6gf1by9kr7m) ⭐️ 7.0/10

Bunny CDN 披露，第三方基础设施提供商 Gcore 因第三方服务器管理软件遭到未经授权的访问。Bunny 在 20 分钟内隔离了位于亚美尼亚的一个受影响 CDN 节点，擦除了服务器，并作为预防措施重新颁发了其平台域名的所有 TLS 证书。 该事件凸显了 CDN 基础设施中的供应链风险，上游提供商的入侵可能影响下游服务。Bunny 的快速遏制和证书重发展现了事件响应的最佳实践，但该事件也强调了对供应商进行严格安全评估的必要性。 Bunny 表示，虽然未发现对其服务器的未经授权访问，但不能完全排除这种可能性；可能暴露的数据包括缓存的 CDN 内容、Pull Zone 配置和 TLS 证书。受影响的服务器已被永久移除，b-cdn.net 和 bunny.run 的所有 TLS 证书已被吊销并重新颁发。

hackernews · SondreDag · Oct 30, 19:05 · [社区讨论](https://news.ycombinator.com/item?id=50308697)

**背景**: CDN（内容分发网络）是一个地理上分布的服务器网络，根据用户位置交付网页内容，以提高速度和可靠性。TLS 证书是用于验证和加密客户端与服务器之间连接的加密凭证。CDN 节点被入侵可能允许攻击者拦截或操纵流量，因此重新颁发证书是关键修复步骤。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gcore.com/infrastructure">Advanced, secure, and compliant infrastructure | Gcore</a></li>
<li><a href="https://arstechnica.com/security/2026/10/hackers-obtain-counterfeit-tls-certificates-for-google-and-other-large-services/">Hackers obtain counterfeit TLS certificates for Google... - Ars Technica</a></li>

</ul>
</details>

**社区讨论**: 评论者赞扬了 Bunny 的迅速且专业的响应，但批评了暗示 Bunny 自身被黑的误导性标题。他们澄清根本原因是上游提供商 Gcore 被入侵，仅影响一个 POP，并讨论了在事件响应中保留日志的重要性。

**标签**: `#security-incident`, `#cdn`, `#supply-chain`, `#tls-certificates`, `#gcore`

---

<a id="item-11"></a>
## [Polymarket 因供应商被入侵暂停交易一小时，承诺全额补偿受影响用户](https://www.nbcnews.com/business/consumer/polymarket-trading-halt-hack-wallets-rcna606405) ⭐️ 7.0/10

最大的预测市场 Polymarket 在发生供应商被入侵事件后暂停交易一小时，该事件影响了用户账户，公司表示将全额补偿受影响用户。 这一事件凸显了加密平台面临的供应链攻击风险日益增加，第三方供应商被入侵可能中断交易并危及用户资金，可能削弱人们对预测市场和去中心化金融的信任。 此次攻击风格类似于盗取 15 亿美元的 Bybit 前端供应链攻击，社区成员指出可复现的 Web 构建难以实现，有人提出 IPFS 作为潜在解决方案但维护不善。

hackernews · theanonymousone · Oct 30, 15:23 · [社区讨论](https://news.ycombinator.com/item?id=50305225)

**背景**: Polymarket 是一个去中心化预测市场，用户使用加密货币对事件结果进行交易。供应链攻击通过入侵第三方供应商，将恶意代码注入平台前端，可能窃取资金或数据。可复现构建旨在确保 Web 应用程序的代码可以被独立验证，但对于动态 Web 应用来说具有挑战性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aszx87410.github.io/beyond-xss/en/ch5/supply-chain-attack/">Frontend Supply Chain Attacks : Attacking Downstream from...</a></li>
<li><a href="https://www.bitcoin.com/prediction-markets/polymarket/">Polymarket Review — Decentralized Prediction Market | Bitcoin.com</a></li>

</ul>
</details>

**社区讨论**: HN 评论者分享了账户被接管和客服无响应的第一手经历，将此次攻击与 Bybit 式前端供应链攻击相比较，并讨论了基于 IPFS 的不可变 Web 应用引导程序等可复现部署的技术方案。

**标签**: `#supply-chain-attack`, `#crypto-security`, `#account-takeover`, `#web-security`, `#incident-response`

---

<a id="item-12"></a>
## [微软追踪从帮助台冒充到 AD CS ESC1/ESC8 滥用的入侵路径](https://www.microsoft.com/en-us/security/blog/2026/10/30/help-desk-impersonation-ad-cs-abuse-investigating-esc1-esc8-intrusion-paths/) ⭐️ 7.0/10

微软安全研究团队发布了一份详细的入侵链分析，展示了攻击者如何冒充 Teams 帮助台获取远程访问权限、执行恶意运行时代码，并最终利用 ESC1 和 ESC8 技术通过身份验证中继和 Kerberos 滥用 Active Directory 证书服务。 这一真实攻击路径凸显了针对帮助台的社会工程攻击如何与 AD CS 错误配置相结合，导致整个域被攻陷；依赖 Teams 支持和 AD CS 的组织应审查其证书注册和身份验证中继防御措施。 该分析聚焦于已知的 AD CS 错误配置（ESC1 和 ESC8），而非新漏洞，并演示了如何利用 Kerberos 和身份验证中继获取证书以提升权限；防御者应注意，Kerberos 中继防护是在服务层面实施的，而非由协议本身提供。

rss · Microsoft Security Blog · Oct 30, 16:11

**背景**: Active Directory 证书服务（AD CS）是微软用于在 Windows 域中颁发和管理数字证书的公钥基础设施。ESC1 指一种错误配置，低权限用户可请求允许以任意用户身份进行身份验证的证书；ESC8 则涉及将身份验证（如 NTLM 或 Kerberos）中继到 AD CS HTTP 注册端点，以获取高权限账户的证书。身份验证中继攻击将捕获的身份验证尝试转发到另一服务，而 Kerberos 中继虽然不如 NTLM 中继那样宽松，但在特定条件下仍可被利用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.adcs-security.com/attacks/esc8">ESC 8 : NTLM Relay to ADCS HTTP Endpoints - AD ... | ADCS Security</a></li>
<li><a href="https://www.thehacker.recipes/ad/movement/kerberos/relay">Kerberos relay | The Hacker Recipes</a></li>
<li><a href="https://cymulate.com/blog/kerberos-authentication-relay-via-cname-abuse/">Kerberos Authentication Relay via DNS CNAME Abuse</a></li>

</ul>
</details>

**标签**: `#AD CS`, `#ESC1`, `#ESC8`, `#Kerberos`, `#help desk impersonation`, `#intrusion analysis`

---

<a id="item-13"></a>
## [Nathan Lambert 在“黑色十月”后重新审视开放模型的网络风险](https://www.interconnects.ai/p/was-i-wrong-about-open-models-and) ⭐️ 7.0/10

Interconnects 通讯作者 Nathan Lambert 发表分析文章，重新审视他此前关于开放权重 AI 模型与网络风险的立场。促使他反思的是他称为“黑色十月”的一波严重漏洞披露，包括 PHP2Shell 和一个严重的 GitLab 漏洞。 这篇文章直接介入 AI 安全与安全政策辩论：如果 AI 赋能的网络威胁正在成为现实，限制开放权重模型的论点可能获得更多支持；但 Lambert 指出，近期黑客事件中闭源模型出现得很多，这使“开放性是主要祸根”的叙事变得复杂。 该分析属于观点评论，而非一手研究或官方公告；文章主张网络风险本质上是社会问题，仅靠 AI 公司无法解决，因此需要在更高层面投入努力。

rss · Interconnects AI · Oct 30, 17:36

**背景**: 开放权重模型是指训练参数可公开下载的 AI 系统，任何人都能运行或微调，这与只能通过 API 访问的闭源模型不同。“黑色十月”指一波严重漏洞披露，例如 PHP2Shell（CVE-2026-109618 和 CVE-2026-109619），它允许攻击者在无需认证的情况下在 PHP Web 服务器上远程执行代码，以及一个严重的 GitLab 漏洞；这些事件加剧了人们对 AI 可能加速网络攻击的担忧。英国 AI 安全研究所（AISI）一直在评估领先的开放权重模型在网络能力上落后前沿模型多远，使这成为一个现实的政策问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.interconnects.ai/p/was-i-wrong-about-open-models-and">Was I wrong about open models & cyber risks ?</a></li>
<li><a href="https://www.vulncheck.com/blog/php2shell-vulnerabilities">PHP 2 Shell Vulnerabilities : CVE-2026-109618 and... | VulnCheck</a></li>
<li><a href="https://www.aisi.gov.uk/blog/how-far-behind-the-frontier-are-leading-open-weight-models-on-cyber">How Far Behind the Frontier are Leading Open Weight Models on...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#open models`, `#cyber risk`, `#vulnerability disclosure`, `#AI policy`

---

<a id="item-14"></a>
## [JEPA 可跨模态学到统一表征，文本 JEPA 对齐优于 72B 语言模型](https://huggingface.co/papers/2610.39302) ⭐️ 7.0/10

一篇新论文声称，联合嵌入预测架构（JEPA）能够跨模态学习到统一的表征，并且将文本 JEPA 与图像编码器对齐后，在对齐任务上优于所测试的参数量高达 72B 的语言模型。 如果得到验证，这表明像 JEPA 这样的潜在空间预测目标可能比扩展自回归语言模型提供更高效的多模态对齐路径，这可能会重塑视觉-语言系统的构建方式。 该主张基于一份简短摘要，未公布方法、基准测试或独立复现，因此与 72B 参数语言模型的比较应被视为初步且未经证实。

rss · BALA AI News · Oct 30, 14:31

**背景**: JEPA（联合嵌入预测架构）是一种自监督框架，它通过预测缺失输入片段的抽象潜在表征来学习，而不是重建原始像素或生成 token。文本 JEPA 将这一思想应用于文本，将同一含义的不同表面形式视为等价目标，而非不同的 token。跨模态表征学习旨在将文本和图像等不同模态映射到共享的语义空间，这正是本文要解决的核心问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.turingpost.com/p/jepa">JEPA : Joint Embedding Predictive Architecture Explained</a></li>
<li><a href="https://www.emergentmind.com/topics/ti-jepa">TI- JEPA : Joint Embedding for Text - Image Alignment</a></li>
<li><a href="https://github.com/sofiabod/TEXT-JEPA">GitHub - sofiabod/ TEXT - JEPA : JEPA for text. sentences are...</a></li>

</ul>
</details>

**标签**: `#JEPA`, `#multimodal learning`, `#representation learning`, `#AI research`, `#language models`

---

