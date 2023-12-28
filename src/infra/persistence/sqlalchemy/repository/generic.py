# Standard Library
from typing import Any, Dict, Generic

# External Libraries
from sqlalchemy.ext.asyncio import AsyncSession

# VerdanTech Source
from src.domain.common import RootEntity
from src.infra.persistence.generic.repository import BaseRepository
from src.infra.persistence.sqlalchemy.mapper.generic import BaseAlchemyMapper
from src.infra.persistence.sqlalchemy.mapper.model import BaseAlchemyModel


class BaseAlchemyRepository[T: RootEntity](BaseRepository[T]):
    mapper: BaseAlchemyMapper

    def __init__(
        self,
        transaction: AsyncSession,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.transaction = transaction

    def _entity_to_model(self, entity: RootEntity) -> BaseAlchemyModel:
        """Wrap entity to model mapping

        Args:
            entity (RootEntity): entity to map

        Returns:
            BaseAlchemyModel: result of mapping
        """
        return self.mapper.to_model(entity=entity)

    def _model_to_entity(self, model: BaseAlchemyModel) -> RootEntity:
        """Wrap model to entity mapping

        Args:
            model (BaseAlchemyModel): model to map

        Returns:
            RootEntity: result of mapping
        """
        return self.mapper.from_model(model=model)
