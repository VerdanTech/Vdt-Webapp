from drf_spectacular.extensions import OpenApiViewExtension
from drf_spectacular.utils import extend_schema

# DRF Spectacular Extensions


class FixLogoutView(OpenApiViewExtension):
    """Patch schema of dj_rest_auth's LogoutView"""

    target_class = "dj_rest_auth.views.LogoutView"

    def view_replacement(self):
        class FixedView(self.target_class):
            serializer_class = None

            @extend_schema(exclude=True)
            def get(self):
                return None

            @extend_schema(
                description="Calls Django logout methods and "
                "deletes the sessionid assigned to the user object"
            )
            def post(self):
                return self.super()

        return FixedView
