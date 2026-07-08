from app.core.config import settings
from app.db.session import get_db


def get_settings():
    return settings


__all__ = [
    "get_settings",
    "get_db",
]