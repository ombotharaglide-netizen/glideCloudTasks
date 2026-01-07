from bson import ObjectId
import crud


class DummyCollection:
    def __init__(self):
        self._last = None
        self.updated = None
        self.deleted = False

    def insert_one(self, user):
        if "_id" not in user:
            user = dict(user)
            user["_id"] = ObjectId("507f1f77bcf86cd799439011")
        self._last = user
        return type("R", (), {"inserted_id": self._last["_id"]})

    def find(self):
        return [self._last] if self._last else []

    def find_one(self, filter):
        fid = filter.get("_id")
        if self._last and str(self._last["_id"]) == str(fid):
            return self._last
        return None

    def update_one(self, filter, update):
        fid = filter.get("_id")
        if self._last and str(self._last["_id"]) == str(fid):
            self._last.update(update.get("$set", {}))
            self.updated = update.get("$set", {})
            return type("R", (), {"modified_count": 1})
        return type("R", (), {"modified_count": 0})

    def delete_one(self, filter):
        fid = filter.get("_id")
        if self._last and str(self._last["_id"]) == str(fid):
            self.deleted = True
            self._last = None
            return type("R", (), {"deleted_count": 1})
        return type("R", (), {"deleted_count": 0})


def test_create_get_update_delete_user(monkeypatch):
    dummy = DummyCollection()
    monkeypatch.setattr(crud, "collection", dummy)
    user = {"name": "Bob", "email": "b@example.com", "age": 25}

    # Create
    res = crud.create_user(user)
    assert res == {"message": "User created"}

    # Get all
    users = crud.get_all_users()
    assert isinstance(users, list)

    # Get by id
    uid = str(dummy._last["_id"])
    res_user = crud.get_user_by_id(uid)
    assert res_user["email"] == "b@example.com"

    # Update
    res_update = crud.update_user(uid, {"age": 26})
    assert res_update == {"message": "User updated"}
    assert dummy.updated == {"age": 26}

    # Delete
    res_del = crud.delete_user(uid)
    assert res_del == {"message": "User deleted"}
    assert dummy.deleted is True

    # Not found
    res_nf = crud.get_user_by_id(uid)
    assert res_nf == {"error": "User not found"}
