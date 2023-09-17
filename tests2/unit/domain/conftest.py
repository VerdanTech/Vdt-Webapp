import pytest
from litestar.contrib.repository.testing.generic_mock_repository import (
    GenericAsyncMockRepository,
)
from src.verdantech_api.lib.utils import IdFactory


@pytest.fixture
def id_factory():
    id_factory = IdFactory()
    return id_factory.factory
