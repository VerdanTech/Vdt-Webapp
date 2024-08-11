# Standard Library
import asyncio
from contextlib import nullcontext
from typing import ContextManager

# External Libraries
import pytest
from svcs import Container

# VerdanTech Source
from tests.mocks.registry import mock_registry


@pytest.fixture
def expected_error_context(request) -> ContextManager:
    """
    Using pytest's parametrization to assert
    that different errors were raised in different test cases
    doesn't work for test cases where no error is to be raised.
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
            pytest.raises(expected_error_context) otherwise.
    """
    if request.param is None:
        return nullcontext()
    else:
        return pytest.raises(request.param)


@pytest.fixture(scope="session", autouse=True)
def event_loop(request):
    """
    Creates an instance of the default event loop for the test session.

    Session scoped as to enable the use of session-scoped connections.

    https://www.core27.co/post/transactional-unit-tests-with-pytest-and-async-sqlalchemy
    """
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
def svcs_container() -> Container:
    """
    Fixture returning an services container
    with a registry full of mock adapters.

    Returns:
        Container: svcs container.
    """
    container = Container(registry=mock_registry)
    return container
