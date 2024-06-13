# External Libraries
import pytest

# VerdanTech Source
from src.common.adapters.security.passlib import PasslibPasswordCrypt


@pytest.fixture
def passlib_password_crypt():
    return PasslibPasswordCrypt()
