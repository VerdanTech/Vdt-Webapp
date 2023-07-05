from pathlib import Path
from typing import List

from decouple import Csv, config

# ==============================================================================
# LITESTAR SETTINGS
# ==============================================================================

# ======================================
# DATABASE SETTINGS
# ======================================

# ======================================
# ALLOWED HOSTS SETTINGS
# ======================================

ALLOWED_HOSTS: List[str] = config("ALLOWED_HOSTS", cast=Csv(), default=".localhost")

# ======================================
# CORS SETTINGS
# ======================================

ALLOWED_ORIGINS: List[str] = config("ALLOWED_ORIGINS", cast=Csv(), default="")

# ======================================
# CSRF SETTINGS
# ======================================

# ======================================
# OPENAPI SETTINGS
# ======================================

OPENAPI_TITLE: str = config("OPENAPI_TITLE", cast=str, default="verdantech_api")
OPENAPI_VERSION: str = config("OPENAPI_VERSION", cast=str)
OPENAPI_DOCUMENTATION_URL: str = "https://github.com/nathanielarking/VerdanTech"
OPENAPI_LICENSE: str = "GPL-3.0-or-later"


# ==============================================================================
# VERDANTECH SETTINGS
# ==============================================================================

# ======================================
# FILE SETTINGS
# ======================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def email_path(*paths: str) -> Path:
    """Appends input path to static email directory"""
    return BASE_DIR.join("verdantech_api/static/emails/", *paths)


# ======================================
# API SETTINGS
# ======================================

USING_HTTPS: bool = config("USING_HTTPS", default=False, cast=bool)
BASE_DOMAIN: str = config("BASE_DOMAIN", cast=bool)
API_URL_BASE: str = "api/"

# ======================================
# MODEL SETTINGS
# ======================================

# UserModel
EMAIL_MIN_LENGTH: int = 1
EMAIL_MAX_LENGTH: int = 255
USERNAME_MIN_LENGTH: int = 3
USERNAME_MAX_LENGTH: int = 50
PASSWORD_MIN_LENGTH: int = 6
PASSWORD_MAX_LENGTH: int = 255
USER_MAX_EMAILS: int = 3
VERIFICATION_KEY_MAX_LENGTH: int = 64

# GardenModel
GARDEN_STR_ID_MAX_LENGTH: int = 6

# ======================================
# EMAIL SETTINGS
# ======================================

EMAIL_CLIENT_HOSTNAME: str = ""
EMAIL_CLIENT_PORT: int = 0
EMAIL_CLIENT_USERNAME: int = ""
EMAIL_CLIENT_PASSWORD: int = ""
EMAIL_CLIENT_SENDER: str = "verdantech@gmail.com"

EMAIL_VERIFICATION_KEY_LENGTH: int = 32
EMAIL_VERIFICATON_EXPIRY_TIME_HOURS: int = 72

# ======================================
# CLIENT RELATED SETTINGS
# ======================================

CLIENT_DOMAIN: str = "verdantech.io"
if USING_HTTPS:
    CLIENT_BASE_URL: str = "https://" + CLIENT_DOMAIN + "/"
else:
    CLIENT_BASE_URL: str = "http://" + CLIENT_DOMAIN + "/"
CLIENT_EMAIL_VERIFICATION_URL: str = CLIENT_BASE_URL + "register/verify/"
CLIENT_PASSWORD_RESET_URL: str = CLIENT_BASE_URL + "register/verify/"
