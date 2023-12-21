# External Libraries
import pytest

# VerdanTech Source
from mocks.infra.persistence.repository.user_mock import MockUserRepository
from tests.domain.user.conftest import user


@pytest.fixture
def mock_user_repo():
    return MockUserRepository()
