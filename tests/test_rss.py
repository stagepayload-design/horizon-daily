from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from unittest.mock import AsyncMock
from unittest.mock import MagicMock

from src.models import RSSSourceConfig
from src.scrapers.rss import RSSScraper


def test_rss_ids_are_deterministic() -> None:
    feed = """<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0"><channel><title>Test</title>
      <item>
        <guid>entry-1</guid>
        <title>Item 1</title>
        <link>https://example.com/item-1</link>
        <pubDate>Fri, 24 Apr 2026 12:00:00 GMT</pubDate>
        <description>Hello</description>
      </item>
    </channel></rss>
    """
    response = MagicMock()
    response.text = feed
    response.raise_for_status.return_value = None
    client = AsyncMock()
    client.get.return_value = response
    source = RSSSourceConfig(name="Test", url="https://example.com/feed.xml")
    scraper = RSSScraper([source], client)
    since = datetime(2026, 4, 24, 0, 0, tzinfo=timezone.utc)

    first = asyncio.run(scraper.fetch(since))[0].id
    second = asyncio.run(scraper.fetch(since))[0].id

    assert first == second
    assert first == "rss:example.com_feed.xml:5e2d5d1e58e94d76"


def test_rss_include_keywords_filter_before_analysis() -> None:
    feed = """<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0"><channel><title>Test</title>
      <item><guid>1</guid><title>Critical CVE exploited</title>
        <link>https://example.com/1</link>
        <pubDate>Fri, 24 Apr 2026 12:00:00 GMT</pubDate></item>
      <item><guid>2</guid><title>Celebrity news</title>
        <link>https://example.com/2</link>
        <pubDate>Fri, 24 Apr 2026 12:00:00 GMT</pubDate></item>
    </channel></rss>"""
    response = MagicMock(text=feed)
    response.raise_for_status.return_value = None
    client = AsyncMock()
    client.get.return_value = response
    source = RSSSourceConfig(
        name="Filtered",
        url="https://example.com/feed.xml",
        include_keywords=["CVE", "zero-day"],
    )

    items = asyncio.run(
        RSSScraper([source], client).fetch(
            datetime(2026, 4, 24, 0, 0, tzinfo=timezone.utc)
        )
    )

    assert [item.title for item in items] == ["Critical CVE exploited"]


def test_rss_exclude_keywords_override_includes() -> None:
    source = RSSSourceConfig(
        name="Filtered",
        url="https://example.com/feed.xml",
        include_keywords=["AI"],
        exclude_keywords=["sponsored"],
    )

    assert RSSScraper._matches_filters(source, "AI model release", "official")
    assert not RSSScraper._matches_filters(source, "AI model release", "Sponsored post")


def test_rss_fetch_limit_caps_a_single_feed() -> None:
    feed = """<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0"><channel><title>Test</title>
      <item><guid>1</guid><title>First</title><link>https://example.com/1</link>
        <pubDate>Fri, 24 Apr 2026 12:00:00 GMT</pubDate></item>
      <item><guid>2</guid><title>Second</title><link>https://example.com/2</link>
        <pubDate>Fri, 24 Apr 2026 12:00:00 GMT</pubDate></item>
    </channel></rss>"""
    response = MagicMock(text=feed)
    response.raise_for_status.return_value = None
    client = AsyncMock()
    client.get.return_value = response
    source = RSSSourceConfig(
        name="Limited", url="https://example.com/feed.xml", fetch_limit=1
    )

    items = asyncio.run(
        RSSScraper([source], client).fetch(
            datetime(2026, 4, 24, 0, 0, tzinfo=timezone.utc)
        )
    )

    assert [item.title for item in items] == ["First"]
