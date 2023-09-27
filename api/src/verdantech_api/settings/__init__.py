from decouple import config

# Import all the base settings, and then overwrite with
# development or production settings depending on the
# environment variable

environment = config("ENVIRONMENT", default="DEV", cast=str)

if environment == "DEV":
    from .dev import *  # noqa
elif environment == "PROD":
    from .prod import *  # noqa
