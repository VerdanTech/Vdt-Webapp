from litestar import Controller, post

from ..urls import USER_LOGIN_URL, USER_LOGOUT_URL


class AuthController(Controller):
    """Authentication controller"""

    @post(path=USER_LOGIN_URL)
    async def login():
        pass

    @post(path=USER_LOGOUT_URL)
    async def logout():
        pass
