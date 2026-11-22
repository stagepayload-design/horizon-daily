# Horizon 每日速递 - 2026-11-22

> From 45 items, 7 important content pieces were selected

---

1. [Lean 形式化验证黎曼假设引热议](#item-1) ⭐️ 9.0/10
2. [GPGME 严重漏洞可能导致远程代码执行](#item-2) ⭐️ 8.0/10
3. [Anthropic 敲响纳斯达克开市钟，据称创 IPO 规模纪录](#item-3) ⭐️ 8.0/10
4. [显示器 USB-C 以太网集线器导致下载速度下降 75%](#item-4) ⭐️ 7.0/10
5. [用 Go 语言编写 PostgreSQL 扩展的新方法](#item-5) ⭐️ 7.0/10
6. [Upload2Shell (CVE-2026-125396)：Ghostscript 沙箱逃逸暴露文件处理风险](#item-6) ⭐️ 7.0/10
7. [Muru：AI 辅助的 Rust 服务器，用于运行 ASGI/WSGI Python 应用](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Lean 形式化验证黎曼假设引热议](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) ⭐️ 9.0/10

据报道，黎曼假设（或其广义形式 GRH）已在 Lean 中完成形式化验证，社区讨论表明该证明涉及对现代数学一大部分的 AI 辅助形式化。 若得到确认，这将是形式数学和 AI 辅助定理证明领域的范式转变里程碑，可能验证 AI 在大规模数学形式化中的作用，并引发关于检查器可靠性和贡献归属的新问题。 该结果的可靠性存在争议：多个具有自洽性证明的独立检查器（如 con-leche 和 con-ron）使得基于漏洞的反驳可能性极低，但过去曾有虚假的 Collatz 反驳通过检查器的事件，凸显了残余风险；据报道有人类专家参与其中。

hackernews · g-b-r · Nov 21, 14:36 · [社区讨论](https://news.ycombinator.com/item?id=50589618)

**背景**: 黎曼假设由黎曼于 1859 年提出，断言黎曼ζ函数的所有非平凡零点的实部均为 1/2，是克雷数学研究所的千禧年大奖难题之一。Lean 是一个交互式定理证明器，拥有一个小的可信内核来检查每一步推理，其数学库 Mathlib 被广泛用于数学形式化。在 Lean 中进行形式化验证意味着将证明编码为精确的逻辑术语，以便内核能够机械地验证它。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Riemann_hypothesis">Riemann hypothesis - Wikipedia</a></li>
<li><a href="https://www.claymath.org/millennium/riemann-hypothesis/">Riemann Hypothesis - Clay Mathematics Institute</a></li>
<li><a href="https://leanprover.github.io/theorem_proving_in_lean/introduction.html">1. Introduction — Theorem Proving in Lean 3 (outdated)...</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了检查器的独立性和可靠性，指出尽管多个独立实现使得基于漏洞的反驳不太可能，但过去曾有虚假证明（如 Collatz）通过检查器；其他人强调了形式化数学的巨大范围，并将功劳归于指导 AI 的人类专家 Levent，同时有人担忧可能出现的单一文化并提出了后续问题。

**标签**: `#formal-verification`, `#Lean`, `#Riemann-Hypothesis`, `#AI-for-math`, `#theorem-proving`

---

<a id="item-2"></a>
## [GPGME 严重漏洞可能导致远程代码执行](https://lists.gnupg.org/pipermail/gnupg-announce/2026q4/000517.html) ⭐️ 8.0/10

GPGME 是 GnuPG 的高层加密 API 的 C 语言库，其一个严重漏洞于 2026 年 11 月 20 日被披露，此前 GitLab 于 2026 年 11 月 12 日向 GnuPG 团队报告了该问题。GitLab 和 Red Hat 已提供补丁，且由于另一个 Ruby2Shell 漏洞，披露时间从原定的 2026 年 11 月 25 日提前。 GPGME 被广泛的应用所使用，包括大多数邮件客户端、许多 XMPP 客户端、Samba、Flatpak、Gpg4win 和 GnuPG Desktop，因此一个可能导致远程代码执行的漏洞会使大量软件面临风险。GitLab 通过 GPGME 支持签名提交，这凸显了在敏感开发工作流中代码执行的潜在可能。 根本原因涉及两个从 gpg 读取状态行和密钥列表的 GPGME 内部函数，并且不能排除利用该漏洞发起远程代码执行攻击的可能性。所有使用 2.3.0 之前版本的 GPGME 的软件，无论是作为共享库、DLL 还是静态链接，都会受到影响。

hackernews · gdgghhhhh · Nov 21, 08:32 · [社区讨论](https://news.ycombinator.com/item?id=50587208)

**背景**: GPGME（GnuPG Made Easy）是一个 C 语言库，为应用程序提供高层 API，以便使用 GnuPG 作为后端执行加密、解密和签名等加密操作。它是许多依赖 OpenPGP 标准的开源和商业产品中的基础组件。协调披露是指漏洞发现者与供应商私下合作，在公开细节之前修复漏洞的过程，旨在降低风险并确保补丁就绪。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/news/GnuPG-GPGME-Critical">GnuPG's GPGME Affected By Critical Security Bug In Turn... - Phoronix</a></li>
<li><a href="https://www.gnupg.org/documentation/manuals/gpgme/">Top (The ‘ GnuPG Made Easy’ Reference Manual)</a></li>
<li><a href="https://github.com/gpg/gpgme">GitHub - gpg/ gpgme : GnuPG Made Easy. NOTE: Maintainers are not...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，据称 Red Hat 五年前就在其打包中修复了该问题，但上游错过了；同时有人争论该漏洞究竟是真正的远程代码执行还是仅仅是一个双重释放错误。一些人对没有 Rust 级别工具的 C/C++ 代码的安全性表示担忧，另一些人则要求澄清哪些软件受到影响。

**标签**: `#GnuPG`, `#GPGME`, `#RCE`, `#vulnerability`, `#coordinated disclosure`

---

<a id="item-3"></a>
## [Anthropic 敲响纳斯达克开市钟，据称创 IPO 规模纪录](https://www.tmtpost.com/8213535.html) ⭐️ 8.0/10

一则简短的新闻声称 Anthropic 已在纳斯达克上市，并创下史上最大规模 IPO 纪录，但未提供财务细节、日期或一手信源。 若消息属实，像 Anthropic 这样的领先 AI 实验室创纪录的 IPO 将是一个重大行业事件，可能重塑 AI 融资和公开市场动态，但目前该说法未经证实，且仅基于一份单薄的二手聚合报道。 该消息缺乏一手证据、财务数据或佐证，且来自二手聚合源（BALA AI News via tmtpost），因此可信度有限；没有 Anthropic 或纳斯达克的官方确认。

rss · BALA AI News · Nov 21, 13:31

**背景**: Anthropic 是一家 AI 安全与研究公司，以开发 Claude 等大型语言模型而闻名。IPO（首次公开募股）是私营公司首次向公众出售股份并成为上市公司的过程，通常是一个重要的里程碑，可提供资本和流动性。纳斯达克是美国主要的证券交易所之一，许多科技公司在此上市。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/">Home \ Anthropic</a></li>
<li><a href="https://www.bloomberg.com/features/2026-how-ipos-work/">What Is an IPO ? How Initial Public Offerings Work</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#IPO`, `#AI industry`, `#Nasdaq`, `#funding`

---

<a id="item-4"></a>
## [显示器 USB-C 以太网集线器导致下载速度下降 75%](https://blog.tymscar.com/posts/studiodisplayethernet/) ⭐️ 7.0/10

一位博主发现，通过 USB-C 显示器连接以太网会增加延迟，导致数据包丢失，下载速度下降 75%。通过使用需要更少确认的不同以太网适配器解决了该问题。 这凸显了 USB-C 集线器和扩展坞的隐藏性能陷阱，这些设备在现代笔记本电脑中越来越常见。用户可能因 USB、以太网和供电之间的不透明交互而不知不觉地遭受网络性能下降。 显示器集线器增加的延迟使笔记本电脑无法及时确认数据包，填满了以太网适配器的缓冲区并导致数据包丢失。切换到具有不同缓冲特性的适配器解决了问题。

hackernews · soheilpro · Nov 21, 10:36 · [社区讨论](https://news.ycombinator.com/item?id=50587875)

**背景**: USB-C 显示器通常包含内置集线器，通过单根电缆提供以太网、USB 端口和供电。然而，这些集线器可能引入额外的延迟和复杂性，影响网络性能。TCP 吞吐量对数据包丢失很敏感，而数据包丢失可能由网络适配器中的缓冲区溢出引起。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://discussions.apple.com/thread/7787638">USB - C ethernet pass through via Ultrafine… - Apple Community</a></li>
<li><a href="https://www.creativebloq.com/reviews/dell-p2723de">This 27-inch monitor has plenty going for it , not least the USB - C hub.</a></li>

</ul>
</details>

**社区讨论**: 评论者澄清问题是由于延迟增加导致缓冲区溢出和数据包丢失，一些人分享了类似的调试经历。一位评论者指出显示器方面无关紧要，因为这本质上是 USB 网络交换机的问题。

**标签**: `#networking`, `#USB`, `#hardware-debugging`, `#packet-loss`, `#hackernews`

---

<a id="item-5"></a>
## [用 Go 语言编写 PostgreSQL 扩展的新方法](https://jespino.github.io/gopgext/) ⭐️ 7.0/10

一个名为 gopgext 的新项目展示了如何用 Go 语言编写 PostgreSQL 扩展，并分享了相关技术和代码示例。作者 jespino 此前曾用 Go 开发 Linux 内核模块，显示出将 Go 推向底层系统编程的丰富经验。 这一点很重要，因为 PostgreSQL 扩展传统上用 C 语言编写，或越来越多地使用 Rust（通过 pgrx），而 Go 提供了一种更安全、更高效的替代方案，具有垃圾回收和丰富的生态系统。如果成功，它可以降低 Go 开发者贡献 PostgreSQL 扩展的门槛，从而可能增加可用扩展的数量和多样性。 由于 C ABI 和运行时约束（如垃圾回收和 goroutine 调度）可能干扰 PostgreSQL 的内存管理和信号处理，用 Go 编写 PostgreSQL 扩展颇具挑战性。该项目可能通过精心集成来解决这些问题，但性能开销和与 PostgreSQL 内部机制的兼容性仍是关键考量。

hackernews · valyala · Nov 21, 17:08 · [社区讨论](https://news.ycombinator.com/item?id=50591260)

**背景**: PostgreSQL 是一个高度可扩展的数据库，允许用户通过扩展添加新功能，这些扩展通常用 C 语言编写并动态加载。pgrx 是一个流行的框架，用于用 Rust 编写 PostgreSQL 扩展，提供了比 C 更安全的替代方案。Go 是一种静态类型、编译型语言，以其简单性和并发支持而闻名，但由于其运行时和垃圾回收器，它通常不用于数据库扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=50591260">PostgreSQL Extensions in Go | Hacker News</a></li>
<li><a href="https://whatisgithub.com/pgcentralfoundation/pgrx">What is pgrx ? · whatisgithub</a></li>

</ul>
</details>

**社区讨论**: 社区反应积极，用户对简化 PostgreSQL 扩展编写表示兴奋，但也有人指出出于性能考虑仍会选择 pgrx。其他人提到了相关项目如 plgo（一个用于编写 PostgreSQL 扩展的 Go 库）以及作者之前用 Go 开发 Linux 内核模块的工作，凸显了使用 Go 进行底层系统编程的日益增长的兴趣。

**标签**: `#PostgreSQL`, `#Go`, `#extensions`, `#database`, `#tooling`

---

<a id="item-6"></a>
## [Upload2Shell (CVE-2026-125396)：Ghostscript 沙箱逃逸暴露文件处理风险](https://pwn.ai/upload2shell) ⭐️ 7.0/10

一篇详细分析文章披露了“Upload2Shell”漏洞（CVE-2026-125396），这是 Ghostscript 10.08.0 之前版本中一个-dSAFER 绕过漏洞，可通过.putgstringcopy 和.forceput 恢复实现沙箱逃逸至代码执行。该漏洞影响 Ghostscript、ImageMagick 和 FFmpeg 等广泛部署的文件处理工具，CVSS 评分为 8.5（高危）。 该漏洞意义重大，因为 Ghostscript 是唯一广泛使用的 PostScript 解释器，常被图像和文档处理流水线调用，因此沙箱逃逸可能导致在处理不可信文件时发生远程代码执行。它凸显了在缺乏强隔离的环境中执行复杂文件格式的系统性风险。 该漏洞是 Ghostscript 10.08.0 之前版本中的-dSAFER 绕过，截至 2026 年 11 月 10 日尚无已知利用，CVSS 评分为 8.5。CVE 编号似乎日期超前，且该文章被批评为难以阅读，缺乏明确的补丁细节或利用状态。

hackernews · f311a · Nov 21, 18:29 · [社区讨论](https://news.ycombinator.com/item?id=50592097)

**背景**: Ghostscript 是 PostScript 和 PDF 文件的解释器，其-dSAFER 选项旨在处理不可信文档时限制文件操作。然而，PostScript 是一种完整的编程语言，安全地沙箱化它非常困难；Ghostscript 内置的沙箱已多次被绕过。像 ImageMagick 和 FFmpeg 这样的文件处理工具通常将 PostScript/PDF 处理委托给 Ghostscript，因此 Ghostscript 中的漏洞可能传播到许多应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cve.now/CVE-2026-125396">CVE - 2026 - 125396 : Ghost PDL sandbox escape to code execution</a></li>
<li><a href="https://cve.radio/cve/CVE-2026-125396/">CVE - 2026 - 125396 , CVSS 8.5 High, ArtifexSoftware... | cve.radio</a></li>
<li><a href="https://ghostscript.com/security/">Ghostscript : Security Vulnerability Policy</a></li>

</ul>
</details>

**社区讨论**: 评论者批评文章的时间线难以阅读，呼吁提供受影响版本和补丁日期的清晰表格。他们还讨论了 Ghostscript 因 PostScript 是编程语言而固有的安全问题，并建议在严格的 seccomp+landlock 沙箱中运行文件处理工具，或从库中移除十年前的遗留代码。

**标签**: `#vulnerability`, `#ghostscript`, `#sandboxing`, `#file-processing`, `#security`

---

<a id="item-7"></a>
## [Muru：AI 辅助的 Rust 服务器，用于运行 ASGI/WSGI Python 应用](https://simonwillison.net/2026/Nov/21/muru/) ⭐️ 7.0/10

mod_wsgi 的创建者 Graham Dumpleton 发布了 Muru，这是一个 AI 辅助的 Rust 服务器，用于在开发和 生产环境中运行 ASGI 和 WSGI Python 应用。他在 2026 年 11 月 4 日至 11 月 21 日期间发布了 18 篇异常详细的公开开发日志，记录了该项目的开发过程。 Muru 将二十年的生产环境 Python 服务经验带入现代 Rust 服务器，可能为传统 WSGI 和现代 ASGI 应用提供统一解决方案。其详细的公开开发日志为 Python Web 基础设施社区提供了宝贵的技术见解。 开发日志涵盖工作进程内部机制、一次导入多次 fork、开发环境中的 HTTPS、同时运行 WSGI 和 ASGI、无需重启的发布、无需服务网格的金丝雀部署、Kubernetes 集成、缩容到零，以及带追踪的每页工具栏等主题。Dumpleton 强调，虽然 AI 协助完成了大量工作，但判断什么才算足够好仍依赖于他二十年 mod_wsgi 经验所形成的判断力。

rss · Simon Willison · Nov 21, 23:56

**背景**: WSGI（Web 服务器网关接口）是 2003 年创建的用于托管 Python Web 应用的规范，mod_wsgi 是其最古老的主流实现，用于 Apache HTTP 服务器。ASGI（异步服务器网关接口）是较新的标准，支持异步 Python Web 框架。Graham Dumpleton 是一位知名的 Python 开发者，他还创建了 wrapt 库，并此前发布了 wrapture——一个 AI 辅助的 monkey patch 和追踪工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.deployhq.com/blog/python-application-servers-wsgi-vs-asgi-guide">Python Application Servers in 2026: WSGI vs ASGI , Gunicorn to...</a></li>
<li><a href="https://grahamdumpleton.me/posts/2026/08/introducing-wrapture/">Introducing wrapture - Graham Dumpleton</a></li>
<li><a href="https://simonwillison.net/2026/Aug/31/introducing-wrapture/">Introducing wrapture | Simon Willison’s Weblog</a></li>

</ul>
</details>

**标签**: `#python`, `#asgi`, `#wsgi`, `#rust`, `#web-servers`

---

