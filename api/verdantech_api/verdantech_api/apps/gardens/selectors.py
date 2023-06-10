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


def garden_membership_get_visible(fetched_by: User) -> List[int]:
    """
    Return all garden memberships containing the user
    or containing a garden the user is associated with
    """

    garden_ids = garden_get_visible(fetched_by=fetched_by)

    query = Q(user=fetched_by) | Q(garden__id__in=garden_ids)

    return GardenMembership.objects.filter(query).values_list("garden_id", flat=True)


def garden_membership_detail(
    fetched_by: User, username: str, hashid: str
) -> GardenMembership:
    """
    Given a username and garden, get
    the garden membership if the user
    has access to it
    """

    membership_ids = garden_membership_get_visible(fetched_by=fetched_by)

    query = (
        Q(id__in=membership_ids) & Q(user__username=username) & Q(garden__hashid=hashid)
    )

    membership = GardenMembership.objects.filter(query).first()

    if membership is None:
        raise ApplicationError(
            message="Membership does not exist or is not accessible to the user"
        )

    return GardenMembership.objects.filter(query).first()


def garden_membership_invite_list(fetched_by: User) -> List[GardenMembership]:
    """
    Return a list of garden memberships
    with open or closed invites
    """

    membership_ids = garden_membership_get_visible(fetched_by=fetched_by)

    query = Q(id__in=membership_ids) & Q(user=fetched_by) & Q(open_invite=True)

    return GardenMembership.objects.filter(query).all()


def garden_membership_invite_detail(fetched_by: User, id: int) -> GardenMembership:
    """
    Return the garden membership invite
    with the given ID
    """

    membership_ids = garden_membership_get_visible(fetched_by=fetched_by)

    query = (
        Q(id__in=membership_ids) & Q(id=id) & Q(user=fetched_by) & Q(open_invite=True)
    )

    membership_invite = GardenMembership.objects.filter(query).first()

    if membership_invite is None:
        raise ApplicationError(
            message="Invite does not exist or is not accessible to the user"
        )

    return membership_invite
