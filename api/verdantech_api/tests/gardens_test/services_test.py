import pytest
from django.core.exceptions import PermissionDenied

from verdantech_api.apps.core.exceptions import ApplicationError
from verdantech_api.apps.gardens.models import Garden, GardenMembership
from verdantech_api.apps.gardens.services import (
    garden_create,
    garden_create_parse_invitees,
    garden_membership_accept,
    garden_membership_create,
    garden_membership_delete,
    garden_membership_update,
    garden_update,
)

pytestmark = pytest.mark.django_db


class TestGardenCreateParseInvitees:
    def test_users_returned(self, UserMake):
        """
        Ensure that the users are properly
        fetched and not included if they
        don't exist
        """

        users = UserMake.create_batch(3)

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


class TestGardenCreate:
    def test_arguments_set(self, UserMake):
        """
        Ensure that the arguments
        are properly set
        """

        user = UserMake.create()
        name = "test"
        visibility = Garden.VisibilityChoices.PUBLIC

        garden, invitations_sent = garden_create(
            name=name, creator=user, visibility=visibility
        )

        assert garden.name == name
        assert garden.creator == user
        assert garden.visibility == visibility
        assert invitations_sent is None

    def test_creator_and_admin_set(self, UserMake):
        """
        Ensure that the admin role is
        properly set
        """

        user = UserMake.create()
        name = "test"

        garden, invitations_sent = garden_create(name=name, creator=user)

        assert garden.members.count() == 1
        assert (
            garden.members.filter(user=user).first().role
            == GardenMembership.RoleChoices.ADMIN
        )

    def test_visibility_default(self, UserMake):
        """
        Ensure that the default visibility is PRIVATE
        """

        user = UserMake.create()
        name = "test"

        garden, invitations_sent = garden_create(name=name, creator=user)

        assert garden.visibility == Garden.VisibilityChoices.PRIVATE

    def test_extra_users_invited(self, UserMake):
        """
        Ensure that extra users specified are invited
        """

        user = UserMake.create()
        name = "test"

        invitees = UserMake.create_batch(3)
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


class TestGardenUpdate:
    def test_arguments_updated(self, UserMake, GardenMake):
        """
        Ensure that the arguments are properly updated
        """

        user = UserMake.create()
        garden = GardenMake.create()

        GardenMembership.objects.create(
            user=user,
            garden=garden,
            role=GardenMembership.RoleChoices.ADMIN,
            open_invite=False,
        )

        new_name = "test"
        new_visibility = "PUBLIC"

        garden = garden_update(
            user=user, hashid=garden.hashid, name=new_name, visibility=new_visibility
        )

        assert garden.name == new_name
        assert garden.visibility == new_visibility

    def test_admin_required(self, UserMake, GardenMake):
        """
        Ensure that the admin role is required
        """

        user = UserMake.create()
        garden = GardenMake.create()

        GardenMembership.objects.create(
            user=user,
            garden=garden,
            role=GardenMembership.RoleChoices.EDIT,
            open_invite=False,
        )

        new_name = "test"
        new_visibility = "PUBLIC"

        with pytest.raises(PermissionDenied):
            garden = garden_update(
                user=user,
                hashid=garden.hashid,
                name=new_name,
                visibility=new_visibility,
            )


class TestGardenMembershipCreate:
    def test_arguments_set(self, UserMake, GardenMake):
        """
        Ensure that the arguments
        are properly set
        """

        garden = GardenMake.create()
        user = UserMake.create()
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

    def test_default_role_view(self, UserMake, GardenMake):
        """
        Ensure that if a role is not passed,
        it defaults to VIEW
        """

        garden = GardenMake.create()
        user = UserMake.create()
        inviter = garden.members.first().user

        garden_membership = garden_membership_create(
            user=user, garden=garden, inviter=inviter
        )

        assert garden_membership.role == GardenMembership.RoleChoices.VIEW

    def test_user_in_garden(self, UserMake, GardenMake):
        """
        Ensure that only users from within a garden
        can invite others to that garden
        """

        garden = GardenMake.create()
        user = UserMake.create()
        inviter = UserMake.create()

        with pytest.raises(PermissionDenied):
            garden_membership_create(user=user, garden=garden, inviter=inviter)

    def test_permissions(self, UserMake, GardenMake):
        """
        Ensure that users without the admin role
        can only invite others to a role that
        less than their role's level of permissions
        """

        garden = GardenMake.create()
        users = UserMake.create_batch(2)
        invitee = UserMake.create()

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


class TestGardenMembershipAccept:
    def test_membership_accepted(self, UserMake, GardenMake):
        """
        Ensure that the membership invite
        is successfully updated
        """

        user = UserMake.create()
        garden = GardenMake.create()

        membership_invite = GardenMembership.objects.create(
            user=user, garden=garden, open_invite=True
        )

        membership = garden_membership_accept(
            user=user, membership_invite_id=membership_invite.id
        )

        assert membership == membership_invite
        assert membership.open_invite is False


class TestGardenMembershipUpdate:
    def test_membership_updated(self, UserMake, GardenMake):
        """
        Ensure the model is updated sucessfully
        """

        users = UserMake.create_batch(2)
        garden = GardenMake.create()

        GardenMembership.objects.create(
            user=users[0],
            garden=garden,
            open_invite=False,
            role=GardenMembership.RoleChoices.ADMIN,
        )
        membership = GardenMembership.objects.create(
            user=users[1],
            garden=garden,
            open_invite=False,
            role=GardenMembership.RoleChoices.VIEW,
        )

        garden_membership_update(
            user=users[0],
            membership=membership,
            new_role=GardenMembership.RoleChoices.EDIT,
        )

        assert membership.role == GardenMembership.RoleChoices.EDIT

    def test_admin_required(self, UserMake, GardenMake):
        """
        Ensure that admin permissions are required
        """

        users = UserMake.create_batch(2)
        garden = GardenMake.create()

        GardenMembership.objects.create(
            user=users[0],
            garden=garden,
            open_invite=False,
            role=GardenMembership.RoleChoices.EDIT,
        )
        membership = GardenMembership.objects.create(
            user=users[1],
            garden=garden,
            open_invite=False,
            role=GardenMembership.RoleChoices.VIEW,
        )

        with pytest.raises(PermissionDenied):
            garden_membership_update(
                user=users[0],
                membership=membership,
                new_role=GardenMembership.RoleChoices.EDIT,
            )

    def test_admins_cant_demote_themselves(self, UserMake, GardenMake):
        """
        Ensure that admins can't change their own roles
        """

        user = UserMake.create()
        garden = GardenMake.create()

        membership = GardenMembership.objects.create(
            user=user,
            garden=garden,
            open_invite=False,
            role=GardenMembership.RoleChoices.ADMIN,
        )

        with pytest.raises(ApplicationError):
            garden_membership_update(
                user=user,
                membership=membership,
                new_role=GardenMembership.RoleChoices.EDIT,
            )

    def test_cant_demote_creator(self, UserMake, GardenMake):
        """
        Ensure that the creator of a garden cant have
        their permissions changed
        """

        users = UserMake.create_batch(2)
        garden = GardenMake.create()

        GardenMembership.objects.create(
            user=users[0],
            garden=garden,
            open_invite=False,
            role=GardenMembership.RoleChoices.ADMIN,
        )
        membership = GardenMembership.objects.create(
            user=users[1],
            garden=garden,
            open_invite=False,
            role=GardenMembership.RoleChoices.ADMIN,
        )
        garden.creator = users[1]

        with pytest.raises(ApplicationError):
            garden_membership_update(
                user=users[0],
                membership=membership,
                new_role=GardenMembership.RoleChoices.EDIT,
            )


class TestGardenMembershipDelete:
    def test_admin_membership_deleted(self, UserMake, GardenMake):
        """
        Ensure that an admin can delete a membership
        """
        users = UserMake.create_batch(2)
        garden = GardenMake.create()

        GardenMembership.objects.create(
            user=users[0],
            garden=garden,
            open_invite=False,
            role=GardenMembership.RoleChoices.ADMIN,
        )
        membership = GardenMembership.objects.create(
            user=users[1],
            garden=garden,
            open_invite=False,
            role=GardenMembership.RoleChoices.VIEW,
        )
        id = membership.id

        garden_membership_delete(
            user=users[0],
            membership=membership,
        )

        assert GardenMembership.objects.filter(id=id).exists() is False

    def test_self_membership_deleted(self, UserMake, GardenMake):
        """
        Ensure that a user can delete their own membership
        """
        user = UserMake.create()
        garden = GardenMake.create()

        membership = GardenMembership.objects.create(
            user=user,
            garden=garden,
            open_invite=False,
            role=GardenMembership.RoleChoices.VIEW,
        )
        id = membership.id

        garden_membership_delete(
            user=user,
            membership=membership,
        )

        assert GardenMembership.objects.filter(id=id).exists() is False

    def test_admin_required(self, UserMake, GardenMake):
        """
        Ensure that admin permissions are required
        """

        users = UserMake.create_batch(2)
        garden = GardenMake.create()

        GardenMembership.objects.create(
            user=users[0],
            garden=garden,
            open_invite=False,
            role=GardenMembership.RoleChoices.EDIT,
        )
        membership = GardenMembership.objects.create(
            user=users[1],
            garden=garden,
            open_invite=False,
            role=GardenMembership.RoleChoices.VIEW,
        )

        with pytest.raises(PermissionDenied):
            garden_membership_delete(
                user=users[0],
                membership=membership,
            )

    def test_cant_kick_creator(self, UserMake, GardenMake):
        """
        Ensure that the creator of a garden cant have
        their membership deleted
        """
        users = UserMake.create_batch(2)
        garden = GardenMake.create()

        GardenMembership.objects.create(
            user=users[0],
            garden=garden,
            open_invite=False,
            role=GardenMembership.RoleChoices.ADMIN,
        )
        membership = GardenMembership.objects.create(
            user=users[1],
            garden=garden,
            open_invite=False,
            role=GardenMembership.RoleChoices.ADMIN,
        )
        garden.creator = users[1]

        with pytest.raises(ApplicationError):
            garden_membership_delete(user=users[0], membership=membership)
