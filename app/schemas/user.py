from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr


class UserResponse(BaseModel):

    id: UUID

    full_name: str

    username: str

    email: EmailStr

    phone: str | None = None

    is_active: bool

    is_verified: bool

    model_config = ConfigDict(
        from_attributes=True
    )