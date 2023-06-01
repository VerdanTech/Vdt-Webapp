from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

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

    users = models.ManyToManyField(
        User,
        related_name="user_gardens",
        verbose_name=_("garden users"),
        through="GardenMembership",
        through_fields=("garden", "user"),
    )

    address = models.CharField(_("address"), max_length=100, null=True, blank=True)

    long = models.DecimalField(
        _("longitude coordinate"), max_digits=9, decimal_places=6, null=True, blank=True
    )
    lat = models.DecimalField(
        _("latitude coordinate"), max_digits=9, decimal_places=6, null=True, blank=True
    )

    def __str__(self):
        return self.string_id

    def clean(self):

        # Ensure the admin count is greater than zero
        if not (self.members.filter(role="ADMIN").count() > 0):
            raise ValidationError("Requires minimum 1 admin")

        pass


class GardenMembership(BaseModel):
    """
    Garden memberships tie user models to roles, allowing
    users to be invited to gardens
    """

    inviter = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="inviter",
        null=True,
        blank=True,
        related_name="invitations_sent",
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="user", related_name="memberships"
    )
    garden = models.ForeignKey(
        Garden, on_delete=models.CASCADE, verbose_name="garden", related_name="members"
    )

    class RoleChoices(models.TextChoices):
        ADMIN = "ADMIN", _("Admin")
        EDIT = "EDIT", _("Editor")
        VIEW = "VIEW", _("Viewer")

    role = models.CharField(
        _("role"),
        max_length=6,
        choices=RoleChoices.choices,
        default=RoleChoices.VIEW,
    )

    open_invite = models.BooleanField(_("open invite"), default=True)

    class Meta:

        constraints = [
            models.UniqueConstraint(
                fields=["user", "garden"], name="user_unique_in_garden"
            )
        ]
