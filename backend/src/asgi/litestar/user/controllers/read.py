# External Libraries
from litestar import Controller, get

from .. import urls


class UserReadController(Controller):
    """User read operations controller"""

    path = urls.USER_READ_CONTROLLER_URL_BASE

    @get(path=urls.USER_LIST_URL)
    async def user_list() -> None:
        pass

    @get(path=urls.USER_DETAIL_URL)
    async def user_detail() -> None:
        pass

    @get(path=urls.USER_CHECK_USERNAME_URL)
    async def user_check_username() -> None:
        pass

    @get(path=urls.USER_CHECK_EMAIL_URL)
    async def user_check_email() -> None:
        pass

    @get(path=urls.USER_CHECK_PASSWORD_URL)
    async def user_check_password() -> None:
        pass
