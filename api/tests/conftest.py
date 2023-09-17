from contextlib import nullcontext

import pytest
from src.verdantech_api.infrastructure.persistence.repository.mock.mock_entity import (
    MockEntityRepository,
)


@pytest.fixture
def expected_error_context(request):
    if request.param is None:
        return nullcontext()
    else:
        return pytest.raises(request.param)


@pytest.fixture
def mock_entity_repo():
    return MockEntityRepository()
