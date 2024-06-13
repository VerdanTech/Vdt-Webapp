# Standard Library
from typing import List

# External Libraries
import pytest
from pytest_mock import MockerFixture

# VerdanTech Source
from src.user.domain import PasswordResetConfirmation, User
from src.user.interfaces.persistence.user import AbstractUserRepository
from src.utils import key_generator

# ======================================
# generate_unique_key() tests
# ======================================


@pytest.mark.parametrize(
    ("generated_keys", "existing_users", "expected_output"),
    [
        # Test case: key is unique, and it is returned.
        (
            ["abc"],
            [],
            "abc",
        ),
        # Test case: key is not unique, another generated, and it is returned.
        (
            ["abc", "123"],
            [
                User(
                    username="existing_user",
                    password_reset_confirmation=PasswordResetConfirmation(key="abc"),
                )
            ],
            "123",
        ),
    ],
)
async def test_generate_unique_key(
    generated_keys: List[str],
    existing_users: List[User],
    expected_output: str,
    mock_user_repo: AbstractUserRepository,
    mocker: MockerFixture,
):
    """
    Ensure a unique key is generated
    given a repository existence function.

    Args:
        generated_keys (List[str]): mock keys to generate retuned from key_generator.
        existing_users (List[User]): existing users to pre-populate repository with.
        expected_output (str): expected unique key returned.
        mock_user_repo (AbstractUserRepository): fixture providing mock user repository
        mocker (MockerFixture): pytest-mock.
    """
    key_length = 10
    mock_key_generator = mocker.patch.object(
        key_generator,
        "key_generator",
        side_effect=generated_keys,
    )

    await mock_user_repo.add_many(existing_users)

    assert (
        await key_generator.generate_unique_key(
            length=key_length,
            repo=mock_user_repo,
            existence_method_name="password_reset_confirmation_key_exists",
            existence_method_argument_name="key",
        )
        == expected_output
    )
    mock_key_generator.assert_called_with(length=key_length)
