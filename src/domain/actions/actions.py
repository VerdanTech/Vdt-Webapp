# Standard Library
from enum import Enum

# VerdanTech Source
from src.domain.common import Ref, RootEntity, root_entity_transform
from src.domain.user import User
from src.domain.utils import TimeWindow

from .reminder import Reminder


class ActionEnum(Enum):
    # Plants
    SEED_PLANT = "seed plant"
    THIN_PLANT = "thin plants"
    HARDEN_PLANT = "harden plant"
    TRANSPLANT_PLANT = "transplant"
    HARVEST_PLANT = "harvest plant"
    EXPIRE_PLANT = "expire plant"
    WATER_PLANT = "water plant"
    PRUNE_PLANT = "prune plant"
    FERTILIZE_PLANT = "fertilize plant"

    # PlantContainers
    MOVE_CONTAINER = "move container"
    COVER_CONTAINER = "cover container"
    WEED_CONTAINER = "weed plant"
    FERTILIZE_CONTAINER = "fertilize container"
    TILL_CONTAINER = "till container"

    # Workspaces
    TIDY_WORKSPACE = "tidy workspace"

    # Gardens

    # Misc
    CUSTOM = "custom"
    UNDEFINED = "undefined"


@root_entity_transform
class Action(RootEntity):
    action_type: ActionEnum | str
    time_window: TimeWindow
    reminders: set[Reminder]
    assignees: set[Ref[User]]
    title: str
    description: str | None = None

    def dismiss(self):
        """dismiss the action"""

    def update(self):
        """bring action up to a date"""

    def complete(self):
        """complete an action"""
