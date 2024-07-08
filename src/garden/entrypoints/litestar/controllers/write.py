# External Libraries
from litestar import Controller, Request, post
from litestar.datastructures import State
from litestar.params import Dependency
from svcs import Container

# VerdanTech Source
from src import settings
from src.common.interfaces.email import AbstractEmailEmitter
from src.common.interfaces.security.crypt.crypt import AbstractPasswordCrypt
from src.entrypoints.litestar import openapi
from src.entrypoints.litestar.exceptions import (
    ClientError,
    ServerError,
    litestar_exception_map,
)
from src.garden.domain.sanitizers import GardenSanitizer
from src.ops.garden.controllers.write import GardenWriteOpsController
from src.ops.garden.schemas import read as read_ops_schemas, write as write_ops_schemas
from src.user.interfaces.persistence.user.user import AbstractUserRepository

from .. import routes, urls


class GardenWriteApiController(Controller):
    """
    Garden write ASGI controller.
    """

    path = urls.GARDEN_WRITE_CONTROLLER_URL_BASE
    tags = ["gardens"]

    @post(
        path=urls.GARDEN_CREATE_URL,
        name=routes.GARDEN_CREATE_NAME,
        summary="Garden creation.",
        description="Creates a new Garden and invites requested users.",
        response_description="The full newly created garden object",
        operation_id=routes.GARDEN_CREATE_NAME,
    )
    async def garden_create(
        self,
        request: Request,
        data: write_ops_schemas.GardenCreateInput,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> read_ops_schemas.GardenFullSchema:
        """
        Calls the garden creation application operation.

        Args:
            data (UserCreateInput): input DTO.
            svcs_container (Container): svcs service
                locator container.

        Returns:
            UserSelfDetail: user self-reference DTO.
        """
        svcs_container.register_local_value(State, state)
        garden_write_ops_controller, garden_sanitizer = await svcs_container.aget(
            GardenWriteOpsController, GardenSanitizer
        )
        user_repo, email_emitter = await svcs_container.aget_abstract(
            AbstractUserRepository, AbstractEmailEmitter
        )
        with litestar_exception_map():
            garden_schema = await garden_write_ops_controller.create(
                client=request.user,
                data=data,
                user_repo=user_repo,
                garden_sanitizer=garden_sanitizer,
                email_emitter=email_emitter,
            )
        return garden_schema

    """
    @patch(path=urls.USER_CHANGE_USERNAME_URL)
    async def user_change_username() -> None:
        pass

    @patch(path=urls.USER_CHANGE_PASSWORD_URL)
    async def user_change_password() -> None:
        pass

    @post(path=urls.USER_EMAIL_CHANGE_REQUEST_URL)
    async def user_email_change_request() -> None:
        pass

    @delete(path=urls.USER_DELETE_URL)
    async def user_delete() -> None:
        pass
    """
