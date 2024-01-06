# Standard Library
from typing import Optional

# VerdanTech Source
from src.domain.common import Ref
from src.domain.user.entities import User

from ..entities import Garden, GardenMembership
from ..enums import RoleEnum, VisibilityEnum

type UserRoleTuples = list[tuple[User, RoleEnum]]
type UserMembershipTuples = list[tuple[User, GardenMembership]]


def garden_create(
    client: User,
    name: str,
    description: Optional[str] = None,
    user_role_tuples: UserRoleTuples = [],
    visibility: VisibilityEnum = VisibilityEnum.PRIVATE,
) -> tuple[Garden, UserMembershipTuples]:
    """
    Creates a new garden.

    Args:
        client (User): the User that is creating the Garden.
        name (str): the name of the Garden.
        description (Optional[str]): the description of the Garden. Defaults to None.
        user_role_tuples (Optional[UserRoleTuples]): a list of tuples of
            Users and Roles to use to create a set of GardenMembership
            invites on the new Garden. Defaults to [].
        visibility (Optional[VisibilityEnum]): the visibilty to set on the Garden.
            Defaults to VisibilityEnum.PRIVATE.

    Returns:
        tuple[Garden, UserMembershipTuples]: the new Garden and the
            GardenMemberships creator on it.
    """
    # Create an new Garden entity.
    creator_ref = Ref[User](client.id_or_error())
    garden = Garden(
        name=name, creator=creator_ref, description=description, visibility=visibility
    )

    # Create a membership for the creator.
    creator_membership = GardenMembership(
        inviter=creator_ref,
        user=creator_ref,
        garden=garden,
        role=RoleEnum.ADMIN,
        open_invite=False,
    )

    # If any users were invited, create additional memberships.
    invitations = [(invitee, role) for invitee, role in user_role_tuples]
    invitee_memberships = [
        GardenMembership(
            inviter=creator_ref,
            user=Ref[User](invitee.id_or_error()),
            garden=garden,
            role=role,
            open_invite=True,
        )
        for invitee, role in invitations
    ]

    # Add memberships to garden.
    garden.memberships = [creator_membership] + invitee_memberships

    # Combine lists of Users and Membership invitations into list of tuples.
    invitees = [invitation[0] for invitation in invitations]
    user_invitiation_tuples = list(zip(invitees, invitee_memberships))

    return garden, user_invitiation_tuples
