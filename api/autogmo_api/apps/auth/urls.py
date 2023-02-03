from django.urls import include, path

from . import views

urlpatterns = [
    path(
        "auth/",
        include(
            [
                path("login/", views.LoginView.as_view(), name="login"),
            ]
        ),
    )
]
