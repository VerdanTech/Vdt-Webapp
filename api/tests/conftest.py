from contextlib import nullcontext
from functools import partial

import pytest
from src.verdantech_api.domain.utils.key_generator import key_generator

from .utils import MockEntityRepository


@pytest.fixture
def expected_error_context(request):
    if request.param is None:
        return nullcontext()
    else:
        return pytest.raises(request.param)


@pytest.fixture
def mock_entity_repo():
    return MockEntityRepository(id_factory=partial(key_generator, length=8))
