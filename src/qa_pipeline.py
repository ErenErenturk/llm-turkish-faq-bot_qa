from config import log, MODE
import requests
import json
import os
from prompt_builder import build_prompt

instructions_path = os.path.join(os.path.dirname(__file__), "prompt_instructions.json")
with open(instructions_path, "r", encoding="utf-8") as f:
    INSTRUCTIONS = json.load(f)

def ask_model(prompt, model="qwen:7b-chat", timeout=90):
    try:
        log(f"🟡 [DEBUG] {model} modeline prompt gönderiliyor (timeout={timeout}s)...")
        log(f"📤 [PROMPT]:\n---\n{prompt}\n---")

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": True,
            },
            stream=True,
            timeout=timeout + 30
        )
        response.raise_for_status()

        final_output = ""
        for line in response.iter_lines():
            if not line:
                continue
            try:
                data = json.loads(line.decode("utf-8"))
                final_output += data.get("response", "")
            except json.JSONDecodeError:
                continue

        log(f"📥 [RESPONSE]:\n---\n{final_output[:500]}...\n---")
        return final_output

    except requests.Timeout:
        return f"{model} zaman aşımına uğradı."
    except Exception as e:
        return f"{model} hatası: {str(e)}"

def ask_llm(question, context, history=None):
    log("Tüm işlem Qwen modeli ile başlatılıyor...")

    memory_prompt = ""
    if history:
        for i, (user_q, assistant_a) in enumerate(history):
            memory_prompt += f"Kullanıcı: {user_q}\nAsistan: {assistant_a}\n"

    prompt = memory_prompt + f"Kullanıcı: {question}\n\nBağlam:\n{context}\n\nAsistan:"
    return ask_model(prompt, model="qwen:7b-chat", timeout=150)
