# Standard Library
import uuid
from dataclasses import field

# External Libraries
import Ref
import Value

# VerdanTech Source
from src.workspace.domain.workspace import Workspace

from .plant import Plant


class PlantGroup(RootEntity):
    parent: Ref[Workspace] | Ref[AgroPlan]
    plants: list[Plant] = field(default_factory=list)
    size: int
