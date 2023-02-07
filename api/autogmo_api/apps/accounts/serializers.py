from dj_rest_auth.serializers import (
    PasswordResetSerializer as RestAuthPasswordResetSerializer,
)

from .forms import PasswordResetForm


class PasswordResetSerializer(RestAuthPasswordResetSerializer):
    @property
    def password_reset_form_class(self):
        """Overriding default dj-rest-auth form, in order to insert
        a password reset URL that points to the frontend
        """
        return PasswordResetForm
