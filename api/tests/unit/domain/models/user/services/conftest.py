import pytest
from src.verdantech_api.domain.models.user.services.verification import (
    VerificationService,
)


@pytest.fixture
def verification_service():
    return VerificationService()
