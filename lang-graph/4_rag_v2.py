import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langsmith import traceable

load_dotenv()

os.environ['LANGSMITH_PROJECT'] = 'RAG Application'

PDF_PATH = "book1.pdf"

config = {"run_name": "RAG Application - v2"}


# ------------------------ traceable setup ------------------------
@traceable(name="pdf_loader")
def pdf_loader():
    loader = PyPDFLoader(file_path=PDF_PATH)
    return loader.load()


@traceable(name="data_splitter")
def data_splitter(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_documents(docs)
    return chunks


@traceable(name='build_vectorstore')
def build_vectorstore(splits):
    emb = OllamaEmbeddings(model="all-minilm:latest")

    # vectorstore db
    vs = FAISS.from_documents(splits, emb)
    return vs