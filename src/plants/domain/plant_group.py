# Standard Library
from dataclasses import field

# VerdanTech Source
from src.common.domain import EntityIdType, Ref, Value
from src.workspace.domain.workspace import Workspace

from .plant import Plant


class PlantGroup(RootEntity):
    parent: Ref[Workspace] | Ref[AgroPlan]
    plants: list[Plant] = field(default_factory=list)
    size: int
