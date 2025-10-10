from langchain_ollama import ChatOllama


# Example financial news article
financial_news_article = """
Tesla shares dropped 4% today after the company reported lower-than-expected quarterly earnings.
CEO Elon Musk cited increased production costs and weakening demand in China as key factors.
Investors reacted negatively to the outlook for the next quarter, which predicted flat revenue growth.
"""

# Prompt for summarization
summarization_prompt = f"""
Summarize the following financial news article in 1-2 sentences:

{financial_news_article}
"""

# Prompt for sentiment analysis
sentiment_prompt = f"""
What is the overall sentiment of the following financial news article? Respond with Positive, Negative, or Neutral and explain briefly.

{financial_news_article}
"""

# Function to query the OpenAI LLM


def query_llm(prompt):
    model = ChatOllama(model='gemma3:4b')
    response = model.invoke(prompt)
    return response.content


# Get responses
summary = query_llm(summarization_prompt)
sentiment = query_llm(sentiment_prompt)

# output
print("📝Summary: ")
print(summary)
print("\n📈Sentiment: ")
print(sentiment)
