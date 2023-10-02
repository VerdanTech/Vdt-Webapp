from litestar.config.allowed_hosts import AllowedHostsConfig
from litestar.config.cors import CORSConfig
from litestar.config.csrf import CSRFConfig
from litestar.logging import StructLoggingConfig
from src.verdantech_api import settings

allowed_hosts_config = AllowedHostsConfig(allowed_hosts=settings.ALLOWED_HOSTS)

cors_config = CORSConfig(allow_origins=settings.ALLOW_ORIGINS)

csrf_config = CSRFConfig()

logging_config = StructLoggingConfig()
