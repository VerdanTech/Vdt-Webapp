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
# API SETTINGS
# ======================================

USING_HTTPS: bool = config("USING_HTTPS", default=False, cast=bool)
BASE_DOMAIN: str = config("BASE_DOMAIN", cast=bool)
API_URL_BASE: str = "api/"

# ======================================
# MODEL SETTINGS
# ======================================

# UserModel
USERNAME_MAX_LENGTH: int = 50
USERNAME_MIN_LENGTH: int = 50
PASSWORD_MAX_LENGTH: int = 255
PASSWORD_MIN_LENGTH: int = 255
EMAIL_MAX_LENGTH: int = 255
VERIFICATION_KEY_MAX_LENGTH: int = 64

# GardenModel
GARDEN_STR_ID_MAX_LENGTH: int = 6

# ======================================
# EMAIL SETTINGS
# ======================================

DEFAULT_EMAIL_SENDER: str = "verdantech@gmail.com"

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
