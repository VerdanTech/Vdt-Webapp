# Standard Library
import uuid
from datetime import datetime

# External Libraries
from svcs import Container

# VerdanTech Source
from src import settings
from src.common.interfaces.persistence.uow import AbstractUow
from src.common.ops.queries import Query, QueryResult, RefSchema, query_result_transform
from src.garden.domain import (
    Garden,
    GardenMembership,
    RoleEnum,
    VisibilityEnum,
    commands,
    generate_garden_key,
)
from src.user.domain import User

# ======================================
# QueryResults
# ======================================


@query_result_transform
class GardenMembershipPublicSchema(QueryResult[GardenMembership]):
    """Schema for returning a brief, public representation of a GardenMembership."""

    garden_ref: RefSchema
    user_ref: RefSchema
    role: RoleEnum
    created_at: datetime


@query_result_transform
class GardenMembershipFullSchema(QueryResult[GardenMembership]):
    """Schema for returning a detailed representation of a GardenMembership."""

    garden_ref: RefSchema
    user_ref: RefSchema
    inviter_ref: RefSchema | None
    role: RoleEnum
    accepted: bool
    favorite: bool
    created_at: datetime


@query_result_transform
class GardenPartialSchema(QueryResult[Garden]):
    """Schema for returning a partial representation of a Garden."""

    id: uuid.UUID
    name: str
    key: str
    creator_ref: RefSchema | None
    visibility: VisibilityEnum
    num_memberships: int


@query_result_transform
class AssociatedPartialsResult(QueryResult[None]):
    """
    Schema for returning a partial representation
    of all gardens associated with the client.
    """

    favorites: set[GardenPartialSchema]
    pending_memberships: set[GardenPartialSchema]
    admin_memberships: set[GardenPartialSchema]
    edit_memberships: set[GardenPartialSchema]
    view_memberships: set[GardenPartialSchema]
    recently_viewed: set[GardenPartialSchema]


@query_result_transform
class GardenFullSchema(QueryResult[Garden]):
    """Schema for returning a detailed representation of a Garden."""

    id: uuid.UUID
    name: str
    key: str
    creator_ref: RefSchema | None
    visibility: VisibilityEnum
    environment_ref: RefSchema | None
    num_memberships: int
    memberships: set[GardenMembershipFullSchema]
    description: str
    expired: bool


@query_result_transform
class UniqueGardenKeyResult(QueryResult[None]):
    """Schema for returning a unique garden key generated by the server."""

    key: str


# ======================================
# Queries
# ======================================


class GardenMostRelevantPartialsQuery(Query):
    """
    Queries the most relevant gardens for the client.

    Attributes:
        max_gardens (int): the maximum number of gardens to return.
    """

    max_gardens: int


class GardenPartialsByKeysQuery(Query):
    """
    Queries garden partials by a list of keys.

    Attributes:
        keys (list[str]): the keys of the gardens to query.
    """

    keys: list[commands.GardenKey]


class GardenFullByKeyQuery(Query):
    """
    Queries a full garden by key.

    Attributes:
        key (str): the key of the garden to query.
    """

    key: commands.GardenKey


# ======================================
# Query handlers
# ======================================


async def generate_unique_garden_key(
    svcs_container: Container, client: User
) -> UniqueGardenKeyResult:
    """
    Generate a unique garden key for the client.

    Args:
        svcs_container (Container): service locator.
        client (User): the client user.
    """
    # Locate services
    uow = await svcs_container.aget(AbstractUow)

    async with uow:
        # Generate an initial key
        key = generate_garden_key(use_random_plant_name=True)

        # While the key exists, generate a new key.
        # If more than MAX_GARDEN_RANDOM_PLANT_KEY_GENERATION_ATTEMPTS,
        # stop using random plant names (in case they are all taken).
        attempts: int = 0
        while await uow.repos.gardens.key_exists(key):
            if attempts > settings.MAX_GARDEN_RANDOM_PLANT_KEY_GENERATION_ATTEMPTS:
                key = generate_garden_key(use_random_plant_name=False)
            else:
                key = generate_garden_key(use_random_plant_name=True)
            attempts += 1

        return UniqueGardenKeyResult(key=key)


async def get_associated_partials(
    svcs_container: Container, client: User
) -> AssociatedPartialsResult:
    """
    Get a partial representation of all gardens associated with the client.

    Args:
        svcs_container (Container): service locator.
        client (User): the client user.
    """
    ...


async def get_most_relevant_partials(
    query: GardenMostRelevantPartialsQuery, svcs_container: Container, client: User
) -> list[GardenPartialSchema]:
    """
    Get a partial representation of the most relevant gardens for the client.

    Args:
        svcs_container (Container): service locator.
        client (User): the client user.
    """
    ...


async def get_partials_by_key(
    query: GardenPartialsByKeysQuery, svcs_container: Container, client: User
) -> list[GardenPartialSchema]:
    """
    Get a partial representation of gardens by their keys.

    Args:
        query (GardenPartialsByKeysQuery): the query.
        svcs_container (Container): service locator.
        client (User): the client user.
    """
    ...


async def get_full_by_key(
    query: GardenFullByKeyQuery, svcs_container: Container, client: User
) -> GardenFullSchema:
    """
    Get a full representation of a single gardens by its key.

    Args:
        query (GardenFullByKeyQuery): the query.
        svcs_container (Container): service locator.
        client (User): the client user.
    """
    ...
