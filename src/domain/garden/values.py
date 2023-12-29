# Standard Library
from enum import Enum


class VisibilityEnum(Enum):
    PRIVATE = "PRIVATE"
    UNLISTED = "UNLISTED"
    PUBLIC = "PUBLIC"


class RoleEnum(Enum):
    ADMIN = "ADMIN"
    EDIT = "EDIT"
    VIEW = "VIEW"
