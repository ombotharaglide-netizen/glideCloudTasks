from fastapi import FastAPI
from search import search

app = FastAPI()

@app.post("/query")
def query_vector(query: str):
    results = search(query, top_k=3)
    return {
        "query": query,
        "results": results
    }
