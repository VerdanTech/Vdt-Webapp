from .base import *

# ==============================================================================
# AUTHENTICATION AND AUTHORIZATION SETTINGS
# ==============================================================================

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

ACCOUNT_EMAIL_VERIFICATION = "optional"

# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# ==============================================================================
# DATABASE SETTINGS
# ==============================================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "test_db.sqlite3",
    }
}
