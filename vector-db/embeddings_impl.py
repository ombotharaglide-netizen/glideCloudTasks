import requests
import config


def get_embedding(text: str):
    """Call Ollama embeddings API and return embedding vector.

    Uses `OLLAMA_URL` and `OLLAMA_MODEL` from `config.py`. If `OLLAMA_API_KEY`
    is set, it will be sent as a Bearer token header.
    """
    payload = {
        "model": config.OLLAMA_MODEL,
        "input": text,
    }
    headers = {}
    if config.OLLAMA_API_KEY:
        headers["Authorization"] = f"Bearer {config.OLLAMA_API_KEY}"

    resp = requests.post(config.OLLAMA_URL, json=payload, headers=headers, timeout=30)
    # some test fakes may not implement raise_for_status
    if hasattr(resp, "raise_for_status"):
        resp.raise_for_status()
    data = resp.json()

    # Ollama returns embedding under ['embedding'] or nested; be defensive
    if isinstance(data, dict) and "embedding" in data:
        return data["embedding"]
    # Some endpoints return list of embeddings
    if isinstance(data, list) and len(data) and "embedding" in data[0]:
        return data[0]["embedding"]

    raise RuntimeError(f"Unexpected embedding response: {data}")
