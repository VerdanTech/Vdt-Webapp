# Standard Library
import uuid
from datetime import datetime

# External Libraries
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Table,
    Uuid,
)
from sqlalchemy.orm import composite, relationship

# VerdanTech Source
from src.common.adapters.persistence.sqlalchemy.mapper import (
    default_uuid,
    mapper_registry,
)
from src.user.domain import Email, EmailConfirmation, PasswordResetConfirmation, User


def base_confirmation_composite_values(self) -> tuple[uuid.UUID, datetime]:
    """
    Required by SqlAlchemy to map value objects to composites (multiple columns).

    Returns:
        tuple[Uuid, DateTime]: the composite values.
    """
    return self.key, self.created_at


setattr(EmailConfirmation, "__composite_values__", base_confirmation_composite_values)
setattr(
    PasswordResetConfirmation,
    "__composite_values__",
    base_confirmation_composite_values,
)

user_table = Table(
    "user_table",
    mapper_registry.metadata,
    Column("id", Uuid, primary_key=True, default=default_uuid),
    Column("username", String, unique=True, nullable=False),
    Column("_password_hash", String, nullable=False),
    Column("is_active", Boolean, nullable=False),
    Column("is_superuser", Boolean, nullable=False),
    Column("password_reset_confirmation_key", Uuid, nullable=True),
    Column("password_reset_confirmation_created_at", DateTime, nullable=True),
    Column("created_at", DateTime, nullable=False),
)

user_email_table = Table(
    "user_email_table",
    mapper_registry.metadata,
    # Composite primary key is used for one-to-many value objects
    Column(
        "user_id",
        Uuid,
        ForeignKey("user_table.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column("address", String, primary_key=True, nullable=False, unique=True),
    Column("verified", Boolean, nullable=False),
    Column("primary", Boolean, nullable=False),
    Column("confirmation_key", Uuid, nullable=True),
    Column("confirmation_created_at", DateTime, nullable=True),
    Column("verified_at", DateTime, nullable=True),
)

mapper_registry.map_imperatively(
    User,
    user_table,
    properties={
        # Note the lack of a back_populates here, as the relationship is one-way.
        # Adding the back_populates causes issues when reassining the entire collection.
        "emails": relationship(
            Email,
            order_by=user_email_table.c.verified_at,
            collection_class=list,
        ),
        "password_reset_confirmation": composite(
            PasswordResetConfirmation,
            user_table.c.password_reset_confirmation_key,
            user_table.c.password_reset_confirmation_created_at,
        ),
    },
)
mapper_registry.map_imperatively(
    Email,
    user_email_table,
    properties={
        "user": relationship(User, back_populates="emails"),
        "confirmation": composite(
            EmailConfirmation,
            user_email_table.c.confirmation_key,
            user_email_table.c.confirmation_created_at,
        ),
    },
)
