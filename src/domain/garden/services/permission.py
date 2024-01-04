# VerdanTech Source
from src.domain.garden.entities import GardenMembership

from ..enums import ActionEnum, PermissionEnum, RoleEnum
from ..exceptions import GardenAuthorizationException

permission_rules: dict[ActionEnum, PermissionEnum] = {
    ActionEnum.INVITE_ADMIN: PermissionEnum.REQUIRES_ADMIN,
    ActionEnum.INVITE_EDIT: PermissionEnum.REQUIRES_ADMIN,
    ActionEnum.INVITE_VIEW: PermissionEnum.REQUIRES_ADMIN,
}


def _authorize(role: RoleEnum, permission: PermissionEnum) -> bool:
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


def authorize(membership: GardenMembership, action: ActionEnum):
    permission = permission_rules[action]
    role = membership.role
    return _authorize(role=role, permission=permission)


def assert_authorization(membership: GardenMembership, action):
    permission = permission_rules[action]
    role = membership.role
    if not _authorize(role=membership.role, permission=permission):
        raise GardenAuthorizationException(
            f"The action {action} requires the permission {permission}, but this user has role {role}"
        )
