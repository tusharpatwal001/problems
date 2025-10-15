from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Simple one-line prompt
prompt = PromptTemplate.from_template("{question}")

# model
model = ChatOllama(model="gemma3:4b")

# parser
parser = StrOutputParser()

# chain: prompt -> llm -> parser
chain = prompt | model | parser

user_input = input("Ask any question: ")
# run it
result = chain.invoke({"question":user_input})
print(result)
