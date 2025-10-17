import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ['LANGSMITH_PROJECT'] = 'RAG Application'

PDF_PATH = "book1.pdf"

# 1 load PDF
loader = PyPDFLoader(file_path=PDF_PATH)
docs = loader.load()

# 2 Chunk
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(docs)

# 3 Embedding + vector-index
embedding = OllamaEmbeddings(model="nomic-embed-text:latest")
vs = FAISS.from_documents(documents=chunks, embedding=embedding)
retriever = vs.as_retriever(select_type="similarity", search_kwargs={"k": 4})

# 4 Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer ONLY from the provided context. If not found, say you don't know."),
    ("human", "Question: {question}\n\nContext:\n{context}")
])

# 5 chain
llm = ChatOllama(model="qwen3:8b")


def format_docs(docs):
    return "\n\n".join(d.page_content for d in docs)


parallel = RunnableParallel({
    "context": retriever | RunnableLambda(format_docs),
    "question": RunnablePassthrough()
})

config = {"run_name": "RAG Application - v1"}

chain = parallel | prompt | llm | StrOutputParser()

# 6 Ask Questions
print("PDF RAG ready. Ask a question")
q = input("\nQuestion: ")
ans = chain.invoke(q.strip(), config=config)
print("\nA:", ans)
