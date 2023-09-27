from litestar import Controller, delete, patch, post
from litestar.di import Provide
from src.verdantech_api.api.exceptions import litestar_exception_map
from src.verdantech_api.application.user.operations import (
    UserWriteOperations,
    provide_user_write_operations,
)
from src.verdantech_api.application.user.schemas.api.common import UserSelfDetail
from src.verdantech_api.application.user.schemas.api.write import UserCreateInput
from src.verdantech_api.domain.interfaces.security.crypt import AbstractPasswordCrypt
from src.verdantech_api.domain.models.user.services.sanitization import UserSanitizer
from src.verdantech_api.infrastructure.email.emitter import (
    EmailEmitter,
    provide_litestar_email_emitter,
)

from ..urls import urls


class UserWriteController(Controller):
    """User write operations controller"""

    dependencies = {
        "user_repo": Provide(),
        "user_write_operations": Provide(provide_user_write_operations),
    }

    @post(
        name="users:create",
        summary="User registration",
        description="Register a new user and send an email verification",
        tags=["users"],
        path=urls.USER_CREATE_URL,
        dto=UserCreateInput,
        return_dto=UserSelfDetail,
        dependencies={
            "user_sanitizer": Provide(),
            "password_crypt": Provide(),
            "email_emitter": Provide(provide_litestar_email_emitter),
        },
    )
    async def user_create(
        self,
        data: UserCreateInput,
        user_write_operations: UserWriteOperations,
        user_sanitizer: UserSanitizer,
        email_emitter: EmailEmitter,
        password_crypt: AbstractPasswordCrypt,
    ) -> UserSelfDetail:
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
    async def user_change_username():
        pass

    @patch(path=urls.USER_CHANGE_PASSWORD_URL)
    async def user_change_password():
        pass

    @post(path=urls.USER_EMAIL_CHANGE_REQUEST_URL)
    async def user_email_change_request():
        pass

    @delete(path=urls.USER_DELETE_URL)
    async def user_delete():
        pass
