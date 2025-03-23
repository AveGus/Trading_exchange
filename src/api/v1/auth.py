from fastapi import APIRouter

from services.auth.login import register
from services.users import UserCreate, CreatedUser

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/register", response_model=CreatedUser)
async def register_new_user(user: UserCreate) -> CreatedUser:
    user = await register(user)
    return user
