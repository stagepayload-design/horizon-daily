---
layout: default
title: Daily Archive
permalink: /archive/
---

# 日报归档

{% assign zh_posts = site.posts | where: "lang", "zh" %}
{% assign years = zh_posts | group_by_exp: "post", "post.date | date: '%Y'" %}
{% for year in years %}
## {{ year.name }}

{% assign months = year.items | group_by_exp: "post", "post.date | date: '%Y-%m'" %}
{% for month in months %}
### {{ month.name }}

{% for post in month.items %}
- [{{ post.date | date: "%Y-%m-%d" }}]({{ post.url | relative_url }})
{% endfor %}
{% endfor %}
{% endfor %}
