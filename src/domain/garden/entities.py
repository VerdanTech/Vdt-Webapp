# Standard Library
from dataclasses import field
from typing import List

# VerdanTech Source
from src.domain.common import Ref, RootEntity, root_entity_dataclass
from src.domain.plants.entities import PlantSet
from src.domain.user.entities import User
from src.domain.workspace.entities import Workspace

from .values import RoleEnum, VisibilityEnum


@root_entity_dataclass
class Garden(RootEntity):
    key_id: str
    name: str
    creator: Ref[User] | None
    visibility: VisibilityEnum
    admins: List[Ref["GardenMembership"]]
    editors: List[Ref["GardenMembership"]] = field(default_factory=list)
    viewers: List[Ref["GardenMembership"]] = field(default_factory=list)
    plantsets: List[Ref[PlantSet]] = field(default_factory=list)
    workspaces: List[Ref[Workspace]] = field(default_factory=list)


@root_entity_dataclass
class GardenMembership(RootEntity):
    inviter: Ref[User] | None
    user: Ref[User]
    garden: Ref[Garden]
    role: RoleEnum
    open_invite: bool = True
