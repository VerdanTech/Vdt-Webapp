# Standard Library
import re

# External Libraries
from pydantic import AfterValidator, EmailStr, Field, SecretStr, validator
from typing_extensions import Annotated

# VerdanTech Source
from src import settings
from src.domain.common import Command, EntityIdType
from src.interfaces.persistence.common import AbstractUow

# Load all banned usernames
banned_usernames = []
with open(settings.static_path("banned_fields/usernames.txt"), "r") as file:
    for line in file:
        username = line.strip()
        banned_usernames.append(username.lower())


def username_validator(username: str) -> str:
    """
    Raises:
        ValueError:
            Raised if the username does not match
                the pattern specified in the settings.
            If the username is included
                within the banned usernames list.
    """
    if not re.match(settings.USERNAME_PATTERN, username):
        raise ValueError(settings.USERNAME_PATTERN_DESCRIPTION)
    if username.lower() in banned_usernames:
        raise ValueError("unsafe or offensive")
    return username


def password_validator(password: str) -> str:
    """
    Raises:
        ValueError:
            Raised if the password does not match
                the pattern specified in the settings.
    """
    if not re.match(settings.PASSWORD_PATTERN, password):
        raise ValueError(settings.PASSWORD_PATTERN_DESCRIPTION)
    return password


Username = Annotated[
    str,
    Field(
        min_length=settings.USERNAME_MIN_LENGTH, max_length=settings.USERNAME_MAX_LENGTH
    ),
    AfterValidator(username_validator),
]
Password = Annotated[
    SecretStr,
    Field(
        min_length=settings.PASSWORD_MIN_LENGTH, max_length=settings.PASSWORD_MAX_LENGTH
    ),
    AfterValidator(password_validator),
]
ConfirmationKey = Annotated[
    str,
    Field(
        min_length=settings.EMAIL_VERIFICATION_KEY_LENGTH,
        max_length=settings.EMAIL_VERIFICATION_KEY_LENGTH,
    ),
]


class CreateUser(Command):
    """
    Create a new user.
    """

    username: Username
    email_address: EmailStr
    password1: Password
    password2: Password

    @validator("password2")
    def passwords_match(cls, password2, values, **kwargs):
        """
        Raises:
            ValueError: Raised if the two passwords two not match.
        """
        if "password1" in values and password2 != values["password1"]:
            raise ValueError("passwords do not match")

    async def validate_against_uow(self, uow: AbstractUow):
        """
        TODO
        Validates the command against the database.

        Args:
            uow (_type_): _description_

        Raises:
            ValueError: if the username or email address already
                exist in the database.
        """
        pass


class UpdateUser(Command):
    """
    Update a user's username, email address, or password fields.
    """

    password: Password
    new_username: Username | None = None
    new_email_address: EmailStr | None = None
    new_password1: Password | None = None
    new_password2: Password | None = None

    @validator("new_password2")
    def passwords_match(cls, password2, values, **kwargs):
        """
        Raises:
            ValueError: Raised if the two passwords two not match.
        """
        if "password1" not in values and password2 is None:
            return
        elif "password1" in values and password2 != values["password1"]:
            raise ValueError("passwords do not match")

    async def validate_against_uow(self, uow: AbstractUow):
        """
        TODO
        Validates the command against the database.

        Args:
            uow (_type_): _description_

        Raises:
            ValueError: if the username or email address already
                exist in the database.
        """
        pass


class Login(Command):
    """
    Authenticate a user.
    """

    email_address: EmailStr
    password: Password


class RequestEmailConfirmation(Command):
    """
    Puts in a request to have
    an email address verified.
    """

    email_address: EmailStr


class ConfirmEmailConfirmation(Command):
    """
    Closes an email confirmation request.
    """

    key: ConfirmationKey


class RequestPasswordReset(Command):
    """
    Puts in a request to reset the user's
    password through email.
    """

    email_address: EmailStr


class ConfirmPasswordReset(Command):
    """
    Closes a password resest request.
    """

    user_id: EntityIdType
    key: ConfirmationKey
    new_password1: Password
    new_password2: Password

    @validator("new_password2")
    def passwords_match(cls, new_password2, values, **kwargs):
        """
        Raises:
            ValueError: Raised if the two passwords two not match.
        """
        if "new_password1" not in values and new_password2 is None:
            return
        elif "new_password1" in values and new_password2 != values["password1"]:
            raise ValueError("passwords do not match")
