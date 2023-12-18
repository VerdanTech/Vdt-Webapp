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
        async with litestar_client as client:
            path = client.app.route_reverse(routes.USER_CREATE_NAME)
            input_data = UserCreateInput(
                username="new_username",
                email_address="new_email@gmail.com",
                password1="New_password*1",
                password2="New_password*1",
            )
            response = await client.post(
                path,
                json=asdict(input_data),
            )
            assert response.status_code == 201
            pass
