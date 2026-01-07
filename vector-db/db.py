from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["vector_db"]
collection = db["documents"]
