from fastapi import APIRouter

router = APIRouter()

@router.post("/start-monitor")
def start_monitor():
    return {"status": "Go backend will be notified soon"}


# Directory: mmm-fastapi-backend/app/schemas/user.py
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str