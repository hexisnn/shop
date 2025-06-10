from pydantic import BaseModel
from datetime import date

class User(BaseModel):
    email: str
    username: str
    password: str
    phone: str
    address: str
    role: list
    create_at: date

class UserLogin(BaseModel):
    email: str
    password: str