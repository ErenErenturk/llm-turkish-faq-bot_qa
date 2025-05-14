from config import log, MODE
import requests
import json
import os
from prompt_builder import build_prompt

def ask_model(prompt, model="qwen:7b-chat", timeout=90):
    try:
        log(f"{model} modeline prompt gönderiliyor (timeout={timeout}s)...")
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "timeout": timeout
                }
            },
            timeout=timeout + 30
        )
        response.raise_for_status()
        reply = response.json()["response"]
        log(f"{model} cevabı: {reply[:200]}...")
        return reply
    except requests.Timeout:
        return f"{model} zaman aşımına uğradı."
    except Exception as e:
        return f"{model} hatası: {str(e)}"

def chunk_context_and_summarize(context, chunk_size=1000):
    summaries = []
    log(f"Context uzunluğu: {len(context)} karakter — {len(context) // chunk_size + 1} parçaya bölünüyor.")
    for i in range(0, len(context), chunk_size):
        chunk = context[i:i + chunk_size]
        log(f"Chunk {i//chunk_size + 1} özetleniyor...")
        prompt = f"""Aşağıdaki metin bir belge parçasıdır. Bu metindeki en önemli bilgileri sade ve kısa şekilde özetle.
Detaya girme, sadece öz bilgilere odaklan.

Metin:
{chunk}

Kısa Özet:"""
        summary = ask_model(prompt, model="gemma:2b", timeout=60)
        summaries.append(summary.strip())
    return "\n".join(summaries)

def guess_document_type(summary: str) -> str:
    json_path = os.path.join(os.path.dirname(__file__), 'document_types.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        document_types = json.load(f)

    summary_lower = summary.lower()
    for doc_type, keywords in document_types.items():
        if any(keyword in summary_lower for keyword in keywords):
            return doc_type
    return "general"

def ask_gemma(question, context):
    log("Tüm işlem Gemma ile başlatılıyor...")

    # Metni özetle
    summarized_context = chunk_context_and_summarize(context)

    # Belge türünü tahmin et
    doc_type = guess_document_type(summarized_context)

    # Prompt oluştur
    prompt = build_prompt(question, summarized_context, doc_type)

    # Cevap al
    return ask_model(prompt, model="gemma:2b", timeout=90)
