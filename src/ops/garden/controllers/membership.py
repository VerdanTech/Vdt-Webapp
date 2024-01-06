# VerdanTech Source
from src.domain.garden.entities import Garden
from src.domain.garden.services import membership as membership_domain_services
from src.domain.garden.values import GardenMembership
from src.domain.user.entities import User
from src.interfaces.persistence.garden.repository import AbstractGardenRepository
from src.interfaces.persistence.user.repository import AbstractUserRepository

from ..schemas import membership as schemas
from ..services import membership as services


class GardenMembershipOpsController:
    def __init__(self, garden_repo: AbstractGardenRepository):
        self.garden_repo = garden_repo

    async def invite(
        self,
        client: User,
        data: schemas.GardenInviteCreateInput,
        user_repo: AbstractUserRepository,
    ) -> GardenMembership:
        # Retrieve invitee
        invitee = await user_repo.get_user_by_id(id=data.user_id)
        if invitee is None:
            raise Exception

        # Retrieve garden
        garden = await self.garden_repo.get_garden_by_id(id=data.garden_id)
        if garden is None:
            raise Exception

        membership = await services.invite(
            client=client,
            invitee_id=data.user_id,
            garden_id=data.garden_id,
            role=data.role,
            garden_repo=self.repo,
            user_repo=user_repo,
        )

        await self.garden_repo.update(garden)

        return membership

    async def accept_invite(self, client: User, data: schemas.GardenInviteAcceptInput):
        # Retrieve garden
        garden = await self.garden_repo.get_garden_by_id(id=data.garden_id)
        if garden is None:
            raise Exception

        membership = garden.confirm_membership(user=client)
        if membership is None:
            raise Exception

        await self.garden_repo.update(garden)

        return membership

    async def leave(self):
        pass

    async def set_role(self):
        pass
