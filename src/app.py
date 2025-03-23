from fastapi import FastAPI
from api.v1.auth import router as auth_router

app = FastAPI()

app.include_router(auth_router, prefix="/api/v1")


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str) -> dict[str, str]:
    return {"message": f"Hello {name}"}
