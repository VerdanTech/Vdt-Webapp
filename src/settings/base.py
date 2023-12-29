# Standard Library
from enum import Enum
from pathlib import Path

# External Libraries
from decouple import Csv, config

# ============================================================================
# API SETTINGS
# ============================================================================

# ======================================
# OPENAPI SETTINGS
# ======================================

OPENAPI_TITLE: str = "VerdanTech-Backend"
OPENAPI_VERSION: str = "v0.0.1"
OPENAPI_DOCUMENTATION_URL: str = "https://github.com/VerdanTech/VerdanTech-Backend"
OPENAPI_LICENSE: str = "GPL-3.0-or-later"

# ======================================
# URL SETTINGS
# ======================================

USING_HTTPS = config("USING_HTTPS", default=False, cast=bool)
BASE_DOMAIN = config("BASE_DOMAIN", cast=str, default="127.0.0.1")
API_URL_BASE: str = "/vdtapi"

# ======================================
# CLIENT RELATED SETTINGS
# ======================================

CLIENT_DOMAIN: str = "verdantech.io"
if USING_HTTPS:
    CLIENT_BASE_URL: str = "https://" + CLIENT_DOMAIN + "/"
else:
    CLIENT_BASE_URL: str = "http://" + CLIENT_DOMAIN + "/"
CLIENT_EMAIL_VERIFICATION_URL: str = CLIENT_BASE_URL + "register/verify/"
CLIENT_PASSWORD_RESET_URL: str = CLIENT_BASE_URL + "password_reset/"

# ======================================
# ALLOWED HOSTS SETTINGS
# ======================================

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv(), default=".localhost")

# ======================================
# CORS SETTINGS
# ======================================

ALLOW_ORIGINS = config("ALLOWED_ORIGINS", cast=Csv(), default="")

# ======================================
# CSRF SETTINGS
# ======================================

# ============================================================================
# APPLICATION SETTINGS
# ============================================================================

# ======================================
# QUEUE SETTINGS
# ======================================

SAQ_WORKERS = 1

# ======================================
# DATABASE SETTINGS
# ======================================

# Postgres
POSTGRES_DB_NAME = config("POSTGRES_DB_NAME", cast=str)
POSTGRES_DB_USER = config("POSTGRES_DB_USER", cast=str)
POSTGRES_DB_PASSWORD = config("POSTGRES_DB_PASSWORD", cast=str)
POSTGRES_URI = str(  # Todo: fix str() required for type checker.
    config(
        "POSTGRES_DB_URI",
        cast=str,
        default=f"postgresql+asyncpg://{POSTGRES_DB_USER}:{POSTGRES_DB_PASSWORD}@postgres:5432/{POSTGRES_DB_NAME}",
    )
)

# Sqlalchemy
ALCHEMY_URI = POSTGRES_URI
# Name of the client attribute in the global app state
ALCHEMY_CLIENT_NAME: str = "sqlalchemy_client"
# Whether to rollback / not commit database transactions
ALCHEMY_TRANSACTION_ROLLBACK = True

# Redis
REDIS_URI: str = "redis://localhost"

# ======================================
# FILE SETTINGS
# ======================================

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_BASE_DIR: str = "static/"

EMAIL_BASE_DIR: str = "static/emails/"


def static_path(*paths: str) -> Path:
    """Appends input path to static files directory"""
    return BASE_DIR.joinpath(STATIC_BASE_DIR, *paths)


def email_path(*paths: str) -> Path:
    """Appends input path to static email directory"""
    return BASE_DIR.joinpath(EMAIL_BASE_DIR, *paths)


# ======================================
# EMAIL SETTINGS
# ======================================

# Client
EMAIL_CLIENT_HOSTNAME: str = ""
EMAIL_CLIENT_PORT: int = 0
EMAIL_CLIENT_USERNAME: str = ""
EMAIL_CLIENT_PASSWORD: str = ""
EMAIL_CLIENT_SENDER: str = "verdantech@gmail.com"


# Verification
class EmailConfirmationOptions(Enum):
    REQUIRED_FOR_NONE = 0
    REQUIRED_FOR_WRITE = 1
    REQUIRED_FOR_ALL = 2

    def verification_required(self) -> bool:
        return (
            self.value == self.REQUIRED_FOR_WRITE or self.value == self.REQUIRED_FOR_ALL
        )


EMAIL_CONFIRMATION = EmailConfirmationOptions.REQUIRED_FOR_WRITE
EMAIL_VERIFICATION_KEY_LENGTH: int = 32
EMAIL_VERIFICATON_EXPIRY_TIME_HOURS: int = 72

# Email confirmation
EMAIL_FILEPATH_EMAIL_CONFIRMATION = email_path("email_verification.html")
EMAIL_SUBJECT_EMAIL_CONFIRMATION: str = "Email verification - VerdanTech"
# Password reset
EMAIL_FILEPATH_PASSWORD_RESET = email_path("password_reset.html")
EMAIL_SUBJECT_PASSWORD_RESET: str = "Password reset - VerdanTech"

# ============================================================================
# DOMAIN MODEL SETTINGS
# ============================================================================

# ======================================
# USER SETTINGS
# ======================================

EMAIL_MIN_LENGTH: int = 1
EMAIL_MAX_LENGTH: int = 255
USERNAME_MIN_LENGTH: int = 3
USERNAME_MAX_LENGTH: int = 50
PASSWORD_MIN_LENGTH: int = 6
PASSWORD_MAX_LENGTH: int = 255
USER_MAX_EMAILS: int = 3
VERIFICATION_KEY_MAX_LENGTH: int = 64

# ======================================
# GARDEN SETTINGS
# ======================================

GARDEN_STR_ID_MAX_LENGTH: int = 6
