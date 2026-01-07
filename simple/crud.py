from db import collection
from schema import user_serializer, users_serializer
from bson import ObjectId

def create_user(user: dict):
    collection.insert_one(user)
    return {"message": "User created"}

def get_all_users():
    users = collection.find()
    return users_serializer(users)

def get_user_by_id(id: str):
    user = collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_serializer(user)
    return {"error": "User not found"}

def update_user(id: str, data: dict):
    collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": data}
    )
    return {"message": "User updated"}

def delete_user(id: str):
    collection.delete_one({"_id": ObjectId(id)})
    return {"message": "User deleted"}
