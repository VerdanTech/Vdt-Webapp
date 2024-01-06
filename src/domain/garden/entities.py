# Standard Library
from dataclasses import field, replace
from typing import Optional

# VerdanTech Source
from src import settings
from src.domain.common import Ref, RootEntity, root_entity_dataclass
from src.domain.exceptions import FieldNotFound
from src.domain.user.entities import User
from src.utils.key_generator import key_generator

from .enums import RoleEnum, VisibilityEnum
from .exceptions import MembershipAlreadyConfirmed
from .values import EnvironmentAttributeProfile, GardenMembership


@root_entity_dataclass
class Garden(RootEntity):
    """
    Garden entity domain model.

    A Garden is the highest level container in the application.
    It groups together multiple Users via GardenMemberships,
    and serves as a one-to-many reference point for Workspaces, Plantsets,
    and most other application models.
    """

    name: str
    creator: Ref[User] | None
    key_id: str = field(
        default_factory=lambda: key_generator(length=settings.GARDEN_STR_ID_LENGTH)
    )
    memberships: list[GardenMembership] = field(default_factory=list)
    """There must exist only one GardenMembership for any given User."""
    description: str | None = None
    visibility: VisibilityEnum = VisibilityEnum.PRIVATE
    attributes: list[EnvironmentAttributeProfile] = field(default_factory=list)
    expired: bool = False

    def get_membership(self, user: User) -> Optional[GardenMembership]:
        """
        Returns the GardenMembership belonging to a User,
        or None if no membership exists.

        Args:
            user (User): the member to return the membership for.

        Returns:
            Optional[GardenMembership]: the membership, or None if
                no membership exists.
        """
        if not user.persisted:
            return None

        for membership in self.memberships:
            if membership.user.id == user.id:
                return membership

        return None

    def is_user_member(self, user: User) -> bool:
        """
        Checks if there exists a GardenMembership belonging
        to a User. This includes pending membership invites.

        Args:
            user (User): the member to check the existence
                of a membership for.

        Returns:
            bool: True if a membership does exist containing
                the User, False otherwise.
        """
        if not user.persisted:
            return False

        if self.creator is not None and user.id == self.creator.id:
            return True

        if user.id in [membership.user.id for membership in self.memberships]:
            return True

        return False

    def is_user_confirmed_member(self, user: User) -> bool:
        """
        Checks if there exists a GardenMembership belonging
        to a User, only including confirmed memberships with
        no open invitations.

        Args:
            user (User): the member to check the existence
                of a confirmed membership for.

        Returns:
            bool: True if a confirmed membership does exist
                containing the User, False otherwise.
        """
        if not user.persisted:
            return False

        if self.creator is not None and user.id == self.creator.id:
            return True

        if user.id in [
            membership.user.id
            for membership in self.memberships
            if not membership.open_invite
        ]:
            return True

        return False

    def confirm_membership(self, user: User) -> GardenMembership:
        """
        Closes a membership invitation given the User it belongs to.

        Args:
            user (User): the User with the GardenMembership invite
                to accept.

        Raises:
            MembershipAlreadyConfirmed: raised if the User does have
                an existing GardenMembership, but the invite has
                already been confirmed.
            FieldNotFound: raised if the User does not have an
                existing GardenMembership.

        Returns:
            GardenMembership: the GardenMembership after confirmation.
        """
        for idx, membership in enumerate(self.memberships):
            if membership.user.id == user.id:
                if membership.open_invite is False:
                    raise MembershipAlreadyConfirmed(
                        "The invite to this Garden has already been accepted."
                    )

                self.memberships[idx] = replace(membership, open_invite=False)
                return membership

        raise FieldNotFound("The User does not have an invitation to this Garden.")

    def remove_membership(self, user: User) -> None:
        """
        Removes a membership given the User is belongs to.

        Args:
            user (User): the User with the GardenMembership invite
                to remove.

        Raises:
            FieldNotFound: raised if the User does not have an
                existing GardenMembership.
        """
        for idx, membership in enumerate(self.memberships):
            if membership.user.id == user.id:
                self.memberships.pop(idx)
        raise FieldNotFound("The User does not have a membership with this Garden.")

    def change_role(self, user: User, new_role: RoleEnum) -> GardenMembership:
        """
        Changes the role of a membership given the User is belongs to.

        Args:
            user (User): the User with the GardenMembership invite
                to change the role of.

        Raises:
            FieldNotFound: raised if the User does not have an
                existing GardenMembership.
        """
        for idx, membership in enumerate(self.memberships):
            if membership.user.id == user.id:
                new_membership = replace(membership, role=new_role)
                self.memberships[idx] = new_membership
                return new_membership
        raise FieldNotFound("The User does not have a membership with this Garden.")
