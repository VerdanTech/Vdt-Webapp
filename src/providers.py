# ======================================
# PROVIDER KEY (PK) NAMES
# These key names automatically configure all provided dependencies
# in the provider key. The route handlers of the ASGI, as well as the
# provider functions which depend on other dependencies, which are what the
# dependencies are injected into, need to have arguments with
# names matching these keys to receive them.
# ======================================

# ========== Application Operations ========== #

# User
USER_READ_OPS_PK = "user_read_ops"
USER_WRITE_OPS_PK = "user_write_ops"
USER_VERIFICATION_OPS_PK = "user_verification_ops"
USER_AUTH_OPS_PK = "user_auth_ops"

# ========== Sanitizers ========== #

USER_SANITIZER_PK = "user_sanitizer"

# ========== Persistence ========== #

# Database
SQL_CLIENT_PK = "sql_client"
SQL_TRANSACTION_PK = "sql_transaction"

# Serializer
USER_SERIALIZER_PK = "user_serializer"

# Repositories
USER_STORE_REPO_PK = "user_store_repo"

# ========== Email ========== #

EMAIL_CLIENT_PK = "email_client"
EMAIL_EMITTER_PK = "email_emitter"

# ========== Security ========== #

# Crypt
PASSWORD_CRYPT_PK = "password_crypt"