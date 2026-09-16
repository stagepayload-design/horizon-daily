# Horizon 每日速递 - 2026-07-10

> From 39 items, 14 important content pieces were selected

---

1. [欧盟议会批准大规模消息扫描至 2028 年](#item-1) ⭐️ 9.0/10
2. [OpenAI 发布 GPT-5.6，在 ARC-AGI-3 上达到 SOTA](#item-2) ⭐️ 9.0/10
3. [腾讯 Hy3：小型 LLM 与 DeepSeek Flash V4 竞争](#item-3) ⭐️ 8.0/10
4. [用 Rust 重写的 Postgres 通过全部回归测试](#item-4) ⭐️ 8.0/10
5. [美国陆军后勤系统脆弱，下一场战争可能崩溃](#item-5) ⭐️ 8.0/10
6. [Meta 推出付费代理型 AI 模型 Muse Spark 1.1](#item-6) ⭐️ 8.0/10
7. [内部服务 TLS：ACME DNS-01 与分裂 DNS 之争](#item-7) ⭐️ 8.0/10
8. [PayRange Android 应用 7.0.7 存在严重 SSL 和 JS 注入漏洞](#item-8) ⭐️ 8.0/10
9. [Xerte Online Toolkit 认证绕过导致远程代码执行](#item-9) ⭐️ 8.0/10
10. [OpenAI 启动生物漏洞赏金计划](#item-10) ⭐️ 8.0/10
11. [SpaceXAI 发布 Grok 4.5，首个 Opus 级模型](#item-11) ⭐️ 8.0/10
12. [在 32GB 内存笔记本上运行 GLM 5.2](#item-12) ⭐️ 7.0/10
13. [Mitchell Hashimoto 谈 Ghostty 为何选择 Zig 而非 Rust](#item-13) ⭐️ 7.0/10
14. [GLM 5.2 在记账方面接近人类水平](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [欧盟议会批准大规模消息扫描至 2028 年](https://www.patrick-breyer.de/en/eu-parliament-greenlights-chat-control-1-0-breyer-our-children-lose-out/) ⭐️ 9.0/10

欧洲议会批准了“聊天控制 1.0”法案，允许美国科技公司在无搜查令的情况下扫描私人消息，有效期至 2028 年，尽管多数投票的欧洲议会议员反对该措施。 这一决定标志着欧盟数字隐私权的重大转变，允许对私人通信进行大规模监控，并开创了可能削弱加密和用户信任的先例。 否决该法规的动议未能通过，因为它需要全体 720 名欧洲议会议员的绝对多数（361 票），而不仅仅是投票者的多数；只有 314 票反对，276 票赞成，17 票弃权，113 人缺席。

hackernews · rapnie · Jul 9, 11:03 · [社区讨论](https://news.ycombinator.com/item?id=48843923)

**背景**: “聊天控制 1.0”最初在 2024 年 3 月被两次否决，但通过紧急程序被重新启动。该法律允许在无事先怀疑的情况下，扫描 Instagram、Discord、Snapchat、Skype、Xbox、Gmail 和 iCloud 等平台上的直接消息，以查找非法内容。

**社区讨论**: 评论者对议会的操作手法表示愤怒，指出投票安排在暑假前，许多议员已经离开，而要求绝对多数才能否决法律的规定实际上让少数人通过了该法。有人称这是“极权主义”举动，损害了欧盟的合法性。

**标签**: `#privacy`, `#surveillance`, `#EU legislation`, `#digital rights`, `#encryption`

---

<a id="item-2"></a>
## [OpenAI 发布 GPT-5.6，在 ARC-AGI-3 上达到 SOTA](https://openai.com/index/gpt-5-6/) ⭐️ 9.0/10

OpenAI 发布了 GPT-5.6，这是一款新的前沿模型，在 ARC-AGI-3 基准测试上达到了最先进的性能，并引入了改进的意图理解和图像处理能力。 此次发布标志着 AI 推理和泛化能力的重大进步，因为 GPT-5.6 是首个在 ARC-AGI-3 游戏中获胜的经过验证的前沿模型。它还通过更好的意图理解增强了开发者体验，可能减少对显式逐步指令的需求。 GPT-5.6 在 ARC-AGI-3 上达到 7.8%，创下新的 SOTA。该模型在处理图像时保留原始图像尺寸，其开发者指南强调了改进的意图理解能力，可以在不指定每个步骤的情况下推断用户目标。

hackernews · OpenAI Blog · Jul 9, 17:04 · [社区讨论](https://news.ycombinator.com/item?id=48849066)

**背景**: ARC-AGI（人工通用智能抽象与推理语料库）是一个基准测试，旨在衡量 AI 从少量示例中推理和泛化的能力，常被视为通用智能的代理指标。GPT-5.6 是 OpenAI GPT 系列的最新模型，继 GPT-5.5 之后推出，可通过 OpenAI API 和 Codex 应用使用。

**社区讨论**: 社区评论褒贬不一：一些用户称赞在 ARC-AGI-3 上取得的新 SOTA 和改进的意图理解，而另一些用户则将其与 Claude Code 和 Sonnet 5 等模型比较，指出 GPT-5.6 的编码性能与 GPT-5.5 相似，略逊于 Sonnet 5。也有人对基准比较持怀疑态度，一位评论者指出 OpenAI 默认将某个竞争对手排除在某些基准之外。

**标签**: `#AI`, `#OpenAI`, `#GPT-5.6`, `#LLM`, `#ARC-AGI`

---

<a id="item-3"></a>
## [腾讯 Hy3：小型 LLM 与 DeepSeek Flash V4 竞争](https://hy.tencent.com/research/hy3) ⭐️ 8.0/10

腾讯发布了 Hy3，这是一个小型但功能强大的大语言模型，现已在 OpenRouter 上提供，免费使用至 7 月 21 日。该模型因其与 DeepSeek Flash V4 相比具有竞争力的定价和性能而引发讨论。 Hy3 表明小型模型在能力上可以媲美大型模型，可能降低用户成本并支持本地部署。它与 DeepSeek Flash V4 的竞争性定价可能改变 LLM 市场格局。 Hy3 比 DeepSeek V4 Flash 稍大，但据报道在某些基准测试上匹配或超过 DeepSeek V4 Pro。目前在 OpenRouter 上的有效输入价格与 DeepSeek 托管的 DeepSeek Flash V4 相同。

hackernews · andai · Jul 9, 15:27 · [社区讨论](https://news.ycombinator.com/item?id=48847552)

**背景**: 大语言模型（LLM）是在大量文本数据上训练的人工智能系统，用于生成类似人类的文本。像 Hy3 这样的小型模型旨在平衡性能和计算效率，使其对成本敏感的应用和本地部署具有吸引力。

**社区讨论**: 社区成员注意到 Hy3 在其尺寸下具有令人惊讶的能力，有人建议它可能成为流行的本地模型。然而，一位评论者质疑其相对于竞争对手的价值，指出其在 OpenRouter 上的排名已经下降。

**标签**: `#AI/ML`, `#LLM`, `#model release`, `#Tencent`, `#OpenRouter`

---

<a id="item-4"></a>
## [用 Rust 重写的 Postgres 通过全部回归测试](https://github.com/malisper/pgrust) ⭐️ 8.0/10

一个名为 pgrust 的项目使用大语言模型将 PostgreSQL 数据库用 Rust 重写，并 100%通过了 Postgres 回归测试套件。 这展示了使用 AI 生成代码将大型成熟代码库重写为内存安全语言的可行性，有望提升安全性和性能，同时也引发了关于代码质量和许可证的讨论。 该项目使用大语言模型生成与 Postgres 行为一致的 Rust 代码，作者指出重写的许多技术也适用于数据库的重构。

hackernews · SweetSoftPillow · Jul 9, 06:18 · [社区讨论](https://news.ycombinator.com/item?id=48841676)

**背景**: PostgreSQL 是一个有 30 年历史的用 C 语言编写的关系型数据库。Rust 是一种现代系统语言，无需垃圾回收即可提供内存安全。用 Rust 重写关键基础设施是减少安全漏洞的一个日益增长的趋势。

**社区讨论**: 社区讨论了测试策略（如镜像生产流量）、审查 LLM 生成代码的挑战（一个月内 7101 次提交）以及许可证问题——pgrust 使用了 AGPL 而非原 PostgreSQL 许可证。

**标签**: `#Postgres`, `#Rust`, `#LLM`, `#database`, `#rewrite`

---

<a id="item-5"></a>
## [美国陆军后勤系统脆弱，下一场战争可能崩溃](https://mwi.westpoint.edu/the-glass-backbone-why-the-armys-logistics-will-break-in-the-next-war/) ⭐️ 8.0/10

《现代战争研究所》的一篇文章指出，美国陆军后勤系统过度依赖脆弱的供应链，将在重大冲突中崩溃，这与二战等历史教训相呼应。 该分析揭示了美国军事战备中的关键弱点，后勤失败可能削弱其在对等对手（如中国或俄罗斯）高强度冲突中的作战效能。 文章批评陆军关注“牙齿与尾巴比率”和预算优先事项，忽视了后勤现代化，并警告精确弹药和复杂系统在战时难以快速补充。

hackernews · baud147258 · Jul 9, 13:24 · [社区讨论](https://news.ycombinator.com/item?id=48845442)

**背景**: 后勤——军队的调动和补给——在历史上对战争胜负具有决定性作用。美国陆军目前依赖全球供应链获取零部件和燃料，这可能因敌方对港口、机场或网络基础设施的攻击而中断。

**社区讨论**: 评论者大多同意文章的观点，引用了对抗汉尼拔的费边战略和现代无人机战争等历史例子。一些人讨论了 SpaceX 星舰等新技术对后勤的影响，另一些人则指出自二战以来美国工业基础已经萎缩。

**标签**: `#military logistics`, `#systems thinking`, `#strategic analysis`, `#supply chain`

---

<a id="item-6"></a>
## [Meta 推出付费代理型 AI 模型 Muse Spark 1.1](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/) ⭐️ 8.0/10

Meta 发布了 Muse Spark 1.1，这是一个通过 API 访问的付费代理型 AI 模型，并附有详细的评估报告和开发者资源。 这标志着 Meta 开始将其 AI 模型商业化，以更低的价格和强劲的性能提供了 OpenAI 和 Anthropic 的竞争替代方案。 定价为每百万输入 token 1.25 美元，每百万输出 token 4.5 美元，缓存输入为 0.15 美元。该模型专为代理型任务设计，并包含一个仅限 bash 工具的评估框架。

hackernews · ot · Jul 9, 14:10 · [社区讨论](https://news.ycombinator.com/item?id=48846184)

**背景**: 代理型 AI 模型可以自主执行编码或系统管理等任务。Meta 此前发布了 Llama 等开放权重模型，但 Muse Spark 1.1 是一个付费的封闭 API 模型。

**社区讨论**: 社区评论关注基准测试方法问题（例如在 Terminal-Bench 中覆盖 CPU/RAM 限制），并称赞其低定价。Simon Willison 创建了 LLM 插件以便于访问，一些人认为这是 Meta 在削弱竞争对手。

**标签**: `#AI`, `#Meta`, `#agentic model`, `#API`, `#machine learning`

---

<a id="item-7"></a>
## [内部服务 TLS：ACME DNS-01 与分裂 DNS 之争](https://tuxnet.dev/posts/tls-for-internal-services/) ⭐️ 8.0/10

一篇关于使用 ACME 和 DNS 验证管理内部服务 TLS 证书的详细指南发布，引发了社区关于分裂 DNS 与 DNS-01 挑战优劣的辩论。 这场讨论凸显了使用受信任证书保护内部服务的持续挑战，这对于转向零信任架构和自动化证书管理的组织至关重要。 该指南推荐使用 Let's Encrypt 的 DNS-01 验证以避免分裂 DNS 的复杂性，而一些评论者则倾向于使用 step-ca 等内部 CA 以获得完全控制。

hackernews · mrl5 · Jul 9, 14:57 · [社区讨论](https://news.ycombinator.com/item?id=48846995)

**背景**: TLS 证书对加密内部流量至关重要，但由于域名验证要求，从公共 CA 为内部服务获取证书存在困难。ACME 自动化证书签发，DNS-01 通过 DNS 记录进行验证，无需暴露内部服务。分裂 DNS 对同一域名在内外网返回不同 IP，增加了证书管理的复杂性。

**社区讨论**: 评论者普遍倾向于 DNS-01 验证而非分裂 DNS，认为其降低了复杂性和维护负担。一些人主张使用 step-ca 等内部 CA，另一些人指出使用通配符证书的 DNS-01 可以避免证书透明度日志中的名称泄露。

**标签**: `#TLS`, `#internal services`, `#ACME`, `#DNS`, `#certificate management`

---

<a id="item-8"></a>
## [PayRange Android 应用 7.0.7 存在严重 SSL 和 JS 注入漏洞](https://kb.cert.org/vuls/id/152953) ⭐️ 8.0/10

PayRange Android 应用 7.0.7 版本被披露存在两个漏洞（CVE-2026-13462 和 CVE-2026-13461），分别导致接受无效 SSL 证书以及通过 JavaScript 注入逃逸 WebView 沙箱。 这些漏洞可能允许中间人攻击者拦截敏感数据（包括凭证和支付信息），甚至向连接的硬件发出命令，影响广泛使用的 PayRange 支付应用的用户和机器操作员。 SSL 绕过接受通用名称以 'payrange.com' 结尾或包含 'stripe.com' 的证书，以及满足特定条件（涉及 'fetlifestatus.com'）的证书，包括自签名证书。JavaScript 注入可逃逸 WebView 沙箱，在设备上执行危险操作。

rss · CERT CC Vulnerability Notes · Jul 9, 17:03

**背景**: PayRange 是一款用于自动售货机和其他无人值守零售机的移动支付应用，使用蓝牙和互联网连接。Android 应用中的 WebView 用于显示网页内容但受沙箱保护；然而，不正确的 SSL 验证和 JavaScript 注入可能打破该沙箱。这些漏洞由研究员 Tahi Wilton Geary 发现并通过 CERT/CC 报告。

**标签**: `#security`, `#vulnerability`, `#android`, `#mobile payment`, `#CVE`

---

<a id="item-9"></a>
## [Xerte Online Toolkit 认证绕过导致远程代码执行](https://kb.cert.org/vuls/id/734812) ⭐️ 8.0/10

Xerte Online Toolkit 中披露了两个严重漏洞（CVE-2026-14261 和 CVE-2026-12116），允许未经认证的攻击者绕过认证并实现远程代码执行。已发布修复版本 v3.15.5 和 v3.14.6。 Xerte 是一个广泛使用的开源电子学习平台；这些漏洞可能允许攻击者获得服务器的完全控制权、窃取数据或向学习者分发恶意内容。所有受影响安装应立即修补。 CVE-2026-14261 利用安装后残留的 /setup/ 目录，允许重新配置到攻击者控制的数据库。CVE-2026-12116 允许将防病毒二进制路径更改为 PHP 解释器，导致上传的文件作为 PHP 代码执行。

rss · CERT CC Vulnerability Notes · Jul 9, 12:37

**背景**: Xerte Online Toolkit 是一个开源套件，用于在浏览器中创建交互式电子学习内容。它在安装过程中使用一个 setup 文件夹，该文件夹在安装后仍然可访问，并且有一个可由管理员修改的防病毒二进制路径设置。这些设计缺陷使得链式利用成为可能。

**标签**: `#security`, `#vulnerability`, `#RCE`, `#authentication bypass`, `#open-source`

---

<a id="item-10"></a>
## [OpenAI 启动生物漏洞赏金计划](https://openai.com/index/bio-bug-bounty) ⭐️ 8.0/10

OpenAI 宣布了一项生物漏洞赏金计划，旨在激励对人工智能相关生物风险的研究，并为识别人工智能在生物技术中可能被滥用的风险提供奖励。 该计划是人工智能安全领域的重要一步，解决了人工智能在生物技术中的双重用途问题，并鼓励在危害发生前主动识别风险。 该计划邀请研究人员提交关于人工智能模型如何被滥用以制造生物威胁的报告，奖励金额取决于发现的严重性和新颖性。

rss · OpenAI Blog · Jul 9, 10:00

**背景**: 人工智能模型，尤其是大型语言模型，可能被用于设计有害的生物制剂。漏洞赏金计划在网络安全领域很常见，但在生物风险领域是新颖的，反映了对人工智能安全日益增长的担忧。

**标签**: `#AI safety`, `#bounty program`, `#biotechnology`, `#OpenAI`

---

<a id="item-11"></a>
## [SpaceXAI 发布 Grok 4.5，首个 Opus 级模型](https://www.latent.space/p/ainews-spacexai-launches-grok-45) ⭐️ 8.0/10

SpaceXAI 在收购 Cursor 后发布了 Grok 4.5，这是其首个 Opus 级模型。这标志着该公司快速发展的一个重要里程碑。 Grok 4.5 代表了 AI 能力的飞跃，可能为行业树立新标杆。作为 Opus 级模型，它可能挑战其他前沿模型，并加速各领域的创新。 该模型被描述为“Opus 级”，表明它属于最强大、能力最强的模型之一。此次发布紧随 SpaceXAI 收购 Cursor 之后，暗示了新技术的整合。

rss · Latent Space · Jul 9, 06:05

**背景**: SpaceXAI 是一家领先的 AI 研究实验室，以开发先进语言模型而闻名。Opus 级模型通常指最高性能等级，可与 GPT-4 或 Claude 3 Opus 等模型相媲美。收购代码生成工具 Cursor 可能增强了该模型的能力。

**标签**: `#AI`, `#Grok`, `#SpaceXAI`, `#model release`, `#frontier lab`

---

<a id="item-12"></a>
## [在 32GB 内存笔记本上运行 GLM 5.2](https://github.com/JustVugg/colibri) ⭐️ 7.0/10

一位开发者创建了 Colibrì，这是一个轻量级的 C 语言引擎，通过 int4 量化和按需磁盘流式传输路由专家，在配备 32GB RAM 的普通 12 核笔记本上运行了 744B 参数的 GLM 5.2 混合专家大语言模型。 这表明最先进的开源大语言模型可以在没有 GPU 的消费级硬件上运行，可能使个人和小团队也能使用强大的 AI 模型。 该引擎使用 int4 量化将约 17B 的密集参数常驻内存（约 9.9 GB），而 21,504 个路由专家（磁盘上约 370 GB）按需流式传输并带有 LRU 缓存，冷启动时达到每秒 0.1 个 token。

hackernews · vforno · Jul 9, 08:05 · [社区讨论](https://news.ycombinator.com/item?id=48842459)

**背景**: GLM 5.2 是一个 744B 参数的混合专家（MoE）模型，每个 token 仅激活约 40B 参数，比同等大小的密集模型更高效。Int4 量化将每个权重的精度降至 4 位，大幅降低内存需求，但会损失一些精度。按需磁盘流式传输仅从磁盘加载所需的专家权重，以速度换取内存。

**社区讨论**: 评论者对该方法表示兴趣，有人指出 0.1 tok/s 对于交互式使用太慢，但可用于隔夜批处理。其他人分享了针对 Apple Silicon 或 llama.cpp 修改的类似项目，还有人担心持续磁盘流式传输会加速 SSD 磨损。

**标签**: `#LLM`, `#optimization`, `#open-source`, `#quantization`, `#GLM`

---

<a id="item-13"></a>
## [Mitchell Hashimoto 谈 Ghostty 为何选择 Zig 而非 Rust](https://alexalejandre.com/programming/interview-with-mitchell-hashimoto/) ⭐️ 7.0/10

Ghostty 的创建者 Mitchell Hashimoto 在一次采访中解释了为何选择 Zig 而非 Rust 来开发终端模拟器，提到了文化和实用主义原因。 这一讨论凸显了 Zig 与 Rust 在实际应用中的权衡，影响开发者在性能关键型应用中的语言选择。 Hashimoto 指出，虽然 Rust 的理念很好，但他不喜欢 Rust 的文化，并发现 Zig 的简洁性更符合他对 Ghostty 的目标。

hackernews · veqq · Jul 9, 17:17 · [社区讨论](https://news.ycombinator.com/item?id=48849292)

**背景**: Ghostty 是一个用 Zig 编写的快速、功能丰富的终端模拟器。Zig 是一种注重简洁和控制性的底层系统语言，而 Rust 则强调安全性和零成本抽象。采访探讨了这两种语言在文化和技术上的差异。

**社区讨论**: 评论褒贬不一：一些人称赞 Hashimoto 的实用主义方法，另一些人则批评他的言论显得狭隘，并认为 Zig 社区可能与 Rust 社区一样负面。Zig 作者 Andrew Kelley 关于 Bun 的 Rust 重写的相关讨论提供了更多背景。

**标签**: `#Zig`, `#Ghostty`, `#terminal emulator`, `#programming languages`, `#software engineering`

---

<a id="item-14"></a>
## [GLM 5.2 在记账方面接近人类水平](https://toot-books.pages.dev/blog/glm-5-2-vat-benchmark) ⭐️ 7.0/10

GLM 5.2 在增值税记账基准测试中达到了接近人类的准确率，正确分类了 97.5% 的交易，而人类基准为 98.2%。 这一结果表明，LLM 能够以高准确率自动化核心记账任务，可能降低会计成本和错误，但也引发了关于责任以及人类记账员更广泛工作范围的担忧。 该基准测试仅测试了从银行流水和发票中进行交易分类，排除了查找发票或处理模糊情况等任务，这些任务通过用户备注模拟。模型的错误包括因描述模糊和缺少上下文导致的错误分类。

hackernews · adamkurkiewicz · Jul 9, 18:29 · [社区讨论](https://news.ycombinator.com/item?id=48850414)

**背景**: 记账涉及记录财务交易，通常用于增值税目的。像 GLM 5.2 这样的 LLM 正被用于自动化此类任务，但现实中的记账需要更广泛的技能，如查找发票和解释复杂情况。错误的责任仍然是一个关键问题，因为 LLM 无法承担法律责任。

**社区讨论**: 评论者指出，基准测试的范围比人类记账员的工作范围更窄，并提出了责任问题：如果 LLM 出错，谁去坐牢？一些人对 GLM 5.2 背后的公司缺乏透明度表示怀疑，而另一些人则认为通过改进知识库，自动化有潜力。

**标签**: `#LLM`, `#bookkeeping`, `#automation`, `#benchmark`, `#liability`

---

