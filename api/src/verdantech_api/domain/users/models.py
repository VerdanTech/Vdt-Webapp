from datetime import datetime, timedelta

from litestar.contrib.sqlalchemy.base import BigIntAuditBase
from litestar.dto.factory import dto_field
from sqlalchemy import DateTime, ForeignKey, String, func, relationship
from sqlalchemy.orm import Mapped, mapped_column

from verdantech_api.settings import (
    EMAIL_MAX_LENGTH,
    EMAIL_VERIFICATON_EXPIRY_TIME_HOURS,
    USERNAME_MAX_LENGTH,
)


class UserModel(BigIntAuditBase):
    """User model"""

    username: Mapped[str] = mapped_column(
        String(length=USERNAME_MAX_LENGTH, unique=True)
    )
    password_hash: Mapped[str | None] = mapped_column(
        String(), info=dto_field("private")
    )
    emails: Mapped[set["EmailModel"]] = relationship(
        back_populates="user", lazy="select"
    )
    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)

    async def is_verified():
        pass


class EmailModel(BigIntAuditBase):
    """Email address model"""

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user_model.id", ondelete="CASCADE")
    )
    user: Mapped[UserModel] = relationship(back_populates="emails")
    email: Mapped[str] = mapped_column(length=EMAIL_MAX_LENGTH, unique=True)
    is_verified: Mapped[bool] = mapped_column(default=False)
    is_primary: Mapped[bool] = mapped_column(default=True)

    # Set when email is created or set to primary - defines sorting order for
    # deleting oldest email
    set_at: Mapped[datetime] = mapped_column(DateTime(), default=func.now())

    confirmation: Mapped["EmailAddressConfirmationModel"] = relationship(
        back_populates="email", lazy="selectin"
    )

    def set_primary_status(self) -> None:
        """Update the is_primary and primary_at fields
        to indicate primary status
        """
        self.is_primary = True
        self.set_at = func.now()

    def remove_primary_status(self) -> None:
        """Update the is_primary field to reflect
        loss of primary status
        """
        self.is_primary = False


class AbstractEmailConfirmationModel(BigIntAuditBase):
    """Abstract model for storing email confirmation details"""

    key: Mapped[str] = mapped_column(unique=True, info=dto_field("private"))

    to_delete: Mapped[bool] = mapped_column(default=False)

    def is_expired(self) -> bool:
        """Returns whether the confirmation has expired,
        and update the to_delete

        Returns:
            bool: whether the confirmation has expired
        """
        expired = datetime.now() > (
            self.created_at + timedelta(hours=EMAIL_VERIFICATON_EXPIRY_TIME_HOURS)
        )
        if expired:
            self.to_delete = True
        return expired


class EmailAddressConfirmationModel(AbstractEmailConfirmationModel):
    """Email address confirmation model"""

    email_id: Mapped[int] = mapped_column(
        ForeignKey("email_address_model.id", ondelete="CASCADE")
    )
    email: Mapped[EmailModel] = relationship(back_populates="confirmation")


class PasswordResetConfirmationModel(AbstractEmailConfirmationModel):
    """Password reset confirmation model"""

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user_model.id", ondelete="CASCADE")
    )
    user: Mapped[UserModel] = relationship(back_populates="password_confirmation")
    password_hash: Mapped[str | None] = mapped_column(
        String(), info=dto_field("private")
    )
