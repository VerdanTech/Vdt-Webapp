# Standard Library
from typing import Literal

# VerdanTech Source
from src.common.domain import value_transform

from .profile import CultivarAttributeProfile


@value_transform
class AnnualLifecycleProfile(CultivarAttributeProfile):
    seed_to_germ: float | None = None
    germ_to_transplant: float | None = None
    germ_to_first_harvest: float | None = None
    first_to_last_harvest: float | None = None
