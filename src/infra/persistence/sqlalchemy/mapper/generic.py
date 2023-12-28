# Standard Library
from typing import Generic

# VerdanTech Source
from src.domain.common import RootEntity

from .model import BaseAlchemyModel


class BaseAlchemyMapper[T: RootEntity]:
    """Implementation of a model mapper interface using sqlalchemy."""

    entity = T
    model: BaseAlchemyModel

    @staticmethod
    def to_model(entity: T) -> BaseAlchemyModel:
        """Given a root entity, map into sqlalchemy model.

        Args:
            entity (RootEntity): the entity to map

        Returns:
            BaseAlchemyModel: the resultant sqlalchemy model
        """
        raise NotImplementedError

    @staticmethod
    def from_model(model: BaseAlchemyModel) -> RootEntity:
        """Given a sqlalchemy model, map into python object

        Args:
            BaseAlchemyModel: the sqlalchemy model to map

        Returns:
            RootEntity: the resultant object
        """
        raise NotImplementedError
