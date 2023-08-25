import pytest
from src.verdantech_api.domain.utils.sanitizers.sanitization.generic import (
    Sanitization,
    SanitizationConfig,
)


@pytest.fixture
def sanitization() -> Sanitization:
    """Provide a base validation class instance"""
    return Sanitization(SanitizationConfig(spec=0, error_message=""))
