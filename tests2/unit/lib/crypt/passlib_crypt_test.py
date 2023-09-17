import pytest


class TestPasslibCrypt:
    async def test_get_password_hash(self, passlib_password_crypt) -> None:
        """Test that the encryption key is formatted correctly."""
        secret_str_hash = await passlib_password_crypt.get_password_hash("This is a password!")
        secret_bytes_hash = await passlib_password_crypt.get_password_hash(b"This is a password too!")

        assert secret_str_hash.startswith("$argon2")
        assert secret_bytes_hash.startswith("$argon2")

    @pytest.mark.parametrize(
        "valid_password,tested_password,expected_result",
        (
            ("SuperS3cret123456789!!", "SuperS3cret123456789!!", True),
            ("SuperS3cret123456789!!", "Invalid!!", False),
        ),
    )
    async def test_verify_password(
        self,
        passlib_password_crypt,
        valid_password: str,
        tested_password: str,
        expected_result: bool,
    ) -> None:
        """Test that the encryption key is formatted correctly."""

        secret_str_hash = await passlib_password_crypt.get_password_hash(valid_password)
        is_valid = await passlib_password_crypt.verify_password(
            tested_password, secret_str_hash
        )

        assert is_valid == expected_result
