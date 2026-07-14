# Horizon 每日速递 - 2026-07-14

> From 43 items, 15 important content pieces were selected

---

1. [llama.cpp b9993 新增 Hy3 模型支持与 MTP 推测解码](#item-1) ⭐️ 8.0/10
2. [Telegram 的 t.me 域名被注册商暂停](#item-2) ⭐️ 8.0/10
3. [三星健康应用威胁：拒绝 AI 训练将删除数据](#item-3) ⭐️ 8.0/10
4. [前 NOAA 员工推出 Climate.us 以保护气候数据](#item-4) ⭐️ 8.0/10
5. [对 15 款电子垃圾 GPU 进行现代 AI 工作负载基准测试](#item-5) ⭐️ 8.0/10
6. [CISA 的 GitHub 泄露事件复盘：安全团队的关键教训](#item-6) ⭐️ 8.0/10
7. [无需 Xcode 图形界面即可构建和发布苹果应用](#item-7) ⭐️ 7.0/10
8. [苹果 SpeechAnalyzer API 与 Whisper 的基准测试](#item-8) ⭐️ 7.0/10
9. [Sega CD《Silpheed》FMV 工程深度解析](#item-9) ⭐️ 7.0/10
10. [免费 API 聚合 2.48 亿条 VEX 声明，45%的 CVE 不受影响](#item-10) ⭐️ 7.0/10
11. [YouTube 吉他谱解析器利用 Claude 视觉生成 PDF](#item-11) ⭐️ 7.0/10
12. [在 SQL 中实现神经网络](#item-12) ⭐️ 7.0/10
13. [CISA 将 Cisco IOS CSRF 漏洞加入已知被利用漏洞目录](#item-13) ⭐️ 7.0/10
14. [DOOMQL：将 SQLite 用作类 Doom 游戏引擎](#item-14) ⭐️ 7.0/10
15. [Datasette 代码频率图展示 AI 影响](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [llama.cpp b9993 新增 Hy3 模型支持与 MTP 推测解码](https://github.com/ggml-org/llama.cpp/releases/tag/b9993) ⭐️ 8.0/10

llama.cpp 版本 b9993 新增了对腾讯 Hy3（混元 3）模型架构的支持，这是一个 295B 参数的混合专家（MoE）模型，并引入了多令牌预测（MTP）推测解码以加速推理。 此版本使 llama.cpp 用户能够在本地运行腾讯强大的开源权重 Hy3 模型，并通过 MTP 推测解码提升推理速度，扩展了消费级硬件上支持的大语言模型生态系统。 Hy3 架构具有每头 Q/K RMSNorm、带专家选择偏置的 sigmoid 路由器、始终激活的无门控共享专家以及前导密集块（first_k_dense_replace）。该实现从 charlie12345 的分支移植并适配了当前主线 API。

github · github-actions[bot] · Jul 13, 23:09

**背景**: llama.cpp 是一个流行的开源 C++ 库，用于在 CPU 和 GPU 上高效运行大语言模型。Hy3（混元 3）模型是腾讯的 295B 参数 MoE 模型，每个令牌仅激活 21B 参数，使其适合本地部署。MTP 推测解码允许模型每次前向传播预测多个令牌，从而提高吞吐量而不牺牲输出质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.runlocalai.co/models/hunyuan-3.0">Hunyuan 3 .0 ( Hy 3 ) — local inference guide | RunLocalAI</a></li>
<li><a href="https://www.spheron.network/blog/deploy-hunyuan-3-gpu-cloud/">Deploy Hunyuan 3 on GPU Cloud: Self-Host... | Spheron Blog</a></li>
<li><a href="https://medium.com/practical-llm-systems/i-tested-mtp-speculative-decoding-on-two-qwen-models-one-was-a-trap-46c2dfe584c7">I Tested MTP Speculative Decoding on Two Qwen Models... | Medium</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#model support`, `#speculative decoding`, `#MoE`, `#open-source`

---

<a id="item-2"></a>
## [Telegram 的 t.me 域名被注册商暂停](https://www.whois.com/whois/t.me) ⭐️ 8.0/10

Telegram 的短链接域名 t.me 已被其注册商 GoDaddy 暂停，WHOIS 状态码显示包括 clientHold 和 clientRenewProhibited。 此次暂停可能影响全球数百万用户对 Telegram 短链接的访问，并引发对注册商在域名争议中权力的担忧。 域名状态码表明暂停很可能源于法律或监管行动，社区讨论指出可能来自俄罗斯、法国或印度。

hackernews · Tiberium · Jul 13, 19:52 · [社区讨论](https://news.ycombinator.com/item?id=48897878)

**背景**: 域名暂停是指注册商或注册局将域名置于保留状态，通常因法律纠纷或政策违规。GoDaddy 是一家大型域名注册商，但因不透明的暂停做法而受到批评。Telegram 的 t.me 域名用于短链接和频道引用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://domainnamewire.com/2026/06/17/godaddy-customer-must-pay-652k-after-suing-over-domain-suspension/">GoDaddy customer must pay $652k after suing over domain ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论对 Telegram 依赖 GoDaddy 表示惊讶，因其以不透明著称。用户还推测法律原因，印度考试泄题调查是主要嫌疑对象。有人指出在暂停前刚启动 Telegram 频道的讽刺性。

**标签**: `#Telegram`, `#domain suspension`, `#ICANN`, `#GoDaddy`, `#legal investigation`

---

<a id="item-3"></a>
## [三星健康应用威胁：拒绝 AI 训练将删除数据](https://neow.in/cWsyMTV3) ⭐️ 8.0/10

三星健康更新了政策，要求用户同意将其健康数据用于 AI 训练，否则将删除所有已收集的数据。该政策涵盖睡眠、用药、医疗记录和周期追踪数据。 这引发了严重的隐私担忧，因为用户被迫在失去健康数据或允许敏感信息用于 AI 训练之间做出选择。它为科技公司如何处理用户数据同意设定了有争议的先例。 数据类别包括身体测量、营养、步数、活动和睡眠数据。选择退出的用户数据将被删除，但仍可使用不收集数据的基本功能。

hackernews · bundie · Jul 13, 20:01 · [社区讨论](https://news.ycombinator.com/item?id=48897991)

**背景**: 三星健康是一款健身和健康追踪应用，从三星设备收集各种健康指标。AI 训练利用这些数据改进算法和功能，但当同意成为强制要求时，会引发隐私问题。类似做法在 Meta 和 Google 等其他公司也受到批评。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://9to5google.com/2026/07/13/samsung-health-ai-training-data-consent/">Samsung Health will delete your data without AI training consent</a></li>
<li><a href="https://www.androidauthority.com/samsung-health-train-ai-data-3686684/">Samsung will kill your health data if you don't consent to AI training</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了不满，有人指出选择退出会使设备可用性降低，并质疑是否应获得部分退款。另一个人讽刺地欢迎删除数据作为隐私好处。还有人批评三星健康糟糕的用户体验和广告。

**标签**: `#privacy`, `#health data`, `#AI training`, `#Samsung`, `#data ethics`

---

<a id="item-4"></a>
## [前 NOAA 员工推出 Climate.us 以保护气候数据](https://19thnews.org/2026/07/noaa-climate-data-website/) ⭐️ 8.0/10

前 NOAA 员工推出了 Climate.us 网站，旨在保存并提供公众访问可能受当前政府威胁的气候数据。 该举措确保纳税人资助的气候数据在政治威胁下仍可公开获取，支持科学研究、政策制定和公众意识。 该网站依赖捐款运营，正如社区评论所指出的，它专注于历史和持续的数据收集与存档。

hackernews · benwerd · Jul 13, 19:57 · [社区讨论](https://news.ycombinator.com/item?id=48897945)

**背景**: NOAA（美国国家海洋和大气管理局）是美国政府机构，收集和维护大量气候数据。在当前政府下，一些气候数据和数据库已被终止或移除，引发了对数据丢失的担忧。Climate.us 由前 NOAA 员工创建，旨在存档并提供对这些关键数据的访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ncei.noaa.gov/cdo-web/">Climate Data Online (CDO) - The National Climatic Data ...</a></li>
<li><a href="https://www.perplexity.ai/page/noaa-ends-billion-dollar-weath-AVJDkuU2S4.mbIxw6gDFeQ">NOAA ends billion-dollar weather disasters database</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了对数据保存的支持，同时提出了关于长期可持续性和资金的问题。一些人讨论了使用 IPFS 等去中心化存储来存放政府数据的想法，而另一些人则辩论政府数据是否应自动属于公共领域。

**标签**: `#climate data`, `#data preservation`, `#open data`, `#government transparency`, `#archiving`

---

<a id="item-5"></a>
## [对 15 款电子垃圾 GPU 进行现代 AI 工作负载基准测试](https://esologic.com/benchmarking-tesla-gpus/) ⭐️ 8.0/10

一项对 15 款旧 GPU（如 Tesla P100、V100）在 LLM 推理等现代任务上的详细基准测试表明，电子垃圾 GPU 在 AI 工作负载中可能具有成本效益。 这很重要，因为它为预算有限的 AI 爱好者和小型团队提供了实用数据，表明旧硬件仍能以可用速度运行现代模型，从而减少电子垃圾并降低入门门槛。 基准测试涵盖 15 款 GPU，包括 Tesla P4、P100、V100 等，使用 Llama 3.1 8B 和 Qwen 2.5 7B 等模型测试 LLM 推理性能。其中 Tesla P4 仅 75W TDP 和 8GB 显存，被强调为特别高效的选择。

hackernews · eso_logic · Jul 13, 13:48 · [社区讨论](https://news.ycombinator.com/item?id=48892638)

**背景**: 电子垃圾 GPU 是指那些常被丢弃但仍可重新用于 AI 推理等非游戏任务的旧显卡。LLM 推理是指运行训练好的大型语言模型以生成文本的过程，这需要大量的 GPU 显存和算力。对这些显卡进行基准测试有助于用户了解它们在现代 AI 工作负载下的实际性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://asibiont.com/en/blog/benchmarking-15-videokart-e-waste-chto-realno-kupit-v-2026-godu-dlya-ai-i-igr">Benchmarking 15 ' E - Waste ' GPUs with Modern... — ASI Biont Blog</a></li>
<li><a href="https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/">Mastering LLM Techniques: Inference Optimization | NVIDIA Technical...</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了实际经验，一位用户称赞 Tesla P4 的低功耗和低成本，另一位则推荐 Radeon Pro V620 作为更新的替代品。一些人在讨论 P100、V100 等显卡中哪款性价比最高，其他人则询问功耗以及在 Qwen 3.6 27B 等更大模型上的性能。

**标签**: `#GPU benchmarking`, `#e-waste`, `#AI inference`, `#LLM`, `#hardware`

---

<a id="item-6"></a>
## [CISA 的 GitHub 泄露事件复盘：安全团队的关键教训](https://krebsonsecurity.com/2026/07/lessons-learned-from-cisas-recent-github-leak/) ⭐️ 8.0/10

CISA 发布了一份数据泄露事件的事后分析报告，该事件中一名承包商在公共 GitHub 仓库中暴露了内部凭证（包括 AWS GovCloud 密钥），持续近六个月后才被 KrebsOnSecurity 告知。 这一事件暴露了主要政府机构在事件响应和凭证管理方面的关键漏洞，为所有安全团队提供了可操作的教训，以防止类似泄露事件。 泄露的凭证在通知后仍有效 48 小时，且 CISA 当时预算和人员配置不足，这可能导致了响应延迟。

rss · Krebs on Security · Jul 13, 15:03

**背景**: CISA 是美国负责网络安全和基础设施保护的联邦机构。AWS GovCloud 是为满足严格合规要求的政府客户设计的云环境。GitHub 是一个流行的代码托管平台，公共仓库中意外泄露凭证是常见的安全风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/">CISA Admin Leaked AWS GovCloud Keys on Github – Krebs on...</a></li>
<li><a href="https://aws.amazon.com/govcloud-us/">AWS GovCloud (US) - Amazon Web Services</a></li>
<li><a href="https://groundy.com/articles/cisa-admin-leaked-aws-govcloud-keys-on-github-what-federal-secret-scanning/">CISA Admin Leaked AWS GovCloud Keys on GitHub: What Federal...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#incident response`, `#GitHub`, `#CISA`, `#data leak`

---

<a id="item-7"></a>
## [无需 Xcode 图形界面即可构建和发布苹果应用](https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/) ⭐️ 7.0/10

一份详细指南展示了如何使用 XcodeGen 和 fastlane 等工具，完全通过命令行构建、签名和发布 Mac 和 iOS 应用，绕过 Xcode 的图形界面。 这使得苹果应用开发能够无缝集成到 CI/CD 流水线和 LLM 辅助编码工作流中，减少手动 GUI 步骤，提高开发者的自动化水平。 该方法需要安装 Xcode 以使用其工具链，但通过 XcodeGen 生成项目文件，fastlane 处理代码签名和部署，全程无需打开 Xcode 的图形界面。

hackernews · speckx · Jul 13, 18:22 · [社区讨论](https://news.ycombinator.com/item?id=48896665)

**背景**: Xcode 是苹果用于 macOS 和 iOS 应用的集成开发环境（IDE），但其图形界面在自动化方面可能缓慢且繁琐。像 xcodebuild、XcodeGen 和 fastlane 这样的命令行工具允许开发者编写构建和发布的脚本，这对于持续集成和交付（CI/CD）流水线至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/">Building and Shipping Mac and iOS Apps Without Ever Opening...</a></li>
<li><a href="https://stackoverflow.com/questions/69315164/how-to-create-an-ios-app-build-using-command-line-tool-without-xcode/69315458">swift - How to create an iOS app build using command line tool...</a></li>
<li><a href="https://fastlane.tools/">fastlane - App automation done right</a></li>

</ul>
</details>

**社区讨论**: 评论者强调了在 Mac 上无沙箱运行编码代理的安全隐患，提及 xAI 上传用户主目录的事件。其他人分享了替代工具，如用于 Linux 上 iOS 开发的 xtool 和面向 LLM 的苹果开发工具 Axiom，同时一位用户感叹 Mac 硬件的高成本是入门障碍。

**标签**: `#iOS development`, `#macOS`, `#automation`, `#CI/CD`, `#LLM tools`

---

<a id="item-8"></a>
## [苹果 SpeechAnalyzer API 与 Whisper 的基准测试](https://get-inscribe.com/blog/apple-speech-api-benchmark.html) ⭐️ 7.0/10

苹果在 iOS 26 和 macOS 26 中推出了新的语音转文本 API SpeechAnalyzer，取代了旧的 SFSpeechRecognizer。Inscribe 的基准测试显示，它比 OpenAI 的 Whisper 更快，但准确率略低。 这可能会颠覆许多仅封装 Whisper 的付费应用，因为苹果可能提供原生的转录界面。这也凸显了向设备端、保护隐私的语音分析发展的趋势。 基准测试在数学讲座上将 SpeechAnalyzer 与 Whisper-Large-V2 进行了对比，发现其速度显著更快，准确率仅略低。但社区成员指出，Nvidia 的 Nemotron 和 Parakeet 或 Mistral 的 Voxtral 等新模型可能是更好的比较对象。

hackernews · get-inscribe · Jul 13, 16:06 · [社区讨论](https://news.ycombinator.com/item?id=48894752)

**背景**: Whisper 是 OpenAI 于 2022 年发布的开源语音识别模型，被广泛使用。苹果的新 SpeechAnalyzer API 专为设备端处理设计，优先考虑隐私和速度。该基准测试由提供语音转文本服务的公司 Inscribe 进行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.apple.com/videos/play/wwdc2025/277/">Bring advanced speech -to-text to your app with... - Apple Developer</a></li>
<li><a href="https://get-inscribe.com/blog/apple-speech-api-benchmark.html">Apple 's New Speech API vs Whisper: The First Real Benchmark</a></li>
<li><a href="https://en.wikipedia.org/wiki/Whisper_(speech_recognition_system)">Whisper ( speech recognition system) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者认为 Whisper 已经过时，像 Nvidia 的 Nemotron 或 Mistral 的 Voxtral 这样的新模型才是更好的基准。一些人担心苹果的原生解决方案可能使许多付费转录应用过时，而另一些人则分享了该 API 在实时转录速度方面的积极体验。

**标签**: `#speech recognition`, `#Apple`, `#benchmarking`, `#ASR`, `#Whisper`

---

<a id="item-9"></a>
## [Sega CD《Silpheed》FMV 工程深度解析](https://fabiensanglard.net/silpheed/index.html) ⭐️ 7.0/10

Fabien Sanglard 发布了一篇详细的技术分析，揭示了 Sega CD 版《Silpheed》如何利用全动态视频（FMV）和巧妙的工程手段在有限硬件上模拟 3D 图形。 该分析突显了早期 3D 模拟技术的独创性，为对硬件限制和创造性问题解决感兴趣的复古游戏开发者与爱好者提供了宝贵见解。 文章解释了《Silpheed》使用预渲染的 3D 背景作为 FMV 播放，并利用 Sega CD 的精灵缩放与旋转硬件实时叠加玩家飞船和敌人。

hackernews · ibobev · Jul 13, 14:52 · [社区讨论](https://news.ycombinator.com/item?id=48893639)

**背景**: Sega CD 是 Genesis 的扩展配件，增加了更快的 CPU 和用于增强精灵缩放与旋转的自定义图形芯片，但缺乏真正的 3D 多边形能力。《Silpheed》是一款射击游戏，通过将 FMV 背景与 2D 精灵结合来模拟 3D，营造出深度和运动的错觉。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mobygames.com/game/11910/silpheed/">Silpheed (1993) - MobyGames</a></li>
<li><a href="https://www.hardcoregaming101.net/silpheed/">Silpheed – Hardcore Gaming 101</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sega_CD">Sega CD - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞了这篇文章，并分享了相关的演示场景成就，例如 Mega Drive 上的 Overdrive 2 和卡带版《Sonic 3D》开场，突显了在有限硬件上实现的令人印象深刻的壮举。

**标签**: `#retro gaming`, `#game development`, `#Sega CD`, `#graphics programming`, `#technical deep-dive`

---

<a id="item-10"></a>
## [免费 API 聚合 2.48 亿条 VEX 声明，45%的 CVE 不受影响](https://getreel.dev/vex) ⭐️ 7.0/10

getreel.dev 上推出了一项新的免费 API，聚合了 2.48 亿条 VEX 声明，显示 45%的 CVE 在任何产品中都不受影响。 这有助于安全团队通过过滤掉无关的 CVE 来优先处理漏洞，减少警报疲劳，专注于实际威胁。 该 API 从多个来源聚合 VEX 声明，提供机器可读的数据，可集成到漏洞管理工作流程中。

rss · Hacker News Show HN · Jul 13, 23:07

**背景**: VEX（漏洞可利用性交换）声明是机器可读的文档，用于指示特定漏洞（CVE）是否实际影响某个产品。传统的漏洞扫描通常会标记所有 CVE，导致噪音；VEX 通过提供产品特定的上下文来帮助过滤误报。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.root.io/concepts/vex">VEX Statements - Root</a></li>
<li><a href="https://secportal.io/blog/vex-vulnerability-exploitability-exchange-guide">VEX Guide: Vulnerability Exploitability eXchange Explained</a></li>
<li><a href="https://www.sbomvault.ai/blog/vex-vulnerability-exploitability-exchange-explained">VEX explained: which CVEs actually matter | SBOMVault.ai</a></li>

</ul>
</details>

**标签**: `#API`, `#Vulnerability Management`, `#CVE`, `#VEX`, `#Security`

---

<a id="item-11"></a>
## [YouTube 吉他谱解析器利用 Claude 视觉生成 PDF](https://github.com/marcelpanse/youtube-guitar-tab-parser) ⭐️ 7.0/10

一款名为 youtube-guitar-tab-parser 的新命令行工具，利用 Claude 视觉 API 从 YouTube 教学视频中提取吉他谱，并将检测到的谱线拼接成 PDF 文档。 该工具提供了一种新颖实用的方法，从视频中转录吉他谱，有望为音乐人节省数小时的手动转录时间，使学习歌曲更加高效。 该工具下载视频、采样帧、使用 Claude 视觉定位谱表区域、裁剪帧、根据小节号去重，并将不同的谱线垂直拼接成 PDF。

rss · Hacker News Show HN · Jul 13, 20:13

**背景**: 吉他谱（tab）是一种指示指板按弦位置的乐谱形式，常用于在线教学。现有的转录服务通常无法准确从视频中提取谱表，尤其是当谱表显示在屏幕上时。该工具利用计算机视觉和大语言模型（LLM）来克服这些限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude-api-cookbook.vercel.app/claude-api-vision-multimodal/">Claude Vision API : Image Analysis with Python & Node.js (2026)</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（41 条评论）显示出浓厚兴趣，用户称赞巧妙使用 Claude 视觉，并讨论潜在改进，如处理不同谱表样式和增加对其他乐器的支持。部分用户对 API 成本及在不同视频格式上的可靠性表示担忧。

**标签**: `#guitar`, `#computer vision`, `#CLI`, `#music transcription`, `#LLM`

---

<a id="item-12"></a>
## [在 SQL 中实现神经网络](https://github.com/xqlsystems/xarray-sql/blob/claude/xarray-sql-mnist-demo/benchmarks/nn.py) ⭐️ 7.0/10

作者利用 Xarray-SQL 的数组到表格映射，完全在 SQL 中实现了一个神经网络，证明了矩阵乘法和自动微分可以表示为关系操作。 这项工作挑战了神经网络需要专门数组框架的假设，表明 SQL 数据库可以作为具有逻辑-物理分离的分布式训练平台，可能简化大规模 GPU 训练。 该实现利用 DataFusion 的访问者模式进行自动微分（受 JAX 启发），并利用该模型中梯度简化为雅可比矩阵对角线上的逐行操作这一洞察。神经网络已通过 Coiled 的地理空间基准验证。

rss · Hacker News Show HN · Jul 13, 20:00

**背景**: Xarray-SQL 是一个实验性库，将多维数组映射到关系表，从而允许对数组数据执行 SQL 查询。Coiled 地理空间基准套件测试大规模（100 TB）气候和地理操作。作者之前的工作表明，重网格化是一个稀疏矩阵-向量乘积，可以用 SQL 的 JOIN 和 GROUP BY 表达。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/alxmrs/xarray-sql">GitHub - alxmrs/ xarray - sql : An experiment to query Xarray datasets...</a></li>
<li><a href="https://xql.systems/xarray-sql/">xarray - sql - xarray - sql</a></li>
<li><a href="https://docs.coiled.io/blog/geospatial-benchmarks.html">Large Scale Geospatial Benchmarks — Coiled documentation</a></li>

</ul>
</details>

**标签**: `#neural networks`, `#SQL`, `#array databases`, `#geospatial`, `#data modeling`

---

<a id="item-13"></a>
## [CISA 将 Cisco IOS CSRF 漏洞加入已知被利用漏洞目录](https://www.cisa.gov/news-events/alerts/2026/07/13/cisa-adds-one-known-exploited-vulnerability-catalog) ⭐️ 7.0/10

CISA 已将 CVE-2008-4128（Cisco IOS 12.4 中的跨站请求伪造漏洞）添加到其已知被利用漏洞（KEV）目录中，原因是该漏洞已被积极利用。 此次添加触发了美国联邦机构根据约束性操作指令（BOD）26-04 的强制修复要求，该指令要求对公开暴露资产上的高风险漏洞在 72 小时内完成修补。这也向所有组织表明，这个旧漏洞仍然是一个真实威胁。 CVE-2008-4128 影响 Cisco IOS 12.4，允许远程攻击者通过 CSRF 执行任意命令。BOD 26-04 取代了 BOD 22-01 和 19-02，强调基于风险的优先级排序，并要求机构在修补前检查是否存在被入侵迹象。

rss · CISA Cybersecurity Advisories · Jul 13, 12:00

**背景**: CISA 的已知被利用漏洞（KEV）目录列出了已被积极利用的漏洞，作为修复的优先级列表。约束性操作指令（BOD）26-04 是 CISA 的一项指令，要求联邦机构快速修复高风险漏洞，特别是那些可能让攻击者获得完全控制权的面向互联网的系统。Cisco IOS 是一种在企业及政府网络中广泛使用的网络操作系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://f1tym1.com/2026/07/13/cisa-adds-cisco-ios-cross-site-request-forgery-vulnerability-to-known-exploited-catalog/">CISA Adds Cisco IOS Cross - Site Request Forgery Vulnerability to...</a></li>
<li><a href="https://hacknjill.com/cybersecurity/cybersecurity-threats-and-defense/cve-2008-4128-cisco-ios-cross-site-request-forgery-vulnerability-actively-exploi/">CVE-2008-4128: Cisco IOS Cross - Site Request Forgery ... - Hack'n Jill</a></li>

</ul>
</details>

**标签**: `#CISA`, `#vulnerability`, `#KEV`, `#Cisco IOS`, `#security`

---

<a id="item-14"></a>
## [DOOMQL：将 SQLite 用作类 Doom 游戏引擎](https://simonwillison.net/2026/Jul/13/doomql/#atom-everything) ⭐️ 7.0/10

Peter Gostev 构建了 DOOMQL，一款类 Doom 的第一人称射击游戏，其中 SQLite 通过 SQL 查询处理所有游戏逻辑，包括移动、碰撞、敌人和渲染。该游戏作为 Python 终端脚本运行，并使用递归 CTE 在 SQL 中实现完整的光线追踪器。 DOOMQL 展示了 SQLite 的非传统创意用法，突破了数据库能力的边界。它彰显了 SQL 在实时模拟方面的潜力，可能激发游戏开发和数据库驱动应用的新思路。 该游戏使用 GPT-5.6 Sol 实现为 Python 终端脚本，渲染 SQL 查询是一个大型递归 CTE，每帧为每个像素生成一行。游戏状态存储在 SQLite 数据库中，可使用 Datasette 进行探索，Datasette App 插件可显示实时小地图与游戏视图。

rss · Simon Willison · Jul 13, 22:34

**背景**: SQLite 是一个自包含、无服务器、零配置的数据库引擎，广泛用于移动应用、浏览器和嵌入式系统，以其可靠性和小巧著称。DOOMQL 利用 SQLite 的递归 CTE 和虚拟表，完全在 SQL 查询中执行实时光线投射和游戏逻辑，将数据库视为核心模拟引擎而不仅仅是数据存储。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/petergpt/doomql">GitHub - petergpt/ doomql : A playable terminal FPS whose simulation...</a></li>
<li><a href="https://www.sqlite.org/">SQLite Home Page</a></li>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT - 5 . 6 Sol : a next-generation model | OpenAI</a></li>

</ul>
</details>

**标签**: `#SQLite`, `#game development`, `#creative coding`, `#Python`, `#retro gaming`

---

<a id="item-15"></a>
## [Datasette 代码频率图展示 AI 影响](https://simonwillison.net/2026/Jul/13/datasette-code-frequency/#atom-everything) ⭐️ 7.0/10

Simon Willison 分享了他的开源项目 Datasette 的 GitHub 代码频率图，显示 2026 年代码增删出现巨大峰值，他将其归因于编码代理和 Opus 4.8、GPT-5.5、Fable 5、GPT-5.6 Sol 等先进 AI 模型的使用。 这提供了具体的数据驱动证据，展示了 AI 辅助开发工具如何显著提升开源生产力，为关于编码代理对软件开发影响的讨论提供了真实世界的基准。 最大峰值显示 2026 年单周新增 37,022 行、删除 9,528 行，远超此前峰值。该图表覆盖 2018 年至 2026 年的活动，早期显著峰值出现在 2018 年初和 2025 年末。

rss · Simon Willison · Jul 13, 21:45

**背景**: GitHub 的代码频率图可视化仓库中每周代码行的增删情况。Datasette 是由 Simon Willison 创建的开源数据探索与发布工具。编码代理是能够自主编写和修改代码的 AI 系统，通常由 GPT 和 Claude 等大型语言模型驱动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/13/datasette-code-frequency/">datasette code - frequency chart on GitHub | Simon Willison’s Weblog</a></li>
<li><a href="https://datasette.io/">Datasette : An open source multi-tool for exploring and publishing data</a></li>
<li><a href="https://github.com/simonw/datasette">GitHub - simonw/ datasette : An open source multi-tool for exploring and...</a></li>

</ul>
</details>

**标签**: `#AI-assisted development`, `#open source`, `#productivity`, `#coding agents`

---

