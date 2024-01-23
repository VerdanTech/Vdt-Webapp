# Standard Library
from dataclasses import field

# VerdanTech Source
from src.domain.common import EntityIdType, Ref, Value
from src.domain.workspace.workspace import Workspace

from .plant import Plant


class PlantGroup(Value):
    parent: Ref[Workspace] | Ref[AgroPlan]
    plants: list[Plant] = field(default_factory=list)
    size: int
