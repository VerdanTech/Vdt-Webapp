from datetime import datetime

from litestar.contrib.sqlalchemy.base import BigIntAuditBase
from litestar.dto.factory import dto_field
from sqlalchemy import ForeignKey, String, relationship
from sqlalchemy.orm import Mapped, mapped_column

from verdantech_api.settings import EMAIL_MAX_LENGTH, USERNAME_MAX_LENGTH


class UserModel(BigIntAuditBase):
    """User model"""

    username: Mapped[str] = mapped_column(
        String(length=USERNAME_MAX_LENGTH, unique=True)
    )
    password_hash: Mapped[str | None] = mapped_column(
        String(), info=dto_field("private")
    )
    emails: Mapped[set["EmailAddressModel"]] = relationship(
        back_populates="user", lazy="select"
    )
    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)

    async def is_verified():
        pass


class EmailAddressModel(BigIntAuditBase):
    """Email address model"""

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user_model.id", ondelete="CASCADE")
    )
    user: Mapped[UserModel] = relationship(back_populates="emails")
    email: Mapped[str] = mapped_column(length=EMAIL_MAX_LENGTH, unique=True)
    is_verified: Mapped[bool] = mapped_column(default=False)
    is_primary: Mapped[bool] = mapped_column(default=True)
    confirmation: Mapped["EmailAddressConfirmationModel"] = relationship(
        back_populates="email", lazy="selectin"
    )


class EmailAddressConfirmationModel(BigIntAuditBase):
    """Email address confirmation model"""

    email_id: Mapped[int] = mapped_column(
        ForeignKey("email_address_model.id", ondelete="CASCADE")
    )
    email: Mapped[EmailAddressModel] = relationship(back_populates="confirmation")

    key_hash: Mapped[str] = mapped_column(unique=True, info=dto_field("private"))


class PasswordResetConfirmationModel(BigIntAuditBase):
    """Password reset confirmation model"""

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user_model.id", ondelete="CASCADE")
    )
    user: Mapped[UserModel] = relationship(back_populates="password_confirmation")
    password_hash: Mapped[str | None] = mapped_column(
        String(), info=dto_field("private")
    )
    key_hash: Mapped[str] = mapped_column(unique=True, info=dto_field("private"))
    sent_at: Mapped[datetime]
