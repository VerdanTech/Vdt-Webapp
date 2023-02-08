from dj_rest_auth.registration.views import (
    RegisterView as RestAuthRegisterView,
    SocialLoginView,
)
from dj_rest_auth.views import (
    LoginView as RestAuthLogin,
    PasswordResetConfirmView as RestAuthPasswordResetConfirmView,
    PasswordResetView as RestAuthPasswordResetView,
)
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


@method_decorator(ensure_csrf_cookie, name="get")
class CSRFTokenView(APIView):
    """Obtain valid CSRF token"""

    permission_classes = [AllowAny]
    authentication_classes = []

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


@method_decorator(csrf_protect, name="post")
class RegisterView(RestAuthRegisterView):
    """Add CSRF protection to registration view"""

    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication]


@method_decorator(csrf_protect, name="post")
class PasswordResetView(RestAuthPasswordResetView):
    """Add CSRF protection to password reset view"""

    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication]


@method_decorator(csrf_protect, name="post")
class PasswordResetConfirmView(RestAuthPasswordResetConfirmView):
    """Add CSRF protection to password reset confirm view"""

    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication]
