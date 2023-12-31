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
    admins: Optional[list[User]] = None,
    description: Optional[str] = None,
    visibility: VisibilityEnum = VisibilityEnum.PRIVATE,
    editors: Optional[list[User]] = None,
    viewers: Optional[list[User],] = None,
) -> Garden:
    if creator.id is None:
        raise Exception
    creator_ref = Ref[User](creator.id)

    garden = Garden(
        name=name, creator=creator_ref, description=description, visibility=visibility
    )

    if admins:
        admin_refs = [Ref[User](admin.id) for admin in admins if admin.id is not None]
        admin_refs.insert(0, creator_ref)
    else:
        admin_refs = [creator_ref]

    admin_memberships = [
        GardenMembership(
            inviter=creator_ref,
            user=admin_ref,
            garden=garden,
            role=RoleEnum.ADMIN,
            open_invite=False,
        )
        if admin_ref.id == creator_ref.id
        else GardenMembership(
            inviter=creator_ref, user=admin_ref, garden=garden, role=RoleEnum.ADMIN
        )
        for admin_ref in admin_refs
    ]

    garden.admins = admin_memberships

    if editors:
        edit_memberships = [
            GardenMembership(
                inviter=creator_ref,
                user=Ref[User](editor.id),
                garden=garden,
                role=RoleEnum.EDIT,
            )
            for editor in editors
            if editor.id is not None
        ]
        garden.editors = edit_memberships

    if viewers:
        view_memberships = [
            GardenMembership(
                inviter=creator_ref,
                user=Ref[User](viewer.id),
                garden=garden,
                role=RoleEnum.VIEW,
            )
            for viewer in viewers
            if viewer.id is not None
        ]
        garden.viewers = view_memberships

    return garden
