from typing import Any, Dict

from src.verdantech_api.domain.models.common.entities import RootEntityT
from src.verdantech_api.infrastructure.persistence.mapper.alchemy.model import BaseAlchemyModel
from src.verdantech_api.infrastructure.persistence.mapper.alchemy.mapper import BaseAlchemyMapper

from ..generic import BaseRepository


class BaseAlchemyRepository(BaseRepository[RootEntityT]):
    def __init__(
        self,
        session,
        mapper: BaseAlchemyMapper,
        **kwargs: Dict[str, Any],
    ) -> None:
        super().__init__(**kwargs)
        self.session = session
        self.mapper = mapper

    def _entity_to_model(self, entity: RootEntityT) -> BaseAlchemyModel:
        """Wrap entity to model mapping

        Args:
            entity (RootEntityT): entity to map

        Returns:
            BaseAlchemyModel: result of mapping
        """
        return self.mapper.to_model(entity=entity)

    def _model_to_entity(
        self, model: BaseAlchemyModel
    ) -> RootEntityT:
        """Wrap model to entity mapping

        Args:
            model (BaseAlchemyModel): model to map

        Returns:
            RootEntityT: result of mapping
        """
        return self.mapper.from_model(model=model)
