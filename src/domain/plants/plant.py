# Standard Library
from datetime import date, datetime
from enum import Enum

# External Libraries
from attrs import field

# VerdanTech Source
from src.domain.common import (
    Ref,
    RootEntity,
    Value,
    root_entity_transform,
    value_transform,
)
from src.domain.cultivars import Cultivar
from src.domain.workspace import GeometricHistory, LocationHistory


class OriginEnum(Enum):
    """Describes the process by which a plant is brought into being."""

    DIRECT_SEED = "direct seed"
    """A seed is sown directly into the area it will reach maturity in."""
    SEED_TRANSPLANT = "seed transplant"
    """A seed is sown in one area and then transplanted into the area it will reach maturity in."""
    SEEDLING_TO_TRANSPLANT = "seelding transplant"
    """A seedling is transplanted directly into the area it will reach maturity in."""


@value_transform
class QuantityHistoryPoint(Value):
    quantity: int
    time: datetime | None


@value_transform
class QuantityHistory(Value):
    quantity_points: set[QuantityHistoryPoint] = field(factory=set)


@value_transform
class Lifespan(Value):
    origin: OriginEnum = OriginEnum.DIRECT_SEED
    location_history: LocationHistory = LocationHistory()
    geometric_history: GeometricHistory = GeometricHistory()
    quantity_history: QuantityHistory = QuantityHistory()
    seed_date: date | None = None
    germ_date: date | None = None
    first_harvest_date: date | None = None
    last_harvest_date: date | None = None
    expiry_date: date | None = None

    @property
    def undefined(self) -> bool:
        """
        Returns:
            bool: True if the Lifespan has no defined location, geometries, or lifespan points.
        """
        return (
            self.location_history.locations is None
            and self.geometric_history.geometries is None
            and self.seed_date is None
            and self.germ_date is None
            and self.first_harvest_date is None
            and self.last_harvest_date is None
            and self.expiry_date is None
        )


@root_entity_transform
class Plant(RootEntity):
    cultivar_ref: Ref[Cultivar]
    recorded_lifespan: Lifespan = Lifespan()
    expected_lifespan: Lifespan = Lifespan()

    @property
    def committed(self) -> bool:
        """
        Returns:
            bool: True if the Plant has any recorded observations.
        """
        return not self.recorded_lifespan.undefined

    def similar(self, other) -> bool:
        """
        Returns

        Args:
            other (_type_): _description_

        Returns:
            bool: True if self and other share enough attributes
                relavent to display on the Calendar that
                they can be grouped together.
        """
