import asyncio
from crawl4ai.async_configs import CrawlerRunConfig, DefaultMarkdownGenerator, BrowserConfig
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai import AsyncWebCrawler

config = CrawlerRunConfig(
    markdown_generator=DefaultMarkdownGenerator(
        content_filter=PruningContentFilter(threshold=0.6),
        options={"ignore_links": True}
    )
)


async def main():
    browser_config = BrowserConfig()

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://github.com/Snapchat/Valdi/blob/main/README.md",
            config=config
        )
        print(result.html)
        print(type(result.html))
        return result.html


if __name__ == "__main__":

    # asyncio.run(main())
    content = asyncio.run(main())
    file_path = "normal_html.html"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"HTML content saved to {file_path}")
