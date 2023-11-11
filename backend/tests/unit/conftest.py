import pytest
from src.infra.persistence.repository.mock.user.repository import MockUserRepository
from src.interfaces.security.crypt import MockPasswordCrypt
from src.utils.sanitizers.object import MockObjectSanitizer


@pytest.fixture
def mock_password_crypt():
    return MockPasswordCrypt()


@pytest.fixture
def mock_user_repo():
    return MockUserRepository()


@pytest.fixture
def mock_object_sanitizer():
    return MockObjectSanitizer()
