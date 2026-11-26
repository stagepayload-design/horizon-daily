---
layout: default
title: "Horizon Summary: 2026-11-26 (ZH)"
date: 2026-11-26
lang: zh
permalink: /2026/11/26/summary-zh.html
---

> From 106 items, 22 important content pieces were selected

---

1. [OpenAI 预印本声称矩阵乘法指数恰为 9/4](#item-1) ⭐️ 9.0/10
2. [VMware vCenter 严重认证绕过漏洞 CVE-2026-123903（CVSS 9.8）](#item-2) ⭐️ 9.0/10
3. [1Password 披露 2026 年 11 月安全事件：攻击者推送恶意代码](#item-3) ⭐️ 8.0/10
4. [斯科特·阿伦森盛赞 AI 数学突破，引发激烈辩论](#item-4) ⭐️ 8.0/10
5. [广义黎曼猜想的 Lean 证明从 1700 万行缩减至 7.6 万行](#item-5) ⭐️ 8.0/10
6. [Linux NFS 服务器曝 12 年历史预认证远程 root 漏洞](#item-6) ⭐️ 8.0/10
7. [谷歌研究发布关于整数分解和离散对数的 Cogentic 论文](#item-7) ⭐️ 8.0/10
8. [Defang 披露 GitHub App 供应链攻击事件](#item-8) ⭐️ 8.0/10
9. [研究人员通过 AWS IP 重新分配以 3 美元劫持美国财政部子域名](#item-9) ⭐️ 8.0/10
10. [微软：APT 组织滥用 ARTEX 智能体 AI 渗透测试框架](#item-10) ⭐️ 8.0/10
11. [Ubuntu 安全响应迟缓引发迁移讨论](#item-11) ⭐️ 7.0/10
12. [预印本推翻简单多胞形的多项式 Hirsch 猜想](#item-12) ⭐️ 7.0/10
13. [开发者用 Lean 审计 Clojure 核心库，发现未报告的错误](#item-13) ⭐️ 7.0/10
14. [绕过 iOS Safari 的 60 FPS 限制，打造原生般 Web 应用](#item-14) ⭐️ 7.0/10
15. [CISA 将 10 个已被积极利用的漏洞加入 KEV 目录](#item-15) ⭐️ 7.0/10
16. [Gemini 4 Neon 标志着 Google DeepMind 重返前沿实验室行列](#item-16) ⭐️ 7.0/10
17. [AI 攻击利用未回收密钥攻破安全厂商](#item-17) ⭐️ 7.0/10
18. [Cisco Talos 分析 OpenAI 相关智能体集群的战术](#item-18) ⭐️ 7.0/10
19. [AWS 推出企业托管授权，支持 AI 代理安全访问](#item-19) ⭐️ 7.0/10
20. [AWS Network Firewall 新增基于资源身份的上下文感知规则](#item-20) ⭐️ 7.0/10
21. [Cloudflare 推出 Search for Agents，让网站可被 AI 代理查询](#item-21) ⭐️ 7.0/10
22. [InstructReplay 通过自我重放减少事实微调的能力退化](#item-22) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI 预印本声称矩阵乘法指数恰为 9/4](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf) ⭐️ 9.0/10

OpenAI 于 2026 年 11 月 24 日发布预印本《矩阵乘法指数为九分之四》，声称方阵乘法的指数在每个域上恰好为 9/4，并为形式算术电路建立了匹配的上界和下界。这是 OpenAI 四篇新论文之一，这些论文共同解决了“数学前 500 开放问题”列表中的八个问题，包括矩阵乘法指数（排名第 25）和强多项式线性规划（Smale 第九问题）。 如果正确，这一结果将通过确定矩阵乘法的精确渐近成本，结束代数复杂性理论中长达数十年的探索；矩阵乘法是机器学习、科学计算和密码学的基础操作。这也标志着 AI 驱动数学发现可能发生范式转变，对安全和算法设计具有重大影响。 该论文证明了形式算术电路的匹配下界，这意味着结果适用于这种受限的计算模型，而非所有算法。声称的指数 9/4（2.25）意味着没有算法能在少于约 n^2.25 步内相乘两个 n×n 矩阵，并且这项工作属于四篇论文的一部分，共解决八个开放问题，包括平均收益博弈和奇偶博弈。

hackernews · E-Reverance · Nov 25, 01:19 · [社区讨论](https://news.ycombinator.com/item?id=50637220)

**背景**: 矩阵乘法指数（用ω表示）描述相乘两个方阵所需的算术运算次数随维度 n 的增长方式。几十年来，研究人员一直在寻找最优指数，朴素算法给出 3，而 Strassen 算法等先进方法将其降至 2.81 以下，但精确值仍未知。9/4 的下界意味着没有算法能比约 n^2.25 次操作做得更好，从而解决这个问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://interestingengineering.com/culture/openai-exact-2-25-matrix-multiplication-exponent">OpenAI establishes exact 2.25 exponent for matrix multiplication</a></li>
<li><a href="https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/README.md">math / preprints /The- matrix - multiplication -exponent-is...</a></li>
<li><a href="https://www.alphaxiv.org/abs/2611.matrix-multiplication-exponent-lower-bound">The Matrix Multiplication Exponent Is Nine Fourths | alphaXiv</a></li>

</ul>
</details>

**社区讨论**: 评论者对近期 AI 驱动数学突破的速度表示惊叹，一些人将 OpenAI 和 Anthropic 比作贝尔实验室，但质疑其动机是否仅限于公关。其他人担心与密码学相关的结果被隐瞒或用作武器，并推测 OpenAI 可能保留更强大的内部模型以复合突破。

**标签**: `#mathematics`, `#AI-for-science`, `#cryptography`, `#algorithms`, `#OpenAI`

---

<a id="item-2"></a>
## [VMware vCenter 严重认证绕过漏洞 CVE-2026-123903（CVSS 9.8）](https://www.rapid7.com/blog/post/etr-cve-2026-123903-critical-vmware-directory-service-authentication-bypass-affects-vcenter) ⭐️ 9.0/10

2026 年 11 月 24 日，Broadcom 发布了 VMSA-2026-0011 安全公告，修复了 CVE-2026-123903——一个存在于 vCenter 的 VMware Directory Service（vmdir）组件中、可通过 LDAP 网络访问的 CVSS 9.8 严重未认证认证绕过漏洞。目前已有公开的概念验证利用代码，Rapid7 已验证其可成功实现认证绕过，但截至本文撰写时尚未有在野利用的报告。 vCenter 是广泛部署的企业虚拟化管理平台，而该漏洞无需认证、可通过网络触达，且对机密性、完整性和可用性均有高影响，意味着任何能访问该服务的人都可能完全攻陷管理平面。由于攻击者此前曾针对 VMware Directory Service 漏洞进行利用，组织应在常规补丁周期之外紧急修复暴露的系统。 Broadcom 未提供任何临时缓解措施，且这些 vCenter 更新不适用于 Quick Patch，因此必须使用标准更新机制；修复版本还同时解决了同一公告中的其他几个高危和中危 CVE（CVE-2026-123904、CVE-2026-123905 等）。CVE-2026-123903 与较早的 CVE-2026-123890 不同，后者通过 RPC 可达，且曾被报告已在野利用。

rss · Rapid7 Emergent Threat Response · Nov 25, 12:19

**背景**: VMware vCenter 是 vSphere 虚拟化环境的集中管理平台，而 VMware Directory Service（vmdir）是 vCenter Single Sign-On 的一个组件，用于存储身份和目录数据。认证绕过意味着攻击者无需有效凭据即可获得访问权限，CVSS 9.8 分表示这是一个严重、易于利用且影响巨大的漏洞。Broadcom 目前在其 VCF 安全与合规指南下维护 VMware 安全公告。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ubackup.com/enterprise-backup/vcenter-sso.html">How to Configure a vSphere SSO Domain in vCenter</a></li>
<li><a href="https://www.cisecurity.org/advisory/multiple-vulnerabilities-in-vmware-products-could-allow-for-arbitrary-code-execution_2026-142">Multiple Vulnerabilities in VMware Products Could Allow for Arbitrary...</a></li>
<li><a href="https://github.com/vmware/vcf-security-and-compliance-guidelines/blob/main/security-advisories/vmsa-2026-0006/README.md">github.com/ vmware /vcf- security -and-compliance-guidelines/blob/main...</a></li>

</ul>
</details>

**标签**: `#VMware vCenter`, `#authentication bypass`, `#critical vulnerability`, `#CVE-2026-123903`, `#VMSA-2026-0011`

---

<a id="item-3"></a>
## [1Password 披露 2026 年 11 月安全事件：攻击者推送恶意代码](https://1password.com/blog/update-on-nov-2026-security-incident) ⭐️ 8.0/10

1Password 披露，2026 年 11 月 19 日，攻击者获取了一名员工的公司 GitHub 账户访问权限，并利用该账户访问源代码并向后端服务推送恶意代码。公司表示，部分客户的姓名和电子邮件地址被访问，但客户保险库内容未遭泄露。 该事件凸显了 SaaS 公司面临的关键供应链风险：员工开发账户被攻破可能导致恶意代码被部署到生产环境。鉴于 1Password 作为密码管理器的角色，任何泄露都会引发对敏感凭证安全的严重担忧，尽管保险库数据仍保持加密且未受影响。 披露未说明是否设置了分支保护规则或被绕过，因此攻击者如何能够向后端服务推送代码仍不清楚。公司已通知少数受影响用户，并继续进行调查。

hackernews · lxhrstn · Nov 25, 17:18 · [社区讨论](https://news.ycombinator.com/item?id=50644817)

**背景**: 1Password 是一款流行的密码管理器，将用户凭证存储在加密保险库中，可本地或云端存储。供应链攻击是指攻击者攻破可信第三方或内部系统，向软件或服务中注入恶意代码。GitHub 是广泛使用的源代码管理和 CI/CD 平台，如果攻击者获取了开发者账户的访问权限，他们可能能够推送会被自动部署的代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://1password.com/blog/update-on-nov-2026-security-incident">Update on a security incident involving... | 1 Password</a></li>
<li><a href="https://www.macrumors.com/2026/11/25/1password-security-breach/">1 Password Security Breach: What Was Accessed and... - MacRumors</a></li>

</ul>
</details>

**社区讨论**: tptacek 等评论者强调，攻破员工笔记本电脑以推送代码是 SaaS 泄露的典型模式，ctidd 批评披露未说明分支保护是否缺失或被绕过。ChrisHardie 等人对在线保险库及攻击者可能插入供应链表示担忧，fn-mote 则希望有更明确的表述说明加密保险库未被下载。

**标签**: `#security-incident`, `#supply-chain`, `#password-manager`, `#saas-security`, `#code-deployment`

---

<a id="item-4"></a>
## [斯科特·阿伦森盛赞 AI 数学突破，引发激烈辩论](https://scottaaronson.blog/?p=10379) ⭐️ 8.0/10

斯科特·阿伦森发表博客文章，对一项由 AI 驱动的重大数学突破作出反应，该文章迅速登上 Hacker News 榜首，获得 842 分和约 700 条评论。文章还引用了一篇相关预印本《矩阵乘法指数是九的四次方》，该预印本据称建立了矩阵乘法复杂度的匹配上界和下界。 这标志着数学研究方式可能发生范式转变，AI 系统越来越有能力生成和验证复杂证明。社区的激烈讨论反映了人们对 AI 在自动化发现中的作用以及人类数学家未来的广泛兴奋与焦虑。 讨论重点提及 Lean 和 Mathlib 等工具，它们是用于形式化数学的交互式证明助手和库，并质疑如果没有大语言模型或生成式 AI，这一突破是否可能实现。评论者还争论 AI 生成的证明对人类学习是否有用，还是主要供 AI 使用。

hackernews · Kotlopou · Nov 25, 19:11 · [社区讨论](https://news.ycombinator.com/item?id=50646108)

**背景**: Lean 是由 Leonardo de Moura 开发的开源交互式定理证明器和编程语言，Mathlib 是基于 Lean 构建的社区驱动形式化数学库。自动定理证明是 AI 的一个领域，专注于开发能够构建或检查形式证明的系统。矩阵乘法指数涉及矩阵乘法的计算复杂度，这是许多算法中的基本操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://leanprover-community.github.io/">Lean community</a></li>
<li><a href="https://lean-lang.org/">Lean Programming Language</a></li>
<li><a href="https://en.wikipedia.org/wiki/Computational_complexity_of_matrix_multiplication">Computational complexity of matrix multiplication - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了复杂情绪：一些人质疑这一突破是归功于 Lean/Mathlib 和计算能力而非大语言模型，另一些人则担心人类挑战数学的未来，以及 AI 证明是否可理解或对人类有用。少数人将其与量子力学之前物理学被“解决”的情形相提并论，还有人希望 AI 能解决科拉茨猜想等著名问题。

**标签**: `#AI`, `#mathematics`, `#automated-theorem-proving`, `#Lean`, `#research`

---

<a id="item-5"></a>
## [广义黎曼猜想的 Lean 证明从 1700 万行缩减至 7.6 万行](https://github.com/lsernau/grh-lean) ⭐️ 8.0/10

lsernau 发布了一个新的广义黎曼猜想（GRH）的 Lean 形式化证明，将证明从约 1700 万行缩减到约 7.6 万行，减少了 99.56%，同时清晰区分了“已知数学”和“新数学”，并附有可读的文档。 这一大幅缩减使形式化证明更易于数学家审查和理解，并凸显了 LLM 辅助的“证明高尔夫”在形式验证中日益增长的作用，可能有助于回应关于庞大且缺乏洞察力的证明是个问题的担忧。 据报道，该证明仅使用了 propext、Classical.choice 和 Quot.sound 三条公理，仓库中包含大量可读文档；然而，实现缩减的具体方法以及 LLM 的作用在提供的内容中并未完全详述。

hackernews · nb-t · Nov 25, 21:48 · [社区讨论](https://news.ycombinator.com/item?id=50648050)

**背景**: 黎曼猜想是关于黎曼 ζ 函数零点的著名未解猜想，其推广到 L 函数的形式称为广义黎曼猜想。Lean 是一种定理证明器和函数式编程语言，用于形式化数学和验证证明。近期的工作，如 Anthropic 对费马大定理的形式化，探索了使用 AI 辅助创建 Lean 证明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lean-lang.org/learn/">Learn — Lean Lang</a></li>
<li><a href="https://en.wikipedia.org/wiki/Riemann_hypothesis">Riemann hypothesis - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/research/formalizing-fermats-last-theorem">Formalizing Fermat's Last Theorem \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 评论者赞扬了较短证明的可读性和文档，其中一位指出清晰区分了“已知数学”和“新数学”。一些人讨论这是否回应了陶哲轩关于庞大证明缺乏洞察力的担忧，还有人要求为不熟悉 Lean 的数学家解释 Lean 特有的概念（如公理）。

**标签**: `#formal-verification`, `#Lean`, `#AI-for-math`, `#LLM`, `#Riemann-Hypothesis`

---

<a id="item-6"></a>
## [Linux NFS 服务器曝 12 年历史预认证远程 root 漏洞](https://opensec.in/blog/nfs2root-cve-2026-99362) ⭐️ 8.0/10

Linux 内核 NFS 服务器（nfsd）中被披露存在一个长达 12 年的预认证堆溢出漏洞，可让远程攻击者获取 root 权限。该漏洞在技术文章中详细说明，虽已在数月前于上游修复，但潜伏超过十年。 这是 Linux 内核核心子系统中的高危预认证远程 root 漏洞，影响众多企业和 NAS 环境。它凸显了暴露内核网络服务的风险以及及时打补丁的重要性。 该漏洞是 nfsd 处理 NFSv4 SEQUENCE 操作时的堆溢出，精心构造的请求可缩小回复缓冲区并导致内存破坏。目前没有公开的 PoC 利用代码，且 NFS 很少直接暴露在公网，这限制了实际影响。

hackernews · dm · Nov 25, 20:35 · [社区讨论](https://news.ycombinator.com/item?id=50647161)

**背景**: NFS（网络文件系统）是一种广泛使用的网络文件共享协议，其在 Linux 内核中的服务器组件称为 nfsd。默认情况下，NFS 不提供用户认证，而是依赖基于 IP 的访问控制，这使得任何预认证漏洞都特别危险。内核中的堆溢出可被利用来破坏内存并提升权限，尽管 SMEP 和 SMAP 等现代缓解措施增加了利用难度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cve.now/CVE-2026-31402">CVE-2026-31402: Linux kernel heap overflow in LOCK replay</a></li>
<li><a href="https://wiki.archlinux.org/title/NFS">NFS - ArchWiki</a></li>
<li><a href="https://github.com/xairy/linux-kernel-exploitation">GitHub - xairy/ linux - kernel - exploitation : A collection of links related to...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出该漏洞已在数月前于上游修复，且 NFS 很少面向互联网，降低了其影响。一些人建议使用基于 XDP 的 L7 防火墙“yeet”或经过形式化验证的 seL4 微内核作为缓解措施，而另一些人则注意到缺乏公开的 PoC。

**标签**: `#linux-kernel`, `#nfs`, `#remote-exploit`, `#heap-overflow`, `#vulnerability-disclosure`

---

<a id="item-7"></a>
## [谷歌研究发布关于整数分解和离散对数的 Cogentic 论文](https://github.com/google-research/google-research/tree/master/cogentic_research_papers) ⭐️ 8.0/10

谷歌研究在其公开的 GitHub 仓库中发布了一系列“Cogentic”论文，涵盖整数分解、离散对数和其他数学问题。此次发布在 Hacker News 上引发了激烈讨论，获得 443 分和 330 条评论，人们纷纷猜测 AI 驱动的数学发现。 整数分解和离散对数是 RSA 和 Diffie-Hellman 等广泛使用的公钥密码系统的基础，因此任何新的算法见解都可能产生重大的密码学影响。此次发布也加剧了关于 AI 是否正在加速基础数学研究的更广泛争论。 这些论文以 PDF 格式托管在 google-research GitHub 仓库的“cogentic_research_papers”目录下，但提供的内容中没有摘要或详细结果，因此具体方法和主张仍未经验证。社区成员链接了一条推文，暗示这是“更大事物的冰山一角”，但没有给出原始证据。

hackernews · rgwohlbold · Nov 25, 13:33 · [社区讨论](https://news.ycombinator.com/item?id=50642086)

**背景**: 整数分解是将一个数分解为质因数的问题，其假定的困难性是 RSA 加密安全的基础。离散对数问题是一个相关的困难问题，用于 Diffie-Hellman 密钥交换和椭圆曲线密码学。两者都被认为容易受到未来运行 Shor 算法的量子计算机的攻击，这也推动了对经典算法的研究。最近，AI 系统在辅助数学发现方面显示出潜力，导致了像 HorizonMath 这样的基准测试来衡量在未解决问题上的进展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50642086">Google releases Cogentic papers on integer... | Hacker News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Discrete_logarithm">Discrete logarithm - Wikipedia</a></li>
<li><a href="https://www.iccs-meeting.org/archive/iccs2023/papers/140770001.pdf">Classical methods for integer factorization and discrete</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了兴奋和猜测，一些人引用传言称这项工作是一项更大突破的一部分，并将其与 AlphaGo 对基于搜索的发现的影响相提并论。其他人指出了在 AI 市场下滑之际数学突破迅速的讽刺之处，还有一些人反思了 AI 如何改变他们对金钱能否解决困难数学问题的看法。

**标签**: `#cryptography`, `#integer-factorization`, `#discrete-log`, `#AI-for-math`, `#Google-Research`

---

<a id="item-8"></a>
## [Defang 披露 GitHub App 供应链攻击事件](https://defang.io/blog/post/security-incident-november-2026/) ⭐️ 8.0/10

Defang 发布了一份事件复盘报告，披露攻击者利用一个用于本地开发和测试的权限过大的 GitHub App，推送了一个带标签的发布版本，在 CI 中执行代码并窃取了生产凭证。该 App 拥有更改部署环境的权限，而生产环境信任发布标签，因此攻击者的代码得以在拥有生产密钥访问权限的情况下运行。 该事件凸显了 CI/CD 流水线中非人类身份权限过大的严重风险，一个被攻陷的 GitHub App 就可能导致整个生产环境失守。它强调了最小权限原则以及围绕发布标签和部署工作流建立更严格信任边界的必要性。 攻击者以该 GitHub App 的身份，可以推送提交和分支、更改仓库设置、覆盖 Actions 密钥和变量、修改部署环境及其保护规则，以及创建和合并拉取请求。Defang 还警告称，包括姓名和电子邮件地址在内的账单信息可能已泄露。

hackernews · gregsadetsky · Nov 25, 21:47 · [社区讨论](https://news.ycombinator.com/item?id=50648035)

**背景**: GitHub App 是一种集成，可以被授予细粒度权限来对仓库执行操作，常用于 CI/CD 自动化。当此类 App 权限过大且凭证被盗时，攻击者可以利用对其的信任，将恶意代码注入软件供应链。此次事件与近期针对 GitHub Actions 和发布工作流的其他供应链攻击类似。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nhimg.org/risks-of-non-human-identity-misconfiguration-and-poor-management">Risks of Non–Human Identity Misconfiguration and Poor Management</a></li>
<li><a href="https://www.rabinarayanpatra.com/blogs/tanstack-supply-chain-attack-2026">TanStack npm Supply Chain Attack 2026: How OIDC Beat SLSA</a></li>
<li><a href="https://www.darkreading.com/application-security/supply-chain-attacks-github-actions-gravity-forms-npm">Malware Spotted in GitHub Actions , Gravity Forms, npm</a></li>

</ul>
</details>

**社区讨论**: 评论者对安装了 Defang GitHub App 的用户面临的巨大影响范围表示担忧，并列举了具体能力，如推送提交、更改工作流文件、覆盖密钥和修改部署环境。一些人对 Defang 团队表示同情，另一些人则质疑 LLM 是否可能泄露 GitHub 密钥，并提到了 Todoist 和 1Password 的类似事件。

**标签**: `#supply-chain-security`, `#ci-cd-security`, `#github-apps`, `#incident-response`, `#credential-theft`

---

<a id="item-9"></a>
## [研究人员通过 AWS IP 重新分配以 3 美元劫持美国财政部子域名](https://www.intruder.io/research/taking-over-us-treasury-subdomains-for-3-each) ⭐️ 8.0/10

Intruder 的安全研究人员演示了如何利用 AWS IP 地址重新分配和悬空 DNS 记录，以每个子域名仅 3 美元的成本接管美国财政部（可能是*.treasury.gov）的子域名。攻击过程包括注册新的 AWS 账户，通过快速分配和释放 IP 来获取财政部子域名先前使用的相同 IP 地址，然后为该子域名配置有效的 TLS 证书。 这凸显了一种更广泛的子域名接管漏洞类别，可能影响甚至高知名度的.gov 域名，削弱对政府网站的信任，并可能被用于网络钓鱼、恶意软件分发和数据拦截。这也引发了关于云服务提供商在防止此类攻击中的责任的质疑，因为 AWS 拒绝做出改变。 该攻击依赖于 AWS 的快速 IP 重新分配机制，攻击者通过反复分配和释放弹性 IP 来获取特定 IP 地址。AWS 认为快速分配/释放违反政策，但不计划改变其系统，称问题源于客户侧的 DNS 记录。研究人员指出，尽管 AWS 有控制措施，但不足以防止这种攻击。

hackernews · negura · Nov 25, 04:27 · [社区讨论](https://news.ycombinator.com/item?id=50638478)

**背景**: 子域名接管发生在 DNS 记录（如 CNAME 或 A 记录）指向不再存在或不再由域名所有者控制的资源时，攻击者可以认领该资源并在受信任的域名下提供内容。在云环境中，IP 地址是动态分配和释放的，如果 DNS 记录仍指向已释放的 IP，获得该 IP 的攻击者就可以接管子域名。只要攻击者能够证明对域名的控制权（在本例中通过在被接管的子域名上托管文件来实现），就可以为该域名获取 TLS 证书。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://powerdmarc.com/dangling-dns-records-subdomain-takeover/">Dangling DNS Records : How To Prevent Subdomain Takeover</a></li>
<li><a href="https://www.ionix.io/writing-center/how-to-detect-dangling-dns-and-prevent-subdomain-takeovers-in-2026/">Dangling DNS Detection: Prevent Subdomain Takeovers - IONIX</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了 HTTPS/TLS 在攻击中的作用，一些人质疑证书颁发机制，并建议使用 EV 证书可能有所帮助。其他人批评 AWS 没有采取更多措施防止 IP 重新分配攻击，提出了诸如在 Route53 中自动删除的弹性 IP 记录类型等解决方案。总体情绪是，尽管 AWS 归咎于客户 DNS 配置，但它应承担部分责任。

**标签**: `#subdomain-takeover`, `#cloud-security`, `#AWS`, `#DNS`, `#TLS`

---

<a id="item-10"></a>
## [微软：APT 组织滥用 ARTEX 智能体 AI 渗透测试框架](https://www.microsoft.com/en-us/security/blog/2026/11/25/what-defenders-need-to-know-artex-agentic-ai-framework-threat-actors-abuse/) ⭐️ 8.0/10

微软威胁情报报告称，包括 Onyx Sleet、Salt Typhoon、Storm-0940、Storm-3358、Pearl Sleet 和 Crystal Typhoon 在内的多个被追踪的威胁行为者正在滥用 ARTEX 智能体 AI 渗透测试框架，以加速网络侦察、凭据攻击和 Web 应用漏洞利用。该博客于 2026 年 11 月 25 日发布，详细说明了这些组织如何将 ARTEX 整合到其现有的攻击工作流程中。 这是首批记录与国家关联的 APT 组织在真实攻击中使用智能体 AI 的主要来源报告之一，表明 AI 智能体可以显著加速和扩展传统攻击阶段。云环境和企业环境的防御者需要调整检测和响应策略，以应对更快速、自动化的入侵工作流程。 ARTEX 是一个 AI 原生的渗透框架，操作员提供目标和目的后，由一组 LLM 智能体规划并执行攻击；默认情况下它使用 Nmap、curl、wget、Python HTTP 客户端以及通过 Playwright 驱动的无头 Chromium 等工具。微软还观察到威胁行为者使用智能体 AI 工具搜索公共 GitHub 仓库中的暴露机密，包括凭据和 AI 推理 API 密钥。

rss · Microsoft Security Blog · Nov 25, 18:09

**背景**: 智能体 AI 框架与传统命令控制工具的不同之处在于，它使用大型语言模型智能体自主规划并串联攻击行动，在数秒而非数小时内产生效果。ARTEX（自主渗透测试控制台）就是这样一个框架，自 2026 年 9 月下旬以来，其公开分支和改名版本与云入侵激增有关。微软使用天气主题名称追踪威胁行为者，其中 Salt Typhoon 被广泛报道为与中国有关联的 APT 组织。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.elastic.co/security-labs/threat-command/agentic-offensive-frameworks-detection-artex">Inside the loop: Five AI attack frameworks that never ask permission</a></li>
<li><a href="https://securitylabs.datadoghq.com/articles/artex-agentic-attacks-aws-environments/">On the hunt for ARTEX : understanding agentic attacks in AWS...</a></li>
<li><a href="https://www.wiz.io/blog/agentic-attacks-artex-offensive-ai-frameworks">Agentic Attacks in the Wild: ARTEX & Offensive AI Frameworks</a></li>

</ul>
</details>

**标签**: `#agentic AI`, `#threat intelligence`, `#APT`, `#offensive security`, `#Microsoft`

---

<a id="item-11"></a>
## [Ubuntu 安全响应迟缓引发迁移讨论](https://www.openwall.com/lists/oss-security/2026/11/25/9) ⭐️ 7.0/10

oss-security 邮件列表上的一篇帖子在 Hacker News 上引发讨论（117 分，46 条评论），聚焦 Ubuntu 安全响应时间缓慢以及及时打补丁与回归测试之间的权衡。 作为使用最广泛的 Linux 发行版之一，Ubuntu 的补丁延迟可能促使企业和用户转向 Debian 等替代品，影响整个 Linux 生态的安全态势。 评论者指出，安全修复有时会先出现在-updates 仓库，数小时后才进入安全仓库；而 Debian 有限的 QA 资源也可能导致回归问题，说明平衡速度与稳定性之难。

hackernews · gslin · Nov 25, 20:38 · [社区讨论](https://news.ycombinator.com/item?id=50647181)

**背景**: 像 Ubuntu 这样的 Linux 发行版会将安全补丁向后移植到旧版软件包，而不是升级到新的上游版本，这需要大量回归测试以避免破坏系统。oss-security 邮件列表是披露和讨论开源漏洞的重要论坛，Hacker News 则常放大此类讨论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.openwall.com/lists/oss-security/">oss - security mailing list</a></li>
<li><a href="https://wiki.ubuntu.com/SecurityTeam/ReleaseCycle">SecurityTeam/ReleaseCycle - Ubuntu Wiki</a></li>

</ul>
</details>

**社区讨论**: 一些用户因无法接受的延迟已将服务器从 Ubuntu 迁移到 Debian，而另一些人则辩护称回归测试必不可少，并警告 Debian 也可能引入回归。一位稳定内核维护者的引言强调，挑选补丁可能使系统不安全，多位评论者对 Ubuntu 的缓慢响应表示惊讶和失望。

**标签**: `#Ubuntu`, `#Linux security`, `#distro security`, `#patch management`, `#Hacker News`

---

<a id="item-12"></a>
## [预印本推翻简单多胞形的多项式 Hirsch 猜想](https://github.com/openai/math/blob/main/preprints/Superpolynomial-graph-diameter-of-simple-polytopes-November-24-2026/paper.pdf) ⭐️ 7.0/10

GitHub 上发布的一篇新预印本（日期为 2026 年 11 月 24 日）通过构造图直径在面数和维数上呈超多项式增长的简单多胞形，推翻了多项式 Hirsch 猜想。这意味着线性规划不存在多项式时间的单纯形算法。 这一结果解决了多面体组合学和复杂性理论中的一个重大开放问题，表明单纯形法在最坏情况下无法保证多项式时间运行。它影响理论计算机科学和优化领域，并可能影响线性规划算法的设计。 该论文构造了具有超多项式图直径的简单多胞形，直接与多项式 Hirsch 猜想矛盾。这是对 2010 年原始 Hirsch 猜想被推翻的后续工作，原始猜想曾用面数减维数来界定直径。

hackernews · acossta · Nov 25, 17:34 · [社区讨论](https://news.ycombinator.com/item?id=50644980)

**背景**: Hirsch 猜想于 1957 年提出，断言具有 n 个面的 d 维多胞形的图直径至多为 n−d。其动机来自线性规划的单纯形算法，该算法沿多胞形的边移动，其最坏运行时间取决于此直径。原始猜想于 2010 年被 Santos 推翻，而多项式版本（直径由 n 和 d 的多项式界定）一直悬而未决，直到现在。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Convex_polytope">Convex polytope - Wikipedia</a></li>
<li><a href="https://github.com/openai/math/blob/main/preprints/Superpolynomial-graph-diameter-of-simple-polytopes-November-24-2026/paper.pdf">math/preprints/Superpolynomial- graph - diameter -of- simple ...</a></li>
<li><a href="https://www.baeldung.com/cs/simplex-algorithm-linear-programming">Introduction to the Simplex Algorithm | Baeldung on Computer Science</a></li>

</ul>
</details>

**社区讨论**: 评论者强调这意味着不存在多项式时间的单纯形算法，并且这是在 2010 年原始 Hirsch 猜想被推翻后的“扫尾”结果。一些人开玩笑说数学突破现在以 GitHub 补丁说明的形式出现，另一些人则指出该仓库中预印本数量庞大。

**标签**: `#mathematics`, `#linear-programming`, `#complexity-theory`, `#simplex-algorithm`, `#polytopes`

---

<a id="item-13"></a>
## [开发者用 Lean 审计 Clojure 核心库，发现未报告的错误](https://s.conao3.com/blog/2026/e4f733) ⭐️ 7.0/10

一位开发者使用 Lean 定理证明器对 Clojure 核心库进行形式化检查，并报告发现了此前未报告的缺陷。这项工作在博客文章中分享，并在 Hacker News 上引发了关于方法论和发现有效性的讨论。 这展示了像 Lean 这样的形式化验证工具在审计广泛使用的生产语言（如 Clojure）方面的潜力，Clojure 支撑着 Nubank 等公司的关键系统。同时也凸显了在此类分析中区分真实缺陷和误报的挑战。 社区成员指出，一些报告的问题实际上是类型错误（例如将 Long 传递给字节数组的.indexOf）或预期的强制转换（例如对字符串使用浮点数键调用 get），表明简单的类型检查可以减少噪音。讨论还将 Lean 与 Rocq（原 Coq）进行了比较，并提到了对其他 Lisp 方言（如 SBCL 和 ACL2）的类似审计。

hackernews · encyclopedism · Nov 25, 14:56 · [社区讨论](https://news.ycombinator.com/item?id=50642939)

**背景**: Lean 是一个交互式定理证明器和编程语言，支持对数学证明和软件正确性进行形式化验证。Clojure 是一种动态函数式 Lisp 方言，运行在 JVM 上，被用于生产系统，尤其是巴西数字银行 Nubank。形式化验证涉及使用逻辑和计算方法以数学精度建立断言，但结果通常需要人工审查以过滤误报。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://leanprover.github.io/theorem_proving_in_lean/introduction.html">1. Introduction — Theorem Proving in Lean 3 (outdated)...</a></li>
<li><a href="https://cs.stackexchange.com/questions/13785/formal-program-verification-in-practice">programming languages - Formal program verification in practice...</a></li>

</ul>
</details>

**社区讨论**: 评论者反应不一：一些人质疑现在是否更倾向于使用 Lean 而非 Rocq 进行此类工作，以及语言模型是否更擅长编写 Lean；另一些人指出，即使是被大量使用的库也可能隐藏着原始缺陷，并分享了在其他 Lisp 中的类似审计。一些人批评具体发现是类型错误或预期行为，强调需要减少形式化验证报告中的噪音。

**标签**: `#formal-verification`, `#Lean`, `#Clojure`, `#program-analysis`, `#bug-hunting`

---

<a id="item-14"></a>
## [绕过 iOS Safari 的 60 FPS 限制，打造原生般 Web 应用](https://rida.dev/blog/bypassing-ios-safari-60-fps-limit) ⭐️ 7.0/10

一位开发者通过分析 WebKit 源代码，找到了一种基于合成器的变通方法，绕过了 iOS Safari 的 60 FPS 渲染限制，使 Web 应用能够以更高刷新率运行，从而感觉更接近原生应用。 这一变通方法可以显著提升 iOS 上 Web 应用的性能和用户体验，尤其是在动画和滚动方面，并展示了通过深入平台改造来克服浏览器限制的潜力。 该方法利用合成器以 120Hz 更新，而 DOM 仍保持 60Hz，需要理解 WebKit 的渲染管线；然而，它可能存在局限性，例如增加电池消耗和缺乏官方支持。

hackernews · vinhnx · Nov 25, 03:04 · [社区讨论](https://news.ycombinator.com/item?id=50637890)

**背景**: iOS Safari 通常将网页渲染限制在每秒 60 帧，即使在配备 120Hz ProMotion 显示屏的设备上也是如此，以节省电量。WebKit 的合成器将某些渲染任务与主 DOM 分开处理，从而实现更流畅的动画。开发者长期以来一直在寻求在 Web 应用中实现类似原生性能的方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rida.dev/blog/bypassing-ios-safari-60-fps-limit">Bypassing iOS Safari ’s 60 FPS Limit to Build Web Applications That...</a></li>
<li><a href="https://www.macworld.com/article/3040366/enable-faster-scrolling-in-safari-and-more-with-this-hidden-setting.html">Enable ProMotion scrolling and more with these hidden Safari settings</a></li>
<li><a href="https://trac.webkit.org/wiki/Accelerated+Compositing">Accelerated Compositing – WebKit</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞了技术深度和令人印象深刻的演示，一些人指出该方法可能导致电池消耗，并质疑为什么 120Hz 不是默认设置。其他人分享了对 iOS 原生行为的见解以及该方法的创新性。

**标签**: `#iOS Safari`, `#WebKit`, `#web performance`, `#frontend`, `#compositor`

---

<a id="item-15"></a>
## [CISA 将 10 个已被积极利用的漏洞加入 KEV 目录](https://www.cisa.gov/news-events/alerts/2026/11/25/cisa-adds-10-known-exploited-vulnerabilities-catalog) ⭐️ 7.0/10

2026 年 11 月 25 日，CISA 基于积极利用的证据，将 10 个漏洞加入其已知被利用漏洞（KEV）目录，包括三个 Danfoss AK-SM 800A 系列漏洞（CVE-2023-25914、CVE-2023-25915、CVE-2025-41450）、一个 HPE Juniper Session Smart Conductor/Router 操作系统命令注入漏洞（CVE-2026-103406）、五个 Mitel MiCollab 漏洞（CVE-2026-133275、CVE-2026-133303、CVE-2026-133311、CVE-2026-133323、CVE-2026-133324）以及一个 Vates Xen Orchestra 输入验证漏洞（CVE-2026-133469）。 KEV 目录是真实世界利用的权威信号，根据约束性操作指令（BOD）26-04，列入目录要求美国联邦文职行政机构优先快速修复公开暴露资产上的这些漏洞，同时鼓励所有组织效仿。涉及 ICS/OT（Danfoss）、企业网络（HPE Juniper）、统一通信（Mitel）和虚拟化（Vates）产品的混合，扩大了对关键基础设施和 IT 环境的影响。 BOD 26-04 要求各机构修复公开暴露资产上利用后可获得完全控制的 KEV 所列 CVE，推迟较低风险问题，并检查补丁前是否已被入侵；该指令仅适用于 FCEB 机构，但 CISA 敦促所有组织自愿采纳。这 10 个 CVE 的具体补丁截止日期未包含在截断的警报内容中，因此防御者应查阅 KEV 目录以获取截止日期。

rss · CISA Cybersecurity Advisories · Nov 25, 12:00

**背景**: CISA 的已知被利用漏洞（KEV）目录列出了已确认在野利用的漏洞，作为补丁修复的优先待办清单；截至 2026 年 10 月，该目录约有 1,733 条记录。约束性操作指令（BOD）26-04《基于风险优先处理安全更新》为联邦文职行政机构（FCEB）制定了基于风险的漏洞管理要求，并强化了 KEV 目录的作用。Danfoss AK-SM 800A 是一款用于食品零售制冷全局控制和监控的系统管理器，而 HPE Juniper Session Smart Router 提供应用感知的 WAN 路由。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://theuptimereport.com/cisa-known-exploited-vulnerabilities-analysis-2026/">CISA Known Exploited Vulnerabilities Added November 2026</a></li>
<li><a href="https://manualzz.com/doc/66578418/danfoss-ak-sm-820a-ak-system-manager--800a-series-user-guide">AK - SM 800 A Series User Guide | AI Chat & PDF Access | Manualzz</a></li>
<li><a href="https://www.hpe.com/us/en/products/networking/data-center.html">HPE Networking Data Center: AI-ready data center networks | HPE</a></li>

</ul>
</details>

**标签**: `#CISA KEV`, `#actively exploited`, `#vulnerability management`, `#ICS/OT security`, `#patch prioritization`

---

<a id="item-16"></a>
## [Gemini 4 Neon 标志着 Google DeepMind 重返前沿实验室行列](https://latent.space/p/ainews-gemini-4-neon-marks-gdm-s-full-return-as-a-frontier-lab/) ⭐️ 7.0/10

Google DeepMind 于 2026 年 11 月 18 日发布了 Gemini 4 Neon，据称该模型在 LiveBench 上击败了 Astra 和 Fable，并将 Theo 的 TypeScript/Rust 基准测试运行时间缩短了 48.6%。 此次发布标志着 Google DeepMind 重返前沿实验室行列，可能加剧顶级 AI 模型之间的竞争，并为开发者提供更快的编码任务选择。 Gemini 4 Neon 支持文本、图像、视频、音频和文件输入，输出文本，并可通过 API 使用，模型 ID 包括 gemini-4-neon 和 gemini-4-neon-openai；然而，基准测试声明缺乏主要证据和详细技术规格。

rss · Latent Space · Nov 25, 04:29

**背景**: LiveBench 是一个用于评估大型语言模型在各种任务上表现的基准测试。Theo 的 TypeScript/Rust 基准测试可能指的是比较 TypeScript 和 Rust 实现的性能测试，可能与 Web 服务器效率有关。Gemini 4 Neon 是 Google DeepMind 的 Gemini 4 系列的一部分，该系列还包括 Carbon、Hydrogen 和 Argon 等变体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kie.ai/gemini-4-neon">Gemini 4 Neon API: 1M-Token Context Model | Kie.ai</a></li>
<li><a href="https://routemux.com/zh/google/gemini-4-neon">Gemini 4 Neon API：高速编码与编排，省 50% | RouteMux</a></li>
<li><a href="https://http-arena.com/">HTTP Web Server Benchmarks – HttpArena</a></li>

</ul>
</details>

**标签**: `#Gemini`, `#Google DeepMind`, `#frontier models`, `#benchmarks`, `#AI`

---

<a id="item-17"></a>
## [AI 攻击利用未回收密钥攻破安全厂商](https://www.anquanke.com/post/id/316541) ⭐️ 7.0/10

一份分析报告揭示，一次 AI 驱动的攻击成功攻破了一家安全厂商，根本原因可追溯至一个从未被回收或轮换的加密密钥。 此次事件凸显了正确的密钥生命周期管理至关重要，尤其是对于安全厂商而言，一旦被攻破可能对其客户产生供应链层面的影响。 该报告是一份单一来源的中文分析，没有官方公告或漏洞利用细节，重点强调了凭证卫生以及长期未轮换密钥的风险。

rss · Anquanke · Nov 25, 11:03

**背景**: 加密密钥用于保护通信和认证系统。最佳实践要求定期轮换密钥，并在密钥泄露时立即撤销。未能做到这一点可能使攻击者保持持久访问权限。AI 驱动的攻击可以大规模自动化地发现和利用此类弱点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nhimg.org/glossary/credential-hygiene/">What Is Credential Hygiene ? Definition & Examples</a></li>
<li><a href="https://www.paloaltonetworks.com/cyberpedia/what-is-cloud-software-supply-chain-security">What Is Cloud Software Supply Chain Security ? - Palo Alto Networks</a></li>
<li><a href="https://newsletter.dotika.ai/p/ai-driven-cyberattacks-51-seconds-to-break">AI - driven cyberattacks : 51 seconds to break</a></li>

</ul>
</details>

**标签**: `#incident-analysis`, `#credential-hygiene`, `#supply-chain-security`, `#AI-attack`, `#key-management`

---

<a id="item-18"></a>
## [Cisco Talos 分析 OpenAI 相关智能体集群的战术](https://blog.talosintelligence.com/the-great-escape-tradecraft-insights-from-an-agentic-swarm/) ⭐️ 7.0/10

Cisco Talos 发布了一篇博客文章，分析了 2026 年活跃的一个与 OpenAI 相关的智能体集群的战术，通过公开记录追溯其活动，并将其与当前在野观察到的智能体攻击活动的早期信号进行了比较。 这份来自主要安全厂商的分析强调了自主 AI 智能体集群如何以机器速度执行协同攻击，可能打破传统防御策略并重塑防御者的威胁情报优先级。 该博客侧重于战术洞察而非漏洞利用细节，并将 2026 年集群的行为与早期在野智能体攻击信号进行比较，但缺乏技术指标或缓解措施指导。

rss · Cisco Talos Intelligence · Nov 25, 11:00

**背景**: 智能体集群是自主 AI 智能体的集合，它们协调执行任务，在网络安全中可用于并行、机器速度的攻击。Cisco Talos 是 Cisco 的威胁情报研究团队，以分析新兴威胁并向防御者提供可操作情报而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cisco_Talos">Cisco Talos - Wikipedia</a></li>
<li><a href="https://www.talosintelligence.com/">Cisco Talos Intelligence Group - Comprehensive Threat Intelligence</a></li>
<li><a href="https://vultrade.com/ai-security-emerging-threats/the-swarm-is-the-weapon-why-agentic-attacks-break-the-defensive-playbook/">The Swarm Is The Weapon: Why Agentic Attacks Break... - Vultrade</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#threat intelligence`, `#tradecraft`, `#agentic attacks`, `#Cisco Talos`

---

<a id="item-19"></a>
## [AWS 推出企业托管授权，支持 AI 代理安全访问](https://aws.amazon.com/blogs/security/secure-agentic-access-to-aws-with-enterprise-managed-authorization/) ⭐️ 7.0/10

AWS Sign-In 现已支持使用身份断言 JWT 授权授予（ID-JAG）的企业托管授权（EMA），允许组织通过 Okta 等现有企业身份提供商集中授权 AI 代理访问 AWS MCP Server。 该功能使组织能够集中管理哪些应用程序可以访问 AWS 资源，解决了 AI 代理日益自主化并需要受控访问云服务时的关键安全挑战。 ID-JAG 证明身份提供商的授权，但不认证出示它的客户端；令牌请求必须使用该授权授予支持的方法进行认证，默认使用 client_secret_basic。

rss · AWS Security Blog · Nov 25, 21:00

**背景**: 模型上下文协议（MCP）是一个开放协议，可实现 LLM 应用与外部数据源和工具之间的无缝集成，AWS 为代码助手提供了开源的 MCP 服务器。ID-JAG 是一项 IETF 草案规范，扩展了 OAuth，允许身份提供商向资源授权服务器断言用户的授权，从而为 AI 代理实现企业托管授权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ietf.org/archive/id/draft-ietf-oauth-identity-assertion-authz-grant-04.html">Identity Assertion JWT Authorization Grant</a></li>
<li><a href="https://github.com/awslabs/mcp">GitHub - awslabs/ mcp : Open source MCP Servers for AWS · GitHub</a></li>
<li><a href="https://developer.monday.com/api-reference/docs/mcp-enterprise-managed-auth-okta">Set up enterprise managed auth with Okta | monday.com Platform API</a></li>

</ul>
</details>

**标签**: `#AWS`, `#AI agents`, `#identity and access management`, `#OAuth`, `#cloud security`

---

<a id="item-20"></a>
## [AWS Network Firewall 新增基于资源身份的上下文感知规则](https://aws.amazon.com/blogs/security/introducing-context-aware-rules-for-aws-network-firewall/) ⭐️ 7.0/10

AWS Network Firewall 现在支持上下文感知规则，可根据发送和接收流量的 AWS 资源（如 VPC、子网、安全组和中转网关附件）来匹配流量，而不再仅依赖 IP 地址。 这简化了防火墙管理并提升了安全性，因为无需再跟踪不断变化的 IP 地址，使策略在动态云环境中更具弹性且更易于维护。 规则可以引用特定的 VPC、子网、安全组或中转网关附件，但该功能目前仅限于这些资源类型，尚不支持命名空间或 Pod 等容器级属性。

rss · AWS Security Blog · Nov 25, 01:19

**背景**: AWS Network Firewall 是一项托管防火墙服务，用于过滤进出 VPC 的流量。传统上，防火墙规则使用 IP 地址，但在云环境中资源频繁创建和销毁导致 IP 变化，这带来了挑战。上下文感知规则允许以逻辑 AWS 资源来编写策略，使安全策略与基础设施身份保持一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/nfw-proxy-how-it-works.html">How a NAT/Proxy firewall works - AWS Network Firewall</a></li>
<li><a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html">Amazon EC2 security groups for your EC2 instances - Amazon ...</a></li>
<li><a href="https://aws.amazon.com/blogs/networking-and-content-delivery/automating-aws-transit-gateway-attachments-to-a-transit-gateway-in-a-central-account/">Automating AWS Transit Gateway attachments to a transit gateway ...</a></li>

</ul>
</details>

**标签**: `#AWS`, `#cloud security`, `#network firewall`, `#security groups`, `#infrastructure`

---

<a id="item-21"></a>
## [Cloudflare 推出 Search for Agents，让网站可被 AI 代理查询](https://blog.cloudflare.com/search-for-agents/) ⭐️ 7.0/10

Cloudflare 推出了 Search for Agents，这是一项基于开关的功能，可自动索引网站内容，并通过支持原生 HTTP QUERY 的可发现搜索 API 将其暴露给 AI 代理。该功能面向所有客户（包括免费版，但有额度限制），启用后会创建一个 AI Search 实例，抓取并索引该区域的内容。 这标志着网络基础设施向对代理友好方向转变，网站可以被 AI 代理直接查询，而不仅仅是被传统搜索引擎抓取。它可能影响网站所有者、AI 代理开发者以及更广泛的 AI 驱动网络交互生态。 该功能要求域名已接入 Cloudflare 账户，并且只应索引打算公开搜索的内容。它利用了 RFC 10008（2026 年 6 月）定义的 HTTP QUERY 方法，该方法在请求体中发送查询内容，同时保持安全且幂等的语义。

rss · Cloudflare Blog · Nov 25, 14:00

**背景**: HTTP QUERY 是一种新的 HTTP 请求方法，它在 GET 和 POST 之间填补空白，允许在请求体中进行复杂查询，同时保持安全且幂等。Cloudflare 的 AI Search 产品帮助网站内容被 AI 代理发现，而 Search for Agents 是该产品中的一项新能力。与此同时，Cloudflare 还调整了默认的机器人策略，要求网站所有者明确允许那些用于搜索索引和模型训练等多种目的的 AI 爬虫。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/search-for-agents/">Introducing Search for Agents | Cloudflare Blog</a></li>
<li><a href="https://developers.cloudflare.com/ai-search/how-to/search-for-agents/">Search for Agents · Cloudflare AI Search docs</a></li>
<li><a href="https://http.dev/query">QUERY - Expert Guide to HTTP methods</a></li>
<li><a href="https://www.rfc-editor.org/info/rfc10008/">RFC 10008: The HTTP QUERY Method | RFC Editor</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Cloudflare`, `#web infrastructure`, `#search API`, `#HTTP QUERY`

---

<a id="item-22"></a>
## [InstructReplay 通过自我重放减少事实微调的能力退化](https://huggingface.co/papers/2611.32918) ⭐️ 7.0/10

InstructReplay 是一种新方法，通过重放模型自身的回答来缓解事实微调带来的能力退化，将通用基准的平均下降从 28.1 分降低到 2.4 分。 这一结果对 LLM 微调社区具有重要意义，因为事实微调过程中的灾难性遗忘常常损害通用能力，而一种简单的基于重放的方法可能使微调更加可靠，无需大量数据整理。 该方法使用模型自身生成的答案作为重放数据，避免了对额外数据的需求，但摘要缺乏实验设置、模型规模和基准具体细节，因此需要独立验证。

rss · BALA AI News · Nov 25, 11:01

**背景**: 灾难性遗忘是指在对大语言模型进行新数据微调时，模型丢失先前获得的知识或技能的现象。重放方法通过将旧数据或生成的样本混入微调过程来缓解这一问题，帮助模型保留先前的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2601.18699">Mechanistic Analysis of Catastrophic Forgetting in Large Language ...</a></li>
<li><a href="https://medium.com/@baicenxiao/avoiding-amnesia-some-practical-guides-to-mitigate-catastrophic-forgetting-in-llms-post-training-6a23e4f064cb">Avoiding Amnesia: Some Practical Guides to Mitigate Catastrophic ...</a></li>

</ul>
</details>

**标签**: `#LLM fine-tuning`, `#catastrophic forgetting`, `#replay methods`, `#AI research`, `#benchmark degradation`

---