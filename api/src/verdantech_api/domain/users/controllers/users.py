from typing import TYPE_CHECKING

from litestar import Controller, Request, delete, get, patch, post
from litestar.di import Provide

from verdantech_api.lib.crypt import provide_password_crypt
from verdantech_api.lib.email import provide_email_client
from verdantech_api.lib.utils import strid_generator
from verdantech_api.lib.validators import (
    provide_email_validator,
    provide_password_validator,
    provide_username_validator,
)

from ..dependencies import (
    provide_email_confirmation_repo,
    provide_email_repo,
    provide_email_verification_service,
    provide_user_repo,
    provide_user_service,
)
from ..schemas import UserCreateInput, UserOutput
from ..urls import (
    USER_CHANGE_USERNAME_URL,
    USER_CHECK_USERNAME_AVAILABLE_URL,
    USER_CREATE_URL,
    USER_DELETE_URL,
    USER_DETAIL_URL,
    USER_LIST_URL,
)

if TYPE_CHECKING:
    from ..services.email_verification import EmailVerificationService
    from ..services.users import UserService


class UserController(Controller):
    """User controller"""

    dependencies = {
        "user_repo": Provide(provide_user_repo),
        "email_repo": Provide(provide_email_repo),
        "email_validator": Provide(provide_email_validator),
        "username_validator": Provide(provide_username_validator),
        "password_validator": Provide(provide_password_validator),
        "password_crypt": Provide(provide_password_crypt),
        "user_service": Provide(provide_user_service),
    }

    @get(operation_id="user_list", path=USER_LIST_URL)
    async def user_list(user_service: UserService):
        pass

    @get(path=USER_DETAIL_URL)
    async def user_detail(user_service: UserService):
        pass

    @get(path=USER_CHECK_USERNAME_AVAILABLE_URL)
    async def user_check_username(user_service: UserService):
        pass

    async def user_check_email(user_service: UserService):
        pass

    async def user_check_password(user_service: UserService):
        pass

    @post(
        name="users:create",
        summary="Register a new user",
        description="Register a new user and send an email verification",
        tags=["users"],
        dependencies={
            "email_client": Provide(provide_email_client),
            "email_confirmation_repo": Provide(provide_email_confirmation_repo),
            "key_generator": Provide(strid_generator),
            "email_verification_service": Provide(provide_email_verification_service),
        },
        dto=UserCreateInput,
        return_dto=UserOutput,
        path=USER_CREATE_URL,
    )
    async def user_create(
        user_service: UserService,
        email_verification_service: EmailVerificationService,
        data: UserCreateInput,
        request: Request,
    ):
        # Register user and email in database
        user, email = await user_service.create(
            email=data.email,
            username=data.username,
            password1=data.password1,
            password2=data.password2,
        )
        # Send email verification
        await email_verification_service.send_email_verification(email=email)

        return user

    @patch(path=USER_CHANGE_USERNAME_URL)
    async def user_change_username(user_service: UserService):
        pass

    @delete(path=USER_DELETE_URL)
    async def user_delete(user_service: UserService):
        pass
