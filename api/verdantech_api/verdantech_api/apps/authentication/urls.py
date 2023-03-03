from dj_rest_auth import views as base_auth_views
from django.urls import include, path

from . import views

urlpatterns = [
    path(
        "auth/",
        include(
            [
                path(r"csrf", views.CSRFTokenView.as_view(), name="csrf_token"),
                path(r"login", views.LoginView.as_view(), name="login"),
                path(r"logout", base_auth_views.LogoutView.as_view(), name="logout"),
            ]
        ),
    )
]
