from sentence_transformers import SentenceTransformer

print("⚙️ Loading embedding model")
model = SentenceTransformer("paraphrase-xlm-r-multilingual-v1")
print("✅ Embedding model loaded")

def get_embeddings(texts):
    return model.encode(texts, show_progress_bar=True)
