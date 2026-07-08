from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.models.base import BaseModel
from uuid import UUID

class Blog(BaseModel):
    __tablename__ = "blogs"

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    slug: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False
    )

    excerpt: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    thumbnail: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="draft"
    )

    views: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    author = relationship(
        "User",
        back_populates="blogs"
    )

    def __repr__(self):
        return f"<Blog(id={self.id}, title={self.title})>"