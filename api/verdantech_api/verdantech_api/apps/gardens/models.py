from django.conf import settings
from django.core.validators import validate_unicode_slug
from django.db import models
from django.utils.translation import gettext_lazy as _

from verdantech_api.apps.core.models import BaseModel
from verdantech_api.apps.core.utils import hashid_generator

User = settings.AUTH_USER_MODEL


class Garden(BaseModel):
    """
    Gardens are isolated containers for workspaces, plantsets,
    planting schemes, and other app functionality.
    Users can create gardens and join others, with admin, edit, and view roles.
    """

    name = models.CharField(
        _("name"), max_length=50, validators=[validate_unicode_slug]
    )
    hashid = models.CharField(max_length=6, null=True, blank=True, unique=True)
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

    def is_abandoned(self):
        """
        Check whether a garden is still in use
        """

        # Ensure the admin count is greater than zero
        if self.members.filter(role=GardenMembership.RoleChoices.ADMIN).count() > 0:
            return False
        else:
            return True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        # Generate a unique hash ID
        if not self.hashid:
            self.hashid = hashid_generator()
            while Garden.objects.filter(hashid=self.hashid).exists():
                self.hashid = hashid_generator()

        super(Garden, self).save(*args, **kwargs)


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
