# Standard Library
from typing import TypedDict

# VerdanTech Source
from src.utils import sanitizers

from .entities import User


class UserSanitizerConfig(TypedDict):
    username: sanitizers.FieldSanitizer[
        sanitizers.basic.LengthSanitization,
        sanitizers.basic.RegexSanitization,
        sanitizers.basic.BanSanitization,
        sanitizers.repo.UniqueSanitization,
    ]
    email_address: sanitizers.FieldSanitizer[
        sanitizers.basic.LengthSanitization,
        sanitizers.basic.RegexSanitization,
        sanitizers.basic.BanSanitization,
        sanitizers.repo.UniqueSanitization,
        sanitizers.custom.EmailSanitization,
    ]
    password: sanitizers.FieldSanitizer[
        sanitizers.basic.LengthSanitization,
        sanitizers.basic.RegexSanitization,
        sanitizers.basic.BanSanitization,
    ]
    confirmation_key: sanitizers.FieldSanitizer[sanitizers.basic.LengthSanitization]


class UserSanitizer(sanitizers.ObjectSanitizer[UserSanitizerConfig]):
    async def sanitize_object(self, user: User) -> None:
        """Sanitize a user object

        Args:
            user (User): user to sanitize
        """
        await self.username.sanitize(input=user.username)
        for email in user.emails:
            await self.email_address.sanitize(input=email.address)
