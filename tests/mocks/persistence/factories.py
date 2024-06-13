# VerdanTech Source
from tests.mocks.persistence.mock_uow import MockUow


def provide_mock_uow() -> MockUow:
    return MockUow()
