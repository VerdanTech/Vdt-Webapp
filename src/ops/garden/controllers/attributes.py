# VerdanTech Source
from src import settings
from src.domain.garden.enums import RoleEnum
from src.domain.garden.garden import Garden
from src.domain.garden.sanitizers import GardenSanitizer
from src.domain.garden.services import create as create_domain_services
from src.domain.user.entities import User
from src.interfaces.email.emitter import AbstractEmailEmitter
from src.interfaces.persistence.garden.repository import AbstractGardenRepository
from src.interfaces.persistence.user.repository import AbstractUserRepository
from src.ops.environment.schemas import EnvironmentAttributeClusterInput
from src.ops.exceptions import EntityNotFound
from src.ops.garden.schemas.read import GardenFullSchema
from src.utils.key_generator import generate_unique_key


class GardenAttrsOpsController:
    def __init__(self, garden_repo: AbstractGardenRepository):
        self.garden_repo = garden_repo

    async def set_attributes(
        self,
        client: User,
        data: EnvironmentAttributeClusterInput,
    ) -> GardenFullSchema:
        pass
