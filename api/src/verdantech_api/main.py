from litestar import Litestar
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyAsyncConfig, SQLAlchemyPlugin


def create_app() -> Litestar:
    """Application factory patten for Litestar instance"""

    db_config = SQLAlchemyAsyncConfig(connection_string="sqlite+aiosqlite:///db.sqlite")

    app = Litestar(route_handlers=[], plugins=[SQLAlchemyPlugin(db_config)])

    return app
