import pytest

from verdantech_api.apps.core.exceptions import ApplicationError
from verdantech_api.apps.gardens.models import GardenMembership
from verdantech_api.apps.gardens.selectors import (
    garden_detail,
    garden_get_visible,
    garden_list,
    garden_members,
)

pytestmark = pytest.mark.django_db


class TestGetVisibleGarden:
    def test_query_result(self, UserMake, GardenMake):
        """
        Ensure the query filters by user and
        open invitation, and returns garden ids
        """

        user = UserMake.create()
        gardens = GardenMake.create_batch(3)

        membership1 = GardenMembership(user=user, garden=gardens[1], open_invite=True)
        membership2 = GardenMembership(user=user, garden=gardens[2], open_invite=False)
        membership1.save()
        membership2.save()

        garden_ids = garden_get_visible(user=user)

        assert gardens[0].id not in garden_ids
        assert gardens[1].id not in garden_ids
        assert gardens[2].id in garden_ids


class TestGardenList:
    def test_query_result(self, UserMake, GardenMake):
        """
        Ensure the query filters by user and
        open invitation, and returns garden objects
        """

        user = UserMake.create()
        gardens = GardenMake.create_batch(3)

        membership1 = GardenMembership(user=user, garden=gardens[1], open_invite=True)
        membership2 = GardenMembership(user=user, garden=gardens[2], open_invite=False)
        membership1.save()
        membership2.save()

        returned_gardens = garden_list(fetched_by=user)

        assert gardens[0] not in returned_gardens
        assert gardens[1] not in returned_gardens
        assert gardens[2] in returned_gardens


class TestGardenDetail:
    def test_query_result(self, UserMake, GardenMake):
        """
        Ensure the query filters by user
        and returns a single garden object
        """

        user = UserMake.create()
        garden = GardenMake.create()

        membership1 = GardenMembership(user=user, garden=garden, open_invite=False)
        membership1.save()

        garden_query = garden_detail(fetched_by=user, hashid=garden.hashid)

        assert garden_query == garden

    def test_does_not_exist(self, UserMake):
        """
        Ensure the query raises an application error
        for a garden which does not exist
        """

        user = UserMake.create()

        with pytest.raises(ApplicationError):
            garden_detail(fetched_by=user, hashid="888888")


class TestGardenMembers:
    def test_result(self, UserMake, BaseGardenMake):
        """
        Ensure the function produces the
        correct output
        """

        users = UserMake.create_batch(3)
        garden = BaseGardenMake.create()

        membership1 = GardenMembership(user=users[0], garden=garden, open_invite=False)
        membership2 = GardenMembership(user=users[1], garden=garden, open_invite=False)
        membership3 = GardenMembership(user=users[2], garden=garden, open_invite=True)
        membership1.save()
        membership2.save()
        membership3.save()

        expected_output = [
            {"username": users[0].username, "role": "VIEW"},
            {"username": users[1].username, "role": "VIEW"},
        ]

        members = garden_members(garden)

        assert members == expected_output
