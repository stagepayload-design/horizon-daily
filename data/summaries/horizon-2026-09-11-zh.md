# Horizon 每日速递 - 2026-09-11

> From 38 items, 11 important content pieces were selected

---

1. [CERT-EU 警告 Check Point 存在严重 RCE 漏洞（CVSS 9.8）](#item-1) ⭐️ 9.0/10
2. [AOMEI Backupper 驱动漏洞可致 UEFI 级攻击](#item-2) ⭐️ 8.0/10
3. [OpenAI 推出搭载 GPT-6 Astra 的金融版 ChatGPT](#item-3) ⭐️ 8.0/10
4. [trynix.dev 借助 qemu-wasm 在浏览器中启动任意 Nix 包](#item-4) ⭐️ 8.0/10
5. [Shopify 因 AI 智能体回归原生移动开发](#item-5) ⭐️ 8.0/10
6. [Cloudflare 1.1.1.1 解析器新增后量子 DNSSEC 支持](#item-6) ⭐️ 8.0/10
7. [研究人员利用 Codex 和 ChatGPT 挖掘基因组以寻找新型抗菌分子](#item-7) ⭐️ 7.0/10
8. [OpenAI 在 ChatGPT Work 中推出数据智能体](#item-8) ⭐️ 7.0/10
9. [OpenAI 与 GSA 合作扩大美国政府 AI 访问](#item-9) ⭐️ 7.0/10
10. [Unit 42 揭示通过 Kubernetes 节点 root 权限滥用 SPIFFE/SPIRE 身份](#item-10) ⭐️ 7.0/10
11. [为 AI 供电本质上是架构问题，而非单纯的能源问题](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [CERT-EU 警告 Check Point 存在严重 RCE 漏洞（CVSS 9.8）](https://cert.europa.eu/publications/security-advisories/2026-012/) ⭐️ 9.0/10

2026 年 9 月 9 日，Check Point 发布了紧急安全更新，修复影响 Security Gateway、Security Management Server 和 Spark Firewall 的两个严重漏洞，这些设备均配置了 Remote Access VPN 或 Site-to-Site VPN。两个漏洞的 CVSS 评分均为 9.8，可允许未经身份验证的远程攻击者在受影响设备上执行任意代码，CERT-EU 因此发布紧急公告，建议立即安装热修复补丁。 由于这些产品部署在网络边界，被企业和政府机构广泛使用，一个未经身份验证且评分达到最高严重级别的 RCE 漏洞意味着设备可能被完全攻陷，风险极高。CERT-EU 的紧急公告表明，面向互联网和边界设备必须立即修补，这对欧盟及其他地区的安全团队而言是最高优先级的行动事项。 这些漏洞仅影响配置了 Remote Access VPN 或 Site-to-Site VPN 的部署环境，两者的 CVSS 评分均为 9.8，属于远程代码执行漏洞中的最高严重级别。CERT-EU 特别建议在安装热修复补丁时优先处理面向互联网和边界的设备。

rss · CERT-EU Security Advisories · Sep 10, 10:20

**背景**: CVSS（通用漏洞评分系统）是业界评估漏洞严重程度的标准框架，评分范围为 0 到 10 分，9.8 分意味着这是一个无需身份验证即可远程利用的严重漏洞。Check Point Security Gateway 和 Security Management Server 是 Check Point 企业防火墙与 VPN 架构的核心组件，而 Spark Firewall 是 Check Point 较新的产品。CERT-EU 是面向欧盟机构、机关和组织的计算机应急响应团队，负责发布安全公告并协调欧洲范围内的安全事件响应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator">NVD CVSS v3 Calculator</a></li>
<li><a href="https://cert.europa.eu/">CERT - EU</a></li>
<li><a href="https://en.wikipedia.org/wiki/Computer_emergency_response_team">Computer emergency response team - Wikipedia</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#checkpoint`, `#remote-code-execution`, `#cert-eu`

---

<a id="item-2"></a>
## [AOMEI Backupper 驱动漏洞可致 UEFI 级攻击](https://kb.cert.org/vuls/id/687587) ⭐️ 8.0/10

CERT/CC 发布了 VU#687587（CVE-2026-12780），这是 AOMEI Backupper 8.4.0 所附带的 amwrtdrv.sys 内核驱动中的一个权限分配错误漏洞。该驱动创建了一个没有安全描述符、任何用户都可访问的设备对象，使任意非特权本地用户都能打开 \\.\mwrtdrv\DISK0 并向物理磁盘发出不受限制的写请求。 由于该漏洞允许写入分区前间隙（LBA 34–2047）并修改 GPT，攻击者可以注入在 Windows 加载之前运行的恶意 UEFI 载荷，从而绕过 HVCI、EDR、Windows Defender 和 Hyper-V 隔离。在仅使用 TPM 保护的 BitLocker 系统上，这还会促成在预启动阶段窃取卷主密钥（VMK）材料的“邪恶女佣”攻击。 利用该漏洞需要本地非特权访问权限，并且要执行 UEFI 代码路径还需关闭 Secure Boot；载荷会在 UEFI 启动设备选择（BDS）阶段执行。CERT/CC 建议更新到修复后的 amwrtdrv.sys，无法打补丁的用户应卸载 AOMEI Backupper，或将驱动启动类型从 AUTO_START 改为禁用，而启用 Secure Boot 仅能提供纵深防御。

rss · CERT CC Vulnerability Notes · Sep 10, 17:46

**背景**: AOMEI Backupper 是一款 Windows 备份与灾难恢复软件，它使用 amwrtdrv.sys 内核驱动来执行镜像、克隆等底层磁盘操作。内核驱动以高权限运行，因此若驱动暴露的设备对象缺乏适当的访问控制，就会成为本地权限提升的途径。HVCI（虚拟机监控程序保护的代码完整性）是 Windows 基于虚拟化的安全功能，用于校验内核代码完整性；而 BitLocker 的卷主密钥（VMK）是一种中间密钥，用于保护全卷加密密钥，通常由 TPM 或密码保护器封装。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sentinelone.com/vulnerability-database/cve-2026-12780/">CVE-2026-12780: AOMEI Backupper Privilege Escalation Flaw</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows/security/hardware-security/enable-virtualization-based-protection-of-code-integrity">Enable memory integrity | Microsoft Learn</a></li>
<li><a href="https://security.stackexchange.com/questions/214671/what-is-the-purpose-of-the-volume-master-key-in-bitlocker">What is the purpose of the Volume Master Key in BitLocker ?</a></li>

</ul>
</details>

**标签**: `#vulnerability`, `#privilege-escalation`, `#kernel-driver`, `#UEFI`, `#BitLocker`

---

<a id="item-3"></a>
## [OpenAI 推出搭载 GPT-6 Astra 的金融版 ChatGPT](https://openai.com/index/introducing-chatgpt-financial-services) ⭐️ 8.0/10

OpenAI 宣布推出 ChatGPT for Financial Services，这一专用产品将内置的机构金融数据源与全新的 GPT-6 Astra 模型相结合，用于研究、建模以及生成可直接交付客户的材料。该产品被定位为 OpenAI 服务金融行业的多种解决方案之一。 这标志着 OpenAI 首次推出面向金融服务的专用垂直产品，表明其正进军对准确性、合规性和数据来源要求极高的受监管企业市场。此举可能加速银行、资产管理公司和金融科技企业对 AI 的采用，同时给彭博、FactSet 等竞争对手及其他企业 AI 厂商带来压力。 GPT-6 Astra 也可通过 OpenAI API 以 gpt-6-astra 的名称调用，并可通过 Microsoft Azure 和 Amazon Bedrock 获取，标准 API 定价为每百万输入 token 10 美元、每百万输出 token 50 美元。该公告本身内容简短，未详细说明具体的数据提供商、合规认证或金融服务层级的定价。

rss · OpenAI Blog · Sep 10, 07:00

**背景**: GPT-6 Astra 是 OpenAI 的下一代旗舰模型，接替此前的 GPT 版本，主打面向工作的任务，例如生成格式正确的演示文稿。ChatGPT for Financial Services 建立在 OpenAI 向垂直企业产品扩展的整体战略之上，此前它已推出 ChatGPT 个人理财体验，允许用户连接自己的金融账户。由于监管和数据安全方面的顾虑，金融机构历来对生成式 AI 的采用较为谨慎。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-chatgpt-financial-services/">Introducing ChatGPT for Financial Services | OpenAI</a></li>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT - 6 Astra : A new generation of intelligence | OpenAI</a></li>
<li><a href="https://openai.com/index/personal-finance-chatgpt/">A new personal finance experience in ChatGPT | OpenAI</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#ChatGPT`, `#Financial Services`, `#GPT-6`, `#Enterprise AI`

---

<a id="item-4"></a>
## [trynix.dev 借助 qemu-wasm 在浏览器中启动任意 Nix 包](https://simonwillison.net/2026/Sep/10/trynix/) ⭐️ 8.0/10

Farid Zakaria 发布了 trynix.dev，他称之为自己在 Nix 领域的“代表作”。该项目利用 qemu-wasm 在浏览器内完整运行一个 x86_64 Linux 虚拟机，并能启动过去 13 年间的任意 Nix 包。这些包可通过 URL 直接寻址，访问 https://trynix.dev/?pkg=python3%403.6.2 并点击“Load”即可获得一个运行 2017 年 Python 3.6.2 的交互式 shell；配套的 GitHub Action 名为 trynix-preview，会在 Pull Request 上评论一个可启动链接。 这让历史版本和可复现的软件环境只需一个浏览器就能即时访问，对可复现性研究、软件考古以及代码审查流程都具有重要意义。同时它也表明基于 WebAssembly 的虚拟化已相当成熟，因为完整的 x86_64 虚拟机如今可以在客户端运行，无需任何服务器基础设施。 该虚拟机由 ktock 的 qemu-wasm 项目驱动，该项目将 QEMU 编译为 WebAssembly；包通过简单的查询参数寻址，例如 ?pkg=python3%403.6.2。trynix-preview 这个 GitHub Action 不需要服务器，只需要浏览器，而且该方法覆盖了大约 13 年历史中的 Nix 包。

rss · Simon Willison · Sep 10, 23:44

**背景**: Nix 是一个纯函数式包管理器，以可复现构建和声明式系统配置著称，其 Nixpkgs 集合收录了跨多个版本的大量软件包。WebAssembly（Wasm）是一种面向栈式虚拟机的可移植二进制指令格式，能让程序以接近原生的速度在浏览器中运行；qemu-wasm 则将 QEMU 模拟器编译为 WebAssembly，使完整的 Linux 虚拟机可以在网页内执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ktock/qemu-wasm">GitHub - ktock/ qemu - wasm : QEMU on browser · GitHub</a></li>
<li><a href="https://nixos.org/">Nix & NixOS | Declarative builds and deployments</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Nix`, `#WebAssembly`, `#qemu`, `#reproducibility`, `#browser`

---

<a id="item-5"></a>
## [Shopify 因 AI 智能体回归原生移动开发](https://simonwillison.net/2026/Sep/10/shopify-react-native/) ⭐️ 8.0/10

Shopify 宣布将其移动应用从 React Native 迁回分别使用 Swift（iOS）和 Kotlin（Android）的原生代码库，推翻了其在 2020 年做出的决定。该公司表示，AI 智能体现在能够承担足够多的实现、翻译、测试和审查工作，因此维护两个原生平台不再是决定性的成本因素。 这是一个值得关注的案例：一家大型公司因为 AI 编程智能体改变了底层成本计算，而推翻了被广泛效仿的架构决策。如果其他大型工程组织跟进，这可能标志着跨平台框架的退潮，并重塑移动团队的组建与组织方式。 Shopify 维护着三个重要的 React Native 库：react-native-skia、flash-list 和 restyle。前两个正在移交给新的维护者，而用户基数较小的 restyle 将于 2026 年底归档。

rss · Simon Willison · Sep 10, 21:11

**背景**: React Native 是 Meta 推出的基于 JavaScript 的框架，允许开发者用基本相同的代码库构建原生渲染的 iOS 和 Android 应用，这正是 Shopify 在 2020 年采用它以避免重复开发功能的原因。原生开发则意味着分别用 Swift（苹果用于 iOS 和 macOS 的语言）和 Kotlin（JetBrains 用于 Android 的语言）编写独立应用。AI 编程智能体是能够自主编写、翻译、测试和审查代码的工具，有可能降低跨平台重复工作的成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://reactnative.dev/">React Native</a></li>
<li><a href="https://www.swift.org/">Swift Programming Language</a></li>
<li><a href="https://kotlinlang.org/">Kotlin Programming Language</a></li>

</ul>
</details>

**标签**: `#React Native`, `#Mobile Development`, `#AI Agents`, `#Shopify`, `#Software Engineering`

---

<a id="item-6"></a>
## [Cloudflare 1.1.1.1 解析器新增后量子 DNSSEC 支持](https://blog.cloudflare.com/post-quantum-dnssec-1111/) ⭐️ 8.0/10

Cloudflare 宣布其公共 DNS 解析器 1.1.1.1 现已支持使用 NIST 的后量子算法 ML-DSA-44 来验证 DNSSEC 签名，这些签名的大小达到 2,420 字节。该博客文章详细介绍了 Cloudflare 如何大规模处理这些大尺寸签名并缓解降级风险。 这是使 DNS 基础设施能够抵御未来量子计算机攻击的重要一步，因为 DNSSEC 目前依赖可能被量子计算机破解的经典算法。它影响所有使用 1.1.1.1 的用户，并为其他 DNS 解析器采用后量子密码学树立了先例。 ML-DSA-44 签名大小为 2,420 字节，远大于传统 DNSSEC 签名，可能导致分片并需要谨慎处理。Cloudflare 还解决了降级风险，即攻击者可能强制回退到较弱的算法。

rss · Cloudflare Blog · Sep 10, 13:00

**背景**: DNSSEC（域名系统安全扩展）是一组为 DNS 记录添加加密签名以防止欺骗的扩展。后量子密码学是指设计用于抵御量子计算机攻击的算法，因为量子计算机可能破解广泛使用的公钥算法如 RSA 和 ECC。ML-DSA-44 是 NIST 标准化的后量子数字签名算法，前身为 Dilithium。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ietf.org/ietf-ftp/internet-drafts/draft-sheth-pqc-dnssec-strategy-01.html">Post - Quantum Cryptography Strategy for DNSSEC</a></li>
<li><a href="https://dn.org/quantum‑safe-cryptography-and-future-dnssec-algorithms/">Quantum ‑Safe Cryptography and Future DNSSEC Algorithms – DN.org</a></li>
<li><a href="https://oneuptime.com/blog/post/2026-01-15-protect-dnssec-downgrade-attacks/view">How to Protect Against DNSSEC Downgrade Attacks</a></li>

</ul>
</details>

**标签**: `#post-quantum`, `#DNSSEC`, `#Cloudflare`, `#cryptography`, `#DNS`

---

<a id="item-7"></a>
## [研究人员利用 Codex 和 ChatGPT 挖掘基因组以寻找新型抗菌分子](https://openai.com/index/using-codex-chatgpt-to-search-for-new-antimicrobials) ⭐️ 7.0/10

César de la Fuente 的实验室正在使用 OpenAI 的 Codex 和 ChatGPT，从现存及已灭绝生物的基因组中搜索能够对抗耐药感染的抗菌候选分子。这一案例研究发布在 OpenAI 博客上，展示了 AI 编程与语言工具如何被直接应用于现实世界的科学发现工作流程。 抗菌素耐药性是一场日益严重的全球健康危机，而传统药物发现流程的速度远远跟不上需求。这一案例表明，AI 工具可以加速新型抗菌候选分子的识别，并有可能激励其他研究实验室采用类似的 AI 驱动方法。 该实验室使用 Codex 进行代码生成，使用 ChatGPT 进行推理和数据分析，以挖掘基因组数据，包括来自已灭绝生物的序列。尽管基因组挖掘和 AI 已经加速了抗菌肽的发现，但仍存在挑战，例如数据集有限、毒性被忽视以及翻译后修饰未被充分考虑。

rss · OpenAI Blog · Sep 10, 16:00

**背景**: 抗菌素耐药性是指细菌进化出对抗生素的防御能力，使感染更难治疗。基因组挖掘是一种扫描 DNA 序列以寻找可能产生抗菌化合物（如抗菌肽）的基因的技术。OpenAI 的 Codex 是专门用于生成和理解代码的 AI 模型，而 ChatGPT 是用于推理和分析的对话式 AI 模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/codex/">Codex | AI Coding Partner from OpenAI | OpenAI</a></li>
<li><a href="https://www.news-medical.net/news/20260406/AI-helps-researchers-find-antimicrobial-peptides-in-Earthe28099s-harshest-habitat.aspx?trk=article-ssr-frontend-pulse_little-text-block">AI helps researchers find antimicrobial peptides in Earth’s harshest...</a></li>
<li><a href="https://www.drugdiscoverynews.com/antimicrobial-resistance-the-silent-pandemic-15271">Antimicrobial resistance : The silent pandemic | Drug Discovery News</a></li>

</ul>
</details>

**标签**: `#AI for science`, `#drug discovery`, `#antimicrobial resistance`, `#Codex`, `#ChatGPT`

---

<a id="item-8"></a>
## [OpenAI 在 ChatGPT Work 中推出数据智能体](https://openai.com/index/put-data-to-work) ⭐️ 7.0/10

OpenAI 在 ChatGPT Work 中推出了一个数据智能体（Data agent），让用户能够连接公司数据、发现洞察，并使用自然语言构建交互式仪表板。该功能被定位为让组织中的任何人都能在无需专业分析技能的情况下把数据用起来。 这标志着 OpenAI 从通用聊天显著扩展到企业商业智能与分析领域，将与成熟的 BI 工具以及新兴的自然语言生成仪表板产品展开竞争。它可能改变企业与其数据交互的方式，降低非技术员工生成报告和仪表板的门槛。 该数据智能体是 ChatGPT Work 的一部分，核心在于连接公司数据源并通过自然语言提示生成交互式仪表板。OpenAI 将其定位为产品扩展而非基础研究突破，公告中对支持的数据连接器、定价和可用性的细节较为有限。

rss · OpenAI Blog · Sep 10, 15:00

**背景**: 商业智能（BI）传统上需要专门的工具和技能来查询数据库并构建仪表板。近年来大语言模型的进步催生了自然语言界面，让用户可以直接向数据提问并自动生成图表和报告，这一领域目前正面临来自 RowSpeak、Lark 以及集成 Odoo 的 AI 仪表板等厂商的竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rowspeak.ai/">Excel AI for Data Analysis, Charts, Reports & Dashboards - RowSpeak</a></li>
<li><a href="https://www.larksuite.com/en_us/blog/ai-dashboard">AI dashboard : Visualize, analyze and optimize with AI | Lark</a></li>
<li><a href="https://www.braincuber.com/ai-dashboard">AI Dashboard for Odoo | Braincuber Technologies</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#ChatGPT`, `#Enterprise AI`, `#Data Analytics`, `#Natural Language Interfaces`

---

<a id="item-9"></a>
## [OpenAI 与 GSA 合作扩大美国政府 AI 访问](https://openai.com/index/expanding-ai-access-us-government) ⭐️ 7.0/10

OpenAI 与美国总务管理局（GSA）宣布合作，为符合条件的联邦、州、地方和部落政府提供 0 美元许可费、50%的使用折扣以及扩展的网络防御支持。该计划旨在使 OpenAI 的 AI 工具更易于公共部门实体使用。 这一合作显著降低了政府机构采用先进 AI 的成本障碍，可能加速 AI 在公共服务和网络安全中的整合。它反映了 AI 公司战略性地进入公共部门以影响政府技术采用的更广泛趋势。 该优惠包括为符合条件的政府实体提供 0 美元许可费和 50%的使用折扣，以及扩展的网络防御支持。这建立在 OpenAI 现有的政府 focused 举措如 ChatGPT Gov 的基础上。

rss · OpenAI Blog · Sep 10, 07:00

**背景**: 美国总务管理局（GSA）是一家负责管理政府采购和共享服务的联邦机构。OpenAI 一直在扩展其政府产品，包括 ChatGPT Gov，这是其 AI 的一个版本，专为政府机构设计，以简化对前沿模型的访问。这一合作是 AI 公司与政府合作以负责任和安全地部署 AI 的日益增长趋势的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/expanding-ai-access-us-government/">Expanding AI access and cyber defense for federal, state... | OpenAI</a></li>
<li><a href="https://openai.com/global-affairs/introducing-chatgpt-gov/">Introducing ChatGPT Gov | OpenAI</a></li>
<li><a href="https://openai.com/solutions/industries/government/">Solutions for government | OpenAI</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#government`, `#AI access`, `#cyber defense`, `#public sector`

---

<a id="item-10"></a>
## [Unit 42 揭示通过 Kubernetes 节点 root 权限滥用 SPIFFE/SPIRE 身份](https://unit42.paloaltonetworks.com/kubernetes-spiffe-spire-identity-spoofing/) ⭐️ 7.0/10

Palo Alto Networks 的 Unit 42 发布了一篇技术深度分析，详细说明了在攻陷的 Kubernetes 节点上拥有 root 权限的攻击者如何滥用 SPIFFE/SPIRE 元数据来伪造和窃取同节点工作负载的身份。该攻击利用 cgroup 操纵，诱骗 SPIRE agent 的 Workload API 将恶意进程认证为合法工作负载。 SPIFFE/SPIRE 是 CNCF 毕业标准，广泛部署于 Kubernetes 和云原生环境中，用短期密码学身份替代长期密钥，因此这一后渗透技术动摇了防御者的核心信任假设。它表明节点级失陷可能悄然升级为跨同节点工作负载的身份窃取，影响任何依赖 SPIRE 实现零信任工作负载身份的组织。 该攻击通过让恶意进程请求 SPIRE agent 的 Workload API 来实施；agent 读取被伪造的 cgroup 数据并判定其与目标工作负载匹配，从而实现身份伪造和窃取。该技术要求攻击者在节点上拥有 root 权限，并针对将工作负载绑定到其身份的认证机制。

rss · Palo Alto Unit 42 · Sep 10, 10:00

**背景**: SPIFFE（Secure Production Identity Framework for Everyone）是一项开放标准，用于在动态云环境中为工作负载提供密码学身份，而不依赖网络位置，SPIRE 是其参考实现。在 Kubernetes 中，SPIRE agent 运行在节点上并对工作负载身份进行认证，通常使用 cgroup 等内核级元数据来验证发出请求的工作负载。这一设计假设节点及其内核元数据是可信的，而一旦攻击者获得 root 权限，该假设便不再成立。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://unit42.paloaltonetworks.com/kubernetes-spiffe-spire-identity-spoofing/">The Machine With Many Faces: Post-Exploitation Identity Misuse in...</a></li>
<li><a href="https://cyber.netsecops.io/articles/post-exploitation-identity-misuse-in-spiffe-spire-on-kubernetes/">Unit 42 Details Post-Exploitation Identity Spoofi... - CyberNetSec.io</a></li>
<li><a href="https://spiffe.io/">SPIFFE | Secure Production Identity Framework for Everyone</a></li>

</ul>
</details>

**标签**: `#Kubernetes`, `#SPIFFE/SPIRE`, `#Cloud Security`, `#Post-Exploitation`, `#Identity Spoofing`

---

<a id="item-11"></a>
## [为 AI 供电本质上是架构问题，而非单纯的能源问题](https://www.technologyreview.com/2026/09/10/1141649/powering-ai-is-an-architecture-problem/) ⭐️ 7.0/10

2026 年 7 月 22 日，位于全球最大数据中心集群所在地弗吉尼亚州阿什本的输电线路发生故障，数秒内从电网中切除了超过 3 吉瓦的负荷；两年前也发生过类似事件，一次性导致约 60 个弗吉尼亚设施和 1500 兆瓦负荷脱网。MIT Technology Review 认为，这些反复出现的电网扰动表明，为 AI 供电本质上是一个架构问题，需要重新思考能源基础设施。 随着 AI 数据中心向阿什本“数据中心走廊”这类超大规模枢纽集中，单一故障就可能引发近乎同时的备用电源切换，并在东部互联电网中传播频率和电压扰动。这会影响 PJM 等电网运营商、超大规模数据中心运营方，并最终影响依赖这些设施的 AI 服务的可靠性。 7 月 22 日的事件中，超大规模设施自动切换到备用电源，导致超过 3 吉瓦的需求在数秒内从 PJM 电网中消失；而更早的事故则源于单个浪涌保护器失效，造成约 1500 兆瓦负荷脱落。这些事件凸显出数据中心负荷转移的速度和规模可能比传统规划假设更快地破坏电网稳定。

rss · MIT Technology Review AI · Sep 10, 11:00

**背景**: 浪涌保护器是一种保护装置，可将过高的电压导入大地，以保护敏感电气设备免受雷击和操作过电压的影响；一旦失效，它就无法再发挥这一功能，并可能引发更大范围的停电。弗吉尼亚州阿什本被称为“数据中心走廊”，拥有全球最密集的数据中心，而 PJM 是运营该地区电网的区域输电组织。由于 AI 工作负载需要巨大且集中的电力，数据中心备用系统与电网稳定性之间的相互作用已成为核心基础设施问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.datacenterknowledge.com/outages/fault-in-data-center-alley-triggered-3-gw-load-drop-on-pjm">Fault in Data Center Alley Triggered 3 GW Load Drop</a></li>
<li><a href="https://www.tingfire.com/blog/what-happened-when-3-gigawatt-of-data-center-demand-disappeared-from-the-grid/">What Happened When 3 Gigawatts of Data - Center Demand...</a></li>
<li><a href="https://www.electricalindia.in/selection-application-of-surge-arrester/">Selection & Application Of Surge Arrester | Electrical India Magazine</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#data centers`, `#power grid`, `#energy`, `#architecture`

---

