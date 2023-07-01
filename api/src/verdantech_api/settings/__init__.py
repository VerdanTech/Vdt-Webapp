from decouple import config
from litestar.config.app import AppConfig
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyAsyncConfig, SQLAlchemyPlugin

# Import all the base settings, and then overwrite with
# development or production settings depending on the
# environment variable

if config("DEV_OR_PROD", cast=str) == "dev":
    import dev as settings
elif config("DEV_OR_PROD", case=str) == "prod":
    import prod as settings

sqlalchemy_config = SQLAlchemyAsyncConfig()

# allowed_hosts_config = AllowedHostsConfig(allowed_hosts=ALLOWED_HOSTS)

# cors_config = CORSConfig()

# csrf_config = CSRFConfig()

# db_config = SQLAlchemyAsyncConfig(connection_string="sqlite+aiosqlite:///db.sqlite")

app_config = AppConfig()
