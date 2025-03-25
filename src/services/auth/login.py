from uuid import uuid4
from models import User
from asyncpg.exceptions import UniqueViolationError


class UserAlreadyExistsError(Exception):
    pass


async def registration_new_user(name: str, *, role: str = "USER") -> User:
    try:
        if await User.select().where(User.name == name).first():
            raise UserAlreadyExistsError("Пользователь уже существует")
        user = User(name=name, role=role, api_key=f"key-{uuid4()}")
        await user.save()
        return user
    except UniqueViolationError:
        return UserAlreadyExistsError("Пользователь уже существует")
    except Exception as e:
        if "duplicate key" in str(e):
            api_key = f"key-{uuid4()}"
            user.api_key = api_key
            await user.save()
            return user
        raise Exception(f"Ошибка сервера: {str(e)}")
