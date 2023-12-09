# ======================================
# BASE
# ======================================

USER_ROUTER_NAME_BASE: str = "users:"

# ======================================
# READ
# ======================================

USER_LIST_NAME: str = USER_ROUTER_NAME_BASE + "list"
USER_DETAIL_NAME: str = USER_ROUTER_NAME_BASE + "detail"
USER_CHECK_USERNAME_NAME: str = USER_ROUTER_NAME_BASE + "check_username"
USER_CHECK_EMAIL_NAME: str = USER_ROUTER_NAME_BASE + "check_email/"
USER_CHECK_PASSWORD_NAME: str = USER_ROUTER_NAME_BASE + "check_password/"

# ======================================
# WRITE
# ======================================

USER_CREATE_NAME: str = USER_ROUTER_NAME_BASE + "create"
USER_CHANGE_USERNAME_NAME: str = USER_ROUTER_NAME_BASE + "change_username"
USER_CHANGE_PASSWORD_NAME: str = USER_ROUTER_NAME_BASE + "change_password"
USER_EMAIL_CHANGE_REQUEST_NAME: str = USER_ROUTER_NAME_BASE + "change_email_request/"
USER_DELETE_NAME: str = USER_ROUTER_NAME_BASE + "delete"

# ======================================
# VERIFICATION
# ======================================

USER_EMAIL_VERIFICATION_REQUEST_NAME: str = USER_ROUTER_NAME_BASE + "email_verification"
USER_EMAIL_VERIFICATION_CONFIRM_NAME: str = USER_ROUTER_NAME_BASE + "email_confirmation"
USER_PASSWORD_RESET_REQUEST_NAME: str = USER_ROUTER_NAME_BASE + "password_reset_request"
USER_PASSWORD_RESET_CONFIRM_NAME: str = USER_ROUTER_NAME_BASE + "password_reset_confirm"

# ======================================
# AUTHENTICATION
# ======================================

USER_LOGIN_NAME: str = USER_ROUTER_NAME_BASE + "login"
USER_LOGOUT_NAME: str = USER_ROUTER_NAME_BASE + "logout"
