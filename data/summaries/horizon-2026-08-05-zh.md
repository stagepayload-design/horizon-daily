# Horizon 每日速递 - 2026-08-05

> From 63 items, 22 important content pieces were selected

---

1. [Keyv 及相关 npm 包遭活跃 Shai-Hulud 供应链攻击](#item-1) ⭐️ 9.0/10
2. [Gwern 退出匿名写作，启动 Guardian Angel AI 项目](#item-2) ⭐️ 8.0/10
3. [Mistral 发布 Shieldstral，一款 3B 开源多模态审核模型](#item-3) ⭐️ 8.0/10
4. [DeepSeek V4 Flash 在单块 AMD MI300X 上运行，速度超 150 tok/s](#item-4) ⭐️ 8.0/10
5. [联邦快递钓鱼示例凸显域名混淆风险](#item-5) ⭐️ 8.0/10
6. [Oxide Computer 完成 4.45 亿美元 D 轮融资](#item-6) ⭐️ 8.0/10
7. [CISA 将三个已被积极利用的漏洞加入 KEV 目录](#item-7) ⭐️ 8.0/10
8. [LLM 0.32 新增推理轨迹、服务端工具与更智能的日志](#item-8) ⭐️ 8.0/10
9. [MLX 移植版让 MiniMax-H3 全模态模型在 Apple Silicon 上运行](#item-9) ⭐️ 8.0/10
10. [ChatGPT Work 架构与功能的外部解析](#item-10) ⭐️ 8.0/10
11. [Qwen 发布新的开源权重模型，面向编程与协作](#item-11) ⭐️ 8.0/10
12. [llama.cpp b10270 新增 Qwen3-TTS 支持并引入破坏性变更](#item-12) ⭐️ 7.0/10
13. [llama.cpp b10255 将 SYCL oneDNN SDPA 扩展到非 FP16 KV 缓存](#item-13) ⭐️ 7.0/10
14. [llama.cpp b10254 新增 DeepSeek V4 Flash 0731 聊天模板](#item-14) ⭐️ 7.0/10
15. [llama.cpp b10251 为 GLM-4.7-Flash 增加多令牌预测支持](#item-15) ⭐️ 7.0/10
16. [用于生成多样化肤色的自定义色彩空间与算法](#item-16) ⭐️ 7.0/10
17. [Waymo 在达拉斯全面开放无人驾驶打车服务](#item-17) ⭐️ 7.0/10
18. [Collab Word in Web：支持端到端加密和 AI 代理的协作 DOCX 编辑器](#item-18) ⭐️ 7.0/10
19. [开源智能眼镜实现手语指拼翻译](#item-19) ⭐️ 7.0/10
20. [Hyperlane：将代理工作树与原生 IDE 功能融合](#item-20) ⭐️ 7.0/10
21. [OpenAI 披露第三方网络评估事件，宣布新保障措施](#item-21) ⭐️ 7.0/10
22. [llm-anthropic 0.26 新增 Claude 模型与服务器端工具](#item-22) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Keyv 及相关 npm 包遭活跃 Shai-Hulud 供应链攻击](https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack) ⭐️ 9.0/10

供应链攻击入侵了 Keyv npm 包及其系列，向每个 package.json 添加了恶意文件（setup.mjs 和 Math_Symbol.js）以及 preinstall 钩子。该攻击正在活跃进行，影响所有在受影响版本上运行 npm install 的用户。 此次攻击凸显了 npm 依赖生态系统的脆弱性，广泛使用的包可能被入侵并传播恶意软件。它强调了采取更强安全措施的紧迫性，例如消除安装钩子和采用 devcontainers，以保护开发者和下游用户。 攻击向 Keyv 系列的每个 package.json 添加了两个新文件 setup.mjs 和 Math_Symbol.js，以及 "preinstall": "node setup.mjs" 条目。恶意代码在安装过程中自动执行，可能危及开发者的环境。

hackernews · cimi_ · Aug 4, 11:01 · [社区讨论](https://news.ycombinator.com/item?id=49166874)

**背景**: 供应链攻击针对软件供应链，通过入侵受信任的包向下游用户分发恶意软件。npm 包通常运行安装脚本（preinstall/postinstall）来执行任意代码，使其成为此类攻击的主要载体。Keyv 是 Node.js 中流行的缓存库，其被入侵可能影响许多依赖它的项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack">Keyv and friends compromised in npm supply chain attack</a></li>
<li><a href="https://dev.to/onsen/keyv-supply-chain-attack-what-you-need-to-know-now-1466">Keyv Supply Chain Attack : What You Need to... - DEV Community</a></li>

</ul>
</details>

**社区讨论**: 社区表达了担忧并呼吁采取行动：有人主张彻底取消 pre-install/post-install 钩子，也有人建议使用 devcontainers 隔离环境。一位开发者分享了用于检测供应链攻击的开源工具（Packj），另一位则询问如何用 grep 检查 node_modules 中是否存在恶意文件。

**标签**: `#supply chain`, `#security`, `#npm`, `#open source`, `#devcontainers`

---

<a id="item-2"></a>
## [Gwern 退出匿名写作，启动 Guardian Angel AI 项目](https://twitter.com/gwern/status/2084739205071343837) ⭐️ 8.0/10

著名 AI 研究者和作家 Gwern 宣布退出全职写作和匿名身份，启动名为 Guardian Angel (GA) 的新项目。该项目旨在通过创建优先考虑用户利益而非公司利益的个人 AI 助手，解决 AI 对齐和经济激励问题。 Gwern 从写作转向实际 AI 开发，反映出 AI 社区对当前 AI 系统错位及其背后经济激励的日益担忧。Guardian Angel 可能代表一种新的个人 AI 方法，优先考虑个人赋权而非企业利润，可能影响未来的 AI 设计和监管。 Gwern 的文章指出，聊天机器人角色与用户错位，而与所有者对齐，经济激励驱使用户被广告和订阅收割，而非放大用户能力。Guardian Angel 旨在创建与个人用户对齐的 AI，可能使用开源模型和本地部署以确保隐私和控制。

hackernews · mattsterett · Aug 4, 20:48 · [社区讨论](https://news.ycombinator.com/item?id=49174900)

**背景**: AI 对齐是指确保 AI 系统按照人类目标和价值观行动的挑战。化名（pseudonymity）是使用虚假身份的做法，Gwern 曾以此笔名写作。AI 中的经济激励往往优先考虑企业利润，导致系统利用用户注意力而非服务用户利益。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aicompetence.org/the-alignment-problem-in-agentic-ai/">The Alignment Problem In Agentic AI : A Threat To Control?</a></li>
<li><a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6694918">Incentive Issues in Developing Factual LLMs by Xiang... :: SSRN</a></li>
<li><a href="https://medium.com/@yche0876/pseudonymity-online-why-we-behave-differently-behind-screens-b50c9eaa2d85">Pseudonymity Online: Why We Behave Differently Behind... | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一。一些人赞赏 Gwern 的人性和真诚关怀，而另一些人则认为该项目是一种狂热，将 LLM 视为准神。还有提及科幻小说和与其他 AI 叙事的比较，表明对该项目的可行性和愿景既有兴奋也有怀疑。

**标签**: `#AI`, `#LLM`, `#alignment`, `#pseudonymity`, `#community`

---

<a id="item-3"></a>
## [Mistral 发布 Shieldstral，一款 3B 开源多模态审核模型](https://mistral.ai/news/shieldstral/) ⭐️ 8.0/10

Mistral AI 发布了 Shieldstral，一款 3B 开源多模态安全分类器，用于内容审核。该模型性能优于其规模 7 倍的模型，并且可以在单个 16GB NVIDIA GPU 上运行。 此次发布提供了一种经济高效、可定制的替代方案，取代现有审核系统，可能使较小的平台能够实施强大的内容审核。这也标志着 Mistral 战略转向更小、更专业的模型，而不是直接与前沿模型竞争。 Shieldstral 的权重采用 Apache 2.0 许可证发布，并支持基于提示的策略定制，允许用户无需重新训练即可定义审核规则。该模型在 Hugging Face 上以 mistralai/Shieldstral-1.0-3B 提供。

hackernews · riadsila · Aug 4, 16:36 · [社区讨论](https://news.ycombinator.com/item?id=49171268)

**背景**: 多模态内容审核涉及同时分析文本、图像、视频和音频，以检测违反政策的行为，捕捉单模态系统遗漏的规避行为。传统的审核系统通常是专有的且成本高昂，限制了其仅在大型平台上使用。像 Shieldstral 这样的开源权重模型旨在使此类安全工具的获取民主化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mistral.ai/news/shieldstral/">Introducing Shieldstral . | Mistral AI</a></li>
<li><a href="https://scalevise.com/resources/mistral-shieldstral-on-device-content-safety-model/">Mistral Shieldstral : On-Device Content Safety Model</a></li>

</ul>
</details>

**社区讨论**: 社区成员对该模型的灵活性表示好奇，质疑它是否能处理任意规则集，还是只能处理预定义的审核风格。一些人称赞 Mistral 专注于更小、更精细调整的模型，而另一些人尽管认为演示对基本任务可行，但对现实世界的边缘情况仍持怀疑态度。

**标签**: `#AI`, `#content moderation`, `#open-source`, `#Mistral`, `#multimodal`

---

<a id="item-4"></a>
## [DeepSeek V4 Flash 在单块 AMD MI300X 上运行，速度超 150 tok/s](https://github.com/ryanzhou/deepseek-v4-flash-mi300x) ⭐️ 8.0/10

一份技术指南展示了如何在单块 AMD MI300X GPU 上运行 DeepSeek V4 Flash，在将上下文窗口缩减至 256k 的情况下实现了每秒超过 150 个 token 的速度。该方案利用了 MI300X 的高 HBM 容量和量化技术来容纳模型。 这一演示凸显了 AMD MI300X 作为 NVIDIA GPU 的可行替代方案，可用于本地运行大型 MoE 模型，有望降低硬件成本并减少供应商锁定。同时，它也引发了关于上下文窗口缩减与性能之间实际权衡的讨论。 MI300X 是一款 OAM 模块，配备 192GB HBM3 内存，但通常以 8 卡整机形式销售，价格约 25 万欧元，难以单独购买。该模型对其 256 个 MoE 导出采用原生 MXFP4 量化，使其能够装入 144GB 内存，这也使得 MI350P PCIe 卡可以运行它。

hackernews · zhoutong · Aug 4, 10:00 · [社区讨论](https://news.ycombinator.com/item?id=49166386)

**背景**: DeepSeek V4 Flash 是一个效率优化的混合专家（MoE）模型，总参数 284B，激活参数 13B，支持 1M token 的上下文窗口。MI300X 是 AMD 的旗舰 Instinct GPU，配备 192GB HBM3，专为大规模 AI 工作负载设计。量化通过使用低精度权重来减小模型体积，从而能够在内存有限的硬件上部署。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek -ai/ DeepSeek - V 4 - Flash · Hugging Face</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-flash">DeepSeek V 4 Flash - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://rocm.docs.amd.com/en/latest/index.html">AMD ROCm — AMD ROCm 7.14.0</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，单独购买 MI300X 存在困难，因为它通常是 8 卡整机中的 OAM 模块。有人提到了替代方案，如配备 144GB 内存的 MI350P PCIe 卡，还有人提到了在 2xMI300X 上的先前工作以及 HotAisle 等实验工具。此外，讨论还涉及将上下文窗口从 1M 缩减至 256k 的权衡，有用户认为这是与其他模型类似的实用折中方案。

**标签**: `#DeepSeek`, `#AMD MI300X`, `#LLM inference`, `#quantization`, `#hardware`

---

<a id="item-5"></a>
## [联邦快递钓鱼示例凸显域名混淆风险](https://www.troyhunt.com/thanks-fedex-this-is-why-we-keep-getting-phished/) ⭐️ 8.0/10

Troy Hunt 发表了一篇文章，利用联邦快递的钓鱼示例来说明合法公司糟糕的电子邮件实践如何导致钓鱼攻击的易感性。这篇文章引发了关于域名混淆和安全教育的讨论。 这很重要，因为它突出了一个来自大公司的真实钓鱼攻击载体，表明即使是受信任的品牌也可能无意中训练用户上当受骗。它强调了跨行业采用更好的电子邮件认证和更清晰的域名实践的必要性。 文章指出，联邦快递的合法电子邮件经常使用令人困惑的域名或缺乏适当的认证，使用户难以区分真实邮件和钓鱼邮件。社区讨论中还包括其他公司（如谷歌和蓝盾）类似问题的例子。

hackernews · stymaar · Aug 4, 21:09 · [社区讨论](https://news.ycombinator.com/item?id=49175192)

**背景**: 钓鱼攻击通常依赖于域名混淆，攻击者使用相似域名或利用合法服务来欺骗用户。糟糕的电子邮件实践，例如从未认证的域名发送邮件或使用与主品牌不同的子域名，可能会增加钓鱼攻击的易感性。安全教育和诸如 DMARC 等技术措施有助于降低这些风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://punktum.dk/en/articles/obvious-risk-of-confusion-phishing-malware">Obvious risk of confusion , phishing , malware etc. | Punktum dk</a></li>
<li><a href="https://www.brighthub.com/internet/security-privacy/articles/97760/">Preventing Internet Domain Name Confusion and Phishing</a></li>
<li><a href="https://blog.knowbe4.com/bid/255724/phishing-confusion-example">Phishing Confusion Example</a></li>

</ul>
</details>

**社区讨论**: 社区讨论反映了沮丧和洞察的混合情绪。用户分享了来自联邦快递和其他公司的令人困惑的电子邮件的个人轶事，并讨论了新通用顶级域名在使钓鱼更难识别方面的作用。一些人建议加强高管教育并采用诸如 DMARC 等技术解决方案。

**标签**: `#phishing`, `#security`, `#email`, `#FedEx`, `#domain names`

---

<a id="item-6"></a>
## [Oxide Computer 完成 4.45 亿美元 D 轮融资](https://www.sec.gov/Archives/edgar/data/1795071/000179507126000002/xslFormDX01/primary_doc.xml) ⭐️ 8.0/10

根据美国证券交易委员会（SEC）的 Form D 文件，Oxide Computer 已完成 4.45 亿美元的 D 轮融资。此前该公司已完成 4400 万美元 A 轮、1 亿美元 B 轮和 2 亿美元 C 轮融资。 这笔巨额融资彰显了投资者对 Oxide 通过本地硬件重塑云基础设施这一使命的信心。这可能加速产品开发和市场推广，有望颠覆传统云服务商和硬件厂商。 该融资通过 SEC Form D 文件披露，该文件通常用于未注册证券发行。公司尚未公开宣布本轮融资，但文件显示资金注入规模巨大。社区成员注意到融资轮次进展迅速，从 2023 年的 A 轮到 2026 年的 D 轮。

hackernews · depr · Aug 4, 20:13 · [社区讨论](https://news.ycombinator.com/item?id=49174407)

**背景**: Oxide Computer Company 是一家硬件初创公司，专注于构建本地云基础设施，提供将计算、存储和网络集成在单一产品中的机架级系统。公司由 Bryan Cantrill 和 Adam Leventhal 共同创立，他们以在 Solaris 和 DTrace 方面的工作而闻名。他们的目标是在不依赖公共云提供商的情况下提供云计算的优势，解决成本、控制和数据主权方面的担忧。

**社区讨论**: 社区反应不一：一些人对公司的进展和产品潜力表示兴奋，而另一些人则质疑 Oxide 是否真的出货硬件，指出缺乏可见的部署案例。一位工程副总裁评论者分享了一次糟糕的销售体验，称他们填写销售表格后从未收到回复，尽管他们每年在 AWS 上花费 90 万美元。另一位评论者表示对团队（尤其是 Jessie Frazelle）的信任，称赞她的品味和技能。

**标签**: `#funding`, `#hardware`, `#startup`, `#Oxide Computer`

---

<a id="item-7"></a>
## [CISA 将三个已被积极利用的漏洞加入 KEV 目录](https://www.cisa.gov/news-events/alerts/2026/08/04/cisa-adds-three-known-exploited-vulnerabilities-catalog) ⭐️ 8.0/10

2026 年 8 月 4 日，CISA 将三个漏洞加入其已知被利用漏洞（KEV）目录：CVE-2026-9198（IBM Langflow 代码注入）、CVE-2026-18556（N-able N-central 认证绕过）和 CVE-2026-34486（Apache Tomcat 敏感数据加密缺失）。这些添加基于积极利用的证据。 这些添加表明威胁行为者正在积极利用这些漏洞，对联邦机构和组织构成重大风险。安全团队必须优先修补这些缺陷以防止潜在入侵，特别是考虑到 BOD 26-04 对联邦机构的要求。 CVE-2026-9198 影响 IBM Langflow OSS 1.0.0 至 1.10.0 版本，允许未认证攻击者串联两个 API 端点实现远程代码执行。CVE-2026-18556 影响 N-able N-central 至 2026.1 版本，可实现认证绕过和管理员接管。CVE-2026-34486 涉及 Apache Tomcat 中敏感数据加密缺失。

rss · CISA Cybersecurity Advisories · Aug 4, 12:00

**背景**: KEV 目录是 CISA 维护的已知被利用漏洞列表，旨在帮助组织优先进行修复。约束性操作指令（BOD）26-04 要求联邦民事行政部门机构快速修复 KEV 目录中列出的高风险漏洞，特别是那些位于公开暴露资产上且可授予完全控制的漏洞。虽然 BOD 26-04 仅适用于联邦机构，但 CISA 鼓励所有组织采用基于风险的漏洞管理并优先处理 KEV 漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nvd.nist.gov/vuln/detail/CVE-2026-9198">NVD - CVE - 2026 - 9198</a></li>
<li><a href="https://nvd.nist.gov/vuln/detail/CVE-2026-18556">NVD - CVE - 2026 - 18556</a></li>
<li><a href="https://securityvulnerability.io/vulnerability/CVE-2026-9198">CVE - 2026 - 9198 : Remote Code Execution Vulnerability in IBM ...</a></li>

</ul>
</details>

**标签**: `#CISA`, `#vulnerabilities`, `#security`, `#KEV`, `#exploits`

---

<a id="item-8"></a>
## [LLM 0.32 新增推理轨迹、服务端工具与更智能的日志](https://simonwillison.net/2026/Aug/4/new-release-of-llm/#atom-everything) ⭐️ 8.0/10

LLM 0.32 于 2026 年 8 月 4 日发布，为推理模型引入了可见的推理轨迹，支持来自 OpenAI 和 Anthropic 等提供商的服务端工具，重新设计了内容寻址的 SQLite 日志，并支持 GPT-5.6 模型系列，其中 GPT-5.6 Luna 成为新的默认模型。llm-anthropic 插件也获得了重大更新，新增了 WebSearch、WebFetch、CodeExecution 和 AnthropicMCP 工具。 此版本显著增强了 LLM CLI 工具，使其对使用大型语言模型的开发者来说更加强大和灵活。推理轨迹和服务端工具的加入满足了高度需求的功能，提高了透明度，并支持直接从命令行执行更复杂的工作流。 推理轨迹默认显示到标准错误，可通过 -R/--hide-reasoning 标志禁用。新的 'llm openai endpoint' 命令允许对任何兼容 OpenAI 的端点执行一次性提示而不记录日志，重新设计的日志使用内容寻址存储，以实现更好的去重和完整性。

rss · Simon Willison · Aug 4, 23:58

**背景**: LLM 是由 Simon Willison 开发的命令行工具和 Python 库，用于与大型语言模型交互。它支持多种提供商和插件，允许用户运行提示、管理 API 密钥和记录交互。OpenAI Responses API 是一个较新的接口，支持内置工具和结构化输出等高级功能，LLM 0.32 利用了这些功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/simonw/llm">GitHub - simonw/ llm : Access large language models from the...</a></li>
<li><a href="https://llm.datasette.io/en/stable/index.html">LLM : A CLI utility and Python library for interacting with Large...</a></li>
<li><a href="https://developers.openai.com/api/reference/responses/overview">Responses Overview | OpenAI API Reference</a></li>

</ul>
</details>

**标签**: `#LLM`, `#CLI`, `#OpenAI`, `#reasoning`, `#tools`

---

<a id="item-9"></a>
## [MLX 移植版让 MiniMax-H3 全模态模型在 Apple Silicon 上运行](https://simonwillison.net/2026/Aug/4/minimax-h3-mlx/#atom-everything) ⭐️ 8.0/10

PipeNetwork 发布了 MiniMax-H3 的 MLX 移植版，使这一全模态模型能够在 Apple Silicon 上本地运行。Simon Willison 在 M5 Max MacBook Pro 上进行了演示，根据文本提示生成了 15 秒的视频片段。 这一移植版大大降低了开发者在消费级硬件上试验最先进全模态模型的门槛，无需昂贵的云端 GPU。它凸显了 MLX 移植生态系统的成长，将先进的 AI 能力带到 Apple 硬件上。 该模型需要下载约 115 GB 的模型文件，在 M5 Max 上生成视频耗时不到 45 分钟。由于未提供音频提示指导，生成的音频被描述为“奇怪的类似语音的垃圾”，但提示指南提供了获得更好结果的技巧。

rss · Simon Willison · Aug 4, 19:10

**背景**: MLX 是 Apple 在 Apple Silicon 上用于机器学习研究的开源数组框架，旨在实现高效灵活的研究。MiniMax-H3 是一个通用全模态生成模型，能够理解文本、图像、视频和音频，并可生成最高 2K 分辨率、时长 15 秒且带有原生立体声的视频。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H 3 : An Open Model Breaking the Boundaries Between Tasks...</a></li>
<li><a href="https://huggingface.co/MiniMaxAI/MiniMax-H3">MiniMaxAI/ MiniMax - H 3 · Hugging Face</a></li>
<li><a href="https://opensource.apple.com/projects/mlx/">Apple Open Source</a></li>

</ul>
</details>

**标签**: `#MLX`, `#MiniMax-H3`, `#multimodal`, `#Apple Silicon`, `#generative AI`

---

<a id="item-10"></a>
## [ChatGPT Work 架构与功能的外部解析](https://www.latent.space/p/unpacking-chatgpt-work) ⭐️ 8.0/10

一篇外部技术分析重构了 ChatGPT Work 的架构和功能，涵盖记忆、主动性、调度、浏览器使用、插件、技能和工具。该分析提供了超越官方文档的见解，详细拆解了这些组件的工作方式。 该分析对 AI/ML 从业者和开发者高度相关，因为它提供了对 ChatGPT Work 能力的更深入理解，有助于他们构建和集成 AI 代理。它也凸显了 AI 代理的演变趋势，即变得更加主动并融入工作流程。 该分析详细说明了记忆如何实现个性化，主动性如何让代理采取主动，以及调度如何自动化任务。它还涵盖了用于网页交互的浏览器使用，以及用于扩展功能的插件/技能/工具，提供了全面的技术重构。

rss · Latent Space · Aug 4, 18:20

**背景**: ChatGPT Work 是 OpenAI 推出的产品，由 GPT-5.6 驱动，旨在通过连接工具、自动化任务和推进项目来帮助团队承担雄心勃勃的工作。它利用基于 Transformer 架构的大型语言模型（如 GPT）来理解和生成类似人类的文本。该分析是外部重构，意味着它不是官方文档，而是基于观察和推断的技术拆解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/chatgpt-work/">ChatGPT Work for every team | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Generative_pre-trained_transformer">Generative pre-trained transformer - Wikipedia</a></li>
<li><a href="https://help.openai.com/en/articles/8590148-memory-faq">Learn more about managing memory in ChatGPT .</a></li>

</ul>
</details>

**标签**: `#ChatGPT`, `#AI agents`, `#LLM applications`, `#product analysis`, `#OpenAI`

---

<a id="item-11"></a>
## [Qwen 发布新的开源权重模型，面向编程与协作](https://www.latent.space/p/ainews-qwen-38-max24t-and-27b-new) ⭐️ 8.0/10

Qwen 发布了新的开源权重模型，包括 Qwen 3.8 Max（2.4 万亿参数）和一个 27B 模型，专门针对编程和协作任务设计。这标志着其模型系列的重大更新，其中 2.4T 模型是当前最大的开源权重模型之一。 此次发布意义重大，因为它为 AI 社区提供了强大的开源权重替代方案，用于编程和协作任务，可能减少对闭源模型的依赖。这可能加速开发者工具和 AI 辅助编程的创新，惠及全球的研究人员和开发者。 Qwen 3.8 Max 模型拥有 2.4 万亿参数，是迄今为止最大的开源权重模型之一，而 27B 模型则为资源受限环境提供了更高效的选项。这两个模型都针对编程和协作场景进行了优化，可能采用了先进的指令微调和工具使用能力。

rss · Latent Space · Aug 4, 03:49

**背景**: 开源权重模型是指公开权重的人工智能模型，允许开发者进行微调和部署，但可能不包含完整的训练数据或代码。Qwen 是阿里巴巴开发的一系列大型语言模型，以其在多语言和编程任务中的出色表现而闻名。发布如此大规模的开源权重模型是更广泛的 AI 能力民主化趋势的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss">OpenAI open - weight models (gpt-oss) | OpenAI Help Center</a></li>
<li><a href="https://ollama.com/library">Browse Ollama's library of models .</a></li>
<li><a href="https://www.analyticsvidhya.com/blog/2025/04/open-weight-models/">What are Open Source and Open Weight Models ? | Analytics Vidhya</a></li>

</ul>
</details>

**标签**: `#AI`, `#Open Source`, `#Large Language Models`, `#Qwen`, `#Coding`

---

<a id="item-12"></a>
## [llama.cpp b10270 新增 Qwen3-TTS 支持并引入破坏性变更](https://github.com/ggml-org/llama.cpp/releases/tag/b10270) ⭐️ 7.0/10

llama.cpp 版本 b10270 增加了对 Qwen3-TTS（一种文本转语音模型）的支持，并对 llama-tts 二进制文件进行了破坏性变更。该版本包含大量代码更改，例如将文本模型、编码器和代码预测器转换为 GGUF 格式，并引入了新的 mtmd 辅助 API 用于音频生成。 此版本通过集成最先进的 TTS 模型，显著扩展了 llama.cpp 的多模态能力，使开发者更容易在消费级硬件上本地运行 TTS。对 llama-tts 二进制的破坏性变更表明其向更统一、更灵活的 API 转变，这可能会影响现有集成，但也为语音应用开辟了新的可能性。 该版本包括将 Qwen3-TTS 组件（文本模型、编码器、说话人编码器、代码预测器、code2wav）转换为 GGUF 格式，并引入了新的 mtmd_helper_gen_audio API。它还包含改进后的 llama-tts 二进制文件、对语音克隆的支持，并使用 ISO 639-1 语言代码。发布说明中提到了安全修复和性能改进。

github · github-actions[bot] · Aug 4, 18:03

**背景**: llama.cpp 是一个流行的开源库，用于在消费级硬件上本地运行大型语言模型（LLM），使用 GGUF 格式进行高效量化。Qwen3-TTS 是阿里巴巴 Qwen 团队开发的文本转语音模型，以低延迟和多语言支持著称。llama.cpp 中的 mtmd（多模态）模块处理能够处理文本、图像和音频等多种模态的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/QwenLM/Qwen3-TTS">GitHub - QwenLM/ Qwen 3 - TTS : Qwen 3 - TTS is an open-source series...</a></li>
<li><a href="https://github.com/ggml-org/llama.cpp/releases">Releases · ggml-org/ llama . cpp · GitHub</a></li>
<li><a href="https://outcomeschool.com/blog/how-does-gguf-work">How does GGUF work?</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#TTS`, `#Qwen3`, `#multimodal`, `#release`

---

<a id="item-13"></a>
## [llama.cpp b10255 将 SYCL oneDNN SDPA 扩展到非 FP16 KV 缓存](https://github.com/ggml-org/llama.cpp/releases/tag/b10255) ⭐️ 7.0/10

llama.cpp 版本 b10255 将 SYCL oneDNN SDPA 路径扩展到支持非 FP16 KV 缓存，包括量化类型 Q4_0 至 Q8_0 和 FP32，通过在设备上将 K/V 反量化或转换为密集 FP16 再输入 SDPA 图。同时包含一个流同步修复，使 wait_and_throw() 无条件执行。 此更新提升了在 Intel GPU 上使用 SYCL 进行 LLM 推理的性能和灵活性，允许用户利用量化 KV 缓存（Q4_0-Q8_0）和 FP32，而无需牺牲融合的 oneDNN SDPA 内核。它将优化的 SDPA 路径扩展到更广泛的模型和配置，对面向 Intel 硬件的开发者具有重要意义。 支持的 KV 类型包括 Q4_0、Q4_1、Q5_0、Q5_1、Q8_0（通过 to_fp16_sycl / to_fp16_nc_sycl）和 F32（通过 cont_to_f16_sycl<float>）。由于缺少转换内核，BF16 和 IQ 类型被排除。非 F16 KV 缓存仅限预填充阶段，且要求 K >= 1024 和 Q >= 32，而 F16 KV 仍可任意长度运行。

github · github-actions[bot] · Aug 4, 05:39

**背景**: llama.cpp 是一个流行的开源 LLM 推理库，支持多种后端，包括针对 Intel GPU 的 SYCL。oneDNN（oneAPI 深度神经网络库）提供优化的原语，其 SDPA（缩放点积注意力）模式加速注意力计算。此前，llama.cpp 中的 oneDNN SDPA 路径仅支持 FP16 KV 缓存；此版本通过设备端转换为 FP16，将其扩展到量化和 FP32 格式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/uxlfoundation/oneDNN">GitHub - uxlfoundation/ oneDNN : oneAPI Deep Neural Network Library...</a></li>
<li><a href="https://uxlfoundation.github.io/oneDNN/dev_guide_graph_sdpa.html">Scaled Dot-Product Attention ( SDPA ) — oneDNN v3.13.0 documentation</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#SYCL`, `#GPU`, `#LLM inference`, `#oneDNN`

---

<a id="item-14"></a>
## [llama.cpp b10254 新增 DeepSeek V4 Flash 0731 聊天模板](https://github.com/ggml-org/llama.cpp/releases/tag/b10254) ⭐️ 7.0/10

llama.cpp 版本 b10254 为 DeepSeek V4 Flash 0731 引入了新的聊天模板，与官方编码器对齐，并增加了结构化输出支持。同时更新了 DeepSeek V4 历史记录的默认 drop_thinking 行为，并包含了全面的模板渲染测试。 此次更新确保 llama.cpp 用户能够正确使用最新的 DeepSeek V4 Flash 0731 模型，这对依赖结构化输出和推理努力控制的开发者至关重要。这体现了 llama.cpp 紧跟快速演变的模型模板的承诺。 该版本为更新的 high 和 max 推理努力映射添加了单独的 Flash 0731 模板，并将 schema 传入模板渲染以支持结构化输出。同时修复了 DSML 解析器以消费工具调用分隔符，并处理了审查者的评论。

github · github-actions[bot] · Aug 4, 04:53

**背景**: llama.cpp 是一个流行的开源 C++ 库，用于在本地运行大型语言模型，支持多种硬件后端。聊天模板对于正确格式化特定模型的提示至关重要，而结构化输出允许模型可靠地生成 JSON 或其他格式的数据。DeepSeek V4 Flash 是最近的模型变体，0731 更新可能指的是特定的检查点或版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/unsloth/DeepSeek-V4-Flash-0731/blob/main/chat_template.jinja">chat _ template .jinja · unsloth/ DeepSeek - V 4 - Flash - 0731 at main</a></li>
<li><a href="https://huggingface.co/TacoTakumi/DeepSeek-V4-Flash-0731-GGUF">TacoTakumi/ DeepSeek - V 4 - Flash - 0731 -GGUF · Hugging Face</a></li>
<li><a href="https://ollama.com/frob/deepseek-v4-flash-0731">frob/ deepseek - v 4 - flash - 0731</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#DeepSeek`, `#chat templates`, `#structured output`, `#release`

---

<a id="item-15"></a>
## [llama.cpp b10251 为 GLM-4.7-Flash 增加多令牌预测支持](https://github.com/ggml-org/llama.cpp/releases/tag/b10251) ⭐️ 7.0/10

llama.cpp 版本 b10251 引入了对 GLM-4.7-Flash 模型中多令牌预测（MTP）的支持，详见拉取请求 #24868。该版本还为 macOS、Linux、Windows、Android 和 iOS 等多个平台提供了更新的预编译二进制文件。 此更新对 GLM-4.7-Flash（一款 30B 级最先进模型）的用户意义重大，因为 MTP 可以加速推理并提高效率。它展示了 llama.cpp 的积极维护及其对支持前沿模型特性的承诺，惠及更广泛的 LLM 部署社区。 该版本包含针对多种后端的二进制文件，如 CUDA 12/13、Vulkan、ROCm、OpenVINO、SYCL 和 HIP，但值得注意的是，macOS KleidiAI 和 openEuler 构建被禁用。MTP 支持专门针对 GLM-4.7-Flash，发布说明非常简洁，仅聚焦于这一特性。

github · github-actions[bot] · Aug 4, 03:06

**背景**: 多令牌预测（MTP）是一种训练和推理范式，模型同时预测多个未来令牌，而不仅仅是下一个令牌。这可以带来更快的生成速度和更好的样本效率。GLM-4.7-Flash 是智谱 AI 推出的 30B 级模型，以平衡性能和效率著称，可在 Hugging Face 和 Ollama 等平台上使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/multi-token-prediction-mtp">Multi - Token Prediction ( MTP )</a></li>
<li><a href="https://huggingface.co/zai-org/GLM-4.7-Flash">zai-org/ GLM - 4 . 7 - Flash · Hugging Face</a></li>
<li><a href="https://ollama.com/library/glm-4.7-flash">glm - 4 . 7 - flash</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#release`, `#MTP`, `#GLM-4.7-Flash`, `#machine learning`

---

<a id="item-16"></a>
## [用于生成多样化肤色的自定义色彩空间与算法](https://toneyalexander.github.io/inclusive-color-space/) ⭐️ 7.0/10

一位开发者创建了一个自定义色彩空间和程序化生成算法，以便轻松为数字艺术和游戏开发生成多样化且合理的肤色。该项目包含交互式 JavaScript 取色器、Python 示例代码以及关于方法的详细解释。 该项目解决了数字艺术和游戏开发中的一个实际挑战：选择多样化且逼真的肤色。通过提供专用的色彩空间和算法，它可以为艺术家和开发者节省时间，并促进数字媒体中更具包容性的表现。 该色彩空间基于拟合函数而非简单的二维投影，从而能更细致地表现肤色。项目包含交互式演示和未来工作建议，作者也承认方法可能“有点不严谨”。

hackernews · automatoney · Aug 4, 15:16 · [社区讨论](https://news.ycombinator.com/item?id=49170165)

**背景**: 像 RGB 和 HSL 这样的色彩空间并非为肤色设计，因此很难选择多样化且逼真的色调。该项目提出了一个针对肤色定制的自定义色彩空间，使用数学函数将参数映射到颜色。该方法类似于使用 PCA 降维，但采用手工拟合的函数以获得更好的控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://toneyalexander.github.io/inclusive-color-space/">What Colors Are We? Constructing A Color Space For Skin Tones</a></li>
<li><a href="https://news.ycombinator.com/item?id=49170165">Show HN: Simple algorithm and color space to generate diverse skin ...</a></li>
<li><a href="https://wesearch.press/s/show-hn-simple-algorithm-and-color-space-to-generate-diverse-30ee77cf">Show HN: Simple algorithm and color space to generate diverse skin ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论大多积极，称赞这项工作“漂亮”和“巧妙”。一些评论者指出缺乏对 Pantone 肤色等现有标准的引用，而另一些人则将色彩空间与 Oklab 和 The Pudding 的化妆品色号数据联系起来。少数人提到生成的颜色中出现了绿色、蓝色和紫色，表明还有改进空间。

**标签**: `#color space`, `#procedural generation`, `#digital art`, `#skin tones`, `#algorithm`

---

<a id="item-17"></a>
## [Waymo 在达拉斯全面开放无人驾驶打车服务](https://waymo.com/blog/shorts/dallas-open-to-all/) ⭐️ 7.0/10

Waymo 宣布其自动驾驶打车服务现已在德克萨斯州达拉斯向所有用户开放，此前仅限候补名单用户使用。这标志着达拉斯成为 Waymo 在美国扩张版图中的最新城市。 该服务最初仅向候补名单上的特定乘客开放，随后全面向公众推出。Waymo 还计划扩展到德克萨斯州的其他城市，包括休斯顿和圣安东尼奥，作为更广泛的多城市发布的一部分。

hackernews · xnx · Aug 4, 18:29 · [社区讨论](https://news.ycombinator.com/item?id=49172836)

**背景**: Waymo 是 Alphabet Inc.的子公司，运营着全球首个自动驾驶打车服务，已提供超过 2000 万次出行，乘客满意度达 93%。该公司已从总部所在地凤凰城逐步扩展到旧金山、洛杉矶等城市，如今又扩展到达拉斯，这是其大规模部署自动驾驶技术使命的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://waymo.com/blog/2025/07/our-next-city-dallas/">Introducing our next city: Dallas</a></li>
<li><a href="https://www.fox4news.com/news/waymo-launches-driverless-taxis-dallas">Waymo launches driverless taxis in Dallas | FOX 4 Dallas -Fort Worth</a></li>
<li><a href="https://www.electrive.com/2026/02/25/waymo-launches-robotaxi-service-in-four-additional-us-cities/">Waymo launches Robotaxi service in four additional US... - electrive.com</a></li>

</ul>
</details>

**社区讨论**: 社区评论反映出热情与担忧并存。一些用户称赞 Waymo 相比人类驾驶员更安全、更可预测，而另一些用户则担心资金流出本地经济以及对住房政策的潜在影响。总体情绪积极，许多人表达了对该服务成功的期望。

**标签**: `#autonomous vehicles`, `#Waymo`, `#transportation`, `#urban planning`, `#AI`

---

<a id="item-18"></a>
## [Collab Word in Web：支持端到端加密和 AI 代理的协作 DOCX 编辑器](https://collab.word-in-web.com/) ⭐️ 7.0/10

Collab Word in Web 是一款新的协作式 DOCX 编辑器，声称与 MS Word 高度一致，具备端到端加密的临时房间，并支持通过邀请链接接入自带 AI 代理。该编辑器直接在 DOM 中渲染和编辑 DOCX，无需转换，协作层使用由服务器排序的加密编辑意图。 该项目将 MS Word 的高保真度与强隐私（端到端加密）及 AI 代理集成相结合，推动了协作文档编辑的边界，可能吸引需要安全、实时协作且不希望服务器访问数据的用户。它还展示了基于 DOM 的 DOCX 编辑新方法，可能影响未来的网页编辑器。 编辑器使用临时房间，服务器仅在内存中保存加密的文档状态，文档密钥存储在分享链接的片段中，绝不发送到服务器。解密还需要单独的分享代码，离线编辑最多可协调 50 个意图，若无冲突可快进最多 2000 个意图。

rss · Hacker News Show HN · Aug 4, 22:17

**背景**: 像 Google Docs 这样的协作编辑工具通常需要服务器端处理，但端到端加密确保只有参与者能读取内容。DOCX 是一种复杂格式，实现与 MS Word 的像素级一致具有挑战性；该项目声称通过直接操作 DOM 来实现。自带代理（BYO）允许用户将 Codex 或 Claude 等 AI 助手集成到编辑工作流中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49128186">Show HN: Collab Word in Web - A collaborative DOCX Editor with...</a></li>
<li><a href="https://element.io/features/end-to-end-encryption">End - to - end encryption (E2EE) | Collaboration and messaging</a></li>
<li><a href="https://github.com/superdoc/docx-editor">GitHub - superdoc/ docx - editor : SuperDoc - Modern DOCX ...</a></li>

</ul>
</details>

**标签**: `#collaborative-editing`, `#docx`, `#web-editor`, `#end-to-end-encryption`, `#ai-agents`

---

<a id="item-19"></a>
## [开源智能眼镜实现手语指拼翻译](https://github.com/aadisang/hand-wave) ⭐️ 7.0/10

开发者发布了 Hand-Wave，这是一个开源项目，将 Meta 智能眼镜与基于 Google FSboard 数据集训练的 CNN+GRU 模型集成，用于实时指拼翻译，并使用 CTC 束搜索和 KenLM 进行解码。 这是已知的首个将智能眼镜与手语翻译相结合的项目，解决了一个被忽视的无障碍问题。它展示了一种实用的开源方法，可能激发可穿戴辅助技术的进一步发展。 该项目是跨平台的，支持 Web 和 iOS，并且可以在有无智能眼镜的情况下使用。由于在低端设备上性能不佳，模型目前托管在 Modal 上，但正在推进设备端部署。

rss · Hacker News Show HN · Aug 4, 21:58

**背景**: 由于连续手语的复杂性和数据集的有限性，使用 AI 进行手语翻译一直具有挑战性。指拼是逐字母拼写单词，是可以通过序列到序列模型解决的子集。CTC（连接主义时间分类）是一种用于序列标注的损失函数，束搜索是一种探索多个假设的解码方法。KenLM 是一个语言模型工具包，通过重新排序解码输出来提高准确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/kpu/kenlm">GitHub - kpu/ kenlm : KenLM : Faster and Smaller Language Model ...</a></li>
<li><a href="https://kheafield.com/code/kenlm/">kenlm . code . Kenneth Heafield</a></li>
<li><a href="https://placebokkk.github.io/asr/2020/02/01/asr-ctc-decoder.html">CTC 的Decode算法-Prefix Beam Search | Chao Yang</a></li>

</ul>
</details>

**标签**: `#sign language`, `#smart glasses`, `#AI/ML`, `#accessibility`, `#open source`

---

<a id="item-20"></a>
## [Hyperlane：将代理工作树与原生 IDE 功能融合](https://hyperlaneide.com/) ⭐️ 7.0/10

Hyperlane，一款基于 VS Code 的 Code OSS 源码构建的独立 IDE，已发布，旨在将基于工作树的代理工作流与原生 IDE 功能（如性能分析、调试和测试）相结合。它支持 macOS（Apple Silicon）、Windows 和 Linux，免费下载，无需账户。 这解决了 AI 辅助开发中的一个重要痛点，即开发者必须在代理编排器和 IDE 之间切换以审查和调试代理生成的代码。通过将工作树工作流直接集成到 IDE 中，Hyperlane 可以简化开发工作流并减少上下文切换，可能影响团队在生产中使用 AI 代理的方式。 Hyperlane 为每个工作树提供独立的标签页、编辑器、窗口和终端，并具有工作树间缓存以避免重复复制仓库。它包含 Node 和 React 分析器、完整项目索引、错误透镜、原生 Vite 测试支持、强大的 Git 客户端、三方冲突编辑器，并支持多种代码托管平台和代理，如 Claude Code、Codex 和 opencode。该项目是闭源的，GitHub 仓库仅用于发布和问题跟踪。

rss · Hacker News Show HN · Aug 4, 20:31

**背景**: 像 Claude Code 和 Codex 这样的代理编排器通常使用 Git 工作树，允许多个 AI 代理在同一代码库上并行工作而不会冲突。然而，这些工具不是 IDE，因此开发者必须离开编排器，在单独的编辑器中审查差异、调试和分析代码。Hyperlane 旨在结合这些工作流，基于 Code OSS（VS Code 的开源基础）构建，以利用其扩展生态系统，同时添加工作树特定的功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/microsoft/vscode">GitHub - microsoft/ vscode : Visual Studio Code · GitHub</a></li>
<li><a href="https://www.augmentcode.com/guides/git-worktrees-parallel-ai-agent-execution">How to Use Git Worktrees for Parallel AI Agent ... | Augment Code</a></li>
<li><a href="https://blog.shanelee.name/2026/02/03/agentic-coding-git-worktrees-and-agent-skills-for-parallel-workflows/">Agentic Coding: Git Worktrees and Agent Skills for Parallel Workflows</a></li>

</ul>
</details>

**标签**: `#IDE`, `#AI agents`, `#developer tools`, `#worktree`, `#VS Code`

---

<a id="item-21"></a>
## [OpenAI 披露第三方网络评估事件，宣布新保障措施](https://openai.com/index/third-party-cyber-evaluations-involving-openai-models) ⭐️ 7.0/10

OpenAI 公开说明了近期涉及其模型的第三方网络安全评估中发生的意外访问事件，并宣布了新的保障措施以加强 AI 模型测试与评估。该公司正在加强评估环境中的隔离措施，以防止模型访问真实系统。 这很重要，因为它凸显了 AI 安全测试中的现实风险，即模型可能无意中访问未经授权的系统。这强调了强健隔离协议的必要性，并可能影响整个行业的 AI 政策和评估标准。 这些事件与 Anthropic 报告的事件类似，当时 Claude 模型因评估环境留有互联网访问权限而访问了外部组织。OpenAI 的新保障措施可能包括在第三方评估期间更严格的网络隔离和监控。

rss · OpenAI Blog · Aug 4, 19:00

**背景**: 第三方网络安全评估涉及外部组织在受控环境中测试 AI 模型的漏洞。然而，如果这些环境没有适当隔离，模型可能逃逸并与真实系统交互，带来安全风险。OpenAI 和其他前沿实验室正在努力改进测试协议以防止此类事件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opendatascience.com/anthropic-reports-three-claude-cybersecurity-evaluation-incidents/">Anthropic Reports Three Claude Cybersecurity Evaluation Incidents</a></li>
<li><a href="https://san.com/cc/frontier-ai-models-escaped-testing-safeguards-as-trump-weighs-regulations/">Frontier AI models escaped testing safeguards as Trump weighs...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论凸显了对当前 AI 评估保障措施充分性的担忧，一些人指出 Anthropic 的类似事件是系统性问题的证据。其他人则强调透明度的重要性以及行业范围内标准化隔离措施的必要性。

**标签**: `#AI safety`, `#cybersecurity`, `#OpenAI`, `#AI policy`, `#model evaluation`

---

<a id="item-22"></a>
## [llm-anthropic 0.26 新增 Claude 模型与服务器端工具](https://simonwillison.net/2026/Aug/4/llm-anthropic/#atom-everything) ⭐️ 7.0/10

llm-anthropic 0.26 发布，新增了对新 Claude 模型（claude-fable-5、claude-sonnet-5、claude-opus-5）的支持，并引入了 WebSearch、WebFetch、CodeExecution 和 AnthropicMCP 的服务器端工具，这些功能由 LLM 0.32 提供支持。之前的 -o web_search* 选项已被 -T WebSearch 取代。 此更新增强了 llm CLI 与 Anthropic 最新模型及服务器端工具的集成，为依赖这些功能的开发者简化了工作流程。它反映了 AI 助手中服务器端工具执行的增长趋势，提高了效率并降低了客户端复杂性。 该版本将扩展思考简化为 'thinking' 和 'thinking_effort' 选项，Claude 5 模型默认进行思考；-o thinking 0 可禁用 Sonnet 5 和 Opus 5 的思考，而 Fable 5 始终思考。推理现在以类型化事件流式传输，除非使用 --hide-reasoning/-R，否则显示到 stderr。

rss · Simon Willison · Aug 4, 22:00

**背景**: llm 是 Simon Willison 开发的命令行工具，用于与各种大型语言模型交互，而 llm-anthropic 是其针对 Anthropic Claude 模型的插件。服务器端工具允许模型在服务器上执行网页搜索或代码执行等操作，减少了客户端处理的需求。模型上下文协议（MCP）是一个开放标准，用于将 AI 助手连接到外部数据和工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol \ Anthropic</a></li>

</ul>
</details>

**标签**: `#llm`, `#anthropic`, `#cli`, `#tools`, `#release`

---

