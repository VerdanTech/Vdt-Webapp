# Standard Library
from typing import List

# External Libraries
import pytest
import svcs
from pytest_mock import MockerFixture
from svcs import Container

# VerdanTech Source
from src.common.interfaces.persistence.uow import AbstractUow
from src.user.domain import PasswordResetConfirmation, User
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
    svcs_container: Container,
    mocker: MockerFixture,
):
    """
    Ensure a unique key is generated
    given a repository existence function.

    Args:
        generated_keys (List[str]): mock keys to generate retuned from key_generator.
        existing_users (List[User]): existing users to pre-populate repository with.
        expected_output (str): expected unique key returned.
        svcs_container (Container): service locator with mock services.
        mocker (MockerFixture): pytest-mock.
    """
    uow = await svcs_container.aget_abstract(AbstractUow)

    key_length = 10
    mock_key_generator = mocker.patch.object(
        key_generator,
        "key_generator",
        side_effect=generated_keys,
    )

    for user in existing_users:
        await uow.repos.users.add(user)

    assert (
        await key_generator.generate_unique_key(
            length=key_length,
            repo=uow.repos.users,
            existence_method_name="password_reset_confirmation_key_exists",
            existence_method_argument_name="key",
        )
        == expected_output
    )
    mock_key_generator.assert_called_with(length=key_length)
