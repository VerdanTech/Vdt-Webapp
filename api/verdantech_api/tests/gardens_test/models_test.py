import pytest
from django.db.utils import IntegrityError

from verdantech_api.apps.gardens.models import GardenMembership

pytestmark = pytest.mark.django_db


class TestGardenModelValidaton:
    def test_minimum_admins(self, BaseGarden):
        """
        Ensure the garden shows as abandoned if there is no admins
        """

        garden = BaseGarden.create()

        assert garden.is_abandoned()

    def test_hashid_set(self, BaseGarden):
        """
        Ensure that the garden's hashid is set upon creation
        """

        garden = BaseGarden.create()

        assert garden.hashid is not None


class TestGardenMembershipModelValidation:
    def test_one_membership_per_user_per_garden(self, User, Garden):
        """
        Ensure users only have one membership per garden
        """

        user = User.create()
        garden = Garden.create()

        membership1 = GardenMembership(
            user=user, garden=garden, role=GardenMembership.RoleChoices.ADMIN
        )
        membership1.save()

        with pytest.raises(IntegrityError):
            membership2 = GardenMembership(
                user=user, garden=garden, role=GardenMembership.RoleChoices.ADMIN
            )
            membership2.save()
