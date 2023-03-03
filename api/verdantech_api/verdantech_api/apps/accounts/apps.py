from django.apps import AppConfig
from django.conf import settings


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "verdantech_api.apps.accounts"

    description = "Functionality related to user account management "
    "and authentication."

    # Expose DRF Spectacular schema extensions
    # in schema.py to python interpreter
    def ready(self):
        if settings.DEBUG:
            import verdantech_api.apps.accounts.schema  # noqa: F401
