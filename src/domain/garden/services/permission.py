# VerdanTech Source
from src.domain.garden.entities import GardenMembership

from ..enums import OperationEnum, PermissionEnum, RoleEnum
from ..exceptions import GardenAuthorizationException

permission_rules: dict[OperationEnum, PermissionEnum] = {
    OperationEnum.INVITE_ADMIN: PermissionEnum.REQUIRES_ADMIN,
    OperationEnum.INVITE_EDIT: PermissionEnum.REQUIRES_ADMIN,
    OperationEnum.INVITE_VIEW: PermissionEnum.REQUIRES_ADMIN,
    OperationEnum.ADMIN_TO_EDIT: PermissionEnum.REQUIRES_ADMIN,
    OperationEnum.ADMIN_TO_VIEW: PermissionEnum.REQUIRES_ADMIN,
    OperationEnum.EDIT_TO_ADMIN: PermissionEnum.REQUIRES_ADMIN,
    OperationEnum.EDIT_TO_VIEW: PermissionEnum.REQUIRES_ADMIN,
    OperationEnum.VIEW_TO_ADMIN: PermissionEnum.REQUIRES_ADMIN,
    OperationEnum.VIEW_TO_EDIT: PermissionEnum.REQUIRES_ADMIN,
    OperationEnum.KICK_ADMIN: PermissionEnum.REQUIRES_ADMIN,
    OperationEnum.KICK_EDIT: PermissionEnum.REQUIRES_ADMIN,
    OperationEnum.KICK_VIEW: PermissionEnum.REQUIRES_ADMIN,
}
"""
Match Operation IDs with PermissionEnums.
"""


def authorize(membership: GardenMembership, operation: OperationEnum) -> bool:
    """
    Compares a GardenMembership with an operation ID to asses the
    application of the permission rule associated with the operation.

    Args:
        membership (GardenMembership): membership to attempt authorization with.
        operation (OperationEnum): operation to authorize.

    Returns:
        bool: true if the operation is authorized.
    """
    permission = permission_rules[operation]
    role = membership.role
    return _authorize(role=role, permission=permission)


def assert_authorization(membership: GardenMembership, operation) -> None:
    """
    Compares a GardenMembership with an operation ID to asses the
    application of the permission rule associated with the operation.

    Args:
        membership (GardenMembership): membership to attempt authorization with.
        operation (OperationEnum): operation to authorize.

    Raises:
        GardenAuthorizationException: raised if the authorization fails.
    """
    permission = permission_rules[operation]
    role = membership.role
    if not _authorize(role=membership.role, permission=permission):
        raise GardenAuthorizationException(
            f"""
            The action \"{operation}\" 
            requires the permission \"{permission}\", 
            but this user has role \"{role}\".
            """
        )


def _authorize(role: RoleEnum, permission: PermissionEnum) -> bool:
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


class PermissionRouter:
    @staticmethod
    def invite(role: RoleEnum) -> OperationEnum:
        """
        Maps a role to an operation ID in the context
        of a new GardenMembership invite operation.

        Args:
            new_role (RoleEnum): the role of the invitation.

        Returns:
            OperationEnum: the operation ID.
        """
        match role:
            case RoleEnum.ADMIN:
                return OperationEnum.INVITE_ADMIN
            case RoleEnum.EDIT:
                return OperationEnum.INVITE_EDIT
            case RoleEnum.VIEW:
                return OperationEnum.INVITE_VIEW
            case _:
                raise ValueError(
                    "Unhandled RoleEnum in invite() permission router domain service."
                )

    @staticmethod
    def change_role(client_role: RoleEnum, new_role: RoleEnum) -> OperationEnum:
        """
        Maps a client's role and a subject's new role to an
        operation ID in the context of the client setting
        the subject's role to new_role.

        Args:
            client_role (RoleEnum): the role of the client
                performing the operation.
            new_role (RoleEnum): the new role being set
                on the subject.

        Returns:
            OperationEnum: the operation ID.
        """
        match client_role:
            case RoleEnum.ADMIN:
                match new_role:
                    case RoleEnum.ADMIN:
                        raise Exception
                    case RoleEnum.EDIT:
                        return OperationEnum.ADMIN_TO_EDIT
                    case RoleEnum.VIEW:
                        return OperationEnum.ADMIN_TO_VIEW
                    case _:
                        raise ValueError(
                            "Unhandled RoleEnum in change_role() permission router domain service."
                        )

            case RoleEnum.EDIT:
                match new_role:
                    case RoleEnum.ADMIN:
                        return OperationEnum.EDIT_TO_ADMIN
                    case RoleEnum.EDIT:
                        raise Exception
                    case RoleEnum.VIEW:
                        return OperationEnum.EDIT_TO_VIEW
                    case _:
                        raise ValueError(
                            "Unhandled RoleEnum in change_role() permission router domain service."
                        )

            case RoleEnum.VIEW:
                match new_role:
                    case RoleEnum.ADMIN:
                        return OperationEnum.VIEW_TO_ADMIN
                    case RoleEnum.EDIT:
                        return OperationEnum.VIEW_TO_EDIT
                    case RoleEnum.VIEW:
                        raise Exception
                    case _:
                        raise ValueError(
                            "Unhandled RoleEnum in change_role() permission router domain service."
                        )

            case _:
                raise ValueError(
                    "Unhandled RoleEnum in change_role() permission router domain service."
                )

    @staticmethod
    def kick(role: RoleEnum) -> OperationEnum:
        """
        Maps a subject's role to an operation ID in the
        context of the subject being removed from a Garden.

        Args:
            role (RoleEnum): the role of the user being removed.

        Returns:
            OperationEnum: the operation ID.
        """
        match role:
            case RoleEnum.ADMIN:
                return OperationEnum.KICK_ADMIN
            case RoleEnum.EDIT:
                return OperationEnum.KICK_EDIT
            case RoleEnum.VIEW:
                return OperationEnum.KICK_VIEW
            case _:
                raise ValueError(
                    "Unhandled RoleEnum in kick() permission router domain service."
                )
