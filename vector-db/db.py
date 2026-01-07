from pymongo import MongoClient
import config

client = MongoClient(config.MONGO_URI)
db = client["vector_db"]
collection = db["documents"]
