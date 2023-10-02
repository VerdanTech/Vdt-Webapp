from src.verdantech_api import providers, settings

# Select application-wide dependencies
application_layer_dependencies = providers.select(
    settings.DB_CLIENT_PK, settings.DB_SESSION_PK
)
