# Standard Library
from dataclasses import dataclass
from typing import Optional

# VerdanTech Source
from src.domain.common import EntityIdType
from src.domain.garden.enums import VisibilityEnum


@dataclass
class GardenCreateInput:
    name: str
    description: str
    admin_ids: Optional[list[EntityIdType]] = None
    editor_ids: Optional[list[EntityIdType]] = None
    viewer_ids: Optional[list[EntityIdType]] = None
    visibility: VisibilityEnum = VisibilityEnum.PRIVATE
