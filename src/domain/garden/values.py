# Standard Library
from dataclasses import field
from datetime import date, datetime

# VerdanTech Source
from src.domain.common import Ref, Value, value_dataclass
from src.domain.user.entities import User

from .entities import Garden
from .enums import RoleEnum


@value_dataclass
class GardenMembership(Value):
    """
    GardenMembership domain value.

    GardenMemberships connect Users and Gardens,
    allowing conditional access with different roles.
    """

    garden: Garden
    inviter: Ref[User] | None
    user: Ref[User]
    role: RoleEnum = RoleEnum.VIEW
    open_invite: bool = True
    favorite: bool = False
    created_at: datetime = field(default_factory=datetime.now)


class EnvironmentAttributeProfile(Value):
    pass


@value_dataclass
class FrostDateProfile(EnvironmentAttributeProfile):
    first_frost_date: date
    last_frost_date: date
