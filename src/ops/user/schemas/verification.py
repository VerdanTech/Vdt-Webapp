# Standard Library
from dataclasses import dataclass

# VerdanTech Source
from src.domain.common import EntityIDType
from src.domain.user.sanitizers import UserSanitizer
from src.utils.sanitizers.options import GroupErrorsByEnum, SelectEnum as specs

from ..sanitizers import validate_password_match


@dataclass
class UserVerifyEmailRequestInput:
    """
    Input for putting in a request to have
    an email address verified.
    """

    email_address: str

    async def sanitize(self, user_sanitizer: UserSanitizer) -> None:
        """
        Validate and normalize the input data.

        Args:
            user_sanitizer (UserSanitizer): user object sanitizer.
        """
        sanitized_data = await user_sanitizer.sanitize(
            input_data={
                "email_address": self.email_address,
            },
            spec_select={
                "email_address": [
                    specs.EMAIL,
                ]
            },
            group_errors_by=GroupErrorsByEnum.OBJECT,
        )
        self.email_address = sanitized_data["email_address"]


@dataclass
class UserVerifyEmailConfirmInput:
    """
    Input for closing an email confirmation request.
    """

    key: str

    async def sanitize(self, user_sanitizer: UserSanitizer) -> None:
        """
        Validate and normalize the input data.

        Args:
            user_sanitizer (UserSanitizer): user object sanitizer.
        """
        sanitized_data = await user_sanitizer.sanitize(
            input_data={
                "confirmation_key": self.key,
            },
            spec_select={"confirmation_key": [specs.LENGTH]},
            group_errors_by=GroupErrorsByEnum.OBJECT,
        )
        self.key = sanitized_data["confirmation_key"]


@dataclass
class UserPasswordResetRequestInput:
    """
    Input for putting in a request to have a user's password
    reset via email verification.
    """

    email_address: str

    async def sanitize(self, user_sanitizer: UserSanitizer) -> None:
        """
        Validate and normalize the input data.

        Args:
            user_sanitizer (UserSanitizer): user object sanitizer.
        """
        sanitized_data = await user_sanitizer.sanitize(
            input_data={
                "email_address": self.email_address,
            },
            spec_select={"email_address": [specs.EMAIL]},
            group_errors_by=GroupErrorsByEnum.OBJECT,
        )
        self.email_address = sanitized_data["email_address"]


@dataclass
class UserPasswordResetConfirmInput:
    """
    Input for closing and confirming a password reset request.
    """

    user_id: EntityIDType
    key: str
    new_password1: str
    new_password2: str

    async def sanitize(self, user_sanitizer: UserSanitizer) -> None:
        """
        Validate and normalize the input data.

        Args:
            user_sanitizer (UserSanitizer): user object sanitizer.
        """
        validate_password_match(
            password1=self.new_password1, password2=self.new_password2
        )
        sanitized_data = await user_sanitizer.sanitize(
            input_data={
                "password": self.new_password1,
                "confirmation_key": self.key,
            },
            spec_select={
                "password": [specs.LENGTH, specs.REGEX, specs.BAN],
                "confirmation_key": [specs.LENGTH],
            },
        )
        self.new_password1 = sanitized_data["password"]
        self.new_password2 = sanitized_data["password"]
        self.key = sanitized_data["confirmation_key"]
