# Standard Library
from enum import Enum


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
