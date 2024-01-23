# Standard Library
from typing import Optional
from uuid import UUID

# External Libraries
from litestar import Controller, Request, get
from litestar.datastructures import State
from litestar.params import Dependency
from svcs import Container

# VerdanTech Source
from src.asgi.litestar.exceptions import ClientError, litestar_exception_map
from src.domain.common import EntityIdType
from src.ops.user.controllers import UserReadOpsController
from src.ops.user.schemas.read import UserFullSchema, UserPublicSchema

from .. import routes, urls


class UserReadController(Controller):
    """User read operations controller"""

    path = urls.USER_READ_CONTROLLER_URL_BASE
    tags = ["users"]

    @get(
        path=urls.USER_PROFILES_URL,
        name=routes.USER_PROFILES_NAME,
        summary="User profiles view.",
        description="Returns the profiles of the user ids given. Returns an error if a user does not exist. If no user ids are provided, the client's profile is returned.",
        response_description="The list of users requested, or the client user.",
        operation_id=routes.USER_PROFILES_NAME,
    )
    async def user_profiles(
        self,
        request: Request,
        user_ids: Optional[list[UUID]],
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> list[UserPublicSchema] | UserFullSchema:
        svcs_container.register_local_value(State, state)
        user_read_ops_controller = await svcs_container.aget(UserReadOpsController)
        with litestar_exception_map():
            user_schemas = await user_read_ops_controller.profiles(
                client=request.user, user_ids=user_ids
            )
        return user_schemas
