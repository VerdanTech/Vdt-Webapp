# Standard Library
from typing import Generic

# VerdanTech Source
from src.domain.common import RootEntityT

from .model import BaseAlchemyModel


class BaseAlchemyMapper(Generic[RootEntityT]):
    """Implementation of a model mapper interface using sqlalchemy."""

    entity: RootEntityT
    model: BaseAlchemyModel

    @staticmethod
    def to_model(self, entity: RootEntityT) -> BaseAlchemyModel:
        """Given a root entity, map into sqlalchemy model.

        Args:
            entity (RootEntity): the entity to map

        Returns:
            BaseAlchemyModel: the resultant sqlalchemy model
        """
        raise NotImplementedError

    @staticmethod
    def from_model(self, model: BaseAlchemyModel) -> RootEntityT:
        """Given a sqlalchemy model, map into python object

        Args:
            BaseAlchemyModel: the sqlalchemy model to map

        Returns:
            RootEntityT: the resultant object
        """
        raise NotImplementedError
