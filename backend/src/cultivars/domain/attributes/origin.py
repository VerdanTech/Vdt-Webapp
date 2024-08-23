# VerdanTech Source
from src.attributes.domain import Attribute, AttributeProfile
from src.common.domain import value_transform

from ..enums import OriginEnum

type AllowedOriginsType = set[OriginEnum]


class AllowedOrigins(Attribute[AllowedOriginsType]):
    label = "Allowed Origins"
    description = "The methods applicable to starting a plant instance"


@value_transform
class OriginProfile(AttributeProfile):
    label = "Origin Profile"
    description = "Defined instantiation behaviour, ie. how plants are initialized when they are added to the model"

    allowed_origins: AllowedOrigins
