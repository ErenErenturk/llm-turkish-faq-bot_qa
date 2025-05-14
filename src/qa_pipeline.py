from config import log, MODE
import requests

def ask_model(prompt, model="gemma:2b", timeout=90):
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
        prompt = f"""Aşağıdaki metin bir özgeçmiş parçasıdır. Bu metindeki en önemli bilgileri sade ve kısa şekilde özetle. 
Detaya girme, sadece öz bilgilere odaklan.

Metin:
{chunk}

Kısa Özet:
"""
        summary = ask_model(prompt, model="gemma:2b", timeout=60)
        summaries.append(summary.strip())
    return "\n".join(summaries)

def build_prompt(question, context):
    return f"""Soru: {question}

İlgili içerik:
{context}

Yukarıdaki içeriği temel alarak soruyu açık, kısa ve sade bir şekilde cevapla.
Cevap:
"""

def ask_gemma(question, context):
    log("Tüm işlem gemma modeli ile başlatılıyor...")
    summarized_context = chunk_context_and_summarize(context)
    log("Final prompt oluşturuluyor...")
    final_prompt = build_prompt(question, summarized_context)
    return ask_model(final_prompt, model="gemma:2b", timeout=90)