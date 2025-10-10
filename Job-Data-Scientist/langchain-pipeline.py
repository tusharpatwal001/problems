from langchain.chains import RetrievalQA
from langchain_ollama import ChatOllama
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# ---------- Step 1: Ingest stock data ----------
stock = "TCS"
urls = ["https://www.moneycontrol.com/news/business/earnings/tcs-q2-show-in-line-while-street-unclear-on-data-centre-push-should-you-buy-sell-or-hold-13608140.html"]
loader = WebBaseLoader(urls)
documents = loader.load()

# ---------- Step 2: Split text ----------
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(documents)

# ---------- Step 3: Embed + store ----------
embeddings = OllamaEmbeddings(model="mxbai-embed-large:latest")
db = FAISS.from_documents(chunks, embedding=embeddings)

# ---------- Step 4: LLM + QA Chain ----------
llm = ChatOllama(model="gemma3:4b")
qa = RetrievalQA.from_llm(llm=llm, retriever=db.as_retriever())

# ---------- Step 5: Query ----------
query = f"Given current market news about this stock, is {stock} likely to rise or fall? Give a 1-2 line brief about it."
result = qa.invoke(query)
print(result)

# response
# {'query': 'Given current market news about this stock, is TCS likely to rise or fall? Give a 1-2 line brief about it.', 
# 'result': 'Based on the available news, analysts are cautiously optimistic about TCS. 
# While there’s uncertainty around the data center push, the company’s in-line results, margin improvements, 
# and willingness to invest suggest the stock could rise, particularly from a medium to long-term perspective.'}
