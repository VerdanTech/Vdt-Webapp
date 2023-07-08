from litestar import Litestar

from src.verdantech_api.settings import app_config


def create_app() -> Litestar:
    """Application factory patten for Litestar instance"""

    app = Litestar.from_config(app_config)

    return app
