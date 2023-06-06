import pytest
from django.core.exceptions import PermissionDenied

from verdantech_api.apps.gardens.models import Garden, GardenMembership
from verdantech_api.apps.gardens.services import (
    garden_create,
    garden_create_parse_invitees,
    garden_membership_create,
)

pytestmark = pytest.mark.django_db


class TestGardenModelCreateParseInvitees:
    def test_users_returned(self, User):
        """
        Ensure that the users are properly
        fetched and not included if they
        don't exist
        """

        users = User.create_batch(3)

        input_list = [
            {"username": users[0].username, "role": "ADMIN"},
            {"username": users[1].username, "role": "EDIT"},
            {"username": users[2].username, "role": "VIEW"},
            {"username": "user_does_not_exist", "role": "ADMIN"},
        ]

        expected_output_list = [
            {"user": users[0], "role": "ADMIN"},
            {"user": users[1], "role": "EDIT"},
            {"user": users[2], "role": "VIEW"},
        ]

        output_list = garden_create_parse_invitees(input_list)

        assert output_list == expected_output_list


class TestGardenModelCreate:
    def test_arguments_set(self, User):
        """
        Ensure that the arguments
        are properly set
        """

        user = User.create()
        name = "test"
        visibility = Garden.VisibilityChoices.PUBLIC

        garden, invitations_sent = garden_create(
            name=name, creator=user, visibility=visibility
        )

        assert garden.name == name
        assert garden.creator == user
        assert garden.visibility == visibility
        assert invitations_sent is None

    def test_creator_and_admin_set(self, User):
        """
        Ensure that the admin role is
        properly set
        """

        user = User.create()
        name = "test"

        garden, invitations_sent = garden_create(name=name, creator=user)

        assert garden.members.count() == 1
        assert (
            garden.members.filter(user=user).first().role
            == GardenMembership.RoleChoices.ADMIN
        )

    def test_visibility_default(self, User):
        """
        Ensure that the default visibility is PRIVATE
        """

        user = User.create()
        name = "test"

        garden, invitations_sent = garden_create(name=name, creator=user)

        assert garden.visibility == Garden.VisibilityChoices.PRIVATE

    def test_extra_users_invited(self, User):
        """
        Ensure that extra users specified are invited
        """

        user = User.create()
        name = "test"

        invitees = User.create_batch(3)
        user_role_pairs = [
            {"user": invitees[0], "role": GardenMembership.RoleChoices.VIEW},
            {"user": invitees[1], "role": GardenMembership.RoleChoices.EDIT},
            {"user": invitees[2], "role": GardenMembership.RoleChoices.ADMIN},
        ]

        garden, invitations_sent = garden_create(
            name=name, creator=user, invitees=user_role_pairs
        )

        assert garden.members.count() == 4
        assert (
            garden.members.filter(user=invitees[0]).first().role
            == GardenMembership.RoleChoices.VIEW
        )
        assert (
            garden.members.filter(user=invitees[1]).first().role
            == GardenMembership.RoleChoices.EDIT
        )
        assert (
            garden.members.filter(user=invitees[2]).first().role
            == GardenMembership.RoleChoices.ADMIN
        )


class TestGardenMembershipModelCreate:
    def test_arguments_set(self, User, Garden):
        """
        Ensure that the arguments
        are properly set
        """

        garden = Garden.create()
        user = User.create()
        inviter = garden.members.first().user
        role = GardenMembership.RoleChoices.EDIT

        garden_membership = garden_membership_create(
            user=user, garden=garden, inviter=inviter, role=role
        )

        assert garden_membership.user == user
        assert garden_membership.garden == garden
        assert garden_membership.open_invite
        assert garden_membership.inviter == inviter
        assert garden_membership.role == role

    def test_default_role_view(self, User, Garden):
        """
        Ensure that if a role is not passed,
        it defaults to VIEW
        """

        garden = Garden.create()
        user = User.create()
        inviter = garden.members.first().user

        garden_membership = garden_membership_create(
            user=user, garden=garden, inviter=inviter
        )

        assert garden_membership.role == GardenMembership.RoleChoices.VIEW

    def test_user_in_garden(self, User, Garden):
        """
        Ensure that only users from within a garden
        can invite others to that garden
        """

        garden = Garden.create()
        user = User.create()
        inviter = User.create()

        with pytest.raises(PermissionDenied):
            garden_membership_create(user=user, garden=garden, inviter=inviter)

    def test_permissions(self, User, Garden):
        """
        Ensure that users without the admin role
        can only invite others to a role that
        less than their role's level of permissions
        """

        garden = Garden.create()
        users = User.create_batch(2)
        invitee = User.create()

        GardenMembership.objects.create(
            user=users[0], garden=garden, role=GardenMembership.RoleChoices.VIEW
        )
        GardenMembership.objects.create(
            user=users[1], garden=garden, role=GardenMembership.RoleChoices.EDIT
        )

        with pytest.raises(PermissionDenied):
            garden_membership_create(user=invitee, garden=garden, inviter=users[0])

        with pytest.raises(PermissionDenied):
            garden_membership_create(
                user=invitee,
                garden=garden,
                inviter=users[1],
                role=GardenMembership.RoleChoices.EDIT,
            )

        with pytest.raises(PermissionDenied):
            garden_membership_create(
                user=invitee,
                garden=garden,
                inviter=users[1],
                role=GardenMembership.RoleChoices.ADMIN,
            )
