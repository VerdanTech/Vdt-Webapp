from django.apps import apps

from .base import *

# ==============================================================================
# CORE SETTINGS
# ==============================================================================

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += ["debug_toolbar", "drf_spectacular", "drf_spectacular_sidecar"]

# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

# ==============================================================================
# API SETTINGS
# ==============================================================================

REST_FRAMEWORK["DEFAULT_SCHEMA_CLASS"] = "drf_spectacular.openapi.AutoSchema"


# ==============================================================================
# SPECTACULAR DOCUMENTATION SETTINGS
# ==============================================================================

app_tags = [
    {"name": app_label.removeprefix("verdantech_api.apps.")}
    for app_label in INSTALLED_APPS
    if app_label.startswith("verdantech_api.apps.")
]

SPECTACULAR_SETTINGS = {
    "TITLE": "VerdanTech-API",
    "DESCRIPTION": "API of the VerdanTech Project Web Application",
    "VERSION": "0.1.0",
    "SERVERS": [{"url": "http://localhost:5173/api"}],
    # "SCHEMA_PATH_PREFIX_INSERT": "api",
    "TAGS": app_tags,
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
    "COMPONENT_SPLIT_REQUEST": True,
    "AUTHENTICATION_WHITELIST": ["rest_framework.authentication.SessionAuthentication"],
    "PARSER_WHITELIST": [
        "rest_framework.parsers.JSONParser",
    ],
    "RENDERER_WHITELIST": ["rest_framework.renderers.JSONRenderer"],
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

# ==============================================================================
# SECURITY SETTINGS
# ==============================================================================

ALLOWED_HOSTS = ["*"]
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SAMESITE = "None"
CSRF_TRUSTED_ORIGINS = ["*"]
SESSION_COOKIE_SAMESITE = "None"
SESSION_COOKIE_HTTPONLY = False

CORS_ALLOW_ALL_ORIGINS = True
CSRF_TRUSTED_ORIGINS = ["http://localhost:5173", "http://127.0.0.1:5173"]
CORS_ALLOW_CREDENTIALS = True
