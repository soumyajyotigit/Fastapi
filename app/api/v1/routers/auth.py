from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.get("/")
async def auth_home():

    return {
        "message": "Authentication Module"
    }


@router.get("/login")
async def login():

    return {
        "message": "Login API Coming Soon"
    }


@router.get("/register")
async def register():

    return {
        "message": "Register API Coming Soon"
    }