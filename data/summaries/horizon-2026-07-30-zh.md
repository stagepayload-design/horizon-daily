# Horizon 每日速递 - 2026-07-30

> From 36 items, 19 important content pieces were selected

---

1. [开源引擎在 M 系列 Mac 上仅用 2GB 内存运行 Gemma 4 26B](#item-1) ⭐️ 9.0/10
2. [JetBrains TeamCity 严重远程代码执行漏洞 (CVE-2026-63077)](#item-2) ⭐️ 9.0/10
3. [llama.cpp b10174 为 GLM-5.2 添加 NextN/MTP 推测解码支持](#item-3) ⭐️ 8.0/10
4. [AI 初创企业减少研究发表](#item-4) ⭐️ 8.0/10
5. [Kimi K3-256k：半价上下文窗口](#item-5) ⭐️ 8.0/10
6. [文档型 AI 蠕虫通过 Word 版 Copilot 自我传播](#item-6) ⭐️ 8.0/10
7. [长政策文件无法有效约束 AI 智能体](#item-7) ⭐️ 8.0/10
8. [Anthropic 的密码分析结果引发 AI 智能辩论](#item-8) ⭐️ 8.0/10
9. [Develar app-builder 中存在通过符号链接跟随在 macOS 上任意文件覆盖漏洞](#item-9) ⭐️ 8.0/10
10. [OPeNDAP Hyrax 存在 SSRF 和凭证泄露漏洞](#item-10) ⭐️ 8.0/10
11. [Cisco FMC 静态凭据漏洞允许未认证访问](#item-11) ⭐️ 8.0/10
12. [两个 API 设置使 GPT-5.6 在 ARC-AGI-3 上得分翻三倍](#item-12) ⭐️ 8.0/10
13. [OpenAI 为 10 万研究人员免费提供 ChatGPT](#item-13) ⭐️ 8.0/10
14. [AI 在后量子密码学转型中的作用](#item-14) ⭐️ 8.0/10
15. [Vision Pro 用于沉浸式建筑漫游](#item-15) ⭐️ 7.0/10
16. [Mitchell Hashimoto 创立 Superlogical，将 Ghostty 转让给非营利组织](#item-16) ⭐️ 7.0/10
17. [KOReader：开源电子书阅读器应用提升 Kobo 和 Kindle 体验](#item-17) ⭐️ 7.0/10
18. [AI 公司招聘数千名电工和木匠](#item-18) ⭐️ 7.0/10
19. [Darktable：免费 RAW 编辑器媲美付费软件](#item-19) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [开源引擎在 M 系列 Mac 上仅用 2GB 内存运行 Gemma 4 26B](https://github.com/drumih/turbo-fieldfare) ⭐️ 9.0/10

TurboFieldfare 是一个开源的 Swift/Metal 推理引擎，通过从 SSD 流式传输路由专家，在任意 M 系列 Mac 上仅用约 2GB 内存即可运行 4 位量化的 Gemma 4 26B-A4B-IT 模型，在 8GB M2 MacBook Air 上达到 5–6 tok/s，在 M5 MacBook Pro 上达到 31–35 tok/s。 这一突破使得在低内存 Apple Silicon 设备上运行大型 MoE 模型成为可能，推动了设备端 AI 的普及，并降低了对强大语言模型的硬件要求。 模型的 4 位权重约占 14GB，但 TurboFieldfare 仅将共享层和 KV 缓存保留在 RAM 中，同时使用有界并行 pread 和小型专家缓存从 SSD 流式传输路由专家。它包含一个实验性的 OpenAI 兼容服务器，支持流式传输和工具调用。

hackernews · gitpusher42 · Jul 29, 15:05 · [社区讨论](https://news.ycombinator.com/item?id=49098510)

**背景**: 混合专家（MoE）架构使用多个专门的子网络（专家）和路由机制，每个 token 仅激活部分专家，从而在较低计算成本下实现更大模型。KV 缓存存储过去的键值张量，以避免自回归生成中的重复计算。Metal 是 Apple 的 GPU 框架，用于 Apple Silicon 上的高性能图形和计算。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/learning/scaling-ai-models-with-mixture-of-experts-moe-design-principles-and-real-world-applications/intro-to-moe-architecture">Intro to MoE architecture - Scaling AI Models with Mixture of Experts ...</a></li>
<li><a href="https://huggingface.co/blog/not-lain/kv-caching">KV Caching Explained: Optimizing Transformer Inference Efficiency</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞了这一创新，有人指出 llama.cpp 也可以通过 mmap 运行大型模型，但缺乏同步 SSD 流式优化。一位用户提供了在旧版 macOS 上编译的解决方法，另一位表示有兴趣与 DiffusionGemma 项目结合。

**标签**: `#inference engine`, `#on-device AI`, `#MoE`, `#Swift`, `#Metal`

---

<a id="item-2"></a>
## [JetBrains TeamCity 严重远程代码执行漏洞 (CVE-2026-63077)](https://www.rapid7.com/blog/post/etr-cve-2026-63077-critical-unauthenticated-remote-code-execution-in-jetbrains-teamcity) ⭐️ 9.0/10

JetBrains 披露了 CVE-2026-63077，这是一个影响所有 TeamCity On-Premises 版本的严重未认证远程代码执行漏洞，CVSS 评分为 9.8。该漏洞允许未认证攻击者通过代理轮询协议执行任意操作系统命令。 TeamCity 是一款广泛使用的 CI/CD 工具，成功利用该漏洞可能导致服务器完全被控、凭据泄露以及流水线完整性受损。各组织必须紧急修补以防止潜在入侵。 该漏洞是代理轮询协议中的不可信数据反序列化问题。修复版本为 TeamCity 2025.11.7 和 2026.1.3；针对 2017.1 及更高版本提供了安全补丁插件。TeamCity Cloud 用户不受影响。

rss · Rapid7 Emergent Threat Response · Jul 29, 16:16

**背景**: TeamCity 是一个持续集成和交付服务器，使用构建代理来执行任务。代理轮询协议用于代理检查新任务。反序列化漏洞发生在未经验证的反序列化不可信数据时，可能允许攻击者注入恶意对象。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.intelfusions.com/news/jetbrains-teamcity-unauthenticated-rce-build-server-takeover">Critical JetBrains TeamCity bug lets attackers hijack... | IntelFusions</a></li>
<li><a href="https://www.techrepublic.com/article/news-critical-teamcity-rce-flaw/">Critical TeamCity Flaw Could Let Unauthenticated... - TechRepublic</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#CVE`, `#JetBrains`, `#RCE`

---

<a id="item-3"></a>
## [llama.cpp b10174 为 GLM-5.2 添加 NextN/MTP 推测解码支持](https://github.com/ggml-org/llama.cpp/releases/tag/b10174) ⭐️ 8.0/10

llama.cpp 版本 b10174 为 GLM-5.2 (GLM_DSA) 模型引入了 NextN/MTP 推测解码支持，包括张量加载、图构建以及草稿头的 KV 缓存设置。 这使得 GLM-5.2 模型能够通过内置草稿头进行推测解码，从而加速推理，降低延迟且不牺牲输出质量。它扩展了 llama.cpp 对新型模型架构的支持，惠及开源 LLM 生态系统。 草稿头使用密集 MLA 和 sigmoid 门控 MoE 及共享专家，MTP 上下文仅对 nextn 层使用普通注意力 KV 缓存。该版本还在转换脚本中为 GLM-5.2 添加了 --mtp/--no-mtp 导出选项。

github · github-actions[bot] · Jul 29, 07:14

**背景**: 推测解码通过使用较小的草稿模型每步预测多个 token，再由主模型验证，从而加速 LLM 推理。多 token 预测 (MTP) 是一种变体，其中草稿头集成在主模型内部，无需单独的草稿模型。GLM-5.2 是清华大学最新的大语言模型，采用密集 MLA 和 MoE 架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://linux.do/t/topic/2673428">GLM 5.2本地部署，llama.cpp今日更新了add NextN /MTP speculative ...</a></li>
<li><a href="https://localllm.in/blog/mtp-lm-studio">Multi-Token Prediction ( MTP ) LM Studio Tutorial - Boost... | LocalLLM.in</a></li>
<li><a href="https://medium.com/practical-llm-systems/i-tested-mtp-speculative-decoding-on-two-qwen-models-one-was-a-trap-46c2dfe584c7">I Tested MTP Speculative Decoding on Two Qwen Models... | Medium</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#speculative decoding`, `#GLM-5.2`, `#MTP`, `#inference`

---

<a id="item-4"></a>
## [AI 初创企业减少研究发表](https://www.science.org/content/article/ai-s-top-startups-are-barely-publishing-their-research) ⭐️ 8.0/10

一项最新分析显示，顶级 AI 初创公司因竞争压力和学术出版负面经历，正越来越多地选择不发表研究成果。 这一趋势威胁到 AI 研究的可重复性和开放科学，可能减缓集体进步，并将知识集中在少数私营实体手中。 该研究以累计引用量作为研究重要性的指标，OpenAI 领先，其次是旷视科技、Hugging Face 和 Waymo 等公司。

hackernews · YeGoblynQueenne · Jul 29, 21:25 · [社区讨论](https://news.ycombinator.com/item?id=49103285)

**背景**: 历史上，AI 研究通过开放发表蓬勃发展，促进了快速进步。但随着 AI 的商业价值提升，初创公司面临保护知识产权、避免帮助 OpenAI 和 Anthropic 等竞争对手的压力。

**社区讨论**: 评论者分享了第一手经验：一位提到在与顶级期刊的负面经历后，其初创公司停止发表以防止竞争对手复制成果。另一位批评 AI 研究的“博客化”，未经证实的声明像社交媒体一样传播。

**标签**: `#AI research`, `#startups`, `#open science`, `#publication culture`

---

<a id="item-5"></a>
## [Kimi K3-256k：半价上下文窗口](https://www.kimi.com/code/docs/en/kimi-code/models) ⭐️ 8.0/10

Kimi 推出了 K3-256k 模型，在上下文不超过 256k token 时提供与完整 K3 模型相同的性能，但配额消耗减半。 这一定价变化使长上下文 AI 更加可及，可能促使竞争对手采用类似的基于上下文的定价策略，从而惠及开发者和企业。 K3-256k 模型是 API 层面的变化，并非不同模型；它使用相同的底层 K3 架构，但上下文限制更小。完整的 K3 模型支持高达 1M token，消耗约两倍的配额。

hackernews · monneyboi · Jul 29, 19:25 · [社区讨论](https://news.ycombinator.com/item?id=49101852)

**背景**: Kimi K3 是一个 2.8 万亿参数的混合专家模型，支持 1M token 上下文，采用 Kimi Delta Attention 和 Attention Residuals 技术。基于上下文的定价正在成为一种将成本与处理更长序列的计算开销对齐的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kimi-ai.chat/models/kimi-k3/">Kimi K 3 : 1M Context, API Pricing & Limits</a></li>
<li><a href="https://vllm.ai/blog/2026-07-27-k3">Kimi K 3 Is Here: Efficient Day-0 Support on vLLM | vLLM Blog</a></li>
<li><a href="https://www.aimagicx.com/blog/llm-api-pricing-comparison-2026">LLM API Pricing in 2026: The Complete Cost Comparison... | AI Magicx</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，这功能上与 OpenAI 在 272k token 处的阶梯定价类似，有人对采用硬性截止而非平滑梯度感到惊讶。其他人澄清说，这一变化是 API 层面的，并非量化模型。

**标签**: `#AI`, `#pricing`, `#context length`, `#API`, `#LLM`

---

<a id="item-6"></a>
## [文档型 AI 蠕虫通过 Word 版 Copilot 自我传播](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/) ⭐️ 8.0/10

研究员 Håkon Måløy 展示了一种新型提示注入变体，将对 Microsoft Word 版 Copilot 的攻击升级为自我复制的蠕虫，隐藏在文档中的恶意指令可篡改输出并传播到新文档。 这一发现揭示了 AI 集成生产力工具中的关键安全漏洞，蠕虫可在用户无察觉的情况下传播，可能危及整个组织的敏感数据。 该攻击利用了 Word 版 Copilot 无法区分用户提示和文档内文本的缺陷，使得隐藏指令得以执行并复制到新创建的文件中。截至发布时，尚无针对此类漏洞的可靠缓解措施。

hackernews · Canopy9560 · Jul 29, 11:44 · [社区讨论](https://news.ycombinator.com/item?id=49096188)

**背景**: 提示注入攻击是将恶意指令嵌入 AI 模型处理的数据中，使其违背用户意图行事。本例中，攻击者将指令隐藏在 Word 文档中；当 Word 版 Copilot 处理该文档时，可能遵循这些指令，篡改内容并将攻击传播到用户打开的其他文档。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theregister.com/security/2026/07/29/word-worm-crawls-into-copilot-spreads-chaos/5280588">Word worm crawls into Copilot , spreads chaos</a></li>
<li><a href="https://dev.to/onsen/ai-worms-in-word-how-document-borne-threats-self-propagate-5gc7">AI Worms in Word: How Document-Borne Threats Self - Propagate</a></li>
<li><a href="https://penaxtra.com/blog/self-propagating-ai-worm-what-it-means">The Self - Propagating AI Worm : Separating the Signal... | Penaxtra Blog</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了担忧，有人指出指令与数据混合的根本问题不太可能解决。其他人分享了实际担忧，例如蠕虫通过 GitHub 评论或电子邮件传播，还有人报告已完全禁用 Copilot 以避免风险。

**标签**: `#AI security`, `#prompt injection`, `#Copilot`, `#adversarial attacks`, `#LLM vulnerabilities`

---

<a id="item-7"></a>
## [长政策文件无法有效约束 AI 智能体](https://arxiv.org/abs/2607.25398) ⭐️ 8.0/10

一篇题为《Handbook.md》的新论文表明，由于长上下文模型的根本性局限，长政策文档无法可靠地约束 AI 智能体，这一结论得到了社区轶事的佐证。 这一发现挑战了使用冗长政策文档控制 AI 智能体的常见做法，凸显了在智能体部署于实际任务时的关键安全与可靠性问题。 该论文提供了经验证据，表明拥有大上下文窗口的模型仍无法遵循长指令，社区评论将其归因于 KV 缓存量化、采样器质量差以及工作记忆有限。

hackernews · spIrr · Jul 29, 13:01 · [社区讨论](https://news.ycombinator.com/item?id=49096969)

**背景**: 长上下文 LLM 声称能处理数百万个 token，但其可靠遵循指令的能力会随长度下降。AI 智能体常依赖政策文档来约束行为，但这种方法假设模型能有效利用所有提供的上下文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/you-cannot-govern-autonomous-ai-agents-policy-documents-alberto-rosas-k0xee">You Cannot Govern Autonomous AI Agents With Policy Documents ...</a></li>
<li><a href="https://www.linkedin.com/pulse/do-we-still-need-rag-now-llms-have-million-token-context-enugala-gtxnc">Do We Still Need RAG Now That LLMs Have Million-Token Context ...</a></li>
<li><a href="https://ai-trends.notion.site/Long-Context-Windows-Opportunities-and-Challenges-1404869badd7804f87b9f596fdb1fee6">Long Context Windows: Opportunities and Challenges | Notion</a></li>

</ul>
</details>

**社区讨论**: 评论者赞同这一发现，分享了 Claude 在短时间内忽略 CLAUDE.md 文件中指令的轶事。有人认为本地推理可以缓解问题，也有人指出即使是人类也难以遵循冗长的政策文档。

**标签**: `#LLMs`, `#long-context`, `#AI safety`, `#benchmarking`, `#agent behavior`

---

<a id="item-8"></a>
## [Anthropic 的密码分析结果引发 AI 智能辩论](https://blog.cryptographyengineering.com/2026/07/29/some-notes-about-anthropics-new-results/) ⭐️ 8.0/10

Anthropic 发布了两个新的密码分析结果，均由他们未发布的先进模型 Claude Mythos 生成，包括对一种签名方案的攻击和对 7 轮 AES-128 的改进密码分析。 这些结果表明，AI 模型在密码分析等复杂推理任务中变得越来越有能力，挑战了关于进展放缓或模型仅仅是“高级自动补全”的观点。 博客文章指出，密码分析中使用的所有成分都不奇特，强调突破来自持续的提示而非新颖技术。Claude Mythos 仍未向公众发布，仅限受信任的合作伙伴访问。

hackernews · supermatou · Jul 29, 16:42 · [社区讨论](https://news.ycombinator.com/item?id=49099804)

**背景**: 密码分析是分析密码系统以发现弱点的研究。像 Claude 这样的 AI 模型正被应用于此类任务，显示出协助发现漏洞的潜力。这些结果由 AI 安全公司 Anthropic 发布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cryptographyengineering.com/2026/07/29/some-notes-about-anthropics-new-results/">Some thoughts about Anthropic ’s new cryptanalysis results</a></li>
<li><a href="https://dataconomy.com/2026/07/29/anthropic-ai-flaws-hawk-aes/">Anthropic AI Uncovers New Attacks On Post-quantum... - Dataconomy</a></li>
<li><a href="https://www.anthropic.com/research/discovering-cryptographic-weaknesses">Discovering cryptographic weaknesses with Claude \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调，这些结果挑战了“高级自动补全”的观点，一位用户指出持续的提示（“不，继续”）是关键。另一位用户推测，未发布的 Mythos 模型在实践中可能被过滤，限制了其在网络安全方面的使用。

**标签**: `#AI`, `#cryptanalysis`, `#Anthropic`, `#machine learning`, `#security`

---

<a id="item-9"></a>
## [Develar app-builder 中存在通过符号链接跟随在 macOS 上任意文件覆盖漏洞](https://kb.cert.org/vuls/id/293714) ⭐️ 8.0/10

Develar 的 app-builder 中的 zipx.Unzip 例程存在漏洞，通过利用 APFS 中的符号链接跟随和 Unicode 规范化冲突，可在 macOS 上实现任意文件覆盖。 该漏洞影响 Electron 生态系统中广泛使用的打包工具 electron-builder，可能破坏构建应用的完整性，并导致供应链攻击。 攻击结合了指向目标文件的名为 'ss' 的符号链接条目和名为 'ß' 的普通文件（APFS 将其视为与 'ss' 等效），从而绕过路径验证。修复措施包括拒绝逃逸输出目录的符号链接，并在文件写入中添加 O_NOFOLLOW。

rss · CERT CC Vulnerability Notes · Jul 29, 17:25

**背景**: APFS（Apple 文件系统）由于 Unicode 规范化，将某些 Unicode 等效文件名视为相同，例如 'ß' 和 'ss'。Develar 的 app-builder 是 electron-builder 用于打包 Electron 应用的命令行工具。漏洞产生的原因是 zipx.Unzip 例程在验证路径之前未执行规范化，从而允许精心构造的 ZIP 存档覆盖任意文件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.strix.ai/cve/CVE-2026-13723">CVE-2026-13723: A vulnerability in the `zipx. Unzip ` extraction routine...</a></li>
<li><a href="https://github.com/develar/app-builder">GitHub - develar / app - builder : Generic helper tool to build app in...</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#macOS`, `#Electron`, `#supply chain`

---

<a id="item-10"></a>
## [OPeNDAP Hyrax 存在 SSRF 和凭证泄露漏洞](https://kb.cert.org/vuls/id/305509) ⭐️ 8.0/10

CERT/CC 披露了 CVE-2026-16637，该漏洞存在于 OPeNDAP Hyrax 中，通过未经验证的 HTTP 重定向绕过 AllowedHosts 白名单，导致 SSRF 和凭证泄露。 该漏洞影响使用 OPeNDAP Hyrax 的科学数据服务器，可能暴露内部服务并泄露 Earthdata 凭证（User-Id、Echo-Token）给攻击者，危及敏感研究数据。 该漏洞源于 Hyrax 在跟随 HTTP 重定向时未重新验证目标是否在 AllowedHosts 白名单中，并且可能转发遗留的 Echo-Token 凭证。补丁预计将在 Hyrax-1.18.0 或更高版本中发布。

rss · CERT CC Vulnerability Notes · Jul 29, 15:18

**背景**: OPeNDAP Hyrax 是一个开源数据服务器，通过 OPeNDAP 协议实现对科学数据集的远程访问。服务器端请求伪造（SSRF）允许攻击者从服务器向内部或外部系统发起请求。Earthdata Login 是 NASA 用于访问地球观测数据的认证系统，而 Echo-Token 是一种不应暴露的遗留凭证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://portswigger.net/web-security/ssrf">What is SSRF (Server-side request forgery)? Tutorial & Examples</a></li>
<li><a href="https://urs.earthdata.nasa.gov/">Earthdata Login</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#SSRF`, `#OPeNDAP`, `#credential disclosure`

---

<a id="item-11"></a>
## [Cisco FMC 静态凭据漏洞允许未认证访问](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-static-cred-BET3Cjh?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Cisco%20Secure%20Firewall%20Management%20Center%20Software%20Static%20Credential%20Vulnerability%26vs_k=1) ⭐️ 8.0/10

Cisco 披露了 Secure Firewall Management Center (FMC) 软件中的一个高严重性漏洞 (CVE-2026-20316)，其中低权限账户的静态凭据允许未经认证的远程攻击者登录并访问敏感数据。该漏洞已在零日攻击中被积极利用。 该漏洞至关重要，因为它可与其他 FMC 漏洞结合以提升权限，可能导致系统完全受损。它影响广泛部署的企业防火墙管理软件，使许多组织面临风险。 该漏洞源于 Web 界面中低权限账户的硬编码凭据。如果 FMC 管理接口未暴露于公共互联网，攻击面会减小。Cisco 已发布软件更新，且没有可用的变通方案。

rss · Cisco Security Advisories · Jul 29, 16:00

**背景**: Cisco Secure Firewall Management Center (FMC) 是 Cisco 防火墙的集中管理平台。静态凭据是嵌入在软件中的固定、不可更改的密码，攻击者可以发现并使用它们获得未授权访问。Cisco 安全影响评级 (SIR) 为高，反映了与其他漏洞结合时可能提升权限的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/cisco-warns-of-fmc-static-credential-flaw-exploited-in-zero-day-attacks/">Cisco warns of FMC static credential flaw exploited in zero-day attacks</a></li>

</ul>
</details>

**标签**: `#Cisco`, `#vulnerability`, `#security`, `#firewall`, `#static credentials`

---

<a id="item-12"></a>
## [两个 API 设置使 GPT-5.6 在 ARC-AGI-3 上得分翻三倍](https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores) ⭐️ 8.0/10

OpenAI 发现，启用两个 API 设置——跨轮次保留推理和启用压缩——使 GPT-5.6 Sol 在 ARC-AGI-3 基准测试上的得分从约 0.37%提升至超过 1%，翻了三倍。这一改进无需任何模型重新训练或架构变更。 这一结果表明，简单的推理时调整就能显著提升 AI 在挑战性推理基准上的表现，为无需昂贵重新训练即可改进 AI 提供了实用路径。同时，它也凸显了记忆和上下文管理对于复杂多步推理任务的重要性。 这两个设置是 OpenAI Responses API 的一部分：'retain_reasoning'保留模型在对话轮次间的思维链，而'compaction'用更高效的上下文压缩方法替代滚动截断。GPT-5.6 Sol 是 GPT-5.6 系列的旗舰模型，定价为每百万输入 tokens 5 美元，每百万输出 tokens 30 美元。

rss · OpenAI Blog · Jul 29, 15:00

**背景**: ARC-AGI-3 是 ARC Prize Foundation 于 2026 年 3 月发布的一个交互式推理基准测试，提供超过 200 万美元奖金，奖励能在新颖推理任务上匹敌未经训练的人类的人工智能。根据初始排行榜，没有前沿模型得分超过 0.37%。该基准测试挑战 AI 探索新环境、即时获取目标、构建可适应的世界模型并持续学习。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC - AGI - 3</a></li>
<li><a href="https://winbuzzer.com/2026/03/30/arc-agi-3-offers-2m-ai-matching-human-reasoning-benchmark-xcxwbn/">ARC - AGI - 3 Offers $2M for AI Matching Human Reasoning</a></li>

</ul>
</details>

**标签**: `#AI`, `#ARC-AGI`, `#GPT`, `#reasoning`, `#benchmark`

---

<a id="item-13"></a>
## [OpenAI 为 10 万研究人员免费提供 ChatGPT](https://openai.com/index/chatgpt-for-academic-researchers) ⭐️ 8.0/10

OpenAI 宣布将为 10 万名学术研究人员免费提供其最先进的 ChatGPT 模型，以加速科学发现。 这一举措使学术界能够平等使用尖端 AI，可能加速医学、物理学和生物学等领域的研究。 该优惠包括对最先进模型（如 GPT-4 和 GPT-4 Turbo）的访问权限，符合条件的研究人员无需付费。

rss · OpenAI Blog · Jul 29, 10:00

**背景**: ChatGPT 是 OpenAI 开发的大型语言模型，能生成类似人类的文本，并协助写作、分析和编程等任务。学术研究人员常因预算限制而无法使用此类先进 AI 工具。

**标签**: `#AI`, `#OpenAI`, `#Academic Research`, `#Scientific Discovery`, `#ChatGPT`

---

<a id="item-14"></a>
## [AI 在后量子密码学转型中的作用](https://simonwillison.net/2026/Jul/29/matthew-green/#atom-everything) ⭐️ 8.0/10

著名密码学家 Matthew Green 指出，当前向后量子密码学的转型是 AI 推进密码分析的绝佳时机，可能增强对 HAWK 等新算法的信心。 这一评论强调了 AI 在破解和增强密码系统方面的双重潜力，这在全球向抗量子标准过渡的关键时期尤为重要。如果 AI 在密码分析上取得成功，它可以验证新算法的安全性并防止未来的漏洞。 Green 提到了 Impagliazzo 的“Minicrypt”世界，即 AI 可能破坏所有难题的场景，但他乐观地认为 AI 反而会加强密码分析文献。背景是 Anthropic 最近的工作，其中 AI 模型在 60 小时内削弱了后量子签名方案 HAWK。

rss · Simon Willison · Jul 29, 18:18

**背景**: 后量子密码学旨在取代当前易受量子计算机攻击的公钥算法（如 RSA 和 ECC）。NIST 正在举办竞赛以标准化新算法，HAWK 是候选数字签名方案之一。Impagliazzo 的五种世界描述了可能的计算复杂性场景，其中 Minicrypt 是存在单向函数但公钥密码学不可能的世界。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.resultsense.com/news/2026-07-29-claude-cryptographic-weaknesses-hawk-aes/">AI model weakens NIST post - quantum candidate in 60 hours</a></li>
<li><a href="https://bravenewcoin.com/insights/mythos-weakened-a-post-quantum-cipher-for-100000">Mythos Weakened a Post - Quantum Cipher for $100,000</a></li>
<li><a href="https://blog.computationalcomplexity.org/2004/06/impagliazzos-five-worlds.html">Computational Complexity: Impagliazzo 's Five Worlds</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#cryptanalysis`, `#AI`, `#security`

---

<a id="item-15"></a>
## [Vision Pro 用于沉浸式建筑漫游](https://christianselig.com/2026/07/vision-pro-house/) ⭐️ 7.0/10

Christian Selig 描述了使用 Apple Vision Pro 进行沉浸式建筑漫游，以直观评估空间比例并模拟一年中不同时间的阳光。 这一新颖应用展示了 Vision Pro 在娱乐之外的潜力，为建筑师和房主提供了施工前进行设计验证和日照分析的强大工具。 漫游允许用户体验 1:1 比例感知和动态光照，帮助识别比例问题并优化窗户位置以提高能效和舒适度。

hackernews · robbiet480 · Jul 29, 20:39 · [社区讨论](https://news.ycombinator.com/item?id=49102774)

**背景**: 多年来，虚拟现实建筑漫游已通过 HTC Vive 和 Quest 3 等头显实现，但 Vision Pro 的高分辨率显示屏和空间计算能力提供了更流畅、更直观的体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nuviraspace.com/vr-architectural-walkthroughs/">7 Key Ways VR Architectural Walkthroughs Outperform Static...</a></li>
<li><a href="https://shadowmap.org/">Shadowmap | The Sun for Everyone – Sunlight & Shadow Analysis in...</a></li>
<li><a href="https://rendimension.com/blog/examples-of-immersive-walkthroughs-for-architecture-pros/">Immersive Walkthrough Examples for Architects | Rendimension</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了使用 VR 进行建筑设计的积极体验，其中一位指出，在走过模拟后，实际建成的房子感觉与虚拟模型完全一样。另一位建议将用途扩展到追踪现有房屋中的布线和管道。

**标签**: `#Vision Pro`, `#Architecture`, `#VR`, `#Design`, `#Spatial Computing`

---

<a id="item-16"></a>
## [Mitchell Hashimoto 创立 Superlogical，将 Ghostty 转让给非营利组织](https://www.superlogical.com/) ⭐️ 7.0/10

Mitchell Hashimoto 宣布成立新公司 Superlogical，该公司将在开源终端库 libghostty 之上构建商业产品。他已将 Ghostty 的所有权转让给一个非营利组织，确保该项目保持社区治理。 此举展示了一种可持续的开源商业模式：公司在社区拥有的基础之上构建专有产品，类似于 Red Hat 或 GitLab 的运作方式。同时，它确保了 Ghostty 的长期独立性，并鼓励更广泛地将 libghostty 作为终端应用的共享构建块来使用。 Superlogical 将使用与所有人相同的 MIT 许可证下的 libghostty，并将上游改进贡献回社区。Ghostty 是一个快速、跨平台的终端模拟器，使用 GPU 加速和平台原生 UI，libghostty 用 C 和 Zig 编写。

hackernews · yan · Jul 29, 15:41 · [社区讨论](https://news.ycombinator.com/item?id=49098965)

**背景**: Ghostty 是一款以性能和跨平台支持著称的现代终端模拟器。HashiCorp 联合创始人 Mitchell Hashimoto 创建了 Ghostty 作为开源项目。通过将所有权转让给非营利组织，他确保项目的治理独立于任何单一公司，类似于 Linux 基金会或 Blender 基金会使用的模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ghostty.org/">Ghostty</a></li>
<li><a href="https://github.com/ghostty-org/ghostty">GitHub - ghostty -org/ ghostty : Ghostty is a fast, feature-rich, and...</a></li>

</ul>
</details>

**社区讨论**: 社区反应积极，许多人称赞将所有权转让给非营利组织是对开源的有力承诺。一些人将其与 OLE/COM 相提并论，认为 libghostty 可以实现可组合的终端应用。少数用户批评标题含糊不清，但总体情绪是支持的。

**标签**: `#open source`, `#terminal`, `#business model`, `#Mitchell Hashimoto`, `#software engineering`

---

<a id="item-17"></a>
## [KOReader：开源电子书阅读器应用提升 Kobo 和 Kindle 体验](https://koreader.rocks/) ⭐️ 7.0/10

KOReader，一款开源电子书阅读器应用，在 Kobo 和 Kindle 等设备用户中持续获得关注，提供原生 EPUB 和 PDF 支持、Calibre 无线同步以及可自定义手势等高级功能。 KOReader 展示了开源软件增强专有电子阅读器的能力，让用户拥有更多控制权和功能。其强大的社区支持和高参与度（656 分，211 条评论）凸显了其对阅读爱好者的价值。 用户报告称 KOReader 显著改善了阅读体验，但部分人指出其界面不够直观且偶尔有卡顿。该应用支持越狱的 Kindle 以及 Remarkable 2 和小米墨案 InkPalm 5 等设备。

hackernews · Cider9986 · Jul 29, 11:05 · [社区讨论](https://news.ycombinator.com/item?id=49095865)

**背景**: KOReader 是一个主要为电子墨水屏设备设计的开源文档查看器。它源自 Cool Reader 项目的分支，已发展成功能丰富的替代固件，支持多种格式并提供定制选项。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tiktok.com/discover/e-reader-that-allows-you-to-download-from-anywhere">E Reader That Allows You to Download from Anywhere | TikTok</a></li>
<li><a href="https://en.wikipedia.org/wiki/Comparison_of_e-book_formats">Comparison of e -book formats - Wikipedia</a></li>
<li><a href="https://www.the-ebook-reader.com/kindle-comparison.html">Kindle Comparison Table - Kindle Buying Guide</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体积极，用户称赞 KOReader 的功能和自由度。但部分用户批评其界面不直观和手势操作卡顿，一名用户因此放弃使用。总体而言，讨论体现了热情与建设性反馈的平衡。

**标签**: `#open-source`, `#e-reader`, `#software`, `#community`

---

<a id="item-18"></a>
## [AI 公司招聘数千名电工和木匠](https://www.nytimes.com/2026/07/29/business/economy/data-center-electricians-training.html) ⭐️ 7.0/10

AI 公司正在招聘数千名电工和木匠来建设数据中心，标志着劳动力需求向建筑行业的重大转变。 这一趋势凸显了 AI 所需的大规模基础设施建设，为技工行业创造了新的就业机会，同时也引发了对繁荣-萧条周期和未来冷却需求的担忧。 文章指出，数据中心建设是劳动密集型的，需要电工负责电力系统，木匠负责结构工作，繁荣期工资可能很高，但低迷期不稳定。

hackernews · thm · Jul 29, 14:43 · [社区讨论](https://news.ycombinator.com/item?id=49098198)

**背景**: 数据中心是容纳 AI 和云计算服务计算硬件的设施。其建设需要专业技工，如电工负责高压布线，木匠负责框架和冷却基础设施。

**社区讨论**: 评论者警告繁荣-萧条周期，有人指出电工可能一年赚 30 万美元，下一年只赚 3 万美元。另有人提到未来液体冷却需求，暗示水管工可能成为下一个需求热点。

**标签**: `#AI infrastructure`, `#labor market`, `#data centers`, `#technology trends`

---

<a id="item-19"></a>
## [Darktable：免费 RAW 编辑器媲美付费软件](https://www.darktable.org/) ⭐️ 7.0/10

Darktable，一款免费开源的 RAW 照片编辑器，作为 Adobe Lightroom 等付费软件的强大替代品持续获得关注，以零成本提供丰富的功能和流程。 这很重要，因为它为摄影师（尤其是预算有限或使用 Linux 的用户）提供了专业级工具，挑战了专有软件的主导地位，可能降低成本并提高可及性。 Darktable 具有虚拟灯箱和暗房功能，在数据库中管理数字底片，并支持多种相机。然而，它的学习曲线陡峭，一些用户报告与 Lightroom 相比存在性能问题和组织方面的不足。

hackernews · siatko · Jul 29, 12:33 · [社区讨论](https://news.ycombinator.com/item?id=49096654)

**背景**: RAW 文件包含来自数码相机的未处理传感器数据，比 JPEG 提供更大的编辑灵活性。Darktable 是一款处理这些 RAW 文件的开源应用程序，提供曝光校正、调色等工具，类似于 Adobe Lightroom 但免费。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.darktable.org/">darktable</a></li>
<li><a href="https://fixthephoto.com/darktable-review.html">Darktable Review 2026 – Is Darktable Better Than Adobe Lr?</a></li>

</ul>
</details>

**社区讨论**: 社区评论褒贬不一：许多人称赞 Darktable 的功能和质量，认为它是付费软件的可行替代品；而其他人则批评其在某些硬件上性能缓慢以及版本间破坏性的工作流程变更。由于发展方向分歧，存在一个名为 Ansel 的分支。

**标签**: `#photography`, `#open source`, `#RAW editing`, `#software review`

---

