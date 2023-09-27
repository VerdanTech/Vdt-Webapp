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
    pass
