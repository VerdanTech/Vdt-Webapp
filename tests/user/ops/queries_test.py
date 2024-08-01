# Standard Library
import uuid

# External Libraries
import pytest
from pydantic import SecretStr
from pytest_mock import MockerFixture
from svcs import Container

# VerdanTech Source
from src import settings
from src.common.interfaces.persistence.uow import AbstractUow
from src.common.interfaces.security.passwords import AbstractPasswordCrypt
from src.common.ops.exceptions import EntityNotFound
from src.exceptions import ApplicationException
from src.user.domain.models import User
from src.user.ops import queries

# ======================================
# verify_password() tests
# ======================================


async def test_verify_password_user_not_found(svcs_container: Container) -> None:
    """
    Ensure that when the query is called with an email that does
    not match an existing user, the EntityNotFound exception is raised.

    Args:
        svcs_container (Container): service locator with mock services.
    """
    nonexistant_email = "nonexistant_email@gmail.com"

    query = queries.UserPasswordVerificationQuery(
        email_address=nonexistant_email, password=SecretStr("Test_password1$")
    )

    with pytest.raises(EntityNotFound):
        await queries.verify_password(query=query, svcs_container=svcs_container)


async def test_verify_password_email_confirmation_required(
    svcs_container: Container, mocker: MockerFixture
) -> None:
    """
    Ensure that when the query is called with an email that does
    exist but the user is not verified and email confirmation is required,
    the PasswordVerificationResult returned indicates that email verification is required.

    Args:
        svcs_container (Container): service locator with mock services.
    """
    uow = await svcs_container.aget_abstract(AbstractUow)

    # Ensure the email confirmation setting is set to required
    mocker.patch(
        "src.settings.EMAIL_CONFIRMATION",
        settings.EmailConfirmationOptions.REQUIRED_FOR_LOGIN,
    )

    existing_email = "existing_email@gmail.com"

    # Add existing user
    user = User(username="existing_username")
    user.email_create(address=existing_email, max_emails=3, verification=True)
    async with uow:
        await uow.repos.users.add(user)
        await uow.commit()

    query = queries.UserPasswordVerificationQuery(
        email_address=existing_email, password=SecretStr("Test_password1$")
    )

    result = await queries.verify_password(query=query, svcs_container=svcs_container)

    assert result.verified is False and result.email_verification_required is True


async def test_verify_password_success_incorrect_password(
    svcs_container: Container,
) -> None:
    """
    Ensure that when the query is called with an email that does
    exist and a password which does not match that of the user, the
    PasswordVerificationResult returned indicates that the password is not verified.

    Args:
        svcs_container (Container): service locator with mock services.
    """
    uow, password_crypt = await svcs_container.aget_abstract(
        AbstractUow, AbstractPasswordCrypt
    )

    existing_email = "existing_email@gmail.com"
    existing_password = "Existing_password1$"

    # Add existing user
    user = User(username="existing_username")
    user.email_create(address=existing_email, max_emails=3, verification=False)
    await user.set_password(
        password=existing_password + "incorrect", password_crypt=password_crypt
    )
    async with uow:
        await uow.repos.users.add(user)
        await uow.commit()

    query = queries.UserPasswordVerificationQuery(
        email_address=existing_email, password=SecretStr(existing_password)
    )

    result = await queries.verify_password(query=query, svcs_container=svcs_container)

    assert result.verified is False


async def test_verify_password_success_correct_password(
    svcs_container: Container,
) -> None:
    """
    Ensure that when the query is called with an email that does
    exist and a password which matches that of the user, the
    PasswordVerificationResult returned indicates that the password is verified.

    Args:
        svcs_container (Container): service locator with mock services.
    """
    uow, password_crypt = await svcs_container.aget_abstract(
        AbstractUow, AbstractPasswordCrypt
    )

    existing_email = "existing_email@gmail.com"
    existing_password = "Existing_password1$"

    # Add existing user
    user = User(username="existing_username")
    user.email_create(address=existing_email, max_emails=3, verification=False)
    await user.set_password(password=existing_password, password_crypt=password_crypt)
    async with uow:
        await uow.repos.users.add(user)
        await uow.commit()

    query = queries.UserPasswordVerificationQuery(
        email_address=existing_email, password=SecretStr(existing_password)
    )

    result = await queries.verify_password(query=query, svcs_container=svcs_container)

    assert result.verified is True


# ======================================
# public_profiles() tests
# ======================================


async def test_public_profiles_success(svcs_container: Container) -> None:
    """
    Ensure that the profiles query returns a list of public user schemas.

    Args:
        svcs_container (Container): service locator with mock services.
    """
    uow = await svcs_container.aget_abstract(AbstractUow)

    # Add existing users
    users = [User(username="user1"), User(username="user2"), User(username="user3")]
    async with uow:
        for user in users:
            await uow.repos.users.add(user)
        await uow.commit()

    nonexistant_id = uuid.uuid4()
    query = queries.UserPublicProfilesQuery(
        user_ids=[user.id_or_error() for user in users]
    )
    query.user_ids.append(nonexistant_id)

    result = await queries.public_profiles(query=query, svcs_container=svcs_container)

    assert (
        queries.UserPublicSchema.cast(users[0]) in result
        and queries.UserPublicSchema.cast(users[1]) in result
        and queries.UserPublicSchema.cast(users[2]) in result
        and nonexistant_id not in [user.id for user in result]
    )


# ======================================
# client_profile() tests
# ======================================


async def test_client_profile_no_client(svcs_container: Container) -> None:
    """
    Ensure that the method raises an exception for no client user.

    Args:
        svccs_container (Container): service locator with mock services.
    """
    client = None
    with pytest.raises(ApplicationException):
        await queries.client_profile(client=client)  # type: ignore


async def test_client_profile_success(svcs_container: Container, user: User) -> None:
    """
    Ensure that the method returns the client user's full schema.

    Args:
        svcs_container (Container): service locator with mock services.
    """
    result = await queries.client_profile(client=user)
    assert result == queries.UserFullSchema.cast(user)
