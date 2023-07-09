import pytest
from src.verdantech_api.lib.validators.generic.validations import Validation


@pytest.fixture
def base_validation():
    return Validation(validate_against=0, error_message="")
