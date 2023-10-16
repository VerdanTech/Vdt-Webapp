from typing import List

import pytest
from pytest_mock import MockerFixture
from src.utils.sanitizers.field import FieldSanitizer
from src.utils.sanitizers.object import (
    ObjectSanitizer,
    ObjectSanitizerConfig,
)
from src.utils.sanitizers.sanitization.generic import Sanitization


@pytest.fixture
def mock_sanitizations(mocker: MockerFixture) -> List[Sanitization]:
    """Provides a list of mock sanitizations"""
    sanitization_classes = [
        Sanitization,
        Sanitization,
        Sanitization,
    ]
    mock_sanitizations = [
        mocker.MagicMock(spec=sanitization_class)
        for sanitization_class in sanitization_classes
    ]
    return mock_sanitizations


@pytest.fixture
def field_sanitizer(
    mock_sanitizations: List[Sanitization], mocker: MockerFixture
) -> FieldSanitizer:
    """Return a FieldSanitizer with mock sanitizations"""
    return FieldSanitizer(*mock_sanitizations)


class MockEntitySanitizerConfig(ObjectSanitizerConfig):
    int_field: FieldSanitizer
    str_field: FieldSanitizer


class MockEntitySanitizer(ObjectSanitizer[MockEntitySanitizerConfig]):
    pass


@pytest.fixture
def mock_entity_sanitizer():
    config = MockEntitySanitizerConfig(
        int_field=FieldSanitizer(), str_field=FieldSanitizer()
    )
    return MockEntitySanitizer(config=config)
