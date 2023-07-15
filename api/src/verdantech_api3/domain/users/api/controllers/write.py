from typing import TYPE_CHECKING

from litestar import Controller, Request, delete, get, patch, post
from litestar.di import Provide
from src.verdantech_api.lib.crypt import provide_password_crypt
from src.verdantech_api.lib.email import provide_email_client
from src.verdantech_api.lib.field_validators import (
    provide_email_validator,
    provide_password_validator,
    provide_username_validator,
)
from src.verdantech_api.lib.utils import strid_generator

from ..schemas import UserCreateInput, UserOutput
from ..urls import (
    USER_CHANGE_URL,
    USER_CREATE_URL,
    USER_DELETE_URL,
    USER_EMAIL_CHANGE_URL,
)

if TYPE_CHECKING:
    from ..services.users import UserService


class UserWriteController(Controller):
    """User write operations controller"""

    @post(
        name="users:create",
        summary="Register a new user",
        description="Register a new user and send an email verification",
        tags=["users"],
        dto=UserCreateInput,
        return_dto=UserOutput,
        path=USER_CREATE_URL,
    )
    async def user_create(
        data: UserCreateInput,
        request: Request,
    ):
        pass

    @post(path=USER_EMAIL_CHANGE_URL)
    async def user_email_change():
        pass

    @patch(path=USER_CHANGE_URL)
    async def user_change(user_service: UserService):
        pass

    @delete(path=USER_DELETE_URL)
    async def user_delete(user_service: UserService):
        pass
