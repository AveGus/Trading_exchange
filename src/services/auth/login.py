from models import User
from services.exceptions import UserAlreadyExistsError
from services.types import UserRole, ApiKey


async def registration_new_user(name: str, role: str = UserRole.USER) -> User:
    user = await User.objects().get_or_create(
        User.name == name, defaults={User.role: role, User.api_key: ApiKey.generate()}
    )
    if not user._was_created:
        raise UserAlreadyExistsError()
    return user
