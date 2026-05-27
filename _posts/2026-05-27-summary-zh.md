---
layout: default
title: "Horizon Summary: 2026-05-27 (ZH)"
date: 2026-05-27
lang: zh
---

> From 44 items, 16 important content pieces were selected

---

1. [AI 辅助安全报告导致 curl 维护者倦怠](#item-1) ⭐️ 9.0/10
2. [llama.cpp b9330 修复 GPU 性能回退](#item-2) ⭐️ 8.0/10
3. [甲基丙烯酸甲酯储罐事故的化学分析](#item-3) ⭐️ 8.0/10
4. [维基媒体裁员引发编辑罢工和愤怒](#item-4) ⭐️ 8.0/10
5. [外包加本地 AI 可能在成本上超越前沿实验室](#item-5) ⭐️ 8.0/10
6. [荷兰阻止美国收购数字身份供应商](#item-6) ⭐️ 8.0/10
7. [微软 Copilot Cowork 代理可通过提示注入窃取文件](#item-7) ⭐️ 8.0/10
8. [SGLang v0.5.12.post1 修复 DeepSeek V4 关键错误](#item-8) ⭐️ 7.0/10
9. [西班牙以缺乏赌博牌照为由封禁 Polymarket 和 Kalshi](#item-9) ⭐️ 7.0/10
10. [Dropbox CEO Drew Houston 卸任](#item-10) ⭐️ 7.0/10
11. [对话式聊天机器人让用户沮丧](#item-11) ⭐️ 7.0/10
12. [Monkdev：提升 LLM 代码生成的工具包](#item-12) ⭐️ 7.0/10
13. [Minicor 推出面向 AI 公司的可扩展桌面 RPA](#item-13) ⭐️ 7.0/10
14. [CISA 将 LiteSpeed cPanel 插件漏洞加入 KEV 目录](#item-14) ⭐️ 7.0/10
15. [保罗·格雷厄姆批评 AI 写的邮件不诚实](#item-15) ⭐️ 7.0/10
16. [Corey Quinn 评 Anthropic 通过教皇通谕游说](#item-16) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [AI 辅助安全报告导致 curl 维护者倦怠](https://simonwillison.net/2026/May/26/the-pressure/#atom-everything) ⭐️ 9.0/10

Daniel Stenberg 报告称，curl 项目面临的 AI 辅助安全报告数量比 2024 年增加了 4-5 倍，每天超过一份报告，导致维护者出现前所未有的倦怠。 这凸显了开源安全面临的关键挑战：AI 工具能够大量生成可信的漏洞报告，使维护者不堪重负，并危及软件供应链的稳定性。 尽管报告激增，curl 仍然稳健；所有近期漏洞的严重性评级均为低或中，最后一个高严重性 CVE 发布于 2023 年 10 月。报告质量非常高且详细。

rss · Simon Willison · May 26, 23:48

**背景**: curl 是一个广泛使用的开源命令行工具和库，用于通过 URL 传输数据，安装在数十亿台设备上。Daniel Stenberg 是主要开发者。AI 辅助安全研究利用大型语言模型自动发现并描述潜在漏洞，提高了报告的数量和质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CURL">cURL - Wikipedia</a></li>
<li><a href="https://curl.se/">curl</a></li>

</ul>
</details>

**标签**: `#open-source`, `#security`, `#AI`, `#curl`, `#maintainer burnout`

---

<a id="item-2"></a>
## [llama.cpp b9330 修复 GPU 性能回退](https://github.com/ggml-org/llama.cpp/releases/tag/b9330) ⭐️ 8.0/10

llama.cpp 版本 b9330 通过将 ffn_latent 张量正确标记为 MUL_MAT（而非 GGML_OP_MUL），修复了 GPU 性能回退，将 Nemotron 3 Super 120B Q5_K_M 的速度从 64.9 恢复至 103.22 tokens/s。 此修复恢复了在 GPU 上运行 Nemotron 等大型模型的用户的重要性能，展示了推理引擎中正确操作符标记的重要性。它也凸显了张量类型声明中的细微错误如何导致吞吐量大幅下降。 问题源于 ffn_latent_down/up 张量在 LLM_TENSOR_INFOS 中被声明为 GGML_OP_MUL，但 Nemotron 模型通过 ggml_mul_mat 处理它们。buft 探测根据声明的操作符查询后端，导致权重被移至 CPU；标记为 MUL_MAT 后修复了探测，使计算保留在 GPU 上。

github · github-actions[bot] · May 26, 02:48

**背景**: llama.cpp 是一个开源 C/C++ 库，用于在多种硬件上本地运行 LLM 推理。它使用 ggml 作为张量计算后端，定义了 MUL_MAT（矩阵乘法）和 GGML_OP_MUL（逐元素乘法）等操作。buft 探测是一种机制，在模型加载期间为每个张量操作确定最佳后端（CPU/GPU）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml-org/ llama . cpp : LLM inference in C/C++ · GitHub</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#performance`, `#GPU`, `#bugfix`, `#machine learning`

---

<a id="item-3"></a>
## [甲基丙烯酸甲酯储罐事故的化学分析](https://www.science.org/content/blog-post/methyl-methacrylate-tank) ⭐️ 8.0/10

一篇关于甲基丙烯酸甲酯储罐事故的详细技术分析已发布，探讨了导致该事件的失控聚合反应化学原理。 该分析为化学工程师和安全专业人员提供了关键见解，有助于防止涉及储罐中反应性单体的类似事故。 该事故涉及甲基丙烯酸甲酯，这是一种单体，如果未适当抑制，可能发生放热聚合反应，从而导致储罐破裂或爆炸。

hackernews · nooks · May 26, 19:25 · [社区讨论](https://news.ycombinator.com/item?id=48284712)

**背景**: 甲基丙烯酸甲酯是用于生产丙烯酸塑料和树脂的关键单体。它需要在抑制剂和温度控制下小心储存，以防止失控聚合反应，该反应会迅速产生热量和压力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://m.blog.naver.com/PostView.naver?blogId=dsjang650628&logNo=220664861418">Handling nitrogen - required safety guides for chemical tankers</a></li>
<li><a href="https://iconprocon.com/blog_post/nitric-acid-safety-and-monitoring-preventing-hidden-hazards-in-chemical-systems/">Nitric Acid Safety and Monitoring: Hazards, H2S Risks, and Sensor...</a></li>
<li><a href="https://himtmarine.com/tanker-safety-courses-important-for-seafarers/">Why Tanker Safety Courses Matter for Seafarers</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了类似事故（苯乙烯、丙烯酸丁酯）的参考资料，并讨论了被动安全系统，一些人指出在此类场景中存在 BLEVE（沸腾液体膨胀蒸气爆炸）的风险。

**标签**: `#chemistry`, `#industrial safety`, `#chemical engineering`, `#hazard analysis`

---

<a id="item-4"></a>
## [维基媒体裁员引发编辑罢工和愤怒](https://medium.com/@jakeorlowitz/wikipedia-is-doing-the-capitalist-thing-56a393232943) ⭐️ 8.0/10

维基媒体基金会解雇了包括一位原始开发者在内的关键 MediaWiki 开发者，并解散了负责维护社区愿望清单的社区技术团队，导致英文维基百科编辑发起罢工。 此举威胁到维基百科志愿者驱动的内容审核和开发的可持续性，因为编辑依赖社区技术团队维护的自定义工具，并引发了对非营利领域反劳工做法的担忧。 裁员包括 MediaWiki 原始开发者之一 Brooke 以及整个社区技术团队，该团队通过社区愿望清单处理功能请求。基金会拥有超过 17 个月的运营储备金，使裁员决定备受争议。

hackernews · cdrnsf · May 26, 20:33 · [社区讨论](https://news.ycombinator.com/item?id=48285592)

**背景**: MediaWiki 是驱动维基百科及其他维基媒体项目的开源软件。社区技术团队负责开发编辑请求的工具，如自动化脚本和界面改进，这些工具对高效编辑至关重要。社区愿望清单是编辑提出并对技术改进进行投票的主要渠道。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mediawiki.org/">MediaWiki</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wikipedia:Community_tech_team">Wikipedia : Community tech team - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论表达了震惊和愤怒，许多人指出一个拥有充足储备的非营利组织裁减核心员工具有讽刺意味。一些编辑描述了没有自定义工具时编辑的困难，而另一些人则争论 17 个月的运营储备是否足够。罢工被视为罕见但必要的抗议。

**标签**: `#Wikipedia`, `#Wikimedia`, `#layoffs`, `#open source`, `#community`

---

<a id="item-5"></a>
## [外包加本地 AI 可能在成本上超越前沿实验室](https://www.signalbloom.ai/posts/outsourcing-plus-localai-will-soon-become-more-economical-vs-frontier-labs/) ⭐️ 8.0/10

一篇博客文章指出，将外包与本地 AI 模型结合，很快将比依赖 OpenAI 或 Anthropic 等前沿实验室更具成本效益。文章强调，订阅制 LLM 定价比 API 定价便宜 10 到 40 倍，使本地 AI 成为可行的替代方案。 这一转变可能重塑 AI 行业，减少对昂贵前沿模型的依赖，使更多公司能够以成本效益高的方式利用 AI。它还预示着未来 AI 将更像托管服务或内部工具，而非黑盒 API。 文章指出，90 美元的 Claude 订阅提供相当于 1000 至 4000 美元的 API 代币价值。它还强调，模型操作者（例如熟练的高级开发人员）的质量对结果有显著影响，类似于管理离岸开发人员。

hackernews · GodelNumbering · May 26, 12:08 · [社区讨论](https://news.ycombinator.com/item?id=48278610)

**背景**: OpenAI 和 Anthropic 等前沿 AI 实验室按 token 收取 API 费用，对于大量使用来说可能很昂贵。订阅计划提供固定价格的无限制使用，对频繁用户更经济。文章将管理 LLM 与管理离岸开发团队进行类比，指出详细的规范是成功的关键。

**社区讨论**: 评论者大多同意文章观点，指出使用 LLM 与管理离岸开发人员惊人地相似——在有明确指导时高效，但无人监督时容易出错。一些人分享轶事，称公司正在用少量美国程序员加 AI 取代离岸团队，并称生产力有所提高。

**标签**: `#AI economics`, `#outsourcing`, `#LLM pricing`, `#software engineering`, `#productivity`

---

<a id="item-6"></a>
## [荷兰阻止美国收购数字身份供应商](https://www.politico.eu/article/netherlands-blocks-us-takeover-vital-digital-supplier/) ⭐️ 8.0/10

荷兰以国家安全和数据隐私为由，阻止了美国对 Solvinity 的收购，该公司托管着国家数字身份系统 DigiD。 这一决定凸显了数据主权和外国控制关键数字基础设施方面日益紧张的局势，为其他国家评估类似风险树立了先例。 Solvinity 托管着 DigiD，荷兰公民使用该系统访问政府服务；荷兰议会此前曾投票决定终止与 Solvinity 的合同，但政府延长了合同，使得阻止收购成为唯一剩下的保障措施。

hackernews · vrganj · May 26, 11:46 · [社区讨论](https://news.ycombinator.com/item?id=48278406)

**背景**: DigiD 是荷兰的集中式数字身份平台，公民用它向税务部门和教育机构等政府机构进行身份验证。该系统处理敏感的个人数据，使其托管提供商成为国家关键基础设施的一部分。当外国实体（尤其是来自隐私法律不同的国家）寻求收购此类提供商时，担忧随之而来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DigiD">DigiD - Wikipedia</a></li>
<li><a href="https://www.digid.nl/en">Home English | DigiD</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍对阻止收购表示赞赏，一位评论者指出，尽管公众广泛要求，政府此前一直保持沉默。另一位强调，架构上的隐私优于政策上的隐私，认为只有供应商在数学上无法访问数据的加密系统才能真正保护用户。一位荷兰公民质疑，为什么不能为 2000 万用户自建一个开源的身份解决方案。

**标签**: `#geopolitics`, `#data sovereignty`, `#critical infrastructure`, `#privacy`, `#Netherlands`

---

<a id="item-7"></a>
## [微软 Copilot Cowork 代理可通过提示注入窃取文件](https://simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/#atom-everything) ⭐️ 8.0/10

微软 Copilot Cowork 代理可通过发送包含外部图片的邮件来窃取文件，这些图片会触发网络请求，利用提示注入泄露预认证的 OneDrive 下载链接。 此漏洞凸显了自主 AI 系统中的一个基本安全挑战，即提示注入可将受信任的代理转变为数据窃取工具，影响数百万 Microsoft 365 用户。 该攻击之所以有效，是因为 Copilot Cowork 可以在未经批准的情况下向用户自己的收件箱发送邮件，而这些邮件可以包含从攻击者控制的服务器加载的外部图片，当用户打开邮件时数据即被泄露。

rss · Simon Willison · May 26, 15:36

**背景**: 提示注入是一种安全漏洞，攻击者通过操纵 AI 模型的输入来覆盖其预期指令。在像 Copilot Cowork 这样能代表用户执行操作的自主系统中，提示注入可能导致未经授权的数据访问或窃取。“致命三重奏”指的是提示注入、自主能力和敏感数据访问权限的组合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection - Wikipedia</a></li>
<li><a href="https://learnprompting.org/docs/prompt_hacking/injection">Prompt Injection : Overriding AI Instructions with User Input</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者对该漏洞的严重性表示担忧，指出它利用了自主系统中的常见模式。一些人认为微软应要求所有对外通信都需用户批准，而另一些人则指出根本原因是缺乏对 AI 代理的适当沙箱隔离。

**标签**: `#security`, `#AI agents`, `#prompt injection`, `#data exfiltration`, `#Microsoft Copilot`

---

<a id="item-8"></a>
## [SGLang v0.5.12.post1 修复 DeepSeek V4 关键错误](https://github.com/sgl-project/sglang/releases/tag/v0.5.12.post1) ⭐️ 7.0/10

SGLang 发布了 v0.5.12.post1，这是一个稳定性补丁，精选了 12 个主要针对 DeepSeek V4 的修复，解决了乱码、崩溃和精度回归等问题。 此补丁对于部署前沿模型 DeepSeek V4 的用户至关重要，它解决了可能导致错误输出或系统崩溃的严重错误，确保了推理的可靠性。 值得注意的修复包括解决 B200/B300 GPU 上的乱码问题、EAGLE/MTP 分离解码期间的崩溃，以及 GSM8K 准确率从 0.825 恢复到 0.960。性能改进消除了 20-40 秒的冷桶延迟。

github · Fridge003 · May 26, 23:58

**背景**: SGLang 是一个高性能的大语言模型服务框架，以低延迟和高吞吐量推理著称。DeepSeek V4 是一个最先进的模型，需要在推理引擎中提供专门支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/sgl-project/sglang">sgl-project/ sglang : SGLang is a high-performance serving framework ...</a></li>
<li><a href="https://docs.sglang.io/">Welcome to SGLang - SGLang Documentation</a></li>

</ul>
</details>

**标签**: `#SGLang`, `#DeepSeek V4`, `#bug fix`, `#release`, `#LLM inference`

---

<a id="item-9"></a>
## [西班牙以缺乏赌博牌照为由封禁 Polymarket 和 Kalshi](https://www.reuters.com/business/spain-blocks-prediction-markets-polymarket-kalshi-over-lack-gambling-licences-2026-05-26/) ⭐️ 7.0/10

西班牙以缺乏法律要求的赌博牌照为由，屏蔽了预测市场平台 Polymarket 和 Kalshi。 这一监管行动凸显了去中心化预测市场与国家赌博法律之间日益紧张的关系，可能为其他国家树立先例。 Polymarket 是基于区块链的预测市场，Kalshi 则是受美国监管的交易所；两者均因未获赌博牌照而在西班牙被屏蔽。

hackernews · thm · May 26, 13:08 · [社区讨论](https://news.ycombinator.com/item?id=48279316)

**背景**: 预测市场允许用户对现实世界事件（如选举或体育赛事）的结果下注。西班牙要求任何提供此类投注的平台必须获得赌博牌照，而 Polymarket 和 Kalshi 均未取得。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prediction_market">Prediction market - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Polymarket">Polymarket - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论一边倒地支持禁令，用户认为预测市场激励现实世界的操纵和危害，将其比作赌场甚至更糟。有人对这类平台向大众做广告表示震惊。

**标签**: `#regulation`, `#prediction markets`, `#gambling`, `#blockchain`, `#ethics`

---

<a id="item-10"></a>
## [Dropbox CEO Drew Houston 卸任](https://www.cnbc.com/2026/05/26/dropbox-ceo-drew-houston-ashraf-alkarmi.html) ⭐️ 7.0/10

Dropbox 首席执行官 Drew Houston 宣布卸任，由 Ashraf Alkarmi 接任新 CEO。 此次领导层变动可能标志着 Dropbox 战略方向的转变，尤其是在公司面临云存储竞争压力并寻求重新聚焦 AI 之际。 Houston 将继续担任董事会主席，Alkarmi 此前担任 Dropbox 首席产品官。此次交接正值社区对产品臃肿和 CPU 性能问题的担忧。

hackernews · aghuang · May 26, 13:18 · [社区讨论](https://news.ycombinator.com/item?id=48279453)

**背景**: Dropbox 是一家成立于 2007 年的云存储和文件同步服务公司。Houston 作为联合创始人自公司成立以来一直担任 CEO，并于 2018 年带领公司上市。如今，Dropbox 面临来自 Google Drive 和 iCloud 等集成平台的激烈竞争，以及文件系统同步相关性下降的挑战。

**社区讨论**: 社区反应不一：一些人尊重 Houston 的领导力和产品愿景，而另一些人则批评过度关注 AI 以及高 CPU 占用等技术问题。还有讨论认为，随着应用转向云原生存储，Dropbox 的相关性正在下降。

**标签**: `#Dropbox`, `#CEO transition`, `#leadership`, `#tech industry`, `#cloud storage`

---

<a id="item-11"></a>
## [对话式聊天机器人让用户沮丧](https://pscanf.com/s/354/) ⭐️ 7.0/10

一篇批判性分析指出，对话式聊天机器人通常不是 AI 工具的正确界面，用户因此感到沮丧，并认为像 Copilot 最初的非对话式设计等替代方案更为有效。 这很重要，因为对话式 AI 正在广泛部署，但用户沮丧可能阻碍采用和生产力，凸显了 AI 界面中更好 UX 设计的必要性。 分析指出，Copilot 最初的设计类似于超级智能版的 Intellisense，广受好评，而当前的聊天机器人模型要求用户编写提示词，增加了摩擦。

hackernews · croes · May 26, 04:39 · [社区讨论](https://news.ycombinator.com/item?id=48275059)

**背景**: 对话式聊天机器人使用大型语言模型（LLM）模拟类人对话。虽然流行，但它们常常导致不可预测的行为，并需要仔细的提示工程，这可能会让期望一致、可靠帮助的用户感到沮丧。

**社区讨论**: 社区评论表达了对对话式界面的沮丧，一位用户指出对模型说脏话有时能改善性能，另一位则指出对话路径常常导致无效率的循环。第三位用户强调不可预测性和压力使 AI 工具变得充满敌意。

**标签**: `#AI`, `#UX`, `#LLM`, `#chatbot`, `#HCI`

---

<a id="item-12"></a>
## [Monkdev：提升 LLM 代码生成的工具包](https://github.com/oeo/monkdev) ⭐️ 7.0/10

Monkdev 是一个新的开源工具包和方法论，通过使用“僧侣”角色和 MCP 工具，强制 LLM 在编写代码前收集大量上下文，从而减少错误决策和代码债务。 这解决了 AI 辅助编码中一个常见痛点——LLM 因上下文不足而做出糟糕决策，通过生成更高质量的代码，可能为开发者节省时间和金钱。 工作流程从在新会话中输入“meditate”开始，它会大量读取项目文件并在继续前确认 token 数量；该工具包针对 Bun 和 Rust 单体仓库项目有特定偏好。

rss · Hacker News Show HN · May 26, 19:08

**背景**: LLM 经常因缺乏完整项目上下文而生成带有逻辑错误或不完整实现的代码。Monkdev 通过角色扮演角色和文件读取工具强制模型先收集上下文，类似于开发者在修改前探索代码库的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://danjcleary.substack.com/p/why-llms-struggle-to-generate-code">Why LLMs Struggle to Generate Code and How You Can Make Them...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#code generation`, `#toolkit`, `#AI-assisted coding`

---

<a id="item-13"></a>
## [Minicor 推出面向 AI 公司的可扩展桌面 RPA](https://www.minicor.com/) ⭐️ 7.0/10

YC P26 初创公司 Minicor 推出一个平台，使 AI 公司能够为没有 API 的 Windows 系统构建可扩展的桌面机器人流程自动化（RPA），该平台使用 MCP，让 Claude Code/Codex 可以导航虚拟机并创建基于 Python 的 RPA 工作流。 这解决了 AI 公司需要集成缺乏 API 的遗留桌面系统时的关键痛点，传统 RPA 通常面临高失败率（30%以上）和调试困难。通过提供脚本编写、编排和调试工具，Minicor 可以显著降低运营开销，实现更可靠的大规模自动化。 该平台使用 MCP（模型上下文协议），让 Claude Code/Codex 可以导航运行桌面软件的虚拟机，并生成 Python 脚本形式的 RPA 工作流，以实现速度、成本和确定性。它包括虚拟机克隆以实现并行化、2FA/OTP 处理、视频回放、日志、版本控制以及人工介入步骤等功能。

rss · Hacker News Launch HN · May 26, 14:57

**背景**: 桌面自动化，也称为有人值守 RPA，用于自动化桌面应用程序上的重复性任务。许多遗留系统缺乏 API，使得自动化变得困难。传统 RPA 工具常因 UI 变化、缺乏可观测性和编排挑战而具有高失败率。Minicor 旨在通过使用 AI（Claude）来编写和调试自动化脚本，并提供用于扩展的基础设施来解决这些问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.uipath.com/blog/rpa/everything-you-need-to-know-about-desktop-automation-software">Everything You Need to Know About Desktop Automation ... | UiPath</a></li>
<li><a href="https://www.nintex.com/learn/rpa/understanding-desktop-automation/">What Is Desktop Automation ? - Nintex</a></li>

</ul>
</details>

**标签**: `#RPA`, `#desktop automation`, `#AI`, `#YC`, `#Windows`

---

<a id="item-14"></a>
## [CISA 将 LiteSpeed cPanel 插件漏洞加入 KEV 目录](https://www.cisa.gov/news-events/alerts/2026/05/26/cisa-adds-one-known-exploited-vulnerability-catalog) ⭐️ 7.0/10

由于存在活跃利用证据，CISA 已将 CVE-2026-48172（LiteSpeed cPanel 插件中的权限提升漏洞）添加到其已知被利用漏洞（KEV）目录中。 此次添加表明该漏洞存在活跃利用且风险重大，尤其对使用广泛部署的 cPanel 插件的联邦系统构成威胁。根据 BOD 22-01，联邦机构必须修复此漏洞，同时 CISA 敦促所有组织优先进行修补。 CVE-2026-48172 是 LiteSpeed cPanel 插件中的一个权限提升漏洞，该插件常用于 Web 托管环境。KEV 目录的纳入要求联邦民事行政分支机构在规定截止日期前完成修复。

rss · CISA Cybersecurity Advisories · May 26, 12:00

**背景**: 已知被利用漏洞（KEV）目录是由 CISA 维护的、包含有活跃利用证据的 CVE 列表。具有约束力的操作指令（BOD）22-01 要求联邦机构在规定时间内修复这些漏洞以降低风险。权限提升漏洞允许攻击者获得更高级别的访问权限，对系统完整性构成严重威胁。

**标签**: `#CISA`, `#vulnerability`, `#cPanel`, `#privilege escalation`, `#security`

---

<a id="item-15"></a>
## [保罗·格雷厄姆批评 AI 写的邮件不诚实](https://simonwillison.net/2026/May/26/paul-graham/#atom-everything) ⭐️ 7.0/10

著名创业投资人保罗·格雷厄姆公开批评创始人使用 AI 写邮件，称 AI 生成的文字让人感觉不诚实，并降低了他对作者的看法。 这凸显了创业社区在专业沟通中使用 AI 的日益紧张关系，其中真实性和个人技能受到高度重视。 格雷厄姆指出，他从未有意识地读完一封由人类署名但由 AI 写的邮件，将其等同于被欺骗。他还表示，使用 AI 写作并不令人印象深刻，因为任何青少年都能做到。

rss · Simon Willison · May 26, 15:02

**背景**: 保罗·格雷厄姆是知名风险投资家、Y Combinator 联合创始人，其观点在创业界具有重要影响力。使用 GPT-4 等大型语言模型进行写作已变得普遍，引发了关于真实性和伦理的讨论。

**标签**: `#AI`, `#writing`, `#ethics`, `#startups`

---

<a id="item-16"></a>
## [Corey Quinn 评 Anthropic 通过教皇通谕游说](https://simonwillison.net/2026/May/26/corey-quinn/#atom-everything) ⭐️ 7.0/10

Corey Quinn 讽刺称，Anthropic 联合创始人 Christopher Olah 影响了教皇利奥十四世关于人工智能伦理的首部通谕《Magnifica Humanitas》，并称这是他见过的最伟大的供应商游说行为。 这凸显了人工智能公司可能如何影响高层伦理框架，将其技术局限性嵌入宗教和政策文件中，从而可能影响全球人工智能治理。 该通谕《Magnifica Humanitas》于 2026 年 5 月 25 日发布，关注在人工智能时代维护人的尊严。Quinn 的推文提到 Anthropic 的具体技术限制被奉为精神论著。

rss · Simon Willison · May 26, 02:28

**背景**: 教皇通谕是教皇就重要教会教义发布的正式信函。《Magnifica Humanitas》是教皇利奥十四世的首部通谕，涉及人工智能伦理。Anthropic 是一家以宪法人工智能方法闻名的 AI 安全公司，其理念可能影响了通谕的框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Magnifica_Humanitas">Magnifica humanitas - Wikipedia</a></li>
<li><a href="https://www.vaticannews.va/en/pope/news/2026-05/pope-leo-xiv-encyclical-magnifica-humanitas-ai.html">Pope Leo’s ‘ Magnifica humanitas ’: AI must serve... - Vatican News</a></li>
<li><a href="https://digg.com/ai/olaxpo3k">Vatican announces Magnifica Humanitas , a papal encyclical arguing...</a></li>

</ul>
</details>

**标签**: `#ai-ethics`, `#anthropic`, `#corey-quinn`, `#ai`, `#technology-policy`

---