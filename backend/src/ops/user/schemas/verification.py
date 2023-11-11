from dataclasses import dataclass

from backend.src.domain.user.services.sanitizers import UserSanitizer
from src.domain.common.entities import EntityIDType

from ..services.sanitization.password import validate_password_match


@dataclass
class UserVerifyEmailRequestInput:
    email_address: str

    async def sanitize(self, user_sanitizer: UserSanitizer) -> None:
        sanitized_data = await user_sanitizer.sanitize(
            input={
                "email_address": self.email_address,
            },
        )
        self.email_address = sanitized_data["email_address"]


@dataclass
class UserVerifyEmailConfirmInput:
    key: str

    async def sanitize(self, user_sanitizer: UserSanitizer) -> None:
        sanitized_data = await user_sanitizer.sanitize(
            input={
                "confirmation_key": self.key,
            },
        )
        self.key = sanitized_data["confirmation_key"]


@dataclass
class UserPasswordResetRequestInput:
    email_address: str

    async def sanitize(self, user_sanitizer: UserSanitizer) -> None:
        sanitized_data = await user_sanitizer.sanitize(
            input={
                "email_address": self.email_address,
            },
        )
        self.email_address = sanitized_data["email_address"]


@dataclass
class UserPasswordResetConfirmInput:
    user_id: EntityIDType
    key: str
    old_password: str
    new_password1: str
    new_password2: str

    async def sanitize(self, user_sanitizer: UserSanitizer) -> None:
        validate_password_match(
            password1=self.new_password1, password2=self.new_password2
        )
        sanitized_data = await user_sanitizer.sanitize(
            input={
                "password": self.new_password1,
                "confirmation_key": self.key,
            },
        )
        self.new_password1 = sanitized_data["password"]
        self.new_password2 = sanitized_data["password"]
        self.key = sanitized_data["confirmation_key"]
