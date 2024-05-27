# Standard Library
from typing import List

# External Libraries
import pytest
from pytest_mock import MockerFixture

# VerdanTech Source
from src.domain import exceptions as domain_exceptions
from src.domain.user import User
from src.domain.user.email import Email, PasswordResetConfirmation
from src.interfaces.email.emitter import AbstractEmailEmitter
from src.interfaces.persistence.user import AbstractUserRepository
from src.ops import exceptions as ops_exceptions
from src.ops.user.services import verification as verification_services

pytestmark = [pytest.mark.unit]

# ======================================
# verification_services.email_confirmation_create() tests
# ======================================


async def test_email_confirmation_create(
    user: User, mock_user_repo: AbstractUserRepository, mocker: MockerFixture
) -> None:
    """
    Ensure the _generate_unique_email_confirmation_key method is called, and the
    resulting key is used to make a new EmailConfirmation on the email identified
    by the email address provided as an argument, and the email confimration email
    is emitted.

    Args:
        user (User): user factory fixture.
        mock_user_repo (AbstractUserRepository): mock user repository fixture.
        mocker (MockerFixture): pytest-mock.
    """
    key_length = 10
    generated_key = "abc"
    email_address = user.emails[0].address
    mock_generate_unique_email_confirmation_key = mocker.patch.object(
        verification_services,
        "generate_unique_email_confirmation_key",
        return_value=generated_key,
    )
    mock_email_emitter = mocker.Mock(spec=AbstractEmailEmitter)

    await verification_services.email_confirmation_create(
        user=user,
        email_address=email_address,
        key_length=key_length,
        user_repo=mock_user_repo,
        email_emitter=mock_email_emitter,
    )

    assert (
        user._get_email_by_confirmation_key(key=generated_key).address == email_address
    )
    mock_generate_unique_email_confirmation_key.assert_awaited_once_with(
        length=key_length, user_repo=mock_user_repo
    )
    mock_email_emitter.emit_user_email_confirmation.assert_called_once_with(
        email_address=email_address,
        username=user.username,
        key=generated_key,
    )


# ======================================
# verification_services.password_reset_create() tests
# ======================================


async def test_password_reset_create_unpersisted_user(
    user: User, mocker: MockerFixture
) -> None:
    """
    Ensure that UserIntegrityError is raised if the user provided
    does not have an ID.

    Args:
        user (User): user factory fixture.
        mocker (MockerFixture): pytest-mock.
    """
    user.id = None
    primary_email_address = user.primary_email.address

    with pytest.raises(domain_exceptions.EntityIntegrityException):
        await verification_services.password_reset_create(
            user=user,
            email_address=primary_email_address,
            key_length=0,
            user_repo=mocker.Mock(),
            email_emitter=mocker.Mock(),
        )


async def test_password_reset_create_incorrect_email_address(
    user: User, mocker: MockerFixture
) -> None:
    """
    Ensure that EntityNotFound is raised if the email address provided
    as an argument is not the user's primary email.

    Args:
        user (User): user factory fixture.
        mocker (MockerFixture): pytest-mock.
    """
    user.id = 0
    non_primary_address = "abc@abc.com"
    user.emails = [
        Email(address=non_primary_address, primary=False),
        Email(address="primary@abc.com", primary=True),
    ]

    with pytest.raises(ops_exceptions.EntityNotFound):
        await verification_services.password_reset_create(
            user=user,
            email_address=non_primary_address,
            key_length=0,
            user_repo=mocker.Mock(),
            email_emitter=mocker.Mock(),
        )


async def test_password_reset_create_success(
    user: User, mock_user_repo: AbstractUserRepository, mocker: MockerFixture
) -> None:
    """
    Ensure the _generate_unique_password_reset_key method is called, and the
    resulting key is used to make a new PasswordResetConfirmation, and the
    password reset email is emitted.

    Args:
        user (User): user factory fixture.
        mock_user_repo (AbstractUserRepository): mock user repository fixture.
        mocker (MockerFixture): pytest-mock.
    """
    key_length = 10
    generated_key = "abc"
    user.id = 0
    primary_email_address = user.primary_email.address

    mock__generate_unique_password_reset_key = mocker.patch.object(
        verification_services,
        "_generate_unique_password_reset_key",
        return_value=generated_key,
    )
    mock_email_emitter = mocker.Mock(spec=AbstractEmailEmitter)

    await verification_services.password_reset_create(
        user=user,
        email_address=primary_email_address,
        key_length=key_length,
        user_repo=mock_user_repo,
        email_emitter=mock_email_emitter,
    )

    assert user.password_reset_confirmation.key == generated_key
    mock__generate_unique_password_reset_key.assert_awaited_once_with(
        length=key_length, user_repo=mock_user_repo
    )
    mock_email_emitter.emit_user_password_reset.assert_called_once_with(
        email_address=primary_email_address,
        username=user.username,
        user_id=user.id,
        key=generated_key,
    )


# ======================================
# verification_services._generate_unique_email_confirmation_key() tests
# ======================================


async def test_generate_unique_email_confirmation_key(
    mock_user_repo: AbstractUserRepository,
    mocker: MockerFixture,
):
    """
    Ensure that the generalized unique key method is called
    with the name of the email confirmation key existence method
    "email_confirmation_key_exists", and the key is returned.

    Args:
        mock_user_repo (MockUserRepository): fixture providing mock
            user repoistory to test on.
        mocker (MockerFixture): pytest-mock.
    """
    key_length = 10
    generated_key = "abc"
    mock_generate_unique_key = mocker.patch(
        "src.ops.user.services.verification.generate_unique_key",
        return_value=generated_key,
    )

    assert (
        await verification_services.generate_unique_email_confirmation_key(
            length=key_length, user_repo=mock_user_repo
        )
        == generated_key
    )
    mock_generate_unique_key.assert_called_once_with(
        length=key_length,
        repo=mock_user_repo,
        existence_method_name="email_confirmation_key_exists",
        existence_method_argument_name="key",
    )


# ======================================
# verification_services._generate_unique_password_reset_key() tests
# ======================================


async def test__generate_unique_password_reset_key(
    mock_user_repo: AbstractUserRepository,
    mocker: MockerFixture,
):
    """
    Ensure that the generalized unique key method is called
    with the name of the password reset key existence method
    "password_reset_confirmation_key_exists", and the key is returned.

    Args:
        mock_user_repo (MockUserRepository): fixture providing mock
            user repoistory to test on.
        mocker (MockerFixture): pytest-mock.
    """
    key_length = 10
    generated_key = "abc"
    mock_generate_unique_key = mocker.patch(
        "src.ops.user.services.verification.generate_unique_key",
        return_value=generated_key,
    )

    assert (
        await verification_services._generate_unique_password_reset_key(
            length=key_length, user_repo=mock_user_repo
        )
        == generated_key
    )
    mock_generate_unique_key.assert_called_once_with(
        length=key_length,
        repo=mock_user_repo,
        existence_method_name="password_reset_confirmation_key_exists",
        existence_method_argument_name="key",
    )
