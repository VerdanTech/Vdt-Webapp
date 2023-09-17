from src.verdantech_api.domain.interfaces.persistence.user.repository import (
    AbstractUserRepository,
)
from src.verdantech_api.domain.utils.key_generator import key_generator


class VerificationService:
    """Namespace for email and password verification functions"""

    @classmethod
    async def generate_open_email_confirmation_key(
        cls, length: int, user_repo: AbstractUserRepository
    ) -> str:
        """Generate a unique email confirmation key

        Args:
            length (int): length of the key to generate
            user_repo (AbstractUserRepository): user repository

        Returns:
            str: the unique key
        """
        return await cls.generate_open_key(
            length=length,
            repo=user_repo,
            uniqueness_method_name="email_confirmation_key_exists",
        )

    @classmethod
    async def generate_open_password_reset_key(
        cls, length: int, user_repo: AbstractUserRepository
    ) -> str:
        """Generate a unique password reset key

        Args:
            length (int): length of the key to generate
            user_repo (AbstractUserRepository): user repository

        Returns:
            str: the unique key
        """
        return await cls.generate_open_key(
            length=length,
            repo=user_repo,
            uniqueness_method_name="password_reset_confirmation_key_exists",
        )

    @classmethod
    async def generate_open_key(
        cls, length: int, repo: AbstractUserRepository, uniqueness_method_name: str
    ) -> str:
        """Generate a unique verification key

        Args:
            length (int): length of the key to generate
            repo (AbstractUserRepository): user repository
                instance
            method_name (str): the name of the repository
                uniqueness check method

        Returns:
            str: the unique key
        """
        key = key_generator(length=length)
        while await repo.async_dynamic_call(
            method_name=uniqueness_method_name, key=key
        ):
            key = key_generator(length=length)
        return key
