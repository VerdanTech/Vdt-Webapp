# Standard Library
from datetime import date, datetime

# External Libraries
from attrs import field

# VerdanTech Source
from src.common.domain import (
    Ref,
    RootEntity,
    Value,
    root_entity_transform,
    value_transform,
)
from src.cultivars.domain import Cultivar, CultivarCollection, OriginEnum
from src.geometry import GeometricHistory
from src.workspace.domain import LocationHistory, Workspace


class HarvestSizeEnum:
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


@value_transform
class Harvest(Value):
    date: date
    quantity: float
    quality: HarvestSizeEnum


@value_transform
class QuantityHistoryPoint(Value):
    quantity: float
    time: datetime | None


@value_transform
class QuantityHistory(Value):
    quantities: set[QuantityHistoryPoint] = field(factory=set)

    @property
    def undefined(self) -> bool:
        """
        Returns:
            bool: True if the GeometryHistory has no defined
                geometries.
        """
        return not self.quantities


@value_transform
class Lifespan(Value):
    origin: OriginEnum | None = None
    location_history: LocationHistory = LocationHistory()
    geometric_history: GeometricHistory = GeometricHistory()
    quantity_history: QuantityHistory = QuantityHistory()
    seed_date: date | None = None
    germ_date: date | None = None
    expiry_date: date | None = None
    harvests: list[Harvest] = field(factory=list)

    @property
    def undefined(self) -> bool:
        """
        Returns:
            bool: True if the Lifespan has no defined location,
                geometries, or lifespan points.
        """
        return (
            self.location_history.undefined
            and self.geometric_history.undefined
            and self.quantity_history.undefined
            and self.seed_date is None
            and self.germ_date is None
            and self.expiry_date is None
            and not self.harvests
        )


@root_entity_transform
class Plant(RootEntity):
    _cultivar_collection_ref: Ref[CultivarCollection]
    _cultivar_name: str
    _cultivar: Cultivar
    recorded_lifespan: Lifespan = Lifespan()
    expected_lifespan: Lifespan = Lifespan()

    @property
    def cultivar() -> Cultivar:
        ...

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


class PlantGroup(RootEntity):
    parent: Ref[Workspace] | Ref[AgroPlan]
    plants: list[Plant] = field(default_factory=list)
    size: int
