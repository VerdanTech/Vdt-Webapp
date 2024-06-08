# External Libraries
import pytest
from svcs import Container

# VerdanTech Source
from src.user.domain import User
from src.common.interfaces.email import AbstractEmailEmitter
from src.interfaces.security.crypt import AbstractPasswordCrypt
from src.ops.user.controllers.write import UserWriteOpsController
from src.ops.user.schemas.write import UserCreateInput
from src.utils.sanitizers import basic, custom, repo
from src.utils.sanitizers.spec import SpecError

pytestmark = [pytest.mark.unit]


class TestUserWriteOpsController:
    # ======================================
    # UserWriteOpsController.create() tests
    # ======================================

    async def test_create_invalid_input(
        self,
        user_write_ops_controller: UserWriteOpsController,
        svcs_container: Container,
    ) -> None:
        """
        Ensure that when the operation is called with a maximally invalid data input,
        a SpecError is raised with all the invalid results.

        Args:
            user_write_ops_controller (UserWriteOpsController): fixture
                providing controller to test.
            svcs_container (Container): service locator with mock services.
        """
        # Retrieve dependencies
        user_sanitizer = await svcs_container.aget(UserSanitizer)
        password_crypt, email_emitter = await svcs_container.aget_abstract(
            AbstractPasswordCrypt, AbstractEmailEmitter
        )

        # Fails length, regex, ban, and uniqueness sanitization.
        existing_invalid_username = "$a"

        # Fails email, and uniqueness sanitization.
        existing_invalid_email = "a"

        # Fails length and regex sanitization.
        invalid_password = "a"

        # Add existing user
        existing_user = User(username=existing_invalid_username)
        existing_user.email_create(address=existing_invalid_email, max_emails=1)
        await user_write_ops_controller.user_repo.add(user=existing_user)

        input_data = UserCreateInput(
            username=existing_invalid_username,
            email_address=existing_invalid_email,
            password1=invalid_password,
            password2=invalid_password,
        )

        with pytest.raises(SpecError) as error:
            await user_write_ops_controller.create(
                data=input_data,
                user_sanitizer=user_sanitizer,
                password_crypt=password_crypt,
                email_emitter=email_emitter,
            )

        error_message = error.value.args[0]

        assert (
            error_message["username"][basic.LengthSpec.name] is not None
            and error_message["username"][basic.RegexSpec.name] is not None
            and error_message["username"][basic.BanSpec.name] is not None
            and error_message["username"][repo.UniqueSpec.name] is not None
        )

        assert (
            error_message["email_address"][custom.EmailSpec.name] is not None
            and error_message["email_address"][repo.UniqueSpec.name] is not None
        )

        assert (
            error_message["password"][basic.LengthSpec.name] is not None
            and error_message["password"][basic.RegexSpec.name] is not None
        )

    async def test_create_password_mismatch(
        self,
        user_write_ops_controller: UserWriteOpsController,
        svcs_container: Container,
    ) -> None:
        """
        Ensure that when the operation is called with mismatched password inputs,
        a SpecError is raised.

        Args:
            user_write_ops_controller (UserWriteOpsController): fixture
                providing controller to test.
            svcs_container (Container): service locator with mock services.
        """
        # Retrieve dependencies
        user_sanitizer = await svcs_container.aget(UserSanitizer)
        password_crypt, email_emitter = await svcs_container.aget_abstract(
            AbstractPasswordCrypt, AbstractEmailEmitter
        )

        input_data = UserCreateInput(
            username="new_username",
            email_address="new_email_address@test.com",
            password1="New_password12",
            password2="Mismatched_password12",
        )

        with pytest.raises(SpecError) as error:
            await user_write_ops_controller.create(
                data=input_data,
                user_sanitizer=user_sanitizer,
                password_crypt=password_crypt,
                email_emitter=email_emitter,
            )

        error_message = error.value.args[0]

        assert error_message["MultiFieldError"] is not None

    async def test_create_success(
        self,
        user_write_ops_controller: UserWriteOpsController,
        svcs_container: Container,
    ) -> None:
        """
        Ensure the user creation operation creates a user and persists
        them into the repository.

        Args:
            user_write_ops_controller (UserWriteOpsController): fixture
                providing controller to test.
            svcs_container (Container): service locator with mock services.
        """
        # Retrieve dependencies
        user_sanitizer = await svcs_container.aget(UserSanitizer)
        password_crypt, email_emitter = await svcs_container.aget_abstract(
            AbstractPasswordCrypt, AbstractEmailEmitter
        )

        input_data = UserCreateInput(
            username="new_username",
            email_address="new_email_address@test.com",
            password1="New_password12",
            password2="New_password12",
        )

        result = await user_write_ops_controller.create(
            data=input_data,
            user_sanitizer=user_sanitizer,
            password_crypt=password_crypt,
            email_emitter=email_emitter,
        )

        persisted_user = (
            await user_write_ops_controller.user_repo.get_user_by_email_address(
                email_address=result.primary_email.address
            )
        )

        assert (
            persisted_user.id == result.id
            and persisted_user.username == result.username
            and persisted_user._password_hash is not None
        )
