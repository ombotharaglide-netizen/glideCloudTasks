import numpy as np
from embeddings import get_embedding
from db import collection

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search(query):
    query_embedding = get_embedding(query)

    best_score = -1
    best_text = ""

    for doc in collection.find():
        score = cosine_similarity(query_embedding, doc["embedding"])

        if score > best_score:
            best_score = score
            best_text = doc["text"]

    return best_text
