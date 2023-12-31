from src.domain.garden.values import EnvironmentAttributeProfile

from src.domain.user.entities import User
from src.domain.common import Ref
from typing import Optional

from ..entities import Garden
from ..enums import VisibilityEnum


def create_garden(
    creator: User,
    name: str,
    admins: Optional[list[User]] = None,
    description: Optional[str] = None,
    visibility: VisibilityEnum = VisibilityEnum.PRIVATE,
    editors: Optional[list[User]] = None,
    viewers: Optional[list[User],] = None,
    plantsets: Optional[list[PlantSet]] = None,
    attributes: Optional[list[EnvironmentAttributeProfile]] = None,
) -> Garden:
    if creator.id is None:
        raise Exception

    garden = Garden(name=name, creator=Ref[User](creator.id))

    garden.admins = []
