# Standard Library
from enum import Enum
from pathlib import Path
from typing import List

# External Libraries
from decouple import Csv, config

# ============================================================================
# API SETTINGS
# ============================================================================

# ======================================
# OPENAPI SETTINGS
# ======================================

OPENAPI_TITLE: str = "verdantech_api"
OPENAPI_VERSION: str = "v0.0.1"
OPENAPI_DOCUMENTATION_URL: str = "https://github.com/nathanielarking/VerdanTech"
OPENAPI_LICENSE: str = "GPL-3.0-or-later"

# ======================================
# URL SETTINGS
# ======================================

USING_HTTPS: bool = config("USING_HTTPS", default=False, cast=bool)
BASE_DOMAIN: str = config("BASE_DOMAIN", cast=str, default="127.0.0.1")
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

ALLOWED_HOSTS: List[str] = config("ALLOWED_HOSTS", cast=Csv(), default=".localhost")

# ======================================
# CORS SETTINGS
# ======================================

ALLOW_ORIGINS: List[str] = config("ALLOWED_ORIGINS", cast=Csv(), default="")

# ======================================
# CSRF SETTINGS
# ======================================

# ============================================================================
# APPLICATION SETTINGS
# ============================================================================

# ======================================
# PROVIDER KEY (PK) NAMES
# These key names automatically configure all provided dependencies
# in the provider key. The route handlers of the API, which is what the
# dependencies are injected into, still need to have arguments with
# names matching these keys to receive them.
# ======================================

# ========== Operations ========== #

# User
USER_READ_OP_PK = "user_read_operations"
USER_WRITE_OP_PK = "user_write_operations"
USER_VERIFICATION_OP_PK = "user_verification_operations"
USER_AUTH_OP_PK = "user_auth_operations"

# ========== Sanitizers ========== #

USER_SANITIZER_PK = "user_sanitizer"

# ========== Persistence ========== #

# Database
DB_CLIENT_PK = "db_client"
DB_SESSION_PK = "db_session"

# Serializer
USER_SERIALIZER_PK = "user_serializer"

# Repositories
USER_REPOSITORY_PK = "user_repo"

# ========== Email ========== #

EMAIL_CLIENT_PK = "email_client"
EMAIL_EMITTER_PK = "email_emitter"

# ========== Security ========== #

# Crypt
PASSWORD_CRYPT_PK = "password_crypt"

# ======================================
# DATABASE SETTINGS
# ======================================

POSTGRES_DB_NAME: str = config("POSTGRES_DB_NAME", cast=str)
POSTGRES_DB_USER: str = config("POSTGRES_DB_USER", cast=str)
POSTGRES_DB_PASSWORD: str = config("POSTGRES_DB_PASSWORD", cast=str)
POSTGRES_URI: str = config(
    "POSTGRES_DB_URI",
    cast=str,
    default=f"postgresql+asyncpg://{POSTGRES_DB_USER}:{POSTGRES_DB_PASSWORD}@postgres:5432/{POSTGRES_DB_NAME}",
)

ALCHEMY_URI: str = POSTGRES_URI

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

EMAIL_CLIENT_HOSTNAME: str = ""
EMAIL_CLIENT_PORT: int = 0
EMAIL_CLIENT_USERNAME: int = ""
EMAIL_CLIENT_PASSWORD: int = ""
EMAIL_CLIENT_SENDER: str = "verdantech@gmail.com"


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

EMAIL_FILEPATH_EMAIL_CONFIRMATION: str = email_path("email_verification.html")
EMAIL_SUBJECT_EMAIL_CONFIRMATION: str = "Email verification - VerdanTech"
EMAIL_FILEPATH_PASSWORD_RESET: str = email_path("password_reset.html")
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
