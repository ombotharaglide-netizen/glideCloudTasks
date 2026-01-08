import numpy as np
from embeddings import get_embedding
from db import collection

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search(query, top_k=3, min_score=0.6):
    query_embedding = get_embedding(query)
    results = []

    for doc in collection.find():
        embedding = doc.get("embedding")

        # SAFETY CHECK
        if not embedding:
            continue

        score = cosine_similarity(query_embedding, embedding)

        if score >= min_score:
            results.append({
                "text": doc["text"],
                "score": round(float(score), 4)
            })

    # Sort only if results exist
    if results:
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:top_k]

   
    return []
