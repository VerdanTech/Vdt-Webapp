# External Libraries
import pytest

# VerdanTech Source
from tests.mocks.infra.persistence.repository.user_mock import MockUserRepository


@pytest.fixture
def mock_user_repo():
    return MockUserRepository()
