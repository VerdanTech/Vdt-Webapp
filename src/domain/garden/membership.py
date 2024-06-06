# Standard Library
from datetime import datetime
from typing import TYPE_CHECKING

# External Libraries
from attrs import field

# VerdanTech Source
from src.domain.common import Ref, Value, value_transform
from src.domain.user import User

from .enums import OperationEnum, PermissionEnum, RoleEnum
from .exceptions import GardenAuthorizationException
from .permission import permission_rules

if TYPE_CHECKING:
    from .garden import Garden


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
