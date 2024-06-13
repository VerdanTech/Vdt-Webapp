# VerdanTech Source
from src.common.domain import Ref, RootEntity, root_entity_transform
from src.environment.domain import Environment
from src.garden.domain.garden import Garden


@root_entity_transform
class Workspace(RootEntity):
    garden_ref: Ref[Garden]
    name: str
    environment_ref: Ref[Environment] | None = None
