import asyncio

import pytest


@pytest.fixture(scope="session")
def event_loop():
    """
    Creates an instance of the default event loop for the test session.

    https://www.core27.co/post/transactional-unit-tests-with-pytest-and-async-sqlalchemy
    """
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()
