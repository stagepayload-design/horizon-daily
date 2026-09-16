# Horizon 每日速递 - 2026-09-14

> From 4 items, 1 important content pieces were selected

---

1. [ComfyUI 9.3 反序列化 RCE 实测：官方未当作漏洞修复的"唯一漏网之鱼"](#item-1) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ComfyUI 9.3 反序列化 RCE 实测：官方未当作漏洞修复的"唯一漏网之鱼"](https://xz.aliyun.com/news/92827) ⭐️ 8.0/10

一份实测报告披露了 CVE-2026-68771，这是一个影响 ComfyUI v0.22.0 至 v0.25.0 的反序列化远程代码执行漏洞，该漏洞在 v0.26.0 中被修复，但据称官方并未将其视为安全问题处理。所有测试均在本地隔离虚拟机中进行，作者也提醒不要对未授权目标进行复现。 ComfyUI 是广泛用于 Stable Diffusion 及其他生成式 AI 工作流的节点式界面，因此其中的未授权 RCE 漏洞可能使自托管实例面临系统被完全攻陷的风险。官方未将该缺陷视为安全问题处理的说法，也引发了人们对快速演进的 AI 工具生态中漏洞披露与补丁管理实践的担忧。 根据漏洞数据库信息，该缺陷位于 LoadTrainingDataset 节点，其 execute() 函数使用 torch.load(f) 从服务器输出目录加载数据集分片，从而启用了不安全的 pickle 反序列化。该漏洞被描述为无需认证，即攻击者无需有效凭据即可触发，影响版本为 v0.22.0 至 v0.25.0，并在 v0.26.0 中修复。

rss · Aliyun Xianzhi Community · Sep 14, 01:19

**背景**: ComfyUI 是一个开源、基于节点的图形界面，用于构建和运行生成式 AI 图像与视频流水线，用户通常在自己的机器或服务器上自行托管。反序列化漏洞发生在应用程序从不受信任的数据重建对象时，而在 Python 中，pickle 格式尤其危险，因为它在加载过程中可以执行任意代码。远程代码执行（RCE）是最严重的一类漏洞之一，因为它允许攻击者在目标系统上运行命令。CVE 编号是分配给公开披露安全缺陷的标准标识符。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://app.opencve.io/cve/CVE-2026-68771">CVE - 2026 - 68771 - Vulnerability Details - OpenCVE</a></li>
<li><a href="https://vulmon.com/vulnerabilitydetails?qid=CVE-2026-68771">CVE - 2026 - 68771 - Unsafe Deserialization Remote Code</a></li>
<li><a href="https://www.rapid7.com/db/vulnerabilities/cve-2026-68771/">CVE - 2026 - 68771 : Comfy -Org... | Rapid7 Vulnerability Database</a></li>

</ul>
</details>

**标签**: `#security`, `#vulnerability`, `#RCE`, `#ComfyUI`, `#AI/ML`

---

