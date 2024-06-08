# External Libraries
import pytest
from svcs import Container

# VerdanTech Source
from src import settings
from src.user.domain import User
from src.user.domain.email import EmailConfirmation
from src.common.interfaces.email import AbstractEmailEmitter
from src.interfaces.security.crypt.crypt import AbstractPasswordCrypt
from src.common.ops import exceptions as ops_exceptions
from src.ops.user.controllers.verification import UserVerificationOpsController
from src.ops.user.schemas.verification import (
    UserPasswordResetConfirmInput,
    UserPasswordResetRequestInput,
    UserVerifyEmailConfirmInput,
    UserVerifyEmailRequestInput,
)
from src.utils.key_generator import key_generator
from src.utils.sanitizers import basic, custom
from src.utils.sanitizers.spec import SpecError

pytestmark = [pytest.mark.unit]


class TestUserVerificationOpsController:
    # ================================================================
    # UserVerificationOpsController.email_confirmation_request() tests
    # ================================================================

    async def test_email_confirmation_request_invalid_input(
        self,
        user_verification_ops_controller: UserVerificationOpsController,
        svcs_container: Container,
    ) -> None:
        """
        Ensure that when the operation is called with an invalid email,
        a SpecError is raised with all the invalid results.

        Args:
            user_verification_ops_controller (UserVerificationOpsController):
                fixture providing controller to test.
            svcs_container (Container): service locator with mock services.
        """
        # Retrieve dependencies
        user_sanitizer = await svcs_container.aget(UserSanitizer)
        email_emitter = await svcs_container.aget_abstract(AbstractEmailEmitter)

        # Fails email sanitization.
        invalid_email = "a"

        input_data = UserVerifyEmailRequestInput(email_address=invalid_email)

        with pytest.raises(SpecError) as error:
            await user_verification_ops_controller.email_confirmation_request(
                data=input_data,
                user_sanitizer=user_sanitizer,
                email_emitter=email_emitter,
            )

        error_message = error.value.args[0]

        assert error_message["email_address"][custom.EmailSpec.name] is not None

    async def test_email_confirmation_request_user_not_found(
        self,
        user_verification_ops_controller: UserVerificationOpsController,
        svcs_container: Container,
    ) -> None:
        """
        Ensure that when the operation is called with an email that does
        not match an existing user, the EntityNotFound exception is raised.

        Args:
            user_verification_ops_controller (UserVerificationOpsController):
                fixture providing controller to test.
            svcs_container (Container): service locator with mock services.
        """
        # Retrieve dependencies
        user_sanitizer = await svcs_container.aget(UserSanitizer)
        email_emitter = await svcs_container.aget_abstract(AbstractEmailEmitter)

        nonexistant_valid_email = "nonexistant_email@gmail.com"

        input_data = UserVerifyEmailRequestInput(email_address=nonexistant_valid_email)

        with pytest.raises(ops_exceptions.EntityNotFound):
            await user_verification_ops_controller.email_confirmation_request(
                data=input_data,
                user_sanitizer=user_sanitizer,
                email_emitter=email_emitter,
            )

    async def test_email_confirmation_request_success(
        self,
        user_verification_ops_controller: UserVerificationOpsController,
        svcs_container: Container,
    ) -> None:
        """
        Ensure that the operation creates a new email confirmation object
        on the user's email.

        Args:
            user_verification_ops_controller (UserVerificationOpsController):
                fixture providing controller to test.
            svcs_container (Container): service locator with mock services.
        """
        # Retrieve dependencies
        user_sanitizer = await svcs_container.aget(UserSanitizer)
        email_emitter = await svcs_container.aget_abstract(AbstractEmailEmitter)

        existing_valid_email = "existing_email@gmail.com"

        # Add existing user
        existing_user = User(username="existing_username")
        existing_user.email_create(address=existing_valid_email, max_emails=1)
        existing_user.emails[0] = existing_user.emails[0].transform(
            verified=False, confirmation=None
        )
        await user_verification_ops_controller.user_repo.add(user=existing_user)

        input_data = UserVerifyEmailRequestInput(email_address=existing_valid_email)

        await user_verification_ops_controller.email_confirmation_request(
            data=input_data,
            user_sanitizer=user_sanitizer,
            email_emitter=email_emitter,
        )

        persisted_user = (
            await user_verification_ops_controller.user_repo.get_user_by_email_address(
                email_address=existing_valid_email
            )
        )

        assert persisted_user.emails[0].confirmation is not None

    # ================================================================
    # UserVerificationOpsController.email_confirmation_confirm() tests
    # ================================================================

    async def test_email_confirmation_confirm_invalid_input(
        self,
        user_verification_ops_controller: UserVerificationOpsController,
        svcs_container: Container,
    ) -> None:
        """
        Ensure that when the operation is called with an invalid key,
        a SpecError is raised with all the invalid results.

        Args:
            user_verification_ops_controller (UserVerificationOpsController):
                fixture providing controller to test.
            svcs_container (Container): service locator with mock services.
        """
        # Retrieve dependencies
        user_sanitizer = await svcs_container.aget(UserSanitizer)

        # Fails length sanitization.
        invalid_key = "a"

        input_data = UserVerifyEmailConfirmInput(key=invalid_key)

        with pytest.raises(SpecError) as error:
            await user_verification_ops_controller.email_confirmation_confirm(
                data=input_data,
                user_sanitizer=user_sanitizer,
            )

        error_message = error.value.args[0]

        assert error_message["confirmation_key"][basic.LengthSpec.name] is not None

    async def test_email_confirmation_confirm_user_not_found(
        self,
        user_verification_ops_controller: UserVerificationOpsController,
        svcs_container: Container,
    ) -> None:
        """
        Ensure that when the operation is called with a confirmation key that does
        not match an existing user, the EntityNotFound exception is raised.

        Args:
            user_verification_ops_controller (UserVerificationOpsController):
                fixture providing controller to test.
            svcs_container (Container): service locator with mock services.
        """
        # Retrieve dependencies
        user_sanitizer = await svcs_container.aget(UserSanitizer)

        nonexistant_valid_key = key_generator(
            length=settings.VERIFICATION_KEY_MAX_LENGTH
        )

        input_data = UserVerifyEmailConfirmInput(key=nonexistant_valid_key)

        with pytest.raises(ops_exceptions.EntityNotFound):
            await user_verification_ops_controller.email_confirmation_confirm(
                data=input_data,
                user_sanitizer=user_sanitizer,
            )

    async def test_email_confirmation_confirm_success(
        self,
        user_verification_ops_controller: UserVerificationOpsController,
        svcs_container: Container,
    ) -> None:
        """
        Ensure that the operation confirms and closes an existing
        email confirmation object on the user's email and verifies it.

        Args:
            user_verification_ops_controller (UserVerificationOpsController):
                fixture providing controller to test.
            svcs_container (Container): service locator with mock services.
        """
        # Retrieve dependencies
        user_sanitizer = await svcs_container.aget(UserSanitizer)

        existing_valid_email = "existing_email@gmail.com"
        existing_valid_key = key_generator(length=settings.VERIFICATION_KEY_MAX_LENGTH)

        # Add existing user
        existing_user = User(username="existing_username")
        existing_user.email_create(address=existing_valid_email, max_emails=1)
        existing_user.emails[0] = existing_user.emails[0].transform(
            verified=False,
            confirmation=EmailConfirmation(key=existing_valid_key),
        )
        await user_verification_ops_controller.user_repo.add(user=existing_user)

        input_data = UserVerifyEmailConfirmInput(key=existing_valid_key)

        await user_verification_ops_controller.email_confirmation_confirm(
            data=input_data,
            user_sanitizer=user_sanitizer,
        )

        persisted_user = (
            await user_verification_ops_controller.user_repo.get_user_by_email_address(
                email_address=existing_valid_email
            )
        )

        assert (
            persisted_user.emails[0].confirmation is None
            and persisted_user.emails[0].verified is True
        )

    # ================================================================
    # UserVerificationOpsController.password_reset_request() tests
    # ================================================================

    async def test_password_reset_request_invalid_input(
        self,
        user_verification_ops_controller: UserVerificationOpsController,
        svcs_container: Container,
    ) -> None:
        """
        Ensure that when the operation is called with an invalid email,
        a SpecError is raised with all the invalid results.

        Args:
            user_verification_ops_controller (UserVerificationOpsController):
                fixture providing controller to test.
            svcs_container (Container): service locator with mock services.
        """
        # Retrieve dependencies
        user_sanitizer = await svcs_container.aget(UserSanitizer)
        email_emitter = await svcs_container.aget_abstract(AbstractEmailEmitter)

        # Fails email sanitization.
        invalid_email = "a"

        input_data = UserPasswordResetRequestInput(email_address=invalid_email)

        with pytest.raises(SpecError) as error:
            await user_verification_ops_controller.password_reset_request(
                data=input_data,
                user_sanitizer=user_sanitizer,
                email_emitter=email_emitter,
            )

        error_message = error.value.args[0]

        assert error_message["email_address"][custom.EmailSpec.name] is not None

    async def test_password_reset_request_user_not_found(
        self,
        user_verification_ops_controller: UserVerificationOpsController,
        svcs_container: Container,
    ) -> None:
        """
        Ensure that when the operation is called with an email that does
        not match an existing user, the EntityNotFound exception is raised.

        Args:
            user_verification_ops_controller (UserVerificationOpsController):
                fixture providing controller to test.
            svcs_container (Container): service locator with mock services.
        """
        # Retrieve dependencies
        user_sanitizer = await svcs_container.aget(UserSanitizer)
        email_emitter = await svcs_container.aget_abstract(AbstractEmailEmitter)

        nonexistant_valid_email = "nonexistant_email@gmail.com"

        input_data = UserPasswordResetRequestInput(
            email_address=nonexistant_valid_email
        )

        with pytest.raises(ops_exceptions.EntityNotFound):
            await user_verification_ops_controller.password_reset_request(
                data=input_data,
                user_sanitizer=user_sanitizer,
                email_emitter=email_emitter,
            )

    async def test_password_reset_request_success(
        self,
        user_verification_ops_controller: UserVerificationOpsController,
        svcs_container: Container,
    ) -> None:
        """
        Ensure that the operation creates a new password reset confirmation
        object on the user.

        Args:
            user_verification_ops_controller (UserVerificationOpsController):
                fixture providing controller to test.
            svcs_container (Container): service locator with mock services.
        """
        # Retrieve dependencies
        user_sanitizer = await svcs_container.aget(UserSanitizer)
        email_emitter = await svcs_container.aget_abstract(AbstractEmailEmitter)

        existing_valid_email = "existing_email@gmail.com"

        # Add existing user
        existing_user = User(username="existing_username")
        existing_user.email_create(address=existing_valid_email, max_emails=1)
        await user_verification_ops_controller.user_repo.add(user=existing_user)

        input_data = UserPasswordResetRequestInput(email_address=existing_valid_email)

        await user_verification_ops_controller.password_reset_request(
            data=input_data,
            user_sanitizer=user_sanitizer,
            email_emitter=email_emitter,
        )

        persisted_user = (
            await user_verification_ops_controller.user_repo.get_user_by_email_address(
                email_address=existing_valid_email
            )
        )

        assert persisted_user.password_reset_confirmation is not None

    # ================================================================
    # UserVerificationOpsController.password_reset_confirm() tests
    # ================================================================

    async def test_password_reset_confirm_invalid_input(
        self,
        user_verification_ops_controller: UserVerificationOpsController,
        svcs_container: Container,
    ) -> None:
        """
        Ensure that when the operation is called with an invalid key and passwords,
        a SpecError is raised with all the invalid results.

        Args:
            user_verification_ops_controller (UserVerificationOpsController):
                fixture providing controller to test.
            svcs_container (Container): service locator with mock services.
        """
        # Retrieve dependencies
        user_sanitizer = await svcs_container.aget(UserSanitizer)
        password_crypt = await svcs_container.aget_abstract(AbstractPasswordCrypt)

        # Fails length sanitization.
        invalid_key = "a"

        # Fails length and regex sanitization.
        invalid_password = "a"

        input_data = UserPasswordResetConfirmInput(
            user_id=0,
            key=invalid_key,
            new_password1=invalid_password,
            new_password2=invalid_password,
        )

        with pytest.raises(SpecError) as error:
            await user_verification_ops_controller.password_reset_confirm(
                data=input_data,
                user_sanitizer=user_sanitizer,
                password_crypt=password_crypt,
            )

        error_message = error.value.args[0]

        assert error_message["confirmation_key"][basic.LengthSpec.name] is not None

        assert (
            error_message["password"][basic.LengthSpec.name] is not None
            and error_message["password"][basic.RegexSpec.name] is not None
        )

    async def test_password_reset_confirm_password_mismatch(
        self,
        user_verification_ops_controller: UserVerificationOpsController,
        svcs_container: Container,
    ) -> None:
        """
        Ensure that when the operation is called with passwords that,
        do not match, a SpecError is raised.

        Args:
            user_verification_ops_controller (UserVerificationOpsController):
                fixture providing controller to test.
            svcs_container (Container): service locator with mock services.
        """
        # Retrieve dependencies
        user_sanitizer = await svcs_container.aget(UserSanitizer)
        password_crypt = await svcs_container.aget_abstract(AbstractPasswordCrypt)

        existing_valid_key = key_generator(length=settings.VERIFICATION_KEY_MAX_LENGTH)

        # Fails password match.
        new_password1 = "New_password12"
        new_password2 = "New_password13"

        input_data = UserPasswordResetConfirmInput(
            user_id=0,
            key=existing_valid_key,
            new_password1=new_password1,
            new_password2=new_password2,
        )

        with pytest.raises(SpecError) as error:
            await user_verification_ops_controller.password_reset_confirm(
                data=input_data,
                user_sanitizer=user_sanitizer,
                password_crypt=password_crypt,
            )

        error_message = error.value.args[0]

        assert error_message["MultiFieldError"] is not None

    async def test_password_reset_confirm_user_not_found(
        self,
        user_verification_ops_controller: UserVerificationOpsController,
        svcs_container: Container,
    ) -> None:
        """
        Ensure that when the operation is called with a confirmation key that does
        not match an existing user, the EntityNotFound exception is raised.

        Args:
            user_verification_ops_controller (UserVerificationOpsController):
                fixture providing controller to test.
            svcs_container (Container): service locator with mock services.
        """
        # Retrieve dependencies
        user_sanitizer = await svcs_container.aget(UserSanitizer)
        password_crypt = await svcs_container.aget_abstract(AbstractPasswordCrypt)

        nonexistant_valid_key = key_generator(
            length=settings.VERIFICATION_KEY_MAX_LENGTH
        )

        input_data = UserPasswordResetConfirmInput(
            user_id=0,
            key=nonexistant_valid_key,
            new_password1="New_password12",
            new_password2="New_password12",
        )

        with pytest.raises(ops_exceptions.EntityNotFound):
            await user_verification_ops_controller.password_reset_confirm(
                data=input_data,
                user_sanitizer=user_sanitizer,
                password_crypt=password_crypt,
            )

    async def test_password_reset_confirm_success(
        self,
        user_verification_ops_controller: UserVerificationOpsController,
        svcs_container: Container,
    ) -> None:
        """
        Ensure that the operation confirms and closes an existing
        password reset confirmation on the user email and overwrites the password.

        Args:
            user_verification_ops_controller (UserVerificationOpsController):
                fixture providing controller to test.
            svcs_container (Container): service locator with mock services.
        """
        # Retrieve dependencies
        user_sanitizer = await svcs_container.aget(UserSanitizer)
        password_crypt = await svcs_container.aget_abstract(AbstractPasswordCrypt)

        existing_valid_email = "existing_email@gmail.com"
        existing_valid_key = key_generator(length=settings.VERIFICATION_KEY_MAX_LENGTH)
        new_password = "New_password12"

        # Add existing user
        existing_user = User(username="existing_username")
        existing_user._password_hash = None
        existing_user.email_create(address=existing_valid_email, max_emails=1)
        existing_user.password_reset_create(key=existing_valid_key)
        existing_user = await user_verification_ops_controller.user_repo.add(
            user=existing_user
        )

        input_data = UserPasswordResetConfirmInput(
            user_id=existing_user.id_or_error(),
            key=existing_valid_key,
            new_password1=new_password,
            new_password2=new_password,
        )

        await user_verification_ops_controller.password_reset_confirm(
            data=input_data,
            user_sanitizer=user_sanitizer,
            password_crypt=password_crypt,
        )

        persisted_user = (
            await user_verification_ops_controller.user_repo.get_user_by_email_address(
                email_address=existing_valid_email
            )
        )

        assert (
            persisted_user.password_reset_confirmation is None
            and persisted_user._password_hash is not None
        )
