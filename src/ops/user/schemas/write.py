# Standard Library
from dataclasses import dataclass
from typing import Optional

# VerdanTech Source
from src.domain.user.sanitizers import UserSanitizer
from src.ops.common import schema_dataclass
from src.utils import sanitizers
from src.utils.sanitizers.options import GroupErrorsByEnum, SelectEnum as specs

from ..sanitizers import validate_password_match


@schema_dataclass
class UserCreateInput:
    """
    Input for creating a new user.
    """

    username: str
    email_address: str
    password1: str
    password2: str

    async def sanitize(self, user_sanitizer: UserSanitizer) -> None:
        """
        Validate and normalize the input data.

        Args:
            user_sanitizer (UserSanitizer): user object sanitizer.
        """
        validate_password_match(password1=self.password1, password2=self.password2)

        sanitized_data = await user_sanitizer.sanitize(
            input_data={
                "username": self.username,
                "email_address": self.email_address,
                "password": self.password1,
            },
            spec_select={
                "username": [specs.LENGTH, specs.REGEX, specs.BAN, specs.UNIQUE],
                "email_address": [
                    specs.LENGTH,
                    specs.UNIQUE,
                    specs.EMAIL,
                ],
                "password": [specs.LENGTH, specs.REGEX, specs.BAN],
            },
            group_errors_by=GroupErrorsByEnum.OBJECT,
        )
        self.username = sanitized_data["username"]
        self.email_address = sanitized_data["email_address"]
        self.password1 = sanitized_data["password"]
        self.password2 = sanitized_data["password"]


@schema_dataclass
class UserChangeInput:
    """
    Input for changing an existing user's fields.
    """

    password: str
    new_username: Optional[str] = None
    new_email_address: Optional[str] = None
    new_password1: Optional[str] = None
    new_password2: Optional[str] = None

    async def sanitize(self, user_sanitizer: UserSanitizer) -> None:
        """
        Validate and normalize the input data.

        Args:
            user_sanitizer (UserSanitizer): user object sanitizer.
        """
        input_data = {}
        spec_select = {}

        if self.new_username is not None:
            input_data["username"] = self.new_username
            spec_select["username"] = [
                specs.LENGTH,
                specs.REGEX,
                specs.BAN,
                specs.UNIQUE,
            ]

        if self.new_email_address is not None:
            input_data["email_address"] = self.new_email_address
            spec_select["email_address"] = [
                specs.LENGTH,
                specs.UNIQUE,
                specs.EMAIL,
            ]

        if (self.new_password1 is not None and self.new_password2 is None) or (
            self.new_password2 is not None and self.new_password1 is None
        ):
            raise sanitizers.spec.SpecError(
                {"MultiFieldError": "Only one version of new_password was given."}
            )
        elif self.new_password1 is not None and self.new_password2 is not None:
            validate_password_match(
                password1=self.new_password1, password2=self.new_password2
            )

            input_data["password"] = self.password1
            spec_select["password"] = [specs.LENGTH, specs.REGEX, specs.BAN]

        sanitized_data = await user_sanitizer.sanitize(
            input_data=input_data,
            spec_select=spec_select,
            group_errors_by=GroupErrorsByEnum.OBJECT,
        )
        self.username = sanitized_data["username"]
        self.email_address = sanitized_data["email_address"]
        self.password1 = sanitized_data["password"]
        self.password2 = sanitized_data["password"]

        if self.new_username is not None:
            self.new_username = sanitized_data["username"]

        if self.new_email_address is not None:
            self.new_email_address = sanitized_data["email_address"]
        if self.new_password1 is not None:
            self.new_password1 = sanitized_data["password"]
            self.new_password2 = sanitized_data["password"]
