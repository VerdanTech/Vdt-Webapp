from pytest_mock import MockerFixture
from src.application.user.services.sanitization.cases import (
    sanitize_all_fields_password_match,
    sanitize_only_email,
    sanitize_passwords,
)
from src.domain.user.services.sanitization import UserSanitizer
from src.utils.sanitizers.field import DISABLE_FIELD
from src.utils.sanitizers.object import MockObjectSanitizer
from src.utils.sanitizers.sanitization.basic import (
    BanSanitization,
    LengthSanitization,
    RegexSanitization,
)
from src.utils.sanitizers.sanitization.repo import (
    UniqueSanitization,
)


async def test_sanitize_all_fields_password_match(
    mock_object_sanitizer: MockObjectSanitizer, mocker: MockerFixture
) -> None:
    """Ensure the password matcher and object sanitizer is called
        with all fields enabled, and the sanitized data is returned

    Args:
        mock_object_sanitizer (MockObjectSanitizer): fixture providing
            a mock object sanitizer for testing
        mocker (MockerFixture): pytest-mock
    """
    username = "TestUsername"
    email_address = "test@test.com"
    password1 = "test_password"
    password2 = "test_password"
    expected_output = {
        "username": username,
        "email_address": email_address,
        "password": password1,
    }
    mock_validate_password_match = mocker.patch(
        "src.application.user.services.sanitization.cases.validate_password_match"
    )
    mock_sanitize = mocker.patch.object(
        mock_object_sanitizer,
        "sanitize",
        return_value={
            "username": username,
            "email_address": email_address,
            "password": password1,
        },
    )

    sanitized_data = await sanitize_all_fields_password_match(
        username=username,
        email_address=email_address,
        password1=password1,
        password2=password2,
        user_sanitizer=mock_object_sanitizer,
    )

    assert sanitized_data == expected_output
    mock_validate_password_match.assert_called_once_with(
        password1=password1, password2=password2
    )
    mock_sanitize.assert_awaited_once_with(
        input={
            "username": username,
            "email_address": email_address,
            "password": password1,
        },
    )


async def test_sanitize_only_email(
    mock_object_sanitizer: MockObjectSanitizer, mocker: MockerFixture
) -> None:
    """Ensure the user sanitizer is called with only the email
        field enabled, and the sanitized data is returned

    Args:
        mock_object_sanitizer (MockObjectSanitizer): fixture providing
            a mock object sanitizer for testing
        mocker (MockerFixture): pytest-mock
    """
    email_address = "test@test.com"
    expected_output = {"email_address": email_address}
    mock_sanitize = mocker.patch.object(
        mock_object_sanitizer, "sanitize", return_value={"email_address": email_address}
    )

    sanitized_data = await sanitize_only_email(
        email_address=email_address, user_sanitizer=mock_object_sanitizer
    )

    assert sanitized_data == expected_output
    mock_sanitize.assert_awaited_once_with(
        input={"email_address": email_address},
        disabled_fields={
            "username": DISABLE_FIELD,
            "password": DISABLE_FIELD,
            "email_address": [
                UniqueSanitization,
                LengthSanitization,
                UniqueSanitization,
                RegexSanitization,
            ],
        },
    )


async def test_sanitize_passwords(
    mock_object_sanitizer: MockObjectSanitizer, mocker: MockerFixture
) -> None:
    """Ensure the password matcher is called and the user sanitizer
        is called with the username and email fields disabled

    Args:
        mock_object_sanitizer (MockObjectSanitizer): fixture providing
            a mock object sanitizer for testing
        mocker (MockerFixture): pytest-mock
    """
    password1 = "test_password"
    password2 = "test_password"
    expected_output = {
        "password": password1,
    }
    mock_validate_password_match = mocker.patch(
        "src.application.user.services.sanitization.cases.validate_password_match"
    )
    mock_sanitize = mocker.patch.object(
        mock_object_sanitizer,
        "sanitize",
        return_value={
            "password": password1,
        },
    )

    sanitized_data = await sanitize_passwords(
        password1=password1,
        password2=password2,
        user_sanitizer=mock_object_sanitizer,
    )

    assert sanitized_data == expected_output
    mock_validate_password_match.assert_called_once_with(
        password1=password1, password2=password2
    )
    mock_sanitize.assert_awaited_once_with(
        input={
            "password": password1,
        },
        disabled_fields={"username": DISABLE_FIELD, "email_address": DISABLE_FIELD},
    )
