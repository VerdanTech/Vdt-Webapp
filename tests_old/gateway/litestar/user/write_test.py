# Standard Library
import json
from dataclasses import asdict

# External Libraries
import pytest
from litestar.testing import AsyncTestClient
from svcs import Container

# VerdanTech Source
from src.gateway.litestar.user import routes
from src.interfaces.persistence.user.user import AbstractUserRepository
from src.ops.user.schemas import write as write_ops_schemas

pytestmark = [pytest.mark.asgi]


class TestUserWriteApiController:
    # ================================================================
    # TestUserWriteApiController.user_create() tests
    # ================================================================
    async def test_user_create_422_failure(
        self, litestar_client: AsyncTestClient, svcs_container: Container
    ) -> None:
        """
        Ensure that the user_create endpoint successfully returns a 422 status
        code when a user is attempted to be created with fields that already exist.

        Args:
            litestar_client (AsyncTestClient): test client fixture.
            user_repo (AbstractUserRepository): user repository fixture.
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
        response = await litestar_client.post(
            path,
            json=asdict(input_data),
        )
        assert response.status_code == 422

    async def test_user_create_201_success(
        self, litestar_client: AsyncTestClient, svcs_container: Container
    ) -> None:
        """
        Ensure that the user_create endpoint successfully creates a user
        and returns a response containing the created user.

        Args:
            litestar_client (AsyncTestClient): test client fixture.
            user_repo (AbstractUserRepository): user repository fixture.
        """
        user_repo = await svcs_container.aget(AbstractUserRepository)
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
        persisted_user = await user_repo.get_user_by_email_address(
            email_address=input_data.email_address
        )

        assert response.status_code == 201
        assert (
            persisted_user is not None
            and response_dict["username"]
            == input_data.username
            == persisted_user.username
            and response_dict["emails"][0]["address"]
            == input_data.email_address
            == persisted_user.emails[0].address
        )
