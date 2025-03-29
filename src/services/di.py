from config import settings
from fastapi import Header, HTTPException, status
from typing import Annotated
from models import User


async def get_current_user(
    authorization: Annotated[str, Header(..., alias="Authorization")],
) -> User:
    if not authorization.startswith(settings.APIKEY_POSTFIX):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid authorization format. Expected 'TOKEN <key>'",
        )
    api_key = authorization.split(settings.APIKEY_POSTFIX)[1]
    user = await User.objects().where(User.api_key == api_key).first()
    if not user:
        raise HTTPException(status_code=401, detail="Неверный API-ключ")
    return user
