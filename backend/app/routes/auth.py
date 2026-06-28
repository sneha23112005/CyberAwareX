from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["Authentication"])


class UserRegister(BaseModel):
    name: str
    email: str
    password: str


@router.post("/register")
def register(user: UserRegister):
    return {
        "message": f"Welcome {user.name}!",
        "email": user.email,
        "status": "Registration Successful"
    }