# External Libraries
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    String,
    Table,
    Uuid, Enum, Text
)
from sqlalchemy.orm import composite, relationship

# VerdanTech Source
from src.common.adapters.persistence.sqlalchemy.mapper import (
    default_uuid,
    mapper_registry,
)
from src.garden.domain import Garden, GardenMembership, VisibilityEnum
from src.common.domain import Ref

garden_table = Table(
    "garden_table",
    mapper_registry.metadata,
    Column("id", Uuid, primary_key=True, default=default_uuid),
    Column("name", String, unique=False, nullable=False),
    Column("key", String, unique=True, nullable=False),
    Column("creator_ref_id", Uuid, nullable=True),
    Column("visibility", Enum(VisibilityEnum), nullable=False),
    Column("description", Text, nullable=True),
    Column("is_active", Boolean, nullable=False),
    Column("created_at", DateTime, nullable=False),
)

garden_membership_table = Table(
    "garden_membership_table",
    mapper_registry.metadata,
    # Composite primary key is used for one-to-many value objects
    Column(
        "garden_id",
        Uuid,
        ForeignKey("garden_table.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column("user_ref_id", Uuid, primary_key=True),
    Column("inviter_ref_id", Uuid, nullable=True),
    Column("role", Enum, nullable=False),
    Column("accepted_at", DateTime, nullable=True),
    Column("favorite", Boolean, nullable=False),
    Column("created_at", DateTime, nullable=False),
)

mapper_registry.map_imperatively(
    Garden,
    garden_table,
    properties={
        # Note the lack of a back_populates here, as the relationship is one-way.
        # Adding the back_populates causes issues when reassining the entire collection.
        "membership": relationship(
            GardenMembership,
            collection_class=set,
            cascade="all, delete-orphan",
        ),
        "creator_ref": composite(
            Ref,
            garden_table.c.creator_ref_id,
        ),
    },
)
mapper_registry.map_imperatively(
    GardenMembership,
    garden_membership_table,
    properties={
        "garden": relationship(Garden, back_populates="memberships"),
        "user_ref": composite(
            Ref,
            garden_membership_table.c.user_ref_id,
        ),
        "inviter_ref": composite(
            Ref,
            garden_membership_table.c.inviter_ref_id,
        ),
    },
)
