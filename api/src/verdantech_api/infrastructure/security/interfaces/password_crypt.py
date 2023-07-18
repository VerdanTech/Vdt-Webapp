from abc import ABC, abstractmethod

from pydantic import SecretBytes, SecretStr


class AbstractPasswordCrypt(ABC):
    @abstractmethod
    async def get_password_hash(
        plaintext_password: SecretBytes | SecretStr | str | bytes,
    ) -> str:
        """Get password hash.

        Args:
            password: Plain password
        Returns:
            str: Hashed password
        """
        if isinstance(plaintext_password, SecretBytes | SecretStr):
            password = plaintext_password.get_secret_value()
        return password

    @abstractmethod
    async def verify_password(
        plain_password: SecretBytes | SecretStr | str | bytes, hashed_password: str
    ) -> bool:
        """Verify Password.

        Args:
            plain_password (SecretBytes | SecretStr): Password input
            hashed_password (str): Password hash to verify against

        Returns:
            bool: True if the password hashes match
        """
        if isinstance(plain_password, SecretBytes | SecretStr):
            plain_password = plain_password.get_secret_value()
        return False
