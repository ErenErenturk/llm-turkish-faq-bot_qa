import os
from sentence_transformers import SentenceTransformer
from joblib import Memory
import os
import certifi

print("Loading embedding model...")
model = SentenceTransformer("paraphrase-multilingual-mpnet-base-v2")
print("Embedding model loaded.")

# 📦 Embed cache klasörü
cache_dir = os.path.join(os.path.dirname(__file__), "../.cache")
memory = Memory(cache_dir, verbose=0)

@memory.cache
def get_embeddings(texts):
    return model.encode(texts, show_progress_bar=False)
