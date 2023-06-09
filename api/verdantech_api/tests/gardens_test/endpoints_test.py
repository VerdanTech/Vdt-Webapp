import pytest
from django.urls import reverse
from rest_framework import status

from verdantech_api.apps.core.exceptions import ApplicationError
from verdantech_api.apps.gardens.models import Garden, GardenMembership

pytestmark = pytest.mark.django_db

garden_list_endpoint = reverse("garden_list")
garden_create_endpoint = reverse("garden_create")
garden_membership_invite_list_endpoint = reverse("garden_membership_invite_list")


class TestGardenListEndpoint:
    def test_garden_list(self, client, UserMake, GardenMake):
        """
        Ensure the garden list endpoint returns
        the correct gardens
        """

        user = UserMake.create()
        client.force_authenticate(user=user)
        gardens = GardenMake.create_batch(4)

        membership1 = GardenMembership(user=user, garden=gardens[1], open_invite=True)
        membership2 = GardenMembership(user=user, garden=gardens[2], open_invite=False)
        gardens[2].creator = user
        gardens[2].save()
        membership3 = GardenMembership(user=user, garden=gardens[3], open_invite=False)
        membership1.save()
        membership2.save()
        membership3.save()

        expected_response = [
            {
                "hashid": gardens[2].hashid,
                "name": gardens[2].name,
                "creator_username": user.username,
            },
            {
                "hashid": gardens[3].hashid,
                "name": gardens[3].name,
                "creator_username": "",
            },
        ]

        response = client.get(
            garden_list_endpoint,
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data == expected_response


class TestGardenCreateEndpoint:
    def test_garden_create(self, client, UserMake):
        """
        Ensure that the endpoint
        creates a garden sucessfully
        """

        user = UserMake.create()
        client.force_authenticate(user=user)

        request = {"name": "test_garden"}

        response = client.post(garden_create_endpoint, data=request, format="json")

        garden_hashid = (
            Garden.objects.filter(creator=user, name="test_garden").first().hashid
        )
        expected_response = {
            "hashid": garden_hashid,
            "name": "test_garden",
            "invitations_sent": None,
        }

        assert response.status_code == status.HTTP_200_OK
        assert response.data == expected_response

    def test_garden_create_invitations(self, client, UserMake):
        """
        Ensure that the endpoint
        invites users sucessfully
        """

        users = UserMake.create_batch(4)
        client.force_authenticate(user=users[0])

        request = {
            "name": "test_garden",
            "invitees": [
                {"username": users[1].username, "role": "ADMIN"},
                {"username": users[2].username, "role": "EDIT"},
                {"username": users[3].username, "role": "VIEW"},
                {"username": "user_does_not_exist", "role": "VIEW"},
            ],
        }

        response = client.post(garden_create_endpoint, data=request, format="json")

        garden_hashid = (
            Garden.objects.filter(creator=users[0], name="test_garden").first().hashid
        )
        expected_response = {
            "hashid": garden_hashid,
            "name": "test_garden",
            "invitations_sent": [
                {"username": users[1].username, "role": "ADMIN"},
                {"username": users[2].username, "role": "EDIT"},
                {"username": users[3].username, "role": "VIEW"},
            ],
        }

        assert response.status_code == status.HTTP_200_OK
        assert response.data == expected_response


class TestGardenDetailEndpoint:
    def test_garden_detail(self, client, UserMake, BaseGardenMake):
        """
        Ensure that the garden detail endpoint
        returns the correct details
        """
        users = UserMake.create_batch(3)
        client.force_authenticate(user=users[0])
        garden = BaseGardenMake.create()

        membership1 = GardenMembership(user=users[0], garden=garden, open_invite=False)
        membership2 = GardenMembership(user=users[1], garden=garden, open_invite=False)
        membership3 = GardenMembership(user=users[2], garden=garden, open_invite=True)
        membership1.save()
        membership2.save()
        membership3.save()

        expected_response = {
            "hashid": garden.hashid,
            "name": garden.name,
            "visibility": garden.visibility,
            "members": [
                {"username": users[0].username, "role": "VIEW"},
                {"username": users[1].username, "role": "VIEW"},
            ],
        }

        endpoint = reverse("garden_detail", args=[garden.hashid])
        response = client.get(endpoint)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == expected_response

    def test_garden_detail_does_not_exist(self, client, UserMake, BaseGardenMake):
        """
        Ensure that the garden detail endpoint
        returns the correct error for inaccessible
        gardens
        """

        user = UserMake.create()
        client.force_authenticate(user=user)
        garden = BaseGardenMake.create()

        expected_response = {
            "message": "Garden does not exist or is not accessible to the user",
            "extra": {},
        }

        endpoint = reverse("garden_detail", args=[garden.hashid])

        response = client.get(endpoint)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == expected_response


class TestGardenUpdateEndpoint:
    def test_garden_update(self, client, UserMake, GardenMake):
        """
        Ensure that the garden update endpoint
        updates the correct details
        """

        user = UserMake.create()
        client.force_authenticate(user=user)
        garden = GardenMake.create()

        GardenMembership.objects.create(
            user=user,
            garden=garden,
            role=GardenMembership.RoleChoices.ADMIN,
            open_invite=False,
        )

        new_name = "test"
        new_visibility = "PUBLIC"

        request = {"name": new_name, "visibility": new_visibility}

        expected_response = {
            "hashid": garden.hashid,
            "name": new_name,
            "visibility": new_visibility,
        }

        endpoint = reverse("garden_update", args=[garden.hashid])
        response = client.post(endpoint, data=request, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert response.data == expected_response


class TestGardenInviteListEndpoint:
    def test_garden_invite_list(self, client, UserMake, GardenMake):
        """
        Ensure the garden invite list endpoint
        returns the correct invites
        """

        user = UserMake.create()
        client.force_authenticate(user=user)
        gardens = GardenMake.create_batch(3)

        admin0 = Garden.objects.filter(id=gardens[0].id).first().users.first()
        membership0 = GardenMembership.objects.create(
            user=user, garden=gardens[0], inviter=admin0, open_invite=True
        )
        admin1 = Garden.objects.filter(id=gardens[1].id).first().users.first()
        membership1 = GardenMembership.objects.create(
            user=user, garden=gardens[1], inviter=admin1, open_invite=True
        )
        admin2 = Garden.objects.filter(id=gardens[2].id).first().users.first()
        membership2 = GardenMembership.objects.create(
            user=user, garden=gardens[2], inviter=admin2, open_invite=False
        )

        expected_response = [
            {
                "hashid": gardens[0].hashid,
                "name": gardens[0].name,
                "inviter_username": admin0.username,
                "role": membership0.role,
            },
            {
                "hashid": gardens[1].hashid,
                "name": gardens[1].name,
                "inviter_username": admin1.username,
                "role": membership1.role,
            },
        ]

        response = client.get(garden_membership_invite_list_endpoint, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert response.data == expected_response


class TestGardenInviteEndpoint:
    def test_garden_invite(self, client, UserMake, GardenMake):
        """
        Ensure that a garden invite is
        successfully created
        """
        user = UserMake.create()
        garden = GardenMake.create()

        admin = (
            garden.members.filter(role=GardenMembership.RoleChoices.ADMIN).first().user
        )
        client.force_authenticate(user=admin)
        print(admin.username)

        request = {"username": user.username, "role": "ADMIN"}

        expected_response = {"username": user.username, "role": "ADMIN"}

        endpoint = reverse("garden_membership_invite_create", args=[garden.hashid])
        response = client.post(endpoint, data=request, format="json")

        assert response.status_code == status.HTTP_200_OK
        assert response.data == expected_response


class TestGardenInviteAcceptEndpoint:
    pass


class TestGardenInviteRejectEndpoint:
    pass


class TestGardenMembershipDemoteEndpoint:
    pass


class TestGardenMembershipRevokeEndpoint:
    pass
