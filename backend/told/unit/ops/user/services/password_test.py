from typing import ContextManager

import pytest
from pytest_mock import MockerFixture
from src.domain.user.entities import User
from src.domain.user.exceptions import UserNotAuthenticated
from src.ops.user.services import verification as verification_services

pytestmark = [pytest.mark.unit]


@pytest.mark.skip
async def test_password_reset_create(mocker: MockerFixture) -> None:
    """Ensure that the domain service and email emitter
        are called with the proper arguments

    Args:
        mocker (MockerFixture): pytest-mock
    """
    generated_key = "abc"
    mock_new_password_reset = mocker.patch(
        "src.ops.user.services.password.reset.PasswordResetService.new_password_reset",
        return_value=generated_key,
    )
    mock_emit_password_reset_email = mocker.patch(
        "src.ops.user.services.password.reset.emit_password_reset_email"
    )
    mock_user = mocker.MagicMock()
    mock_user.username = "username"
    mock_user.id = "test_id"
    address = "test@test.com"
    key_length = 0
    mock_user_repo = mocker.Mock()
    mock_email_emitter = mocker.Mock()

    await verification_services.password_reset_create(
        user=mock_user,
        email_address=address,
        key_length=key_length,
        user_repo=mock_user_repo,
        email_emitter=mock_email_emitter,
    )

    mock_new_password_reset.assert_awaited_once_with(
        user=mock_user, address=address, key_length=key_length, user_repo=mock_user_repo
    )
    mock_emit_password_reset_email.assert_awaited_once_with(
        email_address=address,
        username=mock_user.username,
        user_id=mock_user.id,
        key=generated_key,
        email_emitter=mock_email_emitter,
    )


@pytest.mark.skip
@pytest.mark.parametrize(
    ("verify_password_result", "expected_error_context"),
    [(True, None), (False, UserNotAuthenticated)],
    indirect=["expected_error_context"],
)
async def test_password_reset_confirm(
    verify_password_result: bool,
    expected_error_context: ContextManager,
    mocker: MockerFixture,
) -> None:
    """Ensure that the user authentication and reset password
        domain services are called, and the proper exception is raised
        upon validation failure

    Args:
        verify_password_result (bool): mock result of password authentication
        expected_error_context (ContextManager): An instance of nullcontext() if
            expected_error_context = None and pytest.raises(expected_error_context)
            otherwise See: tests/conftest.py
        mocker (MockerFixture): pytest-mock
    """
    old_password = "old_password"
    new_password = "new_password"
    mock_password_crypt = mocker.Mock()
    mock_user = mocker.MagicMock(spec=User)
    mock_user.verify_password.return_value = verify_password_result

    with expected_error_context as error:
        await verification_services.password_reset_confirm(
            user=mock_user,
            old_password=old_password,
            new_password=new_password,
            password_crypt=mock_password_crypt,
        )
        mock_user.verify_password.assert_awaited_once_with(
            password=old_password, password_crypt=mock_password_crypt
        )

        if error is None:
            mock_user.reset_password.assert_awaited_once_with(
                new_password=new_password, password_crypt=mock_password_crypt
            )
