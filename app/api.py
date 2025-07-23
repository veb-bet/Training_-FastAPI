from fastapi import FastAPI, HTTPException
from .models import User
from .storage import add_user, get_all_users

app = FastAPI(title="FastAPI + Typer Project")

@app.get("/users", response_model=list[User])
def get_users():
    return get_all_users()

@app.post("/users", response_model=User, status_code=201)
def create_user(user: User):
    existing = [u for u in get_all_users() if u.id == user.id]
    if existing:
        raise HTTPException(status_code=400, detail="User with this ID already exists.")
    add_user(user)
    return user
