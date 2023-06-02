from typing import List, Tuple

from django.core.exceptions import PermissionDenied

from verdantech_api.apps.accounts.models import User

from .models import Garden, GardenMembership

user_role_pair_list = List[Tuple[User, str]]


def garden_create(
    name: str,
    creator: User,
    invitees: user_role_pair_list = None,
    visibility: str = Garden.VisibilityChoices.PRIVATE,
) -> Garden:
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
    if invitees:
        for user_role_pair in invitees:
            garden_membership_create(
                user=user_role_pair[0],
                garden=garden,
                inviter=creator,
                role=user_role_pair[1],
            )

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
