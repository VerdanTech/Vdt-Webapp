# Standard Library
import re
import uuid

# External Libraries
from pydantic import BeforeValidator, Field, ValidationError
from typing_extensions import Annotated

# VerdanTech Source
from src import settings
from src.common.domain import Command, ValidatorWrapper
from src.common.interfaces.persistence import AbstractUow

from .enums import RoleEnum, VisibilityEnum

# Constants
GARDEN_NAME_MIN_LENGTH = 2
GARDEN_NAME_MAX_LENGTH = 50
GARDEN_NAME_PATTERN = r"[0-9A-Za-z ]+"
GARDEN_NAME_PATTERN_DESCRIPTION: str = "only alphanumeric characters and spaces."
GARDEN_NAME_FIELD_DESCRIPTION = f"Must be between {GARDEN_NAME_MIN_LENGTH} and {GARDEN_NAME_MAX_LENGTH} characters long and contain {GARDEN_NAME_PATTERN_DESCRIPTION}"

GARDEN_KEY_MIN_LENGTH = 4
GARDEN_KEY_MAX_LENGTH = 16
GARDEN_KEY_PATTERN = r"[0-9A-Za-z-]+"
GARDEN_KEY_PATTERN_DESCRIPTION = "only alphanumeric characters and hyphens."
GARDEN_KEY_FIELD_DESCRIPTION = f"Must be between {GARDEN_KEY_MIN_LENGTH} and {GARDEN_KEY_MAX_LENGTH} characters long and contain {GARDEN_KEY_PATTERN_DESCRIPTION}"

GARDEN_DESCRIPTION_MAX_LENGTH = 1400
GARDEN_DESCRIPTION_FIELD_DESCRIPTION = (
    f"Must be at most {GARDEN_DESCRIPTION_MAX_LENGTH} characters long"
)

# Load all banned garden names and keys
banned_fields = []
with open(settings.static_path("banned_fields.txt"), "r") as file:
    for line in file:
        field = line.strip()
        banned_fields.append(field.lower())


def garden_name_validator(value: str) -> str:
    """
    Raises:
        ValueError:
            Raised if the garden name does not match
                the pattern specified in the settings.
            If the name is included
                within the banned names list.
    """
    value = value.strip()

    if len(value) < GARDEN_NAME_MIN_LENGTH:
        raise ValueError(f"Must be at least {GARDEN_NAME_MIN_LENGTH} characters long")
    if len(value) > GARDEN_NAME_MAX_LENGTH:
        raise ValueError(f"Must be at most {GARDEN_NAME_MAX_LENGTH} characters long")
    if not re.match(GARDEN_NAME_PATTERN, value):
        raise ValueError(f"Must contain {GARDEN_NAME_PATTERN_DESCRIPTION}")
    if value.lower() in banned_fields:
        raise ValueError("Denied: matches a reserved name or is offensive")
    return value


def garden_key_validator(value: str) -> str:
    """
    Raises:
        ValueError:
            Raised if the garden key does not match
                the pattern specified in the settings.
            If the key is included
                within the banned keys list.
    """
    value = value.strip().lower()

    if len(value) < GARDEN_KEY_MIN_LENGTH:
        raise ValueError(f"Must be at least {GARDEN_KEY_MIN_LENGTH} characters long")
    if len(value) > GARDEN_KEY_MAX_LENGTH:
        raise ValueError(f"Must be at most {GARDEN_KEY_MAX_LENGTH} characters long")
    if not re.match(GARDEN_KEY_PATTERN, value):
        raise ValueError(f"Must contain {GARDEN_KEY_PATTERN_DESCRIPTION}")
    if value.lower() in banned_fields:
        raise ValueError("Denied: matches a reserved name or is offensive")
    return value


GardenName = Annotated[
    str,
    ValidatorWrapper(garden_name_validator),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        min_length=GARDEN_NAME_MIN_LENGTH,
        max_length=GARDEN_NAME_MAX_LENGTH,
        description=GARDEN_NAME_FIELD_DESCRIPTION,
        json_schema_extra={"pattern": GARDEN_NAME_PATTERN},
    ),
]
GardenKey = Annotated[
    str,
    ValidatorWrapper(garden_key_validator),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        min_length=GARDEN_KEY_MIN_LENGTH,
        max_length=GARDEN_KEY_MAX_LENGTH,
        description=GARDEN_KEY_FIELD_DESCRIPTION,
        json_schema_extra={"pattern": GARDEN_KEY_PATTERN},
    ),
]
GardenDescription = Annotated[
    str,
    Field(
        max_length=GARDEN_DESCRIPTION_MAX_LENGTH,
        description=GARDEN_DESCRIPTION_FIELD_DESCRIPTION,
    ),
    BeforeValidator(lambda v: v.strip()),
]


class GardenCreateCommand(Command):
    """
    Create a new garden.
    """

    name: GardenName
    key: GardenKey | None
    description: GardenDescription = ""
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
