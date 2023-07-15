from litestar import Controller, post

from ..urls import (
    USER_REQUEST_EMAIL_CHANGE_URL,
    USER_RESEND_EMAIL_VERIFICATION_URL,
    USER_VERIFY_EMAIL_URL,
)


class EmailVerificationController(Controller):
    """Email verification controller"""

    @post(path=USER_VERIFY_EMAIL_URL)
    async def user_verify_email():
        pass

    @post(path=USER_RESEND_EMAIL_VERIFICATION_URL)
    async def user_resend_email_verification():
        pass

    @post(path=USER_REQUEST_EMAIL_CHANGE_URL)
    async def user_request_email_change():
        pass
