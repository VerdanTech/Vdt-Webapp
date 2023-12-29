# External Libraries
from litestar import Controller, Response, post
from litestar.datastructures import State
from svcs import Container

# VerdanTech Source
from src.asgi.litestar.auth import jwt_cookie_auth
from src.domain.user.entities import User
from src.domain.user.sanitizers import UserSanitizer
from src.interfaces.persistence.user.repository import AbstractUserRepository
from src.interfaces.security.crypt import AbstractPasswordCrypt

from .. import routes, schemas, urls


class UserAuthController(Controller):
    """User authentication operations controller"""

    path = urls.USER_AUTH_CONTROLLER_BASE

    @post(
        name=routes.USER_LOGIN_NAME,
        opt={"exclude_from_auth": True},
        summary="User login",
        description="Authenticate the request with JWT cookie authentication.",
        tags=["users"],
        path=urls.USER_LOGIN_URL,
        return_dto=schemas.UserSelfDetail,
    )
    async def user_login(
        self, data: schemas.UserLoginInput, state: State, svcs_container: Container
    ) -> Response[User]:
        svcs_container.register_local_value(State, state)
        user_sanitizer = await svcs_container.aget(UserSanitizer)
        user_repo, password_crypt = await svcs_container.aget_abstract(
            AbstractUserRepository, AbstractPasswordCrypt
        )

        await data.sanitize(user_sanitizer=user_sanitizer)

        user = await user_repo.get_user_by_email_address(
            email_address=data.email_address
        )

        if user is None:
            pass

        if not user.verify_password(
            password=data.password, password_crypt=password_crypt
        ):
            pass

        return jwt_cookie_auth.login(identifier=str(user.id), response_body=user)
