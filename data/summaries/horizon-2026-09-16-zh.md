# Horizon 每日速递 - 2026-09-16

> From 3 items, 1 important content pieces were selected

---

1. [Cisco 邮件网关 9.8 分漏洞遭在野利用：一封邮件即可获取 root 权限](#item-1) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Cisco 邮件网关 9.8 分漏洞遭在野利用：一封邮件即可获取 root 权限](https://www.anquanke.com/post/id/316111) ⭐️ 8.0/10

Cisco 已确认 CVE-2026-76461 正在被在野利用。这是 Cisco Secure Email Gateway 所用 AsyncOS 中的一个严重 SQL 注入漏洞（CVSS 评分 9.8），未经身份验证的攻击者只需发送一封精心构造的邮件，即可在底层操作系统上以 root 权限执行任意命令。Cisco Secure Email and Web Manager 与 Cisco Secure Web Appliance 被报告不受该漏洞影响，Cisco 已在安全公告中发布修复版本。 邮件网关按设计必须位于网络边界并接受来自公网的 SMTP 连接，因此任何未修补的设备都可被攻击者直接触达，且无需身份验证或用户交互，这对使用 Cisco Secure Email Gateway 的企业构成高风险。一旦利用成功，攻击者将完全以 root 权限控制这台边界主机，可能借此进行横向移动、拦截邮件并进一步入侵内网。 该漏洞是设备邮件解析逻辑中的预认证 SQL 注入（CWE-89），可升级为在底层操作系统上以 root 权限执行任意命令，无需登录也无需用户点击。无法立即修补的管理员被建议将管理平面从互联网上撤下，并把 SMTP 和 HTTP 监听器限制为仅接受已知中继和负载均衡器的连接。

rss · Anquanke · Sep 16, 10:26

**背景**: Cisco Secure Email Gateway 是一款基于 Cisco AsyncOS 操作系统的邮件安全设备，用于过滤进出邮件中的钓鱼、恶意软件等威胁。CVSS 评分 9.8（满分 10）代表严重级别的漏洞，而“在野利用”意味着已有真实攻击者在使用该漏洞，而不仅仅是研究人员。SQL 注入是一类将不可信输入当作数据库命令执行的漏洞，而在此漏洞中，触发点正是邮件正文本身的内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehackernews.com/2026/09/cisco-secure-email-gateway-flaw.html">Cisco Secure Email Gateway Flaw Exploited in the Wild, Enables...</a></li>
<li><a href="https://www.cycognito.com/blog/emerging-threat-cve-2026-76461-cisco-secure-email-gateway-root-rce-via-email-parsing/">Emerging Threat: (CVE-2026-76461) Cisco Secure Email Gateway ...</a></li>
<li><a href="https://yusmpgroup.com/news/cisco-secure-email-gateway-rce-exploited">Cisco Secure Email Gateway RCE Exploited | YuSMP</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#Cisco`, `#exploit`, `#email gateway`

---

