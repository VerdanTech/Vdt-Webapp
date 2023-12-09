from dataclasses import asdict
from src.asgi.litestar.user import urls, routes
from src.ops.user.schemas.write import UserCreateInput
import pytest
from litestar.testing import AsyncTestClient

class TestUserWriteApiController:
    async def test_create(self, litestar_client: AsyncTestClient) -> None:
        path = litestar_client.app.route_reverse(routes.USER_CREATE_NAME)
        #input_data = UserCreateInput(username="new_username", email_address="new_email@gmail.com", password1="New_password*1", password2="New_password*1")
        #request = asdict(input_data)
        #response = await litestar_client.post(path, data=request)
        #print(response)
        #assert 1 == 2
        pass