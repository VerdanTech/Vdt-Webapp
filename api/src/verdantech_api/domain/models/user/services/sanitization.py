from typing import TypedDict

from src.verdantech_api.domain.utils.sanitizers import FieldSanitizer, ObjectSanitizer
from src.verdantech_api.domain.utils.sanitizers.sanitization.basic import (
    BanSanitization,
    LengthSanitization,
    RegexSanitization,
)
from src.verdantech_api.domain.utils.sanitizers.sanitization.custom import (
    EmailSanitization,
)
from src.verdantech_api.domain.utils.sanitizers.sanitization.repo import (
    UniqueSanitization,
)

from ..entities import User


class UserSanitizerConfig(TypedDict):
    username: FieldSanitizer[
        LengthSanitization, RegexSanitization, BanSanitization, UniqueSanitization
    ]
    email_address: FieldSanitizer[
        LengthSanitization,
        RegexSanitization,
        BanSanitization,
        EmailSanitization,
        UniqueSanitization,
    ]
    password: FieldSanitizer[LengthSanitization, RegexSanitization, BanSanitization]


class UserSanitizer(ObjectSanitizer[UserSanitizerConfig]):
    async def sanitize_object(self, user: User) -> None:
        """Sanitize a user object

        Args:
            user (User): user to sanitize
        """
        self.username.sanitize(input=user.username)
        for email in user.emails:
            self.email_address.sanitize(input=email.address)
