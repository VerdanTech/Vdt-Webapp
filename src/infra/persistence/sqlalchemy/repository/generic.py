# Standard Library
from typing import Any, Dict, Generic

# External Libraries
from sqlalchemy.ext.asyncio import AsyncSession

# VerdanTech Source
from src.domain.common import RootEntityT
from src.infra.persistence.generic.repository import BaseRepository
from src.infra.persistence.sqlalchemy.mapper.generic import BaseAlchemyMapper
from src.infra.persistence.sqlalchemy.mapper.model import BaseAlchemyModel


class BaseAlchemyRepository(BaseRepository[RootEntityT]):
    mapper: BaseAlchemyMapper

    def __init__(
        self,
        transaction: AsyncSession,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.transaction = transaction

    def _entity_to_model(self, entity: RootEntityT) -> BaseAlchemyModel:
        """Wrap entity to model mapping

        Args:
            entity (RootEntityT): entity to map

        Returns:
            BaseAlchemyModel: result of mapping
        """
        return self.mapper.to_model(entity=entity)

    def _model_to_entity(self, model: BaseAlchemyModel) -> RootEntityT:
        """Wrap model to entity mapping

        Args:
            model (BaseAlchemyModel): model to map

        Returns:
            RootEntityT: result of mapping
        """
        return self.mapper.from_model(model=model)
