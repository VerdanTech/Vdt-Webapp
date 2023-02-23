from dj_rest_auth.registration.views import RegisterView as RestAuthRegisterView
from dj_rest_auth.views import (
    LoginView as RestAuthLogin,
    PasswordResetConfirmView as RestAuthPasswordResetConfirmView,
    PasswordResetView as RestAuthPasswordResetView,
)
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from drf_spectacular.utils import extend_schema
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response


@method_decorator(ensure_csrf_cookie, name="get")
class CSRFTokenView(GenericAPIView):
    """Sets response cookie: "csrftoken" to a valid CSRF token"""

    permission_classes = [AllowAny]
    authentication_classes = []

    @extend_schema(responses=None)
    def get(self, request: Request) -> Response:
        return Response("CSRF Cookie set.")


@method_decorator(csrf_protect, name="post")
class LoginView(RestAuthLogin):
    """Login using Session authentication.
    Requires CSRF token to prevent login-csrf,
    see: https://docs.djangoproject.com/en/4.1/ref/csrf/
    """

    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication]


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
