from typing import TYPE_CHECKING

from litestar import Controller, get
from litestar.di import Provide

from verdantech_api.lib.crypt import provide_password_crypt
from verdantech_api.lib.email import provide_email_client

from ..urls import USER_CHECK_USERNAME_AVAILABLE_URL, USER_DETAIL_URL, USER_LIST_URL

if TYPE_CHECKING:
    from ..services.users import UserService


class UserReadController(Controller):
    """User read operations controller"""

    @get(operation_id="user_list", path=USER_LIST_URL)
    async def user_list(user_service: UserService):
        pass

    @get(path=USER_DETAIL_URL)
    async def user_detail(user_service: UserService):
        pass

    @get(path=USER_CHECK_USERNAME_AVAILABLE_URL)
    async def user_check_username(user_service: UserService):
        pass
