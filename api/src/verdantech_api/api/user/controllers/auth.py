from litestar import Controller, get

from ..urls import urls


class UserAuthController(Controller):
    """User authentication operations controller"""

    @get(path=urls.USER_LOGIN_URL)
    async def user_login():
        pass

    @get(path=urls.USER_LOGOUT_URL)
    async def user_logout():
        pass
