from dj_rest_auth import views as base_auth_views
from dj_rest_auth.registration import views as registration_auth_views
from django.urls import include, path

from . import views

urlpatterns = [
    path(
        "accounts/",
        include(
            [
                path(
                    r"password/reset",
                    views.PasswordResetView.as_view(),
                    name="password_reset",
                ),
                path(
                    r"password/reset/confirm",
                    views.PasswordResetConfirmView.as_view(),
                    name="password_reset_confirm",
                ),
                path(
                    r"password/change",
                    base_auth_views.PasswordChangeView.as_view(),
                    name="password_change",
                ),
                # Registration
                path(
                    r"registration",
                    views.RegisterView.as_view(),
                    name="registration",
                ),
                path(
                    r"registration/verify_email",
                    registration_auth_views.VerifyEmailView.as_view(),
                    name="verify_email",
                ),
                path(
                    r"registration/resend_email",
                    registration_auth_views.ResendEmailVerificationView.as_view(),
                    name="resend_email",
                ),
            ]
        ),
    )
]
