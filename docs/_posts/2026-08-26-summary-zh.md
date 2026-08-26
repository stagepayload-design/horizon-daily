---
layout: default
title: "Horizon Summary: 2026-08-26 (ZH)"
date: 2026-08-26
lang: zh
---

> From 37 items, 18 important content pieces were selected

---

1. [苹果发布 M6 和 M5 Ultra 芯片](#item-1) ⭐️ 9.0/10
2. [OpenAI Jalapeño 芯片在测试中超越 Nvidia Blackwell](#item-2) ⭐️ 9.0/10
3. [llama.cpp v0.3.0 新增多模态、MTP、张量拆分](#item-3) ⭐️ 8.0/10
4. [FDA 批准首款可穿戴双功能血糖酮体监测仪](#item-4) ⭐️ 8.0/10
5. [Nitter 收到停止函后关闭所有实例](#item-5) ⭐️ 8.0/10
6. [Firefox 157 将在所有平台默认启用 JPEG XL](#item-6) ⭐️ 8.0/10
7. [SpaceX 宣布投资 1000 亿美元的 Starbase Louisiana 发射场](#item-7) ⭐️ 8.0/10
8. [Kaltura HTML5 播放器存在未修补的严重 RCE 和文件读取漏洞](#item-8) ⭐️ 8.0/10
9. [EVE Online 启动期待已久的 Python 3 迁移](#item-9) ⭐️ 8.0/10
10. [Open WebUI v0.11.1 新增人工审批工具调用功能](#item-10) ⭐️ 7.0/10
11. [Python 预声明常量的怪癖与历史奇闻](#item-11) ⭐️ 7.0/10
12. [LatticeDB：受 SQLite 启发的嵌入式图数据库](#item-12) ⭐️ 7.0/10
13. [关于创业文化的个人随笔在 Hacker News 上引发共鸣](#item-13) ⭐️ 7.0/10
14. [工具提示需要延迟，并在鼠标移向时跳过延迟](#item-14) ⭐️ 7.0/10
15. [CISA 将正在被利用的 Gitea 远程代码执行漏洞加入 KEV 目录](#item-15) ⭐️ 7.0/10
16. [HTML 标签名字符允许执行 JavaScript](#item-16) ⭐️ 7.0/10
17. [OpenAI 首席财务官阐释智能丰裕背后的全栈](#item-17) ⭐️ 7.0/10
18. [吴恩达转向 AI 工程领域](#item-18) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [苹果发布 M6 和 M5 Ultra 芯片](https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/) ⭐️ 9.0/10

苹果于 2026 年 8 月 25 日发布了 M6 和 M5 Ultra 芯片。M6 是苹果首款 2nm 处理器，首次搭载于新款 Mac mini；M5 Ultra 则驱动新款 Mac Studio，是苹果迄今最强大的芯片。 这标志着苹果芯片系列在性能和 AI 计算方面的重大飞跃，可能重塑高端台式机和笔记本电脑市场。2nm 技术的引入以及对 AI 能力的关注，可能影响整个行业未来的芯片发展。 M6 采用 12 核 CPU，由台积电以 2nm 工艺制造。M5 Ultra 在 Mac Studio 配置中最高支持 512GB 内存和 16TB 存储，顶配机型售价为 24,699 美元。

hackernews · interpol_p · Aug 25, 13:01 · [社区讨论](https://news.ycombinator.com/item?id=49433292)

**背景**: 苹果的 M 系列芯片是基于 ARM 的片上系统（SoC），自 2020 年起取代英特尔处理器，为 Mac 提供动力。M6 和 M5 Ultra 延续了这一系列，其中 M6 是首款 2nm 芯片，提供更好的性能和能效。M5 Ultra 定位为苹果产品线中最强大的芯片，面向专业用户和 AI 工作负载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_M6">Apple M 6 - Wikipedia</a></li>
<li><a href="https://9to5mac.com/2026/08/25/apple-launches-next-gen-apple-silicon-chips-m6-and-m5-ultra/">Apple launches next-gen Apple Silicon chips : M 6 and... - 9to5Mac</a></li>

</ul>
</details>

**社区讨论**: 社区评论反映出对性能提升的兴奋，一些用户注意到速度上的明显差异。还有关于定价的讨论，一位用户计算了高端配置的成本，并猜测苹果可能会跳过 M6 Pro/Max/Ultra 版本，专注于面向 AI 的 M7 芯片。

**标签**: `#Apple`, `#hardware`, `#AI`, `#chips`, `#M6`

---

<a id="item-2"></a>
## [OpenAI Jalapeño 芯片在测试中超越 Nvidia Blackwell](https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia) ⭐️ 9.0/10

OpenAI 与博通合作，于 2026 年 6 月 24 日发布了其首款定制 AI 推理芯片“Jalapeño”。早期基准测试（包括 SemiAnalysis 在 Hot Chips 2026 上的 InferenceX 测试）显示，它在每千瓦时令牌数上优于 Nvidia Blackwell，推理成本预计下降约 50%。 这标志着 AI 硬件格局可能发生转变，因为一家主要 AI 实验室转向定制芯片以降低成本并提高效率。如果成功，它可能挑战 Nvidia 的主导地位，并推动更多 AI 公司进行垂直整合。 该芯片采用台积电 3nm 工艺，专为基于 Transformer 的 LLM 推理设计。据社区分析，其性能与 Nvidia Blackwell 和 Google TPU 相当，芯片尺寸与 Nvidia Rubin 相近，但 NVFP4 PFLOPs 仅为后者的三分之一。预计 2026 年底在 Azure 上大规模部署。

hackernews · bmulholland · Aug 25, 14:06 · [社区讨论](https://news.ycombinator.com/item?id=49434378)

**背景**: AI 推理芯片是专为运行训练后模型而优化的处理器，比通用 GPU 具有更高效率。OpenAI 此举顺应了谷歌（TPU）和亚马逊（Trainium）等科技巨头开发定制芯片以降低 AI 工作负载成本并提高性能的趋势。该芯片架构针对当前 Transformer 注意力模式定制，可能限制其对未来模型变化的适应性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.spheron.network/blog/openai-jalapeno-chip-gpu-cloud-inference-2026/">OpenAI Jalapeño Chip Explained: What... | Spheron Blog</a></li>
<li><a href="https://vncmac.com/en/blog/2026-openai-jalapeno-chip-broadcom-inference-nvidia-2026.html">OpenAI Jalapeño Chip : 50% Cheaper Inference | VNCMac</a></li>
<li><a href="https://locsic.com/thinking/openai-jalapeno-deep-analysis/">Inside Jalapeño : What Happens When an AI Company… — Locsic</a></li>
<li><a href="https://gentic.news/article/openai-jalapeno-chip-beats-nvidia">OpenAI Jalapeño Chip Beats Nvidia Blackwell … | gentic.news</a></li>
<li><a href="https://andrew.ooo/answers/openai-custom-silicon-vs-google-tpu-vs-amazon-trainium-june-2026/">OpenAI Jalapeño vs Google TPU vs Amazon Trainium... — andrew.ooo</a></li>
<li><a href="https://macdate.com/en/blog/openai-jalapeno-inference-chip-50-cheaper-20260625.html">OpenAI Jalapeño Chip : 50% Cheaper Inference, Challenging Nvidia</a></li>

</ul>
</details>

**社区讨论**: 社区评论对推理芯片的潜力表示兴奋，将新兴市场比作早期 GPU 时代。一些人讨论效率指标，指出人类仍比当前芯片高效 22 倍，并争论芯片尺寸与性能的权衡。还有人幽默地指出 FP4 精度的讽刺性以及 SemiAnalysis 分析师非常规的背景。

**标签**: `#AI hardware`, `#OpenAI`, `#Nvidia`, `#custom chips`, `#inference`

---

<a id="item-3"></a>
## [llama.cpp v0.3.0 新增多模态、MTP、张量拆分](https://github.com/ggml-org/llama.cpp/releases/tag/v0.3.0) ⭐️ 8.0/10

llama.cpp v0.3.0 引入了带新型 DSA-ISWA KV 缓存的多模态模型 dots3-note，为 GLM-4.5-Air 增加了 MTP 支持，并为 DeepSeek 4 增加了张量拆分模式。同时将 ggml 升级到 v0.22.0，带来性能增强。 此版本显著扩展了 llama.cpp 的功能，支持本地推理先进的多模态模型，并提升了 DeepSeek 4 等新模型的性能。它通过为广泛使用的开源工具提供前沿特性，惠及 AI/ML 社区。 该版本包含针对 dots3-note 的新型 DSA-ISWA KV 缓存类型、对 GLM-4.5-Air 的 MTP 支持，以及通过 -sm tensor 为 DeepSeek 4 提供的张量拆分。ggml v0.22.0 带来了元后端张量拆分、带并行编译的逐操作 Metal 内核，以及非原地 ggml_clamp。

github · github-actions[bot] · Aug 25, 10:22

**背景**: llama.cpp 是一个流行的开源项目，用于在消费级硬件上本地运行大型语言模型。MTP（多令牌预测）允许每次前向传播生成多个令牌，从而加速推理。张量拆分将模型层分布到多个 GPU 上，以处理大型模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://korshunov.ai/en/article/20686-llama-cpp-0-3-0-adds-dots3-note-model-and-tensor-split-for-deepseek-4/">llama.cpp 0.3.0 adds dots3-note model and tensor-split for DeepSeek 4</a></li>
<li><a href="https://sourceforge.net/projects/llama-cpp.mirror/files/v0.3.0/">llama.cpp - Browse /v0.3.0 at SourceForge.net</a></li>
<li><a href="https://specpicks.com/reviews/llama-cpp-mtp-regression-kv-cache-quant-2026">MTP in llama . cpp : The Regression, the Fix | SpecPicks</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#AI/ML`, `#release`, `#multimodal`, `#ggml`

---

<a id="item-4"></a>
## [FDA 批准首款可穿戴双功能血糖酮体监测仪](https://www.fda.gov/news-events/press-announcements/fda-authorizes-first-wearable-device-continuously-monitors-both-ketone-levels-and-blood-sugar) ⭐️ 8.0/10

美国食品药品监督管理局（FDA）已批准 Libre Duo 10 天连续双功能葡萄糖酮体监测系统，这是首款可同时连续监测酮体和血糖水平的可穿戴设备。该设备被批准用于 2 岁及以上糖尿病患者。 这一批准标志着糖尿病护理领域的重大监管里程碑，通过提供葡萄糖和酮体的实时数据，可能改善疾病管理。它有助于预防糖尿病酮症酸中毒（DKA），并加强日常糖尿病管理，尤其对 1 型糖尿病患者。 该设备由雅培糖尿病护理公司开发，是一款 10 天可穿戴系统，集成了连续葡萄糖监测（CGM）和酮体监测功能。它被批准用于 2 岁及以上人群，FDA 公告强调其可能减少单独监测设备的负担。

hackernews · sunnynagra · Aug 25, 19:07 · [社区讨论](https://news.ycombinator.com/item?id=49439017)

**背景**: 连续葡萄糖监测仪（CGM）被糖尿病患者广泛用于实时追踪血糖水平，而酮体监测通常通过尿液或血液测试进行，尤其是在生病或血糖偏高时。糖尿病酮症酸中毒（DKA）是一种严重并发症，当酮体积累时可能发生，频繁监测酮体有助于预防。Libre Duo 将这两种功能整合到一个可穿戴传感器中，简化了患者的监测流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fda.gov/news-events/press-announcements/fda-authorizes-first-wearable-device-continuously-monitors-both-ketone-levels-and-blood-sugar">FDA Authorizes First Wearable Device That Continuously Monitors ...</a></li>
<li><a href="https://www.pharmacytimes.com/view/fda-clears-first-continuous-glucose-ketone-monitor">FDA Clears First Continuous Glucose - Ketone Monitor</a></li>
<li><a href="https://www.patientcareonline.com/view/fda-authorizes-first-wearable-device-to-continuously-monitor-glucose-ketones">FDA Authorizes First Wearable Device to Continuously Monitor ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了个人情感、技术怀疑和澄清的混合观点。一位用户分享了一位朋友因 DKA 去世的个人故事，并对这一进展表示感激。另一位用户对无创血糖传感仍持怀疑态度，但欢迎为糖尿病管理增加的工具。第三位用户质疑“可穿戴”一词，指出它似乎像 CGM 一样插入手臂，而另一位评论说酮体监测对普通糖尿病患者的实用性有限。

**标签**: `#FDA`, `#wearable`, `#diabetes`, `#healthtech`, `#medical devices`

---

<a id="item-5"></a>
## [Nitter 收到停止函后关闭所有实例](https://github.com/zedeus/nitter/issues/1442) ⭐️ 8.0/10

广受欢迎、注重隐私的 Twitter 替代前端 Nitter 收到了停止函，导致所有实例被关闭，等待法律建议。 这一事件凸显了依赖抓取或使用大型平台 API 的开源项目在法律上的脆弱性。它可能会阻碍类似项目的发展，并影响依赖隐私保护方式访问社交媒体的用户。 Nitter 项目收到了停止函，所有实例在可预见的未来都将保持关闭。目前尚未披露具体的发函方和法律依据。

hackernews · Banditoz · Aug 25, 17:08 · [社区讨论](https://news.ycombinator.com/item?id=49437283)

**背景**: Nitter 是一个免费开源、注重隐私和性能的 Twitter 替代前端，允许用户在没有 JavaScript 或跟踪的情况下浏览推文。停止函是一种正式要求停止涉嫌非法活动的文件，通常威胁如果不遵守将提起诉讼。它不是法院命令，而是潜在法律行动的前兆。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nitter">Nitter - Wikipedia</a></li>
<li><a href="https://www.investopedia.com/terms/c/cease-and-desist.asp">investopedia.com/terms/c/ cease - and - desist .asp</a></li>

</ul>
</details>

**社区讨论**: 社区成员表达了失望和沮丧，一些人指出组织仍依赖 Twitter 进行沟通，使 Nitter 变得必不可少。其他人讨论了为此类项目提供法律保护的必要性，并批评美国公司的法律施压。一些人还将 Nitter 的情况与其他获得支持而非法律威胁的社区项目进行了比较。

**标签**: `#Nitter`, `#cease and desist`, `#open source`, `#privacy`, `#legal`

---

<a id="item-6"></a>
## [Firefox 157 将在所有平台默认启用 JPEG XL](https://groups.google.com/a/mozilla.org/g/dev-platform/c/3YMV4MS34KA?pli=1) ⭐️ 8.0/10

Firefox 157 将在所有平台默认启用 JPEG XL，这标志着下一代图像格式的一个重要里程碑。这一变化紧随浏览器此前对该格式的支持，并与 Chromium 的类似举措保持一致。 此举显著推动了 JPEG XL 的采用，因为 Firefox 是一个拥有大量用户的主要浏览器。这给其他浏览器和平台带来了支持该格式的压力，可能促进行业更广泛的采用和网络图像压缩的改进。 Firefox 和 Chromium 都使用基于 Rust 的 jxl-rs 库来支持 JPEG XL，而 Apple 在其平台中已提供 libjxl（C++）。社区对这两个库的基准比较以及 Apple 是否会在其平台中采用 Rust 感到好奇。

hackernews · yboris · Aug 25, 17:55 · [社区讨论](https://news.ycombinator.com/item?id=49437946)

**背景**: JPEG XL 是一种下一代图像格式，旨在压缩效率和画质上超越 PNG、JPEG 和 WebP 等现有格式。它支持渐进式解码，即使数据部分加载也能快速显示图像。该格式已开发多年，浏览器支持正在逐步增加。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jpegxl.info/index.html">JPEG XL : Superior Image Compression</a></li>
<li><a href="https://www.loc.gov/preservation/digital/formats/fdd/fdd000536.shtml">JPEG XL Image Encoding</a></li>
<li><a href="https://cloudinary.com/blog/how_jpeg_xl_compares_to_other_image_codecs">How JPEG XL Compares to Other Image Codecs</a></li>

</ul>
</details>

**社区讨论**: 社区评论对 JPEG XL 的潜力表示兴奋，一位用户希望在几年内完全摆脱 JPEG。其他人则讨论技术方面，如 Rust 实现和跨浏览器支持，并指出 Chromium 也默认启用 JPEG XL。

**标签**: `#JPEG XL`, `#Firefox`, `#image format`, `#browser`, `#Rust`

---

<a id="item-7"></a>
## [SpaceX 宣布投资 1000 亿美元的 Starbase Louisiana 发射场](https://www.spacex.com/sites/starbase-la) ⭐️ 8.0/10

SpaceX 正式宣布在路易斯安那州沿海建设新的发射场和星舰工厂 Starbase Louisiana，计划投资高达 1000 亿美元，并创造 3000 个就业岗位。该消息由 Gwynne Shotwell 和州长 Jeff Landry 在路易斯安那州阿布维尔宣布。 这标志着 SpaceX 发射基础设施的重大扩张，可能实现更频繁的发射和进入太阳同步轨道，这对地球观测卫星很有价值。该项目预计将为美国最贫困地区之一带来显著经济发展，类似于 Starbase Texas 的影响。 该设施将位于 125,000 英亩的沿海沼泽地上，投资是 SpaceX 复制并扩大其 Starbase Texas 运营的一部分。该地点的位置为太阳同步轨道发射提供了优势，需要相对于赤道约 98 度的向南发射角度。

hackernews · bilsbie · Aug 25, 16:37 · [社区讨论](https://news.ycombinator.com/item?id=49436822)

**背景**: SpaceX 一直在德克萨斯州博卡奇卡的 Starbase Texas 开发星舰发射系统，该地已成为测试和发射巨型火箭的中心。新的路易斯安那州站点旨在支持更大规模的生产和发射操作，可能缓解德克萨斯州站点的拥堵。太阳同步轨道常用于地球观测卫星，因为它们能提供一致的照明条件，使路易斯安那州的位置具有战略价值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://political.org/2026/08/25/spacex-plans-100-billion-spaceport-in-louisiana/">SpaceX Announces $100 Billion Starbase Louisiana Spaceport in...</a></li>
<li><a href="https://arstechnica.com/space/2026/08/spacex-intends-to-invest-up-to-100-billion-in-massive-louisiana-spaceport/">SpaceX intends to invest up to $100 billion in massive Louisiana ...</a></li>
<li><a href="https://www.nytimes.com/2026/08/25/technology/spacex-louisiana-spaceport.html">SpaceX to Spend $100 Billion on Spaceport in Louisiana</a></li>

</ul>
</details>

**社区讨论**: 社区评论总体积极，用户强调了对当地技工的经济利益以及雄心勃勃项目的兴奋感。一些用户指出了该地点的轨道优势，而另一些用户则指出网页文案重复，可能由 LLM 生成。少数评论对马斯克的时间表表示怀疑。

**标签**: `#SpaceX`, `#space exploration`, `#Louisiana`, `#launch site`, `#economic impact`

---

<a id="item-8"></a>
## [Kaltura HTML5 播放器存在未修补的严重 RCE 和文件读取漏洞](https://kb.cert.org/vuls/id/308749) ⭐️ 8.0/10

CERT/CC 披露了 Kaltura HTML5 播放器库（mwEmbed/html5lib）中的两个严重漏洞，CVE-2026-19913 和 CVE-2026-19912，均源于 mwEmbedLoader.php 端点中的不安全反序列化。这些漏洞允许未经身份验证的远程攻击者读取任意文件并执行任意代码，目前尚无供应商补丁。 Kaltura 是一个广泛使用的 AI 视频平台，这些漏洞影响个人安装和多租户 CDN 基础设施，可能暴露敏感数据并导致服务器完全受损。由于无需身份验证且尚无补丁，这对所有受影响的部署构成严重风险。 CVE-2026-19913 利用 ServiceUrl 参数中的 file://路径通过错误消息读取本地文件，而 CVE-2026-19912 利用 uiconf_id 参数中的目录遍历将恶意序列化对象写入 Web 可访问目录，实现 RCE。仅使用 memcache 后端可能缓解 RCE 路径，但无法修复根本的反序列化和路径清理问题。

rss · CERT CC Vulnerability Notes · Aug 25, 16:11

**背景**: 不安全反序列化是指未经验证地反序列化不可信数据，攻击者可操纵序列化对象以引发意外行为。在 PHP 中，如果用户输入未经过滤，unserialize()函数可能被利用来执行任意代码或读取文件。Kaltura HTML5 播放器库中的 mwEmbedLoader.php 端点接受用户控制的 ServiceUrl 参数，并在未经验证的情况下获取和反序列化，从而导致这些漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kb.cert.org/vuls/id/308749">VU#308749 - Remote Code Execution and Arbitrary File Read ...</a></li>
<li><a href="https://dbugs.ptsecurity.com/vulnerability/PT-2026-81395">CVE-2026-19913 — Kaltura Kaltura Html5 Player | dbugs</a></li>
<li><a href="https://securityonline.info/kaltura-server-flaws/">Unpatched Kaltura Server Flaws Enable Code Execution</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#Kaltura`, `#RCE`, `#deserialization`

---

<a id="item-9"></a>
## [EVE Online 启动期待已久的 Python 3 迁移](https://simonwillison.net/2026/Aug/25/eve-online-move-to-python-3/) ⭐️ 8.0/10

EVE Online 宣布开始从 Stackless Python 2.7 迁移到 Python 3，使用 futurize 脚本处理 240 万行代码，并手动审查约 20,000 处行为差异。 此次迁移意义重大，因为 EVE Online 是生产环境中规模最大、运行时间最长的 Python 代码库之一，其成功过渡将为其他仍需迁移的大型 Python 2 项目提供宝贵经验。 迁移将首先使用 futurize 脚本，然后手动审查约 20,000 处 Python 2 和 3 行为差异，例如整数除法。公告未说明如何替换 Stackless，但去年他们在新游戏 EVE Frontier 中展示了使用 carbonengine/scheduler 库的解决方案。

rss · Simon Willison · Aug 25, 22:59

**背景**: EVE Online 自 2003 年上线以来一直运行在 Stackless Python 上，最近一次重大升级是在 2010 年升级到 Stackless Python 2.7。Stackless Python 是 CPython 的一个变体，提供微线程以支持并发。Python 2 已于 2020 年停止维护，因此迁移到 Python 3 对于持续支持和安全至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://python-future.org/futurize.html">futurize : Py2 to Py2/3 — Python-Future documentation</a></li>
<li><a href="https://www.cnblogs.com/lao454490095/p/4397261.html">stackless python 初体验 - ScutLaozk - 博客园</a></li>
<li><a href="https://python.plainenglish.io/main-differences-between-python-2-x-python-3-x-c574cc14be9d">Main Differences Between Python 2 anPython 3 | by Sara Cemal</a></li>

</ul>
</details>

**标签**: `#Python`, `#EVE Online`, `#Migration`, `#Stackless`, `#Software Engineering`

---

<a id="item-10"></a>
## [Open WebUI v0.11.1 新增人工审批工具调用功能](https://github.com/open-webui/open-webui/releases/tag/v0.11.1) ⭐️ 7.0/10

Open WebUI v0.11.1 引入了人工审批工具调用的功能，允许用户在对话中手动批准或拒绝工具调用。它还新增了一个内置工具，让模型可以向用户提出多项选择题，并重构了流式传输，仅发送增量文本更新。 此次更新增强了 AI 交互中的安全性和用户控制，这对于 AI 代理日益自主执行操作至关重要。它回应了人们对意外工具使用的日益关注，并为开源平台中负责任的 AI 部署树立了先例。 审批功能是可选的，可由管理员启用；用户可以在每个对话中切换自由运行和审批模式，并且选择会被记住。流式传输重构通过仅发送新增文本片段而非每次发送整个消息，减少了数据传输和服务器负载。

github · github-actions[bot] · Aug 25, 21:17

**背景**: Open WebUI 是一个流行的开源界面，用于与大型语言模型交互，支持工具调用和多用户环境等功能。人在回路（HITL）是一种设计模式，让人类参与 AI 系统的决策过程，通常用于批准或否决操作。此次发布符合行业向更安全的 AI 代理行为发展的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.openwebui.com/features/extensibility/plugin/tools/">Tools / Open WebUI</a></li>
<li><a href="https://open-webui.com/tools/">Tools - Open WebUI</a></li>

</ul>
</details>

**标签**: `#open-webui`, `#AI`, `#human-in-the-loop`, `#release`, `#tools`

---

<a id="item-11"></a>
## [Python 预声明常量的怪癖与历史奇闻](https://sebsite.pw/w/20260801-pythonconstants.html) ⭐️ 7.0/10

一篇文章探讨了 Python 预声明常量（如 True、False、None 和__debug__）的怪癖和历史奇闻，指出它们行为不一致及其背后的原因。讨论中包含了 CPython issue 的链接和 Guido van Rossum 的评论。 这很重要，因为理解这些怪癖有助于 Python 开发者避免陷阱，并理解语言设计的权衡。它还引发了关于语言设计以及可用性与一致性之间平衡的社区讨论。 文章指出，True、False 和 None 是关键字而非标识符，这在 Python 中很不寻常。__debug__常量尤其奇怪：在 PYTHONOPTIMIZE=1 下，`if __debug__:`保护的代码会从字节码中完全省略，并且不能对其赋值，因为这样做会破坏编译器的假设。

hackernews · rbanffy · Aug 25, 21:39 · [社区讨论](https://news.ycombinator.com/item?id=49441033)

**背景**: Python 在内置命名空间中有少量预声明常量，包括 True、False、None 和__debug__。这些常量在语言中广泛使用，但行为各异：有些是关键字，有些（历史上）可赋值，有些与编译器有特殊交互。文章和讨论提供了历史背景，例如 Python 3 中 True 和 False 变为不可赋值的变化，以及 walrus 运算符在某个疏忽中的作用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://codegurus.eu/pythons-pre-declared-constants-are-kinda-weird-2/">Python 's pre - declared constants are kinda weird... - CodeGurus</a></li>
<li><a href="https://de.sonto.tech/articles/pythons-pre-declared-constants-are-kinda-weird/">python 's pre - declared constants are kinda weird | Sonto</a></li>
<li><a href="https://docs.python.org/3/library/constants.html">Built-in Constants — Python 3.14.7 documentation</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了复杂情绪：一些人批评 Python 的设计不一致，而另一些人则为其可用性权衡辩护。一位评论者赞赏这项调查，并链接到 CPython issue #80233 和 Guido 的解释。另一位则强调了__debug__独特的条件编译行为。

**标签**: `#Python`, `#language design`, `#CPython`, `#programming languages`

---

<a id="item-12"></a>
## [LatticeDB：受 SQLite 启发的嵌入式图数据库](https://github.com/jeffhajewski/latticedb) ⭐️ 7.0/10

LatticeDB 是一个新的开源嵌入式图数据库，旨在像 SQLite 一样易于使用，可通过 pip install latticedb 安装 Python 包。它通过提供零配置的嵌入式体验，旨在简化本地图数据库的使用。 这很重要，因为它解决了开发者在本地使用图数据库时遇到的痛点，现有解决方案往往繁琐。通过提供类似 SQLite 的嵌入式替代方案，它可以降低在应用程序和本地开发中使用图数据库的门槛，可能影响开发者工具生态系统。 LatticeDB 支持属性图，并提供 Python API，具有哈希嵌入等向量搜索功能。然而，嵌套列表和字典值目前未通过公共绑定/C API 公开，错误处理通过特定的异常类提供。

hackernews · smiths1999 · Aug 25, 16:52 · [社区讨论](https://news.ycombinator.com/item?id=49437049)

**背景**: 图数据库以节点、边和属性的形式存储数据，适合处理连接数据。SQLite 是一种流行的嵌入式关系数据库，无需独立服务器即可在进程内运行，LatticeDB 旨在为图工作负载带来类似的便利。其他嵌入式图数据库也存在，如 CogDB 和 LoraDB，但 LatticeDB 专注于易用性和 Python 集成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://latticedb.org/">LatticeDB - Embedded Property-Graph Database</a></li>
<li><a href="https://pypi.org/project/latticedb/">latticedb · PyPI</a></li>
<li><a href="https://cogdb.io/">CogDB – Embedded Graph Database for Python | Graphs , Vectors...</a></li>

</ul>
</details>

**社区讨论**: 社区表现出浓厚的兴趣，提出了关于层次化访问控制建模、类似 Litestream 的备份解决方案以及将 RDF 数据映射到 LatticeDB 节点-边模型的问题。总体情绪积极，对该项目及其示例表示赞赏。

**标签**: `#graph database`, `#embedded database`, `#SQLite alternative`, `#developer tools`, `#open source`

---

<a id="item-13"></a>
## [关于创业文化的个人随笔在 Hacker News 上引发共鸣](https://rorz.io/writing/my-friend-aaron) ⭐️ 7.0/10

一篇题为《我的朋友亚伦》的个人随笔发布在 rorz.io 上，并迅速登上 Hacker News 首页，引发广泛讨论。故事通过亚伦这个角色探讨了野心、妄想和创业文化等主题。 这篇随笔的流行凸显了科技文化中一种常见原型的普遍认同——不断寻找快速致富点子的执着者。它之所以引起共鸣，是因为许多读者都认识像亚伦这样的人，使其成为对创业生态系统的有价值的社会评论。 作者 sarreph 指出，这个故事最初投稿给一个写作比赛但未获回应，在 Hacker News 上发布是一次“碰运气”，却超过了任何比赛认可。评论者称赞了亚伦妄想症逐步发展的可信描写，并将其与现实中的例子如 Justin.tv 和预测市场进行类比。

hackernews · sarreph · Aug 25, 16:53 · [社区讨论](https://news.ycombinator.com/item?id=49437069)

**背景**: Hacker News 是一个以科技为重点的热门社交新闻网站，用户提交链接并参与讨论。能够捕捉科技文化细微之处的个人随笔和故事往往在那里获得关注，尤其是当它们与社区的共同经历产生共鸣时。随笔《我的朋友亚伦》涉及了 AI 过度使用、预测市场和准社会关系等主题，这些对科技社区的许多人来说都很熟悉。

**社区讨论**: 社区讨论总体积极，评论者如 JohnMakin 指出，这个故事之所以引起共鸣，是因为大多数人都认识一个“亚伦”——一个宁愿搞各种计划也不愿真正工作的人。Tyre 称赞了写作，并将其与 Justin.tv 和 Twitch 联系起来，而 corndoge 则欣赏亚伦行为的每个细节都可信且 relatable。作者也对热烈的反响表达了感谢。

**标签**: `#startup-culture`, `#personal-essay`, `#psychology`, `#tech-community`, `#storytelling`

---

<a id="item-14"></a>
## [工具提示需要延迟，并在鼠标移向时跳过延迟](https://blog.master.dev/tooltips-need-a-delay-and-then-they-need-to-skip-it/) ⭐️ 7.0/10

文章提出，工具提示在显示前应有一个延迟，但如果用户光标正移向工具提示的位置，则应跳过该延迟，从而提高可用性并减少挫败感。 这一微妙的交互细节显著提升了带有悬停元素（如菜单和工具提示）的界面的用户体验。它解决了常见的痛点：工具提示出现太快或太慢，影响效率和用户满意度。 该技术涉及测量光标的轨迹和速度以预测意图，当用户主动移向工具提示时跳过延迟。这种方法在响应性和防止意外触发之间取得平衡，并且可以用几行 JavaScript 实现。

hackernews · ibobev · Aug 25, 16:35 · [社区讨论](https://news.ycombinator.com/item?id=49436786)

**背景**: 工具提示是悬停在元素上时出现的小型信息弹出框。通常使用延迟来防止意外触发，但固定的延迟在用户有意移向工具提示时可能显得迟钝。迟滞（hysteresis）的概念——即动作的阈值取决于变化的方向——与此相关。

**社区讨论**: 评论者赞赏这种对细节的关注，并提到了历史先例，如苹果的 System 6 和 Jef Raskin 的工作。一些人分享了实现类似技术的个人经验，另一些人则引用了相关资源并将这一概念描述为迟滞。

**标签**: `#UX`, `#UI design`, `#tooltips`, `#interaction design`, `#HCI`

---

<a id="item-15"></a>
## [CISA 将正在被利用的 Gitea 远程代码执行漏洞加入 KEV 目录](https://www.cisa.gov/news-events/alerts/2026/08/25/cisa-adds-one-known-exploited-vulnerability-catalog) ⭐️ 7.0/10

CISA 已将 CVE-2026-60004（一个严重的 Gitea 代码注入漏洞）添加到其已知被利用漏洞（KEV）目录中，原因是确认存在活跃利用。该漏洞影响 Gitea 和 Forgejo 1.17 至 1.27.0 版本，补丁已在 1.27.1 或更高版本中提供。 此次添加表明该漏洞正在被积极利用，对使用受影响 Gitea 或 Forgejo 实例的组织构成重大风险。根据 BOD 26-04，联邦机构必须及时修复该漏洞，同时鼓励所有组织优先修补以防止入侵。 CVE-2026-60004 是一个预认证远程代码执行漏洞，CVSS 评分为 9.8，源于 diffpatch API，该 API 使用 'git apply --cached' 应用提供的补丁。管理员应立即升级到 Gitea 1.27.1 或更高版本，并保留相关日志以供取证分析。

rss · CISA Cybersecurity Advisories · Aug 25, 12:00

**背景**: KEV 目录是 CISA 维护的已知被利用漏洞列表，用于指导联邦机构和更广泛的社区优先进行修复。约束操作指令 26-04 要求 FCEB 机构快速修复目录中列出的高风险漏洞，尤其是那些在利用后可完全控制资产的漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vulmon.com/vulnerabilitydetails?qid=CVE-2026-60004">Vulnerability details of CVE - 2026 - 60004</a></li>
<li><a href="https://github.com/shinthink/CVE-2026-60004">shinthink/ CVE - 2026 - 60004 : CVE - 2026 - 60004 — Gitea /Forgejo...</a></li>
<li><a href="https://blog.gridinsoft.com/cve-2026-60004-gitea-rce/">CVE - 2026 - 60004 Exploited: Patch Gitea Now | Gridinsoft Blogs</a></li>

</ul>
</details>

**标签**: `#CISA`, `#KEV`, `#vulnerability`, `#security`, `#Gitea`

---

<a id="item-16"></a>
## [HTML 标签名字符允许执行 JavaScript](https://portswigger.net/research/whats-in-a-tag-name-javascript-apparently) ⭐️ 7.0/10

PortSwigger Research 的一位安全研究员调查了 HTML 标签名中允许哪些字符，发现了令人惊讶的组合，这些组合能够执行 JavaScript。研究揭示，除了标准的'a-zA-Z'之外，某些字符也可以用于标签名，从而产生潜在的 XSS 攻击向量。 这项研究对 Web 安全具有重要意义，因为它发现了新的 XSS 攻击向量，可能绕过常见的输入过滤器和 WAF。了解这些字符允许规则有助于开发者和安全专业人员更好地加固他们的应用程序，以抵御跨站脚本攻击。 该研究可能详细说明了标签名中首字母之后允许的特定字符，例如数字、连字符以及其他特殊字符。这些发现可用于构造绕过仅阻止特定标签或字符的过滤器的有效载荷。

rss · PortSwigger Research · Aug 25, 14:24

**背景**: 在 HTML 中，标签名不区分大小写，可以包含字母、数字和某些标点符号。然而，浏览器具有宽松的解析规则，可能允许意外的字符，这些字符可能被利用进行 XSS 攻击。事件处理属性如 onfocus，结合 autofocus 和 tabindex，可以执行 JavaScript，这在常见的 XSS 有效载荷中可以看到。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://html.spec.whatwg.org/multipage/syntax.html">HTML Standard</a></li>
<li><a href="https://shazzer.co.uk/vectors/697ca88a274f790a0323f684">Characters allowed as start of HTML tag name - Shazzer</a></li>
<li><a href="https://freedium-mirror.cfd/https://medium.com/p/009e1f6e99d7">Bypassing a “Safe” Input Field: Reflected XSS via Unescaped HTML ...</a></li>

</ul>
</details>

**标签**: `#web security`, `#XSS`, `#HTML parsing`, `#JavaScript`, `#research`

---

<a id="item-17"></a>
## [OpenAI 首席财务官阐释智能丰裕背后的全栈](https://openai.com/index/the-full-stack-behind-abundant-intelligence) ⭐️ 7.0/10

OpenAI 首席财务官 Sarah Friar 发表了一篇博客文章，解释了芯片、计算、模型和产品方面的进步如何协同作用，以更低的成本、更大的规模提供更有用的智能。文章强调了公司在扩展 AI 能力的同时降低成本的战略重点。 这标志着 OpenAI 致力于降低 AI 成本，使其对企业和开发者更易获取和扩展。这也反映了整个行业优化 AI 全栈（从硬件到应用）以实现“智能丰裕”的趋势。 该文章引入了“每美元有用智能”作为关键指标，与 Friar 早前提出的 AI 记分卡建议一致。它强调了整个栈的复合改进，包括像“Jalapeño”这样的定制芯片和先进模型，以实现成本降低。

rss · OpenAI Blog · Aug 25, 07:05

**背景**: OpenAI 是一家领先的 AI 研究和部署公司，以 GPT-4 和 ChatGPT 等模型闻名。AI 栈指的是技术层——芯片、计算基础设施、模型和应用——它们共同实现 AI 能力。降低这些层的成本对于扩大 AI 采用至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.therundown.ai/p/openai-spicy-new-custom-ai-chip">OpenAI 's spicy new custom AI chip</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sarah_Friar">Sarah Friar - Wikipedia</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI infrastructure`, `#compute`, `#cost reduction`, `#industry trends`

---

<a id="item-18"></a>
## [吴恩达转向 AI 工程领域](https://www.latent.space/p/ainews-andrew-ng-gets-into-ai-engineering) ⭐️ 7.0/10

据 Latent Space 报道，AI 领域的杰出人物吴恩达宣布进入 AI 工程领域。这标志着他的关注点从研究和教育转向实际工程应用。 鉴于吴恩达在 AI 社区中的影响力，他进入 AI 工程领域可能会为这一新兴学科带来更多关注和资源。这也可能激励其他研究人员和实践者关注 AI 系统的实际应用。 该公告通过 Latent Space 平台发布，该平台以报道 AI 发展动态而闻名。目前尚未透露吴恩达在 AI 工程领域的具体项目或计划的细节。

rss · Latent Space · Aug 25, 02:50

**背景**: 吴恩达是 Google Brain 的联合创始人，曾任百度首席科学家，也是 Coursera 的联合创始人。他一直是 AI 领域的杰出教育家，其课程已向数百万人介绍了机器学习。AI 工程是一个专注于构建和部署 AI 系统的实际方面的领域，包括软件工程、MLOps 和系统设计。

**标签**: `#AI`, `#Andrew Ng`, `#AI Engineering`, `#Industry News`

---