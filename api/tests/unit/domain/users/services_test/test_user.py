import pytest
from src.verdantech_api.domain.users.services.user import UserService


class TestUserService:
    async def test_create_user(self, user_service: UserService):
        """Ensure that the function creates the new database objects
            and adds them to the database

        Args:
            user_service (UserService): the service to test on
        """
        input_username = "username"
        input_email = "email"
        input_hashed_password = "hashed_password"

        user, email = await user_service.create_user(
            username=input_username,
            email=input_email,
            hashed_password=input_hashed_password,
        )

        assert user.id is not None
        assert user.username == input_username
        assert user.password_hash == input_hashed_password
        assert email in user.emails
        assert email.address == input_email
