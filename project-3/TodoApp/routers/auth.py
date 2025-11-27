from fastapi import APIRouter
from pydantic import BaseModel
from models import Users

router = APIRouter()


class UserRequest(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    password: str
    is_active: bool
    role: str


@router.get("/auth/")
async def get_user():
    return {"user": "authenticated"}


async def create_usel(user_request: UserRequest):
    user_model = Users(
        email=user_request.email,
        username=user_request.username,
        first_name=user_request.first_name,
        last_name=user_request.last_name,
        hashed_password=user_request.password,
        is_active=True,
        role=user_request.role,
    )

    return user_model
