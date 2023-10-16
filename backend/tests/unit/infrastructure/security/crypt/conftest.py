import pytest
from src.infrastructure.security.crypt.passlib.passlib import (
    PasslibPasswordCrypt,
)


@pytest.fixture
def passlib_password_crypt():
    return PasslibPasswordCrypt()
