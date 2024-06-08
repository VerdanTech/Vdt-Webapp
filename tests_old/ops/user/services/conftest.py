# External Libraries
import pytest

# VerdanTech Source
from mocks.infra.persistence.repository.user_mock import MockUserRepository
from tests_old.domain.user.conftest import user  # noqa: F401 - pytest fixture


@pytest.fixture
def mock_user_repo():
    return MockUserRepository()
