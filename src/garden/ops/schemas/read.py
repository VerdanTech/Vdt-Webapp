# Standard Library
import uuid
from datetime import datetime

# VerdanTech Source
from src.common.interfaces.events.message import RefSchema, schema
from src.environment.domain.attributes import (
    EnvironmentAttributeCluster as EnvironmentAttributeClusterSchema,
)
from src.garden.domain import Garden, GardenMembership, RoleEnum, VisibilityEnum
from src.ops.user.schemas.read import UserPublicSchema
from src.user.domain import User

"""
Note: The UUID class is used directly instead of the EntityIdType alias
because Litestar schema generation currently types it as Any. 
"""


@schema
class GardenMembershipPublicSchema:
    """Schema for returning a brief, public representation of a GardenMembership."""

    garden_ref: RefSchema[Garden]
    user_ref: RefSchema[User]
    role: RoleEnum
    created_at: datetime

    def __hash__(self) -> int:
        """Used to make hashability transparent to type checkers."""
        return super().__hash__()

    @classmethod
    def from_model(
        cls,
        membership: GardenMembership,
    ) -> "GardenMembershipPublicSchema":
        """
        Create an instance of the schema from a GardenMembership.

        Args:
            membership (GardenMembership): the garden membership to convert.

        Returns:
            GardenMembershipPublicSchema: the schema result.
        """
        # Retrieve Garden schema
        garden_ref_schema = RefSchema.from_model(membership.garden_ref)

        # Retrieve user schema
        user_ref_schema = RefSchema.from_model(membership.user_ref)

        return cls(
            garden_ref=garden_ref_schema,
            user_ref=user_ref_schema,
            role=membership.role,
            created_at=membership.created_at,
        )


@schema
class GardenMembershipFullSchema:
    """Schema for returning a detailed representation of a GardenMembership."""

    garden_ref: RefSchema[Garden]
    user_ref: RefSchema[User]
    role: RoleEnum
    accepted: bool
    favorite: bool
    created_at: datetime
    inviter_ref: RefSchema[User] | None = None

    def __hash__(self) -> int:
        """Used to make hashability transparent to type checkers."""
        return super().__hash__()

    @classmethod
    def from_model(cls, membership: GardenMembership) -> "GardenMembershipFullSchema":
        """
        Create an instance of the schema from a GardenMembership.

        Args:
            membership (GardenMembership): the garden membership to convert.

        Returns:
            GardenMembershipPublicSchema: the schema result.
        """
        # Retrieve Garden schema
        garden_ref_schema = RefSchema.from_model(membership.garden_ref)

        # Retrieve user schema
        user_ref_schema = RefSchema.from_model(membership.user_ref)

        # Retrieve inviter schema
        inviter_ref_schema = None
        if membership.inviter_ref:
            inviter_ref_schema = RefSchema.from_model(membership.inviter_ref)

        return cls(
            garden_ref=garden_ref_schema,
            user_ref=user_ref_schema,
            role=membership.role,
            accepted=membership.accepted,
            favorite=membership.favorite,
            created_at=membership.created_at,
            inviter_ref=inviter_ref_schema,
        )


@schema
class GardenFullSchema:
    """Schema for returning a detailed representation of a Garden."""

    id: uuid.UUID
    key: str
    name: str
    visibility: VisibilityEnum
    num_memberships: int
    memberships: set[GardenMembershipPublicSchema]
    description: str | None
    attributes_ref: RefSchema[EnvironmentAttributeClusterSchema] | None
    creator_ref: RefSchema[User] | None = None

    @classmethod
    def from_model(cls, garden: Garden) -> "GardenFullSchema":
        """
        Create an instance of the schema from a Garden.

        Args:
            garden (Garden): the garden to convert.

        Returns:
            GardenFullSchema: the schema result.
        """
        # Retrieve creator schema
        creator_ref_schema = None
        if garden.creator_ref:
            creator_ref_schema = RefSchema.from_model(garden.creator_ref)

        # Retrieve attributes schema
        attributes_ref_schema = None
        if garden.attributes_ref:
            attributes_ref_schema = RefSchema.from_model(garden.attributes_ref)

        return cls(
            id=garden.id_or_error(),
            key=garden.key,
            name=garden.name,
            creator_ref=creator_ref_schema,
            visibility=garden.visibility,
            num_memberships=garden.num_memberships,
            memberships={
                GardenMembershipPublicSchema.from_model(membership)
                for membership in garden.memberships
            },
            attributes_ref=attributes_ref_schema,
            description=garden.description,
        )
