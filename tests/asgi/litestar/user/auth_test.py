# Standard Library
import json
from dataclasses import asdict

# External Libraries
import pytest
from litestar.testing import AsyncTestClient

# VerdanTech Source
from src.asgi.litestar.user import routes
from src.ops.user.schemas import auth as auth_ops_schemas

pytestmark = [pytest.mark.integration]


class TestUserAuthApiController:
    # ================================================================
    # TestUserAuthApiController.user_login() tests
    # ================================================================
    async def test_user_not_found_404(self, litestar_client: AsyncTestClient) -> None:
        """
        Ensure that the user_login() endpoint successfully returns the 404 status code
        when and an empty response body when the user does not exist.

        Args:
            litestar_client (AsyncTestClient): test client fixture.
        """
        nonexistant_valid_email_address = "nonexistant_email@gmail.com"
        path = litestar_client.app.route_reverse(routes.USER_LOGIN_NAME)
        input_data = auth_ops_schemas.UserLoginInput(
            email_address=nonexistant_valid_email_address,
            password="password*1",
        )

        response = await litestar_client.post(
            path,
            json=asdict(input_data),
        )

        assert response.status_code == 404