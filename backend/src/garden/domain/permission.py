from .enums import OperationEnum, PermissionEnum, RoleEnum

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
    def revoke_membership(role: RoleEnum) -> OperationEnum:
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
