# import basics
import os
import time
from dotenv import load_dotenv

# import ollama embeddings
from langchain_ollama import OllamaEmbeddings

# import langchain
from langchain_chroma import Chroma
from langchain_core.documents import Document

# documents
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

# initialize embeddings model
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# loading the PDF document
loader = PyPDFDirectoryLoader("documents/")

raw_documents = loader.load()

# splitting the document
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=400,
    length_function=len,
    is_separator_regex=False,
)

# creating the chunks
documents = text_splitter.split_documents(raw_documents)

# generate unique id's
i = 0
uuids = []

while i < len(documents):
    i += 1
    uuids.append(f"id{i}")

# initialize Chroma vector store (LOCAL DB)
vector_store = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

# add to database
vector_store.add_documents(documents=documents, ids=uuids)

