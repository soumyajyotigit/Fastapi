from pydantic import BaseModel, ConfigDict, EmailStr


class RegisterRequest(BaseModel):
    full_name: str
    username: str
    email: EmailStr
    phone: str | None = None
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    sub: str | None = None


class RegisterResponse(BaseModel):
    id: str
    full_name: str
    username: str
    email: EmailStr

    model_config = ConfigDict(
        from_attributes=True
    )