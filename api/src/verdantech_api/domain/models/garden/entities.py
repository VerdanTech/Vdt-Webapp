from datetime import datetime
from typing import List

from ..common.entities import RootEntity
from ..plants.values import PlantSetRef
from ..user.values import UserRef
from ..workspace.values import WorkspaceRef
from .values import GardenMembershipRefGarden, GardenRef, RoleEnum, VisibilityEnum


class Garden(RootEntity):
    short_id: str
    name: str
    creator: UserRef | None
    visibility: VisibilityEnum
    admins: List[GardenMembershipRefGarden]
    editors: List[GardenMembershipRefGarden]
    viewers: List[GardenMembershipRefGarden]
    plantsets: List[PlantSetRef]
    workspaces: List[WorkspaceRef]


class GardenMembership(RootEntity):
    inviter: UserRef | None
    user: UserRef
    garden: GardenRef
    role: RoleEnum
    created_at: datetime

    open_invite: bool = True
