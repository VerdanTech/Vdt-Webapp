from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.accounts"

    # Expose DRF Spectacular schema extensions
    # in schema.py to python interpreter
    def ready(self):
        import apps.accounts.schema  # noqa: F401
