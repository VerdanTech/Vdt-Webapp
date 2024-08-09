# External Libraries
import pytest

# VerdanTech Source
from src import exceptions
from src.garden.domain import Garden, GardenMembership, generate_garden_key
from tests.user.conftest import user  # noqa: F401 - pytest fixture

pytestmark = [pytest.mark.unit]
# VerdanTech Source
from src.user.domain import User


def test_generate_garden_key() -> None:
    pass


class TestGarden:
    pass

    # ======================================
    # Garden.num_memberships() tests
    # ======================================
    def test_num_memberships(self, garden: Garden) -> None:
        """
        Ensure that the method returns the number of memberships on the garden.

        Args:
            garden (Garden): garden factory fixture.
        """
        assert garden.num_memberships == len(garden.memberships)

    # ======================================
    # Garden.is_user_member() tests
    # ======================================
    def test_is_user_member(self, user: User, garden: Garden) -> None:
        """
        Ensure that the method returns true if the user is a member,
        and false if not.

        Args:
            user (User): user factory fixture. Note that this user
                is set as the creator within the Garden fixture.
            garden (Garden): garden factory fixture.
        """
        assert garden.is_user_member(user) is True
        garden.memberships.pop()
        assert garden.is_user_member(user) is False

    # ======================================
    # Garden.get_membership() tests
    # ======================================
    # ======================================
    # Garden.accept_membership() tests
    # ======================================
    # ======================================
    # Garden.remove_membership() tests
    # ======================================
    # ======================================
    # Garden.revoke_membership() tests
    # ======================================
    # ======================================
    # Garden.change_role() tests
    # ======================================
