# Standard Library
from typing import List

# VerdanTech Source
from src.domain.common import (
    Entity,
    RootEntity,
    entity_dataclass,
    root_entity_dataclass,
)


@root_entity_dataclass
class PlantSet(RootEntity):
    name: str
    plant_types: List["PlantType"]


@entity_dataclass
class PlantType(Entity):
    name: str
    abbreviation: str
    parent_name: str
    attribute_profiles: List["PlantAttributeProfile"]


@entity_dataclass
class PlantAttributeProfile(Entity):
    name: str
    # attributes: List[PlantAttribute]
