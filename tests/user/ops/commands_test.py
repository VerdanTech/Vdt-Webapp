# Standard Library
import uuid

# External Libraries
import pytest
from pydantic import SecretStr
from svcs import Container

# VerdanTech Source
from src import settings
from src.common.interfaces.persistence.uow import AbstractUow
from src.common.interfaces.security.passwords import AbstractPasswordCrypt
from src.common.ops.exceptions import EntityNotFound
from src.user.domain import commands, events
from src.user.domain.models import PasswordResetConfirmation, User
from src.user.ops import commands as handlers
from src.utils.key_generator import key_generator

pytestmark = [pytest.mark.unit]


# ======================================
# create_user() tests
# ======================================


async def test_create_user_success(
    svcs_container: Container,
) -> None:
    """
    Ensure the user creation operation creates a user and persists
    them into the repository.

    Args:
        svcs_container (Container): service locator with mock services.
    """
    # Locate services
    uow = await svcs_container.aget(AbstractUow)

    command = commands.UserCreateCommand(
        username="new_username",
        email_address="new_email_address@test.com",
        password1=SecretStr("New_password12"),
        password2=SecretStr("New_password12"),
    )

    await handlers.create_user(command=command, svcs_container=svcs_container)

    async with uow:
        persisted_user = await uow.repos.users.get_by_username(
            username=command.username
        )

    # Assert the user was persisted correctly
    assert (
        isinstance(persisted_user, User)
        and persisted_user.id_or_error()
        and persisted_user.username == command.username
        and persisted_user._password_hash is not None
    )

    # Assert the follow up event was raised correctly
    assert isinstance(
        next(uow.collect_new_events(), None), events.EmailPendingConfirmation
    ) and isinstance(next(uow.collect_new_events(), None), events.UserCreateCommandd)


# ======================================
# request_email_confirmation() tests
# ======================================


async def test_request_email_confirmation_email_not_found(
    svcs_container: Container,
) -> None:
    """
    Ensure that when the operation is called with an email that does
    not match an existing user, the EntityNotFound exception is raised.

    Args:
        svcs_container (Container): service locator with mock services.
    """
    nonexistant_email = "nonexistant_email@gmail.com"

    command = commands.UserRequestEmailConfirmationCommand(email_address=nonexistant_email)

    with pytest.raises(EntityNotFound):
        await handlers.request_email_confirmation(
            command=command, svcs_container=svcs_container
        )


async def test_email_confirmation_request_success(
    svcs_container: Container,
) -> None:
    """
    Ensure that the operation creates a new EmailPendingConfirmation event

    Args:
        svcs_container (Container): service locator with mock services.
    """
    uow = await svcs_container.aget(AbstractUow)

    existing_email = "existing_email@gmail.com"

    # Add existing user
    user = User(username="existing_username")
    user.email_create(address=existing_email, max_emails=3, verification=False)
    async with uow:
        await uow.repos.users.add(user)
        await uow.commit()

    command = commands.UserRequestEmailConfirmationCommand(email_address=existing_email)
    await handlers.request_email_confirmation(
        command=command, svcs_container=svcs_container
    )

    # Assert the follow up event was raised correctly
    assert isinstance(
        next(uow.collect_new_events(), None), events.EmailPendingConfirmation
    )


# ================================================================
# confirm_email_confirmation() tests
# ================================================================


async def test_confirm_email_confirmation_user_not_found(
    svcs_container: Container,
) -> None:
    """
    Ensure that when the operation is called with a confirmation key that does
    not match an existing user, the EntityNotFound exception is raised.

    Args:
        svcs_container (Container): service locator with mock services.
    """
    command = commands.UserConfirmEmailConfirmationCommand(key=uuid.uuid4())

    with pytest.raises(EntityNotFound):
        await handlers.confirm_email_confirmation(
            command=command, svcs_container=svcs_container
        )


async def test_confirm_email_confirmation_success(
    svcs_container: Container,
) -> None:
    """
    Ensure that the operation confirms and closes an existing
    email confirmation object on the user's email and verifies it.

    Args:
        svcs_container (Container): service locator with mock services.
    """
    uow = await svcs_container.aget(AbstractUow)

    existing_email = "existing_email@gmail.com"
    existing_key = uuid.uuid4()

    # Add existing user
    user = User(username="existing_username")
    user.email_create(address=existing_email, max_emails=3, verification=True)
    user.email_confirmation_create(address=existing_email, key=existing_key)
    async with uow:
        await uow.repos.users.add(user)
        await uow.commit()

    command = commands.UserConfirmEmailConfirmationCommand(key=existing_key)
    await handlers.confirm_email_confirmation(
        command=command, svcs_container=svcs_container
    )

    async with uow:
        persisted_user = await uow.repos.users.get_by_email_address(existing_email)

    # Assert the user was persisted correctly
    assert (
        isinstance(persisted_user, User)
        and persisted_user.primary_email.confirmation is None
    )


# ======================================
# request_password_reset() tests
# ======================================


async def test_request_password_reset_email_not_found(
    svcs_container: Container,
) -> None:
    """
    Ensure that when the operation is called with an email that does
    not match an existing user, the EntityNotFound exception is raised.

    Args:
        svcs_container (Container): service locator with mock services.
    """
    nonexistant_email = "nonexistant_email@gmail.com"

    command = commands.UserRequestPasswordResetCommand(email_address=nonexistant_email)

    with pytest.raises(EntityNotFound):
        await handlers.request_password_reset(
            command=command, svcs_container=svcs_container
        )


async def test_request_password_reset_email_found_but_unprimary(
    svcs_container: Container,
) -> None:
    """
    Ensure that when the operation is called with an email that does
    match an existing user but is not the primary email, the EntityNotFound exception is raised.

    Args:
        svcs_container (Container): service locator with mock services.
    """
    uow = await svcs_container.aget(AbstractUow)

    existing_email = "existing_email@gmail.com"
    existing_unprimary_email = "existing_email_unprimary@gmail.com"

    # Add existing user
    user = User(username="existing_username")
    user.email_create(
        address=existing_unprimary_email, max_emails=3, verification=False
    )
    user.email_create(address=existing_email, max_emails=3, verification=False)
    async with uow:
        await uow.repos.users.add(user)
        await uow.commit()

    command = commands.UserRequestPasswordResetCommand(email_address=existing_unprimary_email)

    with pytest.raises(EntityNotFound):
        await handlers.request_password_reset(
            command=command, svcs_container=svcs_container
        )


async def test_request_password_reset_success(
    svcs_container: Container,
) -> None:
    """
    Ensure that the operation creates a new PasswordPendingReset event.

    Args:
        svcs_container (Container): service locator with mock services.
    """
    uow = await svcs_container.aget(AbstractUow)

    existing_email = "existing_email@gmail.com"

    # Add existing user
    user = User(username="existing_username")
    user.email_create(address=existing_email, max_emails=3, verification=False)
    async with uow:
        await uow.repos.users.add(user)
        await uow.commit()
    command = commands.UserRequestPasswordResetCommand(email_address=existing_email)
    await handlers.request_password_reset(
        command=command, svcs_container=svcs_container
    )

    assert isinstance(next(uow.collect_new_events(), None), events.PasswordPendingReset)


# ======================================
# confirm_password_reset() tests
# ======================================


async def test_confirm_password_reset_key_not_found(
    svcs_container: Container,
) -> None:
    """
    Ensure that when the operation is called with a key that does
    not match an existing user, the EntityNotFound exception is raised.

    Args:
        svcs_container (Container): service locator with mock services.
    """
    command = commands.UserConfirmPasswordResetCommand(
        user_id=uuid.uuid4(),
        key=uuid.uuid4(),
        new_password1=SecretStr("New_password12"),
        new_password2=SecretStr("New_password12"),
    )
    with pytest.raises(EntityNotFound):
        await handlers.confirm_password_reset(
            command=command, svcs_container=svcs_container
        )


async def test_confirm_password_reset_success(
    svcs_container: Container,
) -> None:
    """
    Ensure that the operation confirms and closes an existing
    password reset confirmation on the user and overwrites the password.

    Args:
        svcs_container (Container): service locator with mock services.
    """
    uow, password_crypt = await svcs_container.aget(AbstractUow, AbstractPasswordCrypt)

    existing_email = "existing_email@gmail.com"
    existing_key = uuid.uuid4()
    new_password = "New_password1"

    # Add existing user
    user = User(username="existing_username")
    user.email_create(address=existing_email, max_emails=3, verification=False)
    user.password_reset_confirmation = PasswordResetConfirmation(key=existing_key)
    async with uow:
        await uow.repos.users.add(user)
        await uow.commit()

    command = commands.UserConfirmPasswordResetCommand(
        user_id=user.id_or_error(),
        key=existing_key,
        new_password1=SecretStr(new_password),
        new_password2=SecretStr(new_password),
    )
    await handlers.confirm_password_reset(
        command=command, svcs_container=svcs_container
    )

    async with uow:
        persisted_user = await uow.repos.users.get_by_email_address(existing_email)

    # Assert the user was persisted correctly
    assert (
        isinstance(persisted_user, User)
        and persisted_user.password_reset_confirmation is None
        and await user.verify_password(
            password=new_password, password_crypt=password_crypt
        )
        is True
    )
