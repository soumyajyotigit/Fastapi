from app.db.models.user import User
from app.db.models.blog import Blog

user = User(
    full_name="Soumya",
    username="soumya",
    email="soumya@gmail.com",
    password="123456"
)

blog = Blog(
    title="FastAPI Guide",
    slug="fastapi-guide",
    content="This is my first blog."
)

user.blogs.append(blog)

print(user.blogs)
print(blog.author)