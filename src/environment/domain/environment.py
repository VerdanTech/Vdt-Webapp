# VerdanTech Source
from src.common.domain import RootEntity, root_entity_transform

from .attributes import EnvironmentAttributeCluster


@root_entity_transform
class Environment(RootEntity):
    attributes: EnvironmentAttributeCluster
