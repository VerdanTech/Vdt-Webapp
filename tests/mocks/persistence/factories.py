# VerdanTech Source
from tests.mocks.persistence.mock_uow import MockUow


def provide_mock_uow() -> MockUow:
    uow = MockUow()

    # TODO: For some reason, the event iterator was persisting across tests.
    # This is a temporary fix to ensure the event iterator is empty before each test.
    for event in uow.collect_new_events():
        pass
    return MockUow()
