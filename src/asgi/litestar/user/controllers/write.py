# External Libraries
from litestar import Controller, delete, patch, post

# VerdanTech Source
from src import settings
from src.asgi.litestar import select_dependencies
from src.asgi.litestar.exceptions import litestar_exception_map
from src.domain.user.entities import User
from src.domain.user.sanitizers import UserSanitizer
from src.interfaces.email.emitter import AbstractEmailEmitter
from src.interfaces.security.crypt import AbstractPasswordCrypt
from src.ops.user.controllers import UserWriteOpsController
from src.ops.user.schemas import write as write_schemas

from .. import schemas, urls


class UserWriteApiController(Controller):
    """User write api controller"""

    path = urls.USER_WRITE_CONTROLLER_URL_BASE
    #dependencies = select_dependencies(
        #settings.USER_REPOSITORY_PK, 
        #settings.USER_WRITE_OP_PK
    #)

    @post(
        name="users:create",
        summary="User registration",
        description="Register a new user and send an email verification",
        tags=["users"],
        path=urls.USER_CREATE_URL,
        return_dto=schemas.UserSelfDetail,
        #dependencies=select_dependencies(
            #settings.USER_SANITIZER_PK,
            #settings.PASSWORD_CRYPT_PK,
            #settings.EMAIL_CLIENT_PK,
            #settings.EMAIL_EMITTER_PK,
        #),
    )
    async def user_create(
        self,
        data: write_schemas.UserCreateInput,
        user_write_operations: UserWriteOpsController,
        user_sanitizer: UserSanitizer,
        email_emitter: AbstractEmailEmitter,
        password_crypt: AbstractPasswordCrypt,
    ) -> User:
        """
        Call the main user creation application operation.

        Args:
            data (UserCreateInput): input DTO.
            user_write_operations (UserWriteOpsController):
                application operations.
            user_sanitizer (UserSanitizer): user sanitizer.
            email_emitter (EmailEmitter): email emitter.
            password_crypt (AbstractPasswordCrypt): password crypt.

        Returns:
            UserSelfDetail: user self-reference DTO.
        """
        async with litestar_exception_map:
            user = await user_write_operations.create(
                data=data,
                user_sanitizer=user_sanitizer,
                password_crypt=password_crypt,
                email_emitter=email_emitter,
            )
        return user

    """
    @patch(path=urls.USER_CHANGE_USERNAME_URL)
    async def user_change_username() -> None:
        pass

    @patch(path=urls.USER_CHANGE_PASSWORD_URL)
    async def user_change_password() -> None:
        pass

    @post(path=urls.USER_EMAIL_CHANGE_REQUEST_URL)
    async def user_email_change_request() -> None:
        pass

    @delete(path=urls.USER_DELETE_URL)
    async def user_delete() -> None:
        pass
    """