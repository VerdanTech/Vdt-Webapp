# Standard Library
import json
from dataclasses import asdict

# External Libraries
import pytest
from litestar.testing import AsyncTestClient

# VerdanTech Source
from src.asgi.litestar.user import routes, urls
from src.ops.user.schemas.write import UserCreateInput


@pytest.mark.skip
class TestUserWriteApiController:
    async def test_create(self, litestar_client: AsyncTestClient) -> None:
        path = litestar_client.app.route_reverse(routes.USER_CREATE_NAME)
        input_data = UserCreateInput(
            username="new_username",
            email_address="new_email@gmail.com",
            password1="New_password*1",
            password2="New_password*1",
        )
        print(asdict(input_data))
        response = await litestar_client.post(
            path,
            json=asdict(input_data),
        )
        print(response)
        assert response.status_code == 201
        pass
