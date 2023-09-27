from pytest_mock import MockerFixture
from src.verdantech_api.application.user.schemas.api.verification import (
    UserPasswordResetConfirmInput,
    UserPasswordResetRequestInput,
    UserVerifyEmailRequestInput,
)
from src.verdantech_api.application.user.schemas.api.write import UserCreateInput
from src.verdantech_api.application.user.services.sanitization.inputs import (
    sanitize_password_reset_confirm,
    sanitize_password_reset_request,
    sanitize_user_create,
    sanitize_verify_email_request,
)
from src.verdantech_api.domain.utils.sanitizers.object import MockObjectSanitizer


async def test_sanitize_user_create(
    mock_object_sanitizer: MockObjectSanitizer, mocker: MockerFixture
) -> None:
    """Ensure the all fields sanitizer with password match method is called,
        and the sanitized data is returned

    Args:
        mock_object_sanitizer (MockObjectSanitizer): fixture providing
            a mock object sanitizer for testing
        mocker (MockerFixture): pytest-mock
    """
    input_data = UserCreateInput(
        username="TestUsername",
        email_address="test@test.com",
        password1="test_password",
        password2="test_password",
    )
    expected_output = {
        "username": input_data.username,
        "email_address": input_data.email_address,
        "password": input_data.password1,
    }
    mock_sanitize_all_fields_pasword_match = mocker.patch(
        "src.verdantech_api.application.user.services.sanitization.inputs.sanitize_all_fields_password_match",
        return_value=expected_output,
    )

    sanitized_data = await sanitize_user_create(
        data=input_data, user_sanitizer=mock_object_sanitizer
    )

    assert sanitized_data == expected_output
    mock_sanitize_all_fields_pasword_match.assert_awaited_once_with(
        username=input_data.username,
        email_address=input_data.email_address,
        password1=input_data.password1,
        password2=input_data.password1,
        user_sanitizer=mock_object_sanitizer,
    )


async def test_sanitize_verify_email_request(
    mock_object_sanitizer: MockObjectSanitizer, mocker: MockerFixture
) -> None:
    """Ensure the email only sanitization function is called, and
        the sanitization data returned

    Args:
        mock_object_sanitizer (MockObjectSanitizer): fixture providing
            a mock object sanitizer for testing
        mocker (MockerFixture): pytest-mock
    """
    input_data = UserVerifyEmailRequestInput(email_address="test@test.com")
    expected_output = {"email_address": input_data.email_address}
    mock_sanitize_all_fields_pasword_match = mocker.patch(
        "src.verdantech_api.application.user.services.sanitization.inputs.sanitize_only_email",
        return_value=expected_output,
    )

    sanitized_data = await sanitize_verify_email_request(
        data=input_data, user_sanitizer=mock_object_sanitizer
    )

    assert sanitized_data == expected_output
    mock_sanitize_all_fields_pasword_match.assert_awaited_once_with(
        email_address=input_data.email_address, user_sanitizer=mock_object_sanitizer
    )


async def test_sanitize_password_reset_request(
    mock_object_sanitizer: MockObjectSanitizer, mocker: MockerFixture
) -> None:
    """Ensure the email only sanitization function is called,
        and the sanitized data is returned

    Args:
        mock_object_sanitizer (MockObjectSanitizer): fixture providing
            a mock object sanitizer for testing
        mocker (MockerFixture): pytest-mock
    """
    input_data = UserPasswordResetRequestInput(email_address="test@test.com")
    expected_output = {"email_address": input_data.email_address}
    mock_sanitize_all_fields_pasword_match = mocker.patch(
        "src.verdantech_api.application.user.services.sanitization.inputs.sanitize_only_email",
        return_value=expected_output,
    )

    sanitized_data = await sanitize_password_reset_request(
        data=input_data, user_sanitizer=mock_object_sanitizer
    )

    assert sanitized_data == expected_output
    mock_sanitize_all_fields_pasword_match.assert_awaited_once_with(
        email_address=input_data.email_address, user_sanitizer=mock_object_sanitizer
    )


async def test_sanitize_password_reset_confirm(
    mock_object_sanitizer: MockObjectSanitizer, mocker: MockerFixture
) -> None:
    """Ensure the dual password sanitization method is called,
        and the sanitized data is returned

    Args:
        mock_object_sanitizer (MockObjectSanitizer): fixture providing
            a mock object sanitizer for testing
        mocker (MockerFixture): pytest-mock
    """
    input_data = UserPasswordResetConfirmInput(
        user_id="123",
        key="abc",
        old_password="old_password",
        new_password1="password",
        new_password2="password",
    )
    expected_output = {"password": "password"}
    mock_sanitize_passwords = mocker.patch(
        "src.verdantech_api.application.user.services.sanitization.inputs.sanitize_passwords",
        return_value=expected_output,
    )

    sanitized_data = await sanitize_password_reset_confirm(
        data=input_data, user_sanitizer=mock_object_sanitizer
    )

    assert sanitized_data == expected_output
    mock_sanitize_passwords.assert_awaited_once_with(
        password1=input_data.new_password1,
        password2=input_data.new_password2,
        user_sanitizer=mock_object_sanitizer,
    )
