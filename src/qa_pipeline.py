import requests
from app import log, MODE

def ask_model(prompt, model="mistral", timeout=120):
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
        prompt = f"Aşağıdaki metni özetle:\n\n{chunk}\n\nÖzet:"
        summary = ask_model(prompt, model="gemma:2b", timeout=60)
        summaries.append(summary.strip())
    return "\n".join(summaries)

def build_prompt(question, context):
    return f"{question}\n{context}\nCevap:"

def ask_mistral(question, context):
    log("Özetleme başlatılıyor...")
    summarized_context = chunk_context_and_summarize(context)
    log("Final prompt oluşturuluyor...")
    final_prompt = build_prompt(question, summarized_context)
    log("Mistral'a final prompt gönderiliyor...")
    return ask_model(final_prompt, model="mistral", timeout=180)
