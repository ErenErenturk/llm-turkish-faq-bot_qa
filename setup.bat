@echo off
echo Installing Python dependencies...
pip install -r requirements.txt

echo Pulling Qwen 7B Chat model...
ollama pull qwen:7b-chat

echo Building embeddings and FAISS index...
python src\embed.py

echo All set! Run the app with:
echo streamlit run src\app.py
