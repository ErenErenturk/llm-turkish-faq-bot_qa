import streamlit as st
from ingest import load_documents
from embed import get_embeddings
from vector_store import create_faiss_index
from qa_pipeline import retrieve_context, build_prompt, ask_mistral
from sentence_transformers import SentenceTransformer

st.title("Türkçe LLM Soru-Cevap Botu")

# Load and embed documents
docs = load_documents("data")
model = SentenceTransformer('dbmdz/bert-base-turkish-cased')
doc_embeddings = get_embeddings(docs)
index = create_faiss_index(doc_embeddings)

question = st.text_input("Bir soru yazın:")

if question:
    context = retrieve_context(question, index, docs, model)
    prompt = build_prompt(question, context)
    
    st.write("### Oluşturulan Prompt")
    st.code(prompt)

    st.write("### Mistral'dan Gelen Cevap")
    answer = ask_mistral(prompt)
    st.success(answer.strip())
