from litestar.contrib.sqlalchemy.base import BigIntAuditBase
from litestar.dto.factory import dto_field
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

USERNAME_MAX_LENGTH = 50
PASSWORD_MAX_LENGTH = 255


class UserModel(BigIntAuditBase):
    """User model"""

    username: Mapped[str] = mapped_column(
        String(length=USERNAME_MAX_LENGTH, unique=True)
    )
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str | None] = mapped_column(
        String(length=PASSWORD_MAX_LENGTH), info=dto_field("private")
    )
    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)
    is_verified: Mapped[bool] = mapped_column(default=False)
