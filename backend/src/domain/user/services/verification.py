from src.interfaces.email.emitter import AbstractEmailEmitter
from src.interfaces.persistence.user.repository import AbstractUserRepository
from src.utils.key_generator import key_generator

from .. import exceptions
from ..entities import User


async def email_confirmation_create(
    user: User,
    address: str,
    key_length: int,
    user_repo: AbstractUserRepository,
    email_emitter: AbstractEmailEmitter,
) -> None:
    """Generate new email confirmation key, and add a new email confirmation

    Args:
        user (User): user to add a new confirmation on
        address (str): email to add a new confirmation on
        key_length (int): application setting
        user_repo (AbstractUserRepository): user repository

    Returns:
        str: generated key
    """
    key = await generate_open_email_confirmation_key(
        length=key_length, user_repo=user_repo
    )
    user.email_confirmation_create(address=address, key=key)
    email_emitter.emit_user_email_confirmation(
        email_address=address, username=user.username, key=key
    )


async def password_reset_create(
    user: User,
    address: str,
    key_length: int,
    user_repo: AbstractUserRepository,
    email_emitter: AbstractEmailEmitter,
) -> None:
    """Generate a new password reset confirmation key, and add a new
        password reset confirmation

    Args:
        user (User): user to add a new confirmation on
        key_length (int): application setting
        user_repo (AbstractUserRepository): user repository

    Returns:
        str: generated key
    """
    primary_email = user.get_primary_email()
    if not address == primary_email.address:
        raise exceptions.UserNotFound("The email address was not enabled.")
    key = await generate_open_password_reset_key(length=key_length, user_repo=user_repo)
    user.password_reset_create(key=key)
    email_emitter.emit_user_password_reset(
        email_address=address, username=user.username, user_id=user.id, key=key
    )


async def generate_open_email_confirmation_key(
    length: int, user_repo: AbstractUserRepository
) -> str:
    """Generate a unique email confirmation key

    Args:
        length (int): length of the key to generate
        user_repo (AbstractUserRepository): user repository

    Returns:
        str: the unique key
    """
    # The name of the method on the AbstractUserRepository
    # that returns True when an email confirmation key exists
    # in any user
    uniqueness_method_name = "email_confirmation_key_exists"
    return await _generate_open_key(
        length=length,
        repo=user_repo,
        uniqueness_method_name=uniqueness_method_name,
    )


async def generate_open_password_reset_key(
    length: int, user_repo: AbstractUserRepository
) -> str:
    """
    Generate a unique password reset key.

    Args:
        length (int): length of the key to generate.
        user_repo (AbstractUserRepository): user repository.

    Returns:
        str: the unique key.
    """
    # The name of the method on the AbstractUserRepository
    # that returns True when an email confirmation key exists
    # in any user
    uniqueness_method_name = "password_reset_confirmation_key_exists"
    return await _generate_open_key(
        length=length,
        repo=user_repo,
        uniqueness_method_name=uniqueness_method_name,
    )


async def _generate_open_key(
    length: int, user_repo: AbstractUserRepository, uniqueness_method_name: str
) -> str:
    """
    Generate a unique verification key.

    Args:
        length (int): length of the key to generate.
        repo (AbstractUserRepository): user repository
            instance.
        method_name (str): the name of the repository
            uniqueness check method.

    Returns:
        str: the unique key.
    """
    key = key_generator(length=length)
    while await user_repo.async_dynamic_call(
        method_name=uniqueness_method_name, key=key
    ):
        key = key_generator(length=length)
    return key
