from __future__ import annotations

import re
from typing import TYPE_CHECKING

import pytest
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core import mail
from django.urls import reverse
from rest_framework import status

if TYPE_CHECKING:
    from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db

login_endpoint = reverse("login")
csrf_token_endpoint = reverse("csrf_token")
registration_endpoint = reverse("registration")
verify_email_endpoint = reverse("verify_email")
resend_email_endpoint = reverse("resend_email")
password_reset_endpoint = reverse("password_reset")
password_reset_confirm_endpoint = reverse("password_reset_confirm")


class TestRegistrationEndpoints:
    def test_registration_and_email_confirmation_without_csrf(self, csrf_client):
        """Ensure the registration view requires a CSRF token"""

        username = "testusername"
        email = "test@test.com"
        password = "testtest11"

        data = {
            "username": username,
            "email": email,
            "password1": password,
            "password2": password,
        }

        response = csrf_client.post(registration_endpoint, data=data, format="json")

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_registration_and_email_confirmation(self, csrf_client):
        """Ensure the registration process is working correctly"""

        User = get_user_model()
        username = "testusername"
        email = "test@test.com"
        password = "testtest11"

        data = {
            "username": username,
            "email": email,
            "password1": password,
            "password2": password,
        }

        csrf_client.get(
            csrf_token_endpoint,
            format="json",
        )

        response = csrf_client.post(
            registration_endpoint,
            data=data,
            format="json",
            HTTP_X_CSRFTOKEN=csrf_client.cookies["csrftoken"].value,
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert User.objects.all().count() == 1
        assert len(mail.outbox) == 1

        csrf_client.post(
            resend_email_endpoint,
            data={"email": email},
            format="json",
            HTTP_X_CSRFTOKEN=csrf_client.cookies["csrftoken"].value,
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert len(mail.outbox) == 2

        # Obtain key from email message body
        message = mail.outbox[1].body
        key = re.search(r"%s(.*)" % (settings.CLIENT_EMAIL_VERIFY_URL), message).group(
            1
        )

        response = csrf_client.post(
            verify_email_endpoint,
            data={"key": key},
            format="json",
            HTTP_X_CSRFTOKEN=csrf_client.cookies["csrftoken"].value,
        )

        assert response.status_code == status.HTTP_200_OK


class TestPasswordEndpoints:
    def test_password_reset_without_csrf(self, csrf_client):
        """Ensure the password reset view requires a CSRF token"""

        email = "test@test.com"

        response = csrf_client.post(
            password_reset_endpoint, data={"email": email}, format="json"
        )

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_password_reset(self, csrf_client):
        """Ensure the password reset process is working correctly"""

        User = get_user_model()
        user = User.objects.create_user(
            email="test@example.com",
            username="test",
            password="cgbff8o9mXwYbN",
        )
        new_password = "otsftNTeraXwYrstN"

        csrf_client.get(
            csrf_token_endpoint,
            format="json",
        )

        response = csrf_client.post(
            password_reset_endpoint,
            data={"email": user.email},
            format="json",
            HTTP_X_CSRFTOKEN=csrf_client.cookies["csrftoken"].value,
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(mail.outbox) == 1

        # Obtain user id from email message body
        message = mail.outbox[0].body
        user_id = re.search(
            r"%s(.*)/" % (settings.CLIENT_PASSWORD_RESET_URL), message
        ).group(1)
        # Obtain key from email message body
        token = re.search(
            r"%s(.*)" % (settings.CLIENT_PASSWORD_RESET_URL + f"{user_id}/"), message
        ).group(1)

        data = {
            "uid": user_id,
            "token": token,
            "new_password1": new_password,
            "new_password2": new_password,
        }

        response = csrf_client.post(
            password_reset_confirm_endpoint,
            data=data,
            format="json",
            HTTP_X_CSRFTOKEN=csrf_client.cookies["csrftoken"].value,
        )

        assert response.status_code == status.HTTP_200_OK

        response = csrf_client.post(
            login_endpoint,
            data={"email": user.email, "password": new_password},
            format="json",
            HTTP_X_CSRFTOKEN=csrf_client.cookies["csrftoken"].value,
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert "sessionid" in response.cookies
