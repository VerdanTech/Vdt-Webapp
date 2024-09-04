# Standard Library
import uuid
from typing import TYPE_CHECKING

# VerdanTech Source
from src.common.domain import Event, Ref, event_transform
from src.user.domain import User

if TYPE_CHECKING:
    from .models import Garden, GardenInvite, RoleEnum


@event_transform
class PendingInvites(Event):
    """
    Emitted when garden membership invitiations are pending.

    These memberships may not have been validated for existence
    of garden membership of the inviter, or existence of users.
    """

    garden_ref: Ref["Garden"]
    client_ref: Ref[User]
    admin_usernames: list[str] = []
    editor_usernames: list[str] = []
    viewer_usernames: list[str] = []


@event_transform
class InvitesCreated(Event):
    """
    Emitted when garden membership invitations are created.
    """

    inviter_username: str
    garden_name: str
    garden_key: str
    invites: list["GardenInvite"]


@event_transform
class MembershipAccepted(Event):
    """
    Emitted when a new member joins a garden.
    """

    garden_ref: Ref["Garden"]
    user_ref: Ref[User]
    role: "RoleEnum"


@event_transform
class MembershipRevoked(Event):
    """
    Emitted when a member is removed from a garden.
    """

    garden_ref: Ref["Garden"]
    user_ref: Ref[User]
