import pytest
from pytest_mock import MockerFixture
from src.application.user.services.email.addition import (
    add_first_email,
    new_email_verification,
)


@pytest.mark.parametrize(("require_email_verification"), [(True), (False)])
async def test_add_new_email(
    require_email_verification: bool, mocker: MockerFixture
) -> None:
    """Ensure the proper email addition domain services are called
        depending on the email verification setting

    Args:
        require_email_verification (bool): configured in
            app settings
        mocker (_type_): pytest-mock
    """
    mock_add_first_email_verification_required = mocker.patch(
        "src.application.user.services.email.addition.EmailAdditionService.add_first_email_verification_required",
        return_value="abc",
    )
    mock_add_first_email_verification_not_required = mocker.patch(
        "src.application.user.services.email.addition.EmailAdditionService.add_first_email_verification_not_required"
    )
    mock_emit_email_verification_email = mocker.patch(
        "src.application.user.services.email.addition.emit_email_verification_email"
    )
    mock_user = mocker.MagicMock()
    mock_user.username = "username"
    mock_user_repo = mocker.Mock()
    mock_email_emitter = mocker.Mock()

    await add_first_email(
        user=mock_user,
        email_address="email@email.com",
        require_email_verification=require_email_verification,
        verification_key_length=0,
        user_repo=mock_user_repo,
        email_emitter=mock_email_emitter,
    )

    if require_email_verification:
        mock_add_first_email_verification_required.assert_awaited_once_with(
            user=mock_user,
            address="email@email.com",
            key_length=0,
            user_repo=mock_user_repo,
        )
        mock_emit_email_verification_email.assert_awaited_once_with(
            email_address="email@email.com",
            username="username",
            key="abc",
            email_emitter=mock_email_emitter,
        )
    else:
        mock_add_first_email_verification_not_required.assert_called_once_with(
            user=mock_user, address="email@email.com"
        )


async def test_new_email_verification(mocker: MockerFixture) -> None:
    """Ensure that the domain service and email emitter
        are called with the proper arguments

    Args:
        mocker (MockerFixture): pytest-mock
    """
    generated_key = "abc"
    mock_new_verification = mocker.patch(
        "src.application.user.services.email.addition.EmailVerificationService.new_verification",
        return_value=generated_key,
    )
    mock_emit_email_verification_email = mocker.patch(
        "src.application.user.services.email.addition.emit_email_verification_email"
    )
    mock_user = mocker.MagicMock()
    mock_user.username = "username"
    address = "test@test.com"
    key_length = 0
    mock_user_repo = mocker.Mock()
    mock_email_emitter = mocker.Mock()

    await new_email_verification(
        user=mock_user,
        email_address=address,
        key_length=key_length,
        user_repo=mock_user_repo,
        email_emitter=mock_email_emitter,
    )

    mock_new_verification.assert_awaited_once_with(
        user=mock_user, address=address, key_length=key_length, user_repo=mock_user_repo
    )
    mock_emit_email_verification_email.assert_awaited_once_with(
        email_address=address,
        username=mock_user.username,
        key=generated_key,
        email_emitter=mock_email_emitter,
    )
