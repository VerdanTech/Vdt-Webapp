# Standard Library
from typing import Annotated

# External Libraries
from pydantic import Field

# VerdanTech Source
from src.common.adapters.utils.spec_manager import SpecCollection
from src.common.domain import Command, value_transform

from ..enums import OriginEnum
from .profile import CultivarAttributeProfile

type AllowedOriginsType = set[OriginEnum]

values = {}
descriptions = {
    "origin_profile": {
        "field": ("The origin refers to the method used to create plants. "),
        "label": "Origin Profile",
    },
    "allowed_origins": {
        "field": (
            "A cultivar may be allowed to start in any combination of origins. "
            "In general, plants may be started from seed and transplanted to where they reach maturity, "
            "started from seed in the location they reach maturity, or brought in as seedlings. "
            "Some plants, such as carrots, don't tolerate transplants, and so must be started directly."
        ),
        "label": "Allowed Origins",
    },
}
origin_specs = SpecCollection("origin_profile", values, descriptions)


@value_transform
class OriginProfile(CultivarAttributeProfile):
    allowed_origins: set[OriginEnum] | None = None


class OriginProfileUpdateCommand(Command):
    allowed_origins: Annotated[
        set[OriginEnum], Field(description=descriptions["allowed_origins"]["field"])
    ] | None = None
