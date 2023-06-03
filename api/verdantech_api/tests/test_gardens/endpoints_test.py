import pytest
from django.urls import reverse
from rest_framework import status

from verdantech_api.apps.gardens.models import GardenMembership

pytestmark = pytest.mark.django_db

garden_list_endpoint = reverse("garden_list")


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
                "name": gardens[2].name,
                "creator_username": user.username,
            },
            {"id": gardens[3].id, "name": gardens[3].name, "creator_username": ""},
        ]

        response = client.get(
            garden_list_endpoint,
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data == expected_response
