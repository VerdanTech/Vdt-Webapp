# External Libraries
import uuid
import pytest
from faker import Faker

# VerdanTech Source
from src.garden.domain import Garden, GardenMembership, RoleEnum, generate_garden_key
from src.user.domain import User
from tests.user.conftest import user

fake = Faker()


@pytest.fixture
def garden(user: User) -> Garden:
    user.id = uuid.uuid4()
    garden = Garden(
        name=fake.name(),
        key=generate_garden_key(use_random_plant_name=True),
        creator_ref=user.ref,
    )
    garden.memberships.update(
        [GardenMembership(user_ref=user.ref, role=RoleEnum.ADMIN, inviter_ref=None)]
    )
    garden.events = []
    return garden
