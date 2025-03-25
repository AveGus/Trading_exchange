from uuid import UUID

from pydantic import BaseModel
from fastapi import Header, HTTPException, status
from typing import Annotated
from models import User
from services.types import UserRole


class NewUser(BaseModel):
    name: str


class CreatedUser(BaseModel):
    id: UUID
    name: str
    role: UserRole
    api_key: str


async def get_current_user(
    authorization: Annotated[str, Header(..., alias="Authorization")],
):
    if not authorization.startswith("TOKEN "):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid authorization format. Expected 'TOKEN <key>'",
        )
    api_key = authorization[6:]
    user = await User.select().where(User.api_key == api_key).first()
    if not user:
        raise HTTPException(status_code=401, detail="Неверный API-ключ")
    return user
