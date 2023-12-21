# External Libraries
from decouple import config

from enum import Enum

# Import all the base settings, and then overwrite with
# development or test or production settings depending on the
# environment variable

class AppEnvironment(Enum):
    TEST = 0
    DEV = 1
    PROD = 2

ENVIRONMENT = AppEnvironment.TEST
environment_env_var = config("ENVIRONMENT", default="DEV", cast=str)

if environment_env_var == "TEST":
    from .test import * # noqa
    ENVIRONMENT = AppEnvironment.TEST
if environment_env_var == "DEV":
    from .dev import *  # noqa
    ENVIRONMENT = AppEnvironment.DEV
elif environment_env_var == "PROD":
    from .prod import *  # noqa
    ENVIRONMENT = AppEnvironment.PROD
else:
    raise ValueError("Test/Dev/Prod environment variable (ENVIRONMENT) is not a valid enumeration.")
