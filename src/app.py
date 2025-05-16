import os
import streamlit as st
import json
import faiss
import warnings
from sentence_transformers import SentenceTransformer
from embed import get_embeddings
from qa_pipeline import ask_llm
from config import log

warnings.filterwarnings("ignore", category=UserWarning, module="torch")

st.set_option('client.showErrorDetails', True)
st.set_page_config(page_title="LLM Türkçe Soru-Cevap Botu", layout="centered")
st.title("Türkçe Soru-Cevap Asistanı")

# Initialize session memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Load QA dataset and embed once
if "dataset_chunks" not in st.session_state:
    with open("data/qa_dataset.json", encoding="utf-8") as f:
        data = json.load(f)

    st.session_state.dataset_chunks = [
        item["question"] + " " + item.get("context", "") + " " + item["answer"]
        for item in data
    ]
    st.session_state.chunk_embeddings = get_embeddings(st.session_state.dataset_chunks)

    index = faiss.IndexFlatL2(len(st.session_state.chunk_embeddings[0]))
    index.add(st.session_state.chunk_embeddings)
    st.session_state.index = index
    st.session_state.data = data

# Chat-like layout
st.write("Aşağıdaki alana sorularınızı yazabilirsiniz.")
question = st.text_input("Soru", placeholder="Bir şeyler sorun...")

if question:
    with st.spinner("Yanıt hazırlanıyor..."):
        embed_model = SentenceTransformer("models/paraphrase-multilingual-mpnet-base-v2")
        q_embed = embed_model.encode([question])
        indices = st.session_state.index.search(q_embed, 3)[1][0]

        context = "\n\n".join([
            st.session_state.dataset_chunks[i]
            for i in indices if i < len(st.session_state.dataset_chunks)
        ])

        answer = ask_llm(question, context, st.session_state.chat_history)
        st.session_state.chat_history.append((question, answer))

# Display chat history
for i, (q, a) in enumerate(reversed(st.session_state.chat_history), 1):
    with st.container():
        st.markdown(f"**Siz:** {q}")
        st.markdown(f"**Asistan:** {a}")
        st.markdown("---")

# Reset chat
if st.button("Yeni Sohbet Başlat"):
    st.session_state.chat_history = []
    st.experimental_rerun()
