from typing import Dict, List, Tuple

from django.core.exceptions import PermissionDenied

from verdantech_api.apps.accounts.models import User

from .models import Garden, GardenMembership
from .selectors import garden_detail, garden_membership_invite_detail


def garden_create_parse_invitees(
    invitees: List[Dict[str, str]] = None
) -> List[Dict[User, str]]:
    """
    Turn the list of usernames and roles into a list
    of users and roles, not including any usernames
    that don't exist
    """

    if invitees is None:
        return None

    # Extract usernames from invitee list
    usernames = [invitee["username"] for invitee in invitees]

    # Get user objects
    users = User.objects.filter(username__in=usernames)

    # Construct output list
    output_list = []
    for invitee in invitees:

        # Add user object to output list only if it exists
        user = next(
            (user for user in users if user.username == invitee["username"]), None
        )
        if user is not None:
            output_list.append({"user": user, "role": invitee["role"]})

    return output_list


def garden_create(
    name: str,
    creator: User,
    invitees: List[Dict[User, str]] = None,
    visibility: str = Garden.VisibilityChoices.PRIVATE,
) -> Tuple[Garden, List[Dict[str, str]]]:
    """Create a new garden and save it to the database"""

    # Create the model
    garden = Garden(name=name, creator=creator, visibility=visibility)
    garden.full_clean()
    garden.save()

    # Add the creator as admin
    garden_membership = GardenMembership(
        user=creator,
        garden=garden,
        open_invite=False,
        inviter=creator,
        role=GardenMembership.RoleChoices.ADMIN,
    )
    garden_membership.full_clean()
    garden_membership.save()

    # Add any invitees
    invitations_sent = None
    if invitees:
        for user_role_pair in invitees:
            user = user_role_pair["user"]
            role = user_role_pair["role"]
            garden_membership_create(
                user=user,
                garden=garden,
                inviter=creator,
                role=role,
            )

        # Construct list of users invited
        invitations_sent = [
            {
                "username": user_role_pair["user"].username,
                "role": user_role_pair["role"],
            }
            for user_role_pair in invitees
        ]

    return garden, invitations_sent


def garden_update(
    user: User, hashid: str, name: str = None, visibility: str = None
) -> Garden:
    """
    Update the garden name, or visibility
    """

    garden = garden_detail(fetched_by=user, hashid=hashid)
    membership = garden.members.filter(user=user).first()

    if membership.role != GardenMembership.RoleChoices.ADMIN:
        raise PermissionDenied()

    updated = False
    if name is not None:
        garden.name = name
        updated = True
    if visibility is not None:
        garden.visibility = visibility
        updated = True

    if updated:
        garden.full_clean()
        garden.save()

    return garden


def garden_membership_create(
    user: User,
    garden: Garden,
    inviter: User,
    role: str = GardenMembership.RoleChoices.VIEW,
) -> GardenMembership:
    """
    Create a new garden membership and save it to the database
    """

    # Ensure that only users from within a garden can send invites
    inviter_membership = GardenMembership.objects.filter(
        garden=garden, user=inviter
    ).first()
    if not inviter_membership:
        raise PermissionDenied(
            "Users must have an existing membership in a garden to invite others"
        )

    # If this is an invitiation, ensure proper permissions
    inviter_role = inviter_membership.role

    if inviter_role == GardenMembership.RoleChoices.VIEW:
        raise PermissionDenied(
            "Users with the VIEW permission cannot invite others to a garden"
        )
    elif inviter_role == GardenMembership.RoleChoices.EDIT and (
        role == GardenMembership.RoleChoices.EDIT
        or role == GardenMembership.RoleChoices.ADMIN
    ):
        raise PermissionDenied(
            "Users with the EDIT permission can only invite others to the VIEW role"
        )

    # Create the model
    garden_membership = GardenMembership(
        inviter=inviter, user=user, garden=garden, role=role, open_invite=True
    )
    garden_membership.full_clean()
    garden_membership.save()

    return garden_membership


def garden_membership_accept(user: User, membership_invite_id: int) -> GardenMembership:
    """
    Accept the invite for a garden membership,
    turning the open_invite field to false
    """

    membership_invite = garden_membership_invite_detail(
        fetched_by=user, id=membership_invite_id
    )

    membership_invite.open_invite = False
    membership_invite.full_clean()
    membership_invite.save()

    return membership_invite


def garden_membership_update(user: User):
    pass


def garden_membership_delete():
    pass
