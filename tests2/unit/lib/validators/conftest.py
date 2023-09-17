from typing import List, Tuple

import pytest
from pytest_mock import MockerFixture
from src.verdantech_api.lib.validators.generic.validations import (
    BannedInputValidation,
    MaxLengthValidation,
    MaxSizeValidation,
    MinLengthValidation,
    MinSizeValidation,
    RegexValidation,
    Validation,
    ValidationConfig,
)
from src.verdantech_api.lib.validators.generic.validators import FieldValidator


@pytest.fixture
def base_validation() -> Validation:
    """Provide a base validation class instance"""
    return Validation(ValidationConfig(validate_against=0, error_message=""))


@pytest.fixture
def mock_validations(mocker: MockerFixture) -> List[Validation]:
    """Provides a list of mock validations"""
    validation_classes = [
        MinSizeValidation,
        MaxSizeValidation,
        MinLengthValidation,
        MaxLengthValidation,
        RegexValidation,
        BannedInputValidation,
    ]
    mock_validations = [
        mocker.MagicMock(spec=validation_class)
        for validation_class in validation_classes
    ]
    return mock_validations


@pytest.fixture
def field_validator(
    mock_validations: List[Validation], mocker: MockerFixture
) -> FieldValidator:
    """Return a FieldValidator with all mock validations"""
    return FieldValidator(*mock_validations)
