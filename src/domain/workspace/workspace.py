# Standard Library
from dataclasses import field

# VerdanTech Source
from src.domain.common import (
    Entity,
    Ref,
    RootEntity,
    entity_dataclass,
    root_entity_dataclass,
)
from src.domain.garden.garden import Garden

from .planting_area import PlantingArea


@root_entity_dataclass
class Workspace(RootEntity):
    garden_ref: Ref[Garden]
    name: str
    planting_areas: list[PlantingArea] = field(default_factory=list)
