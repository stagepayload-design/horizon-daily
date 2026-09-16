# Horizon 每日速递 - 2026-05-29

> From 28 items, 10 important content pieces were selected

---

1. [Anthropic 以 9650 亿美元估值完成 650 亿美元 H 轮融资](#item-1) ⭐️ 9.0/10
2. [CISA 警告通过 Nx Console 和 GitHub 的供应链攻击](#item-2) ⭐️ 9.0/10
3. [分析 LLM 写作气味](#item-3) ⭐️ 8.0/10
4. [Postgres 作为持久化工作流的唯一后端](#item-4) ⭐️ 8.0/10
5. [GitHub 因零日 Windows 漏洞封禁安全研究员](#item-5) ⭐️ 8.0/10
6. [Casdoor IAM 平台遭受多项严重漏洞攻击](#item-6) ⭐️ 8.0/10
7. [Anthropic 发布 Claude Opus 4.8，预告 Mythos 模型](#item-7) ⭐️ 7.0/10
8. [学生在宿舍打造百万美元键盘控制器](#item-8) ⭐️ 7.0/10
9. [互动文章讽刺 AI 驱动的阶级分化](#item-9) ⭐️ 7.0/10
10. [异步智能体时代：Devin 工作流与智能体记忆](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Anthropic 以 9650 亿美元估值完成 650 亿美元 H 轮融资](https://www.anthropic.com/news/series-h) ⭐️ 9.0/10

Anthropic 宣布完成由 Altimeter Capital、Dragoneer、Greenoaks 和 Sequoia Capital 领投的 650 亿美元 H 轮融资，投后估值达 9650 亿美元。该公司还报告其年化经常性收入达到 470 亿美元，在收入和估值上均超过 OpenAI。 本轮融资标志着 AI 行业的重大转变，Anthropic 超越 OpenAI 成为估值最高的私营 AI 公司。巨大的估值和收入增长表明企业对 Claude 的强劲需求，可能加速 AI 在各行业的应用。 650 亿美元的融资额是历史上最大的私募融资轮之一，9650 亿美元的估值使 Anthropic 接近成为“千角兽”（估值达 1 万亿美元的公司）。该公司 470 亿美元的年化经常性收入较 2026 年 4 月报告的 300 亿美元大幅增长。

hackernews · meetpateltech · May 28, 18:09 · [社区讨论](https://news.ycombinator.com/item?id=48313048)

**背景**: H 轮融资是面向成熟初创公司的后期风险投资轮，旨在实现大规模增长或为退出做准备。投后估值是指投资完成后公司的即时价值。Anthropic 开发了 Claude AI 助手，与 OpenAI 的 ChatGPT 直接竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/series-h">Anthropic raises $65B in Series H funding at $965B post-money...</a></li>
<li><a href="https://startupheroes.io/startups/glossary/series-h-funding/">What is Series H Funding ?</a></li>
<li><a href="https://angelinvestorsnetwork.com/startups/valuationpost-money-valuation-explained-for-founders">Post - Money Valuation Explained for Founders</a></li>

</ul>
</details>

**社区讨论**: 评论者指出 Anthropic 在收入和估值上已超越 OpenAI，有人称 OpenAI“摇摇欲坠且脆弱”。其他人讨论了年化经常性收入的概念，以及公司更长时间保持私有、估值接近 1 万亿美元才上市的趋势。

**标签**: `#AI`, `#funding`, `#Anthropic`, `#valuation`, `#industry-news`

---

<a id="item-2"></a>
## [CISA 警告通过 Nx Console 和 GitHub 的供应链攻击](https://www.cisa.gov/news-events/alerts/2026/05/28/supply-chain-compromises-impact-nx-console-and-github-repositories) ⭐️ 9.0/10

CISA 发布了关于针对开发者生态系统的活跃供应链攻击的警报，包括通过恶意 Nx Console VS Code 扩展（版本 18.95.0）入侵 GitHub，以及“Megalodon”活动注入恶意 GitHub Actions 工作流。 这些攻击破坏了受信任的开发工具和 CI/CD 管道，可能影响依赖 GitHub 和 Nx Console 的数千个组织，导致源代码和秘密被未经授权访问。 恶意 Nx Console 扩展通过 VS Code 的自动更新机制分发，因此安装了该扩展的用户可能无需手动操作就收到了它。CVE-2026-48027 已被分配并添加到 CISA 的 KEV 目录中。

rss · CISA Cybersecurity Advisories · May 28, 12:00

**背景**: 供应链攻击通过破坏开发者信任的工具和流程来针对软件开发生命周期。Nx Console 是一个用于 Nx 工作区的流行 VS Code 扩展，GitHub Actions 是一个 CI/CD 平台。攻击者利用自动更新和 CI/CD 管道来分发恶意软件并窃取凭据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nx.dev/getting-started/editor-setup">Learn about Nx Console , an extension for VS Code and WebStorm.</a></li>
<li><a href="https://marketplace.visualstudio.com/items?itemName=nrwl.angular-console">Nx Console - Visual Studio Marketplace</a></li>
<li><a href="https://dev.to/manoit/cicd-pipeline-supply-chain-attacks-surge-2026-security-response-strategy-3n44">CI / CD Pipeline Supply Chain Attacks Surge... - DEV Community</a></li>

</ul>
</details>

**标签**: `#supply chain security`, `#CI/CD`, `#VS Code extension`, `#GitHub compromise`, `#CISA alert`

---

<a id="item-3"></a>
## [分析 LLM 写作气味](https://shvbsle.in/various-llm-smells/) ⭐️ 8.0/10

一篇题为《各种 LLM 气味》的文章列举了 LLM 生成文本中常见的风格模式，如“honest caveat”和“load bearing”，并讨论了如何检测和避免这些模式。 随着 LLM 被广泛用于写作辅助，识别这些模式有助于写作者保持独特风格，避免生成千篇一律、可被检测的 AI 输出。 文章列举了“The honest caveat:”和“blast radius”等具体例子，社区评论还补充了对比否定（“It's not X, it's Y”）等模式。

hackernews · speckx · May 28, 19:02 · [社区讨论](https://news.ycombinator.com/item?id=48313810)

**背景**: LLM 写作气味是指大型语言模型生成文本中频繁出现的风格化特征，通常源于训练数据偏差和提示模式。检测这些气味有助于用户优化提示词并编辑输出，使其听起来更自然。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://shvbsle.in/various-llm-smells/">Various LLM smells | Shiv After Dark</a></li>
<li><a href="https://iamwillwang.com/notes/llm-isms/">Stylistic smells in LLM writing .</a></li>
<li><a href="https://dbuschek.medium.com/when-llms-write-our-papers-1cc746373cd0">When LLMs Write Our Papers. Four issues I notice as... | Medium</a></li>

</ul>
</details>

**社区讨论**: 评论者如 tptacek 建议使用 LLM 进行批评而非直接生成，以保留个人风格；其他人则警告用户在不熟悉的领域可能高估 LLM 输出质量。

**标签**: `#LLM`, `#writing`, `#AI detection`, `#prompt engineering`, `#quality`

---

<a id="item-4"></a>
## [Postgres 作为持久化工作流的唯一后端](https://www.dbos.dev/blog/postgres-is-all-you-need-for-durable-execution) ⭐️ 8.0/10

DBOS 的一篇博客文章探讨了如何将 Postgres 作为持久化工作流执行的唯一后端，从而消除对 Temporal 等独立工作流引擎的需求。 这种方法通过将状态管理和工作流执行统一到单个数据库中，简化了技术栈，可能降低后端系统的运维复杂性和成本。 文章讨论了利用 Postgres 的事务性 DDL、咨询锁和 LISTEN/NOTIFY 等特性来实现持久化工作流，并与 Temporal、DBOS 和 absurd 等替代方案进行了比较。

hackernews · KraftyOne · May 28, 18:41 · [社区讨论](https://news.ycombinator.com/item?id=48313530)

**背景**: 持久化工作流确保长时间运行的过程在故障后能够存活并从断点继续执行。传统上，这需要像 Temporal 这样的专用工作流引擎，增加了复杂性。Postgres 作为成熟的关系型数据库，已经提供了 ACID 事务和可靠性，使其成为直接管理工作流状态的候选方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/safetycultureengineering/building-resilient-microservice-workflows-with-temporal-a-next-gen-workflow-engine-a9637a73572d">Building Resilient Microservice Workflows with Temporal ... | Medium</a></li>
<li><a href="https://www.baeldung.com/java-temporal-workflow-engine">Getting Started With the Temporal Workflow Engine in Java | Baeldung</a></li>
<li><a href="https://temporal.io/blog/workflow-engine-principles">Workflow Engine Design Principles | Temporal</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了使用 Temporal、DBOS 和 absurd 等替代方案的经验，指出 Temporal 中存在负载大小限制等问题。一些人表示有兴趣将状态存储和工作流逻辑统一到 Postgres 中，而另一些人则指出了现有的实现，如 Conductor OSS 和自定义驱动程序。

**标签**: `#Postgres`, `#durable workflows`, `#backend engineering`, `#state management`, `#Temporal`

---

<a id="item-5"></a>
## [GitHub 因零日 Windows 漏洞封禁安全研究员](https://www.tomshardware.com/tech-industry/cyber-security/microsofts-github-bans-security-researcher-who-posted-zero-day-windows-exploits-because-company-ruined-their-life-expert-claims-action-is-vindictive-and-promises-further-retaliation) ⭐️ 8.0/10

GitHub 封禁了一名发布 Windows 零日漏洞的安全研究员，该研究员指责此举是报复行为，并威胁将采取进一步报复措施。 这一事件凸显了软件厂商与安全研究员之间日益紧张的关系，尤其是在漏洞赏金计划和披露政策方面，可能会阻碍负责任的披露行为。 据报道，该研究员借助 AI 发现了这些零日漏洞，并在被封禁前未从微软获得任何补偿。社区猜测该研究员可能会将漏洞出售给其他方。

hackernews · possibilistic · May 28, 21:45 · [社区讨论](https://news.ycombinator.com/item?id=48315968)

**背景**: 零日漏洞利用是指针对软件厂商未知的漏洞进行攻击，在补丁发布前即可造成危害。漏洞赏金计划旨在激励研究人员私下报告漏洞，但关于报酬和披露方式的争议可能导致漏洞公开和封禁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zero-day_vulnerability">Zero - day vulnerability - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bug_bounty_program">Bug bounty program - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论观点不一：一些人批评微软可能迫使研究人员将漏洞出售给其他方，而另一些人则质疑研究人员的动机，并指出厂商团队通常有动力支付赏金。还有人对 AI 在发现漏洞中的作用进行了猜测。

**标签**: `#security`, `#zero-day`, `#GitHub`, `#Microsoft`, `#bug bounty`

---

<a id="item-6"></a>
## [Casdoor IAM 平台遭受多项严重漏洞攻击](https://kb.cert.org/vuls/id/780781) ⭐️ 8.0/10

CERT/CC 披露了 Casdoor 2.362.0 及更早版本中的七个漏洞（CVE-2026-9090 至 CVE-2026-9096），可实现身份验证绕过、多因素认证绕过、权限提升以及 SAML 断言重放。 Casdoor 是一个广泛使用的开源 IAM 平台；这些漏洞可能允许攻击者冒充任何用户（包括管理员），并在组织间获得持久的未授权访问。 这些漏洞包括 SAML 证书信任绕过（CVE-2026-9090）、社交登录中的 MFA 绕过（CVE-2026-9091）、未经验证的邮箱绑定（CVE-2026-9092）、缺少 AudienceRestriction 验证（CVE-2026-9093）、跨组织令牌交换（CVE-2026-9094）以及缺少 SAML 重放保护（CVE-2026-9095）。

rss · CERT CC Vulnerability Notes · May 28, 16:13

**背景**: Casdoor 是一个开源的身份与访问管理（IAM）平台，提供单点登录（SSO）并支持多种协议，包括 SAML、OAuth 2.0 和 OIDC。它还作为 AI 代理的模型上下文协议（MCP）网关。SAML 是一种基于 XML 的标准，用于在身份提供商和服务提供商之间交换身份验证和授权数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/casdoor/casdoor">GitHub - casdoor / casdoor : An open-source Agent-first Identity and...</a></li>
<li><a href="https://casdoor.ai/">Casdoor · AI-Native Identity and Access Management ( IAM ) / SSO...</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#authentication bypass`, `#Casdoor`, `#IAM`

---

<a id="item-7"></a>
## [Anthropic 发布 Claude Opus 4.8，预告 Mythos 模型](https://www.anthropic.com/news/claude-opus-4-8) ⭐️ 7.0/10

Anthropic 发布了 Claude Opus 4.8，相比前代有适度但切实的提升，并宣布了 Project Glasswing 下的新 'Mythos' 模型类别，该模型已在部分组织中进行网络安全测试。 此次发布表明 Anthropic 在前沿模型上持续迭代，而 Mythos 的预告则预示着 AI 能力的重大飞跃，尤其是在网络安全领域。在网页界面中切换自适应思考的功能也解决了用户的常见痛点。 Opus 4.8 在智能体编码、推理、金融分析和知识工作等基准测试中优于竞争对手。现在网页界面中提供了自适应思考开关，用户可以在其降低输出质量时将其关闭。

hackernews · craigmart · May 28, 16:49 · [社区讨论](https://news.ycombinator.com/item?id=48311647)

**背景**: Anthropic 的 Claude 模型是大型语言模型（LLM），与 OpenAI 的 GPT 和 Google 的 Gemini 竞争。Opus 是 Anthropic 能力最强的模型类别，4.x 系列已经历多次小版本更新（4.5、4.6、4.7、4.8）。Project Glasswing 是一项内部计划，旨在开发具有更强安全措施的下一代 AI 系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/crk1py1jgzko">What is Anthopic's Claude Mythos and what risks does it pose?</a></li>
<li><a href="https://www.axios.com/2026/05/28/anthropic-opus-release-mythos">A Mythos - class model is expected in the coming weeks.</a></li>
<li><a href="https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-confirms-claude-mythos-class-models-will-roll-out-to-the-public/">Anthropic confirms Claude Mythos - class models will roll out to the...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论热烈，用户指出这是 Anthropic 前沿模型首次经历三次小版本更新，每次提升幅度不大。一些用户对能够关闭自适应思考表示赞赏，而另一些用户则强调了在构建 RTS 游戏等基准测试中的出色编码表现。

**标签**: `#AI`, `#Anthropic`, `#Claude`, `#LLM`, `#Frontier Models`

---

<a id="item-8"></a>
## [学生在宿舍打造百万美元键盘控制器](https://nick.winans.io/blog/nice-nano/) ⭐️ 7.0/10

学生 Nick Winans 在宿舍开发并销售了价值超过 100 万美元的 Nice!Nano 无线键盘控制器，在机械键盘小众社区中取得了成功。 这个故事表明，个人可以通过瞄准热情的小众社区，在没有传统风险投资或制造资源的情况下，创造出高利润的硬件产品。 Nice!Nano 是一款用于 DIY 机械键盘的开源无线控制器，支持蓝牙和 Zephyr RTOS。到 2025 年，该产品销售额超过 100 万美元，主要通过 Discord 和 Reddit 上的社区驱动营销实现。

hackernews · mattrighetti · May 28, 20:25 · [社区讨论](https://news.ycombinator.com/item?id=48314951)

**背景**: 机械键盘爱好者社区经常从头开始构建定制键盘，需要控制器来管理按键和连接。像 Nice!Nano 这样的无线控制器支持蓝牙连接，这对于整洁的桌面设置非常受欢迎。在美国，有意辐射器需要 FCC 认证，以确保它们不会造成有害干扰。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://compliancetesting.com/tested-to-comply-with-fcc-standards/">What Does “Tested to Comply With FCC ...” - Compliance Testing</a></li>
<li><a href="https://xyztech.com/blogs/power-bank/understanding-ce-fcc-rohs-and-other-electronic-certifications">CE, FCC , ROHS & Other Certifications: What Do They Mean? – XYZtech</a></li>

</ul>
</details>

**社区讨论**: 评论者赞扬了这一成就，但也提出了关于营销策略和 FCC 合规性的问题。一位用户指出该产品作为有意辐射器缺少 FCC ID，而另一位用户则好奇该产品如何在许多类似项目失败的情况下获得成功。

**标签**: `#hardware`, `#entrepreneurship`, `#keyboard`, `#wireless`, `#product-development`

---

<a id="item-9"></a>
## [互动文章讽刺 AI 驱动的阶级分化](https://permanent-upper-crow.jasonwu.ink/) ⭐️ 7.0/10

一篇名为《永久的上层乌鸦》的互动文章发布，讽刺了 AI 驱动的阶级分化和地位追求，灵感来自作者在 AI 领域的经历。 这篇文章对 AI 炒作和炫耀性消费进行了文化批判，引起了 Hacker News 社区的共鸣，并引发了关于 AI 社会影响的讨论。 文章包含 106 位 CEO/公司，在第 107 个时循环；作者表示这是一时兴起在一天内完成的，灵感来自 AI 领域的对话。

hackernews · whiteblossom · May 28, 15:23 · [社区讨论](https://news.ycombinator.com/item?id=48310280)

**背景**: 该文章采用类似游戏的形式，批判 AI 炒作可能加剧阶级分化，与科技文化中的炫耀性消费和地位游戏相类比。

**社区讨论**: 评论者指出作者本人是一家自动化工作的 AI 初创公司联合创始人的讽刺性，其他人则将其比作“被提”和地位游戏的徒劳。作者对关注度表示感谢，并对未来抱有希望。

**标签**: `#AI`, `#societal impact`, `#satire`, `#class dynamics`, `#tech culture`

---

<a id="item-10"></a>
## [异步智能体时代：Devin 工作流与智能体记忆](https://www.latent.space/p/cognition) ⭐️ 7.0/10

一期播客邀请了 Cognition 的 Walden Yan 和 OpenInspect 的 Cole Murray，讨论异步 AI 智能体的兴起，包括 Devin 的提交工作流、从规格到 PR 的流水线、完整虚拟机使用、智能体记忆以及产品经理直接发布代码。 这次讨论突显了软件工程领域的范式转变，AI 智能体以异步方式运行，可能自动化大部分开发工作流，并让产品经理等非工程师也能发布代码。 播客涵盖了 Devin 使用完整虚拟机并在会话间保持智能体记忆的能力，从而能够执行复杂的多步骤任务，例如将规格直接转换为拉取请求。

rss · Latent Space · May 28, 18:41

**背景**: AI 智能体是能够规划、使用工具并适应反馈的系统，不同于简单的聊天机器人。异步智能体可以独立运行，无需持续的人类输入即可处理任务。智能体记忆使这些系统能够在会话间保留上下文，这对于长时间运行的工作流至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cli.devin.ai/">Quickstart - Devin CLI</a></li>
<li><a href="https://www.linkedin.com/pulse/architecture-memory-agentic-ai-systems-part-1-giridhar-thoopurani-3xzac">The Architecture of Memory in Agentic AI Systems (Part 1)</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#software engineering`, `#workflow automation`, `#Devin`, `#async agents`

---

