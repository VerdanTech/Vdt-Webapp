# Standard Library
import json
from dataclasses import asdict

# External Libraries
import pytest
from litestar.testing import AsyncTestClient
from svcs import Container

# VerdanTech Source
from src.user.domain import User
from src.gateway.litestar.user import routes
from src.interfaces.persistence.user.user import AbstractUserRepository
from src.interfaces.security.crypt import AbstractPasswordCrypt
from src.ops.user.schemas import auth as auth_ops_schemas

pytestmark = [pytest.mark.asgi]


class TestUserAuthApiController:
    # ================================================================
    # TestUserAuthApiController.user_login() tests
    # ================================================================
    async def test_user_not_found_404_user_not_found(
        self, litestar_client: AsyncTestClient
    ) -> None:
        """
        Ensure that the user_login() endpoint successfully returns the 404 status code
        when the user does not exist.

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

    async def test_user_not_found_401_user_wrong_password(
        self, user: User, litestar_client: AsyncTestClient, svcs_container: Container
    ) -> None:
        """
        Ensure that the user_login() endpoint successfully returns the 401 status code
        when the incorrect password is provided.

        Args:
            litestar_client (AsyncTestClient): test client fixture.
        """
        user_repo, password_crypt = await svcs_container.aget(
            AbstractUserRepository, AbstractPasswordCrypt
        )

        password = "existing_password"
        await user.set_password(
            password=password, password_crypt=password_crypt, overwrite=True
        )
        await user_repo.add(user)

        path = litestar_client.app.route_reverse(routes.USER_LOGIN_NAME)
        input_data = auth_ops_schemas.UserLoginInput(
            email_address=user.emails[0].address,
            password="wrong_password",
        )

        response = await litestar_client.post(
            path,
            json=asdict(input_data),
        )

        assert response.status_code == 401

    async def test_user_not_found_201_success(
        self, user: User, litestar_client: AsyncTestClient, svcs_container: Container
    ) -> None:
        """
        Ensure that the user_login() endpoint successfully returns the 401 status code
        when the correct password is provided.

        Args:
            litestar_client (AsyncTestClient): test client fixture.
        """
        user_repo, password_crypt = await svcs_container.aget(
            AbstractUserRepository, AbstractPasswordCrypt
        )

        password = "existing_password"
        await user.set_password(
            password=password, password_crypt=password_crypt, overwrite=True
        )
        await user_repo.add(user)

        path = litestar_client.app.route_reverse(routes.USER_LOGIN_NAME)
        input_data = auth_ops_schemas.UserLoginInput(
            email_address=user.emails[0].address,
            password=password,
        )

        response = await litestar_client.post(
            path,
            json=asdict(input_data),
        )

        assert response.status_code == 201
