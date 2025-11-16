# required library for Simple Crawling
import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig


async def main():
    browser_config = BrowserConfig()
    run_config = CrawlerRunConfig()

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            # Understanding the Response
            # The arun method returns a CrawlResult object with several useful properties.
            url="https://iana.org/domains/example",
            config=run_config
        )
        print(result.markdown)
        
if __name__ == "__main__":
    asyncio.run(main())