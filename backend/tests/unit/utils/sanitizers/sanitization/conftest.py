import pytest
from src.utils.sanitizers.sanitization.generic import Sanitization, SanitizationConfig


@pytest.fixture
def sanitization() -> Sanitization:
    """Provide a base validation class instance"""
    return Sanitization(SanitizationConfig(spec=0, error_message=""))
