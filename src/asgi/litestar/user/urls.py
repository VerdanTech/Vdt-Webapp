# ======================================
# BASE
# ======================================

USER_ROUTER_URL_BASE: str = "users/"

# ======================================
# READ
# ======================================

USER_READ_CONTROLLER_URL_BASE = "read/"

USER_LIST_URL: str = "list/"
USER_DETAIL_URL: str = "{user_id:str}/detail/"
USER_CHECK_USERNAME_URL: str = "{username:str}/check_username/"
USER_CHECK_EMAIL_URL: str = "{email:str}/check_email/"
USER_CHECK_PASSWORD_URL: str = "{password:str}/check_password/"

# ======================================
# WRITE
# ======================================

USER_WRITE_CONTROLLER_URL_BASE = "write/"

USER_CREATE_URL: str = "create/"
USER_CHANGE_USERNAME_URL: str = "change_username/"
USER_CHANGE_PASSWORD_URL: str = "change_password/"
USER_EMAIL_CHANGE_REQUEST_URL: str = "change_email_request/"
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
USER_LOGOUT_URL: str = "logout/"
