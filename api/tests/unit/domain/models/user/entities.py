from typing import ContextManager

import pytest
from src.verdantech_api.domain.interfaces.security.crypt import AbstractPasswordCrypt
from src.verdantech_api.domain.models.user.entities import User
from src.verdantech_api.domain.models.user.exceptions import PasswordAlreadySetError


class TestUser:
    def test_set_username(self, user: User) -> None:
        """Ensure the lowercase username is saved into
        the user object

        Args:
            user (User): user object to test on (pytest fixture)
        """
        username = "TestUsername"
        user.set_username(username=username)
        assert user.username == username
        assert user.username_norm == username.lower()

    def test_add_email(self, user: User) -> None:
        """Ensure the correct values are set
        and email unverified

        Args:
            user (User): user (User): user object to test on (pytest fixture)
        """
        address = "TestEmail@Test.com"
        primary = False
        key = "aBcDeFg"

        user.add_email(address=address, primary=primary, key=key)

        assert user.emails[0].address == address
        assert user.emails[0].primary == primary
        assert user.emails[0].confirmation.key == key
        assert not user.emails[0].verified

    def test_add_verified_email(self, user: User) -> None:
        """Ensure the correct values are set
        and email verified

        Args:
            user (User): user (User): user object to test on (pytest fixture)
        """

        address = "TestEmail@Test.com"
        primary = False

        user.add_verified_email(address=address, primary=primary)

        assert user.emails[0].address == address
        assert user.emails[0].primary == primary
        assert user.emails[0].confirmation is None
        assert user.emails[0].verified

    @pytest.mark.parametrize(
        ("existing_password", "password", "overwrite", "expected_error_context"),
        [
            # Test case: no existing password -> no error
            (None, "TestPassword", False, None),
            # Existing password -> error
            ("ExistingPassword", "TestPassword", False, PasswordAlreadySetError),
            # Existing password but overwrite = True -> no error
            ("ExistingPassword", "TestPassword", True, None),
        ],
        indirect=["expected_error_context"],
    )
    async def test_set_password(
        self,
        existing_password: str,
        password: str,
        overwrite: bool,
        expected_error_context: ContextManager,
        user: User,
        mock_password_crypt: AbstractPasswordCrypt,
    ) -> None:
        """Ensure the password is set, and error is raised if
            password already exists and overwrite is not specified

        Args:
            existing_password (str): pre-existing user password
            password (str): new password
            overwrite (bool): explicit password overwrite permission
            expected_error_context (ContextManager): An instance of nullcontext() if
                expected_error_context = None and pytest.raises(expected_error_context)
                otherwise See: tests/conftest.py
            user (User): user object to test on (pytest fixture)
            mock_password_crypt (AbstractPasswordCrypt): (pytest fixture)
        """
        if existing_password:
            user._password_hash = existing_password

        with expected_error_context as error:
            await user.set_password(
                password=password,
                password_crypt=mock_password_crypt,
                overwrite=overwrite,
            )
            if error is None:
                assert user._password_hash == f"{password}::hash"

    @pytest.mark.parametrize(
        ("existing_password", "password", "expected_result"),
        [
            ("TestPassword", "TestPassword", True),
            ("TestPasword", "NotTestPassword", False),
        ],
    )
    async def test_verify_password(
        self,
        existing_password: str,
        password: str,
        expected_result: bool,
        user: User,
        mock_password_crypt: AbstractPasswordCrypt,
    ) -> None:
        """Ensure the function compares the input with
        password hash correctly

        Args:
            existing_password (str): existing user password
            password (str): input for comparison
            expected_result (bool): expected result of comparison
            user (User): user object to test on (pytest fixture)
            mock_password_crypt (AbstractPasswordCrypt): (pytest fixture)
        """
        user._password_hash = await mock_password_crypt.get_password_hash(
            plain_password=existing_password
        )

        assert (
            await user.verify_password(
                password=password, password_crypt=mock_password_crypt
            )
            == expected_result
        )
