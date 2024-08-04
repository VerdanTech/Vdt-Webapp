# Standard Library
import re
import uuid

# External Libraries
from pydantic import EmailStr, Field, SecretStr, model_validator
from pydantic_core import PydanticCustomError
from typing_extensions import Annotated, Self

# VerdanTech Source
from src import settings
from src.common.domain import Command, ValidatorWrapper
from src.common.interfaces.persistence import AbstractUow

# Constants
USERNAME_MIN_LENGTH = 3
USERNAME_MAX_LENGTH = 50
USERNAME_PATTERN = r"^[a-zA-Z0-9_]*$"
USERNAME_PATTERN_DESCRIPTION = "only alphanumeric characters and underscores."
USERNAME_FIELD_DESCRIPTION = f"Must be between {USERNAME_MIN_LENGTH} and {USERNAME_MAX_LENGTH} characters long and contain {USERNAME_PATTERN_DESCRIPTION}"

PASSWORD_MIN_LENGTH = 6
PASSWORD_MAX_LENGTH = 255
PASSWORD_PATTERN = r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*\W).*$"
PASSWORD_PATTERN_DESCRIPTION = "at least one lowercase letter, one uppercase letter, one digit, and one special character"
PASSWORD_FIELD_DESCRIPTION = f"Must be between {PASSWORD_MIN_LENGTH} and {PASSWORD_MAX_LENGTH} characters long and contain {PASSWORD_PATTERN_DESCRIPTION}"

# Load all banned garden names and keys
banned_fields = []
with open(settings.static_path("banned_fields.txt"), "r") as file:
    for line in file:
        field = line.strip()
        banned_fields.append(field.lower())


def username_validator(value: str) -> str:
    """
    Raises:
        ValueError:
            Raised if the username does not match
                the required length.
            Raised if the username does not match
                the pattern specified in the settings.
            If the username is included
                within the banned usernames list.
    """
    value = value.strip()

    if len(value) < USERNAME_MIN_LENGTH:
        raise AssertionError(f"Must be at least {USERNAME_MIN_LENGTH} characters long")
    if len(value) > USERNAME_MAX_LENGTH:
        raise AssertionError(f"Must be at most {USERNAME_MAX_LENGTH} characters long")
    if not re.match(USERNAME_PATTERN, value):
        raise AssertionError(f"Must contain {USERNAME_PATTERN_DESCRIPTION}")
    if value.lower() in banned_fields:
        raise AssertionError("Denied: matches a reserved name or is offensive")
    return value


def password_validator(value: str) -> str:
    """
    Raises:
        AssertionError:
            Raised if the password does not match
                the required length.
            The pattern specified in the settings.
    """
    print(value)
    if len(value) < PASSWORD_MIN_LENGTH:
        raise AssertionError(f"Must be at least {PASSWORD_MIN_LENGTH} characters long")
    if len(value) > PASSWORD_MAX_LENGTH:
        raise AssertionError(f"Must be at most {PASSWORD_MAX_LENGTH} characters long")
    if not re.match(PASSWORD_PATTERN, value):
        raise AssertionError(f"Must contain {PASSWORD_PATTERN_DESCRIPTION}")
    return value


Username = Annotated[
    str,
    ValidatorWrapper(username_validator),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        description=USERNAME_FIELD_DESCRIPTION,
        json_schema_extra={
            "min_length": USERNAME_MIN_LENGTH,
            "max_length": USERNAME_MAX_LENGTH,
            "pattern": USERNAME_PATTERN,
        },
    ),
]
Password = Annotated[
    SecretStr,
    ValidatorWrapper(password_validator),
    # Note: Field used only for annotation, to allow custom error messages.
    Field(
        description=PASSWORD_FIELD_DESCRIPTION,
        json_schema_extra={
            "min_length": PASSWORD_MIN_LENGTH,
            "max_length": PASSWORD_MAX_LENGTH,
            "pattern": PASSWORD_PATTERN,
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

    @model_validator(mode="after")
    def passwords_match(self) -> Self:
        """
        Raises:
            AssertionError: Raised if the two passwords do not match.
        """
        if self.password1 != self.password2:
            raise AssertionError("Passwords do not match")
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
            raise AssertionError("Username already exists")
        if await uow.repos.users.email_exists(email_address=self.email_address):
            raise AssertionError("Email already exists")


class UserUpdateCommand(Command):
    """
    Update a user's username, email address, or password fields.
    """

    password: Password
    new_username: Username | None = None
    new_email_address: EmailStr | None = None
    new_password1: Password | None = None
    new_password2: Password | None = None

    @model_validator(mode="after")
    def passwords_match(self) -> Self:
        """
        Raises:
            AssertionError: Raised if the two passwords do not match.
        """
        if self.new_password1 != self.new_password2:
            raise PydanticCustomError("password1", "Passwords do not match")
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
        if self.new_username is not None and await uow.repos.users.username_exists(
            username=self.new_username
        ):
            raise AssertionError("Username already exists")
        if self.new_email_address is not None and await uow.repos.users.email_exists(
            email_address=self.new_email_address
        ):
            raise AssertionError("Email already exists")


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
            AssertionError: Raised if the two passwords do not match.
        """
        if self.new_password1 != self.new_password2:
            raise PydanticCustomError("password1", "Passwords do not match")
        return self
