# External Libraries
from attrs import field

# VerdanTech Source
from src.domain.common import Ref, RootEntity, root_entity_transform
from src.domain.environment import Environment
from src.domain.exceptions import FieldNotFound
from src.domain.user import User

from .enums import RoleEnum, VisibilityEnum
from .exceptions import MembershipAlreadyConfirmed
from .membership import GardenMembership


@root_entity_transform
class Garden(RootEntity):
    """
    Garden entity domain model.

    A Garden is the highest level container in the application.
    It groups together multiple Users via GardenMemberships,
    and serves as a one-to-many reference point for Workspaces, Plantsets,
    and most other application models.
    """

    key: str
    name: str
    creator_ref: Ref[User] | None
    visibility: VisibilityEnum = VisibilityEnum.PRIVATE
    environment_ref: Ref[Environment] | None = None
    memberships: set[GardenMembership] = field(factory=set)
    """There must exist only one GardenMembership for any given User."""
    description: str = ""
    expired: bool = False

    @property
    def num_memberships(self) -> int:
        """
        The number of memberships contained in the garden.

        Returns:
            int: the number of memberships.
        """
        return len(self.memberships)

    def get_membership(self, user: User) -> GardenMembership | None:
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
            if membership.user_ref.id == user.id:
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

        if self.creator_ref is not None and user.id == self.creator_ref.id:
            return True

        for membership in self.memberships:
            if user.id == membership.user_ref.id:
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

        if self.creator_ref is not None and user.id == self.creator_ref.id:
            return True

        for membership in self.memberships:
            if not membership.accepted:
                continue
            elif user.id == membership.user_ref.id:
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
        for membership in self.memberships:
            if membership.user_ref.id == user.id:
                if membership.accepted:
                    raise MembershipAlreadyConfirmed(
                        "The invite to this Garden has already been accepted."
                    )

                new_membership = membership.transform(accepted=True)
                self.memberships.remove(membership)
                self.memberships.add(new_membership)
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
        for membership in self.memberships:
            if membership.user_ref.id == user.id:
                self.memberships.remove(membership)
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
        for membership in self.memberships:
            if membership.user_ref.id == user.id:
                new_membership = membership.transform(role=new_role)
                self.memberships.remove(membership)
                self.memberships.add(new_membership)
        raise FieldNotFound("The User does not have a membership with this Garden.")
