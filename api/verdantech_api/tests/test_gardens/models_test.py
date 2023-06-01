import pytest
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from verdantech_api.apps.gardens.models import GardenMembership

pytestmark = pytest.mark.django_db


class TestGardenModelValidaton:

    # This is supposed to be a unit test, but I can't figure out how to mock the many-to-many models
    def test_minimum_admins(self, mocker, BaseGarden):
        """
        Ensure there is at least one admin in a garden.
        """

        garden = BaseGarden()
        garden.save()

        with pytest.raises(ValidationError):
            garden.clean()


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


class TestGardenModelCreate:
    def test_creator_and_admin_set(self):
        """
        Ensure that creator and admin lists are set
        """
        pass

    def test_extra_users_invited(self):
        """
        Ensure that extra users specified are invited
        """
        pass

    def test_default_timezone(self):
        """
        Ensure timezone is set to creator's timezone
        """
        pass

    def test_address_or_coordinates_set(self):
        """
        Ensure that, if either the address or the
        coordinates are being set,
        """

        pass
