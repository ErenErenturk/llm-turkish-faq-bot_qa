from vector_store import query_index
from embed import get_embeddings

def retrieve_context(question, index, docs, embed_model):
    q_embed = embed_model.encode([question])
    indices = query_index(index, q_embed, top_k=3)
    context = "\n\n".join([docs[i] for i in indices[0]])
    return context

def build_prompt(question, context):
    return f"""Soru: {question}
Belgelerden Alınan Bilgiler:
{context}
Cevap:
"""
