from litestar import Controller, delete, get, patch, post


class UserController(Controller):
    """User controller"""

    pass

    async def user_list():
        pass

    async def user_detail():
        pass

    async def user_check_username_available():
        pass

    async def user_create():
        pass

    async def user_verify_email():
        pass

    async def user_resend_email_verification():
        pass

    async def user_reset_password_request():
        pass

    async def user_reset_password_confirm():
        pass

    async def user_update():
        pass

    async def user_delete():
        pass


class AuthController(Controller):
    """Authentication controller"""

    async def login():
        pass

    async def logout():
        pass
