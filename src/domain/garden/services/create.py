# Standard Library
from typing import Optional

# VerdanTech Source
from src.domain.common import Ref
from src.domain.garden.values import EnvironmentAttributeProfile
from src.domain.plants.entities import PlantSet
from src.domain.user.entities import User

from ..entities import Garden, GardenMembership
from ..enums import RoleEnum, VisibilityEnum


def create_garden(
    creator: User,
    name: str,
    description: Optional[str] = None,
    invitations: Optional[list[tuple[User, RoleEnum]]] = None,
    visibility: VisibilityEnum = VisibilityEnum.PRIVATE,
) -> Garden:
    creator.assert_persisted()
    creator_ref = Ref[User](creator.id)

    garden = Garden(
        name=name, creator=creator_ref, description=description, visibility=visibility
    )

    creator_membership = GardenMembership(
        inviter=creator_ref,
        user=creator_ref,
        garden=garden,
        role=RoleEnum.ADMIN,
        open_invite=False,
    )

    invitee_memberships = []
    if invitations is not None:
        invitee_memberships = [
            GardenMembership(
                inviter=creator_ref,
                user=Ref[User](invitee.id),
                garden=garden,
                role=role,
                open_invite=True,
            )
            for invitee, role in invitations if invitee.id is not None
        ]

    garden.memberships = ([creator_membership] + invitee_memberships)

    return garden
