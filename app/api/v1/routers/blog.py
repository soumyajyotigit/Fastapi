from fastapi import APIRouter

router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"]
)


@router.get("/")
async def get_blogs():

    return {
        "message": "Blogs Module"
    }


@router.get("/{blog_id}")
async def get_blog(blog_id: int):

    return {
        "blog_id": blog_id
    }