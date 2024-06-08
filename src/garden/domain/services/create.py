# VerdanTech Source
from src.user.domain import User

from ....garden.domain.enums import RoleEnum, VisibilityEnum
from ..garden import Garden, GardenMembership

type UserRoleTupleList = list[tuple[User, RoleEnum]]
type UserMembershipTuples = list[tuple[User, GardenMembership]]


def garden_create(
    creator: User,
    key: str,
    name: str,
    description: str = "",
    invitee_role_tuples: UserRoleTupleList = [],
    visibility: VisibilityEnum = VisibilityEnum.PRIVATE,
) -> tuple[Garden, UserMembershipTuples]:
    """
    Creates a new Garden and associated GardenMemberships.

    Args:
        creator (User): the User that is creating the Garden.
        name (str): the name of the Garden.
        description (Optional[str]): the description of the Garden. Defaults to None.
        invitee_role_tuples (Optional[UserRoleTuples]): a list of tuples of
            Users and Roles to use to create a set of GardenMembership
            invites on the new Garden. Defaults to [].
        visibility (Optional[VisibilityEnum]): the visibilty to set on the Garden.
            Defaults to VisibilityEnum.PRIVATE.

    Returns:
        tuple[Garden, UserMembershipTuples]: the new Garden and the
            GardenMemberships creator on it.
    """
    # Create an new Garden entity.
    garden = Garden(
        name=name,
        key=key,
        creator_ref=creator.ref,
        description=description,
        visibility=visibility,
    )

    # Create a membership for the creator.
    creator_membership = GardenMembership(
        garden_ref=garden.ref,
        inviter_ref=creator.ref,
        user_ref=creator.ref,
        role=RoleEnum.ADMIN,
        accepted=True,
    )

    # If any users were invited, create additional memberships.
    invitations = [(invitee, role) for invitee, role in invitee_role_tuples]
    invitee_memberships = {
        GardenMembership(
            garden_ref=garden.ref,
            inviter_ref=creator.ref,
            user_ref=invitee.ref,
            role=role,
            accepted=False,
        )
        for invitee, role in invitations
    }

    # Add memberships to garden.
    garden.memberships = {creator_membership}
    garden.memberships.update(invitee_memberships)

    # Combine lists of Users and Membership invitations into list of tuples.
    invitees = [invitation[0] for invitation in invitations]
    user_invitiation_tuples = list(zip(invitees, invitee_memberships))

    return garden, user_invitiation_tuples
