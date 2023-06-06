import pytest
from django.urls import reverse
from rest_framework import status

from verdantech_api.apps.gardens.models import Garden, GardenMembership

pytestmark = pytest.mark.django_db

garden_list_endpoint = reverse("garden_list")
garden_create_endpoint = reverse("garden_create")


class TestGardenListEndpoint:
    def test_garden_list(self, client, User, Garden):
        """
        Ensure the garden list endpoint returns
        the correct gardens
        """

        user = User.create()
        client.force_authenticate(user=user)
        gardens = Garden.create_batch(4)

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
                "id": gardens[2].id,
                "hashid": gardens[2].hashid,
                "name": gardens[2].name,
                "creator_username": user.username,
            },
            {
                "id": gardens[3].id,
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
    def test_garden_create(self, client, User):
        """
        Ensure that the endpoint
        creates a garden sucessfully
        """

        user = User.create()
        client.force_authenticate(user=user)

        request = {"name": "test_garden"}

        response = client.post(garden_create_endpoint, data=request, format="json")

        garden_hashid = (
            Garden.objects.filter(creator=user, name="test_garden").first().hashid
        )
        expected_response = {
            "id": 1,
            "hashid": garden_hashid,
            "name": "test_garden",
            "invitations_sent": None,
        }

        assert response.status_code == status.HTTP_200_OK
        assert response.data == expected_response

    def test_garden_create_invitations(self, client, User):
        """
        Ensure that the endpoint
        invites users sucessfully
        """

        users = User.create_batch(4)
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
            "id": 1,
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
    def test_garden_detail(self, client, User, Garden):
        """
        Ensure that the garden detail endpoint
        returns the correct details
        """
        pass

    def test_garden_detail_permissions(self, client, User, Garden):
        """
        Ensure that the garden detail endpoint
        returns the correct error for inaccessible
        gardens
        """
        pass


class TestGardenUpdateEndpoint:
    def test_garden_update(self, client, User, Garden):
        """
        Ensure that the garden update endpoint
        updates the correct details
        """
        pass

    def test_garden_update_permissions(self, client, User, Garden):
        """
        Ensure that the garden update endpoint
        returns the correct error for inaccessible
        gardens
        """
        pass


class TestGardenInviteEndpoint:
    def test_garden_invite(self, client, User, Garden):
        """
        Ensure that a garden invite is
        successfully created
        """
        pass

    def test_garden_invite(self, client, User, Garden):
        """
        Ensure that a
        """


class TestGardenInviteAcceptEndpoint:
    pass


class TestGardenInviteRejectEndpoint:
    pass


class TestGardenMembershipDemoteEndpoint:
    pass


class TestGardenMembershipRevokeEndpoint:
    pass
