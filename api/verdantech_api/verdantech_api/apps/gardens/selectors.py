from typing import Dict, List

from django.db.models import Q

from verdantech_api.apps.accounts.models import User
from verdantech_api.apps.core.exceptions import ApplicationError
from verdantech_api.apps.gardens.models import Garden, GardenMembership


def garden_get_visible(user: User) -> List[int]:
    """
    Return a list of Garden primary keys that is
    visible to the given user
    """

    query = Q(user=user) & Q(open_invite=False)

    return GardenMembership.objects.filter(query).values_list("garden_id", flat=True)


def garden_list(fetched_by: User) -> List[Garden]:
    """
    Return the list of garden objects that are
    visible to the given user
    """

    garden_ids = garden_get_visible(user=fetched_by)
    query = Q(id__in=garden_ids)

    return Garden.objects.filter(query)


def garden_detail(fetched_by: User, hashid: str) -> Garden:
    """
    Return the garden requested by the user
    """

    garden_ids = garden_get_visible(user=fetched_by)
    query = Q(id__in=garden_ids) & Q(hashid=hashid)

    garden = Garden.objects.filter(query).first()

    if garden is None:
        raise ApplicationError(
            message="Garden does not exist or is not accessible to the user"
        )

    return garden


def garden_members(garden: Garden) -> List[Dict[str, str]]:
    """
    Return a list of dicts containing the members
    of a garden and their roles
    """
    members = []
    for membership in garden.members.all():
        if not membership.open_invite:
            members.append(
                {"username": membership.user.username, "role": membership.role}
            )

    return members


def garden_membership_invite_list(fetched_by: User) -> List[GardenMembership]:
    """
    Return a list of garden memberships
    with open invites
    """

    query = Q(user=fetched_by) & Q(open_invite=True)
    return GardenMembership.objects.filter(query).all()


def garden_membership_invite_detail(fetched_by: User, id: int) -> GardenMembership:
    """
    Return the garden membership with the
    given ID
    """

    membership_invite = (
        garden_membership_invite_list(fetched_by=fetched_by).filter(id=id).first()
    )

    if membership_invite is None:
        raise ApplicationError(
            message="Invite does not exist or is not accessible to the user"
        )

    return membership_invite
