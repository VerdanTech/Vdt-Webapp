# Standard Library
from typing import TypedDict

# VerdanTech Source
from src.utils import sanitizers


class UserSanitizerConfig(TypedDict):
    username: sanitizers.FieldSanitizer[
        sanitizers.basic.LengthSpec,
        sanitizers.basic.RegexSpec,
        sanitizers.basic.BanSpec,
        sanitizers.repo.UniqueSpec,
    ]
    email_address: sanitizers.FieldSanitizer[
        sanitizers.basic.LengthSpec,
        sanitizers.basic.RegexSpec,
        sanitizers.basic.BanSpec,
        sanitizers.repo.UniqueSpec,
        sanitizers.custom.EmailSpec,
    ]
    password: sanitizers.FieldSanitizer[
        sanitizers.basic.LengthSpec,
        sanitizers.basic.RegexSpec,
        sanitizers.basic.BanSpec,
    ]
    confirmation_key: sanitizers.FieldSanitizer[sanitizers.basic.LengthSpec]


class UserSanitizer(sanitizers.ObjectSanitizer[UserSanitizerConfig]):
    """
    Type declaration for the User entity sanitizer.

    Fields:
        username
        email_address
        password
        confirmation_key
    """

    pass
