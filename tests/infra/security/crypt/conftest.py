# External Libraries
import pytest

# VerdanTech Source
from src.adapters.security.crypt.passlib import PasslibPasswordCrypt


@pytest.fixture
def passlib_password_crypt():
    return PasslibPasswordCrypt()
