from vector_store import query_index
from embed import get_embeddings
import subprocess
import requests

def ask_mistral(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "mistral", "prompt": prompt, "stream": False},
            timeout=60
        )
        response.raise_for_status()
        return response.json()["response"]
    except requests.Timeout:
        return "Mistral zaman aşımına uğradı."
    except Exception as e:
        return f"Hata: {str(e)}"

def retrieve_context(question, index, docs, embed_model):
    q_embed = embed_model.encode([question])
    indices = query_index(index, q_embed, top_k=3)
    context = "\n\n".join([docs[i] for i in indices[0] if i < len(docs)])
    return context

def build_prompt(question, context):
    return f"""Soru: {question}
Belgelerden Alınan Bilgiler:
{context}
Cevap:
"""
