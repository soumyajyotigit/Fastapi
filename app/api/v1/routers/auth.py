from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.auth import (
    RegisterRequest,
    LoginRequest,
    TokenResponse,
)
from app.services.auth_service import AuthService
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["Authentication"])

from app.api.deps import get_current_user


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    user_data: RegisterRequest,
    db: AsyncSession = Depends(get_db),
):
    return await AuthService.register(db, user_data)


# @router.post("/login", response_model=TokenResponse)
# async def login(
#     user_data: LoginRequest,
#     db: AsyncSession = Depends(get_db),
# ):
#     return await AuthService.login(db, user_data)

@router.post("/login", response_model=TokenResponse)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
):
    return await AuthService.login(
        db,
        form_data,
    )

@router.get("/me")
async def me(
    current_user=Depends(get_current_user),
):

    return current_user