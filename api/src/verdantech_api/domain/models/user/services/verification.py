from litestar.contrib.repository.abc import AbstractAsyncRepository
from src.verdantech_api.domain.utils.key_generator import key_generator


class VerificationService:
    """Namespace for email verification functions"""
    @classmethod
    async def generate_open_email_confirmation_key(
        cls, length: int, user_repo: AbstractAsyncRepository
    ) -> str:
        """Generate a unique email confirmation key

        Args:
            length (int): length of the key to generate
            user_repo (AbstractAsyncRepository): user repository

        Returns:
            str: the unique key
        """
        return await cls.generate_open_key(
            length=length, repo=user_repo, field_name="emails.confirmation.key"
        )

    @classmethod
    async def generate_open_password_reset_key(
        cls, length: int, user_repo: AbstractAsyncRepository
    ) -> str:
        """Generate a unique password reset key

        Args:
            length (int): length of the key to generate
            user_repo (AbstractAsyncRepository): user repository

        Returns:
            str: the unique key
        """
        return await cls.generate_open_key(
            length=length, repo=user_repo, field_name="password_reset_confirmation.key"
        )

    @classmethod
    async def generate_open_key(
        cls, length: int, repo: AbstractAsyncRepository, field_name: str
    ) -> str:
        """Generate a unique verification key

        Args:
            length (int): length of the key to generate
            repo (AbstractAsyncRepository): repo to validate
                uniqueness on
            field_name (str): field name to validate uniqueness on

        Returns:
            str: the unique key
        """
        key = key_generator(length=length)
        while repo.exists(field_name=field_name, values=key):
            key = key_generator(length=length)
        return key
