from src.verdantech_api.domain.interfaces.persistence.user.repository import (
    AbstractUserRepository,
)
from src.verdantech_api.domain.interfaces.security.crypt import AbstractPasswordCrypt
from src.verdantech_api.domain.models.user.entities import User
from src.verdantech_api.domain.models.user.exceptions import UserNotAuthenticated
from src.verdantech_api.domain.models.user.services.verification import (
    PasswordResetService,
)
from src.verdantech_api.infrastructure.email.litestar_emitter import EmailEmitter

from ..email.verification import emit_password_reset_email


async def new_password_reset(
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
    key = await PasswordResetService.new_password_reset(
        user=user,
        address=email_address,
        key_length=key_length,
        user_repo=user_repo,
    )
    await emit_password_reset_email(
        email_address=email_address,
        username=user.username,
        user_id=user._id,
        key=key,
        email_emitter=email_emitter,
    )


async def close_password_reset(
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
        raise UserNotAuthenticated("The provided password is not correct")

    # Reset password
    await user.reset_password(new_password=new_password, password_crypt=password_crypt)
