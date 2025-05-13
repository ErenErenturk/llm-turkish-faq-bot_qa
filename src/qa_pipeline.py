from vector_store import query_index
from embed import get_embeddings
import subprocess

def ask_mistral(prompt):
    try:
        result = subprocess.run(
            ['ollama', 'run', 'mistral', prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=60
        )
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
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
