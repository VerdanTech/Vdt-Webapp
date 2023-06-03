import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db

csrf_token_endpoint = reverse("csrf_token")
login_endpoint = reverse("login")


class TestCSRFTokenEndpoint:
    def test_csrf(self, client):
        """Ensure that a CSRF token is correctly issued at the endpoint"""

        response = client.get(
            csrf_token_endpoint,
            format="json",
        )

        assert response.status_code == status.HTTP_200_OK
        assert "csrftoken" in response.data


class TestLoginEndpoint:
    def test_login_without_csrf(self, csrf_client, mocker):
        """Ensure the login view is CSRF protected"""

        User = get_user_model()
        plaintext_password = "cgbff8o9mXwYbN"
        user = User.objects.create_user(
            email="test@example.com",
            username="test",
            password=plaintext_password,
        )

        response = csrf_client.post(
            login_endpoint,
            data={"email": user.email, "password": plaintext_password},
            format="json",
        )

        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert "CSRF verification failed" in response.content.decode()

    def test_login_with_csrf(self, csrf_client):
        """Ensure the login view is suceeds with email, password, and csrf token"""

        User = get_user_model()
        plaintext_password = "cgbff8o9mXwYbN"
        user = User.objects.create_user(
            email="test@example.com",
            username="test",
            password=plaintext_password,
        )

        csrf_client.get(
            csrf_token_endpoint,
            format="json",
        )

        response = csrf_client.post(
            login_endpoint,
            data={"email": user.email, "password": plaintext_password},
            format="json",
            HTTP_X_CSRFTOKEN=csrf_client.cookies["csrftoken"].value,
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert "sessionid" in response.cookies
