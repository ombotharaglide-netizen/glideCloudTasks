import requests
import config

def get_embedding(text: str):
    payload = {
        "model": config.OLLAMA_MODEL,
        "prompt": text,   # ✅ CORRECT KEY
    }

    headers = {}
    if config.OLLAMA_API_KEY:
        headers["Authorization"] = f"Bearer {config.OLLAMA_API_KEY}"

    resp = requests.post(
        config.OLLAMA_URL,
        json=payload,
        headers=headers,
        timeout=30
    )
    resp.raise_for_status()
    data = resp.json()

    # Ollama embedding response
    if "embedding" in data and data["embedding"]:
        return data["embedding"]

    raise RuntimeError(f"Embedding not generated. Response: {data}")
