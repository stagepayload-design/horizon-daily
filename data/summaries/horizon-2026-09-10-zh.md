# Horizon 每日速递 - 2026-09-10

> From 43 items, 18 important content pieces were selected

---

1. [OpenAI 发布面向企业工作的 GPT-6 Astra](#item-1) ⭐️ 9.0/10
2. [Calif Research 发布 WeWorm：首个通过微信通话传播的零点击蠕虫](#item-2) ⭐️ 9.0/10
3. [OpenAI 的 Astra-next 声称 88 小时内找到纳维-斯托克斯奇点](#item-3) ⭐️ 9.0/10
4. [vLLM v0.29.0 将 Model Runner V2 设为默认，新增 770B MoE 支持](#item-4) ⭐️ 8.0/10
5. [苹果发布折叠屏 iPhone Duo，引发开发者与设计热议](#item-5) ⭐️ 8.0/10
6. [Shopify 收购 Tailwind CSS 背后的公司 Tailwind Labs](#item-6) ⭐️ 8.0/10
7. [Raschka 解析 GPT-6 Astra、循环 Transformer 与隐藏推理](#item-7) ⭐️ 8.0/10
8. [Gist 分析 Qwen 3.8 的推理预填是否跟随 GPT-5.5 Pro](#item-8) ⭐️ 8.0/10
9. [研究者揭示恶意软件如何绕过谷歌广告审核](#item-9) ⭐️ 8.0/10
10. [Cisco FMC 身份验证绕过漏洞可致未授权 root 访问](#item-10) ⭐️ 8.0/10
11. [IEEE Spectrum：越来越多证据表明自动驾驶汽车能挽救生命](#item-11) ⭐️ 7.0/10
12. [苹果发布 Apple Watch Series 12，新增健康传感与音频笔记功能](#item-12) ⭐️ 7.0/10
13. [Desert Ant Labs 推出端侧 AI 模型，提供免费额度](#item-13) ⭐️ 7.0/10
14. [GNU Radio 通过 WebAssembly 移植到浏览器](#item-14) ⭐️ 7.0/10
15. [Read the Docs 发布近期 DDoS 攻击复盘报告](#item-15) ⭐️ 7.0/10
16. [Planet Labs 开放卫星数据源：一份实用的工程实践指南](#item-16) ⭐️ 7.0/10
17. [Anthropic 研究所描绘 AI 经济未来，引发激烈争论](#item-17) ⭐️ 7.0/10
18. [CISA 将四个已被积极利用的漏洞加入 KEV 目录](#item-18) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI 发布面向企业工作的 GPT-6 Astra](https://openai.com/index/gpt-6-astra-next-generation-work) ⭐️ 9.0/10

OpenAI 发布了 GPT-6 Astra，称其是面向企业的最强模型，具备高级推理、计算机操作以及更强的写作和设计判断能力。该模型被定位为面向工作的下一代智能，API 模型 ID 为 gpt-6-astra，且没有 gpt-6 别名。 这是 OpenAI 的旗舰级发布，将 AI 进一步推向端到端编程、研究和代理式计算机操作等企业工作流。它将影响正在评估 AI 平台的企业，并可能加剧与 Anthropic 等对手在计算机操作和推理领域的竞争。 独立评测指出，Astra 在 ARC-AGI-3 上 99.9% 的亮眼成绩与标准测试框架下的 62.7% 存在巨大差距，综合智能指数没有提升。该模型面向困难的端到端编程、计算机操作、研究和代理工作，并通过 API 以 gpt-6-astra 的 ID 提供。

rss · OpenAI Blog · Sep 9, 11:00

**背景**: 大语言模型是在海量文本数据上训练、能够生成和推理语言的 AI 系统；思维链提示等高级推理技术让它们能处理多步骤问题。计算机操作指 AI 能像人一样操作软件界面，这一能力由 Anthropic 的 Claude 率先推动，如今已成为企业自动化的核心。OpenAI 的 GPT 系列是其旗舰模型线，每一代新模型通常都会提升企业和开发者应用的标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ofox.ai/zh/blog/gpt-6-astra-review-2026/">GPT - 6 Astra 测评：37 分的裂口，和你看不见的那部分思考</a></li>
<li><a href="https://evolink.ai/blog/gpt-6-astra-api-guide">How to Use GPT - 6 Astra API: Setup, Effort & Migration</a></li>
<li><a href="https://openai.robocurve.org/gpt-6-astra/">GPT - 6 Astra on robot arms | Robocurve</a></li>

</ul>
</details>

**社区讨论**: 早期评测持怀疑态度，指出 Astra 在 ARC-AGI-3 上的头条成绩与标准测试框架结果之间存在 37 分的差距，并指出综合智能指数没有提升。一些观察者还指出，Astra 在某些实体拼图任务上会卡住，而竞争模型却能成功。

**标签**: `#OpenAI`, `#GPT-6`, `#AI`, `#LLM`, `#Enterprise AI`

---

<a id="item-2"></a>
## [Calif Research 发布 WeWorm：首个通过微信通话传播的零点击蠕虫](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research 发布了 WeWorm 的演示，称这是首个通过微信通话在 iOS 和 Android 上传播的零点击蠕虫。该团队表示，借助 AI 协助，他们在约两天内找到了漏洞并编写出首个远程代码执行（RCE）利用程序，随后又用一周时间构建出蠕虫。 这标志着 AI 辅助漏洞发现与利用开发的一次范式转变，表明小团队如今能在数天内而非数月内构建出大规模移动蠕虫。这对移动安全、微信庞大的用户群体以及围绕攻击能力的 AI 安全讨论都有重大影响。 受害者无需接听电话或对手机进行任何操作；即使接听，也听不到任何声音，利用仍然成功。据 Calif 称，底层漏洞是微信 VoIP 协议栈中的内存破坏问题，团队强调人类负责判断目标与安全测试，而 AI 完成了大部分工作。

rss · Simon Willison · Sep 10, 00:56

**背景**: 零点击漏洞利用无需用户任何操作即可入侵设备，因此比需要点击或下载的攻击危险得多。蠕虫是一种通过自动感染新设备或账号进行自我复制的恶意软件，而远程代码执行（RCE）意味着攻击者可在目标上运行任意代码。微信是中国极受欢迎的即时通讯与通话应用，因此通过其通话功能传播的蠕虫可能迅速波及大量用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.1950.ai/post/wechat-zero-click-worm-how-ai-turned-a-voip-vulnerability-into-a-self-spreading-account-hijacking-t">WeChat Zero-Click Worm: How AI Turned a VoIP Vulnerability Into...</a></li>
<li><a href="https://iplogger.org/blog/researchers-build-wechat-zero-click-worm-hijacking-phones-via-calls/">WeChat Zero-Click Worm: AI-Powered Call Hijacks Threaten Android...</a></li>
<li><a href="https://www.itsecuritynews.info/one-wechat-call-was-enough-to-hijack-accounts-across-iphone-and-android/">One WeChat Call Was Enough to Hijack Accounts... - IT Security News</a></li>

</ul>
</details>

**标签**: `#ai-security`, `#mobile-security`, `#zero-click-exploit`, `#wechat`, `#vulnerability-research`

---

<a id="item-3"></a>
## [OpenAI 的 Astra-next 声称 88 小时内找到纳维-斯托克斯奇点](https://www.latent.space/p/ainews-openai-reports-navier-stokes) ⭐️ 9.0/10

据报道，OpenAI 使用了一个名为 Astra-next 的大规模多智能体系统，包含约 10,000 个智能体、消耗 1300 亿个 token、成本超过 4000 万美元，在短短 88 小时内找到了纳维-斯托克斯方程的一个奇点。如果得到验证，这将成为史上第二个被授予的千禧年大奖的有力竞争者。 如果属实，这代表着人工智能与数学两个领域的范式转变，表明大规模多智能体系统能够攻克困扰人类数学家一个多世纪的难题。这也将证明巨额算力和 token 投入是通往真正科学发现的可行路径，可能重塑科研的资助与开展方式。 该声明基于约 10,000 个智能体和 1300 亿个 token，成本超过 4000 万美元，但来源内容简短，缺乏技术细节或独立验证。纳维-斯托克斯方程解的存在性与光滑性是七个千禧年大奖难题之一，每个难题由克莱数学研究所提供 100 万美元奖金。

rss · Latent Space · Sep 9, 05:04

**背景**: 千禧年大奖难题是数学领域最著名的七个未解问题，由位于马萨诸塞州剑桥市的克莱数学研究所设立，每道题的正确解答可获得 100 万美元奖金。纳维-斯托克斯方程解的存在性与光滑性问题，是问描述流体运动的方程的解是否始终保持光滑，还是会产生奇点，它被视为数学物理中最深奥的未解问题之一。迄今为止，千禧年大奖只颁发过一次，授予了因庞加莱猜想而获奖的格里戈里·佩雷尔曼，但他拒绝了该奖项。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Millennium_Prize_Problems">Millennium Prize Problems - Wikipedia</a></li>
<li><a href="https://www.claymath.org/millennium-problems/">The Millennium Prize Problems - Clay Mathematics Institute</a></li>
<li><a href="https://openai.com/index/gpt-6-astra-next-generation-work/">GPT-6 Astra : The next generation in intelligence for work | OpenAI</a></li>

</ul>
</details>

**标签**: `#AI`, `#mathematics`, `#Navier-Stokes`, `#multi-agent systems`, `#OpenAI`

---

<a id="item-4"></a>
## [vLLM v0.29.0 将 Model Runner V2 设为默认，新增 770B MoE 支持](https://github.com/vllm-project/vllm/releases/tag/v0.29.0) ⭐️ 8.0/10

vLLM 发布了 v0.29.0，包含来自 277 位贡献者的 594 次提交，在从池化模型开始的推广完成后，正式将 Model Runner V2（MRV2）设为所有模型的默认执行核心。该版本还新增了对腾讯 770B/49B 激活参数的 Hy4-preview MoE、Qwen3.8-Flash-Next、Kimi K3 NVFP4 检查点的支持，并带来了批量分片采样和 CUDA 图内存分析等大量性能优化。 将 MRV2 设为所有模型的默认执行核心，是 vLLM 这一最广泛使用的开源 LLM 推理引擎的重要架构里程碑，直接影响所有运行生产级 LLM 服务基础设施的用户。对新大型模型的支持以及将 logits 内存降低至 1/TP、内核加速 6.6-7.6 倍等优化，意味着服务前沿规模模型时成本更低、吞吐更高。 MRV2 新增了用于 KV 缓存自动调优的 CUDA 图内存分析、将每步 logits 内存降低 1/TP 的批量分片采样、提示嵌入（prompt embeds），以及用于投机解码下统一解码的填充式 FULL cudagraph 调度。MRV1 仍在少数 ROCm 模型和 MRV2 尚不支持的功能中使用；破坏性变更包括移除十个已弃用的模型架构，以及弃用 `python -m vllm.entrypoints.openai.api_server` 而推荐使用 `vllm serve`。

github · khluu · Sep 9, 08:54

**背景**: vLLM 是一个广受欢迎的开源大语言模型高效服务引擎，采用 PagedAttention 和连续批处理等技术。Model Runner V2 是对 vLLM 模型执行核心的从零重写，旨在更模块化、更快速且不改变 API，此前需要通过 VLLM_USE_V2_MODEL_RUNNER 环境变量手动启用。新的 Hy4-preview 模型使用了门控 DeepSeek 稀疏注意力（DSA），这是一种稀疏注意力机制，由索引器挑选少量较早的 token 参与昂贵的注意力计算。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vllm-website-m20r6h0mr-inferact-inc.vercel.app/blog/mrv2">Model Runner V 2 : A Modular and Faster Core for vLLM | vLLM Blog</a></li>
<li><a href="https://aiwiki.ai/wiki/hy4_preview">Hy4 Preview | AI Wiki</a></li>

</ul>
</details>

**标签**: `#vllm`, `#llm-inference`, `#model-serving`, `#release`, `#performance-optimization`

---

<a id="item-5"></a>
## [苹果发布折叠屏 iPhone Duo，引发开发者与设计热议](https://www.apple.com/iphone-duo/) ⭐️ 8.0/10

苹果正式发布了其首款折叠屏 iPhone——iPhone Duo，采用无折痕的书本式设计，并配备类似 iPad 的界面，支持并排多任务应用。该消息引发了社区的巨大反响，超过 1600 条评论讨论了其设计、对开发者的影响以及苹果不断演变的战略。 这标志着苹果正式进入折叠屏手机市场，可能给三星、谷歌等安卓折叠屏厂商带来压力，同时推动开发者创建能更好利用大尺寸柔性屏幕的自适应应用。这也暗示了苹果在新领导层下产品战略的转变，对整个移动生态系统具有深远影响。 据传 iPhone Duo 将配备 2400 万像素屏下摄像头，并可能取消一项关键安全功能，但细节尚未确认。预计该产品将于 2026 年 9 月左右上市，售价高达 2100 至 2500 美元，且苹果据称正利用 iPhone Air 作为折叠屏工程的试验田。

hackernews · thecosmicfrog · Sep 9, 18:15 · [社区讨论](https://news.ycombinator.com/item?id=49630931)

**背景**: 折叠屏手机已存在多年，主要来自三星和谷歌等安卓厂商，但通常存在明显折痕和应用优化不佳的问题。苹果的加入意义重大，因为其庞大的用户群和开发者生态可能最终推动主流应用开发者正确支持折叠屏形态。iPhone Duo 类似 iPad 的界面表明苹果正利用其现有的平板软件，以打造跨设备尺寸的无缝体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2p0eDl6ekR4RWZxVHo3NHNYSGRDZ0FQAQ?hl=en-IN&gl=IN&ceid=IN:en">Google News - Foldable iPhone may have a 24-megapixel...</a></li>
<li><a href="https://tech.yahoo.com/phones/articles/iphone-air-reveals-apple-foldable-191925364.html">How iPhone Air Reveals Apple ’s Foldable Phone Strategy</a></li>
<li><a href="https://www.linkedin.com/news/story/apples-foldable-iphone-to-feature-ipad-like-interface-7744545/">Apple's foldable iPhone to feature iPad-like interface | LinkedIn</a></li>

</ul>
</details>

**社区讨论**: 社区情绪褒贬不一：一些人称赞 Duo 的无折痕设计以及 John Ternus 领导下主题演讲的新鲜氛围，而另一些人则持怀疑态度，将折叠屏比作荷马的车——既是更差的手机也是更差的平板。安卓折叠屏用户则感到兴奋，认为苹果的加入将迫使开发者为折叠屏设计合适的应用，一些年长用户则将其视为迈向单一全能设备的一步。

**标签**: `#Apple`, `#iPhone`, `#foldable phones`, `#hardware`, `#mobile development`

---

<a id="item-6"></a>
## [Shopify 收购 Tailwind CSS 背后的公司 Tailwind Labs](https://tailwindcss.com/blog/tailwind-is-joining-shopify) ⭐️ 8.0/10

Shopify 已收购 Tailwind CSS 这一流行开源实用优先 CSS 框架背后的公司 Tailwind Labs，该消息在 Tailwind 官方博客上公布。此前 Tailwind Labs 的文档流量自 2023 年初以来下降约 40%，并因 AI 对其业务的冲击裁掉了约 75% 的工程团队。 这笔收购凸显了 AI 正在如何颠覆开发者工具公司的商业模式，即便是拥有广泛使用的开源项目和强大品牌的公司也难以幸免。它也引发了关于“开源加商业”模式可持续性的疑问，以及 Shopify 的所有权对 Tailwind 未来方向和社区意味着什么。 Tailwind Labs 是一家规模很小、支持远程办公的公司，员工仅数人，其主要商业产品一直以 UI 模板和文档为中心，而非大规模托管服务。社区成员指出，Shopify 很可能是在收购其人才和品牌，而在 AI 时代销售 UI 模板可能是一条死路，即便对 Tailwind 这样强大的品牌也是如此。

hackernews · EdwinHoksberg · Sep 9, 13:27 · [社区讨论](https://news.ycombinator.com/item?id=49626190)

**背景**: Tailwind CSS 是一个开源的实用优先 CSS 框架，开发者可以直接在 HTML 中组合细粒度的工具类来为网站设置样式，而不必像 Bootstrap 那样依赖预定义的组件类。其背后的公司 Tailwind Labs 围绕该框架，通过文档、UI 模板和相关工具建立了商业模式。近年来，大语言模型在生成代码方面越来越强大，这减少了开发者查阅文档和购买预制 UI 资源的需求，给靠开发者工具变现的公司带来了压力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tailwind_CSS">Tailwind CSS - Wikipedia</a></li>
<li><a href="https://github.com/tailwindlabs/tailwindcss">GitHub - tailwindlabs/tailwindcss: A utility-first CSS framework for rapid...</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为这笔收购是 AI 侵蚀 Tailwind Labs 商业模式的后果，有人指出其 75% 的工程团队已被裁撤，文档流量下降了 40%。也有人争论在原生 CSS 和 AI 辅助编码不断进步的情况下，新建网站是否还需要 Tailwind；同时许多人对该框架表示感谢，并希望团队获得了良好的回报。

**标签**: `#Tailwind CSS`, `#Shopify`, `#acquisition`, `#open source`, `#AI impact`

---

<a id="item-7"></a>
## [Raschka 解析 GPT-6 Astra、循环 Transformer 与隐藏推理](https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and) ⭐️ 8.0/10

Sebastian Raschka 发表了一篇技术深度分析文章，探讨了 GPT-6 Astra、循环（循环深度）Transformer 以及隐藏推理等概念，并在 Hacker News 上引发了 336 分、118 条评论的热烈讨论。文章澄清了《The Information》所报道的“循环深度”技术本质上等同于堆叠更多 Transformer 层，只是通过复用权重来节省 GPU 显存，而非某种全新的秘密方法。 该分析有助于澄清 GPT-6 Astra 使用某种“秘密技术”从而使思维链监控变得更困难的说法，说明循环 Transformer 是一种已有研究基础的已知架构方法。这很重要，因为理解隐藏推理对于 AI 安全、可解释性以及评估模型思考过程对用户和审计者可见程度至关重要。 社区成员指出，将整个 Transformer 模型循环作用于自身，按定义就属于隐藏推理，因为中间推理轨迹被反馈回模型而非直接输出，不过理论上仍有可能同时提取该轨迹和最终的输出轨迹。讨论中还引用了 Will Merrill 关于思维链和通用 Transformer 的研究，以及一篇关于哪些计算问题至少需要多少思维链才能解决的博客文章。

hackernews · ModelForge · Sep 9, 14:37 · [社区讨论](https://news.ycombinator.com/item?id=49627370)

**背景**: 循环 Transformer（也称为通用 Transformer 或循环深度模型）在多次迭代中复用相同的 Transformer 权重，从而在不增加参数量或显存占用的情况下有效增加网络深度。隐藏推理指的是模型在激活空间中内部完成重要计算，却不将其在思维链中表达出来的情况，这会使监控和可解释性变得更加困难。GPT-6 Astra 是 OpenAI 最新的前沿模型，据报道在 ARC-AGI-3 上得分 99.9%，在 FrontierMath Tier 4 上得分 98%，不过部分评测显示不同测试框架下结果差异巨大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.lesswrong.com/posts/ZrgFfeWuckpwK5Lyi/hidden-reasoning-in-llms-a-taxonomy">Hidden Reasoning in LLMs : A Taxonomy — LessWrong</a></li>
<li><a href="https://en.ain.ua/2026/09/04/openai-released-gpt-6-astra/">GPT - 6 Astra from OpenAI. What can the new AI model do?</a></li>
<li><a href="https://ofox.ai/zh/blog/gpt-6-astra-review-2026/">GPT - 6 Astra 测评：37 分的裂口，和你看不见的那部分思考</a></li>

</ul>
</details>

**社区讨论**: 评论者总体上认同 Raschka 的澄清，有人指出循环 Transformer 只是通过权重复用来节省显存，而像通用 Transformer 这样的早期工作已被遗忘。其他人则争论循环 Transformer 是否按定义就构成隐藏推理，分享了关于思维链需求的研究参考，并对 MSPAINT 计算机使用演示等案例表示惊叹，同时有用户惋惜 Astra 的行为似乎在周中发生了变化。

**标签**: `#LLM`, `#transformers`, `#GPT-6`, `#hidden reasoning`, `#AI research`

---

<a id="item-8"></a>
## [Gist 分析 Qwen 3.8 的推理预填是否跟随 GPT-5.5 Pro](https://gist.github.com/wsxiaoys/e0286dc6bb624ff5fdf49e7f4c528ba3) ⭐️ 8.0/10

wsxiaoys 发布的一份 GitHub gist 分析了 Qwen 3.8 的推理预填是否跟随 GPT-5.5 Pro，利用已知漏洞从闭源模型中恢复思维链。该分析引发了关于模型蒸馏和基准污染的争论。 这项分析提出了重要问题：像 Qwen 这样的开源模型是否在蒸馏 GPT-5.5 Pro 等闭源模型的专有推理轨迹，这可能对 AI 伦理、许可和基准完整性产生重大影响。它还凸显了公开推理轨迹作为蒸馏证据的可靠性问题。 该方法包括使用最先进的模型运行基准测试，恢复其思维链，然后将该思维链的前 1% 输入开源模型，观察其是否以类似风格继续。该漏洞在 stolen-thoughts.com 的论文中描述，允许从 OpenAI 和 Anthropic 模型中恢复可读的思维链。

hackernews · wsxiaoys · Sep 9, 17:24 · [社区讨论](https://news.ycombinator.com/item?id=49630026)

**背景**: 思维链（CoT）提示是一种通过让大语言模型展示中间步骤来激发其推理能力的技术。模型蒸馏将知识从大模型转移到小模型，通常通过用大模型的输出训练小模型来实现。'stolen thoughts' 漏洞从闭源模型中恢复隐藏的推理轨迹，从而能够分析潜在的蒸馏行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2201.11903">[2201.11903] Chain - of - Thought Prompting Elicits Reasoning in Large...</a></li>

</ul>
</details>

**社区讨论**: 评论者争论 Qwen 和 GPT 推理之间的重叠是由于蒸馏还是仅仅因为训练在相同的基准解决方案上。一些人质疑使用公开推理轨迹作为证据的可靠性，而另一些人指出 Qwen 3.8 是在 stolen-thoughts 论文发布后训练的，因此可能见过那些轨迹。

**标签**: `#AI/ML`, `#model distillation`, `#reasoning traces`, `#Qwen`, `#GPT`

---

<a id="item-9"></a>
## [研究者揭示恶意软件如何绕过谷歌广告审核](https://xlii.space/eng/malicious-software-on-google-ads/) ⭐️ 8.0/10

一名安全研究者在其博客 xlii.space 上发布了一篇详细的技术文章，演示了恶意软件如何通过谷歌广告进行投放，并指出谷歌自动化广告审核流程中的漏洞。该文章在 Hacker News 上获得 354 分和 213 条评论，作者随后表示，只有在问题经论坛曝光后，其账号才被恢复。 该事件凸显了大型平台的自动化内容审核机制可能被利用来向普通用户传播恶意软件，引发了对平台责任和广告审核体系有效性的质疑。它也反映出一种更广泛的趋势：企业越来越依赖自动化系统，导致用户在决策出错时几乎无从申诉。 文章逐步描述了让恶意广告通过审核的方法，暗示谷歌的审核流程高度依赖自动化检查，而缺乏持续的人工监督。作者指出，其账号只有在事件被 Hacker News 放大传播后才被恢复，说明问题解决依赖舆论压力而非正常的申诉渠道。

hackernews · xlii · Sep 9, 11:43 · [社区讨论](https://news.ycombinator.com/item?id=49624856)

**背景**: 谷歌广告（Google Ads）是谷歌的广告平台，允许企业在谷歌搜索、YouTube 及其他渠道投放广告；所有新建或修改的广告在上线前都应经过审核。谷歌的广告政策明确禁止恶意软件和滥用广告网络的行为，但执行主要依赖自动化系统与有限的人工审核相结合。长期以来，恶意行为者一直试图利用广告验证环节的漏洞，向用户投放危险链接或恶意软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.google.com/adspolicy/answer/15939580?hl=en">Malicious Software - Advertising Policies Help</a></li>
<li><a href="https://b2b-cyber-security.de/en/measures-against-malicious-advertising-software/">Measures against malicious advertising software - B2B Cyber Security</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为，谷歌的自动化系统已成为一堵让用户申诉无门的墙，有人指出大语言模型时代加剧了这一问题，而问题本身早已存在。其他人则提到 YouTube 上的诈骗广告和 AdSense 上的恐吓软件，认为谷歌的执法不一致或漠不关心；作者也确认，其账号是在 Hacker News 讨论之后才被恢复的。

**标签**: `#security`, `#advertising`, `#malware`, `#google`, `#platform-accountability`

---

<a id="item-10"></a>
## [Cisco FMC 身份验证绕过漏洞可致未授权 root 访问](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Cisco%20Secure%20Firewall%20Management%20Center%20Software%20Authentication%20Bypass%20Vulnerability%26vs_k=1) ⭐️ 8.0/10

Cisco 披露了 Cisco Secure Firewall Management Center（FMC）软件 Web 界面中的一个严重身份验证绕过漏洞（CVE-2026-20079），该漏洞源于系统启动时创建的不当系统进程。未经身份验证的远程攻击者可通过发送特制 HTTP 请求执行脚本并获得底层操作系统的 root 访问权限；Cisco 已发布软件更新，且没有可用的临时缓解措施。 这是一个严重级别的漏洞，允许未经身份验证的攻击者完全攻陷防火墙管理平面，可能危及整个受管防火墙集群和企业网络。运行本地部署 FMC 且管理界面暴露于互联网的组织必须立即修补，该漏洞属于 Cisco 2026 年 3 月半年度捆绑安全公告的一部分。 该漏洞源于系统启动时创建的不当系统进程，可通过向 FMC Web 界面发送特制 HTTP 请求加以利用。Cisco 指出，如果 FMC 管理界面没有公共互联网访问，攻击面会有所减小，但不存在临时缓解措施，打补丁是唯一的修复方式。

rss · Cisco Security Advisories · Sep 9, 16:00

**背景**: Cisco Secure Firewall Management Center（FMC）是 Cisco Secure Firewall 设备（包括 ASA 和 Firepower Threat Defense（FTD）设备）的集中管理平台，负责策略配置、事件监控和设备管理。身份验证绕过漏洞使攻击者能够完全跳过登录过程并访问受保护的功能，在本例中还可提升至底层操作系统的 root 权限。由于 FMC 掌控整个防火墙集群的安全策略，管理平面被攻陷可能对企业网络产生连锁影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sysin.org/blog/cisco-fmc-10/">Cisco Secure Firewall Management Center Virtual... - sysin</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#cisco`, `#authentication bypass`, `#firewall`

---

<a id="item-11"></a>
## [IEEE Spectrum：越来越多证据表明自动驾驶汽车能挽救生命](https://spectrum.ieee.org/are-self-driving-cars-safe) ⭐️ 7.0/10

IEEE Spectrum 发表了一篇题为《Are Self Driving Cars Safe as Early Data Suggests?》的文章，认为越来越多的证据表明自动驾驶汽车能够挽救生命，该文在 Hacker News 上引发了细致的讨论，焦点在于如何解读背后的安全数据。评论者就死亡数据的偏斜、比较基准等统计细节，以及自主性与安全之间的社会权衡展开了辩论。 自动驾驶汽车的安全问题具有重大的社会和技术影响，因为用于证明其部署合理性的数据可能影响监管、保险市场和公众接受度。讨论表明，仅有有利数据还不够——在自动驾驶汽车被广泛强制推行之前，还需要社会认同和谨慎的比较基准。 评论者指出，Waymo 将其事故率与普通司机而非其实际取代的网约车司机进行比较，而网约车司机涉及的严重事故更少，因此在更公平的基准下这些数字看起来就没那么亮眼。其他人则指出，死亡数据受到多种因素的严重偏斜，例如未系安全带（44%）、超速（29%）、酒精相关（约 30%），以及行人和骑行者等弱势道路使用者（约占死亡人数的 20%）。

hackernews · bookofjoe · Sep 9, 17:14 · [社区讨论](https://news.ycombinator.com/item?id=49629886)

**背景**: 自动驾驶汽车（也称自主汽车或机器人汽车）是能够以较少或无需人工输入方式运行的车辆，而 robotaxi 则是由网约车公司运营的自动驾驶汽车。领先的自动驾驶公司常常以累计行驶里程作为成熟度的标志，但通过道路测试来证明安全性仍是一个统计难题，因为罕见的致命事件需要海量数据才能可靠衡量。IEEE Spectrum 是 IEEE 的旗舰出版物，IEEE 是工程与技术领域的主要专业组织。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://spectrum.ieee.org/are-self-driving-cars-safe">Are Self Driving Cars Safe as Early Data Suggests? - IEEE Spectrum</a></li>
<li><a href="https://en.wikipedia.org/wiki/Self-driving_car">Self-driving car - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/pulse/can-we-prove-autonomous-vehicle-safety-through-road-testing-suho-chu-re3hc">Can We Prove Autonomous Vehicle Safety Through Road Testing...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论内容丰富且观点多样：一些评论者认为，更好的驾驶教育、更高的考试标准或禁酒也能挽救生命，但同样面临缺乏社会认同的问题；另一些人则批评“安全崇拜”被用来为限制出行自由辩护。一个反复出现的主题是，投入自动驾驶汽车的资源或许更适合用于公共交通；还有一位评论者预测，自动驾驶汽车保险更便宜，最终可能使人类驾驶成为一种奢侈。

**标签**: `#autonomous vehicles`, `#safety`, `#transportation`, `#public policy`, `#statistics`

---

<a id="item-12"></a>
## [苹果发布 Apple Watch Series 12，新增健康传感与音频笔记功能](https://www.apple.com/newsroom/2026/09/introducing-apple-watch-series-12-with-the-all-new-health-sensing-system/) ⭐️ 7.0/10

苹果于 2026 年 9 月发布了 Apple Watch Series 12，搭载全新的健康传感系统和 S11 芯片，可实现更高频率的心率与心率变异性（HRV）测量，并由此支持全新的“准备度评分”功能。该手表还新增了音频笔记功能，这一功能成为 Hacker News 上激烈争论的焦点。 此次发布表明苹果继续将健康监测作为可穿戴设备的核心差异化卖点，但升级的渐进性引发了关于智能手表品类是否已进入“边际收益递减”阶段的讨论。而始终在线的音频功能则引发了更广泛的隐私与知情同意问题，可能影响用户和监管机构对可穿戴设备的看法。 Series 12 可每五分钟测量一次 HRV，苹果称这能在夜间指标显现之前就发现健康变化，同时步数统计也更加准确。值得注意的是，音频笔记功能仅限最新款手表使用，但其外观设计与前代完全相同，因此旁人无法分辨哪位佩戴者正在录音。

hackernews · Lealen · Sep 9, 17:56 · [社区讨论](https://news.ycombinator.com/item?id=49630566)

**背景**: Apple Watch 是苹果的智能手表产品线，集健身追踪、健康监测和通知功能于一体。心率变异性（HRV）衡量的是心跳间隔时间的变化，常被用作恢复状态和压力的指标。S11 芯片是 Series 12 内部的处理器，而“准备度评分”是一项新指标，根据健康数据总结用户适合进行活动的程度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2026/09/introducing-apple-watch-series-12-with-the-all-new-health-sensing-system/">Introducing Apple Watch Series 12 , with the all-new Health Sensing ...</a></li>
<li><a href="https://www.apple.com/apple-watch-series-12/">Apple Watch Series 12 - Apple</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论者意见严重分歧：许多人批评始终在线的录音功能存在隐私和知情同意风险，指出外观设计未变导致无法知道谁在监听；另一些人则认为该手表已进入边际收益递减阶段，并称赞 Garmin 等替代品在续航上的优势。还有人抱怨苹果在最新系统更新中放弃了对 Series 6 至 8 以及初代 Ultra 的支持，认为这既浪费又不环保。

**标签**: `#apple-watch`, `#wearables`, `#privacy`, `#health-tech`, `#product-launch`

---

<a id="item-13"></a>
## [Desert Ant Labs 推出端侧 AI 模型，提供免费额度](https://desertant.com/blog/introducing-desert-ant-labs/) ⭐️ 7.0/10

Desert Ant Labs 于 9 月 8 日正式上线，推出 18 个覆盖音频、视觉和文本的端侧 AI 模型，每月最多 10 万台活跃设备可免费使用，无需 token 或登录。这些模型以 Swift、Kotlin 和 JavaScript SDK 形式提供，权重托管在 Hugging Face 上，其中名为 Voz 的转录模型号称比 Whisper 快 4.7 倍。 这标志着不断壮大的本地 AI 生态又迈出重要一步，在手机、平板和笔记本上直接运行模型有望消除按次调用的云端成本并保护数据隐私。同时，它也引发了关于端侧软件商业模式应如何运作的讨论，与成熟的云端大模型计费方式形成对比。 这些 SDK 基于 Core ML 构建，面向 iOS 和 macOS，采用 async/await API，且每个模型在各平台上行为一致，便于一次开发、多端部署。值得注意的是，目前尚无 Python SDK，一些开发者认为这是一个短板。

hackernews · willwhitedc · Sep 9, 11:39 · [社区讨论](https://news.ycombinator.com/item?id=49624823)

**背景**: 端侧 AI 指的是在用户本地硬件上运行机器学习模型，而不是把请求发送到云端服务器，这样可以降低延迟、避免按次计费，并让敏感数据不出设备。小型专用模型之所以越来越可行，是因为现代手机和笔记本普遍搭载了专用神经处理芯片，而它们一天中大部分时间处于闲置状态。Desert Ant Labs 进入的领域已有 llama.cpp、MLC LLM 和 Ollama 等工具，但它通过统一 SDK 提供一套精选的专用模型来形成差异化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://byteiota.com/desert-ant-labs-ships-18-on-device-ai-models-free/">Desert Ant Labs Ships 18 On - Device AI Models Free | byteiota</a></li>
<li><a href="https://desertant.com/swift/">On - device AI Models for iOS and macOS | Desert Ant Labs</a></li>
<li><a href="https://github.com/Desert-Ant-Labs/desert-ant-core/">GitHub - Desert - Ant - Labs / desert - ant -core: On - device AI SDKs for...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者总体上欢迎这一概念，多人称赞小型专用模型以及本地推理相比按次云端调用在经济上的优势。担忧主要集中在商业模式不清晰、缺少 Python SDK，以及认为发布文案像是大模型生成的；还有一位评论者指出，Voz 转录模型似乎只是 Parakeet v3 加上新的 macOS/iOS 专用推理代码。

**标签**: `#on-device AI`, `#local LLMs`, `#edge computing`, `#AI business models`, `#mobile development`

---

<a id="item-14"></a>
## [GNU Radio 通过 WebAssembly 移植到浏览器](https://gnuradioworld.com/) ⭐️ 7.0/10

一个通过 WebAssembly 编译、可在浏览器中运行的 GNU Radio 移植版本在 Hacker News 上亮相，获得了 166 分和 23 条评论。该演示让用户无需安装本地软件，就能直接在网页中运行 GNU Radio 的信号处理流图。 在浏览器中运行 GNU Radio 降低了软件定义无线电和数字信号处理实验的门槛，用户可以即时尝试流图而无需安装本地工具链。这也表明 WebAssembly 正成为此前仅限于桌面应用的重型实时信号处理工作负载的可行目标平台。 该移植更像是一次技术展示而非成熟产品：评论者指出演示页面的描述文字难以阅读，而且似乎没有音频输出，说明它本意是处理来自真实无线电的信号，而不是作为独立的入门教程。相关的 WebAssembly SDR 项目也已存在，包括通过 WebUSB 连接 USRP B200 的射频扫描器、AX.25 解码器和 FM 接收机。

hackernews · kristianpaul · Sep 9, 15:53 · [社区讨论](https://news.ycombinator.com/item?id=49628576)

**背景**: GNU Radio 是一个历史悠久的开源工具包，用于构建软件定义无线电和数字信号处理系统，传统上作为本地桌面应用运行。WebAssembly（WASM）是一种可移植的二进制指令格式，能让用 C 或 C++ 等语言编写的代码以接近原生的速度在浏览器中运行。软件定义无线电用软件取代专用硬件电路，使通用计算机加上射频前端就能接收并解码多种无线电信号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@coders.stop/webassembly-web-workers-the-boring-combo-thats-actually-solving-the-ui-freeze-problem-nobody-79bb9999d915">WebAssembly + Web Workers: The Boring Combo... | Medium</a></li>
<li><a href="https://www.sdr-radio.com/download">Download - SDR - Radio .com - Software Defined Radio</a></li>

</ul>
</details>

**社区讨论**: 整体情绪偏正面，评论者称该项目“超级酷”，并将其与 MaxMSP 相提并论。不过也有几位用户批评演示的入门引导：有人表示“完全不知道自己在看什么”，认为描述文字难以阅读；还有人回忆在 RTL-SDR 早期觉得 GNU Radio 晦涩难用。一位评论者还分享了自己基于 WebUSB+WASM 的 USRP B200 射频扫描器、AX.25 解码器和 FM 接收机项目，成为讨论中的亮点。

**标签**: `#gnuradio`, `#software-defined-radio`, `#webassembly`, `#dsp`, `#signal-processing`

---

<a id="item-15"></a>
## [Read the Docs 发布近期 DDoS 攻击复盘报告](https://about.readthedocs.com/blog/2026/09/2026-ddos-attack/) ⭐️ 7.0/10

Read the Docs 发布了一份详细的复盘报告，披露其文档托管服务近期遭遇的一次 DDoS 攻击，并描述了攻击者如何不断调整流量以绕过 Cloudflare 的防御。该文章在 Hacker News 上引发讨论，获得 151 分和 51 条评论，话题涉及 Cloudflare 在七层防护上的局限、可能的法律追责途径，以及此次攻击可能由 AI 驱动的猜测。 Read the Docs 是开源项目广泛使用的文档托管平台，一旦服务中断会影响成千上万的开发者及其用户。此次事件凸显了一个更广泛的担忧：Cloudflare 的七层防御在面对自适应、AI 辅助的僵尸网络时可能力不从心，这或将改变基础设施团队对 DDoS 防护的思考方式。 复盘报告指出，此次攻击具有高度自适应性；社区成员也观察到，Cloudflare 在缓解四层流量型攻击方面通常强于七层应用层攻击。评论者还质疑，鉴于攻击者会不断调整行为，启用 Cloudflare 的“Under Attack”模式是否真能奏效。

hackernews · davidfischer · Sep 9, 15:55 · [社区讨论](https://news.ycombinator.com/item?id=49628614)

**背景**: DDoS（分布式拒绝服务）攻击通过来自大量来源的流量淹没服务，使其无法正常访问。四层攻击针对 TCP/UDP 等传输层协议，依靠巨大流量取胜；七层攻击则针对 HTTP 等应用层请求，更难与正常用户区分。Cloudflare 是广泛使用的内容分发网络和 DDoS 缓解服务商，在其全球边缘节点提供 L3 至 L7 的集成防护。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cloudflare.com/learning/ddos/how-to-prevent-ddos-attacks/">How to prevent DDoS attacks | Methods and tools</a></li>
<li><a href="https://www.a10networks.com/blog/the-machine-war-has-begun-cybercriminals-leveraging-ai-in-ddos-attacks/">AI DDoS Attacks : How Cybercriminals Use AI | A10 Networks</a></li>
<li><a href="https://antibot24.com/blog/protecting-against-l7-ddos-attack">Protecting Against L 7 DDoS Attacks: When a Bot Poses as a Human...</a></li>

</ul>
</details>

**社区讨论**: 评论者就 Cloudflare 的“Under Attack”模式能否缓解这种自适应攻击展开争论，有人认为 Cloudflare 擅长防御四层攻击，但在七层 DDoS 上表现不佳。还有人猜测此次攻击可能由 AI 驱动，或是某个 AI 实验室的测试；一位评论者则呼吁采取更强硬的法律手段，包括起诉那些被攻陷设备形成僵尸网络的制造商。

**标签**: `#security`, `#ddos`, `#cloudflare`, `#infrastructure`, `#post-mortem`

---

<a id="item-16"></a>
## [Planet Labs 开放卫星数据源：一份实用的工程实践指南](https://tech.marksblogg.com/planet-labs-open-satellite-feed.html) ⭐️ 7.0/10

Mark Litwintschik 发布了一篇详细的技术博客，讲解如何访问和使用 Planet Labs 的开放卫星影像数据源，包括其开放的 S3 存储桶。文章还引发了社区讨论，涉及非营利组织定价、相关工具以及卫星命名等话题。 Planet Labs 运营着全球最大的商业卫星星座之一，每天对地球所有陆地进行成像，因此将其部分数据开放获取，降低了研究人员、开发者和环保组织的使用门槛。该文章可复现的工程方法也为处理大规模地理空间数据提供了范例。 该数据源通过开放的 S3 存储桶提供，博客强调实用且可复现的影像拉取与处理流程。社区成员指出，Planet 的定价对非营利组织仍是障碍，一个环保组织称其仅针对一小段海岸线的报价就高达每年约 3 万美元。

hackernews · marklit · Sep 9, 15:44 · [社区讨论](https://news.ycombinator.com/item?id=49628429)

**背景**: Planet Labs 是一家成立 15 年的旧金山公司，负责制造和运营卫星星座，历史上曾运营过四个不同的星座。它每天对全球陆地进行成像，数据被用于森林砍伐监测、农业和灾害响应等场景。此类开放数据源让开发者无需支付商业授权费用即可试用真实卫星影像。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://linkrena.com/tools/planet-labs-open-satellite-feed">Planet Labs ' Open Satellite Feed - Benchmarks & Tips for Big Data ...</a></li>
<li><a href="https://www.planet.com/">Planet Labs : Satellite Imagery & Earth Data Analytics</a></li>
<li><a href="https://gisgeography.com/free-satellite-imagery-data-list/">15 Free Satellite Imagery Data Sources - GIS Geography</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该文章是软件工程的典范，有人称它回答了“软件工程长什么样”。一位环保非营利组织的联合创始人指出了开放数据与可负担高分辨率影像之间的差距，其他人则提到了 Mapterhorn 的 PMTiles 等相关项目，并质疑大部分卫星是否服务于 Flock 监控公司。

**标签**: `#satellite-imagery`, `#geospatial`, `#data-engineering`, `#open-data`, `#Planet Labs`

---

<a id="item-17"></a>
## [Anthropic 研究所描绘 AI 经济未来，引发激烈争论](https://www.anthropic.com/institute/econ-scenarios) ⭐️ 7.0/10

Anthropic 研究所发布了一份分析报告，探讨由 AI 塑造的多种可能经济未来，该内容登上 Hacker News 首页，获得 7.0 分和约 325 条评论。报告勾勒了从 AI 驱动生产力提升到 LLM 几乎不产生经济影响等多种情景，引发了社区的批判性讨论。 作为领先的 AI 实验室之一，Anthropic 对 AI 经济影响的论述可能影响政策制定者、企业和公众对劳动力替代、不平等和算力市场的看法。Hacker News 上的质疑反应表明，乐观的生产力叙事远未得到普遍认同。 这些情景据称忽略了更黑暗的结果，如教育受损、社会信任侵蚀和阶级冲突，并假设生产力提升会转化为更多面对患者的时间，而非裁员。评论者还指出，算力价格可能大幅下降，且许多数据中心是由可能在赢家通吃市场中无法生存的公司建造的。

hackernews · oumua_don17 · Sep 9, 13:38 · [社区讨论](https://news.ycombinator.com/item?id=49626373)

**背景**: Anthropic 是一家以 Claude 系列大语言模型闻名的 AI 安全公司，其研究所发布关于 AI 社会影响的研究。这场争论反映了业界更广泛的讨论：AI 究竟会增强还是取代劳动者，以及算力——训练和运行 AI 所需的处理能力——将如何定价和分配。Hacker News 是技术人员常去的热门论坛，因此其反应可以反映专家社区的舆论风向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gentic.news/article/compute-shortage-to-split-ai">Compute Shortage to Split AI Market : Rich… | gentic.news</a></li>
<li><a href="https://www.linkedin.com/posts/onechronos_the-currency-of-the-ai-age-activity-7493364163403042816-lfEa">OneChronos CEO on Building AI Compute Markets with... | LinkedIn</a></li>

</ul>
</details>

**社区讨论**: 评论者大多持批评态度，认为这些情景在经济上过于天真，因为成本驱动的系统会用 AI 来裁员，而不是给员工更多时间。其他人表示，最不乐观的情景应包括教育受损、注意力持续时间缩短、信任侵蚀和不平等加剧等真实危害，还有人认为这篇文章不过是软件公司炮制的投机性未来学。

**标签**: `#AI economics`, `#future of work`, `#Anthropic`, `#labor displacement`, `#technology policy`

---

<a id="item-18"></a>
## [CISA 将四个已被积极利用的漏洞加入 KEV 目录](https://www.cisa.gov/news-events/alerts/2026/09/09/cisa-adds-four-known-exploited-vulnerabilities-catalog) ⭐️ 7.0/10

2026 年 9 月 9 日，CISA 基于已被积极利用的证据，将四个漏洞加入其已知被利用漏洞（KEV）目录：CVE-2025-25249（Fortinet 堆缓冲区溢出）、CVE-2026-19490（Citrix NetScaler 身份验证绕过）、CVE-2026-87491（Google Chromium V8 越界写入）以及 CVE-2026-20079（Cisco Firewall Management Center 身份验证绕过）。 这些漏洞影响 Fortinet、Citrix 和 Cisco 广泛部署的企业产品，以及 Chrome 和许多其他浏览器所使用的 Chromium V8 引擎，因此对攻击者具有很高的利用价值。根据约束性操作指令（BOD）26-04，美国联邦文职机构必须快速修复公开暴露资产上列入 KEV 的漏洞，CISA 也敦促所有组织采用同样的基于风险的优先级排序。 这四个 CVE 涵盖两个身份验证绕过漏洞（Citrix NetScaler 和 Cisco Firewall Management Center）、Fortinet 多产品中的堆缓冲区溢出，以及 Google Chromium V8 中的越界写入。BOD 26-04 要求各机构优先修复公开暴露资产上、利用后可获得完全控制权的 KEV 漏洞，并检查系统在打补丁前是否已被入侵；KEV 提名需要提供 CVE 编号、利用证据和明确的缓解指南。

rss · CISA Cybersecurity Advisories · Sep 9, 12:00

**背景**: KEV 目录是 CISA 维护的权威列表，收录已在真实环境中被利用的漏洞，供防御者优先安排修补。堆缓冲区溢出是指程序向堆分配的缓冲区写入超出其容量的数据，可能导致代码执行；而利用替代路径或通道的身份验证绕过则允许攻击者无需有效凭据即可访问受保护资源。Chromium 的 V8 是 Chrome 及许多其他浏览器使用的 JavaScript 引擎，因此其中的缺陷可能影响非常庞大的用户群体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog">cisa .gov/ known - exploited - vulnerabilities - catalog</a></li>
<li><a href="https://community.opentextcybersecurity.com/vulnerability-vault-228/alert-cisa-adds-seven-known-exploited-vulnerabilities-to-catalog-release-date-september-02-2026-365548">Alert CISA Adds Seven Known Exploited Vulnerabilities to Catalog ...</a></li>
<li><a href="https://cyberexperts.com/2026-09-03-cisa-adds-three-known-exploited-vulnerabilities-to-catalog/">CISA Adds Three Known Exploited Vulnerabilities to Catalog</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerabilities`, `#CISA`, `#KEV`, `#exploitation`

---

