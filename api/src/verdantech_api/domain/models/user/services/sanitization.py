from src.verdantech_api.domain.utils.sanitizers import FieldSanitizer, ObjectSanitizer
from src.verdantech_api.domain.utils.sanitizers.sanitization import (
    BanSanitization,
    EmailSanitization,
    LengthSanitization,
    RegexSanitization,
    UniqueSanitization,
)


class UserSanitizer(ObjectSanitizer):
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
