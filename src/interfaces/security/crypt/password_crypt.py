# Standard Library
from typing import Protocol


class AbstractPasswordCrypt(Protocol):
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
        ...

    async def verify_password(
        self, plain_password: str | bytes, hashed_password: str
    ) -> bool:
        """
        Verify Password.

        Args:
            plain_password (SecretBytes | SecretStr): password input.
            hashed_password (str): password hash to verify against.

        Returns:
            bool: True if the password hashes match
        """
        ...
