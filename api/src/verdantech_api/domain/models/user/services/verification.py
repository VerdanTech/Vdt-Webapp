from src.verdantech_api.domain.interfaces.persistence.user.repository import (
    AbstractUserRepository,
)
from src.verdantech_api.domain.utils.key_generator import key_generator

from ..entities import User


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


class EmailVerificationService:
    @staticmethod
    async def new_verification(
        user: User, address: str, key_length: int, user_repo: AbstractUserRepository
    ) -> str:
        """Generate new email confirmation key, and add a new email confirmation

        Args:
            user (User): user to add a new confirmation on
            address (str): email to add a new confirmation on
            key_length (int): application setting
            user_repo (AbstractUserRepository): user repository

        Returns:
            str: generated key
        """
        key = await VerificationService.generate_open_email_confirmation_key(
            length=key_length, user_repo=user_repo
        )
        user.new_email_verification(address=address, key=key)
        return key


class PasswordResetService:
    @staticmethod
    async def new_password_reset(
        user: User, key_length: int, user_repo: AbstractUserRepository
    ) -> str:
        """Generate a new password reset confirmation key, and add a new
            password reset confirmation

        Args:
            user (User): user to add a new confirmation on
            key_length (int): application setting
            user_repo (AbstractUserRepository): user repository

        Returns:
            str: generated key
        """
        key = await VerificationService.generate_open_password_reset_key(
            length=key_length, user_repo=user_repo
        )
        user.new_password_reset(key=key)
        return key
