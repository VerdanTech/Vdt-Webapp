# Standard Library
import uuid
from dataclasses import asdict

# External Libraries
import pytest
from litestar.testing import AsyncTestClient
from svcs import Container

# VerdanTech Source
from src import settings
from src.user.domain import PasswordResetConfirmation, User
from src.user.domain.email import Email, EmailConfirmation
from src.gateway.litestar.user import routes
from src.interfaces.persistence.user.user import AbstractUserRepository
from src.ops.user.schemas import verification as verification_ops_schemas
from src.utils.key_generator import key_generator

pytestmark = [pytest.mark.asgi]


class TestUserVerificationApiController:
    # ================================================================
    # UserVerificationApiController.user_email_confirmation_request() tests
    # ================================================================
    async def test_user_email_confirmation_request_404_nonexistant_user(
        self, litestar_client: AsyncTestClient
    ) -> None:
        """
        Ensure that the user_email_confirmation_request endpoint returns
        a failure status code when no email_address exists.

        Args:
            litestar_client (AsyncTestClient): test client fixture.
            user_repo (AbstractUserRepository): user repository fixture.
        """
        path = litestar_client.app.route_reverse(
            routes.USER_EMAIL_VERIFICATION_REQUEST_NAME
        )
        input_data = verification_ops_schemas.UserVerifyEmailRequestInput(
            email_address="nonexistant_email@gmail.com"
        )

        response = await litestar_client.post(
            path,
            json=asdict(input_data),
        )

        assert response.status_code == 404

    async def test_user_email_confirmation_request_201_success(
        self,
        user: User,
        litestar_client: AsyncTestClient,
        svcs_container: Container,
    ) -> None:
        """
        Ensure that the user_email_confirmation_request endpoint returns
        a success status code.

        Args:
            litestar_client (AsyncTestClient): test client fixture.
            user_repo (AbstractUserRepository): user repository fixture.
        """
        user_repo = await svcs_container.aget(AbstractUserRepository)

        email_address = "existing_email@gmail.com"
        user.emails = [Email(address=email_address, confirmation=None, verified=False)]
        await user_repo.add(user)

        path = litestar_client.app.route_reverse(
            routes.USER_EMAIL_VERIFICATION_REQUEST_NAME
        )
        input_data = verification_ops_schemas.UserVerifyEmailRequestInput(
            email_address=email_address
        )

        response = await litestar_client.post(
            path,
            json=asdict(input_data),
        )
        persisted_user = await user_repo.get_user_by_email_address(
            email_address=email_address
        )

        assert response.status_code == 201
        assert (
            persisted_user is not None
            and persisted_user.emails[0].confirmation is not None
        )

    # ================================================================
    # UserVerificationApiController.user_email_confirmation_confirm() tests
    # ================================================================

    async def test_user_email_confirmation_confirm_404_nonexistant_user(
        self, litestar_client: AsyncTestClient
    ) -> None:
        """
        Ensure that the user_email_confirmation_confirm endpoint returns
        a failure status code when no key exists.

        Args:
            litestar_client (AsyncTestClient): test client fixture.
        """
        nonexistant_valid_key = key_generator(
            length=settings.VERIFICATION_KEY_MAX_LENGTH
        )

        path = litestar_client.app.route_reverse(
            routes.USER_EMAIL_VERIFICATION_CONFIRM_NAME
        )
        input_data = verification_ops_schemas.UserVerifyEmailConfirmInput(
            key=nonexistant_valid_key
        )

        response = await litestar_client.post(
            path,
            json=asdict(input_data),
        )

        assert response.status_code == 404

    async def test_user_email_confirmation_confirm_201_success(
        self,
        user: User,
        litestar_client: AsyncTestClient,
        svcs_container: Container,
    ) -> None:
        """
        Ensure that the user_email_confirmation_confirm endpoint returns
        a success status code.

        Args:
            litestar_client (AsyncTestClient): test client fixture.
        """
        user_repo = await svcs_container.aget(AbstractUserRepository)

        email_address = "existing_email@gmail.com"
        existing_valid_key = key_generator(length=settings.VERIFICATION_KEY_MAX_LENGTH)
        user.emails = [
            Email(
                address=email_address,
                confirmation=EmailConfirmation(key=existing_valid_key),
                verified=False,
            )
        ]
        await user_repo.add(user)

        path = litestar_client.app.route_reverse(
            routes.USER_EMAIL_VERIFICATION_CONFIRM_NAME
        )
        input_data = verification_ops_schemas.UserVerifyEmailConfirmInput(
            key=existing_valid_key
        )

        response = await litestar_client.post(
            path,
            json=asdict(input_data),
        )
        persisted_user = await user_repo.get_user_by_email_address(
            email_address=email_address
        )

        assert response.status_code == 201
        assert (
            persisted_user is not None
            and persisted_user.emails[0].confirmation is None
            and persisted_user.emails[0].verified is True
        )

    # ================================================================
    # UserVerificationApiController.user_password_reset_request() tests
    # ================================================================

    async def test_user_password_reset_request_404_nonexistant_user(
        self, litestar_client: AsyncTestClient
    ) -> None:
        """
        Ensure that the user_password_reset_request endpoint returns
        a failure status code when no email_address exists.

        Args:
            litestar_client (AsyncTestClient): test client fixture.
            user_repo (AbstractUserRepository): user repository fixture.
        """
        path = litestar_client.app.route_reverse(
            routes.USER_PASSWORD_RESET_REQUEST_NAME
        )
        input_data = verification_ops_schemas.UserPasswordResetRequestInput(
            email_address="nonexistant_email@gmail.com"
        )

        response = await litestar_client.post(
            path,
            json=asdict(input_data),
        )

        assert response.status_code == 404

    async def test_user_password_reset_request_201_success(
        self,
        user: User,
        litestar_client: AsyncTestClient,
        svcs_container: Container,
    ) -> None:
        """
        Ensure that the user_password_reset_request endpoint returns
        a success status code.

        Args:
            litestar_client (AsyncTestClient): test client fixture.
            user_repo (AbstractUserRepository): user repository fixture.
        """
        user_repo = await svcs_container.aget(AbstractUserRepository)
        await user_repo.add(user)

        path = litestar_client.app.route_reverse(
            routes.USER_PASSWORD_RESET_REQUEST_NAME
        )
        input_data = verification_ops_schemas.UserPasswordResetRequestInput(
            email_address=user.primary_email.address
        )

        response = await litestar_client.post(
            path,
            json=asdict(input_data),
        )
        persisted_user = await user_repo.get_user_by_email_address(
            email_address=user.primary_email.address
        )

        assert response.status_code == 201
        assert (
            persisted_user is not None
            and persisted_user.password_reset_confirmation is not None
        )

    # ================================================================
    # UserVerificationApiController.user_password_reset_confirm() tests
    # ================================================================
    @pytest.mark.skip
    async def test_user_password_reset_confirm_404_nonexistant_user(
        self, litestar_client: AsyncTestClient
    ) -> None:
        """
        Ensure that the user_password_reset_confirm endpoint returns
        a failure status code when no key exists.

        Args:
            litestar_client (AsyncTestClient): test client fixture.
        """
        nonexistant_valid_key = key_generator(
            length=settings.VERIFICATION_KEY_MAX_LENGTH
        )

        path = litestar_client.app.route_reverse(
            routes.USER_PASSWORD_RESET_CONFIRM_NAME
        )
        input_data = verification_ops_schemas.UserPasswordResetConfirmInput(
            user_id=uuid.uuid4(),
            key=nonexistant_valid_key,
            new_password1="New_password*1",
            new_password2="New_password*1",
        )

        response = await litestar_client.post(
            path,
            json=asdict(input_data),
        )

        assert response.status_code == 404

    async def test_user_password_reset_confirm_201_success(
        self, user: User, litestar_client: AsyncTestClient, svcs_container: Container
    ) -> None:
        """
        Ensure that the user_password_reset_confirm endpoint returns
        a success status code.

        Args:
            litestar_client (AsyncTestClient): test client fixture.
        """
        user_repo = await svcs_container.aget(AbstractUserRepository)

        existing_valid_key = key_generator(length=settings.VERIFICATION_KEY_MAX_LENGTH)
        new_password = "New_password*1"
        user.password_reset_confirmation = PasswordResetConfirmation(
            key=existing_valid_key
        )
        await user_repo.add(user)

        path = litestar_client.app.route_reverse(
            routes.USER_PASSWORD_RESET_CONFIRM_NAME
        )
        input_data = verification_ops_schemas.UserPasswordResetConfirmInput(
            user_id=user.id_or_error(),
            key=existing_valid_key,
            new_password1=new_password,
            new_password2=new_password,
        )

        response = await litestar_client.post(
            path,
            json=asdict(input_data),
        )
        persisted_user = await user_repo.get_user_by_email_address(
            email_address=user.emails[0].address
        )

        assert response.status_code == 201
        assert (
            persisted_user is not None
            and persisted_user.password_reset_confirmation is None
        )
