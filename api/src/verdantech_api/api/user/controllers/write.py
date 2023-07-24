from typing import TYPE_CHECKING

from litestar import Controller, Request, delete, get, patch, post
from litestar.di import Provide
from src.verdantech_api.application.user.operations.write import UserWriteOperations
from src.verdantech_api.infrastructure.email.emitter import (
    EmailEmitter,
    provide_litestar_email_emitter,
)
from src.verdantech_api.infrastructure.security.interfaces import AbstractPasswordCrypt

from ..schema import UserCreateInput, UserOutput
from ..urls import (
    USER_CHANGE_URL,
    USER_CREATE_URL,
    USER_DELETE_URL,
    USER_EMAIL_CHANGE_REQUEST_URL,
)


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
        user_write_operations: UserWriteOperations,
        email_emitter: EmailEmitter,
        password_crypt: AbstractPasswordCrypt,
    ):
        try:
            user = await user_write_operations.create(
                data=data,
                password_crypt=password_crypt,
                email_emitter=email_emitter,
            )
        except Exception:
            pass
        return user

    @patch(path=USER_CHANGE_URL)
    async def user_change():
        pass

    @post(path=USER_EMAIL_CHANGE_REQUEST_URL)
    async def user_email_change_request():
        pass

    @delete(path=USER_DELETE_URL)
    async def user_delete():
        pass
