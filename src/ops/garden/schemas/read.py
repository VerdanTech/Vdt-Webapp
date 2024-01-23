# Standard Library
import uuid
from datetime import datetime

# VerdanTech Source
from src.domain.environment.attributes import (
    EnvironmentAttributeCluster as EnvironmentAttributeClusterSchema,
)
from src.domain.garden.enums import RoleEnum, VisibilityEnum
from src.domain.garden.garden import Garden, GardenRef as GardenRefSchema
from src.domain.garden.membership import GardenMembership
from src.ops.common import schema_dataclass
from src.ops.user.schemas.read import UserPublicSchema

"""
Note: The UUID class is used directly instead of the EntityIdType alias
because Litestar schema generation currently types it as Any. 
"""


@schema_dataclass
class GardenMembershipPublicSchema:
    """Schema for returning a brief, public representation of a GardenMembership."""

    user: UserPublicSchema
    role: RoleEnum
    created_at: datetime
    garden_ref: GardenRefSchema | None = None

    @classmethod
    def from_model(
        cls,
        membership: GardenMembership,
        include_garden_ref: bool = False,
    ) -> "GardenMembershipPublicSchema":
        """
        Create an instance of the schema from a GardenMembership.

        Args:
            membership (GardenMembership): the garden membership to convert.
            include_garden_key (bool): whether to include a ref to the garden
                in the schema. Defaults to False.

        Returns:
            GardenMembershipPublicSchema: the schema result.
        """
        # Retrieve Garden schema
        garden_ref_schema = None
        if include_garden_ref:
            garden_ref_schema = membership.garden.ref.to_schema()

        # Retrieve user schema
        user_schema = UserPublicSchema.from_model(membership.user)

        return cls(
            user=user_schema,
            role=membership.role,
            created_at=membership.created_at,
            garden_ref=garden_ref_schema,
        )


@schema_dataclass
class GardenMembershipFullSchema:
    """Schema for returning a detailed representation of a GardenMembership."""

    user: UserPublicSchema
    role: RoleEnum
    open_invite: bool
    favorite: bool
    created_at: datetime
    garden_ref: GardenRefSchema | None = None
    inviter: UserPublicSchema | None = None

    @classmethod
    def from_model(
        cls, membership: GardenMembership, include_garden_ref: bool = False
    ) -> "GardenMembershipFullSchema":
        """
        Create an instance of the schema from a GardenMembership.

        Args:
            membership (GardenMembership): the garden membership to convert.
            include_garden_key (bool): whether to include a ref to the garden
                in the schema. Defaults to False.

        Returns:
            GardenMembershipPublicSchema: the schema result.
        """
        # Retrieve Garden schema
        garden_ref_schema = None
        if include_garden_ref:
            garden_ref_schema = membership.garden.ref.to_schema()

        # Retrieve user schema
        user_schema = UserPublicSchema.from_model(membership.user)

        # Retrieve inviter schema
        inviter_schema = None
        if membership.inviter:
            inviter_schema = UserPublicSchema.from_model(membership.inviter)

        return cls(
            user=user_schema,
            role=membership.role,
            open_invite=membership.open_invite,
            favorite=membership.favorite,
            created_at=membership.created_at,
            garden_ref=garden_ref_schema,
            inviter=inviter_schema,
        )


@schema_dataclass
class GardenFullSchema:
    """Schema for returning a detailed representation of a Garden."""

    id: uuid.UUID
    key: str
    name: str
    visibility: VisibilityEnum
    num_memberships: int
    memberships: list[GardenMembershipPublicSchema]
    attributes: EnvironmentAttributeClusterSchema
    description: str
    creator: UserPublicSchema | None = None

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
        creator_schema = None
        if garden.creator:
            creator_schema = UserPublicSchema.from_model(garden.creator)

        return cls(
            id=garden.id,
            key=garden.key,
            name=garden.name,
            creator=creator_schema,
            visibility=garden.visibility,
            num_memberships=garden.num_memberships,
            memberships=[
                GardenMembershipPublicSchema.from_model(membership)
                for membership in garden.memberships
            ],
            attributes=garden.attributes,
            description=garden.description,
        )
