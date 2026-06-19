# Horizon 每日速递 - 2026-06-19

> From 61 items, 17 important content pieces were selected

---

1. [发现 1 万个 GitHub 仓库分发木马恶意软件](#item-1) ⭐️ 9.0/10
2. [CISA 敦促加固 Fortinet 设备应对凭证泄露](#item-2) ⭐️ 9.0/10
3. [厂商签名的 UEFI 应用可绕过安全启动](#item-3) ⭐️ 9.0/10
4. [强制同意投诉导致 Elkjop 被罚 180 万欧元](#item-4) ⭐️ 8.0/10
5. [医院和大学以 90%更低成本重新利用药物](#item-5) ⭐️ 8.0/10
6. [Modos 彩色电子纸显示器达到 60Hz 刷新率](#item-6) ⭐️ 8.0/10
7. [Popa 僵尸网络与以色列上市公司关联](#item-7) ⭐️ 8.0/10
8. [OpenAI 推理模型助力罕见儿童遗传病诊断](#item-8) ⭐️ 8.0/10
9. [Ubiquiti 推出基于 ZFS 的企业级 NAS](#item-9) ⭐️ 7.0/10
10. [康奈尔 CS 6120 高级编译器课程上线自学版](#item-10) ⭐️ 7.0/10
11. [新工具检测 LLM 对你名字的识别程度](#item-11) ⭐️ 7.0/10
12. [超越 .gitignore：Git 的其他忽略机制](#item-12) ⭐️ 7.0/10
13. [W Social：欧洲数字主权还是政治作秀？](#item-13) ⭐️ 7.0/10
14. [Gerrymandle：每日解谜游戏教你选区划分](#item-14) ⭐️ 7.0/10
15. [Emacs 31 预览：Tree-sitter、原生编译、Eglot](#item-15) ⭐️ 7.0/10
16. [新版 Outlook 启动需 10 秒，经典版瞬间打开](#item-16) ⭐️ 7.0/10
17. [Datasette Apps：在 Datasette 内运行沙盒化 HTML/JS 应用](#item-17) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [发现 1 万个 GitHub 仓库分发木马恶意软件](https://orchidfiles.com/github-repositories-distributing-malware/) ⭐️ 9.0/10

一名安全研究人员发现超过 1 万个 GitHub 仓库正在主动分发木马恶意软件，这些仓库针对的是自动化代理和依赖系统，而非人类用户。 这种大规模供应链攻击对开源生态系统构成重大威胁，因为自动化工具和 CI/CD 流水线可能在不知情的情况下拉取恶意代码，导致广泛感染。 这些仓库克隆新项目并频繁删除和推送提交以保持在搜索结果中的可见性，利用自动化代理获取依赖。该活动可能针对即将到来的重大选举。

hackernews · theorchid · Jun 18, 11:45 · [社区讨论](https://news.ycombinator.com/item?id=48583928)

**背景**: 开源中的供应链攻击利用了对第三方依赖的信任。攻击者创建看似合法的恶意包或仓库，诱骗自动化系统将其纳入。依赖混淆攻击是一种常见变体，攻击者发布与内部包名称相似的包。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/orchidfiles/i-discovered-a-large-scale-malware-distribution-campaign-on-github-4m6o">I discovered a large-scale malware distribution campaign on GitHub</a></li>
<li><a href="https://thepixelspulse.com/posts/github-malware-repositories-lessons/">10,000 GitHub Malware Repositories: What They Showed Us</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，该攻击针对的是自动化代理而非人类，频繁删除提交可使仓库保持在“最近更新”搜索的顶部。一些用户报告他们的名字被附加到未知项目上，突显了冒充问题。

**标签**: `#malware`, `#supply chain security`, `#GitHub`, `#open source`, `#cybersecurity`

---

<a id="item-2"></a>
## [CISA 敦促加固 Fortinet 设备应对凭证泄露](https://www.cisa.gov/news-events/alerts/2026/06/18/cisa-urges-hardening-fortinet-devices-after-reports-credential-exposure) ⭐️ 9.0/10

CISA 于 2026 年 6 月 18 日发布紧急公告，警告恶意行为者已从约 74,000 台可公开访问的 Fortinet 设备（包括防火墙和 SSL VPN 网关）中窃取凭证，此活动被称为 FortiBleed。 此次大规模凭证泄露影响全球政府及私营机构，可能使攻击者获得对关键网络的持久访问权限。CISA 建议的加固措施对于缓解即时风险并防止进一步利用至关重要。 CISA 建议立即采取五项行动：终止会话并重置凭证、强制使用 PBKDF2 存储凭证、审查日志以发现可疑活动、启用抗钓鱼多因素认证，以及通过将管理接口限制在可信网络来减少攻击面。

rss · CISA Cybersecurity Advisories · Jun 18, 12:00

**背景**: Fortinet FortiGate 设备广泛用于企业和政府网络中的防火墙和 VPN 网关。FortiBleed 活动据称暴露了超过 73,000 台设备的凭证，其中约一半面向互联网。PBKDF2 是一种基于密码的密钥派生函数，可增强凭证存储以抵御暴力破解攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.locker.io/en/locker-whitepaper/security-fundamentals/password-based-key-derivation-function-2">Locker Support | Password - based Key Derivation Function 2</a></li>
<li><a href="https://8thlight.com/insights/taking-password-storage-up-a-notch">Taking Password Storage Up A Notch | 8th Light</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#CISA`, `#Fortinet`, `#VPN`, `#credential exposure`

---

<a id="item-3"></a>
## [厂商签名的 UEFI 应用可绕过安全启动](https://kb.cert.org/vuls/id/457458) ⭐️ 9.0/10

多个厂商签名的 UEFI 应用程序（包括 Acer、AMD、华硕等厂商的 GRUB2 和 UEFI shell）存在漏洞，可被用于 BYOVD 式攻击绕过安全启动，在操作系统初始化前执行任意代码。 该漏洞破坏了安全启动这一现代系统的关键安全机制，使攻击者能够部署绕过操作系统防御的持久性恶意软件或内核 rootkit，影响范围涉及多个厂商的广泛设备。 受影响的二进制文件将被添加到特定厂商的 DBX 撤销列表中以防止执行。ESET 的研究人员发现了这些漏洞，涉及能够操作系统内存或 NVRAM 变量但缺乏适当访问控制的 UEFI 应用程序。

rss · CERT CC Vulnerability Notes · Jun 18, 19:41

**背景**: UEFI 安全启动确保系统启动时仅执行经过加密签名的固件和引导加载程序。禁止签名数据库（DBX）维护了一个已撤销签名的黑名单。BYOVD（自带易受攻击驱动程序）攻击利用带有漏洞的合法签名驱动程序来执行恶意代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kb.cert.org/vuls/id/457458">VU#457458 - Vendor-signed UEFI applications found vulnerable to...</a></li>
<li><a href="https://www.securityweek.com/flaw-in-industrial-computer-makers-uefi-apps-enables-secure-boot-bypass-on-many-devices/">Flaw in Industrial Computer Maker's UEFI Apps Enables Secure Boot ...</a></li>
<li><a href="https://blog.hansenpartnership.com/the-meaning-of-all-the-uefi-keys/">The Meaning of all the UEFI Keys | James Bottomley's random Pages</a></li>

</ul>
</details>

**标签**: `#security`, `#UEFI`, `#Secure Boot`, `#vulnerability`, `#BYOVD`

---

<a id="item-4"></a>
## [强制同意投诉导致 Elkjop 被罚 180 万欧元](https://www.thatprivacyguy.com/blog/elkjop-forced-consent-fine/) ⭐️ 8.0/10

一位隐私倡导者在 2021 年投诉 Elkjop 将同意营销作为客户俱乐部会员的条件，导致挪威数据保护局（Datatilsynet）在 2026 年对其处以 180 万欧元罚款。 此案表明 GDPR 对强制同意的禁令可通过巨额罚款执行，警示那些将同意与服务捆绑的公司，并赋予个人挑战非法数据实践的力量。 罚款为 2000 万挪威克朗（约 180 万欧元），监管机构认定 Elkjop 违反 GDPR 第 7 条第 4 款，将同意营销作为加入客户俱乐部的条件。投诉人早在五年前就警告过该公司。

hackernews · speckx · Jun 18, 18:31 · [社区讨论](https://news.ycombinator.com/item?id=48589501)

**背景**: GDPR（通用数据保护条例）是欧盟保护个人数据和隐私的法律。第 7 条第 4 款特别禁止将同意数据处理作为获取服务的条件，除非该处理对于服务是必要的。强制同意发生在公司要求用户同意非服务必需的数据使用时。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.thatprivacyguy.com/blog/elkjop-forced-consent-fine/">I told them forced consent was unlawful. Five years later it cost Elkjop ...</a></li>
<li><a href="https://news.ycombinator.com/item?id=48589501">I told them forced consent was unlawful. 5 years later it cost Elkjop ...</a></li>
<li><a href="https://gdpr-info.eu/">General Data Protection Regulation ( GDPR ) – Legal Text</a></li>

</ul>
</details>

**社区讨论**: 评论者对结果表示满意，指出抵制强制同意的重要性。有人分享了挪威语官方决定和英文翻译的链接，还有人强调了求职申请隐私政策中的类似问题。

**标签**: `#GDPR`, `#privacy`, `#data protection`, `#consent`, `#regulation`

---

<a id="item-5"></a>
## [医院和大学以 90%更低成本重新利用药物](https://www.kcl.ac.uk/news/hospitals-and-universities-repurposing-drugs-at-90-lower-cost) ⭐️ 8.0/10

医院和大学正在以极低的成本将现有药物重新用于新适应症，与品牌药相比，价格通常降低 90%或更多。 这挑战了传统的药品定价模式，提高了患者获得可负担治疗的机会，尤其对于罕见病和新药开发不经济的疾病。 例如，Avastin（贝伐珠单抗）用于黄斑变性的每剂成本约 50 美元，而类似药物 Lucentis 每剂约 1500 美元。然而，重新利用面临监管障碍，因为没有简化的途径可以在未经制造商同意的情况下扩展已批准的用途。

hackernews · giuliomagnifico · Jun 18, 10:33 · [社区讨论](https://news.ycombinator.com/item?id=48583386)

**背景**: 药物重新利用是指为现有已批准药物寻找新用途，与开发新药相比，可显著缩短开发时间并降低成本。在 COVID-19 疫情期间，重新利用获得了新的关注。然而，制药公司通常对现有药物进行微小修改以获得新专利，例如 esketamine（Spravato）与氯胺酮的情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC9336118/">Drug repurposing : a systematic review on root causes, barriers and...</a></li>
<li><a href="https://www.iqvia.com/blogs/2022/05/drug-repurposing-basics">Drug Repurposing Basics | IQVIA</a></li>

</ul>
</details>

**社区讨论**: 评论者强调了现实中的例子，如 Avastin 与 Lucentis、esketamine 与氯胺酮，指出了制药激励体系的系统性问题。一些人表示支持像 Cures Within Reach 这样的非营利组织，它们资助罕见病的药物重新利用研究。

**标签**: `#healthcare`, `#drug repurposing`, `#pharmaceutical pricing`, `#biomedical research`

---

<a id="item-6"></a>
## [Modos 彩色电子纸显示器达到 60Hz 刷新率](https://spectrum.ieee.org/modos-e-paper-monitor) ⭐️ 8.0/10

两人初创公司 Modos 正在开发 Modos Flow，这是一款 13.3 英寸彩色电子纸显示器，分辨率 3200x2400，刷新率 60Hz，支持触摸输入，由名为 Enchanter 的定制 FPGA 控制器实现。 这标志着电子纸技术的重大飞跃，使彩色电子墨水显示器可用于网页浏览和视频播放等通用计算任务，与传统 LCD/OLED 显示器相比，可能减少眼睛疲劳和功耗。 该显示器采用 Carta 彩色电子纸面板，通过 FPGA 驱动的局部刷新技术实现 60Hz 刷新率。单色版售价 619 美元，彩色版售价 719 美元，于 2026 年 5 月 27 日在 Crowd Supply 上发起众筹。

hackernews · Vinnl · Jun 18, 11:41 · [社区讨论](https://news.ycombinator.com/item?id=48583897)

**背景**: 电子纸显示器（如 E Ink 的产品）以超低功耗和阳光下可读性著称，但传统上刷新率低且色彩有限。大多数电子纸显示器为单色，刷新率低于 10Hz，不适合动态内容。Modos Flow 旨在通过定制控制器实现更快的局部更新，克服这些限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://spectrum.ieee.org/modos-e-paper-monitor">Modos Color Monitor Pushes E - Paper Displays... - IEEE Spectrum</a></li>
<li><a href="https://thequantumdispatch.com/articles/modos-flow-fpga-color-e-paper-monitor-13-inch-touchscreen-crowd-supply-may-27-2026">Modos Flow Launches on Crowd Supply... — The Quantum Dispatch</a></li>
<li><a href="https://news.ycombinator.com/item?id=48583897">Modos Color Monitor Pushes E - Paper Displays Further | Hacker News</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区对这一技术成就表示兴奋，一些用户担心高刷新率下面板的寿命。其他人则注意到 RLCD 和电子纸等替代显示技术有望实现户外可用、电池高效的设备。

**标签**: `#e-paper`, `#display technology`, `#hardware`, `#startup`, `#monitor`

---

<a id="item-7"></a>
## [Popa 僵尸网络与以色列上市公司关联](https://krebsonsecurity.com/2026/06/popa-botnet-linked-to-publicly-traded-israeli-firm/) ⭐️ 8.0/10

研究人员将“Popa”Android 僵尸网络与 NetNut 关联，NetNut 是上市公司 Alarum Technologies Ltd（纳斯达克：ALAR）旗下的住宅代理服务，该僵尸网络已感染数百万台电视盒用于广告欺诈和数据抓取。 这一关联揭示了一家合法上市公司可能从网络犯罪基础设施中获利，引发了对企业责任和住宅代理行业道德问题的严重质疑。 Popa 僵尸网络已活跃四年，强迫受感染的 Android 电视盒转发流量用于广告欺诈、账户接管和大规模数据抓取。NetNut 自称提供超过 8500 万个住宅代理。

rss · Krebs on Security · Jun 18, 17:37

**背景**: 僵尸网络是由攻击者远程控制的受感染设备网络。住宅代理通过真实家庭 IP 地址路由流量，使恶意活动看起来合法。NetNut 是主要的住宅代理提供商，其母公司 Alarum Technologies 在纳斯达克上市。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://netnut.io/">NetNut - High Quality Proxies Network For Web Data Collection</a></li>
<li><a href="https://finance.yahoo.com/quote/ALAR/">Alarum Technologies Ltd. (ALAR) Stock Price, News... - Yahoo Finance</a></li>
<li><a href="https://github.com/topics/android-trojan">android -trojan · GitHub Topics · GitHub</a></li>

</ul>
</details>

**标签**: `#botnet`, `#Android`, `#security`, `#ad fraud`, `#residential proxy`

---

<a id="item-8"></a>
## [OpenAI 推理模型助力罕见儿童遗传病诊断](https://openai.com/index/diagnose-rare-childhood-diseases) ⭐️ 8.0/10

研究人员使用 OpenAI 推理模型重新分析了未确诊的儿童罕见遗传病病例，发现了 18 个此前遗漏的新诊断。 所用模型是 OpenAI 的推理模型（可能是 o3 或 o4-mini），能够分析基因组数据和临床信息，识别致病基因变异。

rss · OpenAI Blog · Jun 18, 08:00

**背景**: 罕见遗传病常因致病基因变异难以识别而多年无法确诊。随着新知识出现，对已有基因组数据进行重新分析也颇具挑战。AI 推理模型能整合多源数据，自动加速这一过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/diagnose-rare-childhood-diseases/">Using AI to help physicians diagnose rare genetic diseases ... | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_o3">OpenAI o3 - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/pulse/speeding-diagnosis-rare-genetic-disorders-help-monica-bertagnolli-x0sme">Speeding the Diagnosis of Rare Genetic Disorders with the Help of...</a></li>

</ul>
</details>

**标签**: `#AI`, `#healthcare`, `#rare diseases`, `#diagnosis`, `#OpenAI`

---

<a id="item-9"></a>
## [Ubiquiti 推出基于 ZFS 的企业级 NAS](https://blog.ui.com/article/introducing-enterprise-nas) ⭐️ 7.0/10

Ubiquiti 发布了企业级 NAS（ENAS），这是一款基于 ZFS 文件系统的网络附加存储设备，无重复许可费用，并集成了 UniFi 管理。 这标志着 Ubiquiti 进入企业存储市场，提供无许可费用的 ZFS 解决方案，可能对 QNAP 和 Synology 等老牌厂商构成挑战，尤其对已投资 UniFi 生态的用户。 ENAS 配备双 25 Gigabit SFP28 端口、冗余电源，支持 PB 级扩展和多站点备份编排。但社区成员质疑机械硬盘能否饱和 25GbE 链路。

hackernews · ksec · Jun 18, 14:24 · [社区讨论](https://news.ycombinator.com/item?id=48585866)

**背景**: ZFS 是一种先进的文件系统和逻辑卷管理器，以数据完整性、快照和高效复制等特性著称。Ubiquiti 主要以网络设备闻名，其软件可靠性在社区中一直存在争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.ui.com/article/introducing-enterprise-nas">Introducing Enterprise NAS , Built on ZFS</a></li>
<li><a href="https://news.ycombinator.com/item?id=48585866">Ubiquiti : Enterprise NAS , Built on ZFS | Hacker News</a></li>
<li><a href="https://docs.freebsd.org/en/books/handbook/zfs/">Chapter 22. The Z File System ( ZFS ) | FreeBSD Documentation Portal</a></li>

</ul>
</details>

**社区讨论**: 社区意见不一：一些人称赞无重复费用和采用 ZFS，而另一些人则对 Ubiquiti 的软件质量和过去的安全事件表示担忧，有用户称其为企业环境中的“生产测试版”。

**标签**: `#Ubiquiti`, `#NAS`, `#ZFS`, `#enterprise storage`, `#hardware`

---

<a id="item-10"></a>
## [康奈尔 CS 6120 高级编译器课程上线自学版](https://www.cs.cornell.edu/courses/cs6120/2025fa/self-guided/) ⭐️ 7.0/10

康奈尔大学的 CS 6120 高级编译器课程现已作为免费自学在线资源开放，涵盖经典和现代编译器技术。 这为全球学习者提供了高质量的编译器教育，填补了免费在线课程中高级主题的空白。 课程涵盖死代码消除、数据流分析、SSA 形式及动态编译等主题，但社区反馈指出追踪编译并非重点方向。

hackernews · ibobev · Jun 18, 11:04 · [社区讨论](https://news.ycombinator.com/item?id=48583606)

**背景**: 编译器将高级编程语言翻译成机器代码。高级编译器课程通常涵盖优化技术和运行时系统，建立在编译器入门概念之上。

**社区讨论**: 社区评论批评课程对追踪编译的侧重已过时，认为类型反馈、推测和去优化更为重要。也有人质疑死代码消除等主题是否真正属于高级内容。

**标签**: `#compilers`, `#education`, `#programming languages`, `#systems`

---

<a id="item-11"></a>
## [新工具检测 LLM 对你名字的识别程度](https://www.intheweights.com/) ⭐️ 7.0/10

新网站 intheweights.com 允许用户通过并行查询多个模型并聚类响应，检查前沿和小型 LLM 从训练数据中识别其姓名或身份的程度。 该工具揭示了个人数据嵌入 LLM 训练集的程度，引发了关于隐私、同意以及个人在 AI 模型中可追溯性的重要问题。 该网站并行查询前沿和小型模型，聚类响应，并提供识别分数。它使用多种模型，包括大规模和较小的开源模型，以比较识别强度。

hackernews · Hacker News Show HN · Jun 18, 20:49 · [社区讨论](https://news.ycombinator.com/item?id=48591348)

**背景**: 大型语言模型（LLM）在来自互联网的大量文本数据上训练，这些数据可能包含个人信息。术语“权重”指神经网络中编码学习模式的数值参数。前沿模型是大型、最先进的模型，而小型 LLM 则更紧凑高效。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.breakthroughpursuit.com/small-models-big-wins-when-to-prefer-task-specific-over-frontier/">Small Models, Big Wins: When to Prefer Task‑Specific over Frontier</a></li>
<li><a href="https://www.geeksforgeeks.org/deep-learning/the-role-of-weights-and-bias-in-neural-networks/">Weights and Bias in Neural Networks - GeeksforGeeks</a></li>

</ul>
</details>

**社区讨论**: 社区评论反应不一：一些用户觉得该工具很有趣并分享结果，而另一些则对提交真实姓名表示隐私担忧。一位用户指出该工具可用于将姓名与 IP 地址关联，另一位则强调了数据未经同意被使用的问题。

**标签**: `#LLM`, `#privacy`, `#training data`, `#web tool`, `#AI`

---

<a id="item-12"></a>
## [超越 .gitignore：Git 的其他忽略机制](https://nelson.cloud/.gitignore-isnt-the-only-way-to-ignore-files-in-git/) ⭐️ 7.0/10

文章解释了 Git 除了常见的 .gitignore 文件之外，还提供了其他忽略文件的方法，包括全局排除（每用户忽略规则）和用于忽略差异的 .gitattributes。 了解这些替代方法有助于开发者避免用个人或特定环境的条目污染项目的 .gitignore 文件，从而保持仓库整洁并减少意外提交。 全局排除在 ~/.config/git/ignore 中配置，按用户应用于所有仓库；而 .gitattributes 可以将某些文件标记为“二进制”以抑制差异输出。

hackernews · FergusArgyll · Jun 18, 10:29 · [社区讨论](https://news.ycombinator.com/item?id=48583356)

**背景**: Git 使用 .gitignore 文件来指定 Git 应忽略的故意未跟踪文件。然而，某些文件（如 IDE 配置或操作系统产物）属于个人文件，不应放在共享的 .gitignore 中。Git 为此提供了全局排除文件和仓库特定的排除文件（如 .git/info/exclude）。

**社区讨论**: 评论者称赞了全局排除功能，指出它解决了开发者将个人文件添加到每个项目 .gitignore 中的常见问题。一位用户强调了 .gitattributes 用于忽略差异（例如 package-lock.json），另一位用户纠正说 ~/.config/git/ignore 是每用户设置，而非机器级别。

**标签**: `#Git`, `#version control`, `#developer tools`, `#best practices`

---

<a id="item-13"></a>
## [W Social：欧洲数字主权还是政治作秀？](https://blog.elenarossini.com/w-social-public-institutions-and-the-theater-of-european-digital-sovereignty/) ⭐️ 7.0/10

Elena Rossini 的一篇博文批评了 W Social，这是一个作为 X 等美国平台替代品推出的欧洲社交平台，认为它缺乏透明度，与开源项目 Eurosky 相比更像是一场作秀。 这一批评凸显了欧洲数字主权运动中真正的开源努力与政治动机项目之间的紧张关系，影响公众信任和政策方向。 W Social 使用与 Bluesky 相同的 AT 协议，但以有限责任公司形式运营，可能存在盈利动机；而 Eurosky 是一个非营利组织，在同一协议上透明地构建。

hackernews · nemoniac · Jun 18, 12:46 · [社区讨论](https://news.ycombinator.com/item?id=48584497)

**背景**: 欧洲数字主权是指欧盟减少对美国科技巨头依赖的努力。W Social 和 Eurosky 都是基于 AT 协议构建的社交网络，该协议支持互操作性。然而，W Social 获得了大量媒体关注和欧盟政客的支持，而 Eurosky 则基本未被注意。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zdfheute.de/politik/deutschland/w-social-nachrichtenplattform-twitter-100.html">W Social – das neue Twitter? Europas Antwort auf "X" am Start</a></li>
<li><a href="https://eurosky.tech/">Eurosky - Building a thriving open social web for Europe</a></li>

</ul>
</details>

**社区讨论**: 评论者对 W Social 的动机表示怀疑，有人称其为‘带有欧洲口音的 TruthSocial’，并指出其创始人的金融背景。其他人则指出，透明的 Eurosky 项目缺乏媒体报道，与 W Social 的高调发布形成对比。

**标签**: `#digital sovereignty`, `#social media`, `#Europe`, `#open source`, `#politics`

---

<a id="item-14"></a>
## [Gerrymandle：每日解谜游戏教你选区划分](https://gerrymandle.cc/) ⭐️ 7.0/10

一款名为 Gerrymandle 的每日解谜游戏上线，让玩家通过重新划分选区来学习 gerrymandering。该游戏在 Hacker News 上发布后迅速获得高度关注，获得 130 分和 62 条评论。 这款游戏将复杂且常被掩盖的政治策略变得通俗易懂，可能提升公民教育水平。它还引发了关于公平选区划分和选举改革的讨论，这些在许多民主国家都是关键议题。 游戏优先考虑趣味性而非完全写实；例如，如果两个党派在一个选区打成平手，则无人获胜，这虽不现实但简化了概念。该游戏设计为每日谜题，配有清晰的说明和精美的呈现。

hackernews · realmofthemad · Jun 18, 14:16 · [社区讨论](https://news.ycombinator.com/item?id=48585739)

**背景**: Gerrymandering 是指操纵选举区边界以偏袒特定政党或群体的做法。它常被批评破坏公平代表权，在美国和其他国家是一个有争议的问题。该术语源于 1812 年马萨诸塞州的一项选区重划计划，该计划创建了一个形状像蝾螈的选区，结合了州长 Elbridge Gerry 的名字和“salamander”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gerrymandering">Gerrymandering - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Electoral_district">Electoral district - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该游戏的教育潜力，有人建议它非常适合高中公民课堂。其他人讨论了公平选区划分的数学方法，并引用了学术论文和桌游“Berrymandering”。

**标签**: `#game`, `#gerrymandering`, `#civics`, `#puzzle`, `#politics`

---

<a id="item-15"></a>
## [Emacs 31 预览：Tree-sitter、原生编译、Eglot](https://www.rahuljuliato.com/posts/emacs-31-around-the-corner) ⭐️ 7.0/10

Emacs 31 对 tree-sitter 集成、原生编译和内置 LSP 客户端 Eglot 进行了重大改进。这些变化已在早期用户中测试，预计将在下一个版本中发布。 这些增强使 Emacs 更快、更现代化，帮助其保持与 VS Code 等当代编辑器的竞争力。改进还通过提供更好的开箱即用语言支持，降低了新用户的使用门槛。 Tree-sitter 提供增量解析，实现准确的语法高亮和代码导航；原生编译将 Elisp 编译为机器码，显著提升速度。Eglot 将语言服务器协议支持直接集成到 Emacs 中，提供自动补全和诊断等功能。

hackernews · frou_dh · Jun 18, 12:10 · [社区讨论](https://news.ycombinator.com/item?id=48584135)

**背景**: Emacs 是一个高度可扩展的文本编辑器，已开发超过 40 年。Tree-sitter 是一个解析库，能够快速增量解析源代码；原生编译使用 libgccjit 将 Emacs Lisp 编译为原生代码。Eglot 是一个极简的 LSP 客户端，从 Emacs 29 开始被捆绑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://emacs-tree-sitter.github.io/">Tree - sitter :: Emacs Tree - sitter</a></li>
<li><a href="https://www.masteringemacs.org/article/speed-up-emacs-libjansson-native-elisp-compilation">Speed up Emacs with native elisp compilation - Mastering Emacs</a></li>
<li><a href="https://joaotavora.github.io/eglot/">Eglot : The Emacs Client for the Language Server Protocol</a></li>

</ul>
</details>

**社区讨论**: 社区对新功能感到兴奋，许多长期用户重申了对 Emacs 的承诺。一些用户指出，LLM 可以帮助新用户通过协助配置来克服陡峭的学习曲线。一些幽默评论指出，许多用户升级后会继续像以前一样使用 Emacs。

**标签**: `#emacs`, `#editor`, `#open-source`, `#software-development`, `#community`

---

<a id="item-16"></a>
## [新版 Outlook 启动需 10 秒，经典版瞬间打开](https://www.windowslatest.com/2026/06/15/microsofts-new-outlook-takes-10-seconds-to-do-what-outlook-classic-does-instantly-on-windows/) ⭐️ 7.0/10

据 Windows Latest 报道，微软基于 WebView2 构建的新版 Outlook 执行某些任务需要约 10 秒，而经典版 Outlook 瞬间完成。 这种性能倒退凸显了现代基于 Web 的应用中软件臃肿的普遍趋势，影响了整个 Windows 生态系统的用户生产力和满意度。 新版 Outlook 基于 WebView2（一种 Web 渲染引擎），批评者指出加载顺序不当和不必要的数据渲染是导致速度变慢的原因。

hackernews · Adam-Hincu · Jun 18, 12:19 · [社区讨论](https://news.ycombinator.com/item?id=48584207)

**背景**: 软件臃肿指程序的新版本变得更慢、占用更多资源。基于 Web 的应用常因臃肿的框架和低效代码而出现此问题。经典版 Outlook 是原生桌面应用，而新版 Outlook 本质上是包裹在原生外壳中的 Web 应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://stackshala.medium.com/what-really-makes-software-bloated-hint-its-not-just-size-ac32a2224344">What Really Makes Software Bloated ? (Hint: It’s Not Just...) | Medium</a></li>
<li><a href="https://www.definitions.net/definition/software+bloat">What does software bloat mean?</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了其他微软应用（如记事本）类似变慢的个人经历，并讨论了问题是 Web 应用固有还是微软实现特有问题。有人指出其他基于 Web 的邮件客户端（如 Fastmail）仍然很快。

**标签**: `#Microsoft Outlook`, `#performance`, `#web apps`, `#software bloat`, `#user experience`

---

<a id="item-17"></a>
## [Datasette Apps：在 Datasette 内运行沙盒化 HTML/JS 应用](https://simonwillison.net/2026/Jun/18/datasette-apps/#atom-everything) ⭐️ 7.0/10

Simon Willison 发布了新插件 datasette-apps，允许用户在 Datasette 内部托管沙盒化的 HTML+JavaScript 应用，支持只读 SQL 查询，并可通过存储查询实现写入操作。 该插件将 Datasette 从数据探索工具扩展为构建自定义交互应用的平台，支持仪表盘、时间线、内部工具等新用例，同时通过沙盒机制保障安全。 应用在 iframe 中运行，设置 sandbox="allow-scripts allow-forms" 并通过 CSP 头阻止对外 HTTP 请求，防止数据泄露。该插件最初为 Datasette Agent 构建，后升级为独立概念。

rss · Simon Willison · Jun 18, 23:58

**背景**: Datasette 是一个用于探索和发布数据的开源工具，提供 JSON API 支持自定义前端。datasette-apps 插件允许直接在 Datasette 界面中嵌入完整的 HTML/JS 应用，以 SQLite 作为后端。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datasette.io/tools/datasette-app">datasette - app - a tool for Datasette</a></li>
<li><a href="https://pypi.org/project/datasette-apps/">Create apps that live inside Datasette</a></li>

</ul>
</details>

**标签**: `#datasette`, `#plugin`, `#sql`, `#web-applications`, `#sandbox`

---

