from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI(title="Users API", version="1.0.0")

# Simulación de usuarios hardcodeados
HARDCODED_USERS = [
    {"user_id": 1, "name": "Alice"},
    {"user_id": 2, "name": "Bob"},
    {"user_id": 3, "name": "Charlie"},
    {"user_id": 4, "name": "Diana"},
    {"user_id": 5, "name": "Eve"},
]

# Modelo para crear usuarios (aunque no lo vamos a usar en este caso)
class CreateUserRequest(BaseModel):
    name: str

@app.get("/")
def root():
    return {"message": "Users API is running"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/users/random")
def get_random_user():
    user = random.choice(HARDCODED_USERS)
    return user

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": "John Doe"}

@app.post("/users")
def create_users(_request: CreateUserRequest):  # El request lo ignoramos
    return HARDCODED_USERS