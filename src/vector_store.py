import faiss
import numpy as np

def create_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def query_index(index, embedding, top_k=3):
    distances, indices = index.search(embedding, top_k)
    return indices
