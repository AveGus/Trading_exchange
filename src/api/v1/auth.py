from fastapi import APIRouter, HTTPException

from models import User
from services.auth.login import registration_new_user, UserAlreadyExistsError
from services.users import NewUser, CreatedUser

router = APIRouter(
    prefix="/register",
    tags=["register"],
)


@router.post("", response_model=CreatedUser)
async def register_new_user(new_user: NewUser) -> User:
    try:
        user = await registration_new_user(name=new_user.name)
        return user
    except UserAlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
