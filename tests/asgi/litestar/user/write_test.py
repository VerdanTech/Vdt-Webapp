# Standard Library
import json
from dataclasses import asdict

# External Libraries
import pytest
from litestar.testing import AsyncTestClient
from sqlalchemy.ext.asyncio import AsyncSession

# VerdanTech Source
from src.asgi.litestar.user import routes
from src.infra.persistence.sqlalchemy.repository.user import UserAlchemyRepository
from src.ops.user.schemas import write as write_ops_schemas

pytestmark = [pytest.mark.asgi]


class TestUserWriteApiController:
    # ================================================================
    # TestUserWriteApiController.user_create() tests
    # ================================================================
    async def test_user_create(
        self,
        litestar_client: AsyncTestClient,
        sql_transaction: AsyncSession
    ) -> None:
        """
        Ensure that the user_create endpoint successfully creates a user
        and returns a response containing the created user.

        Args:
            litestar_client (AsyncTestClient): test client fixture.
        """
        path = litestar_client.app.route_reverse(routes.USER_CREATE_NAME)
        input_data = write_ops_schemas.UserCreateInput(
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

        response = await litestar_client.post(
            path,
            json=asdict(input_data),
        )
        response_dict = json.loads(response.content)

        assert response.status_code == 422


        #user_repo = UserAlchemyRepository(transaction=sql_transaction)
        #def call_user_repo():
            #return user_repo.get_user_by_email_address(email_address=input_data.email_address)
        #async with litestar_client.blocking_portal.call(call_user_repo) as user:
            #assert user is not None
