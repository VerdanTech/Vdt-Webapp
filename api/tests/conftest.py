from contextlib import nullcontext
from typing import ContextManager

import pytest
from src.verdantech_api.infrastructure.persistence.repository.mock.mock_entity import (
    MockEntityRepository,
)


@pytest.fixture
def expected_error_context(request) -> ContextManager:
    """Using pytest's parametrization to assert
        that different errors were raised doesn't work
        for test cases where no error is to be raised.
        If a parameter called "expected_error" is defined
        and used in a test like:

        with pytest.raises(expected_error):
            ...

        the test will fail if expected_error is None.

        This fixture allows the use of an
        expected_error_context parameter, which can be an
        instance of any exception or None. If None,
        the fixture returns a nullcontext context manager
        which essentially does no assertion. If not None,
        the fixture returns a pytest.raises() context manager
        configured with the given exception.

        To use, define a parameter called "expected_error_context",
        and add it to the parametrization like so:

        @pytest.mark.parametrization(
            ("expected_error_context"),
            [(None), (Exception)],
            indirect=["expected_error_context"]
        )

    Returns:
        ContextManager: An instance of nullcontext() if
            expected_error_context = None and
            pytest.raises(expected_error_context) otherwise
    """
    if request.param is None:
        return nullcontext()
    else:
        return pytest.raises(request.param)


@pytest.fixture
def mock_entity_repo():
    return MockEntityRepository()
