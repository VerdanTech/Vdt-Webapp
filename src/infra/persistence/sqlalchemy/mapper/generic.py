# Standard Library
from typing import Type

# VerdanTech Source
from src.domain.common import RootEntity
from src.infra.persistence.generic.mapper import AbstractMapper

from .model import BaseAlchemyModel


class BaseAlchemyMapper[RootEntityT: RootEntity, AlchemyModelT: BaseAlchemyModel](
    AbstractMapper
):
    """Implementation of a model mapper interface using sqlalchemy."""

    entity: Type[RootEntityT]
    model: Type[AlchemyModelT]

    @staticmethod
    def to_model(entity: RootEntityT) -> AlchemyModelT:
        """
        Given a root entity, map into sqlalchemy model.

        Args:
            entity (RootEntityT): the entity to map.

        Returns:
            AlchemyModelT: the resultant sqlalchemy model.
        """
        raise NotImplementedError

    @staticmethod
    def from_model(model: AlchemyModelT) -> RootEntityT:
        """
        Given a sqlalchemy model, map into python object

        Args:
            AlchemyModelT: the sqlalchemy model to map.

        Returns:
            RootEntityT: the resultant object.
        """
        raise NotImplementedError
