# VerdanTech Source
from src.domain.garden.sanitizers import GardenSanitizer
from src.domain.user.entities import User
from src.interfaces.email.emitter import AbstractEmailEmitter
from src.interfaces.persistence.garden.repository import AbstractGardenRepository
from src.interfaces.persistence.user.repository import AbstractUserRepository

from ..schemas import write as schemas
from ..services import create as create_services


class GardenWriteOpsController:
    def __init__(self, garden_repo: AbstractGardenRepository):
        self.garden_repo = garden_repo

    async def create(
        self,
        client: User,
        data: schemas.GardenCreateInput,
        user_repo: AbstractUserRepository,
        garden_sanitizer: GardenSanitizer,
        email_emitter: AbstractEmailEmitter,
    ):
        # Sanitize input data
        await data.sanitize(garden_sanitizer=garden_sanitizer)

        return await create_services.garden_create(
            creator=client,
            name=data.name,
            description=data.description,
            admin_ids=data.admin_ids,
            editor_ids=data.editor_ids,
            viewer_ids=data.viewer_ids,
            visibility=data.visibility,
        )

    async def change(self):
        pass
