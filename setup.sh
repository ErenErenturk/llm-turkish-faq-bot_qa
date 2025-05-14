#!/bin/bash

echo "📦 Python bağımlılıkları yükleniyor..."
pip install -r requirements.txt

echo "🤖 Qwen 7B Chat modeli indiriliyor..."
ollama pull qwen:7b-chat

echo "🧠 Embedding modeli ve FAISS index oluşturuluyor..."
python src/embed.py

echo "✅ Kurulum tamamlandı! Uygulamayı başlatmak için:"
echo "streamlit run src/app.py"
