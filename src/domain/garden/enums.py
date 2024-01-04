# Standard Library
from enum import Enum, auto


class VisibilityEnum(Enum):
    PRIVATE = auto()
    UNLISTED = auto()
    PUBLIC = auto()


class RoleEnum(Enum):
    ADMIN = auto()
    EDIT = auto()
    VIEW = auto()


class PermissionEnum(Enum):
    NOT_ALLOWED = auto()
    REQUIRES_ADMIN = auto()
    REQUIRES_EDIT = auto()
    REQUIRES_VIEW = auto()


class ActionEnum(Enum):
    INVITE_ADMIN = auto()
    INVITE_EDIT = auto()
    INVITE_VIEW = auto()
    ADMIN_TO_EDIT = auto()
    ADMIN_TO_VIEW = auto()
    EDIT_TO_ADMIN = auto()
    EDIT_TO_VIEW = auto()
    VIEW_TO_ADMIN = auto()
    VIEW_TO_EDIT = auto()
