# External Libraries
from attrs import field

# VerdanTech Source
from src.common.domain import Ref, RootEntity, root_entity_transform
from src.domain.environment import Environment
from src.domain.exceptions import FieldNotFound
from src.user.domain import User

from .enums import RoleEnum, VisibilityEnum
from .exceptions import MembershipAlreadyConfirmed
from .membership import GardenMembership

# Standard Library
from datetime import datetime
from typing import TYPE_CHECKING

# External Libraries
from attrs import field

# VerdanTech Source
from src.common.domain import Ref, Value, value_transform
from src.user.domain import User

from .enums import OperationEnum, PermissionEnum, RoleEnum
from .exceptions import GardenAuthorizationException
from .permission import permission_rules


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

@value_transform
class GardenMembership(Value):
    """
    GardenMembership domain value.

    GardenMemberships connect Users and Gardens,
    allowing conditional access with different roles.
    """

    garden_ref: Ref["Garden"]
    """The garden the membership exists on."""
    user_ref: Ref[User]
    """The holder of the membership."""
    inviter_ref: Ref[User] | None
    """The user responsible for creating the membership."""
    role: RoleEnum = RoleEnum.VIEW
    """The persmissions of the membership."""
    accepted: bool = False
    """Whether the membership invitation has been accepted."""
    favorite: bool = False
    created_at: datetime = field(factory=datetime.now)

    def __hash__(self) -> int:
        """Used to make hashability transparent to type checkers."""
        return super().__hash__()

    def authorize(self, operation: OperationEnum) -> bool:
        """
        Compares self with an operation ID to asses the
        application of the permission rule associated with the operation.

        Args:
            operation (OperationEnum): operation to authorize.

        Returns:
            bool: true if the operation is authorized.
        """
        permission = permission_rules[operation]
        role = self.role
        return self._authorize(role=role, permission=permission)

    def assert_authorization(self, operation) -> None:
        """
        Compares self with an operation ID to asses the
        application of the permission rule associated with the operation.

        Args:
            operation (OperationEnum): operation to authorize.

        Raises:
            GardenAuthorizationException: raised if the authorization fails.
        """
        permission = permission_rules[operation]
        role = self.role
        if not self._authorize(role=self.role, permission=permission):
            raise GardenAuthorizationException(
                f"""
                The action: \"{operation}\" 
                requires the permission: \"{permission}\", 
                but this user has role: \"{role}\".
                """
            )

    def _authorize(self, role: RoleEnum, permission: PermissionEnum) -> bool:
        """
        Compares a GardenMembership's role with a permission requirement.

        Args:
            role (RoleEnum): role of the GardenMembership.
            permission (PermissionEnum): the permission level
                of the operation.

        Returns:
            bool: true if the role is authorized to peform the operation.
        """
        if permission is PermissionEnum.REQUIRES_ADMIN and role is RoleEnum.ADMIN:
            return True
        elif permission is PermissionEnum.REQUIRES_EDIT and (
            role is RoleEnum.ADMIN or role is RoleEnum.EDIT
        ):
            return True
        elif permission is PermissionEnum.REQUIRES_VIEW and (
            role is RoleEnum.ADMIN or role is RoleEnum.EDIT or role is RoleEnum.VIEW
        ):
            return True
        return False
