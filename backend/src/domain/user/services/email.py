from src.interfaces.persistence.user.repository import (
    AbstractUserRepository,
)

from ..entities import User
from .verification import VerificationService


class EmailAdditionService:
    @staticmethod
    async def add_first_email_verification_required(
        user: User,
        address: str,
        key_length: int,
        user_repo: AbstractUserRepository,
    ) -> str:
        """Add first email to user object.
            Primary is true and verification key is generated

        Args:
            user (User): user object to add email too
            address (str): email address to add
            user_repo (AbstractUserRepository): user repository

        Returns:
            str: generated verification key
        """
        key = await VerificationService.generate_open_email_confirmation_key(
            length=key_length, user_repo=user_repo
        )
        user.add_email(
            address=address,
            primary=True,
            key=key,
        )
        return key

    @staticmethod
    def add_first_email_verification_not_required(
        user: User,
        address: str,
    ) -> None:
        """Add first email to user object. Primary is true and no key is needed

        Args:
            user (User): user object to add email too
            address (str): email address to add
        """
        user.add_verified_email(address=address, primary=True)

    @staticmethod
    async def add_non_first_email_verification_required(
        user: User,
        address: str,
        key_length: int,
        user_repo: AbstractUserRepository,
    ) -> str:
        """Add non-first email to user object.
            Primary is false as it will be set to true upon verification.
            Verification key is generated

        Args:
            user (User): user object to add email too
            address (str): email address to add
            user_repo (AbstractUserRepository): user repository

        Returns:
            str: generated verification key
        """
        key = await VerificationService.generate_open_email_confirmation_key(
            length=key_length, user_repo=user_repo
        )
        user.add_email(
            address=address,
            primary=False,
            key=key,
        )
        return key

    @staticmethod
    def add_non_first_email_verification_not_required(
        user: User,
        address: str,
    ) -> None:
        """Add non-first email to user object. Primary is true and no key is needed

        Args:
            user (User): user object to add email too
            address (str): email address to add
        """
        user.add_verified_email(address=address, primary=True)
