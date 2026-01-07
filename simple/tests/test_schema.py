from bson import ObjectId
from schema import user_serializer, users_serializer


def test_user_serializer():
    user = {"_id": ObjectId("507f1f77bcf86cd799439011"), "name": "Alice", "email": "a@example.com", "age": 30}
    res = user_serializer(user)
    assert res["id"] == "507f1f77bcf86cd799439011"
    assert res["name"] == "Alice"
    assert res["email"] == "a@example.com"


def test_users_serializer():
    user = {"_id": ObjectId("507f1f77bcf86cd799439011"), "name": "Alice", "email": "a@example.com", "age": 30}
    res = users_serializer([user])
    assert isinstance(res, list)
    assert res[0]["email"] == "a@example.com"
