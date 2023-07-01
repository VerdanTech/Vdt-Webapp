from litestar import Controller, post

from ..urls import USER_RESET_PASSWORD_CONFIRM_URL, USER_RESET_PASSWORD_REQUEST_URL


class PasswordResetController(Controller):
    """Password reset controller"""

    @post(path=USER_RESET_PASSWORD_REQUEST_URL)
    async def user_reset_password_request():
        pass

    @post(path=USER_RESET_PASSWORD_CONFIRM_URL)
    async def user_reset_password_confirm():
        pass
