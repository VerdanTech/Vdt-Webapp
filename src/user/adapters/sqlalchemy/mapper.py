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
from src import settings
from src.common.adapters.persistence.sqlalchemy.mapper import (
    default_uuid,
    mapper_registry,
    metadata,
)
from src.user.domain import Email, EmailConfirmation, PasswordResetConfirmation, User

user_table = Table(
    "users",
    metadata,
    Column("id", Uuid, primary_key=True, default=default_uuid),
    Column(
        "username", String(settings.USERNAME_MAX_LENGTH), unique=True, nullable=False
    ),
    Column("_password_hash", String, nullable=False),
    Column("is_active", Boolean, nullable=False),
    Column("is_superuser", Boolean, nullable=False),
    Column("password_reset_confirmation_key", Uuid, nullable=True),
    Column("password_reset_confirmation_created_at", DateTime, nullable=True),
    Column("created_at", DateTime, nullable=False),
)

user_email_table = Table(
    "user_email_table",
    metadata,
    Column(
        "user_id", Uuid, ForeignKey("user.id", ondelete="CASCADE"), primary_key=True
    ),
    Column("_list_index", Integer, primary_key=True),
    Column("address", String, nullable=False, unique=True),
    Column("verified", Boolean, nullable=False),
    Column("primary", Boolean, nullable=False),
    Column("confirmation_key", Uuid, nullable=True),
    Column("confirmation_created_at", DateTime, nullable=True),
    Column("verified_at", DateTime, nullable=False),
)

mapper_registry.map_imperatively(
    User,
    user_table,
    properties={
        "emails": relationship(
            Email,
            back_populates="user",
            order_by=user_email_table.c._list_index,
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
