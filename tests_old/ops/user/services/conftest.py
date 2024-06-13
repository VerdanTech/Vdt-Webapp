# External Libraries
import pytest

# VerdanTech Source
from tests.mocks.infra.persistence.repository.user_mock import MockUserRepository
from tests.user.unit.conftest import user  # noqa: F401 - pytest fixture


@pytest.fixture
def mock_user_repo():
    return MockUserRepository()
