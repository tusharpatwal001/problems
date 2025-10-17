from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
os.environ['LANGSMITH_PROJECT'] = 'Sequential LLM App'

prompt1 = PromptTemplate(template="Generate a detailed report on {topic}", input_variables=['topic'])

prompt2 = PromptTemplate(template="Generate a 5 pointer summary from the following text \n{text}",
                         input_variables=['text'])

model1 = ChatOllama(model="gemma3:4b", temperature=0.7)
model2 = ChatOllama(model="deepseek-r1:latest", temperature=0.5)

parser = StrOutputParser()

config = {
    "tags":["llm app", "report generation", "summarization"],
    "metadata":{"model":"gemma3:4b", "model1_temp":0.7, "parser":"stroutputparser"}
}

chain = prompt1 | model1 | parser | prompt2 | model2 | parser

response = chain.invoke({"topic": "Unemployment crisis"}, config=config)
print(response)
