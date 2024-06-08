# ======================================
# BASE
# ======================================

USER_ROUTER_URL_BASE: str = "users/"


# ======================================
# COMMANDS
# ======================================

USER_COMMAND_CONTROLLER_BASE: str = "commands/"

USER_CREATE_URL: str = "create/"
USER_UPDATE_URL: str = "update/"
USER_DELETE_URL: str = "delete/"

USER_LOGIN_URL: str = "login/"

USER_EMAIL_VERIFICATION_REQUEST_URL: str = "email/verification_request/"
USER_EMAIL_VERIFICATION_CONFIRM_URL: str = "email/verification_confirm/"
USER_PASSWORD_RESET_REQUEST_URL: str = "password/request/"
USER_PASSWORD_RESET_CONFIRM_URL: str = "password/confirm/"


# ======================================
# VIEWS
# ======================================

USER_VIEW_CONTROLLER_BASE: str = "commands/"

USER_PROFILES_URL: str = "{user_ids:str}/profile/"
