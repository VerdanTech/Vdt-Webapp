from typing import ContextManager

import pytest
from pytest_mock import MockerFixture
from src.verdantech_api.application.user.operations.verification import (
    UserVerificationOperations,
)
from src.verdantech_api.application.user.schemas.api.verification import (
    UserPasswordResetConfirmInput,
    UserPasswordResetRequestInput,
    UserVerifyEmailConfirmInput,
    UserVerifyEmailRequestInput,
)
from src.verdantech_api.domain.models.user.entities import User
from src.verdantech_api.domain.models.user.exceptions import (
    EmailConfirmationKeyNotFound,
    PasswordResetConfirmationNotFound,
    UserNotFound,
)
from src.verdantech_api.domain.models.user.values import (
    Email,
    EmailConfirmation,
    PasswordResetConfirmation,
)
from src.verdantech_api.domain.utils.sanitizers.object import ObjectSanitizer


class TestUserVerificationOperations:
    @pytest.mark.parametrize(
        (
            "existing_user",
            "existing_email",
            "email_to_search",
            "email_with_new_confirmation",
            "expected_error_context",
        ),
        [
            # Test case: user exists with the email searched,
            # no error is raised
            (
                User(
                    username="test",
                ),
                Email(
                    address="test@test.com",
                ),
                "test@test.com",
                Email(
                    address="test@test.com", confirmation=EmailConfirmation(key="abc")
                ),
                None,
            ),
            # Test case: no user exists with the email searched,
            # the proper error is raised
            (None, None, "test@test.com", None, UserNotFound),
        ],
        indirect=["expected_error_context"],
    )
    async def test_email_verification_request(
        self,
        existing_user: User | None,
        existing_email: Email | None,
        email_to_search: str,
        email_with_new_confirmation: Email | None,
        expected_error_context: ContextManager,
        mock_object_sanitizer: ObjectSanitizer,
        user_verification_operations: UserVerificationOperations,
        mocker: MockerFixture,
    ):
        """Ensure that the proper sanitization method is called,
            the user is searched for in the repository and the proper
            error is called if they aren't found, the new email
            verification method is called, and the user is re-persisted

        Args:
            existing_user (User | None): user pre-populate repository with
            existing_email (Email | None): email to pre-populate existing user with
            email_to_search (str): email to search for in test
            email_with_new_confirmation (Email): mock side effect of
                calling the new email verification application service
            expected_error_context (ContextManager): An instance of nullcontext() if
                expected_error_context = None and pytest.raises(expected_error_context)
                otherwise See: tests/conftest.py
            mock_object_sanitizer (ObjectSanitizer): fixture providing mock
                object sanitizer
            user_verification_operations (UserVerificationOperations): fixture
                providing verification operations to test on
            mocker (MockerFixture): pytest-mock
        """
        input_data = UserVerifyEmailRequestInput(email_address="test@test.com")
        if existing_user is not None:
            existing_user.emails = [existing_email]

            # Add the side effect to make the mocked function have the
            # intended effect on the user object in the repository
            mock_new_email_verification = mocker.patch(
                "src.verdantech_api.application.user.operations.verification.new_email_verification",
                side_effect=lambda user, address, key_length, user_repo, email_emitter: setattr(
                    existing_user, "emails", [email_with_new_confirmation]
                ),
            )
            existing_user = await user_verification_operations.user_repo.add(
                existing_user
            )
        mock_sanitize_verify_email_request = mocker.patch(
            "src.verdantech_api.application.user.operations.verification.sanitize_verify_email_request",
            return_value={"email_address": input_data.email_address},
        )
        mock_email_emitter = mocker.Mock()
        mock_key_length = mocker.patch(
            "src.verdantech_api.application.user.operations.verification.settings.EMAIL_VERIFICATION_KEY_LENGTH"
        )

        with expected_error_context as error:
            await user_verification_operations.email_verification_request(
                data=input_data,
                user_sanitizer=mock_object_sanitizer,
                email_emitter=mock_email_emitter,
            )

            mock_sanitize_verify_email_request.assert_awaited_once_with(
                data=input_data, user_sanitizer=mock_object_sanitizer
            )

            if error is None:
                mock_new_email_verification.assert_awaited_once_with(
                    user=existing_user,
                    address=input_data.email_address,
                    key_length=mock_key_length,
                    user_repo=user_verification_operations.user_repo,
                    email_emitter=mock_email_emitter,
                )
                assert (
                    user_verification_operations.user_repo.collection[0]
                    .emails[0]
                    .confirmation
                    is not None
                )

    @pytest.mark.parametrize(
        (
            "existing_user",
            "existing_email",
            "key_to_search",
            "verified_email",
            "expected_error_context",
        ),
        [
            # Test case: user exists with the confirmation key, no error is raised
            (
                User(
                    username="test",
                ),
                Email(
                    address="test@test.com",
                    verified=False,
                    confirmation=EmailConfirmation(key="abc"),
                ),
                "abc",
                Email(address="test@test.com", verified=True),
                None,
            ),
            # Test case: no user exists with the key, the proper error is raised
            (None, None, "abc", None, EmailConfirmationKeyNotFound),
        ],
        indirect=["expected_error_context"],
    )
    async def test_email_verification_confirm(
        self,
        existing_user: User | None,
        existing_email: Email | None,
        key_to_search: str,
        verified_email: Email | None,
        expected_error_context: ContextManager,
        user_verification_operations: UserVerificationOperations,
        mocker: MockerFixture,
    ):
        """Ensure the proper domain functions are called, the user
            is re-persisted into the repository, and the proper
            error is raised if no matching email confirmation is found

        Args:
            existing_user (User | None): user pre-populate repository with
            existing_email (Email | None): email to pre-populate existing user with
            key_to_search (str): email confirmation key to search for in test
            verified_email (Email | None): email to replace unverified email upon
                verification through domain function
            expected_error_context (ContextManager): An instance of nullcontext() if
                expected_error_context = None and pytest.raises(expected_error_context)
                otherwise See: tests/conftest.py
            user_verification_operations (UserVerificationOperations): fixture
                providing class in question to test on
            mocker (MockerFixture): pytest-mock
        """
        input_data = UserVerifyEmailConfirmInput(key="abc")
        if existing_user is not None:
            existing_user.emails = [existing_email]

            # Add the side effect to make the mocked function have the
            # intended effect on the user object in the repository
            mock_verify_email = mocker.patch.object(
                existing_user,
                "verify_email",
                side_effect=lambda key: setattr(
                    existing_user, "emails", [verified_email]
                ),
            )
            existing_user = await user_verification_operations.user_repo.add(
                existing_user
            )

        with expected_error_context as error:
            await user_verification_operations.email_verification_confirm(
                data=input_data
            )

            if error is None:
                mock_verify_email.assert_called_once_with(key="abc")
                assert (
                    user_verification_operations.user_repo.collection[0]
                    .emails[0]
                    .verified
                    is True
                )

    @pytest.mark.parametrize(
        (
            "existing_user",
            "existing_email",
            "email_to_search",
            "new_reset_confirmation",
            "expected_error_context",
        ),
        [
            # Test case: user exists with the email searched,
            # no error is raised
            (
                User(
                    username="test",
                ),
                Email(
                    address="test@test.com",
                ),
                "test@test.com",
                PasswordResetConfirmation(key="abc"),
                None,
            ),
            # Test case: no user exists with the email searched,
            # the proper error is raised
            (None, None, "test@test.com", None, UserNotFound),
        ],
        indirect=["expected_error_context"],
    )
    async def test_password_reset_request(
        self,
        existing_user: User | None,
        existing_email: Email | None,
        email_to_search: str,
        new_reset_confirmation: PasswordResetConfirmation | None,
        expected_error_context: ContextManager,
        mock_object_sanitizer: ObjectSanitizer,
        user_verification_operations: UserVerificationOperations,
        mocker: MockerFixture,
    ):
        """Ensure that the proper sanitization method is called,
            the user is searched for in the repository and the proper
            error is called if they aren't found, the new password reset
            method is called, and the user is re-persisted

        Args:
            existing_user (User | None): user pre-populate repository with
            existing_email (Email | None): email to pre-populate existing user with
            email_to_search (str): email to search for in test
            new_reset_confirmation (PasswordResetConfirmation): mock side effect of
                calling the new password reset application service
            expected_error_context (ContextManager): An instance of nullcontext() if
                expected_error_context = None and pytest.raises(expected_error_context)
                otherwise See: tests/conftest.py
            mock_object_sanitizer (ObjectSanitizer): fixture providing mock
                object sanitizer
            user_verification_operations (UserVerificationOperations): fixture
                providing verification operations to test on
            mocker (MockerFixture): pytest-mock
        """
        input_data = UserPasswordResetRequestInput(email_address="test@test.com")
        if existing_user is not None:
            existing_user.emails = [existing_email]

            # Add the side effect to make the mocked function have the
            # intended effect on the user object in the repository
            mock_new_password_reset = mocker.patch(
                "src.verdantech_api.application.user.operations.verification.new_password_reset",
                side_effect=lambda user, address, key_length, user_repo, email_emitter: setattr(
                    existing_user, "password_reset_confirmation", new_reset_confirmation
                ),
            )
            existing_user = await user_verification_operations.user_repo.add(
                existing_user
            )
        mock_sanitize_password_reset_request = mocker.patch(
            "src.verdantech_api.application.user.operations.verification.sanitize_password_reset_request",
            return_value={"email_address": input_data.email_address},
        )
        mock_email_emitter = mocker.Mock()
        mock_key_length = mocker.patch(
            "src.verdantech_api.application.user.operations.verification.settings.EMAIL_VERIFICATION_KEY_LENGTH"
        )

        with expected_error_context as error:
            await user_verification_operations.password_reset_request(
                data=input_data,
                user_sanitizer=mock_object_sanitizer,
                email_emitter=mock_email_emitter,
            )

            mock_sanitize_password_reset_request.assert_awaited_once_with(
                data=input_data, user_sanitizer=mock_object_sanitizer
            )

            if error is None:
                mock_new_password_reset.assert_awaited_once_with(
                    user=existing_user,
                    address=input_data.email_address,
                    key_length=mock_key_length,
                    user_repo=user_verification_operations.user_repo,
                    email_emitter=mock_email_emitter,
                )
                assert (
                    user_verification_operations.user_repo.collection[
                        0
                    ].password_reset_confirmation
                    is not None
                )

    @pytest.mark.parametrize(
        (
            "existing_user",
            "existing_password_reset_confirmation",
            "key_to_search",
            "expected_error_context",
        ),
        [
            (User(username="test"), PasswordResetConfirmation(key="abc"), "abc", None),
            (None, None, "abc", PasswordResetConfirmationNotFound),
        ],
        indirect=["expected_error_context"],
    )
    async def test_password_reset_confirm(
        self,
        existing_user: User | None,
        existing_password_reset_confirmation: PasswordResetConfirmation | None,
        key_to_search: str,
        expected_error_context: ContextManager,
        user_verification_operations: UserVerificationOperations,
        mock_object_sanitizer: ObjectSanitizer,
        mocker: MockerFixture,
    ) -> None:
        """Ensure the proper sanitization method is awaited, the user is
            retrieved from the repository else the proper error is raised,
            the application service is called and the user re-persisted

        Args:
            existing_user (User | None): user to pre-populate repository with
            existing_password_reset_confirmation (PasswordResetConfirmation | None):
                password reset confirmation to pre-populate user with
            key_to_search (str): the confirmation key to attempt a search for
            expected_error_context (ContextManager): An instance of nullcontext() if
                expected_error_context = None and pytest.raises(expected_error_context)
                otherwise See: tests/conftest.py
            user_verification_operations (UserVerificationOperations): fixture
                providing application service to test on
            mock_object_sanitizer (ObjectSanitizer): mock user sanitizer
            mocker (MockerFixture): pytest-mock
        """
        mock_password_crypt = mocker.Mock()
        if existing_user is not None:
            existing_user.password_reset_confirmation = (
                existing_password_reset_confirmation
            )

            # Add the side effect to make the mocked function have the
            # intended effect on the user object in the repository
            mock_close_password_reset = mocker.patch(
                "src.verdantech_api.application.user.operations.verification.close_password_reset",
                side_effect=lambda user, old_password, new_password, password_crypt: setattr(
                    existing_user, "password_reset_confirmation", None
                ),
            )
            existing_user = await user_verification_operations.user_repo.add(
                existing_user
            )
        input_data = UserPasswordResetConfirmInput(
            user_id=(existing_user.id if existing_user is not None else "abc"),
            key=key_to_search,
            old_password="old_password",
            new_password1="new_password",
            new_password2="new_password",
        )
        mock_sanitize_password_reset_confirm = mocker.patch(
            "src.verdantech_api.application.user.operations.verification.sanitize_password_reset_confirm",
            return_value={"password": input_data.new_password1},
        )

        with expected_error_context as error:
            await user_verification_operations.password_reset_confirm(
                data=input_data,
                user_sanitizer=mock_object_sanitizer,
                password_crypt=mock_password_crypt,
            )
            mock_sanitize_password_reset_confirm.assert_awaited_once_with(
                data=input_data, user_sanitizer=mock_object_sanitizer
            )

            if error is None:
                mock_close_password_reset.assert_called_once_with(
                    user=existing_user,
                    old_password=input_data.old_password,
                    new_password=input_data.new_password1,
                    password_crypt=mock_password_crypt,
                )
                assert (
                    user_verification_operations.user_repo.collection[
                        0
                    ].password_reset_confirmation
                    is None
                )
