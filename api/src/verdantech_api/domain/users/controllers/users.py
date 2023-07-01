from litestar import Controller, delete, get, patch, post

from ..urls import (
    USER_CHANGE_USERNAME_URL,
    USER_CHECK_USERNAME_AVAILABLE_URL,
    USER_CREATE_URL,
    USER_DELETE_URL,
    USER_DETAIL_URL,
    USER_LIST_URL,
)


class UserController(Controller):
    """User controller"""

    @get(path=USER_LIST_URL)
    async def user_list():
        pass

    @get(path=USER_DETAIL_URL)
    async def user_detail():
        pass

    @get(path=USER_CHECK_USERNAME_AVAILABLE_URL)
    async def user_check_username_available():
        pass

    @post(path=USER_CREATE_URL)
    async def user_create():
        pass

    @patch(path=USER_CHANGE_USERNAME_URL)
    async def user_change_username():
        pass

    @delete(path=USER_DELETE_URL)
    async def user_delete():
        pass
