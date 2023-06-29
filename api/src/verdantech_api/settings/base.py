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

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv(), default=".localhost")

# ======================================
# CORS SETTINGS
# ======================================

ALLOWED_ORIGINS = config("ALLOWED_ORIGINS", cast=Csv(), default="")

# ======================================
# CSRF SETTINGS
# ======================================

# ======================================
# OPENAPI SETTINGS
# ======================================

OPENAPI_TITLE = config("OPENAPI_TITLE", cast=str, default="verdantech_api")
OPENAPI_VERSION = config("OPENAPI_VERSION", cast=str)
OPENAPI_DOCUMENTATION_URL = "https://github.com/nathanielarking/VerdanTech"
OPENAPI_LICENSE = "GPL-3.0-or-later"


# ==============================================================================
# VERDANTECH SETTINGS
# ==============================================================================

# ======================================
# MODEL SETTINGS
# ======================================

USERNAME_MAX_LENGTH = config("USERNAME_MAX_LENGTH", cast=int, default=50)
PASSWORD_MAX_LENGTH = config("PASSWORD_MAX_LENGTH", cast=int, default=255)
EMAIL_MAX_LENGTH = config("USERNAME_MAX_LENGTH", cast=int, default=255)
EMAIL_VERIFICATION_KEY_MAX_LENGTH = config("PASSWORD_MAX_LENGTH", cast=int, default=64)

# ======================================
# EMAIL SETTINGS
# ======================================
