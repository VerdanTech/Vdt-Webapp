# Standard Library
from typing import Any, Dict, Generic

# External Libraries
from sqlalchemy.ext.asyncio import AsyncSession

# VerdanTech Source
from src.domain.common.entities import RootEntityT
from src.infra.persistence.mapper.alchemy.generic import BaseAlchemyMapper
from src.infra.persistence.mapper.alchemy.model import BaseAlchemyModel

from ..generic import BaseRepository


class BaseAlchemyRepository(BaseRepository[RootEntityT]):
    mapper: BaseAlchemyMapper

    def __init__(
        self,
        session: AsyncSession,
        **kwargs: Dict[str, Any],
    ) -> None:
        super().__init__(**kwargs)
        self.session = session

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
