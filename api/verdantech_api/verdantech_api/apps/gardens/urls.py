from django.urls import include, path

from . import views

urlpatterns = [
    path(
        "gardens/",
        include(
            [
                path(r"", views.GardenListView.as_view(), name="garden_list"),
                path(
                    r"invites",
                    views.GardenMembershipInviteListView.as_view(),
                    name="garden_membership_invite_list",
                ),
                path(
                    r"invites/<int:id>/accept",
                    views.GardenMembershipInviteAcceptView.as_view(),
                    name="garden_membership_invite_accept",
                ),
                path(r"create", views.GardenCreateView.as_view(), name="garden_create"),
                path(
                    r"<str:hashid>",
                    views.GardenDetailView.as_view(),
                    name="garden_detail",
                ),
                path(
                    r"<str:hashid>/update",
                    views.GardenUpdateView.as_view(),
                    name="garden_update",
                ),
                path(
                    r"<str:hashid>/members/create",
                    views.GardenMembershipInviteCreateView.as_view(),
                    name="garden_membership_invite_create",
                ),
                path(
                    r"<str:hashid>/members/update",
                    views.GardenMembershipUpdateView.as_view(),
                    name="garden_membership_update",
                ),
                path(
                    r"<str:hashid>/members/delete",
                    views.GardenMembershipDeleteView.as_view(),
                    name="garden_membership_delete",
                ),
            ]
        ),
    )
]
