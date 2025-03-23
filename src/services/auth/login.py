from fastapi import HTTPException
from uuid import uuid4
from models import User
from services.users import UserCreate


async def register(user_data: UserCreate):
    existing_user = await User.select().where(User.name == user_data.name).first()
    if existing_user:
        raise HTTPException(
            status_code=400, detail="Пользователь с таким именем уже существует"
        )
    api_key = f"key-{uuid4()}"
    new_user = User(name=user_data.name, role=user_data.role, api_key=api_key)
    await new_user.save()
    return new_user
