import os
from pathlib import Path

from decouple import Csv, config

# ==============================================================================
# CORE SETTINGS
# ==============================================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DEBUG = config("DEBUG", default=True, cast=bool)

SECRET_KEY = config(
    "SECRET_KEY",
    default="django-insecure-n=r5mq#q09@3v_#x$ijj=l)(5aix3tav%!%_e9qrynsz=7+9ob",
)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ROOT_URLCONF = "verdantech_api.urls"

STATIC_URL = "static/"

WSGI_APPLICATION = "verdantech_api.wsgi.application"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "timezone_field",
    "verdantech_api.apps.core",
    "verdantech_api.apps.authentication",
    "verdantech_api.apps.accounts",
    "verdantech_api.apps.gardens",
]

SITE_ID = 1

TIME_ZONE = "UTC"
USE_TZ = True

# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ==============================================================================
# API SETTINGS
# ==============================================================================

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": ["rest_framework.parsers.JSONParser"],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
    ],
}

API_URL_BASE = config("API_URL_BASE", default="", cast=str)

# ==============================================================================
# SECURITY SETTINGS
# ==============================================================================

ADMINS = []
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="127.0.0.1", cast=Csv())
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SAMESITE = "Lax"
CSRF_TRUSTED_ORIGINS = []
SESSION_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_HTTPONLY = True

# ==============================================================================
# DATABASES SETTINGS
# ==============================================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ==============================================================================
# AUTHENTICATION AND AUTHORIZATION SETTINGS
# ==============================================================================

AUTH_USER_MODEL = "accounts.User"

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

CSRF_COOKIE_SAMESITE = "Strict"
SESSION_COOKIE_SAMESITE = "Strict"
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ==============================================================================
# TEMPLATES SETTINGS
# ==============================================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ==============================================================================
# I18N AND L10N SETTINGS
# ==============================================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# ==============================================================================
# MEDIA FILES SETTINGS
# ==============================================================================

MEDIA_URL = "media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# ==============================================================================
# STATIC FILES SETTINGS
# ==============================================================================

STATIC_URL = "static/"

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

# ==============================================================================
# ALLAUTH SETTINGS: https://django-allauth.readthedocs.io/en/latest/configuration.html
# ==============================================================================

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_PRESERVE_USERNAME_CASING = False
ACCOUNT_ADAPTER = "verdantech_api.apps.accounts.adapters.AccountAdapter"
ACCOUNT_EMAIL_SUBJECT_PREFIX = config("DOMAIN_NAME", default="verdantech.com", cast=str)
ACCOUNT_MAX_EMAIL_ADDRESSES = 3

# ==============================================================================
# DJ_REST_AUTH SETTINGS: https://dj-rest-auth.readthedocs.io/en/latest/configuration.html
# ==============================================================================

REST_AUTH_TOKEN_MODEL = None
REST_SESSION_LOGIN = True
LOGOUT_ON_PASSWORD_CHANGE = True
REST_AUTH_SERIALIZERS = {
    "LOGIN_SERIALIZER": "verdantech_api.apps.authentication.serializers.LoginSerializer",
    "PASSWORD_RESET_SERIALIZER": "verdantech_api.apps.accounts.serializers.PasswordResetSerializer",
}

# ==============================================================================
# FIRST-PARTY SETTINGS
# ==============================================================================

if config("USING_HTTPS", default=True, cast=bool):
    ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
    CLIENT_BASE_URL = (
        "https://" + config("DOMAIN_NAME", default="verdantech.com", cast=str) + "/"
    )
else:
    ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"
    CLIENT_BASE_URL = (
        "http://" + config("DOMAIN_NAME", default="verdantech.com", cast=str) + "/"
    )

CLIENT_EMAIL_VERIFY_URL = CLIENT_BASE_URL + config(
    "CLIENT_EMAIL_VERIFY_URL_POSTFIX", default="register/verify/", cast=str
)
CLIENT_PASSWORD_RESET_URL = CLIENT_BASE_URL + config(
    "CLIENT_PASSWORD_RESET_URL_POSTFIX", default="password/reset/", cast=str
)

SIMPLE_ENVIRONMENT = config("SIMPLE_ENVIRONMENT", default="local")
