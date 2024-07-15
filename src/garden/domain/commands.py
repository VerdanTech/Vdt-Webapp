# Standard Library
import re
import uuid

# External Libraries
from pydantic import AfterValidator, BeforeValidator, Field, ValidationError
from typing_extensions import Annotated

# VerdanTech Source
from src import settings
from src.common.domain import Command
from src.common.interfaces.persistence import AbstractUow

from .enums import RoleEnum, VisibilityEnum

# Load all banned garden names and keys
banned_fields = []
with open(settings.static_path("banned_fields.txt"), "r") as file:
    for line in file:
        field = line.strip()
        banned_fields.append(field.lower())


def garden_name_validator(garden_name: str) -> str:
    """
    Raises:
        ValueError:
            Raised if the garden name does not match
                the pattern specified in the settings.
            If the name is included
                within the banned names list.
    """
    if not re.match(settings.GARDEN_NAME_PATTERN, garden_name):
        raise ValueError(settings.GARDEN_NAME_PATTERN_DESCRIPTION)
    if garden_name.lower() in banned_fields:
        raise ValueError("unsafe or offensive")
    return garden_name


def garden_key_validator(garden_key: str) -> str:
    """
    Raises:
        ValueError:
            Raised if the garden key does not match
                the pattern specified in the settings.
            If the key is included
                within the banned keys list.
    """
    if not re.match(settings.GARDEN_KEY_PATTERN, garden_key):
        raise ValueError(settings.GARDEN_KEY_PATTERN_DESCRIPTION)
    if garden_key.lower() in banned_fields:
        raise ValueError("unsafe or offensive")
    return garden_key


GardenName = Annotated[
    str,
    Field(
        min_length=settings.GARDEN_NAME_MIN_LENGTH,
        max_length=settings.GARDEN_NAME_MAX_LENGTH,
    ),
    # Trim beginning and end whitespace before validation
    BeforeValidator(lambda v: v.strip()),
    AfterValidator(garden_name_validator),
]
GardenKey = Annotated[
    str,
    Field(
        min_length=settings.GARDEN_KEY_MIN_LENGTH,
        max_length=settings.GARDEN_KEY_MAX_LENGTH,
    ),
    # Trim beginning and end whitespace and apply lowercase before validation
    BeforeValidator(lambda v: v.strip().lower()),
    AfterValidator(garden_key_validator),
]


class GardenCreateCommand(Command):
    """
    Create a new garden.
    """

    name: GardenName
    key: GardenKey | None
    description: str = ""
    visibility: VisibilityEnum = VisibilityEnum.PRIVATE
    admin_ids: list[uuid.UUID] = []
    editor_ids: list[uuid.UUID] = []
    viewer_ids: list[uuid.UUID] = []

    async def validate_against_uow(self, uow: AbstractUow):
        """
        Validates the command against the database.

        Args:
            uow (AbstractUow): Unit of work providing database access.

        Raises:
            ValueError: if the username or email address already
                exist in the database.
        """
        if self.key is not None and await uow.repos.gardens.key_exists(self.key):
            raise ValidationError("Garden key already exists")


class GardenMembershipCreateCommand(Command):
    """
    Garden invitation command.

    Fields:
        garden_key (str): the key id of the garden to create the membership invitation to.
        admin_ids (str): the key ids of the users to invite as admins.
        editor_ids (str): the key ids of the users to invite as editors.
        viewer_ids (str): the key ids of the users to invite as viewers.
    """

    garden_id: uuid.UUID
    admin_ids: list[uuid.UUID] = []
    editor_ids: list[uuid.UUID] = []
    viewer_ids: list[uuid.UUID] = []


class GardenMembershipAcceptCommand(Command):
    """
    Garden membership invitation acceptance command.


    """

    garden_key: GardenKey


class GardenMembershipDeleteCommand(Command):
    """
    Garden membership deletion command.
    """

    garden_key: GardenKey


class GardenMembershipRevokeCommand(Command):
    """
    Garden membership removal command.

    Fields:
        garden_key (str): the key id of the garden to change the membership on.
        user_username (str): the username of the user with the membership to remove.
    """

    garden_id: uuid.UUID
    user_id: uuid.UUID


class GardenMembershipRoleChangeCommand(Command):
    """
    Garden membership role change command.

    Fields:
        garden_key (str): the key id of the garden to change the membership on.
        user_username (str): the username of the user with the membership.
        role (RoleEnum): the role to set on the membership.
    """

    garden_id: uuid.UUID
    user_id: uuid.UUID
    role: RoleEnum
