from embeddings_impl import get_embedding
from db import collection

def ingest():
    collection.delete_many({})

    with open("documents.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # skip empty lines

            embedding = get_embedding(line)
            collection.insert_one({
                "text": line,
                "embedding": embedding
            })

    print("Documents stored in MongoDB")

if __name__ == "__main__":
    ingest()
