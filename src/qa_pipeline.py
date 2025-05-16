from dotenv import load_dotenv
load_dotenv()

from config import log, MODE
import requests
import json
import os
from prompt_builder import build_prompt

# Load prompt instructions
instructions_path = os.path.join(os.path.dirname(__file__), "prompt_instructions.json")
with open(instructions_path, "r", encoding="utf-8") as f:
    INSTRUCTIONS = json.load(f)

def ask_model(prompt, model="llama-3.3-70b-versatile", timeout=60):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable not set.")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    try:
        log(f"🟡 [DEBUG] {model} modeline prompt gönderiliyor (timeout={timeout}s)...")
        log(f"📤 [PROMPT]:\n---\n{prompt}\n---")

        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=timeout
        )
        response.raise_for_status()

        output = response.json()["choices"][0]["message"]["content"]
        log(f"📥 [RESPONSE]:\n---\n{output[:500]}...\n---")
        return output

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

def ask_llm(question, context, chat_history=None):
    log("Tüm işlem Groq modeli ile başlatılıyor...")

    doc_type = guess_document_type(context)
    prompt = build_prompt(question, context, doc_type, INSTRUCTIONS)

    # Chat history varsa prompt öncesine ekle
    if chat_history:
        history_text = "\n".join([f"Kullanıcı: {q}\nAsistan: {a}" for q, a in chat_history])
        prompt = f"{history_text}\n\n{prompt}"

    return ask_model(prompt)

