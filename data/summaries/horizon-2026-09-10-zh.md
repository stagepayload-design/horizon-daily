# Horizon 每日速递 - 2026-09-10

> From 4 items, 2 important content pieces were selected

---

1. [不解密 HTTPS 也能识别内网大模型 API 流量](#item-1) ⭐️ 8.0/10
2. [CVE-2026-71486：vLLM derender 端点可被用于资源耗尽攻击](#item-2) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [不解密 HTTPS 也能识别内网大模型 API 流量](https://xz.aliyun.com/news/92806) ⭐️ 8.0/10

一篇技术深度文章展示了如何在不进行 HTTPS 解密、不安装终端插件的情况下，仅通过分析 DNS、SNI、JA3、HTTP 和 SSE 五层流量特征来识别内网大模型 API 的使用。作者用四道 Suricata 规则闸门回放混合 pcap 抓包，得到六条告警全部为真阳性，并在 12 个主流站点及 pip 装包场景下实现零误报。 随着企业越来越多地通过大模型 API 传输敏感数据，安全团队需要能够发现隔离网段内未经授权或影子 AI 使用的手段。该方法提供了一种无需终端代理、即使 TLS 加密阻断载荷检查也能生效的实用监控方案，对网络安全和 AI 基础设施治理具有重要价值。 检测依赖多层指纹：DNS 查询、TLS SNI、JA3 客户端指纹、HTTP 头部以及 SSE 流式模式。作者指出 DoH 只能拆掉 DNS 这一道闸门，而 IP 直连配合前置代理会让 DNS 和 SNI 同时失效，说明该方法存在已知的绕过局限。

rss · Aliyun Xianzhi Community · Sep 10, 03:55

**背景**: JA3 是一种通过对 TLS ClientHello 消息字段进行哈希来为客户端生成指纹的方法，可在发送任何 HTTP 数据之前识别软件类型。Suricata 是一款开源 IDS/IPS，通过签名规则匹配网络流量；SSE（Server-Sent Events）是一种基于文本的协议，常被大模型 API 用于在长连接 HTTP 上逐 token 流式返回响应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://browserleaks.com/tls">TLS Client Test - TLS Fingerprinting - BrowserLeaks</a></li>
<li><a href="https://docs.suricata.io/en/latest/rules/index.html">8. Suricata Rules — Suricata 9.0.0-dev documentation</a></li>
<li><a href="https://hpbn.co/server-sent-events-sse/">Browser APIs and Protocols : Server - Sent Events ( SSE ) - High...</a></li>

</ul>
</details>

**标签**: `#LLM API detection`, `#network security`, `#traffic analysis`, `#Suricata`, `#HTTPS bypass`

---

<a id="item-2"></a>
## [CVE-2026-71486：vLLM derender 端点可被用于资源耗尽攻击](https://xz.aliyun.com/news/92805) ⭐️ 7.0/10

编号为 CVE-2026-71486 的漏洞影响 0.26.0 之前的 vLLM 版本：两个 derender 端点会接受调用方提交的嵌套 GenerateResponse 对象，并在资源边界校验之前执行去分词、logprob 处理以及 OpenAI 兼容响应构造。拥有 API 访问权限的客户端因此可以提交格式合法但规模异常的 JSON，抢占 CPU、内存、响应缓冲与带宽，从而影响同一实例上的其他请求。 vLLM 是被广泛使用的高吞吐 LLM 推理与服务引擎，其 API 面上的资源耗尽漏洞会直接影响生产环境中的 LLM 服务可用性。任何低于 0.26.0 且向已认证客户端暴露 derender 路由的部署，都应把升级和路由收敛列为近期优先事项。 该漏洞被归类为“资源分配无限制或节流”，端点在处理超大对象时未强制执行输出边界或响应大小限制。利用该漏洞需要能够访问这两个 derender 端点的已认证 API 客户端，因此实际暴露面取决于这些路由是否启用且可达。

rss · Aliyun Xianzhi Community · Sep 10, 02:17

**背景**: vLLM 是一个开源、高吞吐且内存高效的大语言模型推理与服务引擎。其 derender 端点属于辅助 API，用于把内部的 GenerateResponse 对象转换回去分词文本以及 OpenAI 兼容的响应格式。由于这一转换发生在资源限制生效之前，客户端只需发送一个非常大的嵌套负载，就能迫使服务端进行高开销处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xz.aliyun.com/news/92805">从一个辅助 API 看资源边界： CVE - 2026 - 71486 （ vLLM ）-先知社区</a></li>
<li><a href="https://access.redhat.com/security/cve/cve-2026-71486">CVE - 2026 - 71486 - Red Hat Customer Portal</a></li>
<li><a href="https://security.snyk.io/vuln/SNYK-PYTHON-VLLM-18912241">Allocation of Resources Without Limits or Throttling in vllm | Snyk</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#security`, `#CVE`, `#resource-exhaustion`, `#LLM-serving`

---

