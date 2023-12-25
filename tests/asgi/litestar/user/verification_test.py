# Standard Library
import json
from dataclasses import asdict

# External Libraries
import pytest
from litestar.testing import AsyncTestClient

# VerdanTech Source
from src import settings
from src.asgi.litestar.user import routes, urls
from src.ops.user.schemas import verification as verification_ops_schemas
from src.utils.key_generator import key_generator

pytestmark = [pytest.mark.integration]

class TestUserVerificationApiController:
    # ================================================================
    # UserVerificationApiController.user_email_confirmation_request() tests
    # ================================================================
    async def test_user_email_confirmation_request(self, litestar_client: AsyncTestClient) -> None:
        """
        Ensure that the user_email_confirmation_request endpoint returns
        a success status code.

        Args:
            litestar_client (AsyncTestClient): test client fixture.
        """
        path = litestar_client.app.route_reverse(routes.USER_EMAIL_VERIFICATION_REQUEST_NAME)
        input_data = verification_ops_schemas.UserVerifyEmailRequestInput(
            email_address="existing_email@gmail.com"
        )

        response = await litestar_client.post(
            path,
            json=asdict(input_data),
        )

        assert response.status_code == 422


    # ================================================================
    # UserVerificationApiController.user_email_confirmation_confirm() tests
    # ================================================================
    async def test_user_email_confirmation_confirm(self, litestar_client: AsyncTestClient) -> None:
        """
        Ensure that the user_email_confirmation_confirm endpoint returns
        a success status code.

        Args:
            litestar_client (AsyncTestClient): test client fixture.
        """
        path = litestar_client.app.route_reverse(routes.USER_EMAIL_VERIFICATION_CONFIRM_NAME)

    # ================================================================
    # UserVerificationApiController.user_password_reset_request() tests
    # ================================================================
    async def test_user_password_reset_request(self, litestar_client: AsyncTestClient) -> None:
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
    async def test_user_password_reset_confirm(self, litestar_client: AsyncTestClient) -> None:
        """
        Ensure that the user_password_reset_confirm endpoint returns
        a success status code.

        Args:
            litestar_client (AsyncTestClient): test client fixture.
        """
        pass