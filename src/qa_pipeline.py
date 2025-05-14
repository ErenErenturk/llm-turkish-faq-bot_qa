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

def guess_document_type(summary: str) -> str:
    json_path = os.path.join(os.path.dirname(__file__), 'document_types.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        document_types = json.load(f)

    summary_lower = summary.lower()
    for doc_type, keywords in document_types.items():
        if any(keyword in summary_lower for keyword in keywords):
            return doc_type
    return "general"

def ask_llm(question, context):
    log("Tüm işlem Qwen modeli ile başlatılıyor...")

    # Belge türünü doğrudan context üzerinden tahmin et
    doc_type = guess_document_type(context)

    # Prompt oluştur
    prompt = build_prompt(question, context, doc_type)

    # Cevap al
    return ask_model(prompt, model="qwen:7b-chat", timeout=90)

