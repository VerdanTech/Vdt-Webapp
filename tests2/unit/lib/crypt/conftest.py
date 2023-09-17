import pytest
from src.verdantech_api.lib.crypt.passlib_crypt import PasslibPasswordCrypt


@pytest.fixture
def passlib_password_crypt():
    return PasslibPasswordCrypt()
