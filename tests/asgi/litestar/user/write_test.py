# Standard Library
import json
from dataclasses import asdict

# External Libraries
import pytest
from litestar.testing import AsyncTestClient

# VerdanTech Source
from src.asgi.litestar.user import routes, urls
from src.ops.user.schemas.write import UserCreateInput

pytestmark = [pytest.mark.integration]


class TestUserWriteApiController:
    async def test_create(self, litestar_client: AsyncTestClient) -> None:
        """
        Ensure that the test_create endpoint successfully creates a user
        and returns a response containing the created user.

        Args:
            litestar_client (AsyncTestClient): test client fixture.
        """
        path = litestar_client.app.route_reverse(routes.USER_CREATE_NAME)
        input_data = UserCreateInput(
            username="new_username",
            email_address="new_email@gmail.com",
            password1="New_password*1",
            password2="New_password*1",
        )

        response = await litestar_client.post(
            path,
            json=asdict(input_data),
        )
        response_dict = json.loads(response.content)

        assert response.status_code == 201
        assert (
            response_dict["username"] == input_data.username
            and response_dict["emails"][0]["address"] == input_data.email_address
        )
