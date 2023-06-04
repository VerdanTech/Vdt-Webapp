from django.urls import include, path

from . import views

urlpatterns = [
    path(
        "garden/",
        include(
            [
                path(r"", views.GardenListView.as_view(), name="garden_list"),
                path(r"create", views.GardenCreateView.as_view(), name="garden_create"),
            ]
        ),
    )
]
