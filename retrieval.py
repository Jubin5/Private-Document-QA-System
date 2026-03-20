# import basics
import os
from dotenv import load_dotenv

# import ollama embeddings
from langchain_ollama import OllamaEmbeddings

# import langchain
from langchain_chroma import Chroma
from langchain_core.documents import Document

load_dotenv()

# initialize embeddings model
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# load existing Chroma DB
vector_store = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

# retrieval
retriever = vector_store.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 5, "score_threshold": 0.1},
)

results = retriever.invoke("what is the abstract?")

# show results
print("RESULTS:")

for res in results:
    print(f"* {res.page_content} [{res.metadata}]")