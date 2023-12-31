# Standard Library
from enum import Enum

from src.asgi.litestar.router import create_routers


class VisibilityEnum(Enum):
    PRIVATE = "PRIVATE"
    UNLISTED = "UNLISTED"
    PUBLIC = "PUBLIC"


class RoleEnum(Enum):
    ADMIN = "ADMIN"
    EDIT = "EDIT"
    VIEW = "VIEW"

class PermissionsEnum():
    """
    requires admin
    requires edit 
    requires view
    any, even anon allowed
    """