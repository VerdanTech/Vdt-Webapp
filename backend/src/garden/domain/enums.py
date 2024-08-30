# Standard Library
from enum import Enum


class GardenVisibilityEnum(Enum):
    """
    Visibility controls the ability of a Garden
    to be read-accessed by those who are not members.
    """

    PRIVATE = "private"
    """Only Users with memberships of role VIEW have read-access."""
    UNLISTED = "unlisted"
    """Anyone with a link has read-access, but the link is not publicly listed."""
    PUBLIC = "public"
    """Anyone with a link has read-access, and the Garden may be publicly searchable."""


class RoleEnum(Enum):
    ADMIN = "admin"
    EDIT = "editor"
    VIEW = "viewer"


class PermissionEnum(Enum):
    NOT_ALLOWED = "not allowed"
    """The operation is not allowed by anyone."""
    REQUIRES_ADMIN = "admin permissions"
    """The operation requires the ADMIN role."""
    REQUIRES_EDIT = "editor permissions"
    """The operation requires the EDIT role."""
    REQUIRES_VIEW = "viewer permissions"
    """The operation requires the VIEW role."""


class OperationEnum(Enum):
    """
    Defines operation IDs for attachment to PermissionEnum
    to define custom permission rules.
    """

    # New invite.
    INVITE_ADMIN = "invite an admin"
    """Create a new GardenMembership with the ADMIN role."""
    INVITE_EDIT = "invite an editor"
    """Create a new GardenMembership with the EDIT role."""
    INVITE_VIEW = "inviter a viewer"
    """Create a new GardenMembership with the VIEW role."""

    # Change role.
    ADMIN_TO_EDIT = "change the role of an admin to an editor"
    """Change the role on a GardenMembership from ADMIN to EDIT."""
    ADMIN_TO_VIEW = "change the role of an admin to a viewer"
    """Change the role on a GardenMembership from ADMIN to VIEW."""
    EDIT_TO_ADMIN = "change the role of an editor to an admin"
    """Change the role on a GardenMembership from EDIT to ADMIN."""
    EDIT_TO_VIEW = "change the role of an editor to a viewer"
    """Change the role on a GardenMembership from EDIT to VIEW."""
    VIEW_TO_ADMIN = "change the role of an viewer to an admin"
    """Change the role on a GardenMembership from VIEW to ADMIN."""
    VIEW_TO_EDIT = "change the role of an viewer to an editor"
    """Change the role on a GardenMembership from VIEW to EDIT."""
    KICK_ADMIN = "remove an admin from a garden"
    """Delete a GardenMembership with role ADMIN."""
    KICK_EDIT = "remove an editor from a garden"
    """Delete a GardenMembership with role EDIT."""
    KICK_VIEW = "remove a viewer from a garden"
    """Delete a GardenMembership with role VIEW."""
