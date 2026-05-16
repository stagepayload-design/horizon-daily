---
layout: default
title: "Horizon Summary: 2026-05-16 (ZH)"
date: 2026-05-16
lang: zh
---

> From 49 items, 18 important content pieces were selected

---

1. [Zulip 转型为独立基金会](#item-1) ⭐️ 9.0/10
2. [Google Project Zero 披露 Pixel 10 零点击漏洞链](#item-2) ⭐️ 9.0/10
3. [vLLM v0.21.0：重大变更、KV 卸载与推测解码](#item-3) ⭐️ 8.0/10
4. [Mitchell Hashimoto 警告企业陷入 AI 精神病态](#item-4) ⭐️ 8.0/10
5. [美国司法部要求苹果和谷歌披露超 10 万应用用户信息](#item-5) ⭐️ 8.0/10
6. [Image-blaster：单张图片生成 3D 环境](#item-6) ⭐️ 8.0/10
7. [OCaml 上太空：OxCaml 降低 GC 延迟](#item-7) ⭐️ 8.0/10
8. [ABC 新闻移除所有 FiveThirtyEight 文章](#item-8) ⭐️ 8.0/10
9. [伦敦警方首次在抗议活动中使用人脸识别](#item-9) ⭐️ 8.0/10
10. [新书探索史蒂夫·乔布斯的 NeXT 岁月](#item-10) ⭐️ 8.0/10
11. [加州法案要求停服网游提供补丁或退款](#item-11) ⭐️ 7.0/10
12. [S 形曲线无法拯救 AI 进展](#item-12) ⭐️ 7.0/10
13. [Waymo 因涉水故障召回 3800 辆无人驾驶出租车](#item-13) ⭐️ 7.0/10
14. [Jason Scott 的 ASCII 博客聚焦数字保存](#item-14) ⭐️ 7.0/10
15. [Radicle 推出基于 Git 的去中心化代码协作平台](#item-15) ⭐️ 7.0/10
16. [ShaderKit：一款带循环调试工具的浏览器 GLSL 编辑器](#item-16) ⭐️ 7.0/10
17. [MIT 开源工具逆向工程 LinkedIn 私信实现本地访问](#item-17) ⭐️ 7.0/10
18. [CISA 将微软 Exchange XSS 漏洞加入 KEV 目录](#item-18) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Zulip 转型为独立基金会](https://blog.zulip.com/2026/05/15/announcing-zulip-foundation/) ⭐️ 9.0/10

Zulip 宣布成立 Zulip 基金会，这是一个独立的非营利组织，旨在确保项目的长期开源治理，同时核心团队成员将退出并加入 Anthropic。 此举确保了 Zulip 作为社区治理的开源项目的未来，解决了对商业压力的担忧，并在用户和贡献者之间建立信任。 该基金会将拥有 Zulip 的商标和资产，其治理结构旨在服务于公共利益，而离职的团队成员将加入 Anthropic，而非竞争对手。

hackernews · boramalper · May 15, 18:37 · [社区讨论](https://news.ycombinator.com/item?id=48152168)

**背景**: Zulip 是一个开源团队聊天平台，以其基于主题的线程模型而闻名。许多开源项目已转向基金会治理以确保独立性和可持续性，例如 React 加入 Linux 基金会。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zulip">Zulip - Wikipedia</a></li>
<li><a href="https://zulip.com/">Zulip is an organized team chat app for distributed teams of all sizes.</a></li>
<li><a href="https://github.com/zulip/zulip">zulip / zulip : Zulip server and web application. Open-source team chat ...</a></li>

</ul>
</details>

**社区讨论**: 社区表达了复杂的情绪：对基金会承诺的长期稳定性感到兴奋，但担心 PR 审查缓慢以及团队离职的表象，有些人将其与 Bun 的收购相提并论。

**标签**: `#open-source`, `#governance`, `#Zulip`, `#foundation`, `#community`

---

<a id="item-2"></a>
## [Google Project Zero 披露 Pixel 10 零点击漏洞链](https://projectzero.google/2026/05/pixel-10-exploit.html) ⭐️ 9.0/10

Google Project Zero 研究人员发现了一个针对 Pixel 10 设备的完整零点击漏洞链，从远程 Dolby 音频解码漏洞（CVE-2025-54957）开始，通过一个易受攻击的视频驱动程序升级到完全的内核控制。 该漏洞链凸显了由 AI 驱动的消息处理功能引入的更大攻击面，这些功能在用户交互之前解码媒体，从而实现了零点击攻击。它强调了现代移动设备在集成更多 AI 功能时面临日益增长的安全挑战。 该漏洞链更新了针对 CVE-2025-54957 的先前 Dolby 漏洞，调整了 Pixel 10 特定库版本的偏移量。值得注意的是，这是研究人员报告的首次在供应商披露后 90 天内修补的 Android 驱动程序漏洞。

hackernews · happyhardcore · May 15, 13:39 · [社区讨论](https://news.ycombinator.com/item?id=48148460)

**背景**: 零点击漏洞允许攻击者在没有任何用户交互的情况下入侵设备，因此非常危险。现代手机上的 AI 功能通常会预处理消息（例如解码音频或图像）以实现智能回复或摘要，无意中扩大了攻击面。Google Project Zero 是一个安全研究团队，致力于发现和披露零日漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cyberpress.org/zero-click-exploit-chain-for-pixel-10/">Google Project Zero Reveals Zero-Click Exploit Chain for Pixel 10</a></li>
<li><a href="https://gbhackers.com/pixel-10-zero-click-exploit-chain/">Google Project Zero Details Pixel 10 Zero-Click Exploit Chain</a></li>
<li><a href="https://oxo.is/blog/2026/05/13/news-2026-05-13-a-0-click-exploit-chain-for-the-pixel-10-when-a-door-closes/">A 0-click exploit chain for the Pixel 10 : When a Door Closes...</a></li>

</ul>
</details>

**社区讨论**: 评论者对 AI 功能带来的更大攻击面表示担忧，有人指出未经用户同意预处理消息是一个反复出现的错误。其他人赞扬了谷歌相对较快的修补时间（90 天），但对更广泛的 Android 生态系统感到担忧。一些人质疑最近公布的漏洞激增，将其归因于 AI 炒作或实际漏洞的增加。

**标签**: `#security`, `#exploit`, `#Android`, `#Pixel`, `#Project Zero`

---

<a id="item-3"></a>
## [vLLM v0.21.0：重大变更、KV 卸载与推测解码](https://github.com/vllm-project/vllm/releases/tag/v0.21.0) ⭐️ 8.0/10

vLLM v0.21.0 正式弃用 transformers v4，要求 C++20 编译环境，将 KV 卸载与混合内存分配器 (HMA) 集成，为推理模型添加了带思考预算的推测解码支持，并为 Blackwell GPU 引入了 TOKENSPEED_MLA 注意力后端。 此版本通过强制使用现代依赖、提升内存效率和推理速度，对生产环境中的 LLM 服务产生重大影响，尤其适用于推理模型和 NVIDIA Blackwell 硬件。 transformers v4 弃用是破坏性变更，需迁移至 v5；构建时必须使用 C++20。HMA 与 KV 卸载集成后，每层 KV 缓存占用可减半，但已知 NIXL 连接器会静默禁用 HMA。

github · khluu · May 15, 08:44

**背景**: vLLM 是一个高吞吐量的 LLM 推理引擎。KV 卸载将键值缓存移至 CPU 或远程内存以减轻 GPU 内存压力。推测解码使用较小的草稿模型加速生成。HMA 在 GPU 和 CPU 之间动态分配内存以实现最佳性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm/issues/42024">[Bug]: NIXL connector silently disables HMA , halving KV cache...</a></li>
<li><a href="https://pypi.org/project/tokenspeed-mla/">Speed-of-light TokenSpeed MLA kernels for Blackwell SM100 and...</a></li>
<li><a href="https://iamhemanth.in/blog/speculative-decoding-the-billion-dollar-trick-hiding-in-plain-sight">Speculative Decoding : The Billion-Dollar Trick Hiding in Plain Sight</a></li>

</ul>
</details>

**社区讨论**: 社区评论对 HMA 和推测解码的改进表示兴奋，但也报告了一个关键错误：NIXL 连接器会静默禁用 HMA，使有效 KV 缓存容量减半。用户建议在生产环境升级前仔细测试。

**标签**: `#vLLM`, `#LLM inference`, `#GPU optimization`, `#speculative decoding`, `#transformers`

---

<a id="item-4"></a>
## [Mitchell Hashimoto 警告企业陷入 AI 精神病态](https://twitter.com/mitchellh/status/2055380239711457578) ⭐️ 8.0/10

HashiCorp 工具（如 Terraform 和 Vagrant）的创建者 Mitchell Hashimoto 发帖警告，许多公司正因盲目信任 AI 输出而患上“AI 精神病态”，导致系统脆弱和决策失误。 这一评论凸显了在软件工程和商业决策中快速采用 AI 的关键风险，可能导致系统性不稳定和人类监督的缺失。 Hashimoto 在 X（原 Twitter）和 Mastodon 上的帖子引发了 316 条评论的讨论，用户们争论了在未经验证的情况下过度依赖 AI 进行代码生成和决策的危险。

hackernews · reasonableklout · May 15, 20:26 · [社区讨论](https://news.ycombinator.com/item?id=48153379)

**背景**: AI 精神病态指不加批判地将 AI 生成的内容视为权威，而不进行人工验证。这在软件工程中尤其危险，因为 AI 编写的代码可能引入难以发现的细微错误或安全漏洞。

**社区讨论**: 评论者大多同意 Hashimoto 的观点，分享了公司发布有缺陷的 AI 生成代码并依赖 AI 代理快速修复的轶事，他们认为这形成了一个脆弱的循环。一些人指出，这最终可能迫使软件工程采用更严格的工程实践。

**标签**: `#AI`, `#software engineering`, `#risk management`, `#critical thinking`

---

<a id="item-5"></a>
## [美国司法部要求苹果和谷歌披露超 10 万应用用户信息](https://macdailynews.com/2026/05/15/u-s-doj-demands-apple-and-google-unmask-over-100000-users-of-popular-car-tinkering-app-in-emissions-crackdown/) ⭐️ 8.0/10

美国司法部于 2026 年 3 月和 4 月向苹果和谷歌发出传票，要求提供超过 10 万名安装 Auto Agent 应用（一种用于禁用排放控制系统的汽车改装工具）用户的下载和账户数据。 此案为政府对应用商店用户的监控开创了先例，引发了严重的隐私担忧，并凸显了集中式应用分发的风险。它可能影响数百万出于合法目的改装车辆的用户。 司法部要求获取所有下载 Auto Agent 应用的用户数据，包括合法使用该应用的用户，而不仅仅是违反排放法规的用户。根据联合法庭文件，传票于 2026 年 3 月和 4 月发出。

hackernews · tencentshill · May 15, 17:28 · [社区讨论](https://news.ycombinator.com/item?id=48151383)

**背景**: Auto Agent 是一款允许用户修改汽车发动机控制单元（ECU）设置的移动应用，通常用于禁用柴油颗粒过滤器或选择性催化还原等排放控制系统。虽然有些人将其用于性能调校，但也有人用它来绕过排放测试，这在许多司法管辖区是非法的。司法部的调查针对的是可能违反《清洁空气法》的行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://macdailynews.com/2026/05/15/u-s-doj-demands-apple-and-google-unmask-over-100000-users-of-popular-car-tinkering-app-in-emissions-crackdown/">U.S. DOJ demands Apple and Google unmask over 100,000 users of...</a></li>
<li><a href="https://news.ycombinator.com/item?id=48151383">U.S. DOJ demands Apple and Google unmask over 100k users of...</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了强烈的隐私担忧，一些人认为政府应针对特定违规者而非所有用户。其他人指出，这一先例可能被汽车制造商用来压制合法的改装，例如禁用 GPS 追踪。少数人建议使用像 F-Droid 这样的匿名应用商店来避免监控。

**标签**: `#privacy`, `#government surveillance`, `#app stores`, `#legal`, `#emissions`

---

<a id="item-6"></a>
## [Image-blaster：单张图片生成 3D 环境](https://github.com/neilsonnn/image-blaster) ⭐️ 8.0/10

Image-blaster 是一个开源工具，利用 WorldLabs 的 Marble 模型等 AI 技术，从单张图片生成 3D 环境、特效和网格。 该工具大幅降低了 3D 内容创作的门槛，使艺术家和开发者能够从单张照片快速构建 3D 场景原型，从而加速游戏开发、电影和 AR/VR 领域的工作流程。 该工具使用 WorldLabs 的 Marble 模型实现空间智能，并可能集成 Meshy.ai 等其他模型用于非场景资产。它是开源的，托管在 GitHub 上，允许社区贡献。

hackernews · MattRogish · May 15, 15:42 · [社区讨论](https://news.ycombinator.com/item?id=48150069)

**背景**: 图像到 3D 生成是一个新兴的 AI 领域，将 2D 图像转换为 3D 模型。由李飞飞创立的 WorldLabs 最近发布了 Marble，这是一个世界模型，可以从图像生成 3D 世界，代表了向空间智能迈出的重要一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fastcompany.com/91437004/fei-fei-li-world-labs-spatial-ai-mapping-3d">Fei-Fei Li debuts world -generating AI model - Fast Company</a></li>
<li><a href="https://hy3d.dev/">Hunyuan 3 D | Free AI Image to 3 D Generator - No Signup</a></li>

</ul>
</details>

**社区讨论**: 评论者对从多图像到单图像 3D 生成的进步印象深刻，一些人称赞 WorldLabs 模型的质量。然而，有用户报告结果经常出现幻觉且不可用，另一个人则对类似的等距精灵工具表示兴趣。

**标签**: `#3D generation`, `#AI`, `#computer vision`, `#open source`, `#image-to-3D`

---

<a id="item-7"></a>
## [OCaml 上太空：OxCaml 降低 GC 延迟](https://gazagnaire.org/blog/2026-05-14-borealis.html) ⭐️ 8.0/10

一篇博客文章报告称，OxCaml 的栈注解消除了 GC 压力，在卫星调度热路径上将 p99.9 延迟从每包 29 纳秒降至 9 纳秒，处理 2500 万数据包时零次 minor GC。 这表明像 OCaml 这样的垃圾回收语言能够实现适用于太空系统的确定性、低延迟性能，可能拓宽高级语言在嵌入式和实时环境中的应用。 通过在调度代码中添加 @local 栈注解，将分配从堆移至栈，从而减少了 GC 压力和延迟。吞吐量与原始版本相当。

hackernews · yminsky · May 15, 10:55 · [社区讨论](https://news.ycombinator.com/item?id=48147058)

**背景**: OCaml 是一种函数式编程语言，其垃圾回收器 (GC) 可能导致不可预测的暂停。OxCaml 是 OCaml 的扩展，引入了栈分配注解 (@local)，使开发者能够控制分配并减少 GC 压力。太空软件要求高可靠性和低延迟，因此 GC 开销是一个关注点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://oxcaml.org/documentation/stack-allocation/reference/">OxCaml | Stack allocation | Reference</a></li>
<li><a href="https://anil.recoil.org/notes/oxcaml-httpz">My (very) fast zero-allocation webserver using OxCaml</a></li>
<li><a href="https://www.thenextgentechinsider.com/posts/oxcaml-supercharging-ocaml-for-modern-development">OxCaml: Supercharging OCaml for Modern Development</a></li>

</ul>
</details>

**社区讨论**: 社区成员指出了历史先例：一位用户早在 2016 年就在卫星上部署了 OCaml。其他人讨论了让 GC 语言像非 GC 语言一样运行的难度，并质疑内存安全是否是卫星网络中最大的攻击面。

**标签**: `#OCaml`, `#space`, `#GC`, `#systems programming`, `#latency`

---

<a id="item-8"></a>
## [ABC 新闻移除所有 FiveThirtyEight 文章](https://twitter.com/baseballot/status/2055309076209492208) ⭐️ 8.0/10

ABC 新闻已移除 FiveThirtyEight 的所有文章，实际上删除了该数据新闻网站的整个存档。此举发生在该网站经历裁员和投资减少后逐渐衰落之后。 此次移除抹去了大量数据新闻内容，包括标志性的可视化和分析，凸显了企业品牌忽视问题。它影响了依赖 FiveThirtyEight 独特内容的研究人员、记者和公众。 FiveThirtyEight 创始人 Nate Silver 透露，ABC 拒绝将 IP 卖回给他，理由是他批评了他们的品牌管理。该网站的 GitHub 仓库目前仍可用，但用户被敦促备份。

hackernews · cmsparks · May 15, 19:07 · [社区讨论](https://news.ycombinator.com/item?id=48152553)

**背景**: FiveThirtyEight 是由 Nate Silver 创立的数据新闻网站，以对政治、体育和科学的统计分析而闻名。它于 2013 年被 ABC 新闻收购，后来归迪士尼所有。在 2023 年裁员后，该网站的输出减少，最终导致关闭。

**社区讨论**: 评论者对高质量可视化的丢失表示悲伤，并批评 ABC 的管理。一些人指出 FiveThirtyEight 只在选举年盈利，而另一些人猜测 ABC 拒绝出售 IP 是出于小气。

**标签**: `#data journalism`, `#FiveThirtyEight`, `#corporate strategy`, `#content removal`, `#visualization`

---

<a id="item-9"></a>
## [伦敦警方首次在抗议活动中使用人脸识别](https://reclaimthenet.org/london-police-deploy-facial-recognition-at-protest-for-first-time) ⭐️ 8.0/10

伦敦大都会警察在活动人士汤米·罗宾逊组织的抗议集会上部署了实时人脸识别技术，这是英国首次授权在抗议活动中使用该技术。 这为警方在政治活动中进行监控开创了先例，引发了对隐私、公民自由以及可能被滥用于合法抗议的严重担忧。此举可能鼓励其他警察部队采取类似策略。 这场名为“团结王国，团结西方”的集会由有犯罪前科的活动人士汤米·罗宾逊组织。大都会警察此前在克罗伊登试点 LFR，六个月内每三天逮捕一人。

hackernews · Cider9986 · May 15, 20:28 · [社区讨论](https://news.ycombinator.com/item?id=48153400)

**背景**: 实时人脸识别通过摄像头实时扫描人脸，并与通缉名单进行比对。该技术因不准确和种族偏见而受到批评，在公共场所使用也引发隐私担忧。英国一直在扩大监控权力，包括使用闭路电视和数据追踪。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.lutzker.com/insights/curtailing-bias-in-facial-recognition-technology/">Curtailing Bias in Facial Recognition Technology - Lutzker & Lutzker</a></li>

</ul>
</details>

**社区讨论**: 评论者对这项技术的有效性表示怀疑，指出闭路电视未能帮助前首相找回被盗自行车。有人指出，对汤米·罗宾逊这样的争议人物使用监控具有讽刺意味，并警告此类工具日后可能被用于针对其他事业。还有人注意到人脸识别对硬件要求低，暗示其可能变得普及。

**标签**: `#facial recognition`, `#privacy`, `#surveillance`, `#UK`, `#protest`

---

<a id="item-10"></a>
## [新书探索史蒂夫·乔布斯的 NeXT 岁月](https://spectrum.ieee.org/steve-jobs-next-computer) ⭐️ 8.0/10

一本新书深入探讨了史蒂夫·乔布斯在 NeXT Computer 的转型岁月，分析了该公司的技术以及乔布斯的个人成长如何后来塑造了苹果的复兴。 这段时期对于理解现代苹果至关重要，因为 NeXT 的操作系统成为了 macOS 和 iOS 的基础，而乔布斯的领导力演变是苹果复兴的关键。 这本书涵盖了乔布斯在 NeXT 的 12 年（1985 年至 1997 年），重点介绍了 NeXTSTEP 和 NeXT 计算机的开发，以及乔布斯作为管理者的成熟过程。

hackernews · rbanffy · May 15, 10:34 · [社区讨论](https://news.ycombinator.com/item?id=48146908)

**背景**: NeXT 是史蒂夫·乔布斯于 1985 年离开苹果后创办的一家电脑公司。其操作系统 NeXTSTEP 基于 Mach 内核和 BSD Unix，后来成为苹果 macOS 和 iOS 的基础。该公司在商业上并不成功，但其技术产生了深远影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NeXTSTEP">NeXTSTEP - Wikipedia</a></li>
<li><a href="https://www.howtogeek.com/698532/before-mac-os-x-what-was-nextstep-and-why-did-people-love-it/">Before Mac OS X: What Was NeXTSTEP , and Why Did People Love It?</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，现代苹果很大程度上建立在 NeXT 技术之上，而乔布斯在 NeXT 的时期是他个人成长的阶段。有人不同意将早期苹果描述为失败，指出 Apple II 的成功。还有人提到一个将 NeXTSTEP 外观和感觉移植到 Linux 的项目。

**标签**: `#Steve Jobs`, `#NeXT`, `#Apple`, `#tech history`, `#business biography`

---

<a id="item-11"></a>
## [加州法案要求停服网游提供补丁或退款](https://arstechnica.com/gaming/2026/05/bill-to-keep-online-games-playable-clears-key-hurdle-in-california/) ⭐️ 7.0/10

一项加州法案要求游戏发行商在关闭服务器时，要么发布补丁使在线游戏可离线运行，要么提供退款；该法案于 2026 年 5 月通过了关键的立法障碍。 该法案可能为美国的数字消费者权益和游戏保存开创先例，迫使发行商考虑在线游戏的长期支持，并可能降低游戏因服务器关闭而无法游玩的风险。 该法案豁免了仅通过订阅提供的游戏，批评者认为这可能加速向订阅模式的转变。发行商还可能面临高昂的合规成本，从而可能完全阻碍在线游戏的创作。

hackernews · Lihh27 · May 15, 19:48 · [社区讨论](https://news.ycombinator.com/item?id=48152994)

**背景**: 在线游戏通常依赖中央服务器提供核心功能，当发行商关闭这些服务器时，游戏将无法游玩。这引发了消费者的不满，并呼吁立法保护购买行为。其他地区已有类似法律，例如法国的消费者保护规则。

**社区讨论**: 评论者意见分歧：一些人主张开源服务器代码以允许社区运营服务器，而另一些人则警告该法案可能使在线游戏的生产风险更高，从而可能损害小型开发者。还有人担心意外后果，例如迫使发行商转向纯订阅模式。

**标签**: `#digital rights`, `#game preservation`, `#legislation`, `#consumer protection`, `#online games`

---

<a id="item-12"></a>
## [S 形曲线无法拯救 AI 进展](https://www.astralcodexten.com/p/the-sigmoids-wont-save-you) ⭐️ 7.0/10

一篇文章认为 AI 进展可能不遵循 S 形曲线，并警告在未理解基本限制的情况下外推趋势是有风险的。 这挑战了 AI 扩展将平稳持续的常见假设，敦促社区考虑潜在的平台期或技术转变。 文章使用飞机速度等历史例子说明技术如何达到极限并被取代，并引入林迪定律作为替代启发式方法。

hackernews · Tomte · May 15, 10:51 · [社区讨论](https://news.ycombinator.com/item?id=48147021)

**背景**: S 形曲线描述缓慢的初始增长、快速加速然后趋于平稳。在 AI 中，扩展定律表明性能随计算量可预测地提升，但基本限制可能导致放缓。

**社区讨论**: 评论者就林迪定律对 AI 趋势的适用性展开辩论，一些人指出作者在 AGI 时间线上有个人利益。其他人则强调预测技术限制的困难。

**标签**: `#AI`, `#scaling laws`, `#technology trends`, `#machine learning`, `#philosophy of science`

---

<a id="item-13"></a>
## [Waymo 因涉水故障召回 3800 辆无人驾驶出租车](https://www.cnbc.com/2026/05/12/waymo-recalls-3800-robotaxis-after-able-drive-into-standing-water.html) ⭐️ 7.0/10

Waymo 对 3800 辆无人驾驶出租车发起召回，以修复一个导致部分车辆驶入积水的软件故障。修复通过空中升级（OTA）部署，无需物理召回。 这一事件凸显了自动驾驶面临的棘手边缘场景——区分湿路面与深水——并展示了集中式空中升级在快速修复整个车队安全问题上的优势。 此次召回涉及所有在运营的 3800 辆 Waymo 车辆。软件更新改进了感知系统检测和避开积水的能力，但公司未披露具体的传感器变更细节。

hackernews · drob518 · May 15, 18:00 · [社区讨论](https://news.ycombinator.com/item?id=48151767)

**背景**: Waymo 的自动驾驶系统“Waymo Driver”使用摄像头、雷达和激光雷达感知环境。积水是一个已知的边缘场景，因为它看起来与湿路面相似，驶入深水可能损坏车辆或导致乘客被困。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.usatoday.com/story/news/weather/2026/05/13/waymo-robotaxi-car-recall-severe-weather/90051311007/">Waymo recall after one hit flooded road. Can robotaxis drive in storms?</a></li>
<li><a href="https://www.kognic.com/articles/edge-cases-autonomous-driving">Edge Cases in Autonomous Driving: Detection and Handling Guide</a></li>

</ul>
</details>

**社区讨论**: 评论者指出感知问题的难度，有人建议安装专用水位传感器。其他人则称赞空中升级模式，认为这种快速的全车队修复使自动驾驶汽车随着时间推移比人类驾驶员更安全。

**标签**: `#autonomous vehicles`, `#Waymo`, `#safety`, `#software update`, `#edge case`

---

<a id="item-14"></a>
## [Jason Scott 的 ASCII 博客聚焦数字保存](https://ascii.textfiles.com/) ⭐️ 7.0/10

分享了一个指向 Jason Scott 的 ASCII 博客（ascii.textfiles.com）的链接，表彰他在数字保存和归档方面的持续工作，包括为互联网档案馆数字化了超过 1300 盘磁带和 13000 本手册。 Jason Scott 的丰富贡献对于保存数字历史至关重要，使晦涩的文化遗产对公众可访问，并确保信息保持自由。 博客文章本身只是一个简单的链接，但社区评论强调了具体成就：数字化了一生收集的磁介质（超过 1300 盘磁带）以及现在互联网档案馆上的 13000 本手册合集。

hackernews · bookofjoe · May 15, 14:02 · [社区讨论](https://news.ycombinator.com/item?id=48148726)

**背景**: Jason Scott 是一位数字档案管理员、历史学家，也是 Archive Team 的联合创始人，以在互联网档案馆的工作而闻名。自 20 世纪 90 年代以来，他的 ASCII 博客一直是复古计算和保存的中心。数字保存涉及通过大规模数字化项目，将数字内容从过时和衰败中拯救出来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://anarchivism.org/w/Jason_Scott_Talks">Jason Scott Talks - Anarchivism</a></li>
<li><a href="https://archive.org/details/jason-scott-everything-is-burning-a-fireside-chat-banff-november-2024">Everything Is Great Except the Burning: A Fireside Chat : Jason Scott ...</a></li>
<li><a href="https://flipso.com/p/m96khtnve">Jason Scott ’s weblog on archiving, manuals, and digital preservation .</a></li>

</ul>
</details>

**社区讨论**: 评论者赞扬 Jason Scott 的奉献精神和产出，有人提到他数字化了超过 1300 盘罕见的纽约音乐和文化磁带。另一个人强调了过去十年上传的 13000 本手册，称其为非凡成就。还有用户指出了更新的存档链接，并提到 Jason Scott 在 Twitch 上的直播。

**标签**: `#digital preservation`, `#archiving`, `#Jason Scott`, `#Internet Archive`, `#retrocomputing`

---

<a id="item-15"></a>
## [Radicle 推出基于 Git 的去中心化代码协作平台](https://radicle.dev/) ⭐️ 7.0/10

Radicle 推出了一个基于 Git 的自主、点对点代码协作平台，为 GitHub 等中心化平台提供了去中心化替代方案。该平台允许开发者托管和协作仓库，无需依赖任何单一实体。 这很重要，因为它解决了中心化代码托管中日益严重的审查、控制和隐私问题。通过实现抗审查的协作，Radicle 赋能开发者，并促进更具韧性的开源生态系统。 Radicle 是本地优先的，支持在可信对等点之间选择性复制的私有仓库，但静态数据未加密。该平台默认使用加密身份和签名工件，并采用 Apache 2.0 许可证，而非 AGPL。

hackernews · KolmogorovComp · May 15, 12:07 · [社区讨论](https://news.ycombinator.com/item?id=48147603)

**背景**: 传统的代码托管平台如 GitHub 是中心化的，意味着单一公司控制网络并可能审查或限制访问。Radicle 基于广泛使用的版本控制系统 Git 构建，但增加了点对点层以实现去中心化协作。该项目至少从 2020 年开始开发，并于 2023 年 4 月宣布了 Heartwood 协议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://radicle.dev/">The Radicle forge is an open source, peer-to-peer code collaboration ...</a></li>
<li><a href="https://security-zone.info/cybersecurity/radicle-sovereign-code-forge-built-on-git/">Radicle: Sovereign { code forge } built on Git - Security Zone Info</a></li>
<li><a href="https://dev.abobateam.com/item?id=48147603">Radicle: Sovereign { code forge } built on Git | Hacker News</a></li>

</ul>
</details>

**社区讨论**: 社区评论呈现复杂情绪：一些用户称赞 Radicle 的本地优先设计和私有仓库支持，而另一些用户则对私有仓库安全性以及选择 Apache 2.0 而非 AGPL 表示担忧，担心这可能导致 SaaS 公司拥抱并扩展该平台。也有用户怀念 Radicle 早期的网站设计。

**标签**: `#decentralization`, `#git`, `#code forge`, `#open source`, `#p2p`

---

<a id="item-16"></a>
## [ShaderKit：一款带循环调试工具的浏览器 GLSL 编辑器](https://shaderkit.com/app) ⭐️ 7.0/10

ShaderKit 是一款新的基于浏览器的 GLSL 编辑器，提供高级循环调试功能，如循环检查模式和 X 时间重映射，以及高达 8K 的云渲染和带有自定义调色板及抖动的 GIF 导出器。 它通过提供 Shadertoy 所缺少的导出流程和调试工具，解决了着色器艺术社区的一个空白，使艺术家更容易完成和分享他们的分形艺术。 核心编辑器和功能是免费的，而云渲染由于 GPU 成本需要付费。它还包含一个可选的基于 Claude 的氛围模式，用于 AI 辅助着色器生成。

rss · Hacker News Show HN · May 15, 22:38

**背景**: GLSL（OpenGL 着色语言）用于编写在 GPU 上运行的着色器，常用于实时图形和分形艺术。Shadertoy 是一个流行的在线分享 GLSL 着色器的平台，但缺乏内置导出和高级调试工具。ShaderKit 旨在通过专为创建无缝循环着色器而设计的功能来填补这一空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Shadertoy">Shadertoy - Wikipedia</a></li>

</ul>
</details>

**标签**: `#GLSL`, `#shader art`, `#fractal art`, `#web tool`, `#creative coding`

---

<a id="item-17"></a>
## [MIT 开源工具逆向工程 LinkedIn 私信实现本地访问](https://allman.sh/) ⭐️ 7.0/10

一位开发者发布了 Allman，这是一个开源 CLI 和 TUI 工具，通过逆向工程 LinkedIn 的即时通讯系统，让用户本地访问自己的私信，全程借助 Claude Code 在 24 小时内完成构建。 该工具挑战了平台对用户自有数据收费的模式，并展示了 AI 如何大幅简化逆向工程，未来可能催生针对其他即时通讯工具的类似方案。 该工具通过将 LinkedIn 编译后的 JavaScript 二进制文件输入 Claude Code，由 AI 逆向工程了整个收件箱。作者指出 LinkedIn 的分片/访问机制很严苛，工具可能会失效，但这种方法证明了借助 AI 逆向工程已变得轻而易举。

rss · Hacker News Show HN · May 15, 20:45

**背景**: 逆向工程是指分析软件的编译代码以理解其内部机制，常用于创建兼容工具或提取数据。传统上这需要深厚的专业知识和大量手动工作。像 Claude Code 这样的 AI 模型现在可以通过解读代码并生成可运行的实现来自动化大部分流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://modernorange.io/item/48153575">Show HN: MIT OSS LinkedIn DMs for Agents ( CLI ...) | Modern Orange</a></li>

</ul>
</details>

**标签**: `#reverse engineering`, `#LinkedIn`, `#open source`, `#AI`, `#messaging`

---

<a id="item-18"></a>
## [CISA 将微软 Exchange XSS 漏洞加入 KEV 目录](https://www.cisa.gov/news-events/alerts/2026/05/15/cisa-adds-one-known-exploited-vulnerability-catalog) ⭐️ 7.0/10

由于存在活跃利用证据，CISA 将微软 Exchange Server 中的一个跨站脚本漏洞 CVE-2026-42897 添加到了已知被利用漏洞（KEV）目录中。 此次添加要求美国联邦机构根据 BOD 22-01 进行修复，并向所有使用微软 Exchange Server 的组织发出严重风险信号，敦促立即打补丁。 该漏洞是微软 Exchange Server 中的一个跨站脚本（XSS）问题，CISA 强烈建议所有组织将其修复作为漏洞管理的优先事项。

rss · CISA Cybersecurity Advisories · May 15, 12:00

**背景**: KEV 目录是根据 BOD 22-01 建立的已知被利用漏洞列表，这些漏洞对联邦网络构成重大风险。联邦机构必须在规定截止日期前修复列表中的漏洞。跨站脚本漏洞允许攻击者向其他用户查看的网页中注入恶意脚本。

**标签**: `#cybersecurity`, `#CISA`, `#Microsoft Exchange`, `#vulnerability`, `#CVE`

---