# Standard Library
from typing import TypedDict

# VerdanTech Source
from src.utils import sanitizers


class GardenSanitizerConfig(TypedDict):
    key_id: sanitizers.FieldSanitizer[
        sanitizers.basic.RegexSpec, sanitizers.repo.ExistsSpec
    ]
    name: sanitizers.FieldSanitizer[
        sanitizers.basic.RegexSpec,
        sanitizers.basic.BanSpec,
    ]
    description: sanitizers.FieldSanitizer[
        sanitizers.basic.LengthSpec,
        sanitizers.basic.RegexSpec,
    ]


class GardenSanitizer(sanitizers.ObjectSanitizer[GardenSanitizerConfig]):
    """
    Type declaration for the Garden entity sanitizer.

    Fields:
        key_id
        name
        description
    """

    pass
