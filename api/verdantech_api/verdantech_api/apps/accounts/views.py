from dj_rest_auth.registration.views import RegisterView as RestAuthRegisterView
from dj_rest_auth.views import (
    PasswordResetConfirmView as RestAuthPasswordResetConfirmView,
    PasswordResetView as RestAuthPasswordResetView,
)
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny


# Add CSRF protection to registration view
@method_decorator(csrf_protect, name="post")
class RegisterView(RestAuthRegisterView):

    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication]


# Add CSRF protection to password reset view
@method_decorator(csrf_protect, name="post")
class PasswordResetView(RestAuthPasswordResetView):

    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication]


# Add CSRF protection to password reset confirm view
@method_decorator(csrf_protect, name="post")
class PasswordResetConfirmView(RestAuthPasswordResetConfirmView):

    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication]
