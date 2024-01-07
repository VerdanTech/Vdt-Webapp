# Standard Library
from dataclasses import asdict

# External Libraries
import pytest
from litestar.testing import AsyncTestClient

# VerdanTech Source
from src.asgi.litestar.user import routes
from src.domain.user.entities import User
from src.domain.user.values import Email
from src.interfaces.persistence.user.repository import AbstractUserRepository
from src.ops.user.schemas import verification as verification_ops_schemas

pytestmark = [pytest.mark.asgi]


class TestUserVerificationApiController:
    # ================================================================
    # UserVerificationApiController.user_email_confirmation_request() tests
    # ================================================================
    async def test_user_email_confirmation_request_404_nonexistant_user(
        self, litestar_client: AsyncTestClient, user_repo: AbstractUserRepository
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
            email_address="existing_email@gmail.com"
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
        user_repo: AbstractUserRepository,
    ) -> None:
        """
        Ensure that the user_email_confirmation_request endpoint returns
        a success status code.

        Args:
            litestar_client (AsyncTestClient): test client fixture.
            user_repo (AbstractUserRepository): user repository fixture.
        """
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
    async def test_user_email_confirmation_confirm_success(
        self, litestar_client: AsyncTestClient
    ) -> None:
        """
        Ensure that the user_email_confirmation_confirm endpoint returns
        a success status code.

        Args:
            litestar_client (AsyncTestClient): test client fixture.
        """
        pass

    # ================================================================
    # UserVerificationApiController.user_password_reset_request() tests
    # ================================================================
    async def test_user_password_reset_request_success(
        self, litestar_client: AsyncTestClient
    ) -> None:
        """
        Ensure that the user_password_reset_request endpoint returns
        a success status code.

        Args:
            litestar_client (AsyncTestClient): test client fixture.
        """
        pass

    # ================================================================
    # UserVerificationApiController.user_password_reset_confirm() tests
    # ================================================================
    async def test_user_password_reset_confirm_success(
        self, litestar_client: AsyncTestClient
    ) -> None:
        """
        Ensure that the user_password_reset_confirm endpoint returns
        a success status code.

        Args:
            litestar_client (AsyncTestClient): test client fixture.
        """
        pass
