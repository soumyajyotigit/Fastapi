from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.auth import (
    RegisterRequest,
    LoginRequest,
    TokenResponse,
)
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(
    user_data: RegisterRequest,
    db: AsyncSession = Depends(get_db),
):
    return await AuthService.register(db, user_data)


@router.post("/login", response_model=TokenResponse)
async def login(
    user_data: LoginRequest,
    db: AsyncSession = Depends(get_db),
):
    return await AuthService.login(db, user_data)