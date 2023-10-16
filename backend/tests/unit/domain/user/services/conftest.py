import pytest
from src.domain.user.services.verification import (
    VerificationService,
)


@pytest.fixture
def verification_service():
    return VerificationService()
