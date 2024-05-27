# VerdanTech Source
from src.domain.common import RootEntity, root_entity_transform

from .attributes import EnvironmentAttributeCluster


@root_entity_transform
class Environment(RootEntity):
    attributes: EnvironmentAttributeCluster
