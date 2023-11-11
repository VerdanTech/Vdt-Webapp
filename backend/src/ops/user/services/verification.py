from src import settings
from src.domain.common.entities import EntityIDType
from src.domain.user import exceptions as domain_exceptions
from src.domain.user.entities import User
from src.domain.user.services import verification as verification_domain_services
from src.infra.email.litestar_emitter import EmailEmitter
from src.interfaces.persistence.user.repository import AbstractUserRepository
from src.interfaces.security.crypt.password_crypt import AbstractPasswordCrypt


async def email_confirmation_create(
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
    key = await verification_domain_services.email_confirmation_create(
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


async def emit_email_verification_email(
    email_address: str, username: str, key: str, email_emitter: EmailEmitter
) -> None:
    """Emit the email with the email verification parameters

    Args:
        email_address (str): email address to send to
        username (str): username of the user receiving
        key (str): verification key
        email_emitter (EmailEmitter): email emitter callable
    """
    await email_emitter(
        receiver=email_address,
        subject="Email verification - VerdanTech",
        filepath=settings.email_path("email_verification.html"),
        username=username,
        client_base_url=settings.CLIENT_BASE_URL,
        verification_url=settings.CLIENT_EMAIL_VERIFICATION_URL + key,
    )


async def password_reset_create(
    user: User,
    email_address: str,
    key_length: str,
    user_repo: AbstractUserRepository,
    email_emitter: EmailEmitter,
) -> None:
    """Call the domain service to generate a new key,
    add new password reset, and password reset
    confirmation email

    Args:
        user (User): user to add reset on
        email_address (str): email to send confirmation to
        key_length (int): application setting
        user_repo (AbstractUserRepository): user repository
        email_emitter (EmailEmitter): email emitter awaitable
    """
    key = await verification_domain_services.password_reset_create(
        user=user,
        address=email_address,
        key_length=key_length,
        user_repo=user_repo,
    )
    await emit_password_reset_email(
        email_address=email_address,
        username=user.username,
        user_id=user.id,
        key=key,
        email_emitter=email_emitter,
    )


async def emit_password_reset_email(
    email_address: str,
    username: str,
    user_id: EntityIDType,
    key: str,
    email_emitter: EmailEmitter,
) -> None:
    """Emit the email with the password reset parameters

    Args:
        email_address (str): email address to send to
        username (str): username of the recepient
        user_id (EntityIDType): ID of the recepiend
        key (str): verification key
        email_emitter (EmailEmitter): email emitter callable
    """
    await email_emitter(
        receiver=email_address,
        subject="Password reset - VerdanTech",
        filepath=settings.email_path("password_reset.html"),
        username=username,
        user_id=user_id,
        client_base_url=settings.CLIENT_BASE_URL,
        reset_url=settings.CLIENT_PASSWORD_RESET_URL + key,
    )


async def password_reset_confirm(
    user: User,
    old_password: str,
    new_password: str,
    password_crypt: AbstractPasswordCrypt,
) -> None:
    """Call the domain service to authenticate the old password,
        raise exception if not, then reset the user's password

    Args:
        user (User): user to reset password on
        old_password (str): old/current password for authentication
        new_password (str): new password to set on the object
        password_crypt (AbstractPasswordCrypt): password hashing interface

    Raises:
        UserNotAuthenticated: raised if the old password fails to authenticate
    """
    # Authorize operation
    if not await user.verify_password(
        password=old_password, password_crypt=password_crypt
    ):
        raise domain_exceptions.UserNotAuthenticated(
            "The provided password is not correct"
        )

    # Reset password
    await user.reset_password(new_password=new_password, password_crypt=password_crypt)
