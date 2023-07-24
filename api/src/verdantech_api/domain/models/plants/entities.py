from typing import List

from ..common.entities import Entity, RootEntity
from .values import PlantAttribute


class PlantSet(RootEntity):
    name: str
    plant_types: List["PlantType"]


class PlantType(Entity):
    name: str
    abbreviation: str
    parent_name: str
    attribute_profiles: List["PlantAttributeProfile"]


class PlantAttributeProfile(Entity):
    name: str
    attributes: List[PlantAttribute]
