# VerdanTech Source
from src import settings
from src.common.domain.planner.calendar import PlantingCalendar
from src.common.interfaces.email import AbstractEmailEmitter
from src.common.interfaces.security.passwords import AbstractPasswordCrypt
from src.common.ops.exceptions import EntityNotFound
from src.user.interfaces.persistence.user.user import AbstractUserRepository

from ..schemas import calendar as schemas
from ..services import verification as verification_services


class PlannerCalendarOpsController:
    def __init__(self, cultivar_repo: AbstractCultivarRepository):
        self.cultivar_repo = cultivar_repo
