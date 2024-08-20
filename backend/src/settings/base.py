# Standard Library
from datetime import timedelta
from enum import Enum
from pathlib import Path

# External Libraries
from decouple import Csv, config

# ============================================================================
# API SETTINGS
# ============================================================================

# ======================================
# URL SETTINGS
# ======================================

USING_HTTPS = config("USING_HTTPS", cast=bool, default=False)
API_URL_BASE: str = ""

# ======================================
# CLIENT RELATED SETTINGS
# ======================================

CLIENT_DOMAIN: str = config("CLIENT_DOMAIN", cast=str, default="verdantech.io")  # type: ignore
if USING_HTTPS:
    CLIENT_BASE_URL: str = "https://" + CLIENT_DOMAIN + "/"
else:
    CLIENT_BASE_URL: str = "http://" + CLIENT_DOMAIN + "/"
CLIENT_EMAIL_VERIFICATION_URL: str = CLIENT_BASE_URL + "register/verify/"
CLIENT_PASSWORD_RESET_URL: str = CLIENT_BASE_URL + "login/reset-password/"
CLIENT_GARDENS_URL: str = CLIENT_BASE_URL + "app/gardens/"

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

# ======================================
# AUTH SETTINGS
# ======================================

ACCESS_JWT_SECRET = str(
    config("ACCESS_JWT_SECRET", cast=str, default="developmentsecret123")
)
ACCESS_JWT_EXPIRY_TIMEDELTA = timedelta(minutes=15)
ACCESS_JWT_ALGORITHM = "HS256"
REFRESH_JWT_SECRET = str(
    config("REFRESH_JWT_SECRET", cast=str, default="developmentsecret456")
)
REFRESH_JWT_EXPIRY_TIMEDELTA = timedelta(days=7)
REFRESH_JWT_ALGORITHM = "HS256"

# ============================================================================
# APPLICATION SETTINGS
# ============================================================================

# ======================================
# TASK BACKEND SETTINGS
# ======================================

NUM_TASK_WORKERS = 1

# ======================================
# DATABASE SETTINGS
# ======================================

# Postgres
POSTGRES_URI = config(
    "POSTGRES_DB_URI",
    cast=str,
    default="postgresql+asyncpg://verdantech_db:xkrytusefhrerifuthrh@postgres:5432/dev_db",
)

# Sqlalchemy
# Name of the client attribute in the global app state
ALCHEMY_CLIENT_NAME: str = "sqlalchemy_client"
# Whether to commit database transactions - disabled in testing
ALCHEMY_TRANSACTION_COMMIT = True

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
    REQUIRED_FOR_NONE = "none"
    REQUIRED_FOR_LOGIN = "required"

    @property
    def verification_required(self) -> bool:
        return self.value == self.REQUIRED_FOR_LOGIN


EMAIL_CONFIRMATION = EmailConfirmationOptions.REQUIRED_FOR_LOGIN
EMAIL_VERIFICATON_EXPIRY_TIME_HOURS: int = 72

# Email confirmation
EMAIL_FILEPATH_EMAIL_CONFIRMATION = email_path("email_verification.html")
EMAIL_SUBJECT_EMAIL_CONFIRMATION: str = "Email verification - VerdanTech"
# Password reset
EMAIL_FILEPATH_PASSWORD_RESET = email_path("password_reset.html")
EMAIL_SUBJECT_PASSWORD_RESET: str = "Password reset - VerdanTech"
# Garden invite
EMAIL_FILEPATH_GARDEN_INVITE = email_path("garden_invite.html")
EMAIL_SUBJECT_GARDEN_INVITE: str = "You've been invited to a Garden - VerdanTech"

# ============================================================================
# DOMAIN MODEL SETTINGS
# ============================================================================

# ======================================
# USER SETTINGS
# ======================================

USER_MAX_EMAILS = 3

# ======================================
# GARDEN SETTINGS
# ======================================


# Garden key field
GARDEN_KEY_KEYGEN_DEFAULT_LENGTH_NO_PLANT_NAME: int = 6
GARDEN_KEY_KEYGEN_DEFAULT_LENGTH_PLANT_NAME: int = 3
"""Default length of the keygen portion of the garden key. when generated with or without a plant name."""
MAX_GARDEN_RANDOM_PLANT_KEY_GENERATION_ATTEMPTS: int = 4
"""The maximum amount of times the key generator will generate an id with a random plant name before reverting to only random characters."""
