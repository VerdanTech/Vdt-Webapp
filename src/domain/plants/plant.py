# Standard Library
from datetime import date

# VerdanTech Source
from src.domain.common import EntityIdType, RootEntity, Value
from src.domain.cultivars.cultivar import Cultivar


class Lifespan(Value):
    sow_date: date | None = None
    germ_date: date | None = None
    first_harvest_date: date | None = None
    last_harvest_date: date | None = None
    expiry_date: date | None = None


class Plant(RootEntity):
    cultivar_ref: EntityIdType | None
    cultivar: Cultivar | None
    committed: bool = False
    workspace_ref: Ref[Workspace]
    planting_area_ref: Ref[PlantingArea] | None
    lifespan: Lifespan = Lifespan()
