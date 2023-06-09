import pytest

from verdantech_api.apps.accounts.selectors import user_detail

pytestmark = pytest.mark.django_db


class TestUserDetail:
    def test_user_returned(self, UserMake):
        """
        Ensure the user detail selector
        returns the correct user
        """

        users = UserMake.create_batch(2)

        user_returned = user_detail(fetched_by=users[0], username=users[1].username)

        assert user_returned == users[1]
