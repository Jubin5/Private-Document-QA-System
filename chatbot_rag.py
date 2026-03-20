#import streamlit
import streamlit as st
import os
from dotenv import load_dotenv

# import ollama
from langchain_ollama import ChatOllama, OllamaEmbeddings

# import langchain
from langchain_community.vectorstores import Chroma
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

st.title("Chatbot")

# initialize embeddings model + vector store
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

vector_store = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append(
        SystemMessage("You are an assistant for question-answering tasks.")
    )

# display chat messages from history on app rerun
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# create the bar where we can type messages
prompt = st.chat_input("Ask something...")

# did the user submit a prompt?
if prompt:

    # show user message
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.messages.append(HumanMessage(prompt))

    # initialize LLM (Ollama)
    llm = ChatOllama(
        model="llama3",
        temperature=0.3
    )

    # retriever
    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": 3, "score_threshold": 0.3},  # lowered threshold
    )

    docs = retriever.invoke(prompt)
    docs_text = "\n\n".join(d.page_content for d in docs)

    # system prompt
    system_prompt = """You are an assistant for question-answering tasks.
Use the following context to answer the question.
If you don't know the answer, say you don't know.
Keep answers concise (max 3 sentences).

Context:
{context}
"""

    system_prompt_fmt = system_prompt.format(context=docs_text)

    print("-- SYS PROMPT --")
    print(system_prompt_fmt)

    # add system prompt
    st.session_state.messages.append(SystemMessage(system_prompt_fmt))

    # generate response
    result = llm.invoke(st.session_state.messages).content

    # show assistant response
    with st.chat_message("assistant"):
        st.markdown(result)
        st.session_state.messages.append(AIMessage(result))