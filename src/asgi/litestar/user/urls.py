# ======================================
# BASE
# ======================================

USER_ROUTER_URL_BASE: str = "users/"

# ======================================
# READ
# ======================================

USER_READ_CONTROLLER_URL_BASE = "read/"

USER_PROFILES_URL: str = "{user_ids:str}/profile/"

# ======================================
# WRITE
# ======================================

USER_WRITE_CONTROLLER_URL_BASE = "write/"

USER_CREATE_URL: str = "create/"
USER_CHANGE_URL: str = "change/"
USER_DELETE_URL: str = "delete/"

# ======================================
# VERIFICATION
# ======================================

USER_VERIFICATION_CONTROLLER_BASE = "verification/"

USER_EMAIL_VERIFICATION_REQUEST_URL: str = "email/verification_request/"
USER_EMAIL_VERIFICATION_CONFIRM_URL: str = "email/verification_confirm/"
USER_PASSWORD_RESET_REQUEST_URL: str = "password/request/"
USER_PASSWORD_RESET_CONFIRM_URL: str = "password/confirm/"

# ======================================
# AUTHENTICATION
# ======================================

USER_AUTH_CONTROLLER_BASE = "auth/"

USER_LOGIN_URL: str = "login/"
