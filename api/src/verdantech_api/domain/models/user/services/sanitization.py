from typing import TypedDict

from src.verdantech_api.domain.utils.sanitizers import FieldSanitizer, ObjectSanitizer
from src.verdantech_api.domain.utils.sanitizers.sanitization.basic.ban import (
    BanSanitization,
    BanSanitizationConfig,
)
from src.verdantech_api.domain.utils.sanitizers.sanitization.basic.length import (
    LengthSanitization,
    LengthSanitizationConfig,
    LengthSanitizationSpec,
)
from src.verdantech_api.domain.utils.sanitizers.sanitization.basic.regex import (
    RegexSanitization,
    RegexSanitizationConfig,
)
from src.verdantech_api.domain.utils.sanitizers.sanitization.custom.email import (
    EmailSanitization,
    EmailSanitizationConfig,
)
from src.verdantech_api.domain.utils.sanitizers.sanitization.repo.unique import (
    UniqueSanitization,
    UniqueSanitizationConfig,
    UniqueSanitizationSpec,
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
