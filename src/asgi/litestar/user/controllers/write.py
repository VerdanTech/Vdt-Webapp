
# External Libraries
from litestar import Controller, post
from litestar.datastructures import State
from litestar.params import Dependency
from svcs import Container

# VerdanTech Source
from src.asgi.litestar.exceptions import litestar_exception_map
from src.domain.user.entities import User
from src.domain.user.sanitizers import UserSanitizer
from src.interfaces.email.emitter import AbstractEmailEmitter
from src.interfaces.security.crypt.password_crypt import AbstractPasswordCrypt
from src.ops.user.controllers.write import UserWriteOpsController
from src.ops.user.schemas import write as write_ops_schemas

from .. import routes, schemas, urls


class UserWriteApiController(Controller):
    """
    User write ASGI controller.
    """

    path = urls.USER_WRITE_CONTROLLER_URL_BASE

    @post(
        name=routes.USER_CREATE_NAME,
        summary="User registration",
        description="Register a new user and send an email verification if configured.",
        tags=["users"],
        path=urls.USER_CREATE_URL,
        return_dto=schemas.UserSelfDetail,
    )
    async def user_create(
        self,
        data: write_ops_schemas.UserCreateInput,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> User:
        """
        Calls the user creation application operation.

        Args:
            data (UserCreateInput): input DTO.
            svcs_container (Container): svcs service
                locator container.

        Returns:
            UserSelfDetail: user self-reference DTO.
        """
        svcs_container.register_local_value(State, state)
        user_write_ops_controller, user_sanitizer = await svcs_container.aget(
            UserWriteOpsController, UserSanitizer
        )
        email_emitter, password_crypt = await svcs_container.aget_abstract(
            AbstractEmailEmitter, AbstractPasswordCrypt
        )
        async with litestar_exception_map():
            user = await user_write_ops_controller.create(
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
