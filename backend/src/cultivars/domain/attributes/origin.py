# VerdanTech Source
from src.common.domain import value_transform

from ..enums import OriginEnum
from .profile import CultivarAttributeProfile

type AllowedOriginsType = set[OriginEnum]


# class AllowedOrigins(Attribute[AllowedOriginsType]):
# label = "Allowed Origins"
# description = "The methods applicable to starting a plant instance"


@value_transform
class OriginProfile(CultivarAttributeProfile):
    label = "Origin Profile"
    description = "Defined instantiation behaviour, ie. how plants are initialized when they are added to the model"


# allowed_origins: AllowedOrigins
