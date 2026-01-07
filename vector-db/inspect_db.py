from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['vector_db']
col = db['documents']
print('count=', col.count_documents({}))
for i, doc in enumerate(col.find().limit(5)):
    text = doc.get('text')
    print(f"{i+1}: {text[:200]}")
