import pytest
from django.core.exceptions import ValidationError


class TestGardenModelValidaton:
    def test_minimum_admins(self, mocker, BaseGarden):
        """
        Ensure there is at least one admin in a garden.
        """

        garden = BaseGarden()
        garden_mock = mocker.Mock(return_value=garden)

        with pytest.raises(ValidationError) as excinfo:
            garden_mock.validate_constraints()
            print(excinfo)

    @pytest.mark.skip
    def test_one_role_per_user(self, User, Garden):
        """
        Ensure users are in at most one role.
        """

        user = User.build()
        gardens = Garden.build_batch(6)

        gardens[0].admins.add(user)
        gardens[0].admins.add(user)

        gardens[1].editors.add(user)
        gardens[1].editors.add(user)

        gardens[2].viewers.add(user)
        gardens[2].viewers.add(user)

        gardens[3].admins.add(user)
        gardens[3].editors.add(user)

        gardens[4].admins.add(user)
        gardens[4].viewers.add(user)

        gardens[5].editors.add(user)
        gardens[5].viewers.add(user)

        for garden in gardens:
            with pytest.raises(ValidationError):
                garden.clean()

    @pytest.mark.skip
    def test_name_unique_in_creator(self, User, Garden):
        """
        Ensure that garden names within a user's collection
        of created gardens are unique
        """

        user = User.build()
        gardens = Garden.build_batch(2)
        gardens[0].name = "test"
        gardens[1].name = "test"
        gardens[0].creator = user
        gardens[1].creator = user

        with pytest.raises(ValidationError):
            gardens[0].validate_constraints()
        with pytest.raises(ValidationError):
            gardens[1].validate_constraints()


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
