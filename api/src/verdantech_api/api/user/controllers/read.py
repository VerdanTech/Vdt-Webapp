from litestar import Controller, get

from ..urls import urls


class UserReadController(Controller):
    """User read operations controller"""

    @get(path=urls.USER_LIST_URL)
    async def user_list():
        pass

    @get(path=urls.USER_DETAIL_URL)
    async def user_detail():
        pass

    @get(path=urls.USER_CHECK_USERNAME_URL)
    async def user_check_username():
        pass

    @get(path=urls.USER_CHECK_EMAIL_URL)
    async def user_check_email():
        pass

    @get(path=urls.USER_CHECK_PASSWORD_URL)
    async def user_check_password():
        pass
