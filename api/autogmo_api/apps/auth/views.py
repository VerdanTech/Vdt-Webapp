from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from rest_framework.views import ApiView
from rest_auth.views import LoginView as RestAuthLogin
from rest_framework import rest_framework_permissions
from rest_framework.authentication import SessionAuthentication


@method_decorator(ensure_csrf_cookie, name='get')
class CSRFCookieView(APIView):
    """Obtain valid CSRF token
    """

    permission_classes = [AllowAny,]
    authentication_classes = []

    def get(self, request: Request) -> Response:
        return Response("CSRF Cookie set.")

@method_decorator(csrf_protect, name='post')
class LoginView(RestAuthLogin):
    """Login using Session authentication.
    """

    authentication_classes = [SessionAuthentication]
    permission_classes = [rest_framework_permissions.AllowAny]


