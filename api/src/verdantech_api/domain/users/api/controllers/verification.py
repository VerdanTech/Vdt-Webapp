from litestar import Controller, post

from ..urls import (
    USER_EMAIL_VERIFICATION_CONFIRM_URL,
    USER_EMAIL_VERIFICATION_REQUEST_URL,
    USER_PASSWORD_RESET_CONFIRM_URL,
    USER_PASSWORD_RESET_REQUEST_URL,
)


class UserVerificationController(Controller):
    """User verification controller"""

    @post(path=USER_EMAIL_VERIFICATION_REQUEST_URL)
    async def user_email_verification_request():
        pass

    @post(path=USER_EMAIL_VERIFICATION_CONFIRM_URL)
    async def user_email_verification_confirm():
        pass

    @post(path=USER_PASSWORD_RESET_REQUEST_URL)
    async def user_password_reset_request():
        pass

    @post(path=USER_PASSWORD_RESET_CONFIRM_URL)
    async def user_password_reset_confirm():
        pass
