# Standard Library
import uuid

# External Libraries
from pydantic import (
    AfterValidator,
    BeforeValidator,
    EmailStr,
    Field,
    SecretStr,
    field_validator,
    model_validator,
)
from typing_extensions import Annotated, Self

# VerdanTech Source
from src import exceptions, settings
from src.common.adapters.utils.spec_manager import SpecManager, Specs
from src.common.domain import Command
from src.common.interfaces.persistence import AbstractUow

from .specs import specs

# Load all banned fields
banned_fields = []
with open(settings.static_path("banned_fields.txt"), "r") as file:
    for line in file:
        field = line.strip()
        banned_fields.append(field.lower())

Username = Annotated[
    str,
    BeforeValidator(lambda v: v.strip()),
    AfterValidator(SpecManager.get_validation_method(specs, "username")),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        description=specs.descriptions["username"]["field"],
        json_schema_extra={
            "min_length": specs.values["username"][Specs.MIN_LENGTH],
            "max_length": specs.values["username"][Specs.MAX_LENGTH],
            "pattern": specs.values["username"][Specs.PATTERN],
        },
    ),
]
Password = Annotated[
    SecretStr,
    AfterValidator(SpecManager.get_validation_method(specs, "password")),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        description=specs.descriptions["password"]["field"],
        json_schema_extra={
            "min_length": specs.values["password"][Specs.MIN_LENGTH],
            "max_length": specs.values["password"][Specs.MAX_LENGTH],
            "pattern": specs.values["password"][Specs.PATTERN],
        },
    ),
]
ConfirmationKey = Annotated[
    uuid.UUID,
    Field(),
]


class UserCreateCommand(Command):
    """
    Create a new user.
    """

    username: Username
    email_address: EmailStr
    password1: Password
    password2: Password

    @field_validator("username")
    @classmethod
    def username_banned(cls, value: str) -> str:
        if isinstance(value, str) and value.lower() in banned_fields:
            raise ValueError("Denied: matches a reserved name or is offensive")
        return value

    @model_validator(mode="after")
    def passwords_match(self) -> Self:
        """
        Raises:
            AssertionError: Raised if the two passwords do not match.
        """
        if self.password1 != self.password2:
            raise exceptions.ValidationError(
                field_errors=[("password2", "Passwords do not match")]
            )
        return self

    async def validate_against_uow(self, uow: AbstractUow):
        """
        Validates the command against the database.

        Args:
            uow (AbstractUow): Unit of work providing database access.

        Raises:
            AssertionError: if the username or email address already
                exist in the database.
        """
        if await uow.repos.users.username_exists(username=self.username):
            raise exceptions.ValidationError(
                field_errors=[("username", "Username already exists")]
            )
        if await uow.repos.users.email_exists(email_address=self.email_address):
            raise exceptions.ValidationError(
                field_errors=[("email_address", "Email already exists")]
            )


class UserUpdateCommand(Command):
    """
    Update a user's username, email address, or password fields.
    """

    password: Password
    new_username: Username | None = None
    new_email_address: EmailStr | None = None
    new_password1: Password | None = None
    new_password2: Password | None = None

    @field_validator("new_username")
    @classmethod
    def username_banned(cls, value: str) -> str:
        if value.lower() in banned_fields:
            raise ValueError("Denied: matches a reserved name or is offensive")
        return value

    @model_validator(mode="after")
    def passwords_match(self) -> Self:
        """
        Raises:
            ValidationError: Raised if the two passwords do not match.
        """
        if self.new_password1 != self.new_password2:
            raise exceptions.ValidationError(
                field_errors=[("password2", "Passwords do not match")]
            )
        return self

    async def validate_against_uow(self, uow: AbstractUow):
        """
        Validates the command against the database.

        Args:
            uow (AbstractUow): Unit of work providing database access.

        Raises:
            ValidationError: if the username or email address already
                exist in the database.
        """
        if self.new_username is not None and await uow.repos.users.username_exists(
            username=self.new_username
        ):
            raise exceptions.ValidationError(
                field_errors=[("new_username", "Username already exists")]
            )
        if self.new_email_address is not None and await uow.repos.users.email_exists(
            email_address=self.new_email_address
        ):
            raise exceptions.ValidationError(
                field_errors=[("new_email_address", "Email already exists")]
            )


class UserRequestEmailConfirmationCommand(Command):
    """
    Puts in a request to have
    an email address verified.
    """

    email_address: EmailStr


class UserConfirmEmailConfirmationCommand(Command):
    """
    Closes an email confirmation request.
    """

    key: ConfirmationKey


class UserRequestPasswordResetCommand(Command):
    """
    Puts in a request to reset the user's
    password through email.
    """

    email_address: EmailStr


class UserConfirmPasswordResetCommand(Command):
    """
    Closes a password resest request.
    """

    user_id: uuid.UUID
    key: ConfirmationKey
    new_password1: Password
    new_password2: Password

    @model_validator(mode="after")
    def passwords_match(self) -> Self:
        """
        Raises:
            ValidationError: Raised if the two passwords do not match.
        """
        if self.new_password1 != self.new_password2:
            raise exceptions.ValidationError(
                field_errors=[("password2", "Passwords do not match")]
            )
        return self
