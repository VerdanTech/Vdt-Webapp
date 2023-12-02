# Standard Library
from enum import Enum

from ..common import Ref


class VisibilityEnum(Enum):
    PRIVATE = "PRIVATE"
    UNLISTED = "UNLISTED"
    PUBLIC = "PUBLIC"


class RoleEnum(Enum):
    ADMIN = "ADMIN"
    EDIT = "EDIT"
    VIEW = "VIEW"


class GardenMembershipRef(Ref):
    pass


class GardenRef(Ref):
    pass
