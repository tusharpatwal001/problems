from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnablePassthrough

os.chdir(os.path.dirname(os.getcwd()))

load_dotenv()


class VectorData:
    def __init__(self, path):
        self.embeddings = OllamaEmbeddings(model=os.getenv("NOMIC_EMBEDDING"))
        self.path = path
        self.folder_path = "faiss_index"
        self.vector_db = self.selecting_vdb
        print(type(self.vector_db))
        self.llm = ChatGoogleGenerativeAI(model=os.getenv(
            "GEMINI_MODEL"), google_api_key=os.getenv("GOOGLE_API_KEY"))

    def data_gathering(self) -> str:
        data = PyPDFLoader(self.path).load()
        splitters = RecursiveCharacterTextSplitter(
            chunk_size=5000, chunk_overlap=1000)
        chunks = splitters.split_documents(data)
        return chunks

    def initialize_vdb(self):
        vector_db = FAISS.from_documents(
            documents=self.data_gathering(), embedding=self.embeddings)
        vector_db.save_local(self.folder_path)
        print(f"Vector Data Base Initialized")
        return vector_db

    def updating_vdb(self):
        vector_db = FAISS.load_local(
            self.folder_path, embeddings=self.embeddings, allow_dangerous_deserialization=True)

        vector_db.add_documents(documents=self.da  ta_gathering())
        print(f"Vector Data Base updated")
        vector_db.save_local(self.folder_path)

        return vector_db

    def selecting_vdb(self):
        if os.path.isdir(self.folder_path):
            return self.updating_vdb
        else:
            return self.initialize_vdb

    def format_docs(self, docs):
        return "\n\n".join(d.page_content for d in docs)

    def rag_(self):

        prompt = PromptTemplate(template="""You are a RAG based model try to answer user query according to the context provided
                        
        Context: 
        {context}

        User query:
        {query}""", input_variables=["context", "query"])

        parallel = RunnableParallel({"context": self.vector_db |
                                     RunnableLambda(self.format_docs), "query": RunnablePassthrough()})
        rag_chain = parallel | prompt | self.llm
        return rag_chain


data_path2 = r"C:\Users\D S Patwal\Downloads\Ai\Anthropic-enterprise-ebook-digital.pdf"
