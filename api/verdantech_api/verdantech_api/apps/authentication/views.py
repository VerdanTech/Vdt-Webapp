from dj_rest_auth.views import LoginView as RestAuthLogin
from django.middleware.csrf import get_token
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from drf_spectacular.utils import extend_schema
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import CSRFTokenSerializer


class CSRFTokenView(GenericAPIView):
    """Returns valid CSRF token"""

    permission_classes = [AllowAny]
    authentication_classes = []

    @extend_schema(responses=CSRFTokenSerializer)
    def get(self, request: Request) -> Response:

        serializer = CSRFTokenSerializer(data={"csrftoken": get_token(request)})

        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response({"error": "Could not create csrftoken"})


@method_decorator(csrf_protect, name="post")
class LoginView(RestAuthLogin):
    """Login using Session authentication.
    Requires CSRF token to prevent login-csrf,
    see: https://docs.djangoproject.com/en/4.1/ref/csrf/
    """

    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication]
