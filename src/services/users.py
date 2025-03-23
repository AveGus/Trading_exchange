from pydantic import BaseModel
from fastapi import Header, HTTPException

from models import User
from services.types import UserRole


class UserCreate(BaseModel):
    name: str
    role: UserRole = UserRole.USER


class CreatedUser(BaseModel):
    name: str
    role: str
    api_key: str


async def get_current_user(api_key: str = Header(...)):
    user = await User.select().where(User.api_key == api_key).first()
    if not user:
        raise HTTPException(status_code=401, detail="Неверный API-ключ")
    return user
