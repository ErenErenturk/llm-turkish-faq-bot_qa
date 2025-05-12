from sentence_transformers import SentenceTransformer

def get_embeddings(texts):
    model = SentenceTransformer('dbmdz/bert-base-turkish-cased')
    embeddings = model.encode(texts, show_progress_bar=True)
    return embeddings
