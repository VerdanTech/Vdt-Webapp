from decouple import config
from litestar.config.allowed_hosts import AllowedHostsConfig
from litestar.config.app import AppConfig
from litestar.config.cors import CORSConfig

# Import all the base settings, and then overwrite with
# development or production settings depending on the
# environment variable

environment = config("ENVIRONMENT", default="DEV", cast=str)

if environment == "DEV":
    from .dev import *  # noqa
elif environment == "PROD":
    from .prod import *  # noqa


allowed_hosts_config = AllowedHostsConfig(allowed_hosts=LITESTAR_ALLOWED_HOSTS)

cors_config = CORSConfig(allow_origins=LITESTAR_ALLOW_ORIGINS)

# csrf_config = CSRFConfig()

app_config = AppConfig(logging_config=logging_config)
