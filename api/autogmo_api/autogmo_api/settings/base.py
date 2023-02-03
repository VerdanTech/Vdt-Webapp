import os
from pathlib import Path

from decouple import Csv, config

# ==============================================================================
# CORE SETTINGS
# ==============================================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = config(
    "SECRET_KEY",
    default="django-insecure-n=r5mq#q09@3v_#x$ijj=l)(5aix3tav%!%_e9qrynsz=7+9ob",
)

DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="127.0.0.1", cast=Csv())

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ROOT_URLCONF = "autogmo_api.urls"

STATIC_URL = "static/"

WSGI_APPLICATION = "autogmo_api.wsgi.application"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "rest_framework",
    "rest_framework.authtoken",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "apps.user",
    "apps.auth"
]

SITE_ID = 1

# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

MIDDLEWARE = [
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
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
    ],
}

API_URL_BASE = config("API_URL_BASE", default="api/", cast=str)

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

AUTH_USER_MODEL = "user.User"

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

CSRF_COOKIE_SAMESITE = 'Strict'
SESSION_COOKIE_SAMESITE = 'Strict'
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True

# Allauth: https://django-allauth.readthedocs.io/en/latest/configuration.html
AUTHENTICATION_METHOD = "email"
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_PRESERVE_USERNAME_CASING = False

# dj-rest-auth / rest_auth: https://dj-rest-auth.readthedocs.io/en/latest/configuration.html
REST_AUTH_TOKEN_MODEL = None
LOGOUT_ON_PASSWORD_CHANGE = True

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
# THIRD-PARTY SETTINGS
# ==============================================================================


# ==============================================================================
# FIRST-PARTY SETTINGS
# ==============================================================================

SIMPLE_ENVIRONMENT = config("SIMPLE_ENVIRONMENT", default="local")
