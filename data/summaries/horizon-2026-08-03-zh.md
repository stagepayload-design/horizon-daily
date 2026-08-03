# Horizon 每日速递 - 2026-08-03

> From 21 items, 7 important content pieces were selected

---

1. [Kakehashi：在 Linux ARM 上运行 macOS 命令行程序](#item-1) ⭐️ 8.0/10
2. [欧盟年龄验证强制硬件绑定证明，引发隐私与 Linux 担忧](#item-2) ⭐️ 8.0/10
3. [公开信辩论 AI 发展与开放权重](#item-3) ⭐️ 8.0/10
4. [llama.cpp b10232 为 DeepSeek V4 超连接添加 Metal 支持](#item-4) ⭐️ 7.0/10
5. [Karpathy 的鹈鹕引发关于 AI 物理世界基准的讨论](#item-5) ⭐️ 7.0/10
6. [F*：面向形式验证的证明导向编程语言](#item-6) ⭐️ 7.0/10
7. [eBay 骚扰活动导致 5600 万美元赔偿及监禁](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Kakehashi：在 Linux ARM 上运行 macOS 命令行程序](https://github.com/wie-project/kakehashi) ⭐️ 8.0/10

Kakehashi 是一个实验性的用户态翻译层，能够让 macOS ARM64 二进制文件在 Linux aarch64 系统上原生运行。目前已有 7-Zip、curl 和 Xcode Git 工具的工作原型，其中 7-Zip 通过了多线程压缩测试，curl 通过了 200 多个命令测试。 该项目解决了在 Linux ARM 上运行 macOS CLI 二进制文件的重大技术挑战，无需完整的模拟器或虚拟机。如果成功，它可能会扩大软件兼容性并减少对 macOS 硬件的需求，类似于 Wine/Proton 对 Windows 应用程序所做的那样。 Kakehashi 以 CLI 为先，不使用 JIT 编译器；它加载 Darwin Mach-O 二进制文件，映射独立的 libSystem，并翻译 BSD 系统调用。7-Zip 原型目前比原生 Linux 执行慢约 5.2 倍，但开发者已制定了优化计划以缩小这一差距。

hackernews · vlad_kalinkin · Aug 2, 16:26 · [社区讨论](https://news.ycombinator.com/item?id=49145937)

**背景**: 由于可执行文件格式、系统库和系统调用的差异，macOS 二进制文件通常无法与 Linux 兼容。Wine 和 Proton 通过翻译 Windows API 调用，成功让 Windows 应用程序在 Linux 上运行，而 Kakehashi 的目标是在 ARM 上为 macOS CLI 工具实现类似的功能。该项目仍处于实验和早期阶段，只有少数工作原型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/wie-project/kakehashi">wie-project/ kakehashi : Userspace macOS translation layer for Linux ...</a></li>

</ul>
</details>

**社区讨论**: 社区对此充满热情并看到潜力，一些人将其与 Wine/Proton 进行比较，并建议与同样致力于 macOS 二进制兼容性的 Darling 项目合作。其他人指出该项目仍处于早期阶段，并对其方法提出疑问，例如虚拟化框架是否会更简单。还有人希望利用它通过 yabridge 等工具在 Linux 上运行 Audio Unit 插件。

**标签**: `#macOS`, `#Linux`, `#ARM`, `#binary compatibility`, `#userspace`

---

<a id="item-2"></a>
## [欧盟年龄验证强制硬件绑定证明，引发隐私与 Linux 担忧](https://linuxiac.com/eu-age-verification-project-mandates-hardware-bound-attestation/) ⭐️ 8.0/10

欧盟委员会的年龄验证提案强制要求硬件绑定证明，用户需通过硬件支持的凭证来证明年龄，这可能将缺乏兼容设备的桌面 Linux 用户排除在外。 该提案可能为欧盟的数字身份和年龄验证开创先例，影响隐私、数字主权和开源生态系统。它引发了对强制依赖 Google 和 Apple 等专有平台的担忧，可能边缘化 Linux 和其他开放系统。 硬件绑定证明使用设备特定密钥（如 TPM、Secure Enclave）生成可验证的证明，但本质上不使用零知识证明，可能暴露设备标识符。该提案是更广泛的欧盟数字钱包计划的一部分，旨在全面数字身份应用之前采用临时解决方案。

hackernews · RobotToaster · Aug 2, 20:44 · [社区讨论](https://news.ycombinator.com/item?id=49148128)

**背景**: 目前欧盟并未法律强制要求年龄验证，但欧盟委员会已提出基于数字身份的解决方案以保护未成年人上网。硬件绑定证明涉及存储在安全硬件中的加密密钥，可证明设备的完整性和身份。这种方法在移动设备中常见，但在桌面 Linux 上较难实现，因为后者通常缺乏此类硬件或支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eff.org/deeplinks/2025/04/digital-identities-and-future-age-verification-europe">Digital Identities and the Future of Age Verification in Europe</a></li>
<li><a href="https://digital-strategy.ec.europa.eu/en/factpages/blueprint-age-verification-solution-help-protect-minors-online">Blueprint for an age verification solution to help protect minors online</a></li>
<li><a href="https://privacyradar.com/news/cybersecurity/eu-internet-id-age-verification-debate/">EU Internet ID Claims Spark Debate Over Age Verification Rules</a></li>

</ul>
</details>

**社区讨论**: 社区评论对真实动机表示怀疑，认为这是将真实身份与在线活动联系起来，而非保护未成年人。有人担忧反竞争行为，因为政府将强制依赖 Google 或 Apple 账户。Linux 用户担心需要第二台非 Linux 设备，技术用户指出硬件证明可能在没有零知识证明的情况下暴露设备 ID。

**标签**: `#privacy`, `#EU regulation`, `#hardware attestation`, `#digital sovereignty`, `#age verification`

---

<a id="item-3"></a>
## [公开信辩论 AI 发展与开放权重](https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything) ⭐️ 8.0/10

Simon Willison 总结了近期关于 AI 发展的公开信，包括由微软主导、235 家公司签署的《开放权重与美国 AI 领导力》，以及由 1324 名前沿 AI 公司员工签署的《Pacing the Frontier》。这些信件就开放权重 AI 模型的利弊展开辩论，并提出国际合作以控制 AI 发展速度。 这些信件反映了 AI 行业在开放权重模型和 AI 安全方面的重大政策辩论，主要公司和研究人员立场对立。其结果可能影响政府对 AI 发展的监管，进而影响创新、竞争和全球 AI 领导地位。 值得注意的是，Anthropic 未签署微软的信件，并发布了自家回应，其 CEO Dario Amodei 呼吁打击工业规模的蒸馏操作。《Pacing the Frontier》信件由 OpenAI 的 Jakub Pachocki 和 Ilya Sutskever 等知名人士签署，请求美国支持国际合作治理工具以控制自动化 AI 发展。

rss · Simon Willison · Aug 2, 04:16

**背景**: 开放权重 AI 模型是指权重公开的 AI 模型，允许任何人使用、修改和研究。这与仅通过 API 访问的封闭模型形成对比。争论焦点在于开放权重是否通过透明度促进创新和安全，还是可能被恶意行为者滥用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/open-weight-ai-models-why-every-enterprise-should-paying-misra-gi2qc">Open - Weight AI Models : Why Every Enterprise Should Be Paying...</a></li>
<li><a href="https://artificialanalysis.ai/models">Comparison of AI Models across Intelligence, Performance, and Price</a></li>
<li><a href="https://openrouter.ai/collections/free-models">Free AI Models on OpenRouter | OpenRouter</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#open source`, `#AI safety`, `#industry`, `#governance`

---

<a id="item-4"></a>
## [llama.cpp b10232 为 DeepSeek V4 超连接添加 Metal 支持](https://github.com/ggml-org/llama.cpp/releases/tag/b10232) ⭐️ 7.0/10

llama.cpp 版本 b10232 实现了 DeepSeek V4 超连接，并带有优化的 Metal SIMDgroup 内核，增加了对 GGML_OP_DSV4_HC_COMB、GGML_OP_DSV4_HC_PRE 和 GGML_OP_DSV4_HC_POST 操作的支持。这使得在 Apple Silicon 设备上高效推理 DeepSeek V4 模型成为可能。 此版本对 Apple 平台上的 llama.cpp 用户意义重大，因为它带来了对最新 DeepSeek V4 架构的支持，可能提升性能并实现这些模型的本地推理。这体现了该项目持续致力于在多样化硬件上支持前沿模型架构。 该实现包括针对新操作的 SIMDgroup 寄存器和 shuffle 优化内核，以及 Metal 调度和支持管道。该版本还测试了生产 Sinkhorn 迭代次数和嵌入宽度，并因单独的拉取请求而禁用了 macOS Apple Silicon KleidiAI 构建。

github · github-actions[bot] · Aug 2, 18:57

**背景**: llama.cpp 是一个开源的 C/C++ 库，用于 LLM 推理，以其极简设置和在多种硬件上的先进性能而闻名。DeepSeek V4 是最近的大语言模型架构，包含超连接，这是一种增强深度网络中信息流动的技术。Metal 是 Apple 的 GPU 框架，而 SIMDgroup 内核针对 Apple GPU 架构上的并行处理进行了优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ggml-org/llama.cpp">GitHub - ggml -org/llama.cpp: LLM inference in C/C++ · GitHub</a></li>
<li><a href="https://github.com/manishklach/mlx-metal-kernels">GitHub - manishklach/mlx-metal- kernels : Experimental MLX custom...</a></li>

</ul>
</details>

**标签**: `#llama.cpp`, `#Metal`, `#DeepSeek V4`, `#GPU kernels`, `#release`

---

<a id="item-5"></a>
## [Karpathy 的鹈鹕引发关于 AI 物理世界基准的讨论](https://twitter.com/karpathy/status/2083749667410727319) ⭐️ 7.0/10

Andrej Karpathy 在 Twitter 上分享了一个 AI 生成的 3D 鹈鹕动画，迅速引发大量关注，并引发了关于其作为 AI 物理世界理解基准意义的讨论。 这一讨论凸显了 AI 评估从静态图像生成向动态 3D 动画的转变，后者能更好地测试模型对物理规律和空间推理的理解。它强调了可复现基准在追踪 AI 向世界模型发展过程中的重要性。 该动画可能是通过 three.js 代码生成的，一些评论者指出 Anthropic 模型可能经过专门训练来生成此类代码，这可能限制了该基准的普适性。此外，鹈鹕动画未共享提示词也受到批评，因为这阻碍了可复现性。

hackernews · delichon · Aug 2, 04:05 · [社区讨论](https://news.ycombinator.com/item?id=49140998)

**背景**: AI 模型最近从生成静态图像发展到创建 3D 动画，这需要对物理交互和空间关系有更深入的理解。像 PhysBench 这样的基准正在被开发，以评估视觉语言模型的物理世界理解能力，而世界模型旨在模拟物理环境中的因果关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://karpathy.ai/">Andrej Karpathy</a></li>
<li><a href="https://ai-search.io/papers/physbench-benchmarking-and-enhancing-vision-language-models-for-physical-world-understanding">PhysBench: Benchmarking and Enhancing Vision-Language Models...</a></li>
<li><a href="https://claudecode.jp/en/news/student/yann-lecun-raises-dollar1-billion-to-build-ai-that-understands-the-physical">Understanding AI World Models: Why Physical ... - ClaudeCode JP</a></li>

</ul>
</details>

**社区讨论**: 评论者就这一动画的意义展开辩论，有人认为它代表了物理世界理解的新基准，而另一些人则指出它可能只是反映了模型编写 three.js 代码的能力。由于缺少提示词，可复现性问题被提出，还有人分享了类似的 AI 生成 3D 项目的经验。

**标签**: `#AI`, `#3D animation`, `#benchmark`, `#Karpathy`, `#physical world`

---

<a id="item-6"></a>
## [F*：面向形式验证的证明导向编程语言](https://fstar-lang.org/) ⭐️ 7.0/10

F* 被强调为一种通用、面向证明的编程语言，它将形式验证集成到开发过程中，允许程序员在编写代码的同时编写正确性证明。社区讨论指出，该语言支持对现有 C 代码库进行增量迁移。 F* 之所以重要，是因为它弥合了形式验证与实际软件开发之间的差距，为关键系统提供了一种证明正确性的方法。它能够增量迁移 C 代码，使其在实际应用中更易采用，可能提升密码学和系统编程等行业的安全性和可靠性。 F* 使用依赖类型和精化类型系统来表达逻辑约束，从而实现自动化定理证明。该语言与 Steel 相关联，Steel 是一种基于并发分离逻辑的面向证明的编程语言，如 ICFP 2021 论文所述。

hackernews · ducktective · Aug 2, 12:31 · [社区讨论](https://news.ycombinator.com/item?id=49143925)

**背景**: 形式验证是一种使用数学方法证明软件行为符合其规范的技术，超越了传统测试。像 F* 这样的面向证明的语言将逻辑断言嵌入类型系统，使开发者能够陈述并证明代码的属性。这种方法在安全敏感领域尤其有价值，因为在这些领域中，错误可能造成严重后果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fstar-lang.org/">F*: A Proof-Oriented Programming Language</a></li>
<li><a href="https://www.linkedin.com/pulse/f-general-purpose-proof-oriented-programming-language-kusho-4bipc">F * : A general-purpose proof - oriented programming language</a></li>
<li><a href="https://asibiont.com/en/blog/f-yazyk-programmirovaniya-kotoryy-dokazyvaet-korrektnost-vashego-koda">F *: The General-Purpose Language That Turns... — ASI Biont Blog</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论情绪复杂：一些用户批评主页缺乏即时代码示例，而另一些用户则称赞 F* 在迁移 C 代码库方面的实用性。一位用户赞赏在增量迁移过程中表达外部库调用的能力，另一位用户询问行业使用情况，表明对实际应用的兴趣。

**标签**: `#formal verification`, `#programming language`, `#proof-oriented`, `#functional programming`, `#security`

---

<a id="item-7"></a>
## [eBay 骚扰活动导致 5600 万美元赔偿及监禁](https://www.ft.com/content/06ec1b03-d4af-40cf-b12a-4ba5a410f6d2) ⭐️ 7.0/10

eBay 同意向大卫和伊娜·施泰纳夫妇支付 5600 万美元，这对夫妇因批评公司而遭到 eBay 安全团队的骚扰和恐吓。包括吉姆·鲍在内的多名前 eBay 安全高管因参与该活动被判处监禁。 此案凸显了企业不当行为的严重后果以及高层问责的重要性。它警告企业，对批评者进行报复会带来法律和财务风险，并引发了对科技行业其他地方是否存在类似行为的质疑。 骚扰活动包括发送令人不安的包裹，如血淋淋的猪面具，并监视施泰纳夫妇的住所。前安全与安保高级总监吉姆·鲍被判处 57 个月监禁，其他高管则被判处较短刑期或罚款。5600 万美元的赔偿是司法部刑事和解的一部分。

hackernews · JumpCrisscross · Aug 2, 19:19 · [社区讨论](https://news.ycombinator.com/item?id=49147435)

**背景**: eBay 是一个主要的在线市场，用户可以在其中买卖商品。施泰纳夫妇发布了一份批评 eBay 的通讯，促使公司安全团队发起了一场旨在让他们闭嘴的活动。此案凸显了企业安全团队在针对被视为威胁的对象时，可能超越法律界限。

**社区讨论**: 评论者对此事是否孤立事件表示怀疑，质疑 eBay 是否对其他批评者进行过类似活动。一些人还指出 eBay 向卖家收取的高额费用，并与 Leboncoin 等竞争对手进行对比。其他人则引用了一个普遍原则，即缺乏监督的个人可能会从事不当行为，并提到了其他公司的类似案例。

**标签**: `#eBay`, `#corporate misconduct`, `#legal`, `#harassment`, `#security`

---

