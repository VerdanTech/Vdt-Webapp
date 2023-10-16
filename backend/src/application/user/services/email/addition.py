from src.interfaces.persistence.user.repository import (
    AbstractUserRepository,
)
from src.domain.user.entities import User
from src.domain.user.services import EmailAdditionService
from src.domain.user.services.verification import (
    EmailVerificationService,
)
from src.infrastructure.email.litestar_emitter import EmailEmitter

from .verification import emit_email_verification_email


async def add_first_email(
    user: User,
    email_address: str,
    require_email_verification: bool,
    verification_key_length: int,
    user_repo: AbstractUserRepository,
    email_emitter: EmailEmitter,
) -> None:
    """Call the domain service email addition functions based on
        whether email verification is required in app settings

    Args:
        user (User): user to add email to
        email_address (str): email address to add
        require_email_verification (bool): app setting
        verification_key_length (int): length of verification key
            to generate it
        user_repo (AbstractUserRepository): user repository
        email_emitter (EmailEmitter): email emitter awaitable
    """
    if require_email_verification:
        key = await EmailAdditionService.add_first_email_verification_required(
            user=user,
            address=email_address,
            key_length=verification_key_length,
            user_repo=user_repo,
        )
        await emit_email_verification_email(
            email_address=email_address,
            username=user.username,
            key=key,
            email_emitter=email_emitter,
        )
    else:
        EmailAdditionService.add_first_email_verification_not_required(
            user=user, address=email_address
        )


async def new_email_verification(
    user: User,
    email_address: str,
    key_length: int,
    user_repo: AbstractUserRepository,
    email_emitter: EmailEmitter,
) -> None:
    """Call the domain service to generate a new key
        and add email confirmation, and send email
        confirmation email

    Args:
        user (User): user to add verification on
        email_address (str): email to verify
        key_length (int): application setting
        user_repo (AbstractUserRepository): user repository
        email_emitter (EmailEmitter): email emitter awaitable
    """
    key = await EmailVerificationService.new_verification(
        user=user,
        address=email_address,
        key_length=key_length,
        user_repo=user_repo,
    )
    await emit_email_verification_email(
        email_address=email_address,
        username=user.username,
        key=key,
        email_emitter=email_emitter,
    )
