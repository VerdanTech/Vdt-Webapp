# External Libraries
import pytest
from pytest_mock import MockerFixture

# VerdanTech Source
from src.domain.user.entities import User
from src.domain.user.services import email as email_services
from src.interfaces.email.emitter import AbstractEmailEmitter
from src.interfaces.persistence.user import AbstractUserRepository

pytestmark = [pytest.mark.unit]

# ======================================
# email_services.email_create() tests
# ======================================


async def test_email_create_verification_false_success(
    user: User, mocker: MockerFixture
) -> None:
    """
    Ensure that the user's email_create method is called with verification=False,
    the correct email address and max_emails, and email confirmation key as None.

    Args:
        user (User): user factory fixture.
        mocker (MockerFixture): pytest-mock.
    """
    email_address = "new_email@test.com"
    max_emails = 3
    mock_user_email_create = mocker.patch.object(user, "email_create")

    await email_services.email_create(
        user=user, address=email_address, max_emails=max_emails
    )

    mock_user_email_create.assert_called_once_with(
        address=email_address,
        max_emails=max_emails,
        verification=False,
        email_confirmation_key=None,
    )


async def test_email_create_verification_true_value_error(user: User) -> None:
    """
    Ensure that when verification=True but no user_repo, key_length, or email_emitter
    is passed, a ValueError is raised.

    Args:
        user (User): user factory fixture
    """

    with pytest.raises(ValueError):
        await email_services.email_create(
            user=user, address="", max_emails=0, verification=True
        )


async def test_email_create_verification_true_success(
    user: User, mock_user_repo: AbstractUserRepository, mocker: MockerFixture
) -> None:
    """
    Ensure that when verification=True, a unique email confirmation key is generated,
    the user's email_create method is called, and the email emitter is called.

    Args:
        user (User): _description_
        mock_user_repo (AbstractUserRepository): _description_
        mocker (MockerFixture): _description_
    """
    email_address = "new_email@test.com"
    max_emails = 3
    key_length = 10
    generated_key = "abc"
    mock_generate_unique_email_confirmation_key = mocker.patch(
        "src.domain.user.services.email.verification_services.generate_unique_email_confirmation_key",
        return_value=generated_key,
    )
    mock_user_email_create = mocker.patch.object(user, "email_create")
    mock_email_emitter = mocker.Mock(spec=AbstractEmailEmitter)

    await email_services.email_create(
        user=user,
        address=email_address,
        max_emails=max_emails,
        verification=True,
        key_length=key_length,
        user_repo=mock_user_repo,
        email_emitter=mock_email_emitter,
    )

    mock_generate_unique_email_confirmation_key.assert_awaited_once_with(
        length=key_length, user_repo=mock_user_repo
    )
    mock_user_email_create.assert_called_once_with(
        address=email_address,
        max_emails=max_emails,
        verification=True,
        email_confirmation_key=generated_key,
    )
    mock_email_emitter.emit_user_email_confirmation.assert_called_once_with(
        email_address=email_address, username=user.username, key=generated_key
    )
