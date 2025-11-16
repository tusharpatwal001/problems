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

# Adding Basic Options
run_config = CrawlerRunConfig(
    word_count_threshold=10,        # Minimum words per content block
    exclude_external_links=True,    # Remove external links
    remove_overlay_elements=True,   # Remove popups/modals
    process_iframes=True           # Process iframe content
)


async def main():
    browser_config = BrowserConfig()

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://github.com/Snapchat/Valdi/blob/main/README.md",
            config=run_config
        )
        # print(result.html)
        # print(type(result.html))
        # return result.html # Raw HTML
        # return result.cleaned_html # Cleaned HTML
        # return result.markdown.raw_markdown # Raw markdown from cleaned html
        # return result.markdown.fit_markdown # Most relevant content in markdown

        # Check success status
        print(result.html)      # True if crawl succeeded
        print(result.status_code)  # HTTP status code (e.g., 200, 404)
        
        # Access extracted media and links
        # print(result.media) # Dictionary of found media (images, videos  , audio)
        # print(result.links) # Dictionary of internal and external links


if __name__ == "__main__":

    content = asyncio.run(main())
    file_path = "loaders_crawl4ai\\basics\\results\\fit_markdown.md"

    with open(file_path, "w", encoding="utf-8") as f:
        if type(content) is str:
            f.write(content)
            print(f"HTML content saved to {file_path}")
        else:
            pass
