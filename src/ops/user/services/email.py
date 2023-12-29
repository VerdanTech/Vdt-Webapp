# Standard Library
from typing import Optional

# VerdanTech Source
from src.domain.user.entities import User
from src.interfaces.email.emitter import AbstractEmailEmitter
from src.interfaces.persistence.user.repository import AbstractUserRepository

from . import verification as verification_services


async def email_create(
    user: User,
    address: str,
    max_emails: int,
    verification: Optional[bool] = False,
    key_length: Optional[int] = None,
    user_repo: Optional[AbstractUserRepository] = None,
    email_emitter: Optional[AbstractEmailEmitter] = None,
) -> None:
    """
    Call the email_create method on the user. Generate an
    email confirmation key with verification_services if
    required.

    Args:
        user (User): user to create email on.
        address (str): address of the created email.
        max_emails (int): maximum emails stored in a User, application setting.
        verification (Optional[bool]): whether to undergo an
            email confirmation process. Defaults to False.
        key_length (Optional[int]): length of the confirmation key to generate.
            Required if verification is True. Defaults to None.
        user_repo (Optional[AbstractUserRepository], optional): user repository interface.
            Required if verification is True. Defaults to None.
        email_emitter (AbstractEmailEmitter): email emitter interface.
            Required if verification is True. Defaults to None.
    Raises:
        ValueError: if user_repo or key_length aren't passed in
            when verification is True.
    """
    # Generate an email confirmation key if verification is True
    key = None
    if verification:
        if user_repo is None or key_length is None or email_emitter is None:
            raise ValueError(
                f"""Arguments key_length and user_repo and email_emitter are required 
                if argument verification is True; {key_length} and {user_repo} and {email_emitter} were passed."""
            )
        key = await verification_services.generate_unique_email_confirmation_key(
            length=key_length, user_repo=user_repo
        )

        await email_emitter.emit_user_email_confirmation(
            email_address=address, username=user.username, key=key
        )

    user.email_create(
        address=address,
        max_emails=max_emails,
        verification=verification,
        email_confirmation_key=key,
    )
