# External Libraries
import pytest
from svcs import Container

# VerdanTech Source
from src.domain.user import User
from src.interfaces.security.crypt import AbstractPasswordCrypt
from src.ops import exceptions as ops_exceptions
from src.ops.user.controllers.auth import UserAuthOpsController
from src.ops.user.schemas.auth import UserLoginInput
from src.utils.sanitizers import custom
from src.utils.sanitizers.spec import SpecError

pytestmark = [pytest.mark.unit]


class TestUserAuthOpsController:
    # ======================================
    # UserAuthOpsController.login() tests
    # ======================================

    async def test_login_invalid_input(
        self, user_auth_ops_controller: UserAuthOpsController, svcs_container: Container
    ) -> None:
        """
        Ensure that when the operation is called with an invalid email,
        a SpecError is raised with all the invalid results.

        Args:
            user_auth_ops_controller (UserAuthOpsController): fixture providing
                controller to test.
            svcs_container (Container): service locator with mock services.
        """
        # Retrieve dependencies
        user_sanitizer = await svcs_container.aget(UserSanitizer)
        password_crypt = await svcs_container.aget_abstract(AbstractPasswordCrypt)

        # Fails length, and email sanitization.
        invalid_email = "a"

        input_data = UserLoginInput(
            email_address=invalid_email, password="test_password"
        )

        with pytest.raises(SpecError) as error:
            await user_auth_ops_controller.login(
                data=input_data,
                user_sanitizer=user_sanitizer,
                password_crypt=password_crypt,
            )

        error_message = error.value.args[0]

        assert error_message["email_address"][custom.EmailSpec.name] is not None

    async def test_login_user_not_found(
        self, user_auth_ops_controller: UserAuthOpsController, svcs_container: Container
    ) -> None:
        """
        Ensure that when the operation is called with an email that does
        not match an existing user, the EntityNotFound exception is raised.

        Args:
            user_auth_ops_controller (UserAuthOpsController): fixture providing
                controller to test.
            svcs_container (Container): service locator with mock services.
        """
        # Retrieve dependencies
        user_sanitizer = await svcs_container.aget(UserSanitizer)
        password_crypt = await svcs_container.aget_abstract(AbstractPasswordCrypt)

        nonexistant_valid_email = "nonexistant_email@gmail.com"

        input_data = UserLoginInput(
            email_address=nonexistant_valid_email, password="test_password"
        )

        with pytest.raises(ops_exceptions.EntityNotFound):
            await user_auth_ops_controller.login(
                data=input_data,
                user_sanitizer=user_sanitizer,
                password_crypt=password_crypt,
            )

    async def test_login_success_correct_password(
        self, user_auth_ops_controller: UserAuthOpsController, svcs_container: Container
    ) -> None:
        """
        Ensure that when the operation is called with an email that does
        exist and a password which matches that of the user, the user is returned.

        Args:
            user_auth_ops_controller (UserAuthOpsController): fixture providing
                controller to test.
            svcs_container (Container): service locator with mock services.
        """
        # Retrieve dependencies
        user_sanitizer = await svcs_container.aget(UserSanitizer)
        password_crypt = await svcs_container.aget_abstract(AbstractPasswordCrypt)

        existing_valid_email = "existing_email@gmail.com"
        existing_password = "existing_password"

        # Add existing user
        existing_user = User(username="existing_username")
        existing_user.email_create(address=existing_valid_email, max_emails=1)
        await existing_user.set_password(
            password=existing_password, password_crypt=password_crypt, overwrite=True
        )
        existing_user = await user_auth_ops_controller.user_repo.add(user=existing_user)

        input_data = UserLoginInput(
            email_address=existing_valid_email, password=existing_password
        )

        user_result = await user_auth_ops_controller.login(
            data=input_data,
            user_sanitizer=user_sanitizer,
            password_crypt=password_crypt,
        )

        assert user_result == existing_user

    async def test_login_success_incorrect_password(
        self, user_auth_ops_controller: UserAuthOpsController, svcs_container: Container
    ) -> None:
        """
        Ensure that when the operation is called with an email that does
        exist and a password which does not match that of the user, None is returned.

        Args:
            user_auth_ops_controller (UserAuthOpsController): fixture providing
                controller to test.
            svcs_container (Container): service locator with mock services.
        """
        # Retrieve dependencies
        user_sanitizer = await svcs_container.aget(UserSanitizer)
        password_crypt = await svcs_container.aget_abstract(AbstractPasswordCrypt)

        existing_valid_email = "existing_email@gmail.com"
        existing_password = "existing_password"

        # Add existing user
        existing_user = User(username="existing_username")
        existing_user.email_create(address=existing_valid_email, max_emails=1)
        await existing_user.set_password(
            password=existing_password, password_crypt=password_crypt, overwrite=True
        )
        await user_auth_ops_controller.user_repo.add(user=existing_user)

        input_data = UserLoginInput(
            email_address=existing_valid_email, password="incorrect_password"
        )

        user_result = await user_auth_ops_controller.login(
            data=input_data,
            user_sanitizer=user_sanitizer,
            password_crypt=password_crypt,
        )

        assert user_result is None
