# VerdanTech Source
from src.domain.garden.services import create as create_domain_services
from src.interfaces.persistence.user.repository import AbstractUserRepository
from src.domain.garden.enums import RoleEnum
from ..schemas import write as schemas


class GardenWriteOpsController:
    def __init__(self, garden_repo: AbstractGardenRepository):
        pass

    async def create(
        self,
        client: User,
        data: schemas.GardenCreateInput,
        user_repo: AbstractUserRepository,
        garden_sanitizer: GardenSanitizer,
    ):
        # Sanitize input data
        await data.sanitize(garden_sanitizer=garden_sanitizer)

        # Fetch invitees
        admin_ids = data.admin_ids or []
        editor_ids = data.editor_ids or []
        viewer_ids = data.viewer_ids or [] 
        invitee_ids = [admin_ids + editor_ids + viewer_ids]
        invitees = await user_repo.get_users_by_id(ids=invitee_ids, raise_not_found=True)
        admin_invitations = [(invitee, RoleEnum.ADMIN) for invitee in invitees if invitee.id in admin_ids]
        edit_invitations = [(invitee, RoleEnum.EDIT) for invitee in invitees if invitee.id in editor_ids]
        view_invitations = [(invitee, RoleEnum.VIEW) for invitee in invitees if invitee.id in viewer_ids]
        invitations = admin_invitations + edit_invitations + view_invitations


        garden = create_domain_services.create_garden(
            creator=client,
            name=data.name,
            description=data.description,
            invitations=invitations,
            visibility=data.visibility,
        )

        garden = await self.garden_repo.add(garden)

        return garden

    async def change(self):
        pass
