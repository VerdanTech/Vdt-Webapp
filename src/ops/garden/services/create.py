# VerdanTech Source
from src.domain.common import EntityIdType
from src.domain.garden.entities import Garden
from src.domain.garden.enums import RoleEnum, VisibilityEnum
from src.domain.garden.services import create as create_domain_services
from src.domain.user.entities import User
from src.interfaces.persistence.user.repository import AbstractUserRepository


async def garden_create(
    client: User,
    name: str,
    description: str,
    user_repo: AbstractUserRepository,
    garden_repo: AbstractGardenRepository,
    admin_ids: list[EntityIdType] = [],
    editor_ids: list[EntityIdType] = [],
    viewer_ids: list[EntityIdType] = [],
    visibility: VisibilityEnum = VisibilityEnum.PRIVATE,
) -> Garden:
    user_role_tuples = []
    invitee_ids = admin_ids + editor_ids + viewer_ids
    if invitee_ids is not []:
        invitees = await user_repo.get_users_by_id(
            ids=invitee_ids, raise_not_found=True
        )

        user_role_tuples = (
            [
                (invitee, RoleEnum.ADMIN)
                for invitee in invitees
                if invitee.id in admin_ids
            ]
            + [
                (invitee, RoleEnum.EDIT)
                for invitee in invitees
                if invitee.id in editor_ids
            ]
            + [
                (invitee, RoleEnum.VIEW)
                for invitee in invitees
                if invitee.id in viewer_ids
            ]
        )

    garden, user_invitation_tuples = create_domain_services.garden_create(
        client=client,
        name=name,
        description=description,
        user_role_tuples=user_role_tuples,
        visibility=visibility,
    )

    garden = await self.garden_repo.add(garden)

    for user_invitation_tuple in user_invitation_tuples:
        user = user_invitation_tuple(0)
        membership = user_invitation_tuple(1)
        await email_emitter.emit_garden_invite(
            email_address=user.primary_email.address,
            username=user.username,
            garden_key_id=garden.key_id,
            garden_name=garden.name,
            inviter_username=creator.username,
            role=str(membership.role),
        )

    return garden
