from datetime import datetime
from typing import List, Optional

from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, composite, mapped_column, relationship
from src.verdantech_api import settings
from src.verdantech_api.domain.models.user.values import (
    EmailConfirmation,
    PasswordResetConfirmation,
)

from ..model import BaseAlchemyModel, IDType

# ======================================
# ENTITIES
# ======================================


class UserAlchemyModel(BaseAlchemyModel):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(String(length=settings.USERNAME_MAX_LENGTH))
    username_norm: Mapped[str]
    _password_hash: Mapped[str] = mapped_column(
        String(length=settings.PASSWORD_MAX_LENGTH)
    )
    emails: Mapped[List["EmailAlchemyModel"]] = relationship(back_populates="user")
    # memberships:
    is_active: Mapped[bool]
    is_superuser: Mapped[bool]
    password_reset_confirmation: Mapped[PasswordResetConfirmation] = composite(
        mapped_column(
            "password_reset_confirmation_key",
            String(length=settings.VERIFICATION_KEY_MAX_LENGTH),
            nullable=True,
        ),
        mapped_column("password_reset_confirmation_created_at"),
    )
    created_at: Mapped[datetime]


# ======================================
# VALUE OBJECTS
# ======================================


class EmailAlchemyModel(BaseAlchemyModel):
    __tablename__ = "user_email"

    # Composite primary key
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="delete-orphan expunge"), primary_key=True
    )
    user: Mapped["UserAlchemyModel"] = relationship(back_populates="emails")
    list_index: Mapped[int] = mapped_column(primary_key=True)

    address: Mapped[str] = mapped_column(String(length=settings.EMAIL_MAX_LENGTH))
    verified: Mapped[bool]
    primary: Mapped[bool]
    confirmation: Mapped[EmailConfirmation] = composite(
        mapped_column(
            "confirmation_key",
            String(length=settings.VERIFICATION_KEY_MAX_LENGTH),
            nullable=True,
        ),
        mapped_column("confirmation_created_at"),
    )
    verified_at: Mapped[datetime]
