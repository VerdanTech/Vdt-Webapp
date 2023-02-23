from dj_rest_auth.serializers import (
    LoginSerializer as RestAuthLoginSerializer,
    PasswordResetSerializer as RestAuthPasswordResetSerializer,
)
from rest_framework import serializers

from .forms import PasswordResetForm


# Overriding default dj-rest-auth behavior, in order
# to not consider username and require email
class LoginSerializer(RestAuthLoginSerializer):

    username = None
    email = serializers.EmailField(required=True)


class PasswordResetSerializer(RestAuthPasswordResetSerializer):
    @property
    def password_reset_form_class(self):
        """Overriding default dj-rest-auth form, in order to insert
        a password reset URL that points to the frontend
        """
        return PasswordResetForm
