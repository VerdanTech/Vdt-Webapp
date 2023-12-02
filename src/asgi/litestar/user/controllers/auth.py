# External Libraries
from litestar import Controller, get

from .. import urls


class UserAuthController(Controller):
    """User authentication operations controller"""

    path = urls.USER_AUTH_CONTROLLER_BASE

    @get(path=urls.USER_LOGIN_URL)
    async def user_login() -> None:
        pass

    @get(path=urls.USER_LOGOUT_URL)
    async def user_logout() -> None:
        pass
