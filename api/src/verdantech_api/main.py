from litestar import Litestar


def create_app() -> Litestar:
    """Application factory patten for Litestar instance"""

    db_config = SQLAlchemyAsyncConfig(connection_string="sqlite+aiosqlite:///db.sqlite")

    app = Litestar.from_config()

    return app
