# Standard Library
from typing import Optional

# VerdanTech Source
from src.domain.common import Ref
from src.domain.user.entities import User

from ..entities import Garden, GardenMembership
from ..enums import ActionEnum, RoleEnum
from .permission import assert_authorization


def create_garden_membership(
    client: User, invitee: User, garden: Garden, role: RoleEnum = RoleEnum.VIEW
) -> GardenMembership:
    client.assert_persisted()
    invitee.assert_persisted()
    garden.assert_persisted()

    # Check if user exists in garden already
    if garden.is_user_member(user=invitee):
        raise Exception

    # Check if inviter is authorized.
    inviter_membership = garden.get_membership(user=client)
    if inviter_membership is None:
        raise Exception

    match role:
        case RoleEnum.ADMIN:
            action = ActionEnum.INVITE_ADMIN
        case RoleEnum.EDIT:
            action = ActionEnum.INVITE_EDIT
        case RoleEnum.VIEW:
            action = ActionEnum.INVITE_VIEW
        case _:
            raise ValueError("Unhandled RoleEnum in invite_user() domain service.")

    assert_authorization(membership=inviter_membership, action=action)

    membership = GardenMembership(
        inviter=Ref(id=client.id),
        user=Ref(id=invitee.id),
        garden=garden,
        role=role,
    )

    garden.memberships.append(membership)

    return membership


def set_role(client: User, subject: User, garden: Garden, new_role: RoleEnum):
    client.assert_persisted()
    subject.assert_persisted()
    garden.assert_persisted()

    if client.id == subject.id:
        raise Exception

    client_membership = garden.get_membership(user=client)
    if client_membership is None:
        raise Exception

    subject_membership = garden.get_membership(user=subject)
    if subject_membership is None:
        raise Exception

    match client_membership.role:
        case RoleEnum.ADMIN:
            match new_role:
                case RoleEnum.ADMIN:
                    raise Exception
                case RoleEnum.EDIT:
                    action = ActionEnum.ADMIN_TO_EDIT
                case RoleEnum.VIEW:
                    action = ActionEnum.ADMIN_TO_VIEW
                case _:
                    raise ValueError("Unhandled RoleEnum in set_role() domain service.")

        case RoleEnum.EDIT:
            match new_role:
                case RoleEnum.ADMIN:
                    action = ActionEnum.EDIT_TO_ADMIN
                case RoleEnum.EDIT:
                    raise Exception
                case RoleEnum.VIEW:
                    action = ActionEnum.EDIT_TO_VIEW
                case _:
                    raise ValueError("Unhandled RoleEnum in set_role() domain service.")

        case RoleEnum.VIEW:
            match new_role:
                case RoleEnum.ADMIN:
                    action = ActionEnum.VIEW_TO_ADMIN
                case RoleEnum.EDIT:
                    action = ActionEnum.VIEW_TO_EDIT
                case RoleEnum.VIEW:
                    raise Exception
                case _:
                    raise ValueError("Unhandled RoleEnum in set_role() domain service.")

        case _:
            raise ValueError("Unhandled RoleEnum in set_role() domain service.")

    assert_authorization(membership=client_membership, action=action)


def leave(client: User, garden: Garden):
    client.assert_persisted()
    garden.assert_persisted()

    garden.remove_membership(user=client)


def kick():
    pass
