import pytest
from src.infra.security.crypt.passlib.passlib import PasslibPasswordCrypt


@pytest.fixture
def passlib_password_crypt():
    return PasslibPasswordCrypt()
