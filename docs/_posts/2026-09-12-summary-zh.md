---
layout: default
title: "Horizon Summary: 2026-09-12 (ZH)"
date: 2026-09-12
lang: zh
---

> From 3 items, 2 important content pieces were selected

---

1. [DeepSeek v4.1-Flash：763B MoE，采用全新因果编码器-解码器架构并支持视觉](#item-1) ⭐️ 8.0/10
2. [Perplexity 将端到端系统托付给 GPT-6 Astra](#item-2) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [DeepSeek v4.1-Flash：763B MoE，采用全新因果编码器-解码器架构并支持视觉](https://www.latent.space/p/ainews-deepseek-v41-flash-763b-p8b) ⭐️ 8.0/10

DeepSeek 发布了 v4.1-Flash，这是一个多模态混合专家（MoE）模型，总参数量达 763B（主干 552B），基于公司全新的因果编码器-解码器（CED）架构构建，并已在 DeepSeek API 上线，原生支持多模态。该模型可原生处理图像和文本，并支持高达一百万 token 的上下文。 这标志着 DeepSeek 以全新架构而非单纯扩大规模的方式重返前沿，其非对称设计承诺以更低成本实现更强智能，可能对整个开放权重与 API 模型生态的定价和效率标准形成压力。社区认为它本应被命名为 v5，说明这次提升之大足以被视为一次代际跨越。 该模型是稀疏的：预填充阶段仅约 8B 参数激活，解码阶段约 16B 激活，因此每 token 的 FLOPs 接近中等规模稠密模型，但全部 552B 主干参数仍需驻留内存以供前向计算。它还采用更小的 KV 缓存以进一步节省开销，而“763B-P8B-D16B”的命名反映了总参数量与激活参数量的对比。

rss · Latent Space · Sep 12, 05:56

**背景**: 混合专家（MoE）模型将大型网络拆分为许多专门的“专家”子网络，每个 token 只路由到其中少数几个，因此总参数量可以非常庞大，而每 token 的计算量保持适中。现代大语言模型大多是仅解码器的因果模型，从左到右生成文本；而因果编码器-解码器则将构建丰富上下文的双向编码器与自回归解码器结合，可提升效率与可解释性。DeepSeek 是一家以发布强大开放权重模型而闻名的中国 AI 实验室，“鲸鱼”是社区对其模型的昵称。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.deepseek.com/en/news/deepseek-v4-1-flash/">Introducing DeepSeek - V 4 . 1 - Flash : smarter, faster, more efficient.</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash">deepseek-ai/DeepSeek-V4.1-Flash · Hugging Face</a></li>
<li><a href="https://apidog.com/blog/how-to-run-deepseek-v4-1-flash-locally/">How to Run DeepSeek-V4.1-Flash Locally ?</a></li>

</ul>
</details>

**社区讨论**: 目前可获得的社区观点是认同 Sebastian 的看法，即这次发布本应被标记为 DeepSeek v5，暗示其提升之大足以配得上一次大版本号跃升。

**标签**: `#DeepSeek`, `#large language models`, `#encoder-decoder`, `#vision`, `#AI research`

---

<a id="item-2"></a>
## [Perplexity 将端到端系统托付给 GPT-6 Astra](https://openai.com/index/perplexity-improving-accuracy-with-astra) ⭐️ 7.0/10

Perplexity 目前正在使用 OpenAI 的 GPT-6 Astra 来撰写沟通内容、修改软件并监控生产系统，而且与早期模型相比，人工检查的频率大幅降低。这标志着这家重要 AI 公司正从人工监督下的 AI 辅助，转向端到端的自主工程工作流。 这是下一代模型在关键工程任务上一次值得关注的实际部署，表明企业对 AI 自主性的信任正在增强。如果像 Perplexity 这样的重要 AI 公司都减少了对生产系统的人工监督，可能会加速整个行业在软件工程和运维中采用智能体式 AI。 该公告内容简短，缺乏基准数据、错误率或回滚流程等技术细节；不过 GPT-6 Astra 已于 2026-09-03 发布，并因基准测试差异引发关注，例如其头条测试框架下 ARC-AGI-3 达到 99.9%，而在标准测试框架下仅为 62.7%。

rss · OpenAI Blog · Sep 14, 00:00

**背景**: Perplexity AI 是一家美国私营软件公司，以其 AI 驱动的答案引擎而闻名，该引擎能够综合实时信息回答用户查询。GPT-6 Astra 是 OpenAI 的下一代模型，被视为早期 GPT 模型的继任者，并与 GPT-5.6 Sol、Claude Fable 5.1 等竞品进行对比。生产监控是指利用传感器和数据持续观察线上系统，在问题影响用户之前发现并诊断它们。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/perplexity-improving-accuracy-with-astra/">Perplexity trusts GPT-6 Astra with end - to - end systems | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Perplexity_AI">Perplexity AI - Wikipedia</a></li>
<li><a href="https://ofox.ai/zh/blog/gpt-6-astra-review-2026/">GPT - 6 Astra 测评：37 分的裂口，和你看不见的那部分思考</a></li>

</ul>
</details>

**标签**: `#AI`, `#GPT-6`, `#Perplexity`, `#software engineering`, `#production systems`

---