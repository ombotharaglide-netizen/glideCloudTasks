from fastapi import FastAPI
from models import User
from crud import (
    create_user,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user
)

app = FastAPI()

@app.post("/users")
def add_user(user: User):
    return create_user(user.dict())

@app.get("/users")
def fetch_users():
    return get_all_users()

@app.get("/users/{id}")
def fetch_user(id: str):
    return get_user_by_id(id)

@app.put("/users/{id}")
def edit_user(id: str, user: User):
    return update_user(id, user.dict())

@app.delete("/users/{id}")
def remove_user(id: str):
    return delete_user(id)
