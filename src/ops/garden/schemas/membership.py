# Standard Library
from dataclasses import dataclass

# VerdanTech Source
from src.domain.common import EntityIdType
from src.domain.garden.enums import RoleEnum


@dataclass
class GardenInviteCreateInput:
    user_id: EntityIdType
    garden_id: EntityIdType
    role: RoleEnum


@dataclass
class GardenInviteAcceptInput:
    garden_id: EntityIdType
