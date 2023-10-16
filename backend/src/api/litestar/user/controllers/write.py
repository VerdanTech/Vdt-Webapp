from litestar import Controller, delete, patch, post
from src import settings
from src.api.litestar import dependencies
from src.api.litestar.exceptions import litestar_exception_map
from src.api.litestar.user.schemas.common import UserSelfDetail
from src.application.user.operations import UserWriteOperations
from src.application.user.schemas.api.write import UserCreateInput
from src.interfaces.security.crypt import AbstractPasswordCrypt
from src.domain.user.entities import User
from src.domain.user.services.sanitization import UserSanitizer
from src.infrastructure.email.litestar_emitter import EmailEmitter

from .. import urls


class UserWriteController(Controller):
    """User write operations controller"""

    path = urls.USER_WRITE_CONTROLLER_URL_BASE
    """dependencies = providers.select(
        settings.USER_REPOSITORY_PK, settings.USER_WRITE_OP_PK
    )"""
    dependencies = dependencies.select(settings.USER_SERIALIZER_PK)

    @post(
        name="users:create",
        summary="User registration",
        description="Register a new user and send an email verification",
        tags=["users"],
        path=urls.USER_CREATE_URL,
        return_dto=UserSelfDetail,
        # dependencies=providers.select(
        # settings.USER_SANITIZER_PK,
        # settings.PASSWORD_CRYPT_PK,
        # settings.EMAIL_CLIENT_PK,
        # settings.EMAIL_EMITTER_PK,
        # ),
    )
    async def user_create(
        self,
        data: UserCreateInput,
        user_write_operations: UserWriteOperations,
        user_sanitizer: UserSanitizer,
        email_emitter: EmailEmitter,
        password_crypt: AbstractPasswordCrypt,
    ) -> User:
        """Call the main user creation application operation

        Args:
            data (UserCreateInput): input DTO
            user_write_operations (UserWriteOperations):
                application operations
            user_sanitizer (UserSanitizer): user sanitizer
            email_emitter (EmailEmitter): email emitter
            password_crypt (AbstractPasswordCrypt): password crypt

        Returns:
            UserSelfDetail: user self-reference DTO
        """
        async with litestar_exception_map:
            user = await user_write_operations.create(
                data=data,
                user_sanitizer=user_sanitizer,
                password_crypt=password_crypt,
                email_emitter=email_emitter,
            )
        return user

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
