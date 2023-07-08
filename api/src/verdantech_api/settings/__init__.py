from decouple import config
from litestar.config.app import AppConfig
from litestar.config.allowed_hosts import AllowedHostsConfig
from litestar.config.cors import CORSConfig
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyAsyncConfig, SQLAlchemyPlugin

# Import all the base settings, and then overwrite with
# development or production settings depending on the
# environment variable

environment = config("ENVIRONMENT", default="DEV", cast=str)

if environment == "DEV":
    from .dev import * # noqa
elif environment == "PROD":
    from .prod import * # noqa


sqlalchemy_config = SQLAlchemyAsyncConfig(connection_string="sqlite+aiosqlite:///db.sqlite")

allowed_hosts_config = AllowedHostsConfig(allowed_hosts=LITESTAR_ALLOWED_HOSTS)

cors_config = CORSConfig(allow_origins=LITESTAR_ALLOW_ORIGINS)

# csrf_config = CSRFConfig()

app_config = AppConfig()
