# VerdanTech Source
from src.domain.garden.services import membership as membership_domain_services
from src.interfaces.persistence.garden.repository import AbstractGardenRepository
from src.interfaces.persistence.user.repository import AbstractUserRepository


async def invite(
    client: User,
    invitee_id: EntityIdType,
    garden_id: EntityIdType,
    role: RoleEnum,
    garden_repo: AbstractGardenRepository,
    user_repo: AbstractUserRepository,
):
    # Retrieve invitee
    invitee = await user_repo.get_user_by_id(id=data.user_id)
    if invitee is None:
        raise Exception

    # Retrieve garden
    garden = await self.garden_repo.get_garden_by_id(id=data.garden_id)
    if garden is None:
        raise Exception

    membership = membership_domain_services.create_garden_membership(
        client=client, invitee=invitee, garden=garden, role=data.role
    )

    await email_emitter.emit_garden_invite(
        email_address=invitee.primary_email.address,
        username=invitee.username,
        garden_key_id=garden.key_id,
        garden_name=garden.name,
        inviter_username=inviter.username,
        role=str(membership.role),
    )

    await self.garden_repo.update(garden)
