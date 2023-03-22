import pytest

from .factories import BaseGardenFactory


@pytest.fixture
def BaseGarden():
    return BaseGardenFactory
