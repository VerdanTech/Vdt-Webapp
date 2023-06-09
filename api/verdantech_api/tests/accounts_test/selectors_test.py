import pytest

from verdantech_api.apps.accounts.selectors import user_detail
from verdantech_api.apps.core.exceptions import ApplicationError

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

    def test_user_does_not_exist(self, UserMake):
        """
        Ensure the user detail selector
        raises an application error for
        a user which does not exist
        """

        user = UserMake.create()

        with pytest.raises(ApplicationError):
            user_detail(fetched_by=user, username="user_does_not_exist")
