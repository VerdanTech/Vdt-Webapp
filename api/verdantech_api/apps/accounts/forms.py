from allauth.account import app_settings
from allauth.account.adapter import get_adapter
from allauth.account.forms import default_token_generator
from allauth.account.utils import user_pk_to_url_str, user_username
from dj_rest_auth.forms import AllAuthPasswordResetForm as RestAuthPasswordResetForm
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site


class PasswordResetForm(RestAuthPasswordResetForm):
    def save(self, request, **kwargs):
        """Overriding the default dj-rest-auth form, in order to insert
        a password reset URL that points to the frontend
        """
        current_site = get_current_site(request)
        email = self.cleaned_data["email"]
        token_generator = kwargs.get("token_generator", default_token_generator)

        for user in self.users:

            temp_key = token_generator.make_token(user)

            # save it to the password reset model
            # password_reset = PasswordReset(user=user, temp_key=temp_key)
            # password_reset.save()

            # send the password reset email
            # path = reverse(
            # "password_reset_confirm",
            # args=[user_pk_to_url_str(user), temp_key],
            # )

            # if getattr(settings, "REST_AUTH_PW_RESET_USE_SITES_DOMAIN", False) is True:
            # url = build_absolute_uri(None, path)
            # else:
            # url = build_absolute_uri(request, path)

            # Override: set URL to our frontend's password reset route
            url = (
                settings.CLIENT_PASSWORD_RESET_URL
                + user_pk_to_url_str(user)
                + "/"
                + temp_key
            )

            context = {
                "current_site": current_site,
                "user": user,
                "password_reset_url": url,
                "request": request,
            }
            if (
                app_settings.AUTHENTICATION_METHOD
                != app_settings.AuthenticationMethod.EMAIL
            ):
                context["username"] = user_username(user)
            get_adapter(request).send_mail(
                "account/email/password_reset_key", email, context
            )
        return self.cleaned_data["email"]
