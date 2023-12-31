# Standard Library
from typing import Optional

# VerdanTech Source
from src.domain.common import Ref
from src.domain.user.entities import User

from ..entities import Garden, GardenMembership
from ..enums import RoleEnum


def invite_user(
    inviter: User, user: User, garden: Garden, role: RoleEnum = RoleEnum.VIEW
) -> Optional[GardenMembership]:
    # Check if user exists in garden already

    # Check if inviter is authorized.

    membership = GardenMembership(
        inviter=Ref(id=inviter.id),
        user=Ref(id=user.id),
        garden=garden,
        role=role,
    )

    return membership


def accept_invite(client: User, membership: GardenMembership) -> GardenMembership:
    membership.open_invite = False

    return membership


def set_role(client: User, subject: User):
    pass


def leave():
    pass
