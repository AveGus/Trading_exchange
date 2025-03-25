from fastapi import FastAPI, Depends
from api.v1.auth import router as auth_router
from models import User
from services.users import get_current_user

app = FastAPI()

app.include_router(auth_router, prefix="/api/v1/public")


# Добавлено для проверки
@app.get("/protected-route")
async def protected_route(user: User = Depends(get_current_user)):
    return {"message": f"Добро пожаловать, {user['name']}!"}
