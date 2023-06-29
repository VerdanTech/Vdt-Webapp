from decouple import config
from litestar.config.app import AppConfig
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyAsyncConfig, SQLAlchemyPlugin

from .base import *

# Import all the base settings, and then overwrite with
# development or production settings depending on the
# environment variable


if config("DEV_OR_PROD", cast=str) == "dev":
    from .dev import *
elif config("DEV_OR_PROD", case=str) == "prod":
    from .prod import *


allowed_hosts_config = AllowedHostsConfig(allowed_hosts=[])

cors_config = CORSConfig()

csrf_config = CSRFConfig()

app_config = AppConfig()
