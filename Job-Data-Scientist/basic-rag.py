from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama.chat_models import ChatOllama
from langchain.chains import RetrievalQA

# ---------- STEP 1: Load your data ----------
loader = TextLoader("Job-Data-Scientist\sample.txt", autodetect_encoding=True)
documents = loader.load()

# ---------- STEP 2: Split into chunks ----------
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = splitter.split_documents(documents)

# ---------- STEP 3: Create embeddings & store in FAISS ----------
embeddings = OllamaEmbeddings(model="mxbai-embed-large:latest")
vector_db = FAISS.from_documents(docs, embedding=embeddings)

# ---------- STEP 4: Initialize LLM ----------
llm = ChatOllama(model="gemma3:4b")

# ---------- STEP 5: Create the RetrievalQA chain ----------
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vector_db.as_retriever(),
    return_source_documents=True
)

# ---------- STEP 6: Ask a question ----------
query = input("Write down your query here: ")
result = qa_chain.invoke({"query": query})

print("\n🧠 Answer:")
print(result["result"])

print("\n📄 Source:")
for doc in result["source_documents"]:
    print(doc.metadata)
