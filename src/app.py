import os
import streamlit as st
import fitz
import faiss
from sentence_transformers import SentenceTransformer
from embed import get_embeddings
from qa_pipeline import build_prompt, ask_gemma
from config import log, MODE

st.set_option('client.showErrorDetails', True)
st.set_page_config(page_title="LLM Türkçe PDF Soru-Cevap Botu", layout="wide")
st.title("📄 Türkçe PDF Q&A Bot (Gemma 2B Only)")

def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i+chunk_size])
    return chunks

def create_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def query_index(index, embedding, top_k=3):
    distances, indices = index.search(embedding, top_k)
    return indices

uploaded_file = st.file_uploader("Bir PDF dosyası yükleyin", type=["pdf"])
question = st.text_input("Sorunuzu yazın:")

if uploaded_file and question:
    with st.spinner("Belge işleniyor..."):
        raw_text = extract_text_from_pdf(uploaded_file)
        chunks = chunk_text(raw_text)
        embed_model = SentenceTransformer("models/paraphrase-multilingual-mpnet-base-v2")
        embeddings = get_embeddings(chunks)
        index = create_faiss_index(embeddings)

    with st.spinner("Cevap hazırlanıyor..."):
        q_embed = embed_model.encode([question])
        indices = query_index(index, q_embed, top_k=3)
        context = "\n\n".join([chunks[i] for i in indices[0] if i < len(chunks)])
        answer = ask_gemma(question, context)

    st.subheader("💬 Cevap")
    st.write(answer.strip())

    with st.expander("🔍 Kullanılan Belgelerden Seçilen Parçalar"):
        st.code(context)