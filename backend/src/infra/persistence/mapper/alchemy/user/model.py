from datetime import datetime
from typing import List, Optional

from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, composite, mapped_column, relationship
from src import settings
from src.domain.user.values import EmailConfirmation, PasswordResetConfirmation

from ..model import BaseAlchemyModel, IDType

# ======================================
# ENTITIES
# ======================================


class UserAlchemyModel(BaseAlchemyModel):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(String(length=settings.USERNAME_MAX_LENGTH))
    _password_hash: Mapped[str] = mapped_column(
        String(length=settings.PASSWORD_MAX_LENGTH)
    )
    emails: Mapped[List["EmailAlchemyModel"]] = relationship(
        back_populates="user", lazy="joined"
    )
    # memberships:
    is_active: Mapped[bool]
    is_superuser: Mapped[bool]
    password_reset_confirmation_key: Mapped[Optional[str]] = mapped_column(
        String(length=settings.VERIFICATION_KEY_MAX_LENGTH), nullable=True
    )
    password_reset_confirmation_created_at: Mapped[Optional[datetime]]
    created_at: Mapped[datetime]


# ======================================
# VALUE OBJECTS
# ======================================


class EmailAlchemyModel(BaseAlchemyModel):
    __tablename__ = "user_email"

    # Composite primary key
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"), primary_key=True
    )
    user: Mapped["UserAlchemyModel"] = relationship(back_populates="emails")
    list_index: Mapped[int] = mapped_column(primary_key=True)

    address: Mapped[str] = mapped_column(String(length=settings.EMAIL_MAX_LENGTH))
    verified: Mapped[bool]
    primary: Mapped[bool]
    confirmation_key: Mapped[Optional[str]] = mapped_column(
        String(length=settings.VERIFICATION_KEY_MAX_LENGTH), nullable=True
    )
    confirmation_created_at: Mapped[Optional[datetime]]
    verified_at: Mapped[Optional[datetime]]
