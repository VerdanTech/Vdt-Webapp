from typing import List

from django.db.models import Q

from verdantech_api.apps.accounts.models import User
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
