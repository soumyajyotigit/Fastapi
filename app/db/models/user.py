from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.models.base import BaseModel

from sqlalchemy.orm import relationship
from uuid import UUID

class User(BaseModel):
    __tablename__ = "users"

    full_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    username: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    phone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    profile_image: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    blogs = relationship(
        "Blog",
        back_populates="author",
        cascade="all, delete-orphan"
    )

    roles = relationship(
        "UserRole",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    refresh_tokens = relationship(
        "RefreshToken",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    def __repr__(self):

        return (
            f"<User(id={self.id}, "
            f"username={self.username}, "
            f"email={self.email})>"
        )