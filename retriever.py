import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def get_top_chunks(query_embedding, stored_embeddings, chunks):
    scores = []

    for i, emb in enumerate(stored_embeddings):
        score = cosine_similarity(query_embedding, emb)
        scores.append((score, chunks[i]))

    scores.sort(reverse=True)
    return [chunk for _, chunk in scores[:3]]