# ======================================
# BASE
# ======================================

USER_ROUTER_NAME_BASE: str = "user_"

# ======================================
# READ
# ======================================

USER_PROFILES_NAME: str = USER_ROUTER_NAME_BASE + "profiles"

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

USER_EMAIL_VERIFICATION_REQUEST_NAME: str = (
    USER_ROUTER_NAME_BASE + "email_verification_request"
)
USER_EMAIL_VERIFICATION_CONFIRM_NAME: str = (
    USER_ROUTER_NAME_BASE + "email_confirmation_confirm"
)
USER_PASSWORD_RESET_REQUEST_NAME: str = USER_ROUTER_NAME_BASE + "password_reset_request"
USER_PASSWORD_RESET_CONFIRM_NAME: str = USER_ROUTER_NAME_BASE + "password_reset_confirm"

# ======================================
# AUTHENTICATION
# ======================================

USER_LOGIN_NAME: str = USER_ROUTER_NAME_BASE + "login"
USER_LOGOUT_NAME: str = USER_ROUTER_NAME_BASE + "logout"
