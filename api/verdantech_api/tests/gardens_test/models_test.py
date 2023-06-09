import pytest
from django.db.utils import IntegrityError

from verdantech_api.apps.gardens.models import GardenMembership

pytestmark = pytest.mark.django_db


class TestGardenModelValidaton:
    def test_minimum_admins(self, BaseGardenMake):
        """
        Ensure the garden shows as abandoned if there is no admins
        """

        garden = BaseGardenMake.create()

        assert garden.is_abandoned()

    def test_hashid_set(self, BaseGardenMake):
        """
        Ensure that the garden's hashid is set upon creation
        """

        garden = BaseGardenMake.create()

        assert garden.hashid is not None


class TestGardenMembershipModelValidation:
    def test_one_membership_per_user_per_garden(self, UserMake, GardenMake):
        """
        Ensure users only have one membership per garden
        """

        user = UserMake.create()
        garden = GardenMake.create()

        membership1 = GardenMembership(
            user=user, garden=garden, role=GardenMembership.RoleChoices.ADMIN
        )
        membership1.save()

        with pytest.raises(IntegrityError):
            membership2 = GardenMembership(
                user=user, garden=garden, role=GardenMembership.RoleChoices.ADMIN
            )
            membership2.save()
