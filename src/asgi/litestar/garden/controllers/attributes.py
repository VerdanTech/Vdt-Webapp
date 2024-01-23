# External Libraries
from litestar import Controller, Request, post
from litestar.datastructures import State
from litestar.params import Dependency
from svcs import Container

# VerdanTech Source
from src import settings
from src.asgi.litestar import openapi
from src.asgi.litestar.exceptions import (
    ClientError,
    ServerError,
    litestar_exception_map,
)
from src.domain.garden.sanitizers import GardenSanitizer
from src.interfaces.email.emitter import AbstractEmailEmitter
from src.interfaces.persistence.user.repository import AbstractUserRepository
from src.interfaces.security.crypt.password_crypt import AbstractPasswordCrypt
from src.ops.environment.schemas import attributes as attrs_ops_schemas
from src.ops.garden.controllers.attributes import GardenAttrsOpsController
from src.ops.garden.schemas import read as read_ops_schemas

from .. import routes, urls


class GardenAttrsApiController(Controller):
    """
    Garden attributes ASGI controller.
    """

    path = urls.GARDEN_ATTRS_CONTROLLER_URL_BASE
    tags = ["gardens"]

    @post(
        path=urls.GARDEN_ATTRS_SET_URL,
        name=routes.GARDEN_ATTRS_SET_NAME,
        summary="Garden environment attributes set.",
        description="Sets environmental attributes on a Garden.",
        response_description="The full newly updated garden object.",
        operation_id=routes.GARDEN_ATTRS_SET_NAME,
    )
    async def set_attributes(
        self,
        request: Request,
        data: attrs_ops_schemas.EnvironmentAttributeClusterInput,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> read_ops_schemas.GardenFullSchema:
        svcs_container.register_local_value(State, state)
        garden_attrs_ops_controller = await svcs_container.aget(
            GardenAttrsOpsController
        )
        with litestar_exception_map():
            garden_schema = await garden_attrs_ops_controller.set_attributes(
                client=request.user,
                data=data,
            )
        return garden_schema
