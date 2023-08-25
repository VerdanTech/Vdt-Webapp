from litestar.contrib.repository.testing.generic_mock_repository import (
    GenericAsyncMockRepository,
)
from src.verdantech_api.domain.models.common.entities import MockEntity


class MockEntityRepository(GenericAsyncMockRepository[MockEntity]):
    model_type = MockEntity
