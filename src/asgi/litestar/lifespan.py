# ============================================================================
# Litestar has the ability to configure both callables and context managers
# into the startup and shutdown of the application. This is used to manage
# a connection to the database.
# ============================================================================

# VerdanTech Source
from src.infra.persistence.sqlalchemy.repository.litestar_lifespan import (
    litestar_alchemy_client_lifespan,
)

lifespan = [litestar_alchemy_client_lifespan]
