# External Libraries
from passlib.context import CryptContext

# VerdanTech Source
from src.common.interfaces.security import AbstractPasswordCrypt

password_crypt_context = CryptContext(schemes=["argon2"], deprecated="auto")


class PasslibPasswordCrypt(AbstractPasswordCrypt):
    """Fulfills the AbstractPasswordCrypt interface."""

    async def get_password_hash(
        self,
        plain_password: str | bytes,
    ) -> str:
        """
        Get password hash.

        Args:
            plain_password: plaintext password.

        Returns:
            str: hashed password.
        """
        return password_crypt_context.hash(secret=plain_password)

    async def verify_password(
        self,
        plain_password: str | bytes,
        hashed_password: str,
    ) -> bool:
        """
        Verify Password.

        Args:
            plain_password (SecretBytes | SecretStr): password input.
            hashed_password (str): password hash to verify against.

        Returns:
            bool: True if the password hashes match
        """
        valid, _ = password_crypt_context.verify_and_update(
            secret=plain_password,
            hash=hashed_password,
        )
        return bool(valid)
