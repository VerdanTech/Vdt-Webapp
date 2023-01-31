from .base import *

# ==============================================================================
# CORE SETTINGS
# ==============================================================================

INSTALLED_APPS += [
    "debug_toolbar",
]

# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# ==============================================================================
# NETWORK SETTINGS
# ==============================================================================

INTERNAL_IPS = ["127.0.0.1"]
