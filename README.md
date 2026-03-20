# 📄 RAG-Based PDF Chatbot using LLM (Ollama + LangChain + Chroma)

## 🚀 Overview

This project implements a **Retrieval-Augmented Generation (RAG) chatbot** that can answer questions from PDF documents using a fully local LLM setup.

It uses:

* 🧠 LLaMA 3 via Ollama (local LLM)
* 🔎 ChromaDB for vector storage
* 🔗 LangChain for orchestration
* 🌐 Streamlit for UI

---

## 🧠 Architecture

PDF → Chunking → Embeddings → Vector DB (Chroma)
User Query → Retrieval → LLM → Response

---

## 📂 Project Structure

```
rag-pdf-chatbot/
│── chatbot_rag.py
│── ingestion.py
│── retrieval.py
│── documents/
│── chroma_db/
│── requirements.txt
│── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone Repo

```bash
git clone https://github.com/Jubin5/Private-Document-QA-System.git
cd Private-Document-QA-System
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Ollama & Models

```bash
ollama pull llama3
ollama pull nomic-embed-text
```

---

## 📥 Ingest Documents

Place your PDFs inside `documents/` folder and run:

```bash
python ingestion.py
```

---

## 🧪 Test Retrieval

```bash
python retrieval.py
```

---

## 💬 Run Chatbot

```bash
streamlit run chatbot_rag.py
```

---

## 🔥 Features

* Fully local (no API cost)
* Semantic search using embeddings
* Context-aware responses
* Clean UI with Streamlit
* Scalable for multiple documents

---

## 🧠 Tech Stack

* LangChain
* Ollama (LLaMA 3)
* ChromaDB
* Streamlit
* Python

---

## 📌 Future Improvements

* Add memory (chat history retrieval)
* Deploy on cloud
* Add multi-document filtering
* Use LangChain Agents

---

## 👨‍💻 Author

Jubin K Babu
