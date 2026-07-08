from app.utils.jwt import (
    create_access_token,
    decode_token,
)

token = create_access_token(
    {"sub": "admin@gmail.com"}
)

print(token)

print(
    decode_token(token)
)