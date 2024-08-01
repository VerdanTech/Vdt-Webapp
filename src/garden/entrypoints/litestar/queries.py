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
    tags = ["gardens"]

    @get(
        path=urls.GARDEN_UNIQUE_KEY_URL,
        name=url_to_route_name(urls.GARDEN_ROUTER_URL_BASE, urls.GARDEN_UNIQUE_KEY_URL),
        summary="Generate a new, unique garden key.",
        description="Generates a unique garden key given a plant name and a random string.",
        operation_id="GardenGenerateUniqueKeyQueryOp",
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

    @get(
        path=urls.GARDEN_ASSOCIATED_PARTIALS_URL,
        name=url_to_route_name(
            urls.GARDEN_ROUTER_URL_BASE, urls.GARDEN_ASSOCIATED_PARTIALS_URL
        ),
        summary="Returns a partial representation of all gardens that are associated with the client",
        description="Returns a partial representation of all gardens that are associated with the client",
        operation_id="GardenAssociatedPartialsQueryOp",
    )
    async def associated_partials(
        self,
        state: State,
        request: Request,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> queries.AssociatedPartialsResult:
        """
        Calls the associated garden partials query.

        Args:
            state (State): Litestar global app state.
            request (Request): Litestar http request object.
            svcs_container (Container): service locator.

        Returns:
            AssociatedPartialsResult: the associated garden partials.
        """
        svcs_container.register_local_value(State, state)
        with litestar_exception_map():
            partials = await queries.get_associated_partials(
                svcs_container=svcs_container, client=request.user
            )
        return partials

    @get(
        path=urls.GARDEN_MOST_RELEVANT_PARTIALS_URL,
        name=url_to_route_name(
            urls.GARDEN_ROUTER_URL_BASE, urls.GARDEN_MOST_RELEVANT_PARTIALS_URL
        ),
        summary="Returns a partial representation of most relevant gardens to the user.",
        description="Returns a partial representation of most relevant gardens to the user, ordered by relevance.",
        operation_id=queries.GardenMostRelevantPartialsQuery.to_operation_id(),
    )
    async def most_relevant(
        self,
        max_gardens: int,
        state: State,
        request: Request,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> list[queries.GardenPartialSchema]:
        """
        Calls the most relevant garden partials query.

        Args:
            max_gardens (int): the maximum number of gardens to return.
            state (State): Litestar global app state.
            request (Request): Litestar http request object.
            svcs_container (Container): service locator.

        Returns:
            list[queries.GardenPartialSchema]: the most relevant garden partials.
        """
        svcs_container.register_local_value(State, state)
        data = queries.GardenMostRelevantPartialsQuery(max_gardens=max_gardens)
        with litestar_exception_map():
            partials = await queries.get_most_relevant_partials(
                query=data, svcs_container=svcs_container, client=request.user
            )
        return partials

    @get(
        path=urls.GARDEN_PARTIALS_BY_KEY_URL,
        name=url_to_route_name(
            urls.GARDEN_ROUTER_URL_BASE, urls.GARDEN_PARTIALS_BY_KEY_URL
        ),
        summary="Returns a partial representation of gardens given by keys.",
        description="Returns a partial representation of gardens given by keys, provided they exist and the client is authorized to use them.",
        operation_id=queries.GardenPartialsByKeysQuery.to_operation_id(),
    )
    async def partials_by_key(
        self,
        garden_keys: list[str],
        state: State,
        request: Request,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> list[queries.GardenPartialSchema]:
        """
        Calls the partials by keys query.

        Args:
            garden_keys (list[str]): the keys of the gardens to return.
            state (State): Litestar global app state.
            request (Request): Litestar http request object.
            svcs_container (Container): service locator.

        Returns:
            list[queries.GardenPartialSchema]: the garden partials.
        """
        svcs_container.register_local_value(State, state)
        data = queries.GardenPartialsByKeysQuery(keys=garden_keys)
        with litestar_exception_map():
            partials = await queries.get_partials_by_key(
                query=data, svcs_container=svcs_container, client=request.user
            )
        return partials

    @get(
        path=urls.GARDEN_FULL_BY_KEY_URL,
        name=url_to_route_name(
            urls.GARDEN_ROUTER_URL_BASE, urls.GARDEN_FULL_BY_KEY_URL
        ),
        summary="Returns a full representation of a garden by its key.",
        description="Returns a full representation of gardens given by a key.",
        operation_id=queries.GardenFullByKeyQuery.to_operation_id(),
    )
    async def full_by_key(
        self,
        garden_key: str,
        state: State,
        request: Request,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> queries.GardenFullSchema:
        """
        Calls the partials by keys query.

        Args:
            garden_key (str): the key of the garden to return.
            state (State): Litestar global app state.
            request (Request): Litestar http request object.
            svcs_container (Container): service locator.

        Returns:
            queries.GardenFullSchema: the garden schema.
        """
        svcs_container.register_local_value(State, state)
        data = queries.GardenFullByKeyQuery(key=garden_key)
        with litestar_exception_map():
            schema = await queries.get_full_by_key(
                query=data, svcs_container=svcs_container, client=request.user
            )
        return schema
