from .base import *

# ==============================================================================
# CORE SETTINGS
# ==============================================================================

INSTALLED_APPS += ["debug_toolbar", "drf_spectacular", "drf_spectacular_sidecar"]

# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

# ==============================================================================
# API SETTINGS
# ==============================================================================

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# ==============================================================================
# SPECTACULAR DOCUMENTATION SETTINGS
# ==============================================================================

SPECTACULAR_SETTINGS = {
    "TITLE": "AutoGMO-API",
    "DESCRIPTION": "API of the AutoGMO "
    "(Automatic Garden Management and Optimization) project.",
    "VERSION": "0.1.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
}

# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "autogmo.web@gmail.com"
EMAIL_HOST_PASSWORD = "kfkbwrymgrowpxhh"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# ==============================================================================
# NETWORK SETTINGS
# ==============================================================================

INTERNAL_IPS = ["127.0.0.1"]
