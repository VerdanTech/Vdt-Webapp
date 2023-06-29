from litestar.contrib.sqlalchemy.base import BigIntAuditBase
from litestar.dto.factory import dto_field
from sqlalchemy import String, relationship, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from verdantech_api.settings import (
    EMAIL_MAX_LENGTH,
    EMAIL_VERIFICATION_KEY_MAX_LENGTH,
    PASSWORD_MAX_LENGTH,
    USERNAME_MAX_LENGTH,
)


class UserModel(BigIntAuditBase):
    """User model"""

    username: Mapped[str] = mapped_column(
        String(length=USERNAME_MAX_LENGTH, unique=True)
    )
    password: Mapped[str | None] = mapped_column(
        String(length=PASSWORD_MAX_LENGTH), info=dto_field("private")
    )
    emails: Mapped[list["EmailAddressModel"]] = relationship(back_populates="user", lazy="select")
    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)

    async def is_verified():
        pass


class EmailAddressModel(BigIntAuditBase):
    """Email address model"""

    user_id: Mapped[int] = mapped_column(ForeignKey("user_model.id", ondelete="CASCADE"))
    user: Mapped[UserModel] = relationship(back_populates="emails")
    email: Mapped[str] = mapped_column(length=EMAIL_MAX_LENGTH, unique=True)
    is_verified: Mapped[bool] = mapped_column(default=False)
    is_primary: Mapped[bool] = mapped_column(default=True)


class EmailAddressConfirmationModel(BigIntAuditBase):
    """Email address confirmation model"""

    key: Mapped[str] = mapped_column(
        unique=True, length=EMAIL_VERIFICATION_KEY_MAX_LENGTH
    )
    sent_at: Mapped[datetime]
