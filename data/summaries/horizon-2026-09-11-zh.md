# Horizon 每日速递 - 2026-09-11

> From 7 items, 2 important content pieces were selected

---

1. [Datasette 发布 1.0a39 与 0.65.4 安全补丁，修复私有表暴露漏洞](#item-1) ⭐️ 7.0/10
2. [Dify 1.6.1 仍存在未授权 SSRF 与沙箱逃逸漏洞](#item-2) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Datasette 发布 1.0a39 与 0.65.4 安全补丁，修复私有表暴露漏洞](https://simonwillison.net/2026/Sep/11/datasette-security/) ⭐️ 7.0/10

Datasette 发布了两个安全补丁版本：面向 alpha 系列的 1.0a39 和面向稳定版 0.65.x 系列的 0.65.4，修复了在同时包含公开表和私有表的实例中可能暴露私有表的隐蔽漏洞。此次修复源于 Sevban Dönmez 报告的问题，Simon Willison 与 Alex Garcia 使用 Claude Fable 5.1、GPT-5.6 和 GPT-6 Astra 进行了大规模审计，并花了近一周时间协作审查修复方案。 任何在公网运行、且同时包含公开表和私有表的 Datasette 实例都应立即应用这些补丁，因为这些漏洞可能导致私有数据泄露。此次发布也标志着开源开发流程正更广泛地转向将前沿模型的安全审计纳入日常工作。 审计在一个共享的私有代码库中进行，两位开发者分工协作：一人编写暴露问题的自动化测试，另一人实现修复，从而确保每个问题都经过两名人类以及多个不同模型的编码代理审查。Willison 表示，团队今后将把前沿模型的安全审计纳入所有开发工作。

rss · Simon Willison · Sep 11, 03:27

**背景**: Datasette 是一个基于 SQLite 的开源 Python 工具，用于探索、浏览和发布数据，通常以 Web 服务形式部署。它支持访问控制，允许部分表公开、部分表保持私有，而此前曾出现过影响部署实例的漏洞，例如开放重定向漏洞（CVE-2025-64481）。由于单个实例可能同时提供公开和私有数据，权限检查中的细微缺陷可能带来严重后果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/simonw/datasette/security">Security Overview · simonw/ datasette · GitHub</a></li>
<li><a href="https://app.opencve.io/cve/CVE-2025-64481">CVE-2025-64481 - Vulnerability Details - OpenCVE</a></li>
<li><a href="https://selfhostedworld.com/software/datasette">Datasette - Self-hosted software</a></li>

</ul>
</details>

**标签**: `#security`, `#datasette`, `#open-source`, `#vulnerability`, `#release`

---

<a id="item-2"></a>
## [Dify 1.6.1 仍存在未授权 SSRF 与沙箱逃逸漏洞](https://xz.aliyun.com/news/92812) ⭐️ 7.0/10

安全研究人员报告称，Dify 1.6.1 版本中存在一个未授权 SSRF 漏洞，其触发地址与之前已修补的 CVE-2025-29720 和 CVE-2025-56520 相同，表明修复并不完整。第二个漏洞位于代码沙箱的网络访问中，攻击者只需创建节点即可实现 SSRF 和命令执行。 Dify 是一个被广泛使用的开源 LLM 应用平台，这些漏洞可能让攻击者进入内网或对受影响的部署执行任意命令。同一个 SSRF 问题在两次 CVE 修补后再次出现，说明存在系统性的修复缺陷，使所有 Dify 用户面临风险。 该 SSRF 无需认证，且与 CVE-2025-29720 和 CVE-2025-56520 共享同一端点；沙箱漏洞则绕过了网络限制，同时实现 SSRF 和命令执行。报告内容简短，缺乏详细的技术分析，但作者指出该问题在很新的版本中依然存在，暗示之前的补丁无效。

rss · Aliyun Xianzhi Community · Sep 11, 01:40

**背景**: SSRF（服务端请求伪造）允许攻击者让服务器向内部或原本不可达的资源发起请求，常用于探测内网或云元数据服务。Dify 的代码沙箱设计用于隔离运行用户代码，阻止文件系统访问、对外网络请求和系统命令；一旦隔离失效，就可能导致 SSRF 和远程命令执行。CVE-2025-29720 是 2025 年 4 月披露的 Dify SSRF 漏洞，CVE-2025-56520 则是相关的后续漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nvd.nist.gov/vuln/detail/CVE-2025-29720">NVD - CVE - 2025 - 29720</a></li>
<li><a href="https://docs.dify.ai/en/cloud/use-dify/nodes/code">Code - Dify Docs</a></li>
<li><a href="https://deepwiki.com/Winson-030/dify-kubernetes/2.5-security-and-isolation">Security and Isolation | Winson-030/ dify -kubernetes | DeepWiki</a></li>

</ul>
</details>

**标签**: `#security`, `#SSRF`, `#vulnerability`, `#Dify`, `#code-sandbox`

---

