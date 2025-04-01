from piccolo.table import Table
from piccolo.columns import Varchar, UUID
import uuid
from services.types import UserRole


class User(Table, tablename="user"):
    id = UUID(primary_key=True, default=uuid.uuid4)
    name = Varchar(length=255, unique=True)
    role = Varchar(length=50, choices=UserRole)
    api_key = Varchar(length=255, unique=True)
