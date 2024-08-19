# External Libraries
from litestar import Controller, Request, get
from litestar.datastructures import State
from litestar.params import Dependency
from svcs import Container

# VerdanTech Source
from src.garden.ops import queries


class GardenQueryController(Controller):
    """Garden read operations controller"""

    path = "query"
    tags = ["gardens"]

    @get(
        path="generate_unique_key",
        summary="Generate a new, unique garden key.",
        description="Generates a unique garden key given a plant name and a random string.",
        operation_id="GardenGenerateUniqueKeyQueryOp",
    )
    async def generate_unique_garden_key(
        self,
        state: State,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> queries.GardenUniqueKeyResult:
        """
        Calls the unique garden key generation query.

        Args:
            state (State): Litestar global app state.
            request (Request): Litestar http request object.
            svcs_container (Container): service locator.

        Returns:
            GardenUniqueKeyResult: the generated key.
        """
        svcs_container.register_local_value(State, state)
        key = await queries.generate_unique_garden_key(
            svcs_container=svcs_container
        )
        return key

    @get(
        path="associated_partials",
        summary="Returns a partial representation of all gardens that are associated with the client",
        description="Returns a partial representation of all gardens that are associated with the client",
        operation_id="GardenAssociatedPartialsQueryOp",
    )
    async def associated_partials(
        self,
        state: State,
        request: Request,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> queries.GardenAssociatedPartialsResult:
        """
        Calls the associated garden partials query.

        Args:
            state (State): Litestar global app state.
            request (Request): Litestar http request object.
            svcs_container (Container): service locator.

        Returns:
            GardenAssociatedPartialsResult: the associated garden partials.
        """
        svcs_container.register_local_value(State, state)
        partials = await queries.get_associated_partials(
            svcs_container=svcs_container, client=request.user
        )
        return partials

    @get(
        path="most_relevant",
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
        partials = await queries.get_most_relevant_partials(
            query=data, svcs_container=svcs_container, client=request.user
        )
        return partials

    @get(
        path="partials_by_key",
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
        partials = await queries.get_partials_by_key(
            query=data, svcs_container=svcs_container, client=request.user
        )
        return partials

    @get(
        path="full_by_key",
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
        schema = await queries.get_full_by_key(
            query=data, svcs_container=svcs_container, client=request.user
        )
        return schema

    @get(
        path="pending_invites",
        summary="Returns a set of pending garden invites",
        description="Returns a set of tuples of gardens and associated pending garden memberships",
        operation_id="GardenPendingInvitesQueryOp",
    )
    async def pending_invites(
        self,
        state: State,
        request: Request,
        svcs_container: Container = Dependency(skip_validation=True),
    ) -> queries.GardenPendingInvitesResult:
        """
        Calls the pending invites query.

        Args:
            state (State): Litestar global app state.
            request (Request): Litestar http request object.
            svcs_container (Container): service locator.

        Returns:
            GardenPendingInvitesResult: the pending invites.
        """
        svcs_container.register_local_value(State, state)
        invites = await queries.get_pending_invites(
            svcs_container=svcs_container, client=request.user
        )
        return invites