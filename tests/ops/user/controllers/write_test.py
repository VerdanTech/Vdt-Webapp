# External Libraries
import pytest
from pytest_mock import MockerFixture
from svcs import Container

# VerdanTech Source
from mocks.infra.persistence.repository.user_mock import MockUserRepository
from mocks.infra.security.mock_crypt import MockPasswordCrypt
from src.dependencies.factories.ops.user.sanitizers import provide_user_sanitizer
from src.domain.user.entities import User
from src.domain.user.sanitizers import UserSanitizer
from src.interfaces.email.emitter import AbstractEmailEmitter
from src.interfaces.persistence.user.repository import AbstractUserRepository
from src.interfaces.security.crypt import AbstractPasswordCrypt
from src.ops.user.controllers.write import UserWriteOpsController
from src.ops.user.schemas.write import UserCreateInput
from src.utils.sanitizers import basic, custom, repo
from src.utils.sanitizers.spec import SpecError

pytestmark = [pytest.mark.integration]



class TestUserWriteOpsController:
    # ======================================
    # UserWriteOpsController.create() tests
    # ======================================

    async def test_create_invalid_input(
        self,
        user_write_ops_controller: UserWriteOpsController,
        svcs_container: Container,
        mocker: MockerFixture,
    ) -> None:
        """
        Ensure that when the operation is called with a maximally invalid data input,
        a SpecError is raised with all the invalid results.

        Args:
            user_write_ops_controller (UserWriteOpsController): fixture
                providing controller to test.
            mock_password_crypt (AbstractPasswordCrypt): fixture
                providing mock password crypt.
            mocker (MockerFixture): pytest_mock.
        """
        # Fails length, regex, ban, and uniqueness sanitization.
        existing_invalid_username = "$a"

        # Fails length, email, and uniqueness sanitization.
        existing_invalid_email = "a"

        # Fails length and regex sanitization.
        invalid_password = "a"

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
                data=input_data, svcs_container=svcs_container
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
        mocker: MockerFixture,
    ) -> None:
        """
        Ensure that when the operation is called with mismatched password inputs,
        a SpecError is raised.

        Args:
            user_write_ops_controller (UserWriteOpsController): fixture
                providing controller to test.
            mock_password_crypt (AbstractPasswordCrypt): fixture
                providing mock password crypt.
            mocker (MockerFixture): pytest_mock.
        """
        input_data = UserCreateInput(
            username="new_username",
            email_address="new_email_address@test.com",
            password1="New_password12",
            password2="Mismatched_password12",
        )

        with pytest.raises(SpecError) as error:
            await user_write_ops_controller.create(
                data=input_data, svcs_container=svcs_container
            )

        error_message = error.value.args[0]

        assert error_message["MultiFieldError"] is not None

    async def test_create_success(
        self,
        user_write_ops_controller: UserWriteOpsController,
        svcs_container: Container,
        mocker: MockerFixture,
    ) -> None:
        """
        Ensure the user creation operation creates a user and persists
        them into the repository.

        Args:
            user_write_ops_controller (UserWriteOpsController): fixture
                providing controller to test.
            mock_password_crypt (AbstractPasswordCrypt): fixture
                providing mock password crypt.
            mocker (MockerFixture): pytest_mock.
        """
        input_data = UserCreateInput(
            username="new_username",
            email_address="new_email_address@test.com",
            password1="New_password12",
            password2="New_password12",
        )

        result = await user_write_ops_controller.create(
            data=input_data, svcs_container=svcs_container
        )

        persisted_user = (
            await user_write_ops_controller.user_repo.get_user_by_email_address(
                email_address=result.get_primary_email().address
            )
        )

        assert (
            persisted_user.id == result.id
            and persisted_user.username == result.username
            and persisted_user._password_hash is not None
        )
