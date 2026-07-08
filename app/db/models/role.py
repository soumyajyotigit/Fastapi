from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.models.base import BaseModel


class Role(BaseModel):
    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    users = relationship(
        "UserRole",
        back_populates="role",
        cascade="all, delete-orphan",
    )

    permissions = relationship(
        "Permission",
        back_populates="role",
        cascade="all, delete-orphan",
    )