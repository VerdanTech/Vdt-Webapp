import pytest

from verdantech_api.apps.gardens.models import GardenMembership
from verdantech_api.apps.gardens.selectors import garden_get_visible, garden_list

pytestmark = pytest.mark.django_db


class TestGetVisibleGarden:
    def test_query_result(self, User, Garden):
        """
        Ensure the query filters by user and
        open invitation, and returns garden ids
        """

        user = User.create()
        gardens = Garden.create_batch(3)

        membership1 = GardenMembership(user=user, garden=gardens[1], open_invite=True)
        membership2 = GardenMembership(user=user, garden=gardens[2], open_invite=False)
        membership1.save()
        membership2.save()

        garden_ids = garden_get_visible(user=user)

        assert gardens[0].id not in garden_ids
        assert gardens[1].id not in garden_ids
        assert gardens[2].id in garden_ids


class TestGardenList:
    def test_query_result(self, User, Garden):
        """
        Ensure the query filters by user and
        open invitation, and returns garden objects
        """

        user = User.create()
        gardens = Garden.create_batch(3)

        membership1 = GardenMembership(user=user, garden=gardens[1], open_invite=True)
        membership2 = GardenMembership(user=user, garden=gardens[2], open_invite=False)
        membership1.save()
        membership2.save()

        returned_gardens = garden_list(fetched_by=user)

        assert gardens[0] not in returned_gardens
        assert gardens[1] not in returned_gardens
        assert gardens[2] in returned_gardens
