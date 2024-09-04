# Standard Library
from typing import Annotated

# External Libraries
from pydantic import Field

# VerdanTech Source
from src.common.adapters.utils.spec_manager import SpecCollection
from src.common.domain import Command, value_transform

from .profile import CultivarAttributeProfile

values = {}
descriptions = {
    "origin_profile": {
        "field": ("The origin refers to the method used to create plants."),
        "label": "Origin Profile",
    },
    "transplantable": {
        "field": (
            "Defines whether a plant may be started as a seed in one location and transplanted to another. "
            "Some plants, such as carrots, don't tolerate transplants, and so must be started directly."
        ),
        "label": "Transplant Allowed",
    },
}
origin_specs = SpecCollection("origin_profile", values, descriptions)


@value_transform
class OriginProfile(CultivarAttributeProfile):
    transplantable: bool | None = None


Transplantable = Annotated[
    bool, Field(description=descriptions["transplantable"]["field"])
]


class OriginProfileUpdateCommand(Command):
    transplantable: Transplantable | None = None