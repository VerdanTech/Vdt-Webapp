from src.interfaces.persistence.user.repository import AbstractUserRepository
from ..schemas import membership as schemas
from src.domain.garden.services import membership as membership_domain_services
class GardenMembershipOpsController:
    def __init__(self):
        pass

    async def invite(self, client: User, data: schemas.GardenInviteCreateInput, user_repo: AbstractUserRepository):
        
        # Retrieve invitee
        invitee = await user_repo.get_user_by_id(id=data.user_id)
        if invitee is None:
            raise Exception

        # Retrieve garden
        garden = await self.garden_repo.get_garden_by_id(id=data.garden_id)
        if garden is None:
            raise Exception
        
        membership = membership_domain_services.create_garden_membership(client=client, invitee=invitee, garden=garden, role=data.role)

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
