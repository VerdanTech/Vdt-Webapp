# Standard Library
import uuid

# External Libraries
from pydantic import AfterValidator, BeforeValidator, Field, field_validator
from typing_extensions import Annotated

# VerdanTech Source
from src import exceptions, settings
from src.common.adapters.utils.spec_manager import SpecManager, Specs
from src.common.domain import Command
from src.common.interfaces.persistence import AbstractUow

from .enums import RoleEnum, VisibilityEnum
from .specs import specs

# Load all banned garden names and keys
banned_fields = []
with open(settings.static_path("banned_fields.txt"), "r") as file:
    for line in file:
        field = line.strip()
        banned_fields.append(field.lower())


GardenName = Annotated[
    str,
    BeforeValidator(lambda v: v.strip()),
    AfterValidator(SpecManager.get_validation_method(specs, "garden_name")),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        description=specs.descriptions["garden_name"]["field"],
        json_schema_extra={
            "min_length": specs.values["garden_name"][Specs.MIN_LENGTH],
            "max_length": specs.values["garden_name"][Specs.MAX_LENGTH],
            "pattern": specs.values["garden_name"][Specs.PATTERN],
        },
    ),
]
GardenKey = Annotated[
    str,
    BeforeValidator(lambda v: v.strip().lower()),
    AfterValidator(SpecManager.get_validation_method(specs, "garden_key")),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        description=specs.descriptions["garden_key"]["field"],
        json_schema_extra={
            "min_length": specs.values["garden_key"][Specs.MIN_LENGTH],
            "max_length": specs.values["garden_key"][Specs.MAX_LENGTH],
            "pattern": specs.values["garden_key"][Specs.PATTERN],
        },
    ),
]
GardenDescription = Annotated[
    str,
    BeforeValidator(lambda v: v.strip()),
    Field(
        description=specs.descriptions["garden_description"]["field"],
        json_schema_extra={
            "max_length": specs.values["garden_description"][Specs.MAX_LENGTH],
        },
    ),
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

    @field_validator("name")
    @classmethod
    def name_banned(cls, value: str) -> str:
        if isinstance(value, str) and value.lower() in banned_fields:
            raise ValueError("Denied: matches a reserved name or is offensive")
        return value

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
            raise exceptions.ValidationError(
                field_errors=[("key", "Garden key already exists")]
            )


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
