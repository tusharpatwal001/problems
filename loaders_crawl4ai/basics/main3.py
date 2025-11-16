# Combining Filters (BM25 + Pruning) in Two Passes

# First pass: Apply PruningContentFilter directly to the raw HTML from result.html (the crawler’s downloaded HTML).
# Second pass: Take the pruned HTML (or text) from step 1, and feed it into BM25ContentFilter, focusing on a user query.

import asyncio
from crawl4ai import CrawlerRunConfig, AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig
from crawl4ai.content_filter_strategy import PruningContentFilter, BM25ContentFilter


async def main(query: str):
    run_config = CrawlerRunConfig()
    browser_config = BrowserConfig()

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(url="https://github.com/Snapchat/Valdi/blob/main/README.md", config=run_config)
        print(result.success)
        print(result.status_code)
        # print(result.html)

        if not result.success or not result.html:
            print("Crawl failed or no HTML content.")
            return

        raw_html = result.html

        # adding pruning filter
        pruning_filter = PruningContentFilter(
            threshold=0.5, min_word_threshold=50)

        # filter_content and return a list of "text chunks"
        pruned_chunks = pruning_filter.filter_content(raw_html)

        # for demonstration combine pruned chunks
        pruned_html = "\n".join(pruned_chunks)

        # adding BM25 content filter with user query
        bm25_filter = BM25ContentFilter(
            user_query=query, bm25_threshold=1.2, language="english")

        # return a list of text chunks
        bm25_chunks = bm25_filter.filter_content(pruned_html)

        if not bm25_chunks:
            print("Nothing matched the BM25 query after pruning.")
            return

        # combine final results
        final_text = "\n---\n".join(bm25_chunks)

        print("==== PRUNED OUTPUT (first pass) ====")
        print(pruned_html[:500], "... (truncated)")  # preview

        print("\n==== BM25 OUTPUT (second pass) ====")
        print(final_text[:500], "... (truncated)")

if __name__ == "__main__":
    asyncio.run(main("Developer"))
