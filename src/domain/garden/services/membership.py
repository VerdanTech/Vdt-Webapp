# VerdanTech Source
from src.domain.common import Ref
from src.domain.exceptions import FieldNotFound
from src.domain.user import User

from ..enums import RoleEnum
from ..exceptions import GardenAuthorizationException, MembershipAlreadyExists
from ..garden import Garden, GardenMembership
from ..permission import PermissionRouter


def create_garden_membership(
    client: User, invitee: User, garden: Garden, role: RoleEnum = RoleEnum.VIEW
) -> GardenMembership:
    """
    Create a new garden membership.

    Args:
        client (User): the User responsible for the creation.
        invitee (User) the User to create the membership for.
        garden (Garden): the Garden to create the membership on.
        role (RoleEnum): the role of the membership to set.

    Raises:
        ValueError: raised if the client is the same as the invitee.
        MembershipAlreadyExists: raised if the invitee already
            has a membership on the Garden.
        GardenAuthorizationException: raised if the client does
            not have the required permissions on their GardenMembership.

    Returns:
        GardenMembership: the new GardenMembership.

    """
    if client == invitee:
        raise ValueError("A client cannot invite themselves.")

    # Raise if user exists in garden already
    if garden.is_user_member(user=invitee):
        raise MembershipAlreadyExists("User already has a membership with this Garden.")

    # Raise if inviter is unauthorized.
    inviter_membership = garden.get_membership(user=client)
    if inviter_membership is None:
        raise GardenAuthorizationException(
            "Not authorized to perform operations in this Garden."
        )
    inviter_membership.assert_authorization(
        operation=PermissionRouter.invite(role=role)
    )

    membership = GardenMembership(
        garden_ref=garden.ref,
        inviter_ref=client.ref,
        user_ref=invitee.ref,
        role=role,
    )
    garden.memberships.add(membership)

    return membership


def revoke_membership(client: User, subject: User, garden: Garden) -> None:
    """
    Removes a User that is not the client from a Garden.

    Args:
        client (User): the User responsible for the removal.
        subject (User): the User that is subject to the removal.
        garden (Garden): the Garden to remove the subject from.

    Raises:
        ValueError: raised if the client is the same as the subject.
        FieldNotFound: raised if the subject does not have a GardenMembership
            with the Garden.
        GardenAuthorizationException: raised if the client does
            not have the required permissions on their GardenMembership.
    """
    if client == subject:
        raise ValueError("A client cannot kick themselves from a Garden.")

    # Raise if subject does not exist in the garden already.
    subject_membership = garden.get_membership(user=subject)
    if subject_membership is None:
        raise FieldNotFound("User does not have a membership with this Garden.")

    # Raise if client is unauthorized.
    client_membership = garden.get_membership(user=client)
    if client_membership is None:
        raise GardenAuthorizationException(
            "Not authorized to perform operations in this Garden."
        )
    client_membership.assert_authorization(
        operation=PermissionRouter.revoke_membership(role=subject_membership.role),
    )

    # Remove the membership
    garden.remove_membership(user=subject)


def change_role(
    client: User, subject: User, garden: Garden, new_role: RoleEnum
) -> GardenMembership:
    """
    Changes the role of a User on a Garden.

    Args:
        client (User): the User responsible for the role change.
        subject (User): the User that is subject to the role change.
        garden (Garden): the Garden to change the membership on.
        new_role (RoleEnum): the new role to set on the GardenMembership.

    Raises:
        ValueError: raised if the client is the same as the subject.
        FieldNotFound: raised if the subject does not have a GardenMembership
            with the Garden.
        GardenAuthorizationException: raised if the client does
            not have the required permissions on their GardenMembership.

    Returns:
        GardenMembership: the new membership after the role change.
    """
    if client == subject:
        raise ValueError("A client cannot change their own role.")

    # Raise if subject does not exist in the garden already.
    subject_membership = garden.get_membership(user=subject)
    if subject_membership is None:
        raise FieldNotFound("User does not have a membership with this Garden.")

    # Raise if client is unauthorized.
    client_membership = garden.get_membership(user=client)
    if client_membership is None:
        raise GardenAuthorizationException(
            "Not authorized to perform operations in this Garden."
        )
    client_membership.assert_authorization(
        operation=PermissionRouter.change_role(
            client_role=client_membership.role, new_role=new_role
        ),
    )

    # Change the role.
    new_membership = garden.change_role(user=subject, new_role=new_role)

    return new_membership
