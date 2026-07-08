from app.db.models.user import User

user = User(
    full_name="Soumya Jyoti",
    username="soumya",
    email="soumya@gmail.com",
    password="hashedpassword"
)

print(user)