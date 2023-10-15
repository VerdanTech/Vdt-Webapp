from pytest_mock import MockerFixture
from src.verdantech_api.application.user.operations.write import UserWriteOperations
from src.verdantech_api.application.user.schemas.api.write import UserCreateInput
from src.verdantech_api.domain.interfaces.security.crypt.password_crypt import (
    AbstractPasswordCrypt,
)
from src.verdantech_api.domain.utils.sanitizers.object import ObjectSanitizer


class TestUserWriteOperations:
    async def test_create(
        self,
        user_write_operations: UserWriteOperations,
        mock_object_sanitizer: ObjectSanitizer,
        mock_password_crypt: AbstractPasswordCrypt,
        mocker: MockerFixture,
    ) -> None:
        """Ensure that the sanitization function is called,
            user is initialized, email is added, and user is added to the repo

        Args:
            user_write_operations (UserWriteOperations): service to test on
            mock_object_sanitizer (ObjectSanitizer): fixture providing mock
                object sanitizer
            mock_password_crypt (AbstractPasswordCrypt): fixture providing mock
                password crypt
            mocker (MockerFixture): pytest-mock
        """
        input_data = UserCreateInput(
            username="test_username",
            email_address="email@email.com",
            password1="test_password",
            password2="test_password",
        )
        mock_sanitize_user_create = mocker.patch(
            "src.verdantech_api.application.user.operations.write.sanitize_user_create",
            return_value={
                "username": input_data.username,
                "email_address": input_data.email_address,
                "password": input_data.password1,
            },
        )
        mock_add_first_email = mocker.patch(
            "src.verdantech_api.application.user.operations.write.add_first_email"
        )
        mock_email_emitter = mocker.Mock()

        user = await user_write_operations.create(
            data=input_data,
            user_sanitizer=mock_object_sanitizer,
            password_crypt=mock_password_crypt,
            email_emitter=mock_email_emitter,
        )

        assert user_write_operations.user_repo.collection[0] == user
        mock_sanitize_user_create.assert_awaited_once_with(
            data=input_data, user_sanitizer=mock_object_sanitizer
        )
        mock_add_first_email.assert_awaited_once()
