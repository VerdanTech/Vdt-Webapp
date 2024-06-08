# External Libraries
import pytest

# VerdanTech Source
from src.adapters.security.crypt.passlib import PasslibPasswordCrypt

pytestmark = [pytest.mark.unit]


class TestPasslibCrypt:
    # ======================================
    # PasslibPasswordCrypt.get_password_hash() tests
    # ======================================

    async def test_get_password_hash(
        self, passlib_password_crypt: PasslibPasswordCrypt
    ) -> None:
        """
        Ensure that the password hasher returns the properly formatted password hash.

        Args:
            passlib_password_crypt (PasslibPasswordCrypt): fixture providing
                class under test.
        """
        secret_str_hash = await passlib_password_crypt.get_password_hash(
            "This is a password!"
        )
        secret_bytes_hash = await passlib_password_crypt.get_password_hash(
            b"This is a password!"
        )

        assert secret_str_hash.startswith("$argon2")
        assert secret_bytes_hash.startswith("$argon2")

    # ======================================
    # PasslibPasswordCrypt.verify_password() tests
    # ======================================

    @pytest.mark.parametrize(
        ("password_to_hash", "password_to_verify", "expected_result"),
        [
            ("SuperS3cret123456789!!", "SuperS3cret123456789!!", True),
            ("SuperS3cret123456789!!", "Invalid!!", False),
        ],
    )
    async def test_verify_password(
        self,
        passlib_password_crypt: PasslibPasswordCrypt,
        password_to_hash: str,
        password_to_verify: str,
        expected_result: bool,
    ) -> None:
        """
        Ensure that True is returned if the password hash matches
        and False otherwise.

        Args:
            passlib_password_crypt (PasslibPasswordCrypt): fixture
                providing class under test.
            password_to_hash (str): the input password to hash.
            password_to_verify (str): the password to check against hash.
            expected_result (bool): expected result of password hash check.
        """

        hashed_password = await passlib_password_crypt.get_password_hash(
            password_to_hash
        )
        is_valid = await passlib_password_crypt.verify_password(
            password_to_verify, hashed_password
        )

        assert is_valid == expected_result
