from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from timezone_field import TimeZoneField

from verdantech_api.apps.core.models import BaseModel

User = settings.AUTH_USER_MODEL


class Garden(BaseModel):
    """
    Gardens are isolated containers for workspaces, plantsets,
    planting schemes, and other app functionality.
    Users can create gardens and join others, with admin, edit, and view roles.
    """

    name = models.CharField(_("name"), max_length=50)
    string_id = models.CharField(
        _("unique sting identifier"), max_length=75, unique=True
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name=_("creator user"),
        null=True,
        blank=True,
        related_name=_("created_gardens"),
    )

    class VisibilityChoices(models.TextChoices):
        PRIVATE = "PRIVATE", _("Private")
        UNLISTED = "UNLISTED", _("Unlisted")
        PUBLIC = "PUBLIC", _("Public")

    visibility = models.CharField(
        _("visibility"),
        max_length=8,
        choices=VisibilityChoices.choices,
        default=VisibilityChoices.PRIVATE,
        help_text=_(
            "Public gardens are view accessible to anyone with a link "
            "and anyone who has been explicitly added "
            "and can appear elsewhere publicly on the app. "
            "Unlisted gardens are view accessible to anyone with a link "
            "and anyone who has been explicitly added "
            "but cannot appear elsewhere publicly on the site. "
            "Private gardens are view accessible only to anyone that is "
            "explicitly invited."
        ),
    )

    admins = models.ManyToManyField(
        User,
        related_name="admin_gardens",
        verbose_name=_("garden_admins"),
        help_text=_(
            "Admin users have the following permisions in a Garden: "
            "Garden settings update, "
            "Admin, editor, viewer list: create, update and delete, "
            "Workspaces create and delete, "
            "Devices create, update, and delete, "
            "ModelOutput control."
        ),
    )
    editors = models.ManyToManyField(
        User,
        related_name="edit_gardens",
        verbose_name=_("garden_editors"),
        help_text=_(
            "Editor users have the following permisions in a Garden: "
            "Garden viewers create, "
            "Planting scheme create, update, and delete, "
            "HarvestEntry create, update, and delete, "
            "ModelInputEntry create, update, and delete."
        ),
    )
    viewers = models.ManyToManyField(
        User,
        related_name="view_gardens",
        verbose_name=_("garden_viewers"),
        help_text=_("Viewer users have read-only permisions in a Garden"),
    )

    timezone = TimeZoneField(
        _("timezone"),
        null=True,
        blank=True,
    )

    # set_coordinates_from_address = models.BooleanField(_("set coordinates from address"), default=True)

    address = models.CharField(_("address"), max_length=100, null=True, blank=True)

    long = models.DecimalField(
        _("longitude coordinate"), max_digits=9, decimal_places=6, null=True, blank=True
    )
    lat = models.DecimalField(
        _("latitude coordinate"), max_digits=9, decimal_places=6, null=True, blank=True
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="admins_count_greaterthan_zero",
                check=models.Q(admins__isnull=False),
            ),
            models.UniqueConstraint(
                name="unique_garden_name_among_user_created_gardens",
                fields=["name", "creator"],
            ),
        ]

    def __str__(self):
        return self.name

    def clean(self):
        pass


class GardenInvite(models.Model):
    # user
    # garden
    # role
    pass
