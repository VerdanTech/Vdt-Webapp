# Standard Library
from dataclasses import field

# VerdanTech Source
from src import settings
from src.domain.common import Ref, RootEntity, root_entity_dataclass
from src.domain.plants.entities import PlantSet
from src.domain.user.entities import User
from src.domain.workspace.entities import Workspace
from src.utils.key_generator import key_generator

from .enums import RoleEnum, VisibilityEnum
from .values import EnvironmentAttributeProfile


@root_entity_dataclass
class Garden(RootEntity):
    name: str
    creator: Ref[User] | None
    key_id: str = field(default_factory=lambda: key_generator(length=settings.GARDEN_STR_ID_LENGTH))
    admins: list[Ref["GardenMembership"]] = field(default_factory=list) 
    description: str | None = None
    visibility: VisibilityEnum = VisibilityEnum.PRIVATE
    editors: list[Ref["GardenMembership"]] = field(default_factory=list)
    viewers: list[Ref["GardenMembership"]] = field(default_factory=list)
    plantsets: list[Ref[PlantSet]] = field(default_factory=list)
    workspaces: list[Ref[Workspace]] = field(default_factory=list)
    attributes: list[EnvironmentAttributeProfile] = field(default_factory=list)



@root_entity_dataclass
class GardenMembership(RootEntity):
    inviter: Ref[User] | None
    user: Ref[User]
    garden: Ref[Garden]
    role: RoleEnum = RoleEnum.VIEW
    open_invite: bool = True
    favorite: bool = False
