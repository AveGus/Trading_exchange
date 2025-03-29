from fastapi import FastAPI, Depends
from api.v1.auth import router as auth_router
from services.di import get_current_user

app = FastAPI()

app.include_router(auth_router, prefix="/api/v1/public")


# Добавлено для проверки
@app.get("/protected-route")
async def protected_route(user=Depends(get_current_user)):
    return {"message": f"Добро пожаловать, {user.name}!"}
