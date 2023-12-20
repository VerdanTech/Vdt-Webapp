# Standard Library
from dataclasses import dataclass

# VerdanTech Source
from src.domain.user.sanitizers import UserSanitizer
from src.utils.sanitizers.options import GroupErrorsByEnum, SelectEnum as specs

from ..sanitizers import validate_password_match


@dataclass
class UserCreateInput:
    username: str
    email_address: str
    password1: str
    password2: str

    async def sanitize(self, user_sanitizer: UserSanitizer) -> None:
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
                    specs.REGEX,
                    specs.BAN,
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
