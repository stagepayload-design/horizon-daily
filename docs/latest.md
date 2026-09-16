---
layout: default
title: Latest Daily
permalink: /latest/
---

# 最新日报

{% assign latest_zh = site.posts | where: "lang", "zh" | first %}
{% if latest_zh %}
[查看 {{ latest_zh.date | date: "%Y-%m-%d" }} 日报]({{ latest_zh.url | relative_url }})
{% else %}
暂无日报。
{% endif %}
