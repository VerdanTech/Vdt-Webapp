# Standard Library
from datetime import datetime
from typing import List

from ..common import root_entity
from ..plants.values import PlantSetRef
from ..user.values import UserRef
from ..workspace.values import WorkspaceRef
from .values import GardenMembershipRefGarden, GardenRef, RoleEnum, VisibilityEnum


@root_entity
class Garden:
    key_id: str
    name: str
    creator: UserRef | None
    visibility: VisibilityEnum
    admins: List[GardenMembershipRefGarden]
    editors: List[GardenMembershipRefGarden]
    viewers: List[GardenMembershipRefGarden]
    plantsets: List[PlantSetRef]
    workspaces: List[WorkspaceRef]


@root_entity
class GardenMembership:
    inviter: UserRef | None
    user: UserRef
    garden: GardenRef
    role: RoleEnum
    created_at: datetime

    open_invite: bool = True
