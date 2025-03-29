import pytest
from models import User


@pytest.mark.asyncio
async def test_register_new_user(client):
    response = client.post("/api/v1/public/register", json={"name": "asdadasd"})
    result = response.json()
    user = await User.objects().get(User.name == "asdadasd")
    assert user.name == "asdadasd"
    assert result["name"] == "asdadasd"


@pytest.mark.asyncio
async def test_register_duplicate_user(client, user: User):
    response = client.post("/api/v1/public/register", json={"name": user.name})
    assert response.status_code == 400
    assert response.json()["detail"] == "Пользователь с таким именем существует"
