from typing import Protocol


class AbstractPasswordCrypt(Protocol):
    async def get_password_hash(
        self,
        plain_password: str | bytes,
    ) -> str:
        """Get password hash.

        Args:
            plain_password: Plain password
        Returns:
            str: Hashed password
        """
        ...

    async def verify_password(
        self, plain_password: str | bytes, hashed_password: str
    ) -> bool:
        """Verify Password.

        Args:
            plain_password (SecretBytes | SecretStr): Password input
            hashed_password (str): Password hash to verify against

        Returns:
            bool: True if the password hashes match
        """
        ...


class MockPasswordCrypt:
    async def get_password_hash(
        self,
        plain_password: str | bytes,
    ) -> str:
        return f"{plain_password}::hash"

    async def verify_password(
        self, plain_password: str | bytes, hashed_password: str
    ) -> bool:
        return f"{plain_password}::hash" == hashed_password
