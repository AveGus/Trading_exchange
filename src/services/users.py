from uuid import UUID
from pydantic import BaseModel, Field
from services.types import UserRole, ApiKey


class NewUser(BaseModel):
    name: str = Field(min_length=3)


class CreatedUser(BaseModel):
    id: UUID
    name: str
    role: UserRole
    api_key: ApiKey
