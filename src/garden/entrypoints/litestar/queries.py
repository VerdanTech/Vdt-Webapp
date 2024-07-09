# External Libraries
from litestar import Controller, Request, get
from litestar.datastructures import State
from litestar.params import Dependency
from svcs import Container

# VerdanTech Source
from src.common.entrypoints.litestar.exceptions import litestar_exception_map
from src.common.entrypoints.litestar.utils import url_to_route_name
from src.garden.ops import queries

from . import urls


class GardenQueryController(Controller):
    """Garden read operations controller"""

    path = urls.GARDEN_QUERY_CONTROLLER_URL_BASE
    tags = ["users"]

    @get(
        path=urls.GARDEN_UNIQUE_KEY_URL,
        name=url_to_route_name(urls.GARDEN_ROUTER_URL_BASE, urls.GARDEN_UNIQUE_KEY_URL),
        summary="Generate a new, unique garden key.",
        description="Generates a unique garden key given a plant name and a random string.",
    )
    async def generate_unique_garden_key(
        self,
        state: State,
        request: Request,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> queries.UniqueGardenKeyResult:
        """
        Calls the unique garden key generation query.

        Args:
            state (State): Litestar global app state.
            request (Request): Litestar http request object.
            svcs_container (Container): service locator.

        Returns:
            UniqueGardenKeyResult: the generated key.
        """
        svcs_container.register_local_value(State, state)
        with litestar_exception_map():
            key = await queries.generate_unique_garden_key(
                svcs_container=svcs_container, client=request.user
            )
        return key
