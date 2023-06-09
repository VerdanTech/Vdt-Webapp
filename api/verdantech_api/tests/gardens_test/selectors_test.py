import pytest

from verdantech_api.apps.core.exceptions import ApplicationError
from verdantech_api.apps.gardens.models import GardenMembership
from verdantech_api.apps.gardens.selectors import (
    garden_detail,
    garden_get_visible,
    garden_list,
    garden_members,
    garden_membership_invite_detail,
    garden_membership_invite_list,
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


class TestGardenMembershipInvitesList:
    def test_query_result(self, UserMake, GardenMake):
        """
        Ensure that the function returns
        all memberships with open invites
        """

        user = UserMake.create()
        gardens = GardenMake.create_batch(3)

        membership1 = GardenMembership.objects.create(
            user=user, garden=gardens[0], open_invite=True
        )
        membership2 = GardenMembership.objects.create(
            user=user, garden=gardens[1], open_invite=True
        )
        membership3 = GardenMembership.objects.create(
            user=user, garden=gardens[2], open_invite=False
        )

        memberships = garden_membership_invite_list(fetched_by=user)

        assert membership1 in memberships
        assert membership2 in memberships
        assert membership3 not in memberships


class TestGardenMembershipInviteDetail:
    def test_query_result(self, UserMake, GardenMake):
        """
        Ensure the query filters by user
        and returns a single GardenMembership object
        """

        user = UserMake.create()
        garden = GardenMake.create()

        membership = GardenMembership.objects.create(
            user=user, garden=garden, open_invite=True
        )

        garden_membership_invite_query = garden_membership_invite_detail(
            fetched_by=user, id=membership.id
        )

        assert garden_membership_invite_query == membership

    def test_does_not_exist(self, UserMake, GardenMake):
        """
        Ensure the query raises an application error
        for an invite which does not exist
        """

        users = UserMake.create_batch(2)
        gardens = GardenMake.create_batch(2)

        membership1 = GardenMembership.objects.create(
            user=users[0], garden=gardens[0], open_invite=False
        )
        membership2 = GardenMembership.objects.create(
            user=users[1], garden=gardens[0], open_invite=True
        )
        membership3 = GardenMembership.objects.create(
            user=users[1], garden=gardens[1], open_invite=True
        )

        with pytest.raises(ApplicationError):
            garden_membership_invite_detail(fetched_by=users[0], id=membership1.id)
        with pytest.raises(ApplicationError):
            garden_membership_invite_detail(fetched_by=users[0], id=membership2.id)
        with pytest.raises(ApplicationError):
            garden_membership_invite_detail(fetched_by=users[0], id=membership3.id)
