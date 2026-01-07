from fastapi import FastAPI
from search import search

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Simple Vector Search API running"}

@app.post("/query")
def query_vector(query: str):
    result = search(query)
    return {
        "query": query,
        "answer": result
    }
