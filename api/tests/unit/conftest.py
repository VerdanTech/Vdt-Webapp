import pytest
from src.verdantech_api.domain.interfaces.security.crypt import MockPasswordCrypt


@pytest.fixture
def mock_password_crypt():
    return MockPasswordCrypt()
